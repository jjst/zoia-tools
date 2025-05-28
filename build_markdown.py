#!/usr/bin/env python3

import argparse
import logging
import re
from pathlib import Path
import pandas as pd
import tiktoken
from dataclasses import dataclass, field
from typing import List, Optional
import numpy as np
from collections import defaultdict

@dataclass
class ModuleOption:
    """
    Modules may have options that can be accessed to configure the module from the menu.
    """
    name: str
    description: str
    
@dataclass
class Parameter:
    """
    Modules have parameters, those each appear as a block on the ZOIA grid.
    Module options may affect how many parameters a module has.
    """
    block: str
    title: str
    knob: Optional[str]
    description: str
    options: Optional[str] = None

@dataclass
class Module:
    """
    A ZOIA module
    """
    name: str
    description: str
    category: str
    category_description: str
    max_blocks: int    
    avg_dsp: Optional[str] = None
    connections: Optional[str] = None
    options: List[ModuleOption] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)

@dataclass
class Category:
    """
    A category of modules
    """
    name: str
    description: str
    modules: List[Module]

def is_repeated_cat(s: str) -> bool:
    if pd.isna(s): 
        return False
    words = s.split()
    return len(words) > 1 and len(set(words)) == 1

def read_and_clean(html_path: Path) -> pd.DataFrame:
    # 1.a: pull the first table
    # This returns a list of DataFrames; using attrs filters on the table’s HTML attributes.
    dfs = pd.read_html(
        html_path,
        attrs={"class": "waffle"},     # only tables with class="waffle"
        flavor="lxml",                 # or "html5lib" if you prefer
        header=1,
        skiprows=0
    )
    df = dfs[0]  # first (and presumably only) matching table
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    df = df.drop(df.columns[:2], axis=1)
    df = df.dropna(axis=0, how="all").reset_index(drop=True)
    
    # 4. Identify the category‐rows (Module Name ending with ':')
    df["is_category"] = (
        df["Category"]
          .str.strip()
          .str.endswith(":")
          .fillna(False)        # ← turn any NaNs into False
    )
    
    df.loc[~df["is_category"], "Category"] = pd.NA
    df["Category"] = df["Category"].str.rstrip(":").str.strip()
    df.loc[df["is_category"], "Category Description"] = df.loc[df["is_category"], "Module Name"]
    df[["Category", "Category Description"]] = df[["Category", "Category Description"]].ffill()
    df = df.loc[~df["is_category"]].reset_index(drop=True)
    df.drop(columns="is_category", inplace=True)

    # Clean / flag module header
    block_nums = pd.to_numeric(df["Block #"], errors="coerce")
    max_blocks = pd.to_numeric(df["Max # of Blocks"], errors="coerce")

    # A header is where block == 1 and max_blocks is a valid number
    df["is_module_header"] = (block_nums == 1) & max_blocks.notna()
    df.loc[df["is_module_header"], "Module Name Clean"] = df.loc[df["is_module_header"], "Module Name"].str.strip()
    # grab the description from the Module Name one row down
    df.loc[df["is_module_header"], "Module Description"] = (
        df["Module Name"].shift(-1)
          .loc[df["is_module_header"]]
          .str.strip()
    )
    df["Module Name Clean"].ffill(inplace=True)
    df["Module Description"].ffill(inplace=True)

    # remove the old “Module Name” column…
    df.drop(columns=["Module Name"], inplace=True)
    
    # …and rename our cleaned‐up field back to “Module Name”
    df.rename(columns={"Module Name Clean": "Module Name"}, inplace=True)

    # Coerce non‐integer values to <NA> and convert to pandas’ nullable Int type
    df["Max # of Blocks"] = (
        pd.to_numeric(df["Max # of Blocks"], errors="coerce")   # turns non‐numeric into NaN
          .astype("Int64")                                      # make it a nullable integer column
    )
    df.drop(columns="is_module_header", inplace=True)
    return df



def slice_modules(df: pd.DataFrame) -> List[Module]:
    modules: List[Module] = []
    
    # iterate in the original order of first appearance
    seen = set()
    for name in df["Module Name"]:
        if name in seen:
            continue
        seen.add(name)
        
        group = df[df["Module Name"] == name]
        header = group.iloc[0]
        
        # 1. module metadata comes from that first row
        module = Module(
            name            = name,
            description     = header["Module Description"],
            max_blocks      = int(header["Max # of Blocks"]) if pd.notna(header["Max # of Blocks"]) else 0,
            avg_dsp         = header["Avg DSP"],
            connections     = header["Might typically connect to"],
            category        = header["Category"],
            category_description = header["Category Description"],
            options         = [],
            parameters      = []
        )
        
        # 2. now every row in this group (including the header row itself, if it has options)
        for _, prow in group.iterrows():
            # menu options
            opt = prow["Module Options"]
            if pd.notna(opt):
                module.options.append(
                    ModuleOption(
                        name=str(opt),
                        description=str(prow["Description"])
                    )
                )
            
            # grid parameters
            block_no = prow["Block #"]
            if pd.notna(block_no):
                module.parameters.append(
                    Parameter(
                        block       = prow["Block #"],
                        title       = prow["Title of block"],
                        knob        = prow["Value modified by knob"] if pd.notna(prow["Value modified by knob"]) else None,
                        description = prow["Description of button"],
                        options     = prow["Module Options"] if pd.notna(prow["Module Options"]) else None
                    )
                )
        
        modules.append(module)
    
    return modules

def build_categories(modules):
    cats: dict[str, Category] = {}
    groups = defaultdict(list)
    
    # 1. Group modules by their .category
    for m in modules:
        groups[m.category].append(m)
    
    # 2. Build one Category per unique name
    for name, mods in groups.items():
        desc = mods[0].category_description  # same for every module in that category
        cats[name] = Category(name=name, description=desc, modules=mods)
    
    # 3. Your final list:
    categories = list(cats.values())
    return categories

def slugify(text: str) -> str:
    # lower, strip non-word, spaces→hyphens
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text

def generate_toc(categories: List[Category]) -> List[str]:
    toc_lines: List[str] = []
    toc_lines.append("## Table of Contents\n")
    for cat in categories:
        cat_slug = slugify(cat.name)
        toc_lines.append(f"- [{cat.name}](#{cat_slug})")
        for mod in cat.modules:
            mod_slug = slugify(mod.name)
            toc_lines.append(f"  - [{mod.name}](#{mod_slug})")
        toc_lines.append("")  # blank line between categories
    return toc_lines

def render_markdown(categories: List[Category]) -> str:
    lines: List[str] = []
    # 1. Title
    lines.append("# ZOIA Module Index\n")
    # 2. TOC
    lines.extend(generate_toc(categories))
    # 3. Full content
    for cat in categories:
        lines.append(f"## {cat.name}")
        lines.append(f"{cat.description}\n")
        for mod in cat.modules:
            lines.append(f"### {mod.name}")
            lines.append(f"{mod.description}")
            lines.append(f"- **Max Blocks:** `{mod.max_blocks}`")
            if mod.avg_dsp:
                lines.append(f"- **Avg DSP:** `{mod.avg_dsp}`")
            if mod.connections:
                lines.append(f"- **Connections:** `{mod.connections}`")
            if mod.options:
                lines.append(f"- **Options:**")
                for opt in mod.options:
                    lines.append(f"  - **`{opt.name}`** – `{opt.description}`")
            if mod.parameters:
                lines.append(f"- **Parameters:**")
                for p in mod.parameters:
                    lines.append(f"  - **Block `{p.block}` – `{p.title}`**")
                    if p.knob:
                        lines.append(f"    - **Knob:** `{p.knob}`")
                    lines.append(f"    - **Description:** `{p.description}`")
                    if p.options:
                        lines.append(f"    - **Option:** `{p.options}`")
            lines.append("")  # blank line after each module
        lines.append("---\n")  # separator between categories

    return "\n".join(lines)

def write_output(md_text: str, out_path: Path) -> None:
    out_path.write_text(md_text, encoding="utf-8")
    logging.info(f"Wrote {out_path} ({len(md_text)} characters)")

# ─── 8. CLI Entrypoint ────────────────────────────────────────────────────────────
def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    p = argparse.ArgumentParser(description="Build ZOIA Module Index MD")
    p.add_argument("html_input", help="Path to exported HTML")
    p.add_argument("md_output", help="Path for generated Markdown")
    args = p.parse_args()

    html_path = Path(args.html_input)
    md_path   = Path(args.md_output)

    logging.info("Reading & cleaning HTML…")
    df = read_and_clean(html_path)


    logging.info("Slicing into modules…")
    modules = slice_modules(df)

    categories = build_categories(modules)

    logging.info("Rendering Markdown…")
    md_text = render_markdown(categories)

    logging.info("Writing Markdown file…")
    write_output(md_text, md_path)

if __name__ == "__main__":
    main()

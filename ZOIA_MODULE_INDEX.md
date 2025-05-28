# ZOIA Module Index

## Table of Contents

- [INTERFACE MODULES](#interface-modules)
  - [Audio Input](#audio-input)
  - [Audio Output](#audio-output)
  - [Midi Notes In](#midi-notes-in)
  - [Midi Pitch Bend](#midi-pitch-bend)
  - [Midi CC in](#midi-cc-in)
  - [Midi Pressure](#midi-pressure)
  - [Midi Clock In](#midi-clock-in)
  - [Midi CC out](#midi-cc-out)
  - [Midi PC out](#midi-pc-out)
  - [Midi Note Out](#midi-note-out)
  - [Midi Clock Out](#midi-clock-out)
  - [Stompswitch](#stompswitch)
  - [Pixel](#pixel)
  - [UI Button](#ui-button)
  - [Pushbutton](#pushbutton)
  - [Device Control](#device-control)
  - [Keyboard](#keyboard)
  - [Cport Exp/CV in](#cport-expcv-in)
  - [Cport CV out](#cport-cv-out)

- [Euroburo CV I/O](#euroburo-cv-io)
  - [CV In](#cv-in)
  - [CV Out](#cv-out)

- [AUDIO MODULES](#audio-modules)
  - [Oscillator](#oscillator)
  - [VCA](#vca)
  - [SV Filter](#sv-filter)
  - [Multi-Filter](#multi-filter)
  - [Delay Line](#delay-line)
  - [Audio Panner](#audio-panner)
  - [Pitch Shifter](#pitch-shifter)
  - [Audio Balance](#audio-balance)
  - [Audio Mixer](#audio-mixer)
  - [Inverter](#inverter)
  - [Audio In Switch](#audio-in-switch)
  - [Audio Out Switch](#audio-out-switch)
  - [All Pass Filter](#all-pass-filter)
  - [Noise](#noise)
  - [Audio Multiply](#audio-multiply)
  - [Bit Crusher](#bit-crusher)
  - [Aliaser](#aliaser)
  - [Buffer Delay](#buffer-delay)
  - [Looper](#looper)
  - [Granular](#granular)
  - [Stereo Spread](#stereo-spread)
  - [Bit Modulator](#bit-modulator)
  - [Diffuser](#diffuser)

- [CONTROL MODULES](#control-modules)
  - [LFO](#lfo)
  - [Sequencer](#sequencer)
  - [ADSR](#adsr)
  - [Sample and Hold](#sample-and-hold)
  - [CV Invert](#cv-invert)
  - [CV Rectify](#cv-rectify)
  - [Value](#value)
  - [Trigger](#trigger)
  - [CV Flip Flop](#cv-flip-flop)
  - [CV Delay](#cv-delay)
  - [CV Loop](#cv-loop)
  - [CV Filter](#cv-filter)
  - [Slew Limiter](#slew-limiter)
  - [Clock Divider](#clock-divider)
  - [Comparator](#comparator)
  - [In Switch](#in-switch)
  - [Out Switch](#out-switch)
  - [Quantizer](#quantizer)
  - [Steps](#steps)
  - [Multiplier](#multiplier)
  - [Rhythm](#rhythm)
  - [Tap to CV](#tap-to-cv)
  - [CV Mixer](#cv-mixer)

- [ANALYSIS MODULES](#analysis-modules)
  - [Onset Detector](#onset-detector)
  - [Env Follower](#env-follower)
  - [Pitch Detector](#pitch-detector)

- [EFFECT MODULES](#effect-modules)
  - [Tone Control](#tone-control)
  - [Delay w/Mod](#delay-wmod)
  - [Ping Pong Delay](#ping-pong-delay)
  - [OD & Distortion](#od-distortion)
  - [Fuzz](#fuzz)
  - [Compressor](#compressor)
  - [Gate](#gate)
  - [Plate Reverb](#plate-reverb)
  - [Hall Reverb](#hall-reverb)
  - [Room Reverb](#room-reverb)
  - [Ghostverb](#ghostverb)
  - [Reverb Lite](#reverb-lite)
  - [Phaser](#phaser)
  - [Chorus](#chorus)
  - [Vibrato](#vibrato)
  - [Flanger](#flanger)
  - [Tremolo](#tremolo)
  - [Env Filter](#env-filter)
  - [Ring Modulator](#ring-modulator)
  - [Cabinet Sim](#cabinet-sim)

## INTERFACE MODULES
Interface modules will connect to and from your other music gear in the physical world. Synth modules, MIDI devices, audio sources, your DAW, footswitches, expression pedals, etc are all connected into ZOIA's button grid here.

### Audio Input
Connect audio from the outside world into the grid. This could be a guitar, bass, synth module, computer audio, etc.
- **Max Blocks:** `2`
- **Avg DSP:** `0.4%`
- **Connections:** `outputs, audio effect inputs, envelope follower, pitch detector, VCAs, sidechain inputs,`
- **Options:**
  - **`channels`** – `select presence of left input, right input, or both`
  - **`input pad`** – `On the Euroburo, the input pad is set here (0, -6, -12dB)`
- **Parameters:**
  - **Block `1` – `pedal input L`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from left pedal input jack`
    - **Option:** `channels`
  - **Block `2` – `pedal input R`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from right pedal input jack`
    - **Option:** `input pad`

### Audio Output
Connect audio from your ZOIA into the outside world. Connect to your amplifier, a DI box, your audio interface, etc. An optional gain control lets you tweak the output level.
- **Max Blocks:** `3`
- **Avg DSP:** `1.7%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`gain control`** – `adds output gain control`
  - **`channels`** – `select presence of left output, right output, or both`
- **Parameters:**
  - **Block `1` – `pedal output L`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to left pedal output jack`
    - **Option:** `gain control`
  - **Block `2` – `pedal output R`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to right pedal output jack`
    - **Option:** `channels`
  - **Block `3*` – `gain`**
    - **Knob:** `output gain`
    - **Description:** `selects output gain of pedal from +20dB to -100dB`

### Midi Notes In
Connect your MIDI keyboard controller to the ZOIA. Connect the note out to an oscillator to have it play your note, and connect the gate out to an ADSR (connected to a VCA) for a natural envelope.
- **Max Blocks:** `32`
- **Avg DSP:** `0.3%`
- **Connections:** `oscillators, MIDI inputs/outputs, CV inputs/outputs,`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will read from`
  - **`# of outputs`** – `adds additional note and gate out outputs, and velocity and trigger outputs if selected, for connecting simultaneously played midi notes. Select 1 note to build a monophonic synth, or add up to 8 notes per MIDI channel.`
  - **`priority`** – `toggles behaviour of simultaneously played MIDI notes, when number of played notes exceeds number of MIDI note outputs present. Prioritize the newest, oldest, highest, lowest played note, or "round robin" input.`
  - **`greedy`** – `outputs are greedy for midi note inputs (all outputs will want to play)`
  - **`velocity output`** – `toggles presence of velocity out block`
  - **`low note`** – `determines lowest played note to receive`
  - **`high note`** – `determines highest played note to receive`
  - **`trigger pulse`** – `toggles presence of trigger out block`
- **Parameters:**
  - **Block `1` – `note out`**
    - **Knob:** `no modifier`
    - **Description:** `detects played note as value from -1 to 1, where -1 is C-2, 0 is A0, and 1 is A10`
    - **Option:** `midi channel`
  - **Block `2` – `gate out`**
    - **Knob:** `no modifier`
    - **Description:** `detects played note on/off status`
    - **Option:** `# of outputs`
  - **Block `3*` – `velocity out`**
    - **Knob:** `no modifier`
    - **Description:** `detects velocity of played note`
    - **Option:** `priority`
  - **Block `4*` – `trigger out`**
    - **Knob:** `no modifier`
    - **Description:** `detects presence of played note as a single momentary pulse`
    - **Option:** `greedy`

### Midi Pitch Bend
Collects MIDI data from pitch bend wheel on keyboards, can be applied to oscillator frequency in parallel with MIDI note data, or used in other ways.
- **Max Blocks:** `1`
- **Avg DSP:** `0.1%`
- **Connections:** `oscilllators, audio effects parameters, LFOs, VCAs, output gain, sequencers,`
- **Options:**
  - **`channel`** – `select MIDI channel to look for pitch bend signal on`
- **Parameters:**
  - **Block `1` – `pitch bend`**
    - **Knob:** `no modifier`
    - **Description:** `delivers incoming pitch bend data as a cv output that you can connect to other things`
    - **Option:** `channel`

### Midi CC in
Connect encoder knobs and sliders on a MIDI interface. Take note of the outgoing CC number of each control and enter it into the controller option.
- **Max Blocks:** `1`
- **Avg DSP:** `0.1%`
- **Connections:** `audio effects parameters, LFOs, VCAs, output gain,`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will read from`
  - **`controller`** – `determines which controller # the module will read from`
  - **`output range`** – `determines range of CV output from from 0 thru 1 or -1 thru 1`
- **Parameters:**
  - **Block `1` – `cc value`**
    - **Knob:** `no modifier`
    - **Description:** `detects control change value from 0 - 127`
    - **Option:** `midi channel`

### Midi Pressure
Many MIDI keyboards have an aftertouch feature that can be triggered by pressing down on a note after it's fully depressed. You can use after touch to trigger a little extra pizazz in your sound.
- **Max Blocks:** `1`
- **Avg DSP:** `0.03%`
- **Connections:** `oscillators, audio effects parameters, LFOs, VCAs, output gain, sequencers,`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will read from`
- **Parameters:**
  - **Block `1` – `channel pressure`**
    - **Knob:** `no modifier`
    - **Description:** `detects pressure of key after note is played. Pressure is additive when multiple keys have pressure applied`
    - **Option:** `midi channel`

### Midi Clock In
Connect incoming MIDI clock to sync your patches to the outside world. Connects directly to ZOIA's MIDI input.
- **Max Blocks:** `4`
- **Avg DSP:** `0.1%`
- **Connections:** `tap tempo inputs, sequencers, VCAs, ADSRs, oscillators, MIDI inputs/outputs, CV inputs/outputs,`
- **Options:**
  - **`clock out`** – `toggles the presence of clock out button`
  - **`reset out`** – `toggles the presence of reset out button`
  - **`run out`** – `toggles the presence of run out button`
  - **`beat modifier`** – `multiplies output at "quarter out" by selected value. choose from 1, 2, 3, 4, 6, 12, 1/2, 1/3, 1/4, 1/6 or 1/12`
- **Parameters:**
  - **Block `1` – `quarter out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs a square wave LFO whose period is the detected BPM`
    - **Option:** `clock out`
  - **Block `2*` – `clock out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs a log sawtooth wave LFO whose period is the amount of time between clock signals`
    - **Option:** `reset out`
  - **Block `3*` – `reset out`**
    - **Knob:** `no modifier`
    - **Description:** `sends a pulse of cv when "song position ptr" message is detected with a value of 0`
    - **Option:** `run out`
  - **Block `4*` – `running output`**
    - **Knob:** `no modifier`
    - **Description:** `if incoming clock signal is detected, output will be 1. if not, output is 0. you can use this in conjuction with a cv switch to allow MIDI clock to override other tap sources, but only when detected.`
    - **Option:** `beat modifier`

### Midi CC out
Send Control Change messages to external MIDI enabled gear through ZOIA's MIDI outputs.
- **Max Blocks:** `1`
- **Avg DSP:** `0.2%`
- **Connections:** `oscillator frequency, midi pressure,`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will send to`
  - **`controller`** – `determines which controller # the module will send control change message to`
- **Parameters:**
  - **Block `1` – `cc out`**
    - **Knob:** `cc out value`
    - **Description:** `sends control change value from 0 - 127`
    - **Option:** `midi channel`

### Midi PC out
Send Program Change messages to external MIDI enabled gear. Select the Program Change value and send a CV signal to trigger in to send message through ZOIA's MIDI outputs.
- **Max Blocks:** `2`
- **Avg DSP:** `0.1%`
- **Connections:** `sends program change messages to external devices?`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will send to`
- **Parameters:**
  - **Block `1` – `pc out`**
    - **Knob:** `pc out value`
    - **Description:** `sends program change value from 0-127`
    - **Option:** `midi channel`
  - **Block `2` – `trigger in`**
    - **Knob:** `minimum trigger state from 0-1`
    - **Description:** `triggers`

### Midi Note Out
Send MIDI notes out to external MIDI enabled gear through ZOIA's MIDI outputs.
- **Max Blocks:** `3`
- **Avg DSP:** `0.1%`
- **Connections:** `keyboard module, LFOs, MIDI inputs/outputs,, CV inputs/outputs, expression pedal,`
- **Options:**
  - **`midi channel`** – `determines which MIDI channel the module will send to`
  - **`velocity output`** – `toggles the presence of a velocity data block for played note`
- **Parameters:**
  - **Block `1` – `note in`**
    - **Knob:** `minimum note from 0-1`
    - **Description:** `sends played note value through selected MIDI channel`
    - **Option:** `midi channel`
  - **Block `2` – `gate in`**
    - **Knob:** `minimum gate in 0-1`
    - **Description:** `sends played note on/off status through selected MIDI channel`
    - **Option:** `velocity output`
  - **Block `3*` – `velocity out`**
    - **Knob:** `minimum note velocity out from 0-1`
    - **Description:** `sends played note velocity data through selected MIDI channel`

### Midi Clock Out
Generate MIDI clock to sync outside devices to your ZOIA. Clock sends directly to ZOIA's MIDI output.
- **Max Blocks:** `5`
- **Avg DSP:** `0.4%`
- **Connections:** `LFOS, sequencers, CV inputs/outputs, pushbuttons/stompswitches`
- **Options:**
  - **`input`** – `select if you'd like your MIDI clock rate determined by the knob/other cv source, or by an LFO or tap source`
  - **`run in`** – `toggles presence of "sent" control`
  - **`reset in`** – `toggles presence of "reset" control`
  - **`position`** – `toggles presence of send position and song position controls`
- **Parameters:**
  - **Block `1` – `cv/tap control`**
    - **Knob:** `cv: frequency of clock in Hz, s, or bpm. tap: none`
    - **Description:** `determines frequency of MIDI clock either by adjusting knob, or connecting a tap, LFO, or other cv source`
    - **Option:** `input`
  - **Block `2*` – `sent`**
    - **Knob:** `cv`
    - **Description:** `an upward change in cv sends "continue" message, a downward change in cv sends a "stop" message. MIDI clock continues to run.`
    - **Option:** `run in`
  - **Block `3*` – `reset`**
    - **Knob:** `cv`
    - **Description:** `un upward change in cv sends "stop", "song position prt 00 00", and "start" messages on 3 consecutive clock pulses. a downward change in cv arms this button for the next reset`
    - **Option:** `reset in`
  - **Block `4*` – `send position`**
    - **Knob:** `cv`
    - **Description:** `un upward change in cv sends "stop" and "song position prt" messages on consecutive clock pulses, sending the position determined by song position button. a downward change in cv arms this button for the next reset`
    - **Option:** `position`
  - **Block `5*` – `song position`**
    - **Knob:** `cv`
    - **Description:** `displays desired song position to trigger as follows - measure : quarter note: sixteenth note`

### Stompswitch
Use this module to connect a stomp switch to other modules. This can be any of ZOIA's 3 stomp switches or an external one. If using an external, remember to set it up in the Config Menu. Once placed, the Scroll and Bypass stomp switches must be "switched to" by holding them both on together for 2 seconds, this will allow them to function in the modules instead of as ZOIA's main user interface. Hold again for 2 seconds to switch back.
- **Max Blocks:** `1`
- **Avg DSP:** `0.1%`
- **Connections:** `tap tempos, MIDI inputs/outputs, oscillator frequency, audio effects, gain stages, sequencer,`
- **Options:**
  - **`stompswitch`** – `select which footswitch to interface. Choose any of the 3 on the ZOIA or an external footswitch (be sure to enter in the Config Menu)`
  - **`action`** – `select the desired behaviour of the switch. If you'd like it to stay engaged, choose latching. If you'd like it to only be engaged while pressed, choose momentary`
  - **`normally`** – `select the desired default switch state. Zero: "Off", One: "On"`
- **Parameters:**
  - **Block `1` – `cv output`**
    - **Knob:** `no modifier`
    - **Description:** `toggles state of stompswitch as determined by edit options`
    - **Option:** `stompswitch`

### Pixel
Puts a coloured block on the grid. The brightness can be controlled by a cv signal or an audio signal. Pixel is a simple, elegant way to create a more visually interactive user interface for your patch.
- **Max Blocks:** `1`
- **Avg DSP:** `0.01%`
- **Connections:** `cv outputs, audio outputs`
- **Options:**
  - **`control`** – `select either cv or audio`
- **Parameters:**
  - **Block `1` – `cv in/audio in`**
    - **Knob:** `cv bias point`
    - **Description:** `control the brightness of the led by sending either cv or audio in, depending on how it is configured in the Options menu`
    - **Option:** `control`

### UI Button
UI Button can function in a couple different ways. It can show you a specific colour at a specific brightness based on the setting of or CV sent to the input. It can also act as a pushbutton with output enabled. To use as a visualizing pixel, connect CV and send the following values: EXTENDED RANGE: Red: 0 - 0.049 (max bright 0.0375), Orange: 0.05 - 0.099 (max bright 0.0875), Mango: 0.10 - 0.149 (max bright 0.1375), Yellow: 0.15 - 0.199 (max bright 0.1875), Lime: 0.20 - 0.249 (max bright 0.2375), Green: 0.25 - 0.299 (max bright 0.2875), Surf: 0.30 - 0.349 (max bright 0.3375), Aqua: 0.35 - 0.399 (max bright 0.3875), Sky: 0.40 - 0.449 (max bright 0.4375), Blue: 0.45 - 0.499 (max bright 0.4875), Purple: 0.50 - 0.549 (max bright 0.5375), Magenta: 0.55 - 0.599 (max bright 0.5875), Pink: 0.60 - 0.649 (max bright 0.6375), Peach: 0.65 - 0.699 (max bright 0.6875) , White: 0.70 - 0.749 (max bright 0.7375). BASIC RANGE: Blue = 0 to 0.099 (0.74 max brightness), Green = 0.1 to 0.199 (0.174 max brightness), Red = 0.2 to 0.299 (0.274 max brightness), Yellow = 0.3 to 0.399 (0.374 max brightness), Cyan = 0.4 to 0.499 (0.474 max brightness), Magenta = 0.5 to 0.599 (0.574 max brightness), White = 0.6 to 0.699 (0.6 to 0.674 brightness).
- **Max Blocks:** `2`
- **Avg DSP:** `0.04%`
- **Connections:** `your finger, LFOs, sequencers, CV inputs/outputs, envelopes, expression pedals, footswitches,`
- **Parameters:**
  - **Block `1` – `in`**
    - **Knob:** `CV input`
    - **Description:** `displays colour/brightness selected by user or by CV input. use this button with optional CV output to send CV by pushing it.`
  - **Block `2*` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs CV of 1 when in button is pushed`

### Pushbutton
Turns a grid button into a button you can push to send a CV signal. Tap in a tempo, open up a VCA, trigger a sequencer, or anything else. The grid is your oyster!
- **Max Blocks:** `1`
- **Avg DSP:** `0.02%`
- **Connections:** `your finger, tap tempos, MIDI inputs/outputs, oscillator frequency, audio effects, gain stages, sequencer,`
- **Options:**
  - **`action`** – `select the desired behaviour of the switch. If you'd like it to stay engaged, choose latching. If you'd like it to only be engaged while pressed, choose momentary`
  - **`normally`** – `select the desired default switch state between zero and one. remember that your connection strength can help you achieve values in between.`
- **Parameters:**
  - **Block `1` – `switch`**
    - **Knob:** `no modifier`
    - **Description:** `push button to engage switch`
    - **Option:** `action`

### Device Control
Control the bypass state, performance mode, or stomp aux mode using CV. A rising or falling CV value will toggle the selected control.
- **Max Blocks:** `1`
- **Avg DSP:** `nan`
- **Connections:** `LFOs, footswitches/pushbuttons, MIDI inputs/outputs, CV inputs/outputs, other sequencers`
- **Options:**
  - **`control`** – `select between controlling the following actions: audio bypass, performance mode, or stomp aux`
- **Parameters:**
  - **Block `1` – `value`**
    - **Knob:** `CV slider from 0 to 1`
    - **Description:** `activates selected action when it sees a value of 1, deactivates action upon seeing a 0`
    - **Option:** `control`

### Keyboard
Turns grid buttons into a keyboard you can connect to an oscillator and play. No external MIDI controller necessary! Tune each keyboard button using the knob to have it play your desired note.
- **Max Blocks:** `26`
- **Avg DSP:** `0.1%`
- **Connections:** `your finger!`
- **Options:**
  - **`# of notes`** – `select how many notes you'd like your new keyboard to be. New buttons are added for each new note, all of which com out of the note out and gate out buttons.`
- **Parameters:**
  - **Block `1` – `note (#)`**
    - **Knob:** `selects desired note to play when button pushed. Click knob to toggle between frequency in Hz and music note`
    - **Description:** `plays note when pushed, like a keyboard`
    - **Option:** `# of notes`
  - **Block `2` – `note out`**
    - **Knob:** `no modifier`
    - **Description:** `CV output of note or frequency played`
  - **Block `3` – `gate out`**
    - **Knob:** `no modifier`
    - **Description:** `CV output of played note on/off status`
  - **Block `4` – `trigger out`**
    - **Knob:** `no modifier`
    - **Description:** `Sends a single momentary pulse`

### Cport Exp/CV in
Connect your expression pedal or a control voltage signal from an external source. Remember to set CPort to either exp or cv in the Config Menu.
- **Max Blocks:** `1`
- **Avg DSP:** `0.1%`
- **Connections:** `audio effects, oscillator frequency, VCAs, LFOs, MIDI inputs/outputs, CV inputs/outputs`
- **Options:**
  - **`output range`** – `determines range of CV output from from 0 to 1 or -1 to 1`
- **Parameters:**
  - **Block `1` – `no modifier`**
    - **Knob:** `cv output`
    - **Description:** `expresses value of either expression pedal or control voltage sensed by Control Port as a numerical value.`
    - **Option:** `output range`

### Cport CV out
This module interprets internal CV and sends it down the ring of a 1/4" TRS connector in the control port as a standard CV signal of 0-5 volts. Remember to set CPort to cv in the Config Menu.
- **Max Blocks:** `1`
- **Avg DSP:** `0.2%`
- **Connections:** `CV inputs/outputs, MIDI inputs/outputs, LFOs, sequencers, ADSRs,`
- **Options:**
  - **`input range`** – `select if you'd like your input to be interpreted as a value from 0 to 1 or as a value from -1 to 1. This will then be sent as a control voltage from 0-5 volts`
- **Parameters:**
  - **Block `1` – `no modifier`**
    - **Knob:** `cv input`
    - **Description:** `interprets value from a module and sends it out the Control Port on the ring of the connector as a control voltage signal from 0-5 volts`
    - **Option:** `input range`

---

## Euroburo CV I/O
These modules are used to connect control voltages between the grid and the outside world.

### CV In
Connect CV from the outside world to the grid.
- **Max Blocks:** `1`
- **Avg DSP:** `0.1%`
- **Connections:** `clocks, triggers, gates, VCAs, pitch, quantizers, ADSRs, sequencers, sample & hold, filter cutoff`
- **Options:**
  - **`out range`** – `sets what range of voltages you want to control other modules. 0-10V is typical for euro pitch control, 0-5V is very common for other CV.`
  - **`inpt range`** – `chooses if the range of what you're sending in goes from 0-1 or from -1 to 1.`
  - **`clk filter`** – `acts as a schmitt trigger to output a clean clock signal (which Zoia requires) from the cv input. The numbers represent the low and high threshold values. ie 2,8 would cause the module to output 0 when the input goes below 0.2 of the input voltage range, and output a high signal when the signal goes above 0.8 of the input voltage range. This helps to avoid modules in Zoia from mis-triggering.`
  - **`transpose 0V`** – `the euroburo maps 0V at it's input to an A note by default. Other synths use C as 0V. Selecting the C option will transpose (add 0.25) to the output of this module so it maps to C on the euroburo oscillator.`
- **Parameters:**
  - **Block `1` – `CV In`**
    - **Knob:** `connect to any module block that accepts control signals`
    - **Description:** `connect external CV signals plugged into a CV IN jack on the euroburo to the control signal input block of modules on the grid`
    - **Option:** `out range`
  - **Block `1` – `CV In`**
    - **Knob:** `connect to any module block that accepts control signals`
    - **Description:** `connect external CV signals plugged into a CV IN jack on the euroburo to the control signal input block of modules on the grid`
    - **Option:** `inpt range`
  - **Block `1` – `CV In`**
    - **Knob:** `connect to any module block that accepts control signals`
    - **Description:** `connect external CV signals plugged into a CV IN jack on the euroburo to the control signal input block of modules on the grid`
    - **Option:** `clk filter`
  - **Block `1` – `CV In`**
    - **Knob:** `connect to any module block that accepts control signals`
    - **Description:** `connect external CV signals plugged into a CV IN jack on the euroburo to the control signal input block of modules on the grid`
    - **Option:** `transpose 0V`

### CV Out
Connect CV from the grid to the outside world.
- **Max Blocks:** `1`
- **Avg DSP:** `0.2%`
- **Connections:** `clocks, triggers, gates, VCAs, pitch, oscillators, ADSRs, sequencers, sample & hold, filter cutoff`
- **Options:**
  - **`out range`** – `sets what range of voltages you want to control other modules. 0-10V is typical for euro pitch control, 0-5V is very common for other CV.`
  - **`in range`** – `chooses if the range of what you're sending in goes from 0-1 or from -1 to 1.`
  - **`transpose 0V`** – `the euroburo maps 0V (and other whole note values) to an A note by default. Some other synths/modules use C as 0V. Selecting the C option will transpose up three semitones (subtract 0.25V) from the output of this module so C in the euroburo plays a C on external synths.`
- **Parameters:**
  - **Block `1` – `CV Out`**
    - **Knob:** `connect to any module block that outputs control signals`
    - **Description:** `connect control signal output block of modules on the grid to a CV OUT jack to be patched to external gear that uses CV`
    - **Option:** `out range`
  - **Block `1` – `CV Out`**
    - **Knob:** `connect to any module block that outputs control signals`
    - **Description:** `connect control signal output block of modules on the grid to a CV OUT jack to be patched to external gear that uses CV`
    - **Option:** `in range`
  - **Block `1` – `CV Out`**
    - **Knob:** `connect to any module block that outputs control signals`
    - **Description:** `connect control signal output block of modules on the grid to a CV OUT jack to be patched to external gear that uses CV`
    - **Option:** `transpose 0V`

---

## AUDIO MODULES
These modules generate or augment audio signals. These are the audio tools generally associated with synthesis but are generally applicable to guitar/bass as well.

### Oscillator
Generates an audio signal in the waveform of your choice. Connect a MIDI device, keyboard module, sequencer, pitch detector, LFO, or any CV source to select the frequency or note the oscillator will play. You can modulate the frequency or pulse width with the optional parameters. Negative CV inputs (from -1 to 0) will generate sub-bass frequencies between 0.027Hz and 27.49Hz. Be careful!
- **Max Blocks:** `4`
- **Avg DSP:** `10%`
- **Connections:** `MIDI inputs, CV inputs, keyboard module output, pitch detector, stompswitches/push buttons, expression pedal,`
- **Options:**
  - **`waveform`** – `select pattern of generated waveform from square, triangle, sawtooth, or sine wave`
  - **`fm in`** – `toggles presence of FM input parameter. this allows you to modulate an incoming audio signal against the oscillator, which acts as a carrier wave.`
  - **`duty cycle`** – `toggle presence of duty cycle parameter. this creates a distorted effect by varying the pulse width`
  - **`upsampling`** – `allows waveform to be generated at 2X sampling rate for better quality (higher CPU)`
- **Parameters:**
  - **Block `1` – `frequency`**
    - **Knob:** `frequency in Hz`
    - **Description:** `determines frequency of synthesized tone. The higher the frequency, the higher the note. Click the knob to toggle between frequency in Hz and music notes. Values -1 thru 0 represent sub-bass frequencies from 0.027 Hz to 27.49 Hz . Values from 0 thru 1 represent (mostly) audible frequencies from 27.5 Hz to 23999 Hz`
    - **Option:** `waveform`
  - **Block `2*` – `FM input`**
    - **Knob:** `no modifier`
    - **Description:** `allows you to connect another oscillator or audio source to modulate the oscillator's frequency.`
    - **Option:** `fm in`
  - **Block `3*` – `duty cycle`**
    - **Knob:** `value in %`
    - **Description:** `adjusts the pulse width of the oscillator`
    - **Option:** `duty cycle`
  - **Block `4` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `output of audio signal generated by oscillator`
    - **Option:** `upsampling`

### VCA
The Voltage Controlled Amplifier module will interpret incoming CV at the level control and boost or cut the volume. Connect an ADSR to create a natural sounding envelope for an oscillator passing through. Connect an LFO to create a tremolo effect. Or connect an expression pedal module or MIDI input for an external volume control.
- **Max Blocks:** `5`
- **Avg DSP:** `0.7%`
- **Connections:** `oscillators, audio inputs/outputs, audio effects,`
- **Options:**
  - **`channels`** – `select if you'd like your voltage controlled amplifier to apply gain to 1 channel or 2 channels`
- **Parameters:**
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects output of another audio source to gain stage`
    - **Option:** `channels`
  - **Block `2*` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects output of another audio source to gain stage`
  - **Block `3` – `level control`**
    - **Knob:** `gain in dB`
    - **Description:** `controls the gain of the output signal`
  - **Block `4` – `audio out 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects amplified signal from audio in 1 to an audio destination`
  - **Block `5*` – `audio out 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects amplified signal from audio in 2 to an audio destination`

### SV Filter
The State Variable Filter will resonate and cutoff around a set frequency.
- **Max Blocks:** `6`
- **Avg DSP:** `3%`
- **Connections:** `audio inputs/outputs, VCAs, oscillators,`
- **Options:**
  - **`low pass output`** – `toggles presence of low pass output. This is on by default`
  - **`hipass output`** – `toggles presence of hipass output`
  - **`bandpass output`** – `toggles presence of bandpass output`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio source into state variable filter`
    - **Option:** `low pass output`
  - **Block `2` – `frequency`**
    - **Knob:** `frequency in Hz`
    - **Description:** `determines cutoff frequency of filter. CV inputs from -1 to 0 cover the frequency range 0.03-27.5 Hz, CV inputs from 0 to 1 cover the frequency range 27.5-23999Hz`
    - **Option:** `hipass output`
  - **Block `3` – `resonance`**
    - **Knob:** `resonance value`
    - **Description:** `determines strength of resonant peak at cutoff frequency`
    - **Option:** `bandpass output`
  - **Block `4` – `lowpass output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio filtered below cutoff frequency`
  - **Block `5*` – `hipass output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio filtered above cutoff frequency`
  - **Block `6*` – `bandpass output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs band of audio within upper and lower limits of frequency cutoff`

### Multi-Filter
A general purpose filter with gain, frequency, and Q controls. Configurable as a high pass, low pass, band pass, bell, hi shelf, or low shelf.
- **Max Blocks:** `5`
- **Avg DSP:** `0.8%`
- **Connections:** `audio inputs/outputs, VCAs, oscillators,`
- **Options:**
  - **`filter shape`** – `select output characteristic of filter between high pass, low pass, , band pass, bell, hi shelf, and low shelf`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio source into filter`
    - **Option:** `filter shape`
  - **Block `2*` – `gain`**
    - **Knob:** `gain in dB`
    - **Description:** `determines gain of filter notch for hi shelf, low shelf, and bell filters`
  - **Block `3` – `frequency`**
    - **Knob:** `frequency in Hz`
    - **Description:** `determines center frequency of filter notch`
  - **Block `4` – `q`**
    - **Knob:** `width from 1-100`
    - **Description:** `determines width of filter notch`
  - **Block `5` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs filtered audio`

### Delay Line
The Delay Line is a simple module that takes audio at the input and delays it by a set amount of time. There is no dry signal, there are no repeats. You can create repeats by connecting the output back to the input, using the connection strength to adjust number of repeats.
- **Max Blocks:** `4`
- **Avg DSP:** `3%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`max time`** – `select maximum delay time from 100ms to 16s`
  - **`tap tempo in`** – `enable tap tempo mode of delay line module`
  - **`interpolation`** – `when set to on, this emulates the blips and sweeps caused by playing back sampled audio at different rates when changing delay times`
  - **`CV Input`** – `when tap tempo in is set to "no", this sets the relationship of incoming CV to delay time, exponential or linear`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio into delay line`
    - **Option:** `max time`
  - **Block `2` – `delay time`**
    - **Knob:** `time in ms`
    - **Description:** `delays audio playback by set time`
    - **Option:** `tap tempo in`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs delayed audio`
    - **Option:** `interpolation`
  - **Block `above: tap tempo off. below: tap tempo on` – `above: tap tempo off. below: tap tempo on`**
    - **Knob:** `above: tap tempo off. below: tap tempo on`
    - **Description:** `above: tap tempo off. below: tap tempo on`
    - **Option:** `CV Input`
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio into delay line`
  - **Block `2` – `modulation in`**
    - **Knob:** `time in ms`
    - **Description:** `connect CV modifier to adjust delay time in real time, complete with pitch shifting`
  - **Block `3` – `tap tempo in`**
    - **Knob:** `time in ms`
    - **Description:** `Connect CV for tap input. Try a clock divider connected to a stompswitch module to give your tapped tempo a ratio.`
  - **Block `4` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs delayed audio`

### Audio Panner
Audio Panner takes either one or two input channels and pans them between two outputs. Connect an LFO for a stereo tremolo effect.
- **Max Blocks:** `5`
- **Avg DSP:** `1%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like to have one audio source panning between two outputs, or two audio sources panning between two outputs`
  - **`pan type`** – `select the behaviour of the pan type between equal power, linear, and -4.5dB. Linear is the most basic, and will output a source at unity gain when it is hard panned, making the center position somewhat quieter than the source. Equal power uses a logarithmic taper to output unity gain across the sweep, resulting in a 3dB increase in the center position from Linear. -4.5dB is a mathematical compromise between the two.`
- **Parameters:**
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from source into panner`
    - **Option:** `channels`
  - **Block `2*` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from source into panner`
    - **Option:** `pan type`
  - **Block `3` – `pan`**
    - **Knob:** `pan value from 0-100`
    - **Description:** `sends audio from one or two input tracks to output tracks depending on pan value. A value of 0 will pan hard to track 1 and a value of 100 will pan hard to track 2. A value of 50 is equal volume on both outputs`
  - **Block `4` – `audio out 1`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio panned from track 1`
  - **Block `5` – `audio out 2`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio panned from track 1 when 1 track mode selected, or audio panned from track 2 when stereo mode selected`

### Pitch Shifter
Pitch Shifter transposes the pitch of incoming audio. Click the knob on the pitch shift parameter to cycle views of CV value, semitones, or cents. Connect an LFO to produce a vibrato effect, or connect whatever you'd like!
- **Max Blocks:** `3`
- **Avg DSP:** `15.5%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from source into pitch shifter`
  - **Block `2` – `pitch shift`**
    - **Knob:** `pitch shift factor`
    - **Description:** `shifts the pitch of the audio from input sources. Click the knob to toggle between CV factor, semitones, or notes`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs pitch shifted audio`

### Audio Balance
Audio Balance mixes an output from 2 inputs. You can run this module either mono or stereo.
- **Max Blocks:** `7`
- **Avg DSP:** `1.7%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`stereo`** – `select if you'd like mono or stereo channels. New inputs and outputs will be added for the left and right sides.`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio source to be balanced`
    - **Option:** `stereo`
  - **Block `2` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio source to be balanced`
  - **Block `3` – `mix`**
    - **Knob:** `mix in CV`
    - **Description:** `sets the mix. 0 is all audio in1, 50 is equal parts both inputs, 100 is all audio2`
  - **Block `4` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `balanced audio output`
  - **Block `1` – `audio in1 L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio source to be balanced (left)`
  - **Block `2` – `audio in1 R`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio source to be balanced (right)`
  - **Block `3` – `audio in2 L`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio source to be balanced (left)`
  - **Block `4` – `audio in2 R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio source to be balanced (right)`
  - **Block `5` – `mix`**
    - **Knob:** `mix in CV`
    - **Description:** `sets the mix. 0 is all audio in1, 50 is equal parts both inputs, 100 is all audio2`
  - **Block `6` – `audio outL`**
    - **Knob:** `no modifier`
    - **Description:** `balanced audio output (left)`
  - **Block `7` – `audio outR`**
    - **Knob:** `no modifier`
    - **Description:** `balanced audio output (right)`

### Audio Mixer
Audio Mixer functions like a stripped down mixing console, where gain is your channel fader and you can place an optional pan control. Mix up to 8 channels, in mono or stereo.
- **Max Blocks:** `34`
- **Avg DSP:** `3% - 20%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`num channels`** – `select how many channels you wish to mix, 2 through 8. New inputs will be added for each channel`
  - **`stereo`** – `select if you'd like a mono or stereo mixer. New inputs and outputs will be added for the left and right sides.`
  - **`panning`** – `toggles the presence of a pan control. Note that in mono mode, the pan control doesn't do anything`
- **Parameters:**
  - **Block `1` – `inL 1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio source to be mixed (left)`
    - **Option:** `num channels`
  - **Block `2*` – `inR 1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio source to be mixed (right)`
    - **Option:** `stereo`
  - **Block `3` – `inL 2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio source to be mixed (left)`
    - **Option:** `panning`
  - **Block `4*` – `inR 2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio source to be mixed (right)`
  - **Block `5` – `gain 1`**
    - **Knob:** `gain in dB`
    - **Description:** `adjust gain of input 1`
  - **Block `6` – `gain 2`**
    - **Knob:** `gain in dB`
    - **Description:** `adjust gain of input 2`
  - **Block `7*` – `pan 1`**
    - **Knob:** `pan value L-R 0-100`
    - **Description:** `adjust pan of input 1`
  - **Block `8*` – `pan 2`**
    - **Knob:** `pan value L-R 0-100`
    - **Description:** `adjust pan of input 2`
  - **Block `9` – `out L`**
    - **Knob:** `no modifier`
    - **Description:** `mixed audio output (left)`
  - **Block `10*` – `out R`**
    - **Knob:** `no modifier`
    - **Description:** `mixed audio output (right)`

### Inverter
The Inverter module takes incoming audio signal and inverts the sound wave 180 degrees out of phase. This module is inaudible unless you have a phase related problem you are trying to solve, in which case it can be very audible. Be sure to put a 1 Buffer Delay module into your "dry" side to line up the Inverter in time for proper phase cancellation.
- **Max Blocks:** `2`
- **Avg DSP:** `0.3%`
- **Connections:** `nan`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `audio input to be inverted`
  - **Block `2` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `inverted audio output`

### Audio In Switch
Audio In Switch takes a selected quantity of audio inputs and allows you to switch between them to a single output. You can use this to select between instruments at your input jacks, use it in conjunction with the Audio Out Switch to select between effects chains, or use it anywhere you'd like to be able to select between incoming audio sources using CV.
- **Max Blocks:** `18`
- **Avg DSP:** `0.8%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`# of inputs`** – `selects how many audio sources you'd like to switch between from 1-16. input jacks will be added for each source and the input select range from 0-1 will divide equally between them`
- **Parameters:**
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to switch`
    - **Option:** `# of inputs`
  - **Block `2*` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to switch`
  - **Block `3` – `in select`**
    - **Knob:** `select value 0-1`
    - **Description:** `divides value from 0-1 between number of present switch inputs and selects audio source corresponding to value present`
  - **Block `4` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio selected audio source`

### Audio Out Switch
Audio Out Switch takes an audio input and routes it between a set quantity of audio outputs. You can use it at your output jacks to select between amplifiers or mixer channels, use it in conjunction with the Audio In Switch to select between effects chains, or use it anywhere you'd like to be able to select an outgoing audio path using CV.
- **Max Blocks:** `18`
- **Avg DSP:** `0.7%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`# of outputs`** – `selects how many audio outputs you'd like to switch between from 1-16. output jacks will be added for each output and the select range from 0-1 will divide equally between them`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to switch`
    - **Option:** `# of outputs`
  - **Block `2` – `out select`**
    - **Knob:** `select value 0-1`
    - **Description:** `divides value from 0-1 between number of present switch outputs and sends input audio to corresponding switch output`
  - **Block `3` – `audio out 1`**
    - **Knob:** `no modifier`
    - **Description:** `sends audio from input source if chosen by switch parameter`
  - **Block `4*` – `audio out 2`**
    - **Knob:** `no modifier`
    - **Description:** `sends audio from input source if chosen by switch parameter`

### All Pass Filter
All Pass Filter passes through all frequencies at equal gain, but changes phase relationship between them.
- **Max Blocks:** `3`
- **Avg DSP:** `5%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`# of poles`** – `selects quantity of poles phase shifting will augment, 1 through 8`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio from source into all pass filter`
    - **Option:** `# of poles`
  - **Block `2` – `filter gain`**
    - **Knob:** `gain in dB`
    - **Description:** `determines gain of phase shift`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs filtered audio`

### Noise
Generates white noise from a single button. Use the strength of your connection as a level control. Helpful in connection with VCAs and ADSRs in creating drum sounds, etc.
- **Max Blocks:** `1`
- **Avg DSP:** `0.4%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, FM inputs, analysis modules`
- **Parameters:**
  - **Block `1` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs white noise generated by module`

### Audio Multiply
Takes one audio input and mathematically multiplies it with the other. This produces a ring mod/vocoder-like effect, or can be used as an alternative to a pitch-shifter to produce analog-like octave fuzz sounds when used with a fuzz or distortion. This module likes hot signals so be sure to bump the connection strengths. Remember that silence at any one of the inputs will result in silence at the output!
- **Max Blocks:** `3`
- **Avg DSP:** `0.4%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Parameters:**
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio in to multiplier`
  - **Block `2` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio in to multiplier`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `multiplied audio output`

### Bit Crusher
Bit Crusher produces distortion by reducing audio bandwidth by a set number of bits. Distortion becomes audible around 20 bits reduced. This effect can get noisy so try it with a gate.
- **Max Blocks:** `3`
- **Avg DSP:** `1%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`fractions`** – `allows you to adjust quantity of bits crushed by non-whole numbers`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio in to bit crusher`
    - **Option:** `fractions`
  - **Block `2` – `crushed bits`**
    - **Knob:** `# bits crushed from 0-31`
    - **Description:** `determines number of bits to reduce sonic resolution by`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs bit crushed audio`

### Aliaser
Aliaser produces samples of incoming audio and compares them against each other to find imperfections. These imperfections become the outgoing audio. As sample count grows, so too does the thickness of the outgoing sound. This effect is a signal hog so be sure to boost your connection strengths incoming and outgoing. Try connecting a LFO or envelope follower to the alias amount.
- **Max Blocks:** `3`
- **Avg DSP:** `0.7%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio in to aliaser`
  - **Block `2` – `alias amount`**
    - **Knob:** `# of samples`
    - **Description:** `depth of alias differential`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs aliased audio`

### Buffer Delay
Delays internal audio signal by number of buffers set by buffers option. This module is inaudible, but useful anywhere you need to line up internal parallel audio connections precisely.
- **Max Blocks:** `2`
- **Avg DSP:** `0.4%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`buffers`** – `select how many buffers to delay by from 1-16`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to be delayed`
    - **Option:** `buffers`
  - **Block `2` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs delayed audio`

### Looper
The Looper module allows you to record, overdub, and play back incoming audio, forwards or backwards, at the speed of your choice (pitch shifted). Get loopy!
- **Max Blocks:** `9`
- **Avg DSP:** `3%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`max rec time`** – `choose how much audio you'd like to be able to sample from 1s to 32s`
  - **`length edit`** – `toggles presence of start position and loop length parameters`
  - **`playback`** – `select if your loop will playback continuously or just once when triggered. During continuous playback, triggering the sampler to begin recording again will halt playback`
  - **`length`** – `Fixed plays back your loop and plays it back for its original duration, regardless of playback speed, this can leave gaps or cut off your loop. Pre-speed plays back your loop for its full duration, regardless if you've sped it up or slowed it down.`
  - **`hear while rec`** – `"on" will allow original audio to pass through the looper as you're recording it`
  - **`play reverse`** – `toggles presence of reverse playback parameter`
  - **`overdub`** – `"yes" will add a loop reset trigger, and allow the looper to overdub additional layers of audio over the original loop`
  - **`stop/play but`** – `toggles the presence of a loop playback stop and start trigger input`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to be recorded by sampler`
    - **Option:** `max rec time`
  - **Block `2` – `record`**
    - **Knob:** `rec/stop or rec/overdub/play states`
    - **Description:** `in "playback: once" mode, this button triggers the beginning and the end of recording a loop. in "playback: loop" mode, this button cycles between recording start/overdub/play similar to a conventional looper pedal. try with both latching and momentary footswitch modules, or press with your finger`
    - **Option:** `length edit`
  - **Block `3` – `restart playback`**
    - **Knob:** `no modifier`
    - **Description:** `triggers loop to play back from the beginning. use this to replay a recorded loop again and again in "playback: once" mode.`
    - **Option:** `playback`
  - **Block `4*` – `stop/play`**
    - **Knob:** `stop/play state`
    - **Description:** `triggers a pause in the playback of a loop. send another trigger or press again to unpause at same location in the loop.`
    - **Option:** `length`
  - **Block `5` – `speed/pitch`**
    - **Knob:** `click knob to cycle views of speed in %, pitch in semitones, or pitch in cents.note that in all views, both speed and pitch are affected by changes.`
    - **Description:** `determines speed and pitch profile of recording and loop playback, similar to recording to tape. the first loop is recorded at 100% by default. this parameter is also where the length option takes effect.`
    - **Option:** `hear while rec`
  - **Block `6*` – `start position`**
    - **Knob:** `time in s`
    - **Description:** `determines point in loop to start playback, when playback restarts, either when played as a result of natural looping or when triggered to do so by the restart playback button. note that this parameter presents itself as a value from 0s to the maximum length of time contained in that loop, so plan CV changes accordingly.`
    - **Option:** `play reverse`
  - **Block `7*` – `loop length`**
    - **Knob:** `time in s`
    - **Description:** `determines duration of loop to playback, which will either end playback early in "playback: once" mode, or restart the loop early in "playback: loop". mode. the value of this module is represented by a time in seconds which is equal to the total loop duration minus the time chosen in the "start position" parameter, so that the duration of loop playback can never be longer than the originally recorded loop.`
    - **Option:** `overdub`
  - **Block `8*` – `reverse playback`**
    - **Knob:** `forward or reverse state`
    - **Description:** `determines if looper is recording, overdubbing, or playing back in a forward or reverse trajectory. press button to toggle state or control with latching or momentary footswitch`
    - **Option:** `stop/play but`
  - **Block `9` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs audio playback`

### Granular
Granular breaks up incoming audio into tiny little grains and spits them back out in the quantity and shape of your choosing. Go from modest textures to completely unrecognizable oscillations. Granular can also be used as a granular delay by creating a feedback path from the output back to the input...
- **Max Blocks:** `10`
- **Avg DSP:** `8%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`num grains`** – `determine how many of the same grain to string together from 1-8`
  - **`channels`** – `toggles between mono or stereo operation`
  - **`pos control`** – `toggles behaviour of grain position parameter between CV control and tap tempo. connect an LFO or stomp switch`
  - **`size control`** – `toggles behaviour of grain size parameter between CV control and tap tempo. connect an LFO or stomp switch`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to be granulated`
    - **Option:** `num grains`
  - **Block `2*` – `audio inR`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio to be granulated`
    - **Option:** `channels`
  - **Block `3` – `grain size`**
    - **Knob:** `sample length in ms`
    - **Description:** `determines length of time to sample to create individual grains`
    - **Option:** `pos control`
  - **Block `4` – `grain position`**
    - **Knob:** `time elapsed in ms`
    - **Description:** `determines amount of time to elapse before playing back a sampled grain. when using granular as a delay, this parameter is your delay time. you can set it to be tap tempo in the edit options`
    - **Option:** `size control`
  - **Block `5` – `density`**
    - **Knob:** `grain saturation in CV`
    - **Description:** `works in conjunction with grain size to determine how many grains get created and played back`
  - **Block `6` – `texture`**
    - **Knob:** `grain shape in CV`
    - **Description:** `shapes the fade in and fade out of each grain`
  - **Block `7` – `speed/pitch`**
    - **Knob:** `time factor in %`
    - **Description:** `warps the playback speed and pitch of the grains`
  - **Block `8` – `freeze`**
    - **Knob:** `running of frozen state`
    - **Description:** `toggle between continuously running grains or freeze a continuous playback of a certain grain`
  - **Block `9` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs granulated audio`
  - **Block `10*` – `audio outR`**
    - **Knob:** `no modifier`
    - **Description:** `outputs granulated audio`

### Stereo Spread
Stereo Spread will take one or two channels and enhance their stereo field. This is generally used right before an audio output module but, as always, feel free to experiment!
- **Max Blocks:** `5`
- **Avg DSP:** `2%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`method`** – `select stereo spread technique. Haas (mono in, stereo out) or Mid-Side (2 in, 2 out)`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio source to be enhanced`
    - **Option:** `method`
  - **Block `2` – `delay time`**
    - **Knob:** `time in ms`
    - **Description:** `amount of delay applied to audio out 2`
  - **Block `3` – `audio out 1`**
    - **Knob:** `no modifier`
    - **Description:** `outputs a clean copy of the audio input`
  - **Block `4` – `audio out 2`**
    - **Knob:** `no modifier`
    - **Description:** `outputs a delayed copy of the audio input as determined by delay time`
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio source to be enhanced`
  - **Block `2` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio source to be enhanced`
  - **Block `3` – `side gain`**
    - **Knob:** `gain in dB`
    - **Description:** `adds or subtracts gain from phase inverted audio 1`
  - **Block `4` – `audio out 1`**
    - **Knob:** `no modifier`
    - **Description:** `outputs stereo enhanced audio "mid"`
  - **Block `5` – `audio out 2`**
    - **Knob:** `no modifier`
    - **Description:** `outputs stereo enhanced audio "side"`

### Bit Modulator
Bit Modulator takes one audio input and compares it against the other, creating an unholy glitchy combination of both sounds at the output. Choose between 3 different logic flavours with the "type" option. When taking audio from an external source, it's recommended to put a gate before the input.
- **Max Blocks:** `3`
- **Avg DSP:** `1.2%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Options:**
  - **`type`** – `select the flavour of your bit modulation between and, or, and xor. best not to think about it.`
- **Parameters:**
  - **Block `1` – `audio in 1`**
    - **Knob:** `no modifier`
    - **Description:** `connect an audio source`
    - **Option:** `type`
  - **Block `2` – `audio in 2`**
    - **Knob:** `no modifier`
    - **Description:** `connect another audio source`
  - **Block `3` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs bit modulated combination of both inputs`

### Diffuser
Diffuser spreads your signal across the galaxy like so many shimmering little stars. On it's own it sounds like a modulated slapback delay with no dry signal, but it can be used to construct many a tonal/atonal masterpiece.
- **Max Blocks:** `6`
- **Avg DSP:** `2%`
- **Connections:** `audio inputs/outputs, VCAs, audio effects, oscillators,`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect an audio source`
  - **Block `2` – `gain`**
    - **Knob:** `gain in dB`
    - **Description:** `sets gain of delayed audio sent back to input as a feedback loop`
  - **Block `3` – `size`**
    - **Knob:** `delay size from 80-4999`
    - **Description:** `size of delay gap in samples`
  - **Block `4` – `mod width`**
    - **Knob:** `width size from 3-499 samples`
    - **Description:** `modulation width in samples`
  - **Block `5` – `mod rate`**
    - **Knob:** `rate from 0 - 5.90 seconds`
    - **Description:** `modulation rate in seconds`
  - **Block `6` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `outputs modulated audio`

---

## CONTROL MODULES
These modules control CV, and are the basic building blocks of ZOIA functionality. Use CV input bias to determine a module's starting CV (or minimum), and use the connection strength to determine the maximum value.

### LFO
The Low Frequency Oscillator is one of the workhorse modules of the ZOIA. This will generate CV in the waveform and range of your choosing. Connect it to a sequencer to cycle through steps, to an audio effect to swing it's parameters around, or to any outboard piece of gear through a MIDI or CV interface module. The connection strength you enter at the output will determine the maximum sweep of the LFO.
- **Max Blocks:** `3`
- **Avg DSP:** `0.3%`
- **Connections:** `other LFOs, sequencers, CV inputs, MIDI inputs, footswitches/pushbuttons, envelopes,`
- **Options:**
  - **`waveform`** – `select waveform of oscillator: square, sine, triangle, sawtooth, ramp, or random (essentially a random number generator)`
  - **`swing control`** – `toggles presence of swing amount parameter, allows you to dial in asymmetry to the waveform`
  - **`output`** – `determines range of CV output from from 0 thru 1 or -1 thru 1`
  - **`input`** – `select oscillator frequency source. CV input allows you to dial it in with the knob or control with another source, linear cv is similar but with a different input relationship, and trigger will interpret changes in CV as a tap tempo`
  - **`phase input`** – `toggles presence of phase input parameter`
  - **`phase reset`** – `toggles presence of phase reset parameter`
- **Parameters:**
  - **Block `1` – `frequency/trigger in`**
    - **Knob:** `frequency in Hz (trigger in: no modifier)`
    - **Description:** `sets the frequency at which the LFO oscillates (trigger in: calculates rate of LFO via incoming CV input)`
    - **Option:** `waveform`
  - **Block `2*` – `swing amount`**
    - **Knob:** `swing factor from -100 to 100`
    - **Description:** `determines asymmetry of waveform. Apply negative CV for swing factors under 0`
    - **Option:** `swing control`
  - **Block `3*` – `phase input`**
    - **Knob:** `wave phase in degrees`
    - **Description:** `determines the phase of the generated LFO waveform relative to its native starting point. Use in conjunction with phase reset to sync multiple LFOs with various phase relationships.`
    - **Option:** `output`
  - **Block `4*` – `phase reset`**
    - **Knob:** `send CV signal to restart LFO generation`
    - **Description:** `resets LFO back to its native starting point. Enable this parameter in multiple LFOs and connect a stomp, pushbutton, or other CV source to force them to sync up.`
    - **Option:** `input`
  - **Block `5` – `output`**
    - **Knob:** `no modifier`
    - **Description:** `CV output of LFO`
    - **Option:** `phase input`

### Sequencer
The sequencer allows you to create a number of "steps" (1-32) that can be cycled through, and each step can be used to send a CV value out of that tracks output. The sequencer can have up to 8 tracks, each with their own unique output so it's possible to create complex melodies or rhythmic patterns. Try connecting an LFO to the sequencer's gate input to start the sequencer cycle. Then connect the sequencer output to an oscillator, a cv track to the oscillator's frequency input, and set each step to a different note. Now your ZOIA is playing itself! note: the first track on the sequencer can have each step controlled directly by other CV sources as well.
- **Max Blocks:** `42`
- **Avg DSP:** `2%`
- **Connections:** `nan`
- **Options:**
  - **`number of steps`** – `select number of steps from 1-32. sequencer will consume a button for each step so make sure you have room`
  - **`num of tracks`** – `select number of tracks from 1-8. sequencer will add a button for each track output`
  - **`restart jack`** – `toggles presence of queue start module`
  - **`behaviour`** – `select if you'd like your sequencer to play continuously or only when it's triggered to do so. Sequencer can be triggered by be queue start module (restart jack)`
- **Parameters:**
  - **Block `1` – `step 1`**
    - **Knob:** `note in CV (click knob to show note), CV value of gate, or # of divisions of ratchet on selected track`
    - **Description:** `step will affect the value that's being sent out the output`
    - **Option:** `number of steps`
  - **Block `2*` – `step 2`**
    - **Knob:** `note in CV (click knob to show note), CV value of gate, or # of divisions of ratchet on selected track`
    - **Description:** `step will affect the value that's being sent out the output`
    - **Option:** `num of tracks`
  - **Block `3*` – `step 3`**
    - **Knob:** `note in CV (click knob to show note), CV value of gate, or # of divisions of ratchet on selected track`
    - **Description:** `step will affect the value that's being sent out the output`
    - **Option:** `restart jack`
  - **Block `4*` – `step 4`**
    - **Knob:** `note in CV (click knob to show note), CV value of gate, or # of divisions of ratchet on selected track`
    - **Description:** `step will affect the value that's being sent out the output`
    - **Option:** `behaviour`
  - **Block `5` – `gate in`**
    - **Knob:** `CV value`
    - **Description:** `minimum CV input that triggers the sequencer to engage steps in sequencer. apply CV over minimum to engage next step`
  - **Block `6*` – `queue start`**
    - **Knob:** `CV value`
    - **Description:** `minimum CV input that triggers the sequencer to start its loop over. bring CV above queue start threshold during a step to start the sequencer back at step 1`
  - **Block `7` – `out type 1: CV`**
    - **Knob:** `colour of track`
    - **Description:** `CV type output will display steps as played notes or CV values. Click knob to change track type. Rotate knob to change track colour.`
  - **Block `8*` – `out type 2: gate`**
    - **Knob:** `colour of track`
    - **Description:** `Gate type output will output an on/off status of the associated step. While output selected, steps can be assigned on/off status simply by pushing them. Click knob to change track type. Rotate knob to change track colour.`
  - **Block `9*` – `out type 3: ratchet`**
    - **Knob:** `colour of track`
    - **Description:** `Ratchet type output will divide the step's duration into a set number of divisions. Get your trap on! Click knob to change track type. Rotate knob to change track colour.`

### ADSR
The Attack Decay Sustain Release module is what gives a note generated from an oscillator a natural sounding envelope when played from a keyboard. Connect your oscillator or other audio source to the input of a VCA, and connect the CV output of the ADSR to the CV input on the VCA. Connect the keyboard or MIDI note gate out to the CV input of the ADSR and you've got yourself a simple synthesizer! Tweak the values to taste, or connect them to other CV inputs for experimentation. Use the optional retrigger input to restart the envelope around a note that is played before the ADSR is released.
- **Max Blocks:** `10`
- **Avg DSP:** `0.07%`
- **Connections:** `MIDI notes in (gate in), keyboard (gate out), pushbuttons/footswitches, sequencers, LFOs, MIDI input/outputs, CV inputs/outputs`
- **Options:**
  - **`retrigger input`** – `toggles presence of retrigger parameter`
  - **`initial delay`** – `toggles presence of delay parameter`
  - **`hold attack/decay`** – `toggles presence of hold attack decay parameter`
  - **`str`** – `toggles presence of parameters associated with sustain section. By default this is on, but you can use only the attack and decay portion of the envelope. Notes and CV inputs will not sustain, but rise and fall back down to 0 at the CV output`
  - **`immediate release`** – `if note/CV input is not held until attack reaches its peak, ON: immediate release will skip sustain section and release immediately. If hold sustain release parameter is present, this will also function OFF: envelope will travel to the top of the attack and carry the CV output through the envelope as set up by the user`
  - **`hold sustain/release`** – `toggles presence of hold sustain release parameter`
  - **`time scale`** – `select between linear and exponential time scales at input`
- **Parameters:**
  - **Block `1` – `cv input`**
    - **Knob:** `CV value`
    - **Description:** `an increase in CV value will trigger the ADSR envelope. A plateau of CV at the input will hold the the CV output at the set sustain level`
    - **Option:** `retrigger input`
  - **Block `2*` – `retrigger`**
    - **Knob:** `CV value`
    - **Description:** `a detected increase in CV value will retrigger the attack/decay of the envelope during a sustained note/CV input`
    - **Option:** `initial delay`
  - **Block `3*` – `delay`**
    - **Knob:** `time in ms`
    - **Description:** `time between CV detection at the input and beginning of attack. Useful in adding blooming textures when using multiple voices/effects`
    - **Option:** `hold attack/decay`
  - **Block `4` – `attack`**
    - **Knob:** `time in ms`
    - **Description:** `attack time of envelope. Go from short crisp starts to long slow fade-ins`
    - **Option:** `str`
  - **Block `5*` – `hold attack decay`**
    - **Knob:** `time in ms`
    - **Description:** `time between peak of attack and start of decay during sustained note/CV input. Will hold the envelope at its peak for set duration`
    - **Option:** `immediate release`
  - **Block `6` – `decay`**
    - **Knob:** `time in ms`
    - **Description:** `decay time from peak of attack into sustain section. Go from abruptly stopped notes to gentle fades to the sustain level`
  - **Block `7` – `sustain`**
    - **Knob:** `CV value`
    - **Description:** `selects CV output level during sustained note/CV input. This can be thought of as the "volume" of your sustained notes`
  - **Block `8*` – `hold sustain release`**
    - **Knob:** `time in ms`
    - **Description:** `this variable will tack on additional time between sustain and release once the CV input stops receiving input. This can be useful in lining up fade outs when using multiple voices/effects`
    - **Option:** `hold sustain/release`
  - **Block `9` – `release`**
    - **Knob:** `time in ms`
    - **Description:** `"fade out" time of envelope once sustain has been lifted. End notes abruptly or gently`
    - **Option:** `time scale`
  - **Block `10` – `cv output`**
    - **Knob:** `no modifier`
    - **Description:** `CV output of envelope`

### Sample and Hold
Sample and Hold will take the CV value at the input and hold it in place at the output until triggered to look again at the input and update the output. Connect a LFO to the trigger to convert smooth changes in CV into stepped changes in CV. The speed of the LFO will determine the perceived resolution of the CV output.
- **Max Blocks:** `3`
- **Avg DSP:** `0.1%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV value`
    - **Description:** `CV input to get sampled/held`
  - **Block `2` – `trigger`**
    - **Knob:** `CV value`
    - **Description:** `if track & hold is off: a rise in CV at trigger will cause value at input to be held at output, a decline in CV at trigger arms next trigger. if track & hold is on: a rise in CV at trigger will cause value at input to be held at output, a decline in CV at trigger causes output to follow input.`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `CV output will hold CV value at input when CV applied to trigger input`

### CV Invert
Inverts the incoming CV. For example, a CV input of 1 will output as -1. An input of 0.2 will output as -0.2.
- **Max Blocks:** `2`
- **Avg DSP:** `0.02%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `minimum CV value`
    - **Description:** `CV input to get inverted`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `inverted CV output`

### CV Rectify
CV Rectify will interpret incoming CV from -1 to 1 and "flip" the negative values into positive values equidistant from 0.
- **Max Blocks:** `2`
- **Avg DSP:** `0.07%`
- **Connections:** `nothing, LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV bias`
    - **Description:** `dial in a CV value to be generated`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `CV value`

### Value
Value allows you to connect to multiple modules and adjust their parameters simultaneously from one CV adjustment at the input.
- **Max Blocks:** `2`
- **Avg DSP:** `0.15%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Options:**
  - **`output`** – `determines range of CV output from from 0 thru 1 or -1 thru 1`
- **Parameters:**
  - **Block `1` – `value`**
    - **Knob:** `CV input`
    - **Description:** `input a CV value to be shared. click knob to toggle between CV value and music note`
    - **Option:** `output`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `CV output`

### Trigger
Creates a very short CV pulse (value of 1) on detection of upward CV input. This is useful in creating a tap tempos from regular or irregular CV waveforms, triggering sequencers or ADSRs at specific times, etc.
- **Max Blocks:** `2`
- **Avg DSP:** `0.10%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs,`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV to be triggered from`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outgoing CV trigger`

### CV Flip Flop
This is essentially a latching CV switch with an output of 0 or 1. When the input sees an upward CV change, the flip flop is triggered to change it's output state from 0 to 1 at the next upward change in CV, which must occur after a downward change in CV. So, the flip flop changes from 0 to 1 at every other upward change in CV.
- **Max Blocks:** `2`
- **Avg DSP:** `0.2%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs,`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV to be analysed`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs either 0 or 1 CV, as determined by the flip flop`

### CV Delay
CV Delay will take incoming CV and delay it in time by a set amount.
- **Max Blocks:** `3`
- **Avg DSP:** `1.5%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV to delay. An increase in threshold here will add adjustment to outgoing CV`
  - **Block `2` – `delay time`**
    - **Knob:** `time in ms`
    - **Description:** `determines how long to delay CV for before sending to output`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs delayed CV`

### CV Loop
CV Loop functions similar to an audio looper except records patterns of CV signal instead of audio. You can record and play back snippets of LFOs, sequences, changes in CV or MIDI control etc.
- **Max Blocks:** `8`
- **Avg DSP:** `0.1%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`max rec time`** – `select maximum amount of time you'd like to be able to loop from 1s - 4s`
  - **`length edit`** – `toggles presence of start position and stop position parameters`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV in to get looped`
    - **Option:** `max rec time`
  - **Block `2` – `record`**
    - **Knob:** `press button, and/or CV up to record, CV down to play back`
    - **Description:** `toggles between playback and record states. Push button to toggle between recording and playing loop. Alternatively, a rise in CV will trigger record, and a decrease will trigger playback`
    - **Option:** `length edit`
  - **Block `3` – `play`**
    - **Knob:** `press button, and/or CV up to play back, CV down to stop`
    - **Description:** `toggles between playback and stopped states. Push button to toggle between playing loop and stopping. Alternatively, a rise in CV will trigger playback, and a decrease will trigger stop`
  - **Block `4` – `playback speed`**
    - **Knob:** `playback speed in %`
    - **Description:** `adjusts speed of CV Loop playback`
  - **Block `5*` – `start position`**
    - **Knob:** `position from start of loop in seconds`
    - **Description:** `determines starting point of playback of recorded CV signal. By changing this you can have your loop shortened by chopping off the beginning.`
  - **Block `6*` – `stop position`**
    - **Knob:** `position from end of loop in seconds`
    - **Description:** `determines maximum length of recorded CV signal played back. By changing this you can shorten the loop by chopping off the end.`
  - **Block `7` – `restart loop`**
    - **Knob:** `push button`
    - **Description:** `push button or send a CV increase to restart loop playback from the beginning of recorded loop`
  - **Block `8` – `cv output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs CV playback`

### CV Filter
CV Filter dictates the length of time a CV output will take to respond to a change in CV input, determined by the time constant. The CV change occurs logarithmically for a nice smooth transition. Use this module in series with a MIDI/keyboard note to add portamento to your synth voice. You can also use this module to vary the shape of an LFO waveform or connect to a stomp switch to produce a long slow change in an audio effect.
- **Max Blocks:** `3`
- **Avg DSP:** `0.1%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`control`** – `allows for combined or separate control of upward and downward slew limited CV changes`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV to be filtered`
    - **Description:** `connect CV to filtered`
    - **Option:** `control`
  - **Block `2` – `time constant`**
    - **Knob:** `time in ms`
    - **Description:** `determines the time it takes the CV output to reach 63%, or decay to 37%, of the input`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `filtered CV output`
  - **Block `above: control linked, below: control separate` – `above: control linked, below: control separate`**
    - **Knob:** `above: control linked, below: control separate`
    - **Description:** `above: control linked, below: control separate`
  - **Block `1` – `CV input`**
    - **Knob:** `CV to be filtered`
    - **Description:** `connect CV to filtered`
  - **Block `2` – `rise constant`**
    - **Knob:** `time in ms`
    - **Description:** `determines the time it takes the CV output to reach 63% of the input`
  - **Block `3` – `fall constant`**
    - **Knob:** `time in ms`
    - **Description:** `determines the time it takes the CV output to decay to 37% of the input`
  - **Block `4` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `filtered CV output`

### Slew Limiter
Slew Limiter is similar in behaviour to CV Filter except that the rate of change in changes of CV happen linearly instead of logarithmically. This is the classic portamento, and can be used anywhere CV changes occur to give them a different feel. Try using an unlinked Slew Limiter with a stomp switch module to give more expression pedal-like behaviour to your stomp switch.
- **Max Blocks:** `4`
- **Avg DSP:** `0.2%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`control`** – `allows for combined or separate control of upward and downward slew limited CV changes`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV source`
    - **Option:** `control`
  - **Block `2` – `slew rate`**
    - **Knob:** `time in seconds`
    - **Description:** `determines slew rate. This time value changes the speed at which the CV source responds to changes from its current value.`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs slew limited CV`
  - **Block `above: control linked, below: control separate` – `above: control linked, below: control separate`**
    - **Knob:** `above: control linked, below: control separate`
    - **Description:** `above: control linked, below: control separate`
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV source`
  - **Block `2` – `rising lag`**
    - **Knob:** `time in seconds`
    - **Description:** `determines time change factor of upward changes in CV`
  - **Block `3` – `falling lag`**
    - **Knob:** `time in seconds`
    - **Description:** `determines time change factor of downward changes in CV`
  - **Block `4` – `CV output`**
    - **Knob:** `CV output`
    - **Description:** `outputs slew limited CV`

### Clock Divider
Clock Divider module will detect tempo of incoming CV upward changes, divide it by a user determined ratio, and output CV triggers at the resulting tempo. This can be a handy way of getting a tap tempo from a slightly irregular waveform.
- **Max Blocks:** `4`
- **Avg DSP:** `0.14%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`input`** – `select clock frequency source. CV input allows you to dial it in with the knob or control with another source, tap will interpret changes in CV as a tap tempo`
- **Parameters:**
  - **Block `1` – `input`**
    - **Knob:** `frequency in Hz, ms, or bpm (tap: no modifier)`
    - **Description:** `sets the frequency at which the LFO oscillates (tap in: calculates rate of LFO via incoming CV input)`
    - **Option:** `input`
  - **Block `2` – `reset switch`**
    - **Knob:** `toggles between "waiting" and "armed"`
    - **Description:** `an increase in CV will cease output, a new tap tempo at the input will continue on until reset switch is triggered again`
  - **Block `3` – `dividend`**
    - **Knob:** `select the numerator of your tap fraction from 1-32`
    - **Description:** `create your custom clock division fraction! if this number is higher than the one after it, your clock will be faster than your tap source.`
  - **Block `4` – `divisor`**
    - **Knob:** `select the denominator of your tap fraction from 1-32`
    - **Description:** `create your custom clock division fraction! if this number is higher than the one before it, your clock will be slower than your tap source.`
  - **Block `5` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `tap tempo CV output`

### Comparator
Comparator is a logic module that will switch CV on if positive input is equal to or greater than negative input, and off if positive input is less than negative input. Off can be defined as 0 or -1 by the output range. This can be useful if you'd like to have something happen, but only above a certain threshold.
- **Max Blocks:** `3`
- **Avg DSP:** `0.04%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`output`** – `determines range of CV output from from 0 thru 1 or -1 thru 1`
- **Parameters:**
  - **Block `1` – `CV positive input`**
    - **Knob:** `CV input positive threshold`
    - **Description:** `sets incoming CV positive threshold`
    - **Option:** `output`
  - **Block `2` – `CV negative input`**
    - **Knob:** `CV input negative threshold`
    - **Description:** `sets incoming CV negative threshold`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `CV output. If CV at positive side is greater than CV at negative side, CV output will be 1. If CV at positive side is lower than CV at negative side, CV output will be 0 or -1, depending on output range`

### In Switch
In Switch takes a selected quantity of CV inputs and allows you to switch between them to a single CV output. You can use this to select between LFOs to a CV source, external CV modules, or use in conjunction with the CV out switch to choose between ADSRs or other CV module chains
- **Max Blocks:** `18`
- **Avg DSP:** `0.2%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`num inputs`** – `selects how many CV sources you'd like to switch between from 2-16. input parameters will be added for each source and the input select range from 0-1 will divide equally between them`
- **Parameters:**
  - **Block `1` – `CV input 1`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
    - **Option:** `num inputs`
  - **Block `2*` – `CV input 2`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
  - **Block `3` – `in select`**
    - **Knob:** `select value 0-1`
    - **Description:** `divides value from 0-1 between number of present switch inputs and selects CV source corresponding to value present`
  - **Block `4` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs selected CV source`

### Out Switch
Out Switch takes a CV input and routes it between a set quantity of CV outputs. You can use it to select which sequencers, ADSRs, or tap tempos to send triggers to, etc.
- **Max Blocks:** `18`
- **Avg DSP:** `0.2%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`# of outputs`** – `selects how many CV outputs you'd like to switch from between from 2-16. output parameters will be added for each source and the output select range from 0-1 will divide equally between them`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
    - **Option:** `# of outputs`
  - **Block `2` – `out select`**
    - **Knob:** `select value 0-1`
    - **Description:** `divides value from 0-1 between number of present switch outputs and selects CV output corresponding to value present. If only one output is present, a select value of 0 will turn switch off, a select value above 0 will turn switch on.`
  - **Block `3` – `CV output 1`**
    - **Knob:** `no modifier`
    - **Description:** `if selected, outputs CV input`
  - **Block `4*` – `CV output 2`**
    - **Knob:** `no modifier`
    - **Description:** `if selected, outputs CV input`

### Quantizer
Quantizer will interpret incoming CV and send its nearest equivalent note as a CV output.
- **Max Blocks:** `2`
- **Avg DSP:** `1%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`key/scale jacks`** – `toggles presence of key and scale jacks`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
    - **Option:** `key/scale jacks`
  - **Block `2*` – `key`**
    - **Knob:** `key of output`
    - **Description:** `choose a key between A and G#. connect CV to control remotely`
  - **Block `3*` – `scale`**
    - **Knob:** `scale type`
    - **Description:** `choose between chromatic, major, minor natural, minor harmonic, or minor melodic. connect CV to control remotely`
  - **Block `4` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs CV corrected to match closest note`

### Steps
Steps will interpret incoming changes in upward CV as a tempo, split the wave cycle into a set number of steps, and then send the CV present at the input during each step to the output. You can use this to convert a nice smooth LFO and reduce its resolution into steps.
- **Max Blocks:** `3`
- **Avg DSP:** `0.7%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `connect CV source`
  - **Block `2` – `quant steps`**
    - **Knob:** `number of steps to split wave cycle into`
    - **Description:** `select number of steps from 2 to 63. A higher quantity of steps results in a smoother output wave.`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs quantized CV`

### Multiplier
Multiply will take the CV signal present at each input and multiply them together at the output. In this way you can use one CV source to amplify, tame, or modulate another. Remember that a value of 0 at any input will result in 0 at the output. It's math!
- **Max Blocks:** `9`
- **Avg DSP:** `0.2%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`num inputs`** – `Select how many sources you'd like to multiply together from 2-8. Each value above 2 will add a corresponding input jack.`
  - **`output`** – `determines range of CV output from from 0 to 1 or -1 to 1`
  - **`new val on trig`** – `toggles presence of trigger in parameter`
- **Parameters:**
  - **Block `1` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
    - **Option:** `num inputs`
  - **Block `2` – `CV input`**
    - **Knob:** `CV input`
    - **Description:** `set or connect CV source`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs multiplied CV`
  - **Block `1*` – `trigger in`**
    - **Knob:** `CV input`
    - **Description:** `a change in CV here will generate a new random number and hold it at the output`
    - **Option:** `output`
  - **Block `2` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `generates constantly refreshing random numbers until stopped by optional trigger`
    - **Option:** `new val on trig`

### Rhythm
Rhythm will take an incoming CV signal, interpret it as a series of triggers, record those triggers and play them back at the output.
- **Max Blocks:** `5`
- **Avg DSP:** `0.5%`
- **Connections:** `footswitches/pushbuttons, LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals,`
- **Options:**
  - **`done ctl`** – `toggles presence of play done parameter`
- **Parameters:**
  - **Block `1` – `rec start-stop`**
    - **Knob:** `CV input`
    - **Description:** `triggers starting and stopping of recording`
    - **Option:** `done ctl`
  - **Block `2` – `rhythm in`**
    - **Knob:** `CV input`
    - **Description:** `connect CV to be recorded`
  - **Block `3` – `play`**
    - **Knob:** `CV input`
    - **Description:** `triggers playback of rhythm`
  - **Block `4*` – `play done`**
    - **Knob:** `no modifier`
    - **Description:** `Goes high when playback is done.`
  - **Block `5` – `rhythm out`**
    - **Knob:** `no modifier`
    - **Description:** `CV rhythm output. interprets recorded loop as series of rhythmic pulses`

### Tap to CV
Outputs a CV value proportional to the tap tempo input.
- **Max Blocks:** `4`
- **Avg DSP:** `0.12%`
- **Connections:** `footswitches/pushbuttons, LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs`
- **Options:**
  - **`range control`** – `toggles presense of min time and max time buttons`
  - **`time scale`** – `determines how module interprets cv output from tap source, either linear or exponential`
- **Parameters:**
  - **Block `1` – `tap input`**
    - **Knob:** `no modifier`
    - **Description:** `connect tap source, MIDI clock, or LFO`
    - **Option:** `range control`
  - **Block `2*` – `min time`**
    - **Knob:** `time in s`
    - **Description:** `set the tap tempo minimum time`
    - **Option:** `time scale`
  - **Block `3*` – `max time`**
    - **Knob:** `time in s`
    - **Description:** `set the tap tempo maximum time`
  - **Block `4` – `output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs CV as a value proportional to the detected frequency of incoming taps`

### CV Mixer
An 8 channel CV Mixer and Attenuverter
- **Max Blocks:** `17`
- **Avg DSP:** `0.30%`
- **Connections:** `LFOs, sequencers, MIDI inputs/outputs, CV inputs/outputs, expression pedals, footswitches/pushbuttons`
- **Options:**
  - **`num channels:`** – `select number of channels from 1 to 8. each additional channel adds both a CV input block and a mix/atten slider`
  - **`mode:`** – `select output calculation type. "summing" will add all outputs together, clipping anything outside the +1/-1 CV range, while "average" will output the mean of the outputs, ensuring that  the output doesn't get clipped`
- **Parameters:**
  - **Block `1` – `cv in 1`**
    - **Knob:** `CV input`
    - **Description:** `connect input CV for mixer/attenuverter channel 1`
    - **Option:** `num channels:`
  - **Block `2*` – `cv in 2`**
    - **Knob:** `CV input`
    - **Description:** `connect input CV for mixer/attenuverter channel 2`
    - **Option:** `mode:`
  - **Block `3` – `atten 1`**
    - **Knob:** `CV input slider`
    - **Description:** `set mix/atten level for channel 1: a CV value of 1.0 passes the full signal, 0.5 fully attenuates it, and 0.0 fully inverts it.`
  - **Block `4*` – `atten 2`**
    - **Knob:** `CV input slider`
    - **Description:** `set mix/atten level for channel 2: a CV value of 1.0 passes the full signal, 0.5 fully attenuates it, and 0.0 fully inverts it`
  - **Block `5` – `cv output`**
    - **Knob:** `no modifier`
    - **Description:** `outputs CV as a value proportional to the detected frequency of incoming taps`

---

## ANALYSIS MODULES
These modules take incoming audio and process them into CV according to a characteristic - volume, pitch, or transient response.

### Onset Detector
Onset Detector looks for incoming audio signal and generates a CV trigger at the peaks. Use a regular audio source to advance a sequencer, tap a tempo, etc
- **Max Blocks:** `3`
- **Avg DSP:** `17.0%`
- **Connections:** `inputs, audio effect outputs, VCAs,`
- **Options:**
  - **`sensitivity`** – `toggles presence of sensitivity jack`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `sensitivity`
  - **Block `2*` – `sensitivity`**
    - **Knob:** `value in CV`
    - **Description:** `determines signal strength at which incoming audio triggers outgoing CV`
  - **Block `3` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `sends CV trigger when incoming audio surpasses threshold`

### Env Follower
Envelope Follower will interpret an incoming audio signal as a CV signal based on its signal strength. Use this to trigger filter sweeps, audio effects parameters, LFO rates, etc. The connection strength can act as a sensitivity control.
- **Max Blocks:** `2`
- **Avg DSP:** `5%`
- **Connections:** `inputs, audio effect outputs, VCAs,`
- **Options:**
  - **`rise/fall time`** – `toggles presence of rise and fall time parameters`
  - **`output scale`** – `determines curve of dB to CV interpretation. log is recommended for use with outside audio source, log or linear both work well with internally generated audio`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `rise/fall time`
  - **Block `2*` – `rise time`**
    - **Knob:** `time in seconds`
    - **Description:** `determines time taken for CV to reach peak once audio is detected at input`
    - **Option:** `output scale`
  - **Block `3*` – `fall time`**
    - **Knob:** `time in seconds`
    - **Description:** `determines time taken for CV to reach zero once audio is no longer detected at input`
  - **Block `4` – `CV output`**
    - **Knob:** `no modifier`
    - **Description:** `sends incoming audio level as CV output`

### Pitch Detector
Pitch Detector interprets the pitch of a connected audio signal as a CV note output, which can be sent to an oscillator or quantizer. You can affect the tracking by changing the connection strength between the audio source and the audio input, and transpose which note the oscillator will generate using the connection strength to the oscillator. Click knob to toggle display between frequency in Hz and note.
- **Max Blocks:** `2`
- **Avg DSP:** `2.5%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
  - **Block `2` – `pitch out`**
    - **Knob:** `no modifier`
    - **Description:** `interprets pitch of incoming audio into a music note`

---

## EFFECT MODULES
These are ZOIA's audio effects. If you're a guitar/bass player, this is your playground. Experimentation is key!

### Tone Control
Tone Control is a 3 or 4 band tone control. Use this in conjunction with Distortion, Delay w/Mod, Reverb, or even a clean sound to fundamentally change its character.
- **Max Blocks:** `10`
- **Avg DSP:** `5%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like to EQ one or two channels`
  - **`num mid bands`** – `toggles presence of mid frequency band 2`
- **Parameters:**
  - **Block `1` – `aud in L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `aud in R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `num mid bands`
  - **Block `3` – `low shelf`**
    - **Knob:** `level in dB`
    - **Description:** `adjust gain of all frequencies below X Hz`
  - **Block `4` – `mid gain 1`**
    - **Knob:** `level in dB`
    - **Description:** `adjust gain of mid frequency 1`
  - **Block `5` – `mid frequency 1`**
    - **Knob:** `frequency in Hz`
    - **Description:** `adjust frequency of mid frequency 1`
  - **Block `6*` – `mid gain 2`**
    - **Knob:** `level in dB`
    - **Description:** `adjust gain of mid frequency 2`
  - **Block `7*` – `mid frequency 2`**
    - **Knob:** `frequency in Hz`
    - **Description:** `adjust frequency of mid frequency 2`
  - **Block `8` – `high shelf`**
    - **Knob:** `level in dB`
    - **Description:** `adjust gain of all frequencies above X Hz`
  - **Block `9` – `output L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `10*` – `output R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Delay w/Mod
Delay is one of the classic delay effects. Delay w/Mod differs from the Delay Line module found in Audio Out in that it runs a dry signal alongside the wet, has a feedback section, and a modulation section. Set the delay time either by tap or rotary/CV input. Optional stereo outputs round out the list of features. You can change the character of the delay effect with the "type" option, and/or by setting your mix to wet only, adding tone control and other effects to the output, and connecting your audio source directly to your output (bypassing the delay module) to act as the dry signal.
- **Max Blocks:** `9`
- **Avg DSP:** `18%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like mono, mono to stereo, or stereo channels`
  - **`control`** – `toggles behaviour of tempo input between tap and cv. tap will quantize CV pulses into a tempo, and CV lets you dial in a time similar to a typical delay pedal`
  - **`type`** – `select character of delay line: clean, tape, old tape, or bbd`
  - **`tap ratio`** – `when using tap tempo control mode, this option determines the ratio of repeats per tap cycle. select between 1:1, 2:3, 1:2, 1:3, 3:8, 1:4, 3:16, 1:8, 1:16, and 1:32`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `control`
  - **Block `3` – `delay time`**
    - **Knob:** `time in seconds, bpm, or Hz`
    - **Description:** `click knob to cycle views of delay time. this jack acts as the tap tempo in when selected in control. connect stomp switch, pushbutton, LFO etc`
    - **Option:** `type`
  - **Block `4` – `feedback`**
    - **Knob:** `level in dB`
    - **Description:** `sets feedback in dB. Achieve self oscillation by going fully clockwise to 0db`
    - **Option:** `tap ratio`
  - **Block `5` – `mod rate`**
    - **Knob:** `rate in Hz`
    - **Description:** `modulation rate in Hz`
  - **Block `6` – `mod depth`**
    - **Knob:** `level in CV`
    - **Description:** `modulation depth as CV value.`
  - **Block `7` – `mix`**
    - **Knob:** `level in dB`
    - **Description:** `wet to dry signal level. go from no audible delay at -inf dB to no audible dry signal at -0.00dB`
  - **Block `8` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `9*` – `audio out2`**
    - **Knob:** `no modifier`
    - **Description:** `connect secondary audio output if present`

### Ping Pong Delay
Ping Pong Delay is almost identical to the Delay w/ Mod except for one key aspect: the delay repeats ping pong from left to right across stereo outputs. When stereo inputs are selected, one input will ping while the other pongs, followed by a pong while the other pings into the opposite and then correct outputs.
- **Max Blocks:** `9`
- **Avg DSP:** `18%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like mono to stereo or stereo channels`
  - **`control`** – `toggles behaviour of tempo input between tap and cv. tap will quantize CV pulses into a tempo, and CV lets you dial in a time similar to a typical delay pedal`
  - **`type`** – `select character of delay line: clean, tape, old tape, or bbd`
  - **`tap ratio`** – `when using tap tempo control mode, this option determines the ratio of repeats per tap cycle`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `control`
  - **Block `3` – `delay time`**
    - **Knob:** `time in seconds, bpm, or Hz`
    - **Description:** `click knob to cycle views of delay time. this jack acts as the tap tempo in when selected in control. connect stomp switch, pushbutton, LFO etc`
    - **Option:** `type`
  - **Block `4` – `feedback`**
    - **Knob:** `level in dB`
    - **Description:** `sets feedback in dB. Achieve self oscillation by going fully clockwise to 0db`
    - **Option:** `tap ratio`
  - **Block `5` – `mod rate`**
    - **Knob:** `rate in Hz`
    - **Description:** `modulation rate in Hz`
  - **Block `6` – `mod depth`**
    - **Knob:** `level in CV`
    - **Description:** `modulation depth as CV value.`
  - **Block `7` – `mix`**
    - **Knob:** `level in dB`
    - **Description:** `wet to dry signal level. go from no audible delay at -inf dB to no audible dry signal at -0.00dB`
  - **Block `8` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `9` – `audio out2`**
    - **Knob:** `no modifier`
    - **Description:** `connect secondary audio output if present`

### OD & Distortion
The OD & Distortion module provides classic overdrive and distortion tones.
- **Max Blocks:** `4`
- **Avg DSP:** `17.0%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`model`** – `choose between several flavours of distortion: plexi, germ, classic, or pushed`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `model`
  - **Block `2` – `input gain`**
    - **Knob:** `gain in dB`
    - **Description:** `sets input gain of distortion. the louder the input gain, the higher the distortion factor`
  - **Block `3` – `output gain`**
    - **Knob:** `gain in dB`
    - **Description:** `sets master volume of module. as input gain rises, volume increases just like a typical distortion pedal. use output gain to compensate for this`
  - **Block `4` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`

### Fuzz
The Fuzz module provides gnarly fuzz tones for your sonic enjoyment.
- **Max Blocks:** `4`
- **Avg DSP:** `16.0%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`model`** – `choose between several flavours of fuzz: efuzzy, burly, scoopy, or ugly`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `model`
  - **Block `2` – `input gain`**
    - **Knob:** `gain in dB`
    - **Description:** `sets input gain of distortion. the louder the input gain, the higher the distortion factor`
  - **Block `3` – `output gain`**
    - **Knob:** `gain in dB`
    - **Description:** `sets master volume of module. as input gain rises, volume increases just like a typical distortion pedal. use output gain to compensate for this`
  - **Block `4` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`

### Compressor
Compression is a vastly useful audio tool that controls your signal level according to changes in input level. You can create natural reductions in gain to help things mix better, help tame or enhance transients in synth or instrument signals, etc. The optional stereo side will trigger the module's functions in unison on both channels, creating true stereo compression.
- **Max Blocks:** `8`
- **Avg DSP:** `3%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`attack ctrl`** – `toggles presence of attack control. if not selected, attack is 5.0 ms`
  - **`release ctrl`** – `toggles presence of release control. if not selected, release is 1.05 s`
  - **`ratio ctrl`** – `toggles presence of ratio control. if not selected, ratio is 10.5:1`
  - **`channels`** – `select if you'd like 1 channel of compression or 2. note that in 2 channel mode, both channels trigger the attack and release in parallel, giving the same compression curve to both sides`
  - **`sidechain`** – `select if you'd like the compressor to engage based on the signal dynamic at it's input or from another audio signal`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `attack ctrl`
  - **Block `2*` – `audio inR`**
    - **Knob:** `no modifier`
    - **Description:** `connect second channel of audio input`
    - **Option:** `release ctrl`
  - **Block `3` – `threshold`**
    - **Knob:** `level in dB`
    - **Description:** `input level at which compressor engages`
    - **Option:** `ratio ctrl`
  - **Block `4*` – `attack`**
    - **Knob:** `time in ms`
    - **Description:** `time in which compressor reacts to incoming signal`
    - **Option:** `channels`
  - **Block `5*` – `release`**
    - **Knob:** `time in s`
    - **Description:** `time in which compressor returns to its initial level once signal falls below threshold`
    - **Option:** `sidechain`
  - **Block `6*` – `ratio`**
    - **Knob:** `ratio in X:1`
    - **Description:** `determines how aggressive the gain reduction is`
  - **Block `7*` – `sidechain in`**
    - **Knob:** `no modifier`
    - **Description:** `connect an audio input from which to receive dynamic information`
  - **Block `8` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio compressed from input`
  - **Block `9*` – `audio outR`**
    - **Knob:** `no modifier`
    - **Description:** `connects audio compressed from input R`

### Gate
A standard in studio audio tools, gate can also be used as the key ingredient in gated fuzz tones. Use it to filter out noise from an audio source, or to cut the end off of a reverb's decay, thus creating the classic gated reverb sound. Make sure to experiment with the sidechain input!
- **Max Blocks:** `8`
- **Avg DSP:** `3%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`attack ctrl`** – `toggles presence of attack control. if not selected, attack is 50.5 ms`
  - **`release ctrl`** – `toggles presence of release control. if not selected, release is 1.03 s`
  - **`channels`** – `select if you'd like mono, mono to stereo, or stereo channels`
  - **`sidechain`** – `select if you'd like the gate to open based on the signal dynamic at it's input or from another audio signal`
- **Parameters:**
  - **Block `1` – `audio inL`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `attack ctrl`
  - **Block `2*` – `audio inR`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `release ctrl`
  - **Block `3` – `threshold`**
    - **Knob:** `level in dB`
    - **Description:** `sets the level at which the audio gate will open and close`
    - **Option:** `channels`
  - **Block `4` – `attack`**
    - **Knob:** `time in seconds`
    - **Description:** `once threshold is reached, sets the time it takes for audio gate to fully open. go from sharp and snappy to long and gentle`
    - **Option:** `sidechain`
  - **Block `5` – `release`**
    - **Knob:** `time in seconds`
    - **Description:** `once gate is fully open, sets time the time to close the gate once audio falls back below threshold`
  - **Block `6*` – `sidechain in`**
    - **Knob:** `no modifier`
    - **Description:** `modulation rate in Hz`
  - **Block `7` – `audio outL`**
    - **Knob:** `no modifier`
    - **Description:** `modulation depth as CV value`
  - **Block `8*` – `audio outR`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`

### Plate Reverb
Bask in the ebb and flow of steel molecules as they vibrate with the warm vintage vibe of so many classic recordings.
- **Max Blocks:** `8`
- **Avg DSP:** `22%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Parameters:**
  - **Block `1` – `input L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
  - **Block `2` – `input R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
  - **Block `3` – `decay time`**
    - **Knob:** `time in s`
    - **Description:** `length of time for reverberations to trail off`
  - **Block `4` – `low eq`**
    - **Knob:** `level in dB`
    - **Description:** `cuts or boosts low frequencies from wet signal`
  - **Block `5` – `high eq`**
    - **Knob:** `level in dB`
    - **Description:** `cuts or boosts high frequencies from wet signal`
  - **Block `6` – `mix`**
    - **Knob:** `value from 0 -100`
    - **Description:** `sets mix level from 0 (fully dry) to 100 (fully wet)`
  - **Block `7` – `output L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8` – `output R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Hall Reverb
It's like you're there, looking up at the pulpit, with the warm sun casting in beams of coloured light from the stained glass windows. You're in reverb heaven, now.
- **Max Blocks:** `8`
- **Avg DSP:** `22%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Parameters:**
  - **Block `1` – `input L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
  - **Block `2` – `input R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
  - **Block `3` – `decay time`**
    - **Knob:** `time in s`
    - **Description:** `length of time for reverberations to trail off`
  - **Block `4` – `low eq`**
    - **Knob:** `level in dB`
    - **Description:** `cuts or boosts low frequencies from wet signal`
  - **Block `5` – `high eq (lpf freq)`**
    - **Knob:** `frequency in Hz`
    - **Description:** `select cutoff point of high frequencies from wet signal`
  - **Block `6` – `mix`**
    - **Knob:** `value from 0 -100`
    - **Description:** `sets mix level from 0 (fully dry) to 100 (fully wet)`
  - **Block `7` – `output L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8` – `output R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Room Reverb
Well, you're cooped up in your little room. But that's okay, because you've got some tasty room reverb to swim around in. Don't worry, somebody will come get you out someday.
- **Max Blocks:** `8`
- **Avg DSP:** `22%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Parameters:**
  - **Block `1` – `input L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
  - **Block `2` – `input R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
  - **Block `3` – `decay time`**
    - **Knob:** `time in s`
    - **Description:** `length of time for reverberations to trail off`
  - **Block `4` – `low eq`**
    - **Knob:** `level in dB`
    - **Description:** `cuts or boosts low frequencies from wet signal`
  - **Block `5` – `high eq (lpf freq)`**
    - **Knob:** `frequency in Hz`
    - **Description:** `select cutoff point of high frequencies from wet signal`
  - **Block `6` – `mix`**
    - **Knob:** `value from 0 -100`
    - **Description:** `sets mix level from 0 (fully dry) to 100 (fully wet)`
  - **Block `7` – `output L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8` – `output R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Ghostverb
A spooky, ghostly reverb sound akin to the Ghost mode found in the Empress Reverb. Scare the crap out of all your friends!
- **Max Blocks:** `8`
- **Avg DSP:** `45%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like mono, mono to stereo, or stereo channels`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
  - **Block `3` – `decay/feedback`**
    - **Knob:** `value in CV`
    - **Description:** `sets overall length of reverb tails`
  - **Block `4` – `rate`**
    - **Knob:** `rate in Hz`
    - **Description:** `sets rate of ghostly modulation`
  - **Block `5` – `resonance`**
    - **Knob:** `value in CV`
    - **Description:** `sets the resonance of ghostly modulation`
  - **Block `6` – `mix`**
    - **Knob:** `value in CV`
    - **Description:** `sets mix level from 0 (fully dry) to 100 (fully wet)`
  - **Block `7` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8*` – `audio out2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Reverb Lite
A straightforward CPU friendly reverb sound to add some smoosh to heavier workload patches.
- **Max Blocks:** `6`
- **Avg DSP:** `10%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select if you'd like mono, mono to stereo, or stereo channels`
- **Parameters:**
  - **Block `1` – `input L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `input R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
  - **Block `3` – `decay time`**
    - **Knob:** `time in s`
    - **Description:** `sets overall length of reverb tails`
  - **Block `4` – `mix`**
    - **Knob:** `value in CV`
    - **Description:** `sets mix level from 0 (fully dry) to 100 (fully wet)`
  - **Block `5` – `output L`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `6*` – `output R`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Phaser
Set to stun, Phaser shifts the phase over a set quantity of stages and sweeps the frequency of these poles at a set rate. An optional stereo channel rounds out the list of features.
- **Max Blocks:** `8`
- **Avg DSP:** `15%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select phaser audio path between mono, mono into stereo, or stereo`
  - **`control`** – `select control method over phaser. rate is the typical phaser pedal behaviour with an internal LFO, tap tempo allows you to connect a CV input to tap a tempo into the internal LFO, and CV direct will allow you to connect an external CV source to augment the phase directly. very cool!`
  - **`number of stages`** – `select number of phasing stages. the fewer the stages, the more subtle and classic the phasing. more stages will result in a lusher effect`
- **Parameters:**
  - **Block `1` – `input left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `input right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `control`
  - **Block `3` – `control in`**
    - **Knob:** `rate in Hz, bpm, or ms (click knob to cycle views)`
    - **Description:** `depending on how you set the control mode: dial in a rate, tap in a tempo, or connect a CV source`
    - **Option:** `number of stages`
  - **Block `4` – `resonance`**
    - **Knob:** `level in dB`
    - **Description:** `phased signal can be fed back into input for resonance. dial this in from none all the way to self oscillation`
  - **Block `5` – `width`**
    - **Knob:** `level in CV`
    - **Description:** `determines the width of the phased effect`
  - **Block `6` – `mix`**
    - **Knob:** `percentage in CV`
    - **Description:** `mix controls the level of uneffected signal to phased signal. go from fully dry to fully wet`
  - **Block `7` – `output left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8*` – `output right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Chorus
The classic chorus effect. A nice sounding, fairly standard chorus. Get wackier sounds from it by using CV direct, or build your own from LFOs and delay lines!
- **Max Blocks:** `8`
- **Avg DSP:** `13%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select chorus audio path between mono, mono into stereo, or stereo`
  - **`control`** – `select control method over chorus. rate is the typical chorus pedal behaviour with an internal LFO, tap tempo allows you to connect a CV input to tap a tempo into the internal LFO, and CV direct will allow you to connect an external CV source to augment the modulation directly. tubular!`
  - **`type`** – `*work in progress*`
- **Parameters:**
  - **Block `1` – `input left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `input right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `control`
  - **Block `3` – `control in`**
    - **Knob:** `rate in Hz, bpm, or ms (click knob to cycle views)`
    - **Description:** `depending on how you set the control mode: dial in a rate, tap in a tempo, or connect a CV source`
    - **Option:** `type`
  - **Block `4` – `width`**
    - **Knob:** `level in CV`
    - **Description:** `sets width of modulation`
  - **Block `5` – `tone tilt eq`**
    - **Knob:** `eq tilt in dB`
    - **Description:** `a subtle tone control on the wet signal. from flat, negative values dial out high end and add warmth, while positive values cut bass and add highs`
  - **Block `6` – `mix`**
    - **Knob:** `percentage in CV`
    - **Description:** `mix controls the level of uneffected signal to modulated signal. go from fully dry to fully wet`
  - **Block `7` – `output left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8*` – `output right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Vibrato
Vibrato is your typical pitch bending, wet only sound you'd find on such classic units as the Empress Nebulus, just to name one. Get bendy!
- **Max Blocks:** `6`
- **Avg DSP:** `5%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select vibrato audio path between mono, mono into stereo, or stereo`
  - **`control`** – `select control method over vibrato. rate is the typical vibrato pedal behaviour with an internal LFO, tap tempo allows you to connect a CV input to tap a tempo into the internal LFO, and CV direct will allow you to connect an external CV source to augment the modulation directly. tubular!`
  - **`waveform`** – `select waveform of vibrato pitch: sine, triangle, swung sine, or swung`
- **Parameters:**
  - **Block `1` – `input left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `input right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `control`
  - **Block `3` – `control in`**
    - **Knob:** `rate in Hz, bpm, or ms (click knob to cycle views)`
    - **Description:** `depending on how you set the control mode: dial in a rate, tap in a tempo, or connect a CV source`
    - **Option:** `waveform`
  - **Block `4` – `width`**
    - **Knob:** `level in CV`
    - **Description:** `sets width of vibrato effect`
  - **Block `5` – `output left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `6*` – `output right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Flanger
ZOIA's Flanger module is borrowed right from the Empress Nebulus. This quite versatile flanger encompasses lots of comb filtering territory, but don't hesitate to build flange tones yourself using LFOs and delay lines!
- **Max Blocks:** `9`
- **Avg DSP:** `11%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select vibrato audio path between mono, mono into stereo, or stereo`
  - **`control`** – `select control method over flanger. rate is the typical flanger pedal behaviour with an internal LFO, tap tempo allows you to connect a CV input to tap a tempo into the internal LFO, and CV direct will allow you to connect an external CV source to augment the modulation directly. far out!`
  - **`type`** – `select between three different flavours of flanger: 1960s, 1970s, and thru-0`
- **Parameters:**
  - **Block `1` – `input left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `input right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input (optional)`
    - **Option:** `control`
  - **Block `3` – `control in`**
    - **Knob:** `rate in Hz, bpm, or ms (click knob to cycle views)`
    - **Description:** `depending on how you set the control mode: dial in a rate, tap in a tempo, or connect a CV source`
    - **Option:** `type`
  - **Block `4` – `regeneration`**
    - **Knob:** `level in dB`
    - **Description:** `sends some modulated effect back to the beginning of the flanger for added mojo. dial in a subtle shimmer all the way up to some mega self oscillating weirdness`
  - **Block `5` – `width`**
    - **Knob:** `level in CV`
    - **Description:** `sets width of flanger effect`
  - **Block `6` – `tone tilt eq`**
    - **Knob:** `level in dB`
    - **Description:** `a subtle tone control on the wet signal. from flat, negative values dial out high end and add warmth, while positive values cut bass and add highs`
  - **Block `7` – `mix`**
    - **Knob:** `percentage in CV`
    - **Description:** `mix controls the level of uneffected signal to modulated signal. go from fully dry to fully wet`
  - **Block `8` – `output left`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `9*` – `output right`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Tremolo
Up and down, side to side. Tremolo helps your smile get wide. Set speed and depth and tap in a tempo if you like. If you'd like a tremolo effect with more control, try creating one using the VCA or Audio Panner along with LFOs and various other CV tools to get radical!
- **Max Blocks:** `6`
- **Avg DSP:** `2%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select vibrato audio path between mono, mono into stereo, or stereo`
  - **`control`** – `select control method over tremolo. rate is the typical tremolo pedal behaviour with an internal LFO, tap tempo allows you to connect a CV input to tap a tempo into the internal LFO, and CV direct will allow you to connect an external CV source to augment the tremolo directly. groovy!`
  - **`waveform`** – `select flavour of tremolo effect: fender'ish, vox'ish, triangle, sine, or square`
- **Parameters:**
  - **Block `1` – `audio inL`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio inR`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `control`
  - **Block `3` – `control in`**
    - **Knob:** `rate in Hz, bpm, or ms (click knob to cycle views)`
    - **Description:** `depending on how you set the control mode: dial in a rate, tap in a tempo, or connect a CV source`
    - **Option:** `waveform`
  - **Block `4` – `depth`**
    - **Knob:** `level in CV`
    - **Description:** `depth of tremolo effect. go from subtle dips to complete silence during dips`
  - **Block `5` – `audio outL`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `6*` – `audio outR`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Env Filter
Get your quack on! This fully featured envelope filter has everything you need to tune in that perfect envelope filter and get funky. Great on guitar, bass, or anything else!
- **Max Blocks:** `8`
- **Avg DSP:** `7%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select filter audio path between mono, mono into stereo, or stereo`
  - **`filter type`** – `select filter type: high pass filter, low pass filter, or band pass filter`
  - **`direction`** – `select direction of filter sweep: up or down`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `filter type`
  - **Block `3` – `sensitivity`**
    - **Knob:** `level in CV`
    - **Description:** `determines the sensitivity of the envelope to incoming audio levels`
    - **Option:** `direction`
  - **Block `4` – `min freq`**
    - **Knob:** `frequency in Hz`
    - **Description:** `determines the downward cutoff frequency of the envelope filter`
  - **Block `5` – `max freq`**
    - **Knob:** `frequency in Hz`
    - **Description:** `determines the upward cutoff frequency of the filter`
  - **Block `6` – `filter Q`**
    - **Knob:** `level in CV`
    - **Description:** `determines the width of the filter notch`
  - **Block `7` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `8*` – `audio out2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

### Ring Modulator
A gnarly ring modulation effect. A robot's nightmare, a tweaker's delight!
- **Max Blocks:** `5`
- **Avg DSP:** `14%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`waveform`** – `select waveform of generated carrier wave: sine, square, triangle, or sawtooth`
  - **`ext audio in`** – `toggles parameter #2 to act as a tone generator or as a sidechain input`
  - **`duty cycle`** – `toggles presence of duty cycle parameter`
  - **`upsampling`** – `allows waveform to be generated at 2X sampling rate for better quality (higher CPU)`
- **Parameters:**
  - **Block `1` – `audio in`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `waveform`
  - **Block `2` – `frequency or ext in`**
    - **Knob:** `frequency in Hz, or no modifier`
    - **Description:** `this jack will either generate a carrier frequency to modulate the input signal against, or bring in a second audio source to act as the carrier wave. when "ext audio in" is off, CV inputs from -1 to 0 cover the frequency range 0.03-27.5 Hz, CV inputs from 0 to 1 cover the frequency range 27.5-23999Hz`
    - **Option:** `ext audio in`
  - **Block `3*` – `duty cycle`**
    - **Knob:** `value in %`
    - **Description:** `adjusts the pulse width of the ring modulation`
    - **Option:** `duty cycle`
  - **Block `4` – `mix`**
    - **Knob:** `percentage in CV`
    - **Description:** `mix controls the level of uneffected signal to modulated signal. go from fully dry to fully wet`
    - **Option:** `upsampling`
  - **Block `5` – `audio out`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`

### Cabinet Sim
A versatile guitar cabinet simulator
- **Max Blocks:** `4`
- **Avg DSP:** `10%`
- **Connections:** `inputs, audio effect outputs, VCAs, oscillators,`
- **Options:**
  - **`channels`** – `select audio path between mono, mono into stereo, or stereo`
  - **`type`** – `select cabinet type: 4x12 full, 2x12 dark, 2x12 modern, 1x12, 1x8 lofi, 1x12 vintage, or 4x12 hifi`
- **Parameters:**
  - **Block `1` – `audio in1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio input`
    - **Option:** `channels`
  - **Block `2*` – `audio in2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio input`
    - **Option:** `type`
  - **Block `3` – `audio out1`**
    - **Knob:** `no modifier`
    - **Description:** `connect audio output`
  - **Block `4*` – `audio out2`**
    - **Knob:** `no modifier`
    - **Description:** `connect second audio output`

---

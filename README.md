# Acoustic Levitation Experiments (COMP0031)

This repository contains the code for acoustic levitation experiments conducted as part of the COMP0031 module.

## Experiment Scripts

### amplitude_control.py
This script is used for:
- Determining minimum atomisation threshold
- Analyzing droplet shape evolution over time
- Determining the lowest amplitude to levitate particles

### droplet_stability.py
This script focuses on:
- Evaluating droplet velocity and stability across different concentrations

## Running the Experiments

To execute the code:
1. Ensure all `acoustools` dependencies are installed.
2. Connect the acoustic levitator to your device via USB.
3. Run your desired experiment script from the repository's root directory:

```bash
python amplitude_control.py
```
or

```bash
python droplet_stability.py
```

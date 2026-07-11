# MATLAB processing module

The MATLAB component provides a lightweight signal-processing workflow for transforming sensor streams into meaningful features for gesture-based experiments.

## Included files

- [process_gesture.m](process_gesture.m): example script for preprocessing and feature extraction.

## Requirements

- MATLAB with the Signal Processing Toolbox.
- Optional: Simulink runtime if you plan to extend the workflow into a full model-based pipeline.

## Usage

1. Open [process_gesture.m](process_gesture.m) in MATLAB.
2. Run the script to inspect the preprocessing flow.
3. Adjust the communication settings if you are streaming live data from the ESP32 hardware.

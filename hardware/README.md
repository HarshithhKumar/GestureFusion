# Hardware module

This folder contains the embedded side of the GestureFusion prototype. The ESP32 firmware is intended to collect motion data from an IMU or accelerometer and stream it to a host device for preprocessing and model inference.

## What is included

- [esp32_main.ino](esp32_main.ino): Arduino sketch for reading sensor values and transmitting them over a network connection.
- Wiring guidance: connect the sensor to the ESP32 I2C pins and ensure the devices share a common ground.

## Setup notes

1. Open the firmware in the Arduino IDE.
2. Select the correct ESP32 board and COM port.
3. Update the target IP address and port values before running the sketch.

## Intended workflow

The hardware layer feeds raw motion streams into the MATLAB or Python pipeline for feature extraction and gesture classification.

# GestureFusion

A compact end-to-end gesture-interaction prototype combining ESP32 sensing, MATLAB signal processing, and a Python machine-learning pipeline for gesture classification and visualization.

[Repository](https://github.com/HarshithhKumar/GestureFusion) · Topics: gesture-recognition · embedded-music · esp32 · signal-processing · machine-learning

## Project overview

This repository brings together three layers of the system:

- Embedded sensing: ESP32 firmware for collecting accelerometer and motion data.
- Signal processing: MATLAB-based preprocessing and feature extraction.
- Machine learning: Python training pipeline for gesture classification and model evaluation.

## Why this project stands out

- End-to-end prototype spanning hardware, software, and analytics.
- Reproducible Python training workflow with saved model artifacts.
- Clean package structure suitable for demo presentations and resumes.
- Extensible for future work in real-time inference, audio synthesis, or interactive dashboards.

## Repository structure

- [hardware/](hardware/): ESP32 firmware and hardware notes.
- [matlab/](matlab/): MATLAB processing and feature-extraction scripts.
- [src/gesturefusion/](src/gesturefusion/): Python package for data utilities and experiment helpers.
- [notebooks/](notebooks/): Interactive demo notebook.
- [dashboard/](dashboard/): Static visualization page for sensor data.
- [assets/](assets/): Project assets and illustrations.

## Quick start

### 1. Clone and install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the training pipeline

```bash
python train.py
```

This creates a simple model artifact and metrics report in the [artifacts/](artifacts/) folder.

### 3. Run the tests

```bash
pytest -q
```

### 4. Explore the demo materials

- Open [dashboard/index.html](dashboard/index.html) for a lightweight visualization.
- Open [notebooks/GestureFusion_demo.ipynb](notebooks/GestureFusion_demo.ipynb) for a notebook walkthrough.

## Machine learning workflow

The current training pipeline uses a **synthetic gesture dataset only**. Its reported metrics are useful for testing the workflow, but do not demonstrate real-world gesture-recognition accuracy. The workflow:

1. Generate a synthetic dataset.
2. Split into train and test sets.
3. Train a Random Forest classifier.
4. Save model weights and metrics.

## Future enhancements

Potential next steps for making the project even more impressive include:

- A sample results section with charts and confusion matrices.
- A polished logo or hero section in the README.
- A live dashboard for real-time visualization.

## License

This project is intended for educational and demonstration purposes.

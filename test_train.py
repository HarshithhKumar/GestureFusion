import json
from pathlib import Path

import numpy as np

from train import build_synthetic_dataset, train_model


def test_build_synthetic_dataset_shape_and_labels():
    X, y = build_synthetic_dataset(n_samples=80, n_features=6, n_classes=3)

    assert X.shape == (80, 6)
    assert y.shape == (80,)
    assert set(np.unique(y)).issubset({0, 1, 2})


def test_train_model_writes_artifacts(tmp_path):
    X, y = build_synthetic_dataset(n_samples=120, n_features=6, n_classes=3)

    report = train_model(X, y, output_dir=tmp_path)

    assert report["model_type"] == "RandomForestClassifier"
    assert 0.0 <= report["accuracy"] <= 1.0
    assert (tmp_path / "model.joblib").exists()
    assert (tmp_path / "metrics.json").exists()

    metrics = json.loads((tmp_path / "metrics.json").read_text(encoding="utf-8"))
    assert metrics["accuracy"] == report["accuracy"]

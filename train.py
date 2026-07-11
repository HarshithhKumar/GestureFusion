"""Training pipeline for GestureFusion gesture classification demos."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def build_synthetic_dataset(
    n_samples: int = 200,
    n_features: int = 6,
    n_classes: int = 3,
) -> Tuple[np.ndarray, np.ndarray]:
    """Create a simple synthetic gesture dataset for training demos."""
    rng = np.random.default_rng(42)
    X = rng.normal(loc=0.0, scale=1.0, size=(n_samples, n_features))
    labels = rng.integers(0, n_classes, size=n_samples)

    for cls_idx in range(n_classes):
        X[labels == cls_idx, 0] += cls_idx * 0.8
        X[labels == cls_idx, 1] += cls_idx * 0.5
        X[labels == cls_idx, 2] += cls_idx * 0.2

    return X, labels


def train_model(
    X: np.ndarray,
    y: np.ndarray,
    output_dir: str | Path | None = None,
) -> Dict[str, float | str]:
    """Train a lightweight classifier and save artifacts to disk."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=120,
        max_depth=6,
        random_state=42,
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = float(accuracy_score(y_test, predictions))

    artifact_dir = Path(output_dir or "artifacts")
    artifact_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, artifact_dir / "model.joblib")
    metrics = {"accuracy": accuracy, "n_samples": int(len(y)), "model_type": "RandomForestClassifier"}
    (artifact_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    return metrics


if __name__ == "__main__":
    X, y = build_synthetic_dataset()
    report = train_model(X, y, output_dir="artifacts")
    print(json.dumps(report, indent=2))

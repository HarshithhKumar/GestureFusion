"""Utility helpers for GestureFusion demos and experiments."""

import numpy as np
import pandas as pd


def load_sample_data(path=None):
    """Return a synthetic DataFrame of sensor readings.

    If ``path`` is provided and exists, the function will load it with
    :func:`pandas.read_csv`. Otherwise, a compact synthetic dataset is generated
    for demonstrations and local testing.
    """
    if path is not None:
        try:
            return pd.read_csv(path)
        except Exception:
            pass

    t = np.linspace(0, 2 * np.pi, 120)
    df = pd.DataFrame(
        {
            "time": t,
            "acc_x": np.sin(t) + 0.1 * np.random.randn(len(t)),
            "acc_y": np.cos(t) + 0.1 * np.random.randn(len(t)),
            "gesture_label": np.tile([0, 1, 2], len(t) // 3 + 1)[: len(t)],
        }
    )
    return df


if __name__ == "__main__":
    df = load_sample_data()
    print(df.head())

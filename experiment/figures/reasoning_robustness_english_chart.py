from __future__ import annotations

import os
import sys
from pathlib import Path

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
if str(EXPERIMENT_ROOT) not in sys.path:
    sys.path.insert(0, str(EXPERIMENT_ROOT))

OUT_DIR = EXPERIMENT_ROOT / "result" / "figures"
AVG_XLSX_PATH = EXPERIMENT_ROOT / "result" / "process" / "average_accuracy.xlsx"
WC_XLSX_PATH = EXPERIMENT_ROOT / "result" / "process" / "worst_case_accuracy.xlsx"
os.environ.setdefault("MPLCONFIGDIR", str(EXPERIMENT_ROOT / ".mplconfig"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

from tables.latex_table_creator import (
    EXCLUDED_MODELS,
    MODEL_DISPLAY_NAMES,
)


BG = "#ffffff"
SURFACE = "#ffffff"
BORDER = "#d9d9d9"
TEXT = "#111111"
MUTED = "#444444"
ACCENT = "#7da61a"
ACCENT_DARK = "#adc95a"

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": BORDER,
        "axes.labelcolor": MUTED,
        "axes.titlecolor": TEXT,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "text.color": TEXT,
        "font.family": "monospace",
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlepad": 12,
    }
)


def pct_fmt(x, _):
    return f"{x:.0f}%"


PCT_FORMATTER = FuncFormatter(pct_fmt)


def display_model_name(model_key: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_key, model_key.replace("_", "-"))


def load_metric_pivot(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing metric file: {path}"
        )
    pivot = pd.read_excel(path, header=[0, 1], index_col=0)
    pivot.index = pivot.index.astype(str)
    pivot = pivot.loc[~pivot.index.isin(EXCLUDED_MODELS)]
    return pivot


def build_english_rr_summary(avg_pivot: pd.DataFrame, wc_pivot: pd.DataFrame) -> pd.DataFrame:
    english_avg = avg_pivot.xs("English", level=1, axis=1, drop_level=True)
    english_wc = wc_pivot.xs("English", level=1, axis=1, drop_level=True)
    rr = (english_wc / english_avg).replace([float("inf"), float("-inf")], pd.NA)
    rr = rr.fillna(0)

    summary = rr.mean(axis=1).rename("ReasoningRobustness").reset_index()
    summary = summary.rename(columns={"index": "Model"})
    summary["DisplayModel"] = summary["Model"].map(display_model_name)
    summary = summary.sort_values("ReasoningRobustness", ascending=False).reset_index(drop=True)
    return summary


def plot_english_rr(summary: pd.DataFrame, out_path: Path) -> None:
    labels = summary["DisplayModel"].tolist()
    values = (summary["ReasoningRobustness"] * 100).to_numpy(dtype=float)
    x = np.arange(len(labels))

    fig_w = max(10.5, 0.52 * len(labels) + 2.0)
    fig, ax = plt.subplots(figsize=(fig_w, 5.2), facecolor=BG)

    colors = [ACCENT if i < 3 else ACCENT_DARK for i in range(len(labels))]
    bars = ax.bar(x, values, color=colors, edgecolor="none", width=0.72, zorder=3)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylim(0, max(100, float(values.max()) + 8))
    ax.yaxis.set_major_formatter(PCT_FORMATTER)
    ax.set_ylabel("Reasoning robustness (%)")
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.8, zorder=0)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1.0,
            f"{value:.1f}%",
            va="bottom",
            ha="center",
            fontsize=9,
            color=TEXT,
        )

    fig.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    avg_pivot = load_metric_pivot(AVG_XLSX_PATH)
    wc_pivot = load_metric_pivot(WC_XLSX_PATH)
    summary = build_english_rr_summary(avg_pivot, wc_pivot)
    out_path = OUT_DIR / "english_reasoning_robustness_barchart.png"
    plot_english_rr(summary, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()

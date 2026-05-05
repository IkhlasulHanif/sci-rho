from __future__ import annotations

import os
import sys
from pathlib import Path

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
if str(EXPERIMENT_ROOT) not in sys.path:
    sys.path.insert(0, str(EXPERIMENT_ROOT))

OUT_DIR = EXPERIMENT_ROOT / "result" / "figures"
AVG_XLSX_PATH = EXPERIMENT_ROOT / "result" / "process" / "average_accuracy.xlsx"
os.environ.setdefault("MPLCONFIGDIR", str(EXPERIMENT_ROOT / ".mplconfig"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

from tables.latex_table_creator import EXCLUDED_MODELS, MODEL_DISPLAY_NAMES, MODEL_GROUPS


BG = "#ffffff"
SURFACE = "#ffffff"
BORDER = "#d9d9d9"
TEXT = "#111111"
MUTED = "#444444"

LANG_COLORS = {
    "Arabic": "#b87333",
    "Chinese": "#4e79a7",
    "Hindi": "#f28e2b",
    "Indonesian": "#59a14f",
    "Kazakh": "#e15759",
    "Swahili": "#af7aa1",
}

LANGS = ["Arabic", "Chinese", "Hindi", "Indonesian", "Kazakh", "Swahili"]

MODEL_ORDER = (
    MODEL_GROUPS["closed_source"]
    + [
        "qwen_qwen3_5-122b-a10b",
        "meta-llama_llama-4-scout",
        "OpenGVLab_InternVL3_5-14B",
        "google_gemma-3-12b-it",
        "Qwen_Qwen3-VL-8B-Instruct",
        "aisingapore_Qwen-SEA-LION-v4-8B-VL",
        "allenai_Molmo2-8B",
        "OpenGVLab_InternVL3_5-8B",
        "Qwen_Qwen3-VL-4B-Instruct",
        "aisingapore_Qwen-SEA-LION-v4-4B-VL",
        "allenai_Molmo2-4B",
        "google_gemma-3-4b-it",
        "OpenGVLab_InternVL3_5-4B",
    ]
)

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
        "font.size": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlepad": 12,
    }
)


def pct_fmt(x, _):
    return f"{x:+.0f}%"


PCT_FORMATTER = FuncFormatter(pct_fmt)


def display_model_name(model_key: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_key, model_key.replace("_", "-"))


def load_metric_pivot(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing metric file: {path}")
    pivot = pd.read_excel(path, header=[0, 1], index_col=0)
    pivot.index = pivot.index.astype(str)
    pivot = pivot.loc[~pivot.index.isin(EXCLUDED_MODELS)]
    return pivot


def build_delta_table(avg_pivot: pd.DataFrame) -> pd.DataFrame:
    lang_means = avg_pivot.T.groupby(level=1).mean().T
    english = lang_means["English"]
    delta = pd.DataFrame(index=lang_means.index)
    for lang in LANGS:
        if lang in lang_means.columns:
            delta[lang] = lang_means[lang] - english

    order_rank = {model: idx for idx, model in enumerate(MODEL_ORDER)}
    delta["order_rank"] = delta.index.map(lambda model: order_rank.get(model, len(order_rank)))
    delta = delta.sort_values(["order_rank"]).drop(columns=["order_rank"])
    delta["DisplayModel"] = delta.index.map(display_model_name)
    return delta.reset_index(names="Model")


def plot_delta_table(delta_df: pd.DataFrame, out_path: Path) -> None:
    labels = delta_df["DisplayModel"].tolist()
    x = np.arange(len(labels))
    n_langs = len(LANGS)
    width = 0.12

    fig_w = max(12.0, 0.7 * len(labels) + 4.0)
    fig, ax = plt.subplots(figsize=(fig_w, 4.6), facecolor=BG)

    all_values: list[float] = []
    for i, lang in enumerate(LANGS):
        vals = (delta_df[lang].to_numpy(dtype=float) * 100)
        all_values.extend(vals.tolist())
        offset = (i - (n_langs - 1) / 2) * width
        ax.bar(
            x + offset,
            vals,
            width=width * 0.92,
            color=LANG_COLORS[lang],
            edgecolor="none",
            label=lang,
            zorder=3,
        )

    ymin = min(all_values) if all_values else -1
    ymax = max(all_values) if all_values else 1
    pad = 2.5
    ax.axhline(0, color="#777777", linewidth=1.1, zorder=2)
    ax.set_ylim(ymin - pad, ymax + pad)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=11)
    ax.yaxis.set_major_formatter(PCT_FORMATTER)
    ax.set_ylabel("Delta vs English avg accuracy", fontsize=13)
    ax.grid(axis="y", color=BORDER, linewidth=0.8, alpha=0.8, zorder=0)
    ax.tick_params(axis="y", labelsize=11)
    ax.legend(frameon=False, ncol=3, fontsize=10, loc="upper right", bbox_to_anchor=(1.0, 1.08))

    fig.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    avg_pivot = load_metric_pivot(AVG_XLSX_PATH)
    delta_df = build_delta_table(avg_pivot)
    out_path = OUT_DIR / "english_delta_by_model_barchart.png"
    plot_delta_table(delta_df, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()

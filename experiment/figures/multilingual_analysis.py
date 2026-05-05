"""
Multilingual STEM Accuracy — Model Benchmark Analysis
Reproduces the benchmark charts using matplotlib.

Run:
    python multilingual_analysis.py

Outputs:
    multilingual_analysis.png
    multilingual_analysis_hires.png
"""

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
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import FuncFormatter
from tables.latex_table_creator import MODEL_DISPLAY_NAMES


LANGS = ["Arabic", "Chinese", "English", "Hindi", "Indonesian", "Kazakh", "Swahili"]
SUBJECTS = ["Biology", "Chemistry", "CS", "Math", "Physics"]

SUBJECT_KEY_MAP = {
    "Biology": "Biology",
    "Chemistry": "Chemistry",
    "CS": "Compsci",
    "Math": "Mathematics",
    "Physics": "Physics",
}


BG = "#0d0d0f"
SURFACE = "#141417"
BORDER = "#2a2a2f"
TEXT = "#e8e6e0"
MUTED = "#7a7872"
ACCENT = "#c8f060"
RED = "#f06060"
BLUE = "#60c8f0"
GOLD = "#f0c060"

MODEL_COLORS = ["#888780", "#b4b2a9", "#1D9E75", "#60c8f0", "#7F77DD", "#c8f060"]

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

CMAP = LinearSegmentedColormap.from_list(
    "bench",
    [
        (0.00, "#1e0c0c"),
        (0.15, "#3c1414"),
        (0.35, "#50320f"),
        (0.55, "#324b14"),
        (0.75, "#1e641e"),
        (1.00, "#b4f050"),
    ],
)


def load_metric_pivot(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing metric file: {path}. Run experiment/analyzer.ipynb once first."
        )
    return pd.read_excel(path, header=[0, 1], index_col=0)


def display_model_name(model_key: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_key, model_key.replace("_", "-"))


def short_model_name(display_name: str) -> str:
    short = display_name
    replacements = {
        "InternVL3.5-": "VL3.5-",
        "Gemini-2.5-": "Gm-2.5-",
        "Gemma-3-": "Gemma-",
        "Qwen3-VL-": "Q3VL-",
        "Qwen3.5-": "Q3.5-",
        "SEA-LION-v4-": "SEA-",
        "Llama-4-": "L4-",
        "Molmo2-": "Molmo-",
    }
    for old, new in replacements.items():
        short = short.replace(old, new)
    return short


def pick_model_order(avg_pivot: pd.DataFrame) -> list[str]:
    model_scores = avg_pivot.mean(axis=1).sort_values(ascending=False)
    return model_scores.index.tolist()


def build_metric_tables(
    avg_pivot: pd.DataFrame,
    wc_pivot: pd.DataFrame,
    model_keys: list[str],
) -> tuple[dict, dict]:
    avg_raw: dict[str, dict[str, list[float]]] = {}
    wc_raw: dict[str, dict[str, list[float]]] = {}

    for model_key in model_keys:
        if model_key not in avg_pivot.index or model_key not in wc_pivot.index:
            raise KeyError(f"Model {model_key} not found in metric pivots.")
        pretty_model = display_model_name(model_key)

        avg_raw[pretty_model] = {}
        wc_raw[pretty_model] = {}

        for lang in LANGS:
            avg_vals = []
            wc_vals = []
            for subject in SUBJECTS:
                subject_key = SUBJECT_KEY_MAP[subject]
                col_key = (subject_key, lang)
                avg_vals.append(float(avg_pivot.loc[model_key, col_key]) if col_key in avg_pivot.columns else np.nan)
                wc_vals.append(float(wc_pivot.loc[model_key, col_key]) if col_key in wc_pivot.columns else np.nan)

            avg_raw[pretty_model][lang] = avg_vals
            wc_raw[pretty_model][lang] = wc_vals

    return avg_raw, wc_raw


def mla(data: dict, model: str, lang: str) -> float:
    vals = np.array(data[model][lang], dtype=float)
    return float(np.nanmean(vals))


def lang_avg(data: dict, lang: str) -> float:
    return float(np.nanmean([mla(data, m, lang) for m in MODELS]))


def main() -> None:
    avg_pivot = load_metric_pivot(AVG_XLSX_PATH)
    wc_pivot = load_metric_pivot(WC_XLSX_PATH)
    model_keys = pick_model_order(avg_pivot)

    global MODELS, MSHORT, MODEL_COLORS
    MODELS = [display_model_name(model_key) for model_key in model_keys]
    MSHORT = [short_model_name(name) for name in MODELS]
    color_positions = np.linspace(0.05, 0.95, len(MODELS))
    MODEL_COLORS = [CMAP(pos) for pos in color_positions]

    avg_raw, wc_raw = build_metric_tables(avg_pivot, wc_pivot, model_keys)

    avg_matrix = np.array([[mla(avg_raw, m, l) for l in LANGS] for m in MODELS])
    wc_matrix = np.array([[mla(wc_raw, m, l) for l in LANGS] for m in MODELS])

    lang_avgs = np.array([lang_avg(avg_raw, l) for l in LANGS])
    lang_wcs = np.array([lang_avg(wc_raw, l) for l in LANGS])

    eng_idx = LANGS.index("English")
    penalty_matrix = avg_matrix - avg_matrix[:, eng_idx : eng_idx + 1]

    fig = plt.figure(figsize=(20, 22), facecolor=BG)
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.48, wspace=0.32, top=0.91, bottom=0.05)

    ax_bar = fig.add_subplot(gs[0, 0])
    ax_heat = fig.add_subplot(gs[0, 1])
    ax_penalty = fig.add_subplot(gs[1, :])
    ax_spread = fig.add_subplot(gs[2, 0])
    ax_tier = fig.add_subplot(gs[2, 1])

    fig.text(
        0.07,
        0.955,
        "Multilingual STEM Accuracy — Model Benchmark Analysis",
        fontsize=18,
        fontweight="bold",
        color=TEXT,
        ha="left",
        va="bottom",
    )
    fig.text(
        0.07,
        0.938,
        "6 models  ·  7 languages  ·  5 subjects  ·  average & worst-case conditions",
        fontsize=10,
        color=MUTED,
        ha="left",
        va="bottom",
    )

    x = np.arange(len(LANGS))
    width = 0.38
    bars_avg = ax_bar.bar(x - width / 2, lang_avgs * 100, width=width, color=ACCENT, alpha=0.85, label="Average")
    bars_wc = ax_bar.bar(x + width / 2, lang_wcs * 100, width=width, color=RED, alpha=0.75, label="Worst-case")
    ax_bar.set_xticks(x)
    ax_bar.set_xticklabels(LANGS, rotation=18, ha="right")
    ax_bar.set_ylim(0, 100)
    ax_bar.yaxis.set_major_formatter(PCT_FORMATTER)
    ax_bar.set_title("Average vs. Worst-Case by Language\n(all models & subjects combined)", fontsize=11)
    ax_bar.legend(frameon=False, labelcolor=TEXT, fontsize=9)
    ax_bar.grid(axis="y", zorder=0)
    for bars in (bars_avg, bars_wc):
        for bar in bars:
            h = bar.get_height()
            ax_bar.text(bar.get_x() + bar.get_width() / 2, h + 1.2, f"{h:.0f}", ha="center", va="bottom", fontsize=8)

    im = ax_heat.imshow(avg_matrix * 100, cmap=CMAP, aspect="auto", vmin=0, vmax=100)
    ax_heat.set_xticks(np.arange(len(LANGS)))
    ax_heat.set_xticklabels([l[:3].upper() for l in LANGS], fontsize=9)
    ax_heat.set_yticks(np.arange(len(MODELS)))
    ax_heat.set_yticklabels(MSHORT, fontsize=9)
    ax_heat.set_title("Average Accuracy Heatmap\n(model × language)", fontsize=11)

    for i in range(avg_matrix.shape[0]):
        for j in range(avg_matrix.shape[1]):
            v = avg_matrix[i, j] * 100
            txt_color = "#0d0d0f" if v > 40 else "#e8e6e0"
            ax_heat.text(j, i, f"{v:.0f}%", ha="center", va="center", fontsize=8.5, fontweight="bold", color=txt_color)

    cbar = fig.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.04)
    cbar.ax.yaxis.set_major_formatter(PCT_FORMATTER)
    cbar.ax.tick_params(colors=MUTED, labelsize=8)
    cbar.outline.set_edgecolor(BORDER)

    n_models = len(MODELS)
    group_w = 0.75
    bar_w = group_w / n_models
    xs = np.arange(len(LANGS))
    for i, (model, color) in enumerate(zip(MODELS, MODEL_COLORS)):
        offsets = xs + (i - n_models / 2 + 0.5) * bar_w
        vals = penalty_matrix[i] * 100
        ax_penalty.bar(offsets, vals, width=bar_w * 0.88, color=color, alpha=0.85, label=MSHORT[i], zorder=3)

    ax_penalty.axhline(0, color=BORDER, linewidth=1, zorder=2)
    ax_penalty.set_xticks(xs)
    ax_penalty.set_xticklabels(LANGS)
    ax_penalty.yaxis.set_major_formatter(FuncFormatter(lambda val, _: f"{val:+.0f}%"))
    ax_penalty.set_title(
        "Language Penalty vs. English Baseline (per model)\nnegative values = underperforms English",
        fontsize=11,
    )
    ax_penalty.legend(frameon=False, labelcolor=TEXT, fontsize=9, ncol=n_models, loc="upper right")
    ax_penalty.grid(axis="y", zorder=0)

    for i, (model, color) in enumerate(zip(MODELS, MODEL_COLORS)):
        x_vals = avg_matrix[i] * 100
        y_vals = wc_matrix[i] * 100
        ax_spread.scatter(x_vals, y_vals, color=color, s=60, alpha=0.85, zorder=3, label=MSHORT[i])
        for xv, yv in zip(x_vals, y_vals):
            ax_spread.plot([xv, xv], [yv, xv], color=color, alpha=0.2, linewidth=0.8, zorder=2)

    lim_vals = np.array([0, 100])
    ax_spread.plot(lim_vals, lim_vals, linestyle="--", color=MUTED, linewidth=1)
    ax_spread.set_xlabel("Average accuracy (%)")
    ax_spread.set_ylabel("Worst-case accuracy (%)")
    ax_spread.set_title("Average vs. Worst-Case per Data Point\n(dot = one model-language pair)", fontsize=11)
    ax_spread.legend(frameon=False, labelcolor=TEXT, fontsize=8.5, ncol=2)
    ax_spread.xaxis.set_major_formatter(PCT_FORMATTER)
    ax_spread.yaxis.set_major_formatter(PCT_FORMATTER)
    ax_spread.grid(zorder=0)
    ax_spread.set_xlim(-2, 102)
    ax_spread.set_ylim(-2, 102)

    tier_colors = {
        "English": ACCENT,
        "Chinese": ACCENT,
        "Hindi": GOLD,
        "Indonesian": GOLD,
        "Arabic": GOLD,
        "Kazakh": RED,
        "Swahili": RED,
    }
    tier_labels = {
        "English": "High",
        "Chinese": "High",
        "Hindi": "Mid",
        "Indonesian": "Mid",
        "Arabic": "Mid",
        "Kazakh": "Low",
        "Swahili": "Low",
    }

    sorted_idx = np.argsort(lang_avgs)[::-1]
    sorted_langs = [LANGS[i] for i in sorted_idx]
    sorted_vals = lang_avgs[sorted_idx] * 100
    sorted_wc = lang_wcs[sorted_idx] * 100

    y_pos = np.arange(len(LANGS))
    bars_h = ax_tier.barh(
        y_pos,
        sorted_vals,
        height=0.5,
        color=[tier_colors[l] for l in sorted_langs],
        alpha=0.85,
        zorder=3,
    )
    ax_tier.barh(
        y_pos,
        sorted_wc,
        height=0.5,
        color=[tier_colors[l] for l in sorted_langs],
        alpha=0.3,
        zorder=2,
    )
    ax_tier.set_yticks(y_pos)
    ax_tier.set_yticklabels(sorted_langs, fontsize=10)
    ax_tier.invert_yaxis()
    ax_tier.xaxis.set_major_formatter(PCT_FORMATTER)
    ax_tier.set_xlim(0, 105)
    ax_tier.set_title("Language Resource Tier Ranking\n(solid = avg · faded = worst-case)", fontsize=11)
    ax_tier.grid(axis="x", zorder=0)

    for bar, lang in zip(bars_h, sorted_langs):
        ax_tier.text(
            bar.get_width() + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{bar.get_width():.1f}%  [{tier_labels[lang]}]",
            va="center",
            fontsize=8.5,
            color=tier_colors[lang],
        )

    legend_patches = [
        mpatches.Patch(color=ACCENT, label="High-resource (English, Chinese)"),
        mpatches.Patch(color=GOLD, label="Mid-resource (Hindi, Indonesian, Arabic)"),
        mpatches.Patch(color=RED, label="Low-resource (Kazakh, Swahili)"),
    ]
    ax_tier.legend(handles=legend_patches, frameon=False, labelcolor=TEXT, fontsize=8.5, loc="lower right")

    out_png = OUT_DIR / "multilingual_analysis.png"
    out_png_hires = OUT_DIR / "multilingual_analysis_hires.png"
    plt.savefig(out_png, dpi=150, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.savefig(out_png_hires, dpi=300, bbox_inches="tight", facecolor=BG, edgecolor="none")
    print(f"Saved: {out_png.name} (150 dpi)")
    print(f"Saved: {out_png_hires.name} (300 dpi — print-ready)")


if __name__ == "__main__":
    main()

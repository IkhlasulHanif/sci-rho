import random as rnd
import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image
from physics.helper import *
from fractions import Fraction

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Phy101:
    """
    Electric current: I = Q / t
    Dynamic target: find I OR Q OR t (other two are shown in the diagram).
    """

    def __init__(self):
        self.target = rnd.choice(["I", "Q", "t"])

        self.t = rnd.randint(2, 20)  # s
        self.I = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00])  # A
        self.Q = self.I * self.t  # C

        if self.target == "I":
            self.answer = sig_figs(self.I, 3)
            blank = "I = (_) A"
        elif self.target == "Q":
            self.answer = sig_figs(self.Q, 3)
            blank = "Q = (_) C"
        else:
            self.answer = self.t
            blank = "t = (_) s"

        self.description = (
            "A steady current flows in a straight wire. Point P is a marked point on the wire.\n"
            "The values shown in the diagram relate to the charge that passes point P.\n"
            "Determine the required quantity.\n"
            f"{blank}"
        )

        self.topic = "Electricity"
        self.subtopic = "Electric current"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Electric current, }} I &= {'\\text{?}' if self.target == 'I' else sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Charge passing point P, }} Q &= {'\\text{?}' if self.target == 'Q' else sig_figs(self.Q, 3)}\\,\\text{{C}}\\\\"
            f"\\text{{Time interval, }} t &= {'\\text{?}' if self.target == 't' else self.t}\\,\\text{{s}}\\\\"
            f"\\text{{Step 1: Identify the relationship between current, charge, and time.}} &\\\\"
            f"\\text{{Electric current is defined as the rate of flow of charge:}} &\\\\"
            f"I &= \\frac{{Q}}{{t}}\\\\"
            f"\\text{{Step 2: Rearrange the formula if necessary and substitute the known values:}} &\\\\"
            + (
                f"I &= \\frac{{{sig_figs(self.Q, 3)}}}{{{self.t}}}\\\\"
                f"I &= {self.answer}\\,\\text{{A}}"
                if self.target == "I" else
                f"Q &= I \\times t\\\\"
                f"Q &= {sig_figs(self.I, 3)} \\times {self.t}\\\\"
                f"Q &= {self.answer}\\,\\text{{C}}"
                if self.target == "Q" else
                f"t &= \\frac{{Q}}{{I}} = \\frac{{{sig_figs(self.Q, 3)}}}{{{sig_figs(self.I, 3)}}}\\\\"
                f"t &= {self.answer}\\,\\text{{s}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(7.2, 2.8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wire
        y_wire = 2.0
        ax.plot([1.0, 11.0], [y_wire, y_wire], linewidth=5, color="black", solid_capstyle="round")

        # Label "wire"
        ax.text(1.0, y_wire + 0.55, "wire", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Point P
        ax.plot([6.0], [y_wire],
                marker="o", markersize=7,
                markerfacecolor="white", markeredgecolor="black", markeredgewidth=2,
                linestyle="None", zorder=10)
        ax.text(6.0, y_wire + 0.35, "P", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.10))

        y_arrow = y_wire + 0.95
        ax.annotate("", xy=(10.0, y_arrow), xytext=(2.0, y_arrow),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Labels
        if self.target == "I":
            ax.text(10.05, y_arrow, "I = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 0.70, f"Q = {sig_figs(self.Q,3)} C", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(11.0, 0.70, f"t = {self.t} s", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        elif self.target == "Q":
            ax.text(10.05, y_arrow, f"I = {sig_figs(self.I,3)} A", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 0.70, "Q = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(11.0, 0.70, f"t = {self.t} s", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        else:
            ax.text(10.05, y_arrow, f"I = {sig_figs(self.I,3)} A", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 0.70, f"Q = {sig_figs(self.Q,3)} C", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(11.0, 0.70, "t = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy102:
    """
    Electric current: charge from an I–t graph.
    For constant current: Q = I * t (area under the graph)
    Dynamic target: find Q OR I (values shown on graph/labels).
    """

    def __init__(self):
        self.target = rnd.choice(["Q", "I"])

        self.I = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00])  # A
        self.t = rnd.randint(4, 30)  # s
        self.Q = self.I * self.t  # C

        if self.target == "Q":
            self.answer = sig_figs(self.Q, 3)
        else:
            self.answer = sig_figs(self.I, 3)

        self.description = (
            "The graph shows current against time for a conductor.\n"
            "All relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Electricity"
        self.subtopic = "Electric current"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Current, }} I &= {'\\text{?}' if self.target == 'I' else sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Time, }} t &= {self.t}\\,\\text{{s}}\\\\"
            f"\\text{{Charge transferred, }} Q &= {'\\text{?}' if self.target == 'Q' else sig_figs(self.Q, 3)}\\,\\text{{C}}\\\\"
            f"\\text{{Step 1: Understand the relationship between current, time, and charge.}} &\\\\"
            f"\\text{{Electric current is the rate of flow of charge:}} &\\\\"
            f"I &= \\frac{{Q}}{{t}}\\\\"
            f"\\text{{Consequently, the charge transferred is the area under the current-time graph:}} &\\\\"
            f"Q &= I \\times t\\\\"
            f"\\text{{Step 2: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"Q &= {sig_figs(self.I, 3)} \\times {self.t}\\\\"
                f"Q &= {self.answer}\\,\\text{{C}}"
                if self.target == "Q" else
                f"I &= \\frac{{Q}}{{t}} = \\frac{{{sig_figs(self.Q, 3)}}}{{{self.t}}}\\\\"
                f"I &= {self.answer}\\,\\text{{A}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )

    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.2, 3.8))
        ax.set_xlabel("time / s", fontsize=9)
        ax.set_ylabel("current / A", fontsize=9)
        ax.tick_params(axis="both", labelsize=9)

        # Graph limits
        tmax = max(10, int(self.t * 1.25))
        ymax = max(1.0, float(self.I) * 1.35)

        ax.set_xlim(0, tmax)
        ax.set_ylim(0, ymax)
        ax.grid(True, linestyle="--", alpha=0.45)

        # Constant current region
        ax.plot([0, self.t], [self.I, self.I], linewidth=2, color="black")
        ax.plot([self.t, self.t], [0, self.I], linewidth=2, color="black")
        ax.plot([0, 0], [0, self.I], linewidth=2, color="black")

        # Light shading to indicate "area"
        ax.fill_between([0, self.t], [self.I, self.I], 0, alpha=0.10)

        # Labels
        ax.text(self.t, -0.06 * ymax, f"t = {self.t} s", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "Q":
            ax.text(0.02, 0.96, f"I = {sig_figs(self.I,3)} A", transform=ax.transAxes,
                    ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(0.98, 0.96, "Q = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(0.02, 0.96, f"Q = {sig_figs(self.Q,3)} C", transform=ax.transAxes,
                    ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(0.98, 0.96, "I = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.10)
        plt.close()


class Phy103:
    """
    Potential difference and power: P = IV
    Dynamic target: find P OR I OR V (other two are shown in the diagram).
    """

    def __init__(self):
        self.target = rnd.choice(["P", "I", "V"])

        self.V = rnd.choice([3, 4.5, 6, 9, 12, 15, 18, 24])  # V
        self.I = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])  # A
        self.P = self.V * self.I  # W

        if self.target == "P":
            self.answer = sig_figs(self.P, 3)
            blank = "P = (_) W"
        elif self.target == "I":
            self.answer = sig_figs(self.I, 3)
            blank = "I = (_) A"
        else:
            self.answer = sig_figs(self.V, 3)
            blank = "V = (_) V"

        self.description = (
            "A device is connected in a circuit. The current through the device and the potential difference across it are shown in the diagram.\n"
            "Determine the required quantity.\n"
            f"{blank}"
        )

        self.topic = "Electricity"
        self.subtopic = "Potential difference and power"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Potential difference, }} V &= {'\\text{?}' if self.target == 'V' else sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current, }} I &= {'\\text{?}' if self.target == 'I' else sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Electrical power, }} P &= {'\\text{?}' if self.target == 'P' else sig_figs(self.P, 3)}\\,\\text{{W}}\\\\"
            f"\\text{{Step 1: Identify the relationship between power, current, and potential difference.}} &\\\\"
            f"\\text{{Electrical power }} P \\text{{ is the rate at which energy is transferred:}} &\\\\"
            f"P &= I \\times V\\\\"
            f"\\text{{Step 2: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"P &= {sig_figs(self.I, 3)} \\times {sig_figs(self.V, 3)}\\\\"
                f"P &= {self.answer}\\,\\text{{W}}"
                if self.target == "P" else
                f"I &= \\frac{{P}}{{V}} = \\frac{{{sig_figs(self.P, 3)}}}{{{sig_figs(self.V, 3)}}}\\\\"
                f"I &= {self.answer}\\,\\text{{A}}"
                if self.target == "I" else
                f"V &= \\frac{{P}}{{I}} = \\frac{{{sig_figs(self.P, 3)}}}{{{sig_figs(self.I, 3)}}}\\\\"
                f"V &= {self.answer}\\,\\text{{V}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(7.2, 3.2))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        y_wire = 3.0
        xL, xR = 1.0, 11.0

        # Device block
        dev_w, dev_h = 2.2, 1.6
        x_dev = 6.0
        y_dev = y_wire - dev_h / 2
        ax.add_patch(patches.Rectangle((x_dev - dev_w/2, y_dev), dev_w, dev_h,
                                       fill=False, linewidth=2, edgecolor="black"))
        ax.text(x_dev, y_wire, "device", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Wires to device edges
        ax.plot([xL, x_dev - dev_w/2], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")
        ax.plot([x_dev + dev_w/2, xR], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")

        y_I = 5.1
        ax.annotate("", xy=(9.3, y_I), xytext=(2.7, y_I),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        if self.target == "I":
            ax.text(9.35, y_I, "I = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(9.35, y_I, f"I = {sig_figs(self.I,3)} A", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        y_V = 1.6
        x_left_dev = x_dev - dev_w/2
        x_right_dev = x_dev + dev_w/2
        ax.annotate("", xy=(x_left_dev, y_V), xytext=(x_right_dev, y_V),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        if self.target == "V":
            ax.text(x_dev, y_V - 0.25, "V = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(x_dev, y_V - 0.25, f"V = {sig_figs(self.V,3)} V", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Power label at top-right
        if self.target == "P":
            ax.text(11.0, 5.8, "P = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(11.0, 5.8, f"P = {sig_figs(self.P,3)} W", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy104:
    """
    Potential difference and energy transfer: W = QV
    Dynamic target: find W OR Q OR V (other two shown in the diagram).
    """

    def __init__(self):
        self.target = rnd.choice(["W", "Q", "V"])

        self.V = rnd.choice([3, 4.5, 6, 9, 12, 15, 18, 24])  # V
        self.Q = rnd.choice([0.50, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0])  # C
        self.W = self.Q * self.V  # J

        if self.target == "W":
            self.answer = sig_figs(self.W, 3)
            blank = "W = (_) J"
        elif self.target == "Q":
            self.answer = sig_figs(self.Q, 3)
            blank = "Q = (_) C"
        else:
            self.answer = sig_figs(self.V, 3)
            blank = "V = (_) V"

        self.description = (
            "A charge moves through a potential difference. Values are shown in the diagram.\n"
            "Determine the required quantity.\n"
            f"{blank}"
        )

        self.topic = "Electricity"
        self.subtopic = "Potential difference and power"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Potential difference, }} V &= {'\\text{?}' if self.target == 'V' else sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Charge moved, }} Q &= {'\\text{?}' if self.target == 'Q' else sig_figs(self.Q, 3)}\\,\\text{{C}}\\\\"
            f"\\text{{Energy transferred (Work), }} W &= {'\\text{?}' if self.target == 'W' else sig_figs(self.W, 3)}\\,\\text{{J}}\\\\"
            f"\\text{{Step 1: Identify the relationship between work, charge, and potential difference.}} &\\\\"
            f"\\text{{The potential difference }} V \\text{{ is defined as the work done (energy transferred) per unit charge:}} &\\\\"
            f"V &= \\frac{{W}}{{Q}}\\\\"
            f"\\text{{Rearranging this gives the energy transfer formula:}} &\\\\"
            f"W &= Q \\times V\\\\"
            f"\\text{{Step 2: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"W &= {sig_figs(self.Q, 3)} \\times {sig_figs(self.V, 3)}\\\\"
                f"W &= {self.answer}\\,\\text{{J}}"
                if self.target == "W" else
                f"Q &= \\frac{{W}}{{V}} = \\frac{{{sig_figs(self.W, 3)}}}{{{sig_figs(self.V, 3)}}}\\\\"
                f"Q &= {self.answer}\\,\\text{{C}}"
                if self.target == "Q" else
                f"V &= \\frac{{W}}{{Q}} = \\frac{{{sig_figs(self.W, 3)}}}{{{sig_figs(self.Q, 3)}}}\\\\"
                f"V &= {self.answer}\\,\\text{{V}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.8, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Two points / terminals
        ax.add_patch(patches.Circle((2.5, 2.5), 0.25, fill=False, linewidth=2, edgecolor="black"))
        ax.add_patch(patches.Circle((7.5, 2.5), 0.25, fill=False, linewidth=2, edgecolor="black"))
        ax.text(2.5, 2.95, "A", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.1))
        ax.text(7.5, 2.95, "B", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.1))

        # Arrow showing charge movement
        ax.annotate("", xy=(7.1, 2.5), xytext=(2.9, 2.5),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Labels
        if self.target == "Q":
            ax.text(5.0, 2.85, "Q = ?", ha="center", va="bottom",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(5.0, 2.85, f"Q = {sig_figs(self.Q,3)} C", ha="center", va="bottom",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Potential difference bracket
        ax.annotate("", xy=(2.5, 1.2), xytext=(7.5, 1.2),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        if self.target == "V":
            ax.text(5.0, 0.95, "V = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(5.0, 0.95, f"V = {sig_figs(self.V,3)} V", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "W":
            ax.text(9.7, 4.6, "W = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(9.7, 4.6, f"W = {sig_figs(self.W,3)} J", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy105:
    """
    Resistance and resistivity: ρ = R A / L, with A = π(d/2)^2
    Target: resistivity ρ (values shown in diagram).
    """

    def __init__(self):
        while True:
            self.L = rnd.choice([0.80, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])  # m
            self.d_mm = rnd.choice([0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])  # mm
            self.R = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0, 10.0, 12.0])  # Ω

            d = self.d_mm * 1e-3
            self.A = math.pi * (d / 2) ** 2
            self.rho = self.R * self.A / self.L

            # Keep in a plausible metal-ish range
            if 1e-9 <= self.rho <= 5e-5:
                break

        self.answer = f"{self.rho:.2e}"  # ~3 s.f. in scientific notation

        self.description = (
            "A uniform wire has the dimensions shown in the diagram and its resistance is given.\n"
            "Determine the resistivity of the wire material.\n"
            "ρ = (_) Ω m"
        )

        self.topic = "Electricity"
        self.subtopic = "Resistance and resistivity"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Resistance, }} R &= {sig_figs(self.R, 3)}\\,\\Omega\\\\"
            f"\\text{{Length, }} L &= {self.L}\\,\\text{{m}}\\\\"
            f"\\text{{Diameter, }} d &= {self.d_mm}\\,\\text{{mm}} = {self.d_mm} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            f"\\text{{Resistivity, }} \\rho &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Calculate the cross-sectional area }} A. &\\\\"
            f"\\text{{The wire is uniform with a circular cross-section:}} &\\\\"
            f"A &= \\pi \\left( \\frac{{d}}{{2}} \\right)^2\\\\"
            f"A &= \\pi \\left( \\frac{{{self.d_mm} \\times 10^{{-3}}}}{{2}} \\right)^2\\\\"
            f"A &= {round(self.A, 12)}\\,\\text{{m}}^2\\\\"
            f"\\text{{Step 2: Apply the resistivity formula.}} &\\\\"
            f"\\text{{The resistance of a conductor is given by }} R = \\frac{{\\rho L}}{{A}}. &\\\\"
            f"\\text{{Rearranging for resistivity (}} \\rho \\text{{):}} &\\\\"
            f"\\rho &= \\frac{{R A}}{{L}}\\\\"
            f"\\text{{Step 3: Substitute the known values and solve:}} &\\\\"
            f"\\rho &= \\frac{{{sig_figs(self.R, 3)} \\times {round(self.A, 12)}}}{{{self.L}}}\\\\"
            f"\\rho &= {self.rho:.3e}\\,\\Omega\\,\\text{{m}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega\\,\\text{{m}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.8, 2.8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wire
        ax.add_patch(patches.Rectangle((2.0, 1.7), 6.0, 0.6, fill=False, linewidth=2, edgecolor="black"))

        # Length bracket
        ax.annotate("", xy=(2.0, 1.0), xytext=(8.0, 1.0),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(5.0, 0.82, f"L = {self.L} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Diameter bracket
        ax.annotate("", xy=(5.0, 1.7), xytext=(5.0, 2.3),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(5.25, 2.0, f"d = {self.d_mm} mm", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(2.0, 3.5, f"R = {sig_figs(self.R,3)} Ω", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(9.7, 3.5, "ρ = ?", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy106:
    """
    Resistance and resistivity: R = ρL / A, with A = π(d/2)^2
    Target: resistance R (values shown in diagram).
    """

    def __init__(self):
        # Choose plausible resistivities (Ω m)
        self.rho = rnd.choice([1.6e-8, 2.7e-8, 4.9e-8, 1.1e-6, 1.4e-6, 2.0e-6, 3.0e-6])

        while True:
            self.L = rnd.choice([0.80, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])  # m
            self.d_mm = rnd.choice([0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])  # mm

            d = self.d_mm * 1e-3
            self.A = math.pi * (d / 2) ** 2
            self.R = self.rho * self.L / self.A

            if 0.05 <= self.R <= 200:
                break

        self.answer = sig_figs(self.R, 3)
        self.rho_disp = f"{self.rho:.2e}"

        self.description = (
            "A uniform wire has the dimensions shown in the diagram, and its material has resistivity ρ.\n"
            "Determine the resistance of the wire.\n"
            "R = (_) Ω"
        )

        self.topic = "Electricity"
        self.subtopic = "Resistance and resistivity"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Resistivity, }} \\rho &= {self.rho_disp}\\,\\Omega\\,\\text{{m}}\\\\"
            f"\\text{{Length, }} L &= {self.L}\\,\\text{{m}}\\\\"
            f"\\text{{Diameter, }} d &= {self.d_mm}\\,\\text{{mm}} = {self.d_mm} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            f"\\text{{Resistance, }} R &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Calculate the cross-sectional area }} A. &\\\\"
            f"\\text{{The wire has a circular cross-section:}} &\\\\"
            f"A &= \\pi \\left( \\frac{{d}}{{2}} \\right)^2\\\\"
            f"A &= \\pi \\left( \\frac{{{self.d_mm} \\times 10^{{-3}}}}{{2}} \\right)^2\\\\"
            f"A &= {round(self.A, 12)}\\,\\text{{m}}^2\\\\"
            f"\\text{{Step 2: Apply the resistance formula.}} &\\\\"
            f"\\text{{The resistance }} R \\text{{ is given by:}} &\\\\"
            f"R &= \\frac{{\\rho L}}{{A}}\\\\"
            f"\\text{{Step 3: Substitute the known values and solve:}} &\\\\"
            f"R &= \\frac{{{self.rho_disp} \\times {self.L}}}{{{round(self.A, 12)}}}\\\\"
            f"R &= {round(self.R, 10)}\\,\\Omega\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.8, 2.8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wire
        ax.add_patch(patches.Rectangle((2.0, 1.7), 6.0, 0.6, fill=False, linewidth=2, edgecolor="black"))

        # Length
        ax.annotate("", xy=(2.0, 1.0), xytext=(8.0, 1.0),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(5.0, 0.82, f"L = {self.L} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Diameter
        ax.annotate("", xy=(5.0, 1.7), xytext=(5.0, 2.3),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(5.25, 2.0, f"d = {self.d_mm} mm", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(2.0, 3.5, f"ρ = {self.rho_disp} Ω m", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(9.7, 3.5, "R = ?", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy107:
    """
    Resistance and resistivity: resistance from a V–I graph.
    For an ohmic conductor: R = V / I (gradient of V–I graph).
    Target: resistance R.
    """

    def __init__(self):
        while True:
            self.R = rnd.randint(2, 25)  # Ω
            self.I_point = rnd.choice([0.20, 0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])  # A
            self.V_point = self.R * self.I_point
            if 0.8 <= self.V_point <= 24:
                break

        self.answer = sig_figs(self.R, 3)

        self.description = (
            "The graph shows potential difference V against current I for a conductor.\n"
            "All required values are shown on the diagram.\n"
            "Determine the resistance of the conductor.\n"
            "R = (_) Ω"
        )

        self.topic = "Electricity"
        self.subtopic = "Resistance and resistivity"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Potential difference at a point, }} V &= {sig_figs(self.V_point, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current at the same point, }} I &= {sig_figs(self.I_point, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Resistance, }} R &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between potential difference, current, and resistance.}} &\\\\"
            f"\\text{{For an ohmic conductor, the potential difference }} V \\text{{ is directly proportional to the current }} I: &\\\\"
            f"V &= I R\\\\ "
            f"\\text{{Step 2: Rearrange the formula to solve for resistance (}} R \\text{{).}} &\\\\"
            f"R &= \\frac{{V}}{{I}}\\\\"
            f"\\text{{The resistance is equivalent to the gradient of the }} V\\text{{-}}I \\text{{ graph.}} &\\\\"
            f"\\text{{Step 3: Substitute the known values from the graph point into the equation:}} &\\\\"
            f"R &= \\frac{{{sig_figs(self.V_point, 3)}}}{{{sig_figs(self.I_point, 3)}}}\\\\"
            f"R &= {round(self.R, 10)}\\,\\Omega\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.0, 4.0))
        ax.set_xlabel("current I / A", fontsize=9)
        ax.set_ylabel("potential difference V / V", fontsize=9)
        ax.tick_params(axis="both", labelsize=9)
        ax.grid(True, linestyle="--", alpha=0.45)

        # Choose plotting limits
        Imax = max(1.0, float(self.I_point) * 1.35)
        Vmax = max(5.0, float(self.V_point) * 1.35)
        ax.set_xlim(0, Imax)
        ax.set_ylim(0, Vmax)

        # Line through origin for ohmic conductor
        xs = [0, Imax]
        ys = [0, self.R * Imax]
        ax.plot(xs, ys, linewidth=2, color="black")

        # Mark the given point
        ax.plot([self.I_point], [self.V_point], "ko", markersize=4)
        ax.text(self.I_point, self.V_point + 0.06 * Vmax,
                f"({sig_figs(self.I_point,3)} A, {sig_figs(self.V_point,3)} V)",
                ha="right", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(0.98, 0.96, "R = ?", transform=ax.transAxes,
                ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.10)
        plt.close()


class Phy108:
    """
    Practical circuits: emf and internal resistance.
    Use terminal p.d. relation: V = E - Ir.
    Target: internal resistance r.
    """

    def __init__(self):
        while True:
            self.E = rnd.choice([1.5, 3.0, 4.5, 6.0, 9.0, 12.0])  # V
            self.r = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50, 2.00])  # Ω
            self.R = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20])  # Ω

            self.I = self.E / (self.R + self.r)         # A
            self.V = self.I * self.R                    # V (terminal p.d. across external resistor)

            if 0.2 <= self.I <= 3.5 and 0.8 <= self.V <= (self.E - 0.2):
                break

        self.answer = sig_figs(self.r, 3)

        self.description = (
            "A cell with emf E and internal resistance r supplies a resistor. The ammeter and voltmeter readings are shown.\n"
            "Determine the internal resistance of the cell.\n"
            "r = (_) Ω"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Electromotive force (e.m.f.), }} E &= {sig_figs(self.E, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Terminal potential difference, }} V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current in circuit, }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Internal resistance, }} r &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between e.m.f., terminal p.d., and internal resistance.}} &\\\\"
            f"\\text{{The e.m.f. of a cell is the sum of the terminal p.d. and the 'lost volts' across the internal resistance:}} &\\\\"
            f"E &= V + Ir\\\\"
            f"\\text{{Step 2: Rearrange the equation to solve for the internal resistance (}} r \\text{{).}} &\\\\"
            f"Ir &= E - V\\\\"
            f"r &= \\frac{{E - V}}{{I}}\\\\"
            f"\\text{{Step 3: Substitute the known values into the equation:}} &\\\\"
            f"r &= \\frac{{{sig_figs(self.E, 3)} - {sig_figs(self.V, 3)}}}{{{sig_figs(self.I, 3)}}}\\\\"
            f"r &= \\frac{{{round(self.E - self.V, 10)}}}{{{sig_figs(self.I, 3)}}}\\\\"
            f"r &= {round(self.r, 10)}\\,\\Omega\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 4.2))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        left_x, right_x = 2.0, 8.8
        top_y, bot_y = 8.6, 2.0

        # Ammeter on bottom wire
        x_A = 5.2
        r_A = 0.42
        A_left = (x_A - r_A, bot_y)
        A_right = (x_A + r_A, bot_y)

        # --- Left vertical: internal resistance + cell ---
        y_cell_top, y_cell_bot = 6.2, 3.0
        y_r = 7.4
        wR, hR = 1.2, 0.6

        # Internal resistance box (unknown)
        top_r, bot_r = draw_resistor_box(
            ax, x=left_x, y=y_r, w=wR, h=hR, label="r",
            value_text="r = ?", fontsize=8
        )

        # Wires on left vertical
        draw_wire(ax, [(left_x, top_y), (left_x, top_r)], lw=2)
        draw_wire(ax, [(left_x, bot_r), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)

        # Cell
        draw_cell_vertical(
            ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top,
            value_text=f"E = {sig_figs(self.E,3)} V", fontsize=8
        )

        # Right vertical (continuous)
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Bottom wire split by ammeter
        draw_wire(ax, [(left_x, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=8)
        draw_text(ax, x_A, bot_y - 0.85, f"I = {sig_figs(self.I,3)} A", fontsize=8, boxed=True)

        # Load resistor on top wire
        x_Rload = 6.2
        rL_left = (x_Rload - wR/2, top_y)
        rL_right = (x_Rload + wR/2, top_y)

        draw_wire(ax, [(left_x, top_y), rL_left], lw=2)
        draw_wire(ax, [rL_right, (right_x, top_y)], lw=2)

        draw_resistor_box(
            ax, x=x_Rload, y=top_y, w=wR, h=hR, label="R",
            value_text=f"{self.R} Ω", fontsize=8
        )

        # Voltmeter across external resistor
        x_vm = x_Rload
        y_vm = top_y + 1.1
        r_vm = 0.35

        # leads from resistor ends up to voltmeter level
        draw_wire(ax, [rL_left, (rL_left[0], y_vm)], lw=2)
        draw_wire(ax, [rL_right, (rL_right[0], y_vm)], lw=2)
        # leads to voltmeter circle edges
        draw_wire(ax, [(rL_left[0], y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (rL_right[0], y_vm)], lw=2)
        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=9)

        draw_text(ax, x_vm, y_vm + 0.75, f"V = {sig_figs(self.V,3)} V", fontsize=8, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy109:
    """
    Practical circuits: measuring resistance using ammeter and voltmeter (ideal meters).
    Target: resistance R = V/I.
    """

    def __init__(self):
        while True:
            self.R = rnd.randint(2, 60)  # Ω
            self.I = rnd.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])
            self.V = self.R * self.I
            if 1.0 <= self.V <= 24.0:
                break

        self.answer = sig_figs(self.R, 3)

        self.description = (
            "A resistor is connected in a circuit with an ammeter in series and a voltmeter across the resistor (assume ideal meters).\n"
            "The meter readings are shown in the diagram.\n"
            "Determine the resistance of the resistor.\n"
            "R = (_) Ω"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Voltmeter reading (potential difference), }} V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Ammeter reading (current), }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Resistance, }} R &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between potential difference, current, and resistance.}} &\\\\"
            f"\\text{{Resistance }} R \\text{{ is defined by Ohm's Law as the ratio of potential difference across}} &\\\\"
            f"\\text{{a component to the current flowing through it:}} &\\\\"
            f"R &= \\frac{{V}}{{I}}\\\\"
            f"\\text{{Step 2: Substitute the known values from the meter readings:}} &\\\\"
            f"R &= \\frac{{{sig_figs(self.V, 3)}}}{{{sig_figs(self.I, 3)}}}\\\\"
            f"R &= {round(self.R, 10)}\\,\\Omega\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 4.0))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        left_x, right_x = 2.0, 8.8
        top_y, bot_y = 8.0, 2.0

        # Cell on left vertical
        y_cell_top, y_cell_bot = 7.0, 3.0
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=None, fontsize=8)

        # Right vertical
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Ammeter bottom
        x_A, r_A = 5.0, 0.42
        A_left = (x_A - r_A, bot_y)
        A_right = (x_A + r_A, bot_y)
        draw_wire(ax, [(left_x, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=8)
        draw_text(ax, x_A, bot_y - 0.85, f"I = {sig_figs(self.I,3)} A", fontsize=8, boxed=True)

        # Resistor on top wire (unknown)
        wR, hR = 1.2, 0.6
        x_R = 5.8
        r_left = (x_R - wR/2, top_y)
        r_right = (x_R + wR/2, top_y)
        draw_wire(ax, [(left_x, top_y), r_left], lw=2)
        draw_wire(ax, [r_right, (right_x, top_y)], lw=2)
        draw_resistor_box(ax, x=x_R, y=top_y, w=wR, h=hR, label="R", value_text="R = ?", fontsize=8)

        # Voltmeter across resistor with shown reading
        x_vm, y_vm, r_vm = x_R, top_y + 1.2, 0.35
        draw_wire(ax, [r_left, (r_left[0], y_vm)], lw=2)
        draw_wire(ax, [r_right, (r_right[0], y_vm)], lw=2)
        draw_wire(ax, [(r_left[0], y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (r_right[0], y_vm)], lw=2)
        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=8)
        draw_text(ax, x_vm, y_vm + 0.75, f"V = {sig_figs(self.V,3)} V", fontsize=8, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy110:
    """
    Practical circuits: electrical power.
    Target: P using P = IV (values shown on meters).
    """

    def __init__(self):
        while True:
            self.V = rnd.choice([3, 4.5, 6, 9, 12, 15, 18, 24])
            self.I = rnd.choice([0.20, 0.30, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])
            self.P = self.V * self.I
            if 0.5 <= self.P <= 150:
                break

        self.answer = sig_figs(self.P, 3)

        self.description = (
            "A device is connected in a circuit. The current through the device and the potential difference across it are shown.\n"
            "Determine the power transferred to the device.\n"
            "P = (_) W"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Potential difference, }} V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current, }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Electrical power, }} P &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between power, current, and potential difference.}} &\\\\"
            f"\\text{{The electrical power }} P \\text{{ delivered to a component is the product of the potential}} &\\\\"
            f"\\text{{difference across it and the current flowing through it:}} &\\\\"
            f"P &= I \\times V\\\\"
            f"\\text{{Step 2: Substitute the known values into the equation:}} &\\\\"
            f"P &= {sig_figs(self.I, 3)} \\times {sig_figs(self.V, 3)}\\\\"
            f"P &= {round(self.P, 10)}\\,\\text{{W}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{W}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(7.2, 3.4))
        setup_ax(ax, xlim=(0, 12), ylim=(0, 6))

        y_wire = 3.0
        xL, xR = 1.0, 11.0

        # Device block
        dev_w, dev_h = 2.4, 1.6
        x_dev = 6.0
        ax.add_patch(patches.Rectangle((x_dev - dev_w/2, y_wire - dev_h/2), dev_w, dev_h,
                                       fill=False, linewidth=2, edgecolor="black"))
        ax.text(x_dev, y_wire, "device", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Wires to device edges
        ax.plot([xL, x_dev - dev_w/2], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")
        ax.plot([x_dev + dev_w/2, xR], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")

        # Current arrow (top)
        y_I = 5.1
        ax.annotate("", xy=(9.3, y_I), xytext=(2.7, y_I),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(9.35, y_I, f"I = {sig_figs(self.I,3)} A", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Voltage bracket (bottom) across device
        y_V = 1.6
        ax.annotate("", xy=(x_dev - dev_w/2, y_V), xytext=(x_dev + dev_w/2, y_V),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(x_dev, y_V - 0.25, f"V = {sig_figs(self.V,3)} V", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown power
        ax.text(11.0, 5.8, "P = ?", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy111:
    """
    Practical circuits: electrical energy.
    Use W = IVt. Target: energy W.
    """

    def __init__(self):
        while True:
            self.V = rnd.choice([3, 4.5, 6, 9, 12, 15, 18, 24])
            self.I = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])
            self.t = rnd.choice([5, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60])  # s
            self.W = self.V * self.I * self.t
            if 50 <= self.W <= 10000:
                break

        self.answer = sig_figs(self.W, 3)

        self.description = (
            "A device operates at a steady current and potential difference for a time t, as shown in the diagram.\n"
            "Determine the electrical energy transferred.\n"
            "W = (_) J"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Potential difference, }} V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current, }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Time interval, }} t &= {self.t}\\,\\text{{s}}\\\\"
            f"\\text{{Energy transferred, }} W &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between energy, current, voltage, and time.}} &\\\\"
            f"\\text{{The electrical energy }} W \\text{{ transferred is the product of power (}} P = IV \\text{{) and time:}} &\\\\"
            f"W &= I \\times V \\times t\\\\"
            f"\\text{{Step 2: Substitute the known values into the equation:}} &\\\\"
            f"W &= {sig_figs(self.I, 3)} \\times {sig_figs(self.V, 3)} \\times {self.t}\\\\"
            f"W &= {round(self.W, 10)}\\,\\text{{J}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{J}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(7.2, 3.4))
        setup_ax(ax, xlim=(0, 12), ylim=(0, 6))

        # Device in wire
        y_wire = 3.0
        xL, xR = 1.0, 11.0
        dev_w, dev_h = 2.4, 1.6
        x_dev = 6.0

        ax.add_patch(patches.Rectangle((x_dev - dev_w/2, y_wire - dev_h/2), dev_w, dev_h,
                                       fill=False, linewidth=2, edgecolor="black"))
        ax.text(x_dev, y_wire, "device", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        ax.plot([xL, x_dev - dev_w/2], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")
        ax.plot([x_dev + dev_w/2, xR], [y_wire, y_wire], linewidth=4, color="black", solid_capstyle="round")

        # Current arrow
        y_I = 5.1
        ax.annotate("", xy=(9.3, y_I), xytext=(2.7, y_I),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(9.35, y_I, f"I = {sig_figs(self.I,3)} A", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Voltage bracket
        y_V = 1.6
        ax.annotate("", xy=(x_dev - dev_w/2, y_V), xytext=(x_dev + dev_w/2, y_V),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(x_dev, y_V - 0.25, f"V = {sig_figs(self.V,3)} V", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Time label
        ax.text(1.0, 0.5, f"t = {self.t} s", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown energy
        ax.text(11.0, 5.8, "W = ?", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy112:
    """
    Practical circuits: emf, internal resistance and terminal p.d.
    Use E = V + Ir. Target: emf E.
    """

    def __init__(self):
        while True:
            self.E = rnd.choice([1.5, 3.0, 4.5, 6.0, 9.0, 12.0])  # V
            self.r = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20])  # Ω
            self.R = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15])  # Ω

            self.I = self.E / (self.R + self.r)
            self.V = self.I * self.R
            if 0.2 <= self.I <= 3.5 and 0.8 <= self.V <= (self.E - 0.2):
                break

        self.answer = sig_figs(self.E, 3)

        self.description = (
            "A cell with internal resistance r supplies a resistor. The ammeter reading and the terminal p.d. are shown.\n"
            "Determine the emf of the cell.\n"
            "E = (_) V"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Terminal potential difference, }} V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Current, }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Internal resistance, }} r &= {sig_figs(self.r, 3)}\\,\\Omega\\\\"
            f"\\text{{Electromotive force (e.m.f.), }} E &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Identify the relationship between e.m.f., terminal p.d., and lost volts.}} &\\\\"
            f"\\text{{The e.m.f. of a cell is equal to the terminal potential difference plus the}} &\\\\"
            f"\\text{{potential difference dropped across the internal resistance (lost volts):}} &\\\\"
            f"E &= V + Ir\\\\"
            f"\\text{{Step 2: Calculate the 'lost volts' (}} Ir \\text{{).}} &\\\\"
            f"Ir &= {sig_figs(self.I, 3)} \\times {sig_figs(self.r, 3)}\\\\"
            f"Ir &= {round(self.I * self.r, 10)}\\,\\text{{V}}\\\\"
            f"\\text{{Step 3: Substitute the values to find the e.m.f.}} &\\\\"
            f"E &= {sig_figs(self.V, 3)} + {round(self.I * self.r, 10)}\\\\"
            f"E &= {round(self.E, 10)}\\,\\text{{V}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{V}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.6, 4.2))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        left_x, right_x = 2.0, 8.8
        top_y, bot_y = 8.6, 2.0

        # Left vertical: internal resistance + cell (emf unknown)
        y_cell_top, y_cell_bot = 6.2, 3.0
        y_r = 7.4
        wR, hR = 1.2, 0.6

        # Internal resistance (given)
        top_r, bot_r = draw_resistor_box(
            ax, x=left_x, y=y_r, w=wR, h=hR, label="r",
            value_text=f"r = {sig_figs(self.r,3)} Ω", fontsize=9
        )

        draw_wire(ax, [(left_x, top_y), (left_x, top_r)], lw=2)
        draw_wire(ax, [(left_x, bot_r), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)

        draw_cell_vertical(
            ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top,
            value_text="E = ?", fontsize=9
        )

        # Right vertical
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Ammeter bottom
        x_A, r_A = 5.2, 0.42
        A_left = (x_A - r_A, bot_y)
        A_right = (x_A + r_A, bot_y)
        draw_wire(ax, [(left_x, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=9)
        draw_text(ax, x_A, bot_y - 0.85, f"I = {sig_figs(self.I,3)} A", fontsize=9, boxed=True)

        # Load resistor on top wire (given) 
        x_Rload = 6.2
        rL_left = (x_Rload - wR/2, top_y)
        rL_right = (x_Rload + wR/2, top_y)
        draw_wire(ax, [(left_x, top_y), rL_left], lw=2)
        draw_wire(ax, [rL_right, (right_x, top_y)], lw=2)
        draw_resistor_box(ax, x=x_Rload, y=top_y, w=wR, h=hR, label="R",
                          value_text=f"{self.R} Ω", fontsize=9)

        # Voltmeter across load shows terminal p.d. 
        x_vm, y_vm, r_vm = x_Rload, top_y + 1.1, 0.35
        draw_wire(ax, [rL_left, (rL_left[0], y_vm)], lw=2)
        draw_wire(ax, [rL_right, (rL_right[0], y_vm)], lw=2)
        draw_wire(ax, [(rL_left[0], y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (rL_right[0], y_vm)], lw=2)
        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=9)
        draw_text(ax, x_vm, y_vm + 0.75, f"V = {sig_figs(self.V,3)} V", fontsize=9, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy113:
    """
    Practical circuits: determine emf E and internal resistance r from two readings.
    Terminal p.d. relation: V = E - Ir
    Dynamic target: find r OR E
    """

    def __init__(self):
        self.target = rnd.choice(["r", "E"])

        while True:
            self.E = rnd.choice([1.5, 3.0, 4.5, 6.0, 9.0, 12.0])
            self.r = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00, 1.20, 1.50])

            # Choose two different currents with I1 > I2 so V1 < V2
            self.I1 = rnd.choice([0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0])
            self.I2 = rnd.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0])

            if self.I1 <= self.I2:
                continue

            self.V1 = self.E - self.I1 * self.r
            self.V2 = self.E - self.I2 * self.r

            if self.V1 > 0.8 and self.V2 > 0.8 and self.V1 < self.V2 and self.V2 <= self.E:
                break

        if self.target == "r":
            self.answer = sig_figs(self.r, 3)
        else:
            self.answer = sig_figs(self.E, 3)

        self.description = (
            "A variable resistor (VR) is adjusted to change the current in a circuit containing a cell.\n"
            "For two settings of VR, the current I and the terminal potential difference V are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Measurement 1: }} I_1 &= {sig_figs(self.I1, 3)}\\,\\text{{A}}, \\, V_1 = {sig_figs(self.V1, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Measurement 2: }} I_2 &= {sig_figs(self.I2, 3)}\\,\\text{{A}}, \\, V_2 = {sig_figs(self.V2, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Electromotive force (e.m.f.), }} E &= {'\\text{?}' if self.target == 'E' else sig_figs(self.E, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Internal resistance, }} r &= {'\\text{?}' if self.target == 'r' else sig_figs(self.r, 3)}\\,\\Omega\\\\"
            f"\\text{{Step 1: Set up the simultaneous equations using }} V = E - Ir. &\\\\"
            f"\\text{{(1) }} {sig_figs(self.V1, 3)} &= E - ({sig_figs(self.I1, 3)})r\\\\"
            f"\\text{{(2) }} {sig_figs(self.V2, 3)} &= E - ({sig_figs(self.I2, 3)})r\\\\"
            f"\\text{{Step 2: Solve for internal resistance }} r \\text{{ by subtracting (1) from (2).}} &\\\\"
            f"V_2 - V_1 &= (E - E) - I_2 r - (-I_1 r)\\\\"
            f"V_2 - V_1 &= r(I_1 - I_2)\\\\"
            f"r &= \\frac{{V_2 - V_1}}{{I_1 - I_2}} = \\frac{{{sig_figs(self.V2, 3)} - {sig_figs(self.V1, 3)}}}{{{sig_figs(self.I1, 3)} - {sig_figs(self.I2, 3)}}}\\\\"
            f"r &= {round(self.r, 10)}\\,\\Omega\\\\"
            f"\\text{{Step 3: Solve for e.m.f. }} E \\text{{ by substituting }} r \\text{{ back into equation (1).}} &\\\\"
            + (
                f"E &= V_1 + I_1 r\\\\"
                f"E &= {sig_figs(self.V1, 3)} + ({sig_figs(self.I1, 3)} \\times {round(self.r, 10)})\\\\"
                f"E &= {round(self.E, 10)}\\,\\text{{V}}"
                if self.target == "E" else
                f"\\text{{Internal resistance }} r \\text{{ was found in Step 2.}} &\\\\"
                f"r &= {self.answer}\\,\\Omega"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.0, 2.0
        left_x, right_x = 2.0, 8.5

        # Variable resistor on top wire (clearly labeled VR)
        wR, hR = 1.2, 0.6
        x_vr = 5.7
        vr_left = (x_vr - wR/2, top_y)
        vr_right = (x_vr + wR/2, top_y)

        draw_wire(ax, [(left_x, top_y), vr_left], lw=2)
        draw_wire(ax, [vr_right, (right_x, top_y)], lw=2)

        draw_resistor_box(ax, x=x_vr, y=top_y, w=wR, h=hR, label="VR",
                          value_text=None, fontsize=9)
        draw_text(ax, x_vr, top_y + 0.85, "variable resistor", fontsize=9, boxed=True)

        # Right vertical and bottom wire
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # Left vertical: cell (E and r are properties of the cell)
        y_cell_top, y_cell_bot = 7.0, 3.0
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top,
                           value_text=None, fontsize=9)

        # Put target next to cell (not floating on a random wire)
        if self.target == "r":
            draw_text(ax, left_x - 0.2, 5.0, "r = ?", fontsize=9, ha="right", boxed=True)
            draw_text(ax, left_x - 0.2, 6.0, f"E = {sig_figs(self.E,3)} V", fontsize=9, ha="right", boxed=True)
        else:
            draw_text(ax, left_x - 0.2, 6.0, "E = ?", fontsize=9, ha="right", boxed=True)
            draw_text(ax, left_x - 0.2, 5.0, f"r = {sig_figs(self.r,3)} Ω", fontsize=9, ha="right", boxed=True)

        # Central "two settings" panel 
        draw_text(ax, 6.0, 6.2, "Two settings:", fontsize=9, boxed=True)
        draw_text(ax, 6.0, 5.3, f"1) I₁ = {sig_figs(self.I1,3)} A,  V₁ = {sig_figs(self.V1,3)} V", fontsize=9, boxed=True)
        draw_text(ax, 6.0, 4.4, f"2) I₂ = {sig_figs(self.I2,3)} A,  V₂ = {sig_figs(self.V2,3)} V", fontsize=9, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy114:
    """
    Practical circuits: identical cells in series.
    Total emf = 2E, total internal resistance = 2r.
    Target: emf of ONE cell, E.
    """

    def __init__(self):
        while True:
            self.E = rnd.choice([1.5, 2.0, 3.0, 4.5, 6.0])  # V (each cell)
            self.r = rnd.choice([0.20, 0.30, 0.50, 0.80, 1.00])  # Ω (each cell)
            self.R = rnd.choice([3, 4, 5, 6, 8, 10, 12, 15, 20])  # Ω

            self.I = (2 * self.E) / (self.R + 2 * self.r)
            if 0.2 <= self.I <= 3.0:
                break

        self.answer = sig_figs(self.E, 3)

        self.description = (
            "Two identical cells are connected in series to a resistor. Each cell has internal resistance r.\n"
            "The resistor value and the current are shown in the diagram.\n"
            "Determine the emf E of one cell.\n"
            "E = (_) V"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Number of cells, }} n &= 2\\\\"
            f"\\text{{Internal resistance of one cell, }} r &= {sig_figs(self.r, 3)}\\,\\Omega\\\\"
            f"\\text{{External resistance, }} R &= {self.R}\\,\\Omega\\\\"
            f"\\text{{Circuit current, }} I &= {sig_figs(self.I, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Emf of one cell, }} E &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Calculate the total emf and total internal resistance of the combination.}} &\\\\"
            f"\\text{{For }} n \\text{{ identical cells in series:}} &\\\\"
            f"E_{{total}} &= n E = 2E\\\\"
            f"r_{{total}} &= n r = 2({sig_figs(self.r, 3)}) = {round(2 * self.r, 10)}\\,\\Omega\\\\"
            f"\\text{{Step 2: Apply Ohm's Law to the complete circuit.}} &\\\\"
            f"I &= \\frac{{E_{{total}}}}{{R + r_{{total}}}}\\\\"
            f"2E &= I(R + r_{{total}})\\\\"
            f"\\text{{Step 3: Substitute the known values and solve for }} E. &\\\\"
            f"2E &= {sig_figs(self.I, 3)} \\times ({self.R} + {round(2 * self.r, 10)})\\\\"
            f"2E &= {sig_figs(self.I, 3)} \\times {round(self.R + 2 * self.r, 10)}\\\\"
            f"2E &= {round(self.I * (self.R + 2 * self.r), 10)}\\\\"
            f"E &= \\frac{{{round(self.I * (self.R + 2 * self.r), 10)}}}{{2}}\\\\"
            f"E &= {self.answer}\\,\\text{{V}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{V}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.6))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.0, 2.0
        left_x, right_x = 2.0, 8.5

        # Ammeter inline on bottom wire
        x_A, r_A = 5.3, 0.45
        A_left = (x_A - r_A, bot_y)
        A_right = (x_A + r_A, bot_y)
        draw_wire(ax, [(left_x, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=9)
        draw_text(ax, x_A, bot_y - 0.85, f"I = {sig_figs(self.I,3)} A", fontsize=9, boxed=True)

        # Right side vertical
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Resistor on top wire
        wR, hR = 1.2, 0.6
        x_R = 6.2
        R_left, R_right = (x_R - wR/2, top_y), (x_R + wR/2, top_y)
        draw_wire(ax, [(left_x, top_y), R_left], lw=2)
        draw_wire(ax, [R_right, (right_x, top_y)], lw=2)
        draw_resistor_box(ax, x=x_R, y=top_y, w=wR, h=hR, label="R",
                          value_text=f"{self.R} Ω", fontsize=9)

        # Left side: two cells in series (contiguous)
        y_bottom_cells = 3.0
        y_mid = 5.5
        y_top_cells = 7.8

        draw_wire(ax, [(left_x, top_y), (left_x, y_top_cells)], lw=2)
        draw_wire(ax, [(left_x, y_bottom_cells), (left_x, bot_y)], lw=2)

        # Bottom cell then top cell, touching at y_mid so they are visibly "in series"
        draw_cell_vertical(ax, x=left_x, y_bottom=y_bottom_cells, y_top=y_mid, value_text=None, fontsize=9)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_mid, y_top=y_top_cells, value_text=None, fontsize=9)

        # Labels for the two identical cells
        draw_text(ax, 0.8, 9.2, "2 identical cells (series)", fontsize=9, ha="left", boxed=True)
        draw_text(ax, 0.8, 8.4, f"each: r = {sig_figs(self.r,3)} Ω", fontsize=9, ha="left", boxed=True)
        draw_text(ax, 0.8, 7.6, "each: E = ?", fontsize=9, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy115:
    """
    Practical circuits: identical cells in parallel.
    Equivalent emf = E, equivalent internal resistance = r/2.
    Target: current in the external resistor.
    """

    def __init__(self):
        while True:
            self.E = rnd.choice([1.5, 3.0, 4.5, 6.0, 9.0])  # V
            self.r = rnd.choice([0.30, 0.50, 0.80, 1.00, 1.20, 1.50])  # Ω each
            self.R = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15])  # Ω

            self.r_eq = self.r / 2
            self.I = self.E / (self.R + self.r_eq)

            if 0.2 <= self.I <= 4.0:
                break

        self.answer = sig_figs(self.I, 3)

        self.description = (
            "Two identical cells are connected in parallel to a resistor. Each cell has internal resistance r.\n"
            "The values are shown in the diagram.\n"
            "Determine the current in the resistor.\n"
            "I = (_) A"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Emf of each cell, }} E &= {sig_figs(self.E, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Internal resistance of each cell, }} r &= {sig_figs(self.r, 3)}\\,\\Omega\\\\"
            f"\\text{{External resistance, }} R &= {self.R}\\,\\Omega\\\\"
            f"\\text{{Circuit current, }} I &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Determine the equivalent emf and internal resistance of the parallel combination.}} &\\\\"
            f"\\text{{For identical cells in parallel, the total emf remains the same as a single cell:}} &\\\\"
            f"E_{{total}} &= E = {sig_figs(self.E, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{The equivalent internal resistance (}} r_{{eq}} \\text{{) is found using the parallel resistor rule:}} &\\\\"
            f"\\frac{{1}}{{r_{{eq}}}} &= \\frac{{1}}{{r}} + \\frac{{1}}{{r}} = \\frac{{2}}{{r}} \\implies r_{{eq}} = \\frac{{r}}{{2}}\\\\"
            f"r_{{eq}} &= \\frac{{{sig_figs(self.r, 3)}}}{{2}} = {round(self.r / 2, 10)}\\,\\Omega\\\\"
            f"\\text{{Step 2: Apply Ohm's Law to the complete circuit.}} &\\\\"
            f"I &= \\frac{{E_{{total}}}}{{R + r_{{eq}}}}\\\\"
            f"\\text{{Step 3: Substitute the known values and solve for }} I. &\\\\"
            f"I &= \\frac{{{sig_figs(self.E, 3)}}}{{{self.R} + {round(self.r / 2, 10)}}}\\\\"
            f"I &= \\frac{{{sig_figs(self.E, 3)}}}{{{round(self.R + self.r / 2, 10)}}}\\\\"
            f"I &= {self.answer}\\,\\text{{A}}\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{A}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.0, 4.6))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.0, 2.0
        x_bus_left, x_bus_right = 2.0, 4.6
        right_x = 8.6

        # Buses for the parallel cells
        draw_wire(ax, [(x_bus_left, top_y), (x_bus_right, top_y)], lw=2)
        draw_wire(ax, [(x_bus_left, bot_y), (x_bus_right, bot_y)], lw=2)

        # Two parallel cell branches
        y_cell_top, y_cell_bot = 6.9, 3.1
        x1, x2 = 2.0, 3.8

        # Branch 1
        draw_wire(ax, [(x1, top_y), (x1, y_cell_top)], lw=2)
        draw_wire(ax, [(x1, y_cell_bot), (x1, bot_y)], lw=2)
        draw_cell_vertical(ax, x=x1, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=None, fontsize=9)

        # Branch 2
        draw_wire(ax, [(x2, top_y), (x2, y_cell_top)], lw=2)
        draw_wire(ax, [(x2, y_cell_bot), (x2, bot_y)], lw=2)
        draw_cell_vertical(ax, x=x2, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=None, fontsize=9)

        # Labels
        draw_text(ax, 0.9, 9.2, "2 identical cells (parallel)", fontsize=9, ha="left", boxed=True)
        draw_text(ax, 0.9, 8.4, f"E = {sig_figs(self.E,3)} V", fontsize=9, ha="left", boxed=True)
        draw_text(ax, 0.9, 7.6, f"r = {sig_figs(self.r,3)} Ω each", fontsize=9, ha="left", boxed=True)

        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Resistor on TOP wire
        wR, hR = 1.2, 0.6
        x_R = 6.8
        R_left = (x_R - wR/2, top_y)
        R_right = (x_R + wR/2, top_y)

        draw_wire(ax, [(x_bus_right, top_y), R_left], lw=2)
        draw_wire(ax, [R_right, (right_x, top_y)], lw=2)
        draw_resistor_box(ax, x=x_R, y=top_y, w=wR, h=hR, label="R",
                          value_text=f"{self.R} Ω", fontsize=9)

        # Ammeter on BOTTOM wire
        x_A, r_A = 6.2, 0.45
        A_left, A_right = (x_A - r_A, bot_y), (x_A + r_A, bot_y)

        draw_wire(ax, [(x_bus_right, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=9)

        draw_text(ax, x_A, bot_y - 0.85, "I = ?", fontsize=9, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy116:
    """
    Practical circuits: thermistor in a series circuit (voltmeter across fixed resistor).
    Use potential divider relation in series: V_R = V_s * R / (R + R_T)
    Target: thermistor resistance R_T.
    """

    def __init__(self):
        while True:
            self.Vs = rnd.choice([6, 9, 12])  # V
            self.R = rnd.choice([100, 220, 330, 470, 680, 1000])  # Ω fixed resistor
            self.RT = rnd.choice([150, 220, 330, 470, 680, 1000, 1500, 2200, 3300, 4700])  # Ω thermistor at some temp

            self.VR = self.Vs * self.R / (self.R + self.RT)

            if 0.8 <= self.VR <= (self.Vs - 0.8):
                break

        self.answer = sig_figs(self.RT, 3)

        self.description = (
            "A thermistor (NTC) is connected in series with a fixed resistor. The supply voltage and the voltmeter reading are shown.\n"
            "Determine the resistance of the thermistor.\n"
            "R_T = (_) Ω"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Practical circuits"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Fixed resistance, }} R &= {self.R}\\,\\Omega\\\\"
            f"\\text{{Potential difference across }} R, V_R &= {sig_figs(self.VR, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Thermistor resistance, }} R_T &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Calculate the potential difference across the thermistor (}} V_T \\text{{).}} &\\\\"
            f"\\text{{In a series circuit, the total supply voltage is shared between components:}} &\\\\"
            f"V_s &= V_R + V_T\\\\"
            f"V_T &= {self.Vs} - {sig_figs(self.VR, 3)} = {round(self.Vs - self.VR, 10)}\\,\\text{{V}}\\\\"
            f"\\text{{Step 2: Use the potential divider principle.}} &\\\\"
            f"\\text{{The ratio of potential differences is equal to the ratio of resistances:}} &\\\\"
            f"\\frac{{R_T}}{{R}} &= \\frac{{V_T}}{{V_R}}\\\\"
            f"\\text{{Step 3: Solve for }} R_T. &\\\\"
            f"R_T &= R \\times \\frac{{V_T}}{{V_R}}\\\\"
            f"R_T &= {self.R} \\times \\frac{{{round(self.Vs - self.VR, 10)}}}{{{sig_figs(self.VR, 3)}}}\\\\"
            f"R_T &= {round(self.RT, 10)}\\,\\Omega\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\Omega"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.2))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        left_x, right_x = 2.0, 8.8
        top_y, bot_y = 8.0, 2.0

        # Cell on left
        y_cell_top, y_cell_bot = 7.0, 3.0
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=f"{self.Vs} V", fontsize=9)

        # Right vertical
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Bottom wire
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # Two series components on top wire: fixed resistor + thermistor
        wR, hR = 1.2, 0.6

        x_R = 5.0
        x_T = 7.0

        # Wires top
        draw_wire(ax, [(left_x, top_y), (x_R - wR/2, top_y)], lw=2)
        draw_wire(ax, [(x_R + wR/2, top_y), (x_T - wR/2, top_y)], lw=2)
        draw_wire(ax, [(x_T + wR/2, top_y), (right_x, top_y)], lw=2)

        draw_resistor_box(ax, x=x_R, y=top_y, w=wR, h=hR, label="R",
                          value_text=f"{self.R} Ω", fontsize=9)

        draw_thermistor(ax, x=x_T, y=top_y, label="NTC",
                        value_text="R_T = ?", fontsize=9)

        # Voltmeter across fixed resistor (shows V_R)
        x_vm, y_vm, r_vm = x_R, top_y + 1.2, 0.35
        R_left = (x_R - wR/2, top_y)
        R_right = (x_R + wR/2, top_y)

        draw_wire(ax, [R_left, (R_left[0], y_vm)], lw=2)
        draw_wire(ax, [R_right, (R_right[0], y_vm)], lw=2)
        draw_wire(ax, [(R_left[0], y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (R_right[0], y_vm)], lw=2)
        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=9)
        draw_text(ax, x_vm, y_vm + 0.75, f"V_R = {sig_figs(self.VR,3)} V", fontsize=9, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy117:
    """
    Kirchhoff’s laws: two-loop (mesh) circuit with shared resistor.
    Solve two simultaneous equations for mesh currents.
    Target: current in the shared resistor (magnitude + direction).
    """

    def __init__(self):
        while True:
            self.R1 = rnd.randint(2, 20)
            self.R2 = rnd.randint(2, 20)
            self.R3 = rnd.randint(2, 20)
            self.E1 = rnd.choice([3, 4.5, 6, 9, 12, 15, 18])
            self.E2 = rnd.choice([1.5, 3, 4.5, 6, 9, 12])

            # Solve:
            # (R1+R3)I1 - R3 I2 = E1
            # -R3 I1 + (R2+R3)I2 = E2
            a = self.R1 + self.R3
            b = -self.R3
            c = -self.R3
            d = self.R2 + self.R3
            det = a * d - b * c
            if abs(det) < 1e-9:
                continue

            I1 = (self.E1 * d - b * self.E2) / det
            I2 = (a * self.E2 - self.E1 * c) / det

            self.I1 = I1
            self.I2 = I2

            self.I3 = self.I1 - self.I2  # current through shared resistor (top -> bottom taken as positive)
            if 0.05 <= abs(self.I3) <= 3.0 and 0.05 <= abs(self.I1) <= 3.5 and 0.05 <= abs(self.I2) <= 3.5:
                break

        self.I3_mag = abs(self.I3)
        self.I3_dir = "downwards" if self.I3 >= 0 else "upwards"
        self.answer = f"{sig_figs(self.I3_mag,3)} A {self.I3_dir}"

        self.description = (
            "The circuit contains two loops with a shared resistor. Values are shown in the diagram.\n"
            "Using Kirchhoff’s laws, determine the current in the shared resistor R3.\n"
            "Current = (_) A, direction = (upwards/downwards). Answer format: (_) A upwards/downwards"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Kirchhoff’s laws"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Step 1: Define mesh currents }} I_1 \\text{{ (left loop) and }} I_2 \\text{{ (right loop).}} &\\\\"
            f"\\text{{Let both }} I_1 \\text{{ and }} I_2 \\text{{ flow clockwise. The current }} I_3 \\text{{ (downwards) is }} I_1 - I_2. &\\\\"
            f"\\text{{Step 2: Apply Kirchhoff's Second Law (Loop Rule) to both loops.}} &\\\\"
            f"\\text{{Loop 1 (Left): }} E_1 - I_1 R_1 - (I_1 - I_2) R_3 &= 0 \\\\"
            f"{self.E1} - {self.R1} I_1 - {self.R3} (I_1 - I_2) &= 0 \\\\"
            f"({self.R1 + self.R3}) I_1 - {self.R3} I_2 &= {self.E1} \\quad \\text{{--- (Eq. 1)}} \\\\"
            f"\\text{{Loop 2 (Right): }} -E_2 - I_2 R_2 - (I_2 - I_1) R_3 &= 0 \\\\"
            f"-{self.E2} - {self.R2} I_2 - {self.R3} (I_2 - I_1) &= 0 \\\\"
            f"-{self.R3} I_1 + ({self.R2 + self.R3}) I_2 &= -{self.E2} \\quad \\text{{--- (Eq. 2)}} \\\\"
            f"\\text{{Step 3: Solve the simultaneous equations for }} I_1 \\text{{ and }} I_2. &\\\\"
            f"I_1 &= {sig_figs(self.I1, 4)}\\,\\text{{A}}, \\quad I_2 = {sig_figs(self.I2, 4)}\\,\\text{{A}} \\\\"
            f"\\text{{Step 4: Calculate the current through the shared resistor }} I_3. &\\\\"
            f"I_3 &= I_1 - I_2 = {sig_figs(self.I1, 4)} - ({sig_figs(self.I2, 4)}) \\\\"
            f"I_3 &= {sig_figs(self.I3, 4)}\\,\\text{{A}} \\\\"
            f"\\text{{A positive result indicates downwards flow; negative indicates upwards.}} &\\\\"
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.2, 4.8))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.6, 2.0
        xL, xM, xR = 2.0, 5.0, 8.6

        # Bottom wire
        draw_wire(ax, [(xL, bot_y), (xR, bot_y)], lw=2)

        # Left vertical with cell E1
        y_cell_top, y_cell_bot = 7.2, 3.4
        draw_wire(ax, [(xL, top_y), (xL, y_cell_top)], lw=2)
        draw_wire(ax, [(xL, y_cell_bot), (xL, bot_y)], lw=2)
        draw_cell_vertical(ax, x=xL, y_bottom=y_cell_bot, y_top=y_cell_top,
                           value_text=f"E1 = {self.E1} V", fontsize=9)

        # Right vertical with cell E2
        draw_wire(ax, [(xR, top_y), (xR, y_cell_top)], lw=2)
        draw_wire(ax, [(xR, y_cell_bot), (xR, bot_y)], lw=2)
        draw_cell_vertical(ax, x=xR, y_bottom=y_cell_bot, y_top=y_cell_top,
                           value_text=f"E2 = {self.E2} V", fontsize=8)

        # Top resistors R1 and R2
        wR, hR = 1.2, 0.6
        x_R1 = (xL + xM) / 2
        x_R2 = (xM + xR) / 2

        R1_left, R1_right = (x_R1 - wR/2, top_y), (x_R1 + wR/2, top_y)
        R2_left, R2_right = (x_R2 - wR/2, top_y), (x_R2 + wR/2, top_y)

        draw_wire(ax, [(xL, top_y), R1_left], lw=2)
        draw_wire(ax, [R1_right, (xM, top_y)], lw=2)
        draw_wire(ax, [(xM, top_y), R2_left], lw=2)
        draw_wire(ax, [R2_right, (xR, top_y)], lw=2)

        draw_resistor_box(ax, x=x_R1, y=top_y, w=wR, h=hR, label="R1",
                          value_text=f"{self.R1} Ω", fontsize=9)
        draw_resistor_box(ax, x=x_R2, y=top_y, w=wR, h=hR, label="R2",
                          value_text=f"{self.R2} Ω", fontsize=9)

        # Shared resistor R3 (vertical in the middle)
        x_R3 = xM
        y_R3 = (top_y + bot_y) / 2 - 1
        top3, bot3 = draw_resistor_box(ax, x=x_R3, y=y_R3, w=1.2, h=0.6, label="R3",
                                       value_text=f"{self.R3} Ω", fontsize=9)

        # Connect shared resistor to top and bottom nodes
        draw_wire(ax, [(xM, top_y), (xM, top3)], lw=2)
        draw_wire(ax, [(xM, bot3), (xM, bot_y)], lw=2)

        # Indicate I3 direction reference (downwards)
        ax.annotate("", xy=(xM + 0.9, bot_y + 0.4), xytext=(xM + 0.9, top_y - 2.4),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        draw_text(ax, xM + 1.2, (top_y + bot_y) / 2, "I3", fontsize=9, ha="left", boxed=True)

        # Unknown label
        draw_text(ax, 9.2, 9.2, "I3 = ?", fontsize=9, ha="right", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy118:
    """
    Kirchhoff’s laws: series resistor feeding a parallel network.
    Dynamic target: I_total OR I1 OR I2.
    """

    def __init__(self):
        self.target = rnd.choice(["It", "I1", "I2"])

        while True:
            self.Vs = rnd.choice([6, 9, 12, 15, 18, 24])
            self.Rs = rnd.randint(2, 15)     # series resistor
            self.R1 = rnd.randint(3, 30)     # branch 1
            self.R2 = rnd.randint(3, 30)     # branch 2

            Rp = (self.R1 * self.R2) / (self.R1 + self.R2)
            self.It = self.Vs / (self.Rs + Rp)
            Vp = self.It * Rp
            self.I1 = Vp / self.R1
            self.I2 = Vp / self.R2

            if 0.1 <= self.It <= 4.0 and 0.05 <= self.I1 <= 3.5 and 0.05 <= self.I2 <= 3.5:
                break

        if self.target == "It":
            self.answer = sig_figs(self.It, 3)
        elif self.target == "I1":
            self.answer = sig_figs(self.I1, 3)
        else:
            self.answer = sig_figs(self.I2, 3)

        self.description = (
            "A resistor is connected in series with a parallel network. Values are shown in the diagram.\n"
            "Using Kirchhoff’s laws, determine the requested current.\n"
            "Current = (_) A"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Kirchhoff’s laws"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Series resistance, }} R_s &= {self.Rs}\\,\\Omega\\\\"
            f"\\text{{Branch 1 resistance, }} R_1 &= {self.R1}\\,\\Omega\\\\"
            f"\\text{{Branch 2 resistance, }} R_2 &= {self.R2}\\,\\Omega\\\\"
            f"\\text{{Step 1: Calculate the equivalent resistance of the parallel network (}} R_p \\text{{).}} &\\\\"
            f"R_p &= \\frac{{R_1 R_2}}{{R_1 + R_2}} = \\frac{{{self.R1} \\times {self.R2}}}{{{self.R1} + {self.R2}}}\\\\"
            f"R_p &= {round((self.R1 * self.R2) / (self.R1 + self.R2), 10)}\\,\\Omega\\\\"
            f"\\text{{Step 2: Find the total circuit resistance (}} R_{{total}} \\text{{) and total current (}} I_t \\text{{).}} &\\\\"
            f"R_{{total}} &= R_s + R_p = {self.Rs} + {round((self.R1 * self.R2) / (self.R1 + self.R2), 10)}\\\\"
            f"R_{{total}} &= {round(self.Rs + (self.R1 * self.R2) / (self.R1 + self.R2), 10)}\\,\\Omega\\\\"
            f"I_t &= \\frac{{V_s}}{{R_{{total}}}} = \\frac{{{self.Vs}}}{{{round(self.Rs + (self.R1 * self.R2) / (self.R1 + self.R2), 10)}}}\\\\"
            f"I_t &= {sig_figs(self.It, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Step 3: Solve for the target current using Kirchhoff's laws.}} &\\\\"
            + (
                f"\\text{{The requested value is the total current:}} &\\\\"
                f"I_t &= {self.answer}\\,\\text{{A}}"
                if self.target == "It" else
                f"\\text{{Potential difference across parallel part: }} V_p = I_t R_p &\\\\"
                f"V_p &= {sig_figs(self.It, 3)} \\times {round((self.R1 * self.R2) / (self.R1 + self.R2), 10)} = {round(self.It * (self.R1 * self.R2) / (self.R1 + self.R2), 10)}\\,\\text{{V}}\\\\"
                f"I_1 &= \\frac{{V_p}}{{R_1}} = \\frac{{{round(self.It * (self.R1 * self.R2) / (self.R1 + self.R2), 10)}}}{{{self.R1}}}\\\\"
                f"I_1 &= {self.answer}\\,\\text{{A}}"
                if self.target == "I1" else
                f"\\text{{Potential difference across parallel part: }} V_p = I_t R_p &\\\\"
                f"V_p &= {sig_figs(self.It, 3)} \\times {round((self.R1 * self.R2) / (self.R1 + self.R2), 10)} = {round(self.It * (self.R1 * self.R2) / (self.R1 + self.R2), 10)}\\,\\text{{V}}\\\\"
                f"I_2 &= \\frac{{V_p}}{{R_2}} = \\frac{{{round(self.It * (self.R1 * self.R2) / (self.R1 + self.R2), 10)}}}{{{self.R2}}}\\\\"
                f"I_2 &= {self.answer}\\,\\text{{A}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}\\,\\text{{A}}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.4, 4.8))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        xL, xR = 2.0, 8.8
        top_y, bot_y = 8.6, 2.0

        # Cell on left
        y_cell_top, y_cell_bot = 7.2, 3.4
        draw_wire(ax, [(xL, top_y), (xL, y_cell_top)], lw=2)
        draw_wire(ax, [(xL, y_cell_bot), (xL, bot_y)], lw=2)
        draw_cell_vertical(ax, x=xL, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=f"{self.Vs} V", fontsize=9)

        # Right vertical and bottom wire
        draw_wire(ax, [(xR, bot_y), (xR, top_y)], lw=2)
        draw_wire(ax, [(xL, bot_y), (xR, bot_y)], lw=2)

        # Series resistor on top wire (left side)
        wR, hR = 1.2, 0.6
        x_Rs = 3.8
        Rs_left, Rs_right = (x_Rs - wR/2, top_y), (x_Rs + wR/2, top_y)
        draw_wire(ax, [(xL, top_y), Rs_left], lw=2)
        draw_wire(ax, [Rs_right, (5.0, top_y)], lw=2)
        draw_resistor_box(ax, x=x_Rs, y=top_y, w=wR, h=hR, label="Rs", value_text=f"{self.Rs} Ω", fontsize=9)

        # Parallel network between node A (x=5) and node B (x=7.4)
        xA, xB = 5.0, 7.4
        y_top_branch, y_bot_branch = 7.0, 3.6

        # Node wires
        draw_wire(ax, [(xA, top_y), (xA, y_top_branch)], lw=2)
        draw_wire(ax, [(xA, top_y), (xA, y_bot_branch)], lw=2)
        draw_wire(ax, [(xB, y_top_branch), (xB, y_bot_branch)], lw=2)

        # Connect from series node to xB then to right vertical
        draw_wire(ax, [(xA, top_y), (xB, top_y)], lw=2)
        draw_wire(ax, [(xB, top_y), (xR, top_y)], lw=2)

        # Top branch resistor R1
        x_R1 = (xA + xB) / 2
        R1_left, R1_right = (x_R1 - wR/2, y_top_branch), (x_R1 + wR/2, y_top_branch)
        draw_wire(ax, [(xA, y_top_branch), R1_left], lw=2)
        draw_wire(ax, [R1_right, (xB, y_top_branch)], lw=2)
        draw_resistor_box(ax, x=x_R1, y=y_top_branch, w=wR, h=hR, label="R1", value_text=f"{self.R1} Ω", fontsize=9)

        # Bottom branch resistor R2
        x_R2 = (xA + xB) / 2
        R2_left, R2_right = (x_R2 - wR/2, y_bot_branch), (x_R2 + wR/2, y_bot_branch)
        draw_wire(ax, [(xA, y_bot_branch), R2_left], lw=2)
        draw_wire(ax, [R2_right, (xB, y_bot_branch)], lw=2)
        draw_resistor_box(ax, x=x_R2, y=y_bot_branch, w=wR, h=hR, label="R2", value_text=f"{self.R2} Ω", fontsize=9)

        # Current labels
        if self.target == "It":
            draw_text(ax, 9.2, 9.2, "I_total = ?", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 8.4, f"I1 = {sig_figs(self.I1,3)} A", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 7.6, f"I2 = {sig_figs(self.I2,3)} A", fontsize=9, ha="right", boxed=True)
        elif self.target == "I1":
            draw_text(ax, 9.2, 9.2, f"I_total = {sig_figs(self.It,3)} A", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 8.4, "I1 = ?", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 7.6, f"I2 = {sig_figs(self.I2,3)} A", fontsize=9, ha="right", boxed=True)
        else:
            draw_text(ax, 9.2, 9.2, f"I_total = {sig_figs(self.It,3)} A", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 8.4, f"I1 = {sig_figs(self.I1,3)} A", fontsize=9, ha="right", boxed=True)
            draw_text(ax, 9.2, 7.6, "I2 = ?", fontsize=9, ha="right", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy119:
    """
    Kirchhoff’s laws: parallel branches.
    Same p.d. across each branch: V = I1 R1 = I2 R2.
    Dynamic target: find R2 OR supply voltage V.
    """

    def __init__(self):
        self.target = rnd.choice(["R2", "V"])

        while True:
            self.R1 = rnd.randint(3, 30)  # Ω
            self.I1 = rnd.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])
            self.V = self.R1 * self.I1

            self.I2 = rnd.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50])
            self.R2 = self.V / self.I2

            if 1.0 <= self.V <= 24.0 and 2 <= self.R2 <= 60:
                break

        if self.target == "R2":
            self.answer = sig_figs(self.R2, 3)
        else:
            self.answer = sig_figs(self.V, 3)

        self.description = (
            "Two resistors are connected in parallel. The branch currents are shown in the diagram.\n"
            "Using Kirchhoff’s laws, determine the required quantity.\n"
            "Answer = (_)"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Kirchhoff’s laws"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Branch 1: }} R_1 &= {self.R1}\\,\\Omega, \\, I_1 = {sig_figs(self.I1, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Branch 2: }} R_2 &= {'\\text{?}' if self.target == 'R2' else sig_figs(self.R2, 3)}\\,\\Omega, \\, I_2 = {sig_figs(self.I2, 3)}\\,\\text{{A}}\\\\"
            f"\\text{{Supply Voltage, }} V &= {'\\text{?}' if self.target == 'V' else sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Step 1: Apply Kirchhoff's Second Law to the parallel branches.}} &\\\\"
            f"\\text{{In a parallel circuit, the potential difference across each branch is equal}} &\\\\"
            f"\\text{{to the supply voltage (assuming no internal resistance):}} &\\\\"
            f"V &= I_1 R_1 = I_2 R_2\\\\"
            f"\\text{{Step 2: Calculate the potential difference using the known values for Branch 1.}} &\\\\"
            f"V &= {sig_figs(self.I1, 3)} \\times {self.R1}\\\\"
            f"V &= {sig_figs(self.V, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Step 3: Solve for the target variable.}} &\\\\"
            + (
                f"\\text{{The requested value is the supply voltage:}} &\\\\"
                f"V &= {self.answer}\\,\\text{{V}}"
                if self.target == "V" else
                f"\\text{{Using }} V = I_2 R_2 \\text{{ for Branch 2:}} &\\\\"
                f"R_2 &= \\frac{{V}}{{I_2}} = \\frac{{{sig_figs(self.V, 3)}}}{{{sig_figs(self.I2, 3)}}}\\\\"
                f"R_2 &= {self.answer}\\,\\Omega"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.0, 2.5
        left_x, right_x = 2.0, 8.0

        # Top bus and bottom bus
        draw_wire(ax, [(left_x, top_y), (right_x, top_y)], lw=2)
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # Left vertical split for cell
        y_cell_top, y_cell_bot = 7.2, 3.3
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)

        if self.target == "V":
            cell_text = "V = ?"
        else:
            cell_text = f"V = {sig_figs(self.V,3)} V"
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=cell_text, fontsize=9)

        # Two parallel branch resistors
        x1, x2 = 5.4, 7.0
        wR, hR = 1.2, 0.6

        # R1 branch
        r1_top, r1_bot = draw_resistor_box(ax, x=x1, y=5.9, label="R1",
                                           value_text=f"{self.R1} Ω", fontsize=9)
        draw_wire(ax, [(x1, top_y), (x1, r1_top)], lw=2)
        draw_wire(ax, [(x1, r1_bot), (x1, bot_y)], lw=2)
        draw_text(ax, x1 + 0.7, 6.8, f"I1 = {sig_figs(self.I1,3)} A", fontsize=9, ha="left", boxed=True)

        # R2 branch (maybe unknown)
        if self.target == "R2":
            r2_value = "R2 = ?"
        else:
            r2_value = f"{sig_figs(self.R2,3)} Ω"
        r2_top, r2_bot = draw_resistor_box(ax, x=x2, y=5.0, label="R2",
                                           value_text=r2_value, fontsize=9)
        draw_wire(ax, [(x2, top_y), (x2, r2_top)], lw=2)
        draw_wire(ax, [(x2, r2_bot), (x2, bot_y)], lw=2)
        draw_text(ax, x2 + 0.7, 5.9, f"I2 = {sig_figs(self.I2,3)} A", fontsize=9, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy120:
    """
    Potential dividers (D.C. circuits).
    Two resistors in series across a supply. Output V_out across R2.
    Dynamic target: V_out OR R2 OR R1.
    """

    def __init__(self):
        self.target = rnd.choice(["Vout", "R2", "R1"])

        while True:
            self.Vs = rnd.choice([6, 9, 12, 15, 18, 24])
            self.R1 = rnd.choice([100, 150, 220, 330, 470, 680, 1000, 1500])
            self.R2 = rnd.choice([100, 150, 220, 330, 470, 680, 1000, 1500])

            self.Vout = self.Vs * self.R2 / (self.R1 + self.R2)

            if 0.8 <= self.Vout <= (self.Vs - 0.8):
                break

        if self.target == "Vout":
            self.answer = sig_figs(self.Vout, 3)
        elif self.target == "R2":
            self.answer = sig_figs(self.R2, 3)
        else:
            self.answer = sig_figs(self.R1, 3)

        self.description = (
            "A potential divider is connected across a supply. All values are shown in the diagram.\n"
            "Determine the required quantity.\n"
            "Answer = (_)"
        )

        self.topic = "D.C. circuits"
        self.subtopic = "Potential dividers"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Resistance, }} R_1 &= {'\\text{?}' if self.target == 'R1' else self.R1}\\,\\Omega\\\\"
            f"\\text{{Resistance, }} R_2 &= {'\\text{?}' if self.target == 'R2' else self.R2}\\,\\Omega\\\\"
            f"\\text{{Output voltage, }} V_{{out}} &= {'\\text{?}' if self.target == 'Vout' else sig_figs(self.Vout, 3)}\\,\\text{{V}}\\\\"
            f"\\text{{Step 1: Identify the potential divider formula.}} &\\\\"
            f"\\text{{The output voltage }} V_{{out}} \\text{{ across }} R_2 \\text{{ in a series circuit is given by:}} &\\\\"
            f"V_{{out}} &= V_s \\times \\frac{{R_2}}{{R_1 + R_2}}\\\\"
            f"\\text{{Step 2: Rearrange and substitute to solve for the target variable:}} &\\\\"
            + (
                f"V_{{out}} &= {self.Vs} \\times \\frac{{{self.R2}}}{{{self.R1} + {self.R2}}}\\\\"
                f"V_{{out}} &= {self.Vs} \\times \\frac{{{self.R2}}}{{{self.R1 + self.R2}}}\\\\"
                f"V_{{out}} &= {self.answer}\\,\\text{{V}}"
                if self.target == "Vout" else
                f"\\frac{{V_{{out}}}}{{V_s}} &= \\frac{{R_2}}{{R_1 + R_2}} \\implies \\frac{{{sig_figs(self.Vout, 3)}}}{{{self.Vs}}} = \\frac{{R_2}}{{{self.R1} + R_2}}\\\\"
                f"{round(self.Vout/self.Vs, 10)} ( {self.R1} + R_2 ) &= R_2\\\\"
                f"{round(self.Vout/self.Vs * self.R1, 10)} &= R_2 (1 - {round(self.Vout/self.Vs, 10)})\\\\"
                f"R_2 &= {self.answer}\\,\\Omega"
                if self.target == "R2" else
                f"\\frac{{V_{{out}}}}{{V_s}} &= \\frac{{R_2}}{{R_1 + R_2}} \\implies \\frac{{{sig_figs(self.Vout, 3)}}}{{{self.Vs}}} = \\frac{{{self.R2}}}{{R_1 + {self.R2}}}\\\\"
                f"R_1 + {self.R2} &= \\frac{{{self.R2} \\times {self.Vs}}}{{{sig_figs(self.Vout, 3)}}}\\\\"
                f"R_1 &= {round(self.R2 * self.Vs / self.Vout, 10)} - {self.R2}\\\\"
                f"R_1 &= {self.answer}\\,\\Omega"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.2, 4.2))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        left_x, right_x = 2.0, 8.8
        top_y, bot_y = 8.0, 2.0

        # Cell on left
        y_cell_top, y_cell_bot = 7.0, 3.0
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top, value_text=f"{self.Vs} V", fontsize=9)

        # Right vertical + bottom wire
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # Two resistors in series on top wire: R1 then R2
        wR, hR = 1.2, 0.6
        x_R1 = 4.8
        x_R2 = 7.0

        # Wires and components
        draw_wire(ax, [(left_x, top_y), (x_R1 - wR/2, top_y)], lw=2)
        draw_wire(ax, [(x_R1 + wR/2, top_y), (x_R2 - wR/2, top_y)], lw=2)
        draw_wire(ax, [(x_R2 + wR/2, top_y), (right_x, top_y)], lw=2)

        if self.target == "R1":
            r1_text = "R1 = ?"
        else:
            r1_text = f"{self.R1} Ω"
        draw_resistor_box(ax, x=x_R1, y=top_y, w=wR, h=hR, label="R1", value_text=r1_text, fontsize=9)

        if self.target == "R2":
            r2_text = "R2 = ?"
        else:
            r2_text = f"{self.R2} Ω"
        draw_resistor_box(ax, x=x_R2, y=top_y, w=wR, h=hR, label="R2", value_text=r2_text, fontsize=9)

        # Voltmeter across R2 shows Vout (or unknown)
        x_vm, y_vm, r_vm = x_R2, top_y + 1.2, 0.35
        R2_left = (x_R2 - wR/2, top_y)
        R2_right = (x_R2 + wR/2, top_y)

        draw_wire(ax, [R2_left, (R2_left[0], y_vm)], lw=2)
        draw_wire(ax, [R2_right, (R2_right[0], y_vm)], lw=2)
        draw_wire(ax, [(R2_left[0], y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (R2_right[0], y_vm)], lw=2)
        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=9)

        if self.target == "Vout":
            vout_text = "Vout = ?"
        else:
            vout_text = f"Vout = {sig_figs(self.Vout,3)} V"
        draw_text(ax, x_vm, y_vm + 0.75, vout_text, fontsize=9, boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy121:
    """
    Uniform circular motion (kinematics).
    Use: v = 2πr / T
    Dynamic target: find speed v, OR period T, OR radius r
    """

    def __init__(self):
        self.target = rnd.choice(["v", "T", "r"])

        while True:
            self.r = rnd.choice([0.50, 0.75, 1.00, 1.25, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00])  # m
            self.T = rnd.choice([0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00, 10.0, 12.0])  # s
            self.v = (2 * math.pi * self.r) / self.T  # m/s

            if 0.5 <= self.v <= 30:
                break

        if self.target == "v":
            self.answer = sig_figs(self.v, 3)
        elif self.target == "T":
            self.answer = sig_figs(self.T, 3)
        else:
            self.answer = sig_figs(self.r, 3)

        self.description = (
            "A particle moves with uniform circular motion in a horizontal circle.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Kinematics of uniform circular motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Radius, }} r &= {'\\text{?}' if self.target == 'r' else sig_figs(self.r, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Period, }} T &= {'\\text{?}' if self.target == 'T' else sig_figs(self.T, 3)}\\,\\text{{s}}\\\\"
            f"\\text{{Orbital speed, }} v &= {'\\text{?}' if self.target == 'v' else sig_figs(self.v, 3)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Step 1: Identify the relationship for uniform circular motion.}} &\\\\"
            f"\\text{{The speed }} v \\text{{ is the distance traveled in one period (the circumference) divided}} &\\\\"
            f"\\text{{by the period }} T: &\\\\"
            f"v &= \\frac{{2 \\pi r}}{{T}}\\\\"
            f"\\text{{Step 2: Rearrange and substitute the known values to solve for the target:}} &\\\\"
            + (
                f"v &= \\frac{{2 \\pi \\times {self.r}}}{{{self.T}}}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
                if self.target == "v" else
                f"T &= \\frac{{2 \\pi r}}{{v}} = \\frac{{2 \\pi \\times {self.r}}}{{{sig_figs(self.v, 3)}}}\\\\"
                f"T &= {self.answer}\\,\\text{{s}}"
                if self.target == "T" else
                f"r &= \\frac{{v T}}{{2 \\pi}} = \\frac{{{sig_figs(self.v, 3)} \\times {self.T}}}{{2 \\pi}}\\\\"
                f"r &= {self.answer}\\,\\text{{m}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        cx, cy = 4.7, 5.2
        Rdisp = 3.0

        circ = patches.Circle((cx, cy), Rdisp, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(circ)

        # point on circle
        th = math.radians(40)
        px = cx + Rdisp * math.cos(th)
        py = cy + Rdisp * math.sin(th)
        ax.plot([px], [py], "ko", markersize=4)

        # radius arrow
        ax.annotate("", xy=(px, py), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        mx, my = (cx + px) / 2, (cy + py) / 2

        r_text = "r = ?" if self.target == "r" else f"r = {sig_figs(self.r,3)} m"
        draw_text(ax, mx - 0.1, my + 0.35, r_text, fontsize=9, boxed=True)

        # tangential velocity arrow
        tx, ty = -math.sin(th), math.cos(th)
        L = 1.8
        ax.annotate("", xy=(px + L * tx, py + L * ty), xytext=(px, py),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        v_text = "v = ?" if self.target == "v" else f"v = {sig_figs(self.v,3)} m s⁻¹"
        draw_text(ax, px + L * tx + 0.2, py + L * ty + 0.1, v_text, fontsize=9, ha="left", boxed=True)

        # period label near top
        T_text = "T = ?" if self.target == "T" else f"T = {sig_figs(self.T,3)} s"
        draw_text(ax, cx + 0.1, cy + Rdisp + 0.8, T_text, fontsize=9, boxed=True)

        # direction hint (small curved arrow)
        arc = patches.Arc((cx, cy), 2 * Rdisp, 2 * Rdisp, angle=0, theta1=10, theta2=70, linewidth=2)
        ax.add_patch(arc)
        ax.annotate("", xy=(cx + Rdisp * math.cos(math.radians(70)), cy + Rdisp * math.sin(math.radians(70))),
                    xytext=(cx + Rdisp * math.cos(math.radians(66)), cy + Rdisp * math.sin(math.radians(66))),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy122:
    """
    Uniform circular motion (angular displacement).
    Use: ω = Δθ / Δt; v = rω; s = rΔθ
    Dynamic target: find ω, OR v, OR arc length s from A to B
    """

    def __init__(self):
        self.target = rnd.choice(["omega", "v", "s"])

        while True:
            self.r = rnd.choice([0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00])  # m
            self.dtheta = rnd.choice([math.pi/6, math.pi/4, math.pi/3, math.pi/2, 2*math.pi/3, 3*math.pi/4, 5*math.pi/6])  # rad
            self.dt = rnd.choice([0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00])  # s

            self.omega = self.dtheta / self.dt  # rad/s
            self.v = self.r * self.omega        # m/s
            self.s = self.r * self.dtheta       # m

            if 0.2 <= self.v <= 25 and 0.2 <= self.omega <= 15:
                break

        if self.target == "omega":
            self.answer = sig_figs(self.omega, 3)
        elif self.target == "v":
            self.answer = sig_figs(self.v, 3)
        else:
            self.answer = sig_figs(self.s, 3)

        self.description = (
            "A particle moves with uniform circular motion.\n"
            "It moves from position A to position B in a time interval Δt, as shown.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Kinematics of uniform circular motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Radius, }} r &= {sig_figs(self.r, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Angular displacement, }} \\Delta\\theta &= {sig_figs(self.dtheta, 3)}\\,\\text{{rad}}\\\\"
            f"\\text{{Time interval, }} \\Delta t &= {sig_figs(self.dt, 3)}\\,\\text{{s}}\\\\"
            f"\\text{{Step 1: Calculate the angular speed (}} \\omega \\text{{).}} &\\\\"
            f"\\text{{Angular speed is the rate of change of angular displacement:}} &\\\\"
            f"\\omega &= \\frac{{\\Delta\\theta}}{{\\Delta t}}\\\\"
            f"\\omega &= \\frac{{{sig_figs(self.dtheta, 3)}}}{{{sig_figs(self.dt, 3)}}}\\\\"
            f"\\omega &= {sig_figs(self.omega, 3)}\\,\\text{{rad s}}^{{-1}}\\\\"
            f"\\text{{Step 2: Solve for the specific target variable.}} &\\\\"
            + (
                f"\\text{{The requested value is the angular speed:}} &\\\\"
                f"\\omega &= {self.answer}\\,\\text{{rad s}}^{{-1}}"
                if self.target == "omega" else
                f"\\text{{The linear speed }} v \\text{{ is related to angular speed by }} v = r\\omega: &\\\\"
                f"v &= {sig_figs(self.r, 3)} \\times {sig_figs(self.omega, 3)}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
                if self.target == "v" else
                f"\\text{{The arc length }} s \\text{{ is given by the product of radius and angular displacement:}} &\\\\"
                f"s &= r \\Delta\\theta\\\\"
                f"s &= {sig_figs(self.r, 3)} \\times {sig_figs(self.dtheta, 3)}\\\\"
                f"s &= {self.answer}\\,\\text{{m}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.0, 4.4))
        setup_ax(ax, xlim=(0, 12), ylim=(0, 10))

        cx, cy = 5.0, 5.2
        Rdisp = 3.0

        ax.add_patch(patches.Circle((cx, cy), Rdisp, fill=False, linewidth=2, edgecolor="black"))

        # Choose a start angle for A; B is A + Δθ
        thA = math.radians(20)
        thB = thA + self.dtheta

        Ax = cx + Rdisp * math.cos(thA)
        Ay = cy + Rdisp * math.sin(thA)
        Bx = cx + Rdisp * math.cos(thB)
        By = cy + Rdisp * math.sin(thB)

        ax.plot([Ax], [Ay], "ko", markersize=4)
        ax.plot([Bx], [By], "ko", markersize=4)

        draw_text(ax, Ax + 0.2, Ay + 0.2, "A", fontsize=9, ha="left", boxed=True)
        draw_text(ax, Bx + 0.2, By + 0.2, "B", fontsize=9, ha="left", boxed=True)

        # Radii to A and B
        ax.plot([cx, Ax], [cy, Ay], color="black", linewidth=2)
        ax.plot([cx, Bx], [cy, By], color="black", linewidth=2)

        # Radius label along radius to A
        rm_x, rm_y = (cx + Ax) / 2, (cy + Ay) / 2
        draw_text(ax, rm_x - 0.2, rm_y - 0.65, f"r = {sig_figs(self.r,3)} m", fontsize=9, boxed=True)

        # Arc showing Δθ
        theta1 = math.degrees(thA)
        theta2 = math.degrees(thB)
        arc = patches.Arc((cx, cy), 2 * Rdisp, 2 * Rdisp, angle=0,
                          theta1=theta1, theta2=theta2, linewidth=2)
        ax.add_patch(arc)

        # Small arrow at end of arc for direction
        th_arrow = thB - 0.12
        x1 = cx + Rdisp * math.cos(th_arrow)
        y1 = cy + Rdisp * math.sin(th_arrow)
        x2 = cx + Rdisp * math.cos(thB)
        y2 = cy + Rdisp * math.sin(thB)
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        draw_text(ax, cx + 0.9, cy + 0.3, f"Δθ = {sig_figs(self.dtheta,3)} rad", fontsize=9, boxed=True)
        draw_text(ax, cx - 0.2, cy - Rdisp - 1.0, f"Δt = {sig_figs(self.dt,3)} s", fontsize=9, boxed=True)

        # Unknown label
        if self.target == "omega":
            draw_text(ax, 9.3, 8.2, "ω = ?", fontsize=9, ha="left", boxed=True)
        elif self.target == "v":
            draw_text(ax, 9.3, 8.2, "v = ?", fontsize=9, ha="left", boxed=True)
        else:
            draw_text(ax, 9.3, 8.2, "s = ?", fontsize=9, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy123:
    """
    Uniform circular motion with rotation rate.
    Convert n (rpm) to frequency: f = n/60
    Use: ω = 2πf; v = ωr; T = 1/f
    Dynamic target: find ω, OR v (speed at radius r), OR T (period)
    """

    def __init__(self):
        self.target = rnd.choice(["omega", "v", "T"])

        while True:
            self.n = rnd.choice([30, 45, 60, 75, 90, 120, 150, 180, 240])  # rpm
            self.r = rnd.choice([0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])  # m

            self.f = self.n / 60.0
            self.T = 1 / self.f
            self.omega = 2 * math.pi * self.f
            self.v = self.omega * self.r

            if 0.2 <= self.v <= 20:
                break

        if self.target == "omega":
            self.answer = sig_figs(self.omega, 3)
        elif self.target == "v":
            self.answer = sig_figs(self.v, 3)
        else:
            self.answer = sig_figs(self.T, 3)

        self.description = (
            "A turntable rotates at a constant rate.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Kinematics of uniform circular motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Rotation rate, }} n &= {self.n}\\,\\text{{rpm}}\\\\"
            f"\\text{{Radius, }} r &= {sig_figs(self.r, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Step 1: Convert the rotation rate from rpm to frequency (}} f \\text{{).}} &\\\\"
            f"\\text{{Frequency in Hz is the number of rotations per second:}} &\\\\"
            f"f &= \\frac{{n}}{{60}} = \\frac{{{self.n}}}{{60}} = {self.f}\\,\\text{{Hz}}\\\\"
            f"\\text{{Step 2: Calculate the required quantities.}} &\\\\"
            + (
                f"\\text{{The angular speed }} \\omega \\text{{ is given by }} 2\\pi f: &\\\\"
                f"\\omega &= 2 \\pi \\times {self.f}\\\\"
                f"\\omega &= {self.answer}\\,\\text{{rad s}}^{{-1}}"
                if self.target == "omega" else
                f"\\text{{The period }} T \\text{{ is the time for one complete rotation:}} &\\\\"
                f"T &= \\frac{{1}}{{f}} = \\frac{{1}}{{{self.f}}}\\\\"
                f"T &= {self.answer}\\,\\text{{s}}"
                if self.target == "T" else
                f"\\text{{First, find the angular speed: }} \\omega = 2\\pi f = 2\\pi({self.f}) = {sig_figs(self.omega, 3)}\\,\\text{{rad s}}^{{-1}} &\\\\"
                f"\\text{{Then, use }} v = r\\omega \\text{{ to find the tangential speed:}} &\\\\"
                f"v &= {sig_figs(self.r, 3)} \\times {sig_figs(self.omega, 3)}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        cx, cy = 5.0, 5.0
        Rdisp = 3.0

        ax.add_patch(patches.Circle((cx, cy), Rdisp, fill=False, linewidth=2, edgecolor="black"))

        # Point P on rim-ish
        th = math.radians(35)
        px = cx + Rdisp * math.cos(th)
        py = cy + Rdisp * math.sin(th)
        ax.plot([px], [py], "ko", markersize=4)
        draw_text(ax, px + 0.2, py + 0.2, "P", fontsize=9, ha="left", boxed=True)

        # Radius arrow
        ax.annotate("", xy=(px, py), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        draw_text(ax, (cx + px) / 2 - 0.1, (cy + py) / 2 + 0.35, f"r = {sig_figs(self.r,3)} m", fontsize=9, boxed=True)

        # Direction arc
        arc = patches.Arc((cx, cy), 2 * Rdisp, 2 * Rdisp, angle=0, theta1=10, theta2=80, linewidth=2)
        ax.add_patch(arc)
        ax.annotate("", xy=(cx + Rdisp * math.cos(math.radians(80)), cy + Rdisp * math.sin(math.radians(80))),
                    xytext=(cx + Rdisp * math.cos(math.radians(76)), cy + Rdisp * math.sin(math.radians(76))),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        draw_text(ax, 1.0, 9.2, f"n = {self.n} rpm", fontsize=9, ha="left", boxed=True)

        # Show one derived label and one target
        if self.target == "omega":
            draw_text(ax, 7.3, 8.9, "ω = ?", fontsize=9, ha="left", boxed=True)
        elif self.target == "v":
            # tangential speed arrow at P
            tx, ty = -math.sin(th), math.cos(th)
            L = 1.6
            ax.annotate("", xy=(px + L * tx, py + L * ty), xytext=(px, py),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            draw_text(ax, px + L * tx + 0.2, py + L * ty + 0.1, "v = ?", fontsize=9, ha="left", boxed=True)
        else:
            draw_text(ax, 7.3, 8.9, "T = ?", fontsize=9, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy124:
    """
    Centripetal acceleration.
    Use: a = v^2 / r
    Dynamic target: a, OR v, OR r
    """

    def __init__(self):
        self.target = rnd.choice(["a", "v", "r"])

        while True:
            self.r = rnd.choice([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0, 10.0, 12.0, 15.0, 20.0])  # m
            self.v = rnd.choice([4, 5, 6, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40])  # m/s
            self.a = (self.v ** 2) / self.r  # m/s^2

            if 0.5 <= self.a <= 200:
                break

        if self.target == "a":
            self.answer = sig_figs(self.a, 3)
        elif self.target == "v":
            self.answer = sig_figs(self.v, 3)
        else:
            self.answer = sig_figs(self.r, 3)

        self.description = (
            "A particle moves at constant speed in a horizontal circle.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Centripetal acceleration"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Radius, }} r &= {'\\text{?}' if self.target == 'r' else sig_figs(self.r, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Linear speed, }} v &= {'\\text{?}' if self.target == 'v' else sig_figs(self.v, 3)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Centripetal acceleration, }} a &= {'\\text{?}' if self.target == 'a' else sig_figs(self.a, 3)}\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Step 1: Identify the formula for centripetal acceleration.}} &\\\\"
            f"\\text{{For an object moving in a circle, the acceleration is directed towards the}} &\\\\"
            f"\\text{{centre and its magnitude is given by:}} &\\\\"
            f"a &= \\frac{{v^2}}{{r}}\\\\"
            f"\\text{{Step 2: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"a &= \\frac{{{sig_figs(self.v, 3)}^2}}{{{sig_figs(self.r, 3)}}} = \\frac{{{round(self.v**2, 10)}}}{{{sig_figs(self.r, 3)}}}\\\\"
                f"a &= {self.answer}\\,\\text{{m s}}^{{-2}}"
                if self.target == "a" else
                f"v^2 &= a \\times r = {sig_figs(self.a, 3)} \\times {sig_figs(self.r, 3)} = {round(self.a * self.r, 10)}\\\\"
                f"v &= \\sqrt{{{round(self.a * self.r, 10)}}}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
                if self.target == "v" else
                f"r &= \\frac{{v^2}}{{a}} = \\frac{{{sig_figs(self.v, 3)}^2}}{{{sig_figs(self.a, 3)}}} = \\frac{{{round(self.v**2, 10)}}}{{{sig_figs(self.a, 3)}}}\\\\"
                f"r &= {self.answer}\\,\\text{{m}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        cx, cy = 4.8, 5.2
        Rdisp = 3.0
        ax.add_patch(patches.Circle((cx, cy), Rdisp, fill=False, linewidth=2, edgecolor="black"))

        th = math.radians(35)
        px = cx + Rdisp * math.cos(th)
        py = cy + Rdisp * math.sin(th)
        ax.plot([px], [py], "ko", markersize=4)

        # Radius arrow + label
        ax.annotate("", xy=(px, py), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        r_text = "r = ?" if self.target == "r" else f"r = {sig_figs(self.r,3)} m"
        draw_text(ax, (cx + px) / 2 - 0.1, (cy + py) / 2 + 0.35, r_text, fontsize=9, boxed=True)

        # Velocity arrow tangent
        tx, ty = -math.sin(th), math.cos(th)
        L = 1.8
        ax.annotate("", xy=(px + L * tx, py + L * ty), xytext=(px, py),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        v_text = "v = ?" if self.target == "v" else f"v = {sig_figs(self.v,3)} m s⁻¹"
        draw_text(ax, px + L * tx + 0.2, py + L * ty + 0.1, v_text, fontsize=9, ha="left", boxed=True)

        # Centripetal acceleration arrow (towards centre)
        L2 = 1.6
        ux, uy = (cx - px), (cy - py)
        mag = (ux**2 + uy**2) ** 0.5
        ux, uy = ux / mag, uy / mag
        L2 = 0.90 * mag
        ax.annotate("", xy=(px + L2 * ux, py + L2 * uy), xytext=(px, py),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        a_text = "a = ?" if self.target == "a" else f"a = {sig_figs(self.a,3)} m s⁻²"
        draw_text(ax, px - 1.5, py - 1.5, a_text, fontsize=9, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy125:
    """
    Centripetal acceleration using period.
    Use: a = 4π^2 r / T^2
    Dynamic target: a, OR T, OR r
    """

    def __init__(self):
        self.target = rnd.choice(["a", "T", "r"])

        while True:
            self.r = rnd.choice([0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 8.00, 10.0, 12.0, 15.0])  # m
            self.T = rnd.choice([0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00, 6.00, 8.00])  # s
            self.a = (4 * (math.pi ** 2) * self.r) / (self.T ** 2)

            if 0.5 <= self.a <= 200:
                break

        if self.target == "a":
            self.answer = sig_figs(self.a, 3)
        elif self.target == "T":
            self.answer = sig_figs(self.T, 3)
        else:
            self.answer = sig_figs(self.r, 3)

        self.description = (
            "A particle moves with uniform circular motion.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Centripetal acceleration"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Radius, }} r &= {'\\text{?}' if self.target == 'r' else sig_figs(self.r, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Period, }} T &= {'\\text{?}' if self.target == 'T' else sig_figs(self.T, 3)}\\,\\text{{s}}\\\\"
            f"\\text{{Centripetal acceleration, }} a &= {'\\text{?}' if self.target == 'a' else sig_figs(self.a, 3)}\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Step 1: Identify the formula for centripetal acceleration in terms of period.}} &\\\\"
            f"\\text{{The centripetal acceleration is given by }} a = \\frac{{v^2}}{{r}}. \\text{{ Substituting }} v = \\frac{{2 \\pi r}}{{T}}: &\\\\"
            f"a &= \\frac{{(2 \\pi r / T)^2}}{{r}} = \\frac{{4 \\pi^2 r^2}}{{T^2 r}}\\\\"
            f"a &= \\frac{{4 \\pi^2 r}}{{T^2}}\\\\"
            f"\\text{{Step 2: Rearrange and substitute the known values to solve for the target:}} &\\\\"
            + (
                f"a &= \\frac{{4 \\pi^2 \\times {self.r}}}{{{self.T}^2}} = \\frac{{4 \\pi^2 \\times {self.r}}}{{{round(self.T**2, 10)}}}\\\\"
                f"a &= {self.answer}\\,\\text{{m s}}^{{-2}}"
                if self.target == "a" else
                f"T^2 &= \\frac{{4 \\pi^2 r}}{{a}} = \\frac{{4 \\pi^2 \\times {self.r}}}{{{sig_figs(self.a, 3)}}} = {round((4 * math.pi**2 * self.r) / self.a, 10)}\\\\"
                f"T &= \\sqrt{{{round((4 * math.pi**2 * self.r) / self.a, 10)}}}\\\\"
                f"T &= {self.answer}\\,\\text{{s}}"
                if self.target == "T" else
                f"r &= \\frac{{a T^2}}{{4 \\pi^2}} = \\frac{{{sig_figs(self.a, 3)} \\times {self.T}^2}}{{4 \\pi^2}}\\\\"
                f"r &= \\frac{{{sig_figs(self.a, 3)} \\times {round(self.T**2, 10)}}}{{4 \\pi^2}}\\\\"
                f"r &= {self.answer}\\,\\text{{m}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 4.4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        cx, cy = 4.7, 5.1
        Rdisp = 3.0
        ax.add_patch(patches.Circle((cx, cy), Rdisp, fill=False, linewidth=2, edgecolor="black"))

        th = math.radians(50)
        px = cx + Rdisp * math.cos(th)
        py = cy + Rdisp * math.sin(th)
        ax.plot([px], [py], "ko", markersize=4)

        # radius arrow + label
        ax.annotate("", xy=(px, py), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        r_text = "r = ?" if self.target == "r" else f"r = {sig_figs(self.r,3)} m"
        draw_text(ax, (cx + px) / 2 - 0.1, (cy + py) / 2 + 0.35, r_text, fontsize=9, boxed=True)

        # period label near top
        T_text = "T = ?" if self.target == "T" else f"T = {sig_figs(self.T,3)} s"
        draw_text(ax, cx + 0.3, cy + Rdisp + 0.8, T_text, fontsize=9, boxed=True)

        # centripetal acceleration arrow towards centre
        ux, uy = (cx - px), (cy - py)
        mag = (ux**2 + uy**2) ** 0.5
        ux, uy = ux / mag, uy / mag
        L = 0.9 * mag
        ax.annotate("", xy=(px + L * ux, py + L * uy), xytext=(px, py),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        a_text = "a = ?" if self.target == "a" else f"a = {sig_figs(self.a,3)} m s⁻²"
        draw_text(ax, px - 1.3, py - 2.0, a_text, fontsize=9, ha="left", boxed=True)

        # direction hint
        arc = patches.Arc((cx, cy), 2 * Rdisp, 2 * Rdisp, angle=0, theta1=90, theta2=140, linewidth=2)
        ax.add_patch(arc)
        ax.annotate("", xy=(cx + Rdisp * math.cos(math.radians(140)), cy + Rdisp * math.sin(math.radians(140))),
                    xytext=(cx + Rdisp * math.cos(math.radians(136)), cy + Rdisp * math.sin(math.radians(136))),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()

class Phy126:
    def __init__(self):
        self.mass = rnd.randint(10, 18) * 100
        self.velocity = rnd.randint(20, 35)
        self.radius = rnd.randint(25, 50) * 10
        
        self.fc = (self.mass * (self.velocity**2)) / self.radius
        self.answer = f"{self.fc}"

        self.description = (
            "A car travels around a curved section of a banked road. "
            "The road is banked so that no friction is required for the turn. "
            "Based on the parameters provided in the diagram, calculate the centripetal force acting on the car. "
            "(_) N (Example format: 1250.0)"
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Centripetal Acceleration"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify the given physical quantities} \\\\"
            f"\\text{{Mass, }} m &= {round(self.mass, 10)}\\,\\text{{kg}} \\\\"
            f"\\text{{Velocity, }} v &= {round(self.velocity, 10)}\\,\\text{{m s}}^{{-1}} \\\\"
            f"\\text{{Radius, }} r &= {round(self.radius, 10)}\\,\\text{{m}} \\\\[10pt]"
            "\\textbf{Step 2: State the formula for centripetal force} \\\\"
            "F_c &= \\frac{mv^2}{r} \\\\[10pt]"
            "\\textbf{Step 3: Substitute the values into the equation} \\\\"
            f"F_c &= \\frac{{{round(self.mass, 10)} \\times ({round(self.velocity, 10)})^2}}{{{round(self.radius, 10)}}} \\\\"
            f"F_c &= \\frac{{{round(self.mass, 10)} \\times {round(self.velocity**2, 10)}}}{{{round(self.radius, 10)}}} \\\\[10pt]"
            "\\textbf{Step 4: Calculate the final resultant force} \\\\"
            f"F_c &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        theta_deg = 15
        theta_rad = math.radians(theta_deg)
        
        road_x = [1, 9]
        road_y = [2, 2 + 8 * math.tan(theta_rad)]
        ax.plot([1, 9], [2, 2], color='black', lw=1.5, linestyle='--')
        ax.plot(road_x, road_y, color='black', lw=3)
        
        arc = patches.Arc((1, 2), 3, 3, theta1=0, theta2=theta_deg, color='black', lw=1.5)
        ax.add_patch(arc)
        ax.text(2.8, 2.1, f"{theta_deg}°", fontsize=14, color='black')

        car_center_x = 5
        car_center_y = 2 + (car_center_x - 1) * math.tan(theta_rad)
    
        car = patches.Rectangle((car_center_x-0.7, car_center_y), 1.4, 0.8, 
                                angle=theta_deg, color='white', ec='black', lw=2, zorder=3)
        ax.add_patch(car)

        ax.annotate('', xy=(car_center_x, car_center_y-1.5), xytext=(car_center_x, car_center_y+0.4),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        ax.text(car_center_x + 0.2, car_center_y - 1.4, r"$W$", fontsize=12, color='black')

        n_len = 1.8
        n_dx = -n_len * math.sin(theta_rad)
        n_dy = n_len * math.cos(theta_rad)
        ax.annotate('', xy=(car_center_x + n_dx, car_center_y + n_dy + 0.4), xytext=(car_center_x, car_center_y+0.4),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        ax.text(car_center_x + n_dx - 0.3, car_center_y + n_dy + 0.5, f"$N$", fontsize=12, color='black')

        props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black')
        info_text = f"Mass $m$ = {self.mass} kg\nSpeed $v$ = {self.velocity} m/s\nRadius $r$ = {self.radius} m"
        ax.text(0.5, 7.5, info_text, fontsize=11, bbox=props, va='top')

        ax.text(5, 0.5, "Banked Curve Cross-Section", fontsize=10, ha='center', style='italic')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy127:
    def __init__(self):
        self.G = 6.67430e-11
        self.mass_sun = rnd.uniform(1.98, 2.02) * 1e30 
        self.mass_earth = rnd.uniform(5.97, 5.99) * 1e24 
        self.force = rnd.uniform(3.4, 3.6) * 1e22
        self.r_val = math.sqrt((self.G * self.mass_sun * self.mass_earth) / self.force)
        self.answer = f"{self.r_val}"
        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational force between point masses"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.description = (
            "Based on the masses and gravitational force of attraction provided in the diagram, "
            "calculate the distance between the centres of the planet and the sun. "
            "(_) m (Example format: 150000000000.0)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ given\ quantities} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M_1 = {self.mass_sun:.2e}\\,\\text{{kg}},\ M_2 = {self.mass_earth:.2e}\\,\\text{{kg}} \\\\"
            f"&F = {self.force:.2e}\\,\\text{{N}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Newton's\ Law\ of\ Gravitation} \\\\"
            "&F = \\frac{G M_1 M_2}{r^2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ distance\ (r)} \\\\"
            "&r = \\sqrt{\\frac{G M_1 M_2}{F}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ solve} \\\\"
            f"&r = \\sqrt{{\\frac{{(6.67 \\times 10^{{-11}})({self.mass_sun:.2e})({self.mass_earth:.2e})}}{{{self.force:.2e}}}}} \\\\"
            f"&r = \\mathbf{{{self.answer}\\,\\text{{m}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_orbit_vis = 1.8
        sun_radius = 0.3
        
        sun = plt.Circle((0, 0), sun_radius, color='white', ec='black', lw=2)
        ax.add_patch(sun)
        ax.text(0, 0, "Sun\n$M_1$", ha='center', va='center', fontweight='bold', fontsize=10)
        
        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=0.8, alpha=0.3, fill=False)
        ax.add_patch(orbit)

        ax.plot(r_orbit_vis, 0, 'ko', markersize=10)
        ax.text(r_orbit_vis, 0.2, "Planet\n$M_2$", ha='center', fontweight='bold', fontsize=9)

        ax.annotate('', xy=(r_orbit_vis, -0.5), xytext=(0, -0.5),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text(r_orbit_vis/2, -0.7, "$r = ?$", ha='center', fontsize=12, fontweight='bold')
        
        ax.plot([0, 0], [0, -0.6], 'k:', lw=1)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.6], 'k:', lw=1)

        ax.annotate('', xy=(r_orbit_vis - 0.7, 0), xytext=(r_orbit_vis, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2, mutation_scale=15))
        ax.text(r_orbit_vis - 0.35, 0.13, f"$F = {self.force:.2e}$ N", 
                ha='center', fontsize=10, fontweight='bold')

        data_text = (
            f"Sun mass $M_1$: ${self.mass_sun:.2e}$ kg\n"
            f"Planet mass $M_2$: ${self.mass_earth:.2e}$ kg\n"
            f"$G: 6.67 \\times 10^{{-11}}$ N m$^2$ kg$^{{-2}}$"
        )
        ax.text(-0.5, 1.3, data_text, fontsize=9, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8'))
        ax.set_xlim(-0.8, r_orbit_vis + 0.6)
        ax.set_ylim(-1.0, 1.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy128:
    def __init__(self):
        self.G = 6.67430e-11 
        self.mass_sat = rnd.randint(50, 80) * 100
        self.altitude_km = rnd.randint(15, 25) * 100
        self.radius_planet_km = 6400
        self.force_kn = rnd.uniform(30.0, 45.0)

        self.r_surface = self.radius_planet_km * 1e3
        self.h = self.altitude_km * 1e3
        self.r_total = self.r_surface + self.h
        self.F = self.force_kn * 1e3
        self.m = self.mass_sat
        mass_earth_val = (self.F * (self.r_total**2)) / (self.G * self.m)

        self.answer = f"{mass_earth_val}"
        self.topic = "Gravitational Fields"
        self.subtopic = "Newton's Law of Gravitation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            "A satellite is in a circular orbit at an altitude above the surface of a planet as shown. "
            "Using the parameters provided in the diagram, calculate the mass of the planet. "
            "(_) kg (Example format: 5.97E+24)"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ units\ to\ SI} \\\\"
            f"&r = R + h = {self.radius_planet_km}\\,\\text{{km}} + {self.altitude_km}\\,\\text{{km}} = {self.r_total:.2e}\\,\\text{{m}} \\\\"
            f"&F = {self.force_kn:.1f}\\,\\text{{kN}} = {self.F:.2e}\\,\\text{{N}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Newton's\ Law\ of\ Gravitation} \\\\"
            "&F = \\frac{GMm}{r^2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ to\ solve\ for\ planet\ mass\ (M)} \\\\"
            "&M = \\frac{Fr^2}{Gm} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ values} \\\\"
            f"&M = \\frac{{({self.F:.2e})({self.r_total:.2e})^2}}{{(6.67 \\times 10^{{-11}})({self.m})}} \\\\"
            f"&M = \\mathbf{{{self.answer}\\,\\text{{kg}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        
        r_earth_vis = 1.0
        h_vis = 0.6
        r_orbit_vis = r_earth_vis + h_vis
        limit = r_orbit_vis * 1.4

        planet = plt.Circle((0, 0), r_earth_vis, color='white', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        ax.text(0, 0, "PLANET\n(Mass $M$)", ha='center', va='center', fontsize=10, fontweight='bold')

        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=0.8, fill=False, alpha=0.5)
        ax.add_patch(orbit)

        ax.plot(r_orbit_vis, 0, 'ko', markersize=6, zorder=5)
        ax.text(r_orbit_vis, 0.18, f"Satellite\n$m = {self.m}$ kg", ha='center', fontsize=9, fontweight='bold')

        ax.annotate('', xy=(r_orbit_vis - 0.5, 0), xytext=(r_orbit_vis, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5, mutation_scale=15))
        ax.text(r_orbit_vis - 0.25, 0.1, f"$F = {self.force_kn:.1f}$ kN", ha='center', fontsize=9)

        ax.annotate('', xy=(r_earth_vis, -0.2), xytext=(0, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(r_earth_vis/2, -0.35, f"$R = {self.radius_planet_km}$ km", ha='center', fontsize=9)

        ax.annotate('', xy=(r_orbit_vis, -0.2), xytext=(r_earth_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text((r_earth_vis + r_orbit_vis)/2, -0.35, f"$h = {self.altitude_km}$ km", 
                ha='center', fontsize=9, fontweight='bold')

        ax.annotate('', xy=(r_orbit_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text(r_orbit_vis/2, -1.0, "$r = R + h$", ha='center', fontsize=10, fontweight='bold')

        ax.plot([0, 0], [0, -0.85], 'k:', lw=0.8)
        ax.plot([r_earth_vis, r_earth_vis], [0, -0.25], 'k:', lw=0.8)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.85], 'k:', lw=0.8)

        ax.text(limit*0.7, limit*0.7, "Diagram not to scale", style='italic', fontsize=8, ha='right')

        ax.set_xlim(-0.5, limit)
        ax.set_ylim(-1.2, limit)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy129:
    def __init__(self):
        possible_densities = [(3, 5), (2, 3), (4, 5), (1, 2)]
        possible_g = [(1, 6), (1, 4), (1, 5), (3, 8)]
        
        d_num, d_den = rnd.choice(possible_densities)
        g_num, g_den = rnd.choice(possible_g)
        
        self.rho_m_rho_e = Fraction(d_num, d_den)
        self.g_m_g_e = Fraction(g_num, g_den)

        self.radius_ratio = self.g_m_g_e / self.rho_m_rho_e
        self.answer = f"{self.radius_ratio.numerator} : {self.radius_ratio.denominator}"

        self.description = (
            "Using the relative density and gravitational field strength data provided in the diagram, "
            "determine the ratio of the Moon’s radius $r_M$ to the Earth’s radius $r_E$. "
            "(_) (Example format: 1 : 4)"
        )

        self.topic = "Gravitational Field"
        self.subtopic = "Gravitational field strength"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Express field strength } g \\text{ in terms of density } \\rho \\\\"
            "&g = \\frac{GM}{r^2}, \\quad M = \\rho \\left(\\frac{4}{3}\\pi r^3\\right) \\\\"
            "&g = \\frac{G \\cdot \\rho \\cdot \\frac{4}{3}\\pi r^3}{r^2} = \\frac{4}{3}\\pi G \\rho r \\\\[8pt]"
            "&\\textbf{Step 2: Establish the proportionality} \\\\"
            "&g \\propto \\rho r \\implies \\frac{g_M}{g_E} = \\frac{\\rho_M}{\\rho_E} \\times \\frac{r_M}{r_E} \\\\[8pt]"
            "&\\textbf{Step 3: Substitute the given ratios} \\\\"
            f"&\\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} = \\frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}} \\times \\frac{{r_M}}{{r_E}} \\\\[8pt]"
            "&\\textbf{Step 4: Solve for } \\frac{r_M}{r_E} \\\\"
            f"&\\frac{{r_M}}{{r_E}} = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} \\div \\frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}} = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} \\times \\frac{{{self.rho_m_rho_e.denominator}}}{{{self.rho_m_rho_e.numerator}}} \\\\"
            f"&\\frac{{r_M}}{{r_E}} = \\frac{{{self.radius_ratio.numerator}}}{{{self.radius_ratio.denominator}}} \\\\[8pt]"
            "&\\textbf{Step 5: Final Ratio} \\\\"
            f"&r_M : r_E = \\mathbf{{{self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_E = 1.2
        r_M = r_E * (float(self.radius_ratio.numerator) / float(self.radius_ratio.denominator))
        r_M_vis = max(r_M, 0.3) 

        earth = plt.Circle((0, 0), r_E, color='white', ec='black', lw=2)
        ax.add_artist(earth)
        ax.plot([0, r_E], [0, 0], color='black', lw=1.5)
        ax.text(r_E/2, 0.1, "$r_E$", ha='center', fontsize=12)
        ax.text(0, -r_E-0.3, "EARTH\n" + r"$\rho_E, g_E$", ha='center', weight='bold')

        moon_x = 3.0
        moon = plt.Circle((moon_x, 0), r_M_vis, color='white', ec='black', lw=2)
        ax.add_artist(moon)
        ax.plot([moon_x, moon_x + r_M_vis], [0, 0], color='black', lw=1.5)
        ax.text(moon_x + r_M_vis/2, 0.1, "$r_M$", ha='center', fontsize=12)
        ax.text(moon_x, -r_E-0.3, "MOON\n" + rf"$\rho_M = \frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}}\rho_E$", ha='center', weight='bold')

        ax.text((moon_x)/2, 1.5, f"Given: $g_M = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}}g_E$", 
                ha='center', fontsize=13, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.text((moon_x)/2, -1.8, "*Diagram not to scale", fontsize=10, style='italic', color='black')

        ax.set_xlim(-1.5, moon_x + 1.5)
        ax.set_ylim(-2.2, 2.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy130:
    def __init__(self):
        self.G = 6.67430e-11
        self.planet_diameter_km = rnd.randint(60, 90) * 100 
        self.planet_mass = rnd.uniform(2.0, 5.0) * 1e23
        self.height_km = rnd.randint(2, 6) * 100
        self.rock_mass = rnd.randint(400, 800)

        self.planet_radius_km = self.planet_diameter_km / 2
        self.r_total_m = (self.planet_radius_km + self.height_km) * 1e3

        self.potential = - (self.G * self.planet_mass) / self.r_total_m
        self.answer = f"{self.potential}"

        self.topic = "Gravitational fields"
        self.subtopic = "Gravitational field of a point mass"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            "A rock is located at a distance above a planet's surface as shown. "
            "Using the planet's mass, diameter, and altitude data provided in the diagram, "
            "calculate the gravitational potential at this point. (_) J kg^-1 (Example format: -4.56E+07)"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Identify given values and convert to SI units} \\\\"
            f"&G = {self.G}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.planet_mass:.2e}\\,\\text{{kg}} \\\\"
            f"&R = \\frac{{{self.planet_diameter_km}}}{{2}} = {self.planet_radius_km}\\,\\text{{km}} \\\\"
            f"&h = {self.height_km}\\,\\text{{km}} \\\\[8pt]"
            "&\\textbf{Step 2: Calculate total distance from center } (r) \\\\"
            "&r = R + h \\\\"
            f"&r = ({self.planet_radius_km} + {self.height_km}) \\times 10^3\\,\\text{{m}} \\\\"
            f"&r = {round(self.r_total_m, 10)}\\,\\text{{m}} \\\\[8pt]"
            "&\\textbf{Step 3: Apply the gravitational potential formula} \\\\"
            "&\\phi = -\\frac{GM}{r} \\quad \\text{(Note: independent of rock mass)} \\\\"
            f"&\\phi = -\\frac{{({self.G})({self.planet_mass:.2e})}}{{{round(self.r_total_m, 10)}}} \\\\[8pt]"
            "&\\textbf{Step 4: Final calculation} \\\\"
            f"&\\phi = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 9), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        
        r_planet = 1.5
        h_vis = 1.0
        r_total_vis = r_planet + h_vis

        planet = plt.Circle((0, 0), r_planet, color='white', ec='black', lw=2)
        ax.add_patch(planet)
        ax.text(0, 0, "PLANET\nMass $M$", ha='center', va='center', fontweight='bold', fontsize=12)

        ax.plot(0, 0, 'k+', markersize=10)
        ax.plot(r_total_vis, 0, 'ko', markersize=6) 
        ax.text(r_total_vis, 0.2, f"Rock\n{self.rock_mass} kg", ha='center', fontweight='bold', fontsize=10)

        theta_r = np.radians(135) 
        ax.plot([0, r_planet * np.cos(theta_r)], [0, r_planet * np.sin(theta_r)], 'k--', lw=1.5)
        ax.text(r_planet * 0.5 * np.cos(theta_r) + 0.1, r_planet * 0.5 * np.sin(theta_r) - 0.4, 
                f"$R = {self.planet_radius_km}$ km", fontsize=11, ha='right', fontweight='bold')

        ax.annotate('', xy=(r_total_vis, -0.2), xytext=(r_planet, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text((r_planet + r_total_vis)/2, -0.4, f"$h = {self.height_km}$ km", ha='center', fontsize=11, fontweight='bold')

        ax.annotate('', xy=(r_total_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(r_total_vis/2, -1.0, "$r$", ha='center', fontsize=12, fontweight='bold')

        ax.plot([0, 0], [0, -0.9], 'k:', lw=1)
        ax.plot([r_planet, r_planet], [0, -0.3], 'k:', lw=1)
        ax.plot([r_total_vis, r_total_vis], [0, -0.9], 'k:', lw=1)

        info_box = f"Planet Mass $M = {self.planet_mass:.2e}$ kg\nPlanet Diameter = {self.planet_diameter_km} km"
        ax.text(0.08, 0.98, info_box, transform=ax.transAxes, ha='left', va='top',
                fontsize=11, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.6'))

        ax.text(0.98, 0.02, "*Diagram not to scale", transform=ax.transAxes, 
                ha='right', va='bottom', fontsize=9, style='italic')

        ax.set_xlim(-2.0, 3.5)
        ax.set_ylim(-1.8, 2.2)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy131:
    def __init__(self):
        self.G = 6.67430e-11
        self.planet_diameter_km = rnd.randint(60, 85) * 100 
        self.planet_mass = rnd.uniform(3.0, 6.0) * 1e23
        self.height_km = rnd.randint(3, 7) * 100        
        self.rock_mass = rnd.randint(450, 650)

        self.planet_radius_km = self.planet_diameter_km / 2
        self.total_distance_m = (self.planet_radius_km + self.height_km) * 1e3

        potential_val = -(self.G * self.planet_mass) / self.total_distance_m
        self.answer = f"{potential_val}"

        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational Potential"
        self.source = "Save My Exam"
        self.curriculum = "A-Level"

        self.description = (
            "A rock is located at a specific height above a planet's surface as shown. "
            "Based on the data provided in the diagram, calculate the gravitational potential at the rock's position. "
            "(_) J kg^-1 (Example format: -1.2345e+07)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ given\ quantities\ and\ convert\ to\ SI\ units} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.planet_mass:.2e}\\,\\text{{kg}} \\\\"
            f"&R = \\frac{{{self.planet_diameter_km}}}{{2}} = {self.planet_radius_km}\\,\\text{{km}} = {self.planet_radius_km * 1e3:.2e}\\,\\text{{m}} \\\\"
            f"&h = {self.height_km}\\,\\text{{km}} = {self.height_km * 1e3:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ the\ total\ distance\ from\ the\ centre\ (r)} \\\\"
            "&r = R + h \\\\"
            f"&r = {self.planet_radius_km * 1e3:.2e} + {self.height_km * 1e3:.2e} = {self.total_distance_m:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ the\ gravitational\ potential\ formula} \\\\"
            "&V = -\\frac{GM}{r} \\\\"
            f"&V = -\\frac{{(6.67 \\times 10^{{-11}})({self.planet_mass:.2e})}}{{{self.total_distance_m:.2e}}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Result} \\\\"
            f"&V = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_planet_vis = 1.0
        h_vis = 0.8
        r_orbit_vis = r_planet_vis + h_vis

        planet = plt.Circle((0, 0), r_planet_vis, color='white', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        ax.text(0, 0, "PLANET\n$M = " + f"{self.planet_mass:.1e}" + "$ kg", ha='center', va='center', fontsize=10, fontweight='bold')

        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=1, fill=False, alpha=0.3)
        ax.add_patch(orbit)

        ax.plot(r_orbit_vis, 0, 'ko', markersize=7, zorder=5)
        ax.text(r_orbit_vis, 0.15, f"Rock\n$m = {self.rock_mass}$ kg", ha='center', fontsize=10, fontweight='bold')

        ax.annotate('', xy=(r_planet_vis, -0.2), xytext=(0, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(r_planet_vis/2, -0.4, f"$R = {self.planet_radius_km:g}$ km", ha='center', fontsize=10)

        ax.annotate('', xy=(r_orbit_vis, -0.2), xytext=(r_planet_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text((r_planet_vis + r_orbit_vis)/2, -0.4, f"$h = {self.height_km:g}$ km", 
                ha='center', fontsize=10, fontweight='bold')

        ax.annotate('', xy=(r_orbit_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(r_orbit_vis/2, -1.0, "$r = R + h$", ha='center', fontsize=11, fontweight='bold')

        ax.plot([0, 0], [0, -0.9], 'k:', lw=1)
        ax.plot([r_planet_vis, r_planet_vis], [0, -0.3], 'k:', lw=1)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.9], 'k:', lw=1)

        info_text = f"Planet Diameter = {self.planet_diameter_km} km\n$G = 6.67 \\times 10^{{-11}}$ N m$^2$ kg$^{{-2}}$"
        ax.text(0.02, 0.98, info_text, transform=ax.transAxes, fontsize=10, va='top', ha='left',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_xlim(-1.5, r_orbit_vis + 0.5)
        ax.set_ylim(-1.5, 1.8)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy132:
    def __init__(self):
        self.G = 6.67430e-11 
        self.radius_km = rnd.randint(60, 70) * 100 
        self.mass_earth = rnd.uniform(5.0, 6.5) * 1e24
        self.altitude_km = rnd.randint(10, 25) * 1000

        self.r1 = self.radius_km * 1e3
        self.r2 = (self.radius_km + self.altitude_km) * 1e3

        self.delta_V = -self.G * self.mass_earth * (1/self.r2 - 1/self.r1)
        self.answer = f"{self.delta_V}"

        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational Potential Change"
        self.source = "Original / A-Level Physics"
        self.curriculum = "Cambridge A-Level"

        self.description = (
            "A planet is modeled as an isolated sphere. An object is projected vertically from "
            "the surface of the planet until it reaches a certain altitude. Using the planet's data "
            "provided in the diagram, calculate the change in gravitational potential for this movement. "
            "(_) J kg^-1 (Example format: 44676095.446139514)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Convert all units to SI (meters)} \\\\"
            f"&r_1 = R = {self.radius_km:,}\\,\\text{{km}} = {self.r1:.2e}\\,\\text{{m}} \\\\"
            f"&r_2 = R + h = ({self.radius_km:,} + {self.altitude_km:,})\\,\\text{{km}} = {self.r2:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\textbf{Step 2: State the formula for change in potential } (\\Delta V) \\\\"
            "&\\Delta V = V_2 - V_1 = \\left(-\\frac{GM}{r_2}\\right) - \\left(-\\frac{GM}{r_1}\\right) \\\\"
            "&\\Delta V = GM \\left( \\frac{1}{r_1} - \\frac{1}{r_2} \\right) \\\\[8pt]"
            "&\\textbf{Step 3: Substitute known values} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.mass_earth:.2e}\\,\\text{{kg}} \\\\"
            f"&\\Delta V = (6.67 \\times 10^{{-11}})({self.mass_earth:.2e}) \\left( \\frac{1}{{{self.r1:.2e}}} - \\frac{1}{{{self.r2:.2e}}} \\right) \\\\[8pt]"
            "&\\textbf{Step 4: Final calculation} \\\\"
            f"&\\Delta V = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        
        R_vis = 1.2
        h_vis = 1.0 
        total_r_vis = R_vis + h_vis

        planet = plt.Circle((0, 0), R_vis, color='white', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        
        ax.plot(0, 0, 'k+', markersize=10)
        ax.text(0.1, -0.1, "Centre", fontsize=10, va='top')

        orbit = plt.Circle((0, 0), total_r_vis, color='black', ls='--', lw=1, fill=False, alpha=0.3)
        ax.add_patch(orbit)

        ax.plot(R_vis, 0, 'ko', markersize=6, zorder=5)
        ax.text(R_vis, 0.15, "Initial\nPosition", ha='center', fontsize=10, fontweight='bold')
        
        ax.plot(total_r_vis, 0, 'ko', markersize=6, zorder=5)
        ax.text(total_r_vis, 0.15, "Final\nPosition", ha='center', fontsize=10, fontweight='bold')

        ax.annotate('', xy=(R_vis * np.cos(np.radians(135)), R_vis * np.sin(np.radians(135))), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(-0.3, 0.2, f"$R = {self.radius_km:,}$ km", ha='right', fontsize=11, fontweight='bold')

        ax.annotate('', xy=(total_r_vis, -0.2), xytext=(R_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text((R_vis + total_r_vis)/2, -0.4, f"$h = {self.altitude_km:,}$ km", 
                ha='center', fontweight='bold', fontsize=11)
                
        ax.annotate('', xy=(total_r_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(total_r_vis/2, -1.0, f"$r_2 = R + h$", ha='center', fontsize=11, fontweight='bold')

        ax.plot([0, 0], [0, -0.9], 'k:', lw=1)
        ax.plot([R_vis, R_vis], [0, -0.3], 'k:', lw=1)
        ax.plot([total_r_vis, total_r_vis], [0, -0.9], 'k:', lw=1)
        
        ax.text(0.02, 0.98, f"Planet Mass $M = {self.mass_earth:.2e}$ kg", transform=ax.transAxes,
                fontsize=11, va='top', ha='left', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_xlim(-1.8, total_r_vis + 0.6)
        ax.set_ylim(-1.5, 1.8)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy133:
    def __init__(self):
        self.mass_g = rnd.choice([4, 8, 12, 16]) 
        self.temperature_c = rnd.choice([20, 50, 100, 200]) 
        self.volume_l = rnd.randint(2, 10)
        
        self.molar_mass_he = 4.003e-3
        self.R = 8.314
        self.N_A = 6.022e23
        self.k_B = 1.381e-23
        self.m_atom_he = self.molar_mass_he / self.N_A

        self.temperature_k = self.temperature_c + 273.15
        
        self.c_rms = math.sqrt((3 * self.k_B * self.temperature_k) / self.m_atom_he)
        self.answer = f"{self.c_rms}"

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic Theory of Gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "A rigid vessel contains Helium-4 gas. Assuming Helium behaves as an ideal gas, "
            "use the parameters shown in the diagram to calculate the root-mean-square (r.m.s.) "
            "speed of the helium atoms. (_) m s^-1 (Example format: 1365.234)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Conversion\ to\ SI\ Units} \\\\"
            f"&T = {self.temperature_c} + 273.15 = {self.temperature_k:.2f}\\,\\text{{K}} \\\\"
            f"&m_{{atom}} = \\frac{{M_{{molar}}}}{{N_A}} = \\frac{{4.003 \\times 10^{{-3}}}}{{6.022 \\times 10^{{23}}}} = {self.m_atom_he:.3e}\\,\\text{{kg}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Kinetic\ Theory\ Formula} \\\\"
            "&\\frac{1}{2} m \\langle c^2 \\rangle = \\frac{3}{2} k_B T \\implies c_{rms} = \\sqrt{\\frac{3 k_B T}{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            f"&c_{{rms}} = \\sqrt{{\\frac{{3(1.38 \\times 10^{{-23}})({self.temperature_k:.2f})}}{{{self.m_atom_he:.3e}}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Result} \\\\"
            f"&c_{{rms}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        tank = patches.FancyBboxPatch((0.2, 0.2), 0.6, 0.6, boxstyle="round,pad=0.05", 
                                      fc='none', ec='black', lw=3)
        ax.add_patch(tank)
        
        for _ in range(20):
            px = rnd.uniform(0.25, 0.75)
            py = rnd.uniform(0.25, 0.75)
            ax.plot(px, py, 'o', color='black', markersize=5)
            dx, dy = rnd.uniform(-0.08, 0.08), rnd.uniform(-0.08, 0.08)
            ax.arrow(px, py, dx, dy, head_width=0.015, fc='black', ec='black', alpha=0.7)
            
        ax.text(0.5, 0.9, "Helium-4 Gas", ha='center', fontsize=14, fontweight='bold')
        ax.text(0.88, 0.5, f"$T = {self.temperature_c}^\circ$C", va='center', fontsize=12, fontweight='bold')
        ax.text(0.13, 0.5, f"Mass = {self.mass_g} g", ha='right', va='center', fontsize=12, fontweight='bold')
        ax.text(0.5, 0.1, r"$c_{rms} = \ ?$", ha='center', fontsize=14, fontweight='bold')

        info_box = (
            f"Molar mass = 4.003 g mol$^{{-1}}$\n"
            f"$N_A = 6.022 \\times 10^{{23}}$ mol$^{{-1}}$\n"
            f"$k_B = 1.381 \\times 10^{{-23}}$ J K$^{{-1}}$"
        )
        ax.text(0.05, 0.95, info_box, transform=ax.transAxes, fontsize=10, va='top', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy134:
    def __init__(self):
        while True:
            self.V = rnd.uniform(2.0e-3, 8.0e-3)
            self.T1_c = rnd.randint(10, 40)
            self.delta_T = rnd.randint(15, 50)
            self.T2_c = self.T1_c + self.delta_T
            self.P1 = rnd.uniform(2.0e5, 5.0e5)

            self.T1_k = self.T1_c + 273.15
            self.T2_k = self.T2_c + 273.15

            if 280 <= self.T1_k <= 350:
                break

        self.P2 = self.P1 * self.T2_k / self.T1_k
        self.answer = f"{self.P2}"

        self.topic = "Ideal gases"
        self.subtopic = "Equation of state"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.description = (
            "A rigid container of fixed volume contains an ideal gas. The gas is heated to a new temperature. "
            "Based on the initial and final states shown in the diagram, calculate the final pressure of the gas. "
            "(_) Pa (Example format: 346869.46954977704)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ temperatures\ to\ Kelvin} \\\\"
            f"&T_1 = {self.T1_c} + 273.15 = {self.T1_k:.2f}\\,\\text{{K}} \\\\"
            f"&T_2 = {self.T2_c} + 273.15 = {self.T2_k:.2f}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ Gay-Lussac's\ Law\ (Constant\ Volume)} \\\\"
            "&\\frac{P_1}{T_1} = \\frac{P_2}{T_2} \\implies P_2 = P_1 \\times \\frac{T_2}{T_1} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ final\ pressure} \\\\"
            f"&P_2 = ({self.P1:.2e}) \\times \\frac{{{self.T2_k:.2f}}}{{{self.T1_k:.2f}}} \\\\"
            f"&P_2 = \\mathbf{{{self.answer}\\,\\text{{Pa}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        ax.add_patch(patches.Rectangle((1, 1.5), 2.5, 3, fc='white', ec='black', lw=3))
        for _ in range(25):
            ax.plot(rnd.uniform(1.2, 3.3), rnd.uniform(1.7, 4.3), 'ko', markersize=4)
        
        ax.text(2.25, 5, "Initial State", ha='center', fontweight='bold', fontsize=12)
        ax.text(2.25, 1.1, f"$P_1 = {self.P1:.2e}$ Pa\n$T_1 = {self.T1_c}^\circ$C", ha='center', va='top', fontsize=11, fontweight='bold')

        ax.annotate("", xy=(6, 3), xytext=(4, 3),
                    arrowprops=dict(arrowstyle="->", lw=3, color='black'))
        ax.text(5, 3.4, "HEATING", ha='center', fontweight='bold', fontsize=11)
        ax.text(5, 2.6, f"$V = {self.V:.2e}$ m$^3$\n(Constant)", ha='center', fontsize=10)

        ax.add_patch(patches.Rectangle((6.5, 1.5), 2.5, 3, fc='white', ec='black', lw=3))
        for _ in range(25):
            px, py = rnd.uniform(6.7, 8.8), rnd.uniform(1.7, 4.3)
            ax.plot(px, py, 'ko', markersize=4)
            ax.arrow(px, py, rnd.uniform(-0.15, 0.15), rnd.uniform(-0.15, 0.15), head_width=0.04, color='black')

        ax.text(7.75, 5, "Final State", ha='center', fontweight='bold', fontsize=12)
        ax.text(7.75, 1.1, f"$P_2 = ?$\n$T_2 = {self.T2_c}^\circ$C", ha='center', va='top', fontsize=11, fontweight='bold')

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy135:
    def __init__(self):
        while True:
            self.p1 = rnd.uniform(2.0e5, 5.0e5)
            self.v1 = rnd.uniform(1.0e-3, 3.0e-3)
            self.p2 = rnd.uniform(1.0e5, 3.0e5)
            self.v2 = rnd.uniform(4.0e-3, 6.0e-3)
            
            self.v_total = self.v1 + self.v2
            self.p_final = (self.p1 * self.v1 + self.p2 * self.v2) / self.v_total
            self.answer = f"{self.p_final}"

            if self.p_final > 0:
                break

        self.topic = "Thermal physics"
        self.subtopic = "Ideal gas - Dalton's Law"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "The diagram shows two rigid cylinders, A and B, connected by a tube of "
            "negligible volume with a closed valve. Using the initial parameters provided in the diagram, "
            "calculate the final pressure of the system after the valve is opened and "
            "equilibrium is reached at a constant temperature. (_) Pa (Example format: 291784.95446401695)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Extract\ Data\ from\ Diagram} \\\\"
            f"&\\text{{Cylinder A: }} P_A = {self.p1:.2e}\\,\\text{{Pa}}, \\ V_A = {self.v1:.2e}\\,\\text{{m}}^3 \\\\"
            f"&\\text{{Cylinder B: }} P_B = {self.p2:.2e}\\,\\text{{Pa}}, \\ V_B = {self.v2:.2e}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ Governing\ Principle} \\\\"
            "&\\text{{At constant temperature, the total }} PV \\text{{ product is conserved:}} \\\\"
            "&P_{A}V_{A} + P_{B}V_{B} = P_{final}V_{final} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Total\ Volume} \\\\"
            f"&V_{{total}} = V_A + V_B = {self.v1:.2e} + {self.v2:.2e} = {self.v_total:.2e}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ Solve\ for\ } P_{{final}} \\\\"
            "&P_{{final}} = \\frac{{P_A V_A + P_B V_B}}{{V_{{total}}}} \\\\"
            f"&P_{{final}} = \\frac{{({self.p1:.2e} \\times {self.v1:.2e}) + ({self.p2:.2e} \\times {self.v2:.2e})}}{{{self.v_total:.2e}}} \\\\"
            f"&P_{{final}} = \\mathbf{{{self.answer}\\,\\text{{Pa}}}}"
            "\\end{aligned}\\]"
        )

    def draw_cylinder(self, ax, x_center, width, height):
        x_left = x_center - width/2
        rect = patches.Rectangle((x_left, 1.5), width, height, fc='white', ec='black', lw=2, zorder=2)
        ax.add_patch(rect)
        top = patches.Ellipse((x_center, 1.5 + height), width, width*0.2, fc='white', ec='black', lw=2, zorder=3)
        bottom = patches.Ellipse((x_center, 1.5), width, width*0.2, fc='white', ec='black', lw=2, zorder=1)
        ax.add_patch(top)
        ax.add_patch(bottom)

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis("off")

        self.draw_cylinder(ax, 2.5, 1.8, 3.0)
        ax.text(2.5, 2.8, f"Cylinder A\n$V_A = {self.v1:.2e}$ m$^3$\n$P_A = {self.p1:.2e}$ Pa", ha='center', fontsize=11, fontweight='bold')

        self.draw_cylinder(ax, 7.5, 2.2, 3.5)
        ax.text(7.5, 3.0, f"Cylinder B\n$V_B = {self.v2:.2e}$ m$^3$\n$P_B = {self.p2:.2e}$ Pa", ha='center', fontsize=11, fontweight='bold')

        ax.add_patch(patches.Rectangle((3.4, 2.9), 1.3, 0.4, fc='white', ec='black', lw=2, zorder=1))
        ax.add_patch(patches.Rectangle((5.3, 2.9), 1.1, 0.4, fc='white', ec='black', lw=2, zorder=1))
        
        ax.plot([5, 5], [2.7, 3.5], color='black', lw=4, zorder=5)
        ax.text(5, 2.2, "Valve\n(Closed)", ha='center', fontweight='bold', fontsize=10)

        ax.text(5, 6.2, "ISOTHERMAL GAS MIXING", ha='center', fontsize=14, fontweight='bold')
        ax.text(5, 5.6, r"Find $P_{final}$", ha='center', fontsize=12, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy136:
    def __init__(self):
        while True:
            self.density = rnd.uniform(1.5, 5.0)
            self.pressure = rnd.uniform(2.0e5, 8.0e5)
            self.temperature = rnd.randint(300, 600)

            if self.density > 0 and self.pressure > 0:
                break

        self.v_rms = math.sqrt((3 * self.pressure) / self.density)
        self.answer = f"{self.v_rms}"

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "A sample of an ideal gas is maintained in a rigid container. "
            "Based on the state parameters provided in the diagram, calculate the root-mean-square "
            "(r.m.s.) speed of the gas atoms. (_) m s^-1 (Example format: 709.5655501001263)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ the\ given\ parameters} \\\\"
            f"&P = {self.pressure:.2e}\\,\\text{{Pa}} \\\\"
            f"&\\rho = {self.density:.2f}\\,\\text{{kg m}}^{{-3}} \\\\"
            f"&T = {self.temperature}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ kinetic\ theory\ pressure\ equation} \\\\"
            "&P = \\frac{1}{3} \\rho \\langle c^2 \\rangle \\quad \\text{where } \\sqrt{\\langle c^2 \\rangle} = c_{rms} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ r.m.s.\ speed\ (} c_{rms} \\mathbf{)} \\\\"
            "&c_{rms} = \\sqrt{\\frac{3P}{\\rho}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ values\ and\ calculate} \\\\"
            f"&c_{{rms}} = \\sqrt{{\\frac{{3 \\times {self.pressure:.2e}}}{{{self.density:.2f}}}}} \\\\"
            f"&c_{{rms}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis("off")

        tank_width = 4
        tank_height = 5
        x_start = 3
        y_start = 1.5

        rect = patches.Rectangle((x_start, y_start), tank_width, tank_height, fc='white', ec='black', lw=2, zorder=1)
        ax.add_patch(rect)
        
        top_ellipse = patches.Ellipse((x_start + tank_width/2, y_start + tank_height), tank_width, 0.8, fc='white', ec='black', lw=2, zorder=2)
        ax.add_patch(top_ellipse)
        
        bottom_ellipse = patches.Ellipse((x_start + tank_width/2, y_start), tank_width, 0.8, fc='white', ec='black', lw=2, zorder=0)
        ax.add_patch(bottom_ellipse)

        for _ in range(25):
            px = rnd.uniform(x_start + 0.3, x_start + tank_width - 0.3)
            py = rnd.uniform(y_start + 0.3, y_start + tank_height - 0.3)
            ax.plot(px, py, 'o', color='black', markersize=4, zorder=3)
            
            angle = rnd.uniform(0, 2 * math.pi)
            length = rnd.uniform(0.3, 0.6)
            ax.arrow(px, py, length * math.cos(angle), length * math.sin(angle), 
                     head_width=0.08, fc='black', ec='black', alpha=0.6, zorder=3)

        ax.text(x_start + tank_width/2, y_start + tank_height + 1.0, "Ideal Gas Container", 
                ha='center', fontsize=14, fontweight='bold')

        info_box = (
            f"Pressure ($P$) = {self.pressure:.2e} Pa\n"
            f"Density ($\\rho$) = {self.density:.2f} kg m$^{{-3}}$\n"
            f"Temperature ($T$) = {self.temperature} K"
        )
        ax.text(0.02, 0.98, info_box, transform=ax.transAxes,
                va='top', ha='left', fontsize=11, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.text(x_start - 0.5, y_start + tank_height/2, r"Find $c_{rms}$", 
                ha='right', va='center', fontsize=14, fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy137:
    def __init__(self):
        while True:
            self.v1 = rnd.randint(400, 1200)
            self.T1_c = rnd.randint(10, 50)
            self.delta_T = rnd.randint(100, 300)
            self.T2_c = self.T1_c + self.delta_T

            self.T1_k = self.T1_c + 273.15
            self.T2_k = self.T2_c + 273.15

            if self.T2_k > self.T1_k:
                break

        self.v2 = self.v1 * math.sqrt(self.T2_k / self.T1_k)
        self.answer = f"{self.v2}"
        
        t1_val = f"{self.T1_k:.2f}"
        t2_val = f"{self.T2_k:.2f}"

        self.topic = "Thermal physics"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "Helium behaves as an ideal gas. Based on the initial parameters and the final temperature shown in the diagram, "
            "calculate the final root-mean-square (r.m.s.) speed of the molecules after heating. (_) m s^-1 (Example format: 1234.56)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ temperatures\ to\ Kelvin} \\\\"
            f"&T_1 = {self.T1_c} + 273.15 = {t1_val}\\,\\text{{K}} \\\\"
            f"&T_2 = {self.T2_c} + 273.15 = {t2_val}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ proportional\ relationship} \\\\"
            "&c_{rms} = \\sqrt{\\frac{3kT}{m}} \\implies c_{rms} \\propto \\sqrt{T} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Set\ up\ the\ ratio\ equation} \\\\"
            "&\\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} \\implies v_2 = v_1 \\sqrt{\\frac{T_2}{T_1}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ calculate} \\\\"
            f"&v_2 = {self.v1} \\times \\sqrt{{\\frac{{{t2_val}}}{{{t1_val}}}}} \\\\"
            f"&v_2 = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        def draw_state(x_offset, temp_c, v_rms, label):
            rect = patches.FancyBboxPatch((x_offset, 2), 2.5, 2.5, boxstyle="round,pad=0.1", fc='white', ec='black', lw=2)
            ax.add_patch(rect)
            ax.text(x_offset + 1.25, 5.0, label, ha='center', fontweight='bold', fontsize=12)
            
            for _ in range(15):
                px = rnd.uniform(x_offset + 0.3, x_offset + 2.2)
                py = rnd.uniform(2.3, 4.2)
                ax.plot(px, py, 'ko', markersize=4)
                scale = 0.3 if label == "Initial State" else 0.5
                ax.arrow(px, py, rnd.uniform(-scale, scale), rnd.uniform(-scale, scale), 
                         head_width=0.04, color='black', alpha=0.8)

            v_display = f"{v_rms}" if isinstance(v_rms, int) else "?"
            info = f"$T = {temp_c}^\circ$C\n$v_{{rms}} = {v_display}$ m/s"
            ax.text(x_offset + 1.25, 1.6, info, ha='center', va='top', fontsize=11, fontweight='bold')

        draw_state(1, self.T1_c, self.v1, "Initial State")
        draw_state(6.5, self.T2_c, "v2", "Final State")

        ax.annotate("", xy=(6, 3.25), xytext=(4, 3.25),
                    arrowprops=dict(arrowstyle="->", lw=3, color='black'))
        ax.text(5, 3.5, "HEATING", ha='center', fontweight='bold', fontsize=11)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy138:
    def __init__(self):
        while True:
            self.t_low = rnd.uniform(300, 500)
            self.t_high = self.t_low + rnd.uniform(400, 700)
            self.m_mass_g = 32.0 
            self.m_mass_kg = self.m_mass_g / 1000  
            self.R = 8.31
            
            self.vp_low = np.sqrt(2 * self.R * self.t_low / self.m_mass_kg)
            self.vp_high = np.sqrt(2 * self.R * self.t_high / self.m_mass_kg)
            
            self.answer = f"{self.vp_high}"
            
            if self.vp_high > 500:
                break

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "The provided graph illustrates the distribution of molecular speeds for oxygen gas at two different temperatures. "
            "Identify the characteristics of the distribution and calculate the most probable speed (v_p) for the gas at the higher temperature T_2. "
            "(_) m s^-1 (Example format: 734.9489778209097)"
        )

        t2_val = f"{self.t_high}"
        m_val = f"{self.m_mass_kg:.3f}"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Information\ from\ Graph\ and\ Text} \\\\"
            f"&\\text{{Initial Temperature (}} T_1 \\text{{): }} {self.t_low}\\,\\text{{K}} \\\\"
            f"&\\text{{Target Temperature (}} T_2 \\text{{): }} {t2_val}\\,\\text{{K}} \\\\"
            f"&\\text{{Molar Mass of Oxygen (}} M \\text{{): }} {self.m_mass_g}\\,\\text{{g mol}}^{{-1}} = {m_val}\\,\\text{{kg mol}}^{{-1}} \\\\"
            "&\\text{{Gas Constant (}} R \\text{{): }} 8.31\\,\\text{{J mol}}^{{-1}}\\,\\text{{K}}^{{-1}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Qualitative\ Analysis\ of\ the\ Curves} \\\\"
            "&\\text{{Curve B is broader and its peak is shifted to the right compared to Curve A.}} \\\\"
            "&\\text{{This confirms Curve B represents the higher temperature, }} T_2. \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ Formula\ for\ Most\ Probable\ Speed\ (} v_p \\mathbf{)} \\\\"
            "&v_p = \\sqrt{\\frac{2RT}{M}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitution\ and\ Calculation\ for\ } T_2 \\\\"
            f"&v_p = \\sqrt{{\\frac{{2 \\times 8.31 \\times {t2_val}}}{{{m_val}}}}} \\\\"
            f"&v_p = \\sqrt{{{2 * 8.31 * self.t_high / self.m_mass_kg:.2f}}} \\\\"
            f"&v_p \\approx \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        v = np.linspace(0, 2500, 500)
        
        def maxwell_boltzmann(v, T, M):
            return (M / (2 * np.pi * 8.31 * T))**1.5 * 4 * np.pi * v**2 * np.exp(-M * v**2 / (2 * 8.31 * T))

        f_low = maxwell_boltzmann(v, self.t_low, self.m_mass_kg)
        f_high = maxwell_boltzmann(v, self.t_high, self.m_mass_kg)

        ax.plot(v, f_low, color='black', lw=2.5, ls='-', label=f'Curve A ($T_1 = {self.t_low}$ K)')
        ax.plot(v, f_high, color='black', lw=2.5, ls='--', label=f'Curve B ($T_2 = {self.t_high}$ K)')

        ax.set_xlabel('Molecular Speed $v$ / m s$^{-1}$', fontsize=12, fontweight='bold')
        ax.set_ylabel('Relative Probability $f(v)$', fontsize=12, fontweight='bold')
        ax.set_title('Maxwell-Boltzmann Distribution for Oxygen', fontweight='bold', fontsize=14, pad=15)
        
        ax.legend(frameon=True, loc='upper right', edgecolor='black')
        ax.grid(True, linestyle=':', alpha=0.5, color='black')
        
        ax.set_xlim(0, 1800)
        ax.set_ylim(0, max(f_low) * 1.15)
        
        ax.vlines(self.vp_high, 0, max(f_high), colors='black', linestyles='dotted', lw=2)
        ax.text(self.vp_high + 0.2, max(f_high)*1.05, '$v_p = ?$', ha='center', fontweight='bold')

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300)
        plt.close()


class Phy139:
    def __init__(self):
        while True:
            self.delta_U_kJ = rnd.uniform(30, 80)
            self.Q_kJ = rnd.uniform(10, 60)
            
            self.W_kJ = self.Q_kJ - self.delta_U_kJ
            self.answer = f"{self.W_kJ}"
            self.work_direction = "on the gas" if self.W_kJ < 0 else "by the gas"

            if self.Q_kJ != self.delta_U_kJ:
                break

        self.topic = "Thermal physics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "A monatomic gas is contained within a flexible balloon. "
            "Based on the thermodynamic values provided in the diagram, calculate the magnitude of the work done. "
            "(_) kJ (Example format: 25.0)"
        )

        du_val = f"{self.delta_U_kJ}"
        q_val = f"{self.Q_kJ}"
        w_val = f"{self.W_kJ}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters\ (Sign\ Convention)} \\\\"
            f"&\\text{{Heat supplied to the gas (}} Q \\text{{): }} +{q_val}\\,\\text{{kJ}} \\\\"
            f"&\\text{{Change in internal energy (}} \\Delta U \\text{{): }} +{du_val}\\,\\text{{kJ}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ First\ Law\ of\ Thermodynamics} \\\\"
            "&\\Delta U = Q - W \\quad \\text{{(where }} W \\text{{ is work done by the gas)}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Work\ Done\ (} W \\mathbf{)} \\\\"
            f"&W = Q - \\Delta U \\\\"
            f"&W = {q_val} - {du_val} = {w_val}\\,\\text{{kJ}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Interpret\ the\ Result} \\\\"
            f"&\\text{{Since }} W \\text{{ is negative (}}{w_val}\\,\\text{{kJ), work of }} \\mathbf{{{self.answer}\\,\\text{{kJ}}}} \\\\"
            f"&\\text{{is actually done }} \\mathbf{{{self.work_direction}}}\\text{{ (compression).}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")

        balloon_body = patches.Ellipse((5, 4.5), 4, 4.5, fc='white', ec='black', lw=3, zorder=2)
        ax.add_patch(balloon_body)
        
        nodes = [[4.8, 2.3], [5.2, 2.3], [5, 2.6]]
        polygon = patches.Polygon(nodes, fc='white', ec='black', lw=2, zorder=1)
        ax.add_patch(polygon)

        ax.annotate("", xy=(3.5, 4.5), xytext=(1, 4.5),
                    arrowprops=dict(arrowstyle="->", lw=3, color='black', mutation_scale=20))
        ax.text(1.2, 4.8, f"$Q = +{self.Q_kJ}$ kJ\n(Heat In)", color='black', fontweight='bold', ha='center', fontsize=11)

        ax.annotate("", xy=(8.5, 4.5), xytext=(6.5, 4.5),
                    arrowprops=dict(arrowstyle="<-", lw=3, color='black', mutation_scale=20))
        ax.text(8.5, 4.5, "$W = ?$", color='black', fontsize=14, fontweight='bold', va='center')

        ax.text(5, 4.5, f"$\\Delta U = +{self.delta_U_kJ}$ kJ", 
                ha='center', va='center', fontweight='bold', fontsize=12,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_title("THERMODYNAMICS: BALLOON EXPANSION", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()
        
class Phy140:
    def __init__(self):
        while True:
            self.pressure_kPa = rnd.uniform(100, 400)
            self.delta_U_kJ = rnd.randint(10, 80)
            self.Q_kJ = rnd.randint(100, 200)

            if self.Q_kJ > self.delta_U_kJ:
                break

        self.pressure = self.pressure_kPa * 1000
        self.delta_U = self.delta_U_kJ * 1000
        self.Q = self.Q_kJ * 1000

        self.W = self.Q - self.delta_U
        self.delta_V = self.W / self.pressure
        self.answer = f"{self.delta_V}"

        self.topic = "Thermodynamics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        p_val = f"{self.pressure}"
        du_val = f"{self.delta_U}"
        q_val = f"{self.Q}"
        w_val = f"{self.W}"

        self.description = (
            "An ideal gas is held in a cylinder and expands at a constant pressure. "
            "Using the thermodynamic values shown in the diagram, calculate the magnitude of the change in volume of the gas. "
            "(_) m^3 (Example format: 0.150)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters\ (SI\ Units)} \\\\"
            f"&Q = +{q_val}\\,\\text{{J}} \\\\"
            f"&\\Delta U = +{du_val}\\,\\text{{J}} \\\\"
            f"&P = {p_val}\\,\\text{{Pa}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Work\ Done\ using\ First\ Law} \\\\"
            "&\\Delta U = Q - W \\implies W = Q - \\Delta U \\\\"
            f"&W = {q_val} - {du_val} = {w_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Relate\ Work\ to\ Volume\ Change} \\\\"
            "&\\text{{At constant pressure, }} W = P\\Delta V \\implies \\Delta V = \\frac{W}{P} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitution\ and\ Final\ Calculation} \\\\"
            f"&\\Delta V = \\frac{{{w_val}}}{{{p_val}}} \\\\"
            f"&\\Delta V = \\mathbf{{{self.answer}\\,\\text{{m}}^3}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        cylinder_back = patches.Rectangle((3, 1.5), 4, 6, fc='none', ec='black', lw=3, zorder=0)
        ax.add_patch(cylinder_back)
        
        gas_region = patches.Rectangle((3, 1.5), 4, 3.5, fc='white', hatch='//', alpha=0.5, zorder=1)
        ax.add_patch(gas_region)
        
        for _ in range(25):
            ax.plot(rnd.uniform(3.2, 6.8), rnd.uniform(1.7, 4.8), 'ko', markersize=4, zorder=2)

        piston = patches.Rectangle((3, 4.8), 4, 0.4, fc='white', ec='black', lw=2, zorder=3)
        ax.add_patch(piston)
        piston_rod = patches.Rectangle((4.8, 5.2), 0.4, 2.5, fc='white', ec='black', lw=2, zorder=3)
        ax.add_patch(piston_rod)

        ax.plot([3, 7], [3.5, 3.5], '--', color='black', lw=1.5)
        ax.annotate("", xy=(8, 5), xytext=(8, 3.5),
                    arrowprops=dict(arrowstyle="<->", lw=2, color='black'))
        ax.text(8.3, 4.25, "$\\Delta V = ?$", color='black', fontweight='bold', fontsize=12)

        ax.annotate("", xy=(3.5, 3), xytext=(1.5, 2),
                    arrowprops=dict(arrowstyle="->", lw=3, color='black', mutation_scale=20))
        ax.text(1.0, 1.5, f"$Q = +{self.Q_kJ}$ kJ", color='black', fontweight='bold', ha='center', fontsize=11)

        ax.text(5, 3.2, f"$\\Delta U = +{self.delta_U_kJ}$ kJ", ha='center', fontweight='bold', fontsize=11,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.text(5, 9, f"Constant Pressure\n$P = {self.pressure_kPa}$ kPa", 
                ha='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', ec='black', boxstyle='round,pad=0.5'))

        ax.set_title("GAS EXPANSION IN CYLINDER", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy141:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.1, 0.5)
            self.latent_heat = rnd.uniform(2.2e6, 2.3e6)
            self.pressure = rnd.uniform(1.0e5, 1.02e5)
            self.delta_volume = self.mass * rnd.uniform(1.6, 1.7)

            if self.mass > 0 and self.latent_heat > 0:
                break

        self.Q = self.mass * self.latent_heat
        self.W = self.pressure * self.delta_volume
        self.delta_U = self.Q - self.W
        self.answer = f"{self.delta_U}"

        self.topic = "Thermal physics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        m_str = f"{self.mass:.2f}"
        l_str = f"{self.latent_heat:.2e}"
        p_str = f"{self.pressure:.2e}"
        dv_str = f"{self.delta_volume:.2f}"
        q_val = f"{self.Q:.2e}"
        w_val = f"{self.W:.2e}"

        self.description = (
            "Liquid water at 100°C is completely converted to steam at the same temperature. "
            "Based on the specific data provided in the diagram, calculate the increase in the "
            "internal energy of the system. (_) J (Example format: 734566.9489778209097)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Quantities} \\\\"
            f"&m = {m_str}\\,\\text{{kg}}, \\quad L = {l_str}\\,\\text{{J kg}}^{{-1}} \\\\"
            f"&P = {p_str}\\,\\text{{Pa}}, \\quad \\Delta V = {dv_str}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Thermal\ Energy\ Supplied\ (} Q \\mathbf{)} \\\\"
            "&Q = mL \\\\"
            f"&Q = {m_str} \\times {l_str} = {q_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Work\ Done\ Against\ Atmosphere\ (} W \\mathbf{)} \\\\"
            "&W = P\\Delta V \\\\"
            f"&W = ({p_str}) \\times ({dv_str}) = {w_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Apply\ the\ First\ Law\ of\ Thermodynamics} \\\\"
            "&\\Delta U = Q - W \\\\"
            f"&\\Delta U = {q_val} - {w_val} \\\\"
            f"&\\Delta U = \\mathbf{{{self.answer}\\,\\text{{J}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        beaker = patches.Rectangle((3, 1), 4, 7, fc='none', ec='black', lw=3, zorder=3)
        ax.add_patch(beaker)

        water_level = 2.5
        water = patches.Rectangle((3, 1), 4, water_level - 1, fc='white', hatch='--', ec='black', zorder=2)
        ax.add_patch(water)
        ax.text(5, 1.5, "Liquid Water", ha='center', fontweight='bold')

        for _ in range(25):
            bx = rnd.uniform(3.2, 6.8)
            by = rnd.uniform(water_level + 0.5, 7.5)
            ax.plot(bx, by, 'ko', markersize=3, zorder=3)

        for i in range(5):
            sx = 3.5 + i * 0.75
            ax.annotate("", xy=(sx, 7.5), xytext=(sx, water_level + 0.2),
                        arrowprops=dict(arrowstyle="->", color='black', lw=1.5, ls=':'))

        ax.annotate("", xy=(5, 1), xytext=(5, -0.5),
                    arrowprops=dict(arrowstyle="->", color='black', lw=3))
        ax.text(5, -1.0, f"Heat Source\n$L_v = {self.latent_heat:.2e}$ J/kg", 
                color='black', fontweight='bold', ha='center')

        data_box = (
            f"Mass ($m$) = {self.mass:.2f} kg\n"
            f"Pressure ($P$) = {self.pressure:.2e} Pa\n"
            f"Volume increase $\\Delta V = {self.delta_volume:.2f}$ m$^3$"
        )
        ax.text(0.02, 0.98, data_box, transform=ax.transAxes, va='top', ha='left',
                fontsize=11, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_title("VAPORISATION OF WATER", fontsize=14, fontweight='bold', pad=15)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy142:
    def __init__(self):
        while True:
            self.length = rnd.uniform(0.8, 1.4)
            self.g = 9.81
            self.theta_degrees = rnd.randint(6, 12)
            
            self.period = 2 * math.pi * math.sqrt(self.length / self.g)
            self.omega = 2 * math.pi / self.period
            
            self.theta_rad = math.radians(self.theta_degrees)
            self.max_speed = self.omega * (self.length * self.theta_rad)
            
            if self.max_speed > 0.1:
                break

        self.answer = f"{self.max_speed}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        l_str = f"{self.length:.2f}"
        g_str = f"{self.g:.2f}"
        ang_str = f"{self.theta_degrees}"
        om_str = f"{self.omega:.3f}"
        arc_str = f"{self.length * self.theta_rad:.4f}"

        self.description = (
            "A simple pendulum consists of a small bob attached to a string. "
            "The pendulum is released from rest from the position shown in the diagram. "
            "Assuming the motion is simple harmonic, calculate the maximum speed of the bob "
            f"during its oscillation. (Use g = {g_str} m s\u207b\u00b2). (_) m s^-1 (Example format: 0.126778903)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Information} \\\\"
            f"&L = {l_str}\\,\\text{{m}}, \\quad g = {g_str}\\,\\text{{m s}}^{{-2}}, \\quad \\theta_{{max}} = {ang_str}^\\circ \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Angular\ Frequency\ (} \\omega \\mathbf{)} \\\\"
            f"&\\omega = \\sqrt{{\\frac{{g}}{{L}}}} = \\sqrt{{\\frac{{{g_str}}}{{{l_str}}}}} = {om_str}\\,\\text{{rad s}}^{{-1}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Determine\ Amplitude\ of\ Displacement\ (} x_0 \\mathbf{)} \\\\"
            "&\\text{{For small angles, }} x_0 = L \\theta_{{rad}} \\\\"
            f"&\\theta_{{rad}} = {ang_str} \\times \\frac{{\\pi}}{{180}} \\approx {(self.theta_rad):.4f}\\,\\text{{rad}} \\\\"
            f"&x_0 = {l_str} \\times {(self.theta_rad):.4f} = {arc_str}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Calculate\ Maximum\ Speed\ (} v_{{max}} \\mathbf{)} \\\\"
            "&v_{{max}} = \\omega x_0 \\\\"
            f"&v_{{max}} = {om_str} \\times {arc_str} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(5, 6.5), dpi=300)
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(0, 8.5)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-2.5, 8), 5, 0.3, facecolor='white', edgecolor='black', hatch='///', lw=2, zorder=1))
        ax.plot([-3, 3], [8, 8], color='black', lw=3, zorder=2)

        pivot_x, pivot_y = 0, 8
        v_scale = 5.0
        angle_rad = math.radians(self.theta_degrees)
        bob_x = v_scale * math.sin(angle_rad)
        bob_y = pivot_y - v_scale * math.cos(angle_rad)

        ax.plot([0, 0], [pivot_y, pivot_y - v_scale - 0.6], color='black', linestyle='--', lw=1.5, alpha=0.5)
        ax.plot([pivot_x, bob_x], [pivot_y, bob_y], color='black', lw=2.5, zorder=3)

        ax.text(bob_x/2 + 0.3, (pivot_y + bob_y)/2, f"$L = {self.length:.2f}$ m", 
                color='black', fontweight='bold', fontsize=11, 
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=0.5))

        bob = patches.Circle((bob_x, bob_y), 0.4, facecolor='white', edgecolor='black', lw=2.5, zorder=5)
        ax.add_patch(bob)

        arc_radius = 2.0
        angle_arc = patches.Arc((pivot_x, pivot_y), arc_radius*2, arc_radius*2, 
                                theta1=270, theta2=270+self.theta_degrees, 
                                color='black', lw=2)
        ax.add_patch(angle_arc)
        ax.text(0.5, pivot_y - arc_radius - 0.2, f"$\\theta = {self.theta_degrees}^\\circ$", 
                color='black', fontsize=11, fontweight='bold')

        ax.text(0, pivot_y - v_scale - 1.2, r"Find $v_{max}$ at equilibrium", 
                color='black', fontsize=11, fontweight='bold', ha='center', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        
        ax.set_title("PENDULUM OSCILLATION", fontsize=14, fontweight='bold', pad=15)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy143:
    def __init__(self):
        while True:
            self.num_oscillations = rnd.randint(10, 25)
            self.total_time = rnd.uniform(15.0, 50.0)
            self.period = self.total_time / self.num_oscillations
            self.frequency = 1 / self.period 
            if self.period > 0.4:
                break

        self.answer = f"{self.frequency}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        t_str = f"{self.total_time:.2f}"
        n_str = f"{self.num_oscillations}"
        T_val = f"{self.period:.4f}"

        self.description = (
            "A simple pendulum is observed undergoing small-angle oscillations. "
            "A student uses a stopwatch to measure the time taken for a specific number of complete oscillations. "
            "Using the measurement data from the diagram, determine the frequency of the oscillation. "
            "(_) Hz (Example format: 0.543)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters} \\\\"
            f"&\\text{{Total time, }} t = {t_str}\\,\\text{{s}} \\\\"
            f"&\\text{{Number of oscillations, }} N = {n_str} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ the\ Time\ Period\ (} T \\mathbf{)} \\\\"
            "&T = \\frac{t}{N} \\\\"
            f"&T = \\frac{{{t_str}}}{{{n_str}}} = {T_val}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Frequency\ (} f \\mathbf{)} \\\\"
            "&f = \\frac{1}{T} \\\\"
            f"&f = \\frac{1}{{{T_val}}} = \\mathbf{{{self.answer}\\,\\text{{Hz}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(6, 6.5), dpi=300)
        ax.set_xlim(-4, 4)
        ax.set_ylim(0, 8.5)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-2.5, 8), 5, 0.3, facecolor='white', edgecolor='black', hatch='///', lw=2))
        ax.plot([-3, 3], [8, 8], color='black', lw=3)

        pivot_x, pivot_y = 0, 8
        v_length = 5.0
        angle_deg = 12
        angle_rad = math.radians(angle_deg)
        
        bob_x = v_length * math.sin(angle_rad)
        bob_y = pivot_y - v_length * math.cos(angle_rad)

        ax.plot([0, 0], [pivot_y, pivot_y - v_length - 0.6], color='black', linestyle='--', lw=1.5, alpha=0.5)
        ax.plot([pivot_x, bob_x], [pivot_y, bob_y], color='black', lw=2.5, zorder=2)
        
        path_arc = patches.Arc((pivot_x, pivot_y), v_length*2, v_length*2, 
                               theta1=270-angle_deg, theta2=270+angle_deg, 
                               color='black', linestyle=':', lw=1.5)
        ax.add_patch(path_arc)

        bob = patches.Circle((bob_x, bob_y), 0.35, facecolor='white', edgecolor='black', lw=2.5, zorder=5)
        ax.add_patch(bob)

        ax.annotate("", xy=(-bob_x, bob_y), xytext=(bob_x, bob_y),
                    arrowprops=dict(arrowstyle="<->", connectionstyle="arc3,rad=-0.15", 
                                    color='black', lw=2))

        info_box = (
            f"$\\mathbf{{Stopwatch\\ Data:}}$\n"
            f"Total time ($t$) = {self.total_time:.2f} s\n"
            f"Complete Oscillations ($N$) = {self.num_oscillations}"
        )
        ax.text(-3.8, 1.0, info_box, fontsize=11, 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.6', lw=1.5))

        ax.set_title("PENDULUM FREQUENCY EXPERIMENT", fontsize=14, fontweight='bold', pad=15)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy144:
    def __init__(self):
        while True:
            self.omega = rnd.uniform(1.5, 5.0)
            self.x_max = rnd.uniform(0.02, 0.05)
            self.gradient = -self.omega**2
            self.a_max = abs(self.gradient * self.x_max)
            
            if self.a_max <= 5:
                break

        self.answer = f"{self.omega}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        x_str = f"{self.x_max:.3f}"
        a_str = f"{self.a_max:.3f}"
        grad_abs = f"{abs(self.gradient):.4f}"

        self.description = (
            "A block of mass $m$ is attached to a horizontal spring and undergoes simple harmonic motion. "
            "The illustration shows the block at its maximum displacement. "
            "Using the instantaneous parameters provided, calculate the angular frequency $\\omega$ of the oscillation. "
            "(_) rad s^-1 (Example format: 2.345)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Parameters} \\\\"
            f"&\\text{{Maximum displacement, }} x_{{max}} = {x_str}\\,\\text{{m}} \\\\"
            f"&\\text{{Magnitude of acceleration, }} |a| = {a_str}\\,\\text{{m s}}^{{-2}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Relate\ Acceleration\ to\ Displacement} \\\\"
            "&\\text{{For a system in SHM: }} a = -\\omega^2 x \\\\"
            "&\\text{{Taking the magnitude: }} |a| = \\omega^2 |x| \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ } \\omega^2 \\\\"
            f"&\\omega^2 = \\frac{{|a|}}{{|x|}} = \\frac{{{a_str}}}{{{x_str}}} = {grad_abs}\\,\\text{{rad}}^2\\,\\text{{s}}^{{-2}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Answer} \\\\"
            f"&\\omega = \\sqrt{{{grad_abs}}} = \\mathbf{{{self.answer}\\,\\text{{rad s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
        ax.set_xlim(-0.1, 1.2)
        ax.set_ylim(-0.6, 0.8)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.add_patch(patches.Rectangle((-0.05, -0.1), 0.05, 0.6, facecolor='white', edgecolor='black', hatch='///', lw=2))
        ax.plot([0, 0], [-0.1, 0.5], color='black', lw=4) 
        ax.plot([0, 1.1], [-0.1, -0.1], color='black', lw=3) 

        eq_x = 0.4
        ax.plot([eq_x, eq_x], [-0.2, 0.6], color='black', linestyle='--', lw=1.5, alpha=0.6)
        ax.text(eq_x, 0.65, "Equilibrium\n($x = 0$)", ha='center', fontsize=11, fontweight='bold')

        target_x = 0.85 
        num_coils = 15
        spring_x = np.linspace(0, target_x, 300)
        spring_y = 0.08 * np.sin(2 * np.pi * num_coils * (spring_x / target_x))
        ax.plot(spring_x, spring_y, color='black', lw=2)

        block_w, block_h = 0.2, 0.2
        rect = patches.Rectangle((target_x, -0.1), block_w, block_h, facecolor='white', edgecolor='black', lw=2.5, zorder=5)
        ax.add_patch(rect)
        ax.text(target_x + block_w/2, 0, "$m$", ha='center', va='center', fontsize=14, fontweight='bold')

        ax.annotate("", xy=(target_x + block_w/2, -0.3), xytext=(eq_x, -0.3),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text((target_x + eq_x)/2 + 0.1, -0.45, f"$x_{{max}} = {self.x_max:.3f}$ m", 
                ha='center', fontsize=12, fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='none'))

        ax.annotate("", xy=(target_x - 0.1, 0.3), xytext=(target_x + 0.2, 0.3),
                    arrowprops=dict(arrowstyle='->', color='black', lw=3, mutation_scale=20))
        ax.text(target_x + 0.05, 0.45, f"$a = {self.a_max:.3f}$ m s$^{{-2}}$", 
                ha='center', fontsize=12, fontweight='bold')

        ax.set_title("HORIZONTAL SHM", fontsize=15, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy145:
    def __init__(self):
        while True:
            self.time_first_peak = rnd.uniform(0.5, 1.2)
            self.delta_t = rnd.uniform(0.8, 1.5)
            self.time_second_peak = self.time_first_peak + self.delta_t
            self.period = 2 * self.delta_t

            if self.period > 1.0:
                break

        self.answer = f"{self.period}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        t1_str = f"{self.time_first_peak:.2f}"
        t2_str = f"{self.time_second_peak:.2f}"
        dt_str = f"{self.delta_t:.2f}"

        self.description = (
            "A pendulum bob oscillates with simple harmonic motion. The variation with time $t$ "
            "of its kinetic energy $E_k$ is shown in the graph. Using the time coordinates of the successive maxima, "
            "determine the time period $T$ of the pendulum's oscillation. (_) s Example format: 2.6430486321164166)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Time\ Interval\ between\ Maxima} \\\\"
            f"&\\Delta t = t_2 - t_1 = {t2_str} - {t1_str} = {dt_str}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Relate\ Energy\ Cycle\ to\ Oscillation\ Cycle} \\\\"
            "&\\text{{In SHM, kinetic energy reaches a maximum twice during one complete oscillation.}} \\\\"
            "&\\text{{(Once at the equilibrium position moving right, once moving left).}} \\\\"
            "&\\text{{Therefore, the period of energy variation is half the period of oscillation:}} \\\\"
            "&\\Delta t = \\frac{T}{2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Time\ Period\ (} T \\mathbf{)} \\\\"
            "&T = 2 \\times \\Delta t \\\\"
            f"&T = 2 \\times {dt_str} = \\mathbf{{{self.answer}\\,\\text{{s}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        
        T_osc = self.period
        t_plot = np.linspace(0, 1.8 * T_osc, 1000)
        
        omega_osc = 2 * np.pi / T_osc
        phi = (np.pi / 2) - (omega_osc * self.time_first_peak)
        KE = 15 * (np.sin(omega_osc * t_plot + phi))**2

        ax.plot(t_plot, KE, color='black', linewidth=3, zorder=3)
        
        ax.grid(True, which='both', linestyle='--', alpha=0.5, color='gray')
        ax.set_xlabel("Time $t$ / s", fontsize=12, fontweight='bold')
        ax.set_ylabel("Kinetic Energy $E_k$ / J", fontsize=12, fontweight='bold')
        ax.set_title("KINETIC ENERGY IN SHM", fontsize=14, fontweight='bold', pad=15)

        peak_y = 15
        points = [self.time_first_peak, self.time_second_peak]
        labels = [f"$t_1 = {self.time_first_peak:.2f}$ s", f"$t_2 = {self.time_second_peak:.2f}$ s"]

        for p, l in zip(points, labels):
            ax.scatter(p, peak_y, color='black', s=60, zorder=5)
            ax.annotate(l, xy=(p, peak_y), xytext=(p + 0.05 * T_osc, peak_y + 0.5),
                        fontsize=11, fontweight='bold', color='black',
                        bbox=dict(facecolor='white', alpha=0.9, edgecolor='black'))
            ax.vlines(p, 0, peak_y, colors='black', linestyles=':', lw=2, alpha=0.8)

        ax.set_xlim(0, max(t_plot))
        ax.set_ylim(0, 18)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy146:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.05, 0.25)
            self.KE_mJ = rnd.uniform(15.0, 60.0)
            if self.mass > 0 and self.KE_mJ > 0:
                break

        self.KE = self.KE_mJ * 1e-3
        self.v_max = math.sqrt((2 * self.KE) / self.mass)
        self.answer = f"{self.v_max}"
        
        self.topic = "Oscillations"
        self.subtopic = "Energy in simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        m_str = f"{self.mass:.3f}"
        ke_str = f"{self.KE_mJ:.1f}"

        self.description = (
            "A pendulum bob oscillates with simple harmonic motion. "
            "Based on the physical constraints shown in the diagram, "
            "calculate the maximum speed of the pendulum bob during its motion. "
            "(_) m s^-1 (Example format: 0.1234)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ Units\ to\ SI} \\\\"
            f"&E_{{k,max}} = {ke_str}\\,\\text{{mJ}} = {ke_str} \\times 10^{{-3}}\\,\\text{{J}} = {self.KE:.4f}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ Kinetic\ Energy\ Equation} \\\\"
            "&E_k = \\frac{1}{2} m v^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ Maximum\ Speed\ (} v_{{max}} \\mathbf{)} \\\\"
            "&v_{{max}} = \\sqrt{\\frac{2 E_{{k,max}}}{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ Values\ and\ Solve} \\\\"
            f"&v_{{max}} = \\sqrt{{\\frac{{2 \\times {self.KE:.4f}}}{{{m_str}}}}} \\\\"
            f"&v_{{max}} = \\sqrt{{{ (2*self.KE)/self.mass :.6f}}} \\\\"
            f"&v_{{max}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-2.5, 8), 5, 0.3, facecolor='white', edgecolor='black', hatch='///', lw=2))
        ax.plot([-2.5, 2.5], [8, 8], color='black', lw=3)
        
        pivot_x, pivot_y = 0, 8
        length = 6.0
        
        ax.plot([pivot_x, 0], [pivot_y, pivot_y - length], color='black', lw=2, zorder=2)
        ax.plot([pivot_x, -2], [pivot_y, pivot_y - 5.5], color='black', linestyle='--', alpha=0.4, lw=1.5)
        ax.plot([pivot_x, 2], [pivot_y, pivot_y - 5.5], color='black', linestyle='--', alpha=0.4, lw=1.5)
        
        bob = patches.Circle((0, pivot_y - length), 0.4, facecolor='white', edgecolor='black', lw=2.5, zorder=5)
        ax.add_patch(bob)

        ax.annotate("", xy=(1.8, pivot_y - length), xytext=(-1.8, pivot_y - length),
                    arrowprops=dict(arrowstyle="<->", color='black', lw=2, connectionstyle="arc3,rad=0.15"))
        
        ax.annotate("", xy=(1.2, pivot_y - length), xytext=(0, pivot_y - length),
                    arrowprops=dict(arrowstyle="->", color='black', lw=3, mutation_scale=20))
        ax.text(0.6, pivot_y - length + 0.5, "$v_{max} = ?$", color='black', fontsize=12, fontweight='bold')

        info_box = (
            f"Mass ($m$) = {self.mass:.3f} kg\n"
            f"Max $E_k$ = {self.KE_mJ:.1f} mJ"
        )
        ax.text(-4.5, 0.5, info_box, fontsize=12, fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8', lw=1.5))

        ax.set_title("ENERGY IN PENDULUM SHM", fontsize=15, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy147:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.20, 0.45)
            self.k = rnd.uniform(25.0, 55.0)
            self.amplitude_cm = rnd.uniform(5.0, 7.0)
            self.time_interval = 10.0 
            self.gamma = rnd.uniform(0.15, 0.25) 

            self.amplitude = self.amplitude_cm / 100
            self.omega_0 = math.sqrt(self.k / self.mass)
            
            if (self.omega_0**2 - self.gamma**2) > 0:
                self.omega_d = math.sqrt(self.omega_0**2 - self.gamma**2)
                self.frequency = self.omega_d / (2 * math.pi)
                self.period = 1 / self.frequency
                break

        self.energy_initial = 0.5 * self.k * self.amplitude**2
        self.answer = f"{self.frequency}"
        self.topic = "Oscillations"
        self.subtopic = "Damped oscillations"
        self.source = "Original"
        self.curriculum = "A Level"

        self.description = (
            "The figure shows the displacement-time graph for a damped oscillating system. "
            "Using the parameters embedded in the diagram and the peak coordinates, "
            "determine the frequency of the oscillation. (_) Hz (Example format:1.979976539513881)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Determine\ Period\ (T)\ from\ Peaks} \\\\"
            f"&\\text{{Time of 1st peak }} (t_0) = 0.00\\,\\text{{s}} \\\\"
            f"&\\text{{Time of 2nd peak }} (t_1) \\approx {self.period:.2f}\\,\\text{{s}} \\\\"
            f"&T = t_1 - t_0 = {self.period:.2f}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Frequency\ (f)} \\\\"
            "&f = \\frac{1}{T} = \\frac{1}{" + f"{self.period:.2f}" + "} \\\\"
            f"&f = \\mathbf{{{self.answer}\\,\\text{{Hz}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Initial\ Energy} \\\\"
            "&E = \\frac{1}{2} k A_0^2 = 0.5 \\times " + f"{self.k:.1f} \\times ({self.amplitude:.4f})^2" + " \\\\"
            f"&E = \\mathbf{{{self.energy_initial:.4f}\\,\\text{{J}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
        
        t = np.linspace(0, self.time_interval, 1200)
        env_upper = self.amplitude_cm * np.exp(-self.gamma * t)
        x_t = env_upper * np.cos(self.omega_d * t)
        
        ax.plot(t, env_upper, color='black', linestyle='--', lw=1.5, alpha=0.6)
        ax.plot(t, -env_upper, color='black', linestyle='--', lw=1.5, alpha=0.6)
        ax.plot(t, x_t, color='black', lw=2.5, zorder=3)
        ax.axhline(0, color='black', lw=2)
        
        t0, t1 = 0, self.period
        
        ax.vlines([t0, t1], 
                  ymin=[-self.amplitude_cm - 0.2, -env_upper[np.abs(t-t1).argmin()] - 0.2], 
                  ymax=-self.amplitude_cm - 1.5, 
                  colors='black', linestyles=':', lw=2)
        
        ax.annotate('', xy=(t1, -self.amplitude_cm - 1.2), xytext=(t0, -self.amplitude_cm - 1.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        
        ax.text(t1 + 0.15, -self.amplitude_cm - 1.2, f'$T = {self.period:.2f}$ s', 
                ha='left', va='center', fontsize=12, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='none', pad=1.0, alpha=0.9))

        ax.text(self.time_interval * 0.8, self.amplitude_cm * 0.8, 
                f"Mass = {self.mass:.2f} kg\n$k = {self.k:.1f}$ N/m", 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8'), 
                fontsize=12, fontweight='bold', ha='center')

        ax.set_xlabel("Time $t$ / s", fontsize=13, fontweight='bold')
        ax.set_ylabel("Displacement $x$ / cm", fontsize=13, fontweight='bold')
        ax.set_title("DAMPED OSCILLATION DISPLACEMENT", fontsize=15, fontweight='bold', pad=15)
        
        ax.grid(True, which='both', linestyle=':', alpha=0.5, color='gray')
        ax.minorticks_on()
        
        ax.set_xlim(0, self.time_interval)
        ax.set_ylim(-self.amplitude_cm - 2.5, self.amplitude_cm + 2)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy148:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.8, 2.0)
            self.k = rnd.uniform(20.0, 50.0)
            self.beta = rnd.uniform(0.10, 0.25)

            self.omega0_sq = (2 * self.k) / self.mass
            self.omega_d_sq = self.omega0_sq - self.beta**2

            if self.omega_d_sq > 0:
                self.omega_d = math.sqrt(self.omega_d_sq)
                self.period = 2 * math.pi / self.omega_d
                self.amplitude_cm = rnd.uniform(4.0, 6.0)
                self.amplitude = self.amplitude_cm / 100
                break

        self.answer = f"{self.omega_d}"
        self.topic = "Oscillations"
        self.subtopic = "Damped oscillations"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "A block is connected between two identical springs and undergoes damped oscillations. "
            "Based on the displacement–time graph and the parameters provided in the diagram, "
            "determine the damped angular frequency $\\omega_d$. (_) rad s^-1 (Example format: 6.90700120734646)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Determine\ Damped\ Angular\ Frequency\ (\\omega_d)} \\\\"
            "&\\text{From the graph, the period } T = " + f"{self.period:.2f}\\,\\text{{s}}. \\\\"
            "&\\omega_d = \\frac{2\\pi}{T} = \\frac{2\\pi}{" + f"{self.period:.2f}" + "} \\\\"
            f"&\\omega_d = \\mathbf{{{self.answer}\\,\\text{{rad s}}^{{-1}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ the\ Damped\ Oscillation\ Formula} \\\\"
            "&\\text\\omega_0^2 = \\frac{2k}{M}. \\\\"
            "&\\text{The damped frequency relation is: } \\omega_d^2 = \\omega_0^2 - \\beta^2 \\\\"
            "&\\omega_d^2 = \\frac{2k}{M} - \\beta^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Spring\ Constant\ (k)} \\\\"
            "&\\frac{2k}{M} = \\omega_d^2 + \\beta^2 \\\\"
            "&k = \\frac{M(\\omega_d^2 + \\beta^2)}{2} \\\\"
            f"&k = \\frac{{{self.mass:.2f} \\times ({float(self.answer)**2:.3f} + {self.beta**2:.4f})}}{{2}} \\\\"
            f"&k = \\mathbf{{{self.k:.2f}\\,\\text{{N m}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({"font.size": 10, "axes.linewidth": 1.5})
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

        t_end = 3.5 * self.period
        t = np.linspace(0, t_end, 1500)
        envelope = self.amplitude_cm * np.exp(-self.beta * t)
        y = envelope * np.cos(self.omega_d * t)

        ax.plot(t, y, color='black', lw=2.5, zorder=3)
        ax.plot(t, envelope, color='black', ls='--', lw=1.5, alpha=0.6)
        ax.plot(t, -envelope, color='black', ls='--', lw=1.5, alpha=0.6)
        ax.axhline(0, color='black', lw=2)

        t0, t1 = 0, self.period
        
        ax.vlines([t0, t1], 
                  ymin=[-self.amplitude_cm - 0.2, -envelope[np.abs(t-t1).argmin()] - 0.2], 
                  ymax=-self.amplitude_cm - 1.5, 
                  colors='black', ls=':', lw=2)
        
        ax.annotate('', xy=(t1, -self.amplitude_cm - 1.2), xytext=(t0, -self.amplitude_cm - 1.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        
        ax.text(t1 + 0.15, -self.amplitude_cm - 1.2, f'$T = {self.period:.2f}$ s', 
                ha='left', va='center', fontsize=12, fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.9, edgecolor='none', pad=1.0))

        ax.annotate(f'$A_0 = {self.amplitude_cm:.1f}$ cm', 
                    xy=(0, self.amplitude_cm), xytext=(0.5, self.amplitude_cm + 0.5),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2),
                    fontsize=11, fontweight='bold')

        ax.set_xlabel("Time $t$ / s", fontweight='bold', fontsize=12)
        ax.set_ylabel("Displacement $x$ / cm", fontweight='bold', fontsize=12)
        ax.set_title("DAMPED OSCILLATION ($M + 2k$)", fontsize=14, fontweight='bold', pad=15)
        
        ax.minorticks_on()
        ax.grid(True, which='major', color='gray', ls='-', alpha=0.4)
        ax.grid(True, which='minor', color='gray', ls=':', alpha=0.2)

        info_text = (f"Mass $M = {self.mass:.2f}$ kg\n"
                     f"$\\beta = {self.beta:.2f}$ s$^{{-1}}$")
        ax.text(0.97, 0.95, info_text, transform=ax.transAxes, ha='right', va='top',
                fontsize=11, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_xlim(0, t_end)
        ax.set_ylim(-self.amplitude_cm - 2.5, self.amplitude_cm + 1.5)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy149:
    def __init__(self):
        k_e = 8.99e9 

        while True:
            self.separation_cm = rnd.uniform(10.0, 15.0)
            self.offset_cm = rnd.uniform(2.0, self.separation_cm/2 - 1.5)

            self.separation = self.separation_cm / 100
            self.offset = self.offset_cm / 100

            self.r1 = self.offset
            self.r2 = self.separation - self.offset

            self.Q_true = rnd.uniform(5e-8, 5e-7)

            self.E_given = k_e * self.Q_true * (
                (1 / self.r1**2) - (1 / self.r2**2)
            )

            if 5e3 < abs(self.E_given) < 5e5:
                break

        self.Q = self.E_given / (
            k_e * ((1 / self.r1**2) - (1 / self.r2**2))
        )

        self.answer = f"{self.Q}"
        self.topic = "Electric fields"
        self.subtopic = "Electric fields and field lines"
        self.source = "Save my Exam"
        self.curriculum = "A-Level"

        self.description = (
            "Two identical positive point charges $+Q$ are fixed in a vacuum. Point $A$ is located on the line connecting them. "
            "Based on the resultant electric field strength and distances shown in the diagram, "
            "calculate the magnitude of the charge $Q$. (_) C (Example format: 8.095898412410912e-08)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Distances\ in\ SI\ Units} \\\\"
            f"&r_1 = {self.offset:.3f}\\,\\text{{m}} \\\\"
            f"&r_2 = {self.separation:.3f} - {self.offset:.3f} = {self.r2:.3f}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Formulate\ Resultant\ Electric\ Field} \\\\"
            "&\\text{Field from left charge (rightwards): } E_1 = \\frac{k Q}{r_1^2} \\\\"
            "&\\text{Field from right charge (leftwards): } E_2 = \\frac{k Q}{r_2^2} \\\\"
            "&E_{net} = E_1 - E_2 = k Q \\left( \\frac{1}{r_1^2} - \\frac{1}{r_2^2} \\right) \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitute\ Known\ Values} \\\\"
            f"&{self.E_given:.2e} = (8.99 \\times 10^9) Q \\left( \\frac{1}{{({self.r1:.3f})^2}} - \\frac{1}{{({self.r2:.3f})^2}} \\right) \\\\"
            "&\\mathbf{Step\ 4:\ Solve\ for\ } Q \\\\"
            f"&Q = \\frac{{{self.E_given:.2e}}}{{(8.99 \\times 10^9) ({1/self.r1**2 - 1/self.r2**2:.3f})}} \\\\"
            f"&Q = \\mathbf{{{self.answer}\\,\\text{{C}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(-1, 11)
        ax.set_ylim(-2, 3)
        ax.set_aspect('equal')
        ax.axis("off")

        x1, x2 = 1, 9
        x_a = x1 + (self.offset_cm / self.separation_cm) * (x2 - x1)

        ax.plot([x1, x2], [0, 0], color='black', linestyle='--', lw=1.5, zorder=1)

        for x in [x1, x2]:
            charge = plt.Circle((x, 0), 0.25, color='white', ec='black', lw=2, zorder=5)
            ax.add_patch(charge)
            ax.text(x, 0.5, "$+Q$", ha='center', fontsize=12, fontweight='bold')

        ax.scatter(x_a, 0, color='black', s=100, marker='x', zorder=6, lw=3)
        ax.text(x_a, 0.4, "Point A", ha='center', fontsize=12, fontweight='bold')

        ax.annotate('', xy=(x1, -0.8), xytext=(x2, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text((x1+x2)/2, -1.2, f"$d = {self.separation_cm:.1f}$ cm", ha='center', fontweight='bold', fontsize=11)

        ax.annotate('', xy=(x1, 1.2), xytext=(x_a, 1.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text((x1+x_a)/2, 1.5, f"${self.offset_cm:.1f}$ cm", ha='center', fontsize=11, fontweight='bold')

        ax.text((x1+x2)/2, 2.5, f"$E_{{net}}$ at A = {self.E_given:.2e} V m$^{{-1}}$", 
                ha='center', fontsize=12, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_title("ELECTRIC FIELD SUPERPOSITION", fontsize=14, fontweight='bold', pad=10)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy150:
    def __init__(self):
        self.e = 1.60e-19
        self.m_e = 9.11e-31

        while True:
            self.E_pN = rnd.uniform(1.0, 5.0)
            self.E = self.E_pN * 1e-12
            self.force = self.e * self.E
            self.acceleration = self.force / self.m_e
            if self.acceleration > 0:
                break

        self.answer = f"{self.acceleration}"
        self.description = (
            "An electron is placed in a uniform electric field. Using the parameters provided in the diagram, "
            "calculate the magnitude of the acceleration of the electron. ( _ ) m s⁻² (Example format:  0.4319030554713497)"
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric fields and field lines"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Convert electric field to SI units}\\\\"
            f"E &= {self.E_pN:.5f}\\,\\text{{pN C}}^{{-1}}\\\\"
            "\\text{Since } 1\\,\\text{pN} = 10^{-12}\\,\\text{N},\\\\"
            f"E &= {self.E_pN:.5f} \\times 10^{{-12}}\\\\"
            f"E &= {self.E:.5e}\\,\\text{{N C}}^{{-1}}\\\\"
            "\\textbf{Step 2: Electric force on the electron}\\\\"
            "F &= qE\\\\"
            "q &= 1.60 \\times 10^{-19}\\,\\text{C}\\\\"
            f"F &= (1.60 \\times 10^{{-19}})({self.E:.5e})\\\\"
            f"F &= {self.force:.5e}\\,\\text{{N}}\\\\"
            "\\textbf{Step 3: Apply Newton's Second Law}\\\\"
            "F &= ma\\\\"
            "a &= \\frac{F}{m}\\\\"
            "m &= 9.11 \\times 10^{-31}\\,\\text{kg}\\\\"
            f"a &= \\frac{{{self.force:.5e}}}{{9.11 \\times 10^{{-31}}}}\\\\"
            f"a &= {self.acceleration:.5e}\\,\\text{{m s}}^{{-2}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({
            "font.size": 12,
            "font.family": "serif",
            "text.usetex": False,
            "axes.linewidth": 1.2
        })

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        ax.text(0.5, 4.9, f"Electric field strength, $E = {self.E_pN:.2f}$ pN C$^{-1}$", fontsize=12, fontweight='bold')
        ax.text(0.5, 4.5, r"Charge of electron, $e = 1.60 \times 10^{-19}$ C", fontsize=12)
        ax.text(0.5, 4.1, r"Mass of electron, $m_e = 9.11 \times 10^{-31}$ kg", fontsize=12)

        y_positions = np.linspace(1.0, 3.5, 6)
        for y in y_positions:
            ax.arrow(9.0, y, -8.0, 0,
                     head_width=0.15,
                     head_length=0.3,
                     length_includes_head=True,
                     linewidth=2.0,
                     color="black",
                     alpha=0.8)
        
        ax.text(9.1, 2.25, r"$\vec{E}$", color="black", fontsize=16, weight="bold")

        electron_x, electron_y = 6.0, 2.25
        electron = plt.Circle((electron_x, electron_y), 0.3, 
                              facecolor="white", edgecolor="black", linewidth=2, zorder=5)
        ax.add_patch(electron)
        ax.text(electron_x, electron_y, "-", fontsize=20, ha="center", va="center", weight="bold")
        
        ax.text(electron_x, electron_y + 0.5, "Electron\n$a = ?$", fontsize=12, ha="center", weight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.2)
        plt.close()
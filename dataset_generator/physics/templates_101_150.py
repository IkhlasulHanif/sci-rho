import random as rnd
import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from physics.helper import *

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

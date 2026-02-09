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
            self.description = (
                "The graph shows current against time for a conductor.\n"
                "All relevant values are shown in the diagram.\n"
                "Determine the charge transferred.\n"
                "Q = (_) C"
            )
        else:
            self.answer = sig_figs(self.I, 3)
            self.description = (
                "The graph shows current against time for a conductor.\n"
                "All relevant values are shown in the diagram.\n"
                "Determine the current.\n"
                "I = (_) A"
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
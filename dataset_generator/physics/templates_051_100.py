import random as rnd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image
from physics.helper import *

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Phy051:
    """
    Series circuit with two resistors, an ammeter in series, and a voltmeter across R2.
    Ask for ammeter reading (current).
    """

    def __init__(self):
        # Choose nice integers by constructing Vs = I*(R1+R2)
        while True:
            self.R1 = rnd.randint(2, 20)
            self.R2 = rnd.randint(2, 20)
            self.I = rnd.randint(1, 4)  # A
            self.Vs = self.I * (self.R1 + self.R2)  # V
            if 6 <= self.Vs <= 48:
                break

        self.answer = round(self.I, 2)

        self.description = (
            "A circuit has two resistors in series. A voltmeter is connected across R2 (assume ideal meters). "
            "What is the current shown on the ammeter? (_) A"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electric circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Resistance, }} R_1 &= {self.R1}\\,\\Omega\\\\"
            f"\\text{{Resistance, }} R_2 &= {self.R2}\\,\\Omega\\\\"
            f"\\text{{Total resistance in series:}} &\\\\"
            f"R_{{total}} &= R_1 + R_2\\\\"
            f"&= {self.R1} + {self.R2}\\\\"
            f"&= {round(self.R1 + self.R2, 10)}\\,\\Omega\\\\"
            f"\\text{{Using Ohm's Law for the whole circuit:}} &\\\\"
            f"I &= \\frac{{V_s}}{{R_{{total}}}}\\\\"
            f"&= \\frac{{{self.Vs}}}{{{round(self.R1 + self.R2, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{A}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Outer loop wires
        draw_wire(ax, [(2, 2), (2, 8), (8.5, 8), (8.5, 2), (2, 2)], lw=2)

        # Cell on left side
        ax.plot([2, 2], [8, 7], linewidth=2, color="black")
        ax.plot([2, 2], [3, 2], linewidth=2, color="black")
        draw_cell_vertical(ax, x=2, y_bottom=3, y_top=7, value_text=f"{self.Vs} V")

        # R1 and R2 on top wire
        draw_resistor_box(ax, x=4.5, y=8, label="R1", value_text=f"{self.R1} Ω")
        draw_resistor_box(ax, x=6.9, y=8, label="R2", value_text=f"{self.R2} Ω")

        # Ammeter on bottom wire
        draw_circle_meter(ax, x=5.25, y=2, letter="A")

        # Voltmeter across R2 (simple parallel loop above R2)
        # Tap points near R2 ends
        draw_wire(ax, [(6.3, 8), (6.3, 9.2)], lw=2)
        draw_wire(ax, [(7.5, 8), (7.5, 9.2)], lw=2)
        draw_wire(ax, [(6.3, 9.2), (6.8, 9.2)], lw=2)
        draw_wire(ax, [(7.0, 9.2), (7.5, 9.2)], lw=2)
        draw_circle_meter(ax, x=6.9, y=9.2, letter="V", r=0.35, fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy052:
    """
    Two resistors in parallel. Ammeter measures total current from the supply.
    Ask for total current.
    """

    def __init__(self):
        # Construct integer branch currents: R = V/I
        self.Vs = rnd.choice([6, 9, 12, 18, 24])
        self.I1 = rnd.randint(1, 4)
        self.I2 = rnd.randint(1, 4)

        # Ensure integer resistances in a reasonable range
        while (self.Vs % self.I1 != 0) or (self.Vs % self.I2 != 0):
            self.I1 = rnd.randint(1, 4)
            self.I2 = rnd.randint(1, 4)

        self.R1 = self.Vs // self.I1
        self.R2 = self.Vs // self.I2

        # Avoid identical resistors too often
        if self.R1 == self.R2:
            self.I2 = max(1, (self.I2 % 4) + 1)
            while self.Vs % self.I2 != 0:
                self.I2 = rnd.randint(1, 4)
            self.R2 = self.Vs // self.I2

        self.Itotal = self.I1 + self.I2
        self.answer = round(self.Itotal, 2)

        self.description = (
            "Two resistors are connected in parallel as shown. The ammeter measures the total current. "
            "What is the ammeter reading? (_) A"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electric circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Resistance, }} R_1 &= {self.R1}\\,\\Omega\\\\"
            f"\\text{{Resistance, }} R_2 &= {self.R2}\\,\\Omega\\\\"
            f"\\text{{Current through }} R_1\\text{{:}} &\\\\"
            f"I_1 &= \\frac{{V_s}}{{R_1}}\\\\"
            f"&= \\frac{{{self.Vs}}}{{{self.R1}}}\\\\"
            f"&= {round(self.I1, 10)}\\,\\text{{A}}\\\\"
            f"\\text{{Current through }} R_2\\text{{:}} &\\\\"
            f"I_2 &= \\frac{{V_s}}{{R_2}}\\\\"
            f"&= \\frac{{{self.Vs}}}{{{self.R2}}}\\\\"
            f"&= {round(self.I2, 10)}\\,\\text{{A}}\\\\"
            f"\\text{{Total current (ammeter reading):}} &\\\\"
            f"I_{{total}} &= I_1 + I_2\\\\"
            f"&= {round(self.I1, 10)} + {round(self.I2, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{A}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        top_y, bot_y = 8.0, 2.5
        left_x, right_x = 2.0, 8.0

        # buses
        draw_wire(ax, [(left_x, top_y), (right_x, top_y)], lw=2)
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # cell inserted on left vertical
        draw_wire(ax, [(left_x, top_y), (left_x, 7.5)], lw=2)
        draw_wire(ax, [(left_x, 3.0), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=3.0, y_top=7.5, value_text=f"{self.Vs} V")

        # ammeter (symbol only)
        draw_circle_meter(ax, x=4.1, y=top_y, letter="A")

        # branches
        x1, x2 = 5.6, 7.3
        r1_top, r1_bot = draw_resistor_box(ax, x=x1, y=5.6, label="R1", value_text=f"{self.R1} Ω", fontsize=14)
        draw_wire(ax, [(x1, top_y), (x1, r1_top)], lw=2)
        draw_wire(ax, [(x1, r1_bot), (x1, bot_y)], lw=2)

        r2_top, r2_bot = draw_resistor_box(ax, x=x2, y=5.6, label="R2", value_text=f"{self.R2} Ω", fontsize=14)
        draw_wire(ax, [(x2, top_y), (x2, r2_top)], lw=2)
        draw_wire(ax, [(x2, r2_bot), (x2, bot_y)], lw=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy053:
    """
    Potential divider with a fixed resistor and an NTC thermistor.
    Voltmeter measures Vout across the thermistor.
    Ask for Vout.
    """

    def __init__(self):
        self.Vs = rnd.choice([6, 9, 12, 15])
        base = rnd.choice([470, 680, 1000, 1500, 2200])  # ohms scale

        # Choose a simple ratio a:b for Rfixed:RT to keep results reasonable
        a, b = rnd.choice([(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)])
        self.R_fixed = a * base
        self.R_T = b * base

        self.Vout = self.Vs * (self.R_T / (self.R_fixed + self.R_T))
        self.answer = round(self.Vout, 2)

        self.description = (
            "A potential divider uses a fixed resistor and an NTC thermistor. "
            "The voltmeter measures V_out across the thermistor. "
            "Calculate V_out. (_) V"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electric circuits"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Supply voltage, }} V_s &= {self.Vs}\\,\\text{{V}}\\\\"
            f"\\text{{Fixed resistance, }} R_{{fixed}} &= {self.R_fixed}\\,\\Omega\\\\"
            f"\\text{{Thermistor resistance, }} R_T &= {self.R_T}\\,\\Omega\\\\"
            f"\\text{{Total resistance, }} R_{{total}} &= R_{{fixed}} + R_T\\\\"
            f"&= {self.R_fixed} + {self.R_T}\\\\"
            f"&= {round(self.R_fixed + self.R_T, 10)}\\,\\Omega\\\\"
            f"\\text{{The output voltage }} V_{{out}} \\text{{ is given by:}} &\\\\"
            f"V_{{out}} &= V_s \\times \\left( \\frac{{R_T}}{{R_{{fixed}} + R_T}} \\right)\\\\"
            f"&= {self.Vs} \\times \\left( \\frac{{{self.R_T}}}{{{round(self.R_fixed + self.R_T, 10)}}} \\right)\\\\"
            f"&= {self.Vs} \\times {round(self.R_T / (self.R_fixed + self.R_T), 10)}\\\\"
            f"&= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))
        top_y, bot_y = 8.0, 2.0
        left_x = 2.0
        x_div = 5.0

        # rails
        draw_wire(ax, [(left_x, top_y), (x_div, top_y)], lw=2)
        draw_wire(ax, [(left_x, bot_y), (7.5, bot_y)], lw=2)

        # left vertical with cell
        draw_wire(ax, [(left_x, top_y), (left_x, 7.0)], lw=2)
        draw_wire(ax, [(left_x, 3.0), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=3.0, y_top=7.0, value_text=f"{self.Vs} V", fontsize=14)

        # fixed resistor (connect to its TRUE top/bottom)
        rf_top, rf_bot = draw_resistor_box(ax, x=x_div, y=6.3, label="R", value_text=f"{self.R_fixed} Ω", fontsize=14)
        draw_wire(ax, [(x_div, top_y), (x_div, rf_top)], lw=2)

        # thermistor
        rt_top, rt_bot = draw_thermistor(ax, x=x_div, y=3.3, label="NTC", value_text=f"{self.R_T} Ω", fontsize=14)
        draw_wire(ax, [(x_div, rf_bot), (x_div, rt_top)], lw=2)
        draw_wire(ax, [(x_div, rt_bot), (x_div, bot_y)], lw=2)

        # voltmeter across thermistor (use meter terminals so it touches the circle)
        V = draw_circle_meter(ax, x=7.5, y=3.2, letter="V", r=0.55, fontsize=14)

        junction = (x_div, rt_top)   # top of thermistor
        draw_wire(ax, [junction, (7.5, rt_top)], lw=2)
        draw_wire(ax, [(7.5, rt_top), V["top"]], lw=2)
        draw_wire(ax, [(7.5, bot_y), V["bottom"]], lw=2)

        draw_text(ax, 8.1, 4.1, "Vout", fontsize=14, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy054:
    """
    Bar magnet with a point P above the center.
    Options A,B,C,D are arrows: A=up, B=right, C=down, D=left.
    Ask which arrow shows the magnetic field direction at P.
    """

    def __init__(self):
        # Randomly choose magnet orientation
        self.N_on_left = rnd.choice([True, False])

        # At a point above the middle, direction is from N to S along the top:
        # If N left -> field points right; if N right -> field points left
        self.answer = "B" if self.N_on_left else "D"

        self.description = (
            "A bar magnet is shown with a point P. "
            "Which arrow (A, B, C, or D) shows the direction of the magnetic field at P? (_)"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electromagnetic effects"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Pole on the left}} &= {'\\text{North (N)}' if self.N_on_left else '\\text{South (S)}'}\\\\"
            f"\\text{{Pole on the right}} &= {'\\text{South (S)}' if self.N_on_left else '\\text{North (N)}'}\\\\"
            "\\text{{Magnetic field lines direction}} &: \\text{From North to South outside the magnet}\\\\"
            "\\text{{At point P (above the magnet):}} &\\\\"
            f"\\text{{Field lines travel from }} {'\\text{left to right}' if self.N_on_left else '\\text{right to left}'} \\text{{ to reach the South pole}}\\\\"
            f"\\text{{Direction at P}} &= {'\\text{Right (B)}' if self.N_on_left else '\\text{Left (D)}'}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 3.8))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Magnet body
        mag = patches.Rectangle((2, 4), 6, 2, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(mag)

        # Label poles
        if self.N_on_left:
            ax.text(2.6, 5, "N", ha="center", va="center", fontsize=14)
            ax.text(7.4, 5, "S", ha="center", va="center", fontsize=14)
        else:
            ax.text(2.6, 5, "S", ha="center", va="center", fontsize=14)
            ax.text(7.4, 5, "N", ha="center", va="center", fontsize=14)

        # Point P
        ax.plot([5], [8], marker="o", markersize=5, color="black")
        ax.text(5.2, 8.0, "P", ha="left", va="center", fontsize=12)

        # Option arrows around P: A up, B right, C down, D left
        arrow(ax, 5, 8, 0, 1.2, label="A", label_offset=(0.0, 0.25))
        arrow(ax, 5, 8, 1.2, 0, label="B", label_offset=(0.25, 0.0))
        arrow(ax, 5, 8, 0, -1.2, label="C", label_offset=(0.0, -0.25))
        arrow(ax, 5, 8, -1.2, 0, label="D", label_offset=(-0.25, 0.0))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy055:
    """
    Wire between magnet poles with a shown B-field direction.
    Current is either into the page (×) or out of the page (•).
    Options A,B,C,D are arrows around the wire: A=up, B=right, C=down, D=left.
    Ask direction of force on the wire.
    """

    def __init__(self):
        # Choose field direction and current direction
        # B_dir = +1 means left->right, -1 means right->left
        self.B_dir = rnd.choice([1, -1])
        # I_dir = +1 means out of page (•, +z), -1 means into page (×, -z)
        self.I_dir = rnd.choice([1, -1])

        # Using F ∝ I × B:
        # If B is +x and I is -z -> F is -y (down)
        # If B is +x and I is +z -> F is +y (up)
        # Reversing B flips force.
        # So force is vertical; options are A (up) or C (down).
        # Determine sign of y:
        # y_sign = I_dir * B_dir (because (+z)×(+x)=+y, (-z)×(+x)=-y, etc.)
        y_sign = self.I_dir * self.B_dir
        self.answer = "A" if y_sign > 0 else "C"

        self.description = (
            "A wire is placed in a magnetic field as shown. The current direction is given on the diagram. "
            "Which arrow (A, B, C, or D) shows the direction of the force on the wire? (_)"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electromagnetic effects"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Magnetic field direction (B)}} &= {'\\text{{Left to Right}}' if self.B_dir == 1 else '\\text{{Right to Left}}'}\\\\"
            f"\\text{{Current direction (I)}} &= {'\\text{{Out of the page (\\textbullet)}}' if self.I_dir == 1 else '\\text{{Into the page (\\texttimes)}}'}\\\\"
            "\\text{{Using Fleming's Left-Hand Rule:}} &\\\\"
            "\\text{{First finger}} &= \\text{{Field (B)}}\\\\"
            "\\text{{Second finger}} &= \\text{{Current (I)}}\\\\"
            "\\text{{Thumb}} &= \\text{{Force (F)}}\\\\"
            "\\text{{Applying the rule:}} &\\\\"
            f"\\text{{Force direction}} &= {'\\text{{Upward (A)}}' if (self.I_dir * self.B_dir) > 0 else '\\text{{Downward (C)}}'}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
        

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Magnet poles blocks
        left = patches.Rectangle((1.2, 3), 2, 4, fill=False, linewidth=2, edgecolor="black")
        right = patches.Rectangle((6.8, 3), 2, 4, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(left)
        ax.add_patch(right)

        # Label N/S to match B direction
        if self.B_dir == 1:
            ax.text(2.2, 5, "N", ha="center", va="center", fontsize=14)
            ax.text(7.8, 5, "S", ha="center", va="center", fontsize=14)
        else:
            ax.text(2.2, 5, "S", ha="center", va="center", fontsize=14)
            ax.text(7.8, 5, "N", ha="center", va="center", fontsize=14)

        # B-field arrow across the gap (centered)
        if self.B_dir == 1:
            arrow(ax, 3.5, 8.2, 3.0, 0.0, label=None)
        else:
            arrow(ax, 6.5, 8.2, -3.0, 0.0, label=None)

        # Wire at center with current symbol
        draw_current_symbol(ax, x=5, y=5, direction=self.I_dir, r=0.40, lw=2)

        # Option arrows around the wire: A up, B right, C down, D left
        arrow(ax, 5, 5, 0, 1.5, label="A", label_offset=(0.0, 0.25))
        arrow(ax, 5, 5, 1.5, 0, label="B", label_offset=(0.25, 0.0))
        arrow(ax, 5, 5, 0, -1.5, label="C", label_offset=(0.0, -0.25))
        arrow(ax, 5, 5, -1.5, 0, label="D", label_offset=(-0.25, 0.0))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy056:
    """
    Simple transformer diagram with Np, Ns and Vp labeled.
    Ask for secondary voltage Vs using Vs = Vp*(Ns/Np).
    """

    def __init__(self):
        self.Vp = rnd.choice([120, 240])

        # Choose a simple turns ratio
        ratio = rnd.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)])
        a, b = ratio  # Np:Ns = a:b

        base = rnd.choice([50, 100, 150, 200])
        self.Np = a * base
        self.Ns = b * base

        self.Vs = self.Vp * (self.Ns / self.Np)
        self.answer = round(self.Vs, 2)

        self.description = (
            "A transformer has the primary and secondary turns shown. The primary voltage is given. "
            "Assume an ideal transformer. Calculate the secondary voltage. (_) V"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electromagnetic effects"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Primary voltage, }} V_p &= {self.Vp}\\,\\text{{V}}\\\\"
            f"\\text{{Primary turns, }} N_p &= {self.Np}\\\\"
            f"\\text{{Secondary turns, }} N_s &= {self.Ns}\\\\"
            "\\text{{The transformer equation relates turns and voltage:}} &\\\\"
            "\\frac{V_s}{V_p} &= \\frac{N_s}{N_p}\\\\"
            "\\text{{Rearranging for secondary voltage }} V_s: &\\\\"
            "V_s &= V_p \\times \\left( \\frac{N_s}{N_p} \\right)\\\\"
            f"&= {self.Vp} \\times \\left( \\frac{{{self.Ns}}}{{{self.Np}}} \\right)\\\\"
            f"&= {self.Vp} \\times {round(self.Ns / self.Np, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Core
        core = patches.Rectangle((4.3, 2.0), 1.4, 6.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(core)

        # Primary coil (left)
        for i in range(5):
            ax.add_patch(patches.Arc((3.2, 3.0 + i*1.1), 1.2, 0.8, angle=0, theta1=0, theta2=180, linewidth=2))

        # Secondary coil (right)
        for i in range(5):
            ax.add_patch(patches.Arc((6.8, 3.0 + i*1.1), 1.2, 0.8, angle=0, theta1=180, theta2=360, linewidth=2))

        # Labels (dynamic values)
        ax.text(2.1, 9.0, f"Np = {self.Np}", ha="left", va="center", fontsize=11)
        ax.text(2.1, 8.2, f"Vp = {self.Vp} V", ha="left", va="center", fontsize=11)

        ax.text(6.2, 9.0, f"Ns = {self.Ns}", ha="left", va="center", fontsize=11)
        ax.text(6.2, 8.2, "Vs = ?", ha="left", va="center", fontsize=11)

        # Simple wires to suggest terminals
        draw_wire(ax, [(2.1, 3.0), (2.1, 7.0)], lw=2)
        draw_wire(ax, [(7.9, 3.0), (7.9, 7.0)], lw=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy057:
    """
    Graph of corrected count rate vs time. Ask for half-life from the graph.
    """

    def __init__(self):
        # Many versions: vary half-life + initial count rate
        self.half_life = rnd.choice([8, 10, 12, 15, 16, 18, 20, 24, 25, 30, 32, 36, 40, 45, 48, 50, 60])
        # Choose N0 divisible by 16 so halving looks clean on labels/points
        self.N0 = rnd.choice([160, 192, 224, 256, 320, 384, 448, 512, 640, 768, 800])

        self.t_max = 4 * self.half_life
        self.answer = self.half_life  # seconds

        self.description = (
            "The graph shows the corrected count rate of a radioactive source over time. "
            "Determine the half-life of the isotope. (_) s"
        )
        self.topic = "Nuclear physics"
        self.subtopic = "Radioactivity"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial count rate, }} N_0 &= {self.N0}\\,\\text{{s}}^{{-1}}\\\\"
            "\\text{{The half-life }} (t_{{1/2}}) \\text{{ is the time taken for the count rate to halve.}} &\\\\"
            "\\text{{Target count rate}} &= \\frac{N_0}{2}\\\\"
            f"&= \\frac{{{self.N0}}}{{2}}\\\\"
            f"&= {round(self.N0 / 2, 10)}\\,\\text{{s}}^{{-1}}\\\\"
            "\\text{{From the graph:}} &\\\\"
            f"\\text{{1. Locate }} {round(self.N0 / 2, 10)}\\,\\text{{s}}^{{-1}} \\text{{ on the vertical axis.}}\\\\"
            "\\text{{2. Move horizontally to the decay curve.}}\\\\"
            "\\text{{3. Move vertically down to the time axis.}}\\\\"
            f"\\text{{Time at }} \\frac{{N_0}}{{2}} &= {self.answer}\\,\\text{{s}}\\\\"
            f"\\text{{Half-life, }} t_{{1/2}} &= {self.answer}\\,\\text{{s}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Plot area (manual axes)
        x0, y0 = 1.6, 1.6
        x1, y1 = 9.4, 9.2
        w = x1 - x0
        h = y1 - y0

        # Axes
        draw_wire(ax, [(x0, y0), (x1, y0)], lw=2)  # x-axis
        draw_wire(ax, [(x0, y0), (x0, y1)], lw=2)  # y-axis

        # Axis labels (minimal)
        ax.text((x0 + x1) / 2, y0 - 1.75, "time / s", ha="center", va="center", fontsize=12)
        ax.text(x0 - 1.75, (y0 + y1) / 2, "count rate / s$^{-1}$",
                ha="center", va="center", rotation=90, fontsize=12)

        # Ticks (x): 0, 1h, 2h, 3h, 4h
        for i in range(5):
            t = i * (self.t_max / 4)
            x = x0 + (t / self.t_max) * w
            draw_wire(ax, [(x, y0), (x, y0 - 0.25)], lw=2)
            ax.text(x, y0 - 0.6, f"{int(t)}", ha="center", va="top", fontsize=11)

        # Ticks (y): 0, N0/4, N0/2, 3N0/4, N0
        y_vals = [0, self.N0 / 4, self.N0 / 2, 3 * self.N0 / 4, self.N0]
        for val in y_vals:
            y = y0 + (val / self.N0) * h
            draw_wire(ax, [(x0, y), (x0 - 0.25, y)], lw=2)
            ax.text(x0 - 0.45, y, f"{int(val)}", ha="right", va="center", fontsize=11)

        # Decay curve: N(t) = N0 * (1/2)^(t/half_life)
        xs, ys = [], []
        for k in range(0, 121):
            t = (k / 120) * self.t_max
            N = self.N0 * (0.5 ** (t / self.half_life))
            xs.append(x0 + (t / self.t_max) * w)
            ys.append(y0 + (N / self.N0) * h)

        ax.plot(xs, ys, color="black", linewidth=2)

        # Plot key points at 0, 1h, 2h, 3h, 4h
        for i in range(5):
            t = i * self.half_life
            N = self.N0 * (0.5 ** i)
            xp = x0 + (t / self.t_max) * w
            yp = y0 + (N / self.N0) * h
            ax.plot([xp], [yp], marker="o", markersize=5, color="black")

        # Save
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy058:
    """
    Identify radiation type (alpha/beta/gamma) from absorber test readings (visual).
    """

    def __init__(self):
        self.radiation = rnd.choice(["alpha", "beta", "gamma"])  # many versions
        self.I0 = rnd.randint(80, 220)

        # Thickness labels for variability
        self.al_mm = rnd.randint(1, 5)
        self.pb_mm = rnd.randint(2, 10)

        # Readings for 4 conditions
        # (No absorber, Paper, Aluminium, Lead)
        if self.radiation == "alpha":
            self.readings = [self.I0, 0, 0, 0]
            self.answer = "A"
        elif self.radiation == "beta":
            paper_factor = rnd.uniform(0.85, 1.00)
            self.readings = [self.I0, int(round(self.I0 * paper_factor)), 0, 0]
            self.answer = "B"
        else:
            # gamma: slight reduction through paper, more through aluminium, reduced (not zero) by lead
            paper_factor = rnd.uniform(0.90, 1.00)
            al_factor = max(0.70, 1.00 - 0.05 * self.al_mm + rnd.uniform(-0.03, 0.03))
            pb_factor = max(0.25, 0.85 - 0.05 * self.pb_mm + rnd.uniform(-0.05, 0.05))

            I_paper = int(round(self.I0 * paper_factor))
            I_al = int(round(I_paper * al_factor))
            I_pb = max(1, int(round(I_al * pb_factor)))

            self.readings = [self.I0, I_paper, I_al, I_pb]
            self.answer = "C"

        self.description = (
            "A radioactive source is tested with different absorbers between the source and a detector. "
            "The detector readings are shown. What type of radiation is emitted?\n"
            "A: alpha   B: beta   C: gamma   (_)"
        )
        self.topic = "Nuclear physics"
        self.subtopic = "Radioactivity"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial reading (no absorber)}} &= {self.readings[0]}\\,\\text{{cps}}\\\\"
            f"\\text{{Reading with paper}} &= {self.readings[1]}\\,\\text{{cps}}\\\\"
            f"\\text{{Reading with aluminium}} &= {self.readings[2]}\\,\\text{{cps}}\\\\"
            f"\\text{{Reading with lead}} &= {self.readings[3]}\\,\\text{{cps}}\\\\"
            "\\text{{Analysis of penetration power:}} &\\\\"
            "\\text{1. Alpha (}\\alpha\\text{) particles} &: \\text{Stopped by a thin sheet of paper.}\\\\"
            "\\text{2. Beta (}\\beta\\text{) particles} &: \\text{Pass through paper but stopped by aluminium.}\\\\"
            "\\text{3. Gamma (}\\gamma\\text{) rays} &: \\text{Pass through paper and aluminium; reduced by thick lead.}\\\\"
            "\\text{{Observation from data:}} &\\\\"
            f"{'\\text{Reading dropped to 0 with paper: Radiation is alpha.}' if self.radiation == 'alpha' else ''}"
            f"{'\\text{Reading passed paper but dropped to 0 with aluminium: Radiation is beta.}' if self.radiation == 'beta' else ''}"
            f"{'\\text{Reading passed paper and aluminium but was reduced by lead: Radiation is gamma.}' if self.radiation == 'gamma' else ''} \\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Row y positions
        ys = [8.2, 6.0, 3.8, 1.6]
        labels = [
            "No absorber",
            "Paper",
            f"Al {self.al_mm} mm",
            f"Pb {self.pb_mm} mm"
        ]

        # Draw 4 mini setups
        for i, y in enumerate(ys):
            # Source
            src = patches.Circle((1.4, y), 0.45, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(src)
            ax.text(1.4, y, "S", ha="center", va="center", fontsize=14)

            # Absorber block (always drawn; "No absorber" is just an empty labelled block)
            abs_rect = patches.Rectangle((4.2, y - 0.55), 1.8, 1.1, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(abs_rect)
            ax.text(5.1, y, labels[i], ha="center", va="center", fontsize=11,
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

            # Detector
            det_rect = patches.Rectangle((7.4, y - 0.65), 2.2, 1.3, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(det_rect)
            ax.text(8.5, y + 0.35, "Detector", ha="center", va="center", fontsize=11)
            ax.text(8.5, y - 0.25, f"{self.readings[i]} cps", ha="center", va="center", fontsize=12,
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))

            # Arrow line (drawn behind boxes)
            draw_wire(ax, [(1.85, y), (7.35, y)], lw=2)

        # Options (kept minimal, but visible)
        ax.text(0.7, 9.6, "A alpha", ha="left", va="center", fontsize=11)
        ax.text(3.6, 9.6, "B beta", ha="left", va="center", fontsize=11)
        ax.text(6.3, 9.6, "C gamma", ha="left", va="center", fontsize=11)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()
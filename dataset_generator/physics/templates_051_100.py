import random as rnd
import os
import math
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

        # Layout
        top_y, bot_y = 8.0, 2.0
        left_x, right_x = 2.0, 8.5

        # Cell placement on left vertical
        y_cell_top = top_y - 1.0   # 7.0
        y_cell_bot = bot_y + 1.0   # 3.0

        # --- Ammeter inline on bottom wire (wire stops at circle edge) ---
        x_A = (left_x + right_x) / 2
        r_A = 0.45
        A_left  = (x_A - r_A, bot_y)
        A_right = (x_A + r_A, bot_y)

        # Bottom wire split by ammeter
        draw_wire(ax, [(left_x, bot_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, bot_y)], lw=2)

        # Right side vertical (continuous)
        draw_wire(ax, [(right_x, bot_y), (right_x, top_y)], lw=2)

        # Left side split for cell
        draw_wire(ax, [(left_x, top_y), (left_x, y_cell_top)], lw=2)
        draw_wire(ax, [(left_x, y_cell_bot), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=y_cell_bot, y_top=y_cell_top,
                        value_text=f"{self.Vs} V", fontsize=10)

        # ---- Series resistors on the top wire (wire meets resistor edges) ----
        wR, hR = 1.2, 0.6
        span = right_x - left_x

        x_R1 = left_x + 0.40 * span
        x_R2 = left_x + 0.75 * span

        r1_left  = (x_R1 - wR/2, top_y)
        r1_right = (x_R1 + wR/2, top_y)
        r2_left  = (x_R2 - wR/2, top_y)
        r2_right = (x_R2 + wR/2, top_y)

        draw_wire(ax, [(left_x, top_y), r1_left], lw=2)
        draw_wire(ax, [r1_right, r2_left], lw=2)
        draw_wire(ax, [r2_right, (right_x, top_y)], lw=2)

        draw_resistor_box(ax, x=x_R1, y=top_y, w=wR, h=hR, label="R1",
                        value_text=f"{self.R1} Ω", fontsize=10)
        draw_resistor_box(ax, x=x_R2, y=top_y, w=wR, h=hR, label="R2",
                        value_text=f"{self.R2} Ω", fontsize=10)

        # Draw ammeter symbol AFTER wires so it sits cleanly on top
        draw_circle_meter(ax, x=x_A, y=bot_y, letter="A", r=r_A, fontsize=10)

        # ---- Voltmeter across R2 (wire stops at voltmeter circle edge) ----
        x_vm = x_R2
        y_vm = top_y + 1.2
        r_vm = 0.35

        # vertical leads from R2 ends up to voltmeter level
        draw_wire(ax, [r2_left,  (r2_left[0],  y_vm)], lw=2)
        draw_wire(ax, [r2_right, (r2_right[0], y_vm)], lw=2)

        # horizontal leads to voltmeter circle edge
        draw_wire(ax, [(r2_left[0],  y_vm), (x_vm - r_vm, y_vm)], lw=2)
        draw_wire(ax, [(x_vm + r_vm, y_vm), (r2_right[0], y_vm)], lw=2)

        draw_circle_meter(ax, x=x_vm, y=y_vm, letter="V", r=r_vm, fontsize=10)

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

        # --- Ammeter inline on top bus (wire stops at circle edge) ---
        x_A, y_A = 4.1, top_y
        r_A = 0.45
        A_left  = (x_A - r_A, y_A)
        A_right = (x_A + r_A, y_A)

        # Top bus split by ammeter
        draw_wire(ax, [(left_x, top_y), A_left], lw=2)
        draw_wire(ax, [A_right, (right_x, top_y)], lw=2)

        # Bottom bus (continuous)
        draw_wire(ax, [(left_x, bot_y), (right_x, bot_y)], lw=2)

        # Left vertical split for cell
        draw_wire(ax, [(left_x, top_y), (left_x, 7.5)], lw=2)
        draw_wire(ax, [(left_x, 3.0), (left_x, bot_y)], lw=2)
        draw_cell_vertical(ax, x=left_x, y_bottom=3.0, y_top=7.5,
                        value_text=f"{self.Vs} V", fontsize=10)

        # Draw ammeter symbol AFTER wires
        draw_circle_meter(ax, x=x_A, y=y_A, letter="A", r=r_A, fontsize=10)

        # Branches
        x1, x2 = 5.6, 7.3

        r1_top, r1_bot = draw_resistor_box(ax, x=x1, y=5.6, label="R1",
                                        value_text=f"{self.R1} Ω", fontsize=10)
        draw_wire(ax, [(x1, top_y), (x1, r1_top)], lw=2)
        draw_wire(ax, [(x1, r1_bot), (x1, bot_y)], lw=2)

        r2_top, r2_bot = draw_resistor_box(ax, x=x2, y=5.6, label="R2",
                                        value_text=f"{self.R2} Ω", fontsize=10)
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
        draw_cell_vertical(ax, x=left_x, y_bottom=3.0, y_top=7.0, value_text=f"{self.Vs} V", fontsize=10)

        # fixed resistor (connect to its TRUE top/bottom)
        rf_top, rf_bot = draw_resistor_box(ax, x=x_div, y=7.3, label="R", value_text=f"{self.R_fixed} Ω", fontsize=10)
        draw_wire(ax, [(x_div, top_y), (x_div, rf_top)], lw=2)

        # thermistor
        rt_top, rt_bot = draw_thermistor(ax, x=x_div, y=3.0, label="NTC", value_text=f"{self.R_T} Ω", fontsize=10)
        draw_wire(ax, [(x_div, rf_bot), (x_div, rt_top)], lw=2)
        draw_wire(ax, [(x_div, rt_bot), (x_div, bot_y)], lw=2)

        # voltmeter across thermistor (use meter terminals so it touches the circle)
        V = draw_circle_meter(ax, x=7.5, y=2.7, letter="V", r=0.45, fontsize=10)

        junction = (x_div, rt_top)   # top of thermistor
        draw_wire(ax, [junction, (7.5, rt_top)], lw=2)
        draw_wire(ax, [(7.5, rt_top), V["top"]], lw=2)
        draw_wire(ax, [(7.5, bot_y), V["bottom"]], lw=2)

        draw_text(ax, 8.1, 2.7, "Vout", fontsize=10, ha="left", boxed=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy054:
    """
    Bar magnet + point P. Arrow labels A/B/C/D are SHUFFLED each time.
    Also randomizes magnet orientation (horizontal/vertical) + pole arrangement + P location.
    """

    def __init__(self):
        # 1) Randomize magnet orientation
        self.orientation = rnd.choice(["horizontal", "vertical"])

        # 2) Randomize pole arrangement + choose a P location with an unambiguous local field direction
        if self.orientation == "horizontal":
            self.N_on_left = rnd.choice([True, False])
            self.P_pos = rnd.choice(["above", "below"])  # visual variety
            # At a point above/below the center, field is from N to S (left<->right)
            self.correct_dir = "right" if self.N_on_left else "left"
        else:
            self.N_on_top = rnd.choice([True, False])
            self.P_pos = rnd.choice(["left", "right"])   # visual variety
            # At a point left/right of the center, field is from N to S (top<->bottom)
            self.correct_dir = "down" if self.N_on_top else "up"

        # 3) Shuffle which letter labels which direction (many versions)
        dirs = ["up", "right", "down", "left"]
        letters = ["A", "B", "C", "D"]
        rnd.shuffle(letters)
        self.dir_to_label = dict(zip(dirs, letters))

        # Answer is the label on the correct direction arrow
        self.answer = self.dir_to_label[self.correct_dir]

        self.description = (
            "A bar magnet is shown with a point P. "
            "Which arrow (A, B, C, or D) shows the direction of the magnetic field at P? (_)"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electromagnetic effects"
        self.source = "Original"
        self.curriculum = "IGCSE"

        # Reasoning includes the shuffled label mapping
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Magnetic field lines outside a magnet go from N to S.}\\\\"
            f"\\text{{Magnet orientation}} &= \\text{{{self.orientation}}}\\\\"
            f"\\text{{Point location}} &= \\text{{{self.P_pos}}}\\\\"
            f"\\text{{Direction of field at P}} &= \\text{{{self.correct_dir}}}\\\\"
            f"\\text{{Arrow labels: Up={self.dir_to_label['up']}, Right={self.dir_to_label['right']}, "
            f"Down={self.dir_to_label['down']}, Left={self.dir_to_label['left']}}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 3.8))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # --- Draw magnet + poles + point P depending on orientation ---
        if self.orientation == "horizontal":
            # Magnet body
            mag = patches.Rectangle((2, 4), 6, 2, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(mag)

            # Poles
            if self.N_on_left:
                ax.text(2.6, 5, "N", ha="center", va="center", fontsize=14)
                ax.text(7.4, 5, "S", ha="center", va="center", fontsize=14)
            else:
                ax.text(2.6, 5, "S", ha="center", va="center", fontsize=14)
                ax.text(7.4, 5, "N", ha="center", va="center", fontsize=14)

            # Point P: above or below
            xP = 5.0
            yP = 8.0 if self.P_pos == "above" else 2.5
        else:
            # Vertical magnet body
            mag = patches.Rectangle((4, 2), 2, 6, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(mag)

            # Poles
            if self.N_on_top:
                ax.text(5.0, 7.4, "N", ha="center", va="center", fontsize=14)
                ax.text(5.0, 2.6, "S", ha="center", va="center", fontsize=14)
            else:
                ax.text(5.0, 7.4, "S", ha="center", va="center", fontsize=14)
                ax.text(5.0, 2.6, "N", ha="center", va="center", fontsize=14)

            # Point P: left or right
            yP = 5.0
            xP = 2.5 if self.P_pos == "left" else 7.5

        # Draw point P
        ax.plot([xP], [yP], marker="o", markersize=5, color="black")
        ax.text(xP + 0.2, yP, "P", ha="left", va="center", fontsize=12)

        # --- Draw option arrows around P, but labels are SHUFFLED ---
        L = 1.2
        arrow(ax, xP, yP, 0,  L, label=self.dir_to_label["up"],    label_offset=(0.0,  0.25))
        arrow(ax, xP, yP, L,  0, label=self.dir_to_label["right"], label_offset=(0.25, 0.0))
        arrow(ax, xP, yP, 0, -L, label=self.dir_to_label["down"],  label_offset=(0.0, -0.25))
        arrow(ax, xP, yP, -L, 0, label=self.dir_to_label["left"],  label_offset=(-0.25, 0.0))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy055:
    """
    Force on a current-carrying conductor in a magnetic field.
    Randomizes:
      - B direction axis (horizontal or vertical)
      - B direction sign (+/-)
      - current direction (into/out of page)
      - SHUFFLES labels A/B/C/D on the four option arrows
    """

    def __init__(self):
        # Randomize field axis and direction
        self.B_axis = rnd.choice(["x", "y"])     # x = horizontal, y = vertical
        self.B_dir = rnd.choice([1, -1])         # + means right/up; - means left/down

        # Current direction: +1 out of page (dot), -1 into page (cross)
        self.I_dir = rnd.choice([1, -1])

        # Compute force direction using F = I x B with I along ±z
        # If B=(Bx,By,0) and I=(0,0,I):
        # Fx = -I*By, Fy = I*Bx
        Bx = self.B_dir if self.B_axis == "x" else 0
        By = self.B_dir if self.B_axis == "y" else 0
        Fx = -self.I_dir * By
        Fy =  self.I_dir * Bx

        if Fx != 0:
            self.correct_dir = "right" if Fx > 0 else "left"
        else:
            self.correct_dir = "up" if Fy > 0 else "down"

        # Shuffle labels on the four arrows (huge variety)
        dirs = ["up", "right", "down", "left"]
        letters = ["A", "B", "C", "D"]
        rnd.shuffle(letters)
        self.dir_to_label = dict(zip(dirs, letters))

        self.answer = self.dir_to_label[self.correct_dir]

        self.description = (
            "A wire is placed in a magnetic field as shown. The current direction is given on the diagram. "
            "Which arrow (A, B, C, or D) shows the direction of the force on the wire? (_)"
        )
        self.topic = "Electricity and magnetism"
        self.subtopic = "Electromagnetic effects"
        self.source = "Original"
        self.curriculum = "IGCSE"

        # Reasoning includes the shuffled mapping
        B_text = (
            ("right" if self.B_dir == 1 else "left") if self.B_axis == "x"
            else ("up" if self.B_dir == 1 else "down")
        )
        I_text = "out of page (•)" if self.I_dir == 1 else "into page (×)"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Use }\\vec{F}\\propto \\vec{I}\\times\\vec{B}.\\\\"
            f"\\text{{Magnetic field direction}} &= \\text{{{B_text}}}\\\\"
            f"\\text{{Current direction}} &= \\text{{{I_text}}}\\\\"
            f"\\text{{Force direction}} &= \\text{{{self.correct_dir}}}\\\\"
            f"\\text{{Arrow labels: Up={self.dir_to_label['up']}, Right={self.dir_to_label['right']}, "
            f"Down={self.dir_to_label['down']}, Left={self.dir_to_label['left']}}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        setup_ax(ax, xlim=(0, 10), ylim=(0, 10))

        # Wire position
        xW, yW = 5.0, 5.0

        # --- Draw magnet blocks depending on B-axis ---
        if self.B_axis == "x":
            # Side-by-side blocks
            left = patches.Rectangle((1.2, 3), 2, 4, fill=False, linewidth=2, edgecolor="black")
            right = patches.Rectangle((6.8, 3), 2, 4, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(left)
            ax.add_patch(right)

            # Poles define B direction across the gap (N -> S)
            if self.B_dir == 1:  # field to the right
                ax.text(2.2, 5, "N", ha="center", va="center", fontsize=14)
                ax.text(7.8, 5, "S", ha="center", va="center", fontsize=14)
                arrow(ax, 3.5, 8.2, 3.0, 0.0, label=None)
            else:                # field to the left
                ax.text(2.2, 5, "S", ha="center", va="center", fontsize=14)
                ax.text(7.8, 5, "N", ha="center", va="center", fontsize=14)
                arrow(ax, 6.5, 8.2, -3.0, 0.0, label=None)
        else:
            # Top-bottom blocks
            top = patches.Rectangle((3.0, 6.8), 4.0, 2.0, fill=False, linewidth=2, edgecolor="black")
            bottom = patches.Rectangle((3.0, 1.2), 4.0, 2.0, fill=False, linewidth=2, edgecolor="black")
            ax.add_patch(top)
            ax.add_patch(bottom)

            # Poles define B direction (N -> S) vertically through the gap
            if self.B_dir == 1:  # field up
                ax.text(5.0, 2.2, "N", ha="center", va="center", fontsize=14)
                ax.text(5.0, 7.8, "S", ha="center", va="center", fontsize=14)
                arrow(ax, 8.8, 3.5, 0.0, 3.0, label=None)
            else:                # field down
                ax.text(5.0, 2.2, "S", ha="center", va="center", fontsize=14)
                ax.text(5.0, 7.8, "N", ha="center", va="center", fontsize=14)
                arrow(ax, 8.8, 6.5, 0.0, -3.0, label=None)

        # Current symbol at the wire (must be visible!)
        draw_current_symbol(ax, x=xW, y=yW, direction=self.I_dir, r=0.40, lw=2)

        # Option arrows around the wire with SHUFFLED labels
        L = 1.5
        arrow(ax, xW, yW, 0,  L, label=self.dir_to_label["up"],    label_offset=(0.0,  0.25))
        arrow(ax, xW, yW, L,  0, label=self.dir_to_label["right"], label_offset=(0.25, 0.0))
        arrow(ax, xW, yW, 0, -L, label=self.dir_to_label["down"],  label_offset=(0.0, -0.25))
        arrow(ax, xW, yW, -L, 0, label=self.dir_to_label["left"],  label_offset=(-0.25, 0.0))

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


class Phy059:
    """
    SI units (prefixes), uses Q = I t
    """
    def __init__(self):
        # Randomised readings
        self.I_mA = rnd.randint(10, 99) / 10      # 1.0 to 9.9 mA (1 d.p.)
        self.t_ms = rnd.randint(20, 250)          # 20 to 250 ms

        # Calculation
        self.q_C = self.I_mA * self.t_ms * 1e-6   # (mA)(ms) = microcoulomb = 1e-6 C
        self.answer = sig_figs(self.q_C, 3)      # answer stored in C (3 s.f.)

        # Metadata
        self.topic = "Physical quantities and units"
        self.subtopic = "SI units"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            f"An ammeter shows a current of {self.I_mA:.1f} mA flowing for {self.t_ms} ms (see image). "
            "Calculate the charge transferred. Give your answer in coulombs (C).\n"
            "Charge transferred = (_) C"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Current, }} I &= {self.I_mA:.1f}\\,\\text{{mA}}\\\\"
            f"\\text{{Time, }} t &= {self.t_ms}\\,\\text{{ms}}\\\\"
            "\\text{{Convert to SI base units:}} &\\\\"
            f"I &= {self.I_mA:.1f} \\times 10^{{-3}}\\,\\text{{A}} = {round(self.I_mA * 1e-3, 10)}\\,\\text{{A}}\\\\"
            f"t &= {self.t_ms} \\times 10^{{-3}}\\,\\text{{s}} = {round(self.t_ms * 1e-3, 10)}\\,\\text{{s}}\\\\"
            "\\text{{The charge transferred is given by:}} &\\\\"
            "Q &= I \\times t\\\\"
            f"&= ({round(self.I_mA * 1e-3, 10)}\\,\\text{{A}}) \\times ({round(self.t_ms * 1e-3, 10)}\\,\\text{{s}})\\\\"
            f"&= {self.answer}\\,\\text{{C}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        # Draw a simple “ammeter + timer” diagram with randomised readings
        fig, ax = plt.subplots(figsize=(7, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis("off")

        # Ammeter body
        am = patches.FancyBboxPatch(
            (0.7, 1.6), 4.0, 2.8,
            boxstyle="round,pad=0.25,rounding_size=0.25",
            linewidth=2, edgecolor="black", facecolor="white"
        )
        ax.add_patch(am)
        ax.text(2.7, 3.6, "A", fontsize=28, fontweight="bold", ha="center", va="center")
        ax.text(
            2.7, 2.4, f"{self.I_mA:.1f} mA",
            fontsize=14, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="black", pad=0.4)
        )
        ax.text(2.7, 4.35, "ammeter", fontsize=10, ha="center", va="bottom")

        # Timer / stopwatch
        sw = patches.Circle((7.4, 3.0), 1.35, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(sw)
        ax.add_patch(
            patches.Rectangle((7.05, 4.45), 0.7, 0.35,
                              fill=True, facecolor="white", edgecolor="black", linewidth=2)
        )
        ax.text(
            7.4, 3.0, f"{self.t_ms} ms",
            fontsize=14, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="black", pad=0.35)
        )
        ax.text(7.4, 4.85, "timer", fontsize=10, ha="center", va="bottom")

        ax.text(5.0, 0.7, "Current flows for the time shown", fontsize=10, ha="center", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy060:
    """
    Errors and uncertainties, propagation for v = L/t
    """
    def __init__(self):
        # Randomised measurements
        self.L = rnd.randint(60, 180) / 100                 # 0.60 to 1.80 m (2 d.p.)
        self.dL = rnd.choice([0.001, 0.002, 0.003, 0.005])  # m
        self.t = rnd.randint(15, 60) / 10                   # 1.5 to 6.0 s (1 d.p.)
        self.dt = rnd.choice([0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15])  # s

        # Calculations
        self.v = self.L / self.t
        self.frac_unc = (self.dL / self.L) + (self.dt / self.t)   # add fractional uncertainties
        self.perc_unc = self.frac_unc * 100
        self.dv = self.v * self.frac_unc

        self.v_ans = sig_figs(self.v, 3)
        self.dv_ans = sig_figs(self.dv, 2)  # uncertainty typically 1–2 s.f.
        self.answer = f"{self.v_ans} ± {self.dv_ans} m s⁻¹"
        self.topic = "Physical quantities and units"
        self.subtopic = "Errors and uncertainties"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            "A trolley travels a measured distance and the time taken is recorded (see image).\n"
            f"Distance: L = {self.L:.2f} ± {self.dL:.3f} m\n"
            f"Time: t = {self.t:.1f} ± {self.dt:.2f} s\n"
            "Calculate the speed v and the absolute uncertainty in v.\n"
            "v = (_) ± (_) m s⁻¹"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Measured distance, }} L &= {self.L:.2f} \\pm {self.dL:.3f}\\,\\text{{m}}\\\\"
            f"\\text{{Measured time, }} t &= {self.t:.1f} \\pm {self.dt:.2f}\\,\\text{{s}}\\\\"
            "\\text{{The speed }} v \\text{{ is calculated using:}} &\\\\"
            "v &= \\frac{L}{t}\\\\"
            f"&= \\frac{{{self.L:.2f}}}{{{self.t:.1f}}}\\\\"
            f"&= {round(self.v, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{For a quotient, fractional uncertainties are added:}} &\\\\"
            "\\frac{\\Delta v}{v} &= \\frac{\\Delta L}{L} + \\frac{\\Delta t}{t}\\\\"
            f"&= \\frac{{{self.dL:.3f}}}{{{self.L:.2f}}} + \\frac{{{self.dt:.2f}}}{{{self.t:.1f}}}\\\\"
            f"&= {round(self.dL / self.L, 10)} + {round(self.dt / self.t, 10)}\\\\"
            f"&= {round(self.frac_unc, 10)}\\\\"
            "\\text{{Calculate absolute uncertainty }} \\Delta v: &\\\\"
            "\\Delta v &= v \\times \\left( \\frac{\\Delta v}{v} \\right)\\\\"
            f"&= {round(self.v, 10)} \\times {round(self.frac_unc, 10)}\\\\"
            f"&= {round(self.dv, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis("off")

        # Distance double-arrow (cleaner than manual arrows)
        ax.annotate(
            "", xy=(1.0, 1.0), xytext=(9.0, 1.0),
            arrowprops=dict(arrowstyle="<->", linewidth=2, color="black")
        )
        ax.text(
            5.0, 1.35, f"L = {self.L:.2f} ± {self.dL:.3f} m",
            fontsize=12, ha="center", va="bottom",
            bbox=dict(facecolor="white", edgecolor="black", pad=0.35)
        )

        # Stopwatch
        sw = patches.Circle((2.3, 3.4), 1.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(sw)
        ax.add_patch(
            patches.Rectangle((2.0, 4.45), 0.6, 0.3,
                              fill=True, facecolor="white", edgecolor="black", linewidth=2)
        )
        ax.text(
            2.3, 3.4, f"t = {self.t:.1f} ± {self.dt:.2f} s",
            fontsize=11, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="black", pad=0.25)
        )

        # Simple trolley
        cart = patches.Rectangle((6.8, 2.8), 1.8, 1.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(cart)
        ax.add_patch(patches.Circle((7.2, 2.8), 0.18, fill=False, linewidth=2, edgecolor="black"))
        ax.add_patch(patches.Circle((8.2, 2.8), 0.18, fill=False, linewidth=2, edgecolor="black"))
        ax.text(7.7, 3.35, "trolley", fontsize=10, ha="center", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy061:
    """
    Scalars and vectors (coplanar addition via components)
    """
    def __init__(self):
        # Randomised forces and angles
        self.F1 = rnd.randint(4, 10)            # N
        self.F2 = rnd.randint(3, 9)             # N
        self.theta1 = rnd.randrange(20, 71, 5)  # degrees above +x
        self.theta2 = -rnd.randrange(20, 71, 5) # degrees below +x (negative)

        # Components
        th1 = math.radians(self.theta1)
        th2 = math.radians(self.theta2)

        self.F1x = self.F1 * math.cos(th1)
        self.F1y = self.F1 * math.sin(th1)
        self.F2x = self.F2 * math.cos(th2)
        self.F2y = self.F2 * math.sin(th2)

        self.Rx = self.F1x + self.F2x
        self.Ry = self.F1y + self.F2y
        self.R = math.hypot(self.Rx, self.Ry)
        self.answer = sig_figs(self.R, 3)      # magnitude (3 s.f.)
        self.topic = "Physical quantities and units"
        self.subtopic = "Scalars and vectors"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            "Two forces act at a point as shown (see image).\n"
            f"F₁ = {self.F1} N at {self.theta1}° above the +x-axis.\n"
            f"F₂ = {self.F2} N at {abs(self.theta2)}° below the +x-axis.\n"
            "Calculate the magnitude of the resultant force.\n"
            "Resultant magnitude = (_) N"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Force }} F_1 &= {self.F1}\\,\\text{{N at }} {self.theta1}^\\circ \\text{{ above }} +x\\\\"
            f"\\text{{Force }} F_2 &= {self.F2}\\,\\text{{N at }} {abs(self.theta2)}^\\circ \\text{{ below }} +x\\\\"
            "\\text{{Resolve each force into its components:}} &\\\\"
            "F_{1x} &= F_1 \\cos(\\theta_1) = " + f"{self.F1} \\cos({self.theta1}^\\circ) = {round(self.F1x, 10)}\\,\\text{{N}}\\\\"
            "F_{1y} &= F_1 \\sin(\\theta_1) = " + f"{self.F1} \\sin({self.theta1}^\\circ) = {round(self.F1y, 10)}\\,\\text{{N}}\\\\"
            "F_{2x} &= F_2 \\cos(\\theta_2) = " + f"{self.F2} \\cos({self.theta2}^\\circ) = {round(self.F2x, 10)}\\,\\text{{N}}\\\\"
            "F_{2y} &= F_2 \\sin(\\theta_2) = " + f"{self.F2} \\sin({self.theta2}^\\circ) = {round(self.F2y, 10)}\\,\\text{{N}}\\\\"
            "\\text{{Sum the components to find the resultant components:}} &\\\\"
            "R_x &= F_{1x} + F_{2x} = " + f"{round(self.F1x, 10)} + {round(self.F2x, 10)} = {round(self.Rx, 10)}\\,\\text{{N}}\\\\"
            "R_y &= F_{1y} + F_{2y} = " + f"{round(self.F1y, 10)} + {round(self.F2y, 10)} = {round(self.Ry, 10)}\\,\\text{{N}}\\\\"
            "\\text{{Calculate the magnitude of the resultant force }} R: &\\\\"
            "R &= \\sqrt{R_x^2 + R_y^2}\\\\"
            f"&= \\sqrt{{({round(self.Rx, 10)})^2 + ({round(self.Ry, 10)})^2}}\\\\"
            f"&= \\sqrt{{{round(self.Rx**2, 10)} + {round(self.Ry**2, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        # Endpoints for arrows
        th1 = math.radians(self.theta1)
        th2 = math.radians(self.theta2)
        x1, y1 = self.F1 * math.cos(th1), self.F1 * math.sin(th1)
        x2, y2 = self.F2 * math.cos(th2), self.F2 * math.sin(th2)

        max_extent = max(abs(x1), abs(y1), abs(x2), abs(y2), self.F1, self.F2) + 2

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_aspect("equal")
        ax.set_xlim(-1, max_extent)
        ax.set_ylim(-max_extent / 1.5, max_extent / 1.2)
        ax.axis("off")

        # Axes
        ax.annotate("", xy=(max_extent - 0.4, 0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(0, max_extent / 1.25), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(max_extent - 0.2, -0.45, "+x", fontsize=10, ha="right", va="top")
        ax.text(-0.25, max_extent / 1.25, "+y", fontsize=10, ha="right", va="bottom")
        ax.plot(0, 0, "ko", markersize=5)

        # Vectors (labels include randomised magnitudes)
        draw_labeled_arrow(ax, (0, 0), (x1, y1), label=f"F₁ = {self.F1} N",
                           label_position="top", label_offset=0.6, fontsize=10)
        draw_labeled_arrow(ax, (0, 0), (x2, y2), label=f"F₂ = {self.F2} N",
                           label_position="bottom", label_offset=0.6, fontsize=10)

        # Angle arcs + labels
        r1 = min(2.5, self.F1 * 0.5 + 1.2)
        arc1 = patches.Arc((0, 0), 2 * r1, 2 * r1, angle=0, theta1=0, theta2=self.theta1,
                           linewidth=1.6, color="black")
        ax.add_patch(arc1)
        mid1 = math.radians(self.theta1 / 2)
        ax.text(r1 * math.cos(mid1) + 0.15, r1 * math.sin(mid1) + 0.15,
                f"{self.theta1}°", fontsize=10,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        r2 = min(2.1, self.F2 * 0.5 + 1.0)
        arc2 = patches.Arc((0, 0), 2 * r2, 2 * r2, angle=0, theta1=self.theta2, theta2=0,
                           linewidth=1.6, color="black")
        ax.add_patch(arc2)
        mid2 = math.radians(self.theta2 / 2)
        ax.text(r2 * math.cos(mid2) + 0.15, r2 * math.sin(mid2) - 0.15,
                f"{abs(self.theta2)}°", fontsize=10,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy062:
    """
    Displacement–time graph.
    Use gradient of displacement–time graph to find velocity between two points.
    """

    def __init__(self):
        # Choose uniform velocity so graph is a straight line through origin
        self.v = rnd.randint(2, 6)  # m s^-1
        self.tA = rnd.randint(2, 4)                  # s
        self.tB = rnd.randint(self.tA + 2, self.tA + 5)  # s (ensure separation)
        if self.tB > 9:
            self.tB = 9

        self.sA = self.v * self.tA  # m
        self.sB = self.v * self.tB  # m

        self.answer = round(self.v, 2)

        self.description = (
            "The displacement–time graph shows the motion of a particle. "
            "Determine the velocity between points A and B. (_) m s⁻¹"
        )
        self.topic = "Kinematics"
        self.subtopic = "Equations of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Point A}} &= ({self.tA}\\,\\text{{s}}, {self.sA}\\,\\text{{m}})\\\\"
            f"\\text{{Point B}} &= ({self.tB}\\,\\text{{s}}, {self.sB}\\,\\text{{m}})\\\\"
            "\\text{{The velocity is the gradient of the displacement--time graph:}} &\\\\"
            "v &= \\frac{\\Delta s}{\\Delta t}\\\\"
            "v &= \\frac{s_B - s_A}{t_B - t_A}\\\\"
            f"&= \\frac{{{self.sB} - {self.sA}}}{{{self.tB} - {self.tA}}}\\\\"
            f"&= \\frac{{{round(self.sB - self.sA, 10)}}}{{{round(self.tB - self.tA, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))

        # Axes ranges (comfortable padding)
        t_max = 10
        s_max = max(60, self.sB + 6)

        style_graph(
            ax,
            xlabel="time / s",
            ylabel="displacement / m",
            xlim=(0, t_max),
            ylim=(0, s_max),
            xticks=list(range(0, t_max + 1, 1)),
            yticks=list(range(0, s_max + 1, 5)),
        )

        # Main line (uniform motion)
        ax.plot([0, self.tB], [0, self.sB], linewidth=2)

        # Points A and B
        ax.plot(self.tA, self.sA, marker="o", markersize=5)
        ax.plot(self.tB, self.sB, marker="o", markersize=5)

        ax.text(
            self.tA + 0.2, self.sA + 1.5, f"A({self.tA} s, {self.sA} m)",
            fontsize=10, ha="left", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=0.2)
        )
        ax.text(
            self.tB + 0.2, self.sB + 1.5, f"B({self.tB} s, {self.sB} m)",
            fontsize=10, ha="left", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=0.2)
        )

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy063:
    """
    Velocity–time graph.
    Use area under velocity–time graph to find displacement for constant acceleration.
    """

    def __init__(self):
        # Choose values that give a neat integer displacement
        while True:
            self.u = rnd.randint(2, 10)        # m s^-1
            self.a = rnd.randint(1, 4)         # m s^-2
            self.t = rnd.choice([4, 6, 8])     # s (even -> displacement integer)
            self.v = self.u + self.a * self.t  # m s^-1
            if self.v <= 28:
                break

        self.s = self.u * self.t + 0.5 * self.a * self.t**2  # m
        self.answer = round(self.s, 2)

        self.description = (
            "The velocity–time graph shows the motion of a particle for the first "
            f"{self.t} s. Determine the displacement in this time. (_) m"
        )
        self.topic = "Kinematics"
        self.subtopic = "Equations of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial velocity, }} u &= {self.u}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Final velocity, }} v &= {self.v}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Time interval, }} t &= {self.t}\\,\\text{{s}}\\\\"
            "\\text{{The displacement is the area under the velocity--time graph.}} &\\\\"
            "\\text{{For constant acceleration, the area is a trapezium:}} &\\\\"
            "s &= \\text{Area} = \\frac{1}{2}(u + v)t\\\\"
            f"&= \\frac{{1}}{{2}}({self.u} + {self.v}) \\times {self.t}\\\\"
            f"&= \\frac{{1}}{{2}}({round(self.u + self.v, 10)}) \\times {self.t}\\\\"
            f"&= {round(0.5 * (self.u + self.v), 10)} \\times {self.t}\\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))

        t_max = max(10, self.t + 2)
        v_max = max(30, self.v + 6)

        style_graph(
            ax,
            xlabel="time / s",
            ylabel="velocity / m s$^{-1}$",
            xlim=(0, t_max),
            ylim=(0, v_max),
            xticks=list(range(0, t_max + 1, 1)),
            yticks=list(range(0, v_max + 1, 5)),
        )

        # Line from (0,u) to (t,v)
        ax.plot([0, self.t], [self.u, self.v], linewidth=2)

        # Shade area under graph
        ax.fill_between([0, self.t], [self.u, self.v], [0, 0], alpha=0.25)

        # Mark endpoints
        ax.plot(0, self.u, marker="o", markersize=5)
        ax.plot(self.t, self.v, marker="o", markersize=5)

        ax.text(
            0.2, self.u + 1.5, f"(0 s, {self.u} m s⁻¹)",
            fontsize=10, ha="left", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=0.2)
        )
        ax.text(
            self.t + 0.2, self.v + 1.5, f"({self.t} s, {self.v} m s⁻¹)",
            fontsize=10, ha="left", va="bottom",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=0.2)
        )

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy064:
    """
    Uniformly accelerated motion in a gravitational field (no air resistance).
    Drop from rest: use v^2 = u^2 + 2as to find impact speed.
    """

    def __init__(self):
        self.h = rnd.randrange(10, 85, 5)  # m
        self.g = 9.81                      # m s^-2
        self.v = math.sqrt(2 * self.g * self.h)  # m s^-1
        self.answer = sig_figs(self.v, 3)

        self.description = (
            f"A ball is dropped from rest from a height of {self.h} m as shown. "
            "Neglect air resistance. Take g = 9.81 m s⁻². "
            "Calculate the speed just before it hits the ground. (_) m s⁻¹"
        )
        self.topic = "Kinematics"
        self.subtopic = "Equations of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial velocity, }} u &= 0\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Height (displacement), }} s &= {self.h}\\,\\text{{m}}\\\\"
            f"\\text{{Acceleration due to gravity, }} a &= {self.g}\\,\\text{{m s}}^{{-2}}\\\\"
            "\\text{{Using the equation of motion:}} &\\\\"
            "v^2 &= u^2 + 2as\\\\"
            f"v^2 &= 0^2 + 2({self.g})({self.h})\\\\"
            f"v^2 &= {round(2 * self.g * self.h, 10)}\\\\"
            f"v &= \\sqrt{{{round(2 * self.g * self.h, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        # Ground
        ax.plot([0.5, 9.5], [1.0, 1.0], linewidth=2)

        # Cliff / platform
        ax.add_patch(plt.Rectangle((1.0, 1.0), 2.0, 7.0, fill=False, linewidth=2))
        ax.text(2.0, 8.2, "platform", fontsize=10, ha="center", va="bottom")

        # Ball at top edge
        ball_x, ball_y = 3.4, 8.0
        ax.add_patch(plt.Circle((ball_x, ball_y), 0.18, fill=False, linewidth=2))

        # Fall arrow
        ax.annotate(
            "", xy=(ball_x, 1.2), xytext=(ball_x, ball_y - 0.2),
            arrowprops=dict(arrowstyle="->", linewidth=2)
        )
        ax.text(ball_x + 0.35, 4.8, "fall", fontsize=10, ha="left", va="center")

        # Height bracket
        ax.annotate(
            "", xy=(4.8, 8.0), xytext=(4.8, 1.0),
            arrowprops=dict(arrowstyle="<->", linewidth=2)
        )
        ax.text(
            5.1, 4.5, f"h = {self.h} m",
            fontsize=10, ha="left", va="center",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.9, pad=0.2)
        )

        # g label
        ax.text(6.8, 2.0, "g = 9.81 m s⁻²", fontsize=10, ha="left", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy065:
    """
    Momentum & Newton’s laws: impulse from force–time graph
    Force–time triangular pulse on a trolley.
    Use impulse = area under F–t graph and Δp = impulse to find final speed.
    """

    def __init__(self):
        while True:
            self.m = rnd.choice([0.50, 0.80, 1.00, 1.20, 1.50, 2.00])  # kg
            self.Fmax = rnd.choice([80, 100, 120, 140, 160, 180, 200, 220])  # N
            self.T = rnd.choice([0.10, 0.15, 0.20, 0.25, 0.30])  # s
            self.u = rnd.randint(0, 5)  # m s^-1

            self.impulse = 0.5 * self.Fmax * self.T  # N s
            self.v = self.u + self.impulse / self.m  # m s^-1

            if 4 <= self.v <= 30:
                break

        self.answer = sig_figs(self.v, 3)

        self.description = (
            f"A trolley of mass {self.m:.2f} kg moves in a straight line with initial speed {self.u} m s⁻¹. "
            "A resultant force acts in the direction of motion. The force varies with time as shown in the graph.\n"
            "Determine the speed of the trolley at the end of the force pulse. (_) m s⁻¹"
        )

        self.topic = "Dynamics"
        self.subtopic = "Momentum and Newton’s laws of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m:.2f}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial speed, }} u &= {self.u}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Peak force, }} F_{{max}} &= {self.Fmax}\\,\\text{{N}}\\\\"
            f"\\text{{Duration, }} T &= {self.T:.2f}\\,\\text{{s}}\\\\"
            "\\text{{The impulse is the area under the force--time graph.}} &\\\\"
            "\\text{{For a triangular pulse:}} &\\\\"
            "J &= \\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}\\\\"
            f"J &= \\frac{{1}}{{2}} \\times {self.T:.2f} \\times {self.Fmax}\\\\"
            f"&= {round(self.impulse, 10)}\\,\\text{{N s}}\\\\"
            "\\text{{Impulse is equal to the change in momentum:}} &\\\\"
            "J &= \\Delta p = m(v - u)\\\\"
            "\\text{{Rearranging for final speed }} v: &\\\\"
            "v &= u + \\frac{J}{m}\\\\"
            f"&= {self.u} + \\frac{{{round(self.impulse, 10)}}}{{{self.m:.2f}}}\\\\"
            f"&= {self.u} + {round(self.impulse / self.m, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6, 4))

        # Triangle pulse: 0 -> T/2 -> T
        ax.plot([0, self.T / 2, self.T], [0, self.Fmax, 0], linewidth=2, color="black")

        ax.set_xlabel("time / s", fontsize=10)
        ax.set_ylabel("force / N", fontsize=10)
        ax.tick_params(axis="both", labelsize=10)

        ax.set_xlim(0, self.T * 1.25)
        ax.set_ylim(0, self.Fmax * 1.25)
        ax.grid(True, linestyle="--", alpha=0.5)

        # Labels: Fmax and duration
        ax.plot(self.T / 2, self.Fmax, "ko", markersize=4)
        ax.text(self.T / 2, self.Fmax * 1.05, f"{self.Fmax} N", fontsize=10,
                ha="center", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy066:
    """
    Two blocks on a smooth horizontal surface, connected by a light inextensible taut string.
    A horizontal force F is applied to the RIGHT block (m2) pulling the system to the right.
    Ask for the tension in the string.

    Assumptions: smooth surface, light string, taut, no slack.
    """

    def __init__(self):
        # Construct neat integers using F = (m1+m2)a
        while True:
            self.m1 = rnd.randint(1, 6)  # kg (left block)
            self.m2 = rnd.randint(1, 6)  # kg (right block)
            self.a = rnd.randint(1, 4)   # m s^-2
            self.F = self.a * (self.m1 + self.m2)  # N
            if 12 <= self.F <= 90:
                break

        # With force applied to m2, tension accelerates m1:
        self.T = self.m1 * self.a
        self.answer = round(self.T, 2)

        self.description = (
            f"Two blocks of masses {self.m1} kg and {self.m2} kg are connected by a light inextensible string "
            "on a smooth horizontal surface. A horizontal force is applied to the right-hand block as shown.\n"
            f"The applied force is F = {self.F} N. Determine the tension in the string. (_) N"
        )

        self.topic = "Dynamics"
        self.subtopic = "Momentum and Newton’s laws of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of left block, }} m_1 &= {self.m1}\\,\\text{{kg}}\\\\"
            f"\\text{{Mass of right block, }} m_2 &= {self.m2}\\,\\text{{kg}}\\\\"
            f"\\text{{Applied force, }} F &= {self.F}\\,\\text{{N}}\\\\"
            "\\text{{Step 1: Calculate the acceleration of the whole system.}} &\\\\"
            "\\text{{Since the string is inextensible and taut, both blocks move with the same acceleration, }} a. &\\\\"
            "F &= (m_1 + m_2)a\\\\"
            f"a &= \\frac{{F}}{{m_1 + m_2}}\\\\"
            f"&= \\frac{{{self.F}}}{{{self.m1} + {self.m2}}}\\\\"
            f"&= \\frac{{{self.F}}}{{{self.m1 + self.m2}}}\\\\"
            f"&= {round(self.a, 10)}\\,\\text{{m s}}^{{-2}}\\\\"
            "\\text{{Step 2: Consider the forces on the left block (}} m_1 \\text{{) to find tension.}} &\\\\"
            "\\text{{The only horizontal force acting on }} m_1 \\text{{ is the tension, }} T, \\text{{ pulling it to the right.}} &\\\\"
            "T &= m_1 \\times a\\\\"
            f"&= {self.m1} \\times {round(self.a, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        # Enforce global font size = 10
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.4, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Track / ground
        ax.plot([0.5, 9.5], [0.9, 0.9], linewidth=2, color="black")
        ax.text(0.6, 0.55, "smooth surface", fontsize=10, ha="left", va="center")

        # Block geometry
        y0 = 0.9
        h = 1.2
        w = 2.2

        # Place blocks with a clear gap
        x1 = 1.6          # left block
        gap = 1.4
        x2 = x1 + w + gap # right block

        # Draw blocks
        b1 = patches.Rectangle((x1, y0), w, h, fill=False, linewidth=2, edgecolor="black")
        b2 = patches.Rectangle((x2, y0), w, h, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(b1)
        ax.add_patch(b2)

        # Mass labels (above blocks)
        ax.text(x1 + w/2, y0 + h + 0.35, f"m₁ = {self.m1} kg", fontsize=10, ha="center", va="bottom")
        ax.text(x2 + w/2, y0 + h + 0.35, f"m₂ = {self.m2} kg", fontsize=10, ha="center", va="bottom")

        # String (distinct and clearly between blocks)
        y_string = y0 + 0.75*h
        xL = x1 + w
        xR = x2
        ax.plot([xL, xR], [y_string, y_string], linewidth=2, color="black")
        # little "hooks" so it reads as a string connection
        ax.add_patch(patches.Circle((xL, y_string), 0.06, fill=True, color="black"))
        ax.add_patch(patches.Circle((xR, y_string), 0.06, fill=True, color="black"))
        ax.text((xL + xR)/2, y_string + 0.25, "string", fontsize=10, ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Applied force on RIGHT block (clear, no overlap)
        yF = y0 + 0.35*h
        ax.annotate("", xy=(x2 + w + 0.9, yF), xytext=(x2 + w, yF),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(x2 + w + 0.95, yF, f"F = {self.F} N", fontsize=10, ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Acceleration arrow above both blocks (single arrow)
        yA = 3.35
        ax.annotate("", xy=(8.9, yA), xytext=(7.7, yA),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(9.05, yA, "a", fontsize=10, ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy067:
    """
    Momentum & Newton’s laws: lift scale reading (Newton’s 2nd law)
    Person in a lift accelerating vertically.
    Use Newton's 2nd law: N - mg = ma (sign depends on direction).
    """

    def __init__(self):
        self.m = rnd.randint(50, 90)  # kg
        self.a = rnd.choice([0.5, 0.8, 1.0, 1.2, 1.5, 2.0])  # m s^-2
        self.g = 9.81

        self.direction = rnd.choice(["up", "down"])

        if self.direction == "up":
            self.N = self.m * (self.g + self.a)
            dir_text = "upwards"
        else:
            self.N = self.m * (self.g - self.a)
            dir_text = "downwards"

        self.answer = sig_figs(self.N, 3)

        self.description = (
            f"A person of mass {self.m} kg stands on a scale in a lift. "
            f"The lift accelerates {dir_text} at {self.a:.1f} m s⁻². "
            "Take g = 9.81 m s⁻².\n"
            "Determine the reading of the scale (the normal reaction). (_) N"
        )

        self.topic = "Dynamics"
        self.subtopic = "Momentum and Newton’s laws of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of the person, }} m &= {self.m}\\,\\text{{kg}}\\\\"
            f"\\text{{Acceleration, }} a &= {self.a:.1f}\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Acceleration due to gravity, }} g &= 9.81\\,\\text{{m s}}^{{-2}}\\\\"
            "\\text{{Identify the forces acting on the person:}} &\\\\"
            "\\text{1. Weight (downward)} &= mg\\\\"
            "\\text{2. Normal reaction/Scale reading (upward)} &= N\\\\"
            "\\text{{Apply Newton's Second Law (}} F_{{net}} = ma \\text{{):}} &\\\\"
            f"{'\\text{Since acceleration is upwards, the net force is } N - mg: ' if self.direction == 'up' else '\\text{Since acceleration is downwards, the net force is } mg - N: '}\\\\"
            f"{'N - mg &= ma' if self.direction == 'up' else 'mg - N &= ma'}\\\\"
            "\\text{{Rearrange to solve for the normal reaction }} N: &\\\\"
            f"{'N &= m(g + a)' if self.direction == 'up' else 'N &= m(g - a)'}\\\\"
            f"N &= {self.m} \\times ({9.81} {'+' if self.direction == 'up' else '-'} {self.a:.1f})\\\\"
            f"N &= {self.m} \\times {round(self.g + self.a if self.direction == 'up' else self.g - self.a, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(5.5, 4))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Lift box
        lift = patches.Rectangle((2, 2), 6, 6, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(lift)
        ax.text(5, 8.2, "lift", fontsize=10, ha="center", va="bottom")

        # Floor line inside lift
        ax.plot([2.2, 7.8], [3.0, 3.0], linewidth=2, color="black")
        ax.text(8.5, 3.0, "scale", fontsize=10, ha="left", va="center")

        # Person (simple)
        head = patches.Circle((5, 5.3), 0.45, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(head)
        ax.plot([5, 5], [4.85, 3.5], linewidth=2, color="black")  # body
        ax.plot([5, 4.4], [4.3, 3.9], linewidth=2, color="black")  # left arm
        ax.plot([5, 5.6], [4.3, 3.9], linewidth=2, color="black")  # right arm
        ax.plot([5, 4.6], [3.5, 3.1], linewidth=2, color="black")  # left leg
        ax.plot([5, 5.4], [3.5, 3.1], linewidth=2, color="black")  # right leg

        # Forces on person
        # Normal reaction N (up)
        ax.annotate("", xy=(5, 6.9), xytext=(5, 5.9),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(5.2, 6.4, "N", fontsize=10, ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Weight mg (down)
        ax.annotate("", xy=(5, 2.0), xytext=(5, 2.9),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(5.2, 2.5, "mg", fontsize=10, ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Acceleration arrow (outside)
        if self.direction == "up":
            ax.annotate("", xy=(8.9, 7.8), xytext=(8.9, 6.3),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(9.1, 7.05, f"a = {self.a:.1f} m s⁻²", fontsize=10, ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.annotate("", xy=(8.9, 6.3), xytext=(8.9, 7.8),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(9.1, 7.05, f"a = {self.a:.1f} m s⁻²", fontsize=10, ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(2.2, 1.4, f"m = {self.m} kg", fontsize=10, ha="left", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy068:
    """
    Linear momentum conservation: perfectly inelastic collision (stick)
    1D collision: one trolley moves and hits the other trolley (initially stationary).
    After collision they stick together.
    Dynamic direction: Sometimes m1 moves right into m2, Sometimes m2 moves left into m1
    """

    def __init__(self):
        self.m1 = rnd.choice([0.50, 0.80, 1.00, 1.20, 1.50, 2.00])  # kg (left trolley)
        self.m2 = rnd.choice([0.50, 0.80, 1.00, 1.20, 1.50, 2.00])  # kg (right trolley)
        self.u = rnd.randint(2, 10)  # speed magnitude, m s^-1

        # Choose which trolley is moving (minimal diagram: only one arrow)
        # Sign convention: right is positive.
        self.moving = rnd.choice([1, 2])  # 1 => m1 moves right, 2 => m2 moves left

        if self.moving == 1:
            self.u1 = +self.u
            self.u2 = 0
            self.motion_text = f"trolley 1 (mass {self.m1:.2f} kg) moves to the right with speed {self.u} m s⁻¹"
        else:
            self.u1 = 0
            self.u2 = -self.u
            self.motion_text = f"trolley 2 (mass {self.m2:.2f} kg) moves to the left with speed {self.u} m s⁻¹"

        # Conservation of momentum: m1*u1 + m2*u2 = (m1+m2)*v
        self.v = (self.m1 * self.u1 + self.m2 * self.u2) / (self.m1 + self.m2)  # signed velocity
        self.speed = abs(self.v)  # asked for speed (magnitude)
        self.answer = sig_figs(self.speed, 3)

        self.description = (
            f"Two trolleys move on a smooth horizontal track. {self.motion_text} and collides with the other trolley, "
            "which is initially at rest. The trolleys stick together after the collision (see diagram).\n"
            "Determine the common speed immediately after the collision. (_) m s⁻¹"
        )

        self.topic = "Dynamics"
        self.subtopic = "Linear momentum and its conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of trolley 1, }} m_1 &= {self.m1:.2f}\\,\\text{{kg}}\\\\"
            f"\\text{{Mass of trolley 2, }} m_2 &= {self.m2:.2f}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial velocity of trolley 1, }} u_1 &= {self.u1}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Initial velocity of trolley 2, }} u_2 &= {self.u2}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{Using the Principle of Conservation of Momentum:}} &\\\\"
            "\\text{Total momentum before} &= \\text{Total momentum after}\\\\"
            "m_1 u_1 + m_2 u_2 &= (m_1 + m_2)v\\\\"
            "\\text{{Substitute the values into the equation:}} &\\\\"
            f"({self.m1:.2f} \\times {self.u1}) + ({self.m2:.2f} \\times {self.u2}) &= ({self.m1:.2f} + {self.m2:.2f})v\\\\"
            f"{round(self.m1 * self.u1, 10)} + {round(self.m2 * self.u2, 10)} &= {round(self.m1 + self.m2, 10)} \\times v\\\\"
            "\\text{{Solve for the common final velocity }} v: &\\\\"
            f"v &= \\frac{{{round(self.m1 * self.u1 + self.m2 * self.u2, 10)}}}{{{round(self.m1 + self.m2, 10)}}}\\\\"
            f"&= {round(self.v, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{The common speed is the magnitude of the velocity:}} &\\\\"
            f"\\text{{Speed}} &= |v| = {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Track
        ax.plot([0.5, 9.5], [0.9, 0.9], linewidth=2, color="black")

        # Two trolleys (minimal)
        t1 = patches.Rectangle((1.6, 0.9), 2.2, 1.2, fill=False, linewidth=2, edgecolor="black")
        t2 = patches.Rectangle((6.2, 0.9), 2.2, 1.2, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(t1)
        ax.add_patch(t2)

        ax.text(2.7, 2.3, f"m₁={self.m1:.2f} kg", fontsize=10, ha="center", va="bottom")
        ax.text(7.3, 2.3, f"m₂={self.m2:.2f} kg", fontsize=10, ha="center", va="bottom")

        if self.moving == 1:
            # m1 moves right
            ax.annotate("", xy=(4.2, 1.5), xytext=(3.4, 1.5),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(4.25, 1.5, f"u = {self.u} m s⁻¹", fontsize=10, ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            # m2 moves left
            ax.annotate("", xy=(5.8, 1.5), xytext=(6.6, 1.5),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(5.75, 1.5, f"u = {self.u} m s⁻¹", fontsize=10, ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy069:
    """
    Linear momentum conservation: explosion from rest (1D)
    """

    def __init__(self):
        while True:
            self.m_total = rnd.randint(3, 10)  # kg
            self.mA = rnd.randint(1, self.m_total - 1)
            self.mB = self.m_total - self.mA

            # Choose which fragment is the UNKNOWN
            self.target = rnd.choice(["A", "B"])

            # Given speed magnitude (always positive magnitude)
            given_speed = rnd.randint(3, 12)

            # Directions fixed for clarity: A to the right, B to the left
            if self.target == "B":
                # A is given, find B
                self.vA = +given_speed
                self.vB = -(self.mA / self.mB) * self.vA  # negative => left
                unknown_speed = abs(self.vB)
                if 2 <= unknown_speed <= 20:
                    break
            else:
                # B is given, find A
                self.vB = -given_speed
                self.vA = -(self.mB / self.mA) * self.vB  # vB is negative => vA positive
                unknown_speed = abs(self.vA)
                if 2 <= unknown_speed <= 20:
                    break

        # Final answers (speed + direction)
        if self.target == "B":
            self.answer = f"{sig_figs(abs(self.vB), 3)} m s⁻¹ to the left"
        else:
            self.answer = f"{sig_figs(abs(self.vA), 3)} m s⁻¹ to the right"

        # Description changes depending on target
        if self.target == "B":
            self.description = (
                f"An object of total mass {self.m_total} kg is initially at rest on a smooth horizontal surface. "
                "It explodes into two fragments A and B which move in opposite directions (see diagram).\n"
                f"Fragment A has mass {self.mA} kg and moves to the right with speed {self.vA} m s⁻¹.\n"
                f"Fragment B has mass {self.mB} kg. Determine the speed and direction of fragment B.\n"
                "Speed of B = (_) m s⁻¹, direction = (_)"
            )
        else:
            self.description = (
                f"An object of total mass {self.m_total} kg is initially at rest on a smooth horizontal surface. "
                "It explodes into two fragments A and B which move in opposite directions (see diagram).\n"
                f"Fragment B has mass {self.mB} kg and moves to the left with speed {abs(self.vB)} m s⁻¹.\n"
                f"Fragment A has mass {self.mA} kg. Determine the speed and direction of fragment A.\n"
                "Speed of A = (_) m s⁻¹, direction = (_)"
            )

        self.topic = "Dynamics"
        self.subtopic = "Linear momentum and its conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial total momentum, }} p_{{initial}} &= 0\\,\\text{{kg m s}}^{{-1}}\\\\"
            f"\\text{{Mass of fragment A, }} m_A &= {self.mA}\\,\\text{{kg}}\\\\"
            f"\\text{{Mass of fragment B, }} m_B &= {self.mB}\\,\\text{{kg}}\\\\"
            f"{'\\text{Given velocity of A, } v_A &= ' + str(self.vA) + '\\,\\text{m s}^{-1}' if self.target == 'B' else '\\text{Given velocity of B, } v_B &= ' + str(self.vB) + '\\,\\text{m s}^{-1}'}\\\\"
            "\\text{{Using the Principle of Conservation of Momentum:}} &\\\\"
            "p_{{initial}} &= p_{{final}}\\\\"
            "0 &= m_A v_A + m_B v_B\\\\"
            "\\text{{Rearranging for the unknown velocity:}} &\\\\"
            f"{'v_B &= -\\frac{m_A v_A}{m_B}' if self.target == 'B' else 'v_A &= -\\frac{m_B v_B}{m_A}'}\\\\"
            f"{'v_B' if self.target == 'B' else 'v_A'} &= -\\frac{{{self.mA if self.target == 'B' else self.mB} \\times {self.vA if self.target == 'B' else self.vB}}}{{{self.mB if self.target == 'B' else self.mA}}}\\\\"
            f"{'v_B' if self.target == 'B' else 'v_A'} &= {round(self.vB if self.target == 'B' else self.vA, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Surface line
        ax.plot([0.5, 9.5], [0.9, 0.9], linewidth=2, color="black")

        # Explosion point
        ax.add_patch(patches.Circle((5.0, 1.6), 0.18, fill=False, linewidth=2, edgecolor="black"))
        ax.text(5.0, 2.0, "explosion", fontsize=10, ha="center", va="bottom")

        # Right arrow = fragment A (to the right)
        ax.annotate("", xy=(8.7, 1.6), xytext=(5.2, 1.6),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Left arrow = fragment B (to the left)
        ax.annotate("", xy=(1.3, 1.6), xytext=(4.8, 1.6),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Labels depend on which is unknown (keep minimal: one side has value, other has v=?)
        if self.target == "B":
            # A known, B unknown
            ax.text(8.75, 1.6, f"A: {self.mA} kg, {self.vA} m s⁻¹", fontsize=10,
                    ha="left", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.25, 1.6, f"B: {self.mB} kg, v = ?", fontsize=10,
                    ha="right", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            # B known, A unknown
            ax.text(8.75, 1.6, f"A: {self.mA} kg, v = ?", fontsize=10,
                    ha="left", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.25, 1.6, f"B: {self.mB} kg, {abs(self.vB)} m s⁻¹", fontsize=10,
                    ha="right", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(5.0, 3.2, "initially at rest", fontsize=10, ha="center", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy070:
    """
    Linear momentum conservation: 2D collision (stick), find speed & direction
    Two trolleys moving at right angles collide and stick (2D).
    Use momentum conservation in x and y, then find resultant speed and angle.
    """

    def __init__(self):
        # Choose neat momentum ratios to give common exam angles (e.g. 3:4, 1:1, 1:2, 2:1, 4:3)
        ratios = [(3, 4), (4, 3), (1, 1), (1, 2), (2, 1)]
        while True:
            self.rx, self.ry = rnd.choice(ratios)
            self.k = rnd.randint(2, 10)

            # total momenta in x and y (kg m s^-1)
            self.px = self.rx * self.k
            self.py = self.ry * self.k

            # choose masses that divide px and py to keep speeds as integers
            mA_choices = [d for d in range(1, 6) if self.px % d == 0]
            mB_choices = [d for d in range(1, 6) if self.py % d == 0]
            if not mA_choices or not mB_choices:
                continue

            self.mA = rnd.choice(mA_choices)
            self.mB = rnd.choice(mB_choices)

            self.uA = self.px / self.mA  # east (+x)
            self.uB = self.py / self.mB  # north (+y)

            if 1 <= self.uA <= 12 and 1 <= self.uB <= 12:
                break

        self.M = self.mA + self.mB
        self.vx = self.px / self.M
        self.vy = self.py / self.M
        self.v = math.hypot(self.vx, self.vy)
        self.theta = math.degrees(math.atan2(self.vy, self.vx))  # degrees above +x

        self.answer = f"{sig_figs(self.v, 3)} m s⁻¹ at {round(self.theta, 1)}° above +x"

        self.description = (
            "Two trolleys move on a smooth horizontal surface and collide at a point, then stick together.\n"
            "Both Trolley A and B's masses, directions, and speeds are shown in the diagram."
            # f"Trolley A has mass {self.mA} kg and moves east with speed {self.uA:.0f} m s⁻¹.\n"
            # f"Trolley B has mass {self.mB} kg and moves north with speed {self.uB:.0f} m s⁻¹.\n"
            "Determine the speed of the combined trolley and its direction (angle above the +x axis).\n"
            "Speed = (_) m s⁻¹, angle = (_)°"
        )

        self.topic = "Dynamics"
        self.subtopic = "Linear momentum and its conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of trolley A, }} m_A &= {self.mA}\\,\\text{{kg}}\\\\"
            f"\\text{{Mass of trolley B, }} m_B &= {self.mB}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial velocity of A, }} u_A &= {self.uA:.0f}\\,\\text{{m s}}^{{-1}}\\text{{ (east)}}\\\\"
            f"\\text{{Initial velocity of B, }} u_B &= {self.uB:.0f}\\,\\text{{m s}}^{{-1}}\\text{{ (north)}}\\\\"
            "\\text{{Step 1: Conservation of momentum in the x-direction (east):}} &\\\\"
            "p_x &= m_A u_A + m_B(0) = (m_A + m_B) v_x\\\\"
            f"{self.px} &= {self.M} v_x\\\\"
            f"v_x &= \\frac{{{self.px}}}{{{self.M}}} = {round(self.vx, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{Step 2: Conservation of momentum in the y-direction (north):}} &\\\\"
            "p_y &= m_A(0) + m_B u_B = (m_A + m_B) v_y\\\\"
            f"{self.py} &= {self.M} v_y\\\\"
            f"v_y &= \\frac{{{self.py}}}{{{self.M}}} = {round(self.vy, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{Step 3: Calculate the resultant speed }} v: &\\\\"
            "v &= \\sqrt{v_x^2 + v_y^2}\\\\"
            f"&= \\sqrt{{{round(self.vx, 10)}^2 + {round(self.vy, 10)}^2}}\\\\"
            f"&= {round(self.v, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{Step 4: Calculate the angle }} \\theta \\text{{ above the +x axis:}} &\\\\"
            "\\theta &= \\tan^{-1}\\left(\\frac{v_y}{v_x}\\right)\\\\"
            f"&= \\tan^{-1}\\left(\\frac{{{round(self.vy, 10)}}}{{{round(self.vx, 10)}}}\\right)\\\\"
            f"&= {round(self.theta, 10)}^\\circ\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(5.5, 5.0))
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-0.5, 10)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Axes (x to right, y up)
        ax.annotate("", xy=(9.6, 0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(0, 9.6), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(9.7, -0.2, "+x (east)", fontsize=10, ha="right", va="top")
        ax.text(-0.2, 9.7, "+y (north)", fontsize=10, ha="right", va="top")

        # Collision point
        ax.plot(0, 0, "ko", markersize=5)
        ax.text(0.2, 0.2, "collision", fontsize=10, ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Incoming velocity arrows
        # A along +x
        ax.annotate("", xy=(4.5, 0), xytext=(0.3, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(4.6, 0.0, f"A: m={self.mA} kg, u={self.uA:.0f}", fontsize=10,
                ha="left", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # B along +y
        ax.annotate("", xy=(0, 4.5), xytext=(0, 0.3),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(0.0, 4.6, f"B: m={self.mB} kg, u={self.uB:.0f}", fontsize=10,
                ha="center", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Resultant velocity arrow after sticking (scaled for display)
        # Use direction based on vx, vy; scale to fit nicely on plot
        scale = 6.0 / max(1e-9, math.hypot(self.vx, self.vy))
        dx = self.vx * scale
        dy = self.vy * scale

        ax.annotate("", xy=(dx, dy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(dx * 0.55, dy * 0.55, "v", fontsize=10, ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(6.2, 8.8, "after: stick together", fontsize=10, ha="center", va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()
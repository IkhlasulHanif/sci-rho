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
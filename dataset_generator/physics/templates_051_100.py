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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
        self.question_type = "MCQ"

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
        self.question_type = "MCQ"

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
        self.question_type = "Short Answer"

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
        # ax.text(6.2, 8.2, "Vs = ?", ha="left", va="center", fontsize=11)

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
        self.question_type = "Short Answer"

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
        self.question_type = "MCQ"

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
        self.question_type = "Short Answer"

        self.description = (
            "An ammeter shows a current (A) flowing for some time (t) (values are shown in the image). "
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
        self.question_type = "Free-form"

        self.description = (
            "A trolley travels a measured distance and the time taken is recorded (the values are shown in the image).\n"
            "Calculate the speed v and the absolute uncertainty in v.\n"
            "The answer format: v = (_) ± (_) m s⁻¹"
        )
        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Measured distance, }} L &= {self.L:.2f} \\pm {self.dL:.3f}\\,\\text{{m}}\\\\"
            f"\\text{{Measured time, }} t &= {self.t:.1f} \\pm {self.dt:.2f}\\,\\text{{s}}\\\\"
            f"\\text{{The speed }} v \\text{{ is calculated using:}} &\\\\"
            f"v &= \\frac{{L}}{{t}}\\\\"
            f"&= \\frac{{{self.L:.2f}}}{{{self.t:.1f}}}\\\\"
            f"&= {self.v:.4f}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{For a quotient, fractional uncertainties are added:}} &\\\\"
            f"\\frac{{\\Delta v}}{{v}} &= \\frac{{\\Delta L}}{{L}} + \\frac{{\\Delta t}}{{t}}\\\\"
            f"&= \\frac{{{self.dL:.3f}}}{{{self.L:.2f}}} + \\frac{{{self.dt:.2f}}}{{{self.t:.1f}}}\\\\"
            f"&= {self.frac_unc:.6f}\\\\"
            f"\\text{{Calculate absolute uncertainty }} \\Delta v: &\\\\"
            f"\\Delta v &= v \\times \\left( \\frac{{\\Delta v}}{{v}} \\right)\\\\"
            f"&= {self.v:.4f} \\times {self.frac_unc:.6f}\\\\"
            f"&= {self.dv:.4f}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
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
        self.question_type = "Short Answer"

        self.description = (
            "Two forces (F₁ and F₂) act at a point as shown in the image.\n"
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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
            "A ball is dropped from rest from a height of h as shown in the image. "
            "Neglect air resistance. Take g = 9.81 m s⁻². "
            "Calculate the speed just before it hits the ground. (_) m s⁻¹"
        )
        self.topic = "Kinematics"
        self.subtopic = "Equations of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
            "Two blocks are connected by a light inextensible string on a smooth horizontal surface."
            "A horizontal force is applied to the right-hand block as shown.\n"
            "The applied force and both block masses are shown in the image.\n"
            "Determine the tension in the string. (_) N"
        )

        self.topic = "Dynamics"
        self.subtopic = "Momentum and Newton’s laws of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
            self.dir_text = "upwards"
        else:
            self.N = self.m * (self.g - self.a)
            self.dir_text = "downwards"

        self.answer = sig_figs(self.N, 3)

        self.description = (
            f"A person stands on a scale in a lift. "
            f"The lift accelerates {self.dir_text} (both m and a are shown in the image). "
            "Take g = 9.81 m s⁻².\n"
            "Determine the reading of the scale (the normal reaction). (_) N"
        )

        self.topic = "Dynamics"
        self.subtopic = "Momentum and Newton’s laws of motion"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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

        self.description = (
            f"An object of total mass {self.m_total} kg is initially at rest on a smooth horizontal surface. "
            "It explodes into two fragments A and B which move in opposite directions (see diagram).\n"
            "The fragment masses and the known speed are shown in the diagram.\n"
            "Determine the speed and direction of the other fragment.\n"
            "Answer format: (_) m s⁻¹ to the (left/right)"
        )

        self.topic = "Dynamics"
        self.subtopic = "Linear momentum and its conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Free-form"

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
            ax.text(1.25, 1.6, f"B: {self.mB} kg", fontsize=10,
                    ha="right", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            # B known, A unknown
            ax.text(8.75, 1.6, f"A: {self.mA} kg", fontsize=10,
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

        self.answer = f"{sig_figs(self.v, 3)} m s⁻¹ at {round(self.theta, 1)}°"

        self.description = (
            "Two trolleys move on a smooth horizontal surface and collide at a point, then stick together.\n"
            "Both Trolley A and B's masses, directions, and speeds are shown in the diagram."
            "Determine the speed of the combined trolley and its direction (angle above the +x axis).\n"
            "Speed = (_) m s⁻¹, angle = (_)°. Answer format: (_) m s⁻¹ at (_)°"
        )

        self.topic = "Dynamics"
        self.subtopic = "Linear momentum and its conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Free-form"

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


class Phy071:
    """
    Turning effects of forces (moment of a force).
    Beam pivoted at P with a downward force W and an upward force F as shown.
    Find F for equilibrium (principle of moments).
    """

    def __init__(self):
        self.orientation = rnd.choice(["left", "right"])  # Randomly mirror the diagram
        self.W = rnd.choice([10, 12, 14, 16, 18, 20, 24, 30, 36, 40])  # N
        self.d2 = rnd.choice([0.60, 0.80, 1.00, 1.20, 1.40])          # m (pivot to F)
        d1_choices = [0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
        self.d1 = rnd.choice([d for d in d1_choices if d < self.d2])  # m (pivot to W)

        # Calculate required force
        self.F = self.W * self.d1 / self.d2
        self.answer = float(f"{self.F:.3g}")

        self.description = (
            "A light horizontal beam is pivoted at P. The forces and distances are shown in the diagram.\n"
            "Determine the magnitude of the force F required to keep the beam in equilibrium.\n"
            "F = (_) N"
        )
        self.topic = "Forces, density and pressure"
        self.subtopic = "Turning effects of forces"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Weight (downward force), }} W &= {self.W}\\,\\text{{N}}\\\\"
            f"\\text{{Distance from pivot to }} W, d_1 &= {self.d1:.2f}\\,\\text{{m}}\\\\"
            f"\\text{{Distance from pivot to }} F, d_2 &= {self.d2:.2f}\\,\\text{{m}}\\\\"
            "\\text{{For the beam to be in equilibrium, the total moment about pivot P must be zero.}} &\\\\"
            "\\text{{Sum of clockwise moments}} &= \\text{{Sum of anticlockwise moments}}\\\\"
            "\\text{{Assuming the configuration in the diagram:}} &\\\\"
            "W \\times d_1 &= F \\times d_2\\\\"
            "\\text{{Substitute the known values:}} &\\\\"
            f"{self.W} \\times {self.d1:.2f} &= F \\times {self.d2:.2f}\\\\"
            f"{round(self.W * self.d1, 10)} &= F \\times {self.d2:.2f}\\\\"
            "\\text{{Rearrange to solve for }} F: &\\\\"
            f"F &= \\frac{{{round(self.W * self.d1, 10)}}}{{{self.d2:.2f}}}\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Geometry
        y_beam = 2.4
        x_left_end = 1.4
        x_right_end = 9.2

        # Choose pivot/endpoints based on orientation
        if self.orientation == "left":
            xP = x_left_end
            xEnd = x_right_end
        else:
            xP = x_right_end
            xEnd = x_left_end

        # Beam
        ax.plot([x_left_end, x_right_end], [y_beam, y_beam], linewidth=3, color="black")

        # Pivot triangle
        tri = patches.Polygon([[xP, y_beam], [xP - 0.5, y_beam - 0.9], [xP + 0.5, y_beam - 0.9]],
                              closed=True, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(tri)
        ax.text(xP, y_beam - 1.15, "P", ha="center", va="top")

        # Position mapping along beam
        L_pix = abs(xEnd - xP)
        direction = 1 if xEnd > xP else -1

        # Force positions: F at far end, W somewhere between
        xF = xEnd
        xW = xP + direction * L_pix * (self.d1 / self.d2)

        # Downward force W
        ax.annotate("", xy=(xW, y_beam - 0.1), xytext=(xW, y_beam + 1.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(xW, y_beam + 1.25, f"W = {self.W} N", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Upward force F (unknown)
        ax.annotate("", xy=(xF, y_beam + 1.1), xytext=(xF, y_beam - 0.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(xF, y_beam + 1.25, "F", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Distance d1 (pivot to W)
        y1 = 1.4
        ax.annotate("", xy=(xP, y1), xytext=(xW, y1),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((xP + xW) / 2, y1 - 0.15, f"d₁ = {self.d1:.2f} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Distance d2 (pivot to F)
        y2 = 0.9
        ax.annotate("", xy=(xP, y2), xytext=(xF, y2),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((xP + xF) / 2, y2 - 0.15, f"d₂ = {self.d2:.2f} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy072:
    """
    Turning effects of forces (couple and torque).
    Dynamic target: sometimes find torque, sometimes force, sometimes separation.
    """

    def __init__(self):
        self.target = rnd.choice(["tau", "F", "d"])  # what to find

        self.F = rnd.choice([10, 15, 20, 25, 30, 40, 50, 60])  # N (magnitude of each force)
        self.d = rnd.choice([0.10, 0.12, 0.15, 0.18, 0.20, 0.25, 0.30, 0.35])  # m
        self.tau = self.F * self.d  # N m

        if self.target == "tau":
            self.answer = float(f"{self.tau:.3g}")
            self.unknown_label = "τ = ?"
        elif self.target == "F":
            self.answer = float(f"{self.F:.3g}")
            self.unknown_label = "F = ?"
        else:
            self.answer = float(f"{self.d:.3g}")
            self.unknown_label = "d = ?"

        self.description = (
            "Two equal and opposite forces form a couple as shown. All required values are shown in the diagram.\n"
            "Determine the missing quantity indicated by ?.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Forces, density and pressure"
        self.subtopic = "Turning effects of forces"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Magnitude of each force, }} F &= {self.F if self.target != 'F' else '\\text{?}'}\\,\\text{{N}}\\\\"
            f"\\text{{Perpendicular separation, }} d &= {self.d if self.target != 'd' else '\\text{?}'}\\,\\text{{m}}\\\\"
            f"\\text{{Torque of the couple, }} \\tau &= {self.tau if self.target != 'tau' else '\\text{?}'}\\,\\text{{N m}}\\\\"
            "\\text{{The torque of a couple is given by:}} &\\\\"
            "\\tau &= F \\times d\\\\"
            "\\text{{Substituting the known values:}} &\\\\"
            f"{'\\tau' if self.target == 'tau' else str(float(f'{self.tau:.3g}'))} &= "
            f"{self.F if self.target != 'F' else 'F'} \\times {self.d if self.target != 'd' else 'd'}\\\\"
            "\\text{{Solving for the unknown variable:}} &\\\\"
            + (f"\\tau &= {self.F} \\times {self.d}\\\\" if self.target == "tau" else "")
            + (f"F &= \\frac{{{float(f'{self.tau:.3g}')}}}{{{self.d}}}\\\\" if self.target == "F" else "")
            + (f"d &= \\frac{{{float(f'{self.tau:.3g}')}}}{{{self.F}}}\\\\" if self.target == "d" else "")
            + f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{{ 'N m' if self.target == 'tau' else ('N' if self.target == 'F' else 'm') }}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.2, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Bar
        y_bar = 2.0
        xL, xR = 3.0, 7.0
        ax.plot([xL, xR], [y_bar, y_bar], linewidth=3, color="black")

        # Forces (up on left, down on right)
        ax.annotate("", xy=(xL, y_bar + 1.2), xytext=(xL, y_bar + 0.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(xR, y_bar - 1.2), xytext=(xR, y_bar - 0.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Decide what values to show
        show_F = (self.target != "F")
        show_d = (self.target != "d")
        show_tau = (self.target != "tau")

        # Labels for forces
        if show_F:
            ax.text(xL, y_bar + 1.35, f"F = {self.F} N", ha="center", va="bottom",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(xR, y_bar - 1.35, f"F = {self.F} N", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(xL, y_bar + 1.35, "F = ?", ha="center", va="bottom",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(xR, y_bar - 1.35, "F = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Separation d (horizontal)
        y_d = 0.9
        ax.annotate("", xy=(xL, y_d), xytext=(xR, y_d),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        if show_d:
            ax.text((xL + xR) / 2, y_d - 0.15, f"d = {self.d:.2f} m", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text((xL + xR) / 2, y_d - 0.15, "d = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Torque text (top right)
        if show_tau:
            ax.text(9.6, 3.6, f"τ = {float(f'{self.tau:.3g}')} N m", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(9.6, 3.6, "τ = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy073:
    """
    Equilibrium of forces (three coplanar forces in equilibrium at a point).
    Ring with two tensions at angles and a weight downward.
    Dynamic target: find T1 or T2.
    """

    def __init__(self):
        self.g = 9.81
        self.m = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])
        self.W = self.m * self.g

        angles = [25, 30, 35, 40, 45, 50, 55, 60]
        while True:
            self.theta1 = rnd.choice(angles)  # left string angle above horizontal
            self.theta2 = rnd.choice(angles)  # right string angle above horizontal
            # Avoid extreme imbalance
            if abs(self.theta1 - self.theta2) <= 25:
                break

        th1 = math.radians(self.theta1)
        th2 = math.radians(self.theta2)

        # Solve tensions from equilibrium:
        # T1 cosθ1 = T2 cosθ2
        # T1 sinθ1 + T2 sinθ2 = W
        denom = (math.sin(th1) + math.cos(th1) * math.tan(th2))
        self.T1 = self.W / denom
        self.T2 = self.T1 * math.cos(th1) / math.cos(th2)

        self.target = rnd.choice(["T1", "T2"])
        if self.target == "T1":
            self.answer = float(f"{self.T1:.3g}")
        else:
            self.answer = float(f"{self.T2:.3g}")

        self.description = (
            "A small ring is in equilibrium under three coplanar forces as shown. The mass and angles are shown in the diagram.\n"
            "Take g = 9.81 m s⁻². Determine the missing tension.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Forces, density and pressure"
        self.subtopic = "Equilibrium of forces"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m:.1f}\\,\\text{{kg}}\\\\"
            f"\\text{{Weight, }} W &= m \\times g = {self.m:.1f} \\times 9.81 = {round(self.W, 10)}\\,\\text{{N}}\\\\"
            f"\\text{{Angle 1, }} \\theta_1 &= {self.theta1}^\\circ\\\\"
            f"\\text{{Angle 2, }} \\theta_2 &= {self.theta2}^\\circ\\\\"
            "\\text{{For equilibrium, the sum of horizontal components must be zero:}} &\\\\"
            "T_1 \\cos(\\theta_1) &= T_2 \\cos(\\theta_2) \\implies T_2 = T_1 \\frac{\\cos(\\theta_1)}{\\cos(\\theta_2)}\\\\"
            "\\text{{The sum of vertical components must equal the weight:}} &\\\\"
            "T_1 \\sin(\\theta_1) + T_2 \\sin(\\theta_2) &= W\\\\"
            "\\text{{Substituting }} T_2 \\text{{ into the vertical equation:}} &\\\\"
            "T_1 \\sin(\\theta_1) + \\left( T_1 \\frac{\\cos(\\theta_1)}{\\cos(\\theta_2)} \\right) \\sin(\\theta_2) &= W\\\\"
            "T_1 \\left[ \\sin(\\theta_1) + \\cos(\\theta_1) \\tan(\\theta_2) \\right] &= W\\\\"
            "\\text{{Solving for }} T_1: &\\\\"
            f"T_1 &= \\frac{{{round(self.W, 10)}}}{{\\sin({self.theta1}^\\circ) + \\cos({self.theta1}^\\circ) \\tan({self.theta2}^\\circ)}}\\\\"
            f"T_1 &= {round(self.T1, 10)}\\,\\text{{N}}\\\\"
            + (f"\\text{{Solving for }} T_2: &\\\\"
            f"T_2 &= {round(self.T1, 10)} \\times \\frac{{\\cos({self.theta1}^\\circ)}}{{\\cos({self.theta2}^\\circ)}}\\\\"
            f"T_2 &= {round(self.T2, 10)}\\,\\text{{N}}\\\\" if self.target == "T2" else "")
            + f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.2, 4.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Ring (node)
        x0, y0 = 5.0, 3.2
        ax.add_patch(patches.Circle((x0, y0), 0.10, fill=True, color="black"))

        # Reference horizontal line (subtle)
        ax.plot([3.5, 6.5], [y0, y0], linewidth=1.5, color="black")

        # String directions
        L = 3.2
        th1 = math.radians(180 - self.theta1)  # up-left
        th2 = math.radians(self.theta2)        # up-right

        x1, y1 = x0 + L * math.cos(th1), y0 + L * math.sin(th1)
        x2, y2 = x0 + L * math.cos(th2), y0 + L * math.sin(th2)

        # Tension arrows (from ring along strings)
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(x2, y2), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        ax.text((x0 + x1)/2 - 0.2, (y0 + y1)/2 + 0.1, "T₁", ha="right", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text((x0 + x2)/2 + 0.2, (y0 + y2)/2 + 0.1, "T₂", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Weight arrow
        ax.annotate("", xy=(x0, 1.0), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(x0 + 0.25, (y0 + 1.0)/2, "W", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Mass label (shown in diagram)
        ax.text(5.0, 0.55, f"m = {self.m:.1f} kg", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        # Angle labels (shown in diagram)
        ax.text(3.35, y0 + 0.35, f"θ₁ = {self.theta1}°", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(6.65, y0 + 0.35, f"θ₂ = {self.theta2}°", ha="right", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy074:
    """
    Equilibrium of forces (no resultant force and no resultant torque).
    Simply-supported uniform beam with loads; find reaction at A or B (dynamic target).
    """

    def __init__(self):
        self.L = rnd.choice([2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])  # m
        x_choices = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
        self.x = rnd.choice([v for v in x_choices if v < self.L])  # m from A

        self.W_load = rnd.choice([100, 120, 140, 160, 180, 200, 240, 300, 360])  # N
        self.W_beam = rnd.choice([50, 80, 100, 120, 150, 180, 200])              # N

        # Equilibrium:
        # Taking moments about A: RB*L = W_load*x + W_beam*(L/2)
        self.RB = (self.W_load * self.x + self.W_beam * (self.L / 2)) / self.L
        self.RA = self.W_load + self.W_beam - self.RB

        self.target = rnd.choice(["RA", "RB"])
        if self.target == "RA":
            self.answer = float(f"{self.RA:.3g}")
        else:
            self.answer = float(f"{self.RB:.3g}")

        self.description = (
            "A uniform beam is in equilibrium supported at A and B. The loads and distances are shown in the diagram.\n"
            "Determine the missing vertical reaction.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Forces, density and pressure"
        self.subtopic = "Equilibrium of forces"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length of the beam, }} L &= {self.L:.1f}\\,\\text{{m}}\\\\"
            f"\\text{{Weight of the beam (at center), }} W_{{beam}} &= {self.W_beam}\\,\\text{{N}}\\\\"
            f"\\text{{Load weight, }} W_{{load}} &= {self.W_load}\\,\\text{{N}}\\\\"
            f"\\text{{Distance of load from A, }} x &= {self.x:.1f}\\,\\text{{m}}\\\\"
            "\\text{{For equilibrium, the sum of clockwise moments about A equals the sum of anticlockwise moments about A.}} &\\\\"
            "\\sum M_A &= 0\\\\"
            "R_B \\times L &= W_{{load}} \\times x + W_{{beam}} \\times \\left(\\frac{L}{2}\\right)\\\\"
            f"R_B \\times {self.L:.1f} &= {self.W_load} \\times {self.x:.1f} + {self.W_beam} \\times {self.L / 2:.2f}\\\\"
            f"R_B \\times {self.L:.1f} &= {round(self.W_load * self.x, 10)} + {round(self.W_beam * (self.L / 2), 10)}\\\\"
            f"R_B \\times {self.L:.1f} &= {round(self.W_load * self.x + self.W_beam * (self.L / 2), 10)}\\\\"
            f"R_B &= \\frac{{{round(self.W_load * self.x + self.W_beam * (self.L / 2), 10)}}}{{{self.L:.1f}}}\\\\"
            f"R_B &= {round(self.RB, 10)}\\,\\text{{N}}\\\\"
            "\\text{{Using the vertical equilibrium condition:}} &\\\\"
            "R_A + R_B &= W_{{load}} + W_{{beam}}\\\\"
            f"R_A &= {self.W_load} + {self.W_beam} - {round(self.RB, 10)}\\\\"
            f"R_A &= {round(self.RA, 10)}\\,\\text{{N}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(7.0, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Beam geometry
        xA, xB = 1.2, 9.2
        y_beam = 3.2
        ax.plot([xA, xB], [y_beam, y_beam], linewidth=3, color="black")

        # Supports (triangles)
        triA = patches.Polygon([[xA, y_beam], [xA - 0.5, y_beam - 1.0], [xA + 0.5, y_beam - 1.0]],
                               closed=True, fill=False, linewidth=2, edgecolor="black")
        triB = patches.Polygon([[xB, y_beam], [xB - 0.5, y_beam - 1.0], [xB + 0.5, y_beam - 1.0]],
                               closed=True, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(triA)
        ax.add_patch(triB)
        ax.text(xA, y_beam - 1.25, "A", ha="center", va="top")
        ax.text(xB, y_beam - 1.25, "B", ha="center", va="top")

        # Reaction arrows (shown as labels; values not shown)
        ax.annotate("", xy=(xA, y_beam + 0.9), xytext=(xA, y_beam),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(xB, y_beam + 0.9), xytext=(xB, y_beam),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(xA + 0.15, y_beam + 0.6, "R_A", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(xB - 0.15, y_beam + 0.6, "R_B", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Position mapping for load x
        beam_pix = xB - xA
        x_load = xA + beam_pix * (self.x / self.L)

        # Point load
        ax.annotate("", xy=(x_load, y_beam - 0.1), xytext=(x_load, y_beam + 1.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(x_load, y_beam + 1.25, f"W = {self.W_load} N", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Beam weight at centre
        x_c = (xA + xB) / 2
        ax.annotate("", xy=(x_c, y_beam - 0.1), xytext=(x_c, y_beam + 0.9),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(x_c, y_beam + 1.05, f"W_beam = {self.W_beam} N", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Distance labels (shown)
        y_d1 = 1.5
        ax.annotate("", xy=(xA, y_d1), xytext=(x_load, y_d1),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((xA + x_load) / 2, y_d1 - 0.15, f"x = {self.x:.1f} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        y_d2 = 1.1
        ax.annotate("", xy=(xA, y_d2), xytext=(xB, y_d2),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((xA + xB) / 2, y_d2 - 0.15, f"L = {self.L:.1f} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy075:
    """
    Density and pressure (hydrostatic pressure).
    Dynamic target: find pressure difference OR find vertical separation.
    Uses Δp = ρ g Δh.
    """

    def __init__(self):
        self.g = 9.81
        self.rho = rnd.choice([800, 900, 1000, 1100, 1200, 1300])  # kg m^-3
        self.dh = rnd.choice([0.40, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00])  # m
        self.dp = self.rho * self.g * self.dh  # Pa

        self.target = rnd.choice(["dp", "dh"])

        if self.target == "dp":
            self.answer = float(f"{(self.dp/1000):.3g}")  # kPa
        else:
            self.answer = float(f"{self.dh:.3g}")  # m

        self.description = (
            "Two points A and B are in a liquid. All required values are shown in the diagram.\n"
            "Take g = 9.81 m s⁻². Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Forces, density and pressure"
        self.subtopic = "Density and pressure"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Density of liquid, }} \\rho &= {self.rho}\\,\\text{{kg m}}^{{-3}}\\\\"
            f"\\text{{Acceleration of free fall, }} g &= 9.81\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Vertical separation, }} \\Delta h &= {self.dh if self.target == 'dp' else '\\text{?}'}\\,\\text{{m}}\\\\"
            f"\\text{{Pressure difference, }} \\Delta p &= {f'{self.dp/1000:.3g}' if self.target == 'dh' else '\\text{?}'}\\,\\text{{kPa}}\\\\"
            "\\text{{The hydrostatic pressure difference is given by:}} &\\\\"
            "\\Delta p &= \\rho g \\Delta h\\\\"
            "\\text{{Substituting the known values:}} &\\\\"
            + (f"\\Delta p &= {self.rho} \\times 9.81 \\times {self.dh}\\\\" if self.target == "dp" else 
            f"{self.dp/1000:.3g} \\times 10^3 &= {self.rho} \\times 9.81 \\times \\Delta h\\\\")
            + "\\text{{Solving for the unknown variable:}} &\\\\"
            + (f"\\Delta p &= {round(self.dp, 10)}\\,\\text{{Pa}}\\\\" if self.target == "dp" else "")
            + (f"\\Delta p &= {round(self.dp/1000, 10)}\\,\\text{{kPa}}\\\\" if self.target == "dp" else "")
            + (f"\\Delta h &= \\frac{{{self.dp/1000:.3g} \\times 10^3}}{{{self.rho} \\times 9.81}}\\\\" if self.target == "dh" else "")
            + (f"\\Delta h &= {round(self.dh, 10)}\\,\\text{{m}}\\\\" if self.target == "dh" else "")
            + f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{{ 'kPa' if self.target == 'dp' else 'm' }}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(5.8, 4.4))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Container
        xL, xR = 3.0, 7.0
        yB, yT = 1.0, 6.0
        ax.add_patch(patches.Rectangle((xL, yB), xR - xL, yT - yB, fill=False, linewidth=2, edgecolor="black"))

        # Liquid fill (simple)
        y_surface = 5.4
        ax.add_patch(patches.Rectangle((xL + 0.05, yB + 0.05), (xR - xL) - 0.10, (y_surface - yB) - 0.05,
                                       fill=True, linewidth=0, facecolor="#dbefff"))

        ax.plot([xL, xR], [y_surface, y_surface], linewidth=2, color="black")
        ax.text((xL + xR) / 2, y_surface + 0.25, f"ρ = {self.rho} kg m⁻³", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Points A (higher) and B (lower)
        xP = 5.0
        yA = 4.4
        yBpt = yA - 1.4  # base separation visually
        # Use diagram separation label rather than exact scaling; A and B are shown with a bracket value.
        ax.plot(xP, yA, "ko", markersize=4)
        ax.plot(xP, yBpt, "ko", markersize=4)
        ax.text(xP + 0.25, yA, "A", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(xP + 0.25, yBpt, "B", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Bracket between A and B (Δh)
        x_br = 6.4
        ax.annotate("", xy=(x_br, yA), xytext=(x_br, yBpt),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        if self.target == "dp":
            ax.text(x_br + 0.25, (yA + yBpt) / 2, f"Δh = {self.dh:.2f} m", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(9.6, 6.6, "Δp = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(x_br + 0.25, (yA + yBpt) / 2, "Δh = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(9.6, 6.6, f"p_B − p_A = {float(f'{(self.dp/1000):.3g}')} kPa", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(9.6, 0.5, "g = 9.81 m s⁻²", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy076:
    """
    Density and pressure (upthrust / Archimedes' principle).
    Block fully submerged and held by a string.
    Dynamic target: find upthrust OR find tension.
    Uses U = ρ g V and (equilibrium) T + U = mg.
    """

    def __init__(self):
        self.g = 9.81
        self.rho = rnd.choice([800, 900, 1000, 1100, 1200])  # kg m^-3
        self.s_cm = rnd.randint(5, 12)  # cube side in cm (shown)
        self.V = (self.s_cm / 100) ** 3  # m^3

        # Choose a mass that ensures tension positive (object heavier than displaced fluid)
        while True:
            self.m = rnd.choice([0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0])
            self.U = self.rho * self.g * self.V
            self.W = self.m * self.g
            self.T = self.W - self.U
            if self.T > 0.8:  # avoid tiny tension
                break

        self.target = rnd.choice(["T", "U"])

        if self.target == "T":
            self.answer = float(f"{self.T:.3g}")
        else:
            self.answer = float(f"{self.U:.3g}")

        self.description = (
            "A cube is fully submerged in a liquid and held at rest by a light string as shown. The relevant values are shown in the diagram.\n"
            "Take g = 9.81 m s⁻². Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Forces, density and pressure"
        self.subtopic = "Density and pressure"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Side of the cube, }} s &= {self.s_cm}\\,\\text{{cm}} = {self.s_cm / 100:.2f}\\,\\text{{m}}\\\\"
            f"\\text{{Volume of the cube, }} V &= s^3 = ({self.s_cm / 100:.2f})^3 = {round(self.V, 10)}\\,\\text{{m}}^3\\\\"
            f"\\text{{Density of liquid, }} \\rho &= {self.rho}\\,\\text{{kg m}}^{{-3}}\\\\"
            f"\\text{{Mass of the cube, }} m &= {self.m:.1f}\\,\\text{{kg}}\\\\"
            "\\text{{Step 1: Calculate the upthrust (}} U \\text{{) using Archimedes' principle:}} &\\\\"
            "U &= \\rho g V\\\\"
            f"&= {self.rho} \\times 9.81 \\times {round(self.V, 10)}\\\\"
            f"&= {round(self.U, 10)}\\,\\text{{N}}\\\\"
            "\\text{{Step 2: Calculate the weight (}} W \\text{{) of the cube:}} &\\\\"
            "W &= mg\\\\"
            f"&= {self.m:.1f} \\times 9.81\\\\"
            f"&= {round(self.W, 10)}\\,\\text{{N}}\\\\"
            "\\text{{Step 3: Apply the equilibrium condition (}} \\sum F_y = 0 \\text{{):}} &\\\\"
            "\\text{{The upward forces (}} T + U \\text{{) must equal the downward force (}} W \\text{{):}} &\\\\"
            "T + U &= W\\\\"
            "\\text{{Solving for the unknown variable:}} &\\\\"
            + (f"T &= W - U\\\\" if self.target == "T" else "")
            + (f"T &= {round(self.W, 10)} - {round(self.U, 10)}\\\\" if self.target == "T" else "")
            + (f"T &= {round(self.T, 10)}\\,\\text{{N}}\\\\" if self.target == "T" else "")
            + f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.0, 4.4))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Container
        xL, xR = 3.0, 7.2
        yB, yT = 1.0, 6.2
        ax.add_patch(patches.Rectangle((xL, yB), xR - xL, yT - yB, fill=False, linewidth=2, edgecolor="black"))

        # Liquid fill
        y_surface = 5.5
        ax.add_patch(patches.Rectangle((xL + 0.05, yB + 0.05), (xR - xL) - 0.10, (y_surface - yB) - 0.05,
                                       fill=True, linewidth=0, facecolor="#dbefff"))
        ax.plot([xL, xR], [y_surface, y_surface], linewidth=2, color="black")
        ax.text((xL + xR) / 2, y_surface + 0.25, f"ρ = {self.rho} kg m⁻³", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Cube (submerged)
        cube_w = 1.2
        cx, cy = 5.1, 3.1
        ax.add_patch(patches.Rectangle((cx - cube_w/2, cy - cube_w/2), cube_w, cube_w,
                                       fill=False, linewidth=2, edgecolor="black"))

        # String
        ax.plot([cx, cx], [y_surface, cy + cube_w/2], linewidth=2, color="black")

        # Labels shown in diagram (values)
        ax.text(9.5, 5.9, f"m = {self.m:.1f} kg", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(9.5, 5.3, f"side = {self.s_cm} cm", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Forces on cube (minimal but readable)
        # Upthrust arrow (up)
        ax.annotate("", xy=(cx + 1.6, cy + 0.9), xytext=(cx + 1.6, cy - 0.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(cx + 1.85, cy + 0.4, "U", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Weight arrow (down)
        ax.annotate("", xy=(cx + 2.4, cy - 0.9), xytext=(cx + 2.4, cy + 0.1),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(cx + 2.65, cy - 0.4, "W", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Tension label near string (unknown or just T)
        if self.target == "T":
            ax.text(cx - 0.4, (y_surface + cy)/2, "T = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(cx - 0.4, (y_surface + cy)/2, "T", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Upthrust unknown or given? Keep minimal: show unknown label if target is U
        if self.target == "U":
            ax.text(9.2, 6.6, "Upthrust U = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(9.2, 0.6, "g = 9.81 m s⁻²", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy077:
    """
    Energy conservation (work done -> change in kinetic energy).
    Block pulled on a rough horizontal surface: work input - work against friction = gain in KE.
    """

    def __init__(self):
        while True:
            self.m = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0])  # kg
            self.s = rnd.choice([1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])  # m
            self.F = rnd.choice([20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100])  # N
            self.f = rnd.choice([5, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50])  # N

            if self.F <= self.f:
                continue

            self.work_net = (self.F - self.f) * self.s
            self.v = math.sqrt(2 * self.work_net / self.m)

            if 1.0 <= self.v <= 25.0:
                break

        self.answer = sig_figs(self.v, 3)

        self.description = (
            "A block moves on a rough horizontal surface. The mass (m), applied force (F), friction force (f) and distance moved (s) "
            "are shown in the diagram. The block starts from rest.\n"
            "Determine the speed of the block after moving the distance shown.\n"
            "v = (_) m s⁻¹"
        )
        self.topic = "Work, energy and power"
        self.subtopic = "Energy conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m:.1f}\\,\\text{{kg}}\\\\"
            f"\\text{{Applied force, }} F &= {self.F}\\,\\text{{N}}\\\\"
            f"\\text{{Friction force, }} f &= {self.f}\\,\\text{{N}}\\\\"
            f"\\text{{Distance moved, }} s &= {self.s:.1f}\\,\\text{{m}}\\\\"
            "\\text{{Step 1: Calculate the resultant (net) force acting on the block:}} &\\\\"
            "F_{net} &= F - f\\\\"
            f"&= {self.F} - {self.f}\\\\"
            f"&= {self.F - self.f}\\,\\text{{N}}\\\\"
            "\\text{{Step 2: Calculate the net work done on the block:}} &\\\\"
            "W_{net} &= F_{net} \\times s\\\\"
            f"&= {self.F - self.f} \\times {self.s:.1f}\\\\"
            f"&= {round(self.work_net, 10)}\\,\\text{{J}}\\\\"
            "\\text{{Step 3: Use the work-energy theorem (Work done = Change in Kinetic Energy):}} &\\\\"
            "W_{net} &= \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2\\\\"
            "\\text{{Since the block starts from rest (}} u = 0 \\text{{):}} &\\\\"
            f"{round(self.work_net, 10)} &= \\frac{1}{2} \\times {self.m:.1f} \\times v^2\\\\"
            "\\text{{Step 4: Solve for the final speed }} v: &\\\\"
            "v^2 &= \\frac{2 \\times W_{net}}{m}\\\\"
            f"v^2 &= \\frac{{2 \\times {round(self.work_net, 10)}}}{{{self.m:.1f}}}\\\\"
            f"v^2 &= {round(2 * self.work_net / self.m, 10)}\\\\"
            f"v &= \\sqrt{{{round(2 * self.work_net / self.m, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.2, 3.1))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Ground line
        y_ground = 1.0
        ax.plot([0.6, 9.4], [y_ground, y_ground], linewidth=2, color="black")

        # Block
        bx, by = 2.2, y_ground
        bw, bh = 2.0, 1.2
        ax.add_patch(patches.Rectangle((bx, by), bw, bh, fill=False, linewidth=2, edgecolor="black"))
        ax.text(bx + bw/2, by + bh + 0.25, f"m = {self.m:.1f} kg", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Applied force arrow (right)
        yF = by + 0.75*bh
        ax.annotate("", xy=(bx + bw + 1.2, yF), xytext=(bx + bw, yF),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(bx + bw + 1.25, yF, f"F = {self.F} N", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Friction arrow (left)
        yf = by + 0.35*bh
        ax.annotate("", xy=(bx - 1.2, yf), xytext=(bx, yf),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(bx - 1.25, yf, f"f = {self.f} N", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Distance moved bracket
        x_start = bx + 0.2
        x_end = x_start + 5.8
        y_s = 0.35
        ax.annotate("", xy=(x_start, y_s), xytext=(x_end, y_s),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((x_start + x_end)/2, y_s - 0.15, f"s = {self.s:.1f} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Start from rest and unknown final speed (VLM reads)
        ax.text(bx + 0.15, by + bh/2, "u = 0", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        # ax.text(8.7, 2.7, "v = ?", ha="center", va="center",
        #         bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy078:
    """
    Energy conservation with efficiency (useful energy out / total energy in).
    Motor lifts a load through a height.
    Dynamic target: find efficiency OR time OR input power.
    """

    def __init__(self):
        self.g = 9.81
        self.target = rnd.choice(["eta", "t", "P"])

        eta_choices = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]  # percent

        while True:
            self.m = rnd.choice([20, 25, 30, 40, 50, 60, 80, 100, 120])  # kg
            self.h = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20])  # m

            if self.target == "eta":
                self.P = rnd.choice([200, 250, 300, 400, 500, 600, 800, 1000, 1200, 1500, 2000])  # W
                self.t = rnd.choice([5, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80])  # s
                self.E_out = self.m * self.g * self.h
                self.E_in = self.P * self.t
                self.eta = self.E_out / self.E_in
                if 0.15 <= self.eta <= 0.95:
                    break

            elif self.target == "t":
                self.P = rnd.choice([200, 250, 300, 400, 500, 600, 800, 1000, 1200, 1500, 2000])  # W
                self.eta_percent = rnd.choice(eta_choices)
                self.eta = self.eta_percent / 100
                self.t = (self.m * self.g * self.h) / (self.eta * self.P)
                if 3 <= self.t <= 120:
                    break

            else:  # target == "P"
                self.t = rnd.choice([5, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 80])  # s
                self.eta_percent = rnd.choice(eta_choices)
                self.eta = self.eta_percent / 100
                self.P = (self.m * self.g * self.h) / (self.eta * self.t)
                if 100 <= self.P <= 3000:
                    break

        if self.target == "eta":
            self.answer = sig_figs(self.eta * 100, 3)  # %
        elif self.target == "t":
            self.answer = sig_figs(self.t, 3)  # s
        else:
            self.answer = sig_figs(self.P, 3)  # W

        self.description = (
            "A motor lifts a load vertically at constant speed. The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Work, energy and power"
        self.subtopic = "Energy conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m}\\,\\text{{kg}}\\\\"
            f"\\text{{Height, }} h &= {self.h}\\,\\text{{m}}\\\\"
            f"\\text{{Acceleration of free fall, }} g &= 9.81\\,\\text{{m s}}^{{-2}}\\\\"
            "\\text{{Useful work output (Gain in GPE):}} &\\\\"
            "W_{out} &= mgh\\\\"
            f"&= {self.m} \\times 9.81 \\times {self.h}\\\\"
            f"&= {round(self.m * 9.81 * self.h, 10)}\\,\\text{{J}}\\\\"
            "\\text{{Relationship between power, time, and efficiency:}} &\\\\"
            "\\eta &= \\frac{W_{out}}{W_{in}} = \\frac{mgh}{P \\times t}\\\\"
            "\\text{{Solving for the unknown variable:}} &\\\\"
            + (
                f"\\eta &= \\frac{{{round(self.m * 9.81 * self.h, 10)}}}{{{self.P} \\times {self.t}}}\\\\"
                f"&= {round((self.m * 9.81 * self.h) / (self.P * self.t), 10)}\\\\"
                f"\\text{{Efficiency (\\%)}} &= {self.answer}\\%"
                if self.target == "eta" else
                f"t &= \\frac{{mgh}}{{\\eta \\times P}}\\\\"
                f"&= \\frac{{{round(self.m * 9.81 * self.h, 10)}}}{{{self.eta} \\times {self.P}}}\\\\"
                f"&= {self.answer}\\,\\text{{s}}"
                if self.target == "t" else
                f"P &= \\frac{{mgh}}{{\\eta \\times t}}\\\\"
                f"&= \\frac{{{round(self.m * 9.81 * self.h, 10)}}}{{{self.eta} \\times {self.t}}}\\\\"
                f"&= {self.answer}\\,\\text{{W}}"
            ) +
            "\\end{aligned}\\]"
        )
          

    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.2, 4.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Ground
        ax.plot([0.8, 9.2], [1.2, 1.2], linewidth=2, color="black")

        # Pulley/motor box
        ax.add_patch(patches.Rectangle((4.2, 8.0), 1.6, 1.1, fill=False, linewidth=2, edgecolor="black"))
        ax.text(5.0, 9.25, "motor", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Rope
        ax.plot([5.0, 5.0], [8.0, 3.0], linewidth=2, color="black")

        # Load
        ax.add_patch(patches.Rectangle((4.5, 2.0), 1.0, 1.0, fill=False, linewidth=2, edgecolor="black"))
        ax.text(5.0, 3.25, f"m = {self.m} kg", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Height arrow
        ax.annotate("", xy=(7.8, 8.0), xytext=(7.8, 2.0),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(8.05, 5.0, f"h = {self.h} m", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # g label
        ax.text(9.2, 0.6, "g = 9.81 m s⁻²", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Show / hide given values according to target
        # Keep values in image (not in statement)
        if self.target == "eta":
            ax.text(1.0, 9.1, f"P = {self.P} W", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 8.2, f"t = {self.t} s", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 7.3, "η = ?", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        elif self.target == "t":
            ax.text(1.0, 9.1, f"P = {self.P} W", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 8.2, f"η = {self.eta_percent} %", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 7.3, "t = ?", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(1.0, 9.1, f"t = {self.t} s", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 8.2, f"η = {self.eta_percent} %", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(1.0, 7.3, "P = ?", ha="left", va="top",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy079:
    """
    Energy conservation (kinetic energy -> work done by braking force).
    Dynamic target: find braking force OR stopping distance OR initial speed.
    """

    def __init__(self):
        self.target = rnd.choice(["F", "s", "u"])

        while True:
            self.m = rnd.choice([800, 900, 1000, 1100, 1200, 1400, 1600])  # kg

            if self.target == "F":
                self.u = rnd.randint(12, 35)  # m s^-1
                self.s = rnd.choice([15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90])  # m
                self.F = 0.5 * self.m * self.u**2 / self.s
                if 800 <= self.F <= 10000:
                    break

            elif self.target == "s":
                self.u = rnd.randint(12, 35)  # m s^-1
                self.F = rnd.choice([1200, 1500, 1800, 2200, 2600, 3000, 3500, 4000, 5000, 6000, 7000, 8000])  # N
                self.s = 0.5 * self.m * self.u**2 / self.F
                if 10 <= self.s <= 150:
                    break

            else:  # target == "u"
                self.F = rnd.choice([1200, 1500, 1800, 2200, 2600, 3000, 3500, 4000, 5000, 6000, 7000, 8000])  # N
                self.s = rnd.choice([15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100])  # m
                self.u = math.sqrt(2 * self.F * self.s / self.m)
                if 10 <= self.u <= 40:
                    break

        if self.target == "F":
            self.answer = sig_figs(self.F, 3)
        elif self.target == "s":
            self.answer = sig_figs(self.s, 3)
        else:
            self.answer = sig_figs(self.u, 3)

        self.description = (
            "A car moves on a level road and is brought to rest by a constant braking force. The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Work, energy and power"
        self.subtopic = "Energy conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial speed, }} u &= {float(f'{self.u:.3g}') if self.target != 'u' else '\\text{?}'}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Braking force, }} F &= {float(f'{self.F:.3g}') if self.target != 'F' else '\\text{?}'}\\,\\text{{N}}\\\\"
            f"\\text{{Stopping distance, }} s &= {float(f'{self.s:.3g}') if self.target != 's' else '\\text{?}'}\\,\\text{{m}}\\\\"
            "\\text{{The work done by the braking force equals the change in kinetic energy:}} &\\\\"
            "W &= \\Delta E_k\\\\"
            "F \\times s &= \\frac{1}{2} m u^2 - \\frac{1}{2} m v^2\\\\"
            "\\text{{Since the final speed }} v = 0\\text{{:}} &\\\\"
            "F \\times s &= \\frac{1}{2} m u^2\\\\"
            "\\text{{Substituting the known values and solving:}} &\\\\"
            + (
                f"F \\times {float(f'{self.s:.3g}')} &= \\frac{{1}}{{2}} ({self.m}) ({float(f'{self.u:.3g}')})^2\\\\"
                f"F &= \\frac{{0.5 \\times {self.m} \\times {round(self.u**2, 10)}}}{{{float(f'{self.s:.3g}')}}}\\\\"
                f"F &= {self.answer}\\,\\text{{N}}"
                if self.target == "F" else
                f"{float(f'{self.F:.3g}')} \\times s &= \\frac{{1}}{{2}} ({self.m}) ({float(f'{self.u:.3g}')})^2\\\\"
                f"s &= \\frac{{0.5 \\times {self.m} \\times {round(self.u**2, 10)}}}{{{float(f'{self.F:.3g}')}}}\\\\"
                f"s &= {self.answer}\\,\\text{{m}}"
                if self.target == "s" else
                f"{float(f'{self.F:.3g}')} \\times {float(f'{self.s:.3g}')} &= \\frac{{1}}{{2}} ({self.m}) u^2\\\\"
                f"u^2 &= \\frac{{2 \\times {float(f'{self.F:.3g}')} \\times {float(f'{self.s:.3g}')}}}{{{self.m}}}\\\\"
                f"u &= \\sqrt{{{round(2 * self.F * self.s / self.m, 10)}}}\\\\"
                f"u &= {self.answer}\\,\\text{{m s}}^{{-1}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.4, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Road
        y_road = 1.0
        ax.plot([0.6, 9.4], [y_road, y_road], linewidth=2, color="black")

        # Car block
        cx, cy = 2.0, y_road
        cw, ch = 2.2, 1.1
        ax.add_patch(patches.Rectangle((cx, cy), cw, ch, fill=False, linewidth=2, edgecolor="black"))
        ax.text(cx + cw/2, cy + ch + 0.25, f"m = {self.m} kg", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Stop marker
        x_stop = 8.6
        ax.plot([x_stop, x_stop], [y_road, y_road + 1.2], linewidth=2, color="black")
        ax.text(x_stop, y_road + 1.35, "stop", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Stopping distance bracket
        y_s = 0.35
        ax.annotate("", xy=(cx + cw, y_s), xytext=(x_stop, y_s),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        if self.target == "s":
            ax.text((cx + cw + x_stop)/2, y_s - 0.15, "s = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text((cx + cw + x_stop)/2, y_s - 0.15, f"s = {float(f'{self.s:.3g}')} m", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Speed arrow (to right)
        y_u = cy + ch + 0.05
        ax.annotate("", xy=(cx + cw + 1.4, y_u), xytext=(cx + cw + 0.2, y_u),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        if self.target == "u":
            ax.text(cx + cw + 1.55, y_u, "u = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(cx + cw + 1.55, y_u, f"u = {float(f'{self.u:.3g}')} m s⁻¹", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Braking force arrow (left)
        y_F = cy + 0.55*ch
        ax.annotate("", xy=(cx - 1.3, y_F), xytext=(cx, y_F),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        if self.target == "F":
            ax.text(cx - 1.45, y_F, "F = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(cx - 1.45, y_F, f"F = {float(f'{self.F:.3g}')} N", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy080:
    """
    Gravitational potential energy and kinetic energy.
    Vertical throw: KE at launch -> GPE at maximum height.
    Dynamic target: find maximum height OR find launch speed.
    """

    def __init__(self):
        self.g = 9.81
        self.target = rnd.choice(["h", "u"])

        if self.target == "h":
            self.u = rnd.randint(8, 28)  # m s^-1
            self.h = self.u**2 / (2 * self.g)
        else:
            self.h = rnd.choice([2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0])
            self.u = math.sqrt(2 * self.g * self.h)

        # mass shown but cancels
        self.m = rnd.choice([0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50])  # kg

        if self.target == "h":
            self.answer = sig_figs(self.h, 3)
        else:
            self.answer = sig_figs(self.u, 3)

        self.description = (
            "A small ball is projected vertically upwards. The relevant values are shown in the diagram.\n"
            "Neglect air resistance. Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Work, energy and power"
        self.subtopic = "Gravitational potential energy and kinetic energy"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m:.2f}\\,\\text{{kg}}\\\\"
            f"\\text{{Acceleration of free fall, }} g &= 9.81\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Initial speed, }} u &= {self.u if self.target == 'h' else '\\text{?}'}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Maximum height, }} h &= {self.h if self.target == 'u' else '\\text{?}'}\\,\\text{{m}}\\\\"
            "\\text{{Using the Principle of Conservation of Energy:}} &\\\\"
            "\\text{{Kinetic Energy at launch}} &= \\text{{Potential Energy at maximum height}}\\\\"
            "\\frac{1}{2} m u^2 &= m g h\\\\"
            "\\text{{The mass }} m \\text{{ cancels out from both sides:}} &\\\\"
            "\\frac{1}{2} u^2 &= g h\\\\"
            "\\text{{Substituting the known values and solving:}} &\\\\"
            + (
                f"\\frac{{1}}{{2}} ({self.u})^2 &= 9.81 \\times h\\\\"
                f"h &= \\frac{{0.5 \\times {self.u**2}}}{{9.81}}\\\\"
                f"h &= {round(0.5 * self.u**2 / 9.81, 10)}\\,\\text{{m}}\\\\"
                f"\\text{{Final Answer}} &= {self.answer}"
                if self.target == "h" else
                f"\\frac{{1}}{{2}} u^2 &= 9.81 \\times {self.h}\\\\"
                f"u^2 &= 2 \\times 9.81 \\times {self.h}\\\\"
                f"u &= \\sqrt{{{round(2 * 9.81 * self.h, 10)}}}\\\\"
                f"u &= {round(math.sqrt(2 * 9.81 * self.h), 10)}\\,\\text{{m s}}^{{-1}}\\\\"
                f"\\text{{Final Answer}} &= {self.answer}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(5.8, 4.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Ground
        y0 = 1.4
        ax.plot([1.0, 9.0], [y0, y0], linewidth=2, color="black")
        ax.text(1.0, 0.7, "g = 9.81 m s⁻²", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Launch point and max point
        x = 4.0
        y_launch = y0
        y_max = 8.6

        ax.add_patch(patches.Circle((x, y_launch), 0.18, fill=False, linewidth=2, edgecolor="black"))
        ax.add_patch(patches.Circle((x, y_max), 0.14, fill=False, linewidth=2, edgecolor="black"))
        ax.text(x + 0.4, y_max, "max", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Height bracket
        ax.annotate("", xy=(6.8, y_max), xytext=(6.8, y_launch),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        if self.target == "h":
            ax.text(7.05, (y_max + y_launch)/2, "h = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(7.05, (y_max + y_launch)/2, f"h = {self.h:.1f} m", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Velocity arrow at launch
        ax.annotate("", xy=(x, y_launch + 2.6), xytext=(x, y_launch + 0.3),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        if self.target == "u":
            ax.text(x + 0.35, y_launch + 1.5, "u = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(x + 0.35, y_launch + 1.5, f"u = {self.u} m s⁻¹", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Mass label (shown but not needed)
        ax.text(8.9, 9.4, f"m = {self.m:.2f} kg", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy081:
    """
    Gravitational potential energy and kinetic energy.
    """

    def __init__(self):
        self.g = 9.81
        self.m = rnd.choice([100, 150, 200, 250, 300, 400, 500])  # kg (shown; cancels)

        self.motion = rnd.choice(["downhill", "uphill"])  # A -> B as drawn
        self.target = rnd.choice(["v", "dh"])            # unknown speed at B or vertical height change

        if self.target == "v":
            # Given u and Δh; find v
            while True:
                if self.motion == "downhill":
                    self.u = rnd.choice([0, 2, 4, 6, 8, 10, 12, 14])  # m s^-1
                    self.dh = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20, 25, 30])  # m (drop magnitude)
                    self.v = math.sqrt(self.u**2 + 2 * self.g * self.dh)
                    if 4 <= self.v <= 45:
                        break
                else:  # uphill
                    self.u = rnd.randint(10, 28)
                    self.dh = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 12.0])
                    val = self.u**2 - 2 * self.g * self.dh
                    if val > 1.0:
                        self.v = math.sqrt(val)
                        if 2 <= self.v <= self.u and self.v <= 35:
                            break

            self.answer = sig_figs(self.v, 3)

        else:
            # Given u and v; find Δh
            while True:
                if self.motion == "downhill":
                    self.u = rnd.choice([0, 2, 4, 6, 8, 10, 12, 14])
                    self.v = rnd.randint(max(4, self.u + 3), min(45, self.u + 28))
                    self.dh = (self.v**2 - self.u**2) / (2 * self.g)
                    if 1.0 <= self.dh <= 30.0:
                        break
                else:  # uphill
                    self.u = rnd.randint(12, 30)
                    self.v = rnd.randint(2, self.u - 2)
                    self.dh = (self.u**2 - self.v**2) / (2 * self.g)
                    if 0.8 <= self.dh <= 20.0:
                        break

            self.answer = sig_figs(self.dh, 3)

        self.topic = "Work, energy and power"
        self.subtopic = "Gravitational potential energy and kinetic energy"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.description = (
            "A cart moves from A to B on a smooth track as shown. The mass, g, and all required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass, }} m &= {self.m}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial speed at A, }} u &= {self.u}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Acceleration due to gravity, }} g &= 9.81\\,\\text{{m s}}^{{-2}}\\\\"
            "\\text{{Using the Principle of Conservation of Energy:}} &\\\\"
            "\\text{{Total Energy at A}} &= \\text{{Total Energy at B}}\\\\"
            "E_{kA} + E_{pA} &= E_{kB} + E_{pB}\\\\"
            "\\frac{1}{2}mu^2 + mgh_A &= \\frac{1}{2}mv^2 + mgh_B\\\\"
            "\\text{{The mass }} m \\text{{ cancels out from all terms:}} &\\\\"
            "\\frac{1}{2}u^2 + gh_A &= \\frac{1}{2}v^2 + gh_B\\\\"
            "\\text{{Rearranging in terms of the vertical height change, }} \\Delta h = |h_A - h_B|: &\\\\"
            + (
                "\\text{{For downhill motion, }} g\\Delta h = \\frac{1}{2}v^2 - \\frac{1}{2}u^2\\\\"
                if self.motion == "downhill" else
                "\\text{{For uphill motion, }} g\\Delta h = \\frac{1}{2}u^2 - \\frac{1}{2}v^2\\\\"
            ) +
            "\\text{{Substituting the known values and solving:}} &\\\\"
            + (
                f"v^2 &= u^2 {'+' if self.motion == 'downhill' else '-'} 2g\\Delta h\\\\"
                f"v^2 &= ({self.u})^2 {'+' if self.motion == 'downhill' else '-'} 2(9.81)({sig_figs(self.dh, 3)})\\\\"
                f"v &= \\sqrt{{{round(self.u**2 + (1 if self.motion == 'downhill' else -1) * 2 * 9.81 * self.dh, 10)}}}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
                if self.target == "v" else
                f"9.81 \\times \\Delta h &= \\left| \\frac{1}{2}({self.v})^2 - \\frac{1}{2}({self.u})^2 \\right|\\\\"
                f"\\Delta h &= \\frac{{|{round(0.5 * self.v**2, 10)} - {round(0.5 * self.u**2, 10)}|}}{{9.81}}\\\\"
                f"\\Delta h &= {self.answer}\\,\\text{{m}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        self.layout = rnd.choice(["A_left", "A_right"])

        fig, ax = plt.subplots(figsize=(6.4, 4.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Baseline
        ax.plot([0.8, 9.2], [1.0, 1.0], linewidth=2, color="black")

        # Coordinates (A and B)
        xA, xB = (2.0, 8.2) if self.layout == "A_left" else (8.2, 2.0)
        y_high, y_low = 5.6, 2.2

        if self.motion == "downhill":
            yA, yB = y_high, y_low
        else:
            yA, yB = y_low, y_high

        # Track
        ax.plot([xA, xB], [yA, yB], linewidth=3, color="black")

        # Points and small carts
        ax.add_patch(patches.Circle((xA, yA), 0.12, fill=True, color="black"))
        ax.add_patch(patches.Circle((xB, yB), 0.12, fill=True, color="black"))

        ax.add_patch(patches.Rectangle((xA - 0.35, yA - 0.25), 0.7, 0.5, fill=False, linewidth=2, edgecolor="black"))
        ax.add_patch(patches.Rectangle((xB - 0.35, yB - 0.25), 0.7, 0.5, fill=False, linewidth=2, edgecolor="black"))

        ax.text(xA - 0.2, yA + 0.25, "A", ha="right", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(xB + 0.2, yB + 0.25, "B", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Unit direction along track A->B for arrows
        dx, dy = (xB - xA), (yB - yA)
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L

        # Speed arrow at A
        ax.annotate("", xy=(xA + 1.2 * ux, yA + 1.2 * uy), xytext=(xA + 0.2 * ux, yA + 0.2 * uy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(xA + 1.35 * ux, yA + 1.35 * uy, f"u = {self.u} m s⁻¹", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Speed arrow at B
        ax.annotate("", xy=(xB + 1.0 * ux, yB + 1.0 * uy), xytext=(xB + 0.2 * ux, yB + 0.2 * uy),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        if self.target == "v":
            ax.text(xB + 1.15 * ux, yB + 1.15 * uy, "v = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(xB + 1.15 * ux, yB + 1.15 * uy, f"v = {self.v} m s⁻¹", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Vertical height change bracket (always magnitude)
        top_y = max(yA, yB)
        bot_y = min(yA, yB)
        x_br = 9.1  # keep consistent and readable
        ax.annotate("", xy=(x_br, top_y), xytext=(x_br, bot_y),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        if self.target == "dh":
            ax.text(x_br - 0.15, (top_y + bot_y) / 2, "Δh = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(x_br - 0.15, (top_y + bot_y) / 2, f"Δh = {sig_figs(self.dh,3)} m", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Labels
        ax.text(1.0, 0.45, "g = 9.81 m s⁻²", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(9.2, 6.6, f"m = {self.m} kg", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy082:
    """
    Resultant force varies linearly with displacement x from 0 to s (triangle/trapezium).
    Object starts from rest on a smooth horizontal surface.
    """

    def __init__(self):
        self.target = rnd.choice(["W", "v"])

        # Choose shape
        self.shape = rnd.choice(["triangle", "trapezium"])

        while True:
            self.m = rnd.choice([0.50, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00])  # kg
            self.s = rnd.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])  # m

            if self.shape == "triangle":
                self.F0 = 0
                self.F1 = rnd.choice([20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 120, 140])  # N
            else:
                self.F0 = rnd.choice([10, 15, 20, 25, 30, 35, 40, 50, 60])  # N
                self.F1 = rnd.choice([40, 50, 60, 70, 80, 90, 100, 120, 140, 160])  # N
                if self.F1 <= self.F0:
                    continue

            # Work = area under straight-line F-x (trapezium)
            self.W = 0.5 * (self.F0 + self.F1) * self.s  # J

            if self.target == "v":
                self.v = math.sqrt(2 * self.W / self.m)
                if 2 <= self.v <= 40:
                    break
            else:
                if 100 <= self.W <= 5000:
                    break

        if self.target == "W":
            self.answer = sig_figs(self.W, 3)
        else:
            self.answer = sig_figs(self.v, 3)

        self.description = (
            "The graph shows how the resultant force varies with displacement x from 0 to s. "
            "A trolley of mass m starts from rest on a smooth horizontal surface, and all required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Work, energy and power"
        self.subtopic = "Energy conservation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial force, }} F_0 &= {self.F0}\\,\\text{{N}}\\\\"
            f"\\text{{Final force, }} F_1 &= {self.F1}\\,\\text{{N}}\\\\"
            f"\\text{{Total displacement, }} s &= {self.s}\\,\\text{{m}}\\\\"
            f"\\text{{Mass of trolley, }} m &= {self.m:.2f}\\,\\text{{kg}}\\\\"
            "\\text{{Step 1: Calculate the work done (}} W \\text{{).}} &\\\\"
            "\\text{{Work done is equal to the area under the force-displacement graph.}} &\\\\"
            + (
                f"\\text{{Since the shape is a triangle:}} &\\\\"
                f"W &= \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}\\\\"
                f"W &= \\frac{{1}}{{2}} \\times s \\times F_1\\\\"
                if self.shape == "triangle" else
                f"\\text{{Since the shape is a trapezium:}} &\\\\"
                f"W &= \\frac{{1}}{{2}} \\times (F_0 + F_1) \\times s\\\\"
            ) +
            f"W &= \\frac{{1}}{{2}} \\times ({self.F0} + {self.F1}) \\times {self.s}\\\\"
            f"W &= {round(self.W, 10)}\\,\\text{{J}}\\\\"
            + (
                "\\text{{Final Answer}} &= " + str(self.answer) + "\\,\\text{{J}}"
                if self.target == "W" else
                "\\text{{Step 2: Calculate the final speed (}} v \\text{{).}} &\\\\"
                "\\text{{Using the work-energy theorem, where useful work done = gain in kinetic energy:}} &\\\\"
                "W &= \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2\\\\"
                "\\text{{As the trolley starts from rest (}} u = 0 \\text{{):}} &\\\\"
                f"{round(self.W, 10)} &= \\frac{{1}}{{2}} \\times {self.m:.2f} \\times v^2\\\\"
                f"v^2 &= \\frac{{2 \\times {round(self.W, 10)}}}{{{self.m:.2f}}}\\\\"
                f"v &= \\sqrt{{{round(2 * self.W / self.m, 10)}}}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.2, 4.0))

        # Axes limits
        Fmax = max(self.F0, self.F1)
        ax.set_xlim(-0.2, self.s * 1.15)
        ax.set_ylim(0, Fmax * 1.35)

        ax.set_xlabel("displacement x / m", fontsize=10)
        ax.set_ylabel("force F / N", fontsize=10)
        ax.tick_params(axis="both", labelsize=10)

        # Plot line (0,F0) -> (s,F1)
        ax.plot([0, self.s], [self.F0, self.F1], linewidth=2, color="black")
        ax.fill_between([0, self.s], [self.F0, self.F1], [0, 0], alpha=0.18)

        ax.plot([0, self.s], [self.F0, self.F1], "ko", markersize=4)
        ax.text(0, self.F0 + 0.06 * Fmax, f"F₀ = {self.F0} N", fontsize=10,
                ha="left", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(self.s, self.F1 + 0.06 * Fmax, f"F₁ = {self.F1} N", fontsize=10,
                ha="right", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Show s clearly
        ax.text(self.s, -0.10 * Fmax, f"s = {self.s} m", fontsize=10,
                ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Extra info in-figure (mass + from rest)
        ax.text(0.02, 0.98, f"m = {self.m:.2f} kg", transform=ax.transAxes,
                ha="left", va="top", fontsize=10,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(0.02, 0.90, "u = 0", transform=ax.transAxes,
                ha="left", va="top", fontsize=10,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown indicator
        if self.target == "W":
            ax.text(0.98, 0.98, "W = ?", transform=ax.transAxes,
                    ha="right", va="top", fontsize=10,
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(0.98, 0.98, "v = ?", transform=ax.transAxes,
                    ha="right", va="top", fontsize=10,
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        ax.grid(True, linestyle="--", alpha=0.45)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy083:
    """
    Stress and strain (tensile stress / tensile force).
    Uses: σ = F / A,  A = π(d/2)^2
    """

    def __init__(self):
        self.target = rnd.choice(["stress", "force"])      # what to find
        self.force_symbol = rnd.choice(["F", "T"])         # label style on diagram

        d_choices = [0.50, 0.60, 0.75, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50]  # mm

        while True:
            self.d_mm = rnd.choice(d_choices)
            d = self.d_mm * 1e-3
            self.A = math.pi * (d / 2) ** 2

            if self.target == "stress":
                # given force -> find stress
                self.F = rnd.choice([150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900])  # N
                self.sigma = self.F / self.A
                self.sigma_MPa = self.sigma / 1e6
                if 20 <= self.sigma_MPa <= 900:
                    break
            else:
                # given stress -> find force (tension)
                self.sigma_MPa = rnd.choice([30, 40, 50, 60, 80, 100, 120, 150, 180, 200, 250, 300, 350, 400, 500])
                self.sigma = self.sigma_MPa * 1e6
                self.F = self.sigma * self.A
                if 50 <= self.F <= 2000:
                    break

        if self.target == "stress":
            self.answer = sig_figs(self.sigma_MPa, 3)
        else:
            self.answer = sig_figs(self.F, 3)

        self.description = (
            "A wire is in tension. All required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Deformation of solids"
        self.subtopic = "Stress and strain"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diameter, }} d &= {self.d_mm}\\,\\text{{mm}} = {self.d_mm} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            "\\text{{Step 1: Calculate the cross-sectional area }} A: &\\\\"
            "A &= \\pi \\left( \\frac{d}{2} \\right)^2\\\\"
            f"&= \\pi \\left( \\frac{{{self.d_mm} \\times 10^{{-3}}}}{2} \\right)^2\\\\"
            f"&= {round(self.A, 10)}\\,\\text{{m}}^2\\\\"
            "\\text{{Step 2: Relate tensile stress (}} \\sigma \\text{{) and force (}} F \\text{{):}} &\\\\"
            "\\sigma &= \\frac{F}{A}\\\\"
            "\\text{{Step 3: Solve for the unknown variable:}} &\\\\"
            + (
                f"\\sigma &= \\frac{{{sig_figs(self.F, 3)}}}{{{round(self.A, 10)}}}\\\\"
                f"\\sigma &= {round(self.sigma, 10)}\\,\\text{{Pa}}\\\\"
                f"\\sigma &= {self.answer}\\,\\text{{MPa}}"
                if self.target == "stress" else
                f"F &= \\sigma \\times A\\\\"
                f"F &= ({self.sigma_MPa} \\times 10^6) \\times {round(self.A, 10)}\\\\"
                f"F &= {self.answer}\\,\\text{{N}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 2.8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wire (horizontal)
        x1, x2 = 2.0, 8.0
        y = 2.0
        h = 0.6
        ax.add_patch(patches.Rectangle((x1, y - h/2), x2 - x1, h, fill=False, linewidth=2, edgecolor="black"))

        # Tension/force arrows outward
        ax.annotate("", xy=(x1 - 1.2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.annotate("", xy=(x2 + 1.2, y), xytext=(x2, y),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Force labels depend on target
        if self.target == "stress":
            ax.text(x1 - 1.25, y + 0.45, f"{self.force_symbol} = {sig_figs(self.F,3)} N", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(x2 + 1.25, y + 0.45, f"{self.force_symbol} = {sig_figs(self.F,3)} N", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(9.6, 3.6, "σ = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
        else:
            ax.text(x1 - 1.25, y + 0.45, f"{self.force_symbol} = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
            ax.text(x2 + 1.25, y + 0.45, f"{self.force_symbol} = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="black", pad=0.25))
            ax.text(9.6, 3.6, f"σ = {sig_figs(self.sigma_MPa,3)} MPa", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Diameter marker
        xm = (x1 + x2) / 2
        ax.annotate("", xy=(xm, y + h/2), xytext=(xm, y - h/2),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(xm + 0.35, y, f"d = {self.d_mm} mm", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy084:
    """
    Stress and strain: tensile strain in a wire.
    Strain ε = ΔL / L.
    Values are shown in the diagram.
    """

    def __init__(self):
        while True:
            self.L = rnd.choice([1.2, 1.5, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0])  # m
            self.dL_mm = rnd.choice([0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00, 2.50, 3.00, 4.00, 5.00])  # mm
            self.dL = self.dL_mm * 1e-3  # m
            self.strain = self.dL / self.L
            if 1e-5 <= self.strain <= 5e-3:
                break

        self.answer = float(f"{self.strain:.3g}")

        self.description = (
            "A wire is stretched. The original length and the extension are shown in the diagram.\n"
            "Determine the tensile strain in the wire.\n"
            "strain = (_)"
        )
        self.topic = "Deformation of solids"
        self.subtopic = "Stress and strain"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original length, }} L &= {self.L}\\,\\text{{m}}\\\\"
            f"\\text{{Extension, }} \\Delta L &= {self.dL_mm}\\,\\text{{mm}} = {self.dL_mm} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            "\\text{{Step 1: Apply the definition of tensile strain.}} &\\\\"
            "\\text{{Tensile strain (}} \\epsilon \\text{{) is defined as the extension per unit original length:}} &\\\\"
            "\\epsilon &= \\frac{\\Delta L}{L}\\\\"
            "\\text{{Step 2: Substitute the values into the equation (ensuring units are consistent):}} &\\\\"
            f"\\epsilon &= \\frac{{{self.dL_mm} \\times 10^{{-3}}}}{{{self.L}}}\\\\"
            f"\\epsilon &= \\frac{{{self.dL}}}{{{self.L}}}\\\\"
            f"\\epsilon &= {round(self.strain, 10)}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.2, 3.8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wire (vertical)
        x = 5.0
        w = 0.7
        y_bottom = 1.1

        y_original_top = 5.4
        ext_pix = 0.6 + 0.18 * self.dL_mm   # 0.67 to 1.5 approx
        y_actual_top = min(6.85, y_original_top + ext_pix)

        # Draw wire to actual length
        ax.add_patch(patches.Rectangle((x - w/2, y_bottom), w, y_actual_top - y_bottom,
                                       fill=False, linewidth=2, edgecolor="black"))

        # Original length marker (dashed)
        ax.plot([x - 1.4, x + 1.4], [y_original_top, y_original_top],
                linewidth=2, color="black", linestyle="--")

        # Length L bracket (bottom to dashed line)
        xL = 3.0
        ax.annotate("", xy=(xL, y_original_top), xytext=(xL, y_bottom),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(xL - 0.2, (y_original_top + y_bottom) / 2, f"L = {self.L} m",
                ha="right", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Extension ΔL bracket (dashed line to actual top)
        xE = 7.0
        ax.annotate("", xy=(xE, y_actual_top), xytext=(xE, y_original_top),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(xE + 0.25, (y_actual_top + y_original_top) / 2, f"ΔL = {self.dL_mm} mm",
                ha="left", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown label
        # ax.text(2.6, 6.6, "strain = ?", ha="right", va="top",
                # bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy085:
    """
    Elastic and plastic behaviour: Hooke’s law (linear force–extension).
    Determine spring constant k from a force–extension graph (straight line).
    """

    def __init__(self):
        while True:
            self.k = rnd.choice([80, 100, 120, 150, 180, 200, 240, 250, 300, 320, 350, 400, 450, 500])  # N m^-1
            self.x_m = rnd.choice([0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15])               # m
            self.F = self.k * self.x_m
            if 6 <= self.F <= 60:
                break

        self.answer = sig_figs(self.k, 3)

        self.description = (
            "The force–extension graph for a spring is shown. The spring obeys Hooke’s law over the range shown.\n"
            "Determine the spring constant k.\n"
            "k = (_) N m⁻¹"
        )
        self.topic = "Deformation of solids"
        self.subtopic = "Elastic and plastic behaviour"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Extension, }} x &= {self.x_m * 100:.1f}\\,\\text{{cm}} = {self.x_m:.2f}\\,\\text{{m}}\\\\"
            f"\\text{{Force applied, }} F &= {self.F:.1f}\\,\\text{{N}}\\\\"
            "\\text{{Step 1: Apply Hooke's Law.}} &\\\\"
            "\\text{{Hooke's Law states that the force }} F \\text{{ is proportional to the extension }} x: &\\\\"
            "F &= kx\\\\"
            "\\text{{Step 2: Rearrange the equation to solve for the spring constant }} k: &\\\\"
            "k &= \\frac{F}{x}\\\\"
            "\\text{{Step 3: Substitute the values (ensuring }} x \\text{{ is in meters):}} &\\\\"
            f"k &= \\frac{{{self.F:.1f}}}{{{self.x_m:.2f}}}\\\\"
            f"k &= {round(self.k, 10)}\\,\\text{{N m}}^{{-1}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.0, 4.0))

        # Use extension in cm for readability
        x_cm = self.x_m * 100
        ax.plot([0, x_cm], [0, self.F], linewidth=2, color="black")
        ax.scatter([x_cm], [self.F], s=25, color="black")

        ax.set_xlabel("extension x / cm", fontsize=10)
        ax.set_ylabel("force F / N", fontsize=10)
        ax.tick_params(axis="both", labelsize=10)

        ax.set_xlim(0, x_cm * 1.30)
        ax.set_ylim(0, self.F * 1.35)
        ax.grid(True, linestyle="--", alpha=0.45)

        ax.text(x_cm, self.F + 0.06 * self.F, f"({x_cm:.1f} cm, {self.F:.1f} N)",
                ha="right", va="bottom", fontsize=10,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # ax.text(0.98, 0.98, "k = ?", transform=ax.transAxes,
                # ha="right", va="top", fontsize=10,
                # bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy086:
    """
    Elastic and plastic behaviour: elastic potential energy in a spring.
    Spring obeys Hooke’s law. Energy stored = area under F–x graph = 1/2 F x.
    Values are shown in the diagram.
    """

    def __init__(self):
        while True:
            self.x_m = rnd.choice([0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15, 0.18, 0.20, 0.25])  # m
            self.F = rnd.choice([10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60])                # N
            self.E = 0.5 * self.F * self.x_m
            if 0.2 <= self.E <= 20:
                break

        self.answer = sig_figs(self.E, 3)

        self.description = (
            "A spring obeys Hooke’s law. The force applied and the extension are shown in the diagram.\n"
            "Determine the elastic potential energy stored in the spring.\n"
            "E = (_) J"
        )
        self.topic = "Deformation of solids"
        self.subtopic = "Elastic and plastic behaviour"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Extension, }} x &= {self.x_m * 100:.1f}\\,\\text{{cm}} = {self.x_m:.2f}\\,\\text{{m}}\\\\"
            f"\\text{{Applied force, }} F &= {self.F}\\,\\text{{N}}\\\\"
            "\\text{{Step 1: Apply the formula for elastic potential energy.}} &\\\\"
            "\\text{{Since the spring obeys Hooke's law, the work done in stretching is given by:}} &\\\\"
            "E &= \\frac{1}{2} F x\\\\"
            "\\text{{Step 2: Substitute the known values into the equation:}} &\\\\"
            f"E &= \\frac{{1}}{{2}} \\times {self.F} \\times {self.x_m:.2f}\\\\"
            f"E &= {round(self.E, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4.5)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Wall (left)
        ax.plot([1.3, 1.3], [1.2, 3.6], linewidth=3, color="black")
        ax.plot([1.0, 1.3], [3.6, 3.3], linewidth=2, color="black")
        ax.plot([1.0, 1.3], [1.2, 1.5], linewidth=2, color="black")

        # Extension mapping (visual only)
        x_cm = self.x_m * 100
        dx = min(3.0, max(0.6, 0.15 * x_cm))  # keep within a nice range

        x_anchor = 1.3
        x_nat = 5.0
        x_end = x_nat + dx
        y_mid = 2.4

        # Spring zig-zag
        n = 8
        xs = [x_anchor, x_anchor + 0.4]
        ys = [y_mid, y_mid]
        x_start = x_anchor + 0.4
        x_stop = x_end - 0.6

        for i in range(n):
            t = i / (n - 1)
            x_i = x_start + t * (x_stop - x_start)
            y_i = y_mid + (0.35 if i % 2 == 0 else -0.35)
            xs.append(x_i)
            ys.append(y_i)

        xs += [x_stop + 0.25, x_end - 0.6]
        ys += [y_mid, y_mid]
        ax.plot(xs, ys, linewidth=2, color="black")

        # End block
        ax.add_patch(patches.Rectangle((x_end - 0.6, y_mid - 0.35), 0.6, 0.7,
                                       fill=False, linewidth=2, edgecolor="black"))

        # Natural length marker (dashed)
        ax.plot([x_nat, x_nat], [1.2, 3.6], linewidth=2, color="black", linestyle="--")
        ax.text(x_nat, 3.8, "unstretched\nend", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Force arrow
        ax.annotate("", xy=(x_end + 1.2, y_mid), xytext=(x_end, y_mid),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(x_end + 1.25, y_mid + 0.45, f"F = {self.F} N", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Extension bracket (from natural to stretched)
        y_ext = 0.9
        ax.annotate("", xy=(x_nat, y_ext), xytext=(x_end, y_ext),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((x_nat + x_end) / 2, y_ext - 0.15, f"x = {x_cm:.1f} cm", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown label
        # ax.text(9.6, 4.2, "E = ?", ha="right", va="top",
                # bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy087:
    """
    Elastic and plastic behaviour: permanent extension from a force–extension graph.
    Load to a maximum, then unload. Permanent extension is the x-intercept of the unloading line.
    """

    def __init__(self):
        while True:
            self.xp_mm = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 20, 25, 30])  # permanent extension (mm)
            self.xmax_mm = self.xp_mm + rnd.choice([25, 30, 40, 50, 60, 70, 80, 100])  # mm
            self.k_N_per_mm = rnd.choice([0.6, 0.8, 1.0, 1.2, 1.5, 2.0])               # N/mm (unloading gradient)
            self.Fmax = self.k_N_per_mm * (self.xmax_mm - self.xp_mm)                  # N
            if 30 <= self.Fmax <= 160 and self.xmax_mm <= 140:
                break

        self.answer = self.xp_mm  # mm (exact integer)

        self.description = (
            "The force–extension graph for a wire is shown. The wire is loaded and then unloaded along the line shown.\n"
            "Determine the permanent extension of the wire after unloading.\n"
            "permanent extension = (_) mm"
        )
        self.topic = "Deformation of solids"
        self.subtopic = "Elastic and plastic behaviour"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Maximum extension reached, }} x_{{max}} &= {self.xmax_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Maximum force applied, }} F_{{max}} &= {self.Fmax:.1f}\\,\\text{{N}}\\\\"
            f"\\text{{Unloading gradient (spring constant), }} k &= {self.k_N_per_mm:.1f}\\,\\text{{N/mm}}\\\\"
            "\\text{{Step 1: Understand the unloading process.}} &\\\\"
            "\\text{{When a wire is deformed plastically, it unloads along a line parallel}} &\\\\"
            "\\text{{to the initial linear elastic region. The permanent extension }} x_p &\\\\"
            "\\text{{is the extension remaining when the force is returned to zero.}} &\\\\"
            "\\text{{Step 2: Use the equation of the unloading line.}} &\\\\"
            "\\text{{The change in extension during unloading (elastic recovery) is:}} &\\\\"
            "\\Delta x &= \\frac{F_{max}}{k}\\\\"
            f"\\Delta x &= \\frac{{{self.Fmax:.1f}}}{{{self.k_N_per_mm:.1f}}}\\\\"
            f"&= {round(self.Fmax / self.k_N_per_mm, 10)}\\,\\text{{mm}}\\\\"
            "\\text{{Step 3: Calculate the permanent extension }} x_p. &\\\\"
            "x_p &= x_{max} - \\Delta x\\\\"
            f"x_p &= {self.xmax_mm} - {round(self.Fmax / self.k_N_per_mm, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{mm}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 10})

        fig, ax = plt.subplots(figsize=(6.2, 4.0))

        # Plot loading and unloading lines
        ax.plot([0, self.xmax_mm], [0, self.Fmax], linewidth=2, color="black", label="loading")
        ax.plot([self.xmax_mm, self.xp_mm], [self.Fmax, 0], linewidth=2, color="black", linestyle="--", label="unloading")

        # Mark important points
        ax.scatter([0, self.xmax_mm, self.xp_mm], [0, self.Fmax, 0], s=25, color="black")

        # Labels
        ax.set_xlabel("extension / mm", fontsize=10)
        ax.set_ylabel("force / N", fontsize=10)
        ax.tick_params(axis="both", labelsize=10)

        ax.set_xlim(0, max(40, int(self.xmax_mm * 1.20)))
        ax.set_ylim(0, max(60, self.Fmax * 1.30))
        ax.grid(True, linestyle="--", alpha=0.45)

        ax.text(self.xmax_mm, self.Fmax + 0.06 * self.Fmax, f"({self.xmax_mm} mm, {self.Fmax:.1f} N)",
                ha="right", va="bottom", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Unknown label at x-intercept of unloading line
        # ax.text(self.xp_mm, -0.08 * self.Fmax, "xₚ = ?", ha="center", va="top",
                # bbox=dict(facecolor="white", edgecolor="black", pad=0.25))

        # Show unloading gradient (helps interpret the dashed line; still minimal)
        ax.text(0.98, 0.98, f"unloading gradient = {self.k_N_per_mm:.1f} N/mm",
                transform=ax.transAxes, ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy088:
    """
    Progressive waves: wave equation v = fλ.
    Dynamic target: find v OR f OR λ (two are shown in the diagram).
    """

    def __init__(self):
        self.target = rnd.choice(["v", "f", "lam"])

        # Pick nice values so λ is sensible for the diagram
        while True:
            self.v = rnd.choice([20, 25, 30, 40, 50, 60, 80, 100, 120, 150, 200])  # m s^-1
            self.f = rnd.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50])  # Hz
            self.lam = self.v / self.f  # m
            if 0.20 <= self.lam <= 4.00:
                break

        if self.target == "v":
            self.answer = sig_figs(self.v, 3)
        elif self.target == "f":
            self.answer = sig_figs(self.f, 3)
        else:
            self.answer = sig_figs(self.lam, 3)

        self.description = (
            "A progressive wave is shown. Two of the quantities f, λ and v are given in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Waves"
        self.subtopic = "Progressive waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Wave speed, }} v &= {self.v if self.target != 'v' else '\\text{?}'}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Frequency, }} f &= {self.f if self.target != 'f' else '\\text{?}'}\\,\\text{{Hz}}\\\\"
            f"\\text{{Wavelength, }} \\lambda &= {sig_figs(self.lam, 3) if self.target != 'lam' else '\\text{?}'}\\,\\text{{m}}\\\\"
            "\\text{{Step 1: Use the wave equation.}} &\\\\"
            "\\text{{The wave speed is related to the frequency and wavelength by the equation:}} &\\\\"
            "v &= f \\lambda\\\\"
            "\\text{{Step 2: Rearrange and substitute the known values to solve for the unknown:}} &\\\\"
            + (
                f"v &= {self.f} \\times {sig_figs(self.lam, 3)}\\\\"
                f"v &= {self.answer}\\,\\text{{m s}}^{{-1}}"
                if self.target == "v" else
                f"f &= \\frac{{v}}{{\\lambda}} = \\frac{{{self.v}}}{{{sig_figs(self.lam, 3)}}}\\\\"
                f"f &= {self.answer}\\,\\text{{Hz}}"
                if self.target == "f" else
                f"\\lambda &= \\frac{{v}}{{f}} = \\frac{{{self.v}}}{{{self.f}}}\\\\"
                f"\\lambda &= {self.answer}\\,\\text{{m}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        A = 1.0
        lam = self.lam
        x_end = 2.5 * lam
        n = 500

        xs = [x_end * i / (n - 1) for i in range(n)]
        ys = [A * math.sin(2 * math.pi * x / lam) for x in xs]

        fig, ax = plt.subplots(figsize=(6.4, 3.0))
        ax.set_xlim(-0.05 * x_end, 1.05 * x_end)
        ax.set_ylim(-2.0, 2.0)
        ax.set_aspect("auto")
        ax.axis("off")

        # Axis line
        ax.plot([0, x_end], [0, 0], linewidth=2, color="black")

        # Wave
        ax.plot(xs, ys, linewidth=2, color="black")

        # Wavelength bracket (use actual λ for spacing)
        x1 = 0.7 * lam
        x2 = 1.8 * lam
        yb = -1.35
        ax.annotate("", xy=(x1, yb), xytext=(x2, yb),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        if self.target == "lam":
            lam_text = "λ = ?"
        else:
            lam_text = f"λ = {sig_figs(self.lam,3)} m"

        ax.text((x1 + x2) / 2, yb - 0.15, lam_text, ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Corner values (two given, one unknown)
        if self.target == "v":
            ax.text(0.02, 0.92, f"f = {self.f} Hz", transform=ax.transAxes,
                    ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(0.98, 0.92, "v = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        elif self.target == "f":
            ax.text(0.02, 0.92, f"v = {self.v} m s⁻¹", transform=ax.transAxes,
                    ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(0.98, 0.92, "f = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(0.02, 0.92, f"v = {self.v} m s⁻¹", transform=ax.transAxes,
                    ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
            ax.text(0.98, 0.92, f"f = {self.f} Hz", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy089:
    """
    Progressive waves: phase difference between two points on a wave.
    Uses:  φ = 2π(Δx/λ)
    Dynamic target: sometimes find phase difference φ (rad), sometimes find separation Δx (m)
    """

    def __init__(self):
        self.target = rnd.choice(["phi", "dx"])

        # Choose λ and a neat fraction of λ for Δx so φ is a neat multiple of π/4
        self.lam = rnd.choice([0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])  # m
        self.k = rnd.randint(1, 7)  # Δx = (k/8)λ  -> φ = kπ/4
        self.dx = (self.k / 8) * self.lam
        self.phi = 2 * math.pi * (self.dx / self.lam)

        if self.target == "phi":
            self.answer = sig_figs(self.phi, 3)
        else:
            self.answer = sig_figs(self.dx, 3)

        self.description = (
            "A snapshot of a progressive wave is shown. The relevant values for points A and B are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Waves"
        self.subtopic = "Progressive waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Wavelength, }} \\lambda &= {sig_figs(self.lam, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Separation, }} \\Delta x &= {sig_figs(self.dx, 3) if self.target != 'dx' else '\\text{?}'}\\,\\text{{m}}\\\\"
            f"\\text{{Phase difference, }} \\phi &= {sig_figs(self.phi, 3) if self.target != 'phi' else '\\text{?}'}\\,\\text{{rad}}\\\\"
            "\\text{{Step 1: Use the relationship between phase difference and path difference.}} &\\\\"
            "\\text{{The phase difference }} \\phi \\text{{ is proportional to the separation }} \\Delta x \\text{{ relative to the wavelength:}} &\\\\"
            "\\phi &= 2\\pi \\left( \\frac{\\Delta x}{\\lambda} \\right)\\\\"
            "\\text{{Step 2: Rearrange and substitute the known values to solve for the unknown:}} &\\\\"
            + (
                f"\\phi &= 2\\pi \\times \\frac{{{sig_figs(self.dx, 3)}}}{{{sig_figs(self.lam, 3)}}}\\\\"
                f"\\phi &= 2\\pi \\times {round(self.dx / self.lam, 10)}\\\\"
                f"\\phi &= {self.answer}\\,\\text{{rad}}"
                if self.target == "phi" else
                f"\\Delta x &= \\frac{{\\phi \\lambda}}{{2\\pi}}\\\\"
                f"\\Delta x &= \\frac{{{sig_figs(self.phi, 3)} \\times {sig_figs(self.lam, 3)}}}{{2\\pi}}\\\\"
                f"\\Delta x &= {self.answer}\\,\\text{{m}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        A = 1.0
        lam = self.lam
        x_end = 2.0 * lam
        n = 500

        xs = [x_end * i / (n - 1) for i in range(n)]
        ys = [A * math.sin(2 * math.pi * x / lam) for x in xs]

        # Pick A and B positions
        xA = 0.30 * lam
        xB = xA + self.dx
        yA = A * math.sin(2 * math.pi * xA / lam)
        yB = A * math.sin(2 * math.pi * xB / lam)

        fig, ax = plt.subplots(figsize=(6.6, 3.2))
        ax.set_xlim(-0.05 * x_end, 1.05 * x_end)
        ax.set_ylim(-2.2, 2.2)
        ax.axis("off")

        # Axis line
        ax.plot([0, x_end], [0, 0], linewidth=2, color="black")

        # Wave
        ax.plot(xs, ys, linewidth=2, color="black")

        # Mark points A and B
        ax.plot([xA, xB], [yA, yB], "ko", markersize=4)
        ax.text(xA, yA + 0.25, "A", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(xB, yB + 0.25, "B", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Δx bracket
        y_dx = -1.35
        ax.annotate("", xy=(xA, y_dx), xytext=(xB, y_dx),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        if self.target == "dx":
            dx_text = "Δx = ?"
        else:
            dx_text = f"Δx = {sig_figs(self.dx,3)} m"
        ax.text((xA + xB) / 2, y_dx - 0.15, dx_text, ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # λ bracket (one full wavelength)
        y_l = -1.85
        ax.annotate("", xy=(0.2 * lam, y_l), xytext=(1.3 * lam, y_l),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text(0.7 * lam, y_l - 0.15, f"λ = {sig_figs(self.lam,3)} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Phase label in corner
        if self.target == "phi":
            ax.text(0.98, 0.92, "φ = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(0.98, 0.92, f"φ = {sig_figs(self.phi,3)} rad", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy090:
    """
    Doppler effect (sound): moving source, stationary observer.
    Dynamic direction: source approaches or recedes.
    Find observed frequency at the observer.
    """

    def __init__(self):
        self.v_sound = 340  # m s^-1 (shown)
        self.direction = rnd.choice(["approaching", "receding"])

        while True:
            self.f0 = rnd.choice([400, 450, 500, 550, 600, 650, 700, 800, 900, 1000, 1100, 1200])  # Hz
            self.vs = rnd.choice([10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 40])  # m s^-1
            if self.vs < 0.3 * self.v_sound:
                break

        if self.direction == "approaching":
            self.f_obs = self.f0 * (self.v_sound / (self.v_sound - self.vs))
        else:
            self.f_obs = self.f0 * (self.v_sound / (self.v_sound + self.vs))

        self.answer = int(round(self.f_obs))

        self.description = (
            "A sound source emits sound of frequency f₀. The source moves as shown and an observer is stationary.\n"
            "All required values are shown in the diagram.\n"
            "Determine the frequency heard by the observer.\n"
            "f = (_) Hz"
        )

        self.topic = "Waves"
        self.subtopic = "Doppler effect for sound waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Source frequency, }} f_0 &= {self.f0}\\,\\text{{Hz}}\\\\"
            f"\\text{{Speed of sound, }} v &= {self.v_sound}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Speed of source, }} v_s &= {self.vs}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Direction of motion: }} &\\text{{{self.direction.capitalize()}}}\\\\"
            "\\text{{Step 1: Identify the Doppler effect formula for a moving source.}} &\\\\"
            "\\text{{The observed frequency }} f_{{obs}} \\text{{ is given by:}} &\\\\"
            "f_{{obs}} &= f_0 \\left( \\frac{v}{v \\mp v_s} \\right)\\\\"
            "\\text{{Step 2: Apply the correct sign based on the direction of motion.}} &\\\\"
            + (
                "\\text{{Since the source is approaching, the denominator is }} (v - v_s): &\\\\"
                f"f_{{obs}} &= {self.f0} \\times \\left( \\frac{{{self.v_sound}}}{{{self.v_sound} - {self.vs}}} \\right)\\\\"
                if self.direction == "approaching" else
                "\\text{{Since the source is receding, the denominator is }} (v + v_s): &\\\\"
                f"f_{{obs}} &= {self.f0} \\times \\left( \\frac{{{self.v_sound}}}{{{self.v_sound} + {self.vs}}} \\right)\\\\"
            ) +
            f"f_{{obs}} &= {self.f0} \\times \\left( \\frac{{{self.v_sound}}}{{{self.v_sound - self.vs if self.direction == 'approaching' else self.v_sound + self.vs}}} \\right)\\\\"
            f"f_{{obs}} &= {round(self.f_obs, 10)}\\,\\text{{Hz}}\\\\"
            f"\\text{{Final Answer}} &= {self.answer}\\,\\text{{Hz}}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 2.9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Baseline
        ax.plot([0.8, 9.2], [1.0, 1.0], linewidth=2, color="black")

        # Source (left) and Observer (right)
        src = patches.Rectangle((1.6, 1.4), 1.4, 1.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(src)
        ax.text(2.3, 2.55, "source", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        obs = patches.Circle((8.2, 1.9), 0.45, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(obs)
        ax.text(8.2, 2.55, "observer", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Source motion arrow
        y_arrow = 3.1
        if self.direction == "approaching":
            ax.annotate("", xy=(4.2, y_arrow), xytext=(2.6, y_arrow),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(4.25, y_arrow, f"vₛ = {self.vs} m s⁻¹", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.annotate("", xy=(1.0, y_arrow), xytext=(2.6, y_arrow),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            ax.text(0.95, y_arrow, f"vₛ = {self.vs} m s⁻¹", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Values in diagram
        ax.text(1.6, 3.7, f"f₀ = {self.f0} Hz", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        # ax.text(9.2, 3.7, "f = ?", ha="right", va="top",
        #         bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        ax.text(9.2, 0.35, f"speed of sound v = {self.v_sound} m s⁻¹", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy091:
    """
    Doppler effect (sound): moving observer, stationary source.
    Dynamic target: find observed frequency f, OR observer speed v_o
    """

    def __init__(self):
        self.v_sound = 340  # m s^-1 (shown)
        self.direction = rnd.choice(["towards", "away"])
        self.target = rnd.choice(["f_obs", "vo"])

        while True:
            self.f0 = rnd.choice([300, 350, 400, 450, 500, 550, 600, 700, 800, 900, 1000])  # Hz
            self.vo = rnd.choice([5, 6, 8, 10, 12, 15, 18, 20, 22, 25])  # m s^-1
            if self.vo < 0.25 * self.v_sound:
                break

        if self.direction == "towards":
            self.f_obs_exact = self.f0 * (self.v_sound + self.vo) / self.v_sound
        else:
            self.f_obs_exact = self.f0 * (self.v_sound - self.vo) / self.v_sound

        self.f_obs = int(round(self.f_obs_exact))

        if self.target == "f_obs":
            self.answer = self.f_obs
        else:
            self.answer = sig_figs(self.vo, 3)

        self.description = (
            "A sound source is stationary and an observer moves as shown.\n"
            "All required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Waves"
        self.subtopic = "Doppler effect for sound waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Source frequency, }} f_0 &= {self.f0}\\,\\text{{Hz}}\\\\"
            f"\\text{{Speed of sound, }} v &= {self.v_sound}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Observer speed, }} v_o &= {self.vo if self.target == 'f_obs' else '\\text{?}'}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Observed frequency, }} f &= {self.f_obs if self.target == 'vo' else '\\text{?}'}\\,\\text{{Hz}}\\\\"
            f"\\text{{Direction of motion: }} &\\text{{Moving {self.direction} the source}}\\\\"
            "\\text{{Step 1: Identify the Doppler effect formula for a moving observer.}} &\\\\"
            "\\text{{The observed frequency }} f \\text{{ is given by:}} &\\\\"
            "f &= f_0 \\left( \\frac{v \\pm v_o}{v} \\right)\\\\"
            "\\text{{Step 2: Apply the correct sign based on the direction of motion.}} &\\\\"
            + (
                "\\text{{Since the observer is moving towards the source, the numerator is }} (v + v_o): &\\\\"
                if self.direction == "towards" else
                "\\text{{Since the observer is moving away from the source, the numerator is }} (v - v_o): &\\\\"
            ) +
            "\\text{{Step 3: Substitute the known values and solve for the unknown.}} &\\\\"
            + (
                f"f &= {self.f0} \\times \\left( \\frac{{{self.v_sound} {'+' if self.direction == 'towards' else '-'} {self.vo}}}{{{self.v_sound}}} \\right)\\\\"
                f"f &= {self.f0} \\times {round((self.v_sound + (self.vo if self.direction == 'towards' else -self.vo)) / self.v_sound, 10)}\\\\"
                f"f &= {round(self.f_obs_exact, 10)}\\,\\text{{Hz}}\\\\"
                if self.target == "f_obs" else
                f"{self.f_obs} &= {self.f0} \\times \\left( \\frac{{{self.v_sound} {'+' if self.direction == 'towards' else '-'} v_o}}{{{self.v_sound}}} \\right)\\\\"
                f"\\frac{{{self.f_obs}}}{{{self.f0}}} &= \\frac{{{self.v_sound} {'+' if self.direction == 'towards' else '-'} v_o}}{{{self.v_sound}}}\\\\"
                f"{round(self.f_obs / self.f0, 10)} \\times {self.v_sound} &= {self.v_sound} {'+' if self.direction == 'towards' else '-'} v_o\\\\"
                f"{round((self.f_obs / self.f0) * self.v_sound, 10)} &= {self.v_sound} {'+' if self.direction == 'towards' else '-'} v_o\\\\"
                f"v_o &= {self.answer}\\,\\text{{m s}}^{{-1}}"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.6, 2.9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Baseline
        ax.plot([0.8, 9.2], [1.0, 1.0], linewidth=2, color="black")

        # Source (left, stationary)
        src = patches.Rectangle((1.6, 1.4), 1.4, 1.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(src)
        ax.text(2.3, 2.55, "source", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Observer (right, moving)
        obs = patches.Circle((8.2, 1.9), 0.45, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(obs)
        ax.text(8.2, 2.55, "observer", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Observer motion arrow
        y_arrow = 3.1
        if self.direction == "towards":
            ax.annotate("", xy=(6.8, y_arrow), xytext=(8.0, y_arrow),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            vo_text = "vₒ = ?" if self.target == "vo" else f"vₒ = {sig_figs(self.vo,3)} m s⁻¹"
            ax.text(6.75, y_arrow, vo_text, ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.annotate("", xy=(9.4, y_arrow), xytext=(8.2, y_arrow),
                        arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
            vo_text = "vₒ = ?" if self.target == "vo" else f"vₒ = {sig_figs(self.vo,3)} m s⁻¹"
            ax.text(9.45, y_arrow, vo_text, ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))

        # Values in diagram
        ax.text(1.6, 3.7, f"f₀ = {self.f0} Hz", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "f_obs":
            ax.text(9.2, 3.7, "f = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(9.2, 3.7, f"f = {self.f_obs} Hz", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(9.2, 0.35, f"speed of sound v = {self.v_sound} m s⁻¹", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy092:
    """
    Doppler effect (sound): source and observer move towards each other.
    Uses: f = f0 * (v + v_o) / (v - v_s)
    Dynamic target: find observed frequency f, OR find source speed v_s
    """

    def __init__(self):
        self.v_sound = 340  # m s^-1 (shown)
        self.target = rnd.choice(["f_obs", "vs"])

        # Choose values and display-friendly results
        while True:
            self.f0 = rnd.choice([400, 450, 500, 550, 600, 650, 700, 800, 900, 1000])  # Hz
            self.vo = rnd.choice([5, 6, 8, 10, 12, 15, 18, 20])  # m s^-1 (observer towards source)
            self.vs_true = rnd.choice([10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 40])  # m s^-1 (source towards observer)

            if self.vo >= 0.25 * self.v_sound or self.vs_true >= 0.3 * self.v_sound:
                continue

            f_calc = self.f0 * (self.v_sound + self.vo) / (self.v_sound - self.vs_true)
            self.f_obs = int(round(f_calc))
            if 350 <= self.f_obs <= 2000:
                break

        if self.target == "f_obs":
            self.answer = self.f_obs
        else:
            # For consistency with what is shown, compute v_s from displayed values
            self.vs = self.v_sound - (self.f0 * (self.v_sound + self.vo) / self.f_obs)
            self.answer = sig_figs(self.vs, 3)

        self.description = (
            "A sound source and an observer move towards each other as shown.\n"
            "All required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Waves"
        self.subtopic = "Doppler effect for sound waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Source frequency, }} f_0 &= {self.f0}\\,\\text{{Hz}}\\\\"
            f"\\text{{Speed of sound, }} v &= {self.v_sound}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Observer speed, }} v_o &= {self.vo}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Source speed, }} v_s &= {self.vs_true if self.target == 'f_obs' else '\\text{?}'}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Observed frequency, }} f &= {self.f_obs if self.target == 'vs' else '\\text{?}'}\\,\\text{{Hz}}\\\\"
            "\\text{{Step 1: Identify the general Doppler effect formula.}} &\\\\"
            "\\text{{When both the source and observer are moving, the observed frequency is:}} &\\\\"
            "f &= f_0 \\left( \\frac{v \\pm v_o}{v \\mp v_s} \\right)\\\\"
            "\\text{{Step 2: Determine the signs for moving towards each other.}} &\\\\"
            "\\text{{Observer moving towards source increases frequency (}} +v_o \\text{{).}} &\\\\"
            "\\text{{Source moving towards observer increases frequency (}} -v_s \\text{{ denominator).}} &\\\\"
            "f &= f_0 \\left( \\frac{v + v_o}{v - v_s} \\right)\\\\"
            "\\text{{Step 3: Substitute the known values and solve for the unknown.}} &\\\\"
            + (
                f"f &= {self.f0} \\times \\left( \\frac{{{self.v_sound} + {self.vo}}}{{{self.v_sound} - {self.vs_true}}} \\right)\\\\"
                f"f &= {self.f0} \\times \\left( \\frac{{{self.v_sound + self.vo}}}{{{self.v_sound - self.vs_true}}} \\right)\\\\"
                f"f &= {round(self.f0 * (self.v_sound + self.vo) / (self.v_sound - self.vs_true), 10)}\\,\\text{{Hz}}\\\\"
                if self.target == "f_obs" else
                f"{self.f_obs} &= {self.f0} \\times \\left( \\frac{{{self.v_sound} + {self.vo}}}{{{self.v_sound} - v_s}} \\right)\\\\"
                f"\\frac{{{self.f_obs}}}{{{self.f0}}} &= \\frac{{{self.v_sound + self.vo}}}{{{self.v_sound} - v_s}}\\\\"
                f"{self.v_sound} - v_s &= \\frac{{{self.f0} \\times {self.v_sound + self.vo}}}{{{self.f_obs}}}\\\\"
                f"{self.v_sound} - v_s &= {round((self.f0 * (self.v_sound + self.vo)) / self.f_obs, 10)}\\\\"
                f"v_s &= {self.v_sound} - {round((self.f0 * (self.v_sound + self.vo)) / self.f_obs, 10)}\\\\"
            ) +
            f"\\\\\\text{{Final Answer}} &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.8, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        ax.plot([0.8, 9.2], [1.0, 1.0], linewidth=2, color="black")

        # Source (left) and observer (right)
        src = patches.Rectangle((1.6, 1.4), 1.4, 1.0, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(src)
        ax.text(2.3, 2.55, "source", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        obs = patches.Circle((8.2, 1.9), 0.45, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(obs)
        ax.text(8.2, 2.55, "observer", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Motion arrows towards each other
        y_arrow = 3.1

        # Source to right
        ax.annotate("", xy=(3.8, y_arrow), xytext=(2.2, y_arrow),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        if self.target == "vs":
            ax.text(3.85, y_arrow, "vₛ = ?", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(3.85, y_arrow, f"vₛ = {self.vs_true} m s⁻¹", ha="left", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Observer to left
        ax.annotate("", xy=(7.1, y_arrow), xytext=(8.2, y_arrow),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(7.05, y_arrow, f"vₒ = {self.vo} m s⁻¹", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Values in diagram
        ax.text(1.6, 3.7, f"f₀ = {self.f0} Hz", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "f_obs":
            ax.text(9.2, 3.7, "f = ?", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(9.2, 3.7, f"f = {self.f_obs} Hz", ha="right", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(9.2, 0.35, f"speed of sound v = {self.v_sound} m s⁻¹", ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy093:
    """
    Polarisation (Malus' law).
    Unpolarised light passes through two polaroids with angle θ between their transmission axes.
    Use: I1 = I0/2 (after first polaroid); I = I1 cos^2 θ
    Dynamic target: find transmitted intensity I, OR angle θ
    """

    def __init__(self):
        self.target = rnd.choice(["I", "theta"])

        # Choose angles with neat cos^2 values
        self.theta = rnd.choice([0, 30, 45, 60])  # degrees
        self.I0 = rnd.choice([16, 24, 32, 40, 48, 64])  # W m^-2 (arbitrary but consistent units)

        self.I1 = self.I0 / 2
        self.I = self.I1 * (math.cos(math.radians(self.theta)) ** 2)

        # Make I display neat
        self.I_disp = float(f"{self.I:.3g}")

        if self.target == "I":
            self.answer = sig_figs(self.I_disp, 3)
        else:
            self.answer = self.theta  # chosen from neat set

        self.description = (
            "Unpolarised light passes through two polaroids. All required values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Waves"
        self.subtopic = "Polarisation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Incident intensity of unpolarised light, }} I_0 &= {self.I0}\\,\\text{{W m}}^{{-2}}\\\\"
            f"\\text{{Angle between transmission axes, }} \\theta &= {self.theta if self.target == 'I' else '\\theta'}^\\circ\\\\"
            "\\text{{Step 1: Calculate intensity after the first polaroid (}} I_1 \\text{{).}} &\\\\"
            "\\text{{When unpolarised light passes through a polaroid, its intensity is halved:}} &\\\\"
            "I_1 &= \\frac{I_0}{2}\\\\"
            f"&= \\frac{{{self.I0}}}{{2}} = {round(self.I1, 10)}\\,\\text{{W m}}^{{-2}}\\\\"
            "\\text{{Step 2: Apply Malus's Law for the second polaroid.}} &\\\\"
            "\\text{{The transmitted intensity }} I \\text{{ is given by:}} &\\\\"
            "I &= I_1 \\cos^2 \\theta\\\\"
            "\\text{{Step 3: Solve for the unknown variable:}} &\\\\"
            + (
                f"I &= {round(self.I1, 10)} \\times \\cos^2({self.theta}^\\circ)\\\\"
                f"I &= {round(self.I1, 10)} \\times {round(math.cos(math.radians(self.theta))**2, 10)}\\\\"
                f"I &= {self.answer}\\,\\text{{W m}}^{{-2}}"
                if self.target == "I" else
                f"{self.I_disp} &= {round(self.I1, 10)} \\times \\cos^2 \\theta\\\\"
                f"\\cos^2 \\theta &= \\frac{{{self.I_disp}}}{{{round(self.I1, 10)}}}\\\\"
                f"\\cos^2 \\theta &= {round(self.I_disp / self.I1, 10)}\\\\"
                f"\\cos \\theta &= \\sqrt{{{round(self.I_disp / self.I1, 10)}}}\\\\"
                f"\\theta &= \\cos^{{-1}}\\left({round(math.sqrt(self.I_disp / self.I1), 10)}\\right)\\\\"
                f"\\theta &= {self.answer}^\\circ"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 2.9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        y = 2.0

        # Incoming light arrow
        ax.annotate("", xy=(3.2, y), xytext=(0.8, y),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(0.8, 3.4, "unpolarised", ha="left", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(0.8, 0.6, f"I₀ = {self.I0} W m⁻²", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Polaroid 1
        p1 = patches.Rectangle((3.3, 1.2), 0.8, 1.6, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(p1)
        ax.text(3.7, 3.1, "P1", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        # Transmission axis of P1 (vertical)
        ax.plot([3.7, 3.7], [1.35, 2.65], linewidth=2, color="black")

        # Polaroid 2
        p2 = patches.Rectangle((5.6, 1.2), 0.8, 1.6, fill=False, linewidth=2, edgecolor="black")
        ax.add_patch(p2)
        ax.text(6.0, 3.1, "P2", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Transmission axis of P2 at angle theta to vertical
        cx, cy = 6.0, 2.0
        L = 0.75
        # angle measured from vertical
        th = math.radians(self.theta)
        dx = L * math.sin(th)
        dy = L * math.cos(th)
        ax.plot([cx - dx, cx + dx], [cy - dy, cy + dy], linewidth=2, color="black")

        # Angle label
        if self.target == "theta":
            ax.text(4.95, 3.55, "θ = ?", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(4.95, 3.55, f"θ = {self.theta}°", ha="center", va="top",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Outgoing light arrow
        ax.annotate("", xy=(9.2, y), xytext=(6.5, y),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Output intensity label
        if self.target == "I":
            ax.text(9.2, 0.6, "I = ?", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(9.2, 0.6, f"I = {self.I_disp} W m⁻²", ha="right", va="center",
                    bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy094:
    """
    Stationary waves (string fixed at both ends).
    Relationships: λ = 2L / n; f = v / λ = n v / (2L)
    Dynamic target: find f, OR λ, OR harmonic number n
    """

    def __init__(self):
        self.target = rnd.choice(["f", "lam", "n"])

        while True:
            self.L = rnd.choice([0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])  # m
            self.v = rnd.choice([80, 100, 120, 150, 180, 200, 220, 250])      # m s^-1
            self.n = rnd.randint(1, 5)

            self.lam = 2 * self.L / self.n
            self.f = (self.n * self.v) / (2 * self.L)

            if 20 <= self.f <= 800 and 0.15 <= self.lam <= 4.0:
                break

        if self.target == "f":
            self.answer = sig_figs(self.f, 3)
        elif self.target == "lam":
            self.answer = sig_figs(self.lam, 3)
        else:
            self.answer = self.n

        self.description = (
            "A stationary wave is set up on a stretched string fixed at both ends. The pattern and values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "Stationary waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length of the string, }} L &= {self.L}\\,\\text{{m}}\\\\"
            f"\\text{{Wave speed, }} v &= {self.v}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Harmonic number, }} n &= {self.n if self.target != 'n' else '\\text{?}'}\\\\"
            f"\\text{{Frequency, }} f &= {sig_figs(self.f, 3) if self.target != 'f' else '\\text{?}'}\\,\\text{{Hz}}\\\\"
            f"\\text{{Wavelength, }} \\lambda &= {sig_figs(self.lam, 3) if self.target != 'lam' else '\\text{?}'}\\,\\text{{m}}\\\\"
            "\\text{{Step 1: Relate wavelength to the length of the string and harmonic number.}} &\\\\"
            "\\text{{For a string fixed at both ends, the length }} L \\text{{ contains }} n \\text{{ half-wavelengths:}} &\\\\"
            "L &= n \\frac{\\lambda}{2} \\implies \\lambda = \\frac{2L}{n}\\\\"
            "\\text{{Step 2: Relate frequency to wave speed and wavelength.}} &\\\\"
            "f &= \\frac{v}{\\lambda} = \\frac{nv}{2L}\\\\"
            "\\text{{Step 3: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"\\lambda &= \\frac{{2 \\times {self.L}}}{{{self.n}}}\\\\"
                f"\\lambda &= {self.answer}\\,\\text{{m}}"
                if self.target == "lam" else
                f"f &= \\frac{{{self.n} \\times {self.v}}}{{2 \\times {self.L}}}\\\\"
                f"f &= {self.answer}\\,\\text{{Hz}}"
                if self.target == "f" else
                f"n &= \\frac{{2L f}}{{v}} = \\frac{{2 \\times {self.L} \\times {sig_figs(self.f, 3)}}}{{{self.v}}}\\\\"
                f"n &= {self.answer}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # String endpoints (fixed)
        x0, x1 = 1.4, 8.8
        y0 = 2.0
        ax.plot([x0, x0], [y0 - 0.7, y0 + 0.7], linewidth=3, color="black")
        ax.plot([x1, x1], [y0 - 0.7, y0 + 0.7], linewidth=3, color="black")

        # Standing wave snapshot: y = y0 + A sin(nπ (x-x0)/Lpix)
        A = 0.65
        npts = 500
        xs = [x0 + (x1 - x0) * i / (npts - 1) for i in range(npts)]
        ys = [y0 + A * math.sin(self.n * math.pi * (x - x0) / (x1 - x0)) for x in xs]
        ax.plot(xs, ys, linewidth=2, color="black")

        # Length bracket
        yL = 0.85
        ax.annotate("", xy=(x0, yL), xytext=(x1, yL),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((x0 + x1) / 2, yL - 0.15, f"L = {self.L} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Values / unknowns (kept in the diagram)
        ax.text(0.02, 0.95, f"v = {self.v} m s⁻¹", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "f":
            ax.text(0.98, 0.95, "f = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"n = {self.n}", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        elif self.target == "lam":
            ax.text(0.98, 0.95, "λ = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"n = {self.n}", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(0.98, 0.95, "n = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"f = {sig_figs(self.f,3)} Hz", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy095:
    """
    Stationary waves (air column): closed at one end, open at the other.
    Resonance condition: L = (2m-1) λ / 4; f = (2m-1) v / (4L)
    Dynamic target: find resonant frequency f, OR tube length L
    """

    def __init__(self):
        self.v = 340  # m s^-1 (speed of sound; shown)
        self.target = rnd.choice(["f", "L"])

        if self.target == "f":
            # Choose L, m then calculate f
            while True:
                self.m = rnd.choice([1, 2, 3])  # mode number
                self.L = rnd.choice([0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 1.00, 1.20])  # m
                self.f = (2 * self.m - 1) * self.v / (4 * self.L)
                if 80 <= self.f <= 1500:
                    break
            self.answer = sig_figs(self.f, 3)
        else:
            # Choose f, m then calculate L (keeps values tidy)
            while True:
                self.m = rnd.choice([1, 2, 3])
                self.f = rnd.choice([170, 200, 255, 300, 340, 400, 425, 510, 600, 680, 850, 1020, 1200])  # Hz
                self.L = (2 * self.m - 1) * self.v / (4 * self.f)
                if 0.20 <= self.L <= 1.50:
                    break
            self.answer = sig_figs(self.L, 3)

        self.description = (
            "A tube is closed at one end and open at the other. The stationary-wave pattern and values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "Stationary waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Speed of sound, }} v &= {self.v}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Mode number, }} m &= {self.m}\\\\"
            f"\\text{{Length of column, }} L &= {sig_figs(self.L, 3) if self.target != 'L' else '\\text{?}'}\\,\\text{{m}}\\\\"
            f"\\text{{Resonant frequency, }} f &= {self.f if self.target != 'f' else '\\text{?}'}\\,\\text{{Hz}}\\\\"
            "\\text{{Step 1: Identify the resonance condition for a tube closed at one end.}} &\\\\"
            "\\text{{For a tube closed at one end, a node exists at the closed end and an}} &\\\\"
            "\\text{{antinode at the open end. The length }} L \\text{{ is an odd multiple of quarter-wavelengths:}} &\\\\"
            "L &= (2m - 1) \\frac{\\lambda}{4}\\\\"
            "\\text{{Step 2: Relate frequency to wave speed and wavelength.}} &\\\\"
            "f &= \\frac{v}{\\lambda} \\implies \\lambda = \\frac{v}{f}\\\\"
            "\\text{{Combining these gives the frequency formula:}} &\\\\"
            "f &= \\frac{(2m - 1)v}{4L}\\\\"
            "\\text{{Step 3: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"f &= \\frac{{(2 \\times {self.m} - 1) \\times {self.v}}}{{4 \\times {sig_figs(self.L, 3)}}}\\\\"
                f"f &= \\frac{{{2 * self.m - 1} \\times {self.v}}}{{{round(4 * self.L, 10)}}}\\\\"
                f"f &= {self.answer}\\,\\text{{Hz}}"
                if self.target == "f" else
                f"L &= \\frac{{(2 \\times {self.m} - 1) \\times {self.v}}}{{4 \\times {self.f}}}\\\\"
                f"L &= \\frac{{{2 * self.m - 1} \\times {self.v}}}{{{4 * self.f}}}\\\\"
                f"L &= {self.answer}\\,\\text{{m}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 2.9))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Tube
        x0, x1 = 2.0, 8.6
        y0, h = 1.6, 1.2
        ax.add_patch(patches.Rectangle((x0, y0), x1 - x0, h, fill=False, linewidth=2, edgecolor="black"))

        # Closed end (left): heavy line
        ax.plot([x0, x0], [y0, y0 + h], linewidth=4, color="black")
        ax.text(x0, y0 - 0.2, "closed", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(x1, y0 - 0.2, "open", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Standing wave in tube: y = mid + A sin(kx), node at closed end
        mid = y0 + h / 2
        A = 0.42
        Lpix = x1 - x0
        k = (2 * self.m - 1) * math.pi / (2 * Lpix)  # shape only (diagrammatic)
        npts = 400
        xs = [x0 + Lpix * i / (npts - 1) for i in range(npts)]
        ys = [mid + A * math.sin(k * (x - x0)) for x in xs]
        ax.plot(xs, ys, linewidth=2, color="black")

        # Length bracket
        yL = 0.85
        ax.annotate("", xy=(x0, yL), xytext=(x1, yL),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        if self.target == "L":
            L_text = "L = ?"
        else:
            L_text = f"L = {sig_figs(self.L,3)} m"
        ax.text((x0 + x1) / 2, yL - 0.15, L_text, ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.25))

        # Mode label + speed of sound
        ax.text(0.02, 0.95, f"mode m = {self.m}", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(0.02, 0.84, f"v = {self.v} m s⁻¹", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Frequency label
        if self.target == "f":
            ax.text(0.98, 0.95, "f = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(0.98, 0.95, f"f = {self.f} Hz", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy096:
    """
    Stationary waves (string): tension / mass per unit length using a harmonic.
    For a string fixed at both ends: f_n = (n / 2L) * sqrt(T / μ)
    Dynamic target: find tension T, OR mass per unit length μ
    """

    def __init__(self):
        self.target = rnd.choice(["T", "mu"])

        while True:
            self.L = rnd.choice([0.60, 0.80, 1.00, 1.20, 1.50])  # m
            self.n = rnd.randint(1, 5)

            self.mu = rnd.choice([0.0020, 0.0030, 0.0040, 0.0050, 0.0060, 0.0080, 0.0100, 0.0120, 0.0150, 0.0200])  # kg m^-1
            self.T = rnd.choice([20, 30, 40, 50, 60, 80, 100, 120, 150, 180, 200, 250, 300])  # N

            self.f = (self.n / (2 * self.L)) * math.sqrt(self.T / self.mu)
            if 30 <= self.f <= 600:
                break

        if self.target == "T":
            self.answer = sig_figs(self.T, 3)
        else:
            self.answer = sig_figs(self.mu, 3)

        self.description = (
            "A stationary wave is produced on a string fixed at both ends. The pattern and values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "Stationary waves"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length of the string, }} L &= {self.L}\\,\\text{{m}}\\\\"
            f"\\text{{Frequency, }} f &= {sig_figs(self.f, 3)}\\,\\text{{Hz}}\\\\"
            f"\\text{{Harmonic number, }} n &= {self.n}\\\\"
            f"\\text{{Tension, }} T &= {sig_figs(self.T, 3) if self.target != 'T' else '\\text{?}'}\\,\\text{{N}}\\\\"
            f"\\text{{Mass per unit length, }} \\mu &= {sig_figs(self.mu, 3) if self.target != 'mu' else '\\text{?}'}\\,\\text{{kg m}}^{{-1}}\\\\"
            "\\text{{Step 1: Use the formula for the frequency of the }} n\\text{{-th harmonic on a string:}} &\\\\"
            "f_n &= \\frac{n}{2L} \\sqrt{\\frac{T}{\\mu}}\\\\"
            "\\text{{Step 2: Rearrange to solve for wave speed (}} v = \\sqrt{T/\\mu} \\text{{) or directly for the target variable:}} &\\\\"
            "v &= \\sqrt{\\frac{T}{\\mu}} = \\frac{2L f}{n}\\\\"
            f"v &= \\frac{{2 \\times {self.L} \\times {sig_figs(self.f, 3)}}}{{{self.n}}}\\\\"
            f"v &= {round(2 * self.L * self.f / self.n, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            "\\text{{Step 3: Solve for the unknown variable using }} v^2 = \\frac{T}{\\mu}: &\\\\"
            + (
                f"T &= \\mu v^2\\\\"
                f"T &= {sig_figs(self.mu, 3)} \\times ({round(2 * self.L * self.f / self.n, 10)})^2\\\\"
                f"T &= {self.answer}\\,\\text{{N}}"
                if self.target == "T" else
                f"\\mu &= \\frac{{T}}{{v^2}}\\\\"
                f"\\mu &= \\frac{{{sig_figs(self.T, 3)}}}{{({round(2 * self.L * self.f / self.n, 10)})^2}}\\\\"
                f"\\mu &= {self.answer}\\,\\text{{kg m}}^{{-1}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 3.0))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # String endpoints
        x0, x1 = 1.4, 8.8
        y0 = 2.0
        ax.plot([x0, x0], [y0 - 0.7, y0 + 0.7], linewidth=3, color="black")
        ax.plot([x1, x1], [y0 - 0.7, y0 + 0.7], linewidth=3, color="black")

        # Standing wave snapshot with n loops
        A = 0.65
        npts = 500
        xs = [x0 + (x1 - x0) * i / (npts - 1) for i in range(npts)]
        ys = [y0 + A * math.sin(self.n * math.pi * (x - x0) / (x1 - x0)) for x in xs]
        ax.plot(xs, ys, linewidth=2, color="black")

        # Length bracket
        yL = 0.85
        ax.annotate("", xy=(x0, yL), xytext=(x1, yL),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((x0 + x1) / 2, yL - 0.15, f"L = {self.L} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Given values in diagram
        ax.text(0.02, 0.95, f"n = {self.n}", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(0.02, 0.84, f"f = {sig_figs(self.f,3)} Hz", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "T":
            ax.text(0.98, 0.95, "T = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"μ = {sig_figs(self.mu,3)} kg m⁻¹", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(0.98, 0.95, "μ = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"T = {sig_figs(self.T,3)} N", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy097:
    """
    Interference (Young double-slit).
    Fringe spacing: w = λD / s
    Dynamic target: find fringe spacing w, OR wavelength λ, OR slit separation s
    """

    def __init__(self):
        self.target = rnd.choice(["w", "lam", "s"])

        while True:
            self.D = rnd.choice([1.0, 1.2, 1.5, 1.8, 2.0, 2.5, 3.0])  # m
            self.s_mm = rnd.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.75, 0.80])  # mm
            self.lam_nm = rnd.choice([420, 450, 480, 500, 520, 550, 580, 600, 620, 650, 680])  # nm

            self.s = self.s_mm * 1e-3       # m
            self.lam = self.lam_nm * 1e-9   # m
            self.w = (self.lam * self.D) / self.s  # m
            self.w_mm = self.w * 1e3

            if 0.6 <= self.w_mm <= 25:
                break

        if self.target == "w":
            self.answer = sig_figs(self.w_mm, 3)
        elif self.target == "lam":
            self.answer = sig_figs(self.lam_nm, 3)
        else:
            self.answer = sig_figs(self.s_mm, 3)

        self.description = (
            "Light passes through a double slit and forms an interference pattern on a screen.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "Interference"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Distance to screen, }} D &= {self.D}\\,\\text{{m}}\\\\"
            f"\\text{{Slit separation, }} s &= {'\\text{?}' if self.target == 's' else f'{sig_figs(self.s_mm, 3)}\\,\\text{{mm}}'} {'= ' + str(self.s) + '\\,\\text{m}' if self.target != 's' else ''}\\\\"
            f"\\text{{Wavelength, }} \\lambda &= {'\\text{?}' if self.target == 'lam' else f'{self.lam_nm}\\,\\text{{nm}}'} {'= ' + str(self.lam) + '\\,\\text{m}' if self.target != 'lam' else ''}\\\\"
            f"\\text{{Fringe spacing, }} w &= {'\\text{?}' if self.target == 'w' else f'{sig_figs(self.w_mm, 3)}\\,\\text{{mm}}'} {'= ' + str(round(self.w, 10)) + '\\,\\text{m}' if self.target != 'w' else ''}\\\\"
            f"\\text{{Step 1: Use the Young double-slit equation.}} &\\\\"
            f"\\text{{The fringe spacing }} w \\text{{ is given by:}} &\\\\"
            f"w &= \\frac{{\\lambda D}}{{s}}\\\\"
            f"\\text{{Step 2: Rearrange and substitute the known values to solve for the unknown:}} &\\\\"
            + (
                f"w &= \\frac{{{self.lam} \\times {self.D}}}{{{self.s}}}\\\\"
                f"w &= {round(self.w, 10)}\\,\\text{{m}}\\\\"
                f"w &= {self.answer}\\,\\text{{mm}}"
                if self.target == "w" else
                f"\\lambda &= \\frac{{w s}}{{D}} = \\frac{{{round(self.w, 10)} \\times {self.s}}}{{{self.D}}}\\\\"
                f"\\lambda &= {round(self.lam, 12)}\\,\\text{{m}}\\\\"
                f"\\lambda &= {self.answer}\\,\\text{{nm}}"
                if self.target == "lam" else
                f"s &= \\frac{{\\lambda D}}{{w}} = \\frac{{{self.lam} \\times {self.D}}}{{{round(self.w, 10)}}}\\\\"
                f"s &= {round(self.s, 10)}\\,\\text{{m}}\\\\"
                f"s &= {self.answer}\\,\\text{{mm}}"
            ) +
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.6, 3.6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        x_slit = 2.4
        x_scr = 10.2

        ax.plot([x_slit, x_slit], [0.9, 5.1], linewidth=6, color="black")

        y_top = 3.9
        y_bot = 2.1
        slit_half = 0.28
        ax.plot([x_slit, x_slit], [y_top - slit_half, y_top + slit_half], linewidth=8, color="white")
        ax.plot([x_slit, x_slit], [y_bot - slit_half, y_bot + slit_half], linewidth=8, color="white")

        ax.text(x_slit, 5.45, "Double slit", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        ax.text(x_slit + 0.25, y_top, "S1", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(x_slit + 0.25, y_bot, "S2", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Slit separation bracket
        ax.annotate("", xy=(x_slit - 1.0, y_top), xytext=(x_slit - 1.0, y_bot),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        s_text = "s = ?" if self.target == "s" else f"s = {sig_figs(self.s_mm,3)} mm"
        ax.text(x_slit - 1.15, (y_top + y_bot) / 2, s_text, ha="right", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # screen
        ax.plot([x_scr, x_scr], [0.9, 5.1], linewidth=6, color="black")
        ax.text(x_scr, 5.45, "Screen", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Distance D (slits to screen)
        yD = 0.55
        ax.annotate("", xy=(x_slit, yD), xytext=(x_scr, yD),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))
        ax.text((x_slit + x_scr) / 2, yD - 0.18, f"D = {self.D} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dy = min(2.2, max(0.70, 0.085 * self.w_mm))
        y_central = 2.8
        y_first = y_central + dy
        y_below = y_central - dy

        dot_style = dict(
            marker="o",
            markersize=7,
            markerfacecolor="white",
            markeredgecolor="black",
            markeredgewidth=2,
            linestyle="None",
            zorder=10
        )

        ax.plot([x_scr], [y_central], **dot_style)
        ax.plot([x_scr], [y_first], **dot_style)
        # ax.plot([x_scr], [y_below], **dot_style)

        # w bracket next to screen
        xw = x_scr + 1.0
        ax.annotate("", xy=(xw, y_first), xytext=(xw, y_central),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.8, color="black"))

        w_text = "w = ?" if self.target == "w" else f"w = {sig_figs(self.w_mm,3)} mm"
        ax.text(xw + 0.2, (y_first + y_central) / 2, w_text, ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Wavelength label
        lam_text = "λ = ?" if self.target == "lam" else f"λ = {self.lam_nm} nm"
        ax.text(1.0, 0.75, lam_text, transform=ax.transAxes,
                ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()


class Phy098:
    """
    Interference (path difference at a point). Two coherent sources S1 and S2 are in phase.
    For a maximum (constructive interference): Δ = |r2 - r1| = mλ
    Dynamic target: find λ, OR m
    """

    def __init__(self):
        self.target = rnd.choice(["lam", "m"])

        while True:
            self.m = rnd.randint(1, 4)
            self.lam = rnd.choice([0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.80])  # m
            self.r1 = rnd.choice([3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0])  # m

            # Make r2 differ by exactly mλ (and keep positive)
            sign = rnd.choice([1, -1])
            self.r2 = self.r1 + sign * (self.m * self.lam)
            if self.r2 > 0.8 and self.r2 < 12.0:
                break

        self.delta = abs(self.r2 - self.r1)

        if self.target == "lam":
            self.answer = sig_figs(self.lam, 3)
        else:
            self.answer = self.m

        self.description = (
            "Two coherent sources S1 and S2 emit waves in phase. Point P is a point of maximum (constructive) interference.\n"
            "The relevant values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "Interference"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance from }} S_1 \\text{{ to }} P, r_1 &= {sig_figs(self.r1, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Distance from }} S_2 \\text{{ to }} P, r_2 &= {sig_figs(self.r2, 3)}\\,\\text{{m}}\\\\"
            f"\\text{{Wavelength, }} \\lambda &= {sig_figs(self.lam, 3) if self.target != 'lam' else '\\text{?}'}\\,\\text{{m}}\\\\"
            f"\\text{{Order number, }} m &= {self.m if self.target != 'm' else '\\text{?}'}\\\\"
            "\\text{{Step 1: Calculate the path difference (}} \\Delta \\text{{) at point }} P. &\\\\"
            "\\Delta &= |r_2 - r_1|\\\\"
            f"&= |{sig_figs(self.r2, 3)} - {sig_figs(self.r1, 3)}|\\\\"
            f"&= {round(self.delta, 10)}\\,\\text{{m}}\\\\"
            "\\text{{Step 2: Apply the condition for constructive interference.}} &\\\\"
            "\\text{{For a maximum, the path difference must be an integer multiple of the wavelength:}} &\\\\"
            "\\Delta &= m \\lambda\\\\"
            "\\text{{Step 3: Substitute the known values and solve for the target variable:}} &\\\\"
            + (
                f"\\lambda &= \\frac{{\\Delta}}{{m}} = \\frac{{{round(self.delta, 10)}}}{{{self.m}}}\\\\"
                f"\\lambda &= {self.answer}\\,\\text{{m}}"
                if self.target == "lam" else
                f"m &= \\frac{{\\Delta}}{{\\lambda}} = \\frac{{{round(self.delta, 10)}}}{{{sig_figs(self.lam, 3)}}}\\\\"
                f"m &= {self.answer}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(6.8, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Source points and point P
        S1 = (1.6, 4.6)
        S2 = (1.6, 1.6)
        P = (8.6, 3.1)

        ax.plot([S1[0], S2[0], P[0]], [S1[1], S2[1], P[1]], "ko", markersize=5)
        ax.text(S1[0] - 0.2, S1[1] + 0.25, "S1", ha="right", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(S2[0] - 0.2, S2[1] - 0.25, "S2", ha="right", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))
        ax.text(P[0] + 0.2, P[1], "P", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.15))

        # Rays
        ax.plot([S1[0], P[0]], [S1[1], P[1]], linewidth=2, color="black")
        ax.plot([S2[0], P[0]], [S2[1], P[1]], linewidth=2, color="black")

        # Label distances (shown in diagram)
        mid1 = ((S1[0] + P[0]) / 2, (S1[1] + P[1]) / 2)
        mid2 = ((S2[0] + P[0]) / 2, (S2[1] + P[1]) / 2)
        ax.text(mid1[0], mid1[1] + 0.25, f"r₁ = {sig_figs(self.r1,3)} m", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(mid2[0], mid2[1] - 0.25, f"r₂ = {sig_figs(self.r2,3)} m", ha="center", va="top",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "lam":
            ax.text(0.98, 0.95, "λ = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"m = {self.m}", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        else:
            ax.text(0.98, 0.95, "m = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
            ax.text(0.98, 0.84, f"λ = {sig_figs(self.lam,3)} m", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy099:
    """
    Diffraction grating: d sinθ = nλ,   with d = 1/(N*1000) if N is lines per mm.
    Dynamic target: find wavelength λ, OR angle θ
    """

    def __init__(self):
        self.target = rnd.choice(["lam", "theta"])

        while True:
            self.N = rnd.choice([300, 400, 500, 600, 800, 1000, 1200])  # lines per mm
            self.n = rnd.choice([1, 2, 3])

            # Choose visible wavelength and compute theta
            self.lam_nm = rnd.choice([400, 420, 450, 480, 500, 520, 550, 580, 600, 620, 650, 680])  # nm
            self.lam = self.lam_nm * 1e-9  # m
            self.d = 1 / (self.N * 1000)   # m

            sin_theta = (self.n * self.lam) / self.d
            if 0 < sin_theta < 1:
                self.theta = math.degrees(math.asin(sin_theta))
                if 10 <= self.theta <= 75:
                    break

        if self.target == "theta":
            self.answer = sig_figs(self.theta, 3)
        else:
            self.answer = sig_figs(self.lam_nm, 3)

        self.description = (
            "Monochromatic light is incident on a diffraction grating. Values are shown in the diagram.\n"
            "Determine the missing quantity.\n"
            "Give your answer in the appropriate form."
        )

        self.topic = "Superposition"
        self.subtopic = "The diffraction grating"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Lines per mm, }} N &= {self.N}\\,\\text{{lines mm}}^{{-1}}\\\\"
            f"\\text{{Order number, }} n &= {self.n}\\\\"
            f"\\text{{Angle of diffraction, }} \\theta &= { '\\text{?}' if self.target == 'theta' else sig_figs(self.theta, 3) }^\\circ\\\\"
            f"\\text{{Wavelength, }} \\lambda &= { '\\text{?}' if self.target == 'lam' else self.lam_nm }\\,\\text{{nm}}\\\\"
            "\\text{{Step 1: Calculate the grating spacing }} d. &\\\\"
            "d &= \\frac{1}{N \\times 10^3}\\\\"
            f"&= \\frac{1}{{{self.N} \\times 1000}}\\\\"
            f"&= {round(self.d, 12)}\\,\\text{{m}}\\\\"
            "\\text{{Step 2: Apply the diffraction grating equation.}} &\\\\"
            "d \\sin \\theta &= n \\lambda\\\\"
            "\\text{{Step 3: Solve for the unknown variable:}} &\\\\"
            + (
                f"\\sin \\theta &= \\frac{{n \\lambda}}{{d}}\\\\"
                f"\\sin \\theta &= \\frac{{{self.n} \\times {self.lam}}}{{{round(self.d, 12)}}}\\\\"
                f"\\sin \\theta &= {round((self.n * self.lam) / self.d, 10)}\\\\"
                f"\\theta &= \\sin^{{-1}}({round((self.n * self.lam) / self.d, 10)})\\\\"
                f"\\theta &= {self.answer}^\\circ"
                if self.target == "theta" else
                f"\\lambda &= \\frac{{d \\sin \\theta}}{{n}}\\\\"
                f"\\lambda &= \\frac{{{round(self.d, 12)} \\times \\sin({sig_figs(self.theta, 3)}^\\circ)}}{{{self.n}}}\\\\"
                f"\\lambda &= {round(self.lam, 12)}\\,\\text{{m}}\\\\"
                f"\\lambda &= {self.answer}\\,\\text{{nm}}"
            ) +
            "\\end{aligned}\\]"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 8})

        fig, ax = plt.subplots(figsize=(6.8, 3.2))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        # Grating as vertical line
        xg = 3.0
        ax.plot([xg, xg], [1.0, 5.0], linewidth=3, color="black")
        ax.text(xg, 5.25, "grating", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Incident ray (along normal)
        y0 = 3.0
        ax.annotate("", xy=(xg, y0), xytext=(0.8, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(0.8, y0 + 0.35, "incident", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Diffracted ray at angle theta
        th = math.radians(self.theta)
        x_max = 9.6
        y_max = 5.6
        y_min = 0.4

        Lx = (x_max - xg) / max(1e-9, math.cos(th))
        if math.sin(th) > 0:
            Ly = (y_max - y0) / max(1e-9, math.sin(th))
        else:
            Ly = (y0 - y_min) / max(1e-9, -math.sin(th))

        L = 0.95 * min(Lx, Ly)

        x2 = xg + L * math.cos(th)
        y2 = y0 + L * math.sin(th)

        ax.annotate("", xy=(x2, y2), xytext=(xg, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        ax.text(xg + 2.8, y0 + 1.6, f"order n = {self.n}", ha="left", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Angle label
        if self.target == "theta":
            th_text = "θ = ?"
        else:
            th_text = f"θ = {sig_figs(self.theta,3)}°"

        ax.text(xg + 0.55, y0 + 0.35, th_text, ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.25))

        # N and lambda labels
        ax.text(0.02, 0.15, f"N = {self.N} lines mm⁻¹", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        if self.target == "lam":
            ax.text(0.98, 0.95, "λ = ?", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.25))
        else:
            ax.text(0.98, 0.95, f"λ = {self.lam_nm} nm", transform=ax.transAxes,
                    ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()


class Phy100:
    """
    Diffraction grating: maximum observable order and its angle.
    Condition: d sinθ = nλ; sinθ <= 1  =>  n_max = floor(d/λ)
    """

    def __init__(self):
        while True:
            self.N = rnd.choice([300, 400, 500, 600, 800, 1000, 1200, 1500])  # lines per mm
            self.lam_nm = rnd.choice([400, 420, 450, 480, 500, 520, 550, 580, 600, 620, 650, 680, 700])  # nm
            self.lam = self.lam_nm * 1e-9
            self.d = 1 / (self.N * 1000)

            self.n_max = int(self.d // self.lam)
            if self.n_max >= 2 and self.n_max <= 6:
                sin_t = (self.n_max * self.lam) / self.d
                if 0 < sin_t <= 1:
                    self.theta_max = math.degrees(math.asin(min(1.0, sin_t)))
                    if 25 <= self.theta_max <= 85:
                        break

        self.answer = f"{self.n_max}, {sig_figs(self.theta_max,3)}"

        self.description = (
            "Monochromatic light is incident on a diffraction grating. Values are shown in the diagram.\n"
            "Determine the highest order maximum that can be observed and the corresponding angle.\n"
            "n_max = (_),  θ_max = (_)°. Answer format (2 values seperated by a comma): (_), (_)"
        )

        self.topic = "Superposition"
        self.subtopic = "The diffraction grating"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Free-form"

        self.reasoning = (
            f"\\begin{{aligned}}"
            f"\\text{{Lines per mm, }} N &= {self.N}\\,\\text{{lines mm}}^{{-1}}\\\\"
            f"\\text{{Wavelength, }} \\lambda &= {self.lam_nm}\\,\\text{{nm}} = {self.lam}\\,\\text{{m}}\\\\"
            f"\\text{{Highest observable order, }} n_{{max}} &= \\text{{?}}\\\\"
            f"\\text{{Angle of highest order, }} \\theta_{{max}} &= \\text{{?}}\\\\"
            f"\\text{{Step 1: Calculate the grating spacing }} d. &\\\\"
            f"d &= \\frac{{1}}{{N \\times 10^3}}\\\\"
            f"&= \\frac{{1}}{{{self.N} \\times 1000}}\\\\"
            f"&= {round(self.d, 12)}\\,\\text{{m}}\\\\"
            f"\\text{{Step 2: Determine the maximum possible order }} n_{{max}}. &\\\\"
            f"\\text{{The condition for a maximum is }} d \\sin \\theta = n \\lambda. \\text{{ Since }} \\sin \\theta \\leq 1: &\\\\"
            f"n &\\leq \\frac{{d}}{{\\lambda}}\\\\"
            f"n &\\leq \\frac{{{round(self.d, 12)}}}{{{self.lam}}}\\\\"
            f"n &\\leq {round(self.d / self.lam, 10)}\\\\"
            f"\\text{{Since }} n \\text{{ must be an integer:}} &\\\\"
            f"n_{{max}} &= {self.n_max}\\\\"
            f"\\text{{Step 3: Calculate the angle }} \\theta_{{max}} \\text{{ for the }} n_{{max}}\\text{{-th order.}} &\\\\"
            f"\\sin \\theta_{{max}} &= \\frac{{n_{{max}} \\lambda}}{{d}}\\\\"
            f"\\sin \\theta_{{max}} &= \\frac{{{self.n_max} \\times {self.lam}}}{{{round(self.d, 12)}}}\\\\"
            f"\\sin \\theta_{{max}} &= {round((self.n_max * self.lam) / self.d, 10)}\\\\"
            f"\\theta_{{max}} &= \\sin^{{-1}}({round((self.n_max * self.lam) / self.d, 10)})\\\\"
            f"\\theta_{{max}} &= {sig_figs(self.theta_max, 3)}^\\circ\\\\"
            f"\\text{{Final Answer}} &= {self.answer}"
            f"\\end{{aligned}}"
        )


    def generate(self, num):
        plt.rcParams.update({"font.size": 9})

        fig, ax = plt.subplots(figsize=(7.6, 3.6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect("equal", adjustable="box")
        ax.axis("off")

        xg = 4.0
        y0 = 3.0
        y_bottom, y_top = 1.0, 5.0

        # grating
        ax.plot([xg, xg], [y_bottom, y_top], linewidth=6, color="black")
        ax.text(xg, y_top + 0.45, "Grating", ha="center", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Incident ray (normal incidence)
        ax.annotate("", xy=(xg, y0), xytext=(1.0, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))
        ax.text(1.0, y0 + 0.35, "incident", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Highest order diffracted ray at theta_max
        th = math.radians(self.theta_max)

        x_max = 11.4
        y_max = 5.6
        y_min = 0.4

        Lx = (x_max - xg) / max(1e-9, math.cos(th))
        if math.sin(th) > 0:
            Ly = (y_max - y0) / max(1e-9, math.sin(th))
        else:
            Ly = (y0 - y_min) / max(1e-9, -math.sin(th))

        L = 0.95 * min(Lx, Ly)
        x2 = xg + L * math.cos(th)
        y2 = y0 + L * math.sin(th)

        ax.annotate("", xy=(x2, y2), xytext=(xg, y0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        # Label near the ray
        xm = xg + 0.55 * (x2 - xg)
        ym = y0 + 0.55 * (y2 - y0)
        ax.text(xm + 0.2, ym + 0.2, "highest order", ha="left", va="bottom",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # Angle arc for theta_max
        r = 1.2
        arc = patches.Arc((xg, y0), 2*r, 2*r, angle=0, theta1=0, theta2=self.theta_max,
                        linewidth=2, color="black")
        ax.add_patch(arc)

        # theta label near the arc
        th_mid = math.radians(self.theta_max / 2)
        ax.text(xg + (r + 0.2) * math.cos(th_mid),
                y0 + (r + 0.2) * math.sin(th_mid),
                "θₘₐₓ", ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=0.1))

        ax.text(0.02, 0.95, f"N = {self.N} lines mm⁻¹", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        ax.text(0.02, 0.84, f"λ = {self.lam_nm} nm", transform=ax.transAxes,
                ha="left", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        # ax.text(0.98, 0.95, "nₘₐₓ = ?", transform=ax.transAxes,
        #         ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))
        # ax.text(0.98, 0.84, "θₘₐₓ = ?", transform=ax.transAxes,
        #         ha="right", va="top", bbox=dict(facecolor="white", edgecolor="none", pad=0.2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.08)
        plt.close()

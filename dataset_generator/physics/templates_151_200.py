import os
from PIL import Image
from physics.helper import *
import random as rnd
import math
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle, Circle, Arc
import numpy as np

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Phy151:
    def __init__(self):
        while True:
            self.distance_mm = rnd.uniform(20.0, 80.0)
            self.voltage = rnd.uniform(100.0, 400.0)
            self.distance = self.distance_mm / 1000

            if self.distance > 0:
                break

        self.field = self.voltage / self.distance
        self.answer = round(self.field, 2)
        self.description = (
            f"Two parallel metal plates are separated by {self.distance_mm:.1f} mm. "
            f"When connected to a {self.voltage:.1f} V d.c. supply, a uniform electric field "
            "is established between the plates. "
            "Calculate the electric field strength between the plates. ( _ ) V m⁻¹"
        )

        self.topic = "Electric fields"
        self.subtopic = "Uniform electric fields"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Electric field between parallel plates}\\\\"
            "E &= \\frac{V}{d}\\\\"
            "\\textbf{Step 2: Convert separation to SI units}\\\\"
            f"d &= {round(self.distance_mm, 10)}\\,\\text{{mm}}\\\\"
            "1\\,\\text{mm} &= 10^{-3}\\,\\text{m}\\\\"
            f"d &= {round(self.distance_mm, 10)} \\times 10^{{-3}}\\\\"
            f"d &= {round(self.distance, 10)}\\,\\text{{m}}\\\\"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"E &= \\frac{{{round(self.voltage, 10)}}}{{{round(self.distance, 10)}}}\\\\"
            f"E &= {round(self.field, 10)}\\,\\text{{V m}}^{{-1}}\\\\"
            f"\\textbf{{Final Answer}} &= {self.answer}\\,\\text{{V m}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({
            "font.size": 11,
            "axes.linewidth": 1.0
        })

        fig, ax = plt.subplots(figsize=(7.2, 4.6))

        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis("off")

        left_plate_x = 5.2
        right_plate_x = 6.8
        plate_bottom = 3.2
        plate_height = 3.0
        plate_width = 0.18

        ax.add_patch(patches.Rectangle(
            (left_plate_x, plate_bottom),
            plate_width,
            plate_height,
            color="black"
        ))

        ax.add_patch(patches.Rectangle(
            (right_plate_x, plate_bottom),
            plate_width,
            plate_height,
            color="black"
        ))

        ax.text(left_plate_x + plate_width/2,
                plate_bottom + plate_height + 0.5,
                "Negative\nplate",
                ha="center")

        ax.text(right_plate_x + plate_width/2,
                plate_bottom + plate_height + 0.5,
                "Positive\nplate",
                ha="center")

        ax.annotate("",
                    xy=(left_plate_x + plate_width, plate_bottom - 0.4),
                    xytext=(right_plate_x, plate_bottom - 0.4),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.2))

        ax.text((left_plate_x + right_plate_x)/2,
                plate_bottom - 0.8,
                 f"{self.distance_mm:.1f} mm",
                ha="center")

        ax.plot([left_plate_x + plate_width/2,
                left_plate_x + plate_width/2],
                [plate_bottom, plate_bottom - 0.5],
                color="black", linewidth=0.8)

        ax.plot([right_plate_x + plate_width/2,
                right_plate_x + plate_width/2],
                [plate_bottom, plate_bottom - 0.5],
                color="black", linewidth=0.8)

        wire_y_bottom = 1.5
        wire_left = 1.0
        wire_right = 11.0

        ax.plot([wire_left, wire_left],
                [plate_bottom + plate_height/2, wire_y_bottom],
                color="black", linewidth=1.2)

        ax.plot([wire_left, left_plate_x],
                [plate_bottom + plate_height/2,
                plate_bottom + plate_height/2],
                color="black", linewidth=1.2)

        ax.plot([right_plate_x + plate_width, wire_right],
                [plate_bottom + plate_height/2,
                plate_bottom + plate_height/2],
                color="black", linewidth=1.2)

        ax.plot([wire_right, wire_right],
                [plate_bottom + plate_height/2, 4.1],
                color="black", linewidth=1.2)

        ax.add_patch(patches.Circle((wire_right, 4.1), 0.12, fill=False))
        ax.add_patch(patches.Circle((wire_right, 3.3), 0.12, fill=False))
        ax.plot([wire_right, wire_right + 0.4],
                [3.9, 3.5],
                color="black", linewidth=1.2)

        ax.plot([wire_right, wire_right],
                [3.3, wire_y_bottom],
                color="black", linewidth=1.2)

        ax.plot([wire_left, wire_right],
                [wire_y_bottom, wire_y_bottom],
                color="black", linewidth=1.2)
        
        supply_width = 3.2
        supply_height = 0.9
        supply_x = (wire_left + wire_right)/2 - supply_width/2
        supply_y = wire_y_bottom - 0.45

        ax.add_patch(patches.Rectangle(
            (supply_x, supply_y),
            supply_width,
            supply_height,
            fill=False,
            linestyle="dashed",
            linewidth=1.0
        ))

        ax.text(supply_x + supply_width/2,
                supply_y + supply_height/2,
                f"{self.voltage:.0f} V dc\nsupply",
                ha="center",
                va="center")
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")

        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)

        plt.close()

class Phy152:
    """
    Force on a charged particle placed between parallel plates.
    Uses E = V/d and F = qE to determine magnitude of electric force.
    """

    def __init__(self):
        while True:
            self.voltage = rnd.uniform(150, 400)          # V
            self.distance_mm = rnd.uniform(30, 80)       # mm
            self.charge_uC = rnd.uniform(-0.5, -0.05)    # μC (negative as shown)

            self.distance = self.distance_mm / 1000      # m
            self.charge = self.charge_uC * 1e-6          # C

            self.E = self.voltage / self.distance        # V m^-1
            self.force = abs(self.charge * self.E)       # magnitude

            if self.force > 0:
                break

        self.answer = round(self.force, 2)

        self.description = (
            f"A small polystyrene ball of charge {self.charge_uC:.2f} μC "
            f"is suspended between two parallel plates separated by "
            f"{self.distance_mm:.0f} mm. The plates are connected to a "
            f"{self.voltage:.0f} V d.c. supply.\n"
            "Calculate the magnitude of the electric force acting on the charge. "
            "( _ ) N"
        )

        self.topic = "Electric fields"
        self.subtopic = "Uniform electric field"
        self.source = "Save My Exam"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Electric field between parallel plates}\\\\ "
            "E &= \\frac{V}{d}\\\\ "
            f"V &= {round(self.voltage,10)}\\,\\text{{V}}\\\\ "
            f"d &= {round(self.distance,10)}\\,\\text{{m}}\\\\ "
            f"E &= \\frac{{{round(self.voltage,10)}}}{{{round(self.distance,10)}}}\\\\ "
            f"E &= {round(self.E,10)}\\,\\text{{V m}}^{{-1}}\\\\ "
            "\\textbf{Step 2: Force on a charge}\\\\ "
            "F &= qE\\\\ "
            f"q &= {round(self.charge,10)}\\,\\text{{C}}\\\\ "
            f"F &= ({round(self.charge,10)})({round(self.E,10)})\\\\ "
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8,5))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis("off")

        plate_height = 4.2
        plate_width = 0.15
        plate_bottom = 3.2

        center_x = 6
        gap = 1.4

        left_x = center_x - gap/2 - plate_width
        right_x = center_x + gap/2

        ax.add_patch(patches.Rectangle((left_x, plate_bottom),
                                    plate_width, plate_height,
                                    color="black"))

        ax.add_patch(patches.Rectangle((right_x, plate_bottom),
                                    plate_width, plate_height,
                                    color="black"))

        ax.text(left_x + plate_width/2,
                plate_bottom + plate_height + 0.6,
                "Negative\nplate",
                ha="center")

        ax.text(right_x + plate_width/2,
                plate_bottom + plate_height + 0.6,
                "Positive\nplate",
                ha="center")
        
        y_mark = plate_bottom - 0.4

        ax.plot([left_x + plate_width/2, left_x + plate_width/2],
                [plate_bottom, y_mark],
                color="black", linewidth=1)

        ax.plot([right_x + plate_width/2, right_x + plate_width/2],
                [plate_bottom, y_mark],
                color="black", linewidth=1)

        ax.annotate("",
            xy=(left_x + plate_width/2, y_mark),
            xytext=(right_x + plate_width/2, y_mark),
            arrowprops=dict(arrowstyle="<->", linewidth=1.2)
        )

        ax.text(center_x, y_mark - 0.4,
                f"{self.distance_mm:.0f} mm",
                ha="center")
        
        ball_x = center_x
        ball_y = plate_bottom + plate_height/2

        ax.add_patch(patches.Circle((ball_x, ball_y),
                                    0.22,
                                    color="black"))

        for dy in [-0.3, 0, 0.3]:
            ax.plot([ball_x - 0.55, ball_x - 0.35],
                    [ball_y + dy, ball_y + dy],
                    color="black", linewidth=0.8)

            ax.plot([ball_x + 0.35, ball_x + 0.55],
                    [ball_y + dy, ball_y + dy],
                    color="black", linewidth=0.8)

        # charge label + leader line
        label_x = ball_x - 1.2
        label_y = ball_y + 1.2

        ax.plot([label_x + 0.2, ball_x - 0.1],
                [label_y - 0.2, ball_y + 0.2],
                color="black", linewidth=0.8)

        ax.text(label_x, label_y,
                f"{self.charge_uC:.2f} μC\ncharge",
                ha="right")

        top_wire_y = plate_bottom + plate_height - 0.2
        bottom_wire_y = 1.6
        left_wire_x = 2
        right_wire_x = 10.2

        ax.plot([left_x, left_wire_x],
                [top_wire_y, top_wire_y],
                color="black", linewidth=1)

        ax.plot([left_wire_x, left_wire_x],
                [top_wire_y, bottom_wire_y],
                color="black", linewidth=1)

        ax.plot([left_wire_x, right_wire_x],
                [bottom_wire_y, bottom_wire_y],
                color="black", linewidth=1)

        ax.plot([right_x + plate_width, right_wire_x],
                [top_wire_y, top_wire_y],
                color="black", linewidth=1)

        ax.plot([right_wire_x, right_wire_x],
                [top_wire_y, 4.2],
                color="black", linewidth=1)

        ax.add_patch(patches.Circle((right_wire_x, 3.9), 0.07, fill=False))
        ax.add_patch(patches.Circle((right_wire_x, 3.3), 0.07, fill=False))

        ax.plot([right_wire_x, right_wire_x + 0.5],
                [3.9, 3.5],
                color="black", linewidth=1)

        ax.plot([right_wire_x, right_wire_x],
                [3.3, bottom_wire_y],
                color="black", linewidth=1)


        supply_width = 2.4
        supply_height = 0.9
        supply_x = center_x - supply_width/2
        supply_y = bottom_wire_y - 0.9

        ax.add_patch(patches.Rectangle(
            (supply_x, supply_y),
            supply_width,
            supply_height,
            fill=False,
            linestyle="dashed"
        ))

        ax.text(center_x,
                supply_y + supply_height/2,
                f"{self.voltage:.0f} V dc\nsupply",
                ha="center",
                va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")

        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)

        plt.close()

class Phy153:
    """
    Coulomb’s law: magnitude of electrostatic force between two point charges.
    Requires unit conversion and substitution into F = k|q1 q2| / r^2.
    """

    def __init__(self):
        self.k = 8.99e9  # N m^2 C^-2

        while True:

            self.q1_nC = rnd.uniform(1.0, 6.0)
            self.q2_nC = rnd.uniform(-8.0, -1.0)

            self.distance_mm = rnd.uniform(5.0, 20.0)

            self.q1 = self.q1_nC * 1e-9
            self.q2 = self.q2_nC * 1e-9
            self.r = self.distance_mm * 1e-3

            self.force = self.k * abs(self.q1 * self.q2) / (self.r ** 2)

            if 1e-6 < self.force < 10:
                break

        self.answer = "{:.2e}".format(self.force)

        self.description = (
            f"Two point charges A and B are separated by {self.distance_mm:.3f} mm in vacuum. "
            f"Charge A is {self.q1_nC:.2f} nC and charge B is {self.q2_nC:.2f} nC. "
            "Determine the magnitude of the force between the two charges. "
            "( _ ) N"
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric force between point charges"
        self.source = "Past Paper"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}}\\\\"
            f"k &= 8.99 \\times 10^{{9}}\\,\\text{{N m^2 C^{{-2}}}}\\\\"
            f"q_1 &= {round(self.q1_nC,10)}\\,\\text{{nC}}\\\\"
            f"q_2 &= {round(self.q2_nC,10)}\\,\\text{{nC}}\\\\"
            f"r &= {round(self.distance_mm,10)}\\,\\text{{mm}}\\\\"
            f"\\\\"
            f"\\text{{Step 1: Convert charges to coulombs}}\\\\"
            f"q_1 &= {round(self.q1_nC,10)} \\times 10^{{-9}}\\,\\text{{C}}\\\\"
            f"&= {round(self.q1,10):.10f}\\,\\text{{C}}\\\\"
            f"q_2 &= {round(self.q2_nC,10)} \\times 10^{{-9}}\\,\\text{{C}}\\\\"
            f"&= {round(self.q2,10):.10f}\\,\\text{{C}}\\\\"
            f"\\\\"
            f"\\text{{Step 2: Convert distance to meters}}\\\\"
            f"r &= {round(self.distance_mm,10)} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            f"&= {round(self.r,10):.10f}\\,\\text{{m}}\\\\"
            f"\\\\"
            f"\\text{{Step 3: Apply Coulomb's Law}}\\\\"
            f"F &= k\\frac{{|q_1 q_2|}}{{r^2}}\\\\"
            f"&= (8.99 \\times 10^{{9}})"
            f"\\frac{{|({round(self.q1,10):.10f})({round(self.q2,10):.10f})|}}"
            f"{{({round(self.r,10):.10f})^2}}\\\\"
            f"\\\\"
            f"\\text{{Step 4: Multiply the charges}}\\\\"
            f"|q_1 q_2| &= {round(abs(self.q1*self.q2),10):.10f}\\\\"
            f"\\\\"
            f"\\text{{Step 5: Square the distance}}\\\\"
            f"r^2 &= {round(self.r**2,10):.10f}\\\\"
            f"\\\\"
            f"\\text{{Step 6: Substitute numerical values}}\\\\"
            f"F &= (8.99 \\times 10^{{9}})"
            f"\\times \\frac{{{round(abs(self.q1*self.q2),10):.10f}}}"
            f"{{{round(self.r**2,10):.10f}}}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 3.5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.axis("off")

        ax.add_patch(
            patches.FancyBboxPatch(
                (0.5, 0.8), 9, 2.4,
                boxstyle="round,pad=0.02",
                edgecolor="none",
                facecolor="#eeeeee"
            )
        )

        xA = 4
        xB = 6
        y = 2

        ax.add_patch(patches.Circle((xA, y), 0.18, color="#555555"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#555555"))

        ax.text(xA, y + 0.35, "A", ha="center", fontsize=11, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=11, weight="bold")

        ax.text(xA, y - 0.45, f"{self.q1_nC:.2f} nC", ha="center")
        ax.text(xB, y - 0.45, f"{self.q2_nC:.2f} nC", ha="center")

        ax.annotate("",
                    xy=(xA, y + 0.6),
                    xytext=(xB, y + 0.6),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.2))

        ax.text((xA + xB)/2, y + 0.85,
                f"{self.distance_mm:.3f} mm",
                ha="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)
        plt.close()


class Phy154:
    """
    Coulomb’s law: magnitude of the electrostatic force between two point charges.
    Requires unit conversion and substitution into F = k|q1 q2| / r^2.
    """

    def __init__(self):

        self.k = 8.99e9  # N m^2 C^-2

        while True:

            # charges in femtocoulomb scale (10^-15 C)
            self.q1_fC = rnd.uniform(1.0, 5.0)
            self.q2_fC = -rnd.uniform(1.0, 5.0)

            # separation in mm
            self.distance_mm = rnd.uniform(3.0, 8.0)

            # convert to SI
            self.q1 = self.q1_fC * 1e-15
            self.q2 = self.q2_fC * 1e-15
            self.r = self.distance_mm * 1e-3

            self.force = self.k * abs(self.q1 * self.q2) / (self.r ** 2)

            if 1e-18 < self.force < 1e-6:
                break

        self.answer = "{:.2e}".format(self.force)

        self.description = (
            f"Two point charges of {self.q1_fC:.2f} × 10⁻¹⁵ C and "
            f"{self.q2_fC:.2f} × 10⁻¹⁵ C are separated by a distance of "
            f"{self.distance_mm:.1f} mm in vacuum. "
            "Calculate the magnitude of the electric force acting on each charge. "
            "( _ ) N"
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric force between point charges"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Coulomb's Law}}\\\\"
            f"F &= k\\frac{{|q_1 q_2|}}{{r^2}}\\\\"
            f"\\\\"
            f"\\text{{Step 2: Convert charges from fC to C}}\\\\"
            f"1\\,\\text{{fC}} &= 10^{{-15}}\\,\\text{{C}}\\\\"
            f"q_1 &= {round(self.q1_fC,10)}\\,\\text{{fC}}\\\\"
            f"&= {round(self.q1_fC,10)} \\times 10^{{-15}}\\,\\text{{C}}\\\\"
            f"q_2 &= {round(self.q2_fC,10)}\\,\\text{{fC}}\\\\"
            f"&= {round(self.q2_fC,10)} \\times 10^{{-15}}\\,\\text{{C}}\\\\"
            f"\\\\"
            f"\\text{{Step 3: Convert distance to meters}}\\\\"
            f"1\\,\\text{{mm}} &= 10^{{-3}}\\,\\text{{m}}\\\\"
            f"r &= {round(self.distance_mm,10)}\\,\\text{{mm}}\\\\"
            f"&= {round(self.distance_mm,10)} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            f"\\\\"
            f"\\text{{Step 4: Multiply charges symbolically}}\\\\"
            f"|q_1 q_2| &= |({round(self.q1_fC,10)} \\times 10^{{-15}})"
            f"({round(self.q2_fC,10)} \\times 10^{{-15}})|\\\\"
            f"&= {round(abs(self.q1_fC*self.q2_fC),10)} \\times 10^{{-30}}\\,\\text{{C}}^2\\\\"
            f"\\\\"
            f"\\text{{Step 5: Square the distance symbolically}}\\\\"
            f"r^2 &= ({round(self.distance_mm,10)} \\times 10^{{-3}})^2\\\\"
            f"&= {round(self.distance_mm**2,10)} \\times 10^{{-6}}\\,\\text{{m}}^2\\\\"
            f"\\\\"
            f"\\text{{Step 6: Substitute into Coulomb's Law}}\\\\"
            f"F &= (8.99 \\times 10^{{9}})"
            f"\\frac{{{round(abs(self.q1_fC*self.q2_fC),10)} \\times 10^{{-30}}}}"
            f"{{{round(self.distance_mm**2,10)} \\times 10^{{-6}}}}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 3.8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.axis("off")

        panel = patches.FancyBboxPatch(
            (0.5, 0.8), 9, 2.4,
            boxstyle="round,pad=0.03",
            edgecolor="none",
            facecolor="#f2f2f2"
        )
        ax.add_patch(panel)

        xA = 4
        xB = 6
        y = 2

        ax.add_patch(patches.Circle((xA, y), 0.18, color="#4a4a4a"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#4a4a4a"))

        ax.text(xA, y + 0.35, "A", ha="center", fontsize=11, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=11, weight="bold")

        ax.text(xA, y - 0.45,
                f"+{self.q1_fC:.2f} ×10⁻¹⁵ C",
                ha="center", fontsize=9)

        ax.text(xB, y - 0.45,
                f"{self.q2_fC:.2f} ×10⁻¹⁵ C",
                ha="center", fontsize=9)

        ax.annotate("",
                    xy=(xA, y + 0.6),
                    xytext=(xB, y + 0.6),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.3))

        ax.text((xA + xB) / 2, y + 0.85,
                f"{self.distance_mm:.1f} mm",
                ha="center", fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)
        plt.close()

class Phy155:
    """
    Electric field at the surface of a charged conducting sphere using
    E = Q / (4π ε0 r^2).
    Multi-step reasoning with unit conversion and algebraic rearrangement.
    """
    def __init__(self):
        self.epsilon0 = 8.85e-12

        self.EA_V_per_cm = rnd.choice([2.0, 2.4, 2.6, 3.0]) * 1e3
        self.EB_V_per_cm = self.EA_V_per_cm / 2
        self.QB_microC = rnd.choice([6.0, 7.0, 7.5, 8.0])

        self.QB = self.QB_microC * 1e-6
        self.EB = self.EB_V_per_cm * 100  # V cm⁻¹ → V m⁻¹

        self.rB = math.sqrt(
            self.QB / (4 * math.pi * self.epsilon0 * self.EB)
        )

        self.rB_cm = self.rB * 100
        self.answer = round(self.rB_cm, 2)

        self.description = (
            f"The field strength at the surface of sphere A is {self.EA_V_per_cm:.1e} V cm⁻¹, "
            f"and the field strength at the surface of sphere B is {self.EB_V_per_cm:.1e} V cm⁻¹.\n"
            f"The magnitude of the charge stored on the surface of sphere B is {self.QB_microC:.1f} μC.\n"
            f"(i) Determine the radius of sphere B."
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric field of a charged conducting sphere"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Electric field at surface of conducting sphere:} &\\\\ "
            "E &= \\frac{Q}{4\\pi \\varepsilon_0 r^2}\\\\ "
            "\\text{Rearranging for } r: &\\\\ "
            "r &= \\sqrt{\\frac{Q}{4\\pi \\varepsilon_0 E}}\\\\ "
            "\\text{Unit conversion:} &\\\\ "
            f"E &= {self.EB_V_per_cm:.1e}\\,\\text{{V cm}}^{{-1}} = {round(self.EB,10)}\\,\\text{{V m}}^{{-1}}\\\\ "
            f"Q &= {self.QB_microC:.1f}\\,\\mu\\text{{C}} = {round(self.QB,10)}\\,\\text{{C}}\\\\ "
            "\\text{Substitute values:} &\\\\ "
            f"r &= \\sqrt{{\\frac{{{round(self.QB,10)}}}"
            f"{{4\\pi ({self.epsilon0}) ({round(self.EB,10)})}}}}\\\\ "
            f"r &= {round(self.rB,10)}\\,\\text{{m}}\\\\ "
            "\\text{Convert to cm:} &\\\\ "
            f"r &= {round(self.rB,10)} \\times 100\\\\ "
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        DESTINATION_FOLDER = "."

        fig, ax = plt.subplots(figsize=(8, 4.5))

        ax.set_xlim(-4, 4)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect("equal")
        ax.axis("off")

        def draw_sphere(center_x, charge_symbol, field_label, field_value):
            sphere = plt.Circle(
                (center_x, 0), 0.9,
                facecolor="#d9d9d9",
                edgecolor="#666666",
                linewidth=2
            )
            ax.add_patch(sphere)

            ax.text(
                center_x, 0,
                charge_symbol,
                ha="center",
                va="center",
                fontsize=22,
                weight="bold",
                color="#cc0000" if charge_symbol == "+" else "#1f77b4"
            )

            angles = np.linspace(0, 2*np.pi, 14, endpoint=False)
            for theta in angles:
                x_start = center_x + 0.9 * np.cos(theta)
                y_start = 0.9 * np.sin(theta)
                x_end = center_x + 1.6 * np.cos(theta)
                y_end = 1.6 * np.sin(theta)

                ax.annotate(
                    "",
                    xy=(x_end, y_end),
                    xytext=(x_start, y_start),
                    arrowprops=dict(
                        arrowstyle="->",
                        linewidth=1.6,
                        color="#f1c232"
                    )
                )

            ax.text(
                center_x, -1.8,
                f"{field_value:.1e} V cm$^{{-1}}$",
                ha="center",
                fontsize=11
            )

            if field_label:
                ax.text(
                    center_x, -2.1,
                    field_label,
                    ha="center",
                    fontsize=11
                )

        draw_sphere(-2.2, "+", "", self.EA_V_per_cm)
        draw_sphere(2.2, "−", f"Q = {self.QB_microC:.1f} μC", self.EB_V_per_cm)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)
        plt.close()

class Phy156:
    """
    Rutherford alpha-particle scattering: closest distance of approach using
    conservation of kinetic energy and electrostatic potential energy.
    """
    def __init__(self):
        self.e = 1.60e-19
        self.epsilon0 = 8.85e-12
        self.k = 1 / (4 * math.pi * self.epsilon0)

        self.m_alpha = 6.64e-27
        self.Z = 79

        while True:
            self.v_coeff = rnd.choice([3.0, 3.2, 3.5, 3.8, 4.0])
            self.v = self.v_coeff * 1e7

            self.q_alpha = 2 * self.e
            self.q_nucleus = self.Z * self.e

            self.KE = 0.5 * self.m_alpha * self.v**2
            self.r_min = self.k * self.q_alpha * self.q_nucleus / self.KE

            if 1e-14 < self.r_min < 5e-14:
                break

        self.answer = round(self.r_min * 1e14, 2)

        self.description = (
            f"Calculate the closest distance of approach for a head-on collision between "
            f"an α particle travelling at a speed of {self.v_coeff:.2f} × 10⁷ m s⁻¹ "
            f"and a gold nucleus (proton number Z = {self.Z}).\n"
            f"Assume that the gold nucleus remains stationary during the collision.\n"
            f"r_min = (_) × 10⁻¹⁴ m"
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Save My Exam"
        self.curriculum = "A-Level"

        ke_coeff, ke_power = f"{self.KE:.3e}".split("e")
        ke_power = int(ke_power)

        r_coeff, r_power = f"{self.r_min:.3e}".split("e")
        r_power = int(r_power)

        self.KE_scientific = f"{ke_coeff} \\times 10^{{{ke_power}}}"
        self.r_scientific = f"{r_coeff} \\times 10^{{{r_power}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Initial kinetic energy of the α particle} &\\\\"
            "E_k &= \\frac{1}{2}mv^2\\\\ "
            f"&= \\frac{{1}}{{2}}({self.m_alpha})( {self.v_coeff} \\times 10^7 )^2\\\\ "
            f"&= {self.KE_scientific}\\,\\text{{J}}\\\\ "
            "\\textbf{Step 2: Electrostatic potential energy at closest approach} &\\\\"
            "E_p &= \\frac{1}{4\\pi \\varepsilon_0} \\frac{q_1 q_2}{r_{min}}\\\\ "
            "\\textbf{Step 3: At closest approach } E_k = E_p &\\\\"
            "\\frac{1}{2}mv^2 &= \\frac{1}{4\\pi \\varepsilon_0} \\frac{q_1 q_2}{r_{min}}\\\\ "
            "\\textbf{Step 4: Rearranging for } r_{min} &\\\\"
            "r_{min} &= \\frac{1}{4\\pi \\varepsilon_0} \\frac{q_1 q_2}{E_k}\\\\ "
            f"&= {round(self.k,10)} \\times "
            f"\\frac{{({2*self.e})( {self.Z} \\times {self.e} )}}{{{self.KE_scientific}}}\\\\ "
            f"&= {self.r_scientific}\\,\\text{{m}}\\\\ "
            "\\textbf{Final Answer} &\\\\"
            f"r_{{min}} &= {self.answer} \\times 10^{{-14}}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif"
        })

        fig, ax = plt.subplots(figsize=(7, 4.5))

        ax.set_xlim(-6, 6)
        ax.set_ylim(-3, 3)
        ax.set_aspect("equal")
        ax.axis("off")

        alpha_center = (-4.5, 0)
        nucleus_center = (4.5, 0)

        alpha = plt.Circle(alpha_center, 0.6, facecolor="#e6e6e6", edgecolor="black", linewidth=2.2)
        ax.add_patch(alpha)
        ax.text(alpha_center[0], alpha_center[1], r"$\alpha$", ha="center", va="center", fontsize=18)

        nucleus = plt.Circle(nucleus_center, 1.6, facecolor="#f4d27a", edgecolor="black", linewidth=2.2)
        ax.add_patch(nucleus)
        ax.text(nucleus_center[0], 0.6, r"$\mathrm{Au}$", ha="center", va="center", fontsize=18)
        ax.text(nucleus_center[0], -0.5, r"$Z = 79$", ha="center", va="center", fontsize=15)

        ax.annotate(
            "",
            xy=(1.5, 0),
            xytext=(-3.5, 0),
            arrowprops=dict(arrowstyle="->", linewidth=2.3, color="black")
        )

        ax.text(
            -1.0, 0.8,
            rf"$v = {self.v_coeff:.2f} \times 10^7\,\mathrm{{m\,s^{{-1}}}}$",
            ha="center",
            fontsize=14
        )

        ax.plot(
            [2.0, 2.0],
            [-1.2, 1.2],
            linestyle=(0, (4, 4)),
            linewidth=1.8,
            color="#2b6cb0"
        )

        ax.annotate(
            "",
            xy=(3.0, -1.7),
            xytext=(0.5, -1.7),
            arrowprops=dict(arrowstyle="<->", linewidth=2.2, color="black")
        )

        ax.text(
            1.75, -2.1,
            r"$r_{\min}$",
            ha="center",
            fontsize=15
        )

        ax.annotate(
            "",
            xy=(2.5, -2.6),
            xytext=(1.0, -2.6),
            arrowprops=dict(arrowstyle="<->", linewidth=1.6, color="black")
        )

        ax.text(
            1.75, -2.95,
            "repulsion",
            ha="center",
            fontsize=13
        )

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy157:
    def __init__(self):
        self.k = 8.99e9
        self.e = 1.602e-19

        while True:
            self.r = rnd.uniform(3.5e-15, 8.0e-15)
            if 3e-15 < self.r < 1e-14:
                break

        self.q_alpha = 2 * self.e
        self.q_gold = 79 * self.e
        self.U = self.k * self.q_alpha * self.q_gold / self.r
        self.answer = f"{self.U:.3e}"

        self.description = (
            f"An α-particle $^4_2$He is moving directly towards a stationary gold nucleus $^{{197}}_{{79}}$Au. "
            f"At a distance of {self.r:.2e} m the α-particle momentarily comes to rest. "
            f"Calculate the electric potential energy of the particles at this instant."
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Original"
        self.curriculum = "A-Level"

        def sci_latex(val):
            if val == 0: return "0"
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        lk = sci_latex(self.k)
        le = sci_latex(self.e)
        lr = sci_latex(self.r)
        lqa = sci_latex(self.q_alpha)
        lqg = sci_latex(self.q_gold)
        lu = sci_latex(self.U)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ known\ quantities} \\\\"
            "&k = " + lk + "\\,\\text{N m}^2\\text{C}^{-2} \\\\"
            "&e = " + le + "\\,\\text{C} \\\\"
            "&r = " + lr + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Determine\ charges} \\\\"
            "&q_{\\alpha} = 2e = " + lqa + "\\,\\text{C} \\\\"
            "&q_{Au} = 79e = " + lqg + "\\,\\text{C} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ Potential\ Energy\ Formula} \\\\"
            "&U = \\frac{k q_1 q_2}{r} = \\frac{(" + lk + ")(" + lqa + ")(" + lqg + ")}{" + lr + "} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Result} \\\\"
            "&U = \\mathbf{" + lu + "\\,\\text{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        y = 2.5
        x_alpha = 3
        x_gold = 9

        gold = plt.Circle((x_gold, y), 0.8, color='#f1c40f', alpha=0.3)
        gold_border = plt.Circle((x_gold, y), 0.8, color='#f39c12', fill=False, lw=2)
        ax.add_patch(gold)
        ax.add_patch(gold_border)
        ax.text(x_gold, y, "$^{197}_{79}$Au\n$+79e$", ha='center', va='center', fontweight='bold')

        alpha = plt.Circle((x_alpha, y), 0.4, color='#e74c3c', alpha=0.3)
        alpha_border = plt.Circle((x_alpha, y), 0.4, color='#c0392b', fill=False, lw=2)
        ax.add_patch(alpha)
        ax.add_patch(alpha_border)
        ax.text(x_alpha, y, "α\n$+2e$", ha='center', va='center', fontweight='bold', color='#c0392b')

        ax.annotate("", xy=(x_alpha + 1, y + 1.2), xytext=(x_alpha - 1.5, y + 1.2),
                    arrowprops=dict(arrowstyle="->", color='#2c3e50', lw=1.5))
        ax.text(x_alpha - 0.2, y + 1.5, "$v", ha='center', fontweight='bold')

        ax.annotate("", xy=(x_gold, y - 1.2), xytext=(x_alpha, y - 1.2),
                    arrowprops=dict(arrowstyle="<->", color='black', lw=1.2))
        
        exponent = int(math.floor(math.log10(abs(self.r))))
        mantissa = self.r / (10 ** exponent)
        ax.text((x_alpha + x_gold) / 2, y - 1.6,
                rf"$r = {mantissa:.2f} \times 10^{{{exponent}}}$ m",
                ha='center', va='center', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none'))

        ax.set_title("ALPHA PARTICLE AT DISTANCE OF CLOSEST APPROACH", fontsize=12, fontweight='bold', pad=10)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy158:
    def __init__(self):
        self.mass_alpha = 6.64e-27

        while True:
            self.speed = rnd.uniform(2.0e7, 6.0e7)
            if 1e7 < self.speed < 1e8:
                break

        self.KE = 0.5 * self.mass_alpha * self.speed**2
        self.answer = f"{self.KE:.3e}"

        self.description = (
            f"An α-particle ($^4_2$He$) is travelling at a speed of {self.speed:.2e} m s$^{-1}$. "
            f"Calculate its kinetic energy in Joules (J)."
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci_latex(val):
            if val == 0: return "0"
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        lm = sci_latex(self.mass_alpha)
        lv = sci_latex(self.speed)
        lv2 = sci_latex(self.speed**2)
        lke = sci_latex(self.KE)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ known\ quantities} \\\\"
            "&m = " + lm + "\\,\\text{kg} \\\\"
            "&v = " + lv + "\\,\\text{m s}^{-1} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Kinetic\ Energy\ formula} \\\\"
            "&E_k = \\frac{1}{2} m v^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution\ and\ Calculation} \\\\"
            "&E_k = 0.5 \\times (" + lm + ") \\times (" + lv + ")^2 \\\\"
            "&E_k = 0.5 \\times (" + lm + ") \\times (" + lv2 + ") \\\\"
            "&\\mathbf{Step\ 4:\ Final\ Answer} \\\\"
            "&E_k = \\mathbf{" + lke + "\\,\\text{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        y = 2.5
        x_start = 2
        
        alpha_grad = plt.Circle((x_start, y), 0.6, color='#e74c3c', alpha=0.2)
        alpha_core = plt.Circle((x_start, y), 0.6, color='#c0392b', fill=False, lw=2.5)
        ax.add_patch(alpha_grad)
        ax.add_patch(alpha_core)

        ax.text(x_start, y, r"$\alpha$", ha='center', va='center', fontsize=20, color='#c0392b', fontweight='bold')
        ax.text(x_start, y - 1.2, "$^4_2$He$^{2+}$", ha='center', fontsize=14, fontweight='bold')
        
        ax.annotate("", xy=(10, y), xytext=(x_start + 0.7, y),
                    arrowprops=dict(arrowstyle="fancy", color='#34495e', lw=1, mutation_scale=20))
        
        exponent = int(math.floor(math.log10(abs(self.speed))))
        mantissa = self.speed / (10 ** exponent)
        
        ax.text(6.5, y + 0.8, rf"$v = {mantissa:.2f} \times 10^{{{exponent}}}\,\text{{m s}}^{{-1}}$", 
                ha='center', fontsize=14, fontweight='bold', bbox=dict(facecolor='white', edgecolor='#34495e', boxstyle='round,pad=0.5'))
        
        ax.text(6.5, y - 0.8, f"$m = {self.mass_alpha:.2e}$ kg", ha='center', fontsize=12, style='italic')

        ax.set_title("KINETIC ENERGY OF A HIGH-SPEED ALPHA PARTICLE", fontsize=12, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy159:
    """
    Combined capacitance of two capacitors connected in series
    in a circuit containing a battery, resistor, and switch.
    """

    def __init__(self):
        while True:
            self.C1 = rnd.randint(10, 40) * 1e-6  # F
            self.C2 = rnd.randint(20, 80) * 1e-6  # F
            if self.C1 != self.C2:
                break

        self.R = rnd.randint(2, 8) * 1e3  # ohm
        self.V = rnd.randint(6, 12)  # V

        self.Ceq = 1 / ((1 / self.C1) + (1 / self.C2))
        self.answer = round(self.Ceq * 1e6, 2)  # µF

        self.description = (
            f"Two capacitors of capacitances {self.C1*1e6:.0f} µF and "
            f"{self.C2*1e6:.0f} µF, and a resistor of resistance "
            f"{self.R/1000:.1f} kΩ are connected as shown. "
            f"The battery has an e.m.f of {self.V} V. "
            f"(i) Calculate the combined capacitance of the two capacitors. (_) µF"
        )

        self.topic = "Capacitance"
        self.subtopic = "Capacitor and Capacitance"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci(val):
            if abs(val) < 1e-5:
                exponent = int(math.floor(math.log10(abs(val))))
                mantissa = val / (10 ** exponent)
                return f"{mantissa:.3f} \\times 10^{{{exponent}}}"
            else:
                return f"{round(val,10)}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"C_1 &= {sci(self.C1)}\\,\\text{{F}}\\\\"
            f"C_2 &= {sci(self.C2)}\\,\\text{{F}}\\\\[6pt]"
            "\\textbf{Step 2: Formula for capacitors in series}\\\\"
            "\\frac{1}{C_{eq}} &= \\frac{1}{C_1} + \\frac{1}{C_2}\\\\[6pt]"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"\\frac{{1}}{{C_{{eq}}}} &= "
            f"\\frac{{1}}{{{sci(self.C1)}}} + "
            f"\\frac{{1}}{{{sci(self.C2)}}}\\\\[6pt]"
            "\\textbf{Step 4: Compute equivalent capacitance}\\\\"
            f"C_{{eq}} &= {sci(self.Ceq)}\\,\\text{{F}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"C_{{eq}} &= {self.answer}\\,\\mu\\text{{F}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        ax.plot([2, 2], [6, 2], linewidth=2, color = "black")

        ax.plot([2, 5], [6, 6], linewidth=2, color = "black")

        ax.plot([5, 5], [5.4, 6.6], linewidth=2, color = "black")
        ax.plot([5.5, 5.5], [5.2, 6.8], linewidth=2, color = "black")
        ax.plot([5.5, 8], [6, 6], linewidth=2, color = "black")
        ax.text(5.25, 7, f"{self.V} V", ha='center', fontsize=12)
        ax.text(8.2, 6.2, "P", fontsize=12)

        ax.plot([8, 10], [6, 4.8], linewidth=2, color = "black")
        ax.plot([10, 12], [4.8, 4.8], linewidth=2, color = "black")
        ax.text(9.2, 5.2, "S", fontsize=12)

        # RIGHT VERTICAL WIRE
        ax.plot([12, 12], [4.8, 2], linewidth=2, color = "black")

        # BOTTOM WIRE WITH CAPACITORS
        ax.plot([12, 9], [2, 2], linewidth=2, color = "black")

        # Capacitor C2
        ax.plot([9, 9], [1.7, 2.3], linewidth=2, color = "black")
        ax.plot([9.5, 9.5], [1.7, 2.3], linewidth=2, color = "black")
        ax.text(9.25, 1.2, f"{self.C2*1e6:.0f} µF", ha='center', fontsize=12)

        ax.plot([9.5, 6], [2, 2], linewidth=2, color = "black")

        # Capacitor C1
        ax.plot([6, 6], [1.7, 2.3], linewidth=2, color = "black")
        ax.plot([6.5, 6.5], [1.7, 2.3], linewidth=2, color = "black")
        ax.text(6.25, 1.2, f"{self.C1*1e6:.0f} µF", ha='center', fontsize=12)

        ax.plot([6.5, 2], [2, 2], linewidth=2, color = "black")

        # RESISTOR BRANCH
        ax.plot([2, 4], [4.5, 4.5], linewidth=2,color = "black")
        ax.add_patch(plt.Rectangle((4, 4.3), 2, 0.4,
                                   fill=False, linewidth=2))
        ax.text(5, 4.9, f"{self.R/1000:.1f} kΩ",
                ha='center', fontsize=12)

        ax.plot([6, 8], [4.5, 4.5], linewidth=2, color = "black")
        ax.text(8.2, 4.7, "Q", fontsize=12)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy160:
    """
    Charge on a capacitor connected in parallel to a battery.
    """

    def __init__(self):
        while True:
            self.Cx = rnd.randint(10, 40) * 1e-6
            self.Cy = rnd.randint(50, 120) * 1e-6
            self.V = rnd.choice([6.0, 9.0, 12.0])
            if self.Cx != self.Cy:
                break

        self.Qx = self.Cx * self.V
        self.answer = round(self.Qx, 2)

        self.description = (
            f"Two capacitors, X and Y, of capacitance "
            f"{self.Cx*1e6:.1f} µF and {self.Cy*1e6:.1f} µF respectively, "
            f"are connected in parallel to a battery of emf {self.V:.1f} V. "
            f"The plates of both capacitors are separated by a vacuum. "
            f"Determine the charge on capacitor X. (_) C"
        )

        self.topic = "Capacitance"
        self.subtopic = "Capacitor and Capacitance"
        self.source = "Original"
        self.curriculum = "A-Level"
        def sci(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"C_X &= {sci(self.Cx)}\\,\\text{{F}}\\\\"
            f"V &= {round(self.V,10)}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 2: Use capacitor charge formula}\\\\"
            "Q &= CV\\\\[6pt]"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"Q_X &= ({sci(self.Cx)})({round(self.V,10)})\\\\[6pt]"
            "\\textbf{Step 4: Compute charge}\\\\"
            f"Q_X &= {sci(self.Qx)}\\,\\text{{C}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"Q_X &= {sci(self.Qx)}\\,\\text{{C}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        plt.rcParams.update({
            "axes.prop_cycle": plt.cycler(color=["black"]),
            "text.color": "black",
            "axes.edgecolor": "black",
            "figure.facecolor": "white"
        })

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

        lw = 2

      
        ax.plot([3, 9], [6, 6], linewidth=lw, color="black")

        ax.plot([3, 3], [6, 4.5], linewidth=lw, color="black")
        ax.plot([2.7, 3.3], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([2.5, 3.5], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([3, 3], [4.1, 2], linewidth=lw, color="black")
        ax.text(1.8, 4.2, f"{self.V:.1f} V", fontsize=10, color="black")

        ax.plot([3, 9], [2, 2], linewidth=lw, color="black")

        ax.plot([6, 6], [6, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([6, 6], [4.1, 2], linewidth=lw, color="black")
        ax.text(5.7, 4.7, "X", ha="center", fontsize=10, color="black")
        ax.text(5.5, 3.7, f"{self.Cx*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        ax.plot([9, 9], [6, 4.5], linewidth=lw, color="black")
        ax.plot([8.6, 9.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([8.6, 9.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([9, 9], [4.1, 2], linewidth=lw, color="black")
        ax.text(8.7, 4.7, "Y", ha="center", fontsize=10, color="black")
        ax.text(8.5, 3.7, f"{self.Cy*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy161:
    """
    Charge on a capacitor connected in parallel to a battery.
    """

    def __init__(self):
        while True:
            self.Cx = rnd.randint(10, 40) * 1e-6
            self.Cy = rnd.randint(50, 120) * 1e-6
            self.V = rnd.choice([6.0, 9.0, 12.0])
            if self.Cx != self.Cy:
                break

        self.Qy = self.Cy * self.V
        self.answer = round(self.Qy, 2)

        self.description = (
            f"Two capacitors, X and Y, of capacitance "
            f"{self.Cx*1e6:.1f} µF and {self.Cy*1e6:.1f} µF respectively, "
            f"are connected in parallel to a battery of emf {self.V:.1f} V. "
            f"The plates of both capacitors are separated by a vacuum. "
            f"Determine the charge on capacitor Y. (_) C"
        )

        self.topic = "Capacitance"
        self.subtopic = "Capacitors and capacitance"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"C_Y &= {sci(self.Cy)}\\,\\text{{F}}\\\\"
            f"V &= {round(self.V,10)}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 2: Use capacitor charge formula}\\\\"
            "Q &= CV\\\\[6pt]"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"Q_Y &= ({sci(self.Cy)})({round(self.V,10)})\\\\[6pt]"
            "\\textbf{Step 4: Compute charge}\\\\"
            f"Q_Y &= {sci(self.Qy)}\\,\\text{{C}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"Q_Y &= {sci(self.Qy)}\\,\\text{{C}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        plt.rcParams.update({
            "axes.prop_cycle": plt.cycler(color=["black"]),
            "text.color": "black",
            "axes.edgecolor": "black",
            "figure.facecolor": "white"
        })

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

        lw = 2

        ax.plot([3, 9], [6, 6], linewidth=lw, color="black")

        ax.plot([3, 3], [6, 4.5], linewidth=lw, color="black")
        ax.plot([2.7, 3.3], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([2.5, 3.5], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([3, 3], [4.1, 2], linewidth=lw, color="black")
        ax.text(1.8, 4.2, f"{self.V:.1f} V", fontsize=10, color="black")

        ax.plot([3, 9], [2, 2], linewidth=lw, color="black")

        ax.plot([6, 6], [6, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([6, 6], [4.1, 2], linewidth=lw, color="black")
        ax.text(5.7, 4.7, "X", ha="center", fontsize=10, color="black")
        ax.text(5.5, 3.7, f"{self.Cx*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        ax.plot([9, 9], [6, 4.5], linewidth=lw, color="black")
        ax.plot([8.6, 9.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([8.6, 9.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([9, 9], [4.1, 2], linewidth=lw, color="black")
        ax.text(8.7, 4.7, "Y", ha="center", fontsize=10, color="black")
        ax.text(8.5, 3.7, f"{self.Cy*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy162:
    """
    Combined capacitance of two capacitors connected in series
    and total energy stored when fully charged.
    """

    def __init__(self):
        while True:
            self.C1 = rnd.randint(10, 40) * 1e-6  # F
            self.C2 = rnd.randint(20, 80) * 1e-6  # F
            if self.C1 != self.C2:
                break

        self.R = rnd.randint(2, 8) * 1e3  # ohm
        self.V = rnd.randint(6, 12)  # V

        self.Ceq = 1 / ((1 / self.C1) + (1 / self.C2))
        self.energy = 0.5 * self.Ceq * self.V**2

        self.answer = round(self.energy, 2)

        self.description = (
            f"Two capacitors of capacitances {self.C1*1e6:.0f} µF and "
            f"{self.C2*1e6:.0f} µF, and a resistor of resistance "
            f"{self.R/1000:.1f} kΩ are connected as shown. "
            f"The battery has an e.m.f of {self.V} V. "
            f"(i) Calculate the combined capacitance of the two capacitors. "
            f"(ii) Hence determine the total energy stored in the two capacitors. (_) J"
        )

        self.topic = "Capacitance"
        self.subtopic = "Energy Stored in a Capacitor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci(val):
            if val == 0:
                return "0"
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            mantissa_str = f"{mantissa:.3f}".rstrip('0').rstrip('.')
            return f"{mantissa_str} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"C_1 &= {sci(self.C1)}\\,\\text{{F}}\\\\"
            f"C_2 &= {sci(self.C2)}\\,\\text{{F}}\\\\"
            f"V &= {self.V}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 2: Equivalent capacitance (series)}\\\\"
            "\\frac{1}{C_{eq}} &= \\frac{1}{C_1} + \\frac{1}{C_2}\\\\"
            f"C_{{eq}} &= {sci(self.Ceq)}\\,\\text{{F}}\\\\[6pt]"
            "\\textbf{Step 3: Energy stored formula}\\\\"
            "E &= \\frac{1}{2} C_{eq} V^2\\\\[6pt]"
            "\\textbf{Step 4: Substitute numerical values}\\\\"
            f"E &= \\frac{{1}}{{2}}({sci(self.Ceq)})({self.V})^2\\\\[6pt]"
            "\\textbf{Final Answer}\\\\"
            f"E &= {sci(self.energy)}\\,\\text{{J}}\\\\[6pt]"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        # LEFT MAIN VERTICAL WIRE
        ax.plot([2, 2], [6, 2], linewidth=2, color = "black")

        # TOP BRANCH (BATTERY)
        ax.plot([2, 5], [6, 6], linewidth=2, color = "black")

        # Battery plates
        ax.plot([5, 5], [5.4, 6.6], linewidth=2, color = "black")
        ax.plot([5.5, 5.5], [5.2, 6.8], linewidth=2, color = "black")
        ax.plot([5.5, 8], [6, 6], linewidth=2, color = "black")
        ax.text(5.25, 7, f"{self.V} V", ha='center', fontsize=12)
        ax.text(8.2, 6.2, "P", fontsize=12)

        # SWITCH
        ax.plot([8, 10], [6, 4.8], linewidth=2, color = "black")
        ax.plot([10, 12], [4.8, 4.8], linewidth=2, color = "black")
        ax.text(9.2, 5.2, "S", fontsize=12)

        # RIGHT VERTICAL WIRE
        ax.plot([12, 12], [4.8, 2], linewidth=2, color = "black")

        # BOTTOM WIRE WITH CAPACITORS
        ax.plot([12, 9], [2, 2], linewidth=2, color = "black")

        # Capacitor C2
        ax.plot([9, 9], [1.7, 2.3], linewidth=2, color = "black")
        ax.plot([9.5, 9.5], [1.7, 2.3], linewidth=2, color = "black")
        ax.text(9.25, 1.2, f"{self.C2*1e6:.0f} µF", ha='center', fontsize=12)

        ax.plot([9.5, 6], [2, 2], linewidth=2, color = "black")

        # Capacitor C1
        ax.plot([6, 6], [1.7, 2.3], linewidth=2, color = "black")
        ax.plot([6.5, 6.5], [1.7, 2.3], linewidth=2, color = "black")
        ax.text(6.25, 1.2, f"{self.C1*1e6:.0f} µF", ha='center', fontsize=12)

        ax.plot([6.5, 2], [2, 2], linewidth=2, color = "black")

        # RESISTOR BRANCH
        ax.plot([2, 4], [4.5, 4.5], linewidth=2,color = "black")
        ax.add_patch(plt.Rectangle((4, 4.3), 2, 0.4,
                                   fill=False, linewidth=2))
        ax.text(5, 4.9, f"{self.R/1000:.1f} kΩ",
                ha='center', fontsize=12)

        ax.plot([6, 8], [4.5, 4.5], linewidth=2, color = "black")
        ax.text(8.2, 4.7, "Q", fontsize=12)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy163:
    def __init__(self):
        while True:
            self.C = rnd.randint(100, 200) * 1e-6
            self.V0 = rnd.uniform(0.6, 0.9)
            self.t = rnd.randint(20, 40) * 1e-3
            self.tau = rnd.uniform(0.02, 0.06)
            self.Vt = self.V0 * math.exp(-self.t / self.tau)
            if self.Vt > 0:
                break

        self.E0 = 0.5 * self.C * self.V0**2
        self.Et = 0.5 * self.C * self.Vt**2
        self.percent_lost = ((self.E0 - self.Et) / self.E0) * 100
        self.answer = f"{self.percent_lost:.2f}"

        self.description = (
            f"A capacitor of capacitance {self.C*1e6:.0f} µF is initially "
            f"charged to a potential difference of {self.V0:.2f} V. "
            f"It discharges through a fixed resistor. The graph shows the variation with time $t$ "
            f"of the potential difference $V$ across the capacitor. "
            f"Calculate the energy lost by the capacitor during the first {int(self.t*1000)} ms "
            f"as a percentage of the initial energy stored."
        )

        self.topic = "Capacitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci_latex(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        lC = sci_latex(self.C)
        lE0 = sci_latex(self.E0)
        lEt = sci_latex(self.Et)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Initial\ energy\ stored\ (E_0)} \\\\"
            "&E_0 = \\frac{1}{2} C V_0^2 = 0.5 \\times (" + lC + ") \\times (" + f"{self.V0:.3f}" + ")^2 \\\\"
            "&E_0 = " + lE0 + "\\,\\text{J} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Potential\ difference\ at\ t = " + f"{int(self.t*1000)}" + "\\,ms} \\\\"
            "&V = V_0 e^{-t/\\tau} = " + f"{self.V0:.3f}" + " \\times e^{" + f"{-self.t/self.tau:.3f}" + "} \\\\"
            "&V = " + f"{self.Vt:.4f}" + "\\,\\text{V} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Energy\ remaining\ (E_t)} \\\\"
            "&E_t = \\frac{1}{2} C V^2 = 0.5 \\times (" + lC + ") \\times (" + f"{self.Vt:.4f}" + ")^2 \\\\"
            "&E_t = " + lEt + "\\,\\text{J} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Percentage\ energy\ lost} \\\\"
            "&\\%\\,\\text{loss} = \\frac{E_0 - E_t}{E_0} \\times 100 \\\\"
            "&\\%\\,\\text{loss} = \\mathbf{" + self.answer + "\\,\\%}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        
        t_plot = np.linspace(0, 0.05, 500)
        V_plot = self.V0 * np.exp(-t_plot / self.tau)
        
        ax.plot(t_plot * 1000, V_plot, color='black', linewidth=2, label='Discharge curve')
        
        ax.scatter([0], [self.V0], color='red', zorder=5)
        ax.text(1, self.V0, f'$V_0 = {self.V0:.2f}$ V', va='bottom', fontweight='bold')
        
        t_ms = self.t * 1000
        ax.scatter([t_ms], [self.Vt], color='red', zorder=5)
        ax.plot([t_ms, t_ms], [0, self.Vt], color='red', linestyle='--', alpha=0.6)
        ax.plot([0, t_ms], [self.Vt, self.Vt], color='red', linestyle='--', alpha=0.6)
        ax.text(t_ms + 1, self.Vt + 0.02, f'$V_t = {self.Vt:.3f}$ V', fontweight='bold')

        ax.set_xlabel("Time $t$ / ms", fontsize=12, fontweight='bold')
        ax.set_ylabel("Potential Difference $V$ / V", fontsize=12, fontweight='bold')
        ax.set_xlim(0, 50)
        ax.set_ylim(0, self.V0 * 1.1)
        
        ax.grid(True, which='both', linestyle=':', alpha=0.7)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        ax.text(25, self.V0 * 0.8, f'$C = {self.C*1e6:.0f}$ µF\n$\\tau = {self.tau*1000:.1f}$ ms', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy164:
    def __init__(self):
        self.R = rnd.randint(50, 300)
        self.C = rnd.randint(10, 80) * 1e-6
        self.tau = self.R * self.C
        self.answer = f"{self.tau:.5f}"

        self.description = (
            f"The diagram shows a circuit used to investigate the discharge of a capacitor. "
            f"The resistor $R$ has a resistance of {self.R} Ω and the capacitor $C$ "
            f"has a capacitance of {self.C*1e6:.0f} µF. "
            f"Calculate the time constant of this circuit."
        )

        self.topic = "Capacitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Original"
        self.curriculum = "A-Level"

        def sci_latex(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        lC = sci_latex(self.C)
        ltau = sci_latex(self.tau)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Data\ Extraction} \\\\"
            "&R = " + str(self.R) + "\\,\\Omega \\\\"
            "&C = " + lC + "\\,\\text{F} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Formula\ Selection} \\\\"
            "&\\tau = RC \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&\\tau = (" + str(self.R) + ") \\times (" + lC + ") \\\\"
            "&\\tau = \\mathbf{" + ltau + "\\,s}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis("off")

        main_color = '#2d3436'
        accent_color = '#0984e3'
        
        ax.plot([2, 4], [5, 5], color=main_color, lw=2)
        ax.plot([5, 8], [5, 5], color=main_color, lw=2)
        ax.plot([2, 8], [1, 1], color=main_color, lw=2)
        ax.plot([2, 2], [1, 5], color=main_color, lw=2)
        ax.plot([8, 8], [1, 5], color=main_color, lw=2)

        ax.plot([4, 4.8], [5, 5.4], color=main_color, lw=2.5)
        ax.add_patch(plt.Circle((4, 5), 0.1, color=main_color))
        ax.add_patch(plt.Circle((5, 5), 0.1, color=main_color))
        ax.text(4.5, 5.6, "Switch", ha='center', fontsize=10, fontweight='bold')

        res_w, res_h = 2.0, 0.7
        res_x, res_y = 4.0, 0.65
        resistor = patches.Rectangle((res_x, res_y), res_w, res_h, facecolor='white', edgecolor=main_color, lw=2, zorder=3)
        ax.add_patch(resistor)
        ax.text(res_x + res_w/2, res_y - 0.5, f"$R = {self.R}$ Ω", ha='center', fontweight='bold', fontsize=11)

        cap_x = 8.0
        cap_y = 3.0
        gap = 0.25
        ax.add_patch(patches.Rectangle((cap_x-0.5, cap_y-0.5), 1, 1, color='white', zorder=2))
        ax.plot([cap_x-0.5, cap_x+0.5], [cap_y+gap, cap_y+gap], color=main_color, lw=3)
        ax.plot([cap_x-0.5, cap_x+0.5], [cap_y-gap, cap_y-gap], color=main_color, lw=3)
        ax.text(cap_x + 0.8, cap_y, f"$C = {self.C*1e6:.0f}$ µF", va='center', fontweight='bold', fontsize=11)

        ax.annotate('', xy=(2, 3.5), xytext=(2, 2.5), arrowprops=dict(arrowstyle='->', color=accent_color, lw=2))
        ax.text(1.3, 3.0, "Discharge\nCurrent", color=accent_color, fontsize=9, rotation=90, va='center', fontweight='bold')

        ax.set_title("CIRCUIT DIAGRAM: CAPACITOR DISCHARGE", fontsize=13, fontweight='bold', pad=25, color=main_color)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy165:
    """
    Energy stored in a capacitor charged through resistor P
    when switch is in position A.
    """

    def __init__(self):
        # Randomised but sensible values
        self.V = rnd.choice([6.0, 9.0, 12.0])
        self.P = rnd.randint(20, 40) * 1e3     # ohm
        self.Q = rnd.randint(200, 400) * 1e3   # ohm
        self.C = rnd.randint(50, 200) * 1e-6   # F

        # Fully charged → capacitor voltage = supply voltage
        self.energy = 0.5 * self.C * self.V**2
        self.answer = round(self.energy, 4)

        self.description = (
            f"The capacitor is connected to a {self.V:.1f} V power supply. "
            f"Two resistors P and Q are {self.P/1000:.0f} kΩ and "
            f"{self.Q/1000:.0f} kΩ respectively. "
            f"The switch is in position A so that the capacitor is fully charged. "
            f"The capacitance is {self.C*1e6:.0f} µF. "
            f"Estimate the energy stored in the capacitor. (_) J"
        )

        self.topic = "Energy stored in a capacitor"
        self.subtopic = "Capacitance"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            mantissa_str = f"{mantissa:.3f}".rstrip('0').rstrip('.')
            return f"{mantissa_str} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Fully charged capacitor}\\\\"
            "V_C &= V_{supply}\\\\"
            f"V_C &= {self.V:.1f}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 2: Energy formula}\\\\"
            "E &= \\frac{1}{2} C V_C^2\\\\[6pt]"
            "\\textbf{Step 3: Substitute values}\\\\"
            f"E &= \\frac{{1}}{{2}}({sci(self.C)})({self.V:.1f})^2\\\\[6pt]"
            "\\textbf{Step 4: Compute energy}\\\\"
            f"E &= {sci(self.energy)}\\,\\text{{J}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"E &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 4.8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis("off")

        lw = 2
        c = "black"

        y_top = 6.5
        y_cap_top = 4.8
        y_cap_bottom = 4.3
        y_switch = 1.6
        y_supply_top = 4.8
        y_supply_bottom = 3.2

        x_left = 4
        x_cap = 8.5
        x_right = 11
        x_resP_left = 6
        x_resP_right = 8
        x_A = x_cap
        x_B = 10.2

        # TOP WIRE 
        ax.plot([x_left, x_right], [y_top, y_top], lw=lw, color=c)

        # Junction dot
        ax.plot(x_cap, y_top, marker='o', markersize=4, color=c)

        #  LEFT SUPPLY
        ax.plot([x_left, x_left], [y_top, y_supply_top], lw=lw, color=c)

        ax.plot(x_left, y_supply_top, marker='o',
                markersize=6, fillstyle='none', color=c)
        ax.plot(x_left, y_supply_bottom, marker='o',
                markersize=6, fillstyle='none', color=c)

        ax.text(2.8, 4.0, f"{self.V:.1f} V", fontsize=12, color=c)

        ax.plot([x_left, x_left], [y_supply_bottom, y_switch], lw=lw, color=c)

        #  RESISTOR P 
        ax.plot([x_left, x_resP_left], [y_switch, y_switch], lw=lw, color=c)

        ax.add_patch(
            plt.Rectangle((x_resP_left, y_switch - 0.25),
                        2.0, 0.5, fill=False, lw=lw, edgecolor=c)
        )

        ax.text(7, 0.6,
                f"P\n{self.P/1000:.0f} kΩ",
                ha="center", fontsize=11, color=c)

        ax.plot([x_resP_right, x_A], [y_switch, y_switch], lw=lw, color=c)

        # SWITCH 
        # Pivot exactly below capacitor
        ax.plot(x_A, y_switch, marker='o',
                markersize=6, fillstyle='none', color=c)
        ax.text(x_A - 0.1, 0.8, "A", fontsize=11, color=c)

        ax.plot(x_B, y_switch, marker='o',
                markersize=6, fillstyle='none', color=c)
        ax.text(x_B - 0.1, 0.8, "B", fontsize=11, color=c)

        # Switch arm from pivot up to capacitor
        ax.plot([x_A, x_cap], [y_switch, 3.0], lw=lw, color=c)

        # CAPACITOR 
        ax.plot([x_cap, x_cap], [3.0, y_cap_bottom], lw=lw, color=c)

        ax.plot([x_cap - 0.4, x_cap + 0.4],
                [y_cap_bottom, y_cap_bottom], lw=lw, color=c)
        ax.plot([x_cap - 0.4, x_cap + 0.4],
                [y_cap_top, y_cap_top], lw=lw, color=c)

        ax.plot([x_cap, x_cap], [y_cap_top, y_top], lw=lw, color=c)

        # RIGHT SIDE 
        ax.plot([x_right, x_right], [y_top, 3.2], lw=lw, color=c)

        # Resistor Q (thin)
        ax.add_patch(
            plt.Rectangle((x_right - 0.3, 3.2),
                        0.6, 2.0, fill=False, lw=lw, edgecolor=c)
        )

        ax.text(x_right + 0.6, 4.2,
                f"Q\n{self.Q/1000:.0f} kΩ",
                fontsize=11, color=c)

        # Vertical down from resistor
        ax.plot([x_right, x_right], [3.2, 2.5], lw=lw, color=c)

    
        ax.plot([x_right, x_B], [2.5, y_switch], lw=lw, color=c)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy166:
    def __init__(self):
        self.L = rnd.uniform(0.5, 2.0)
        self.I = rnd.uniform(0.3, 2.0)
        self.B = rnd.uniform(0.02, 0.1)
        self.theta_deg = rnd.choice([30, 40, 45, 60])
        self.theta = math.radians(self.theta_deg)

        self.force = self.B * self.I * self.L * math.sin(self.theta)
        self.answer = f"{self.force:.3f}"

        self.description = (
            f"A straight conductor of length {self.L:.2f} m carries a current "
            f"of {self.I:.2f} A. It is placed at an angle of {self.theta_deg}° "
            f"to a uniform magnetic field of flux density {self.B:.3f} T. "
            f"Calculate the magnetic force acting on the conductor."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci_latex(val):
            if abs(val) < 0.01 or abs(val) > 1000:
                exponent = int(math.floor(math.log10(abs(val))))
                mantissa = val / (10 ** exponent)
                return f"{mantissa:.3f} \\times 10^{{{exponent}}}"
            return f"{val:.3f}"

        lB = sci_latex(self.B)
        lI = sci_latex(self.I)
        lL = sci_latex(self.L)
        lF = sci_latex(self.force)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ known\ quantities} \\\\"
            "&B = " + lB + "\\,\\text{T} \\\\"
            "&I = " + lI + "\\,\\text{A} \\\\"
            "&L = " + lL + "\\,\\text{m} \\\\"
            "&\\theta = " + str(self.theta_deg) + "^{\\circ} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ the\ Magnetic\ Force\ Formula} \\\\"
            "&F = B I L \\sin\\theta \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&F = (" + lB + ") \\times (" + lI + ") \\times (" + lL + ") \\times \\sin(" + str(self.theta_deg) + "^{\\circ}) \\\\"
            "&F = \\mathbf{" + lF + "\\,N} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&F = " + self.answer + "\\,\\text{N}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis("off")

        field_color = '#0984e3'
        cond_color = '#d35400'
        c_text = '#2d3436'

        for y in np.linspace(1, 5, 5):
            ax.annotate('', xy=(9.5, y), xytext=(0.5, y),
                        arrowprops=dict(arrowstyle='->', color=field_color, lw=1.5, alpha=0.6))
        ax.text(9.6, 5, "Uniform Magnetic\nField ($B$)", color=field_color, fontweight='bold', va='center')
        ax.text(9.6, 4.2, f"$B = {self.B:.3f}$ T", color=field_color, fontsize=9)

        x0, y0 = 3, 2
        length_scale = 5
        x1 = x0 + length_scale * np.cos(self.theta)
        y1 = y0 + length_scale * np.sin(self.theta)

        ax.plot([x0, x1], [y0, y1], lw=12, color=cond_color, alpha=0.3, solid_capstyle='round', zorder=2)
        ax.plot([x0, x1], [y0, y1], lw=2, color=cond_color, zorder=3)
        
        ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle='-|>', color=cond_color, lw=2, mutation_scale=20))
        
        ax.text((x0+x1)/2 - 0.5, (y0+y1)/2 + 0.5, f"$I = {self.I:.2f}$ A", color=cond_color, fontweight='bold', rotation=self.theta_deg)
        ax.text((x0+x1)/2 + 0.2, (y0+y1)/2 - 0.6, f"$L = {self.L:.2f}$ m", color=c_text, style='italic')

        ax.plot([x0, x0 + 2.5], [y0, y0], color=c_text, lw=1, linestyle='--')
        
        arc_r = 1.2
        arc_angles = np.linspace(0, self.theta, 50)
        ax.plot(x0 + arc_r * np.cos(arc_angles), y0 + arc_r * np.sin(arc_angles), color=c_text, lw=1.5)
        ax.text(x0 + 1.5, y0 + 0.4, f"${self.theta_deg}^\circ$", fontsize=12, fontweight='bold')

        ax.set_title("FORCE ON A CONDUCTOR IN A MAGNETIC FIELD", fontsize=12, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy167:
    def __init__(self):
        self.B = rnd.randint(10, 30) * 1e-3
        self.L = rnd.uniform(0.5, 2.0)
        self.I = rnd.uniform(0.5, 3.0)

        self.force = self.B * self.I * self.L
        self.answer = f"{self.force:.3f}"

        self.description = (
            f"A current-carrying conductor is placed at right angles to a uniform magnetic field "
            f"of flux density {self.B:.3f} T. "
            f"The conductor has a length of {self.L:.2f} m and carries a current of {self.I:.2f} A. "
            f"Calculate the magnetic force acting on the conductor."
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Save My Exam" 
        self.curriculum = "A-Level"

        def sci_latex(val):
            if abs(val) < 0.01:
                exponent = int(math.floor(math.log10(abs(val))))
                mantissa = val / (10 ** exponent)
                return f"{mantissa:.3f} \\times 10^{{{exponent}}}"
            return f"{val:.3f}"

        lB = sci_latex(self.B)
        lI = sci_latex(self.I)
        lL = sci_latex(self.L)
        lF = sci_latex(self.force)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ known\ quantities} \\\\"
            "&B = " + lB + "\\,\\text{T}, \\quad L = " + lL + "\\,\\text{m}, \\quad I = " + lI + "\\,\\text{A} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Formula\ (\\theta = 90^\\circ)} \\\\"
            "&F = BIL \\sin(90^\\circ) = BIL \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&F = (" + lB + ") \\times (" + lI + ") \\times (" + lL + ") \\\\"
            "&F = \\mathbf{" + lF + "\\,N}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis("off")

        field_color = '#0984e3'
        cond_color = '#d35400'

        for y in np.linspace(1, 5, 5):
            ax.annotate('', xy=(9.5, y), xytext=(0.5, y),
                        arrowprops=dict(arrowstyle='->', color=field_color, lw=1.5, alpha=0.5))
        
        ax.text(9.6, 5, "Magnetic Field ($B$)", color=field_color, fontweight='bold')
        ax.text(9.6, 4.5, f"$B = {self.B:.3f}$ T", color=field_color, fontsize=9)

        ax.plot([5, 5], [1, 5], lw=12, color=cond_color, alpha=0.3, solid_capstyle='round', zorder=2)
        ax.plot([5, 5], [1, 5], lw=2.5, color=cond_color, zorder=3)
        
        ax.annotate('', xy=(5, 4.5), xytext=(5, 1.5),
                    arrowprops=dict(arrowstyle='-|>', color=cond_color, lw=2, mutation_scale=20))
        
        ax.text(5.3, 3, f"$I = {self.I:.2f}$ A\n$L = {self.L:.2f}$ m", color=cond_color, fontweight='bold', va='center')
        
        ax.plot([5, 5.5], [1.5, 1.5], color='black', lw=1)
        ax.plot([5.5, 5.5], [1.5, 2], color='black', lw=1)

        ax.set_title("CONDUCTOR AT RIGHT ANGLES TO B-FIELD", fontsize=12, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy168:
    def __init__(self):
        self.B_mT = rnd.randint(10, 25)
        self.B = self.B_mT * 1e-3
        self.L = round(rnd.uniform(0.8, 2.0), 2)
        self.I = round(rnd.uniform(0.5, 3.0), 2)
        self.theta = rnd.choice([15, 30, 45, 60])

        self.force = self.B * self.I * self.L * math.sin(math.radians(self.theta))
        self.answer = f"{self.force:.3f}"

        self.description = (
            f"A conductor of length {self.L} m carrying a current of {self.I} A is placed in a "
            f"uniform magnetic field of flux density {self.B_mT} mT. "
            f"Calculate the force on the conductor when it makes an angle of {self.theta}° with the field."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        lF = f"{self.force:.3e}" if self.force < 0.001 else f"{self.force:.4f}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ units} \\\\"
            "&B = " + str(self.B_mT) + "\\,\\text{mT} = " + f"{self.B:.3f}" + "\\,\\text{T} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Formula} \\\\"
            "&F = BIL \\sin\\theta \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution} \\\\"
            "&F = (" + f"{self.B:.3f}" + ")(" + str(self.I) + ")(" + str(self.L) + ")\\sin(" + str(self.theta) + "^{\\circ}) \\\\"
            "&F = \\mathbf{" + lF + "\\,N}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')

        field_color = '#2980b9'
        for x in np.linspace(2, 8, 6):
            for y in np.linspace(2, 8, 6):
                ax.add_patch(plt.Circle((x, y), 0.2, fill=False, edgecolor=field_color, lw=1))
                ax.text(x, y, "×", color=field_color, ha='center', va='center', fontsize=10, fontweight='bold')
        
        ax.text(5, 8.5, f"Uniform $B = {self.B_mT}$ mT (into page)", color=field_color, ha='center', fontweight='bold')

        angle_rad = math.radians(self.theta)
        length_draw = 5
        x0, y0 = 5 - (length_draw/2)*math.cos(angle_rad), 5 - (length_draw/2)*math.sin(angle_rad)
        x1, y1 = 5 + (length_draw/2)*math.cos(angle_rad), 5 + (length_draw/2)*math.sin(angle_rad)

        ax.plot([x0, x1], [y0, y1], color='#c0392b', lw=3, zorder=5)
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color='#c0392b', lw=2, mutation_scale=20))
        
        ax.text(x0, y0 - 0.5, f"$I = {self.I}$ A\n$L = {self.L}$ m", color='#c0392b', fontweight='bold', ha='right')

        ax.plot([5, 7.5], [5, 5], color='black', lw=1, linestyle='--')
        arc_angles = np.linspace(0, angle_rad, 50)
        ax.plot(5 + 1.2*np.cos(arc_angles), 5 + 1.2*np.sin(arc_angles), color='black', lw=1.5)
        ax.text(6.5, 5.3, f"{self.theta}°", fontsize=12, fontweight='bold')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy169:
    def __init__(self):
        self.B = round(rnd.uniform(0.4, 1.2), 2)
        self.width_cm = rnd.randint(4, 10)
        self.length_cm = rnd.randint(6, 14)
        self.I = round(rnd.uniform(1.0, 5.0), 2)

        self.width = self.width_cm / 100
        self.length = self.length_cm / 100

        self.force = self.B * self.I * self.length
        self.answer = f"{self.force:.2f}"

        self.description = (
            f"A rectangular wire loop ABCD is placed in a uniform magnetic field of flux density $B = {self.B}$ T. "
            f"The loop has a width $BC = {self.width_cm}$ cm and a length $AB = {self.length_cm}$ cm. "
            f"A steady current of $I = {self.I}$ A flows through the loop. "
            f"Calculate the magnitude of the magnetic force acting on side AB."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ units\ to\ SI} \\\\"
            "&L_{AB} = " + str(self.length_cm) + "\\,\\text{cm} = " + f"{self.length:.3f}" + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Identify\ relevant\ values} \\\\"
            "&B = " + f"{self.B:.2f}" + "\\,\\text{T}, \\quad I = " + f"{self.I:.2f}" + "\\,\\text{A} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ the\ magnetic\ force\ formula} \\\\"
            "&\\text{Force on AB is perpendicular to the field:} \\\\"
            "&F = B I L \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Calculation} \\\\"
            "&F = (" + f"{self.B:.2f}" + ") \\times (" + f"{self.I:.2f}" + ") \\times (" + f"{self.length:.3f}" + ") \\\\"
            "&F = \\mathbf{" + f"{float(self.answer):.3f}" + "\\,N} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&F = " + self.answer + "\\,\\text{N}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.set_aspect('equal')
        ax.axis('off')

        field_color = '#3498db'
        loop_color = '#2c3e50'
        label_color = '#e67e22'

        for y in np.linspace(0.8, 7.2, 10):
            ax.annotate('', xy=(13, y), xytext=(1, y),
                        arrowprops=dict(arrowstyle='->', color=field_color, lw=1.2, alpha=0.6))
        
        ax.text(12, 6.5, f"$B = {self.B}$ T", color=field_color, fontweight='bold', fontsize=12)

        A = (4.0, 1.5)
        B = (6.0, 5.5)
        C = (10.0, 5.5)
        D = (8.0, 1.5)

        points = [A, B, C, D]
        for i in range(4):
            p1 = points[i]
            p2 = points[(i+1)%4]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=loop_color, lw=3, zorder=5)
            
            mid_p = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
            dx, dy = p2[0]-p1[0], p2[1]-p1[1]
            ax.annotate("", xy=(mid_p[0]+dx*0.1, mid_p[1]+dy*0.1), 
                        xytext=(mid_p[0]-dx*0.1, mid_p[1]-dy*0.1),
                        arrowprops=dict(arrowstyle="->", color=loop_color, lw=2))

        ax.text(A[0]-0.4, A[1]-0.4, "A", fontweight='bold', fontsize=12)
        ax.text(B[0]-0.4, B[1]+0.4, "B", fontweight='bold', fontsize=12)
        ax.text(C[0]+0.4, C[1]+0.4, "C", fontweight='bold', fontsize=12)
        ax.text(D[0]+0.4, D[1]-0.4, "D", fontweight='bold', fontsize=12)

        ax.text((A[0]+B[0])/2 - 1.2, (A[1]+B[1])/2, f"$L = {self.length_cm}$ cm", 
                rotation=63, va='center', fontweight='bold', fontsize=14)
        ax.text((B[0]+C[0])/2, B[1]+0.5, f"$w = {self.width_cm}$ cm", 
                ha='center', fontweight='bold', fontsize=14)
        ax.text((D[0]+A[0])/2, A[1]-0.5, f"Current $I = {self.I}$ A", 
                ha='center', color=label_color, fontweight='bold', fontsize=14)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), 
                    dpi=300, bbox_inches="tight")
        plt.close()

class Phy170:
    def __init__(self):
        self.m = 9.11e-31
        self.q = 1.60e-19

        self.v_base = rnd.randint(2, 6)
        self.v = self.v_base * 1e6

        self.B_base = rnd.randint(2, 6)
        self.B = self.B_base * 1e-3

        self.r = (self.m * self.v) / (self.B * self.q)
        self.answer = f"{self.r:.3f}"

        self.description = (
            f"An electron enters a uniform magnetic field of flux density $B = {self.B_base} \\times 10^{{-3}}$ T "
            f"with a speed of $v = {self.v_base} \\times 10^6$ m s$^{-1}$ perpendicular to the field. "
            f"Calculate the radius of the circular path of the electron."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a moving charge"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ constants} \\\\"
            "&m_e = 9.11 \\times 10^{-31}\\,\\text{kg}, \\quad e = 1.60 \\times 10^{-19}\\,\\text{C} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Force\ Equilibrium} \\\\"
            "&F_B = F_c \\implies Be v = \\frac{m v^2}{r} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ r} \\\\"
            "&r = \\frac{m v}{B e} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitution} \\\\"
            "&r = \\frac{(9.11 \\times 10^{-31})(" + str(self.v_base) + " \\times 10^6)}{(" + str(self.B_base) + " \\times 10^{-3})(1.60 \\times 10^{-19})} \\\\"
            "&r = \\mathbf{" + self.answer + "\\,m}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        field_color = '#b2bec3'
        for x in np.linspace(-4.5, 4.5, 10):
            for y in np.linspace(-4.5, 4.5, 10):
                ax.text(x, y, "×", color=field_color, ha='center', va='center', alpha=0.5)

        radius_draw = 3.0
        orbit = plt.Circle((0, 0), radius_draw, fill=False, color='#2d3436', lw=1.5, ls='--')
        ax.add_patch(orbit)

        ax.add_patch(plt.Circle((radius_draw, 0), 0.15, color='#d63031', zorder=5))
        ax.text(radius_draw + 0.3, -0.3, "electron ($-e$)", color='#d63031', fontweight='bold', fontsize=9)

        ax.annotate('', xy=(radius_draw, 1.5), xytext=(radius_draw, 0),
                    arrowprops=dict(arrowstyle='->', color='#0984e3', lw=2))
        ax.text(radius_draw + 0.2, 1.5, "$v$", color='#0984e3', fontweight='bold', fontsize=12)

        ax.annotate('', xy=(0.2, 0), xytext=(radius_draw, 0),
                    arrowprops=dict(arrowstyle='->', color='#e17055', lw=2))
        ax.text(1.5, 0.2, f"$v = {self.v_base} \\times 10^6$ m s$^{-1}$", color='black', fontweight='bold', fontsize=12)

        ax.plot([0, 0], [0, -radius_draw], color='black', lw=1)
        ax.text(0.2, -radius_draw/2, "$r$", fontweight='bold', fontsize=12)
        ax.add_patch(plt.Circle((0, 0), 0.05, color='black'))

        ax.text(-4.5, 4.5, f"$B = {self.B_base} \\times 10^{{-3}}$ T", fontweight='bold', color='#636e72')

        ax.set_title("ELECTRON ORBIT IN UNIFORM B-FIELD", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy171:
    def __init__(self):
        self.k = 8.99e9
        self.q_base = rnd.randint(2, 12)
        self.q = self.q_base * 1e-9
        self.r_cm = rnd.randint(5, 25)
        self.r = self.r_cm / 100
        self.E = (self.k * self.q) / (self.r**2)
        self.answer = f"{self.E:.3e}"

        self.description = (
            f"A point charge of $Q = +{self.q_base}$ nC is placed in a vacuum. "
            f"Calculate the electric field strength $E$ at a point $P$ located "
            f"at a distance of ${self.r_cm}$ cm from the charge."
        )
        self.topic, self.subtopic = "Electricity", "Electric fields"
        self.curriculum, self.source = "A-Level", "Original"

        e_val_tex = f"{self.E:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Formula\ for\ Electric\ Field\ Strength} \\\\"
            "&E = \\frac{Q}{4\\pi \\varepsilon_0 r^2} = k \\frac{Q}{r^2} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Substitute\ Values\ (SI\ Units)} \\\\"
            "&k = 8.99 \\times 10^9\\,\\text{N m}^2\\,\\text{C}^{-2} \\\\"
            "&Q = " + str(self.q_base) + " \\times 10^{-9}\\,\\text{C} \\\\"
            "&r = " + str(self.r) + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&E = \\frac{(8.99 \\times 10^9)(" + str(self.q_base) + " \\times 10^{-9})}{(" + str(self.r) + ")^2} \\\\"
            "&E = " + e_val_tex + "\\,\\text{V m}^{-1} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&E = " + self.answer + "\\,\\text{V m}^{-1}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 4), dpi=300)
        ax.set_xlim(-1, 6); ax.set_ylim(-1, 3); ax.axis('off')

        ax.add_patch(plt.Circle((0.5, 1), 0.15, color='#e74c3c', ec='black', zorder=5))
        ax.text(0.5, 0.6, f"$Q = +{self.q_base}$ nC", ha='center', fontweight='bold')

        ax.scatter(4.5, 1, marker='x', color='black', s=100)
        ax.text(4.5, 0.7, "Point $P$", ha='center', fontweight='bold')

        ax.annotate('', xy=(4.5, 1), xytext=(0.65, 1),
                    arrowprops=dict(arrowstyle='<->', color='#34495e', lw=1.5))
        ax.text(2.5, 1.2, f"$r = {self.r_cm}$ cm", ha='center', fontsize=11)

        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            dx, dy = 0.6 * np.cos(angle), 0.6 * np.sin(angle)
            ax.annotate('', xy=(0.5+dx*1.5, 1+dy*1.5), xytext=(0.5+dx, 1+dy),
                        arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1, alpha=0.6))

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        ax.text(0.5, 2.5, "Electric Field of a Point Charge", fontsize=12, fontweight='bold', bbox=props)
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy172:
    def __init__(self):
        self.k = 8.99e9
        self.q = 5.0e-9
        self.dist = 0.10 
        self.E_single = (self.k * self.q) / ((self.dist/2)**2)
        self.E_total = 2 * self.E_single
        self.answer = f"{self.E_total:.3e}"

        self.description = (
            "Two identical point charges, each of $Q = +5.0$ nC, are separated by a distance of $10$ cm in air. "
            "Calculate the magnitude of the net electric field strength at the midpoint between the charges if one charge is replaced by $Q = -5.0$ nC."
        )
        self.topic, self.subtopic = "Electricity", "Electric fields"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Field\ Directions} \\\\"
            "&\\text{Field from } +Q \\text{ points away from it (to the right).} \\\\"
            "&\\text{Field from } -Q \\text{ points towards it (also to the right).} \\\\"
            "&\\text{Net field } E_{net} = E_1 + E_2 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Individual\ Field\ Magnitudes} \\\\"
            "&r = 0.05\\,\\text{m (midpoint)} \\\\"
            "&E = \\frac{8.99 \\times 10^9 \\times 5.0 \\times 10^{-9}}{(0.05)^2} = 17980\\,\\text{V m}^{-1} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Summation} \\\\"
            "&E_{net} = 17980 + 17980 = 35960\\,\\text{V m}^{-1} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&E = 3.60 \\times 10^4\\,\\text{V m}^{-1}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis('off')

        ax.add_patch(plt.Circle((2, 2), 0.2, color='#e74c3c', ec='black'))
        ax.text(2, 2.4, "$+Q$", ha='center', fontweight='bold')
        
        ax.add_patch(plt.Circle((8, 2), 0.2, color='#3498db', ec='black'))
        ax.text(8, 2.4, "$-Q$", ha='center', fontweight='bold')

        ax.scatter(5, 2, marker='|', color='black', s=200)
        ax.text(5, 1.6, "Midpoint", ha='center', style='italic')

        ax.annotate('', xy=(8, 1), xytext=(2, 1), arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(5, 0.7, "Separation $d = 10$ cm", ha='center')

        ax.annotate('', xy=(6, 2), xytext=(5, 2), arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
        ax.annotate('', xy=(6.5, 2.2), xytext=(5.5, 2.2), arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
        ax.text(5.7, 2.5, "$E_{net}$", color='#27ae60', fontweight='bold')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy173:
    def __init__(self):
        self.q_base = rnd.randint(2, 9)
        self.q = self.q_base * 1e-19

        self.v_base = rnd.randint(2, 8)
        self.v = self.v_base * 1e6

        self.B_base = rnd.randint(2, 8)
        self.B = self.B_base * 1e-3

        self.theta = rnd.choice([30, 45, 60, 90])

        self.F = self.q * self.v * self.B * math.sin(math.radians(self.theta))
        self.answer = f"{self.F:.3e}"

        self.description = (
            f"A particle with charge $q = {self.q_base} \\times 10^{{-19}}$ C "
            f"enters a uniform magnetic field $B = {self.B_base} \\times 10^{{-3}}$ T "
            f"moving at a speed $v = {self.v_base} \\times 10^6$ m s$^{-1}$. "
            f"The velocity vector makes an angle of {self.theta}° with the field lines. "
            f"Calculate the magnitude of the magnetic force acting on the particle."
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a moving charge"
        self.curriculum = "A-Level"
        self.source = "Original"
        
        lF = f"{self.F:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Values} \\\\"
            "&q = " + str(self.q_base) + "\\times 10^{-19}\\,\\text{C}, \\quad v = " + str(self.v_base) + "\\times 10^6\\,\\text{m s}^{-1} \\\\"
            "&B = " + str(self.B_base) + "\\times 10^{-3}\\,\\text{T}, \\quad \\theta = " + str(self.theta) + "^{\\circ} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Use\ the\ Lorentz\ Force\ Formula} \\\\"
            "&F = q v B \\sin\\theta \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution} \\\\"
            "&F = (" + str(self.q_base) + "\\times 10^{-19})(" + str(self.v_base) + "\\times 10^6)(" + str(self.B_base) + "\\times 10^{-3}) \\sin(" + str(self.theta) + "^{\\circ}) \\\\"
            "&F = \\mathbf{" + lF + "\\,N} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&F = " + self.answer + "\\,\\text{N}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        field_color = '#3498db'
        particle_color = '#e67e22'
        text_color = '#2c3e50'

        for x in np.linspace(-4, 4, 9):
            for y in np.linspace(-4, 4, 9):
                ax.text(x, y, r"$\times$", color=field_color, ha='center', va='center', fontsize=12, alpha=0.6)
        
        ax.text(3.5, 4.2, f"Uniform $B = {self.B_base} \\times 10^{{-3}}$ T", color=field_color, fontweight='bold', ha='right')
        ax.text(3.5, 3.8, "(into page)", color=field_color, fontsize=9, ha='right')

        angle_rad = np.radians(self.theta)
        v_length = 3.5
        vx = v_length * np.cos(angle_rad)
        vy = v_length * np.sin(angle_rad)

        ax.plot([0, 4.5], [0, 0], color=text_color, lw=1, ls='--', alpha=0.8)
        ax.text(4.6, 0, "Field Axis", color=text_color, fontsize=8, va='center')

        ax.annotate('', xy=(vx, vy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='-|>', color=particle_color, lw=3, mutation_scale=20))
        
        ax.add_patch(plt.Circle((0, 0), 0.25, color=particle_color, zorder=5))
        ax.text(-0.2, -0.6, f"$q = {self.q_base} \\times 10^{{-19}}$ C", ha='center', fontweight='bold', fontsize=10)
        ax.text(vx/2, vy/2 + 0.4, f"$v = {self.v_base} \\times 10^6$ m/s", color=particle_color, rotation=self.theta, fontweight='bold')

        if self.theta > 0:
            arc_r = 1.2
            arc_angles = np.linspace(0, angle_rad, 50)
            ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), color=text_color, lw=1.5)
            ax.text(1.5 * np.cos(angle_rad/2), 1.5 * np.sin(angle_rad/2), f"${self.theta}^\circ$", 
                    fontsize=12, fontweight='bold', color=text_color)

        ax.set_title("FORCE ON A MOVING CHARGE IN MAGNETIC FIELD", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_path, dpi=300, bbox_inches="tight")
        plt.close()


class Phy174:
    """
    Motional emf induced in a conductor.
    """

    def __init__(self):
        self.B = round(rnd.uniform(0.4,1.2),2)
        self.L = round(rnd.uniform(0.2,0.8),2)
        self.v = rnd.randint(5,25)

        self.emf = self.B * self.L * self.v
        self.answer = round(self.emf,2)

        self.description = (
            f"A conductor of length {self.L} m moves with speed {self.v} m s^(-1) "
            f"perpendicular to a magnetic field of {self.B} T. "
            "Calculate the induced emf. (_) V"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a Moving Charge"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify the given values}} &\\\\"
            f"B &= {round(self.B, 10)}\\,\\text{{T}}\\\\"
            f"L &= {round(self.L, 10)}\\,\\text{{m}}\\\\"
            f"v &= {round(self.v, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Step 2: State the formula for motional emf}} &\\\\"
            f"\\mathcal{{E}} &= B L v\\\\"
            f"\\text{{Step 3: Substitute the numeric values}} &\\\\"
            f"\\mathcal{{E}} &= ({round(self.B, 10)}\\,\\text{{T}})({round(self.L, 10)}\\,\\text{{m}})({round(self.v, 10)}\\,\\text{{m s}}^{{-1}})\\\\"
            f"\\text{{Step 4: Calculate the induced emf}} &\\\\"
            f"\\mathcal{{E}} &= {round(self.emf, 10)}\\,\\text{{V}}\\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"\\mathcal{{E}} &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        # 1. Draw Magnetic Field (X marks for 'into the page')
        for x in np.linspace(1, 7, 7):
            for y in np.linspace(1, 4, 4):
                ax.text(x, y, '×', color='blue', alpha=0.5, 
                        ha='center', va='center', fontsize=15)
        ax.text(0.5, 4.5, f"B = {self.B} T", color='blue', fontweight='bold')

        # 2. Draw the Conductor (Rod)
        rod_x = 2.5
        rod_y_start = 1.5
        rod_y_end = 3.5
        # Draw a thick gray line for the rod body
        ax.plot([rod_x, rod_x], [rod_y_start, rod_y_end], 
                color='gray', linewidth=8, solid_capstyle='round', zorder=3)
        # Draw a black outline
        ax.plot([rod_x, rod_x], [rod_y_start, rod_y_end], 
                color='black', linewidth=1, zorder=4)

        # 3. Label Length L
        ax.annotate('', xy=(rod_x - 0.3, rod_y_start), xytext=(rod_x - 0.3, rod_y_end),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(rod_x - 0.8, (rod_y_start + rod_y_end)/2, f"L = {self.L} m", 
                va='center', rotation=90)

        # 4. Draw Velocity Vector
        v_arrow_start = (rod_x, (rod_y_start + rod_y_end)/2)
        ax.quiver(v_arrow_start[0], v_arrow_start[1], 1.5, 0, 
                  angles='xy', scale_units='xy', scale=1, color='red', zorder=5)
        ax.text(rod_x + 0.8, (rod_y_start + rod_y_end)/2 + 0.2, f"v = {self.v} m/s", 
                color='red', fontweight='bold')

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.2
        )
        plt.close()

class Phy175:
    def __init__(self):
        self.N = rnd.randint(50, 300)
        self.dPhi = round(rnd.uniform(0.001, 0.01), 4)
        self.dt = round(rnd.uniform(0.01, 0.05), 3)

        self.emf = self.N * (self.dPhi / self.dt)
        self.answer = f"{self.emf:.2f}"

        self.description = (
            f"A coil consisting of {self.N} turns is placed in a region of changing magnetic flux. "
            f"The magnetic flux through the coil changes by {self.dPhi} Wb over a time interval of {self.dt} s. "
            f"Calculate the magnitude of the induced e.m.f. in the coil."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic Induction"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ known\ quantities} \\\\"
            "&N = " + str(self.N) + " \\\\"
            "&\\Delta \\Phi = " + f"{self.dPhi:.4f}" + "\\,\\text{Wb} \\\\"
            "&\\Delta t = " + f"{self.dt:.3f}" + "\\,\\text{s} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ Faraday's\ Law} \\\\"
            "&\\mathcal{E} = N \\left| \\frac{\\Delta \\Phi}{\\Delta t} \\right| \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&\\mathcal{E} = " + str(self.N) + " \\times \\frac{" + f"{self.dPhi:.4f}" + "}{" + f"{self.dt:.3f}" + "} \\\\"
            "&\\mathcal{E} = \\mathbf{" + f"{float(self.answer):.2f}" + "\\,V} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&\\mathcal{E} = " + self.answer + "\\,\\text{V}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')

        coil_color = '#d35400'
        magnet_color_n = '#e74c3c'
        magnet_color_s = '#34495e'

        turns = 8
        t = np.linspace(0, turns * 2 * np.pi, 1000)
        x_coil = 0.15 * np.sin(t)
        y_coil = np.linspace(-1, 1, 1000)
        
        for i in range(len(t)-1):
            color = coil_color if np.cos(t[i]) > 0 else '#8e44ad'
            alpha = 1.0 if np.cos(t[i]) > 0 else 0.3
            ax.plot(x_coil[i:i+2], y_coil[i:i+2], color=coil_color, lw=2.5, alpha=alpha, solid_capstyle='round')

        ax.add_patch(plt.Rectangle((-2.5, -0.3), 1.0, 0.6, color=magnet_color_s, zorder=1))
        ax.add_patch(plt.Rectangle((-1.5, -0.3), 1.0, 0.6, color=magnet_color_n, zorder=1))
        ax.text(-2.0, 0, 'S', color='white', ha='center', va='center', fontweight='bold', fontsize=12)
        ax.text(-1.0, 0, 'N', color='white', ha='center', va='center', fontweight='bold', fontsize=12)
        
        ax.annotate('', xy=(0.2, 0), xytext=(-0.4, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

        field_lines = np.linspace(-0.5, 0.5, 5)
        for fl in field_lines:
            ax.annotate('', xy=(1.5, fl), xytext=(-0.5, fl),
                        arrowprops=dict(arrowstyle='->', color='#3498db', lw=1, alpha=0.4))

        ax.text(0.5, 1.1, f"$N = {self.N}$ turns", fontweight='bold', fontsize=10)
        ax.text(0.5, -1.3, f"$\\Delta\\Phi = {self.dPhi}$ Wb\n$\\Delta t = {self.dt}$ s", 
                ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        ax.set_title("ELECTROMAGNETIC INDUCTION", fontsize=14, fontweight='bold', pad=15)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()
class Phy176:
    def __init__(self):
        self.N = rnd.randint(100, 500)
        self.B = round(rnd.uniform(0.2, 1.0), 2)
        self.A = round(rnd.uniform(0.002, 0.01), 4)
        self.f = rnd.randint(10, 60)

        self.omega = 2 * math.pi * self.f
        self.emf_peak = self.N * self.B * self.A * self.omega
        self.answer = f"{self.emf_peak:.2f}"

        self.description = (
            f"A rectangular coil of {self.N} turns and cross-sectional area {self.A} m$^2$ "
            f"rotates at a constant frequency of {self.f} Hz in a uniform magnetic field "
            f"of flux density {self.B} T. Calculate the peak induced e.m.f."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic induction"
        self.curriculum = "A-Level"
        self.source = "Original"

        lF = f"{float(self.answer):.2f}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Knowns} \\\\"
            "&N = " + str(self.N) + ", \\ B = " + f"{self.B:.2f}" + "\\,\\text{T}, \\ A = " + f"{self.A:.4f}" + "\\,\\text{m}^2, \\ f = " + str(self.f) + "\\,\\text{Hz} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Angular\ Frequency\ (\\omega)} \\\\"
            "&\\omega = 2\\pi f = 2\\pi(" + str(self.f) + ") \\approx " + f"{self.omega:.2f}" + "\\, \\text{rad s}^{-1} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Peak\ e.m.f.\ Formula} \\\\"
            "&\\varepsilon_0 = BAN\\omega \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Calculation} \\\\"
            "&\\varepsilon_0 = (" + f"{self.B:.2f}" + ")(" + f"{self.A:.4f}" + ")(" + str(self.N) + ")(" + f"{self.omega:.2f}" + ") \\\\"
            "&\\varepsilon_0 = \\mathbf{" + lF + "\\,V}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.axis('off')

        mag_n, mag_s, coil_color, field_color = '#e74c3c', '#3498db', '#d35400', '#95a5a6'

        ax.add_patch(plt.Rectangle((-4.5, -1.8), 1.5, 3.6, color=mag_n, alpha=0.9, zorder=1))
        ax.add_patch(plt.Rectangle((3, -1.8), 1.5, 3.6, color=mag_s, alpha=0.9, zorder=1))
        ax.text(-3.75, 0, 'N', color='white', fontsize=24, fontweight='bold', ha='center')
        ax.text(3.75, 0, 'S', color='white', fontsize=24, fontweight='bold', ha='center')

        for y in np.linspace(-1.4, 1.4, 9):
            ax.annotate('', xy=(2.9, y), xytext=(-2.9, y),
                        arrowprops=dict(arrowstyle='->', color=field_color, lw=1, alpha=0.5))
        ax.text(0, 2.2, f"$B = {self.B}$ T", color='#2c3e50', ha='center', fontweight='bold', fontsize=12)

        angle = np.radians(35)
        w, h = 1.3, 1.8
        c, s = np.cos(angle), np.sin(angle)
        rect = np.array([[-w, -h], [w, -h], [w, h], [-w, h], [-w, -h]])
        rot = np.array([[c, -s*0.5], [s, c*0.5]])
        p = rect @ rot.T

        ax.plot([0, 0], [-2.5, 2.5], color='black', lw=1.5, ls=(0, (5, 5)), alpha=0.7, zorder=2)
        ax.text(0, -2.8, "Rotation Axis", ha='center', fontsize=9, style='italic')

        ax.plot(p[:, 0], p[:, 1], color=coil_color, lw=3.5, zorder=5)
        
        normal_len = 1.5
        nx, ny = normal_len * np.sin(angle), -normal_len * np.cos(angle) * 0.5
        ax.annotate('', xy=(nx, ny), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        ax.text(nx, ny-0.3, r"$\vec{n}$ (Normal)", fontsize=10, fontweight='bold')

        ax.annotate('', xy=(1.2, 1.8), xytext=(0.2, 1.4),
                    arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.4", 
                                    color='#27ae60', lw=2.5, mutation_scale=20))
        ax.text(1.3, 2.0, f"$\omega = 2\pi f$\n($f = {self.f}$ Hz)", color='#27ae60', fontweight='bold')

        info_text = f"Coil:\n$N = {self.N}$ turns\n$A = {self.A}$ m$^2$"
        ax.text(-4.2, -2.5, info_text, bbox=dict(facecolor='white', alpha=0.9, edgecolor='#bdc3c7'), fontsize=10)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy177:
    """
    RMS and peak voltage relation.
    """

    def __init__(self):
        self.V_peak = rnd.randint(50, 400)
        self.V_rms = self.V_peak / math.sqrt(2)
        self.answer = round(self.V_rms, 2)

        self.description = (
            f"An alternating voltage has a peak value of {self.V_peak} V. "
            "Calculate the RMS voltage. (_) V"
        )

        self.topic = "Alternating currents"
        self.subtopic = "Characteristics of Alternating Currents"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify given value}} &\\\\"
            f"V_{{\\text{{peak}}}} &= {self.V_peak}\\,\\text{{V}}\\\\"
            f"\\text{{Step 2: State the RMS relationship}} &\\\\"
            f"V_{{\\text{{rms}}}} &= \\frac{{V_{{\\text{{peak}}}}}}{{\\sqrt{{2}}}}\\\\"
            f"\\text{{Step 3: Substitute and calculate}} &\\\\"
            f"V_{{\\text{{rms}}}} &= \\frac{{{self.V_peak}}}{{\\sqrt{{2}}}}\\\\"
            f"V_{{\\text{{rms}}}} &= {round(self.V_rms, 10)}\\,\\text{{V}}\\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"V_{{\\text{{rms}}}} &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Data for plotting
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x)
        rms_val = 1 / np.sqrt(2)

        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot the AC Sine Wave
        ax.plot(x, y, color='blue', linewidth=2, label='AC Voltage')
        
        # Add Peak Voltage Line
        ax.axhline(y=1, color='red', linestyle='--', linewidth=1)
        ax.text(0.1, 1.05, f"$V_{{peak}} = {self.V_peak}$ V", color='red', fontsize=10)
        
        # Add RMS Voltage Line
        ax.axhline(y=rms_val, color='green', linestyle=':', linewidth=1.5)
        ax.text(0.1, rms_val - 0.15, f"$V_{{rms}} \\approx {self.answer}$ V", color='green', fontsize=10)
        
        # Aesthetics
        ax.axhline(0, color='black', linewidth=0.8) # Zero line
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xticks([0, np.pi, 2*np.pi])
        ax.set_xticklabels(['0', '$\pi$', '$2\pi$'])
        ax.set_yticks([-1, 0, 1])
        ax.set_title("Alternating Voltage Waveform", fontsize=12, fontweight='bold')
        ax.set_ylabel("Voltage (V)")
        ax.set_xlabel("Time / Phase (rad)")
        ax.grid(True, alpha=0.3)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.1
        )
        plt.close()


class Phy178:
    """
    RMS and peak current relation.
    """

    def __init__(self):
        self.I_rms = rnd.randint(2, 20)
        self.I_peak = self.I_rms * math.sqrt(2)
        self.answer = round(self.I_peak, 2)

        self.description = (
            f"An alternating current has an RMS value of {self.I_rms} A. "
            "Calculate the peak current. (_) A"
        )

        self.topic = "Alternating currents"
        self.subtopic = "Characteristics of alternating currents"
        self.curriculum = "A-Level"
        self.source = "Past Papers"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify given value}} &\\\\"
            f"I_{{\\text{{rms}}}} &= {self.I_rms}\\,\\text{{A}}\\\\"
            f"\\text{{Step 2: State the peak current formula}} &\\\\"
            f"I_{{\\text{{peak}}}} &= I_{{\\text{{rms}}}} \\times \\sqrt{{2}}\\\\"
            f"\\text{{Step 3: Substitute and calculate}} &\\\\"
            f"I_{{\\text{{peak}}}} &= {self.I_rms} \\times \\sqrt{{2}}\\\\"
            f"I_{{\\text{{peak}}}} &= {round(self.I_peak, 10)}\\,\\text{{A}}\\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"I_{{\\text{{peak}}}} &= {self.answer}\\,\\text{{A}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Data for plotting
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x)
        rms_val = 1 / np.sqrt(2) # Normalizing peak to 1 for the curve

        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot the AC Sine Wave (scaled to peak)
        ax.plot(x, y, color='darkorange', linewidth=2.5, label='AC Current')
        
        # Add Peak Current Line
        ax.axhline(y=1, color='red', linestyle='--', linewidth=1.2)
        ax.text(0.1, 1.05, f"$I_{{peak}} = {self.answer}$ A", color='red', fontsize=10, fontweight='bold')
        
        # Add RMS Current Line
        ax.axhline(y=rms_val, color='teal', linestyle=':', linewidth=1.8)
        ax.text(0.1, rms_val - 0.15, f"$I_{{rms}} = {self.I_rms}$ A", color='teal', fontsize=10, fontweight='bold')
        
        # Aesthetics
        ax.axhline(0, color='black', linewidth=1) # Zero axis
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
        ax.set_xticklabels(['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
        ax.set_yticks([-1, 0, 1])
        ax.set_yticklabels(['$-I_p$', '0', '$I_p$'])
        
        ax.set_title("Alternating Current (AC) Waveform", fontsize=13, pad=15)
        ax.set_ylabel("Current (A)")
        ax.set_xlabel("Phase Angle (rad)")
        ax.grid(True, linestyle=':', alpha=0.6)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.1
        )
        plt.close()

class Phy179:
    """
    Ripple voltage after smoothing capacitor.
    """

    def __init__(self):
        self.I = rnd.randint(1, 5)
        self.f = rnd.randint(50, 60)
        self.C_micro = rnd.randint(200, 1000)
        self.C = self.C_micro * 1e-6

        self.V_ripple = self.I / (self.f * self.C)
        self.answer = round(self.V_ripple, 2)

        self.description = (
            f"A smoothing capacitor of {self.C_micro} μF is connected to a "
            f"{self.f} Hz supply drawing a current of {self.I} A. "
            "Estimate the ripple voltage. (_) V"
        )

        self.topic = "Alternating Currency"
        self.subtopic = "Retrification and Smoothing"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify given values}} &\\\\"
            f"I &= {self.I}\\,\\text{{A}} \\\\"
            f"f &= {self.f}\\,\\text{{Hz}} \\\\"
            f"C &= {self.C_micro} \\times 10^{{-6}}\\,\\text{{F}} \\\\"
            f"\\text{{Step 2: Use the ripple voltage formula}} &\\\\"
            f"V_{{\\text{{ripple}}}} &= \\frac{{I}}{{fC}} \\\\"
            f"\\text{{Step 3: Substitute and calculate}} &\\\\"
            f"V_{{\\text{{ripple}}}} &= \\frac{{{self.I}}}{{{self.f} \\times {round(self.C, 10)}}} \\\\"
            f"V_{{\\text{{ripple}}}} &= {round(self.V_ripple, 10)}\\,\\text{{V}} \\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"V_{{\\text{{ripple}}}} &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        x = np.linspace(0, 4*np.pi, 1000)
        rectified = np.abs(np.sin(x))
        
        # Simulated discharge
        smoothed = []
        curr = 1.0
        for val in rectified:
            if val > curr: curr = val
            else: curr -= 0.001 
            smoothed.append(curr)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, rectified, '--', color='gray', alpha=0.4, label='Rectified Waveform')
        ax.plot(x, smoothed, color='red', linewidth=2.5, label='Smoothed Output')
        
        # Info labels on image
        ax.text(0.5, 1.2, f"Input: {self.f} Hz", color='black', fontsize=9)
        ax.text(0.5, 1.05, f"Load Current: {self.I} A", color='black', fontsize=9)
        ax.text(0.5, 0.9, f"Capacitor: {self.C_micro} µF", color='black', fontsize=9)

        # Indicate Ripple
        ax.annotate(f'Ripple $V_r$', xy=(np.pi*1.3, 0.8), xytext=(np.pi*1.8, 0.5),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1))

        ax.set_ylim(0, 1.4)
        ax.set_title("Bridge Rectifier Output with Capacitor Smoothing", fontweight='bold')
        ax.legend(loc='upper right', frameon=True)
        ax.axis('off')
        
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=600, bbox_inches="tight")
        plt.close()

class Phy180:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(4, 9)
        self.f = self.f_base * 1e14

        self.E = self.h * self.f
        self.answer = f"{self.E:.3e}"

        self.description = (
            f"Calculate the energy of a photon with frequency $f = {self.f_base} \\times 10^{{14}}$ Hz. "
            f"Take Planck's constant $h = 6.63 \\times 10^{{-34}}$ J s."
        )

        self.topic = "Quantum physics"
        self.subtopic = "Energy and momentum of a photon"
        self.curriculum = "A-Level"
        self.source = "Original"

        lE = f"{self.E:.3e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Quantities} \\\\"
            "&h = 6.63 \\times 10^{-34}\\,\\text{J s} \\\\"
            "&f = " + str(self.f_base) + " \\times 10^{14}\\,\\text{Hz} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Photon\ Energy\ Formula} \\\\"
            "&E = hf \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&E = (6.63 \\times 10^{-34})(" + str(self.f_base) + " \\times 10^{14}) \\\\"
            "&E = \\mathbf{" + lE + "\\,J} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&E = " + self.answer + "\\,\\text{J}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

        x = np.linspace(0, 10, 1000)
        sigma = 1.5
        center = 5
        envelope = np.exp(-(x - center)**2 / (2 * sigma**2))
        wave = envelope * np.sin(2 * np.pi * x * (self.f_base/3))

        colors = {4: '#e74c3c', 5: '#e67e22', 6: '#f1c40f', 7: '#2ecc71', 8: '#3498db', 9: '#9b59b6'}
        photon_color = colors.get(self.f_base, '#f39c12')

        ax.plot(x, wave, color=photon_color, lw=3, zorder=3)
        ax.fill_between(x, wave, color=photon_color, alpha=0.1)
        
        ax.annotate('', xy=(center + 1.2, 0.8), xytext=(center - 1.2, 0.8),
                    arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1))
        ax.text(center, 1.0, "Localized Energy Packet", ha='center', fontsize=9, style='italic')

        props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='#bdc3c7')
        param_text = (
            f"$\\mathbf{{Frequency\ (f):}}$\n"
            f"${self.f_base} \\times 10^{{14}}$ Hz\n\n"
            f"$\\mathbf{{Planck's\ Constant\ (h):}}$\n"
            f"$6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.2, 0, param_text, transform=ax.transAxes, fontsize=10, bbox=props, va='center')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy181:
    """
    Momentum of a photon.
    """

    def __init__(self):
        self.h = 6.63e-34
        self.lambda_base = rnd.randint(400, 700)
        self.lambda_m = self.lambda_base * 1e-9

        self.p = self.h / self.lambda_m
        self.answer = round(self.p, 3)

        self.description = (
            f"Calculate the momentum of a photon with wavelength "
            f"{self.lambda_base} nm. "
            f"Take Planck's constant h = 6.63 × 10^{{-34}} J s. (_) kg m s^(-1)"
        )

        self.topic = "Quantum physics"
        self.subtopic = "Energy and Momentum of a photon"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify given wavelength}} &\\\\"
            f"\\lambda &= {self.lambda_base}\\,\\text{{nm}} = {self.lambda_base} \\times 10^{{-9}}\\,\\text{{m}} \\\\"
            f"\\text{{Step 2: Apply the de Broglie relation}} &\\\\"
            f"p &= \\frac{{h}}{{\\lambda}} \\\\"
            f"\\text{{Step 3: Substitute constants and values}} &\\\\"
            f"p &= \\frac{{6.63 \\times 10^{{-34}}}}{{{self.lambda_base} \\times 10^{{-9}}}} \\\\"
            f"\\text{{Step 4: Solve for momentum}} &\\\\"
            f"p &= {round(self.p, 10)}\\,\\text{{kg m s}}^{{-1}} \\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"p &= {self.answer}\\,\\text{{kg m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        x = np.linspace(0, 6*np.pi, 1000)
        y = np.sin(x)
        
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(x, y, color='purple', linewidth=2.5)
        
        # Wavelength indicator between peaks
        ax.annotate('', xy=(0.5*np.pi, 1.2), xytext=(2.5*np.pi, 1.2), 
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
        ax.text(1.5*np.pi, 1.45, f"$\lambda = {self.lambda_base}$ nm", ha='center', fontweight='bold')
        
        # Value of h for context
        ax.text(4*np.pi, 1.2, f"h = 6.63 $\\times$ 10$^{{-34}}$ J s", bbox=dict(facecolor='white', alpha=0.5))

        ax.set_ylim(-1.5, 2.2)
        ax.axis('off')

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=600, bbox_inches="tight")
        plt.close()

class Phy182:
    """Photoelectric effect: maximum kinetic energy."""
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(6, 12)
        self.f = self.f_base * 1e14
        self.phi_base = rnd.randint(2, 5)
        self.phi = self.phi_base * 1e-19
        self.Ek = self.h * self.f - self.phi
        self.answer = round(self.Ek, 22)

        self.description = (
            f"Light of frequency {self.f_base} × 10^{{14}} Hz shines "
            f"on a metal with work function {self.phi_base} × 10^{{-19}} J. "
            "Calculate the maximum kinetic energy of emitted electrons. (_) J"
        )
        self.topic = "Quantum physics", 
        self.subtopic = "Photoelectric effect"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Einstein's photoelectric equation} &\\\\"
            "E_{k, \\text{max}} &= hf - \\Phi \\\\"
            "\\text{Step 2: Calculate photon energy (} hf \\text{)} &\\\\"
            f"hf &= (6.63 \\times 10^{{-34}})({self.f_base} \\times 10^{{14}}) = {round(self.h*self.f, 22)}\\,\\text{{J}} \\\\"
            "\\text{Step 3: Subtract work function} &\\\\"
            f"E_k &= {round(self.h*self.f, 22)} - ({self.phi_base} \\times 10^{{-19}}) \\\\"
            "\\text{Final Answer:} &\\\\"
            f"E_k &= {self.Ek}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axhspan(0, 0.8, color='gray', alpha=0.3)
        ax.annotate('', xy=(1.5, 0.9), xytext=(0.5, 2.5), arrowprops=dict(arrowstyle='->', color='orange', lw=2))
        ax.text(0.1, 2.6, f"Photon\n$f={self.f_base}\\times 10^{{14}}$ Hz", color='orange', fontsize=9)
        ax.annotate('', xy=(3.5, 2.5), xytext=(2, 0.9), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(3.6, 2.6, "Photoelectron\n($E_k$ max)", color='blue', fontsize=9)
        ax.text(2, 0.3, f"Metal Surface ($\Phi = {self.phi_base}\\times 10^{{-19}}$ J)", ha='center', fontweight='bold')
        ax.set_xlim(0, 5); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()
class Phy183:
    def __init__(self):
        self.e = 1.60e-19
        self.Ek_base = rnd.randint(2, 9)
        self.Ek = self.Ek_base * 1e-19
        self.Vs = self.Ek / self.e
        self.answer = f"{self.Vs:.2f}"

        self.description = (
            f"In a photoelectric effect experiment, the maximum kinetic energy of the emitted "
            f"photoelectrons is measured to be $E_{{k, \\text{{max}}}} = {self.Ek_base} \\times 10^{{-19}}$ J. "
            f"Determine the stopping potential $V_s$ required to reduce the photocurrent to zero."
        )

        self.topic = "Quantum physics"
        self.subtopic = "Photoelectric effect"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ the\ Relationship} \\\\"
            "&\\text{The work done by the stopping potential equals the maximum kinetic energy:} \\\\"
            "&E_{k, \\text{max}} = e V_s \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Rearrange\ for\ Stopping\ Potential\ (V_s)} \\\\"
            "&V_s = \\frac{E_{k, \\text{max}}}{e} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution} \\\\"
            "&e = 1.60 \\times 10^{-19}\\,\\text{C} \\\\"
            "&V_s = \\frac{" + str(self.Ek_base) + " \\times 10^{-19}}{1.60 \\times 10^{-19}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Calculation} \\\\"
            "&V_s = \\mathbf{" + self.answer + "\\,V} \\\\"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
        
        # Grafik Ek vs f
        f_threshold = 2
        f = np.linspace(f_threshold, 6, 100)
        Ek_plot = 1.5 * (f - f_threshold)
        ax1.plot(f, Ek_plot, color='#e67e22', lw=2.5, label='$E_{k,max} = hf - \Phi$')
        ax1.axhline(0, color='black', lw=1)
        ax1.axvline(f_threshold, color='black', lw=1, ls='--')
        
        target_Ek_y = 3
        target_f_x = 4
        ax1.scatter(target_f_x, target_Ek_y, color='#d35400', s=100, zorder=5)
        ax1.annotate(f'$E_k = {self.Ek_base} \\times 10^{{-19}}$ J', 
                     xy=(target_f_x, target_Ek_y), xytext=(target_f_x-1.5, target_Ek_y+0.5),
                     arrowprops=dict(arrowstyle='->', color='black'))

        ax1.set_xlabel('Frequency ($f$)', fontweight='bold')
        ax1.set_ylabel('Max Kinetic Energy ($E_{k,max}$)', fontweight='bold')
        ax1.set_title('Energy-Frequency Relationship', fontsize=12, fontweight='bold')
        ax1.set_xticks([]); ax1.set_yticks([])
        ax1.grid(True, alpha=0.3)

        # Diagram Sirkuit Sederhana (Abstraksi)
        ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
        ax2.axis('off')
        
        # Vacuum tube
        tube = plt.Circle((5, 6), 3.5, color='#ecf0f1', ec='#2c3e50', lw=2)
        ax2.add_patch(tube)
        
        # Electrodes
        ax2.plot([3, 3], [4.5, 7.5], color='#2c3e50', lw=4) # Cathode
        ax2.plot([7, 7], [4.5, 7.5], color='#2c3e50', lw=4) # Anode
        ax2.text(2.5, 8, 'Cathode (-)', ha='center', fontweight='bold')
        ax2.text(7.5, 8, 'Anode (+)', ha='center', fontweight='bold')
        
        # Photons and Electrons
        for i in range(3):
            ax2.annotate('', xy=(2.8, 7-i), xytext=(0.5, 8-i),
                         arrowprops=dict(arrowstyle='->', color='#f1c40f', lw=2, connectionstyle="arc3,rad=.2"))
        ax2.scatter([4, 5, 5.5], [6, 5.2, 6.8], color='#3498db', s=50) # Electrons
        ax2.text(1, 8.5, 'Photons ($hf$)', color='#f39c12', fontweight='bold')

        # Voltmeter / stopping potential label
        ax2.add_patch(plt.Rectangle((3.5, 1), 3, 1.5, fill=False, ec='#c0392b', lw=2))
        ax2.text(5, 1.7, f'$V_s = ?$ V', color='#c0392b', ha='center', fontweight='bold', fontsize=12)
        ax2.plot([3, 3, 3.5], [4.5, 1.75, 1.75], color='#c0392b', lw=1.5)
        ax2.plot([7, 7, 6.5], [4.5, 1.75, 1.75], color='#c0392b', lw=1.5)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy184:
    def __init__(self):
        self.h, self.m = 6.63e-34, 9.11e-31
        self.v_base = rnd.randint(1, 5)
        self.v = self.v_base * 1e6
        self.lambda_val = self.h / (self.m * self.v)
        self.answer = f"{self.lambda_val:.3e}"

        self.description = (
            f"An electron is traveling at a speed of $v = {self.v_base} \\times 10^6$ m s$^{{-1}}$. "
            f"Calculate the de Broglie wavelength associated with this electron. "
            f"($m_e = 9.11 \\times 10^{{-31}}$ kg, $h = 6.63 \\times 10^{{-34}}$ J s)"
        )
        
        self.topic = "Quantum physics"
        self.subtopic = "Wave-particle duality"
        self.curriculum = "A-Level"
        self.source = "Original"

        l_val_tex = f"{self.lambda_val:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Constants} \\\\"
            "&m_e = 9.11 \\times 10^{-31}\\,\\text{kg}, \\ v = " + str(self.v_base) + " \\times 10^6\\,\\text{m s}^{-1} \\\\"
            "&h = 6.63 \\times 10^{-34}\\,\\text{J s} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ De\ Broglie\ Equation} \\\\"
            "&\\lambda = \\frac{h}{p} = \\frac{h}{m v} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&\\lambda = \\frac{6.63 \\times 10^{-34}}{(9.11 \\times 10^{-31})(" + str(self.v_base) + " \\times 10^6)} \\\\"
            "&\\lambda = " + l_val_tex + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&\\lambda = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

        x = np.linspace(0, 10, 1000)
        k = 2 + (self.v_base * 0.4) 
        envelope = np.exp(-(x-5)**2 / 2.5)
        wave = envelope * np.cos(2 * np.pi * x * k)

        ax.plot(x, wave, color='#8e44ad', lw=2.5, zorder=3)
        ax.fill_between(x, wave, color='#9b59b6', alpha=0.1)
        
        center_x = 5
        lambda_vis = 1/(k)
        ax.annotate('', xy=(8.5, 0), xytext=(7, 0),
                    arrowprops=dict(arrowstyle='-|>', color='#2980b9', lw=3, mutation_scale=20))
        ax.text(7.75, -0.4, f"$v = {self.v_base} \\times 10^6$ m/s", color='#2980b9', fontweight='bold', ha='center')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$\\mathbf{{Electron\ Data:}}$\n"
            f"$m_e = 9.11 \\times 10^{{-31}}$ kg\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.05, 0.1, info_text, transform=ax.transAxes, fontsize=10, bbox=props)

        ax.set_title("DE BROGLIE WAVE-PARTICLE DUALITY", fontsize=12, fontweight='bold', pad=15)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()
class Phy185:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(4, 8)
        self.f = self.f_base * 1e14
        self.E = self.h * self.f
        self.answer = f"{self.E:.3e}"

        self.description = (
            f"An electron transition between two energy levels in an atom results in the emission "
            f"of radiation with a frequency of $f = {self.f_base} \\times 10^{{14}}$ Hz. "
            f"Calculate the energy difference $\\Delta E$ between these two levels."
        )
        self.topic = "Quantum physics"
        self.subtopic = "Energy levels"
        self.curriculum = "A-Level"
        self.source = "Original"

        lE = f"{self.E:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Parameters} \\\\"
            "&h = 6.63 \\times 10^{-34}\\,\\text{J s} \\\\"
            "&f = " + str(self.f_base) + " \\times 10^{14}\\,\\text{Hz} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Photon\ Energy\ Relation} \\\\"
            "&\\Delta E = hf \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitute\ and\ Calculate} \\\\"
            "&\\Delta E = (6.63 \\times 10^{-34})(" + str(self.f_base) + " \\times 10^{14}) \\\\"
            "&\\Delta E = \\mathbf{" + lE + "\\,J} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&\\Delta E = " + self.answer + "\\,\\text{J}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.hlines([1.5, 4.5], 2, 8, colors='#2c3e50', lw=3)
        ax.text(8.2, 4.5, "$E_2$ (Higher Level)", va='center', fontweight='bold')
        ax.text(8.2, 1.5, "$E_1$ (Lower Level)", va='center', fontweight='bold')

        ax.annotate('', xy=(4, 1.6), xytext=(4, 4.4), 
                    arrowprops=dict(arrowstyle='-|>', color='#c0392b', lw=2.5, mutation_scale=20))
        
        x_wave = np.linspace(4, 7, 100)
        y_wave = 3 + 0.3 * np.sin(2 * np.pi * 3 * x_wave)
        ax.plot(x_wave, y_wave, color='#f39c12', lw=2)
        ax.annotate('', xy=(7.2, 3), xytext=(6.8, 3), 
                    arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2))
        ax.text(7.3, 3.2, "Photon\nemitted", color='#e67e22', fontsize=9, fontweight='bold')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$\\mathbf{{Transition\ Data:}}$\n"
            f"$f = {self.f_base} \\times 10^{{14}}$ Hz\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.5, 5, info_text, transform=ax.transData, fontsize=10, bbox=props)

        ax.text(5, 0.5, "$\\Delta E = E_2 - E_1 = hf$", fontsize=12, fontweight='bold', ha='center')
        ax.set_title("ATOMIC ENERGY LEVEL TRANSITION", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy186:
    def __init__(self):
        self.h, self.c = 6.63e-34, 3.00e8
        self.E_base = rnd.randint(2, 9)
        self.E = self.E_base * 1e-19
        self.lambda_val = (self.h * self.c) / self.E
        self.answer = f"{self.lambda_val:.3e}"

        self.description = (
            f"An electron transition in a hydrogen atom releases energy of $\\Delta E = {self.E_base} \\times 10^{{-19}}$ J. "
            f"Calculate the wavelength $\\lambda$ of the emitted spectral line."
        )
        self.topic = "Quantum physics"
        self.subtopic = "Line spectra"
        self.curriculum = "A-Level"
        self.source = "Original"

        lW = f"{self.lambda_val:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ List\ Physical\ Constants} \\\\"
            "&h = 6.63 \\times 10^{-34}\\,\\text{J s}, \\ c = 3.00 \\times 10^8\\,\\text{m s}^{-1} \\\\"
            "&\\Delta E = " + str(self.E_base) + " \\times 10^{-19}\\,\\text{J} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Energy-Wavelength\ Formula} \\\\"
            "&\\Delta E = \\frac{hc}{\\lambda} \\implies \\lambda = \\frac{hc}{\\Delta E} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&\\lambda = \\frac{(6.63 \\times 10^{-34})(3.00 \\times 10^8)}{" + str(self.E_base) + " \\times 10^{-19}} \\\\"
            "&\\lambda = " + lW + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&\\lambda = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.hlines([1.5, 4.5], 2, 8, colors='#2c3e50', lw=3)
        ax.text(8.2, 4.5, "$E_2$ (Higher Level)", va='center', fontweight='bold')
        ax.text(8.2, 1.5, "$E_1$ (Lower Level)", va='center', fontweight='bold')
        ax.annotate('', xy=(3, 1.6), xytext=(3, 4.4), 
                    arrowprops=dict(arrowstyle='-|>', color='#27ae60', lw=2.5, mutation_scale=20))
        
        ax.text(5, 3.2, f"$\\Delta E = {self.E_base} \\times 10^{{-19}}$ J", color='#1e8449', fontweight='bold', ha='center')

        x_wave = np.linspace(4, 8, 150)
        y_wave = 1.5 + 0.4 * np.abs(np.sin(2 * np.pi * 2 * x_wave)) 
        ax.plot(x_wave, y_wave, color='#9b59b6', lw=2, ls='--')
        ax.text(6, 0.8, "$\\lambda = ?$", color='#8e44ad', fontsize=14, fontweight='bold', ha='center')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        const_text = (
            "$\\mathbf{Constants:}$\n"
            "$h = 6.63 \\times 10^{-34}$ J s\n"
            "$c = 3.00 \\times 10^8$ m s$^{-1}$"
        )
        ax.text(0.5, 5, const_text, transform=ax.transData, fontsize=10, bbox=props)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy187:
    def __init__(self):
        self.mp = 1.6726e-27
        self.mn = 1.6749e-27
        self.A = rnd.randint(10, 30)
        self.Z = rnd.randint(5, self.A - 5)
        self.N = self.A - self.Z

        self.mass_nucleons = (self.Z * self.mp) + (self.N * self.mn)
        self.mass_nucleus = self.mass_nucleons - rnd.uniform(2e-29, 6e-29)

        self.mass_defect = self.mass_nucleons - self.mass_nucleus
        self.answer = f"{self.mass_defect:.4e}"

        self.description = (
            f"A nucleus has a mass number $A = {self.A}$ and atomic number $Z = {self.Z}$. "
            f"The measured mass of the nucleus is ${self.mass_nucleus:.4e}$ kg. "
            f"Calculate the mass defect of this nucleus in kg. "
            f"(Take $m_p = 1.6726 \\times 10^{{-27}}$ kg and $m_n = 1.6749 \\times 10^{{-27}}$ kg)."
        )

        self.topic = "Nuclear physics"
        self.subtopic = "Mass defect and binding energy"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Constituents} \\\\"
            "&\\text{Protons (Z)} = " + str(self.Z) + ", \\ \\text{Neutrons (N)} = " + str(self.N) + " \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Total\ Mass\ of\ Individual\ Nucleons} \\\\"
            "&m_{\\text{total}} = (Z \\times m_p) + (N \\times m_n) \\\\"
            "&m_{\\text{total}} = (" + str(self.Z) + " \\times 1.6726 \\times 10^{-27}) + (" + str(self.N) + " \\times 1.6749 \\times 10^{-27}) \\\\"
            "&m_{\\text{total}} = " + f"{self.mass_nucleons:.4e}" + "\\,\\text{kg} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Mass\ Defect\ (\\Delta m)} \\\\"
            "&\\Delta m = m_{\\text{total}} - m_{\\text{measured}} \\\\"
            "&\\Delta m = " + f"{self.mass_nucleons:.4e}" + " - " + f"{self.mass_nucleus:.4e} \\\\"
            "&\\Delta m = \\mathbf{" + self.answer + "\\,kg}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')

        def draw_nucleus(center_x, center_y, spread, z_count, n_count, label):
            for _ in range(z_count):
                ax.scatter(center_x + rnd.uniform(-spread, spread), 
                           center_y + rnd.uniform(-spread, spread), 
                           color='#e74c3c', s=150, edgecolors='black', zorder=3)
            for _ in range(n_count):
                ax.scatter(center_x + rnd.uniform(-spread, spread), 
                           center_y + rnd.uniform(-spread, spread), 
                           color='#3498db', s=150, edgecolors='black', zorder=2)
            ax.text(center_x, center_y - 1.2, label, ha='center', fontweight='bold', fontsize=11)

        draw_nucleus(2.5, 2.5, 0.8, self.Z, self.N, "Individual Nucleons\n(Separated)")
        
        ax.text(5, 2.5, "$\longrightarrow$", fontsize=30, ha='center', va='center')
        ax.text(5, 3.0, "Binding", fontsize=10, ha='center', color='gray')

        draw_nucleus(7.5, 2.5, 0.4, self.Z, self.N, f"Bound Nucleus\n($A={self.A}, Z={self.Z}$)")

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$Z = {self.Z}$ protons, $N = {self.N}$ neutrons\n"
            f"$m_{{\\text{{measured}}}} = {self.mass_nucleus:.4e}$ kg\n"
            f"$m_p = 1.6726 \\times 10^{{-27}}$ kg\n"
            f"$m_n = 1.6749 \\times 10^{{-27}}$ kg"
        )
        ax.text(0.5, 4.8, info_text, transform=ax.transData, fontsize=9, bbox=props, va='top')

        ax.text(5, 0.5, r"Mass Defect $\Delta m = \sum m_{\text{nucleons}} - m_{\text{nucleus}}$", 
                ha='center', fontsize=12, fontweight='bold', color='#2c3e50')
        
        ax.set_title("MASS DEFECT IN NUCLEAR BINDING", fontsize=14, fontweight='bold', pad=10)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy188:
    """
    Nuclear binding energy visualization: Separated nucleons vs Bound nucleus.
    """
    def __init__(self):
        self.c = 3.00e8
        self.dm_base = rnd.randint(1, 9)
        self.dm = self.dm_base * 1e-29

        self.E = self.dm * (self.c**2)
        self.answer = round(self.E, 22)

        self.description = (
            f"The mass defect of a nucleus is {self.dm_base} × 10^{{-29}} kg. "
            "Calculate the nuclear binding energy. (_) J"
        )
        self.topic, self.subtopic = "Nuclear physics", "Nuclear Binding energy"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Use Einstein's mass-energy equivalence}} &\\\\"
            "E &= \\Delta m c^2 \\\\"
            "\\text{{Step 2: Substitute given mass defect}} &\\\\"
            f"\\Delta m &= {self.dm_base} \\times 10^{{-29}}\\,\\text{{kg}} \\\\"
            f"c &= 3.00 \\times 10^8\\,\\text{{m/s}} \\\\"
            f"E &= ({self.dm_base} \\times 10^{{-29}})(3.00 \\times 10^8)^2 \\\\"
            "\\text{{Step 3: Calculate total energy}} &\\\\"
            f"E &= {self.E:.4e}\\,\\text{{J}} \\\\"
            "\\text{{Final Answer: }} &\\\\"
            f"E &= {self.answer:.4e}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(8, 5))
        
        # 1. Draw Separated Nucleons (Left Side)
        ax.text(1.5, 3.8, "Separated Nucleons\n(Greater Mass)", ha='center', fontweight='bold', color='navy')
        for i in range(6):
            color = 'red' if i % 2 == 0 else 'blue'
            circle = plt.Circle((1 + np.cos(i), 2.5 + np.sin(i)), 0.15, color=color, ec='black', alpha=0.8)
            ax.add_patch(circle)

        # 2. Draw Bound Nucleus (Right Side)
        ax.text(5.5, 3.8, "Bound Nucleus\n(Lesser Mass)", ha='center', fontweight='bold', color='darkgreen')
        for i in range(6):
            color = 'red' if i % 2 == 0 else 'blue'
            # Nucleons are packed tightly
            circle = plt.Circle((5.5 + 0.12*np.cos(i*np.pi/3), 2.5 + 0.12*np.sin(i*np.pi/3)), 0.15, color=color, ec='black')
            ax.add_patch(circle)

        # 3. Arrow representing the transition/loss
        ax.annotate('', xy=(4.2, 2.5), xytext=(2.8, 2.5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        
        # 4. Energy Release (The 'Binding Energy' as photon/burst)
        theta = np.linspace(0, 2*np.pi, 20)
        r = 0.4 + 0.1*np.sin(10*theta)
        ax.plot(5.5 + r*np.cos(theta), 1.0 + r*np.sin(theta), color='orange', lw=2)
        ax.fill(5.5 + r*np.cos(theta), 1.0 + r*np.sin(theta), color='yellow', alpha=0.5)
        ax.text(5.5, 1.0, "Binding\nEnergy ($E$)", ha='center', va='center', fontweight='bold', color='darkorange')

        # 5. Question Labels
        ax.text(0.5, 0.5, f"$\Delta m = {self.dm_base} \\times 10^{{-29}}$ kg", 
                fontsize=11, bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.5'))
        ax.text(0.5, 1.2, "$E = \Delta m c^2$", fontsize=12, fontweight='bold')

        ax.set_xlim(0, 8); ax.set_ylim(0, 4.5); ax.axis('off')
        
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy189:
    """
    Radioactive decay using half-life.
    """
    def __init__(self):
        self.N0 = rnd.randint(500, 2000)
        self.half_life = rnd.randint(2, 10)
        self.n_half_lives = rnd.randint(1, 4)
        self.time = self.n_half_lives * self.half_life

        self.N = self.N0 * (0.5)**(self.n_half_lives)
        self.answer = round(self.N, 2)

        self.description = (
            f"A radioactive sample initially contains {self.N0} nuclei. "
            f"The half-life is {self.half_life} s. "
            f"Calculate the number of nuclei remaining after {self.time} s. (_) nuclei"
        )
        self.topic, self.subtopic = "Nuclear physics", "Radioactive decay"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Determine the number of half-lives (} n \\text{)} &\\\\"
            f"n &= \\frac{{t}}{{T_{{1/2}}}} = \\frac{{{self.time}}}{{{self.half_life}}} = {self.n_half_lives} \\\\"
            "\\text{Step 2: Apply decay formula} &\\\\"
            "N &= N_0 \\left(\\frac{1}{2}\\right)^n \\\\"
            f"N &= {self.N0} \\left(\\frac{1}{2}\\right)^{{{self.n_half_lives}}} \\\\"
            "\\text{Final Answer:} &\\\\"
            f"N &= {self.answer}\\,\\text{{nuclei}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        t_vals = np.linspace(0, self.time * 1.5, 200)
        n_vals = self.N0 * (0.5)**(t_vals / self.half_life)
        
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(t_vals, n_vals, color='darkgreen', lw=2, label='Decay Curve')
        ax.scatter([self.time], [self.N], color='red', zorder=5)
        ax.annotate(f'Remaining: {int(self.N)}', xy=(self.time, self.N), xytext=(self.time+1, self.N+100),
                    arrowprops=dict(arrowstyle='->', color='black'))
        
        ax.set_xlabel("Time (s)"); ax.set_ylabel("Number of Nuclei ($N$)")
        ax.set_title(f"Radioactive Decay ($T_{{1/2}} = {self.half_life}$ s)", fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy190:
    """
    Radioactive Activity calculation (A = λN).
    """
    def __init__(self):
        self.half_life = rnd.randint(10, 60) # in seconds
        self.decay_constant = math.log(2) / self.half_life
        self.N = rnd.randint(1, 9) * 1e12 # Number of undecayed nuclei
        
        # Calculate Activity A = λN
        self.A = self.decay_constant * self.N
        self.answer = round(self.A, 2)

        self.description = (
            f"A radioactive source contains {self.N:.1e} undecayed nuclei. "
            f"If the half-life of the source is {self.half_life} s, "
            f"calculate the activity of the sample in Becquerels (Bq). (_) Bq"
        )
        
        self.topic, self.subtopic = "Nuclear physics", "Radioactive decay"
        self.curriculum, self.source = "A-Level", "Past Papers"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Calculate the decay constant (}}\\lambda\\text{{)}} &\\\\"
            "\\lambda &= \\frac{{\\ln 2}}{{T_{{1/2}}}} = \\frac{{0.693}}{{{self.half_life}}} \\\\"
            f"\\lambda &= {self.decay_constant:.4e}\\,\\text{{s}}^{{-1}} \\\\"
            "\\text{{Step 2: Use the activity formula}} &\\\\"
            "A &= \\lambda N \\\\"
            f"A &= ({self.decay_constant:.4e})({self.N:.1e}) \\\\"
            "\\text{{Step 3: Evaluate result}} &\\\\"
            f"A &= {self.A:.2f}\\,\\text{{Bq}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"A &= {self.answer}\\,\\text{{Bq}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 4))
        
        # Visualize Source
        circle = plt.Circle((0.2, 0.5), 0.1, color='orange', alpha=0.7)
        ax.add_patch(circle)
        ax.text(0.2, 0.3, "Radioactive\nSource", ha='center', fontsize=9, fontweight='bold')
        
        # Visualize Radiation particles/waves
        for i in range(5):
            ax.annotate('', xy=(0.5, 0.5 + i*0.05 - 0.1), xytext=(0.3, 0.5),
                        arrowprops=dict(arrowstyle='->', color='red', alpha=0.6))

        # Visualize Detector (GM Tube)
        ax.add_patch(plt.Rectangle((0.55, 0.4), 0.2, 0.2, color='gray', alpha=0.8))
        ax.text(0.65, 0.65, "GM Tube\nDetector", ha='center', fontsize=9)
        
        # Digital Display
        ax.add_patch(plt.Rectangle((0.55, 0.1), 0.2, 0.15, color='black'))
        ax.text(0.65, 0.15, f"A = ? Bq", color='lime', ha='center', fontsize=10, family='monospace')

        # Info Labels
        ax.text(0.05, 0.85, f"N = {self.N:.1e} nuclei", fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
        ax.text(0.05, 0.72, f"$T_{{1/2}} = {self.half_life}$ s", fontsize=10, bbox=dict(facecolor='white', alpha=0.7))
        
        ax.set_xlim(0, 0.9); ax.set_ylim(0, 1); ax.axis('off')
        ax.set_title("Experimental Setup: Measuring Activity", fontsize=12, fontweight='bold')

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy191:
    """Ultrasound echo time distance calculation."""
    def __init__(self):
        self.v = 1540
        self.time = round(rnd.uniform(0.0002, 0.002), 6)
        self.distance = (self.v * self.time) / 2
        self.answer = round(self.distance, 4)

        self.description = (
            f"An ultrasound pulse is emitted into soft tissue and the echo "
            f"returns after {self.time} s. If the speed of sound in the tissue "
            f"is 1540 m s$^{{-1}}$, calculate the depth of the reflector. (_) m"
        )
        self.topic, self.subtopic = "Medical physics", "Ultrasound"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Use the echo-location formula}} &\\\\"
            "d &= \\frac{{v \\times t}}{{2}} \\\\"
            "\\text{{Step 2: Substitute values}} &\\\\"
            f"d &= \\frac{{(1540)({self.time})}}{{2}} \\\\"
            "\\text{{Step 3: Evaluate result}} &\\\\"
            f"d &= {self.distance:.4f}\\,\\text{{m}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"d &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        # Transducer
        ax.add_patch(plt.Rectangle((0.5, 3), 1, 0.5, color='gray'))
        ax.text(1, 3.6, "Transducer", ha='center', fontsize=10)
        # Pulse and Echo
        ax.annotate('Pulse', xy=(1, 1), xytext=(0.7, 2.5), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.annotate('Echo', xy=(1.3, 2.5), xytext=(1.3, 1), arrowprops=dict(arrowstyle='->', color='red', ls='--', lw=2))
        # Reflector (Organ boundary)
        ax.axhline(0.8, color='brown', lw=3)
        ax.text(3, 0.8, "Reflector / Boundary", va='center')
        # Labels
        ax.text(2.5, 2, f"$t = {self.time}$ s\n$v = 1540$ m/s", bbox=dict(facecolor='white', alpha=0.5))
        ax.set_xlim(0, 5); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy192:
    def __init__(self):
        self.v = 1540
        self.f_mhz = rnd.randint(2, 12)
        self.f = self.f_mhz * 1e6
        self.lambda_val = self.v / self.f
        self.answer = f"{self.lambda_val:.3e}"

        self.description = (
            f"An ultrasound transducer operates at a frequency of $f = {self.f_mhz}$ MHz. "
            f"Given that the speed of ultrasound in human soft tissue is $v = 1540$ m s$^{{-1}}$, "
            f"calculate the wavelength $\\lambda$ of the ultrasound waves in the tissue."
        )
        self.topic = "Medical physics"
        self.subtopic = "Production and use of ultrasound"
        self.curriculum = "A-Level"
        self.source = "Original"

        l_val_tex = f"{self.lambda_val:.3e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Values} \\\\"
            "&v = 1540\\,\\text{m s}^{-1} \\\\"
            "&f = " + str(self.f_mhz) + " \\times 10^6\\,\\text{Hz} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ the\ Wave\ Equation} \\\\"
            "&v = f\\lambda \\implies \\lambda = \\frac{v}{f} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution\ and\ Calculation} \\\\"
            "&\\lambda = \\frac{1540}{" + str(self.f_mhz) + " \\times 10^6} \\\\"
            "&\\lambda = " + l_val_tex + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&\\lambda = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(-2, 3)
        ax.axis('off')

        ax.add_patch(plt.Rectangle((0.5, -1.5), 1.5, 3, color='#95a5a6', alpha=0.8, ec='black', lw=1.5))
        ax.add_patch(plt.Circle((2, 0), 1.5, color='#95a5a6', alpha=0.8, ec='black', lw=1.5))
        ax.text(1.2, 0, "Transducer", rotation=90, va='center', fontweight='bold', color='white')

        ax.add_patch(plt.Rectangle((2.5, -1.8), 7, 3.6, color='#fad7a0', alpha=0.3, ec='#e67e22', lw=2, ls='--'))
        ax.text(6, 2, "Soft Tissue Layer", ha='center', fontweight='bold', color='#d35400')

        x = np.linspace(2.5, 9, 500)
        wave_freq = 1.5
        y = 0.8 * np.sin(2 * np.pi * wave_freq * x)
        ax.plot(x, y, color='#2980b9', lw=2.5)

        peak_x1 = 2.5 + (0.25 / wave_freq)
        peak_x2 = peak_x1 + (1 / wave_freq)
        ax.annotate('', xy=(peak_x1, 1.2), xytext=(peak_x2, 1.2),
                    arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1.5))
        ax.text((peak_x1 + peak_x2)/2, 1.4, r"$\lambda = ?$", ha='center', fontsize=12, fontweight='bold')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$f = {self.f_mhz}$ MHz\n"
            f"$v = 1540$ m s$^{{-1}}$"
        )
        ax.text(0.5, 2.5, info_text, transform=ax.transData, fontsize=10, bbox=props, va='top')

        ax.text(6, -1.2, r"$\lambda = \frac{v}{f}$", fontsize=14, fontweight='bold', color='#2c3e50')
        ax.set_title("ULTRASOUND WAVE IN BIOLOGICAL TISSUE", fontsize=12, fontweight='bold', pad=15)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy193:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(5, 20)
        self.f = self.f_base * 1e18
        self.E = self.h * self.f
        self.answer = f"{self.E:.3e}"

        self.description = (
            f"Calculate the energy of an X-ray photon with a frequency of "
            f"$f = {self.f_base} \\times 10^{{18}}$ Hz. "
            f"Take Planck's constant $h = 6.63 \\times 10^{{-34}}$ J s."
        )
        self.topic = "Medical physics"
        self.subtopic = "X-ray production and energy"
        self.curriculum = "A-Level"
        self.source = "Original"

        l_val_tex = f"{self.E:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\["
            "\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters} \\\\"
            "&h = 6.63 \\times 10^{-34}\\,\\text{J s} \\\\"
            "&f = " + str(self.f_base) + " \\times 10^{18}\\,\\text{Hz} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ Photon\ Energy\ Formula} \\\\"
            "&E = hf \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitution\ and\ Calculation} \\\\"
            "&E = (6.63 \\times 10^{-34})(" + str(self.f_base) + " \\times 10^{18}) \\\\"
            "&E = \\mathbf{" + l_val_tex + "\\,J} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&E = " + self.answer + "\\,\\text{J}"
            "\\end{aligned}"
            "\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        tube_outer = plt.Circle((5, 3), 3.5, color='#ecf0f1', ec='#bdc3c7', lw=1, zorder=0)
        ax.add_patch(tube_outer)

        ax.add_patch(plt.Rectangle((1.5, 2.2), 0.8, 1.6, color='#34495e', ec='black', zorder=5))
        ax.text(1.9, 4.0, "Cathode (-)", ha='center', fontweight='bold', fontsize=9)
        
        anode_coords = [[7.5, 2], [8.5, 2], [8.5, 4], [7.5, 4]]
        ax.add_patch(plt.Polygon(anode_coords, color='#7f8c8d', ec='black', zorder=5))

        target_face = [[6.8, 2.5], [7.5, 2], [7.5, 4], [6.8, 3.5]]
        ax.add_patch(plt.Polygon(target_face, color='#bdc3c7', ec='black', zorder=6))
        ax.text(8, 4.2, "Tungsten Target", ha='center', fontweight='bold', fontsize=9)

        # Electron Beam
        for i in range(4):
            y_offset = 2.4 + i * 0.4
            ax.annotate('', xy=(6.7, y_offset), xytext=(2.4, y_offset),
                        arrowprops=dict(arrowstyle='->', color='#3498db', lw=1.2, ls='--'))
        ax.text(4.5, 3.8, "High-speed\nelectrons", ha='center', color='#2980b9', fontsize=8, style='italic')

        x_wave = np.linspace(7.2, 9.8, 300)
        for shift in [-0.3, 0, 0.3]:
            y_wave = (3 + shift) + 0.3 * np.sin(2 * np.pi * 5 * x_wave)
            ax.plot(x_wave, y_wave, color='#f1c40f', lw=1.5, alpha=0.8)
        
        ax.annotate('', xy=(10.2, 3), xytext=(9.7, 3), 
                    arrowprops=dict(arrowstyle='->', color='#f1c40f', lw=2))
        ax.text(9.0, 2.0, "X-ray Photons\n(Energy $E$)", color='#f39c12', fontweight='bold', fontsize=10, ha='center')

        props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9, edgecolor='white')
        info_text = (
            f"$f = {self.f_base} \\times 10^{{18}}$ Hz\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.5, 5.7, info_text, transform=ax.transData, fontsize=10, bbox=props, va='top')

        ax.text(5, 0.5, "$E = hf$", fontsize=16, fontweight='bold', color='#c0392b', ha='center', 
                bbox=dict(facecolor='#f9ebeb', edgecolor='none', pad=3))
        
        ax.set_title("X-RAY TUBE: PHOTON EMISSION MODEL", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy194:
    """Minimum wavelength of X-rays (Duane-Hunt law)."""
    def __init__(self):
        self.h, self.c, self.e = 6.63e-34, 3.00e8, 1.60e-19
        self.V = rnd.randint(30, 100) * 1000 # 30kV to 100kV
        self.lambda_min = (self.h * self.c) / (self.e * self.V)
        self.answer = round(self.lambda_min, 13)

        self.description = (
            f"An X-ray tube operates at an accelerating potential of {self.V/1000} kV. "
            "Calculate the minimum wavelength ($\lambda_{{min}}$) of the emitted X-rays. (_) m"
        )
        self.topic, self.subtopic = "Medical physics", "Production and use of ultrasound"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Duane-Hunt Law formula}} &\\\\"
            "\\lambda_{{min}} &= \\frac{{hc}}{{eV}} \\\\"
            "\\text{{Step 2: Substitute constants and potential}} &\\\\"
            f"\\lambda_{{min}} &= \\frac{{(6.63 \\times 10^{{-34}})(3.00 \\times 10^8)}}"
            f"{{(1.60 \\times 10^{{-19}})({self.V})}} \\\\"
            "\\text{{Step 3: Evaluate}} &\\\\"
            f"\\lambda_{{min}} &= {self.lambda_min:.4e}\\,\\text{{m}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"\\lambda_{{min}} &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        # X-ray spectrum graph representation
        x = np.linspace(0.5, 5, 200)
        y = (x - 0.5)**2 * np.exp(-x) 
        ax.plot(x, y, color='blue', lw=2)
        ax.fill_between(x, y, color='blue', alpha=0.1)
        # Vertical line for lambda min
        ax.axvline(0.5, color='red', ls='--')
        ax.text(0.6, 0.1, "$\lambda_{min}$", color='red', fontweight='bold')
        ax.set_xlabel("Wavelength ($\lambda$)"); ax.set_ylabel("Intensity")
        ax.set_title(f"X-ray Spectrum at $V = {self.V/1000}$ kV")
        ax.set_xticks([]); ax.set_yticks([])
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()

class Phy195:
    def __init__(self):
        self.L_base = rnd.randint(2, 9)
        self.L = self.L_base * 1e26
        self.I_base = rnd.randint(1, 9)
        self.I = self.I_base * 1e-10
        self.d = math.sqrt(self.L / (4 * math.pi * self.I))
        self.answer = f"{self.d:.3e}"

        self.description = (f"A star has luminosity $L = {self.L_base} \\times 10^{{26}}$ W. "
                            f"The observed intensity on Earth is $I = {self.I_base} \\times 10^{{-10}}$ W m$^{{-2}}$. "
                            "Calculate the distance $d$ to the star.")
        self.topic, self.subtopic = "Astronomy and Cosmology", "Standard candles"
        self.curriculum, self.source = "A-Level", "Original"

        l_val = f"{self.d:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Inverse\ Square\ Law} \\\\"
            "&I = \\frac{L}{4\\pi d^2} \\implies d = \\sqrt{\\frac{L}{4\\pi I}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Substitution} \\\\"
            "&d = \\sqrt{\\frac{" + str(self.L_base) + " \\times 10^{26}}{4\\pi(" + str(self.I_base) + " \\times 10^{-10})}} \\\\"
            "&d = " + l_val + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&d = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#0b0d17')
        ax.set_facecolor('#0b0d17')
        
        for i in range(20, 0, -1):
            ax.add_patch(plt.Circle((0.5, 2), 0.05 + i*0.04, color='#f1c40f', alpha=0.03))
        ax.add_patch(plt.Circle((0.5, 2), 0.08, color='#fffceb', zorder=5))
        
        ax.add_patch(plt.Circle((4.5, 2), 0.1, color='#3498db', zorder=5))
        ax.text(4.5, 1.7, "Earth", color='white', ha='center', fontsize=8)

        angles = np.linspace(-0.6, 0.6, 5)
        for ang in angles:
            ax.plot([0.5, 4.5], [2, 2 + ang], color='#f1c40f', lw=0.8, alpha=0.5, ls='--')

        ax.annotate('', xy=(4.5, 1.0), xytext=(0.5, 1.0),
                    arrowprops=dict(arrowstyle='<->', color='white', lw=1.5))
        ax.text(2.5, 0.7, r"Distance $d = \sqrt{\frac{L}{4\pi I}}$", color='white', ha='center', fontsize=12)
        
        props = dict(boxstyle='round', facecolor='black', alpha=0.7, edgecolor='#f1c40f')
        ax.text(0.5, 3.2, f"Star Luminosity ($L$):\n{self.L_base} $\\times 10^{{26}}$ W", color='white', ha='center', bbox=props)
        ax.text(4.5, 3.2, f"Observed Intensity ($I$):\n{self.I_base} $\\times 10^{{-10}}$ W/m²", color='white', ha='center', bbox=props)

        ax.set_xlim(0, 5); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy196:
    def __init__(self):
        self.sigma = 5.67e-8
        self.L_base = rnd.randint(2, 9)
        self.L = self.L_base * 1e26
        self.T = rnd.randint(3000, 8000)
        self.R = math.sqrt(self.L / (4 * math.pi * self.sigma * self.T**4))
        self.answer = f"{self.R:.3e}"

        self.description = (
            f"A star has a luminosity of $L = {self.L_base} \\times 10^{{26}}$ W "
            f"and a surface temperature of $T = {self.T}$ K. "
            f"Determine the radius $R$ of the star."
        )
        self.topic, self.subtopic = "Astronomy and cosmology", "Stellar radii"
        self.curriculum, self.source = "A-Level", "Original"

        l_val = f"{self.R:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Stefan-Boltzmann\ Law} \\\\"
            "&L = A \\sigma T^4 = (4\\pi R^2) \\sigma T^4 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Rearrange\ for\ Radius} \\\\"
            "&R = \\sqrt{\\frac{L}{4\\pi \\sigma T^4}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&R = \\sqrt{\\frac{" + str(self.L_base) + " \\times 10^{26}}{4\\pi(5.67 \\times 10^{-8})(" + str(self.T) + ")^4}} \\\\"
            "&R = " + l_val + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&R = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='#0b0d17')
        ax.set_facecolor('#0b0d17')
        
        color = '#ff9f43' if self.T < 5000 else '#54a0ff'
        for i in range(60, 0, -1):
            ax.add_patch(plt.Circle((3, 3), (i/60)*1.8, color=color, alpha=0.015))
        ax.add_patch(plt.Circle((3, 3), 1.2, facecolor='white', edgecolor=color, lw=2, zorder=5))
        
        ax.annotate('', xy=(3 + 1.2, 3), xytext=(3, 3),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2, zorder=10))
        ax.text(3.6, 3.1, "$R$", color='black', ha='center', fontweight='bold', zorder=11)
        
        info = f"$L = {self.L_base} \\times 10^{{26}}$ W\n$T = {self.T}$ K"
        ax.text(3, 0.6, info, color='white', ha='center', fontsize=12, 
                bbox=dict(facecolor='#1e272e', edgecolor='white', boxstyle='round,pad=1'))
        
        ax.text(3, 5.2, "Stefan-Boltzmann Equation:\n$L = 4\\pi R^2 \\sigma T^4$", color='white', ha='center', fontsize=11, style='italic')

        ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy198:
    def __init__(self):
        self.c = 3.00e8
        self.z = round(rnd.uniform(0.001, 0.02), 4)
        self.v = self.z * self.c
        self.answer = f"{self.v:.3e}"

        self.description = (
            f"A distant galaxy is observed to have a redshift $z = {self.z}$. "
            f"Calculate the recessional velocity $v$ of this galaxy."
        )
        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Past Papers"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Redshift\ Relation} \\\\"
            "&z = \\frac{\\Delta \\lambda}{\\lambda} \\approx \\frac{v}{c} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Velocity} \\\\"
            "&v = zc = (" + str(self.z) + ")(3.00 \\times 10^8) \\\\"
            "&v = " + f"{self.v:.4e}".replace("e", "\\times 10^{") + "}" + "\\,\\text{m s}^{-1} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&v = " + self.answer + "\\,\\text{m s}^{-1}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#0b0d17')
        ax.set_facecolor('#0b0d17')
        
        ax.scatter(0.5, 2, color='#3498db', s=200, marker='o', edgecolors='white')
        ax.text(0.5, 1.5, "Observer\n(Earth)", color='white', ha='center', fontsize=9)
        
        ax.scatter(4.5, 2, color='#ee5253', s=300, marker='H', alpha=0.8)
        ax.text(4.5, 1.5, f"Galaxy\n$z = {self.z}$", color='white', ha='center', fontsize=10)
        
        ax.annotate('', xy=(5.5, 2), xytext=(4.8, 2),
                    arrowprops=dict(arrowstyle='->', color='#ee5253', lw=3))
        ax.text(5.2, 2.3, "$v$", color='#ee5253', fontsize=14, fontweight='bold')
        
        x = np.linspace(1, 4, 200)
        wave = 2 + 0.2 * np.sin(2 * np.pi * x / (0.4 + self.z * 5))
        ax.plot(x, wave, color='#ee5253', lw=2, alpha=0.7)
        ax.text(2.5, 2.5, "Redshifted Light\n($\\lambda_{obs} > \\lambda_{emit}$)", color='#ee5253', ha='center', fontsize=9)

        ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy199:
    def __init__(self):
        self.H_km_s_mpc = 70
        self.H = (self.H_km_s_mpc * 1000) / (3.086e22)
        self.v_base = rnd.randint(1, 15)
        self.v = self.v_base * 1e6
        self.d = self.v / self.H
        self.answer = f"{self.d:.3e}"

        self.description = (
            f"A galaxy has a recessional velocity $v = {self.v_base} \\times 10^6$ m s$^{{-1}}$. "
            f"Using a Hubble constant $H_0 = {self.H_km_s_mpc}$ km s$^{{-1}}$ Mpc$^{{-1}}$, "
            f"calculate its distance $d$ from Earth."
        )
        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Unit\ Conversion} \\\\"
            "&H_0 = \\frac{70 \\times 10^3}{3.086 \\times 10^{22}} \\approx " + f"{self.H:.4e}".replace("e", "\\times 10^{") + "}" + "\\,\\text{s}^{-1} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Hubble's\ Law} \\\\"
            "&v = H_0 d \\implies d = \\frac{v}{H_0} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Distance} \\\\"
            "&d = \\frac{" + f"{self.v:.2e}".replace("e", "\\times 10^{") + "}}{" + f"{self.H:.4e}".replace("e", "\\times 10^{") + "}} \\\\"
            "&d = " + f"{self.d:.4e}".replace("e", "\\times 10^{") + "}" + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&d = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='#0b0d17')
        ax.set_facecolor('#0b0d17')
        
        ax.plot(0, 0, 'w+', markersize=10)
        ax.text(0, -0.5, "Milky Way", color='white', ha='center', fontsize=8)
        
        for r in [1, 2, 3, 4]:
            circle = plt.Circle((0, 0), r, color='white', fill=False, ls='--', alpha=0.2)
            ax.add_patch(circle)
        
        ax.scatter(3.5, 0.5, color='#ff7f50', s=150, marker='*')
        ax.annotate('', xy=(4.5, 0.7), xytext=(3.7, 0.55), arrowprops=dict(arrowstyle='->', color='white'))
        
        ax.text(2, 0.2, "Distance ($d$)", color='white', ha='center', rotation=10)
        ax.text(4.5, 1.2, f"Recession $v = {self.v_base} \\times 10^6$ m/s", color='white', ha='center', bbox=dict(facecolor='black', alpha=0.5))
        
        ax.text(-3, 2.5, f"Hubble Constant:\n$H_0 = {self.H_km_s_mpc}$ km/s/Mpc", color='white', 
                bbox=dict(facecolor='#2c3e50', edgecolor='#3498db', pad=8))

        ax.set_xlim(-5, 6); ax.set_ylim(-3, 3); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy200:
    def __init__(self):
        self.sigma = 5.67e-8
        self.R_val = rnd.randint(5, 25)
        self.R = self.R_val * 1e8
        self.T = rnd.randint(3000, 12000)
        self.L = 4 * math.pi * self.R**2 * self.sigma * self.T**4
        self.answer = f"{self.L:.3e}"

        self.description = (
            f"A star has a radius of $R = {self.R_val} \\times 10^8$ m and a "
            f"surface temperature of $T = {self.T}$ K. "
            f"Calculate its total luminosity $L$."
        )
        self.topic, self.subtopic = "Astronomy & cosmology", "Stellar radii"
        self.curriculum, self.source = "A-Level", "Original"

        l_val = f"{self.L:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Formula} \\\\"
            "&L = 4\\pi R^2 \\sigma T^4 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Substitution} \\\\"
            "&L = 4\\pi(" + str(self.R_val) + " \\times 10^8)^2 (5.67 \\times 10^{-8}) (" + str(self.T) + ")^4 \\\\"
            "&L = " + l_val + "\\,\\text{W} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&L = " + self.answer + "\\,\\text{W}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='#0b0d17')
        ax.set_facecolor('#0b0d17')
        
        color = '#fff200' if self.T < 6000 else '#00d2ff'
        for r_offset in np.linspace(0, 0.8, 12):
            ax.add_patch(plt.Circle((3, 3), 1.2 + r_offset, color=color, alpha=0.04))
        
        ax.add_patch(plt.Circle((3, 3), 1.2, facecolor='white', edgecolor='gray', lw=1.5))
        
        ax.plot([3, 4.2], [3, 3], color='black', lw=2.5, zorder=10)
        ax.text(3.6, 3.3, "$R$", color='black', ha='center', fontweight='bold', zorder=11)
        
        for angle in range(0, 360, 45):
            rad = np.deg2rad(angle)
            ax.annotate('', xy=(3 + 2.4*np.cos(rad), 3 + 2.4*np.sin(rad)), 
                        xytext=(3 + 1.4*np.cos(rad), 3 + 1.4*np.sin(rad)),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2))

        ax.text(3, 0.5, f"Radius: {self.R_val}e8 m\nTemp: {self.T} K", 
                color='white', ha='center', fontsize=12, 
                bbox=dict(facecolor='#2c3e50', edgecolor='white', pad=10))

        ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()
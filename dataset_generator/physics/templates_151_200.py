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
    """
    Electric field between parallel plates.
    Uses E = V / d for a uniform electric field.
    """

    def __init__(self):
        while True:
            self.distance_mm = rnd.uniform(20.0, 80.0)     # mm
            self.voltage = rnd.uniform(100.0, 400.0)       # V

            self.distance = self.distance_mm / 1000        # convert to m

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

        # Negative plate
        ax.add_patch(patches.Rectangle(
            (left_plate_x, plate_bottom),
            plate_width,
            plate_height,
            color="black"
        ))

        # Positive plate
        ax.add_patch(patches.Rectangle(
            (right_plate_x, plate_bottom),
            plate_width,
            plate_height,
            color="black"
        ))

        # Plate labels
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
                f"{self.distance_mm:.0f} mm",
                ha="center")

        # Small vertical guide lines under plates
        ax.plot([left_plate_x + plate_width/2,
                left_plate_x + plate_width/2],
                [plate_bottom, plate_bottom - 0.5],
                color="black", linewidth=0.8)

        ax.plot([right_plate_x + plate_width/2,
                right_plate_x + plate_width/2],
                [plate_bottom, plate_bottom - 0.5],
                color="black", linewidth=0.8)

        wire_y_bottom = 2.0
        wire_left = 1.0
        wire_right = 11.0

        # Left vertical wire
        ax.plot([wire_left, wire_left],
                [plate_bottom + plate_height/2, wire_y_bottom],
                color="black", linewidth=1.2)

        # Top left horizontal wire
        ax.plot([wire_left, left_plate_x],
                [plate_bottom + plate_height/2,
                plate_bottom + plate_height/2],
                color="black", linewidth=1.2)

        # Top right horizontal wire
        ax.plot([right_plate_x + plate_width, wire_right],
                [plate_bottom + plate_height/2,
                plate_bottom + plate_height/2],
                color="black", linewidth=1.2)

        # Right vertical wire (upper part)
        ax.plot([wire_right, wire_right],
                [plate_bottom + plate_height/2, 4.1],
                color="black", linewidth=1.2)

        # Switch
        ax.add_patch(patches.Circle((wire_right, 4.1), 0.12, fill=False))
        ax.add_patch(patches.Circle((wire_right, 3.3), 0.12, fill=False))
        ax.plot([wire_right, wire_right + 0.4],
                [3.9, 3.5],
                color="black", linewidth=1.2)

        # Right vertical lower wire
        ax.plot([wire_right, wire_right],
                [3.3, wire_y_bottom],
                color="black", linewidth=1.2)

        # Bottom horizontal wire
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

        # Geometry parameters
        plate_height = 4.2
        plate_width = 0.15
        plate_bottom = 2.9

        center_x = 6
        gap = 1.4

        left_x = center_x - gap/2 - plate_width
        right_x = center_x + gap/2

    
        # Plates
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

        # Distance marking (exact center)
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

        # Charged ball (perfect center)
        ball_x = center_x
        ball_y = plate_bottom + plate_height/2

        ax.add_patch(patches.Circle((ball_x, ball_y),
                                    0.22,
                                    color="black"))

        # small field ticks
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


        # Circuit loop (rectangle)
        top_wire_y = plate_bottom + plate_height - 0.2
        bottom_wire_y = 1.6
        left_wire_x = 2
        right_wire_x = 10.2

        # left side
        ax.plot([left_x, left_wire_x],
                [top_wire_y, top_wire_y],
                color="black", linewidth=1)

        ax.plot([left_wire_x, left_wire_x],
                [top_wire_y, bottom_wire_y],
                color="black", linewidth=1)

        # bottom
        ax.plot([left_wire_x, right_wire_x],
                [bottom_wire_y, bottom_wire_y],
                color="black", linewidth=1)

        # right side to switch
        ax.plot([right_x + plate_width, right_wire_x],
                [top_wire_y, top_wire_y],
                color="black", linewidth=1)

        ax.plot([right_wire_x, right_wire_x],
                [top_wire_y, 4.2],
                color="black", linewidth=1)


        # Switch (open, accurate orientation)
        ax.add_patch(patches.Circle((right_wire_x, 3.9), 0.07, fill=False))
        ax.add_patch(patches.Circle((right_wire_x, 3.3), 0.07, fill=False))

        ax.plot([right_wire_x, right_wire_x + 0.5],
                [3.9, 3.5],
                color="black", linewidth=1)

        ax.plot([right_wire_x, right_wire_x],
                [3.3, bottom_wire_y],
                color="black", linewidth=1)


        # Power supply (centered)
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

        # Positions
        xA = 4
        xB = 6
        y = 2

        # Charges
        ax.add_patch(patches.Circle((xA, y), 0.18, color="#555555"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#555555"))

        # Labels A and B
        ax.text(xA, y + 0.35, "A", ha="center", fontsize=11, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=11, weight="bold")

        # Charge values
        ax.text(xA, y - 0.45, f"{self.q1_nC:.2f} nC", ha="center")
        ax.text(xB, y - 0.45, f"{self.q2_nC:.2f} nC", ha="center")

        # Distance arrow
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

        # Background panel
        panel = patches.FancyBboxPatch(
            (0.5, 0.8), 9, 2.4,
            boxstyle="round,pad=0.03",
            edgecolor="none",
            facecolor="#f2f2f2"
        )
        ax.add_patch(panel)

        # Charge positions
        xA = 4
        xB = 6
        y = 2

        # Draw charges
        ax.add_patch(patches.Circle((xA, y), 0.18, color="#4a4a4a"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#4a4a4a"))

        # Labels
        ax.text(xA, y + 0.35, "A", ha="center", fontsize=11, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=11, weight="bold")

        ax.text(xA, y - 0.45,
                f"+{self.q1_fC:.2f} ×10⁻¹⁵ C",
                ha="center", fontsize=9)

        ax.text(xB, y - 0.45,
                f"{self.q2_fC:.2f} ×10⁻¹⁵ C",
                ha="center", fontsize=9)

        # Distance arrow
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

        # Pre-filtered values so no heavy looping is needed
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

        # Geometry positions
        alpha_center = (-4.5, 0)
        nucleus_center = (4.5, 0)

        # Alpha particle (smaller)
        alpha = plt.Circle(alpha_center, 0.6, facecolor="#e6e6e6", edgecolor="black", linewidth=2.2)
        ax.add_patch(alpha)
        ax.text(alpha_center[0], alpha_center[1], r"$\alpha$", ha="center", va="center", fontsize=18)

        # Gold nucleus (significantly larger)
        nucleus = plt.Circle(nucleus_center, 1.6, facecolor="#f4d27a", edgecolor="black", linewidth=2.2)
        ax.add_patch(nucleus)
        ax.text(nucleus_center[0], 0.6, r"$\mathrm{Au}$", ha="center", va="center", fontsize=18)
        ax.text(nucleus_center[0], -0.5, r"$Z = 79$", ha="center", va="center", fontsize=15)

        # Velocity arrow (stops before dashed line, not touching nucleus)
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

        # Vertical dashed 
        ax.plot(
            [2.0, 2.0],
            [-1.2, 1.2],
            linestyle=(0, (4, 4)),
            linewidth=1.8,
            color="#2b6cb0"
        )

        # r_min double arrow (horizontal, proportional length)
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

        # Repulsion arrow (shorter, thinner, horizontal)
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
    """
    Electrostatic potential energy between an alpha particle and a gold nucleus
    at the distance of closest approach.
    """

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
            f"An α-particle ⁴₂He is moving directly towards a stationary gold nucleus ¹⁹⁷₇₉Au. "
            f"At a distance of {self.r:.2e} m the α-particle momentarily comes to rest. "
            f"Calculate the electric potential energy of the particles at this instant. (_) J"
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Original"
        self.curriculum = "A-Level"
        def sci_latex(val):
            if val == 0:
                return "0"
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            return f"{mantissa:.3f} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"k &= {sci_latex(self.k)}\\,\\text{{N m}}^2\\text{{C}}^{{-2}}\\\\"
            f"e &= {sci_latex(self.e)}\\,\\text{{C}}\\\\"
            f"r &= {sci_latex(self.r)}\\,\\text{{m}}\\\\[6pt]"
            "\\textbf{Step 2: Determine charges}\\\\"
            f"q_1 &= 2e = 2({sci_latex(self.e)}) = {sci_latex(self.q_alpha)}\\,\\text{{C}}\\\\"
            f"q_2 &= 79e = 79({sci_latex(self.e)}) = {sci_latex(self.q_gold)}\\,\\text{{C}}\\\\[6pt]"
            "\\textbf{Step 3: Use electrostatic potential energy formula}\\\\"
            "U &= \\dfrac{k q_1 q_2}{r}\\\\[6pt]"
            "\\textbf{Step 4: Substitute numerical values}\\\\"
            f"U &= \\dfrac{{({sci_latex(self.k)})({sci_latex(self.q_alpha)})({sci_latex(self.q_gold)})}}{{{sci_latex(self.r)}}}\\\\[6pt]"
            "\\textbf{Step 5: Compute result}\\\\"
            f"U &= {sci_latex(self.U)}\\,\\text{{J}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"U &= {sci_latex(self.U)}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.axis('off')

        y = 2
        x_alpha = 2
        x_gold = 10

        alpha_radius = 0.5
        gold_radius = 0.9

        alpha_circle = plt.Circle((x_alpha, y), alpha_radius, fill=False, linewidth=1.5)
        gold_circle = plt.Circle((x_gold, y), gold_radius, fill=False, linewidth=1.5)

        ax.add_patch(alpha_circle)
        ax.add_patch(gold_circle)

        ax.text(x_alpha, y + 0.15, "α", ha='center', va='center', fontsize=12)
        ax.text(x_alpha, y - 0.25, "(⁴₂He)", ha='center', va='center', fontsize=11)

        ax.text(x_gold, y + 0.15, "Au", ha='center', va='center', fontsize=12)
        ax.text(x_gold, y - 0.25, "(¹⁹⁷₇₉Au)", ha='center', va='center', fontsize=11)

        ax.plot([x_alpha, x_gold], [y, y], linewidth=1)

        ax.annotate(
            "",
            xy=(x_gold - 1.2, y + 1.0),
            xytext=(x_alpha + 1.0, y + 1.0),
            arrowprops=dict(arrowstyle="->", linewidth=1.2)
        )

        ax.text((x_alpha + x_gold) / 2, y + 1.5,
                "α momentarily at rest",
                ha='center', va='center', fontsize=11)

        ax.annotate(
            "",
            xy=(x_gold, y - 0.9),
            xytext=(x_alpha, y - 0.9),
            arrowprops=dict(arrowstyle="<->", linewidth=1)
        )

        exponent = int(math.floor(math.log10(abs(self.r))))
        mantissa = self.r / (10 ** exponent)

        ax.text((x_alpha + x_gold) / 2, y - 1.2,
                rf"${mantissa:.3f} \times 10^{{{exponent}}}\,\mathrm{{m}}$",
                ha='center', va='center', fontsize=11)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")

        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy158:
    """
    Kinetic energy of an alpha particle moving at high speed.
    """

    def __init__(self):
        self.mass_alpha = 6.64e-27  # kg

        while True:
            self.speed = rnd.uniform(2.0e7, 6.0e7)
            if 1e7 < self.speed < 1e8:
                break

        self.KE = 0.5 * self.mass_alpha * self.speed**2
        self.answer = self.KE

        self.description = (
            f"An α-particle (⁴₂He²⁺) is travelling at a speed of {self.speed:.2e} m s⁻¹. "
            f"Calculate its kinetic energy. (_) J"
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
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
            f"m &= {sci(self.mass_alpha)}\\,\\text{{kg}}\\\\"
            f"v &= {sci(self.speed)}\\,\\text{{m s}}^{{-1}}\\\\[6pt]"
            "\\textbf{Step 2: Write kinetic energy formula}\\\\"
            "E_k &= \\frac{1}{2}mv^2\\\\[6pt]"
            "\\textbf{Step 3: Substitute values}\\\\"
            f"E_k &= \\frac{{1}}{{2}}({sci(self.mass_alpha)})({sci(self.speed)})^2\\\\[6pt]"
            "\\textbf{Step 4: Compute } v^2\\\\"
            f"v^2 &= ({sci(self.speed)})^2\\\\"
            f"&= {sci(self.speed**2)}\\\\[6pt]"
            "\\textbf{Step 5: Final Answer}\\\\"
            f"E_k &= {sci(self.KE)}\\,\\text{{J}}\\\\[6pt]"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.axis('off')

        y = 2
        x_alpha = 3

        alpha_radius = 0.8

        alpha_circle = plt.Circle((x_alpha, y), alpha_radius, fill=False, linewidth=1.5)
        ax.add_patch(alpha_circle)

        ax.text(x_alpha, y + 0.2, "α", ha='center', va='center', fontsize=16)
        ax.text(x_alpha, y - 1.2, r"$^{4}_{2}\mathrm{He}^{2+}$",
                ha='center', va='center', fontsize=16)

        ax.annotate(
            "",
            xy=(10, y),
            xytext=(x_alpha + alpha_radius, y),
            arrowprops=dict(arrowstyle="->", linewidth=1.5)
        )

        exponent = int(math.floor(math.log10(abs(self.speed))))
        mantissa = self.speed / (10 ** exponent)

        ax.text(7, y + 0.6,
                rf"$v = {mantissa:.3f} \times 10^{{{exponent}}}\,\mathrm{{m\,s^{{-1}}}}$",
                ha='center', va='center', fontsize=16)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")

        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
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

        # Top wire
        ax.plot([3, 9], [6, 6], linewidth=lw, color="black")

        # Left battery branch
        ax.plot([3, 3], [6, 4.5], linewidth=lw, color="black")
        ax.plot([2.7, 3.3], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([2.5, 3.5], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([3, 3], [4.1, 2], linewidth=lw, color="black")
        ax.text(1.8, 4.2, f"{self.V:.1f} V", fontsize=10, color="black")

        # Bottom wire
        ax.plot([3, 9], [2, 2], linewidth=lw, color="black")

        # Capacitor X
        ax.plot([6, 6], [6, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([6, 6], [4.1, 2], linewidth=lw, color="black")
        ax.text(5.7, 4.7, "X", ha="center", fontsize=10, color="black")
        ax.text(5.5, 3.7, f"{self.Cx*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        # Capacitor Y
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

        # Top wire
        ax.plot([3, 9], [6, 6], linewidth=lw, color="black")

        # Left battery branch
        ax.plot([3, 3], [6, 4.5], linewidth=lw, color="black")
        ax.plot([2.7, 3.3], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([2.5, 3.5], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([3, 3], [4.1, 2], linewidth=lw, color="black")
        ax.text(1.8, 4.2, f"{self.V:.1f} V", fontsize=10, color="black")

        # Bottom wire
        ax.plot([3, 9], [2, 2], linewidth=lw, color="black")

        # Capacitor X
        ax.plot([6, 6], [6, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.5, 4.5], linewidth=lw, color="black")
        ax.plot([5.6, 6.4], [4.1, 4.1], linewidth=lw, color="black")
        ax.plot([6, 6], [4.1, 2], linewidth=lw, color="black")
        ax.text(5.7, 4.7, "X", ha="center", fontsize=10, color="black")
        ax.text(5.5, 3.7, f"{self.Cx*1e6:.1f} µF",
                ha="center", fontsize=10, color="black")

        # Capacitor Y
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
    """
    Percentage energy lost during capacitor discharge in first 30 ms.
    """

    def __init__(self):
        while True:
            self.C = rnd.randint(100, 200) * 1e-6  # F
            self.V0 = rnd.uniform(0.6, 0.9)       # initial voltage (V)
            self.t = rnd.randint(20, 40) * 1e-3   # s
            self.tau = rnd.uniform(0.02, 0.06)    # time constant (s)

            self.Vt = self.V0 * math.exp(-self.t / self.tau)

            if self.Vt > 0:
                break

        self.E0 = 0.5 * self.C * self.V0**2
        self.Et = 0.5 * self.C * self.Vt**2
        self.percent_lost = ((self.E0 - self.Et) / self.E0) * 100

        self.answer = round(self.percent_lost, 2)

        self.description = (
            f"A capacitor of capacitance {self.C*1e6:.0f} µF is initially "
            f"charged to a potential difference of {self.V0:.2f} V. "
            f"It discharges through a resistor. After {int(self.t*1000)} ms, "
            f"the voltage is given by the exponential decay shown. "
            f"Calculate the energy lost during the first {int(self.t*1000)} ms "
            f"as a percentage of the initial energy. (_) %"
        )

        self.topic = "Capcitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        def sci(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            mantissa_str = f"{mantissa:.3f}".rstrip('0').rstrip('.')
            return f"{mantissa_str} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Initial energy stored}\\\\"
            "E_0 &= \\frac{1}{2} C V_0^2\\\\"
            f"E_0 &= \\frac{{1}}{{2}}({sci(self.C)})({self.V0:.4f})^2\\\\"
            f"E_0 &= {sci(self.E0)}\\,\\text{{J}}\\\\[6pt]"
            "\\textbf{Step 2: Voltage after time } t\\\\"
            "V(t) &= V_0 e^{-t/\\tau}\\\\"
            f"V(t) &= {self.V0:.4f} e^{{-{self.t:.4f}/{self.tau:.4f}}}\\\\"
            f"V(t) &= {self.Vt:.4f}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 3: Energy remaining}\\\\"
            "E(t) &= \\frac{1}{2} C V(t)^2\\\\"
            f"E(t) &= \\frac{{1}}{{2}}({sci(self.C)})({self.Vt:.4f})^2\\\\"
            f"E(t) &= {sci(self.Et)}\\,\\text{{J}}\\\\[6pt]"
            "\\textbf{Step 4: Percentage energy lost}\\\\"
            "\\%\\,\\text{lost} &= "
            "\\frac{E_0 - E(t)}{E_0} \\times 100\\\\"
            f"\\%\\,\\text{{lost}} &= {self.answer}\\,\\%"
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

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.set_xlabel("Time / ms")
        ax.set_ylabel("pd / V")

        t_vals = np.linspace(0, 0.04, 400)
        V_vals = self.V0 * np.exp(-t_vals / self.tau)

        ax.plot(t_vals * 1000, V_vals, linewidth=2, color="black")
        ax.set_xlim(0, 40)
        ax.set_ylim(0, self.V0 * 1.1)

        ax.grid(True, linestyle='--', linewidth=0.5)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy164:
    """
    Time constant of an RC discharge circuit.
    """

    def __init__(self):
        # Randomise but keep values physically sensible
        self.R = rnd.randint(50, 300)  # ohm
        self.C = rnd.randint(10, 80) * 1e-6  # F

        self.tau = self.R * self.C  # s
        self.answer = round(self.tau, 5)

        self.description = (
            f"The resistor, R, in the experiment is fixed at a resistance of "
            f"{self.R} Ω and the capacitor, C, has a capacitance of "
            f"{self.C*1e6:.0f} µF and is discharging. "
            f"Calculate the time constant of the circuit. (_) s"
        )

        self.topic = "Capacitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Original"
        self.curriculum = "A-Level"

        def sci(val):
            exponent = int(math.floor(math.log10(abs(val))))
            mantissa = val / (10 ** exponent)
            mantissa_str = f"{mantissa:.3f}".rstrip('0').rstrip('.')
            return f"{mantissa_str} \\times 10^{{{exponent}}}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"R &= {self.R}\\,\\Omega\\\\"
            f"C &= {sci(self.C)}\\,\\text{{F}}\\\\[6pt]"
            "\\textbf{Step 2: Time constant formula}\\\\"
            "\\tau &= RC\\\\[6pt]"
            "\\textbf{Step 3: Substitute values}\\\\"
            f"\\tau &= ({self.R})({sci(self.C)})\\\\[6pt]"
            "\\textbf{Step 4: Compute time constant}\\\\"
            f"\\tau &= {sci(self.tau)}\\,\\text{{s}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"\\tau &= {self.answer}\\,\\text{{s}}"
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
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        lw = 2

        # Left vertical wire
        ax.plot([2, 2], [5, 1], linewidth=lw, color="black")

        # Battery plates 
        ax.plot([1.8, 2.6], [4.2, 4.2], linewidth=lw, color="black")  # long plate
        ax.plot([1.9, 2.5], [3.8, 3.8], linewidth=lw, color="black")  # short plate
        ax.text(1.5, 4.3, "+", fontsize=12, color="black")
        ax.text(1.5, 3.6, "V", fontsize=12, color="black")

        # Top wire
        ax.plot([2, 6], [5, 5], linewidth=lw, color="black")

        # Resistor (long rectangular, centered)
        ax.add_patch(
            plt.Rectangle((6, 4.6), 2.5, 0.8,
                          fill=False,
                          edgecolor="black",
                          linewidth=lw)
        )
        ax.text(7.25, 5.6, "R", ha="center", fontsize=12, color="black")
        ax.text(7.25, 4.2, f"{self.R} Ω", ha="center", fontsize=11, color="black")

        # Right vertical wire
        ax.plot([8.5, 8.5], [5, 1], linewidth=lw, color="black")

        # Capacitor plates (horizontal plates)
        ax.plot([8.1, 8.9], [3.2, 3.2], linewidth=lw, color="black")
        ax.plot([8.1, 8.9], [2.8, 2.8], linewidth=lw, color="black")
        ax.text(9.2, 3.0, "C", fontsize=12, color="black")
        ax.text(9.2, 2.4, f"{self.C*1e6:.0f} µF", fontsize=11, color="black")

        # Bottom wire
        ax.plot([8.5, 2], [1, 1], linewidth=lw, color="black")

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        dest_image_path = os.path.join(
            DESTINATION_FOLDER, f"image{num}.png"
        )

        plt.savefig(dest_image_path, dpi=600,
                    bbox_inches="tight", pad_inches=0.05)
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
    """
    Magnetic force on a current-carrying conductor
    placed at an angle in a uniform magnetic field.
    """

    def __init__(self):
        self.L = rnd.uniform(0.5, 2.0)          # length (m)
        self.I = rnd.uniform(0.3, 2.0)          # current (A)
        self.B = rnd.uniform(0.02, 0.1)         # magnetic flux density (T)
        self.theta_deg = rnd.choice([ 30, 40, 45, 60])
        self.theta = math.radians(self.theta_deg)

        self.force = self.B * self.I * self.L * math.sin(self.theta)
        self.answer = round(self.force, 3)

        self.description = (
            f"A straight conductor of length {self.L:.2f} m carries a current "
            f"of {self.I:.2f} A. It is placed at an angle of {self.theta_deg}° "
            f"to a uniform magnetic field of flux density {self.B:.3f} T. "
            f"Calculate the force acting on the conductor. (_) N"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"L &= {round(self.L,10)}\\,\\text{{m}}\\\\"
            f"I &= {round(self.I,10)}\\,\\text{{A}}\\\\"
            f"B &= {round(self.B,10)}\\,\\text{{T}}\\\\"
            f"\\theta &= {self.theta_deg}^\\circ\\\\[6pt]"
            "\\textbf{Step 2: Magnetic force formula}\\\\"
            "F &= B I L \\sin\\theta\\\\[6pt]"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"F &= ({round(self.B,10)})"
            f"({round(self.I,10)})"
            f"({round(self.L,10)})"
            f"\\sin({self.theta_deg}^\\circ)\\\\[6pt]"
            "\\textbf{Step 4: Compute force}\\\\"
            f"F &= {round(self.force,10)}\\,\\text{{N}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        lw = 2
        c = "black"

        # Magnetic field lines (horizontal arrows)
        for y in np.linspace(0.8, 5.2, 6):
            ax.plot([0.5, 9], [y, y], lw=1.2, color=c)
            ax.arrow(9, y, 0.5, 0, head_width=0.15,
                     head_length=0.3, fc=c, ec=c)

        # Conductor (tilted cylinder representation)
        x0, y0 = 2, 1
        x1 = 8
        y1 = y0 + (x1 - x0) * np.tan(self.theta)

        ax.plot([x0, x1], [y0, y1], lw=10, color="lightgray",
                solid_capstyle='round')
        ax.plot([x0, x1], [y0, y1], lw=2, color=c)

        # Angle arc
        angle = self.theta
        arc_x = np.linspace(0, angle, 100)
        radius = 1.5
        ax.plot(
            x0 + radius * np.cos(arc_x),
            y0 + radius * np.sin(arc_x),
            lw=1.5,
            color=c
        )
        ax.text(x0 + 1, y0 + 0.2, self.theta_deg, fontsize=12)
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy167:
    """
    Magnetic force on a current-carrying conductor
    placed at right angles to a uniform magnetic field.
    """

    def __init__(self):
        # Generate physically reasonable values
        self.B = rnd.randint(10, 30) * 1e-3      # T
        self.L = rnd.uniform(0.5, 2.0)           # m
        self.I = rnd.uniform(0.5, 3.0)           # A

        # Right angle so sin(90) = 1
        self.force = self.B * self.I * self.L
        self.answer = round(self.force, 3)

        self.description = (
            f"A current-carrying conductor is placed at right angles to a uniform magnetic field "
            f"of flux density {self.B:.3f} T. "
            f"The conductor has a length of {self.L:.2f} m and carries a current of {self.I:.2f} A. "
            f"Calculate the magnetic force acting on the conductor. (_) N"
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Save My Exam" 
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify known quantities}\\\\"
            f"B &= {round(self.B,10)}\\,\\text{{T}}\\\\"
            f"L &= {round(self.L,10)}\\,\\text{{m}}\\\\"
            f"I &= {round(self.I,10)}\\,\\text{{A}}\\\\[6pt]"
            "\\textbf{Step 2: Magnetic force formula}\\\\"
            "F &= BIL\\sin\\theta\\\\"
            "\\text{Since the conductor is at right angles, } \\sin 90^\\circ = 1\\\\[6pt]"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"F &= ({round(self.B,10)})({round(self.I,10)})({round(self.L,10)})\\\\[6pt]"
            "\\textbf{Step 4: Compute force}\\\\"
            f"F &= {round(self.force,10)}\\,\\text{{N}}\\\\[6pt]"
            "\\textbf{Final Answer:}\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        lw = 2
        c = "black"

        # Magnetic field lines (horizontal arrows)
        for y in np.linspace(1, 5, 5):
            ax.plot([0.5, 9], [y, y], lw=1.2, color=c)
            ax.arrow(9, y, 0.5, 0, head_width=0.15,
                     head_length=0.3, fc=c, ec=c)

        # Vertical conductor (right angles to field)
        ax.plot([5, 5], [1, 5], lw=10, color="lightgray",
                solid_capstyle='round')
        ax.plot([5, 5], [1, 5], lw=2, color=c)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy168:
    """
    Magnetic force on a current-carrying conductor placed at an angle 
    to a uniform magnetic field.
    """

    def __init__(self):
        # Generate clean physical values
        self.B_mT = rnd.randint(10, 25)          # mT
        self.B = self.B_mT * 1e-3                # convert to tesla
        self.L = rnd.uniform(0.8, 2.0)           # length in m
        self.L = round(self.L, 2)
        self.I = rnd.uniform(0.5, 3.0)           # current in A
        self.I = round(self.I, 2)
        self.theta = rnd.choice([15, 30, 45, 60])

        # Magnetic force formula: F = B I L sin(theta)
        self.force = self.B * self.I * self.L * math.sin(math.radians(self.theta))
        self.answer = round(self.force, 2)

        self.description = (
            "A current-carrying conductor is placed in a uniform magnetic field. "
            f"The magnetic flux density is {self.B_mT} × 10^{{-3}} T. "
            f"The conductor has a length of {self.L} m and carries a current of {self.I} A. "
            f"Calculate the magnetic force when the conductor makes an angle of {self.theta}° with the magnetic field. (_) N"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\textbf{{Step 1: Write the known quantities}} &\\\\"
            f"B &= {self.B_mT} \\times 10^{{-3}}\\,\\text{{T}}\\\\"
            f"L &= {round(self.L,10)}\\,\\text{{m}}\\\\"
            f"I &= {round(self.I,10)}\\,\\text{{A}}\\\\"
            f"\\theta &= {self.theta}^\\circ\\\\"
            f"\\textbf{{Step 2: Use the magnetic force formula}} &\\\\"
            f"F &= B I L \\sin\\theta\\\\"
            f"\\textbf{{Step 3: Substitute numerical values}} &\\\\"
            f"F &= ({self.B_mT} \\times 10^{{-3}})({round(self.I,10)})({round(self.L,10)})\\sin({self.theta}^\\circ)\\\\"
            f"\\textbf{{Step 4: Evaluate}} &\\\\"
            f"F &= {round(self.force,10)}\\,\\text{{N}}\\\\"
            f"\\textbf{{Final Answer:}} &\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw uniform magnetic field (into page with crosses in circles)
        for x in np.linspace(2, 8, 7):
            for y in np.linspace(2, 8, 7):
                circle = plt.Circle((x, y), 0.25, fill=False, linewidth=1)
                ax.add_patch(circle)
                ax.text(x, y, "×", fontsize=10, ha='center', va='center')

        # Draw conductor centered
        center = np.array([5, 5])
        length_scale = 5
        angle_rad = np.radians(self.theta)
        dx = length_scale * np.cos(angle_rad)
        dy = length_scale * np.sin(angle_rad)

        start = center - np.array([dx, dy]) / 2
        end = center + np.array([dx, dy]) / 2

        ax.plot([start[0], end[0]], [start[1], end[1]], linewidth=4)

        # Current direction arrow
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", linewidth=2))
        ax.text((start[0]+end[0])/2 + 0.3,
                (start[1]+end[1])/2 + 0.3,
                "I", fontsize=12)

        # Angle arc
        arc_theta = np.linspace(0, angle_rad, 100)
        arc_x = 5 + 1.5 * np.cos(arc_theta)
        arc_y = 5 + 1.5 * np.sin(arc_theta)
        ax.plot(arc_x, arc_y, linewidth=1.5)
        ax.text(6.7, 5.8, f"{self.theta}°", fontsize=11)

        # Magnetic field direction label
        ax.text(8.5, 9.2, "B (into page)", fontsize=11)

        # Parameter labels
        ax.text(0.8, 9.5, f"B = {self.B_mT} × 10⁻³ T", fontsize=11)
        ax.text(0.8, 8.9, f"I = {self.I} A", fontsize=11)
        ax.text(0.8, 8.3, f"L = {self.L} m", fontsize=11)
        
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy169:
    """
    Rectangular current-carrying loop in a uniform magnetic field.
    Ask for the magnitude of the magnetic force on one side.
    """

    def __init__(self):
        # Generate clean values
        self.B = round(rnd.uniform(0.4, 1.2), 2)           # Tesla
        self.width_cm = rnd.randint(4, 10)                 # cm
        self.length_cm = rnd.randint(6, 14)                # cm
        self.I = round(rnd.uniform(1.0, 5.0), 2)           # A

        # Convert to meters
        self.width = self.width_cm / 100
        self.length = self.length_cm / 100

        # Force on side perpendicular to field: F = B I L
        self.force = self.B * self.I * self.length
        self.answer = round(self.force, 2)

        self.description = (
            f"A rectangular wire loop ABCD has width {self.width_cm} cm and length {self.length_cm} cm "
            f"placed in a uniform magnetic field of strength {self.B} T. "
            f"The current in the loop is {self.I} A. "
            "Calculate the magnitude of the magnetic force on side AB. (_) N"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\textbf{{Step 1: Convert dimensions to SI units}} &\\\\"
            f"L &= {self.length_cm}\\,\\text{{cm}} = {round(self.length,10)}\\,\\text{{m}}\\\\"
            f"\\textbf{{Step 2: Write known quantities}} &\\\\"
            f"B &= {round(self.B,10)}\\,\\text{{T}}\\\\"
            f"I &= {round(self.I,10)}\\,\\text{{A}}\\\\"
            f"\\textbf{{Step 3: Use magnetic force formula}} &\\\\"
            f"F &= B I L\\\\"
            f"\\textbf{{Step 4: Substitute values}} &\\\\"
            f"F &= ({round(self.B,10)})({round(self.I,10)})({round(self.length,10)})\\\\"
            f"F &= {round(self.force,10)}\\,\\text{{N}}\\\\"
            f"\\textbf{{Final Answer:}} &\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')

        # Uniform Magnetic Field (horizontal lines with arrows) 
        for y in np.linspace(0.8, 7.2, 14):
            ax.plot([0.5, 13.5], [y, y], linewidth=0.8)
            ax.arrow(7, y, 0.8, 0,
                     head_width=0.15,
                     head_length=0.3,
                     length_includes_head=True)

        # Trapezoidal Loop Geometry
        A = (2.0, 2.0)
        B = (4.5, 4.0)
        C = (8.0, 4.0)
        D = (10.5, 2.0)

        # Draw sides
        ax.plot([A[0], B[0]], [A[1], B[1]], linewidth=2.5)
        ax.plot([B[0], C[0]], [B[1], C[1]], linewidth=2.5)
        ax.plot([C[0], D[0]], [C[1], D[1]], linewidth=2.5)
        ax.plot([D[0], A[0]], [D[1], A[1]], linewidth=2.5)

        # Current Direction Arrows 
        ax.annotate("", xy=B, xytext=A, arrowprops=dict(arrowstyle="->", linewidth=2))
        ax.annotate("", xy=C, xytext=B, arrowprops=dict(arrowstyle="->", linewidth=2))
        ax.annotate("", xy=D, xytext=C, arrowprops=dict(arrowstyle="->", linewidth=2))
        ax.annotate("", xy=A, xytext=D, arrowprops=dict(arrowstyle="->", linewidth=2))

        #  Dimension: Top (width) 
        ax.annotate("", xy=(B[0], B[1] + 0.6), xytext=(C[0], C[1] + 0.6),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.5))
        ax.text((B[0] + C[0]) / 2 - 0.6, B[1] + 0.9,
                f"{self.width_cm:.1f} cm", fontsize=12)

        #  Dimension: Left slanted side (length) 
        ax.annotate("", xy=A, xytext=B,
                    arrowprops=dict(arrowstyle="<->", linewidth=1.5))
        mid_x = (A[0] + B[0]) / 2 - 0.8
        mid_y = (A[1] + B[1]) / 2
        ax.text(mid_x, mid_y,
                f"{self.length_cm:.1f} cm", fontsize=12, rotation=28)

        # Current label 
        ax.text(8.5, 1.6, f"{self.I} A", fontsize=12)

        # Corner Labels
        ax.text(A[0] - 0.3, A[1] - 0.3, "A", fontsize=12)
        ax.text(B[0] - 0.2, B[1] + 0.2, "B", fontsize=12)
        ax.text(C[0] + 0.1, C[1] + 0.2, "C", fontsize=12)
        ax.text(D[0] + 0.1, D[1] - 0.3, "D", fontsize=12)

        #  Magnetic Field Strength Label 
        ax.text(1.0, 7.5, f"B = {self.B} T", fontsize=12)
        
        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy170:
    """
    Radius of circular motion of an electron in a uniform magnetic field.
    """

    def __init__(self):
        # Physical constants
        self.m = 9.11e-31          # electron mass (kg)
        self.q = 1.60e-19          # electron charge magnitude (C)

        # Generate clean scientific values
        self.v_base = rnd.randint(2, 6)          # multiplier for 10^6
        self.v = self.v_base * 1e6               # m/s

        self.B_base = rnd.randint(2, 6)          # multiplier for 10^-3
        self.B = self.B_base * 1e-3              # Tesla

        # Radius formula
        self.r = (self.m * self.v) / (self.B * self.q)
        self.answer = round(self.r, 3)

        self.description = (
            f"When the electron enters the magnetic field, its speed is "
            f"{self.v_base} × 10^6 m s^(-1). "
            f"The magnetic field has a magnetic flux density of "
            f"{self.B_base} × 10^(-3) T. "
            "Show that the radius of the circular orbit of the electron "
            "inside the magnetic field is equal to (_) m."
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a moving charge"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Write known quantities} &\\\\"
            "m &= 9.11 \\times 10^{-31}\\,\\text{kg}\\\\"
            "q &= 1.60 \\times 10^{-19}\\,\\text{C}\\\\"
            f"v &= {self.v_base} \\times 10^6\\,\\text{{m s^{{-1}}}}\\\\"
            f"B &= {self.B_base} \\times 10^{{-3}}\\,\\text{{T}}\\\\"
            "\\text{Step 2: Magnetic force provides centripetal force} &\\\\"
            "Bqv &= \\frac{mv^2}{r}\\\\"
            "\\text{Step 3: Rearrange for radius} &\\\\"
            "r &= \\frac{mv}{Bq}\\\\"
            "\\text{Step 4: Substitute values} &\\\\"
            f"r &= \\frac{{(9.11 \\times 10^{{-31}})"
            f"({self.v_base} \\times 10^6)}}"
            f"{{({self.B_base} \\times 10^{{-3}})"
            "(1.60 \\times 10^{-19})}}\\\\"
            "\\text{Step 5: Evaluate numerically} &\\\\"
            f"r &= {round(self.r,10)}\\,\\text{{m}}\\\\"
            "\\text{Final Answer:} &\\\\"
            f"r &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        # Magnetic field into page (crosses)
        for x in np.linspace(-4, 4, 9):
            for y in np.linspace(-4, 4, 9):
                ax.text(x, y, "×", fontsize=10, ha='center', va='center')

        # Circular path
        circle = plt.Circle((0, 0), 2.5, fill=False, linewidth=2)
        ax.add_patch(circle)

        # Velocity arrow (tangent)
        ax.arrow(2.5, 0, 0, 1.2,
                 head_width=0.3,
                 head_length=0.4,
                 length_includes_head=True)

        ax.text(2.8, 1.2, "v", fontsize=12)

        # Radius line
        ax.plot([0, 2.5], [0, 0], linewidth=1.5)
        ax.text(1.2, -0.4, "r", fontsize=12)

        ax.text(-4.5, 4.5, f"B = {self.B_base} × 10⁻³ T", fontsize=11)
        ax.text(-4.5, 4.0, f"v = {self.v_base} × 10⁶ m s⁻¹", fontsize=11)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=600,
            bbox_inches="tight",
            pad_inches=0.05
        )
        plt.close()

class Phy173:
    """
    Magnetic force on a moving charge in a uniform magnetic field.
    """

    def __init__(self):
        self.q_base = rnd.randint(2, 9)
        self.q = self.q_base * 1e-19

        self.v_base = rnd.randint(2, 8)
        self.v = self.v_base * 1e6

        self.B_base = rnd.randint(2, 8)
        self.B = self.B_base * 1e-3

        self.theta = rnd.choice([30, 45, 60, 90])

        self.F = self.q * self.v * self.B * math.sin(math.radians(self.theta))
        self.answer = round(self.F, 3)

        self.description = (
            f"A charged particle of charge {self.q_base} × 10^(-19) C "
            f"moves with speed {self.v_base} × 10^6 m s^(-1) "
            f"in a magnetic field of {self.B_base} × 10^(-3) T "
            f"at an angle of {self.theta}°. "
            "Calculate the magnetic force acting on the particle. (_) N"
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a moving charge"
        self.curriculum = "A-Level"
        self.source = "Original"
        self.reasoning = (
            "\\begin{aligned}"
            f"\\text{{Step 1: Identify given values}} & \\\\"
            f"q &= {self.q_base} \\times 10^{{-19}} \\, \\text{{C}} \\\\"
            f"v &= {self.v_base} \\times 10^{{6}} \\, \\text{{m s}}^{{-1}} \\\\"
            f"B &= {self.B_base} \\times 10^{{-3}} \\, \\text{{T}} \\\\"
            f"\\theta &= {self.theta}^\\circ \\\\"
            f"\\text{{Step 2: Apply the magnetic force formula}} & \\\\"
            f"F &= q v B \\sin(\\theta) \\\\"
            f"\\text{{Step 3: Substitute the values into the equation}} & \\\\"
            f"F &= ({self.q_base} \\times 10^{{-19}}) ({self.v_base} \\times 10^{{6}}) ({self.B_base} \\times 10^{{-3}}) \\sin({self.theta}^\\circ) \\\\"
            f"\\text{{Step 4: Calculate intermediate product}} & \\\\"
            f"qvB &= {round(self.q * self.v * self.B, 10)} \\, \\text{{N}} \\\\"
            f"\\text{{Step 5: Multiply by }} \\sin({self.theta}^\\circ) \\text{{ for final force}} & \\\\"
            f"F &= {round(self.F, 10)} \\, \\text{{N}} \\\\"
            f"\\text{{Final Answer:}} & \\\\"
            f"F &= {self.answer} \\, \\text{{N}}"
            "\\end{aligned}"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7,7))
        ax.set_xlim(-4,4)
        ax.set_ylim(-4,4)
        ax.set_aspect('equal')
        ax.axis('off')

        grid = np.linspace(-3,3,9)
        for x in grid:
            for y in grid:
                ax.text(x, y, r"$\times$", ha='center', va='center', fontsize=14)

        particle = Circle((0,0), 0.25, edgecolor='black', facecolor='white', linewidth=1.5)
        ax.add_patch(particle)
        ax.text(0, 0, r"$q$", ha='center', va='center', fontsize=12)

        angle_rad = np.radians(self.theta)
        vx = 2.5 * np.cos(angle_rad)
        vy = 2.5 * np.sin(angle_rad)

        ax.arrow(0,0,vx,vy,
                head_width=0.25,
                head_length=0.35,
                linewidth=2,
                length_includes_head=True)
        ax.text(vx*1.1, vy*1.1, r"$v$", fontsize=14)

        arc = Arc((0,0), 1.5, 1.5, angle=0,
                theta1=0,
                theta2=self.theta,
                linewidth=1.5)
        ax.add_patch(arc)
        ax.text(0.9*np.cos(angle_rad/2),
                0.9*np.sin(angle_rad/2),
                r"$\theta$",
                fontsize=13)
        ax.text(-3.7, 3.3,
                rf"$B = {self.B_base}\times10^{{-3}}\ \mathrm{{T}}$",
                fontsize=13)

        # --- Title ---
        ax.text(0,3.7,
                "Charged Particle in Uniform Magnetic Field",
                ha='center',
                fontsize=14)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)

        plt.savefig(
            os.path.join(DESTINATION_FOLDER, f"image{num}.png"),
            dpi=800,
            bbox_inches="tight",
            pad_inches=0.1
        )
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
    """
    Faraday's law of electromagnetic induction.
    """

    def __init__(self):
        self.N = rnd.randint(50,300)
        self.dPhi = round(rnd.uniform(0.001,0.01),4)
        self.dt = round(rnd.uniform(0.01,0.05),3)

        self.emf = self.N * (self.dPhi/self.dt)
        self.answer = round(self.emf,2)

        self.description = (
            f"A coil of {self.N} turns experiences a change in magnetic flux "
            f"of {self.dPhi} Wb in {self.dt} s. "
            "Calculate the induced emf. (_) V"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic Induction"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Write known quantities} &\\\\"
            f"N &= {self.N}\\\\"
            f"\\Delta \\Phi &= {round(self.dPhi,10)}\\,\\text{{Wb}}\\\\"
            f"\\Delta t &= {round(self.dt,10)}\\,\\text{{s}}\\\\"
            "\\text{Step 2: Use Faraday's law} &\\\\"
            "\\mathcal{E} &= N\\frac{\\Delta \\Phi}{\\Delta t}\\\\"
            "\\text{Step 3: Substitute values} &\\\\"
            f"\\mathcal{{E}} &= {self.N}\\frac{{{round(self.dPhi,10)}}}{{{round(self.dt,10)}}}\\\\"
            "\\text{Step 4: Evaluate} &\\\\"
            f"\\mathcal{{E}} &= {round(self.emf,10)}\\,\\text{{V}}\\\\"
            "\\text{Final Answer:} &\\\\"
            f"\\mathcal{{E}} &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim(-2, 2)
        ax.set_ylim(-1, 1)
        ax.axis('off')

        # Draw Solenoid/Coil
        t = np.linspace(0, 10 * np.pi, 500)
        x = 0.5 * np.cos(t)
        y = np.linspace(-0.5, 0.5, 500)
        ax.plot(x, y, color='silver', linewidth=2, label='Coil')
        
        # Magnetic Flux lines (arrows)
        for i in np.linspace(-0.4, 0.4, 5):
            ax.annotate('', xy=(0.8, i), xytext=(-0.8, i),
                        arrowprops=dict(arrowstyle='->', color='black', alpha=0.6))

        ax.text(-1.8, 0.8, f"N = {self.N} turns")
        ax.text(-1.8, 0.6, f"ΔΦ = {self.dPhi} Wb", color='black')

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy176:
    """
    Peak emf induced in a rotating coil (AC generator).
    """

    def __init__(self):
        self.N = rnd.randint(100, 500)
        self.B = round(rnd.uniform(0.2, 1.0), 2)
        self.A = round(rnd.uniform(0.002, 0.01), 4)
        self.f = rnd.randint(10, 60)

        self.omega = 2 * math.pi * self.f
        self.emf_peak = self.N * self.B * self.A * self.omega
        self.answer = round(self.emf_peak, 2)

        self.description = (
            f"A coil of {self.N} turns and area {self.A} m^2 rotates "
            f"in a magnetic field of {self.B} T at a frequency of {self.f} Hz. "
            "Calculate the peak induced emf. (_) V"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic induction"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: Identify given values}} &\\\\"
            f"N &= {self.N} \\text{{ turns}} \\\\"
            f"B &= {round(self.B, 10)}\\,\\text{{T}} \\\\"
            f"A &= {round(self.A, 10)}\\,\\text{{m}}^2 \\\\"
            f"f &= {self.f}\\,\\text{{Hz}} \\\\"
            f"\\text{{Step 2: Calculate angular frequency (}} \\omega \\text{{)}} &\\\\"
            f"\\omega &= 2\\pi f \\\\"
            f"&= 2 \\times \\pi \\times {self.f} \\\\"
            f"&= {round(self.omega, 10)}\\,\\text{{rad s}}^{{-1}} \\\\"
            f"\\text{{Step 3: Apply peak emf formula}} &\\\\"
            f"\\mathcal{{E}}_{{\\text{{max}}}} &= NBA\\omega \\\\"
            f"&= ({self.N})({round(self.B, 10)})({round(self.A, 10)})({round(self.omega, 10)}) \\\\"
            f"\\text{{Step 4: Evaluate the result}} &\\\\"
            f"\\mathcal{{E}}_{{\\text{{max}}}} &= {round(self.emf_peak, 10)}\\,\\text{{V}} \\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"\\mathcal{{E}}_{{\\text{{max}}}} &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2, 2)
        ax.axis('off')

        # Draw Magnet Poles
        ax.add_patch(plt.Rectangle((-3, -1), 1, 2, color='red', alpha=0.3)) # North
        ax.add_patch(plt.Rectangle((2, -1), 1, 2, color='blue', alpha=0.3)) # South
        ax.text(-2.7, 0, 'N', fontsize=15, fontweight='bold')
        ax.text(2.3, 0, 'S', fontsize=15, fontweight='bold')

        # Draw Rotating Coil (Perspective)
        ax.plot([-1, 1, 0.5, -1.5, -1], [0.5, 0.5, -0.5, -0.5, 0.5], color='black', linewidth=2)
        
        # Rotation Arrow
        ax.annotate('', xy=(0, 0.8), xytext=(-0.5, 0.5),
                    arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.5", color='green', lw=2))
        ax.text(0.1, 0.9, "ω", color='green', fontsize=12)

        ax.text(-2.8, 1.5, f"B = {self.B} T", fontsize=9)
        ax.text(-2.8, 1.3, f"f = {self.f} Hz", fontsize=9)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
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
    """
    Energy of a photon.
    """

    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(4, 9)
        self.f = self.f_base * 1e14

        self.E = self.h * self.f
        self.answer = round(self.E, 3)

        self.description = (
            f"Calculate the energy of a photon with frequency "
            f"{self.f_base} × 10^{{14}} Hz. "
            f"Take Planck's constant h = 6.63 × 10^{{-34}} J s. (_) J"
        )

        self.topic = "Quantum physics"
        self.subtopic = "Energy and momentum of a photon"
        self.curriculum = "A-Level"
        self.source = "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: State the photon energy formula}} &\\\\"
            f"E &= hf \\\\"
            f"\\text{{Step 2: Identify constants and variables}} &\\\\"
            f"h &= 6.63 \\times 10^{{-34}}\\,\\text{{J s}} \\\\"
            f"f &= {self.f_base} \\times 10^{{14}}\\,\\text{{Hz}} \\\\"
            f"\\text{{Step 3: Substitute and evaluate}} &\\\\"
            f"E &= (6.63 \\times 10^{{-34}})( {self.f_base} \\times 10^{{14}} ) \\\\"
            f"E &= {round(self.E, 10)}\\,\\text{{J}} \\\\"
            f"\\text{{Final Answer:}} &\\\\"
            f"E &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Creating a localized wave packet to represent a photon
        x = np.linspace(0, 12, 1000)
        envelope = np.exp(-(x-6)**2 / 4)
        wave = envelope * np.sin(2 * np.pi * x * 1.5)
        
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(x, wave, color='orange', linewidth=2, label='Photon Energy Packet')
        
        # Adding descriptive text to the image
        ax.text(1, 0.8, f"f = {self.f_base} $\\times$ 10$^{{14}}$ Hz", fontsize=10, fontweight='bold')
        ax.text(1, 0.5, f"h = 6.63 $\\times$ 10$^{{-34}}$ J s", fontsize=10)
        
        ax.set_ylim(-1.2, 1.2)
        ax.set_xlim(0, 12)
        ax.axis('off')
        ax.set_title("Photon Energy Model", fontsize=12, pad=10)

        os.makedirs(DESTINATION_FOLDER, exist_ok=True)
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=600, bbox_inches="tight")
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
        ax.set_title("De Broglie Wavelength and Photon Momentum", fontsize=11)

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
    """Photoelectric effect: stopping potential."""
    def __init__(self):
        self.e = 1.60e-19
        self.Ek_base = rnd.randint(2, 9)
        self.Ek = self.Ek_base * 1e-19
        self.Vs = self.Ek / self.e
        self.answer = round(self.Vs, 2)

        self.description = (
            f"The maximum kinetic energy of emitted electrons is {self.Ek_base} × 10^{{-19}} J. "
            "Calculate the stopping potential. (_) V"
        )
        self.topic, self.subtopic = "Quantum physics", "Photoelectric effect"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Energy relation} &\\\\"
            "E_{k, \\text{max}} &= eV_s \\\\"
            "\\text{Step 2: Rearrange for } V_s &\\\\"
            "V_s &= \\frac{E_k}{e} \\\\"
            "\\text{Step 3: Substitute values} &\\\\"
            f"V_s &= \\frac{{{self.Ek_base} \\times 10^{{-19}}}}{{1.60 \\times 10^{{-19}}}} \\\\"
            "\\text{Final Answer:} &\\\\"
            f"V_s &= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([1, 4], [0, 3], color='red', lw=2, label='$E_k = hf - \Phi$')
        ax.axhline(0, color='black', lw=1); ax.axvline(1, color='black', lw=1)
        ax.set_xlabel("Frequency ($f$)"); ax.set_ylabel("Max Kinetic Energy ($E_k$)")
        ax.text(2, 2.5, f"Given $E_k = {self.Ek_base} \\times 10^{{-19}}$ J", color='red', fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()



class Phy184:
    """De Broglie wavelength of a particle."""
    def __init__(self):
        self.h, self.m = 6.63e-34, 9.11e-31
        self.v_base = rnd.randint(1, 5)
        self.v = self.v_base * 1e6
        self.lambda_val = self.h / (self.m * self.v)
        self.answer = round(self.lambda_val, 12)

        self.description = (
            f"An electron moves with a speed of {self.v_base} × 10^6 m s^{{-1}}. "
            "Calculate its de Broglie wavelength. (_) m"
        )
        self.topic, self.subtopic = "Quantum physics", "Wave-particle duality"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: De Broglie equation} &\\\\"
            "\\lambda &= \\frac{h}{mv} \\\\"
            "\\text{Step 2: Substitute values} &\\\\"
            f"\\lambda &= \\frac{{6.63 \\times 10^{{-34}}}}{{(9.11 \\times 10^{{-31}})({self.v_base} \\times 10^6)}} \\\\"
            "\\text{Step 3: Evaluate result} &\\\\"
            f"\\lambda &= {self.lambda_val:.4e}\\,\\text{{m}} \\\\"
            "\\text{Final Answer:} &\\\\"
            f"\\lambda &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        x = np.linspace(0, 10, 1000)
        y = np.exp(-(x-5)**2/5) * np.sin(2*np.pi*x*1.2)
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(x, y, color='purple', lw=2)
        ax.text(5, 1.2, f"Electron speed $v = {self.v_base} \\times 10^6$ m/s", ha='center', fontweight='bold')
        ax.set_ylim(-1.5, 1.5); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()



class Phy185:
    """Energy difference between atomic levels."""
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(4, 8)
        self.f = self.f_base * 1e14
        self.E = self.h * self.f
        self.answer = round(self.E, 22)

        self.description = (
            f"An electron transition emits radiation of frequency {self.f_base} × 10^{{14}} Hz. "
            "Calculate the energy difference between the levels. (_) J"
        )
        self.topic, self.subtopic = "Quantum physics", "Energy levels"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Photon energy formula} &\\\\"
            "\\Delta E &= hf \\\\"
            "\\text{Step 2: Substitute values} &\\\\"
            f"\\Delta E &= (6.63 \\times 10^{{-34}})({self.f_base} \\times 10^{{14}}) \\\\"
            "\\text{Final Answer:} &\\\\"
            f"\\Delta E &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hlines([1, 3], 1, 4, colors='black', lw=2.5)
        ax.annotate('', xy=(2.5, 1.1), xytext=(2.5, 2.9), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        ax.text(4.2, 3, "$E_{high}$"); ax.text(4.2, 1, "$E_{low}$")
        ax.text(1, 2, f"Transition frequency:\n$f = {self.f_base}\\times 10^{{14}}$ Hz", color='red')
        ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()



class Phy186:
    """Wavelength of emitted spectral line."""
    def __init__(self):
        self.h, self.c = 6.63e-34, 3.00e8
        self.E_base = rnd.randint(2, 9)
        self.E = self.E_base * 1e-19
        self.lambda_val = (self.h * self.c) / self.E
        self.answer = round(self.lambda_val, 12)

        self.description = (
            f"An electron transition releases energy of {self.E_base} × 10^{{-19}} J. "
            "Calculate the wavelength of the emitted photon. (_) m"
        )
        self.topic, self.subtopic = "Quantum physics", "Line spectra"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Photon energy equation} &\\\\"
            "E &= \\frac{hc}{\\lambda} \\\\"
            "\\text{Step 2: Rearrange for wavelength} &\\\\"
            "\\lambda &= \\frac{hc}{E} \\\\"
            "\\text{Step 3: Substitute values} &\\\\"
            f"\\lambda &= \\frac{{(6.63 \\times 10^{{-34}})(3.00 \\times 10^8)}}{{{self.E_base} \\times 10^{{-19}}}} \\\\"
            "\\text{Final Answer:} &\\\\"
            f"\\lambda &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hlines([1, 3], 1, 4, colors='black', lw=2.5)
        ax.annotate('', xy=(2.5, 1.1), xytext=(2.5, 2.9), arrowprops=dict(arrowstyle='->', color='green', lw=2))
        ax.text(1, 2, f"Energy released:\n$\Delta E = {self.E_base} \\times 10^{{-19}}$ J", color='green')
        ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()

class Phy187:
    """
    Mass defect calculation.
    """
    def __init__(self):
        self.mp = 1.6726e-27
        self.mn = 1.6749e-27
        self.A = rnd.randint(10, 30)
        self.Z = rnd.randint(5, self.A - 5)
        self.N = self.A - self.Z

        self.mass_nucleons = (self.Z * self.mp) + (self.N * self.mn)
        # Simulating a realistic nucleus mass (slightly less than nucleons)
        self.mass_nucleus = self.mass_nucleons - rnd.uniform(1e-29, 5e-29)

        self.mass_defect = self.mass_nucleons - self.mass_nucleus
        self.answer = round(self.mass_defect, 30)

        self.description = (
            f"A nucleus has a mass number A = {self.A} and atomic number Z = {self.Z}. "
            f"The measured mass of the nucleus is {self.mass_nucleus:.4e} kg. "
            "Calculate the mass defect. (Take $m_p = 1.67 \times 10^{{-27}}$ kg and $m_n = 1.67 \times 10^{{-27}}$ kg). (_) kg"
        )

        self.topic, self.subtopic = "Nuclear physics", "Mass defect and binding energy"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Calculate mass of individual nucleons}} &\\\\"
            f"m_{{\\text{{total}}}} &= Zm_p + (A-Z)m_n \\\\"
            f"m_{{\\text{{total}}}} &= {self.Z}(1.67 \\times 10^{{-27}}) + {self.N}(1.67 \\times 10^{{-27}}) \\\\"
            f"m_{{\\text{{total}}}} &= {self.mass_nucleons:.4e}\\,\\text{{kg}} \\\\"
            "\\text{{Step 2: Calculate mass defect (}}\\Delta m\\text{{)}} &\\\\"
            "\\Delta m &= m_{\\text{nucleons}} - m_{\\text{nucleus}} \\\\"
            f"\\Delta m &= {self.mass_nucleons:.4e} - {self.mass_nucleus:.4e} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"\\Delta m &= {self.answer:.4e}\\,\\text{{kg}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        for _ in range(self.Z): # Protons
            ax.scatter(rnd.uniform(1.8, 3.2), rnd.uniform(1.8, 3.2), color='red', s=100, edgecolors='black', alpha=0.7)
        for _ in range(self.N): # Neutrons
            ax.scatter(rnd.uniform(1.8, 3.2), rnd.uniform(1.8, 3.2), color='blue', s=100, edgecolors='black', alpha=0.7)
        
        ax.text(2.5, 3.6, f"Nucleus (A={self.A}, Z={self.Z})", ha='center', fontweight='bold', fontsize=12)
        ax.text(0.5, 0.5, f"Measured Mass: {self.mass_nucleus:.4e} kg", fontsize=9, bbox=dict(facecolor='white', alpha=0.8))
        ax.set_xlim(0, 5); ax.set_ylim(0, 4); ax.axis('off')
        
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
    """Wavelength of ultrasound."""
    def __init__(self):
        self.v = 1540
        self.f_mhz = rnd.randint(2, 12)
        self.f = self.f_mhz * 1e6
        self.lambda_val = self.v / self.f
        self.answer = round(self.lambda_val, 6)

        self.description = (
            f"An ultrasound transducer operates at a frequency of {self.f_mhz} MHz. "
            f"Given the speed of sound in tissue is 1540 m s$^{{-1}}$, "
            f"calculate its wavelength. (_) m"
        )
        self.topic, self.subtopic = "Medical physics", "Production and use of ultrasound"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Apply the wave equation}} &\\\\"
            "v &= f\\lambda \\implies \\lambda = \\frac{{v}}{{f}} \\\\"
            "\\text{{Step 2: Convert frequency to Hz}} &\\\\"
            f"f &= {self.f_mhz} \\times 10^6\\,\\text{{Hz}} \\\\"
            "\\text{{Step 3: Substitute values}} &\\\\"
            f"\\lambda &= \\frac{{1540}}{{{self.f_mhz} \\times 10^6}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"\\lambda &= {self.answer:.2e}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        x = np.linspace(0, 10, 500)
        y = np.sin(2 * np.pi * 0.5 * x)
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(x, y, color='purple', lw=2)
        # Indicate wavelength
        ax.annotate('', xy=(2, 1.2), xytext=(4, 1.2), arrowprops=dict(arrowstyle='<->'))
        ax.text(3, 1.4, "Wavelength ($\lambda$)", ha='center')
        ax.text(0, -1.8, f"Frequency: {self.f_mhz} MHz\nSpeed: 1540 m/s", fontsize=9, fontweight='bold')
        ax.set_ylim(-2, 2); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()



class Phy193:
    """X-ray photon energy."""
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(5, 20)
        self.f = self.f_base * 1e18
        self.E = self.h * self.f
        self.answer = round(self.E, 22)

        self.description = (
            f"Calculate the energy of an X-ray photon with a frequency of "
            f"{self.f_base} × 10$^{{18}}$ Hz. (_) J"
        )
        self.topic, self.subtopic = "Medical physics", "Production and use of ultrasound"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Use the photon energy formula}} &\\\\"
            "E &= hf \\\\"
            "\\text{{Step 2: Substitute Planck's constant and frequency}} &\\\\"
            f"E &= (6.63 \\times 10^{{-34}})({self.f_base} \\times 10^{{18}}) \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"E &= {self.E:.4e}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        # Photon wave representation
        x = np.linspace(0, 4, 100)
        y = 2 + 0.3 * np.sin(10 * x)
        ax.plot(x, y, color='orange', lw=2)
        ax.annotate('', xy=(4.5, 2), xytext=(4, 2), arrowprops=dict(arrowstyle='->', color='orange', lw=2))
        ax.text(0.5, 2.5, f"$f = {self.f_base} \\times 10^{{18}}$ Hz", fontweight='bold')
        ax.text(0.5, 1.5, "X-ray Photon Energy ($E$)", color='darkred')
        ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
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
    """Distance to a star using inverse square law."""
    def __init__(self):
        self.L_base = rnd.randint(2, 9)
        self.L = self.L_base * 1e26
        self.I_base = rnd.randint(1, 9)
        self.I = self.I_base * 1e-10
        self.d = math.sqrt(self.L / (4 * math.pi * self.I))
        self.answer = round(self.d, 3)
        self.description = (f"A star has luminosity {self.L_base} × 10$^{{26}}$ W. "
                            f"The observed intensity on Earth is {self.I_base} × 10^{{-10}} W m$^{{-2}}$. "
                            "Calculate the distance to the star. (_) m")
        self.topic, self.subtopic = "Astronomy and Cosmology", "Standard candles"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Inverse square law}} &\\quad I = \\frac{{L}}{{4\\pi d^2}} \\\\"
            "\\text{{Step 2: Rearrange for }} d &\\quad d = \\sqrt{{\\frac{{L}}{{4\\pi I}}}} \\\\"
            "\\text{{Step 3: Substitute}} &\\quad d = \\sqrt{{\\frac{{{self.L_base} \\times 10^{{26}}}}{{4\\pi({self.I_base} \\times 10^{{-10}})}}}} \\\\"
            "\\text{{Final Answer:}} &\\quad d = {self.answer:,.2f}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')
        ax.set_facecolor('black')
        
        # Star glow effect
        for i in range(15, 0, -1):
            ax.add_patch(plt.Circle((0.5, 2), 0.1 + i*0.04, color='white', alpha=0.03))
        ax.add_patch(plt.Circle((0.5, 2), 0.1, color='white', zorder=5))
        
        # Observer/Earth
        ax.add_patch(plt.Circle((4.5, 2), 0.05, color='white', alpha=0.8, zorder=5))
        
        # Light spreading lines (technical style)
        angles = np.linspace(-0.5, 0.5, 5)
        for ang in angles:
            ax.plot([0.5, 4.5], [2, 2 + ang], color='white', lw=0.5, alpha=0.4, ls='--')

        # Distance measurement line
        ax.annotate('', xy=(4.5, 1.3), xytext=(0.5, 1.3),
                    arrowprops=dict(arrowstyle='<->', color='white', lw=1))
        ax.text(2.5, 1.0, f"Distance $d = ?$ m", color='white', ha='center', fontsize=11)
        
        # Parameter Labels
        ax.text(0.5, 2.6, f"Luminosity ($L$)\n{self.L_base}e26 W", color='white', ha='center', fontsize=9)
        ax.text(4.5, 2.6, f"Intensity ($I$)\n{self.I_base}e-10 W/m²", color='white', ha='center', fontsize=9)

        ax.set_xlim(0, 5); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

# class Phy196:
#     """
#     Stellar radius using Stefan-Boltzmann law.
#     """
#     def __init__(self):
#         self.sigma = 5.67e-8
#         self.L_base = rnd.randint(2, 9)
#         self.L = self.L_base * 1e26
#         self.T = rnd.randint(3000, 8000)

#         self.R = math.sqrt(self.L / (4 * math.pi * self.sigma * self.T**4))
#         self.answer = round(self.R, 3)

#         self.description = (
#             f"A star has a luminosity of {self.L_base} × 10$^{{26}}$ W "
#             f"and a surface temperature of {self.T} K. "
#             "Calculate the radius of the star. (_) m"
#         )

#         self.topic, self.subtopic = "Astronomy and cosmology", "Stellar radii"
#         self.curriculum, self.source = "A-Level", "Original"

#         self.reasoning = (
#             "\\[\\begin{aligned}"
#             "\\text{{Step 1: State Stefan-Boltzmann law}} &\\\\"
#             "L &= 4\\pi R^2 \\sigma T^4 \\\\"
#             "\\text{{Step 2: Rearrange for radius }} R &\\\\"
#             "R &= \\sqrt{{\\frac{{L}}{{4\\pi \\sigma T^4}}}} \\\\"
#             "\\text{{Step 3: Substitute values}} &\\\\"
#             f"R &= \\sqrt{{\\frac{{{self.L_base} \\times 10^{{26}}}}{{4\\pi(5.67 \\times 10^{{-8}})({self.T}^4)}}}} \\\\"
#             "\\text{{Step 4: Calculate result}} &\\\\"
#             f"R &= {self.R:.4e}\\,\\text{{m}} \\\\"
#             "\\text{{Final Answer:}} &\\\\"
#             f"R &= {self.answer:,.2f}\\,\\text{{m}}"
#             "\\end{aligned}\\]"
#         )

#     def generate(self, num):
#         fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
#         ax.set_facecolor('black')
#         for i in range(50, 0, -1):
#             alpha = 0.01 + (i/200)
#             ax.add_patch(plt.Circle((3, 3), (i/50)*1.5, color='white', alpha=alpha, lw=0))
#         ax.annotate('', xy=(3 + 1.5, 3), xytext=(3, 3),
#                     arrowprops=dict(arrowstyle='->', color='white', lw=2))
#         ax.text(3.75, 3.2, "Radius ($R$)", color='white', ha='center', fontweight='bold')
#         ax.text(3, 0.8, f"L = {self.L_base}e26 W\nT = {self.T} K", 
#                 color='white', ha='center', fontsize=12, 
#                 bbox=dict(facecolor='black', edgecolor='white', pad=10))
#         ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.axis('off')
#         plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
#         plt.close()

# class Phy197:
#     """
#     Surface temperature from luminosity and radius.
#     """
#     def __init__(self):
#         self.sigma = 5.67e-8
#         self.L_base = rnd.randint(2, 9)
#         self.L = self.L_base * 1e26
#         self.R_val = rnd.randint(5, 20)
#         self.R = self.R_val * 1e8

#         self.T = ((self.L) / (4 * math.pi * self.sigma * self.R**2))**0.25
#         self.answer = round(self.T, 2)

#         self.description = (
#             f"A star has a luminosity of {self.L_base} × 10$^{{26}}$ W "
#             f"and a radius of {self.R_val} × 10$^{{8}}$ m. "
#             "Calculate its surface temperature. (_) K"
#         )

#         self.topic, self.subtopic = "Astronomy and cosmology", "Stellar radii"
#         self.curriculum, self.source = "A-Level", "Original"

#         self.reasoning = (
#             "\\[\\begin{aligned}"
#             "\\text{{Step 1: Stefan-Boltzmann law}} &\\\\"
#             "L &= 4\\pi R^2 \\sigma T^4 \\\\"
#             "\\text{{Step 2: Rearrange for temperature }} T &\\\\"
#             "T &= \\sqrt[4]{{\\frac{{L}}{{4\\pi R^2 \\sigma}}}} \\\\"
#             "\\text{{Step 3: Substitute values}} &\\\\"
#             f"T &= \\left( \\frac{{{self.L_base} \\times 10^{{26}}}}{{4\\pi({self.R_val} \\times 10^{{8}})^2(5.67 \\times 10^{{-8}})}} \\right)^{{1/4}} \\\\"
#             "\\text{{Step 4: Calculate result}} &\\\\"
#             f"T &= {self.T:.2f}\\,\\text{{K}} \\\\"
#             "\\text{{Final Answer:}} &\\\\"
#             f"T &= {self.answer}\\,\\text{{K}}"
#             "\\end{aligned}\\]"
#         )

#     def generate(self, num):
#         fig, ax = plt.subplots(figsize=(7, 5), facecolor='black')
#         ax.set_facecolor('black')
#         x_core, y_core = 3, 2.5
#         r_star = 0.8
#         ax.add_patch(plt.Circle((x_core, y_core), r_star, facecolor='white', zorder=10))
#         for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
#             t = np.linspace(r_star, r_star + 1.2, 50)
#             x = x_core + t * np.cos(angle) + 0.1 * np.sin(20*t) * np.sin(angle)
#             y = y_core + t * np.sin(angle) + 0.1 * np.sin(20*t) * np.cos(angle)
#             ax.plot(x, y, color='white', lw=1, alpha=0.6)
#         ax.text(x_core, y_core - 1.8, f"Find Temperature ($T$)", color='white', ha='center', fontsize=14, fontweight='bold')
#         ax.text(0.5, 4.2, f"L = {self.L_base}e26 W\nR = {self.R_val}e8 m", 
#                 color='white', fontsize=10)
#         ax.set_xlim(0, 6); ax.set_ylim(0, 5); ax.axis('off')
#         plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
#         plt.close()

#         # Technical drawing of a sphere
#         # Gradient effect using concentric circles
#         for i in range(50, 0, -1):
#             alpha = 0.01 + (i/200)
#             ax.add_patch(plt.Circle((3, 3), (i/50)*1.5, color='white', alpha=alpha, lw=0))
        
#         # Radius vector
#         ax.annotate('', xy=(3 + 1.5, 3), xytext=(3, 3),
#                     arrowprops=dict(arrowstyle='->', color='white', lw=2))
#         ax.text(3.75, 3.2, "Radius ($R$)", color='white', ha='center', fontweight='bold')
        
#         # Surface Temperature and Luminosity text
#         ax.text(3, 0.8, f"Luminosity ($L$): {self.L_base}e26 W\nTemperature ($T$): {self.T} K", 
#                 color='white', ha='center', fontsize=12, 
#                 bbox=dict(facecolor='black', edgecolor='white', pad=10))

#         ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.axis('off')
#         plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
#         plt.close()

class Phy198:
    """
    Hubble's law – recessional velocity from redshift.
    """
    def __init__(self):
        self.c = 3.00e8
        self.z = round(rnd.uniform(0.001, 0.02), 4)
        self.v = self.z * self.c
        self.answer = round(self.v, 2)

        self.description = (
            f"A distant galaxy is observed to have a redshift $z = {self.z}$. "
            f"Calculate the recessional velocity of this galaxy. (_) m s$^{{-1}}$"
        )

        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Past Papers"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Redshift-velocity relation}} &\\\\"
            "v &= zc \\\\"
            "\\text{{Step 2: Substitute values}} &\\\\"
            f"v &= ({self.z})(3.00 \\times 10^8) \\\\"
            "\\text{{Step 3: Calculate velocity}} &\\\\"
            f"v &= {self.v:,.2f}\\,\\text{{m s}}^{{-1}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"v &= {self.answer:,.2f}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')
        ax.set_facecolor('black')
        
        # Earth/Observer
        ax.scatter(0.5, 2, color='white', s=100, marker='o')
        ax.text(0.5, 2.4, "Observer\n(Earth)", color='white', ha='center', fontsize=9)
        
        # Receding Galaxy
        ax.scatter(4.5, 2, color='white', s=200, marker='H')
        ax.text(4.5, 2.5, f"Galaxy\n$z = {self.z}$", color='white', ha='center', fontsize=10)
        
        # Velocity Vector
        ax.annotate('', xy=(5.5, 2), xytext=(4.7, 2),
                    arrowprops=dict(arrowstyle='->', color='white', lw=2))
        ax.text(5.1, 2.3, "$v$", color='white', fontsize=12, fontweight='bold')
        
        # Redshift wave representation
        x = np.linspace(1, 4, 100)
        y = 2 + 0.2 * np.sin(2 * np.pi * x / (1 + self.z*5)) # Stretched wave
        ax.plot(x, y, color='white', lw=1.5, ls='--')

        ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()



class Phy199:
    """
    Distance from Hubble's law.
    """
    def __init__(self):
        # Hubble constant in SI units (s^-1)
        self.H_km_s_mpc = 70
        self.H = (self.H_km_s_mpc * 1000) / (3.086e22)
        self.v_base = rnd.randint(1, 15)
        self.v = self.v_base * 1e6

        self.d = self.v / self.H
        self.answer = round(self.d, 2)

        self.description = (
            f"A galaxy has a recessional velocity of {self.v_base} × 10$^6$ m s$^{{-1}}$. "
            f"Using a Hubble constant of {self.H_km_s_mpc} km s$^{{-1}}$ Mpc$^{{-1}}$, "
            "calculate its distance from Earth. (_) m"
        )

        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Convert }} H_0 \\text{{ to SI units}} &\\\\"
            f"H_0 &= \\frac{{70 \\times 10^3}}{{3.086 \\times 10^{{22}}}} \\approx {self.H:.4e}\\,\\text{{s}}^{{-1}} \\\\"
            "\\text{{Step 2: Use Hubble's Law}} &\\\\"
            "v &= H_0 d \\implies d = \\frac{{v}}{{H_0}} \\\\"
            "\\text{{Step 3: Substitute values}} &\\\\"
            f"d &= \\frac{{{self.v:.2e}}}{{{self.H:.4e}}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"d &= {self.answer:.3e}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='black')
        ax.set_facecolor('black')
        
        # Central point (Observer)
        ax.plot(0, 0, 'w+')
        
        # Expanding distance markers
        for r in [1, 2, 3]:
            circle = plt.Circle((0, 0), r, color='white', fill=False, ls=':', alpha=0.3)
            ax.add_patch(circle)
        
        # Galaxy at distance d
        ax.scatter(3, 0, color='white', s=150)
        ax.annotate('', xy=(3.8, 0), xytext=(3.1, 0), arrowprops=dict(arrowstyle='->', color='white'))
        
        ax.text(1.5, 0.2, "Distance ($d$)", color='white', ha='center')
        ax.text(3.5, 0.4, f"$v = {self.v_base} \\times 10^6$ m/s", color='white', ha='center')
        ax.text(-2.5, 2.5, f"$H_0 = {self.H_km_s_mpc}$ km/s/Mpc", color='white', fontsize=10, bbox=dict(facecolor='black', edgecolor='white'))

        ax.set_xlim(-4, 6); ax.set_ylim(-3, 3); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy200:
    """
    Stellar luminosity from radius and temperature.
    """
    def __init__(self):
        self.sigma = 5.67e-8
        self.R_val = rnd.randint(5, 25)
        self.R = self.R_val * 1e8
        self.T = rnd.randint(3000, 12000)

        self.L = 4 * math.pi * self.R**2 * self.sigma * self.T**4
        self.answer = round(self.L, 2)

        self.description = (
            f"A star has a radius of {self.R_val} × 10$^8$ m and a "
            f"surface temperature of {self.T} K. "
            "Calculate its total luminosity. (_) W"
        )

        self.topic, self.subtopic = "Astronomy & cosmology", "Stellar radii"
        self.curriculum, self.source = "A-Level", "Original"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Step 1: Stefan-Boltzmann Law}} &\\\\"
            "L &= 4\\pi R^2 \\sigma T^4 \\\\"
            "\\text{{Step 2: Substitute constants and values}} &\\\\"
            f"L &= 4\\pi({self.R_val} \\times 10^8)^2 (5.67 \\times 10^{{-8}}) ({self.T})^4 \\\\"
            "\\text{{Step 3: Calculate power output}} &\\\\"
            f"L &= {self.L:.4e}\\,\\text{{W}} \\\\"
            "\\text{{Final Answer:}} &\\\\"
            f"L &= {self.answer:.3e}\\,\\text{{W}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
        ax.set_facecolor('black')
        
        # Star sphere with radial 
        for r_offset in np.linspace(0, 0.5, 10):
            circle = plt.Circle((3, 3), 1.2 + r_offset, color='white', alpha=0.05)
            ax.add_patch(circle)
        
        main_star = plt.Circle((3, 3), 1.2, facecolor='white', edgecolor='gray', lw=1)
        ax.add_patch(main_star)
        
        # Dimension lines
        ax.plot([3, 4.2], [3, 3], color='black', lw=2)
        ax.text(3.6, 3.2, "$R$", color='black', ha='center', fontweight='bold')
        
        for angle in range(0, 360, 45):
            rad = np.deg2rad(angle)
            ax.annotate('', xy=(3 + 2*np.cos(rad), 3 + 2*np.sin(rad)), 
                        xytext=(3 + 1.3*np.cos(rad), 3 + 1.3*np.sin(rad)),
                        arrowprops=dict(arrowstyle='->', color='white', lw=1))

        ax.text(3, 0.5, f"Radius: {self.R_val}e8 m\nTemp: {self.T} K", 
                color='white', ha='center', fontsize=11, bbox=dict(facecolor='black', edgecolor='white', pad=8))

        ax.set_xlim(0, 6); ax.set_ylim(0, 6); ax.axis('off')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300)
        plt.close()
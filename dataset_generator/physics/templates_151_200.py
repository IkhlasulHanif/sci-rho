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

        self.answer = f"{self.field:.3e}"

        self.description = (
            "The diagram shows two parallel metal plates connected to a d.c. power supply. "
            "A uniform electric field is produced between the plates. "
            "Calculate the electric field strength between the plates. "
            "(Example Format: 3.546e+10)."
        )

        self.topic = "Electric fields"
        self.subtopic = "Uniform electric fields"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Electric field between parallel plates}\\\\"
            "E &= \\frac{V}{d}\\\\"
            "\\textbf{Step 2: Convert separation to SI units}\\\\"
            f"d &= {self.distance_mm:.2f}\\,\\text{{mm}}\\\\"
            "1\\,\\text{mm} &= 10^{{-3}}\\,\\text{{m}}\\\\"
            f"d &= {self.distance_mm:.2f} \\times 10^{{-3}}\\\\"
            f"d &= {self.distance:.5f}\\,\\text{{m}}\\\\"
            "\\textbf{Step 3: Substitute numerical values}\\\\"
            f"E &= \\frac{{{self.voltage:.2f}}}{{{self.distance:.5f}}}\\\\"
            f"E &= {self.field:.5f}\\,\\text{{V m}}^{{-1}}\\\\"
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
    Uses E = V/d and F = qE.
    """

    def __init__(self):
        while True:
            self.voltage = rnd.uniform(150, 400)
            self.distance_mm = rnd.uniform(30, 80)
            self.charge_uC = rnd.uniform(-0.5, -0.05)

            self.distance = self.distance_mm / 1000
            self.charge = self.charge_uC * 1e-6

            self.E = self.voltage / self.distance
            self.force = abs(self.charge * self.E)

            if self.force > 0:
                break

        self.answer = f"{self.force:.3e}"

        self.description = (
            "The diagram shows a small charged polystyrene ball suspended "
            "between two parallel metal plates connected to a d.c. power supply. "
            "A uniform electric field exists between the plates. "
            "Calculate the magnitude of the electric force acting on the charge. "
            "(Example Format: 3.546e-05). "
        )

        self.topic = "Electric fields"
        self.subtopic = "Uniform electric field"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Electric field between plates}\\\\"
            "E &= \\frac{V}{d}\\\\"
            f"V &= {self.voltage:.2f}\\,\\text{{V}}\\\\"
            f"d &= {self.distance:.5f}\\,\\text{{m}}\\\\"
            f"E &= \\frac{{{self.voltage:.2f}}}{{{self.distance:.5f}}}\\\\"
            f"E &= {self.E:.5f}\\,\\text{{V m}}^{{-1}}\\\\"
            "\\textbf{Step 2: Force on a charge}\\\\"
            "F &= qE\\\\"
            f"q &= {self.charge:.5e}\\,\\text{{C}}\\\\"
            f"F &= ({self.charge:.5e})({self.E:.5f})\\\\"
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
                plate_bottom + plate_height + 0.3,
                "-",
                ha="center", fontsize = 14)

        ax.text(right_x + plate_width/2,
                plate_bottom + plate_height + 0.3,
                "+",
                ha="center", fontsize = 14)
        
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
                f"{self.charge_uC:.2f} μC",
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

        ax.add_patch(patches.Circle((right_wire_x, 4.2), 0.07, fill=False))
        ax.add_patch(patches.Circle((right_wire_x, 3.3), 0.07, fill=False))

        ax.plot([right_wire_x, right_wire_x + 0.5],
                [4.1, 3.5],
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
                f"{self.voltage:.0f} V",
                ha="center",
                va="center")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")

        plt.savefig(dest_image_path,
                    dpi=600,
                    bbox_inches="tight",
                    pad_inches=0.05)

        plt.close()

class Phy153:
    def __init__(self):
        self.k = 8.99e9

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

        self.answer = "{:.2E}".format(self.force)

        self.description = (
            "Two point charges A and B are separated in a vacuum as shown in the image. "
            "Determine the magnitude of the electrostatic force between the two charges. "
            f"Provide your answer in scientific notation  (Example Format: 3.54E-05). "
            "Do not include units."
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric force between point charges"
        self.source = "Past Paper"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Given:}\\\\"
            "k &= 8.99 \\times 10^{9}\\,\\text{N m}^2\\text{C}^{-2}\\\\"
            f"q_1 &= {self.q1_nC:.4g}\\,\\text{{nC}}\\\\"
            f"q_2 &= {self.q2_nC:.4g}\\,\\text{{nC}}\\\\"
            f"r &= {self.distance_mm:.4g}\\,\\text{{mm}}\\\\"
            "\\\\"
            "\\textbf{Step 1: Convert to SI units}\\\\"
            f"q_1 &= {self.q1:.3E}\\,\\text{{C}}\\\\"
            f"q_2 &= {self.q2:.3E}\\,\\text{{C}}\\\\"
            f"r &= {self.r:.3E}\\,\\text{{m}}\\\\"
            "\\\\"
            "\\textbf{Step 2: Coulomb's Law}\\\\"
            "F &= k\\frac{|q_1 q_2|}{r^2}\\\\"
            "\\\\"
            "\\textbf{Step 3: Substitute values}\\\\"
            f"F &= (8.99 \\times 10^9)"
            f"\\frac{{|({self.q1:.3E})({self.q2:.3E})|}}{{({self.r:.3E})^2}}\\\\"
            "\\\\"
            "\\textbf{Step 4: Final result}\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
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

        xA, xB, y = 4, 6, 2

        ax.add_patch(patches.Circle((xA, y), 0.18, color="#2c3e50"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#2c3e50"))

        ax.text(xA, y + 0.35, "A", ha="center", fontsize=12, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=12, weight="bold")

        ax.text(xA, y - 0.5, f"q = {self.q1_nC:.2f} nC", ha="center", fontsize=10)
        ax.text(xB, y - 0.5, f"q = {self.q2_nC:.2f} nC", ha="center", fontsize=10)

        ax.annotate("",
                    xy=(xA, y + 0.7),
                    xytext=(xB, y + 0.7),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.5))
        ax.text((xA + xB)/2, y + 0.9,
                f"r = {self.distance_mm:.3f} mm",
                ha="center", fontsize=11, weight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path,
                    dpi=300,
                    bbox_inches="tight",
                    pad_inches=0.1)
        plt.close()

class Phy154:
    def __init__(self):
        self.k = 8.99e9

        while True:
            self.q1_fC = rnd.uniform(1.0, 5.0)
            self.q2_fC = -rnd.uniform(1.0, 5.0)
            self.distance_mm = rnd.uniform(3.0, 8.0)

            self.q1 = self.q1_fC * 1e-15
            self.q2 = self.q2_fC * 1e-15
            self.r = self.distance_mm * 1e-3

            self.force = self.k * abs(self.q1 * self.q2) / (self.r ** 2)

            if 1e-18 < self.force < 1e-6:
                break

        self.answer = "{:.2E}".format(self.force)
        self.description = "Two point charges A and B are separated in a vacuum as shown in the image. " "Calculate the magnitude of the electric force acting on each charge. " f"Provide your answer in scientific notation  (Example Format: 3.54E-05). " 
        self.topic = "Electric fields" 
        self.subtopic = "Electric force between point charges" 
        self.source = "Original" 
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Given:}\\\\"
            "k &= 8.99 \\times 10^{9}\\,\\text{N m}^2\\text{C}^{-2}\\\\"
            f"q_1 &= {self.q1_fC:.4g} \\times 10^{{-15}}\\,\\text{{C}}\\\\"
            f"q_2 &= {self.q2_fC:.4g} \\times 10^{{-15}}\\,\\text{{C}}\\\\"
            f"r &= {self.distance_mm:.4g}\\,\\text{{mm}}\\\\"
            "\\\\"
            "\\textbf{Step 1: Convert distance to meters}\\\\"
            f"r &= {self.distance_mm:.4g} \\times 10^{{-3}}\\,\\text{{m}}\\\\"
            "\\\\"
            "\\textbf{Step 2: Apply Coulomb's Law}\\\\"
            "F &= k \\frac{|q_1 q_2|}{r^2}\\\\"
            f"F &= (8.99 \\times 10^{{9}})"
            f"\\frac{{|({self.q1:.2E})({self.q2:.2E})|}}{{({self.r:.2E})^2}}\\\\"
            "\\\\"
            "\\textbf{Step 3: Final Calculation}\\\\"
            f"F &= {self.answer}\\,\\text{{N}}"
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

        xA, xB, y = 4, 6, 2

        ax.add_patch(patches.Circle((xA, y), 0.18, color="#4a4a4a"))
        ax.add_patch(patches.Circle((xB, y), 0.18, color="#4a4a4a"))

        ax.text(xA, y + 0.35, "A", ha="center", fontsize=11, weight="bold")
        ax.text(xB, y + 0.35, "B", ha="center", fontsize=11, weight="bold")

        ax.text(xA, y - 0.45, f"+{self.q1_fC:.2f} ×10⁻¹⁵ C", ha="center", fontsize=9)
        ax.text(xB, y - 0.45, f"{self.q2_fC:.2f} ×10⁻¹⁵ C", ha="center", fontsize=9)

        ax.annotate("",
                    xy=(xA, y + 0.6),
                    xytext=(xB, y + 0.6),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.3))

        ax.text((xA + xB) / 2, y + 0.85, f"{self.distance_mm:.1f} mm", ha="center", fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path,
                    dpi=300,
                    bbox_inches="tight",
                    pad_inches=0.1)
        plt.close()

class Phy155:
    def __init__(self):
        self.epsilon0 = 8.85e-12

        self.EA_V_per_cm = rnd.choice([2.0, 2.4, 2.6, 3.0]) * 1e3
        self.EB_V_per_cm = self.EA_V_per_cm / 2
        self.QB_microC = rnd.choice([6.0, 7.0, 7.5, 8.0])

        self.QB = self.QB_microC * 1e-6
        self.EB = self.EB_V_per_cm * 100

        self.rB = math.sqrt(
            self.QB / (4 * math.pi * self.epsilon0 * self.EB)
        )

        self.rB_cm = self.rB * 100
    
        self.answer = "{:.3e}".format(self.rB_cm)

        self.description = (
            "The image shows two charged conducting spheres, A and B, with their respective surface electric field strengths. "
            f"If the charge stored on the surface of sphere B is {self.QB_microC:.1f} μC, its radius is ... cm "
             "(Example Format:  3.544E-05)"
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric field of a charged conducting sphere"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{{Known Identification:}} & \\\\"
            f"E_B &= {self.EB_V_per_cm:.1e}\\,\\text{{V/cm}} = {self.EB:.10g}\\,\\text{{V/m}} \\\\"
            f"Q_B &= {self.QB_microC:.1f}\\,\\mu\\text{{C}} = {self.QB:.10g}\\,\\text{{C}} \\\\"
            "\\\\ \\\\"
            "\\text{{Step 1: Formula for Electric Field}} & \\\\"
            "E &= \\frac{Q}{4\\pi \\varepsilon_0 r^2} \\implies r = \\sqrt{\\frac{Q}{4\\pi \\varepsilon_0 E}} \\\\"
            "\\\\ \\\\"
            "\\text{{Step 2: Substitution}} & \\\\"
            f"r_B &= \\sqrt{{\\frac{{{self.QB:.10g}}}{{4\\pi (8.85 \\times 10^{{-12}}) ({self.EB:.10g})}}}} \\\\"
            f"r_B &= {self.rB:.10g}\\,\\text{{m}} \\\\"
            "\\\\ \\\\"
            "\\text{{Step 3: Final Answer in cm}} & \\\\"
            f"r_B &= {self.rB_cm:.10g}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.set_xlim(-4, 4)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect("equal")
        ax.axis("off")

        def draw_sphere(center_x, charge_symbol, field_label, field_value, show_radius=False):
            sphere_radius = 0.9
            sphere = plt.Circle((center_x, 0), sphere_radius, facecolor="#d9d9d9", edgecolor="#666666", linewidth=2)
            ax.add_patch(sphere)

            ax.text(center_x, 0, charge_symbol, ha="center", va="center", fontsize=22, weight="bold", 
                    color="#cc0000" if charge_symbol == "+" else "#1f77b4")

            angles = np.linspace(0, 2*np.pi, 14, endpoint=False)
            for theta in angles:
                x_start = center_x + sphere_radius * np.cos(theta)
                y_start = sphere_radius * np.sin(theta)
                x_end = center_x + 1.6 * np.cos(theta)
                y_end = 1.6 * np.sin(theta)
                ax.annotate("", xy=(x_end, y_end), xytext=(x_start, y_start),
                            arrowprops=dict(arrowstyle="->", linewidth=1.2, color="#f1c232"))

            ax.text(center_x, -1.8, f"E = {field_value:.1e} V cm$^{{-1}}$", ha="center", fontsize=10)
            
            if field_label:
                ax.text(center_x, -2.1, field_label, ha="center", fontsize=11, weight="bold")

            if show_radius:
                ax.plot([center_x, center_x + sphere_radius], [0, 0], color="black", linestyle="--", linewidth=1.5)
                ax.text(center_x + sphere_radius/2, 0.15, "r", ha="center", fontsize=12, style="italic")

        draw_sphere(-2.2, "+", "Sphere A", self.EA_V_per_cm)
        draw_sphere(2.2, "−", "Sphere B", self.EB_V_per_cm, show_radius=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy156:
    def __init__(self):
        self.e = 1.60e-19
        self.epsilon0 = 8.85e-12
        self.k_val = 1 / (4 * math.pi * self.epsilon0)

        self.m_alpha = 6.64e-27
        self.Z = rnd.choice([47, 79, 82])   # Ag, Au, Pb

        while True:
            self.v_coeff = rnd.uniform(2.5, 5.5)
            self.v = self.v_coeff * 1e7

            self.q_alpha = 2 * self.e
            self.q_nucleus = self.Z * self.e

            self.KE = 0.5 * self.m_alpha * self.v**2
            self.r_min = self.k_val * self.q_alpha * self.q_nucleus / self.KE

            if 1e-14 < self.r_min < 5e-14:
                break

        self.answer_val = self.r_min * 1e14
        self.answer = "{:.2f}".format(self.answer_val)

        self.description = (
            "The image illustrates an alpha particle (α) approaching a metal nucleus head-on. "
            f"If the alpha particle travels at the speed shown and the metal nucleus has proton number Z = {self.Z}, "
            "calculate the closest distance of approach, r_min. "
            "(Example format: 1.34)"
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Save My Exam"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        ke_coeff, ke_power = f"{self.KE:.3e}".split("e")
        r_coeff, r_power = f"{self.r_min:.3e}".split("e")

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Initial kinetic energy of the alpha particle}\\\\"
            "E_k &= \\tfrac{1}{2}mv^2\\\\"
            f"E_k &= 0.5({self.m_alpha})({self.v_coeff:.2f} \\times 10^7)^2\\\\"
            f"E_k &= {ke_coeff} \\times 10^{{{int(ke_power)}}}\\,\\text{{J}}\\\\"
            "\\\\"
            "\\textbf{Step 2: Conservation of energy}\\\\"
            "E_k &= E_p = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1 q_2}{r_{\\min}}\\\\"
            "\\\\"
            "\\textbf{Step 3: Rearranging for } r_{\\min}\\\\"
            "r_{\\min} &= \\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1 q_2}{E_k}\\\\"
            f"r_{{\\min}} &= (8.99 \\times 10^9)"
            f"\\frac{{(2e)({self.Z}e)}}{{{ke_coeff} \\times 10^{{{int(ke_power)}}}}}\\\\"
            "\\\\"
            "\\textbf{Step 4: Final result}\\\\"
            f"r_{{\\min}} &= {r_coeff} \\times 10^{{{int(r_power)}}}\\,\\text{{m}}\\\\"
            f"r_{{\\min}} &= {self.answer} \\times 10^{{-14}}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.set_xlim(-6, 6)
        ax.set_ylim(-3.5, 3.5)
        ax.set_aspect("equal")
        ax.axis("off")

        alpha_center = (-4.5, 0)
        nucleus_center = (4.0, 0)

        alpha = plt.Circle(alpha_center, 0.6, facecolor="#e6e6e6", edgecolor="black", linewidth=2)
        ax.add_patch(alpha)
        ax.text(alpha_center[0], alpha_center[1], r"$\alpha$", ha="center", va="center", fontsize=16)

        nucleus = plt.Circle(nucleus_center, 1.6, facecolor="#f4d27a", edgecolor="black", linewidth=2)
        ax.add_patch(nucleus)
        ax.text(nucleus_center[0], 0.6, "metal", ha="center", va="center", fontsize=16, weight="bold")
        ax.text(nucleus_center[0], -0.5, f"Z = {self.Z}", ha="center", va="center", fontsize=14)

        ax.annotate("", xy=(1.5, 0), xytext=(-3.5, 0),
                    arrowprops=dict(arrowstyle="->", linewidth=2, color="black"))

        ax.text(-1.0, 0.8,
                rf"$v = {self.v_coeff:.2f} \times 10^7$ m/s",
                ha="center", fontsize=12)

        ax.plot([2.0, 2.0], [-1.5, 1.5], linestyle="--", linewidth=1.5, color="#2b6cb0")

        ax.annotate("", xy=(nucleus_center[0], -2.2), xytext=(2.0, -2.2),
                    arrowprops=dict(arrowstyle="<->", linewidth=1.5, color="black"))

        ax.text(3.25, -2.6, r"$r_{\min}$", ha="center", fontsize=14, style="italic")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.2)
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
        self.answer = "{:.3E}".format(self.U)

        self.description = (
            "The image shows an α-particle approaching a stationary gold nucleus. "
            "At the distance shown, the α-particle momentarily comes to rest. "
            "Calculate the electric potential energy (U) of the system at this instant in Joules. "
            "(Example Format: 3.543E-10)"
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Electric potential energy between two charges}\\\\"
            "U &= \\frac{k q_{\\alpha} q_{Au}}{r}\\\\"
            "\\\\"
            "\\textbf{Step 2: Known values}\\\\"
            "k &= 8.99 \\times 10^{9}\\,\\text{N m}^2\\text{C}^{-2}\\\\"
            "q_{\\alpha} &= 2e = 2(1.602 \\times 10^{-19})\\,\\text{C}\\\\"
            "q_{Au} &= 79e = 79(1.602 \\times 10^{-19})\\,\\text{C}\\\\"
            f"r &= {self.r:.2E}\\,\\text{{m}}\\\\"
            "\\\\"
            "\\textbf{Step 3: Substituting into the equation}\\\\"
            "U &= \\frac{(8.99 \\times 10^9)"
            "(3.204 \\times 10^{-19})"
            "(1.2656 \\times 10^{-17})}"
            f"{{{self.r:.2E}}}\\\\"
            "\\\\"
            "\\textbf{Step 4: Final result}\\\\"
            f"U &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        y = 2.5
        x_alpha, x_gold = 3, 9

        ax.add_patch(plt.Circle((x_gold, y), 0.8, color='#f1c40f', alpha=0.3))
        ax.add_patch(plt.Circle((x_gold, y), 0.8, color='#f39c12', fill=False, lw=2))
        ax.text(x_gold, y, "$^{197}_{79}$Au\n$+79e$", ha='center', va='center', fontweight='bold')

        ax.add_patch(plt.Circle((x_alpha, y), 0.4, color='#e74c3c', alpha=0.3))
        ax.add_patch(plt.Circle((x_alpha, y), 0.4, color='#c0392b', fill=False, lw=2))
        ax.text(x_alpha, y, "α\n$+2e$", ha='center', va='center', fontweight='bold', color='#c0392b')

        ax.annotate("", xy=(x_alpha + 0.6, 3.0), xytext=(x_alpha - 0.4, 3.0),
                    arrowprops=dict(arrowstyle="->", color='#2c3e50', lw=2))
        ax.text(x_alpha, y + 0.6, "$v$", ha='center', fontweight='bold', fontsize=12)

        ax.annotate("", xy=(x_gold, y - 1.2), xytext=(x_alpha, y - 1.2),
                    arrowprops=dict(arrowstyle="<->", color='black', lw=1.2))
        ax.text((x_alpha + x_gold) / 2, y - 1.6,
                rf"$r = {self.r:.2E}$ m",
                ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='none', pad=2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy158:
    def __init__(self):
        self.mass_alpha = 6.64e-27

        while True:
            self.speed = rnd.uniform(2.0e7, 6.0e7)
            if 1e7 < self.speed < 1e8:
                break

        self.KE = 0.5 * self.mass_alpha * self.speed**2
        self.answer = "{:.3E}".format(self.KE)

        self.description = (
            "The image shows an α-particle ($^4_2$He$^{2+}$) moving at a constant speed. "
            "Using the physical constants and parameters provided in the image, "
            "calculate the kinetic energy of the α-particle in Joules (J). "
            "(Example Format: 3.54E-12)."
        )

        self.topic = "Electric Fields"
        self.subtopic = "Electric Potentials"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Kinetic energy formula}\\\\"
            "E_k &= \\tfrac{1}{2}mv^2\\\\"
            "\\\\"
            "\\textbf{Step 2: Substitute known values}\\\\"
            f"m &= {self.mass_alpha:.2E}\\,\\text{{kg}}\\\\"
            f"v &= {self.speed:.2E}\\,\\text{{m s}}^{{-1}}\\\\"
            f"E_k &= 0.5 \\times ({self.mass_alpha:.2E}) \\times ({self.speed:.2E})^2\\\\"
            "\\\\"
            "\\textbf{Step 3: Final calculation}\\\\"
            f"E_k &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 5)
        ax.set_aspect('equal')
        ax.axis('off')

        y = 2.5
        x_start = 2
        
        ax.add_patch(plt.Circle((x_start, y), 0.6, color='#e74c3c', alpha=0.2))
        ax.add_patch(plt.Circle((x_start, y), 0.6, color='#c0392b', fill=False, lw=2.5))
        ax.text(x_start, y, r"$\alpha$", ha='center', va='center', fontsize=20, color='#c0392b', fontweight='bold')
        ax.text(x_start, y - 1.2, r"$^4_2$He$^{2+}$", ha='center', fontsize=14, fontweight='bold')
        
        ax.annotate("", xy=(10, y), xytext=(x_start + 0.7, y),
                    arrowprops=dict(arrowstyle="fancy", color='#34495e', lw=1, mutation_scale=20))
        
        ax.text(6.5, y + 0.8, rf"$v = {self.speed:.2E}\,\text{{m s}}^{{-1}}$", ha='center', fontsize=12, fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='#34495e', boxstyle='round,pad=0.5'))
        ax.text(6.5, y - 0.8, rf"$m = {self.mass_alpha:.2E}\,\text{{kg}}$", ha='center', fontsize=12, style='italic',
                bbox=dict(facecolor='white', edgecolor='none', pad=0.5))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
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

        self.R = rnd.uniform(2, 8) * 1e3  # ohm
        self.V = rnd.uniform(6, 12)  # V

        self.Ceq = 1 / ((1 / self.C1) + (1 / self.C2))
        self.answer = "{:.4f}".format(self.Ceq * 1e6)
        self.description = (
            "Two capacitors and a resistor are connected as shown. "
            "Calculate the combined capacitance of the two capacitors. (_) µF. (Example format: 12.3664)"
        )

        self.topic = "Capacitance"
        self.subtopic = "Capacitor and Capacitance"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify given values} \\\\"
            f"C_1 &= {self.C1*1e6:.0f}\\,\\mu\\text{{F}}\\\\"
            f"C_2 &= {self.C2*1e6:.0f}\\,\\mu\\text{{F}}\\\\"
            "\\\\ "
            "\\textbf{Step 2: Use formula for capacitors in series} \\\\"
            "\\frac{1}{C_{eq}} &= \\frac{1}{C_1} + \\frac{1}{C_2}\\\\"
            "\\\\ "
            "\\textbf{Step 3: Substitute and solve} \\\\"
            f"\\frac{{1}}{{C_{{eq}}}} &= \\frac{{1}}{{{self.C1*1e6:.0f}}} + \\frac{{1}}{{{self.C2*1e6:.0f}}}\\\\"
            f"C_{{eq}} &= {self.answer}\\,\\mu\\text{{F}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        # Circuit Layout
        ax.plot([2, 2], [6, 2], linewidth=2, color="black")
        ax.plot([2, 5], [6, 6], linewidth=2, color="black")
        ax.plot([5, 5], [5.4, 6.6], linewidth=2, color="black")
        ax.plot([5.5, 5.5], [5.2, 6.8], linewidth=2, color="black")
        ax.plot([5.5, 8], [6, 6], linewidth=2, color="black")
        ax.text(5.25, 7, f"{self.V} V", ha='center', fontsize=12)

        # Capacitor C2
        ax.plot([9, 9], [1.7, 2.3], linewidth=2, color="black")
        ax.plot([9.5, 9.5], [1.7, 2.3], linewidth=2, color="black")
        ax.text(9.25, 1.2, f"{self.C2*1e6:.0f} µF", ha='center', fontsize=12, fontweight='bold')

        # Capacitor C1
        ax.plot([6, 6], [1.7, 2.3], linewidth=2, color="black")
        ax.plot([6.5, 6.5], [1.7, 2.3], linewidth=2, color="black")
        ax.text(6.25, 1.2, f"{self.C1*1e6:.0f} µF", ha='center', fontsize=12, fontweight='bold')

        # Resistor
        ax.add_patch(plt.Rectangle((4, 4.3), 2, 0.4, fill=False, linewidth=2))
        ax.text(5, 4.9, f"{self.R/1000:.1f} kΩ", ha='center', fontsize=12)

        # Wires
        ax.plot([12, 9.5], [2, 2], linewidth=2, color="black")
        ax.plot([9, 6.5], [2, 2], linewidth=2, color="black")
        ax.plot([6, 2], [2, 2], linewidth=2, color="black")
        ax.plot([12, 12], [4.8, 2], linewidth=2, color="black")
        ax.plot([12, 10], [4.8, 4.8], linewidth=2, color="black")
        ax.plot([8, 10], [6, 4.8], linewidth=2, color="black")
        ax.plot([6, 8], [4.5, 4.5], linewidth=2, color="black")
        ax.plot([2, 4], [4.5, 4.5], linewidth=2, color="black")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.1)
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
        self.answer = "{:.3e}".format(self.Qx)

        self.description = (
            "Two capacitors, X and Y, are connected in parallel to a battery. "
            "Using the values shown in the diagram, calculate the charge on capacitor X. (_) C. (Example format: 1.234e-4)"
        )

        self.topic = "Capacitance"
        self.subtopic = "Capacitor and Capacitance"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify given values}\\\\"
            f"C_X &= {self.Cx * 1e6:.1f}\\,\\mu\\text{{F}}\\\\"
            f"V &= {self.V:.1f}\\,\\text{{V}}\\\\[6pt]"
            "\\textbf{Step 2: Use charge formula}\\\\"
            "Q &= CV\\\\[6pt]"
            "\\textbf{Step 3: Substitute and solve}\\\\"
            f"Q_X &= ({self.Cx:.2E}) \\times ({self.V:.1f})\\\\"
            f"Q_X &= {self.Qx:.2E}\\,\\text{{C}}"
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
    def __init__(self):
        while True:
            self.Ca_val = rnd.randint(10, 50)
            self.Cb_val = rnd.randint(60, 150)
            self.V = rnd.choice([5.0, 10.0, 15.0, 20.0])
            if self.Ca_val != self.Cb_val:
                break

        self.Ca = self.Ca_val * 1e-6
        self.Cb = self.Cb_val * 1e-6
        self.energy_a = 0.5 * self.Ca * (self.V**2)
        self.answer = f"{self.energy_a:.3f}"

        self.description = (
            "Two capacitors, A and B, are connected in parallel to a DC supply. "
            "Using the values shown in the diagram, calculate the energy stored in capacitor A. "
            "(_) J (Example format: 0.123)"
        )

        self.topic = "Capacitance"
        self.subtopic = "Energy Stored in a Capacitor"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Values} \\\\"
            "&C_A = " + str(self.Ca_val) + "\\,\\mu\\text{F} = " + f"{self.Ca:.2e}" + "\\,\\text{F} \\\\"
            "&V = " + f"{self.V:.1f}" + "\\,\\text{V} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Energy\ Formula} \\\\"
            "&W = \\frac{1}{2} C V^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            "&W_A = 0.5 \\times (" + f"{self.Ca:.2e}" + ") \\times (" + f"{self.V:.1f}" + ")^2 \\\\"
            "&W_A = " + self.answer + "\\,\\text{J} \\\\[8pt]"
            "&\\mathbf{Final\ Answer:} \\\\"
            "&W_A = " + self.answer + "\\,\\text{J}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        ax.plot([2, 8, 8, 2, 2], [2, 2, 6, 6, 2], color='black', lw=2)
        ax.plot([5, 5], [2, 6], color='black', lw=2)

        ax.plot([1.5, 2.5], [4.1, 4.1], color='black', lw=3)
        ax.plot([1.8, 2.2], [3.9, 3.9], color='black', lw=1.5)
        ax.text(1.2, 4, f"{self.V:.1f} V", va='center', fontweight='bold', fontsize=12)

        ax.plot([4.5, 5.5], [4.2, 4.2], color='black', lw=3)
        ax.plot([4.5, 5.5], [3.8, 3.8], color='black', lw=3)
        ax.text(5.8, 4.2, "A", fontweight='bold', fontsize=12)
        ax.text(5.8, 3.8, f"$C_A = {self.Ca_val}\\ \\mu$F", fontweight='bold', fontsize=10)

        ax.plot([7.5, 8.5], [4.2, 4.2], color='black', lw=3)
        ax.plot([7.5, 8.5], [3.8, 3.8], color='black', lw=3)
        ax.text(8.8, 4.2, "B", fontweight='bold', fontsize=12)
        ax.text(8.8, 3.8, f"$C_B = {self.Cb_val}\\ \\mu$F", fontweight='bold', fontsize=10)

        ax.scatter([5, 5], [2, 6], color='black', s=50, zorder=5)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy162:
    """
    Combined capacitance of two capacitors connected in series
    and total energy stored when fully charged.
    """
    def __init__(self):

        while True:
            self.C1 = rnd.randint(10, 40) * 1e-6
            self.C2 = rnd.randint(20, 80) * 1e-6
            if self.C1 != self.C2:
                break
        self.R = rnd.randint(2, 8) * 1e3
        self.V = rnd.randint(6, 12)
        self.Ceq = 1 / ((1 / self.C1) + (1 / self.C2))
        self.energy = 0.5 * self.Ceq * self.V**2
        self.answer = "{:.3e}".format(self.energy)

        self.description = (
            "Two capacitors and a resistor are connected as shown. "
            "Determine the total energy stored in the two capacitors. (_) J. (Example format: 1.234e-4) "
        )
        self.topic = "Capacitance"
        self.subtopic = "Energy Stored in a Capacitor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
            "A capacitor discharges through a fixed resistor. "
            "The graph shows the variation with time t of the potential difference V across the capacitor. "
            "Using the values from the graph, calculate the energy lost by the capacitor "
            "during the time interval shown as a percentage of the initial energy stored. (_) %"
            "(Example format: 45.67)"
        )
        self.topic = "Capacitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
            "The diagram shows a circuit used to investigate the discharge of a capacitor. "
            "Using the values shown in the diagram, calculate the time constant of this circuit. (_) s. (Example format: 0.01250)"
        )

        self.topic = "Capacitance"
        self.subtopic = "Discharging a capacitor"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        ax.text(1.5, 3.0, "I", color=accent_color, fontsize=12, va='center', fontweight='bold')
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
        self.V = rnd.choice([6.0, 9.0, 12.0])
        self.P = rnd.randint(20, 40) * 1e3     # ohm
        self.Q = rnd.randint(200, 400) * 1e3   # ohm
        self.C = rnd.randint(50, 200) * 1e-6   # F

        self.energy = 0.5 * self.C * self.V**2
        self.answer = "{:.3e}".format(self.energy)
        self.description = (
            "A capacitor is charged through resistor P by moving the switch to position A. "
            "Using the circuit values shown in the diagram, calculate the energy stored "
            "in the capacitor when it is fully charged. (_) J. (Example format: 8.100e-03)"
        )

        self.topic = "Energy stored in a capacitor"
        self.subtopic = "Capacitance"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis("off")

        lw = 2
        c = "black"

        y_top = 6.5
        y_bottom = 1.5
        x_left = 3
        x_cap = 8.5
        x_right = 12
        
        v_gap = 0.3
        ax.plot([x_left, x_left], [y_top, 4.0 + v_gap], lw=lw, color=c)
        ax.plot([x_left, x_left], [4.0 - v_gap, y_bottom], lw=lw, color=c)
        ax.plot([x_left - 0.4, x_left + 0.4], [4.0 + v_gap, 4.0 + v_gap], lw=3, color=c)
        ax.plot([x_left - 0.2, x_left + 0.2], [4.0 - v_gap, 4.0 - v_gap], lw=3, color=c)
        ax.text(x_left - 1.5, 4.0, f"{self.V:.1f} V", fontsize=12, fontweight='bold', va='center')

        ax.plot([x_left, x_right], [y_top, y_top], lw=lw, color=c)
        ax.plot(x_cap, y_top, marker='o', markersize=4, color=c) 
        
        gap_c = 0.2
        ax.plot([x_cap, x_cap], [y_top, 4.0 + gap_c], lw=lw, color=c)
        ax.plot([x_cap - 0.4, x_cap + 0.4], [4.0 + gap_c, 4.0 + gap_c], lw=3, color=c)
        ax.plot([x_cap - 0.4, x_cap + 0.4], [4.0 - gap_c, 4.0 - gap_c], lw=3, color=c)
        ax.plot([x_cap, x_cap], [4.0 - gap_c, 3.2], lw=lw, color=c) 
        ax.text(x_cap + 0.6, 4.0, f"{self.C*1e6:.0f} µF", va='center', fontsize=11, fontweight='bold')

        y_pivot = 3.2
        y_terminals = 1.5
        x_A = 7.0
        x_B = 10.0
        
        ax.plot(x_cap, y_pivot, marker='o', markersize=5, color=c)
        ax.plot(x_A, y_terminals, marker='o', markersize=6, fillstyle='none', color=c)
        ax.plot(x_B, y_terminals, marker='o', markersize=6, fillstyle='none', color=c)
        ax.text(x_A, y_terminals - 0.6, "A", ha="center", fontsize=12, fontweight='bold')
        ax.text(x_B, y_terminals - 0.6, "B", ha="center", fontsize=12, fontweight='bold')

        ax.plot([x_cap, x_A + 0.1], [y_pivot, y_terminals + 0.1], lw=3, color='darkred')
        ax.plot([x_left, x_A], [y_bottom, y_bottom], lw=lw, color=c)
        ax.add_patch(plt.Rectangle((4.5, y_bottom - 0.25), 1.5, 0.5, fill=True, facecolor='white', lw=lw, edgecolor=c, zorder=4))
        ax.text(5.25, y_bottom + 0.5, f"P: {self.P/1000:.0f} kΩ", ha="center", fontsize=10)

        ax.plot([x_right, x_right], [y_top, 4.5], lw=lw, color=c)
        ax.add_patch(plt.Rectangle((x_right - 0.25, 3.0), 0.5, 1.5, fill=True, facecolor='white', lw=lw, edgecolor=c, zorder=4))
        ax.text(x_right + 0.5, 3.75, f"Q: {self.Q/1000:.0f} kΩ", va='center', fontsize=10)
        ax.plot([x_right, x_right], [3.0, y_terminals], lw=lw, color=c)
        ax.plot([x_right, x_B], [y_terminals, y_terminals], lw=lw, color=c)

        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=600, bbox_inches="tight")
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
            "A straight conductor is placed in a uniform magnetic field as shown. "
            "Using the values provided in the diagram, calculate the magnetic force "
            "acting on the conductor. (_) N. (Example format: 0.012)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
                        arrowprops=dict(arrowstyle='->', color=field_color, lw=1.5, alpha=0.4))
        ax.text(9.6, 5, "Uniform Magnetic\nField ($B$)", color=field_color, fontweight='bold', va='center')
        ax.text(9.6, 4.2, f"$B = {self.B:.3f}$ T", color=field_color, fontsize=10, fontweight='bold')

        x0, y0 = 3, 2
        length_scale = 5
        x1 = x0 + length_scale * np.cos(self.theta)
        y1 = y0 + length_scale * np.sin(self.theta)

        ax.plot([x0, x1], [y0, y1], lw=12, color=cond_color, alpha=0.2, solid_capstyle='round', zorder=2)
        ax.plot([x0, x1], [y0, y1], lw=2, color=cond_color, zorder=3)
        
        ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle='-|>', color=cond_color, lw=2.5, mutation_scale=20))
        
        ax.text((x0+x1)/2 - 0.7, (y0+y1)/2 + 0.6, f"$I = {self.I:.2f}$ A", color=cond_color, fontweight='bold', rotation=self.theta_deg)
        ax.text((x0+x1)/2 + 0.3, (y0+y1)/2 - 0.8, f"$L = {self.L:.2f}$ m", color=c_text, style='italic', fontweight='bold')

        ax.plot([x0, x0 + 2.5], [y0, y0], color=c_text, lw=1, linestyle='--')
        arc_r = 1.2
        arc_angles = np.linspace(0, self.theta, 50)
        ax.plot(x0 + arc_r * np.cos(arc_angles), y0 + arc_r * np.sin(arc_angles), color=c_text, lw=1.5)
        ax.text(x0 + 1.6, y0 + 0.4, f"${self.theta_deg}^\circ$", fontsize=12, fontweight='bold')

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
        self.answer = f"{self.force:5f}"

        self.description = (
            "A current-carrying conductor is placed at right angles to a uniform magnetic field. "
            "Based on the values shown in the diagram, what is the magnetic force acting on the conductor? (_) N "
            "(Example Format: 0.06789)"
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Save My Exam" 
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        
        ax.text(7.5, 5.2, f"Magnetic Field ($B$)\n$B = {self.B:.3f}$ T", 
                color=field_color, fontweight='bold', fontsize=10, ha='center')

        x_c, y_start, y_end = 5, 1, 5
        d_scale = 0.4
        
        ax.add_patch(patches.Rectangle((x_c - d_scale/2, y_start), d_scale, y_end - y_start, 
                                     color=cond_color, alpha=0.8, zorder=3))
        ax.add_patch(patches.Rectangle((x_c - d_scale/6, y_start), d_scale/3, y_end - y_start, 
                                     color='white', alpha=0.4, zorder=4))
        
        ax.annotate('', xy=(5, 4.5), xytext=(5, 1.5),
                    arrowprops=dict(arrowstyle='-|>', color='black', lw=2.5, mutation_scale=20, zorder=5))
        
        ax.text(5.5, 3.5, f"$I = {self.I:.2f}$ A", color=cond_color, fontweight='bold', fontsize=11)
        ax.text(5.5, 2.5, f"$L = {self.L:.2f}$ m", color='black', fontweight='bold', fontsize=11)
        
        ax.plot([5, 5.4], [1.5, 1.5], color='black', lw=1.5)
        ax.plot([5.4, 5.4], [1.5, 1.9], color='black', lw=1.5)

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
        self.answer = f"{self.force:.5f}"

        self.description = (
            "A current-carrying conductor is placed in a uniform magnetic field as shown. "
            "Based on the values provided in the diagram, calculate the magnetic force acting on the conductor. "
            "(_) N (Example Format: 0.07890)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        
        ax.text(5, 9.2, f"Uniform Magnetic Field\n$B = {self.B_mT}$ mT (into page)", 
                color=field_color, ha='center', fontweight='bold', fontsize=11)

        angle_rad = math.radians(self.theta)
        length_draw = 5
        x_p, y_p = 5, 5
        x0, y0 = x_p - (length_draw/2)*math.cos(angle_rad), y_p - (length_draw/2)*math.sin(angle_rad)
        x1, y1 = x_p + (length_draw/2)*math.cos(angle_rad), y_p + (length_draw/2)*math.sin(angle_rad)

        cond_color = '#d35400'
        d_scale = 0.4
        
        ax.add_patch(patches.Rectangle((x0, y0 - d_scale/2), length_draw, d_scale,
                                     angle=self.theta, color=cond_color, alpha=0.8, zorder=4))
        ax.add_patch(patches.Rectangle((x0, y0 - d_scale/6), length_draw, d_scale/3,
                                     angle=self.theta, color='white', alpha=0.3, zorder=5))

        ax.annotate("", xy=(x1, y1), xytext=(x0, y0), 
                    arrowprops=dict(arrowstyle="-|>", color='black', lw=2.5, mutation_scale=20, zorder=6))
        
        ax.text(x0 - 0.5, y0, f"$I = {self.I}$ A\n$L = {self.L}$ m", 
                color=cond_color, fontweight='bold', ha='right', va='center', fontsize=14)

        ax.plot([x_p, x_p + 2.5], [y_p, y_p], color='black', lw=1, linestyle='--')
        arc_r = 1.2
        arc_angles = np.linspace(0, angle_rad, 50)
        ax.plot(x_p + arc_r * np.cos(arc_angles), y_p + arc_r * np.sin(arc_angles), color='black', lw=1.5)
        ax.text(x_p + 1.5, y_p + 0.3, f"{self.theta}°", fontsize=12, fontweight='bold')

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
        self.answer = f"{self.force:.4f}"

        self.description = (
            "A rectangular wire loop ABCD is placed in a uniform magnetic field as shown. "
            "Using the values provided in the diagram, calculate the magnitude of the magnetic force "
            "acting on side AB. (_) N (Example Format: 0.1234)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a current-carrying conductor"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        ax.text((D[0]+A[0])/2, A[1]-0.5, f" $I = {self.I}$ A", 
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
        self.answer = f"{self.r:.5f}"

        self.description = (
            "An electron enters a uniform magnetic field as shown. "
            "Based on the values provided in the diagram, calculate the radius of the circular path of the electron. "
            "(_) m (Example format: 0.00123)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a moving charge"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

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
        ax.text(radius_draw + 0.3, -0.3, "electron", color='#d63031', fontweight='bold', fontsize=9)

        ax.annotate('', xy=(radius_draw, 1.5), xytext=(radius_draw, 0),
                    arrowprops=dict(arrowstyle='->', color='#0984e3', lw=2))
        ax.text(radius_draw + 0.2, 1.5, "$v$", color='#0984e3', fontweight='bold', fontsize=12)

        ax.annotate('', xy=(0.2, 0), xytext=(radius_draw, 0),
                    arrowprops=dict(arrowstyle='->', color='#e17055', lw=2))
        ax.text(1.5, 0.2, f"$v = {self.v_base} \\times 10^6$ m s$^{-1}$", color='black', fontweight='bold', fontsize=10)

        ax.plot([0, 0], [0, -radius_draw], color='black', lw=1)
        ax.text(0.2, -radius_draw/2, "$r$", fontweight='bold', fontsize=12)
        ax.add_patch(plt.Circle((0, 0), 0.05, color='black'))

        ax.text(-4.5, 4.5, f"$B = {self.B_base} \\times 10^{{-3}}$ T", fontweight='bold', color='#636e72')

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
        self.answer = f"{self.E:.4f}"

        self.description = (
            "A point charge is placed in a vacuum as shown. "
            "Based on the values provided in the diagram, calculate the electric field strength E at point P. "
            "(_) V m^-1 (Example Format: 1234.2345)"
        )
        self.topic = "Electricity"
        self.subtopic = "Electric fields"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        self.source =  "Original"
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
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy172:
    def __init__(self):
        self.k = 8.99e9
        self.q = round(rnd.uniform(2.0, 9.0), 2) * 1e-9
        self.dist = round(rnd.uniform(0.06, 0.20), 3)

        r = self.dist / 2

        self.E_single = (self.k * self.q) / (r**2)
        self.E_total = 2 * self.E_single

        self.answer = f"{self.E_total:.1f}"

        self.description = (
            "Two point charges, one +Q and one -Q, are separated by a distance as shown. "
            "Based on the values provided in the diagram, calculate the magnitude of the net electric field strength at the midpoint between the charges. "
            "Assume Coulomb's constant is 8.99 × 10^9 N m^2 C^-2. "
            "(_) V m^-1 (Example format: 12345.2)"
        )

        self.topic, self.subtopic = "Electricity", "Electric fields"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Distance\ to\ midpoint} \\\\"
            f"&r = \\frac{{{self.dist:.3f}}}{{2}} = {r:.3f}\\,\\text{{m}} \\\\[6pt]"
            "&\\mathbf{Step\ 2:\ Field\ from\ one\ charge} \\\\"
            f"&E = \\frac{{8.99\\times10^9 \\times {self.q:.2e}}}{{({r:.3f})^2}} \\\\[6pt]"
            "&\\mathbf{Step\ 3:\ Net\ field} \\\\"
            "&E_{net} = 2E \\\\[6pt]"
            f"&E_{{net}} = {self.E_total:.1f}\\,\\text{{V m}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis('off')

        ax.add_patch(plt.Circle((2, 2), 0.25, color='#e74c3c', ec='black', zorder=3))
        ax.add_patch(plt.Circle((2.1, 2.1), 0.1, color='white', alpha=0.3, zorder=4))
        ax.text(2, 2.5, f"$+Q = {self.q:.2e}$ C", ha='center', fontweight='bold')
        
        ax.add_patch(plt.Circle((8, 2), 0.25, color='#3498db', ec='black', zorder=3))
        ax.add_patch(plt.Circle((8.1, 2.1), 0.1, color='white', alpha=0.3, zorder=4))
        ax.text(8, 2.5, f"$-Q = {self.q:.2e}$ C", ha='center', fontweight='bold')

        ax.scatter(5, 2, marker='|', color='black', s=200, zorder=2)
        ax.text(5, 1.6, "Midpoint", ha='center', style='italic', fontsize=10)

        ax.annotate('', xy=(8, 1.2), xytext=(2, 1.2), arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1.5))
        ax.text(5, 0.8, f"$d = {self.dist:.3f}$ m", ha='center', fontweight='bold')

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
        self.answer = f"{self.F:.2E}"

        self.description = (
            "A particle with charge q enters a uniform magnetic field B with a velocity v as shown. "
            "Based on the values provided in the diagram, calculate the magnitude of the magnetic force acting on the particle. "
            "(_) N (Example format: 1.23E-16)"
        )

        self.topic = "Magnetic fields"
        self.subtopic = "Force on a moving charge"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        for x in np.linspace(-4, 4, 9):
            for y in np.linspace(-4, 4, 9):
                ax.text(x, y, r"$\times$", color=field_color, ha='center', va='center', fontsize=14, alpha=0.4)
        
        ax.text(4.5, 4.5, f"B-Field: {self.B_base} " + r"$\times 10^{-3}$ T", color=field_color, ha='right', fontsize=12)

        angle_rad = np.radians(self.theta)
        v_len = 3.5
        vx, vy = v_len * np.cos(angle_rad), v_len * np.sin(angle_rad)

        ax.plot([0, 4], [0, 0], color='#2c3e50', lw=1.5, ls='--', alpha=0.5)
        
        ax.annotate('', xy=(vx, vy), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='-|>', color=particle_color, lw=4, mutation_scale=30))
        
        ax.add_patch(plt.Circle((0, 0), 0.3, color=particle_color, ec='black', zorder=5))
        
        ax.text(0, -0.7, f"$q = {self.q_base} \\times 10^{{-19}}$ C", ha='center', fontweight='bold', fontsize=11)

        # unit perpendicular vector
        norm = np.hypot(vx, vy)
        px, py = -vy / norm, vx / norm   # perpendicular direction

        offset = 0.5
        tx = vx/2 + offset * px
        ty = vy/2 + offset * py

        ax.text(tx, ty,
                f"$v = {self.v_base} \\times 10^6$ m/s",
                color=particle_color,
                rotation=self.theta,
                fontweight='bold',
                fontsize=14)

        arc_r = 1.2
        arc_angles = np.linspace(0, angle_rad, 50)
        ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), color='#2c3e50', lw=2)
        ax.text(1.7 * np.cos(angle_rad/2), 1.7 * np.sin(angle_rad/2), f"${self.theta}^\\circ$", 
                fontsize=14, fontweight='bold', color='#2c3e50')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
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
        self.answer = f"{self.emf:.3f}"

        self.description = (
            "A conductor of length moves with speed "
            "perpendicular to a magnetic field of B. "
            "Calculate the induced emf. (_) V "
            "(Example format: 11.234)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Force on a Moving Charge"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        for x in np.linspace(1, 7, 7):
            for y in np.linspace(1, 4, 4):
                ax.text(x, y, '×', color='blue', alpha=0.5, 
                        ha='center', va='center', fontsize=15)
        ax.text(0.5, 4.5, f"B = {self.B} T", color='blue', fontweight='bold')

        rod_x = 2.5
        rod_y_start = 1.5
        rod_y_end = 3.5
        ax.plot([rod_x, rod_x], [rod_y_start, rod_y_end], 
                color='gray', linewidth=8, solid_capstyle='round', zorder=3)
        ax.plot([rod_x, rod_x], [rod_y_start, rod_y_end], 
                color='black', linewidth=1, zorder=4)

        ax.annotate('', xy=(rod_x - 0.3, rod_y_start), xytext=(rod_x - 0.3, rod_y_end),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(rod_x - 0.8, (rod_y_start + rod_y_end)/2, f"L = {self.L} m", 
                va='center', rotation=90)

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
        self.answer = f"{self.emf:.3f}"

        self.description = (
            "A coil of N turns is placed in a changing magnetic field as shown. "
            "Using the values provided in the diagram, calculate the magnitude of the induced e.m.f. "
            "(_) V (Example format: 11.234)"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic Induction"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
            "&\\mathcal{E} = \\mathbf{" + self.answer + "\\,V}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

        coil_color = '#d35400'
        
        for i in range(8):
            ax.add_patch(plt.Circle((0, -0.7 + i*0.2), 0.3, fill=False, color=coil_color, lw=3))

        ax.add_patch(plt.Rectangle((-2.5, -0.3), 1.0, 0.6, color='#34495e')) 
        ax.add_patch(plt.Rectangle((-1.5, -0.3), 1.0, 0.6, color='#e74c3c'))
        ax.text(-2.0, 0, 'S', color='white', ha='center', va='center', fontweight='bold')
        ax.text(-1.0, 0, 'N', color='white', ha='center', va='center', fontweight='bold')
        
        ax.annotate('', xy=(-0.4, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle='->', lw=2))

        ax.text(1.2, 0.5, f"$N = {self.N}$ turns", fontweight='bold', fontsize=12)
        ax.text(1.2, -0.5, f"$\\Delta\\Phi = {self.dPhi}$ Wb\n$\\Delta t = {self.dt}$ s", 
                fontsize=11, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

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
            "A rectangular coil rotates in a uniform magnetic field as shown. "
            "Based on the values provided in the diagram, calculate the peak induced e.m.f. "
            "(_) V"
        )

        self.topic = "Magnetic Fields"
        self.subtopic = "Electromagnetic induction"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        self.source = "Original"

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
            "&\\varepsilon_0 = \\mathbf{" + f"{float(self.answer):.2f}" + "\\,V}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
        ax.set_xlim(-6, 6)
        ax.set_ylim(-3, 3)
        ax.axis('off')

        ax.add_patch(plt.Rectangle((-4.5, -2), 1.5, 4, color='#e74c3c', zorder=1))
        ax.add_patch(plt.Rectangle((3, -2), 1.5, 4, color='#3498db', zorder=1))
        ax.text(-3.75, 0, 'N', color='white', fontsize=24, fontweight='bold', ha='center')
        ax.text(3.75, 0, 'S', color='white', fontsize=24, fontweight='bold', ha='center')

        for y in np.linspace(-1.5, 1.5, 9):
            ax.annotate('', xy=(3, y), xytext=(-3, y),
                        arrowprops=dict(arrowstyle='->', color='#95a5a6', lw=1, alpha=0.5))
        ax.text(0, 2.5, f"$B = {self.B}$ T", ha='center', fontweight='bold', fontsize=12)

        ax.plot([0, 0], [-2.5, 2.5], color='black', lw=1.5, ls='--')

        angle = np.radians(35)
        w, h = 1.2, 1.8 

        c, s = np.cos(angle), np.sin(angle)
        pts = np.array([[-w, -h], [w, -h], [w, h], [-w, h], [-w, -h]])
        rot = np.array([[c, 0], [0, 1]]) 
        p = pts @ rot.T
        ax.plot(p[:, 0], p[:, 1], color='#d35400', lw=4, zorder=5)

        nx, ny = 1.2 * np.sin(angle), 1.2 * np.cos(angle)
        ax.annotate('', xy=(nx, ny), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2))
        ax.text(nx, ny+0.2, r"$\vec{n}$", fontsize=14, fontweight='bold')

        ax.annotate('', xy=(0.8, 1.8), xytext=(0.2, 1.4),
                    arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.4", 
                                    color='#27ae60', lw=3, mutation_scale=20))
        ax.text(1.0, 2.0, f"$\omega$\n($f = {self.f}$ Hz)", color='#27ae60', fontweight='bold', fontsize=11)

        # Info box
        info_text = f"Coil:\n$N = {self.N}$\n$A = {self.A}$ m$^2$"
        ax.text(-5.5, -2.5, info_text, bbox=dict(facecolor='white', edgecolor='gray'), fontsize=14)

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
        self.answer = "{:.2f}".format(self.V_rms)
        self.description = (
            f"An alternating voltage has a peak value of V. "
            "Calculate the RMS voltage. (_) V (Example format: 123.45)"
        )

        self.topic = "Alternating currents"
        self.subtopic = "Characteristics of Alternating Currents"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x)
        rms_val = 1 / np.sqrt(2)

        fig, ax = plt.subplots(figsize=(8, 5))
        
        ax.plot(x, y, color='blue', linewidth=2, label='AC Voltage')
        
        ax.axhline(y=1, color='red', linestyle='--', linewidth=1)
        ax.text(0.1, 1.05, f"$V_{{peak}} = {self.V_peak}$ V", color='red', fontsize=10)
        
        ax.axhline(y=rms_val, color='green', linestyle=':', linewidth=1.5)
        
        ax.axhline(0, color='black', linewidth=0.8) 
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xticks([0, np.pi, 2*np.pi])
        ax.set_xticklabels(['0', '$\pi$', '$2\pi$'])
        ax.set_yticks([-1, 0, 1])
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
    def __init__(self):
        self.I_rms = rnd.randint(2, 20)
        self.I_peak = self.I_rms * math.sqrt(2)
        self.answer = f"{self.I_peak:.2f}"

        self.description = (
            f"An alternating current has an RMS value of {self.I_rms} A. "
            "Calculate the peak current. (_) A (Example format: 12.34)"
        )
        self.topic = "Alternating currents"
        self.subtopic = "Characteristics of alternating currents"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        x = np.linspace(0, 2 * np.pi, 1000)
        y = np.sin(x)
        rms_val = 1 / np.sqrt(2) 

        fig, ax = plt.subplots(figsize=(8, 5))
        
        ax.plot(x, y, color='darkorange', linewidth=2.5, label='AC Current')
        
        ax.axhline(y=1, color='red', linestyle='--', linewidth=1.2)
        
        ax.axhline(y=rms_val, color='teal', linestyle=':', linewidth=1.8)
        ax.text(0.1, rms_val - 0.15, f"$I_{{rms}} = {self.I_rms}$ A", color='teal', fontsize=10, fontweight='bold')
        ax.axhline(0, color='black', linewidth=1) 
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
        ax.set_xticklabels(['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
        ax.set_yticks([-1, 0, 1])
        ax.set_yticklabels(['$-I_p$', '0', '$I_p$'])
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
    def __init__(self):
        self.I = rnd.randint(1, 5)
        self.f = rnd.randint(50, 60)
        self.C_micro = rnd.randint(200, 1000)
        self.C = self.C_micro * 1e-6

        self.V_ripple = self.I / (self.f * self.C)
        self.answer = f"{self.V_ripple:.2f}"

        self.description = (
            "A smoothing capacitor is connected to the output of a bridge rectifier as shown. "
            "Using the parameters provided in the diagram, determine the ripple voltage of the output. "
            "(_) V (Example format: 12.34)"
        )

        self.topic = "Alternating Currents"
        self.subtopic = "Rectification and Smoothing"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        fig = plt.figure(figsize=(12, 6), dpi=300)
        
        ax1 = fig.add_subplot(121)
        ax1.axis('off')
        
        ax1.plot([0.5, 1.5], [4, 4], 'k-', lw=2)
        ax1.plot([0.5, 1.5], [1, 1], 'k-', lw=2)
        
        ax1.plot([1.5, 2.5], [4, 2.5], 'k-', lw=2)
        ax1.plot([1.5, 2.5], [1, 2.5], 'k-', lw=2)
        ax1.plot([2.5, 3.5], [2.5, 4], 'k-', lw=2)
        ax1.plot([2.5, 3.5], [2.5, 1], 'k-', lw=2)
        ax1.text(2.5, 2.5, "BRIDGE\nRECTIFIER", ha='center', va='center', fontweight='bold', bbox=dict(facecolor='white', lw=2))
        
        ax1.plot([3.5, 5.5], [4, 4], 'k-', lw=2)
        ax1.plot([3.5, 5.5], [1, 1], 'k-', lw=2)
        
        ax1.plot([4.5, 4.5], [4, 3.1], 'k-', lw=2)
        ax1.plot([4.5, 4.5], [1, 1.9], 'k-', lw=2)
        ax1.plot([4.2, 4.8], [3.1, 3.1], 'k-', lw=3)
        ax1.plot([4.2, 4.8], [1.9, 1.9], 'k-', lw=3)
        ax1.text(
            4.9, 2.5,
            f"Capacitor\n$C = {self.C_micro}\\,\\mu F$\n$I = {self.I}\\,A$",
            va='center'
        )        
        ax1.plot([6, 6], [4, 1], 'k-', lw=2)
        ax1.plot([5.5, 6], [4, 4], 'k-', lw=2)
        ax1.plot([5.5, 6], [1, 1], 'k-', lw=2)
        
        ax1.text(0.5, 2.5, f"AC Input\n$f = {self.f}\\ \\text{{Hz}}$", ha='center', fontweight='bold')

        ax2 = fig.add_subplot(122)
        
        f_vis = 50
        t = np.linspace(0, 0.04, 1000)
        dt = t[1] - t[0]
        v_rect = np.abs(np.sin(2 * np.pi * f_vis * t))
        
        v_smooth = []
        curr = 0.0
        tau = 0.015
        
        for target in v_rect:
            if target > curr:
                curr = target
            else:
                curr = curr * np.exp(-dt / tau)
            v_smooth.append(curr)
            
        v_smooth = np.array(v_smooth)
        
        idx_start = int(0.006 / 0.04 * 1000)
        idx_end = int(0.014 / 0.04 * 1000)
        trough_val = np.min(v_smooth[idx_start:idx_end])
        trough_idx = idx_start + np.argmin(v_smooth[idx_start:idx_end])
        trough_x_ms = t[trough_idx] * 1000
        
        ax2.plot(t * 1000, v_rect, '--', color='gray', alpha=0.3, label='Full-wave Rectified')
        ax2.plot(t * 1000, v_smooth, color='#d35400', lw=2.5, label='Smoothed Output')
        
        ax2.annotate('', xy=(trough_x_ms, trough_val), xytext=(trough_x_ms, 1.0), 
                     arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax2.text(trough_x_ms + 0.5, (1.0 + trough_val) / 2, '$V_{ripple}$', fontweight='bold', fontsize=12)
        
        ax2.axhline(1.0, color='black', lw=1, ls=':', alpha=0.5)
        ax2.axhline(trough_val, color='black', lw=1, ls=':', alpha=0.5)
        
        ax2.set_xlabel("Time (ms)", fontsize=10)
        ax2.set_ylabel("Potential Difference (V)", fontsize=10)
        ax2.grid(True, linestyle=':', alpha=0.6)
        ax2.legend(loc='lower right')
        ax2.set_ylim(0, 1.15)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy180:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.uniform(4, 9)
        self.f = self.f_base * 1e14

        self.E = self.h * self.f
        self.answer = f"{self.E:.3e}"

        self.description = (
            "Calculate the energy of the photon shown in the diagram. "
            "Take Planck's constant $h = 6.63 \\times 10^{-34}$ J s. "
            "(_) J (Example format: 2.652e-19)"
        )

        self.topic = "Quantum physics"
        self.subtopic = "Energy and momentum of a photon"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
                    arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=1.5))
        ax.text(center, 1.0, "Photon", ha='center', fontsize=12, fontweight='bold', style='italic')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor=photon_color)
        param_text = f"Frequency ($f$): ${self.f_base} \\times 10^{{14}}$ Hz"
        ax.text(0.5, 0.1, param_text, transform=ax.transAxes, fontsize=12, fontweight='bold', bbox=props, ha='center')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy181:
    def __init__(self):
        self.h = 6.63e-34
        self.lambda_base = rnd.randint(400, 700)
        self.lambda_m = self.lambda_base * 1e-9

        self.p = self.h / self.lambda_m
        self.answer = f"{self.p:2e}"

        self.description = (
            "Calculate the momentum of the photon with the wavelength indicated in the diagram. "
            "Take Planck's constant h = 6.63 × 10^{-34} J s. "
            "(_) kg m s^-1 (Example format: 1.6575e-27)"
        )

        self.topic = "Quantum physics"
        self.subtopic = "Energy and Momentum of a photon"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        
        fig, ax = plt.subplots(figsize=(8, 3), dpi=300)
        ax.plot(x, y, color='#8e44ad', linewidth=3)
        
        ax.annotate('', xy=(0.5*np.pi, 1.2), xytext=(2.5*np.pi, 1.2), 
                    arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text(1.5*np.pi, 1.5, f"$\\lambda = {self.lambda_base}$ nm", ha='center', fontweight='bold', fontsize=12)
        
        ax.set_ylim(-1.5, 2.2)
        ax.axis('off')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy182:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(6, 12)
        self.f = self.f_base * 1e14
        self.phi_base = rnd.randint(2, 5)
        self.phi = self.phi_base * 1e-19
        self.Ek = self.h * self.f - self.phi
        self.answer = f"{self.Ek:.3e}"

        self.description = (
            "Light shines on a metal surface as shown in the diagram. "
            "Calculate the maximum kinetic energy of the emitted photoelectrons. "
            "(_) J (Example format: 1.318e-19)"
        )
        self.topic = "Quantum physics" 
        self.subtopic = "Photoelectric effect"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
        ax.axhspan(0, 0.8, color='#95a5a6', alpha=0.5)
        
        ax.annotate('', xy=(1.5, 0.9), xytext=(0.5, 2.8), 
                    arrowprops=dict(arrowstyle='-|>,head_length=0.8,head_width=0.4', color='#f39c12', lw=3))
        ax.text(0.1, 3.0, f"Incident Photon\n$f={self.f_base}\\times 10^{{14}}$ Hz", color='#d35400', fontsize=11, fontweight='bold')
        
        ax.annotate('', xy=(3.8, 2.8), xytext=(2, 0.9), 
                    arrowprops=dict(arrowstyle='-|>,head_length=0.8,head_width=0.4', color='#2980b9', lw=3))
        ax.text(3.9, 3.0, "Photoelectron\n($E_k$ max)", color='#2980b9', fontsize=11, fontweight='bold')
        
        ax.text(2.5, 0.4, f"Metal Surface\nWork Function $\\Phi = {self.phi_base}\\times 10^{{-19}}$ J", 
                ha='center', va='center', fontweight='bold', color='black', fontsize=10)
        
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 4.5)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy183:
    def __init__(self):
        self.e = 1.60e-19
        self.Ek_base = rnd.uniform(1, 9)
        self.Ek = self.Ek_base * 1e-19
        self.Vs = self.Ek / self.e
        self.answer = f"{self.Vs:.2f}"

        self.description = (
            "Based on the experimental data provided in the diagrams, determine the "
            "stopping potential $V_s$ required to reduce the photocurrent to zero. "
            "(_) V (Example format: 1.25)"
        )

        self.topic = "Quantum physics"
        self.subtopic = "Photoelectric effect"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        
        f_threshold = 2
        f = np.linspace(f_threshold, 6, 100)
        Ek_plot = 1.5 * (f - f_threshold)
        ax1.plot(f, Ek_plot, color='#e67e22', lw=3, label='$E_{k,max} = hf - \\Phi$')
        ax1.axhline(0, color='black', lw=1.5)
        ax1.axvline(f_threshold, color='black', lw=1.5, ls='--')
        
        target_Ek_y = 3
        target_f_x = 4
        ax1.scatter(target_f_x, target_Ek_y, color='#c0392b', s=120, zorder=5)
        ax1.annotate(f'$E_k = {self.Ek_base} \\times 10^{{-19}}$ J', 
                     xy=(target_f_x, target_Ek_y), xytext=(target_f_x-1.8, target_Ek_y+1.0),
                     arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                     fontweight='bold', fontsize=11)

        ax1.set_xlabel('Frequency ($f$)', fontweight='bold')
        ax1.set_ylabel('Max Kinetic Energy ($E_{k,max}$)', fontweight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(-1, 5)

        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)
        ax2.axis('off')
        
        tube = plt.Circle((5, 6), 3.5, color='#ecf0f1', ec='#2c3e50', lw=2)
        ax2.add_patch(tube)
        
        ax2.plot([3, 3], [4.5, 7.5], color='#2c3e50', lw=5)
        ax2.plot([7, 7], [4.5, 7.5], color='#2c3e50', lw=5)
        ax2.text(2.5, 8.2, 'Cathode (-)', ha='center', fontweight='bold')
        ax2.text(7.5, 8.2, 'Anode (+)', ha='center', fontweight='bold')
        
        for i in range(3):
            ax2.annotate('', xy=(2.8, 7-i), xytext=(0.5, 8-i),
                         arrowprops=dict(arrowstyle='->', color='#f1c40f', lw=2, connectionstyle="arc3,rad=.2"))
        ax2.scatter([4, 5, 5.5], [6, 5.2, 6.8], color='#3498db', s=80) 
        ax2.text(1.5, 8.8, 'Photons', color='#d35400', fontweight='bold', fontsize=11)

        ax2.add_patch(plt.Rectangle((3.5, 1), 3, 1.5, fill=False, ec='#c0392b', lw=2))
        ax2.text(5, 1.75, f'$V_s$', color='#c0392b', ha='center', fontweight='bold', fontsize=14)
        ax2.plot([3, 3, 3.5], [4.5, 1.75, 1.75], color='#c0392b', lw=2)
        ax2.plot([7, 7, 6.5], [4.5, 1.75, 1.75], color='#c0392b', lw=2)
        ax2.set_title('Experiment Setup', fontsize=13, fontweight='bold')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy184:
    def __init__(self):

        self.h = 6.63e-34
        self.m = 9.11e-31

        while True:
            self.v_base = rnd.uniform(1,6)
            self.v = self.v_base * 1e6
            self.lambda_val = self.h / (self.m * self.v)
            if 1e-11 < self.lambda_val < 1e-9:
                break

        self.answer = "{:.3e}".format(self.lambda_val)
        self.description = (
            "Calculate the de Broglie wavelength associated with the electron shown in the diagram. "
            "(_) m (Example format: 1.455e-10)"
        )
        
        self.topic = "Quantum physics"
        self.subtopic = "Wave-particle duality"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        ax.plot(x, wave, color='#8e44ad', lw=3, zorder=3)
        ax.fill_between(x, wave, color='#9b59b6', alpha=0.15)
        
        ax.annotate('', xy=(8.5, 0), xytext=(6.5, 0),
                    arrowprops=dict(arrowstyle='-|>', color='#2980b9', lw=3, mutation_scale=20))
        ax.text(7.5, -0.8, f"$v = {self.v_base} \\times 10^6$ m/s", color='#2980b9', fontweight='bold', ha='center', fontsize=11)

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$\\mathbf{{Electron\ Data:}}$\n"
            f"$m_e = 9.11 \\times 10^{{-31}}$ kg\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.05, 0.1, info_text, transform=ax.transAxes, fontsize=11, bbox=props)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy185:
    def __init__(self):
        self.h = 6.63e-34
        while True:
            self.f_base = rnd.uniform(4, 8) 
            self.f = self.f_base * 1e14
            self.E = self.h * self.f
            if 1e-19 < self.E < 1e-18:
                break
        self.answer = "{:.3e}".format(self.E)
        self.description = (
            "An electron transition between two energy levels in an atom results in the emission "
            "of a photon as shown in the diagram. Calculate the energy difference $\\Delta E$ between these two levels. "
            "(_) J (Example format: 3.315e-19)"
        )
        self.topic = "Quantum physics"
        self.subtopic = "Energy levels"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        ax.hlines([1.5, 4.5], 2, 8, colors='#2c3e50', lw=3.5)
        ax.text(8.2, 4.5, "$E_2$ (Higher Level)", va='center', fontweight='bold', fontsize=11)
        ax.text(8.2, 1.5, "$E_1$ (Lower Level)", va='center', fontweight='bold', fontsize=11)

        ax.annotate('', xy=(4, 1.6), xytext=(4, 4.4), 
                    arrowprops=dict(arrowstyle='-|>', color='#c0392b', lw=3, mutation_scale=20))
        
        x_wave = np.linspace(4, 7.5, 100)
        y_wave = 3 + 0.3 * np.sin(2 * np.pi * 3 * x_wave)
        ax.plot(x_wave, y_wave, color='#f39c12', lw=2.5)
        ax.annotate('', xy=(7.7, 3), xytext=(7.3, 3), 
                    arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2.5))
        ax.text(7.5, 3.4, "Photon emitted", color='#e67e22', fontsize=10, fontweight='bold', ha='center')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$f = {self.f_base} \\times 10^{{14}}$ Hz\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.5, 4.8, info_text, transform=ax.transData, fontsize=11, bbox=props)

        ax.text(5, 0.5, "$\\Delta E = E_2 - E_1 = hf$", fontsize=13, fontweight='bold', ha='center', color='#2c3e50')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy186:
    def __init__(self):
        self.h = 6.63e-34
        self.c = 3.00e8
        while True:
            self.E_base = rnd.uniform(2, 9) 
            self.E = self.E_base * 1e-19
            self.lambda_val = (self.h * self.c) / self.E
            if 1e-7 < self.lambda_val < 1e-6: 
                break
        self.answer = "{:.3e}".format(self.lambda_val)
        self.description = (
            "An electron transition in a hydrogen atom releases energy as shown in the diagram. "
            "Calculate the wavelength $\\lambda$ of the emitted spectral line. "
            "(_) m (Example format: 4.567e-07)"
        )
        self.topic = "Quantum physics"
        self.subtopic = "Line spectra"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        ax.hlines([1.5, 4.5], 2, 8, colors='#2c3e50', lw=3.5)
        ax.text(8.2, 4.5, "$E_2$ (Higher Level)", va='center', fontweight='bold', fontsize=11)
        ax.text(8.2, 1.5, "$E_1$ (Lower Level)", va='center', fontweight='bold', fontsize=11)
        
        ax.annotate('', xy=(3, 1.6), xytext=(3, 4.4), 
                    arrowprops=dict(arrowstyle='-|>,head_length=0.8,head_width=0.4', color='#27ae60', lw=3, mutation_scale=20))
        
        ax.text(3.0, 1.0, f"$\\Delta E = {self.E_base} \\times 10^{{-19}}$ J", color='#1e8449', fontweight='bold', ha='center', fontsize=11)

        x_wave = np.linspace(3.0, 8.5, 150)
        y_wave = 3.0 + 0.5 * np.sin(2 * np.pi * 1.5 * x_wave)
        ax.plot(x_wave, y_wave, color='#9b59b6', lw=2.5) 

        ax.annotate('', xy=(8.7, 3), xytext=(8.4, 3), 
                    arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2.5))
        
        ax.text(4.2, 2.0, "Photon Emitted", color='#8e44ad', fontsize=12, fontweight='bold', ha='center')

        ax.plot([5.5, 5.5], [3.2, 3.8], color='#8e44ad', lw=1.5, ls=':')
        ax.plot([6.1667, 6.1667], [3.2, 3.8], color='#8e44ad', lw=1.5, ls=':')
        ax.annotate('', xy=(5.5, 3.7), xytext=(6.1667, 3.7), 
                    arrowprops=dict(arrowstyle='<->', color='#8e44ad', lw=2))
        ax.text(5.833, 4.0, "$\\lambda$", color='#8e44ad', fontsize=14, fontweight='bold', ha='center')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        const_text = (
            "$\\mathbf{Constants:}$\n"
            "$h = 6.63 \\times 10^{-34}$ J s\n"
            "$c = 3.00 \\times 10^8$ m s$^{-1}$"
        )
        ax.text(0.5, 4.8, const_text, transform=ax.transData, fontsize=11, bbox=props)

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
        self.answer = f"{self.mass_defect:.2e}"

        self.description = (
            "Based on the data provided in the diagram, calculate the mass defect of the nucleus. "
            "(_) kg (Example format: 3.45e-29)"
        )

        self.topic = "Nuclear physics"
        self.subtopic = "Mass defect and binding energy"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
            "&\\Delta m = \\mathbf{" + f"{self.mass_defect:.4e}" + "\\,kg}"
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
                           color='#e74c3c', s=180, edgecolors='black', zorder=3)
            for _ in range(n_count):
                ax.scatter(center_x + rnd.uniform(-spread, spread), 
                           center_y + rnd.uniform(-spread, spread), 
                           color='#3498db', s=180, edgecolors='black', zorder=2)
            ax.text(center_x, center_y - 1.4, label, ha='center', fontweight='bold', fontsize=12)

        draw_nucleus(2.5, 2.5, 0.8, self.Z, self.N, "Individual Nucleons\n(Separated)")
        
        ax.text(5, 2.5, "$\\longrightarrow$", fontsize=40, ha='center', va='center')
        ax.text(5, 3.1, "Binding", fontsize=11, ha='center', color='#7f8c8d', fontweight='bold')

        draw_nucleus(7.5, 2.5, 0.45, self.Z, self.N, f"Bound Nucleus\n($A={self.A}, Z={self.Z}$)")

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$\\mathbf{{Nucleus\ Data:}}$\n"
            f"$Z = {self.Z}$ protons, $N = {self.N}$ neutrons\n"
            f"$m_{{\\text{{measured}}}} = {self.mass_nucleus:.4e}$ kg\n"
            f"$m_p = 1.6726 \\times 10^{{-27}}$ kg\n"
            f"$m_n = 1.6749 \\times 10^{{-27}}$ kg"
        )
        ax.text(0.3, 4.8, info_text, transform=ax.transData, fontsize=10, bbox=props, va='top')

        ax.text(5, 0.5, r"Mass Defect $\Delta m = \sum m_{\text{nucleons}} - m_{\text{nucleus}}$", 
                ha='center', fontsize=13, fontweight='bold', color='#2c3e50')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy188:
    def __init__(self):
        self.c = 3.00e8
        self.dm_base = rnd.uniform(1, 9)
        self.dm = self.dm_base * 1e-29

        self.E = self.dm * (self.c**2)
        self.answer = f"{self.E:.2e}"

        self.description = (
            "Based on the mass defect and constants shown in the diagram, calculate the nuclear binding energy. "
            "(_) J (Example format: 1.23e-11)"
        )
        self.topic, self.subtopic = "Nuclear physics", "Nuclear Binding energy"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
            f"E &= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
        
        ax.text(1.5, 3.8, "Separated Nucleons", ha='center', fontweight='bold', color='#2c3e50', fontsize=12)
        for i in range(6):
            color = '#e74c3c' if i % 2 == 0 else '#3498db'
            circle = plt.Circle((1 + np.cos(i), 2.5 + np.sin(i)), 0.2, color=color, ec='black', lw=1.5, alpha=0.9)
            ax.add_patch(circle)

        ax.text(6.5, 3.8, "Bound Nucleus", ha='center', fontweight='bold', color='#2c3e50', fontsize=12)
        for i in range(6):
            color = '#e74c3c' if i % 2 == 0 else '#3498db'
            circle = plt.Circle((6.5 + 0.15*np.cos(i*np.pi/3), 2.5 + 0.15*np.sin(i*np.pi/3)), 0.2, color=color, ec='black', lw=1.5)
            ax.add_patch(circle)

        ax.annotate('', xy=(5.2, 2.5), xytext=(2.8, 2.5),
                    arrowprops=dict(arrowstyle='-|>', lw=3, color='#7f8c8d', mutation_scale=20))
      
        # ax.text(6.5, 1.0, "Binding\nEnergy ($E = ?$)", ha='center', va='center', fontweight='bold', color='#d35400')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        ax.text(0.5, 0.8, f"$\\Delta m = {self.dm_base} \\times 10^{{-29}}$ kg\n$c = 3.00 \\times 10^8$ m/s", 
                fontsize=12, bbox=props, va='center')

        ax.set_xlim(-1, 8)
        ax.set_ylim(0, 4.5)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy189:
    def __init__(self):
        self.N0 = rnd.randint(500, 2000)
        self.half_life = rnd.randint(2, 10)
        self.n_half_lives = rnd.randint(1, 4)
        self.time = self.n_half_lives * self.half_life

        self.N = self.N0 * (0.5)**(self.n_half_lives)
        self.answer = f"{self.N:.2f}"

        self.description = (
            "A radioactive sample decays over time. Based on the data provided in the graph, "
            "calculate the exact number of nuclei remaining at the target time indicated. "
            "(_) nuclei (Example format: 125.00)"
        )
        self.topic, self.subtopic = "Nuclear physics", "Radioactive decay"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        t_vals = np.linspace(0, self.time * 1.5, 200)
        n_vals = self.N0 * (0.5)**(t_vals / self.half_life)
        
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.plot(t_vals, n_vals, color='#27ae60', lw=3)
        ax.scatter([0, self.half_life, self.time], [self.N0, self.N0/2, self.N], color='#c0392b', zorder=5, s=60)
        
        ax.plot([self.time, self.time], [0, self.N], color='#c0392b', ls='--', lw=1.5)
        ax.plot([0, self.time], [self.N, self.N], color='#c0392b', ls='--', lw=1.5)
        
        ax.annotate(f'$N = ?$', xy=(self.time, self.N), xytext=(self.time + 0.5, self.N + self.N0*0.1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5), fontsize=13, fontweight='bold')
        
        ax.set_xlabel("Time (s)", fontweight='bold')
        ax.set_ylabel("Number of Nuclei ($N$)", fontweight='bold')
        
        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        ax.text(0.95, 0.95, f"$N_0 = {self.N0}$\n$T_{{1/2}} = {self.half_life}$ s\nTarget $t = {self.time}$ s", 
                transform=ax.transAxes, fontsize=12, bbox=props, va='top', ha='right')
        
        ax.grid(True, linestyle=':', alpha=0.7)
        ax.set_ylim(0, self.N0 * 1.1)
        ax.set_xlim(0, self.time * 1.5)
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy190:
    def __init__(self):
        self.half_life = rnd.randint(10, 60)
        self.decay_constant = math.log(2) / self.half_life
        self.N = rnd.randint(1, 9) * 1e12
        
        self.A = self.decay_constant * self.N
        self.answer = f"{self.A:.2e}"

        self.description = (
            "Based on the experimental setup data shown in the diagram, calculate the activity "
            "of the radioactive sample in Becquerels (Bq). (_) Bq (Example format: 5.99e+10)"
        )
        
        self.topic, self.subtopic = "Nuclear physics", "Radioactive decay"
        self.curriculum, self.source = "A-Level", "Past Papers"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        
        circle = plt.Circle((0.2, 0.5), 0.15, color='#e67e22', alpha=0.8, ec='#d35400', lw=2)
        ax.add_patch(circle)
        ax.text(0.2, 0.25, "Radioactive\nSource", ha='center', fontsize=12, fontweight='bold')
        
        for i in range(5):
            ax.annotate('', xy=(0.55, 0.5 + (i-2)*0.06), xytext=(0.35, 0.5),
                        arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2, alpha=0.8))

        ax.add_patch(plt.Rectangle((0.6, 0.35), 0.2, 0.3, color='#7f8c8d', ec='#2c3e50', lw=2))
        ax.text(0.7, 0.7, "GM Tube\nDetector", ha='center', fontsize=12, fontweight='bold')
        
        ax.add_patch(plt.Rectangle((0.62, 0.1), 0.16, 0.2, color='black', ec='#2c3e50', lw=2))
        ax.text(0.7, 0.2, "A = ...", color='#2ecc71', ha='center', va='center', fontsize=13, fontweight='bold')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        ax.text(0.5, 0.9, f"$N = {self.N:.1e}$ \n$T_{{1/2}} = {self.half_life}$ s", 
                ha='center', fontsize=12, bbox=props)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy191:
    def __init__(self):
        self.v = 1540
        self.time = round(rnd.uniform(0.0002, 0.002), 6)
        self.distance = (self.v * self.time) / 2
        self.answer = f"{self.distance:5f}"

        self.description = (
            "An ultrasound pulse is emitted into soft tissue. Based on the echo time and speed of sound "
            "provided in the diagram, calculate the depth of the reflector. (_) m (Example format: 0.63987)"
        )
        self.topic, self.subtopic = "Medical physics", "Ultrasound"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
        
        ax.add_patch(plt.Rectangle((0.5, 3.5), 4, 0.8, color='#bdc3c7', ec='#2c3e50', lw=2))
        ax.text(2.5, 3.9, "Ultrasound Transducer", ha='center', va='center', fontsize=12, fontweight='bold')
        
        ax.annotate('', xy=(2.2, 1.2), xytext=(2.2, 3.4), arrowprops=dict(arrowstyle='->', color='#2980b9', lw=3))
        ax.text(2.0, 2.3, "Pulse", rotation=90, va='center', color='#2980b9', fontweight='bold', fontsize=11)
        
        ax.annotate('', xy=(2.8, 3.4), xytext=(2.8, 1.2), arrowprops=dict(arrowstyle='->', color='#c0392b', ls='--', lw=3))
        ax.text(3.0, 2.3, "Echo", rotation=90, va='center', color='#c0392b', fontweight='bold', fontsize=11)
        
        ax.axhline(1.0, color='#d35400', lw=4)
        ax.text(2.5, 0.6, "Tissue Boundary / Reflector", ha='center', fontweight='bold', color='#d35400', fontsize=11)
        
        ax.annotate('', xy=(4.5, 1.0), xytext=(4.5, 3.5), arrowprops=dict(arrowstyle='<->', color='black', lw=2))
        ax.text(4.7, 2.25, "$d$", va='center', fontweight='bold', fontsize=14)
        
        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#7f8c8d')
        ax.text(0.3, 1.5, f"Echo Time $t = {self.time}$ s\nSpeed $v = 1540$ m s$^{{-1}}$", bbox=props, fontsize=11)
        
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy192:
    def __init__(self):
        self.v = 1540
        self.f_mhz = rnd.randint(2, 12)
        self.f = self.f_mhz * 1e6
        self.lambda_val = self.v / self.f
        self.answer = f"{self.lambda_val:.5f}"

        self.description = (
            "Based on the transducer frequency and speed of ultrasound in the diagram, "
            "calculate the wavelength $\\lambda$ of the waves in the tissue. (_) m (Example format: 0.00385)"
        )
        self.topic = "Medical physics"
        self.subtopic = "Production and use of ultrasound"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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
        ax.add_patch(plt.Circle((2, 0), 1.5, color='#bdc3c7', alpha=0.8, ec='black', lw=1.5))
        ax.text(1.2, 0, "Transducer", rotation=90, va='center', ha='center', fontweight='bold', color='black')

        ax.add_patch(plt.Rectangle((2.5, -1.8), 7, 3.6, color='#fad7a0', alpha=0.3, ec='#e67e22', lw=2, ls='--'))
        ax.text(6, 2.2, "Soft Tissue Layer", ha='center', fontweight='bold', color='#d35400')

        x = np.linspace(2.5, 9, 500)
        wave_freq = 1.5
        y = 0.8 * np.sin(2 * np.pi * wave_freq * x)
        ax.plot(x, y, color='#2980b9', lw=3)

        peak_x1 = 2.5 + (0.25 / wave_freq)
        peak_x2 = peak_x1 + (1 / wave_freq)
        ax.annotate('', xy=(peak_x1, 1.2), xytext=(peak_x2, 1.2),
                    arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=2))
        ax.text((peak_x1 + peak_x2)/2, 1.5, r"$\lambda$", ha='center', fontsize=14, fontweight='bold')

        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$f = {self.f_mhz}$ MHz\n"
            f"$v = 1540$ m s$^{{-1}}$"
        )
        ax.text(0.5, 2.8, info_text, transform=ax.transData, fontsize=12, bbox=props, va='top')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy193:
    def __init__(self):
        self.h = 6.63e-34
        self.f_base = rnd.randint(5, 20)
        self.f = self.f_base * 1e18
        self.E = self.h * self.f
        self.answer = f"{self.E:.2e}"

        self.description = (
            "Calculate the energy of the X-ray photon emitted in the diagram. "
            "(_) J (Example format: 1.23e-15)"
        )
        self.topic = "Medical physics"
        self.subtopic = "X-ray production and energy"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
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

        tube_outer = plt.Circle((5, 3), 3.5, color='#ecf0f1', ec='#bdc3c7', lw=2, zorder=0)
        ax.add_patch(tube_outer)

        ax.add_patch(plt.Rectangle((1.5, 2.2), 0.8, 1.6, color='#34495e', ec='black', lw=1.5, zorder=5))
        ax.text(1.9, 4.2, "Cathode (-)", ha='center', fontweight='bold', fontsize=11)
        
        anode_coords = [[7.5, 2], [8.5, 2], [8.5, 4], [7.5, 4]]
        ax.add_patch(plt.Polygon(anode_coords, color='#7f8c8d', ec='black', lw=1.5, zorder=5))

        target_face = [[6.8, 2.5], [7.5, 2], [7.5, 4], [6.8, 3.5]]
        ax.add_patch(plt.Polygon(target_face, color='#bdc3c7', ec='black', lw=1.5, zorder=6))
        ax.text(8, 4.4, "Tungsten Target", ha='center', fontweight='bold', fontsize=11)

        for i in range(4):
            y_offset = 2.4 + i * 0.4
            ax.annotate('', xy=(6.7, y_offset), xytext=(2.4, y_offset),
                        arrowprops=dict(arrowstyle='->', color='#3498db', lw=1.5, ls='--'))
        ax.text(4.5, 3.8, "High-speed electrons", ha='center', color='#2980b9', fontsize=10, fontweight='bold')

        x_wave = np.linspace(7.2, 9.5, 300)
        for shift in [-0.4, 0, 0.4]:
            y_wave = (3 + shift) + 0.25 * np.sin(2 * np.pi * 5 * x_wave)
            ax.plot(x_wave, y_wave, color='#f39c12', lw=2, alpha=0.9)
        
        ax.annotate('', xy=(9.8, 3), xytext=(9.3, 3), 
                    arrowprops=dict(arrowstyle='->', color='#f39c12', lw=3))

        props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info_text = (
            f"$f = {self.f_base} \\times 10^{{18}}$ Hz\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s"
        )
        ax.text(0.5, 5.8, info_text, transform=ax.transData, fontsize=12, bbox=props, va='top')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy194:
    def __init__(self):
        self.h, self.c, self.e = 6.63e-34, 3.00e8, 1.60e-19
        self.V = rnd.randint(30, 100) * 1000
        self.lambda_min = (self.h * self.c) / (self.e * self.V)
        self.answer = f"{self.lambda_min:.2e}"

        self.description = (
            "Based on the accelerating potential provided in the X-ray spectrum diagram, "
            "calculate the minimum wavelength $\\lambda_{min}$ of the emitted X-rays. "
            "(_) m (Example format: 1.24e-11)"
        )
        self.topic, self.subtopic = "Medical physics", "X-ray production"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        x = np.linspace(0.4, 5, 300)
        y = (x - 0.4)**2 * np.exp(-x + 0.5) 
        
        ax.plot(x, y, color='#8e44ad', lw=3.5)
        ax.fill_between(x, y, color='#9b59b6', alpha=0.2)
        
        ax.axvline(0.4, color='#c0392b', ls='--', lw=2.5)
        
        ax.annotate('', xy=(0.4, 0.4), xytext=(0.9, 0.4),
                    arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2.5))
        ax.text(1.0, 0.38, "$\\lambda_{min}$", color='#c0392b', fontweight='bold', fontsize=16)
        
        props = dict(boxstyle='round,pad=0.8', facecolor='white', alpha=0.95, edgecolor='#bdc3c7', lw=1.5)
        info_text = (
            f"$\\mathbf{{X-ray\\ Tube\\ Data:}}$\n"
            f"Accelerating Potential $V = {int(self.V/1000)}$ kV\n\n"
            f"$\\mathbf{{Constants:}}$\n"
            f"$h = 6.63 \\times 10^{{-34}}$ J s\n"
            f"$c = 3.00 \\times 10^8$ m s$^{{-1}}$\n"
            f"$e = 1.60 \\times 10^{{-19}}$ C"
        )
        ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=13, bbox=props, va='top', ha='right')

        ax.set_xlabel("Wavelength $\\lambda$ (m)", fontweight='bold', fontsize=13)
        ax.set_ylabel("Relative Intensity", fontweight='bold', fontsize=13)
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy195:
    def __init__(self):
        self.L_base = rnd.randint(2, 9)
        self.L = self.L_base * 1e26
        self.I_base = rnd.randint(1, 9)
        self.I = self.I_base * 1e-10
        self.d = math.sqrt(self.L / (4 * math.pi * self.I))
        self.answer = f"{self.d:.2e}"

        self.description = (
            "Based on the astronomical data provided in the diagram, calculate the distance $d$ to the star. "
            "(_) m (Example format: 1.23e+17)"
        )
        self.topic, self.subtopic = "Astronomy and Cosmology", "Standard candles"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 4), facecolor='#0b0d17', dpi=300)
        ax.set_facecolor('#0b0d17')
        
        for i in range(15, 0, -1):
            ax.add_patch(plt.Circle((1, 2), 0.1 + i*0.06, color='#f1c40f', alpha=0.03))
        ax.add_patch(plt.Circle((1, 2), 0.15, color='#fffceb', zorder=5))
        ax.text(1, 1.2, "Star", color='white', ha='center', fontweight='bold')
        
        ax.add_patch(plt.Circle((8, 2), 0.2, color='#3498db', zorder=5))
        ax.text(8, 1.2, "Earth\n(Observer)", color='white', ha='center', fontweight='bold')

        ax.annotate('', xy=(7.6, 2), xytext=(1.5, 2),
                    arrowprops=dict(arrowstyle='<->', color='#bdc3c7', lw=2, ls='--'))
        ax.text(4.5, 2.2, "$d$", color='white', ha='center', fontsize=14, fontweight='bold')
        
        props = dict(boxstyle='round,pad=0.5', facecolor='#1e272e', alpha=0.9, edgecolor='#f1c40f')
        ax.text(1, 3.4, f"$L = {self.L_base} \\times 10^{{26}}$ W", color='#f1c40f', ha='center', bbox=props, fontweight='bold')
        
        props_earth = dict(boxstyle='round,pad=0.5', facecolor='#1e272e', alpha=0.9, edgecolor='#3498db')
        ax.text(8, 3.4, f"$I = {self.I_base} \\times 10^{{-10}}$ W m$^{{-2}}$", color='#3498db', ha='center', bbox=props_earth, fontweight='bold')

        ax.set_xlim(0, 9.5)
        ax.set_ylim(0, 4.5)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy196:
    def __init__(self):
        self.sigma = 5.67e-8
        self.L_base = rnd.randint(2, 9)
        self.L = self.L_base * 1e26
        self.T = rnd.randint(3000, 8000)
        self.R = math.sqrt(self.L / (4 * math.pi * self.sigma * self.T**4))
        self.answer = f"{self.R:.2e}"

        self.description = (
            "Using the star's luminosity and surface temperature provided in the diagram, determine its radius $R$. "
            "(_) m (Example format: 4.81e+10)"
        )
        self.topic, self.subtopic = "Astronomy and cosmology", "Stellar radii"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

        l_val = f"{self.R:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\\ 1:\\ Stefan-Boltzmann\\ Law} \\\\"
            "&L = A \\sigma T^4 = (4\\pi R^2) \\sigma T^4 \\\\[8pt]"
            "&\\mathbf{Step\\ 2:\\ Rearrange\\ for\\ Radius} \\\\"
            "&R = \\sqrt{\\frac{L}{4\\pi \\sigma T^4}} \\\\[8pt]"
            "&\\mathbf{Step\\ 3:\\ Calculation} \\\\"
            "&R = \\sqrt{\\frac{" + str(self.L_base) + " \\times 10^{26}}{4\\pi(5.67 \\times 10^{-8})(" + str(self.T) + ")^4}} \\\\"
            "&R = " + l_val + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\\ Answer:} \\\\"
            "&R = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        star = plt.Circle((5, 4), 2, color='white', ec='black', lw=2, zorder=5)
        ax.add_patch(star)

        ax.plot([5], [4], marker='o', color='black', markersize=6, zorder=10)

        ax.annotate('', xy=(7, 4), xytext=(5, 4),
                    arrowprops=dict(arrowstyle='-|>', color='black', lw=2, mutation_scale=15), zorder=10)
        ax.text(6, 4.2, "$R$", ha='center', fontweight='bold', fontsize=14, zorder=11)

        ax.text(5, 2.8, f"Surface Temperature\n$T = {self.T}$ K", 
                ha='center', va='center', fontsize=12, fontweight='bold', color='black', zorder=10)

        for angle in range(45, 360, 90):
            rad = np.deg2rad(angle)
            start_x = 5 + 2.2 * np.cos(rad)
            start_y = 4 + 2.2 * np.sin(rad)
            end_x = 5 + 3.2 * np.cos(rad)
            end_y = 4 + 3.2 * np.sin(rad)
            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                        arrowprops=dict(arrowstyle='->', color='#d35400', lw=2.5))
            
        ax.text(8.5, 6.5, f"Luminosity\n$L = {self.L_base} \\times 10^{{26}}$ W", 
                color='#d35400', ha='center', fontsize=12, fontweight='bold')

        props = dict(boxstyle='square,pad=0.6', facecolor='white', edgecolor='black', lw=1.5)
        info = (
            f"$\\mathbf{{Stefan-Boltzmann\\ Constant:}}$\n"
            f"$\\sigma = 5.67 \\times 10^{{-8}}$ W m$^{{-2}}$ K$^{{-4}}$"
        )
        ax.text(0.5, 0.5, info, transform=ax.transData, fontsize=11, bbox=props, va='bottom')

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy197:
    def __init__(self):
        self.b = 2.898e-3
        self.T = rnd.randint(3000, 10000)
        self.lambda_max = self.b / self.T
        self.answer = f"{self.lambda_max:.2e}"

        self.description = (
            "Using Wien's displacement law and the surface temperature provided in the stellar "
            "emission spectrum, calculate the peak wavelength $\\lambda_{max}$. "
            "(_) m (Example format:5.89e-07)"
        )
        self.topic, self.subtopic = "Astronomy and Cosmology", "Wien's displacement law"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

        l_val = f"{self.lambda_max:.4e}".replace("e", "\\times 10^{") + "}"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\\ 1:\\ Identify\\ Wien's\\ Law} \\\\"
            "&\\lambda_{\\text{max}} T = 2.898 \\times 10^{-3}\\,\\text{m K} \\\\[8pt]"
            "&\\mathbf{Step\\ 2:\\ Rearrange\\ and\\ Substitute} \\\\"
            "&\\lambda_{\\text{max}} = \\frac{2.898 \\times 10^{-3}}{T} \\\\"
            "&\\lambda_{\\text{max}} = \\frac{2.898 \\times 10^{-3}}{" + str(self.T) + "} \\\\[8pt]"
            "&\\mathbf{Step\\ 3:\\ Calculation} \\\\"
            "&\\lambda_{\\text{max}} = " + l_val + "\\,\\text{m} \\\\[8pt]"
            "&\\mathbf{Final\\ Answer:} \\\\"
            "&\\lambda_{\\text{max}} = " + self.answer + "\\,\\text{m}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        
        x = np.linspace(0.1, 3, 300)
        y = (1 / x**5) * (1 / (np.exp(1 / (x * 0.5)) - 1))
        y = y / np.max(y) 
        
        ax.plot(x, y, color='#e67e22', lw=3)
        ax.fill_between(x, y, color='#d35400', alpha=0.15)
        
        max_idx = np.argmax(y)
        peak_x = x[max_idx]
        peak_y = y[max_idx]

        ax.plot([peak_x, peak_x], [0, peak_y], color='grey', ls=':', lw=2, zorder=4)

        ax.text(peak_x, -0.08, "$\\lambda_{\\text{max}}$", ha='center', fontweight='bold', fontsize=14, color='#c0392b')

        ax.annotate("Peak", xy=(peak_x, peak_y), xytext=(peak_x, peak_y + 0.1),
                    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=11, ha='center', va='bottom', fontweight='bold')
        
        uv_end = 0.38
        visible_end = 0.75
        
        ax.plot([x[0], uv_end], [-0.02, -0.02], color='#9b59b6', lw=6, solid_capstyle='butt')
        ax.plot([uv_end, visible_end], [-0.02, -0.02], color='#3498db', lw=6, solid_capstyle='butt')
        ax.plot([visible_end, x[-1]], [-0.02, -0.02], color='#e74c3c', lw=6, solid_capstyle='butt')
        
        ax.text((x[0] + uv_end) / 2, -0.15, "UV", ha='center', fontsize=10, fontweight='bold', color='black')
        ax.text((uv_end + visible_end) / 2, -0.15, "Visible", ha='center', fontsize=10, fontweight='bold', color='black')
        ax.text((visible_end + x[-1]) / 2, -0.15, "Infrared", ha='center', fontsize=10, fontweight='bold', color='black')
        
        props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='#bdc3c7')
        info = (
            f"$\\mathbf{{Stellar\\ Data:}}$\n"
            f"Surface Temp $T = {self.T}$ K\n\n"
            f"$\\mathbf{{Wien's\\ Constant:}}$\n"
            f"$b = 2.898 \\times 10^{{-3}}$ m K"
        )
        ax.text(0.95, 0.95, info, transform=ax.transAxes, fontsize=12, bbox=props, va='top', ha='right', zorder=10)

        ax.set_xlabel("Wavelength $\\lambda$ ($\\mu$m)", fontweight='bold', fontsize=13)
        ax.set_ylabel("Relative Intensity", fontweight='bold', fontsize=13)
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        ax.set_ylim(-0.2, 1.2)
        ax.set_xlim(0.1, 3)

        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy198:
    def __init__(self):
        self.c = 3.00e8
        self.z = round(rnd.uniform(0.001, 0.02), 4)
        self.v = self.z * self.c
        self.answer = f"{self.v:.2f}"

        self.description = (
            "A distant galaxy's spectrum is redshifted. Using the redshift value in the diagram, "
            "calculate the recessional velocity $v$ of this galaxy. (_) m s^-1 (Example format: 5820000.00)"
        )
        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Past Papers"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 4), facecolor='#0b0d17', dpi=300)
        ax.set_facecolor('#0b0d17')
        
        ax.scatter(1, 2, color='#3498db', s=300, marker='o', edgecolors='white', lw=2)
        ax.text(1, 1.3, "Observer\n(Earth)", color='white', ha='center', fontweight='bold')
        
        ax.scatter(7, 2, color='#e74c3c', s=500, marker='h', alpha=0.9, edgecolors='white', lw=2)
        
        props = dict(boxstyle='round,pad=0.5', facecolor='#1e272e', edgecolor='#e74c3c', lw=2)
        ax.text(7, 3.2, f"Target Galaxy\nRedshift $z = {self.z}$", color='white', ha='center', bbox=props, fontweight='bold')
        
        ax.annotate('', xy=(8.5, 2), xytext=(7.5, 2),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=4))
        ax.text(8.0, 2.3, "Velocity $v$", color='#e74c3c', fontsize=12, fontweight='bold', ha='center')
        
        x = np.linspace(1.5, 6.5, 200)
        wave = 2 + 0.3 * np.sin(2 * np.pi * x / (0.5 + self.z * 10))
        ax.plot(x, wave, color='#e74c3c', lw=2.5, alpha=0.8)
        ax.text(4, 1.2, "Redshifted Light Waves", color='#e74c3c', ha='center', fontsize=11, fontweight='bold')

        ax.set_xlim(0, 9.5)
        ax.set_ylim(0, 4.5)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()


class Phy199:
    def __init__(self):
        self.H_km_s_mpc = 70
        self.H = (self.H_km_s_mpc * 1000) / (3.086e22)
        self.v_base = rnd.randint(1, 15)
        self.v = self.v_base * 1e6
        self.d = self.v / self.H
        self.answer = f"{self.d:.2e}"

        self.description = (
            "Based on the recessional velocity and Hubble constant provided in the diagram, "
            "calculate the distance $d$ to the galaxy. (_) m (Example format: 4.84e+24)"
        )
        self.topic, self.subtopic = "Astronomy & Cosmology", "Cosmology"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(9, 6), facecolor='#111424', dpi=300)
        ax.set_facecolor('#111424')
        
        ax.scatter(0, 0, color='#f39c12', s=600, marker='*', edgecolors='white', lw=1.5, zorder=5)
        ax.text(0, -0.8, "Observer\n(Milky Way)", color='white', ha='center', fontweight='bold', fontsize=11)
        
        for r in [3, 6, 9]:
            circle = plt.Circle((0, 0), r, color='#34495e', fill=False, ls='--', lw=1.5, alpha=0.5)
            ax.add_patch(circle)
        
        g_x, g_y = 6.5, 2.5
        ax.scatter(g_x, g_y, color='#e74c3c', s=400, marker='o', edgecolors='white', lw=1.5, zorder=5)
        ax.text(g_x, g_y + 0.6, "Distant Galaxy", color='white', ha='center', fontweight='bold', fontsize=11)
        
        ax.annotate('', xy=(g_x + 2.0, g_y + 0.77), xytext=(g_x + 0.3, g_y + 0.1), 
                    arrowprops=dict(arrowstyle='-|>,head_length=0.8,head_width=0.4', color='#ff7675', lw=3))
        
        props_v = dict(boxstyle='round,pad=0.5', facecolor='#1e272e', edgecolor='#e74c3c', lw=2)
        ax.text(g_x + 1.5, g_y + 1.5, f"Recessional Velocity $v$\n${self.v_base} \\times 10^6$ m s$^{{-1}}$", 
                color='#ff7675', ha='center', bbox=props_v, fontweight='bold', fontsize=11)
        
        ax.annotate('', xy=(g_x - 0.4, g_y - 0.15), xytext=(0.4, 0.15), 
                    arrowprops=dict(arrowstyle='<->', color='#3498db', lw=2.5, ls='--'))
        ax.text(g_x/2 - 0.6, g_y/2 + 0.6, "Distance $d$", color='#74b9ff', ha='center', rotation=21, fontweight='bold', fontsize=14)
        
        props_h = dict(boxstyle='round,pad=0.8', facecolor='#192a56', edgecolor='#3498db', lw=2)
        const_text = (
            f"$\\mathbf{{Hubble\\ Constant}}$\n"
            f"$H_0 = {self.H_km_s_mpc}$ km s$^{{-1}}$ Mpc$^{{-1}}$\n\n"
            f"$\\mathbf{{Conversion}}$\n"
            f"$1$ Mpc $= 3.086 \\times 10^{{22}}$ m"
        )
        ax.text(-2.5, 3.5, const_text, color='white', ha='center', bbox=props_h, fontsize=11)

        ax.set_xlim(-4.5, 10.5)
        ax.set_ylim(-2.5, 6)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()

class Phy200:
    def __init__(self):
        self.sigma = 5.67e-8
        self.R_val = rnd.randint(5, 25)
        self.R = self.R_val * 1e8
        self.T = rnd.randint(3000, 12000)
        self.L = 4 * math.pi * self.R**2 * self.sigma * self.T**4
        self.answer = f"{self.L:.2e}"

        self.description = (
            "Calculate the total luminosity $L$ of the star using the parameters provided in the diagram. "
            "(_) W (Example format: 1.35e+27)"
        )
        self.topic, self.subtopic = "Astronomy & cosmology", "Stellar radii"
        self.curriculum, self.source = "A-Level", "Original"
        self.question_type = "Short Answer"

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
        plt.style.use("default")
        fig, ax = plt.subplots(figsize=(7, 7), facecolor='#0b0d17', dpi=300)
        ax.set_facecolor('#0b0d17')
        
        color = '#f1c40f' if self.T < 6000 else '#3498db'
        for r_offset in np.linspace(0, 1.2, 15):
            ax.add_patch(plt.Circle((3.5, 3.5), 1.5 + r_offset, color=color, alpha=0.03))
        
        ax.add_patch(plt.Circle((3.5, 3.5), 1.5, facecolor='white', edgecolor=color, lw=3))
        
        ax.annotate('', xy=(5.0, 3.5), xytext=(3.5, 3.5), arrowprops=dict(arrowstyle='->', color='black', lw=2.5))
        ax.text(4.25, 3.6, f"$R = {self.R_val} \\times 10^8$ m", color='black', ha='center', fontweight='bold', fontsize=11)
        
        for angle in range(0, 360, 45):
            rad = np.deg2rad(angle)
            ax.annotate('', xy=(3.5 + 2.8*np.cos(rad), 3.5 + 2.8*np.sin(rad)), 
                        xytext=(3.5 + 1.8*np.cos(rad), 3.5 + 1.8*np.sin(rad)),
                        arrowprops=dict(arrowstyle='->', color=color, lw=3))

        props = dict(boxstyle='round,pad=0.8', facecolor='#1e272e', edgecolor=color, lw=2)
        ax.text(3.5, 0.5, f"Surface Temperature\n$T = {self.T}$ K", color='white', ha='center', fontsize=12, bbox=props, fontweight='bold')
        
        ax.text(3.5, 6.5, "Luminosity $L$", color='white', ha='center', fontsize=16, fontweight='bold')

        ax.set_xlim(0, 7)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=300, bbox_inches="tight")
        plt.close()
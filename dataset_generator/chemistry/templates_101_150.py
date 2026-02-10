import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys

sys.path.append(os.path.dirname(__file__))
from helper import *

DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "chemistry", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)


class Chem101:
    """
    Topic: States of matter
    Visual: Cooling curve showing gas condensing to liquid
    Task: Determine duration of phase change
    """

    def __init__(self):
        self.start_temp = rnd.randint(95, 110)
        self.plateau_temp = rnd.randint(70, 85)
        self.end_temp = rnd.randint(55, 70)

        self.t_A = 0
        self.t_B = rnd.randint(2, 3)
        self.t_C = self.t_B + rnd.randint(3, 5)
        self.t_D = self.t_C + rnd.randint(2, 3)

        self.answer = self.t_C - self.t_B

        self.description = (
            "A gas is left to cool and forms a liquid. "
            "The graph shows how the temperature of the substance changes with time.\n\n"
            "From A to B the substance is a gas.\n"
            "From C to D the substance is a liquid.\n\n"
            "Calculate how long it takes for the substance to become completely liquid."
        )

        self.topic = "States of matter"
        self.subtopic = "Solids, liquids and gases"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Condensation occurs during the constant temperature (plateau) region of the graph.}} &\\\\"
            f"\\text{{Start time of condensation}} &= t_B = {self.t_B}\\,\\text{{minutes}}\\\\"
            f"\\text{{End time of condensation}} &= t_C = {self.t_C}\\,\\text{{minutes}}\\\\"
            f"\\text{{Duration of condensation is given by:}} &\\\\"
            f"t_{{\\text{{duration}}}} &= t_C - t_B\\\\"
            f"&= {self.t_C} - {self.t_B}\\\\"
            f"&= {round(self.t_C - self.t_B, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{minutes}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        times = [self.t_A, self.t_B, self.t_C, self.t_D]
        temps = [self.start_temp, self.plateau_temp, self.plateau_temp, self.end_temp]

        ax.plot(times, temps, 'k-', linewidth=2)
        ax.scatter(times, temps, color='black', zorder=3)

        labels = ["A", "B", "C", "D"]
        for t, temp, label in zip(times, temps, labels):
            ax.text(t, temp + 2, label, fontsize=12, fontweight='bold', ha='center')

        ax.set_xlabel("Time (minutes)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Temperature (°C)", fontsize=14, fontweight='bold')
        ax.set_title("Cooling Curve of a Substance", fontsize=16, fontweight='bold')

        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_axisbelow(True)

        ax.set_xlim(self.t_A, self.t_D + 1)
        ax.set_ylim(self.end_temp - 10, self.start_temp + 10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem102:
    """
    Topic: States of matter
    Subtopic: Diffusion
    Visual: Two chambers showing gas diffusion over time
    Task: Calculate diffusion rate
    """

    def __init__(self):
        self.distance = rnd.randint(4, 12)
        self.time = rnd.randint(2, 8)

        self.rate = self.distance / self.time
        self.answer = round(self.rate, 2)

        self.description = (
            "A gas diffuses across a chamber as shown in the diagram. "
            "The gas travels a measured distance over a period of time.\n\n"
            "Calculate the rate of diffusion of the gas."
        )

        self.topic = "States of matter"
        self.subtopic = "Diffusion"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance travelled}} &= {self.distance}\\,\\text{{cm}}\\\\"
            f"\\text{{Time taken}} &= {self.time}\\,\\text{{s}}\\\\"
            f"\\text{{Diffusion rate is given by:}} &\\\\"
            f"\\text{{Rate}} &= \\frac{{\\text{{distance}}}}{{\\text{{time}}}}\\\\"
            f"&= \\frac{{{self.distance}}}{{{self.time}}}\\\\"
            f"&= {round(self.distance / self.time, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        chamber = Rectangle((0, 0), 10, 4, fill=False, linewidth=2)
        ax.add_patch(chamber)

        divider_x = 3
        ax.plot([divider_x, divider_x], [0, 4], linestyle='--', color='black')

        for _ in range(20):
            x = rnd.uniform(0.3, divider_x - 0.3)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black'))

        for _ in range(15):
            x = rnd.uniform(divider_x + 0.3, 9.7)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black'))

        ax.arrow(divider_x, 2, 3, 0, head_width=0.3, head_length=0.4, fc='black', ec='black')

        ax.text(1.5, 4.3, "High concentration", ha='center', fontsize=11)
        ax.text(7.5, 4.3, "Low concentration", ha='center', fontsize=11)

        ax.text(5, -0.7, f"Distance travelled = {self.distance} cm", ha='center', fontsize=11)
        ax.text(5, -1.3, f"Time taken = {self.time} s", ha='center', fontsize=11)

        ax.set_xlim(-1, 11)
        ax.set_ylim(-2, 5.5)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.set_title("Diffusion of a Gas in a Chamber", fontsize=16, fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem103:
    """
    Topic: Atoms, elements and compounds
    Subtopic: Ions and ionic bonds
    Visual: Dot and cross diagram showing electron transfer
    Task: Determine number of electrons transferred (single numeric answer)
    """

    def __init__(self):
        ionic_pairs = [
            ("Na", "Cl", 1),
            ("K", "Cl", 1),
            ("Mg", "O", 2),
            ("Ca", "O", 2),
            ("Li", "F", 1),
            ("Al", "O", 3),
        ]

        self.metal, self.nonmetal, self.electrons_transferred = rnd.choice(ionic_pairs)

        self.answer = self.electrons_transferred

        self.description = (
            f"The diagram shows electron transfer between {self.metal} and {self.nonmetal} "
            "during ionic bonding.\n\n"
            "Determine the number of electrons transferred."
        )

        self.topic = "Atoms, elements and compounds"
        self.subtopic = "Ions and ionic bonds"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Metal atom:}} &\\quad \\text{{{self.metal}}}\\\\"
            f"\\text{{Non-metal atom:}} &\\quad \\text{{{self.nonmetal}}}\\\\"
            "\\text{{Ionic bonding involves the transfer of valence electrons.}} &\\\\"
            "\\text{{Number of electrons transferred (}} n \\text{{):}} &\\\\"
            f"n &= {self.electrons_transferred}\\\\"
            f"\\text{{Result}} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        metal_center = (3, 5)
        nonmetal_center = (9, 5)

        metal_radius = 1.2
        nonmetal_radius = 1.2

        ax.add_patch(Circle(metal_center, metal_radius, fill=False, linewidth=2))
        ax.add_patch(Circle(nonmetal_center, nonmetal_radius, fill=False, linewidth=2))

        ax.text(*metal_center, self.metal, ha='center', va='center', fontsize=16, fontweight='bold')
        ax.text(*nonmetal_center, self.nonmetal, ha='center', va='center', fontsize=16, fontweight='bold')

        for i in range(self.electrons_transferred):
            angle = 2 * np.pi * i / max(self.electrons_transferred, 1)
            x = metal_center[0] + 0.9 * np.cos(angle)
            y = metal_center[1] + 0.9 * np.sin(angle)
            ax.add_patch(Circle((x, y), 0.15, color='black'))

        for i in range(self.electrons_transferred):
            angle = 2 * np.pi * i / max(self.electrons_transferred, 1)
            x = nonmetal_center[0] + 0.9 * np.cos(angle)
            y = nonmetal_center[1] + 0.9 * np.sin(angle)
            ax.add_patch(Circle((x, y), 0.15, fill=False, linewidth=2))

        ax.arrow(
            metal_center[0] + metal_radius,
            metal_center[1],
            nonmetal_center[0] - metal_center[0] - 2 * metal_radius,
            0,
            head_width=0.3,
            head_length=0.4,
            fc='black',
            ec='black'
        )

        ax.set_xlim(0, 12)
        ax.set_ylim(2, 8)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.set_title(
            f"Electron Transfer During Ionic Bonding ({self.metal} and {self.nonmetal})",
            fontsize=16,
            fontweight='bold'
        )

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem104:
    """
    Topic: Atoms, elements and compounds
    Subtopic: Simple molecules and covalent bonds
    Visual: Dot-and-cross diagram of a simple covalent molecule
    Task: Determine the number of covalent bonds shown (single numeric answer)
    """

    def __init__(self):

        molecules = [
            {"name": "hydrogen", "formula": "H2", "atoms": ["H", "H"], "bonds": 1},
            {"name": "chlorine", "formula": "Cl2", "atoms": ["Cl", "Cl"], "bonds": 1},
            {"name": "oxygen", "formula": "O2", "atoms": ["O", "O"], "bonds": 2},
            {"name": "nitrogen", "formula": "N2", "atoms": ["N", "N"], "bonds": 3},
            {"name": "water", "formula": "H2O", "atoms": ["H", "O", "H"], "bonds": 2},
            {"name": "carbon dioxide", "formula": "CO2", "atoms": ["O", "C", "O"], "bonds": 4},
            {"name": "methane", "formula": "CH4", "atoms": ["H", "C", "H", "H", "H"], "bonds": 4},
            {"name": "ammonia", "formula": "NH3", "atoms": ["H", "N", "H", "H"], "bonds": 3},
        ]

        self.molecule = rnd.choice(molecules)
        self.name = self.molecule["name"]
        self.formula = self.molecule["formula"]
        self.atoms = self.molecule["atoms"]

        self.answer = self.molecule["bonds"]

        self.description = (
            f"The dot-and-cross diagram shows the covalent bonding in a molecule of {self.name} "
            f"({self.formula}).\n\n"
            "How many covalent bonds are shown in the diagram?"
        )

        self.topic = "Atoms, elements and compounds"
        self.subtopic = "Simple molecules and covalent bonds"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\begin{aligned}"
            f"\\text{{Molecule}} &= \\text{{{self.name}}}\\\\"
            f"\\text{{Chemical Formula}} &= \\text{{{self.formula}}}\\\\"
            f"\\text{{The number of covalent bonds }} (n) \\text{{ is the total number of shared electron pairs between atoms.}}\\\\"
            f"n &= {self.answer}\\\\"
            f"\\text{{Total covalent bonds}} &= {self.answer}"
            "\\end{aligned}"
        )

    def _draw_electron(self, ax, x, y, style="dot"):
        if style == "dot":
            ax.add_patch(Circle((x, y), 0.08, color="black"))
        else:
            ax.plot([x - 0.08, x + 0.08], [y - 0.08, y + 0.08], color="black", linewidth=1.5)
            ax.plot([x - 0.08, x + 0.08], [y + 0.08, y - 0.08], color="black", linewidth=1.5)

    def _draw_shared_pair(self, ax, x, y, orientation="horizontal"):
        if orientation == "horizontal":
            self._draw_electron(ax, x - 0.12, y, "dot")
            self._draw_electron(ax, x + 0.12, y, "cross")
        else:
            self._draw_electron(ax, x, y - 0.12, "dot")
            self._draw_electron(ax, x, y + 0.12, "cross")

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        ax.set_aspect("equal")
        ax.axis("off")

        r = 0.9

        if self.formula in ["H2", "Cl2", "O2", "N2"]:
            positions = [(4, 5), (8, 5)]
            bonds_between = [(0, 1, self.answer)] 

        elif self.formula in ["H2O"]:
            positions = [(3.8, 5), (6, 5), (8.2, 5)]
            bonds_between = [(0, 1, 1), (1, 2, 1)]

        elif self.formula in ["CO2"]:
            positions = [(3.8, 5), (6, 5), (8.2, 5)]
            bonds_between = [(0, 1, 2), (1, 2, 2)]

        elif self.formula in ["CH4"]:
            positions = [(6, 5), (6, 7.3), (8.3, 5), (6, 2.7), (3.7, 5)]
            bonds_between = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]

        elif self.formula in ["NH3"]:
            positions = [(6, 5), (6, 7.1), (8.1, 4.2), (3.9, 4.2)]
            bonds_between = [(0, 1, 1), (0, 2, 1), (0, 3, 1)]

        else:
            positions = [(4, 5), (8, 5)]
            bonds_between = [(0, 1, 1)]

        for (x, y), atom in zip(positions, self.atoms):
            ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
            ax.text(x, y, atom, ha="center", va="center", fontsize=16, fontweight="bold")

        for i, j, bond_order in bonds_between:
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            # bond line
            ax.plot([x1, x2], [y1, y2], color="black", linewidth=2)

            mx, my = (x1 + x2) / 2, (y1 + y2) / 2

            if abs(y2 - y1) > abs(x2 - x1):
                orient = "vertical"
            else:
                orient = "horizontal"

            offsets = []
            if bond_order == 1:
                offsets = [(0, 0)]
            elif bond_order == 2:
                offsets = [(-0.15, 0.15), (0.15, -0.15)]
            elif bond_order == 3:
                offsets = [(-0.25, 0.25), (0, 0), (0.25, -0.25)]
            else:
                offsets = [(0, 0)]

            for dx, dy in offsets:
                self._draw_shared_pair(ax, mx + dx, my + dy, orientation=orient)

        ax.set_title(
            f"Dot-and-Cross Diagram: {self.name.capitalize()} ({self.formula})",
            fontsize=16,
            fontweight="bold"
        )

        ax.set_xlim(1.5, 10.5)
        ax.set_ylim(1.5, 8.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem105:

    def __init__(self):

        molecules = [
            {"name": "hydrogen", "formula": "H2", "shared_electrons": 2},
            {"name": "chlorine", "formula": "Cl2", "shared_electrons": 2},
            {"name": "oxygen", "formula": "O2", "shared_electrons": 4},
            {"name": "nitrogen", "formula": "N2", "shared_electrons": 6},
            {"name": "water", "formula": "H2O", "shared_electrons": 4},
            {"name": "ammonia", "formula": "NH3", "shared_electrons": 6},
            {"name": "methane", "formula": "CH4", "shared_electrons": 8},
            {"name": "carbon dioxide", "formula": "CO2", "shared_electrons": 8},
        ]

        self.molecule = rnd.choice(molecules)
        self.name = self.molecule["name"]
        self.formula = self.molecule["formula"]
        self.shared_electrons = self.molecule["shared_electrons"]

        self.answer = self.shared_electrons

        self.description = (
            f"The dot-and-cross diagram shows the bonding electrons in a molecule of {self.name} ({self.formula}).\n\n"
            "Determine the total number of bonding (shared) electrons in the molecule."
        )

        self.topic = "Atoms, elements and compounds"
        self.subtopic = "Simple molecules and covalent bonds"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: }} & {self.name} \\text{{ ({self.formula})}} \\\\"
            f"\\text{{Number of shared electrons per single covalent bond}} &= 2 \\\\"
            "\\text{{Total bonding electrons}} &= \\text{{Total number of shared electron pairs}} \\times 2 \\\\"
            f"\\text{{Based on the dot-and-cross structure of }} {self.formula} & \\text{{:}} \\\\"
            f"n_{{shared}} &= {round(float(self.shared_electrons), 10)} \\\\"
            f"\\text{{Result}} &= {self.answer} \\\\"
            "\\end{aligned}\\]"
        )

    def _draw_dot(self, ax, x, y):
        ax.add_patch(Circle((x, y), 0.07, color="black"))

    def _draw_cross(self, ax, x, y):
        ax.plot([x-0.07, x+0.07], [y-0.07, y+0.07], color="black", linewidth=1.2)
        ax.plot([x-0.07, x+0.07], [y+0.07, y-0.07], color="black", linewidth=1.2)

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        r = 0.9

        if self.formula in ["H2", "Cl2", "O2", "N2"]:
            positions = [(4, 5), (8, 5)]
            bonds = self.shared_electrons // 2
            for (x, y), atom in zip(positions, list(self.formula.replace("2", ""))*2):
                ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
                ax.text(x, y, atom, ha="center", va="center", fontsize=16, fontweight="bold")

            x1, y1 = positions[0]
            x2, y2 = positions[1]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2

            offsets = []
            if bonds == 1:
                offsets = [(0, 0)]
            elif bonds == 2:
                offsets = [(-0.18, 0.18), (0.18, -0.18)]
            elif bonds == 3:
                offsets = [(-0.3, 0.3), (0, 0), (0.3, -0.3)]

            for dx, dy in offsets:
                self._draw_dot(ax, mx + dx - 0.1, my + dy)
                self._draw_cross(ax, mx + dx + 0.1, my + dy)

        else:
            if self.formula == "H2O":
                atoms = ["H", "O", "H"]
                positions = [(3.8, 5), (6, 5), (8.2, 5)]
                bond_pairs = [(0, 1), (1, 2)]
            elif self.formula == "NH3":
                atoms = ["H", "N", "H", "H"]
                positions = [(6, 5), (6, 7.1), (8.1, 4.2), (3.9, 4.2)]
                bond_pairs = [(0, 1), (1, 2), (1, 3)]
            elif self.formula == "CH4":
                atoms = ["C", "H", "H", "H", "H"]
                positions = [(6, 5), (6, 7.3), (8.3, 5), (6, 2.7), (3.7, 5)]
                bond_pairs = [(0, 1), (0, 2), (0, 3), (0, 4)]
            else:
                atoms = ["O", "C", "O"]
                positions = [(3.8, 5), (6, 5), (8.2, 5)]
                bond_pairs = [(0, 1), (1, 2)]

            for (x, y), atom in zip(positions, atoms):
                ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
                ax.text(x, y, atom, ha="center", va="center", fontsize=16, fontweight="bold")

            for i, j in bond_pairs:
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                self._draw_dot(ax, mx - 0.1, my)
                self._draw_cross(ax, mx + 0.1, my)

        ax.set_title(
            f"Bonding Electrons in {self.name.capitalize()} ({self.formula})",
            fontsize=16,
            fontweight="bold"
        )

        ax.set_xlim(1.5, 10.5)
        ax.set_ylim(1.5, 8.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()
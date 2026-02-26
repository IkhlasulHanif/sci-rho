import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys
import math
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle

sys.path.append(os.path.dirname(__file__))
from helper import *

DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "chemistry", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

FARADAY = 96500
MOLAR_MASS_CU = 63.5
MOLAR_MASS_AG = 108
MOLAR_MASS_NI = 58.7 
DENSITY_NI = 8.9

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

class Chem106:
    
    def __init__(self):

        reactions = [
            {
                "name": "Magnesium and Hydrochloric Acid",
                "reactant_A": "Mg",
                "reactant_B": "HCl",
                "product": "H2",
                "coeff_A": 1,
                "coeff_B": 2,
                "Ar_A": 24,
                "Ar_B": 36.5
            },
            {
                "name": "Iron and Sulfur",
                "reactant_A": "Fe",
                "reactant_B": "S",
                "product": "FeS",
                "coeff_A": 1,
                "coeff_B": 1,
                "Ar_A": 56,
                "Ar_B": 32
            },
            {
                "name": "Aluminium and Oxygen",
                "reactant_A": "Al",
                "reactant_B": "O2",
                "product": "Al2O3",
                "coeff_A": 4,
                "coeff_B": 3,
                "Ar_A": 27,
                "Ar_B": 32
            }
        ]

        self.reaction = rnd.choice(reactions)

        self.mass_A = rnd.randint(5, 25)
        self.mass_B = rnd.randint(5, 40)

        self.moles_A = self.mass_A / self.reaction["Ar_A"]
        self.moles_B = self.mass_B / self.reaction["Ar_B"]

        self.norm_A = self.moles_A / self.reaction["coeff_A"]
        self.norm_B = self.moles_B / self.reaction["coeff_B"]

        if self.norm_A < self.norm_B:
            self.limiting = "A"
            self.limiting_moles = self.moles_A
            self.excess_initial = self.moles_B
            self.excess_coeff = self.reaction["coeff_B"]
            self.limiting_coeff = self.reaction["coeff_A"]
            self.excess_Ar = self.reaction["Ar_B"]
        else:
            self.limiting = "B"
            self.limiting_moles = self.moles_B
            self.excess_initial = self.moles_A
            self.excess_coeff = self.reaction["coeff_A"]
            self.limiting_coeff = self.reaction["coeff_B"]
            self.excess_Ar = self.reaction["Ar_A"]

        self.excess_used = self.limiting_moles * (self.excess_coeff / self.limiting_coeff)
        self.excess_leftover_moles = self.excess_initial - self.excess_used
        self.answer = round(self.excess_leftover_moles * self.excess_Ar, 2)

        self.description = (
            f"The graph shows the concentration of two reactants during the reaction "
            f"{self.reaction['reactant_A']} reacting with {self.reaction['reactant_B']}.\n\n"
            f"Initial mass {self.reaction['reactant_A']} = {self.mass_A} g\n"
            f"Initial mass {self.reaction['reactant_B']} = {self.mass_B} g\n\n"
            "Using stoichiometry and the graph, calculate the mass of the excess reactant remaining."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Limiting reagent and excess"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Moles of A}} &= \\frac{{{self.mass_A}}}{{{self.reaction['Ar_A']}}} = {round(self.moles_A,10)}\\\\"
            f"\\text{{Moles of B}} &= \\frac{{{self.mass_B}}}{{{self.reaction['Ar_B']}}} = {round(self.moles_B,10)}\\\\"
            f"\\text{{Limiting reagent determined by mole ratio}} &\\\\"
            f"\\text{{Excess moles remaining}} &= {round(self.excess_leftover_moles,10)}\\\\"
            f"\\text{{Mass remaining}} &= n \\times A_r\\\\"
            f"&= {round(self.excess_leftover_moles,10)} \\times {self.excess_Ar}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)

        if self.limiting == "A":
            conc_A = np.exp(-0.4 * t)
            conc_B = np.exp(-0.4 * t) + 0.2
        else:
            conc_B = np.exp(-0.4 * t)
            conc_A = np.exp(-0.4 * t) + 0.2

        ax.plot(t, conc_A, linewidth=3, color="#2E86C1", label=self.reaction["reactant_A"])
        ax.plot(t, conc_B, linewidth=3, color="#C39A3A", label=self.reaction["reactant_B"])

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Concentration (mol dm$^{-3}$)", fontsize=14, fontweight='bold')
        ax.set_title("Reactant Concentration vs Time", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, max(max(conc_A), max(conc_B)) * 1.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem107:

    def __init__(self):

        chains = [
            {
                "name": "Calcium Carbonate Thermal Decomposition + Acid Reaction",
                "stage1": "CaCO3 → CaO + CO2",
                "stage2": "CaO + 2HCl → CaCl2 + H2O",
                "Ar_start": 100,
                "Ar_final": 111
            },
            {
                "name": "Copper Carbonate Decomposition + Reduction",
                "stage1": "CuCO3 → CuO + CO2",
                "stage2": "CuO + H2 → Cu + H2O",
                "Ar_start": 124,
                "Ar_final": 63.5
            },
            {
                "name": "Zinc Carbonate Decomposition + Acid Reaction",
                "stage1": "ZnCO3 → ZnO + CO2",
                "stage2": "ZnO + 2HCl → ZnCl2 + H2O",
                "Ar_start": 125,
                "Ar_final": 136
            }
        ]

        self.chain = rnd.choice(chains)

        self.start_mass = rnd.randint(20, 80)

        self.start_moles = self.start_mass / self.chain["Ar_start"]

        self.final_moles = self.start_moles

        self.answer = round(self.final_moles * self.chain["Ar_final"], 2)

        self.description = (
            f"The graph shows the amount of substances during a multi-stage reaction chain.\n\n"
            f"Stage 1: {self.chain['stage1']}\n"
            f"Stage 2: {self.chain['stage2']}\n\n"
            f"Initial mass of starting compound = {self.start_mass} g\n\n"
            "Using stoichiometry and the graph, calculate the mass of final product formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Multi-stage reaction chains"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Moles of starting compound}} &= \\frac{{{self.start_mass}}}{{{self.chain['Ar_start']}}}\\\\"
            f"&= {round(self.start_moles,10)}\\\\"
            f"\\text{{Mole ratio through reaction chain is 1:1}} &\\\\"
            f"\\text{{Moles of final product}} &= {round(self.final_moles,10)}\\\\"
            f"\\text{{Mass of final product}} &= n \\times A_r\\\\"
            f"&= {round(self.final_moles,10)} \\times {self.chain['Ar_final']}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)

        start_curve = np.exp(-0.35 * t)
        intermediate_curve = np.exp(-0.35 * (t - 3)**2)
        product_curve = 1 - np.exp(-0.35 * t)

        ax.plot(t, start_curve, linewidth=3, color="#2E86C1", label="Starting compound")
        ax.plot(t, intermediate_curve, linewidth=3, color="#F39C12", label="Intermediate")
        ax.plot(t, product_curve, linewidth=3, color="#28B463", label="Final product")

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Relative amount", fontsize=14, fontweight='bold')
        ax.set_title("Multi-Stage Reaction Chain Progress", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem108: 

    def __init__(self):

        reactions = [
            {
                "name": "Iron and Sulfur",
                "eq": "Fe + S → FeS",
                "A": "Fe",
                "B": "S",
                "P": "FeS",
                "coeff_A": 1,
                "coeff_B": 1,
                "coeff_P": 1,
                "Ar_A": 56,
                "Ar_B": 32,
                "Ar_P": 88
            },
            {
                "name": "Magnesium and Oxygen",
                "eq": "2Mg + O2 → 2MgO",
                "A": "Mg",
                "B": "O2",
                "P": "MgO",
                "coeff_A": 2,
                "coeff_B": 1,
                "coeff_P": 2,
                "Ar_A": 24,
                "Ar_B": 32,
                "Ar_P": 40
            },
            {
                "name": "Aluminium and Oxygen",
                "eq": "4Al + 3O2 → 2Al2O3",
                "A": "Al",
                "B": "O2",
                "P": "Al2O3",
                "coeff_A": 4,
                "coeff_B": 3,
                "coeff_P": 2,
                "Ar_A": 27,
                "Ar_B": 32,
                "Ar_P": 102
            }
        ]

        self.r = rnd.choice(reactions)

        self.mass_A = rnd.randint(8, 40)
        self.mass_B = rnd.randint(8, 60)

        self.moles_A = self.mass_A / self.r["Ar_A"]
        self.moles_B = self.mass_B / self.r["Ar_B"]

        self.norm_A = self.moles_A / self.r["coeff_A"]
        self.norm_B = self.moles_B / self.r["coeff_B"]

        if self.norm_A < self.norm_B:
            self.limiting_moles_norm = self.norm_A
        else:
            self.limiting_moles_norm = self.norm_B

        self.product_moles_theoretical = self.limiting_moles_norm * self.r["coeff_P"]

        self.theoretical_mass = self.product_moles_theoretical * self.r["Ar_P"]

        self.percent_yield_actual = rnd.randint(65, 95)

        self.actual_mass = self.theoretical_mass * self.percent_yield_actual / 100

        self.answer = round(self.percent_yield_actual, 2)

        self.description = (
            f"The graph shows reactant consumption and product formation for the reaction:\n"
            f"{self.r['eq']}\n\n"
            f"Initial mass {self.r['A']} = {self.mass_A} g\n"
            f"Initial mass {self.r['B']} = {self.mass_B} g\n\n"
            f"The actual mass of product obtained = {round(self.actual_mass,2)} g\n\n"
            "Using stoichiometry and the graph, calculate the percentage yield."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Percentage yield with limiting reagent"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"n_{{A}} &= \\frac{{{self.mass_A}}}{{{self.r['Ar_A']}}} = {round(self.moles_A,10)}\\\\"
            f"n_{{B}} &= \\frac{{{self.mass_B}}}{{{self.r['Ar_B']}}} = {round(self.moles_B,10)}\\\\"
            f"\\text{{Limiting reagent determines theoretical product moles}}\\\\"
            f"n_{{P,theoretical}} &= {round(self.product_moles_theoretical,10)}\\\\"
            f"m_{{P,theoretical}} &= n \\times A_r\\\\"
            f"&= {round(self.product_moles_theoretical,10)} \\times {self.r['Ar_P']}\\\\"
            f"&= {round(self.theoretical_mass,10)}\\\\"
            f"\\%\\text{{ yield}} &= \\frac{{m_{{actual}}}}{{m_{{theoretical}}}} \\times 100\\\\"
            f"&= \\frac{{{round(self.actual_mass,10)}}}{{{round(self.theoretical_mass,10)}}} \\times 100\\\\"
            f"&= {self.answer}\\,\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)

        limiting_curve = np.exp(-0.45 * t)
        excess_curve = np.exp(-0.45 * t) + 0.25
        theoretical_product = 1 - np.exp(-0.45 * t)
        actual_product = theoretical_product * (self.percent_yield_actual / 100)

        ax.plot(t, limiting_curve, linewidth=3, color="#2E86C1", label=f"{self.r['A']} (or limiting)")
        ax.plot(t, excess_curve, linewidth=3, color="#C39A3A", label=f"{self.r['B']} (or excess)")
        ax.plot(t, theoretical_product, linewidth=3, color="#28B463", linestyle="--", label="Theoretical product")
        ax.plot(t, actual_product, linewidth=3, color="#E74C3C", label="Actual product")

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Relative amount / concentration", fontsize=14, fontweight='bold')
        ax.set_title("Limiting Reagent and Percentage Yield Reaction Progress", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem109:

    def __init__(self):

        reactions = [
            {
                "eq": "N2 + 3H2 → 2NH3",
                "gas_A": "H2",
                "gas_B": "NH3",
                "coeff_A": 3,
                "coeff_B": 2
            },
            {
                "eq": "H2 + Cl2 → 2HCl",
                "gas_A": "H2",
                "gas_B": "HCl",
                "coeff_A": 1,
                "coeff_B": 2
            },
            {
                "eq": "2SO2 + O2 → 2SO3",
                "gas_A": "SO2",
                "gas_B": "SO3",
                "coeff_A": 2,
                "coeff_B": 2
            }
        ]

        self.r = rnd.choice(reactions)

        self.volume_A = rnd.choice([24, 36, 48, 60, 72, 96])

        self.moles_A = self.volume_A / 24

        self.moles_B = self.moles_A * (self.r["coeff_B"] / self.r["coeff_A"])

        self.volume_B = self.moles_B * 24

        self.answer = round(self.volume_B, 2)

        self.description = (
            f"The bar chart shows gas volumes for the reaction:\n"
            f"{self.r['eq']}\n\n"
            f"Volume of {self.r['gas_A']} reacted = {self.volume_A} dm³\n\n"
            "Using the 24 dm³ mol⁻¹ rule and stoichiometry, calculate the volume of product gas formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Gas volumes using molar gas volume"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Moles of gas A}} &= \\frac{{V}}{{24}}\\\\"
            f"&= \\frac{{{self.volume_A}}}{{24}}\\\\"
            f"&= {round(self.moles_A,10)}\\\\"
            f"\\text{{Mole ratio from equation}}\\\\"
            f"n_{{B}} &= n_{{A}} \\times \\frac{{{self.r['coeff_B']}}}{{{self.r['coeff_A']}}}\\\\"
            f"&= {round(self.moles_A,10)} \\times \\frac{{{self.r['coeff_B']}}}{{{self.r['coeff_A']}}}\\\\"
            f"&= {round(self.moles_B,10)}\\\\"
            f"V_{{B}} &= n_{{B}} \\times 24\\\\"
            f"&= {round(self.moles_B,10)} \\times 24\\\\"
            f"&= {self.answer}\\,\\text{{dm}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        labels = [self.r["gas_A"], self.r["gas_B"]]
        values = [self.volume_A, self.volume_B]

        colors = ["#2E86C1", "#E67E22"]

        bars = ax.bar(labels, values, color=colors, width=0.6)

        ax.set_ylabel("Gas Volume (dm³)", fontsize=14, fontweight='bold')
        ax.set_title("Gas Volume Stoichiometry", fontsize=16, fontweight='bold')

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height,
                    f"{round(height,2)}",
                    ha='center', va='bottom', fontsize=11)

        ax.grid(True, axis='y', linestyle='--', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem110:

    def __init__(self):

        systems = [
            {
                "name": "Sulfur Oxide System",
                "percent_A": 40,
                "percent_B": 60,
                "A": "S",
                "B": "O",
                "Ar_A": 32,
                "Ar_B": 16,
                "empirical": "SO2",
                "reaction": "2SO2 + O2 → 2SO3",
                "Ar_reactant": 64,
                "Ar_product": 80
            },
            {
                "name": "Nitrogen Oxide System",
                "percent_A": 30,
                "percent_B": 70,
                "A": "N",
                "B": "O",
                "Ar_A": 14,
                "Ar_B": 16,
                "empirical": "NO2",
                "reaction": "2NO2 + O2 → 2N2O5",
                "Ar_reactant": 46,
                "Ar_product": 108
            }
        ]

        self.sys = rnd.choice(systems)

        self.sample_mass = rnd.randint(10, 40)

        self.mass_A = self.sample_mass * self.sys["percent_A"] / 100
        self.mass_B = self.sample_mass * self.sys["percent_B"] / 100

        self.moles_A = self.mass_A / self.sys["Ar_A"]
        self.moles_B = self.mass_B / self.sys["Ar_B"]

        self.ratio_A = self.moles_A / min(self.moles_A, self.moles_B)
        self.ratio_B = self.moles_B / min(self.moles_A, self.moles_B)

        self.reactant_mass_given = rnd.randint(20, 80)

        self.reactant_moles = self.reactant_mass_given / self.sys["Ar_reactant"]

        self.product_moles = self.reactant_moles

        self.product_mass = self.product_moles * self.sys["Ar_product"]

        self.answer = round(self.product_mass, 2)

        self.description = (
            f"A compound contains {self.sys['percent_A']}% {self.sys['A']} and "
            f"{self.sys['percent_B']}% {self.sys['B']}.\n\n"
            f"Empirical formula determined = {self.sys['empirical']}\n"
            f"Reaction: {self.sys['reaction']}\n\n"
            f"{self.reactant_mass_given} g of {self.sys['empirical']} reacts.\n\n"
            "Calculate the mass of final product formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Empirical formula → balanced equation → mass product"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"m_A &= {round(self.mass_A,10)}\\\\"
            f"m_B &= {round(self.mass_B,10)}\\\\"
            f"n_A &= \\frac{{m}}{{A_r}} = {round(self.moles_A,10)}\\\\"
            f"n_B &= \\frac{{m}}{{A_r}} = {round(self.moles_B,10)}\\\\"
            f"\\text{{Empirical ratio}} &\\\\"
            f"&= {round(self.ratio_A,10)} : {round(self.ratio_B,10)}\\\\"
            f"n_{{reactant}} &= \\frac{{{self.reactant_mass_given}}}{{{self.sys['Ar_reactant']}}}\\\\"
            f"&= {round(self.reactant_moles,10)}\\\\"
            f"m_{{product}} &= n \\times A_r\\\\"
            f"&= {round(self.product_moles,10)} \\times {self.sys['Ar_product']}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(8, 10))

        beaker = Polygon([
            (2, 8),
            (6, 8),
            (5.5, 2),
            (2.5, 2)
        ], closed=True, fill=False, linewidth=2)

        ax.add_patch(beaker)

        liquid = Polygon([
            (2.4, 3),
            (5.6, 3),
            (5.3, 2.2),
            (2.7, 2.2)
        ], closed=True, color="#AED6F1")

        ax.add_patch(liquid)

        ax.text(4, 7.2, self.sys["empirical"], ha='center', fontsize=16, fontweight='bold')

        ax.text(4, 1.5, f"{self.reactant_mass_given} g sample", ha='center', fontsize=12)

        ax.text(4, 9, "Beaker Reaction Setup", ha='center', fontsize=14, fontweight='bold')

        ax.set_xlim(0, 8)
        ax.set_ylim(0, 10)
        ax.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem111:

    def __init__(self):

        self.F = 96500
        self.Ar_Cu = 63.5

        self.current = rnd.choice([0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5])
        self.time_min = rnd.choice([5, 8, 10, 12, 15, 20, 25, 30, 40])

        self.time_s = self.time_min * 60
        self.charge = self.current * self.time_s
        self.moles_e = self.charge / self.F
        self.moles_cu = self.moles_e / 2
        self.mass_cu = self.moles_cu * self.Ar_Cu

        self.answer = round(self.mass_cu, 2)

        self.description = (
            "The diagram shows a standard electrolysis setup with an ammeter.\n\n"
            "Copper(II) ions are reduced at the cathode:\n"
            "Cu^{2+} + 2e^- → Cu\n\n"
            f"Current = {self.current} A\n"
            f"Time = {self.time_min} minutes\n\n"
            "Calculate the mass of copper deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis mass / moles / charge chain"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"I &= {round(self.current,10)}\\,\\text{{A}}\\\\"
            f"t &= {round(self.time_min,10)}\\,\\text{{min}} = {round(self.time_s,10)}\\,\\text{{s}}\\\\"
            f"Q &= It\\\\"
            f"&= {round(self.current,10)} \\times {round(self.time_s,10)}\\\\"
            f"&= {round(self.charge,10)}\\,\\text{{C}}\\\\"
            f"n(e^-) &= \\frac{{Q}}{{F}}\\\\"
            f"&= \\frac{{{round(self.charge,10)}}}{{{round(self.F,10)}}}\\\\"
            f"&= {round(self.moles_e,10)}\\,\\text{{mol}}\\\\"
            f"\\text{{From }}\\,\\text{{Cu}}^{{2+}} + 2e^- \\rightarrow \\text{{Cu}}:\\quad n(\\text{{Cu}}) &= \\frac{{n(e^-)}}2\\\\"
            f"&= \\frac{{{round(self.moles_e,10)}}}{2}\\\\"
            f"&= {round(self.moles_cu,10)}\\,\\text{{mol}}\\\\"
            f"m(\\text{{Cu}}) &= n(\\text{{Cu}})\\times A_r(\\text{{Cu}})\\\\"
            f"&= {round(self.moles_cu,10)} \\times {round(self.Ar_Cu,10)}\\\\"
            f"&= {round(self.mass_cu,10)}\\,\\text{{g}}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(11, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 20)
        ax.set_ylim(0, 12)

        beaker = Rectangle((6, 2), 8, 7, fill=False, linewidth=2)
        ax.add_patch(beaker)

        solution = Rectangle((6.2, 2.2), 7.6, 4.4, facecolor="#CFE8FF", edgecolor="none", alpha=0.9)
        ax.add_patch(solution)

        ax.text(10, 6.9, "electrolyte", ha="center", va="bottom", fontsize=11, fontweight="bold", color="#1F4E79")

        anode = Rectangle((7.2, 3), 0.4, 5.2, facecolor="#6E6E6E", edgecolor="none")
        cathode = Rectangle((12.4, 3), 0.4, 5.2, facecolor="#6E6E6E", edgecolor="none")
        ax.add_patch(anode)
        ax.add_patch(cathode)

        ax.text(7.4, 8.6, "anode (+)", ha="center", va="bottom", fontsize=10, fontweight="bold")
        ax.text(12.6, 8.6, "cathode (−)", ha="center", va="bottom", fontsize=10, fontweight="bold")

        ax.text(7.4, 2.4, "oxidation", ha="center", va="top", fontsize=9, color="#7D2E2E")
        ax.text(12.6, 2.4, "reduction", ha="center", va="top", fontsize=9, color="#1B5E20")

        ax.text(7.4, 1.6, "2H2O → O2 + 4H+ + 4e−", ha="center", va="top", fontsize=9, color="#7D2E2E")
        ax.text(12.6, 1.6, "Cu2+ + 2e− → Cu", ha="center", va="top", fontsize=9, color="#1B5E20")

        psu = Rectangle((1.2, 6.8), 3.8, 3.0, fill=False, linewidth=2)
        ax.add_patch(psu)
        ax.text(3.1, 8.3, "DC supply", ha="center", va="center", fontsize=11, fontweight="bold")

        ax.text(1.7, 7.3, "+", fontsize=14, fontweight="bold", color="#B03A2E")
        ax.text(4.5, 7.3, "−", fontsize=14, fontweight="bold", color="#1F4E79")

        ammeter_center = (4.0, 10.2)
        ammeter = Circle(ammeter_center, 0.85, fill=False, linewidth=2)
        ax.add_patch(ammeter)
        ax.text(ammeter_center[0], ammeter_center[1] + 0.05, "A", ha="center", va="center", fontsize=14, fontweight="bold")
        ax.text(ammeter_center[0], ammeter_center[1] - 1.3, f"{self.current} A", ha="center", va="center", fontsize=11, fontweight="bold", color="#1F4E79")

        wire_color_pos = "#B03A2E"
        wire_color_neg = "#1F4E79"

        ax.plot([1.7, 1.7, 7.4, 7.4], [7.3, 10.2, 10.2, 8.2], color=wire_color_pos, linewidth=3)
        ax.plot([4.85, 12.6, 12.6, 4.5], [10.2, 10.2, 8.2, 7.3], color=wire_color_neg, linewidth=3)

        arrow1 = FancyArrowPatch((2.6, 10.2), (3.2, 10.2), arrowstyle="->", mutation_scale=15, linewidth=2, color=wire_color_pos)
        arrow2 = FancyArrowPatch((10.8, 10.2), (10.2, 10.2), arrowstyle="->", mutation_scale=15, linewidth=2, color=wire_color_neg)
        ax.add_patch(arrow1)
        ax.add_patch(arrow2)

        ax.text(10, 11.3, "current flow in circuit", ha="center", va="center", fontsize=11, fontweight="bold")

        ax.set_title("Electrolysis Apparatus with Ammeter", fontsize=16, fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem112:

    def __init__(self):

        systems = [
            {
                "cation": "Ag+",
                "metal": "Ag",
                "Ar_metal": 108,
                "electron_ratio": 1,
                "color": "#B0B0B0"
            },
            {
                "cation": "Cu2+",
                "metal": "Cu",
                "Ar_metal": 63.5,
                "electron_ratio": 2,
                "color": "#C87533"
            }
        ]

        self.sys = rnd.choice(systems)

        self.F = 96500

        self.volume_dm3 = rnd.choice([0.25, 0.5, 1.0])
        self.conc = rnd.choice([0.2, 0.4, 0.6, 0.8])

        self.current = rnd.choice([0.5, 1.0, 1.5, 2.0])
        self.time_min = rnd.choice([5, 10, 15, 20, 30])

        self.time_s = self.time_min * 60

        self.initial_moles_ion = self.volume_dm3 * self.conc

        self.charge = self.current * self.time_s
        self.moles_e = self.charge / self.F
        self.moles_metal_possible_from_charge = self.moles_e / self.sys["electron_ratio"]

        self.moles_metal_possible_from_ion = self.initial_moles_ion

        self.actual_moles_metal = min(
            self.moles_metal_possible_from_charge,
            self.moles_metal_possible_from_ion
        )

        self.answer = round(self.actual_moles_metal * self.sys["Ar_metal"], 2)

        self.description = (
            "The diagrams show ion concentration before and after electrolysis.\n\n"
            f"Cation: {self.sys['cation']}\n"
            f"Volume = {self.volume_dm3} dm³\n"
            f"Concentration = {self.conc} mol dm⁻³\n"
            f"Current = {self.current} A\n"
            f"Time = {self.time_min} minutes\n\n"
            "Calculate the mass of metal deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis limiting ion in solution"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"n_{{ion,initial}} &= V \\times C\\\\"
            f"&= {round(self.volume_dm3,10)} \\times {round(self.conc,10)}\\\\"
            f"&= {round(self.initial_moles_ion,10)}\\\\"
            f"Q &= It = {round(self.current,10)} \\times {round(self.time_s,10)} = {round(self.charge,10)}\\\\"
            f"n(e^-) &= \\frac{{Q}}{{F}} = \\frac{{{round(self.charge,10)}}}{{{round(self.F,10)}}} = {round(self.moles_e,10)}\\\\"
            f"n_{{metal,charge}} &= \\frac{{n(e^-)}}{{{self.sys['electron_ratio']}}} = {round(self.moles_metal_possible_from_charge,10)}\\\\"
            f"n_{{metal,actual}} &= \\min({round(self.moles_metal_possible_from_charge,10)}, {round(self.moles_metal_possible_from_ion,10)})\\\\"
            f"&= {round(self.actual_moles_metal,10)}\\\\"
            f"m &= n \\times A_r = {round(self.actual_moles_metal,10)} \\times {self.sys['Ar_metal']}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def _draw_beaker(self, ax, x_offset, label, ion_count_scale):

        beaker = Rectangle((x_offset + 1, 2), 4, 6, fill=False, linewidth=2)
        ax.add_patch(beaker)

        solution = Rectangle((x_offset + 1.1, 2.1), 3.8, 3.5, facecolor="#D6EAF8", edgecolor="none")
        ax.add_patch(solution)

        ax.text(x_offset + 3, 8.5, label, ha="center", fontsize=12, fontweight="bold")

        anode = Rectangle((x_offset + 1.5, 3), 0.3, 4.5, facecolor="#666666")
        cathode = Rectangle((x_offset + 4.2, 3), 0.3, 4.5, facecolor="#666666")
        ax.add_patch(anode)
        ax.add_patch(cathode)

        for i in range(int(ion_count_scale * 8)):
            x = x_offset + rnd.uniform(1.3, 4.7)
            y = rnd.uniform(2.3, 5.3)
            ax.add_patch(Circle((x, y), 0.12, color=self.sys["color"]))
            ax.text(x, y, self.sys["cation"], fontsize=6, ha="center", va="center")

        for _ in range(6):
            start = (x_offset + rnd.uniform(2, 4), rnd.uniform(4, 6))
            end = (x_offset + 4.35, rnd.uniform(4, 6))
            arrow = FancyArrowPatch(start, end, arrowstyle="->", mutation_scale=10, color="#1B5E20")
            ax.add_patch(arrow)

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 14)
        ax.set_ylim(0, 10)

        self._draw_beaker(ax, 0, "Before Electrolysis", 1.0)
        self._draw_beaker(ax, 7, "After Electrolysis", 0.3)

        ax.text(7, 9.5, f"Initial concentration = {self.conc} mol dm⁻³", ha="center", fontsize=11)

        ax.set_title("Electrolysis with Limiting Ion in Solution", fontsize=16, fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem113:

    def __init__(self):

        self.ratio_H2 = 2
        self.ratio_O2 = 1

        self.volume_H2 = rnd.choice([24, 36, 48, 60, 72])
        self.volume_O2 = self.volume_H2 / 2

        if rnd.random() > 0.5:
            self.given_gas = "H2"
            self.given_volume = self.volume_H2
            self.answer = round(self.volume_O2, 2)
        else:
            self.given_gas = "O2"
            self.given_volume = self.volume_O2
            self.answer = round(self.volume_H2, 2)

        self.description = (
            "The Hoffman voltameter shows electrolysis of water.\n\n"
            "2H2O → 2H2 + O2\n\n"
            f"Volume of {self.given_gas} collected = {self.given_volume} cm³\n\n"
            "Calculate the volume of the other gas produced."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis gas volume and stoichiometry"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        if self.given_gas == "H2":
            calc_ratio = self.ratio_O2 / self.ratio_H2
        else:
            calc_ratio = self.ratio_H2 / self.ratio_O2

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Balanced equation gives volume ratio H2:O2 = 2:1}}\\\\"
            f"\\text{{Volume ratio used}} &= {round(calc_ratio,10)}\\\\"
            f"V_{{unknown}} &= V_{{given}} \\times \\text{{ratio}}\\\\"
            f"&= {round(self.given_volume,10)} \\times {round(calc_ratio,10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(8, 10))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 16)

        center_tube = Rectangle((4.5, 2), 1, 12, fill=False, linewidth=2)
        ax.add_patch(center_tube)

        left_tube = Rectangle((2, 6), 1, 8, fill=False, linewidth=2)
        right_tube = Rectangle((7, 6), 1, 8, fill=False, linewidth=2)

        ax.add_patch(left_tube)
        ax.add_patch(right_tube)

        left_height = 6 + (self.volume_H2 / max(self.volume_H2, self.volume_O2)) * 6
        right_height = 6 + (self.volume_O2 / max(self.volume_H2, self.volume_O2)) * 6

        left_gas = Rectangle((2.1, 6), 0.8, left_height - 6, facecolor="#AED6F1")
        right_gas = Rectangle((7.1, 6), 0.8, right_height - 6, facecolor="#F5B7B1")

        ax.add_patch(left_gas)
        ax.add_patch(right_gas)

        ax.text(2.5, 14.5, "H₂", ha="center", fontsize=14, fontweight="bold")
        ax.text(7.5, 14.5, "O₂", ha="center", fontsize=14, fontweight="bold")

        for y in np.linspace(6, 14, 9):
            ax.plot([1.9, 2], [y, y], color="black", linewidth=1)
            ax.plot([8, 8.1], [y, y], color="black", linewidth=1)

        ax.text(2.5, 5.2, f"{round(self.volume_H2,1)} cm³", ha="center", fontsize=11)
        ax.text(7.5, 5.2, f"{round(self.volume_O2,1)} cm³", ha="center", fontsize=11)

        ax.text(5, 1.2, "Electrolysis of Water (Hoffman Voltameter)", ha="center", fontsize=13, fontweight="bold")

        ax.text(5, 0.5, "Expected ratio H₂ : O₂ = 2 : 1", ha="center", fontsize=11)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem114:

    def __init__(self):

        metals = [
            {"metal": "Cu", "Ar": 63.5, "density": 8.96, "electron_ratio": 2, "color": "#C87533"},
            {"metal": "Ag", "Ar": 108, "density": 10.5, "electron_ratio": 1, "color": "#C0C0C0"},
            {"metal": "Ni", "Ar": 58.7, "density": 8.9, "electron_ratio": 2, "color": "#9FA6AD"}
        ]

        self.metal = rnd.choice(metals)

        self.current = rnd.choice([0.5, 1.0, 1.5, 2.0, 2.5])
        self.time_min = rnd.choice([10, 15, 20, 25, 30])
        self.area_cm2 = rnd.choice([10, 20, 30, 40])

        self.F = 96500

        self.time_s = self.time_min * 60
        self.charge = self.current * self.time_s
        self.moles_e = self.charge / self.F
        self.moles_metal = self.moles_e / self.metal["electron_ratio"]
        self.mass = self.moles_metal * self.metal["Ar"]

        self.volume_cm3 = self.mass / self.metal["density"]
        self.thickness_cm = self.volume_cm3 / self.area_cm2
        self.thickness_um = self.thickness_cm * 10000

        self.answer = round(self.thickness_um, 2)

        self.description = (
            "The diagram shows an electroplating setup.\n\n"
            f"Metal being plated = {self.metal['metal']}\n"
            f"Current = {self.current} A\n"
            f"Time = {self.time_min} minutes\n"
            f"Surface area plated = {self.area_cm2} cm²\n\n"
            "Calculate the coating thickness in micrometres (µm)."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electroplating thickness and mass deposition"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"Q &= It = {round(self.current,10)} \\times {round(self.time_s,10)} = {round(self.charge,10)}\\\\"
            f"n(e^-) &= \\frac{{Q}}{{F}} = \\frac{{{round(self.charge,10)}}}{{{self.F}}} = {round(self.moles_e,10)}\\\\"
            f"n(\\text{{metal}}) &= \\frac{{n(e^-)}}{{{self.metal['electron_ratio']}}} = {round(self.moles_metal,10)}\\\\"
            f"m &= nA_r = {round(self.moles_metal,10)} \\times {self.metal['Ar']} = {round(self.mass,10)}\\\\"
            f"V &= \\frac{{m}}{{\\rho}} = \\frac{{{round(self.mass,10)}}}{{{self.metal['density']}}} = {round(self.volume_cm3,10)}\\\\"
            f"t &= \\frac{{V}}{{A}} = \\frac{{{round(self.volume_cm3,10)}}}{{{self.area_cm2}}} = {round(self.thickness_cm,10)}\\\\"
            f"t &= {self.answer}\\,\\mu m"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 20)
        ax.set_ylim(0, 14)

        beaker = Rectangle((5, 3), 10, 8, fill=False, linewidth=2)
        ax.add_patch(beaker)

        solution = Rectangle((5.2, 3.2), 9.6, 5, facecolor="#D6EAF8")
        ax.add_patch(solution)

        anode = Rectangle((6.5, 4), 0.8, 6, facecolor=self.metal["color"])
        ax.add_patch(anode)
        ax.text(6.9, 10.5, f"{self.metal['metal']} anode", ha="center", fontsize=10)

        coin = Circle = Polygon([(13,6),(14,6.5),(14,7.5),(13,8),(12,7.5),(12,6.5)], closed=True, facecolor="#888888")
        ax.add_patch(coin)

        coating = Polygon([(13,6),(14,6.5),(14,7.5),(13,8),(12,7.5),(12,6.5)],
                          closed=True, fill=False, edgecolor=self.metal["color"], linewidth=3)
        ax.add_patch(coating)

        ax.text(13, 8.7, "Cathode object", ha="center", fontsize=10)
        ax.text(13, 5.2, "Metal coating", ha="center", fontsize=9, color=self.metal["color"])

        arrow = FancyArrowPatch((7.5, 7), (12, 7), arrowstyle="->", mutation_scale=15, linewidth=2)
        ax.add_patch(arrow)

        ax.text(10, 7.6, "Metal ions move", ha="center", fontsize=10)

        ax.set_title("Electroplating Setup", fontsize=16, fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem115:

    def __init__(self):

        metals = [
            {"metal": "Cu", "Ar": 63.5, "electron_ratio": 2, "color": "#C87533"},
            {"metal": "Ag", "Ar": 108, "electron_ratio": 1, "color": "#C0C0C0"},
            {"metal": "Ni", "Ar": 58.7, "electron_ratio": 2, "color": "#9FA6AD"}
        ]

        self.metal = rnd.choice(metals)

        self.ore_mass = rnd.choice([50, 80, 100, 120, 150])
        self.purity_percent = rnd.choice([70, 75, 80, 85, 90, 95])

        self.current = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0])
        self.time_min = rnd.choice([20, 30, 40, 50, 60])

        self.F = 96500

        self.pure_metal_mass_available = self.ore_mass * self.purity_percent / 100
        self.moles_metal_available = self.pure_metal_mass_available / self.metal["Ar"]

        self.time_s = self.time_min * 60
        self.charge = self.current * self.time_s
        self.moles_e = self.charge / self.F
        self.moles_metal_possible_from_charge = self.moles_e / self.metal["electron_ratio"]

        self.actual_moles_deposited = min(
            self.moles_metal_available,
            self.moles_metal_possible_from_charge
        )

        self.mass_deposited = self.actual_moles_deposited * self.metal["Ar"]

        self.answer = round(self.mass_deposited, 2)

        self.description = (
            "The diagram shows purification of an impure metal using electrolysis.\n\n"
            f"Ore mass = {self.ore_mass} g\n"
            f"Purity = {self.purity_percent}%\n"
            f"Current = {self.current} A\n"
            f"Time = {self.time_min} minutes\n\n"
            "Calculate the mass of pure metal deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis with impure ore and purity calculation"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"m_{{pure}} &= \\frac{{{self.purity_percent}}}{{100}} \\times {self.ore_mass} = {round(self.pure_metal_mass_available,10)}\\\\"
            f"n_{{metal,available}} &= \\frac{{m}}{{A_r}} = \\frac{{{round(self.pure_metal_mass_available,10)}}}{{{self.metal['Ar']}}} = {round(self.moles_metal_available,10)}\\\\"
            f"Q &= It = {round(self.current,10)} \\times {round(self.time_s,10)} = {round(self.charge,10)}\\\\"
            f"n(e^-) &= \\frac{{Q}}{{F}} = \\frac{{{round(self.charge,10)}}}{{{self.F}}} = {round(self.moles_e,10)}\\\\"
            f"n_{{metal,charge}} &= \\frac{{n(e^-)}}{{{self.metal['electron_ratio']}}} = {round(self.moles_metal_possible_from_charge,10)}\\\\"
            f"n_{{actual}} &= \\min({round(self.moles_metal_available,10)}, {round(self.moles_metal_possible_from_charge,10)}) = {round(self.actual_moles_deposited,10)}\\\\"
            f"m_{{deposited}} &= n \\times A_r = {round(self.actual_moles_deposited,10)} \\times {self.metal['Ar']} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 22)
        ax.set_ylim(0, 14)

        beaker = Rectangle((8, 3), 6, 8, fill=False, linewidth=2)
        solution = Rectangle((8.2, 3.2), 5.6, 5.5, facecolor="#D6EAF8")
        ax.add_patch(beaker)
        ax.add_patch(solution)

        anode = Rectangle((9, 4), 0.8, 6, facecolor="#777777")
        ax.add_patch(anode)
        ax.text(9.4, 10.5, "Impure anode", ha="center", fontsize=10)

        cathode = Rectangle((12.5, 4), 0.8, 6, facecolor="#DDDDDD")
        ax.add_patch(cathode)
        ax.text(12.9, 10.5, "Pure cathode", ha="center", fontsize=10)

        coating = Rectangle((12.4, 4), 1.0, 6, fill=False, edgecolor=self.metal["color"], linewidth=3)
        ax.add_patch(coating)

        for _ in range(6):
            x = rnd.uniform(9.1, 9.7)
            y = rnd.uniform(4.2, 8)
            sludge = Circle((x, y), 0.15, color="#4D4D4D")
            ax.add_patch(sludge)

        ax.text(9.4, 3.3, "Anode sludge", ha="center", fontsize=9)

        arrow = FancyArrowPatch((10, 7), (12.5, 7), arrowstyle="->", mutation_scale=15, linewidth=2, color=self.metal["color"])
        ax.add_patch(arrow)
        ax.text(11.3, 7.6, f"{self.metal['metal']} ions", ha="center", fontsize=10)

        ore_box = Rectangle((2, 7), 3, 2, fill=False, linewidth=2)
        ax.add_patch(ore_box)
        ax.text(3.5, 8, "Ore", ha="center", fontsize=11)

        furnace = Rectangle((5.5, 7), 3, 2, fill=False, linewidth=2)
        ax.add_patch(furnace)
        ax.text(7, 8, "Extraction", ha="center", fontsize=11)

        arrow_flow1 = FancyArrowPatch((5, 8), (5.5, 8), arrowstyle="->", mutation_scale=15)
        arrow_flow2 = FancyArrowPatch((8.5, 8), (8, 8), arrowstyle="->", mutation_scale=15)
        ax.add_patch(arrow_flow1)
        ax.add_patch(arrow_flow2)

        ax.set_title("Impure Ore → Extraction → Electrolysis Purification", fontsize=16, fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem116:
    """
    Topic: Electrolysis – Charge → Electrons → Ion Ratio → Mass
    Vision-based electrolysis diagram
    """

    def __init__(self):

        variations = [
            (1.5, 20),
            (1.8, 25),
            (2.0, 30),
            (2.2, 18),
            (2.5, 15),
            (1.6, 35),
            (2.8, 12),
            (3.0, 10),
            (2.4, 22),
            (1.9, 28),
        ]

        self.current, self.time_minutes = rnd.choice(variations)

        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_electrons = self.charge / FARADAY
        self.moles_copper = self.moles_electrons / 2
        self.mass_copper = self.moles_copper * MOLAR_MASS_CU

        self.answer = round(self.mass_copper, 3)

        self.description = (
            "The diagram shows electrolysis of copper(II) sulfate solution.\n"
            "Use the information in the diagram to calculate\n"
            "the mass of copper produced."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis calculations"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{Time}} &= {self.time_minutes} \\times 60 = {self.time_seconds} \\\\"
            f"\n\\text{{Q}} &= {self.current} \\times {self.time_seconds} = {self.charge} \\\\"
            f"\n\\text{{n(e}}^-\t{{)}} &= {self.charge}/96500 = {self.moles_electrons:.5f} \\\\"
            f"\n\\text{{n(Cu)}} &= {self.moles_electrons:.5f}/2 = {self.moles_copper:.5f} \\\\"
            f"\n\\text{{Mass}} &= {self.answer} \\text{{ g}}"
            r"\n\end{aligned}\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(6, 6.6, "Electrolysis of Copper(II) Sulfate",
                fontsize=16, ha='center', fontweight='bold')

        beaker = patches.Rectangle((3, 1.5), 6, 4, fill=False, linewidth=3)
        ax.add_patch(beaker)

        solution = patches.Rectangle((3.1, 1.6), 5.8, 3.5,
                                     color="#6fa8dc")
        ax.add_patch(solution)

        ax.text(6, 4.8, "CuSO₄(aq)", ha='center',
                fontsize=13, fontweight='bold')

        cathode = patches.Rectangle((4.2, 2), 0.2, 3,
                                    color="black")
        anode = patches.Rectangle((7.6, 2), 0.2, 3,
                                  color="black")
        ax.add_patch(cathode)
        ax.add_patch(anode)

        ax.text(4.3, 5.3, "-", fontsize=18, ha='center')
        ax.text(7.7, 5.3, "+", fontsize=18, ha='center')

        ax.text(6, 6.2,
                f"I = {self.current} A",
                ha='center',
                fontsize=13)

        ax.text(6, 5.9,
                f"Time = {self.time_minutes} min",
                ha='center',
                fontsize=13)

        copper_deposit = patches.Rectangle((4.05, 2),
                                           0.1, 3,
                                           color="#b87333")
        ax.add_patch(copper_deposit)

        ax.text(4.05, 1.2,
                "Cu deposited",
                fontsize=11,
                ha='left')

        ax.text(6, 0.6,
                "Cu²⁺ + 2e⁻ → Cu",
                fontsize=12,
                ha='center')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem117:
    """
    Topic: Electrolysis – Concentration + Volume → Limiting Ion vs Charge
    Vision-based limiting ion electrolysis
    """

    def __init__(self):

        variations = [
            (0.40, 0.50, 2.0, 15),
            (0.30, 0.60, 2.5, 20),
            (0.50, 0.40, 1.8, 25),
            (0.35, 0.55, 2.2, 18),
            (0.45, 0.45, 3.0, 12),
            (0.25, 0.70, 2.4, 22),
            (0.60, 0.30, 1.5, 30),
            (0.38, 0.52, 2.6, 16),
            (0.42, 0.48, 2.1, 14),
            (0.33, 0.65, 2.8, 19),
        ]

        self.concentration, self.volume_dm3, self.current, self.time_minutes = rnd.choice(variations)

        self.moles_ag_available = self.concentration * self.volume_dm3
        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_electrons = self.charge / FARADAY
        self.moles_ag_deposited = min(self.moles_ag_available, self.moles_electrons)
        self.mass_silver = self.moles_ag_deposited * MOLAR_MASS_AG

        self.answer = round(self.mass_silver, 3)

        self.description = (
            "The diagram shows electrolysis of silver nitrate solution.\n"
            "Use the information shown to calculate\n"
            "the mass of silver deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Limiting ion vs charge"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE Higher Tier"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{1. Moles of Ag}}^+ &= c \\times V = {self.concentration} \\times {self.volume_dm3} = {round(self.moles_ag_available, 10)} \\\\"
            f"\n\\text{{2. Time}} &= {self.time_minutes} \\times 60 = {self.time_seconds} \\\\"
            f"\n\\text{{3. Q}} &= {self.current} \\times {self.time_seconds} = {self.charge} \\\\"
            f"\n\\text{{4. n(e}}^-) &= {self.charge}/96500 = {round(self.moles_electrons, 10)} \\\\"
            f"\n\\text{{5. n(Ag from charge)}} &= {round(self.moles_electrons, 10)} \\\\"
            f"\n\\text{{6. Limiting n(Ag)}} &= \\min({round(self.moles_ag_available, 10)}, {round(self.moles_electrons, 10)}) = {round(self.moles_ag_deposited, 10)} \\\\"
            f"\n\\text{{7. Mass}} &= {round(self.moles_ag_deposited, 10)} \\times 108 = {self.answer} \\text{{ g}}"
            r"\n\end{aligned}\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(6, 6.6, "Electrolysis of Silver Nitrate",
                fontsize=16, ha='center', fontweight='bold')

        beaker = patches.Rectangle((3, 1.5), 6, 4, fill=False, linewidth=3)
        ax.add_patch(beaker)

        solution_height = 3.5 * (self.volume_dm3 / 0.70)
        solution = patches.Rectangle((3.1, 1.6), 5.8, solution_height,
                                     color="#d9f2ff")
        ax.add_patch(solution)

        ax.text(6, 4.9, "AgNO₃(aq)", ha='center',
                fontsize=13, fontweight='bold')

        cathode = patches.Rectangle((4.2, 2), 0.2, 3,
                                    color="black")
        anode = patches.Rectangle((7.6, 2), 0.2, 3,
                                  color="black")
        ax.add_patch(cathode)
        ax.add_patch(anode)

        ax.text(4.3, 5.3, "-", fontsize=18, ha='center')
        ax.text(7.7, 5.3, "+", fontsize=18, ha='center')

        silver_deposit = patches.Rectangle((4.05, 2),
                                           0.1, 3,
                                           color="silver")
        ax.add_patch(silver_deposit)

        ax.arrow(4.4, 6, 3.2, 0,
                 head_width=0.15,
                 head_length=0.3,
                 linewidth=2,
                 color='black')

        ax.text(6, 6.2,
                f"I = {self.current} A",
                ha='center',
                fontsize=13)

        ax.text(6, 5.9,
                f"Time = {self.time_minutes} min",
                ha='center',
                fontsize=13)

        ax.text(2.1, 3.5,
                f"{self.concentration} mol dm⁻³",
                fontsize=12)

        ax.text(6, 1.1,
                f"Volume = {self.volume_dm3} dm³",
                fontsize=12,
                ha='center')

        ax.text(6, 0.6,
                "Ag⁺ + e⁻ → Ag",
                fontsize=12,
                ha='center')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem118:
    """
    Topic: Electrolysis → Mass → Volume → Thickness
    Vision-based electroplating problem
    """

    def __init__(self):

        variations = [
            (1.5, 20, 18),
            (2.0, 25, 22),
            (2.5, 30, 20),
            (3.0, 15, 24),
            (1.8, 35, 19),
            (2.2, 40, 23),
            (1.6, 28, 21),
            (2.8, 32, 26),
            (3.2, 18, 17),
            (2.4, 45, 25),
        ]

        self.current, self.time_minutes, self.area_cm2 = rnd.choice(variations)
        self.density = DENSITY_NI

        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_e = self.charge / FARADAY
        self.moles_ni = self.moles_e / 2
        self.mass_ni = self.moles_ni * MOLAR_MASS_NI
        self.volume_cm3 = self.mass_ni / self.density
        self.thickness_cm = self.volume_cm3 / self.area_cm2
        self.thickness_mm = self.thickness_cm * 10

        self.answer = round(self.thickness_mm, 4)

        self.description = (
            "The diagram shows nickel electroplating.\n"
            "Use the information shown to calculate\n"
            "the thickness of nickel deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electroplating thickness"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE Grade 8–9"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{1. Time}} &= {self.time_minutes} \\times 60 = {self.time_seconds} \\\\"
            f"\n\\text{{2. Q}} &= {self.current} \\times {self.time_seconds} = {self.charge} \\\\"
            f"\n\\text{{3. n(e}}^-) &= {self.charge}/96500 = {round(self.moles_e, 10)} \\\\"
            f"\n\\text{{4. n(Ni)}} &= {round(self.moles_e, 10)}/2 = {round(self.moles_ni, 10)} \\\\"
            f"\n\\text{{5. Mass}} &= {round(self.moles_ni, 10)} \\times 58.7 = {round(self.mass_ni, 10)} \\\\"
            f"\n\\text{{6. Volume}} &= {round(self.mass_ni, 10)}/8.9 = {round(self.volume_cm3, 10)} \\\\"
            f"\n\\text{{7. Thickness (cm)}} &= {round(self.volume_cm3, 10)}/{self.area_cm2} = {round(self.thickness_cm, 10)} \\\\"
            f"\n\\text{{8. Thickness (mm)}} &= {round(self.thickness_cm, 10)} \\times 10 = {self.answer} \\text{{ mm}}"
            r"\n\end{aligned}\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(6, 6.6, "Nickel Electroplating Setup",
                fontsize=16, ha='center', fontweight='bold')

        beaker = patches.Rectangle((3, 1.5), 6, 4, fill=False, linewidth=3)
        ax.add_patch(beaker)

        solution = patches.Rectangle((3.1, 1.6), 5.8, 3.5,
                                     color="#a2c4c9")
        ax.add_patch(solution)

        ax.text(6, 4.9, "Ni²⁺(aq)", ha='center',
                fontsize=13, fontweight='bold')

        cathode = patches.Rectangle((4.2, 2), 0.25, 3,
                                    color="black")
        anode = patches.Rectangle((7.6, 2), 0.25, 3,
                                  color="black")
        ax.add_patch(cathode)
        ax.add_patch(anode)

        ax.text(4.3, 5.3, "-", fontsize=18, ha='center')
        ax.text(7.7, 5.3, "+", fontsize=18, ha='center')

        plated_layer = patches.Rectangle((4.05, 2),
                                         0.1, 3,
                                         color="#c0c0c0")
        ax.add_patch(plated_layer)

        ax.text(3.5, 1.2,
                f"Surface area = {self.area_cm2} cm²",
                fontsize=12)

        ax.text(8.5, 1.2,
                f"Density Ni = {self.density} g/cm³",
                fontsize=12)

        ax.arrow(4.5, 6, 3, 0,
                 head_width=0.15,
                 head_length=0.3,
                 linewidth=2,
                 color='black')

        ax.text(6, 6.2,
                f"I = {self.current} A",
                ha='center',
                fontsize=13)

        ax.text(6, 5.9,
                f"Time = {self.time_minutes} min",
                ha='center',
                fontsize=13)

        ax.text(6, 0.6,
                "Ni²⁺ + 2e⁻ → Ni",
                fontsize=12,
                ha='center')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem119:
    """
    Topic: Electroplating Thickness Calculation
    Vision-based realistic setup
    """

    def __init__(self):

        variations = [
            (1.5, 20, 20),
            (2.0, 25, 30),
            (2.5, 30, 20),
            (3.0, 15, 25),
            (1.8, 35, 30),
            (2.2, 40, 18),
            (1.6, 28, 22),
            (2.8, 32, 24),
            (3.2, 18, 26),
            (2.4, 45, 20),
        ]

        self.current, self.time_minutes, self.area_cm2 = rnd.choice(variations)
        self.density = DENSITY_NI

        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_e = self.charge / FARADAY
        self.moles_ni = self.moles_e / 2
        self.mass_ni = self.moles_ni * MOLAR_MASS_NI
        self.volume_cm3 = self.mass_ni / self.density
        self.thickness_cm = self.volume_cm3 / self.area_cm2
        self.thickness_mm = self.thickness_cm * 10

        self.answer = round(self.thickness_mm, 4)

        self.description = (
            "The diagram shows a nickel electroplating setup.\n"
            "Use the information shown to calculate\n"
            "the thickness of nickel deposited."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electroplating thickness"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE Grade 8–9"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{1. Time}} &= {self.time_minutes} \\times 60 = {self.time_seconds} \\\\"
            f"\n\\text{{2. Q}} &= {self.current} \\times {self.time_seconds} = {self.charge} \\\\"
            f"\n\\text{{3. n(e}}^-) &= {self.charge}/96500 = {round(self.moles_e, 10)} \\\\"
            f"\n\\text{{4. n(Ni)}} &= {round(self.moles_e, 10)}/2 = {round(self.moles_ni, 10)} \\\\"
            f"\n\\text{{5. Mass}} &= {round(self.moles_ni, 10)} \\times 58.7 = {round(self.mass_ni, 10)} \\\\"
            f"\n\\text{{6. Volume}} &= {round(self.mass_ni, 10)}/8.9 = {round(self.volume_cm3, 10)} \\\\"
            f"\n\\text{{7. Thickness (cm)}} &= {round(self.volume_cm3, 10)}/{self.area_cm2} = {round(self.thickness_cm, 10)} \\\\"
            f"\n\\text{{8. Thickness (mm)}} &= {round(self.thickness_cm, 10)} \\times 10 = {self.answer} \\text{{ mm}}"
            r"\n\end{aligned}\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(6, 6.6, "Nickel Electroplating Apparatus",
                fontsize=16, ha='center', fontweight='bold')

        beaker = patches.Rectangle((3, 1.5), 6, 4, fill=False, linewidth=3)
        ax.add_patch(beaker)

        solution = patches.Rectangle((3.1, 1.6), 5.8, 3.5,
                                     color="#9fc5e8")
        ax.add_patch(solution)

        ax.text(6, 4.9, "Ni²⁺(aq)", ha='center',
                fontsize=13, fontweight='bold')

        cathode = patches.Rectangle((4.2, 2), 0.3, 3,
                                    color="black")
        anode = patches.Rectangle((7.6, 2), 0.3, 3,
                                  color="black")
        ax.add_patch(cathode)
        ax.add_patch(anode)

        ax.text(4.35, 5.3, "-", fontsize=18, ha='center')
        ax.text(7.75, 5.3, "+", fontsize=18, ha='center')

        plated_layer = patches.Rectangle((4.05, 2),
                                         0.1, 3,
                                         color="#c0c0c0")
        ax.add_patch(plated_layer)

        plate_label = patches.Rectangle((4.05, 1.2), 0.7, 0.3,
                                        color="white", ec="black")
        ax.add_patch(plate_label)
        ax.text(4.4, 1.35,
                f"{self.area_cm2} cm²",
                fontsize=10,
                ha='center')

        ammeter = patches.Circle((6, 6), 0.5, fill=False, linewidth=2)
        ax.add_patch(ammeter)
        ax.text(6, 6, f"{self.current} A",
                ha='center', va='center', fontsize=10)

        ax.plot([4.35, 5.5], [5.3, 6], linewidth=2, color='black')
        ax.plot([7.75, 6.5], [5.3, 6], linewidth=2, color='black')

        ax.text(6, 5.4,
                f"Time = {self.time_minutes} min",
                ha='center',
                fontsize=12)

        ax.text(9.3, 1.2,
                f"Density = {self.density} g/cm³",
                fontsize=11)

        ax.text(6, 0.6,
                "Ni²⁺ + 2e⁻ → Ni",
                fontsize=12,
                ha='center')


        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem120:
    """
    Topic: Percentage Purity + Electrolysis (Extraction)
    Vision-based extraction setup
    """

    def __init__(self):

        variations = [
            (80, 65),
            (80, 75),
            (100, 70),
            (100, 80),
            (120, 75),
            (120, 85),
            (150, 70),
            (150, 90),
            (200, 80),
            (200, 85),
        ]

        self.ore_mass, self.purity_percent = rnd.choice(variations)

        self.pure_cu_mass = self.ore_mass * (self.purity_percent / 100)
        self.answer = round(self.pure_cu_mass, 2)

        self.description = (
            "The diagram shows copper extraction by electrolysis.\n"
            "Use the information shown to calculate\n"
            "the maximum mass of pure copper obtained."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Percentage purity + extraction"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE Higher Tier"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{1. Percentage purity formula}} & \\\\"
            f"\\text{{Pure mass}} &= \\text{{Ore mass}} \\times \\frac{{\\text{{Purity}}}}{{100}} \\\\"
            f"\n\\text{{2. Substitute values}} & \\\\"
            f"m_{{\\text{{Cu}}}} &= {self.ore_mass} \\times \\frac{{{self.purity_percent}}}{{100}} \\\\"
            f"&= {self.ore_mass} \\times {round(self.purity_percent/100, 10)} \\\\"
            f"&= {self.answer} \\text{{ g}}"
            r"\n\end{aligned}\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(6, 6.6, "Copper Extraction by Electrolysis",
                fontsize=16, ha='center', fontweight='bold')

        ore = patches.Circle((2.5, 3.5), 1.2, color="#8d6e63")
        ax.add_patch(ore)

        ax.text(2.5, 3.7,
                f"{self.ore_mass} g",
                ha='center', fontsize=12, fontweight='bold')

        ax.text(2.5, 3.2,
                f"{self.purity_percent}% Cu",
                ha='center', fontsize=11)

        furnace = patches.Rectangle((5, 2.2), 2.5, 2.5,
                                    fill=False, linewidth=3)
        ax.add_patch(furnace)

        ax.text(6.25, 4.5,
                "Electrolysis\nCell",
                ha='center', fontsize=11)

        ax.arrow(3.8, 3.5, 0.9, 0,
                 head_width=0.2,
                 head_length=0.3,
                 linewidth=2,
                 color='black')

        copper_bar = patches.Rectangle((9, 2.8), 1.5, 1.4,
                                       color="#b87333")
        ax.add_patch(copper_bar)

        ax.text(9.75, 2.3,
                "Pure Cu (s)",
                ha='center',
                fontsize=11)

        ax.arrow(7.6, 3.5, 1.2, 0,
                 head_width=0.2,
                 head_length=0.3,
                 linewidth=2,
                 color='black')

        ax.text(6, 1.2,
                "Maximum yield depends on copper purity",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem121:
    def __init__(self):

        variations = [
            (1.0, 0.6, 0.50),
            (0.8, 0.4, 0.50),
            (1.2, 0.9, 0.40),
            (1.5, 1.0, 0.30),
            (0.9, 0.5, 0.60),
            (1.1, 0.7, 0.45),
            (0.7, 0.3, 0.50),
            (1.3, 0.8, 0.35),
            (1.0, 0.2, 0.25),
            (0.6, 0.1, 0.40),
        ]

        self.initial_c, self.final_c, self.volume = rnd.choice(variations)

        self.delta_c = self.initial_c - self.final_c
        self.moles_cu = self.delta_c * self.volume
        self.moles_e = self.moles_cu * 2
        self.charge = self.moles_e * FARADAY

        self.answer = round(self.charge, 0)

        self.description = (
            "The graph shows how Cu²⁺ concentration changes during electrolysis.\n"
            "Use the graph and information shown to calculate\n"
            "the total charge passed."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Graph-based concentration change"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "GCSE Grade 8–9"

        self.reasoning = (
            r"\[\begin{aligned}"
            f"\n\\text{{1. Concentration change}} &= {self.initial_c} - {self.final_c} = {round(self.delta_c, 10)} \\\\"
            f"\n\\text{{2. n(Cu}}^{{2+}}\text{{)}} &= \\Delta c \\times V = {round(self.delta_c, 10)} \\times {self.volume} = {round(self.moles_cu, 10)} \\\\"
            f"\n\\text{{3. Half-equation}} &: \\text{{Cu}}^{{2+}} + 2e^- \\rightarrow \\text{{Cu}} \\\\"
            f"\n\\text{{4. n(e}}^-) &= 2 \\times {round(self.moles_cu, 10)} = {round(self.moles_e, 10)} \\\\"
            f"\n\\text{{5. Charge}} &= nF = {round(self.moles_e, 10)} \\times 96500 = {self.answer} \\text{{ C}}"
            r"\n\end{aligned}\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(12, 7))

        ax_graph = fig.add_axes([0.08, 0.35, 0.5, 0.55])
        ax_graph.plot([0, 10], [self.initial_c, self.final_c], linewidth=3)
        ax_graph.set_xlim(0, 10)
        ax_graph.set_ylim(0, max(self.initial_c, self.final_c) + 0.3)
        ax_graph.set_xlabel("Time")
        ax_graph.set_ylabel("Cu²⁺ concentration (mol dm⁻³)")
        ax_graph.set_title("Concentration vs Time")

        ax_graph.scatter([0, 10], [self.initial_c, self.final_c], s=60)

        ax_diagram = fig.add_axes([0.65, 0.2, 0.3, 0.6])
        ax_diagram.set_xlim(0, 6)
        ax_diagram.set_ylim(0, 7)
        ax_diagram.axis('off')

        beaker = patches.Rectangle((1, 1.5), 4, 3.5, fill=False, linewidth=2)
        ax_diagram.add_patch(beaker)

        solution = patches.Rectangle((1.1, 1.6), 3.8, 3.0, color="#6fa8dc")
        ax_diagram.add_patch(solution)

        ax_diagram.text(3, 4.8, "CuSO₄(aq)", ha='center', fontsize=10)

        cathode = patches.Rectangle((2, 2), 0.2, 2.5, color="black")
        anode = patches.Rectangle((4, 2), 0.2, 2.5, color="black")
        ax_diagram.add_patch(cathode)
        ax_diagram.add_patch(anode)

        ax_diagram.text(2.1, 4.8, "-", fontsize=14, ha='center')
        ax_diagram.text(4.1, 4.8, "+", fontsize=14, ha='center')

        copper = patches.Rectangle((1.9, 2), 0.1, 2.5, color="#b87333")
        ax_diagram.add_patch(copper)

        ax_diagram.text(3, 1.1,
                        f"Volume = {self.volume} dm³",
                        ha='center',
                        fontsize=10)

        ax_diagram.text(3, 0.6,
                        "Cu²⁺ + 2e⁻ → Cu",
                        ha='center',
                        fontsize=9)

        fig.suptitle("Electrolysis of Copper(II) Sulfate",
                     fontsize=15,
                     fontweight='bold')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem122:
    def __init__(self):

        variations = [
            (120, 40),
            (150, 60),
            (200, 80),
            (180, 20),
            (140, 50),
            (160, 30),
            (220, 100),
            (130, 70),
            (170, 90),
            (190, 110),
        ]

        self.reactants_energy, self.products_energy = rnd.choice(variations)

        self.delta_h = self.products_energy - self.reactants_energy
        self.answer = self.delta_h

        self.description = (
            "The reaction pathway diagram shows the energy levels of reactants and products.\n"
            "Calculate the enthalpy change, ΔH, in kJ."
        )

        self.topic = "Chemical Energetics"
        self.subtopic = "Enthalpy change from reaction pathway"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{ΔH}} &= \\text{{Energy of products}} - \\text{{Energy of reactants}}\\\\"
            f"&= {self.products_energy} - {self.reactants_energy}\\\\"
            f"&= {self.answer}\\,\\text{{kJ}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(12, 7))

        fig.text(0.5, 0.92,
                "Reaction Pathway Diagram",
                fontsize=18,
                ha='center',
                fontweight='bold')

        ax = fig.add_axes([0.08, 0.12, 0.84, 0.72])
        ax.set_xlim(0, 10)
        ax.set_ylim(0, max(self.reactants_energy, self.products_energy) + 80)

        ax.set_xlabel("Reaction Progress", fontsize=12)
        ax.set_ylabel("Energy (kJ)", fontsize=12)

        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)
        ax.spines['left'].set_linewidth(1.5)
        ax.spines['bottom'].set_linewidth(1.5)

        ax.plot([1, 4], [self.reactants_energy, self.reactants_energy], linewidth=4)
        ax.plot([6, 9], [self.products_energy, self.products_energy], linewidth=4)

        peak_energy = max(self.reactants_energy, self.products_energy) + 50

        ax.plot([4, 5, 6],
                [self.reactants_energy, peak_energy, self.products_energy],
                linewidth=4)

        ax.text(2.5, self.reactants_energy + 10,
                f"Reactants\n{self.reactants_energy} kJ",
                ha='center',
                fontsize=12)

        ax.text(7.5, self.products_energy + 10,
                f"Products\n{self.products_energy} kJ",
                ha='center',
                fontsize=12)

        ax.annotate("",
                    xy=(8.8, self.products_energy),
                    xytext=(8.8, self.reactants_energy),
                    arrowprops=dict(arrowstyle="<->", linewidth=2.5))

        ax.text(9.05,
                (self.reactants_energy + self.products_energy) / 2,
                "ΔH",
                fontsize=13)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem123:
    def __init__(self):

        variations = [
            (60, 150, 20),
            (80, 200, 50),
            (40, 120, 10),
            (100, 250, 60),
            (70, 180, 30),
            (90, 220, 40),
            (50, 160, 25),
            (110, 300, 70),
            (75, 190, 35),
            (65, 170, 15),
        ]

        self.reactants_energy, self.peak_energy, self.products_energy = rnd.choice(variations)

        self.activation_energy = self.peak_energy - self.reactants_energy
        self.answer = self.activation_energy

        self.description = (
            "The reaction pathway diagram shows energy levels of reactants and products.\n"
            "Calculate the activation energy, Ea, for the forward reaction."
        )

        self.topic = "Chemical Energetics"
        self.subtopic = "Activation energy from reaction pathway"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE Supplement"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{E}}_a &= \\text{{Peak}} - \\text{{Reactants}}\\\\"
            f"&= {self.peak_energy} - {self.reactants_energy}\\\\"
            f"&= {self.answer}\\,\\text{{kJ}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(12, 7))

        fig.text(0.5, 0.94,
                "Reaction Pathway Diagram",
                fontsize=18,
                ha='center',
                fontweight='bold')

        ax = fig.add_axes([0.08, 0.12, 0.84, 0.76])

        ax.set_xlim(0, 10)
        ax.set_ylim(0, self.peak_energy + 80)

        ax.set_xlabel("Reaction Progress", fontsize=12)
        ax.set_ylabel("Energy (kJ)", fontsize=12)

        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

        center = 5
        left = center - 3
        right = center + 3
        peak_x = center

        ax.plot([left - 1.5, left], 
                [self.reactants_energy, self.reactants_energy], 
                linewidth=4)

        ax.plot([left, peak_x, right],
                [self.reactants_energy, self.peak_energy, self.products_energy],
                linewidth=4)

        ax.plot([right, right + 1.5], 
                [self.products_energy, self.products_energy], 
                linewidth=4)

        ax.text(left - 0.75, self.reactants_energy + 12,
                f"Reactants\n{self.reactants_energy} kJ",
                ha='center',
                fontsize=12)

        ax.text(peak_x, self.peak_energy + 12,
                f"Peak\n{self.peak_energy} kJ",
                ha='center',
                fontsize=12)

        ax.text(right + 0.75, self.products_energy + 12,
                f"Products\n{self.products_energy} kJ",
                ha='center',
                fontsize=12)

        ax.annotate("",
                    xy=(peak_x - 0.4, self.peak_energy),
                    xytext=(peak_x - 0.4, self.reactants_energy),
                    arrowprops=dict(arrowstyle="<->", linewidth=2.5))

        ax.text(peak_x - 0.2,
                (self.reactants_energy + self.peak_energy) / 2,
                "Ea",
                fontsize=13)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem124:
    def __init__(self):

        variations = [
            (436, 242, 431),
            (410, 200, 390),
            (450, 250, 420),
            (430, 240, 410),
            (420, 230, 400),
            (440, 260, 415),
            (415, 220, 395),
            (455, 270, 430),
            (435, 245, 405),
            (425, 235, 398),
        ]

        self.hh, self.clcl, self.hcl = rnd.choice(variations)

        self.bonds_broken = self.hh + self.clcl
        self.bonds_formed = 2 * self.hcl
        self.delta_h = self.bonds_broken - self.bonds_formed

        self.answer = self.delta_h

        self.description = (
            "Using the bond energies shown in the table,\n"
            "calculate the enthalpy change of the reaction:\n"
            "H₂ + Cl₂ → 2HCl"
        )

        self.topic = "Chemical Energetics"
        self.subtopic = "Bond energy calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE Supplement"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{ΔH}} &= \\text{{Bonds broken}} - \\text{{Bonds formed}}\\\\"
            f"&= ({self.hh} + {self.clcl}) - (2 \\times {self.hcl})\\\\"
            f"&= {self.bonds_broken} - {self.bonds_formed}\\\\"
            f"&= {self.answer}\\,\\text{{kJ}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.axis('off')

        ax.text(0.5, 0.9, "Bond Energy Table",
                fontsize=16, ha='center', transform=ax.transAxes)

        table_data = [
            ["Bond", "Energy (kJ/mol)"],
            ["H–H", str(self.hh)],
            ["Cl–Cl", str(self.clcl)],
            ["H–Cl", str(self.hcl)],
        ]

        table = ax.table(cellText=table_data,
                         loc='center',
                         cellLoc='center')

        table.scale(1.5, 2)

        ax.text(0.5, 0.25,
                "Reaction:  H₂ + Cl₂ → 2HCl",
                fontsize=14,
                ha='center',
                transform=ax.transAxes)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem125:
    def __init__(self):

        variations = [
            ("Magnesium + Hydrochloric acid", 10, 30, 12, 36),
            ("Calcium carbonate + Hydrochloric acid", 15, 45, 20, 50),
            ("Zinc + Sulfuric acid", 5, 25, 8, 28),
            ("Marble chips + Nitric acid", 20, 60, 25, 70),
            ("Iron + Hydrochloric acid", 10, 40, 15, 45),
            ("Magnesium ribbon + Sulfuric acid", 8, 28, 10, 34),
            ("Calcium + Water", 12, 32, 18, 42),
            ("Sodium carbonate + Hydrochloric acid", 10, 50, 14, 54),
            ("Zinc granules + Nitric acid", 6, 26, 9, 29),
            ("Marble chips + Hydrochloric acid", 10, 30, 16, 46),
        ]

        (self.reaction,
         self.t1,
         self.t2,
         self.v1,
         self.v2) = rnd.choice(variations)

        self.delta_v = self.v2 - self.v1
        self.delta_t = self.t2 - self.t1
        self.rate = self.delta_v / self.delta_t
        self.answer = round(self.rate, 2)

        self.description = (
            f"The graph shows the reaction between {self.reaction}.\n"
            "Using the graph, calculate the rate of reaction."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Rate from gradient"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Rate}} &= \\frac{{\\Delta V}}{{\\Delta t}}\\\\"
            f"&= \\frac{{{self.v2} - {self.v1}}}{{{self.t2} - {self.t1}}}\\\\"
            f"&= \\frac{{{self.delta_v}}}{{{self.delta_t}}}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^3\\,\\text{{s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_axes([0.12, 0.15, 0.75, 0.7])

        times = [self.t1, self.t2]
        volumes = [self.v1, self.v2]

        ax.bar(times, volumes, width=5)

        max_time = max(times) * 1.4
        max_volume = max(volumes) * 1.4

        ax.set_xlim(0, max_time)
        ax.set_ylim(0, max_volume)

        ax.set_xlabel("Time (s)", fontsize=13)
        ax.set_ylabel("Volume of gas (cm³)", fontsize=13)

        ax.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.6)

        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

        for t, v in zip(times, volumes):
            ax.text(t, v + max_volume * 0.03,
                    f"{v} cm³",
                    ha='center',
                    fontsize=11)

        fig.text(0.5, 0.93,
                f"Rate of Reaction Data\n{self.reaction}",
                ha='center',
                fontsize=16,
                fontweight='bold')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem126:
    def __init__(self):

        variations = [
            ("Calcium carbonate + Hydrochloric acid", 150.0, 147.4, 80),
            ("Magnesium + Hydrochloric acid", 120.0, 118.0, 60),
            ("Zinc + Sulfuric acid", 200.0, 197.5, 100),
            ("Marble chips + Nitric acid", 180.0, 177.0, 90),
            ("Iron + Hydrochloric acid", 160.0, 158.5, 70),
            ("Sodium carbonate + Hydrochloric acid", 140.0, 138.0, 50),
            ("Calcium + Water", 130.0, 128.2, 75),
            ("Magnesium ribbon + Sulfuric acid", 170.0, 167.5, 85),
            ("Zinc granules + Hydrochloric acid", 155.0, 152.0, 95),
            ("Marble chips + Hydrochloric acid", 190.0, 187.5, 110),
        ]

        self.reaction, self.initial_mass, self.final_mass, self.finish_time = rnd.choice(variations)

        self.answer = self.finish_time

        self.description = (
            f"The graph shows the reaction between {self.reaction}.\n"
            "From the graph, determine the time taken\n"
            "for the reaction to finish."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Time to completion from mass-loss graph"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial mass}} &= {self.initial_mass}\\,\\text{{g}}\\\\"
            f"\\text{{Final mass}} &= {self.final_mass}\\,\\text{{g}}\\\\"
            f"\\text{{Reaction finishes when mass becomes constant}}\\\\"
            f"\\text{{Time at plateau}} &= {self.answer}\\,\\text{{s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(12, 7))

        fig.text(0.5, 0.95,
                f"Mass Change During Reaction\n{self.reaction}",
                ha='center',
                fontsize=16,
                fontweight='bold')

        ax = fig.add_axes([0.15, 0.35, 0.7, 0.45])

        ax.set_xlim(0, self.finish_time * 1.2)
        ax.set_ylim(self.final_mass - 2, self.initial_mass + 3)

        ax.set_xlabel("Time (s)", fontsize=12)
        ax.set_ylabel("Mass of flask (g)", fontsize=12)

        ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.6)

        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

        import numpy as np
        t = np.linspace(0, self.finish_time, 200)
        k = 3 / self.finish_time
        mass_curve = self.final_mass + (self.initial_mass - self.final_mass) * np.exp(-k * t)

        ax.plot(t, mass_curve, linewidth=3)

        ax.plot([self.finish_time, self.finish_time * 1.15],
                [self.final_mass, self.final_mass],
                linewidth=3)

        ax.scatter([0, self.finish_time],
                [self.initial_mass, self.final_mass],
                s=60)

        ax.text(0, self.initial_mass + 0.5,
                f"{self.initial_mass} g",
                fontsize=10)

        ax.text(self.finish_time, self.final_mass + 0.5,
                f"{self.final_mass} g",
                fontsize=10,
                ha='center')

        ax_table = fig.add_axes([0.25, 0.12, 0.5, 0.12])
        ax_table.axis('off')

        table_data = [
            ["Time (s)", "0", f"{self.finish_time}"],
            ["Mass (g)", f"{self.initial_mass}", f"{self.final_mass}"]
        ]

        table = ax_table.table(cellText=table_data,
                            loc='center',
                            cellLoc='center')

        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 1.5)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem127:
    def __init__(self):

        variations = [
            ("Haber Process (N₂ + 3H₂ ⇌ 2NH₃)", "NH₃", 60, 20, 60),
            ("Contact Process (2SO₂ + O₂ ⇌ 2SO₃)", "SO₃", 50, 25, 75),
            ("Hydrogen iodide formation (H₂ + I₂ ⇌ 2HI)", "HI", 80, 20, 20),
            ("Ester formation", "Ester", 40, 30, 30),
            ("Ammonium chloride formation", "NH₄Cl", 70, 15, 45),
            ("Haber Process", "NH₃", 50, 25, 75),
            ("Contact Process", "SO₃", 60, 20, 60),
            ("Hydrogen iodide formation", "HI", 90, 10, 10),
            ("Ester formation", "Ester", 30, 35, 35),
            ("Ammonium chloride formation", "NH₄Cl", 80, 10, 40),
        ]

        self.process, self.product_name, self.product_mol, self.reactant1_mol, self.reactant2_mol = rnd.choice(variations)

        self.total_moles = self.product_mol + self.reactant1_mol + self.reactant2_mol
        self.percentage_yield = (self.product_mol / self.total_moles) * 100
        self.answer = round(self.percentage_yield, 1)

        self.description = (
            f"The bar chart shows the equilibrium composition for {self.process}.\n"
            f"Calculate the percentage yield of {self.product_name} at equilibrium."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Percentage yield from composition"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total moles}} &= {self.product_mol} + {self.reactant1_mol} + {self.reactant2_mol} = {self.total_moles}\\\\"
            f"\\text{{Percentage yield}} &= \\frac{{{self.product_mol}}}{{{self.total_moles}}} \\times 100\\\\"
            f"&= {self.answer}\\,\\% "
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])

        labels = [self.product_name, "Reactant 1", "Reactant 2"]
        values = [self.product_mol, self.reactant1_mol, self.reactant2_mol]

        ax.bar(labels, values)

        ax.set_ylabel("Amount (mol)")
        ax.set_title(f"Equilibrium Composition\n{self.process}")

        for i, v in enumerate(values):
            ax.text(i, v + 2, str(v), ha='center')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem128:
    def __init__(self):

        variations = [
            ("Haber Process", "N₂ + 3H₂ ⇌ 2NH₃", 4, 2),
            ("Hydrogen iodide formation", "H₂ + I₂ ⇌ 2HI", 2, 2),
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄", 2, 1),
            ("Sulfur trioxide formation", "2SO₂ + O₂ ⇌ 2SO₃", 3, 2),
            ("Ammonium chloride formation", "NH₃ + HCl ⇌ NH₄Cl", 2, 1),
            ("Haber Process", "N₂ + 3H₂ ⇌ 2NH₃", 6, 4),
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄", 4, 2),
            ("Sulfur trioxide formation", "2SO₂ + O₂ ⇌ 2SO₃", 6, 4),
            ("Hydrogen iodide formation", "H₂ + I₂ ⇌ 2HI", 4, 4),
            ("Ammonium chloride formation", "NH₃ + HCl ⇌ NH₄Cl", 4, 2),
        ]

        self.process, self.equation, self.initial_moles, self.equilibrium_moles = rnd.choice(variations)

        self.decrease = self.initial_moles - self.equilibrium_moles
        self.answer = self.decrease

        self.description = (
            f"The diagram shows the equilibrium reaction for {self.process}.\n"
            "Using the graph information, calculate the decrease\n"
            "in total number of moles."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Mole ratio and pressure change"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial moles}} &= {self.initial_moles}\\\\"
            f"\\text{{Equilibrium moles}} &= {self.equilibrium_moles}\\\\"
            f"\\text{{Decrease}} &= {self.initial_moles} - {self.equilibrium_moles}\\\\"
            f"&= {self.answer}\\,\\text{{mol}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        x_start = 3
        spacing = 4

        stages = [
            ("Initial", self.initial_moles, "lightblue"),
            ("Equilibrium", self.equilibrium_moles, "orange")
        ]

        max_moles = max(self.initial_moles, self.equilibrium_moles)

        for i, (label, moles, color) in enumerate(stages):
            x = x_start + i * spacing

            solution_height = 2.5 * (moles / max_moles)

            draw_test_tube(
                ax,
                x,
                1,
                width=1.2,
                height=3.5,
                solution_height=solution_height,
                solution_color=color
            )

            ax.text(x + 0.6, 0.4,
                    f"{label}",
                    ha='center',
                    fontsize=12,
                    fontweight='bold')

            ax.text(x + 0.6, 4.7,
                    f"{moles} mol",
                    ha='center',
                    fontsize=11)

        add_title_box(ax, 6, 5.5,
                    f"Equilibrium Reaction\n{self.equation}",
                    fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem129:
    def __init__(self):

        variations = [
            ("CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O", "CO₂", 72, 90, 0.50),
            ("Mg + 2HCl → MgCl₂ + H₂", "H₂", 48, 60, 0.50),
            ("Zn + 2HCl → ZnCl₂ + H₂", "H₂", 24, 40, 0.40),
            ("CaCO₃ + 2HNO₃ → Ca(NO₃)₂ + CO₂ + H₂O", "CO₂", 96, 100, 0.80),
            ("Fe + 2HCl → FeCl₂ + H₂", "H₂", 36, 70, 0.30),
            ("CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O", "CO₂", 48, 75, 0.50),
            ("Mg + 2HCl → MgCl₂ + H₂", "H₂", 72, 80, 0.60),
            ("Zn + 2HCl → ZnCl₂ + H₂", "H₂", 60, 85, 0.50),
            ("CaCO₃ + 2HNO₃ → Ca(NO₃)₂ + CO₂ + H₂O", "CO₂", 24, 50, 0.20),
            ("Fe + 2HCl → FeCl₂ + H₂", "H₂", 48, 65, 0.40),
        ]

        (self.reaction,
         self.gas_name,
         self.final_volume_cm3,
         self.finish_time,
         self.acid_volume_dm3) = rnd.choice(variations)

        self.molar_gas_volume = 24
        self.volume_dm3 = self.final_volume_cm3 / 1000
        self.moles_gas = self.volume_dm3 / self.molar_gas_volume
        self.moles_hcl = self.moles_gas * 2
        self.concentration = self.moles_hcl / self.acid_volume_dm3

        self.answer = round(self.concentration, 2)

        self.description = (
            f"The graph shows the volume of {self.gas_name} produced in the reaction:\n"
            f"{self.reaction}\n"
            "Calculate the concentration of acid used."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Rate + Moles + Concentration"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Volume (dm³)}} &= {self.final_volume_cm3}/1000 = {round(self.volume_dm3,4)}\\\\"
            f"\\text{{Moles of gas}} &= {round(self.volume_dm3,4)}/24 = {round(self.moles_gas,4)}\\\\"
            f"\\text{{Moles of HCl}} &= 2 \\times {round(self.moles_gas,4)} = {round(self.moles_hcl,4)}\\\\"
            f"\\text{{Concentration}} &= {round(self.moles_hcl,4)}/{self.acid_volume_dm3} = {self.answer}\\,\\text{{mol dm}}^{{-3}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_axes([0.1, 0.15, 0.8, 0.75])

        ax.set_xlim(0, self.finish_time + 20)
        ax.set_ylim(0, self.final_volume_cm3 + 20)

        ax.set_xlabel("Time (s)")
        ax.set_ylabel(f"Volume of {self.gas_name} (cm³)")

        ax.plot([0, self.finish_time],
                [0, self.final_volume_cm3],
                linewidth=3)

        ax.scatter([self.finish_time],
                   [self.final_volume_cm3],
                   s=80)

        ax.text(self.finish_time,
                self.final_volume_cm3 + 5,
                f"{self.final_volume_cm3} cm³",
                ha='center')

        fig.text(0.5, 0.92,
                 f"Gas Volume vs Time\n{self.reaction}",
                 ha='center',
                 fontsize=14,
                 fontweight='bold')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem130:
    def __init__(self):

        variations = [
            ("Haber Process", "N₂ + 3H₂ ⇌ 2NH₃", "N₂", 40, 120, 15, 45, 30),
            ("Haber Process", "N₂ + 3H₂ ⇌ 2NH₃", "N₂", 50, 150, 20, 60, 40),
            ("Sulfur trioxide formation", "2SO₂ + O₂ ⇌ 2SO₃", "SO₂", 60, 40, 30, 20, 60),
            ("Sulfur trioxide formation", "2SO₂ + O₂ ⇌ 2SO₃", "SO₂", 80, 50, 40, 25, 80),
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄", "NO₂", 100, None, 40, None, 60),
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄", "NO₂", 80, None, 30, None, 50),
            ("Hydrogen iodide formation", "H₂ + I₂ ⇌ 2HI", "H₂", 60, 60, 20, 20, 80),
            ("Hydrogen iodide formation", "H₂ + I₂ ⇌ 2HI", "H₂", 50, 50, 10, 10, 80),
            ("Ammonium chloride formation", "NH₃ + HCl ⇌ NH₄Cl", "NH₃", 70, 70, 20, 20, 50),
            ("Ammonium chloride formation", "NH₃ + HCl ⇌ NH₄Cl", "NH₃", 60, 60, 15, 15, 45),
        ]

        (self.process,
         self.equation,
         self.limiting_species,
         self.initial_r1,
         self.initial_r2,
         self.eq_r1,
         self.eq_r2,
         self.eq_product) = rnd.choice(variations)

        self.initial_limiting = self.initial_r1
        self.eq_limiting = self.eq_r1
        self.used = self.initial_limiting - self.eq_limiting
        self.percentage_conversion = (self.used / self.initial_limiting) * 100
        self.answer = round(self.percentage_conversion, 1)

        self.description = (
            f"The diagram shows the equilibrium composition for {self.process}.\n"
            f"Calculate the percentage conversion of {self.limiting_species}."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Percentage conversion"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Amount reacted}} &= {self.initial_limiting} - {self.eq_limiting} = {self.used}\\\\"
            f"\\text{{Percentage conversion}} &= \\frac{{{self.used}}}{{{self.initial_limiting}}} \\times 100\\\\"
            f"&= {self.answer}\\,\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])

        labels = ["Reactant 1", "Reactant 2", "Product"]
        values = [self.eq_r1, self.eq_r2 if self.eq_r2 else 0, self.eq_product]

        ax.bar(labels, values)

        ax.set_ylabel("Amount at equilibrium (mol)")
        ax.set_title(f"Equilibrium Composition\n{self.equation}")

        for i, v in enumerate(values):
            ax.text(i, v + 2, str(v), ha='center')

        fig.text(0.1, 0.05,
                 f"Initial amounts:\nReactant 1 = {self.initial_r1} mol\nReactant 2 = {self.initial_r2 if self.initial_r2 else '-'} mol",
                 fontsize=10)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem131:
    def __init__(self):

        variations = [
            ("Decomposition of hydrogen peroxide", 1.6, 50, 100),
            ("Decomposition of N₂O₅", 2.0, 40, 80),
            ("Acid hydrolysis reaction", 1.2, 30, 60),
            ("Thermal decomposition of CaCO₃", 1.8, 45, 90),
            ("Catalytic decomposition reaction", 2.4, 60, 120),
            ("Photochemical reaction", 1.0, 25, 50),
            ("Ester hydrolysis", 2.2, 55, 110),
            ("Oxidation reaction", 1.4, 35, 70),
            ("Reduction reaction", 1.6, 40, 80),
            ("First-order decay reaction", 2.0, 50, 100),
        ]

        self.reaction, self.initial_c, self.half_time, self.full_time = rnd.choice(variations)

        self.c_half = self.initial_c / 2
        self.c_final = self.initial_c / 4
        self.volume = 0.25

        self.delta_c = self.initial_c - self.c_final
        self.delta_t = self.full_time
        self.rate = self.delta_c / self.delta_t

        self.answer = round(self.rate, 3)

        self.description = (
            f"The graph shows the concentration change for {self.reaction}.\n"
            "Calculate the average rate of reaction between 0 s and final time."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Average rate from concentration-time graph"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Change in concentration}} &= {self.initial_c} - {self.c_final} = {round(self.delta_c,3)}\\\\"
            f"\\text{{Change in time}} &= {self.full_time} - 0 = {self.delta_t}\\\\"
            f"\\text{{Average rate}} &= \\frac{{{round(self.delta_c,3)}}}{{{self.delta_t}}}\\\\"
            f"&= {self.answer}\\,\\text{{mol dm}}^{{-3}}\\,\\text{{s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_axes([0.1, 0.15, 0.8, 0.75])

        ax.set_xlim(0, self.full_time + 20)
        ax.set_ylim(0, self.initial_c + 0.5)

        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Concentration (mol dm⁻³)")

        ax.plot([0, self.half_time, self.full_time],
                [self.initial_c, self.c_half, self.c_final],
                linewidth=3)

        ax.scatter([self.half_time, self.full_time],
                   [self.c_half, self.c_final],
                   s=80)

        ax.text(self.half_time, self.c_half + 0.05,
                f"{self.c_half}",
                ha='center')

        ax.text(self.full_time, self.c_final + 0.05,
                f"{self.c_final}",
                ha='center')

        fig.text(0.5, 0.92,
                 f"Concentration vs Time\n{self.reaction}",
                 ha='center',
                 fontsize=14,
                 fontweight='bold')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem132:
    def __init__(self):

        variations = [
            ("2Fe²⁺ + Cl₂ → 2Fe³⁺ + 2Cl⁻", "Fe²⁺", "Fe³⁺", 1, 0.50),
            ("2Fe²⁺ + Br₂ → 2Fe³⁺ + 2Br⁻", "Fe²⁺", "Fe³⁺", 1, 0.40),
            ("2Cu⁺ + Cl₂ → 2Cu²⁺ + 2Cl⁻", "Cu⁺", "Cu²⁺", 1, 0.30),
            ("Zn → Zn²⁺ + 2e⁻", "Zn", "Zn²⁺", 2, 0.25),
            ("2Ag⁺ + Cu → 2Ag + Cu²⁺", "Cu", "Cu²⁺", 2, 0.20),
            ("2Fe²⁺ + I₂ → 2Fe³⁺ + 2I⁻", "Fe²⁺", "Fe³⁺", 1, 0.60),
            ("2Cu⁺ + Br₂ → 2Cu²⁺ + 2Br⁻", "Cu⁺", "Cu²⁺", 1, 0.45),
            ("Mg → Mg²⁺ + 2e⁻", "Mg", "Mg²⁺", 2, 0.50),
            ("2Ag⁺ + Zn → 2Ag + Zn²⁺", "Zn", "Zn²⁺", 2, 0.35),
            ("2Fe²⁺ + Cl₂ → 2Fe³⁺ + 2Cl⁻", "Fe²⁺", "Fe³⁺", 1, 0.75),
        ]

        (self.equation,
         self.reactant,
         self.product,
         self.electron_change,
         self.moles_used) = rnd.choice(variations)

        self.electrons_transferred = self.moles_used * self.electron_change
        self.answer = round(self.electrons_transferred, 2)

        self.description = (
            f"The diagram shows the redox reaction:\n{self.equation}\n"
            "Calculate the number of moles of electrons transferred."
        )

        self.topic = "Redox"
        self.subtopic = "Oxidation numbers and electron transfer"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Oxidation change}} &= {self.electron_change}\\\\"
            f"\\text{{Moles used}} &= {self.moles_used}\\\\"
            f"\\text{{Electrons transferred}} &= {self.moles_used} \\times {self.electron_change}\\\\"
            f"&= {self.answer}\\,\\text{{mol}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        react_box = Rectangle((1.5, 2.5), 4, 1.5, linewidth=2, edgecolor='black', facecolor='lightblue')
        ax.add_patch(react_box)
        ax.text(3.5, 3.25, self.reactant, ha='center', va='center', fontsize=14, fontweight='bold')

        prod_box = Rectangle((6.5, 2.5), 4, 1.5, linewidth=2, edgecolor='black', facecolor='lightgreen')
        ax.add_patch(prod_box)
        ax.text(8.5, 3.25, self.product, ha='center', va='center', fontsize=14, fontweight='bold')

        arrow = FancyArrow(5.5, 3.25, 1, 0, width=0.2, length_includes_head=True)
        ax.add_patch(arrow)

        ax.text(6, 4.8, self.equation, ha='center', fontsize=14, fontweight='bold')

        ax.text(6, 1.2,
                f"{self.moles_used} mol {self.reactant} used",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem133:
    def __init__(self):

        variations = [
            ("2MnO₄⁻ + 5Fe²⁺ + 8H⁺ → 2Mn²⁺ + 5Fe³⁺ + 4H₂O", 25.0, 0.0200, 18.5, 5, 2),
            ("2MnO₄⁻ + 5Fe²⁺ + 8H⁺ → 2Mn²⁺ + 5Fe³⁺ + 4H₂O", 20.0, 0.0150, 16.0, 5, 2),
            ("2Cr₂O₇²⁻ + 6Fe²⁺ + 14H⁺ → 2Cr³⁺ + 6Fe³⁺ + 7H₂O", 25.0, 0.0100, 20.0, 6, 2),
            ("I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻", 25.0, 0.0500, 10.0, 2, 1),
            ("Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂", 30.0, 0.0200, 25.0, 2, 1),
            ("2MnO₄⁻ + 5Fe²⁺ + 8H⁺ → 2Mn²⁺ + 5Fe³⁺ + 4H₂O", 25.0, 0.0250, 20.0, 5, 2),
            ("2Cr₂O₇²⁻ + 6Fe²⁺ + 14H⁺ → 2Cr³⁺ + 6Fe³⁺ + 7H₂O", 20.0, 0.0200, 15.0, 6, 2),
            ("I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻", 30.0, 0.0400, 12.5, 2, 1),
            ("Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂", 25.0, 0.0150, 20.0, 2, 1),
            ("2MnO₄⁻ + 5Fe²⁺ + 8H⁺ → 2Mn²⁺ + 5Fe³⁺ + 4H₂O", 20.0, 0.0100, 25.0, 5, 2),
        ]

        (self.equation,
         self.fe_volume_cm3,
         self.titrant_conc,
         self.titrant_volume_cm3,
         self.fe_ratio,
         self.titrant_ratio) = rnd.choice(variations)

        self.titrant_volume_dm3 = self.titrant_volume_cm3 / 1000
        self.fe_volume_dm3 = self.fe_volume_cm3 / 1000

        self.moles_titrant = self.titrant_conc * self.titrant_volume_dm3
        self.moles_fe = self.moles_titrant * (self.fe_ratio / self.titrant_ratio)

        self.fe_concentration = self.moles_fe / self.fe_volume_dm3
        self.answer = round(self.fe_concentration, 3)

        self.description = (
            f"The diagram shows the redox titration:\n{self.equation}\n"
            "Calculate the concentration of Fe²⁺ solution."
        )

        self.topic = "Redox"
        self.subtopic = "Redox titration"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Volume (dm³)}} &= {self.titrant_volume_cm3}/1000 = {round(self.titrant_volume_dm3,4)}\\\\"
            f"\\text{{Moles titrant}} &= {self.titrant_conc} \\times {round(self.titrant_volume_dm3,4)} = {round(self.moles_titrant,4)}\\\\"
            f"\\text{{Moles Fe}} &= {round(self.moles_titrant,4)} \\times \\frac{{{self.fe_ratio}}}{{{self.titrant_ratio}}} = {round(self.moles_fe,4)}\\\\"
            f"\\text{{Concentration}} &= {round(self.moles_fe,4)}/{round(self.fe_volume_dm3,4)} = {self.answer}\\,\\text{{mol dm}}^{{-3}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        x_start = 3
        spacing = 4

        chemicals = [
            ("Fe²⁺", f"{self.fe_volume_cm3} cm³", "lightgreen"),
            ("Titrant", f"{self.titrant_conc} mol dm⁻³\n{self.titrant_volume_cm3} cm³", "purple")
        ]

        for i, (label, info, color) in enumerate(chemicals):
            x = x_start + i * spacing

            rect = plt.Rectangle((x, 1), 1.5, 3.5, linewidth=2,
                                 edgecolor='black', facecolor=color)
            ax.add_patch(rect)

            ax.text(x + 0.75, 4.8, label,
                    ha='center', fontsize=12, fontweight='bold')

            ax.text(x + 0.75, 0.5, info,
                    ha='center', fontsize=11)

        ax.text(6, 5.6, self.equation,
                ha='center', fontsize=14, fontweight='bold')

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem134:
    def __init__(self):

        variations = [
            ("CuO + H₂ → Cu + H₂O", "CuO", "Cu", 16.0, 63.5, 16),
            ("PbO + H₂ → Pb + H₂O", "PbO", "Pb", 22.3, 207.2, 16),
            ("Fe₂O₃ + 3H₂ → 2Fe + 3H₂O", "Fe₂O₃", "Fe", 32.0, 55.8, 48),
            ("ZnO + H₂ → Zn + H₂O", "ZnO", "Zn", 20.4, 65.4, 16),
            ("CuO + CO → Cu + CO₂", "CuO", "Cu", 8.0, 63.5, 16),
            ("PbO + CO → Pb + CO₂", "PbO", "Pb", 44.6, 207.2, 16),
            ("Fe₂O₃ + 3CO → 2Fe + 3CO₂", "Fe₂O₃", "Fe", 16.0, 55.8, 48),
            ("ZnO + CO → Zn + CO₂", "ZnO", "Zn", 10.2, 65.4, 16),
            ("CuO + H₂ → Cu + H₂O", "CuO", "Cu", 32.0, 63.5, 16),
            ("PbO + H₂ → Pb + H₂O", "PbO", "Pb", 11.15, 207.2, 16),
        ]

        (self.equation,
         self.reactant,
         self.product,
         self.mass_reactant,
         self.ar_product,
         self.oxygen_mass) = rnd.choice(variations)

        if self.reactant == "Fe₂O₃":
            self.mr_reactant = 2 * 55.8 + 3 * 16
            self.mole_ratio = 2
        else:
            self.mr_reactant = self.ar_product + self.oxygen_mass
            self.mole_ratio = 1

        self.moles_reactant = self.mass_reactant / self.mr_reactant
        self.moles_product = self.moles_reactant * self.mole_ratio
        self.mass_product = self.moles_product * self.ar_product

        self.answer = round(self.mass_product, 2)

        self.description = (
            f"The diagram shows the reaction:\n{self.equation}\n"
            "Calculate the mass of metal produced."
        )

        self.topic = "Redox"
        self.subtopic = "Oxidising agent and mass calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mr of reactant}} &= {round(self.mr_reactant,2)}\\\\"
            f"\\text{{Moles reactant}} &= {self.mass_reactant}/{round(self.mr_reactant,2)} = {round(self.moles_reactant,4)}\\\\"
            f"\\text{{Moles product}} &= {round(self.moles_reactant,4)} \\times {self.mole_ratio} = {round(self.moles_product,4)}\\\\"
            f"\\text{{Mass product}} &= {round(self.moles_product,4)} \\times {self.ar_product} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        react_box = Rectangle((1.5, 2.5), 4, 1.5, linewidth=2,
                              edgecolor='black', facecolor='lightcoral')
        ax.add_patch(react_box)
        ax.text(3.5, 3.25, f"{self.reactant}\n{self.mass_reactant} g",
                ha='center', va='center', fontsize=12, fontweight='bold')

        prod_box = Rectangle((6.5, 2.5), 4, 1.5, linewidth=2,
                             edgecolor='black', facecolor='lightgreen')
        ax.add_patch(prod_box)
        ax.text(8.5, 3.25, f"{self.product}",
                ha='center', va='center', fontsize=14, fontweight='bold')

        arrow = FancyArrow(5.5, 3.25, 1, 0, width=0.2, length_includes_head=True)
        ax.add_patch(arrow)

        ax.text(6, 5.4, self.equation,
                ha='center', fontsize=14, fontweight='bold')

        ax.text(6, 1.2,
                f"Ar: {self.product} = {self.ar_product}",
                ha='center', fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem135:
    def __init__(self):

        variations = [
            (25.0, 20.0, 0.100),
            (20.0, 25.0, 0.100),
            (25.0, 30.0, 0.080),
            (30.0, 25.0, 0.120),
            (20.0, 20.0, 0.150),
            (25.0, 15.0, 0.200),
            (15.0, 20.0, 0.125),
            (40.0, 20.0, 0.050),
            (25.0, 10.0, 0.250),
            (50.0, 25.0, 0.040),
        ]

        self.acid_volume_cm3, self.base_volume_cm3, self.base_conc = rnd.choice(variations)

        self.acid_volume_dm3 = self.acid_volume_cm3 / 1000
        self.base_volume_dm3 = self.base_volume_cm3 / 1000

        self.moles_base = self.base_conc * self.base_volume_dm3
        self.moles_acid = self.moles_base
        self.acid_conc = self.moles_acid / self.acid_volume_dm3

        self.answer = round(self.acid_conc, 3)

        self.description = (
            "The diagram shows an acid–alkali titration.\n"
            "Calculate the concentration of hydrochloric acid."
        )

        self.topic = "Acids and bases"
        self.subtopic = "Acid–alkali titration"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Convert volumes}} &: {self.base_volume_cm3}/1000 = {round(self.base_volume_dm3,5)}\\,\\text{{dm}}^3\\\\"
            f"\\text{{2. Moles NaOH}} &= cV = {self.base_conc} \\times {round(self.base_volume_dm3,5)} = {round(self.moles_base,10)}\\\\"
            f"\\text{{3. 1:1 ratio}} &: n(\\text{{HCl}}) = n(\\text{{NaOH}}) = {round(self.moles_acid,10)}\\\\"
            f"\\text{{4. Concentration HCl}} &= \\frac{{n}}{{V}} = \\frac{{{round(self.moles_acid,10)}}}{{{round(self.acid_volume_dm3,5)}}} = {self.answer}\\,\\text{{mol dm}}^{{-3}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.6,
                "Acid–Alkali Titration Setup",
                ha='center',
                fontsize=16,
                fontweight='bold')

        ax.text(6, 5.1,
                "HCl + NaOH → NaCl + H₂O",
                ha='center',
                fontsize=14,
                fontweight='bold')

        burette = Rectangle((5.6, 2.2), 0.8, 2.6, fill=False, linewidth=2)
        ax.add_patch(burette)

        burette_liquid = Rectangle((5.62, 2.2), 0.76, 2.0, linewidth=0, facecolor="lightgreen", alpha=0.9)
        ax.add_patch(burette_liquid)

        tap = Rectangle((5.85, 2.0), 0.3, 0.2, linewidth=1.5, edgecolor="black", facecolor="lightgray")
        ax.add_patch(tap)

        tip = Polygon([[6.0, 2.0], [6.2, 1.6], [5.8, 1.6]], closed=True, facecolor="lightgray", edgecolor="black")
        ax.add_patch(tip)

        drop = Circle((6.0, 1.35), 0.08, facecolor="lightgreen", edgecolor="black", linewidth=0.8)
        ax.add_patch(drop)

        ax.text(8.7, 3.9,
                f"NaOH(aq)\n{self.base_conc} mol dm⁻³\nVolume used = {self.base_volume_cm3} cm³",
                fontsize=11,
                va='center',
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', linewidth=1.5))

        beaker = Rectangle((4.3, 0.8), 3.4, 1.7, fill=False, linewidth=2)
        ax.add_patch(beaker)

        beaker_liquid = Rectangle((4.32, 0.82), 3.36, 1.1, linewidth=0, facecolor="lightblue", alpha=0.9)
        ax.add_patch(beaker_liquid)

        ax.text(2.0, 1.65,
                f"HCl(aq)\nVolume = {self.acid_volume_cm3} cm³",
                fontsize=11,
                va='center',
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', linewidth=1.5))

        arrow1 = FancyArrowPatch((4.05, 1.6), (4.3, 1.6), arrowstyle="->", linewidth=2)
        ax.add_patch(arrow1)

        arrow2 = FancyArrowPatch((7.95, 3.3), (6.8, 3.3), arrowstyle="->", linewidth=2)
        ax.add_patch(arrow2)

        ax.text(6, 0.35,
                "Use the information shown to calculate the concentration of HCl (mol dm⁻³).",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem136:
    def __init__(self):

        variations = [
            (50.0, 0.200),
            (25.0, 0.200),
            (40.0, 0.150),
            (30.0, 0.300),
            (60.0, 0.100),
            (20.0, 0.250),
            (45.0, 0.200),
            (35.0, 0.160),
            (80.0, 0.050),
            (100.0, 0.080),
        ]

        self.acid_volume_cm3, self.acid_conc = rnd.choice(variations)

        self.acid_volume_dm3 = self.acid_volume_cm3 / 1000
        self.moles_hcl = self.acid_conc * self.acid_volume_dm3
        self.moles_co2 = self.moles_hcl / 2
        self.volume_co2_dm3 = self.moles_co2 * 24
        self.volume_co2_cm3 = self.volume_co2_dm3 * 1000

        self.answer = round(self.volume_co2_cm3, 1)

        self.description = (
            "The diagram shows hydrochloric acid reacting with excess calcium carbonate.\n"
            "Calculate the volume of carbon dioxide produced at r.t.p."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Acid + Carbonate → Gas Volume"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Volume (dm³)}} &= {self.acid_volume_cm3}/1000 = {round(self.acid_volume_dm3,5)}\\\\"
            f"\\text{{2. Moles HCl}} &= {self.acid_conc} \\times {round(self.acid_volume_dm3,5)} = {round(self.moles_hcl,5)}\\\\"
            f"\\text{{3. Ratio 2:1}} &: n(\\text{{CO₂}}) = {round(self.moles_hcl,5)}/2 = {round(self.moles_co2,5)}\\\\"
            f"\\text{{4. Volume (dm³)}} &= {round(self.moles_co2,5)} \\times 24 = {round(self.volume_co2_dm3,5)}\\\\"
            f"\\text{{5. Volume (cm³)}} &= {round(self.volume_co2_dm3,5)} \\times 1000 = {self.answer}\\,\\text{{cm}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        ax.text(7, 6.5,
                "CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        flask_body = Circle((4, 2.5), 1.5, fill=False, linewidth=2)
        ax.add_patch(flask_body)

        flask_neck = Rectangle((3.7, 4), 0.6, 1.2, fill=False, linewidth=2)
        ax.add_patch(flask_neck)

        liquid = Circle((4, 2.5), 1.4, color="lightblue", alpha=0.7)
        ax.add_patch(liquid)

        ax.text(4, 1.8,
                "CaCO₃ (excess)",
                ha='center',
                fontsize=10)

        ax.text(1.0, 3.0,
                f"HCl(aq)\n{self.acid_volume_cm3} cm³\n{self.acid_conc} mol dm⁻³",
                fontsize=11,
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))

        tube = FancyArrowPatch((4.8, 4.6), (8, 4.6), arrowstyle="-", linewidth=3)
        ax.add_patch(tube)

        syringe_body = Rectangle((8, 4), 4, 1.2, fill=False, linewidth=2)
        ax.add_patch(syringe_body)

        plunger = Rectangle((11.5, 4), 0.3, 1.2, fill=True, color="lightgray")
        ax.add_patch(plunger)

        ax.text(10, 5.5,
                "CO₂ (g)",
                ha='center',
                fontsize=12,
                fontweight='bold')

        ax.text(7, 0.5,
                "Use the information shown to calculate the volume of CO₂ produced (cm³).",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem137:
    def __init__(self):

        variations = [
            ("Hydrochloric acid", 0.010),
            ("Hydrochloric acid", 0.100),
            ("Nitric acid", 0.020),
            ("Nitric acid", 0.050),
            ("Sulfuric acid (first proton)", 0.010),
            ("Hydrochloric acid", 0.005),
            ("Nitric acid", 0.200),
            ("Hydrochloric acid", 0.001),
            ("Nitric acid", 0.002),
            ("Hydrochloric acid", 0.050),
        ]

        self.acid_name, self.concentration = rnd.choice(variations)

        self.h_concentration = self.concentration
        self.pH = -math.log10(self.h_concentration)

        self.answer = round(self.pH, 2)

        self.description = (
            f"A solution of {self.acid_name} has concentration "
            f"{self.concentration} mol dm⁻³.\n"
            "Calculate the pH of the solution."
        )

        self.topic = "Acids and bases"
        self.subtopic = "Strong acid pH calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned} " \
            "\\text{Strong acid } & \\text{fully dissociates} \\\\ " \
            "[H^+] &= " + str(self.concentration) + " \\\\ " \
            "\\text{pH} &= -\\log(" + str(self.concentration) + ") \\\\ " \
            "&= " + str(self.answer) + " " \
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(5, 5.5,
                "Strong Acid Solution",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker = Rectangle((3, 1.5), 4, 3, fill=False, linewidth=2)
        ax.add_patch(beaker)

        solution = Rectangle((3.1, 1.6), 3.8, 2.2, linewidth=0, facecolor="lightblue", alpha=0.8)
        ax.add_patch(solution)

        ax.text(5, 3.8,
                f"{self.acid_name}",
                ha='center',
                fontsize=13,
                fontweight='bold')

        ax.text(5, 3.2,
                f"{self.concentration} mol dm⁻³",
                ha='center',
                fontsize=12)

        ax.text(5, 0.6,
                "Use pH = -log[H⁺]",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem138:
    def __init__(self):

        variations = [
            (50.0, 0.200),
            (25.0, 0.200),
            (40.0, 0.150),
            (30.0, 0.300),
            (60.0, 0.100),
            (20.0, 0.250),
            (45.0, 0.200),
            (35.0, 0.160),
            (80.0, 0.050),
            (100.0, 0.080),
        ]

        self.volume_cm3, self.concentration = rnd.choice(variations)

        self.volume_dm3 = self.volume_cm3 / 1000
        self.moles_acid = self.concentration * self.volume_dm3
        self.moles_salt = self.moles_acid

        self.mr_nano3 = 23 + 14 + (16 * 3)
        self.mass_salt = self.moles_salt * self.mr_nano3

        self.answer = round(self.mass_salt, 2)

        self.description = (
            "The diagram shows nitric acid reacting with sodium hydroxide.\n"
            "Calculate the mass of sodium nitrate formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Neutralisation mass calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Volume (dm³)}} &= {self.volume_cm3}/1000 = {round(self.volume_dm3,5)}\\\\"
            f"\\text{{2. Moles HNO₃}} &= {self.concentration} \\times {round(self.volume_dm3,5)} = {round(self.moles_acid,5)}\\\\"
            f"\\text{{3. 1:1 ratio}} &: n(\\text{{NaNO₃}}) = {round(self.moles_salt,5)}\\\\"
            f"\\text{{4. Mr NaNO₃}} &= {self.mr_nano3}\\\\"
            f"\\text{{5. Mass}} &= {round(self.moles_salt,5)} \\times {self.mr_nano3} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "HNO₃ + NaOH → NaNO₃ + H₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker1 = Rectangle((2, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker1)
        liquid1 = Rectangle((2.1, 1.6), 2.8, 2.2, facecolor="lightblue")
        ax.add_patch(liquid1)

        ax.text(3.5, 4.8,
                "Nitric Acid",
                ha='center',
                fontsize=12,
                fontweight='bold')

        ax.text(3.5, 0.8,
                f"{self.volume_cm3} cm³\n{self.concentration} mol dm⁻³",
                ha='center',
                fontsize=11)

        beaker2 = Rectangle((7, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker2)
        liquid2 = Rectangle((7.1, 1.6), 2.8, 2.2, facecolor="lightgreen")
        ax.add_patch(liquid2)

        ax.text(8.5, 4.8,
                "Sodium Hydroxide",
                ha='center',
                fontsize=12,
                fontweight='bold')

        ax.text(6, 0.4,
                "Use the information shown to calculate the mass of NaNO₃ formed (g).",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem139:
    def __init__(self):

        variations = [
            (5.00, 1.20),
            (4.00, 0.96),
            (6.00, 1.44),
            (5.00, 0.96),
            (8.00, 1.92),
            (10.00, 2.40),
            (2.50, 0.60),
            (7.50, 1.80),
            (3.00, 0.72),
            (9.00, 2.16),
        ]

        self.sample_mass, self.co2_volume_dm3 = rnd.choice(variations)

        self.moles_co2 = self.co2_volume_dm3 / 24
        self.moles_caco3 = self.moles_co2
        self.mr_caco3 = 40 + 12 + (16 * 3)
        self.mass_pure = self.moles_caco3 * self.mr_caco3
        self.purity = (self.mass_pure / self.sample_mass) * 100

        self.answer = round(self.purity, 1)

        self.description = (
            "Impure calcium carbonate reacts with excess acid.\n"
            "Use the information shown to calculate\n"
            "the percentage purity of the sample."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Percentage purity"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. n(CO₂)}} &= {self.co2_volume_dm3}/24 = {round(self.moles_co2,5)}\\\\"
            f"\\text{{2. 1:1 ratio}} &: n(CaCO₃) = {round(self.moles_caco3,5)}\\\\"
            f"\\text{{3. Mr CaCO₃}} &= {self.mr_caco3}\\\\"
            f"\\text{{4. Mass pure}} &= {round(self.moles_caco3,5)} \\times {self.mr_caco3} = {round(self.mass_pure,5)}\\\\"
            f"\\text{{5. \\% purity}} &= \\frac{{{round(self.mass_pure,5)}}}{{{self.sample_mass}}} \\times 100 = {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker = Rectangle((4, 1.5), 4, 3.5, fill=False, linewidth=2)
        ax.add_patch(beaker)

        liquid = Rectangle((4.1, 1.6), 3.8, 2.5, facecolor="lightblue")
        ax.add_patch(liquid)

        for i in range(6):
            bubble = Circle((5 + i*0.4, 3.8 + i*0.15), 0.12, color="white")
            ax.add_patch(bubble)

        ax.text(6, 4.8,
                f"Impure CaCO₃\n{self.sample_mass} g",
                ha='center',
                fontsize=12)

        ax.text(6, 0.8,
                f"CO₂ produced = {self.co2_volume_dm3} dm³\nMolar gas volume = 24 dm³ mol⁻¹",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem140:
    def __init__(self):

        variations = [
            10.2,
            5.1,
            15.3,
            20.4,
            7.65,
            12.75,
            25.5,
            3.4,
            17.0,
            8.5,
        ]

        self.mass_al2o3 = rnd.choice(variations)

        self.mr_al2o3 = (27 * 2) + (16 * 3)
        self.mr_alcl3 = 27 + (35.5 * 3)

        self.moles_al2o3 = self.mass_al2o3 / self.mr_al2o3
        self.moles_alcl3 = self.moles_al2o3 * 2
        self.mass_alcl3 = self.moles_alcl3 * self.mr_alcl3

        self.answer = round(self.mass_alcl3, 2)

        self.description = (
            "Aluminium oxide reacts with hydrochloric acid.\n"
            "Use the information shown to calculate\n"
            "the mass of aluminium chloride produced."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Amphoteric oxide reaction"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Mr Al₂O₃}} &= {self.mr_al2o3}\\\\"
            f"\\text{{2. n(Al₂O₃)}} &= {self.mass_al2o3}/{self.mr_al2o3} = {round(self.moles_al2o3,5)}\\\\"
            f"\\text{{3. Mole ratio}} &: 1:2\\\\"
            f"\\text{{4. n(AlCl₃)}} &= 2 \\times {round(self.moles_al2o3,5)} = {round(self.moles_alcl3,5)}\\\\"
            f"\\text{{5. Mr AlCl₃}} &= {self.mr_alcl3}\\\\"
            f"\\text{{6. Mass}} &= {round(self.moles_alcl3,5)} \\times {self.mr_alcl3} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker1 = Rectangle((2, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker1)
        liquid1 = Rectangle((2.1, 1.6), 2.8, 2.2, facecolor="lightgrey")
        ax.add_patch(liquid1)

        ax.text(3.5, 4.8,
                f"Al₂O₃\n{self.mass_al2o3} g",
                ha='center',
                fontsize=12)

        beaker2 = Rectangle((7, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker2)
        liquid2 = Rectangle((7.1, 1.6), 2.8, 2.2, facecolor="lightgreen")
        ax.add_patch(liquid2)

        ax.text(8.5, 4.8,
                "Excess HCl",
                ha='center',
                fontsize=12)

        ax.text(6, 0.6,
                "Calculate the mass of AlCl₃ formed (g).",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem141:
    def __init__(self):

        variations = [
            5.60,
            2.40,
            4.80,
            7.20,
            3.60,
            1.20,
            6.00,
            8.40,
            9.60,
            12.0,
        ]

        self.mass_mg = rnd.choice(variations)

        self.mr_mg = 24
        self.mr_mgso4 = 24 + 32 + (16 * 4)

        self.moles_mg = self.mass_mg / self.mr_mg
        self.moles_mgso4 = self.moles_mg
        self.mass_mgso4 = self.moles_mgso4 * self.mr_mgso4

        self.answer = round(self.mass_mgso4, 2)

        self.description = (
            "Magnesium reacts with excess sulfuric acid.\n"
            "Use the information shown to calculate\n"
            "the mass of magnesium sulfate formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Limiting reagent"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. n(Mg)}} &= {self.mass_mg}/24 = {round(self.moles_mg,5)}\\\\"
            f"\\text{{2. 1:1 ratio}} &: n(MgSO₄) = {round(self.moles_mgso4,5)}\\\\"
            f"\\text{{3. Mr MgSO₄}} &= {self.mr_mgso4}\\\\"
            f"\\text{{4. Mass}} &= {round(self.moles_mgso4,5)} \\times {self.mr_mgso4} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "Mg + H₂SO₄ → MgSO₄ + H₂",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker = Rectangle((2, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker)
        liquid = Rectangle((2.1, 1.6), 2.8, 2.2, facecolor="lightblue")
        ax.add_patch(liquid)

        ax.text(3.5, 4.8,
                f"Excess H₂SO₄",
                ha='center',
                fontsize=12)

        ax.text(3.5, 0.8,
                f"Mg = {self.mass_mg} g",
                ha='center',
                fontsize=11)

        for i in range(4):
            bubble = Circle((3.2 + i*0.4, 3.8 + i*0.15), 0.12, color="white")
            ax.add_patch(bubble)

        ax.text(8.5, 3.5,
                "Calculate mass of MgSO₄ (g)",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem142:
    def __init__(self):

        variations = [
            (50.0, 0.200, 50.0, 0.200),
            (25.0, 0.400, 25.0, 0.400),
            (40.0, 0.250, 40.0, 0.250),
            (20.0, 0.500, 20.0, 0.500),
            (60.0, 0.100, 60.0, 0.100),
            (30.0, 0.300, 30.0, 0.300),
            (10.0, 1.000, 10.0, 1.000),
            (80.0, 0.050, 80.0, 0.050),
            (45.0, 0.200, 45.0, 0.200),
            (100.0, 0.100, 100.0, 0.100),
        ]

        self.v1, self.c1, self.v2, self.c2 = rnd.choice(variations)

        self.moles_ba = (self.v1 / 1000) * self.c1
        self.moles_so4 = (self.v2 / 1000) * self.c2

        self.moles_baso4 = min(self.moles_ba, self.moles_so4)

        self.mr_baso4 = 137 + 32 + (16 * 4)
        self.mass_baso4 = self.moles_baso4 * self.mr_baso4

        self.answer = round(self.mass_baso4, 2)

        self.description = (
            "Barium nitrate reacts with sodium sulfate.\n"
            "Use the information shown to calculate\n"
            "the mass of barium sulfate precipitate formed."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Precipitation reaction"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. n(Ba(NO₃)₂)}} &= ({self.v1}/1000) \\times {self.c1} = {round(self.moles_ba,5)}\\\\"
            f"\\text{{2. n(Na₂SO₄)}} &= ({self.v2}/1000) \\times {self.c2} = {round(self.moles_so4,5)}\\\\"
            f"\\text{{3. 1:1 ratio}} &: n(BaSO₄) = {round(self.moles_baso4,5)}\\\\"
            f"\\text{{4. Mr BaSO₄}} &= {self.mr_baso4}\\\\"
            f"\\text{{5. Mass}} &= {round(self.moles_baso4,5)} \\times {self.mr_baso4} = {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "Ba(NO₃)₂ + Na₂SO₄ → BaSO₄(s) + 2NaNO₃",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker1 = Rectangle((1, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker1)
        liquid1 = Rectangle((1.1, 1.6), 2.8, 2.2, facecolor="lightblue")
        ax.add_patch(liquid1)

        ax.text(2.5, 4.8,
                f"Ba(NO₃)₂\n{self.v1} cm³\n{self.c1} mol dm⁻³",
                ha='center',
                fontsize=11)

        beaker2 = Rectangle((4.5, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker2)
        liquid2 = Rectangle((4.6, 1.6), 2.8, 2.2, facecolor="lightgreen")
        ax.add_patch(liquid2)

        ax.text(6, 4.8,
                f"Na₂SO₄\n{self.v2} cm³\n{self.c2} mol dm⁻³",
                ha='center',
                fontsize=11)

        ax.text(8.5, 3.2, "→", fontsize=20, ha='center')

        beaker3 = Rectangle((9, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker3)
        liquid3 = Rectangle((9.1, 1.6), 2.8, 2.2, facecolor="whitesmoke")
        ax.add_patch(liquid3)

        for i in range(6):
            precip = Circle((9.5 + i*0.3, 1.8), 0.1, color="blue")
            ax.add_patch(precip)

        ax.text(10.5, 4.8,
                "White precipitate\nBaSO₄",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem143:
    def __init__(self):

        variations = [
            (3.60, 2.30),
            (4.50, 2.88),
            (2.70, 1.73),
            (5.40, 3.46),
            (6.00, 3.84),
            (1.80, 1.15),
            (7.20, 4.61),
            (9.00, 5.76),
            (3.00, 1.92),
            (8.10, 5.18),
        ]

        self.initial_mass, self.anhydrous_mass = rnd.choice(variations)

        self.water_mass = self.initial_mass - self.anhydrous_mass

        self.mr_cuso4 = 63.5 + 32 + (16 * 4)
        self.mr_h2o = (2 * 1) + 16

        self.moles_cuso4 = self.anhydrous_mass / self.mr_cuso4
        self.moles_h2o = self.water_mass / self.mr_h2o

        self.x = self.moles_h2o / self.moles_cuso4

        self.answer = round(self.x)

        self.description = (
            "A hydrated copper(II) sulfate sample is heated.\n"
            "Use the information shown to calculate\n"
            "the value of x in CuSO₄·xH₂O."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Water of crystallisation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Mass of water}} &= {self.initial_mass} - {self.anhydrous_mass} = {round(self.water_mass,5)}\\\\"
            f"\\text{{2. n(CuSO₄)}} &= {self.anhydrous_mass}/{self.mr_cuso4} = {round(self.moles_cuso4,5)}\\\\"
            f"\\text{{3. n(H₂O)}} &= {round(self.water_mass,5)}/{self.mr_h2o} = {round(self.moles_h2o,5)}\\\\"
            f"\\text{{4. Ratio}} &= {round(self.moles_h2o,5)} / {round(self.moles_cuso4,5)} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "CuSO₄·xH₂O  →  CuSO₄  +  xH₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker = Rectangle((4, 2), 4, 3, fill=False, linewidth=2)
        ax.add_patch(beaker)

        liquid = Rectangle((4.1, 2.1), 3.8, 2.2, facecolor="lightblue")
        ax.add_patch(liquid)

        ax.text(6, 4.8,
                f"CuSO₄·xH₂O\n{self.initial_mass} g",
                ha='center',
                fontsize=12)

        stove_base = Rectangle((5, 0.8), 2, 0.6, color="gray")
        ax.add_patch(stove_base)

        flame = Polygon([[6,1.4],[5.7,1.0],[6.3,1.0]], color="orange")
        ax.add_patch(flame)

        ax.text(6, 0.3,
                f"After heating:\nCuSO₄ = {self.anhydrous_mass} g",
                ha='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem144:
    def __init__(self):

        variations = [
            (12.0, 18.5),
            (6.5, 10.0),
            (8.0, 12.5),
            (10.0, 15.0),
            (5.0, 7.5),
            (15.0, 23.0),
            (20.0, 30.5),
            (7.5, 11.0),
            (9.0, 13.5),
            (4.0, 6.0),
        ]

        self.mass_zno, self.actual_mass = rnd.choice(variations)

        self.mr_zno = 65 + 16
        self.mr_znno3_2 = 65 + (14 * 2) + (16 * 6)

        self.moles_zno = self.mass_zno / self.mr_zno
        self.moles_product = self.moles_zno
        self.theoretical_mass = self.moles_product * self.mr_znno3_2

        self.percent_yield = (self.actual_mass / self.theoretical_mass) * 100
        self.answer = round(self.percent_yield, 1)

        self.description = (
            "Zinc oxide reacts with excess nitric acid.\n"
            "Use the information shown to calculate\n"
            "the percentage yield of zinc nitrate."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Percentage yield"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Mr ZnO}} &= {self.mr_zno}\\\\"
            f"\\text{{2. n(ZnO)}} &= {self.mass_zno}/{self.mr_zno} = {round(self.moles_zno,5)}\\\\"
            f"\\text{{3. 1:1 ratio}} &: n(Zn(NO₃)₂) = {round(self.moles_product,5)}\\\\"
            f"\\text{{4. Mr Zn(NO₃)₂}} &= {self.mr_znno3_2}\\\\"
            f"\\text{{5. Theoretical mass}} &= {round(self.moles_product,5)} \\times {self.mr_znno3_2} = {round(self.theoretical_mass,5)}\\\\"
            f"\\text{{6. \\% yield}} &= \\frac{{{self.actual_mass}}}{{{round(self.theoretical_mass,5)}}} \\times 100 = {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.5,
                "ZnO + 2HNO₃ → Zn(NO₃)₂ + H₂O",
                ha='center',
                fontsize=16,
                fontweight='bold')

        beaker1 = Rectangle((2, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker1)
        solid = Rectangle((2.2, 1.6), 2.6, 1.0, facecolor="lightgrey")
        ax.add_patch(solid)

        ax.text(3.5, 4.8,
                f"ZnO\n{self.mass_zno} g",
                ha='center',
                fontsize=12)

        ax.text(6, 3.2, "→", fontsize=20, ha='center')

        beaker2 = Rectangle((7, 1.5), 3, 3, fill=False, linewidth=2)
        ax.add_patch(beaker2)
        product = Rectangle((7.2, 1.6), 2.6, 1.5, facecolor="lightblue")
        ax.add_patch(product)

        ax.text(8.5, 4.8,
                f"Zn(NO₃)₂ obtained\n{self.actual_mass} g",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem145:
    def __init__(self):

        variations = [
            ("Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂", "Cl₂", 0),
            ("Br₂ + 2I⁻ → 2Br⁻ + I₂", "Br₂", 0),
            ("H₂ + Cl₂ → 2HCl", "Cl₂", 0),
            ("2Na + Cl₂ → 2NaCl", "Cl₂", 0),
            ("Zn + Cu²⁺ → Zn²⁺ + Cu", "Zn", 0),
            ("2K + Br₂ → 2KBr", "Br₂", 0),
            ("Mg + Cl₂ → MgCl₂", "Cl₂", 0),
            ("Fe + S → FeS", "S", 0),
            ("H₂ + I₂ → 2HI", "I₂", 0),
            ("Ca + Cl₂ → CaCl₂", "Cl₂", 0),
        ]

        self.equation, self.species, self.ox_number = rnd.choice(variations)

        self.answer = self.ox_number

        self.description = (
            f"In the reaction:\n{self.equation}\n"
            f"What is the oxidation number of the element in {self.species}?"
        )

        self.topic = "Redox"
        self.subtopic = "Oxidation numbers"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.species} is an element in its free state}}\\\\"
            f"\\text{{Oxidation number of a free element}} &= 0"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(6, 5.4,
                "Redox Reaction",
                ha='center',
                fontsize=16,
                fontweight='bold')

        ax.text(6, 4.8,
                self.equation,
                ha='center',
                fontsize=14)

        box_width = 3.2
        box_height = 1.2
        y_box = 2.6

        react_box = Rectangle((2 - box_width/2, y_box),
                            box_width,
                            box_height,
                            facecolor="lightblue",
                            edgecolor="black",
                            linewidth=2)
        ax.add_patch(react_box)

        prod_box = Rectangle((10 - box_width/2, y_box),
                            box_width,
                            box_height,
                            facecolor="lightgreen",
                            edgecolor="black",
                            linewidth=2)
        ax.add_patch(prod_box)

        reactants = self.equation.split("→")[0].strip()
        products = self.equation.split("→")[1].strip()

        ax.text(2, y_box + box_height/2,
                reactants,
                ha='center',
                va='center',
                fontsize=12)

        ax.text(10, y_box + box_height/2,
                products,
                ha='center',
                va='center',
                fontsize=12)

        highlight_width = 2.0
        highlight_height = 0.8

        highlight = Rectangle((6 - highlight_width/2, 1.4),
                            highlight_width,
                            highlight_height,
                            facecolor="gold",
                            edgecolor="black",
                            linewidth=2)
        ax.add_patch(highlight)

        ax.text(6, 1.8,
                f"{self.species}\nOxidation number = ?",
                ha='center',
                va='center',
                fontsize=11)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem146:
    def __init__(self):

        variations = [
            ("Fe₂O₃ + 3CO → 2Fe + 3CO₂", "Fe₂O₃", "Fe", 1, 2),
            ("2Al₂O₃ + 3C → 4Al + 3CO₂", "Al₂O₃", "Al", 2, 4),
            ("2MgO + C → 2Mg + CO₂", "MgO", "Mg", 2, 2),
            ("CuO + CO → Cu + CO₂", "CuO", "Cu", 1, 1),
            ("ZnO + C → Zn + CO", "ZnO", "Zn", 1, 1),
            ("PbO + CO → Pb + CO₂", "PbO", "Pb", 1, 1),
            ("SnO₂ + 2CO → Sn + 2CO₂", "SnO₂", "Sn", 1, 1),
            ("2Fe₂O₃ + 3C → 4Fe + 3CO₂", "Fe₂O₃", "Fe", 2, 4),
            ("2NiO + C → 2Ni + CO₂", "NiO", "Ni", 2, 2),
            ("Cr₂O₃ + 3CO → 2Cr + 3CO₂", "Cr₂O₃", "Cr", 1, 2),
        ]

        self.equation, self.reactant, self.product, self.reactant_coeff, self.product_coeff = rnd.choice(variations)

        self.answer = self.product_coeff / self.reactant_coeff

        self.description = (
            f"In the reaction:\n{self.equation}\n"
            f"How many moles of {self.product} are formed from 1 mole of {self.reactant}?"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Mole ratio"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From equation:}}\\\\"
            f"{self.reactant_coeff} \\text{{ mol {self.reactant}}} \\rightarrow {self.product_coeff} \\text{{ mol {self.product}}}\\\\"
            f"\\text{{From 1 mol {self.reactant}:}} &= {self.product_coeff/self.reactant_coeff}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(7, 5.4,
                "Carbon Reduction Reaction",
                ha='center',
                fontsize=16,
                fontweight='bold')

        left, right = self.equation.split("→")
        reactants = [r.strip() for r in left.strip().split("+")]
        products = [p.strip() for p in right.strip().split("+")]

        box_width = 2.0
        box_height = 1.4
        y_box = 2.4

        x_positions = [2.5, 5.5, 8.5, 11.5]
        items = reactants + products

        for i, item in enumerate(items):
            rect = Rectangle(
                (x_positions[i] - box_width/2, y_box),
                box_width,
                box_height,
                facecolor="lightblue" if i < 2 else "lightgreen",
                edgecolor="black",
                linewidth=2
            )
            ax.add_patch(rect)

            ax.text(
                x_positions[i],
                y_box + box_height/2,
                item,
                ha='center',
                va='center',
                fontsize=13,
                fontweight='bold'
            )

        ax.text(4.0, y_box + box_height/2, "+", fontsize=18, ha='center', va='center')
        ax.text(7.0, y_box + box_height/2, "→", fontsize=20, ha='center', va='center')
        ax.text(10.0, y_box + box_height/2, "+", fontsize=18, ha='center', va='center')

        ax.text(7, 0.9,
                f"From 1 mol {self.reactant} → ? mol {self.product}",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem147:
    def __init__(self):

        variations = [
            ("C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2CO₂ + 2C₂H₅OH", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂", "glucose", "carbon dioxide", "C₆H₁₂O₆", "CO₂", 1, 2),
            ("C₆H₁₂O₆ → 2CO₂ + 2C₂H₅OH", "glucose", "carbon dioxide", "C₆H₁₂O₆", "CO₂", 1, 2),
            ("C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2CO₂ + 2C₂H₅OH", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2CO₂ + 2C₂H₅OH", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            ("C₆H₁₂O₆ → 2CO₂ + 2C₂H₅OH", "glucose", "ethanol", "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
        ]

        self.equation, self.reactant_name, self.product_name, self.reactant_formula, self.product_formula, self.reactant_coeff, self.product_coeff = rnd.choice(variations)

        self.answer = int(self.product_coeff / self.reactant_coeff)

        self.description = (
            "Fermentation of glucose produces ethanol.\n"
            "Using the equation shown in the diagram, calculate:\n"
            f"How many molecules of {self.product_name} are formed from one molecule of {self.reactant_name}?"
        )

        self.topic = "Organic chemistry"
        self.subtopic = "Fermentation stoichiometry"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the balanced equation:}}\\\\"
            f"{self.reactant_coeff}\\,\\text{{molecule {self.reactant_formula}}} \\rightarrow {self.product_coeff}\\,\\text{{molecules {self.product_formula}}}\\\\"
            f"\\text{{So from 1 molecule {self.reactant_formula}:}} &= {self.answer}\\,\\text{{molecules {self.product_formula}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(7, 5.4, "Fermentation Reaction",
                ha='center', fontsize=16, fontweight='bold')

        left, right = self.equation.split("→")
        reactants = [r.strip() for r in left.strip().split("+")]
        products = [p.strip() for p in right.strip().split("+")]

        box_width = 2.4
        box_height = 1.4
        y_box = 2.4

        x_react = 2.5
        x_prod_start = 7.5
        gap = 3

        rect = Rectangle((x_react - box_width/2, y_box),
                        box_width, box_height,
                        facecolor="#f7c59f",
                        edgecolor="black",
                        linewidth=2)
        ax.add_patch(rect)
        ax.text(x_react, y_box + box_height/2,
                reactants[0],
                ha='center', va='center',
                fontsize=13, fontweight='bold')

        ax.text(5.2, y_box + box_height/2,
                "→",
                fontsize=22,
                ha='center',
                va='center')

        for i, prod in enumerate(products):
            x = x_prod_start + i * gap

            rect = Rectangle((x - box_width/2, y_box),
                            box_width, box_height,
                            facecolor="#b6d7ff",
                            edgecolor="black",
                            linewidth=2)
            ax.add_patch(rect)

            ax.text(x, y_box + box_height/2,
                    prod,
                    ha='center', va='center',
                    fontsize=13, fontweight='bold')

            if i < len(products) - 1:
                ax.text(x + gap/2,
                        y_box + box_height/2,
                        "+",
                        fontsize=20,
                        ha='center',
                        va='center')

        ax.text(7, 0.9,
                f"From 1 molecule {self.reactant_formula} → ? molecules {self.product_formula}",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem148:
    def __init__(self):

        variations = [
            ("C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O", "ethanol", "CO₂", "C₂H₅OH", "CO₂", 1, 2),
            ("CH₄ + 2O₂ → CO₂ + 2H₂O", "methane", "CO₂", "CH₄", "CO₂", 1, 1),
            ("C₃H₈ + 5O₂ → 3CO₂ + 4H₂O", "propane", "CO₂", "C₃H₈", "CO₂", 1, 3),
            ("C₄H₁₀ + 6.5O₂ → 4CO₂ + 5H₂O", "butane", "CO₂", "C₄H₁₀", "CO₂", 1, 4),
            ("C₂H₄ + 3O₂ → 2CO₂ + 2H₂O", "ethene", "CO₂", "C₂H₄", "CO₂", 1, 2),
            ("C₆H₆ + 7.5O₂ → 6CO₂ + 3H₂O", "benzene", "CO₂", "C₆H₆", "CO₂", 1, 6),
            ("C₂H₆ + 3.5O₂ → 2CO₂ + 3H₂O", "ethane", "CO₂", "C₂H₆", "CO₂", 1, 2),
            ("C₅H₁₂ + 8O₂ → 5CO₂ + 6H₂O", "pentane", "CO₂", "C₅H₁₂", "CO₂", 1, 5),
            ("C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O", "ethanol", "H₂O", "C₂H₅OH", "H₂O", 1, 3),
            ("CH₃OH + 1.5O₂ → CO₂ + 2H₂O", "methanol", "CO₂", "CH₃OH", "CO₂", 1, 1),
        ]

        self.equation, self.reactant_name, self.product_name, self.reactant_formula, self.product_formula, self.reactant_coeff, self.product_coeff = rnd.choice(variations)

        self.answer = int(self.product_coeff / self.reactant_coeff)

        self.description = (
            "Complete combustion reaction is shown.\n"
            "Using the balanced equation in the diagram, calculate:\n"
            f"How many moles of {self.product_name} are produced from 1 mole of {self.reactant_name}?"
        )

        self.topic = "Organic chemistry"
        self.subtopic = "Combustion stoichiometry"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"{self.reactant_coeff}\\,\\text{{mol {self.reactant_formula}}} &\\rightarrow {self.product_coeff}\\,\\text{{mol {self.product_formula}}}\\\\"
            f"\\text{{From 1 mol {self.reactant_formula}:}} &= {self.answer}\\,\\text{{mol {self.product_formula}}}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):

        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(7, 5.4, "Complete Combustion Reaction",
                ha='center', fontsize=16, fontweight='bold')

        left, right = self.equation.split("→")
        reactants = [r.strip() for r in left.strip().split("+")]
        products = [p.strip() for p in right.strip().split("+")]

        box_width = 2.2
        box_height = 1.4

        x_positions = [1.5, 4.5, 8.5, 11.5]
        items = reactants + products
        colors = ["#ffd9b3", "#ffd9b3", "#c6f5c6", "#c6f5c6"]

        for i, item in enumerate(items):
            rect = Rectangle(
                (x_positions[i] - box_width/2, 2.3),
                box_width,
                box_height,
                facecolor=colors[i],
                edgecolor="black",
                linewidth=2
            )
            ax.add_patch(rect)
            ax.text(
                x_positions[i],
                3,
                item,
                ha='center',
                va='center',
                fontsize=13,
                fontweight='bold'
            )

        ax.text(3.0, 3, "+", fontsize=20, ha='center', va='center')
        ax.text(6.5, 3, "→", fontsize=22, ha='center', va='center')
        ax.text(10.0, 3, "+", fontsize=20, ha='center', va='center')

        ax.text(
            7,
            0.9,
            f"From 1 mol {self.reactant_formula} → ? mol {self.product_formula}",
            ha='center',
            fontsize=12
        )

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem149:
    def __init__(self):

        variations = [
            ("1s² 2s² 2p⁴", 6, 16),
            ("1s² 2s² 2p⁵", 7, 17),
            ("1s² 2s² 2p³", 5, 15),
            ("1s² 2s² 2p²", 4, 14),
            ("1s² 2s² 2p¹", 3, 13),
            ("1s² 2s² 2p⁶ 3s¹", 1, 1),
            ("1s² 2s² 2p⁶ 3s²", 2, 2),
            ("1s² 2s² 2p⁶ 3s² 3p⁴", 6, 16),
            ("1s² 2s² 2p⁶ 3s² 3p⁵", 7, 17),
            ("1s² 2s² 2p⁶ 3s² 3p³", 5, 15),
        ]

        self.config, self.valence, self.group = rnd.choice(variations)
        self.answer = self.group

        self.description = (
            "An element has the electron configuration:\n"
            f"{self.config}\n"
            "Determine its group number (IUPAC 1–18)."
        )

        self.topic = "Atomic structure"
        self.subtopic = "Electron configuration → group"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Valence electrons}} &= {self.valence}\\\\"
            f"\\text{{Group number}} &= {self.group}"
            "\\end{aligned}\\]"
        )

    def draw_orbital(self, ax, x, y, label, electrons):
        width = 1.6
        height = 1.3

        box = Rectangle((x - width/2, y),
                        width,
                        height,
                        facecolor="white",
                        edgecolor="black",
                        linewidth=2)
        ax.add_patch(box)

        ax.plot([x, x], [y, y + height], linewidth=2, color="black")

        arrow_y_up = y + height * 0.65
        arrow_y_down = y + height * 0.35

        if electrons == 1:
            ax.text(x - 0.35, arrow_y_up, "↑", fontsize=14, ha='center')
        elif electrons == 2:
            ax.text(x - 0.35, arrow_y_up, "↑", fontsize=14, ha='center')
            ax.text(x + 0.35, arrow_y_down, "↓", fontsize=14, ha='center')

        ax.text(x, y + height + 0.6,
                label,
                ha='center',
                fontsize=12,
                fontweight='bold')

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(7, 5.5,
                "Electron Configuration Diagram",
                ha='center',
                fontsize=16,
                fontweight='bold')

        superscript_map = {
            "⁰": "0",
            "¹": "1",
            "²": "2",
            "³": "3",
            "⁴": "4",
            "⁵": "5",
            "⁶": "6",
            "⁷": "7",
            "⁸": "8",
            "⁹": "9",
        }

        config_parts = self.config.split()

        electron_map = {}

        for part in config_parts:
            orbital = part[:2]
            superscripts = part[2:]
            normal_digits = "".join(superscript_map.get(c, c) for c in superscripts)
            electrons = int(normal_digits)
            electron_map[orbital] = electrons

        orbitals = ["1s", "2s", "2p", "3s", "3p"]
        x_positions = [2, 4, 6, 9, 11]

        for orb, x in zip(orbitals, x_positions):

            electrons = electron_map.get(orb, 0)

            if "p" in orb:
                for i in range(3):
                    e = 0
                    if electrons > i:
                        e = 1
                    if electrons > i + 3:
                        e = 2
                    self.draw_orbital(ax, x + i*0.7, 3, "" if i != 1 else orb, e)
            else:
                self.draw_orbital(ax, x, 3, orb, electrons)

        ax.text(7, 2.2,
                f"Configuration: {self.config}",
                ha='center',
                fontsize=15)

        ax.text(7, 1.4,
                "Determine the group number",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem150:
    def __init__(self):

        variations = [
            ("1s² 2s² 2p⁶ 3s²", 2),
            ("1s² 2s² 2p⁶ 3s¹", 1),
            ("1s² 2s² 2p⁶ 3s² 3p¹", 3),
            ("1s² 2s² 2p⁶ 3s² 3p²", 4),
            ("1s² 2s² 2p⁶ 3s² 3p³", 3),
            ("1s² 2s² 2p⁶ 3s² 3p⁴", 2),
            ("1s² 2s² 2p⁶ 3s² 3p⁵", 1),
            ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 1),
            ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 2),
            ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 2),
        ]

        self.config, self.lost = rnd.choice(variations)
        self.answer = self.lost

        self.description = (
            "An atom has the electron configuration:\n"
            f"{self.config}\n"
            "When forming a stable ion, how many electrons are lost?"
        )

        self.topic = "Atomic structure"
        self.subtopic = "Ion formation"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Valence electrons lost}} &= {self.lost}"
            "\\end{aligned}\\]"
        )

    def draw_orbital(self, ax, x, y, label, electrons):

        width = 1.6
        height = 1.3

        box = Rectangle((x - width/2, y),
                        width,
                        height,
                        facecolor="white",
                        edgecolor="black",
                        linewidth=2)
        ax.add_patch(box)

        ax.plot([x, x], [y, y + height], linewidth=2, color="black")

        up_y = y + height * 0.65
        down_y = y + height * 0.35

        if electrons == 1:
            ax.text(x - 0.35, up_y, "↑", fontsize=14, ha='center')
        elif electrons == 2:
            ax.text(x - 0.35, up_y, "↑", fontsize=14, ha='center')
            ax.text(x + 0.35, down_y, "↓", fontsize=14, ha='center')

        ax.text(x, y + height + 0.6,
                label,
                ha='center',
                fontsize=12,
                fontweight='bold')

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(13, 6))
        ax.set_xlim(0, 15)
        ax.set_ylim(0, 6)
        ax.axis('off')

        ax.text(7.5, 5.5,
                "Ion Formation Diagram",
                ha='center',
                fontsize=16,
                fontweight='bold')

        superscript_map = {
            "⁰": "0",
            "¹": "1",
            "²": "2",
            "³": "3",
            "⁴": "4",
            "⁵": "5",
            "⁶": "6",
            "⁷": "7",
            "⁸": "8",
            "⁹": "9",
        }

        config_parts = self.config.split()

        electron_map = {}

        for part in config_parts:
            orbital = part[:2]
            superscripts = part[2:]
            normal_digits = "".join(superscript_map.get(c, c) for c in superscripts)
            electrons = int(normal_digits)
            electron_map[orbital] = electrons

        orbitals = ["1s", "2s", "2p", "3s", "3p", "4s"]
        x_positions = [2, 4, 6, 8, 10, 12]

        for orb, x in zip(orbitals, x_positions):

            electrons = electron_map.get(orb, 0)

            if "p" in orb:
                for i in range(3):
                    e = 0
                    if electrons > i:
                        e = 1
                    if electrons > i + 3:
                        e = 2
                    self.draw_orbital(ax, x + i*0.7, 3, "" if i != 1 else orb, e)
            else:
                if electrons > 0:
                    self.draw_orbital(ax, x, 3, orb, electrons)

        ax.text(7.5, 2.2,
                f"Configuration: {self.config}",
                ha='center',
                fontsize=15)

        ax.text(7.5, 1.4,
                "Electrons lost = ?",
                ha='center',
                fontsize=12)

        os.makedirs("output", exist_ok=True)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
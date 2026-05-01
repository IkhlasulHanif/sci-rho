import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys
import math
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle, FancyArrow, FancyBboxPatch
from matplotlib.ticker import MultipleLocator

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
        self.start_temp = rnd.choice(range(95, 115, 5))
        self.plateau_temp = rnd.choice(range(70, 90, 5))
        self.end_temp = rnd.choice(range(55, 75, 5))

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
            "Calculate the duration of the phase change!"
        )

        self.topic = "States of matter"
        self.subtopic = "Solids, liquids and gases"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            r"\[\begin{aligned}"
            r"&\text{Step 1: Identify the region where the phase change (condensation) occurs.}\\"
            r"&\quad \text{During a phase change, temperature remains constant, forming a plateau between points B and C.}\\"
            r"&\text{Step 2: Read the start and end times for this plateau from the horizontal axis.}\\"
            fr"&\quad \text{{Start time (point B)}} = {self.t_B} \text{{ minutes}}\\"
            fr"&\quad \text{{End time (point C)}} = {self.t_C} \text{{ minutes}}\\"
            r"&\text{Step 3: Calculate the duration of the condensation process.}\\"
            fr"&\quad \text{{Duration}} = t_C - t_B = {self.t_C} - {self.t_B}\\"
            fr"&\quad \text{{Final Answer}} = {self.answer} \text{{ minutes}}"
            r"\end{aligned}\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        times = [self.t_A, self.t_B, self.t_C, self.t_D]
        temps = [self.start_temp, self.plateau_temp, self.plateau_temp, self.end_temp]

        ax.plot(times, temps, color='royalblue', linewidth=2)
        ax.scatter(times, temps, color='royalblue', zorder=3)

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

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(5))

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
            f"A gas diffuses across a chamber as shown in the diagram. "
            f"The gas travels a measured distance over a period of {self.time}.\n\n"
            f"Calculate the rate of diffusion of the gas (in cm/s)!"
        )

        self.topic = "States of matter"
        self.subtopic = "Diffusion"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Extract the given distance and time values from the diagram.}\\\\"
            f"&\\quad \\text{{Distance travelled}} = {self.distance} \\text{{ cm}}\\\\"
            f"&\\quad \\text{{Time taken}} = {self.time} \\text{{ s}}\\\\"
            "&\\text{Step 2: Recall the formula for the rate of diffusion.}\\\\"
            "&\\quad \\text{Rate} = \\frac{\\text{Distance}}{\\text{Time}}\\\\"
            "&\\text{Step 3: Substitute the given values into the formula and calculate.}\\\\"
            f"&\\quad \\text{{Rate}} = \\frac{{{self.distance}}}{{{self.time}}} = {round(self.distance / self.time, 10)}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer} \\text{{ cm s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        divider_x = 3

        high_bg = Rectangle((0, 0), divider_x, 4,
                            facecolor='lightcoral', alpha=0.3, zorder=0)
        low_bg = Rectangle((divider_x, 0), 10 - divider_x, 4,
                        facecolor='lightblue', alpha=0.3, zorder=0)

        ax.add_patch(high_bg)
        ax.add_patch(low_bg)

        chamber = Rectangle((0, 0), 10, 4, fill=False, linewidth=2, zorder=3)
        ax.add_patch(chamber)

        ax.plot([divider_x, divider_x], [0, 4],
                linestyle='--', color='black', zorder=3)

        for _ in range(20):
            x = rnd.uniform(0.3, divider_x - 0.3)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black', zorder=4))

        for _ in range(15):
            x = rnd.uniform(divider_x + 0.3, 9.7)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black', zorder=4))

        ax.arrow(divider_x, 2, 3, 0,
                head_width=0.3, head_length=0.4,
                fc='black', ec='black', zorder=5)

        ax.text(1.5, 4.3, "High concentration",
                ha='center', fontsize=11, fontweight='bold')
        ax.text(7.5, 4.3, "Low concentration",
                ha='center', fontsize=11, fontweight='bold')

        ax.text(5, -0.7,
                f"Distance travelled = {self.distance} cm",
                ha='center', fontsize=11)

        ax.set_xlim(-1, 11)
        ax.set_ylim(-2, 5.5)
        ax.set_aspect('equal')
        ax.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem103:
    """
    Topic: Atoms, elements and compounds
    Subtopic: Ions and ionic bonds
    Visual: Dot-and-cross diagram showing full outer-shell electrons of metal and non-metal
            before ionic bonding. Dots = metal electrons; crosses = non-metal electrons.
    Task: Determine number of electrons transferred (single numeric answer)
    """

    # Outer-shell (valence) electron counts
    _VALENCE = {
        "Na": 1, "K": 1, "Li": 1,
        "Mg": 2, "Ca": 2,
        "Cl": 7, "F": 7, "Br": 7,
        "O":  6, "S":  6,
    }

    def __init__(self):
        # Only chemically valid 1-to-1 ionic pairs where the metal transfers exactly
        # enough electrons to complete the non-metal's octet.
        ionic_pairs = [
            ("Na", "Cl", 1),
            ("K",  "Cl", 1),
            ("Li", "F",  1),
            ("K",  "Br", 1),
            ("Mg", "O",  2),
            ("Ca", "O",  2),
            ("Na", "F",  1),
            ("Na", "Br", 1),
            ("Li", "Cl", 1),
            ("Li", "Br", 1),
            ("K",  "F",  1),
            ("Mg", "S",  2),
        ]

        self.metal, self.nonmetal, self.electrons_transferred = rnd.choice(ionic_pairs)
        self.answer = self.electrons_transferred

        self.metal_valence    = self._VALENCE[self.metal]
        self.nonmetal_valence = self._VALENCE[self.nonmetal]

        self.description = (
            "The dot-and-cross diagram shows the outer-shell electrons of a metal atom "
            "and a non-metal atom before ionic bonding takes place. "
            "Electrons from the metal atom are shown as dots (•) and electrons from the "
            "non-metal atom are shown as crosses (×). "
            "The arrow indicates the direction of electron transfer.\n\n"
            "How many electrons are transferred from the metal atom to the non-metal atom?"
        )

        self.topic      = "Atoms, elements and compounds"
        self.subtopic   = "Ions and ionic bonds"
        self.source     = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Step 1: Identify the metal atom (shown with dot electrons) — }}"
            f"\\text{{{self.metal}}}.\\\\"
            f"&\\text{{Step 2: Count the dots (•) on the }} \\text{{{self.metal}}} \\text{{ atom.}}\\\\"
            f"&\\quad \\text{{Number of outer-shell electrons}} = {self.metal_valence}\\\\"
            f"&\\text{{Step 3: During ionic bonding the metal transfers ALL its outer-shell}}\\\\"
            f"&\\quad \\text{{electrons to the non-metal to form a stable ion.}}\\\\"
            f"&\\quad \\text{{Electrons transferred}} = {self.electrons_transferred}\\\\"
            f"&\\quad \\boxed{{\\text{{Answer}} = {self.answer}}}"
            "\\end{aligned}\\]"
        )

    # --- drawing helpers ---

    @staticmethod
    def _dot(ax, x, y, r=0.09):
        ax.add_patch(Circle((x, y), r, color='black'))

    @staticmethod
    def _cross(ax, x, y, s=0.09):
        ax.plot([x - s, x + s], [y - s, y + s], color='black', linewidth=1.5)
        ax.plot([x - s, x + s], [y + s, y - s], color='black', linewidth=1.5)

    @staticmethod
    def _shell_positions(cx, cy, d, n, avoid_angle=180):
        """Return (x, y) for n electrons at shell radius d around (cx, cy).
        Electrons are placed at 8 candidate slots (45° apart). Slots nearest to
        avoid_angle are filled last, creating a visible gap on that side."""
        if n == 0:
            return []
        all8 = [i * 45 for i in range(8)]

        def angular_dist(a):
            diff = abs(a - avoid_angle) % 360
            return min(diff, 360 - diff)

        # Sort farthest-from-avoid first so we fill the opposite side first
        ordered = sorted(all8, key=lambda a: -angular_dist(a))
        selected = sorted(ordered[:n])          # keep the n farthest slots
        return [
            (cx + d * np.cos(np.radians(a)),
             cy + d * np.sin(np.radians(a)))
            for a in selected
        ]

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_aspect('equal')
        ax.axis('off')

        r  = 0.90    # atom circle radius
        d  = 1.35    # electron shell radius
        mc = (3.0, 5.0)    # metal centre
        nc = (9.0, 5.0)    # non-metal centre

        # --- atom circles and labels ---
        for centre, label in ((mc, self.metal), (nc, self.nonmetal)):
            ax.add_patch(Circle(centre, r, fill=False, linewidth=2))
            ax.text(*centre, label, ha='center', va='center',
                    fontsize=16, fontweight='bold')

        # Metal: dots clustered toward the right (away from 180° / left side)
        for x, y in self._shell_positions(*mc, d, self.metal_valence, avoid_angle=180):
            self._dot(ax, x, y)

        # Non-metal: crosses fill all positions except the left (180°) side,
        # leaving a visible gap where the incoming electron(s) will arrive.
        for x, y in self._shell_positions(*nc, d, self.nonmetal_valence, avoid_angle=180):
            self._cross(ax, x, y)

        # --- transfer arrow ---
        ax.annotate(
            '', xy=(nc[0] - r - 0.15, nc[1]), xytext=(mc[0] + r + 0.15, mc[1]),
            arrowprops=dict(arrowstyle='->', color='crimson', lw=2.5)
        )

        # --- atom labels below ---
        ax.text(mc[0], mc[1] - r - 0.60,
                f"{self.metal} atom\n(• = outer-shell electrons)",
                ha='center', fontsize=11)
        ax.text(nc[0], nc[1] - r - 0.60,
                f"{self.nonmetal} atom\n(× = outer-shell electrons)",
                ha='center', fontsize=11)

        ax.set_xlim(0.0, 12.0)
        ax.set_ylim(1.8, 8.0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem104:
    """
    Topic: Atoms, elements and compounds
    Subtopic: Simple molecules and covalent bonds
    Visual: Dot-and-cross diagram of a simple covalent molecule
    Task: Determine the total number of covalent bonds in the molecule (single numeric answer)

    Only molecules whose diagram layout is explicitly coded are included, so the diagram
    always correctly shows all bonds and the answer matches what is visible.
    """

    def __init__(self):

        molecules = [
            # --- diatomic single-bond (shown via generic 2-atom layout) ---
            {"name": "hydrogen",          "formula": "H₂",   "atoms": ["H",  "H"],            "bonds": 1},
            {"name": "hydrogen chloride", "formula": "HCl",  "atoms": ["H",  "Cl"],           "bonds": 1},
            {"name": "hydrogen fluoride", "formula": "HF",   "atoms": ["H",  "F"],            "bonds": 1},
            {"name": "hydrogen bromide",  "formula": "HBr",  "atoms": ["H",  "Br"],           "bonds": 1},
            {"name": "chlorine",          "formula": "Cl₂",  "atoms": ["Cl", "Cl"],           "bonds": 1},
            {"name": "fluorine",          "formula": "F₂",   "atoms": ["F",  "F"],            "bonds": 1},
            {"name": "bromine",           "formula": "Br₂",  "atoms": ["Br", "Br"],           "bonds": 1},
            {"name": "iodine",            "formula": "I₂",   "atoms": ["I",  "I"],            "bonds": 1},
            # --- multi-bond diatomics (explicit symmetric layout) ---
            {"name": "oxygen",            "formula": "O₂",   "atoms": ["O",  "O"],            "bonds": 2},
            {"name": "nitrogen",          "formula": "N₂",   "atoms": ["N",  "N"],            "bonds": 3},
            # --- polyatomic molecules with explicit layouts ---
            {"name": "water",             "formula": "H₂O",  "atoms": ["H",  "O",  "H"],      "bonds": 2},
            {"name": "ammonia",           "formula": "NH₃",  "atoms": ["H",  "N",  "H", "H"], "bonds": 3},
            {"name": "methane",           "formula": "CH₄",  "atoms": ["H",  "C",  "H", "H", "H"], "bonds": 4},
            {"name": "carbon dioxide",    "formula": "CO₂",  "atoms": ["O",  "C",  "O"],      "bonds": 4},
        ]

        self.molecule = rnd.choice(molecules)
        self.name     = self.molecule["name"]
        self.formula  = self.molecule["formula"]
        self.atoms    = self.molecule["atoms"]
        self.answer   = self.molecule["bonds"]

        self.description = (
            "The dot-and-cross diagram shows the covalent bonding in a molecule.\n\n"
            "How many covalent bonds does this molecule contain in total?"
        )

        self.topic     = "Atoms, elements and compounds"
        self.subtopic  = "Simple molecules and covalent bonds"
        self.source    = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            r"\[\begin{aligned}"
            r"&\text{Step 1: Identify the molecule shown in the diagram.}\\"
            fr"&\quad \text{{Molecule}} = \text{{{self.name}}} \text{{ ({self.formula})}}\\"
            r"&\text{Step 2: Recall the definition of a covalent bond.}\\"
            r"&\quad \text{Each covalent bond consists of one shared pair of electrons (one dot–cross pair).}\\"
            r"&\text{Step 3: Count every dot–cross pair visible in the diagram.}\\"
            r"&\quad \text{Each pair between two atoms represents one covalent bond.}\\"
            fr"&\quad \text{{Total covalent bonds}} = {self.answer}\\"
            fr"&\quad \text{{Final Answer}} = {self.answer}"
            r"\end{aligned}\]"
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

        # Use Unicode formula strings to match the molecule dict
        if self.formula in ["H₂", "Cl₂", "O₂", "N₂", "F₂", "Br₂", "I₂"]:
            positions = [(4, 5), (8, 5)]
            bonds_between = [(0, 1, self.answer)]

        elif self.formula == "H₂O":
            positions = [(3.8, 5), (6, 5), (8.2, 5)]
            bonds_between = [(0, 1, 1), (1, 2, 1)]

        elif self.formula == "CO₂":
            positions = [(3.8, 5), (6, 5), (8.2, 5)]
            bonds_between = [(0, 1, 2), (1, 2, 2)]

        elif self.formula == "CH₄":
            positions = [(6, 5), (6, 7.3), (8.3, 5), (6, 2.7), (3.7, 5)]
            bonds_between = [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]

        elif self.formula == "NH₃":
            positions = [(6, 5), (6, 7.1), (8.1, 4.2), (3.9, 4.2)]
            bonds_between = [(0, 1, 1), (0, 2, 1), (0, 3, 1)]

        else:
            # Generic single-bond diatomic (HCl, HF, HBr)
            positions = [(4, 5), (8, 5)]
            bonds_between = [(0, 1, 1)]

        for (x, y), atom in zip(positions, self.atoms):
            ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
            ax.text(x, y, atom, ha="center", va="center", fontsize=16, fontweight="bold")

        for i, j, bond_order in bonds_between:
            x1, y1 = positions[i]
            x2, y2 = positions[j]

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
    """
    Topic: Atoms, elements and compounds
    Subtopic: Simple molecules and covalent bonds
    Visual: Dot-and-cross diagram showing bonding electron pairs in a covalent molecule
    Task: Determine the total number of shared (bonding) electrons in the molecule

    Only molecules whose diagram layout is explicitly coded are included, so every
    dot/cross pair drawn in the image corresponds exactly to a shared electron pair
    and the visible count matches the answer.
    """
    def __init__(self):

        molecules = [
            # --- symmetric diatomics (handled by the first branch) ---
            {"name": "hydrogen",          "formula": "H₂",   "atoms": ["H",  "H"],            "bonds": 1, "shared_electrons": 2},
            {"name": "chlorine",          "formula": "Cl₂",  "atoms": ["Cl", "Cl"],           "bonds": 1, "shared_electrons": 2},
            {"name": "fluorine",          "formula": "F₂",   "atoms": ["F",  "F"],            "bonds": 1, "shared_electrons": 2},
            {"name": "bromine",           "formula": "Br₂",  "atoms": ["Br", "Br"],           "bonds": 1, "shared_electrons": 2},
            {"name": "iodine",            "formula": "I₂",   "atoms": ["I",  "I"],            "bonds": 1, "shared_electrons": 2},
            {"name": "oxygen",            "formula": "O₂",   "atoms": ["O",  "O"],            "bonds": 2, "shared_electrons": 4},
            {"name": "nitrogen",          "formula": "N₂",   "atoms": ["N",  "N"],            "bonds": 3, "shared_electrons": 6},
            # --- asymmetric diatomics (handled by the generic else branch) ---
            {"name": "hydrogen chloride", "formula": "HCl",  "atoms": ["H",  "Cl"],           "bonds": 1, "shared_electrons": 2},
            {"name": "hydrogen fluoride", "formula": "HF",   "atoms": ["H",  "F"],            "bonds": 1, "shared_electrons": 2},
            {"name": "hydrogen bromide",  "formula": "HBr",  "atoms": ["H",  "Br"],           "bonds": 1, "shared_electrons": 2},
            # --- polyatomic molecules with explicit layouts ---
            {"name": "water",             "formula": "H₂O",  "atoms": ["H",  "O",  "H"],      "bonds": 2, "shared_electrons": 4},
            {"name": "ammonia",           "formula": "NH₃",  "atoms": ["H",  "N",  "H", "H"], "bonds": 3, "shared_electrons": 6},
            {"name": "methane",           "formula": "CH₄",  "atoms": ["C",  "H",  "H", "H", "H"], "bonds": 4, "shared_electrons": 8},
        ]

        self.molecule         = rnd.choice(molecules)
        self.name             = self.molecule["name"]
        self.formula          = self.molecule["formula"]
        self.atoms            = self.molecule["atoms"]
        self.bonds            = self.molecule["bonds"]
        self.shared_electrons = self.molecule["shared_electrons"]

        self.answer = self.shared_electrons

        self.description = (
            "The dot-and-cross diagram shows the bonding electrons in a molecule.\n\n"
            "Count every dot–cross pair visible in the diagram to find the total number of "
            "bonding (shared) electrons in this molecule."
        )

        self.topic      = "Atoms, elements and compounds"
        self.subtopic   = "Simple molecules and covalent bonds"
        self.source     = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            r"\[\begin{aligned}"
            r"&\text{Step 1: Identify the molecule shown in the diagram.}\\"
            fr"&\quad \text{{Molecule}} = \text{{{self.name}}} \text{{ ({self.formula})}}\\"
            r"&\text{Step 2: Count the number of covalent bonds in the molecule.}\\"
            r"&\quad \text{Each dot–cross pair between two atom circles = one covalent bond.}\\"
            fr"&\quad \text{{Number of covalent bonds}} = {self.bonds}\\"
            r"&\text{Step 3: Calculate the total number of bonding (shared) electrons.}\\"
            r"&\quad \text{Each covalent bond contains exactly 2 shared electrons.}\\"
            fr"&\quad \text{{Total bonding electrons}} = {self.bonds} \times 2\\"
            fr"&\quad \text{{Final Answer}} = {self.answer}"
            r"\end{aligned}\]"
        )

    def _draw_dot(self, ax, x, y):
        ax.add_patch(Circle((x, y), 0.07, color="black"))

    def _draw_cross(self, ax, x, y):
        ax.plot([x-0.07, x+0.07], [y-0.07, y+0.07], color="black", linewidth=1.2)
        ax.plot([x-0.07, x+0.07], [y+0.07, y-0.07], color="black", linewidth=1.2)

    def _draw_shared_pair(self, ax, mx, my, dx=0, dy=0):
        """Draw one dot–cross pair (= one shared electron pair) at midpoint offset."""
        self._draw_dot(ax,   mx + dx - 0.09, my + dy)
        self._draw_cross(ax, mx + dx + 0.09, my + dy)

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        r = 0.9

        # --- symmetric diatomics: H₂, Cl₂, O₂, N₂, F₂, Br₂, I₂ ---
        if self.formula in ["H₂", "Cl₂", "O₂", "N₂", "F₂", "Br₂", "I₂"]:
            positions = [(4.8, 5), (7.2, 5)]
            bond_order = self.bonds  # = shared_electrons // 2

            for (x, y), atom in zip(positions, self.atoms):
                ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
                ax.text(x, y, atom, ha="center", va="center",
                        fontsize=16, fontweight="bold")

            mx, my = (positions[0][0] + positions[1][0]) / 2, 5

            offsets = {1: [(0, 0)],
                       2: [(-0.13, 0.13), (0.13, -0.13)],
                       3: [(-0.22, 0.22), (0, 0), (0.22, -0.22)]}
            for dx, dy in offsets.get(bond_order, [(0, 0)]):
                self._draw_shared_pair(ax, mx, my, dx, dy)

        # --- polyatomic molecules with explicit layouts ---
        elif self.formula == "H₂O":
            atoms     = ["H", "O", "H"]
            positions = [(4.5, 5), (6, 5), (7.5, 5)]
            bond_pairs = [(0, 1), (1, 2)]

        elif self.formula == "NH₃":
            atoms     = ["H", "N", "H", "H"]
            positions = [(6, 5), (6, 6.7), (7.6, 4.4), (4.4, 4.4)]
            bond_pairs = [(0, 1), (1, 2), (1, 3)]

        elif self.formula == "CH₄":
            atoms     = ["C", "H", "H", "H", "H"]
            positions = [(6, 5), (6, 6.8), (7.8, 5), (6, 3.2), (4.2, 5)]
            bond_pairs = [(0, 1), (0, 2), (0, 3), (0, 4)]

        else:
            # Generic single-bond diatomic (HCl, HF, HBr) — 1 shared pair shown
            atoms     = self.atoms[:2]
            positions = [(4.5, 5), (7.5, 5)]
            bond_pairs = [(0, 1)]

        # Draw atoms and bond pairs for non-diatomic branches
        if self.formula not in ["H₂", "Cl₂", "O₂", "N₂", "F₂", "Br₂", "I₂"]:
            for (x, y), atom in zip(positions, atoms):
                ax.add_patch(Circle((x, y), r, fill=False, linewidth=2))
                ax.text(x, y, atom, ha="center", va="center",
                        fontsize=16, fontweight="bold")

            for i, j in bond_pairs:
                mx = (positions[i][0] + positions[j][0]) / 2
                my = (positions[i][1] + positions[j][1]) / 2
                self._draw_shared_pair(ax, mx, my)

        ax.set_title(
            f"Bonding Electrons in {self.name.capitalize()} ({self.formula})",
            fontsize=16,
            fontweight="bold"
        )

        ax.set_xlim(3, 9)
        ax.set_ylim(2.5, 7.5)

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
            "Ar_A": 24.3,
            "Ar_B": 36.5
        },
        {
            "name": "Magnesium and Hydrochloric Acid",
            "reactant_A": "Mg",
            "reactant_B": "HCl",
            "product": "H2",
            "coeff_A": 2,
            "coeff_B": 4,
            "Ar_A": 24,
            "Ar_B": 36.5
        },
        {
            "name": "Magnesium and Hydrochloric Acid",
            "reactant_A": "Mg",
            "reactant_B": "HCl",
            "product": "H2",
            "coeff_A": 1,
            "coeff_B": 3,
            "Ar_A": 25,
            "Ar_B": 37
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
            "name": "Iron and Sulfur",
            "reactant_A": "Fe",
            "reactant_B": "S",
            "product": "FeS",
            "coeff_A": 2,
            "coeff_B": 2,
            "Ar_A": 55.8,
            "Ar_B": 32.1
        },
        {
            "name": "Iron and Sulfur",
            "reactant_A": "Fe",
            "reactant_B": "S",
            "product": "FeS",
            "coeff_A": 3,
            "coeff_B": 3,
            "Ar_A": 57,
            "Ar_B": 31
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
        },
        {
            "name": "Aluminium and Oxygen",
            "reactant_A": "Al",
            "reactant_B": "O2",
            "product": "Al2O3",
            "coeff_A": 2,
            "coeff_B": 3,
            "Ar_A": 26.98,
            "Ar_B": 32
        },
        {
            "name": "Aluminium and Oxygen",
            "reactant_A": "Al",
            "reactant_B": "O2",
            "product": "Al2O3",
            "coeff_A": 6,
            "coeff_B": 5,
            "Ar_A": 27,
            "Ar_B": 31.5
        },
        {
            "name": "Aluminium and Oxygen",
            "reactant_A": "Al",
            "reactant_B": "O2",
            "product": "Al2O3",
            "coeff_A": 4,
            "coeff_B": 4,
            "Ar_A": 28,
            "Ar_B": 33
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
            f"The graph tracks the mass of reactants during the reaction between "
            f"{self.reaction['reactant_A']} and {self.reaction['reactant_B']}.\n\n"
            f"Using stoichiometry and the initial data provided in the graph, "
            f"calculate the exact mass of the excess reactant remaining!"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Limiting reagent and excess"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial masses of the reactants from the graph.}\\\\"
            f"&\\quad \\text{{Mass of }} \\mathrm{{{self.reaction['reactant_A']}}} = {self.mass_A} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Mass of }} \\mathrm{{{self.reaction['reactant_B']}}} = {self.mass_B} \\text{{ g}}\\\\"
            "&\\text{Step 2: Convert these initial masses to moles.}\\\\"
            f"&\\quad \\text{{Moles of }} \\mathrm{{{self.reaction['reactant_A']}}} = \\frac{{{self.mass_A}}}{{{self.reaction['Ar_A']}}} = {round(self.moles_A, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Moles of }} \\mathrm{{{self.reaction['reactant_B']}}} = \\frac{{{self.mass_B}}}{{{self.reaction['Ar_B']}}} = {round(self.moles_B, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Identify the limiting reactant.}\\\\"
            f"&\\quad \\text{{The graph shows }} \\mathrm{{{self.reaction['reactant_A'] if self.limiting == 'A' else self.reaction['reactant_B']}}} \\text{{ reaching 0 g, so it is the limiting reactant.}}\\\\"
            "&\\text{Step 4: Use the stoichiometric ratio to find the moles of excess reactant remaining.}\\\\"
            f"&\\quad \\text{{Excess moles remaining}} = {round(self.excess_leftover_moles, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Convert the remaining moles back to mass to find the value}\\\\"
            f"&\\quad \\text{{Mass remaining}} = {round(self.excess_leftover_moles, 4)} \\times {self.excess_Ar} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)
        decay = ((10 - t) / 10)**2

        if self.limiting == "A":
            mass_A_arr = self.mass_A * decay
            mass_B_arr = (self.mass_B - self.answer) * decay + self.answer
        else:
            mass_B_arr = self.mass_B * decay
            mass_A_arr = (self.mass_A - self.answer) * decay + self.answer

        ax.plot(t, mass_A_arr, linewidth=3, color="#2E86C1", label=self.reaction["reactant_A"])
        ax.plot(t, mass_B_arr, linewidth=3, color="#C39A3A", label=self.reaction["reactant_B"])

        # Start labels (left side)
        ax.annotate(f'{self.reaction["reactant_A"]}: {self.mass_A} g',
                    xy=(0, mass_A_arr[0]), xytext=(-0.3, mass_A_arr[0]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='right', va='center')

        ax.annotate(f'{self.reaction["reactant_B"]}: {self.mass_B} g',
                    xy=(0, mass_B_arr[0]), xytext=(-0.3, mass_B_arr[0]),
                    fontsize=10, color="#C39A3A", fontweight='bold',
                    ha='right', va='center')

        # End labels (right side)
        ax.annotate(f'{round(mass_A_arr[-1], 2)} g',
                    xy=(10, mass_A_arr[-1]), xytext=(10.2, mass_A_arr[-1]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='left', va='center')

        ax.annotate(f'{round(mass_B_arr[-1], 2)} g',
                    xy=(10, mass_B_arr[-1]), xytext=(10.2, mass_B_arr[-1]),
                    fontsize=10, color="#C39A3A", fontweight='bold',
                    ha='left', va='center')

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Mass (g)", fontsize=14, fontweight='bold')
        ax.set_title("Reactant Mass vs Time", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(-2, 12)
        ax.set_ylim(0, max(self.mass_A, self.mass_B) * 1.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem107:

    def __init__(self):

        chains = [
        {
            "name": "Calcium Carbonate Decomposition + Acid Reaction",
            "stage1": "CaCO3 \u2192 CaO + CO2",
            "stage2": "CaO + 2HCl \u2192 CaCl2 + H2O",
            "Ar_start": 100,
            "Ar_final": 111,
            "ar_note": "Ar: Ca=40, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Magnesium Carbonate Decomposition + Acid Reaction",
            "stage1": "MgCO3 \u2192 MgO + CO2",
            "stage2": "MgO + 2HCl \u2192 MgCl2 + H2O",
            "Ar_start": 84,
            "Ar_final": 95,
            "ar_note": "Ar: Mg=24, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Zinc Carbonate Decomposition + Acid Reaction",
            "stage1": "ZnCO3 \u2192 ZnO + CO2",
            "stage2": "ZnO + 2HCl \u2192 ZnCl2 + H2O",
            "Ar_start": 125,
            "Ar_final": 136,
            "ar_note": "Ar: Zn=65, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Copper Carbonate Decomposition + Reduction",
            "stage1": "CuCO3 \u2192 CuO + CO2",
            "stage2": "CuO + H2 \u2192 Cu + H2O",
            "Ar_start": 124,
            "Ar_final": 64,
            "ar_note": "Ar: Cu=64, C=12, O=16, H=1"
        },
        {
            "name": "Iron(II) Carbonate Decomposition + Acid Reaction",
            "stage1": "FeCO3 \u2192 FeO + CO2",
            "stage2": "FeO + 2HCl \u2192 FeCl2 + H2O",
            "Ar_start": 116,
            "Ar_final": 127,
            "ar_note": "Ar: Fe=56, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Manganese Carbonate Decomposition + Acid Reaction",
            "stage1": "MnCO3 \u2192 MnO + CO2",
            "stage2": "MnO + 2HCl \u2192 MnCl2 + H2O",
            "Ar_start": 115,
            "Ar_final": 126,
            "ar_note": "Ar: Mn=55, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Lead Carbonate Decomposition + Acid Reaction",
            "stage1": "PbCO3 \u2192 PbO + CO2",
            "stage2": "PbO + 2HCl \u2192 PbCl2 + H2O",
            "Ar_start": 267,
            "Ar_final": 278,
            "ar_note": "Ar: Pb=207, C=12, O=16, Cl=35.5"
        },
        {
            "name": "Calcium Carbonate Decomposition + Hydration",
            "stage1": "CaCO3 \u2192 CaO + CO2",
            "stage2": "CaO + H2O \u2192 Ca(OH)2",
            "Ar_start": 100,
            "Ar_final": 74,
            "ar_note": "Ar: Ca=40, C=12, O=16, H=1"
        },
    ]

        self.chain = rnd.choice(chains)

        self.start_mass = rnd.randint(20, 80)

        self.start_moles = self.start_mass / self.chain["Ar_start"]

        self.final_moles = self.start_moles

        self.answer = round(self.final_moles * self.chain["Ar_final"], 2)

        self.description = (
            f"The graph tracks the mass of substances during a multi-stage reaction chain.\n\n"
            f"Stage 1: {self.chain['stage1']}\n"
            f"Stage 2: {self.chain['stage2']}\n\n"
            f"Starting mass: {self.start_mass} g\n"
            f"{self.chain['ar_note']}\n\n"
            f"Using stoichiometry and the initial mass provided in the graph, "
            f"calculate the exact mass of the final product formed!"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Multi-stage reaction chains"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial mass of the starting compound from the graph.}\\\\"
            f"&\\quad \\text{{Initial mass}} = {self.start_mass} \\text{{ g}}\\\\"
            "&\\text{Step 2: Convert the initial mass to moles.}\\\\"
            f"&\\quad \\text{{Moles of starting compound}} = \\frac{{{self.start_mass}}}{{{self.chain['Ar_start']}}} = {round(self.start_moles, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Determine the overall mole ratio from the two stages.}\\\\"
            "&\\quad \\text{The ratio of starting compound to final product is 1:1 through the chain.}\\\\"
            f"&\\quad \\text{{Moles of final product}} = {round(self.final_moles, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Convert the moles of final product to mass}\\\\"
            f"&\\quad \\text{{Mass of final product}} = {round(self.final_moles, 4)} \\times {self.chain['Ar_final']} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)

        decay = ((10 - t) / 10)**2
        growth = 1 - decay
        intermediate_hump = 4 * (t/10) * ((10-t)/10)

        start_curve = self.start_mass * decay
        product_curve = self.answer * growth
        intermediate_curve = ((self.start_mass + self.answer) / 2) * intermediate_hump

        ax.plot(t, start_curve, linewidth=3, color="#2E86C1", label="Starting compound")
        ax.plot(t, intermediate_curve, linewidth=3, color="#F39C12", label="Intermediate")
        ax.plot(t, product_curve, linewidth=3, color="#28B463", label="Final product")

        # Start labels (left side)
        ax.annotate(f'Start: {self.start_mass} g',
                    xy=(0, start_curve[0]), xytext=(-0.3, start_curve[0]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='right', va='center')

        ax.annotate(f'0 g',
                    xy=(0, intermediate_curve[0]), xytext=(-0.3, intermediate_curve[0]),
                    fontsize=10, color="#F39C12", fontweight='bold',
                    ha='right', va='center')

        ax.annotate(f'0 g',
                    xy=(0, product_curve[0]), xytext=(-0.3, product_curve[0]),
                    fontsize=10, color="#28B463", fontweight='bold',
                    ha='right', va='center')

        # End labels (right side)
        ax.annotate(f'0 g',
                    xy=(10, start_curve[-1]), xytext=(10.2, start_curve[-1]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='left', va='center')

        ax.annotate(f'0 g',
                    xy=(10, intermediate_curve[-1]), xytext=(10.2, intermediate_curve[-1]),
                    fontsize=10, color="#F39C12", fontweight='bold',
                    ha='left', va='center')

        ax.annotate(f'{self.answer} g',
                    xy=(10, product_curve[-1]), xytext=(10.2, product_curve[-1]),
                    fontsize=10, color="#28B463", fontweight='bold',
                    ha='left', va='center')

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Mass (g)", fontsize=14, fontweight='bold')
        ax.set_title("Multi-Stage Reaction Chain Progress", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(-2, 12)
        ax.set_ylim(0, max(self.start_mass, self.answer) * 1.2)

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
            "name": "Iron and Sulfur",
            "eq": "Fe + S → FeS",
            "A": "Fe",
            "B": "S",
            "P": "FeS",
            "coeff_A": 1,
            "coeff_B": 1,
            "coeff_P": 1,
            "Ar_A": 55.8,
            "Ar_B": 32.1,
            "Ar_P": 87.9
        },
        {
            "name": "Iron and Sulfur",
            "eq": "Fe + S → FeS",
            "A": "Fe",
            "B": "S",
            "P": "FeS",
            "coeff_A": 1,
            "coeff_B": 1,
            "coeff_P": 1,
            "Ar_A": 57,
            "Ar_B": 31,
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
            "name": "Magnesium and Oxygen",
            "eq": "2Mg + O2 → 2MgO",
            "A": "Mg",
            "B": "O2",
            "P": "MgO",
            "coeff_A": 2,
            "coeff_B": 1,
            "coeff_P": 2,
            "Ar_A": 24.3,
            "Ar_B": 32,
            "Ar_P": 40.3
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
            "Ar_A": 25,
            "Ar_B": 31,
            "Ar_P": 39
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
            "Ar_A": 26.98,
            "Ar_B": 32,
            "Ar_P": 101.96
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
            "Ar_A": 28,
            "Ar_B": 33,
            "Ar_P": 104
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
            "Ar_A": 26,
            "Ar_B": 32,
            "Ar_P": 100
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
            f"The graph tracks the masses of reactants and product during the reaction:\n"
            f"{self.r['eq']}\n\n"
            "Using stoichiometry and the data provided in the graph, "
            "calculate the percentage yield of the reaction."
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Percentage yield with limiting reagent"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read initial reactant masses and the actual product mass from the graph.}\\\\"
            f"&\\quad \\text{{Initial mass of }} \\mathrm{{{self.r['A']}}} = {self.mass_A} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Initial mass of }} \\mathrm{{{self.r['B']}}} = {self.mass_B} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Actual mass of }} \\mathrm{{{self.r['P']}}} = {round(self.actual_mass, 2)} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate initial moles to determine the limiting reactant.}\\\\"
            f"&\\quad n(\\mathrm{{{self.r['A']}}}) = \\frac{{{self.mass_A}}}{{{self.r['Ar_A']}}} = {round(self.moles_A, 4)} \\text{{ mol}}\\\\"
            f"&\\quad n(\\mathrm{{{self.r['B']}}}) = \\frac{{{self.mass_B}}}{{{self.r['Ar_B']}}} = {round(self.moles_B, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Based on the mole ratio, the limiting reactant dictates the maximum yield.}}\\\\"
            "&\\text{Step 3: Calculate the theoretical mass of the product.}\\\\"
            f"&\\quad \\text{{Theoretical moles of }} \\mathrm{{{self.r['P']}}} = {round(self.product_moles_theoretical, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Theoretical mass}} = {round(self.product_moles_theoretical, 4)} \\times {self.r['Ar_P']} = {round(self.theoretical_mass, 4)} \\text{{ g}}\\\\"
            "&\\text{Step 4: Calculate the percentage yield.}\\\\"
            "&\\quad \\% \\text{ yield} = \\left( \\frac{\\text{Actual Mass}}{\\text{Theoretical Mass}} \\right) \\times 100\\\\"
            f"&\\quad \\% \\text{{ yield}} = \\left( \\frac{{{round(self.actual_mass, 2)}}}{{{round(self.theoretical_mass, 4)}}} \\right) \\times 100 = {self.answer} \\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        t = np.linspace(0, 10, 200)

        decay = ((10 - t) / 10)**2
        growth = 1 - decay

        used_A = self.limiting_moles_norm * self.r["coeff_A"] * self.r["Ar_A"]
        used_B = self.limiting_moles_norm * self.r["coeff_B"] * self.r["Ar_B"]
        m_end_A = self.mass_A - used_A
        m_end_B = self.mass_B - used_B

        mass_A_arr = (self.mass_A - m_end_A) * decay + m_end_A
        mass_B_arr = (self.mass_B - m_end_B) * decay + m_end_B
        actual_product_arr = self.actual_mass * growth

        ax.plot(t, mass_A_arr, linewidth=3, color="#2E86C1", label=self.r["A"])
        ax.plot(t, mass_B_arr, linewidth=3, color="#C39A3A", label=self.r["B"])
        ax.plot(t, actual_product_arr, linewidth=3, color="#E74C3C", label=f"{self.r['P']} (Actual)")

        # Start labels (left side)
        ax.annotate(f'{self.r["A"]}: {self.mass_A} g',
                    xy=(0, mass_A_arr[0]), xytext=(-0.3, mass_A_arr[0]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='right', va='center')

        ax.annotate(f'{self.r["B"]}: {self.mass_B} g',
                    xy=(0, mass_B_arr[0]), xytext=(-0.3, mass_B_arr[0]),
                    fontsize=10, color="#C39A3A", fontweight='bold',
                    ha='right', va='center')

        ax.annotate(f'{self.r["P"]}: 0 g',
                    xy=(0, actual_product_arr[0]), xytext=(-0.3, actual_product_arr[0] + 0.5),
                    fontsize=10, color="#E74C3C", fontweight='bold',
                    ha='right', va='center')

        # End labels (right side)
        ax.annotate(f'{round(m_end_A, 2)} g',
                    xy=(10, mass_A_arr[-1]), xytext=(10.2, mass_A_arr[-1]),
                    fontsize=10, color="#2E86C1", fontweight='bold',
                    ha='left', va='center')

        ax.annotate(f'{round(m_end_B, 2)} g',
                    xy=(10, mass_B_arr[-1]), xytext=(10.2, mass_B_arr[-1]),
                    fontsize=10, color="#C39A3A", fontweight='bold',
                    ha='left', va='center')

        ax.annotate(f'{round(self.actual_mass, 2)} g',
                    xy=(10, actual_product_arr[-1]), xytext=(10.2, actual_product_arr[-1]),
                    fontsize=10, color="#E74C3C", fontweight='bold',
                    ha='left', va='center')

        ax.set_xlabel("Time (s)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Mass (g)", fontsize=14, fontweight='bold')
        ax.set_title("Reaction Mass Progress & Percentage Yield", fontsize=16, fontweight='bold')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        ax.set_xlim(-2, 12)
        ax.set_ylim(0, max(self.mass_A, self.mass_B, self.actual_mass) * 1.2)

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
        },
        {
            "eq": "2CO + O2 → 2CO2",
            "gas_A": "CO",
            "gas_B": "CO2",
            "coeff_A": 2,
            "coeff_B": 2
        },
        {
            "eq": "CH4 + 2O2 → CO2 + 2H2O",
            "gas_A": "CH4",
            "gas_B": "CO2",
            "coeff_A": 1,
            "coeff_B": 1
        },
        {
            "eq": "C2H4 + 3O2 → 2CO2 + 2H2O",
            "gas_A": "C2H4",
            "gas_B": "CO2",
            "coeff_A": 1,
            "coeff_B": 2
        },
        {
            "eq": "2NO + O2 → 2NO2",
            "gas_A": "NO",
            "gas_B": "NO2",
            "coeff_A": 2,
            "coeff_B": 2
        },
        {
            "eq": "CaCO3 → CaO + CO2",
            "gas_A": "CaCO3",
            "gas_B": "CO2",
            "coeff_A": 1,
            "coeff_B": 1
        },
        {
            "eq": "2H2O2 → 2H2O + O2",
            "gas_A": "H2O2",
            "gas_B": "O2",
            "coeff_A": 2,
            "coeff_B": 1
        },
        {
            "eq": "NH4Cl + NaOH → NH3 + NaCl + H2O",
            "gas_A": "NH4Cl",
            "gas_B": "NH3",
            "coeff_A": 1,
            "coeff_B": 1
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
            "Using the 24 dm³ mol⁻¹ rule, the stoichiometry of the equation, and the data from the graph, "
            "calculate the exact volume of product gas formed!"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Gas volumes using molar gas volume"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        # Convert numbers in gas formulas to LaTeX subscripts
        latex_gas_A = self.r['gas_A']
        latex_gas_B = self.r['gas_B']
        for num in "0123456789":
            latex_gas_A = latex_gas_A.replace(num, f"_{num}")
            latex_gas_B = latex_gas_B.replace(num, f"_{num}")

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial volume of reactant gas from the graph.}\\\\"
            f"&\\quad \\text{{Volume of }} \\mathrm{{{latex_gas_A}}} = {self.volume_A} \\text{{ dm}}^3\\\\"
            "&\\text{Step 2: Convert this volume to moles using molar gas volume (24 dm}^3\\text{ mol}^{-1}\\text{).}\\\\"
            f"&\\quad n(\\mathrm{{{latex_gas_A}}}) = \\frac{{{self.volume_A}}}{{24}} = {round(self.moles_A, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the stoichiometric ratio from the equation to find moles of product.}\\\\"
            f"&\\quad \\text{{Ratio is }} {self.r['coeff_A']} : {self.r['coeff_B']}\\\\"
            f"&\\quad n(\\mathrm{{{latex_gas_B}}}) = {round(self.moles_A, 4)} \\times \\frac{{{self.r['coeff_B']}}}{{{self.r['coeff_A']}}} = {round(self.moles_B, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Convert moles of product back to volume.}\\\\"
            f"&\\quad \\text{{Volume of }} \\mathrm{{{latex_gas_B}}} = {round(self.moles_B, 4)} \\times 24 = {self.answer} \\text{{ dm}}^3\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        labels = [self.r["gas_A"], self.r["gas_B"]]
        
        # FIX: Plot 0 for the second bar so it doesn't give away the answer visually!
        plot_values = [self.volume_A, 0] 

        colors = ["#2E86C1", "#E67E22"]

        bars = ax.bar(labels, plot_values, color=colors, width=0.6)

        ax.set_ylabel("Gas Volume (dm³)", fontsize=14, fontweight='bold')
        ax.set_title("Gas Volume Stoichiometry", fontsize=16, fontweight='bold')

        # --- Visual Aids: Annotate specific numbers, hide the answer ---
        # Annotate the known reactant volume
        ax.text(bars[0].get_x() + bars[0].get_width()/2, self.volume_A,
                f"{self.volume_A}",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color="#2E86C1")

        # Place a giant ? where the second bar would be
        ax.text(bars[1].get_x() + bars[1].get_width()/2, self.volume_A * 0.5,
                "?",
                ha='center', va='center', fontsize=35, fontweight='bold', color="#E67E22")
        # -----------------------------------------------------------------

        ax.grid(True, axis='y', linestyle='--', alpha=0.6)
        
        # Ensure the y-axis scales comfortably above the highest possible value
        true_max = max(self.volume_A, self.volume_B)
        ax.set_ylim(0, true_max * 1.15)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem110:

    def __init__(self):

        systems = [
        {
            "name": "Sulfur Oxide System",
            "percent_A": 66.7, "percent_B": 33.3,
            "A": "S", "B": "O", "Ar_A": 32, "Ar_B": 16,
            "empirical": "SO",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 48, "Ar_product": 64
        },
        {
            "name": "Sulfur Oxide System",
            "percent_A": 50.0, "percent_B": 50.0,
            "A": "S", "B": "O", "Ar_A": 32, "Ar_B": 16,
            "empirical": "SO2",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 64, "Ar_product": 80
        },
        {
            "name": "Sulfur Oxide System",
            "percent_A": 40.0, "percent_B": 60.0,
            "A": "S", "B": "O", "Ar_A": 32, "Ar_B": 16,
            "empirical": "SO3",
            "generic_reaction": "2X → 2(Product) + O2",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 80, "Ar_product": 64
        },
        {
            "name": "Nitrogen Oxide System",
            "percent_A": 30.4, "percent_B": 69.6,
            "A": "N", "B": "O", "Ar_A": 14, "Ar_B": 16,
            "empirical": "NO2",
            "generic_reaction": "4X + O2 → 2(Product)",
            "coeff_reactant": 4, "coeff_product": 2,
            "Ar_reactant": 46, "Ar_product": 108
        },
        {
            "name": "Nitrogen Oxide System",
            "percent_A": 46.7, "percent_B": 53.3,
            "A": "N", "B": "O", "Ar_A": 14, "Ar_B": 16,
            "empirical": "NO",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 30, "Ar_product": 46
        },
        {
            "name": "Nitrogen Oxide System",
            "percent_A": 63.6, "percent_B": 36.4,
            "A": "N", "B": "O", "Ar_A": 14, "Ar_B": 16,
            "empirical": "N2O",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 44, "Ar_product": 60
        },
        {
            "name": "Carbon Oxide System",
            "percent_A": 27.3, "percent_B": 72.7,
            "A": "C", "B": "O", "Ar_A": 12, "Ar_B": 16,
            "empirical": "CO2",
            "generic_reaction": "X + C → 2(Product)",
            "coeff_reactant": 1, "coeff_product": 2,
            "Ar_reactant": 44, "Ar_product": 28
        },
        {
            "name": "Carbon Oxide System",
            "percent_A": 42.9, "percent_B": 57.1,
            "A": "C", "B": "O", "Ar_A": 12, "Ar_B": 16,
            "empirical": "CO",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 28, "Ar_product": 44
        },
        {
            "name": "Phosphorus Oxide System",
            "percent_A": 56.4, "percent_B": 43.6,
            "A": "P", "B": "O", "Ar_A": 31, "Ar_B": 16,
            "empirical": "P2O3",
            "generic_reaction": "2X + O2 → 2(Product)",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 110, "Ar_product": 142
        },
        {
            "name": "Phosphorus Oxide System",
            "percent_A": 43.7, "percent_B": 56.3,
            "A": "P", "B": "O", "Ar_A": 31, "Ar_B": 16,
            "empirical": "P2O5",
            "generic_reaction": "2X → 2(Product) + O2",
            "coeff_reactant": 2, "coeff_product": 2,
            "Ar_reactant": 142, "Ar_product": 110
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

        molar_ratio = self.sys["coeff_product"] / self.sys["coeff_reactant"]
        self.product_moles = self.reactant_moles * molar_ratio

        self.product_mass = self.product_moles * self.sys["Ar_product"]
        self.answer = round(self.product_mass, 2)

        self.description = (
            f"A compound contains {self.sys['percent_A']}% {self.sys['A']} and "
            f"{self.sys['percent_B']}% {self.sys['B']}.\n\n"
            "Based on the reaction setup shown in the diagram, "
            "calculate the exact mass of the final product formed!"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Empirical formula → balanced equation → mass product"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Verify the empirical formula using the given percentages.}\\\\"
            f"&\\quad \\text{{Assume a {self.sample_mass} g sample: }} m_A = {round(self.mass_A, 2)} \\text{{ g}}, m_B = {round(self.mass_B, 2)} \\text{{ g}}\\\\"
            f"&\\quad n_A = \\frac{{{round(self.mass_A, 2)}}}{{{self.sys['Ar_A']}}} = {round(self.moles_A, 4)} \\text{{ mol}}\\\\"
            f"&\\quad n_B = \\frac{{{round(self.mass_B, 2)}}}{{{self.sys['Ar_B']}}} = {round(self.moles_B, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Empirical ratio}} = {round(self.ratio_A, 2)} : {round(self.ratio_B, 2)} \\implies \\mathrm{{{self.sys['empirical']}}}\\\\"
            "&\\text{Step 2: Read the initial mass and reaction equation from the diagram.}\\\\"
            f"&\\quad \\text{{Initial mass of }} \\mathrm{{{self.sys['empirical']}}} = {self.reactant_mass_given} \\text{{ g}}\\\\"
            "&\\text{Step 3: Calculate the moles of reactant and product.}\\\\"
            f"&\\quad n_{{\\text{{reactant}}}} = \\frac{{{self.reactant_mass_given}}}{{{self.sys['Ar_reactant']}}} = {round(self.reactant_moles, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Based on the setup, ratio is }} {self.sys['coeff_reactant']}:{self.sys['coeff_product']} \\implies n_{{\\text{{product}}}} = {round(self.product_moles, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the final mass of the product.}\\\\"
            f"&\\quad m_{{\\text{{product}}}} = {round(self.product_moles, 4)} \\times {self.sys['Ar_product']} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 10))

        beaker = Polygon([
            (2.8, 7.5),
            (5.2, 7.5),
            (4.9, 2.8),
            (3.1, 2.8)
        ], closed=True, fill=False, linewidth=2)

        ax.add_patch(beaker)

        liquid = Polygon([
            (3.15, 3.6),
            (4.85, 3.6),
            (4.7, 3.0),
            (3.3, 3.0)
        ], closed=True, color="#AED6F1")

        ax.add_patch(liquid)

        ax.text(4, 8.6, "Beaker Reaction Setup", ha='center', fontsize=14, fontweight='bold')
        
        ax.text(4, 5.0, f"Reaction:\n{self.sys['generic_reaction']}", ha='center', fontsize=13, fontweight='bold', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="black"))
        
        ax.text(4, 2.1, f"Initial Mass: {self.reactant_mass_given} g", ha='center', fontsize=14, fontweight='bold')

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
            f"The diagram shows a standard electrolysis cell and a stopwatch.\n\n"
            f"A constant current of {self.current} A is passed through the solution.\n\n"
            "Using the data and equations provided, "
            "calculate the mass of copper deposited at the cathode! (round to 2 decimal places)"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis mass / moles / charge chain"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the current, time, and reduction equation from the diagram.}\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A (given)}}\\\\"
            f"&\\quad \\text{{Time }} (t) = {self.time_min} \\text{{ min (from stopwatch)}}\\\\"
            "&\\quad \\text{Equation: } \\mathrm{Cu^{2+} + 2e^- \\rightarrow Cu} \\implies \\text{2 moles of } \\mathrm{e^-} \\text{ per mole of Cu}\\\\"
            "&\\text{Step 2: Convert time to seconds and calculate total charge } (Q = It).\\\\"
            f"&\\quad t = {self.time_min} \\times 60 = {self.time_s} \\text{{ s}}\\\\"
            f"&\\quad Q = {self.current} \\times {self.time_s} = {self.charge} \\text{{ C}}\\\\"
            "&\\text{Step 3: Calculate the moles of electrons transferred.}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{96500}} = {round(self.moles_e, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Use the stoichiometric ratio to find moles of copper.}\\\\"
            f"&\\quad n(\\mathrm{{Cu}}) = \\frac{{{round(self.moles_e, 4)}}}{{2}} = {round(self.moles_cu, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Calculate the final mass of copper.}\\\\"
            f"&\\quad m(\\mathrm{{Cu}}) = {round(self.moles_cu, 4)} \\times {self.Ar_Cu} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        ax.text(7.4, 1.6, "2H2O → O2 + 4H+ + 4e−", ha="center", va="top", fontsize=9, color="#7D2E2E")
        ax.text(12.6, 1.6, "Cu2+ + 2e− → Cu", ha="center", va="top", fontsize=9, color="#1B5E20")

        # --- Visual Aid: Digital Stopwatch ---
        timer_center = (16.5, 9.5)
        timer_box = Rectangle((timer_center[0] - 2.0, timer_center[1] - 0.8), 4.0, 1.6, fill=True, facecolor="black", edgecolor="gray", linewidth=3)
        ax.add_patch(timer_box)
        
        # Format time to look like MM:SS
        time_str = f"{self.time_min:02d}:00"
        ax.text(timer_center[0], timer_center[1] + 0.2, time_str, ha="center", va="center", fontsize=20, fontweight="bold", color="lime", fontfamily="monospace")
        ax.text(timer_center[0], timer_center[1] - 0.45, "MIN : SEC", ha="center", va="center", fontsize=9, color="white")
        ax.text(timer_center[0], timer_center[1] + 1.2, "Stopwatch", ha="center", va="bottom", fontsize=11, fontweight="bold")
        # -------------------------------------

        ax.set_title("Standard Electrolysis Cell", fontsize=16, fontweight="bold")

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
            "The diagrams show an electrolysis setup before and after the reaction.\n\n"
            "Using the parameters provided in the image (current, time, volume, and initial concentration), "
            "calculate the mass of metal deposited at the cathode!"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis limiting ion in solution"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        # Format the cation for LaTeX math mode
        latex_cation = self.sys['cation'].replace('2+', '^{2+}').replace('+', '^+')

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the reaction parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Cation: }} \\mathrm{{{latex_cation}}}, \\text{{ Volume }} (V) = {self.volume_dm3} \\text{{ dm}}^3, \\text{{ Concentration }} (C) = {self.conc} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A}}, \\text{{ Time }} (t) = {self.time_min} \\text{{ min}}\\\\"
            "&\\text{Step 2: Calculate the total initial moles of metal ions in solution.}\\\\"
            f"&\\quad n_{{ion}} = V \\times C = {self.volume_dm3} \\times {self.conc} = {round(self.initial_moles_ion, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Calculate the moles of electrons supplied by the circuit.}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times ({self.time_min} \\times 60) = {self.charge} \\text{{ C}}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{96500}} = {round(self.moles_e, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Determine the theoretical moles of metal from the charge supplied.}\\\\"
            f"&\\quad n_{{metal, charge}} = \\frac{{n(\\mathrm{{e^-}})}}{{{self.sys['electron_ratio']}}} = {round(self.moles_metal_possible_from_charge, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Identify the limiting factor and calculate actual mass deposited.}\\\\"
            f"&\\quad \\text{{Actual moles}} = \\min({round(self.moles_metal_possible_from_charge, 4)}, {round(self.initial_moles_ion, 4)}) = {round(self.actual_moles_metal, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Mass}} = {round(self.actual_moles_metal, 4)} \\times {self.sys['Ar_metal']} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        
        ax.text(x_offset + 1.65, 7.8, "(+)", ha="center", fontsize=11, fontweight="bold")
        ax.text(x_offset + 4.35, 7.8, "(−)", ha="center", fontsize=11, fontweight="bold")

        # Use fixed coordinates instead of random ones to prevent overlapping
        num_ions = int(ion_count_scale * 6)
        y_positions = [4.8, 3.8, 2.8]
        x_positions = [x_offset + 2.5, x_offset + 3.4]
        
        coords = [(x, y) for x in x_positions for y in y_positions]
        
        for i in range(num_ions):
            if i < len(coords):
                x, y = coords[i]
                ax.add_patch(Circle((x, y), 0.25, color=self.sys["color"], alpha=0.9))
                ax.text(x, y, self.sys["cation"], fontsize=8, ha="center", va="center", fontweight="bold")
                
                # Neat, non-overlapping horizontal arrow
                ax.arrow(x + 0.3, y, 0.3, 0, head_width=0.12, head_length=0.15, fc="#1B5E20", ec="#1B5E20")

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_aspect("equal")
        ax.axis("off")

        ax.set_xlim(0, 14)
        ax.set_ylim(0, 10)

        self._draw_beaker(ax, 0, "Before Electrolysis", 1.0)
        self._draw_beaker(ax, 7, "After Electrolysis", 0.3)

        # Neat parameter box so all required variables are easily readable
        box = Rectangle((3.5, 0), 7.0, 1.5, fill=True, facecolor="#F8F9F9", edgecolor="black", linewidth=1.5)
        ax.add_patch(box)
        
        ax.text(7, 1.1, "Experiment Parameters", ha="center", fontsize=11, fontweight="bold")
        ax.text(7, 0.7, f"Current = {self.current} A    |    Time = {self.time_min} min", ha="center", fontsize=11)
        ax.text(7, 0.3, f"Volume = {self.volume_dm3} dm³  |  Init. Conc = {self.conc} mol dm⁻³", ha="center", fontsize=11)

        ax.set_title("Electrolysis", fontsize=16, fontweight="bold", y=0.95)

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
            "The Hoffman voltameter diagram shows the electrolysis of water.\n\n"
            "2H2O → 2H2 + O2\n\n"
            "Using the volume of the known gas collected in the diagram, "
            "calculate the exact volume of the other gas produced!"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis gas volume and stoichiometry"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        if self.given_gas == "H2":
            calc_ratio = self.ratio_O2 / self.ratio_H2
        else:
            calc_ratio = self.ratio_H2 / self.ratio_O2

        # Identify the unknown gas and format for LaTeX
        unknown_gas = "O2" if self.given_gas == "H2" else "H2"
        latex_given = self.given_gas.replace("2", "_2")
        latex_unknown = unknown_gas.replace("2", "_2")

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the volume of the known gas from the voltameter diagram.}\\\\"
            f"&\\quad \\text{{Volume of }} \\mathrm{{{latex_given}}} = {self.given_volume} \\text{{ cm}}^3\\\\"
            "&\\text{Step 2: Identify the stoichiometric ratio from the balanced equation.}\\\\"
            "&\\quad \\mathrm{2H_2O \\rightarrow 2H_2 + O_2}\\\\"
            "&\\quad \\text{Ratio of } \\mathrm{H_2 : O_2} = 2 : 1\\\\"
            "&\\text{Step 3: Calculate the volume of the unknown gas using the ratio.}\\\\"
            f"&\\quad V(\\mathrm{{{latex_unknown}}}) = {self.given_volume} \\times {round(calc_ratio, 4)} = {self.answer} \\text{{ cm}}^3\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(8, 10))
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 16)

        # --- Base reservoir ---
        reservoir = FancyBboxPatch((2.5, 1.5), 5, 2,
                                boxstyle="round,pad=0.1",
                                facecolor="#D6EAF8", edgecolor="black", linewidth=2)
        ax.add_patch(reservoir)
        ax.text(5, 2.5, "Electrolyte Solution", ha="center", va="center",
                fontsize=10, color="#1A5276")

        # --- Left tube (H2) ---
        tube_h = 8
        tube_bottom_y = 3.3
        left_x = 3.2

        # Tube outline
        left_tube = FancyBboxPatch((left_x - 0.5, tube_bottom_y), 1, tube_h,
                                boxstyle="square,pad=0",
                                facecolor="none", edgecolor="black", linewidth=2)
        ax.add_patch(left_tube)

        # Gas pocket at top (H2)
        h2_gas_height = (self.volume_H2 / 72) * tube_h * 0.85
        h2_water_height = tube_h - h2_gas_height

        # Water fill
        water_left = FancyBboxPatch((left_x - 0.48, tube_bottom_y), 0.96, h2_water_height,
                                    boxstyle="square,pad=0",
                                    facecolor="#AED6F1", edgecolor="none")
        ax.add_patch(water_left)

        # Gas fill (top)
        gas_left = FancyBboxPatch((left_x - 0.48, tube_bottom_y + h2_water_height), 0.96, h2_gas_height,
                                boxstyle="square,pad=0",
                                facecolor="#D5F5E3", edgecolor="none")
        ax.add_patch(gas_left)

        # Tube border again on top
        left_tube2 = FancyBboxPatch((left_x - 0.5, tube_bottom_y), 1, tube_h,
                                    boxstyle="square,pad=0",
                                    facecolor="none", edgecolor="black", linewidth=2)
        ax.add_patch(left_tube2)

        # --- Right tube (O2) ---
        right_x = 6.8

        right_tube = FancyBboxPatch((right_x - 0.5, tube_bottom_y), 1, tube_h,
                                    boxstyle="square,pad=0",
                                    facecolor="none", edgecolor="black", linewidth=2)
        ax.add_patch(right_tube)

        o2_gas_height = (self.volume_O2 / 72) * tube_h * 0.85
        o2_water_height = tube_h - o2_gas_height

        water_right = FancyBboxPatch((right_x - 0.48, tube_bottom_y), 0.96, o2_water_height,
                                    boxstyle="square,pad=0",
                                    facecolor="#AED6F1", edgecolor="none")
        ax.add_patch(water_right)

        gas_right = FancyBboxPatch((right_x - 0.48, tube_bottom_y + o2_water_height), 0.96, o2_gas_height,
                                boxstyle="square,pad=0",
                                facecolor="#FADBD8", edgecolor="none")
        ax.add_patch(gas_right)

        right_tube2 = FancyBboxPatch((right_x - 0.5, tube_bottom_y), 1, tube_h,
                                    boxstyle="square,pad=0",
                                    facecolor="none", edgecolor="black", linewidth=2)
        ax.add_patch(right_tube2)

        # --- Electrodes ---
        ax.plot([left_x, left_x], [tube_bottom_y + 0.2, tube_bottom_y + h2_water_height - 0.3],
                color="#2C3E50", linewidth=3, zorder=5)
        ax.plot([right_x, right_x], [tube_bottom_y + 0.2, tube_bottom_y + o2_water_height - 0.3],
                color="#2C3E50", linewidth=3, zorder=5)

        # --- Labels ---
        ax.text(left_x, tube_bottom_y + tube_h + 0.4, "H₂",
                ha="center", fontsize=16, fontweight="bold", color="#1E8449")
        ax.text(right_x, tube_bottom_y + tube_h + 0.4, "O₂",
                ha="center", fontsize=16, fontweight="bold", color="#C0392B")

        # Volume labels
        if self.given_gas == "H2":
            h2_label = f"{self.volume_H2} cm³"
            o2_label = "? cm³"
            h2_color, o2_color = "#1E8449", "#E74C3C"
        else:
            h2_label = "? cm³"
            o2_label = f"{self.volume_O2} cm³"
            h2_color, o2_color = "#E74C3C", "#1E8449"

        ax.text(left_x - 0.9, tube_bottom_y + tube_h - 0.5, h2_label,
                ha="center", fontsize=11, fontweight="bold", color=h2_color,
                rotation=90, va="center")
        ax.text(right_x + 0.9, tube_bottom_y + tube_h - 0.5, o2_label,
                ha="center", fontsize=11, fontweight="bold", color=o2_color,
                rotation=90, va="center")

        # --- Title ---
        ax.text(5, 14.5, "Hoffmann Voltameter", ha="center",
                fontsize=14, fontweight="bold")
        ax.text(5, 13.9, "Electrolysis of Water: 2H₂O → 2H₂ + O₂",
                ha="center", fontsize=11, color="#555555")

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
            f"The diagram shows an electroplating setup connected to a power source of {self.current}A.\n\n"
            "Using the parameters provided in the image (current, time, surface area, and metal type), "
            "calculate the coating thickness in micrometres (\u00b5m) (round to 2 decimal places)!"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electroplating thickness and mass deposition"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Extract the parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A}}, \\text{{ Time }} (t) = {self.time_min} \\text{{ min}}\\\\"
            f"&\\quad \\text{{Area }} (A) = {self.area_cm2} \\text{{ cm}}^2, \\text{{ Metal: }} \\mathrm{{{self.metal['metal']}}}\\\\"
            "&\\text{Step 2: Calculate total charge } (Q) \\text{ in Coulombs.}\\\\"
            f"&\\quad t = {self.time_min} \\times 60 = {self.time_s} \\text{{ s}}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_s} = {self.charge} \\text{{ C}}\\\\"
            "&\\text{Step 3: Calculate moles of electrons and moles of metal.}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{{self.F}}} = {round(self.moles_e, 4)} \\text{{ mol}}\\\\"
            f"&\\quad n(\\mathrm{{{self.metal['metal']}}}) = \\frac{{n(\\mathrm{{e^-}})}}{{{self.metal['electron_ratio']}}} = {round(self.moles_metal, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate mass and volume of the deposited metal.}\\\\"
            f"&\\quad m = n \\times A_r = {round(self.moles_metal, 4)} \\times {self.metal['Ar']} = {round(self.mass, 4)} \\text{{ g}}\\\\"
            f"&\\quad V = \\frac{{m}}{{\\rho}} = \\frac{{{round(self.mass, 4)}}}{{{self.metal['density']}}} = {round(self.volume_cm3, 4)} \\text{{ cm}}^3\\\\"
            "&\\text{Step 5: Calculate thickness in cm, then convert to } \\mu\\text{m.}\\\\"
            f"&\\quad \\text{{Thickness (cm)}} = \\frac{{V}}{{A}} = \\frac{{{round(self.volume_cm3, 4)}}}{{{self.area_cm2}}} = {round(self.thickness_cm, 6)} \\text{{ cm}}\\\\"
            f"&\\quad \\text{{Thickness (}}\\mu\\text{{m)}} = {round(self.thickness_cm, 6)} \\times 10000 = {self.answer} \\, \\mu\\text{{m}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        timer = Rectangle((15, 11.5), 4, 2, fill=True, facecolor="black", edgecolor="gray", linewidth=2)
        ax.add_patch(timer)
        time_str = f"{self.time_min:02d}:00"
        ax.text(17, 12.8, time_str, ha="center", va="center", fontsize=16, fontweight="bold", color="lime", fontfamily="monospace")
        ax.text(17, 12.0, "MIN : SEC", ha="center", va="center", fontsize=8, color="white")

        ax.text(13, 4.3, f"Surface Area\n= {self.area_cm2} cm²", ha="center", va="top", fontsize=11, fontweight="bold", color="#1F618D")
        # ------------------------------------------------------------------------

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
            "The diagram shows the purification of an impure metal using electrolysis.\n\n"
            f"The system is connected to a {self.current}A powersource.\n"
            "Using the parameters provided in the image (current, time, ore mass, metal type, and ore purity), "
            "calculate the mass of pure metal deposited at the cathode!\n"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis with impure ore and purity calculation"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Extract the parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Ore mass}} = {self.ore_mass} \\text{{ g}}, \\text{{ Purity}} = {self.purity_percent} \\%\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A}}, \\text{{ Time }} (t) = {self.time_min} \\text{{ min}}\\\\"
            f"&\\quad \\text{{Metal: }} \\mathrm{{{self.metal['metal']}}}\\\\"
            "&\\text{Step 2: Calculate the available moles of pure metal in the anode.}\\\\"
            f"&\\quad \\text{{Mass of pure metal}} = {self.ore_mass} \\times \\frac{{{self.purity_percent}}}{{100}} = {round(self.pure_metal_mass_available, 4)} \\text{{ g}}\\\\"
            f"&\\quad n(\\mathrm{{{self.metal['metal']}}})_{{\\text{{available}}}} = \\frac{{{round(self.pure_metal_mass_available, 4)}}}{{{self.metal['Ar']}}} = {round(self.moles_metal_available, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Calculate the moles of electrons supplied by the current.}\\\\"
            f"&\\quad t = {self.time_min} \\times 60 = {self.time_s} \\text{{ s}}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_s} = {self.charge} \\text{{ C}}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{96500}} = {round(self.moles_e, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the theoretical moles of metal that the charge can deposit.}\\\\"
            f"&\\quad n(\\mathrm{{{self.metal['metal']}}})_{{\\text{{charge}}}} = \\frac{{n(\\mathrm{{e^-}})}}{{{self.metal['electron_ratio']}}} = {round(self.moles_metal_possible_from_charge, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Determine the limiting factor and calculate final mass.}\\\\"
            f"&\\quad \\text{{Actual moles}} = \\min({round(self.moles_metal_available, 4)}, {round(self.moles_metal_possible_from_charge, 4)}) = {round(self.actual_moles_deposited, 4)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Mass deposited}} = {round(self.actual_moles_deposited, 4)} \\times {self.metal['Ar']} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        # --- Visual Aids: Instruments and Labels (Insert before ax.set_title) ---
        
        # Anode specs (underneath the anode)
        ax.text(9.4, 2.3, f"{self.ore_mass} g Ore", ha="center", fontsize=11, fontweight="bold")
        ax.text(9.4, 1.7, f"{self.purity_percent}% Pure {self.metal['metal']}", ha="center", fontsize=11, fontweight="bold", color="#B03A2E")

        # Stopwatch
        timer = Rectangle((15, 11), 4, 2, fill=True, facecolor="black", edgecolor="gray", linewidth=2)
        ax.add_patch(timer)
        time_str = f"{self.time_min:02d}:00"
        ax.text(17, 12.3, time_str, ha="center", va="center", fontsize=16, fontweight="bold", color="lime", fontfamily="monospace")
        ax.text(17, 11.5, "MIN : SEC", ha="center", va="center", fontsize=8, color="white")
        # ------------------------------------------------------------------------

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem116:
    """
    Topic: Electrolysis – Charge → Electrons → Ion Ratio → Mass
    Vision-based electrolysis diagram
    """

    def __init__(self):

        self.F = 96500
        self.Ar_Cu = 63.5

        self.current = round(rnd.uniform(1.0, 4.0), 1)
        self.time_minutes = rnd.randint(10, 45)

        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_electrons = self.charge / self.F
        self.moles_copper = self.moles_electrons / 2
        self.mass_copper = self.moles_copper * self.Ar_Cu

        self.answer = round(self.mass_copper, 3)

        self.description = (
            "The diagram shows electrolysis of copper(II) sulfate solution. "
            f"The process is done in {self.time_minutes} minutes. \n"
            "Use the information in the diagram to calculate "
            "the mass of copper produced."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis calculations"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Extract the parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A}}, \\text{{ Time }} (t) = {self.time_minutes} \\text{{ min}}\\\\"
            "&\\text{Step 2: Convert time to seconds and calculate total charge } (Q).\\\\"
            f"&\\quad t = {self.time_minutes} \\times 60 = {self.time_seconds} \\text{{ s}}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_seconds} = {round(self.charge, 4)} \\text{{ C}}\\\\"
            "&\\text{Step 3: Calculate moles of electrons.}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{round(self.charge, 4)}}}{{{self.F}}} = {self.moles_electrons:.5f} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Use the half-equation to find moles of copper.}\\\\"
            "&\\quad \\mathrm{Cu^{2+} + 2e^- \\rightarrow Cu} \\implies \\text{2 moles of } \\mathrm{e^-} \\text{ per mole of Cu}\\\\"
            f"&\\quad n(\\mathrm{{Cu}}) = \\frac{{n(\\mathrm{{e^-}})}}{{2}} = \\frac{{{self.moles_electrons:.5f}}}{{2}} = {self.moles_copper:.5f} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Calculate the final mass of copper.}\\\\"
            f"&\\quad \\text{{Mass}} = n \\times A_r = {self.moles_copper:.5f} \\times {self.Ar_Cu} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem117:
    """
    Topic: Electrolysis – Concentration + Volume → Limiting Ion vs Charge
    Vision-based limiting ion electrolysis
    """

    def __init__(self):

        self.F = 96500
        self.Ar_Ag = 108

        self.concentration = round(rnd.uniform(0.2, 0.8), 2)
        self.volume_dm3 = round(rnd.uniform(0.3, 0.8), 2)
        self.current = round(rnd.uniform(1.5, 3.5), 1)
        self.time_minutes = rnd.randint(12, 35)

        self.moles_ag_available = self.concentration * self.volume_dm3
        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_electrons = self.charge / self.F
        self.moles_ag_deposited = min(self.moles_ag_available, self.moles_electrons)
        self.mass_silver = self.moles_ag_deposited * self.Ar_Ag

        self.answer = round(self.mass_silver, 3)

        self.description = (
            f"The diagram shows an electrolysis setup for silver nitrate solution "
            f"of {self.volume_dm3} dm³). "
            f"Using the parameters provided in the image, "
            f"calculate the mass of silver deposited at the cathode!"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Limiting ion vs charge"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Concentration }} = {self.concentration} \\text{{ mol dm}}^{{-3}}, \\text{{ Volume }} = {self.volume_dm3} \\text{{ dm}}^3\\\\"
            f"&\\quad \\text{{Current }} (I) = {self.current} \\text{{ A}}, \\text{{ Time }} = {self.time_minutes} \\text{{ min}}\\\\"
            "&\\text{Step 2: Calculate the available moles of } \\mathrm{Ag^+} \\text{ in solution.}\\\\"
            f"&\\quad n(\\mathrm{{Ag^+}})_{{\\text{{available}}}} = c \\times V = {self.concentration} \\times {self.volume_dm3} = {round(self.moles_ag_available, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Calculate the charge and moles of electrons supplied.}\\\\"
            f"&\\quad t = {self.time_minutes} \\times 60 = {self.time_seconds} \\text{{ s}}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_seconds} = {round(self.charge, 4)} \\text{{ C}}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{round(self.charge, 4)}}}{{96500}} = {round(self.moles_electrons, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Determine the theoretical moles of silver based on charge.}\\\\"
            "&\\quad \\mathrm{Ag^+ + e^- \\rightarrow Ag} \\implies \\text{1 mole of } \\mathrm{e^-} \\text{ deposits 1 mole of Ag}\\\\"
            f"&\\quad n(\\mathrm{{Ag}})_{{\\text{{charge}}}} = {round(self.moles_electrons, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Identify the limiting factor and calculate the final mass.}\\\\"
            f"&\\quad \\text{{Actual moles}} = \\min({round(self.moles_ag_available, 4)}, {round(self.moles_electrons, 5)}) = {round(self.moles_ag_deposited, 5)} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Mass}} = n \\times A_r = {round(self.moles_ag_deposited, 5)} \\times {self.Ar_Ag} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
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

        ax.text(6, 6.2,
                f"I = {self.current} A",
                ha='center',
                fontsize=13)

        ax.text(6, 5.9,
                f"Time = {self.time_minutes} min",
                ha='center',
                fontsize=13)

        ax.text(6, 2.2,
                f"{self.concentration} mol dm⁻³",
                fontsize=12)

        ax.text(6, 0.6,
                "Ag⁺ + e⁻ → Ag",
                fontsize=12,
                ha='center')

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem118:
    """
    Topic: Electrolysis → Mass → Volume → Thickness
    Vision-based electroplating problem
    """

    def __init__(self):

        self.F = 96500
        self.Ar_Ni = 58.7
        self.density = 8.9

        self.current = round(rnd.uniform(1.5, 3.4), 1)
        self.time_minutes = rnd.randint(15, 45)
        self.area_cm2 = rnd.randint(15, 30)

        self.time_seconds = self.time_minutes * 60
        self.charge = self.current * self.time_seconds
        self.moles_e = self.charge / self.F
        self.moles_ni = self.moles_e / 2
        self.mass_ni = self.moles_ni * self.Ar_Ni
        
        self.volume_cm3 = self.mass_ni / self.density
        self.thickness_cm = self.volume_cm3 / self.area_cm2
        self.thickness_mm = self.thickness_cm * 10

        self.answer = round(self.thickness_mm, 4)

        self.description = (
            f"The diagram shows a nickel electroplating setup where the electrode surface area is {self.area_cm2} cm² "
            f"and nickel has a density of {self.density} g/cm³. "
            f"Using the parameters provided in the image, "
            f"calculate the thickness of the nickel deposited in millimetres (mm).\n"
            f"(Round to 4 decimal places)"
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Electroplating thickness"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the parameters from the diagram.}\\\\"
            f"&\\quad I = {self.current} \\text{{ A}}, \\; t = {self.time_minutes} \\text{{ min}}, \\; A = {self.area_cm2} \\text{{ cm}}^2, \\; \\rho = {self.density} \\text{{ g/cm}}^3\\\\"
            "&\\text{Step 2: Convert time to seconds and calculate total charge } (Q).\\\\"
            f"&\\quad t = {self.time_minutes} \\times 60 = {self.time_seconds} \\text{{ s}}\\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_seconds} = {round(self.charge, 4)} \\text{{ C}}\\\\"
            "&\\text{Step 3: Calculate moles of electrons.}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = \\frac{{Q}}{{F}} = \\frac{{{round(self.charge, 4)}}}{{{self.F}}} = {round(self.moles_e, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Find moles and mass of nickel deposited.}\\\\"
            "&\\quad \\mathrm{Ni^{2+} + 2e^- \\rightarrow Ni} \\implies \\text{2 moles of } \\mathrm{e^-} \\text{ deposit 1 mole of Ni}\\\\"
            f"&\\quad n(\\mathrm{{Ni}}) = \\frac{{{round(self.moles_e, 5)}}}{{2}} = {round(self.moles_ni, 5)} \\text{{ mol}}\\\\"
            f"&\\quad m(\\mathrm{{Ni}}) = n \\times A_r = {round(self.moles_ni, 5)} \\times {self.Ar_Ni} = {round(self.mass_ni, 4)} \\text{{ g}}\\\\"
            "&\\text{Step 5: Calculate volume and thickness.}\\\\"
            f"&\\quad V = \\frac{{m}}{{\\rho}} = \\frac{{{round(self.mass_ni, 4)}}}{{{self.density}}} = {round(self.volume_cm3, 5)} \\text{{ cm}}^3\\\\"
            f"&\\quad \\text{{Thickness (cm)}} = \\frac{{V}}{{A}} = \\frac{{{round(self.volume_cm3, 5)}}}{{{self.area_cm2}}} = {round(self.thickness_cm, 5)} \\text{{ cm}}\\\\"
            f"&\\quad \\text{{Thickness (mm)}} = {round(self.thickness_cm, 5)} \\times 10 = {self.answer} \\text{{ mm}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem119:
    """
        Chapter 5.1: Enthalpy diagram
        Visual: Enthalpy energy levels
    """
    
    def __init__(self):
        self.reactant_E  = rnd.randint(20, 150)
        self.product_E   = rnd.randint(20, 150)
        self.activation_E = self.reactant_E + rnd.randint(15, 100)
        
        self.delta_H = self.product_E - self.reactant_E
        self.Ea = self.activation_E - self.reactant_E
        
        self.answer = self.delta_H
        
        self.description = (
            f"An enthalpy profile diagram shows reactants at {self.reactant_E} kJ/mol. "
            "Using the values marked on the y-axis, determine the enthalpy change ΔH (kJ mol⁻¹) for this reaction."
        )

        self.topic = "Energetics"
        self.subtopic = "Enthalpy"
        self.source = "Adapted from IGCSE"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the energy of the reactants from the diagram.}\\\\"
            f"&\\quad E_{{\\text{{reactants}}}} = {self.reactant_E}\\,\\text{{kJ/mol}}\\\\"
            "&\\text{Step 2: Read the energy of the products from the diagram.}\\\\"
            f"&\\quad E_{{\\text{{products}}}} = {self.product_E}\\,\\text{{kJ/mol}}\\\\"
            "&\\text{Step 3: Apply the enthalpy change formula.}\\\\"
            "&\\quad \\Delta H = E_{{\\text{{products}}}} - E_{{\\text{{reactants}}}}\\\\"
            f"&\\quad \\Delta H = {self.product_E} - {self.reactant_E}\\\\"
            f"&\\quad \\Delta H = {self.delta_H}\\,\\text{{kJ/mol}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        profile = draw_enthalpy_profile(ax, self.reactant_E, self.product_E,
                                        self.activation_E, x_start=0, x_end=10)
        
        ax.text(profile['reactant_x'], self.reactant_E + 8, 'Reactants',
               fontsize=14, ha='center', fontweight='bold', color='#2196F3')
        ax.text(profile['product_x'], self.product_E + 8, 'Products',
               fontsize=14, ha='center', fontweight='bold', color='#E91E63')
        
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        ax.set_ylim(0, self.activation_E + 20)
        ax.set_xlim(0, 10.5)
        x_right = ax.get_xlim()[1]

        energy_levels = [
            (self.reactant_E, 'Reactants', '#2196F3', True),
            (self.product_E, 'Products',  '#E91E63', True),
            (self.activation_E, 'Peak',   '#FF9800', False)
        ]

        for y, label, color, bold in energy_levels:
            ax.axhline(y=y, linestyle='--', linewidth=1.2, alpha=0.5, color=color)
            
            ax.text(
                x_right, y,
                f"{y}",
                va='center', ha='left', fontsize=10,
                color=color,
                fontweight='bold' if bold else 'normal'
            )
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem120:
    """
    Topic: Percentage Purity + Electrolysis (Extraction)
    Vision-based extraction setup
    """

    def __init__(self):

        self.ore_mass = rnd.randint(50, 250)
        self.purity_percent = rnd.randint(60, 98)

        self.pure_cu_mass = self.ore_mass * (self.purity_percent / 100)
        self.answer = round(self.pure_cu_mass, 2)

        self.description = (
            f"The diagram shows an extraction setup for copper by electrolysis. "
            f"The ore sample has a mass of {self.ore_mass} g. "
            "Use the information shown to calculate "
            "the maximum mass of pure copper obtained."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Percentage purity + extraction"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Extract the parameters from the diagram.}\\\\"
            f"&\\quad \\text{{Ore mass}} = {self.ore_mass} \\text{{ g}}, \\; \\text{{Purity}} = {self.purity_percent} \\%\\\\"
            "&\\text{Step 2: Apply the percentage purity formula.}\\\\"
            "&\\quad \\text{Pure mass} = \\text{Ore mass} \\times \\frac{\\text{Purity}}{100}\\\\"
            f"&\\quad m(\\mathrm{{Cu}}) = {self.ore_mass} \\times \\frac{{{self.purity_percent}}}{{100}}\\\\"
            f"&\\quad m(\\mathrm{{Cu}}) = {self.ore_mass} \\times {round(self.purity_percent / 100, 4)} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
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

        ax.text(2.5, 3.2,
                f"{self.purity_percent}% Cu",
                ha='center', fontsize=11)

        furnace = patches.Rectangle((5, 2.2), 2.5, 2.5,
                                    fill=False, linewidth=3)
        ax.add_patch(furnace)

        ax.text(6.25, 5,
                "Electrolysis Cell",
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem121:
    def __init__(self):

        self.F = 96500
        
        self.initial_c = round(rnd.uniform(0.8, 1.5), 1)
        self.final_c = round(rnd.uniform(0.1, self.initial_c - 0.3), 1)
        self.volume = round(rnd.choice([0.25, 0.30, 0.40, 0.50, 0.60]), 2)

        self.delta_c = self.initial_c - self.final_c
        self.moles_cu = self.delta_c * self.volume
        self.moles_e = self.moles_cu * 2
        self.charge = self.moles_e * self.F

        self.answer = round(self.charge, 0)

        self.description = (
            "The graph shows how Cu²⁺ concentration changes during electrolysis. "
            "Use the graph and information shown to calculate "
            "the total charge passed."
        )

        self.topic = "Electrochemistry"
        self.subtopic = "Graph-based concentration change"
        self.source = "Adapted from GCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and final concentration from the graph.}\\\\"
            f"&\\quad c_{{\\text{{initial}}}} = {self.initial_c} \\text{{ mol dm}}^{{-3}}, \\; c_{{\\text{{final}}}} = {self.final_c} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\Delta c = {self.initial_c} - {self.final_c} = {round(self.delta_c, 4)} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Read the solution volume from the diagram and calculate moles of } \\mathrm{Cu^{2+}} \\text{ reacted.}\\\\"
            f"&\\quad V = {self.volume} \\text{{ dm}}^3\\\\"
            f"&\\quad n(\\mathrm{{Cu^{{2+}}}}) = \\Delta c \\times V = {round(self.delta_c, 4)} \\times {self.volume} = {round(self.moles_cu, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the half-equation to find the moles of electrons transferred.}\\\\"
            "&\\quad \\mathrm{Cu^{2+} + 2e^- \\rightarrow Cu} \\implies \\text{2 moles of } \\mathrm{e^-} \\text{ per mole of } \\mathrm{Cu^{2+}}\\\\"
            f"&\\quad n(\\mathrm{{e^-}}) = 2 \\times {round(self.moles_cu, 4)} = {round(self.moles_e, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the total charge passed.} \\\\"
            f"&\\quad Q = n(\\mathrm{{e^-}}) \\times F = {round(self.moles_e, 4)} \\times {self.F} = {self.answer} \\text{{ C}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
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

        ax_graph.scatter([0, 10], [self.initial_c, self.final_c], s=60, color="#B03A2E", zorder=5)

        # Explicitly annotate the exact numbers next to the scatter points
        ax_graph.text(0.3, self.initial_c, f"{self.initial_c}", fontsize=11, fontweight="bold", va="bottom", color="#B03A2E")
        ax_graph.text(9.7, self.final_c + 0.05, f"{self.final_c}", fontsize=11, fontweight="bold", ha="right", va="bottom", color="#B03A2E")

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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem122:
    def __init__(self):

        self.reactants_energy = rnd.randint(50, 250)
        self.products_energy = rnd.randint(20, 200)
        
        # Ensure they aren't too close in value
        while abs(self.products_energy - self.reactants_energy) < 15:
            self.products_energy = rnd.randint(20, 200)

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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the energy levels of reactants and products from the diagram.}\\\\"
            f"&\\quad \\text{{Energy of reactants}} = {self.reactants_energy} \\text{{ kJ}}\\\\"
            f"&\\quad \\text{{Energy of products}} = {self.products_energy} \\text{{ kJ}}\\\\"
            "&\\text{Step 2: Calculate the enthalpy change } (\\Delta H).\\\\"
            "&\\quad \\Delta H = \\text{Energy of products} - \\text{Energy of reactants}\\\\"
            f"&\\quad \\Delta H = {self.products_energy} - {self.reactants_energy}\\\\"
            f"&\\quad \\Delta H = {self.answer} \\text{{ kJ}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem123:
    def __init__(self):

        self.reactants_energy = rnd.randint(40, 120)
        self.peak_energy = self.reactants_energy + rnd.randint(50, 150)
        self.products_energy = rnd.randint(20, self.peak_energy - 20)

        self.activation_energy = self.peak_energy - self.reactants_energy
        self.answer = self.activation_energy

        self.description = (
            "The reaction pathway diagram shows energy levels of reactants and products.\n"
            "Calculate the activation energy, Ea, for the forward reaction."
        )

        self.topic = "Chemical Energetics"
        self.subtopic = "Activation energy from reaction pathway"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the energy of the reactants and the peak energy from the diagram.}\\\\"
            f"&\\quad \\text{{Energy of reactants}} = {self.reactants_energy} \\text{{ kJ}}\\\\"
            f"&\\quad \\text{{Peak energy}} = {self.peak_energy} \\text{{ kJ}}\\\\"
            "&\\text{Step 2: Calculate the activation energy } (E_a).\\\\"
            "&\\quad E_a = \\text{Peak energy} - \\text{Energy of reactants}\\\\"
            f"&\\quad E_a = {self.peak_energy} - {self.reactants_energy}\\\\"
            f"&\\quad E_a = {self.answer} \\text{{ kJ}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem124:
    def __init__(self):

        self.hh = 436 + rnd.randint(-15, 15)
        self.clcl = 242 + rnd.randint(-10, 10)
        self.hcl = 431 + rnd.randint(-15, 15)

        self.bonds_broken = self.hh + self.clcl
        self.bonds_formed = 2 * self.hcl
        self.delta_h = self.bonds_broken - self.bonds_formed

        self.answer = self.delta_h

        self.description = (
            "Using the bond energies and the chemical equation provided in the image, "
            "calculate the enthalpy change (\u0394H) of the reaction in kJ/mol."
        )

        self.topic = "Chemical Energetics"
        self.subtopic = "Bond energy calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the bonds broken (reactants) and their total energy.}\\\\"
            "&\\quad \\text{Reactants: } \\mathrm{H_2} \\text{ (H-H bond) and } \\mathrm{Cl_2} \\text{ (Cl-Cl bond)}\\\\"
            f"&\\quad \\text{{Energy in}} = {self.hh} + {self.clcl} = {self.bonds_broken} \\text{{ kJ/mol}}\\\\"
            "&\\text{Step 2: Identify the bonds formed (products) and their total energy.}\\\\"
            "&\\quad \\text{Products: 2 } \\mathrm{HCl} \\text{ (2 } \\times \\text{ H-Cl bonds)}\\\\"
            f"&\\quad \\text{{Energy out}} = 2 \\times {self.hcl} = {self.bonds_formed} \\text{{ kJ/mol}}\\\\"
            "&\\text{Step 3: Calculate the overall enthalpy change } (\\Delta H).\\\\"
            "&\\quad \\Delta H = \\text{Energy in (bonds broken)} - \\text{Energy out (bonds formed)}\\\\"
            f"&\\quad \\Delta H = {self.bonds_broken} - {self.bonds_formed} = {self.answer} \\text{{ kJ/mol}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        # Use a much smaller figure size suitable for a text/table graphic
        fig, ax = plt.subplots(figsize=(6, 4.5))
        ax.axis('off')

        ax.text(0.5, 0.95, "Bond Energy Table",
                fontsize=16, ha='center', fontweight='bold', transform=ax.transAxes)

        table_data = [
            ["Bond", "Energy (kJ/mol)"],
            ["H–H", str(self.hh)],
            ["Cl–Cl", str(self.clcl)],
            ["H–Cl", str(self.hcl)],
        ]

        # Use bounding box (bbox) to strictly control table width/height and positioning
        table = ax.table(cellText=table_data,
                         loc='center',
                         cellLoc='center',
                         bbox=[0.15, 0.35, 0.7, 0.5])

        table.auto_set_font_size(False)
        table.set_fontsize(12)

        # Make header row bold
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight='bold')
                cell.set_facecolor('#F2F3F4')

        ax.text(0.5, 0.15,
                "Reaction:  H₂ + Cl₂ → 2HCl",
                fontsize=14,
                ha='center',
                fontweight='bold',
                transform=ax.transAxes)

        
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
            f"The graph tracks the volume of gas produced over time during the reaction between {self.reaction}. "
            "Using the two data points explicitly highlighted on the graph, calculate the average rate of reaction for this time interval in cm\u00b3/s."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Rate from gradient"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the time and volume data points from the graph.}\\\\"
            f"&\\quad \\text{{Point 1: }} t_1 = {self.t1} \\text{{ s}}, \\; V_1 = {self.v1} \\text{{ cm}}^3\\\\"
            f"&\\quad \\text{{Point 2: }} t_2 = {self.t2} \\text{{ s}}, \\; V_2 = {self.v2} \\text{{ cm}}^3\\\\"
            "&\\text{Step 2: Calculate the change in volume } (\\Delta V) \\text{ and change in time } (\\Delta t).\\\\"
            f"&\\quad \\Delta V = {self.v2} - {self.v1} = {self.delta_v} \\text{{ cm}}^3\\\\"
            f"&\\quad \\Delta t = {self.t2} - {self.t1} = {self.delta_t} \\text{{ s}}\\\\"
            "&\\text{Step 3: Calculate the average rate of reaction.}\\\\"
            "&\\quad \\text{Rate} = \\frac{\\Delta V}{\\Delta t}\\\\"
            f"&\\quad \\text{{Rate}} = \\frac{{{self.delta_v}}}{{{self.delta_t}}} = {self.answer} \\text{{ cm}}^3\\text{{ s}}^{-1}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_axes([0.12, 0.15, 0.75, 0.7])

        times = [self.t1, self.t2]
        volumes = [self.v1, self.v2]

        ax.plot(times, volumes, color="#2E86C1", linewidth=3, zorder=2)
        ax.scatter(times, volumes, color="#E74C3C", s=100, zorder=3)

        for t, v in zip(times, volumes):
            ax.plot([t, t], [0, v], color='gray', linestyle='--', linewidth=1.5, zorder=1)
            ax.plot([0, t], [v, v], color='gray', linestyle='--', linewidth=1.5, zorder=1)

        max_time = max(times) * 1.4
        max_volume = max(volumes) * 1.4

        ax.set_xlim(0, max_time)
        ax.set_ylim(0, max_volume)

        ax.set_xlabel("Time (s)", fontsize=13)
        ax.set_ylabel("Volume of gas (cm³)", fontsize=13)

        ax.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.6)

        for spine in ax.spines.values():
            spine.set_linewidth(1.5)

        # Explicitly mark the exact time and volume points on the axes
        ax.set_xticks(times)
        ax.set_yticks(volumes)
        ax.set_xticklabels([f"{t}" for t in times], fontweight='bold', fontsize=12, color="#E74C3C")
        ax.set_yticklabels([f"{v}" for v in volumes], fontweight='bold', fontsize=12, color="#E74C3C")

        fig.text(0.5, 0.93,
                f"Rate of Reaction Data\n{self.reaction}",
                ha='center',
                fontsize=16,
                fontweight='bold')

        
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and final mass values from the graph.}\\\\"
            f"&\\quad \\text{{Initial mass}} = {self.initial_mass} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final mass}} = {self.final_mass} \\text{{ g}}\\\\"
            "&\\text{Step 2: Identify when the mass stops changing (becomes constant).}\\\\"
            "&\\quad \\text{The reaction finishes when the curve flattens into a horizontal plateau.}\\\\"
            "&\\text{Step 3: Read the time at which the plateau begins from the x-axis.}\\\\"
            f"&\\quad \\text{{Time at plateau}} = {self.answer} \\text{{ s}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the amounts of each component from the bar chart.}\\\\"
            f"&\\quad \\text{{Product}} ({self.product_name}) = {self.product_mol} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Reactant 1}} = {self.reactant1_mol} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Reactant 2}} = {self.reactant2_mol} \\text{{ mol}}\\\\"
            "&\\text{Step 2: Calculate the total number of moles at equilibrium.}\\\\"
            f"&\\quad \\text{{Total moles}} = {self.product_mol} + {self.reactant1_mol} + {self.reactant2_mol} = {self.total_moles} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Calculate the percentage yield of the product.}\\\\"
            "&\\quad \\text{Percentage yield} = \\frac{\\text{moles of product}}{\\text{total moles}} \\times 100\\\\"
            f"&\\quad \\text{{Percentage yield}} = \\frac{{{self.product_mol}}}{{{self.total_moles}}} \\times 100 = {self.answer} \\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and equilibrium moles from the diagram.}\\\\"
            f"&\\quad \\text{{Initial moles}} = {self.initial_moles} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Equilibrium moles}} = {self.equilibrium_moles} \\text{{ mol}}\\\\"
            "&\\text{Step 2: Calculate the decrease in total number of moles.}\\\\"
            "&\\quad \\text{Decrease} = \\text{Initial moles} - \\text{Equilibrium moles}\\\\"
            f"&\\quad \\text{{Decrease}} = {self.initial_moles} - {self.equilibrium_moles} = {self.answer} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
            ("CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O",      "CO₂", 120, 90,  0.50),  # → 0.020
            ("Mg + 2HCl → MgCl₂ + H₂",                  "H₂",  120, 60,  0.25),  # → 0.040
            ("Zn + 2HCl → ZnCl₂ + H₂",                  "H₂",  240, 40,  0.40),  # → 0.050
            ("CaCO₃ + 2HNO₃ → Ca(NO₃)₂ + CO₂ + H₂O",  "CO₂", 360, 100, 0.30),  # → 0.100
            ("Fe + 2HCl → FeCl₂ + H₂",                  "H₂",  144, 70,  0.20),  # → 0.060
            ("CaCO₃ + 2HCl → CaCl₂ + CO₂ + H₂O",      "CO₂", 480, 75,  0.80),  # → 0.050
            ("Mg + 2HCl → MgCl₂ + H₂",                  "H₂",   72, 80,  0.30),  # → 0.020
            ("Zn + 2HCl → ZnCl₂ + H₂",                  "H₂",  336, 85,  0.35),  # → 0.080
            ("CaCO₃ + 2HNO₃ → Ca(NO₃)₂ + CO₂ + H₂O",  "CO₂", 216, 50,  0.30),  # → 0.060
            ("Fe + 2HCl → FeCl₂ + H₂",                  "H₂",  420, 65,  0.50),  # → 0.070
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the final volume of gas produced from the graph.}\\\\"
            f"&\\quad \\text{{Final volume of gas}} = {self.final_volume_cm3} \\text{{ cm}}^3\\\\"
            "&\\text{Step 2: Convert the gas volume from cm³ to dm³.}\\\\"
            f"&\\quad V = \\frac{{{self.final_volume_cm3}}}{{1000}} = {round(self.volume_dm3, 4)} \\text{{ dm}}^3\\\\"
            "&\\text{Step 3: Calculate the moles of gas using molar gas volume (24 dm³ mol⁻¹).}\\\\"
            f"&\\quad n(\\text{{gas}}) = \\frac{{{round(self.volume_dm3, 4)}}}{{24}} = {round(self.moles_gas, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Use the stoichiometric ratio to find moles of HCl.}\\\\"
            f"&\\quad n(\\text{{HCl}}) = 2 \\times {round(self.moles_gas, 4)} = {round(self.moles_hcl, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Calculate the concentration of the acid.}\\\\"
            f"&\\quad c = \\frac{{n}}{{V}} = \\frac{{{round(self.moles_hcl, 4)}}}{{{self.acid_volume_dm3}}} = {self.answer} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Chem130:
    def __init__(self):

        variations = [
            # N₂ + 3H₂ → 2NH₃: NH₃_produced = N₂_reacted × 2
            ("Haber Process",              "N₂ + 3H₂ ⇌ 2NH₃",    "N₂",  40, 120, 15, 45, 50),  # reacted=25 → 50 NH₃
            ("Haber Process",              "N₂ + 3H₂ ⇌ 2NH₃",    "N₂",  50, 150, 20, 60, 60),  # reacted=30 → 60 NH₃
            # 2SO₂ + O₂ → 2SO₃: SO₃_produced = SO₂_reacted (2:2); O₂_reacted = SO₂_reacted/2
            ("Sulfur trioxide formation",  "2SO₂ + O₂ ⇌ 2SO₃",   "SO₂", 60, 40, 30, 25, 30),  # SO₂_reacted=30; O₂_eq=25; SO₃=30
            ("Sulfur trioxide formation",  "2SO₂ + O₂ ⇌ 2SO₃",   "SO₂", 80, 50, 40, 30, 40),  # SO₂_reacted=40; O₂_eq=30; SO₃=40
            # 2NO₂ → N₂O₄: N₂O₄_produced = NO₂_reacted / 2
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄",    "NO₂", 100, None, 40, None, 30),  # reacted=60 → 30 N₂O₄
            ("Dinitrogen tetroxide formation", "2NO₂ ⇌ N₂O₄",    "NO₂",  80, None, 30, None, 25),  # reacted=50 → 25 N₂O₄
            # H₂ + I₂ → 2HI: HI_produced = H₂_reacted × 2; stoichiometry 1:1:2
            ("Hydrogen iodide formation",  "H₂ + I₂ ⇌ 2HI",      "H₂",  60, 60, 20, 20, 80),
            ("Hydrogen iodide formation",  "H₂ + I₂ ⇌ 2HI",      "H₂",  50, 50, 10, 10, 80),
            # NH₃ + HCl → NH₄Cl: 1:1:1 ratio
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
            f"The diagram shows the equilibrium composition for {self.process} "
            f"({self.equation}), with {self.limiting_species} starting at {self.initial_limiting} mol. "
            f"Calculate the percentage conversion of {self.limiting_species}."
        )

        self.topic = "Chemical reactions"
        self.subtopic = "Percentage conversion"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and equilibrium amounts of the limiting reactant.}\\\\"
            f"&\\quad \\text{{Initial amount of }} {self.limiting_species} = {self.initial_limiting} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Equilibrium amount of }} {self.limiting_species} = {self.eq_limiting} \\text{{ mol}}\\\\"
            "&\\text{Step 2: Calculate the amount that reacted.}\\\\"
            f"&\\quad \\text{{Amount reacted}} = {self.initial_limiting} - {self.eq_limiting} = {self.used} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Calculate the percentage conversion.}\\\\"
            "&\\quad \\text{Percentage conversion} = \\frac{\\text{Amount reacted}}{\\text{Initial amount}} \\times 100\\\\"
            f"&\\quad \\text{{Percentage conversion}} = \\frac{{{self.used}}}{{{self.initial_limiting}}} \\times 100 = {self.answer} \\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and final concentrations from the graph.}\\\\"
            f"&\\quad c_{{\\text{{initial}}}} = {self.initial_c} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad c_{{\\text{{final}}}} = {self.c_final} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Calculate the change in concentration and change in time.}\\\\"
            f"&\\quad \\Delta c = {self.initial_c} - {self.c_final} = {round(self.delta_c, 3)} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\Delta t = {self.full_time} - 0 = {self.delta_t} \\text{{ s}}\\\\"
            "&\\text{Step 3: Calculate the average rate of reaction.}\\\\"
            "&\\quad \\text{Average rate} = \\frac{\\Delta c}{\\Delta t}\\\\"
            f"&\\quad \\text{{Average rate}} = \\frac{{{round(self.delta_c, 3)}}}{{{self.delta_t}}} = {self.answer} \\text{{ mol dm}}^{{-3}} \\text{{ s}}^{{-1}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the species that is oxidised from the diagram and equation.}\\\\"
            f"&\\quad \\text{{Reactant species: }} {self.reactant} \\rightarrow {self.product}\\\\"
            "&\\text{Step 2: Determine the change in oxidation number per mole.}\\\\"
            f"&\\quad \\text{{Oxidation number change per mole}} = {self.electron_change}\\\\"
            "&\\text{Step 3: Read the moles of reactant used from the diagram.}\\\\"
            f"&\\quad \\text{{Moles of }} {self.reactant} \\text{{ used}} = {self.moles_used} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the total moles of electrons transferred.}\\\\"
            "&\\quad \\text{Electrons transferred} = \\text{moles} \\times \\text{oxidation change}\\\\"
            f"&\\quad \\text{{Electrons transferred}} = {self.moles_used} \\times {self.electron_change} = {self.answer} \\text{{ mol}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the titrant concentration and volume from the diagram.}\\\\"
            f"&\\quad \\text{{Concentration of titrant}} = {self.titrant_conc} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\text{{Volume of titrant}} = {self.titrant_volume_cm3} \\text{{ cm}}^3\\\\"
            "&\\text{Step 2: Convert the titrant volume to dm³ and calculate moles of titrant.}\\\\"
            f"&\\quad V_{{\\text{{titrant}}}} = \\frac{{{self.titrant_volume_cm3}}}{{1000}} = {round(self.titrant_volume_dm3, 4)} \\text{{ dm}}^3\\\\"
            f"&\\quad n_{{\\text{{titrant}}}} = {self.titrant_conc} \\times {round(self.titrant_volume_dm3, 4)} = {round(self.moles_titrant, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the stoichiometric ratio to find moles of Fe²⁺.}\\\\"
            f"&\\quad n(\\mathrm{{Fe^{{2+}}}}) = {round(self.moles_titrant, 4)} \\times \\frac{{{self.fe_ratio}}}{{{self.titrant_ratio}}} = {round(self.moles_fe, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the concentration of Fe²⁺.}\\\\"
            f"&\\quad V_{{\\text{{Fe}}}} = {round(self.fe_volume_dm3, 4)} \\text{{ dm}}^3\\\\"
            f"&\\quad c(\\mathrm{{Fe^{{2+}}}}) = \\frac{{{round(self.moles_fe, 4)}}}{{{round(self.fe_volume_dm3, 4)}}} = {self.answer} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the mass of the reactant and identify it from the diagram.}\\\\"
            f"&\\quad \\text{{Reactant: }} \\mathrm{{{self.reactant}}}, \\text{{ Mass}} = {self.mass_reactant} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate the molar mass of the reactant.}\\\\"
            f"&\\quad M_r(\\mathrm{{{self.reactant}}}) = {round(self.mr_reactant, 2)} \\text{{ g mol}}^{{-1}}\\\\"
            "&\\text{Step 3: Calculate the moles of the reactant.}\\\\"
            f"&\\quad n(\\mathrm{{{self.reactant}}}) = \\frac{{{self.mass_reactant}}}{{{round(self.mr_reactant, 2)}}} = {round(self.moles_reactant, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Use the mole ratio to find moles of product.}\\\\"
            f"&\\quad n(\\mathrm{{{self.product}}}) = {round(self.moles_reactant, 4)} \\times {self.mole_ratio} = {round(self.moles_product, 4)} \\text{{ mol}}\\\\"
            "&\\text{Step 5: Calculate the mass of product formed.}\\\\"
            f"&\\quad m(\\mathrm{{{self.product}}}) = {round(self.moles_product, 4)} \\times {self.ar_product} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the NaOH concentration and volume from the diagram.}\\\\"
            f"&\\quad c(\\text{{NaOH}}) = {self.base_conc} \\text{{ mol dm}}^{{-3}}, \\; V(\\text{{NaOH}}) = {self.base_volume_cm3} \\text{{ cm}}^3\\\\"
            "&\\text{Step 2: Convert the NaOH volume to dm³ and calculate moles.}\\\\"
            f"&\\quad V(\\text{{NaOH}}) = \\frac{{{self.base_volume_cm3}}}{{1000}} = {round(self.base_volume_dm3, 5)} \\text{{ dm}}^3\\\\"
            f"&\\quad n(\\text{{NaOH}}) = {self.base_conc} \\times {round(self.base_volume_dm3, 5)} = {round(self.moles_base, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Apply the 1:1 mole ratio to find moles of HCl.}\\\\"
            "&\\quad \\text{HCl + NaOH} \\rightarrow \\text{NaCl + H}_2\\text{O} \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{HCl}}) = n(\\text{{NaOH}}) = {round(self.moles_acid, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the concentration of HCl.}\\\\"
            f"&\\quad V(\\text{{HCl}}) = \\frac{{{self.acid_volume_cm3}}}{{1000}} = {round(self.acid_volume_dm3, 5)} \\text{{ dm}}^3\\\\"
            f"&\\quad c(\\text{{HCl}}) = \\frac{{n}}{{V}} = \\frac{{{round(self.moles_acid, 5)}}}{{{round(self.acid_volume_dm3, 5)}}} = {self.answer} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the volume and concentration of HCl from the diagram.}\\\\"
            f"&\\quad V(\\text{{HCl}}) = {self.acid_volume_cm3} \\text{{ cm}}^3, \\; c(\\text{{HCl}}) = {self.acid_conc} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Convert volume to dm³ and calculate moles of HCl.}\\\\"
            f"&\\quad V = \\frac{{{self.acid_volume_cm3}}}{{1000}} = {round(self.acid_volume_dm3, 5)} \\text{{ dm}}^3\\\\"
            f"&\\quad n(\\text{{HCl}}) = {self.acid_conc} \\times {round(self.acid_volume_dm3, 5)} = {round(self.moles_hcl, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 2:1 mole ratio to find moles of CO₂.}\\\\"
            "&\\quad \\text{CaCO}_3 + \\text{2HCl} \\rightarrow \\text{CaCl}_2 + \\text{CO}_2 + \\text{H}_2\\text{O} \\implies 2:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{CO}}_2) = \\frac{{{round(self.moles_hcl, 5)}}}{{2}} = {round(self.moles_co2, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Convert moles of CO₂ to volume using molar gas volume (24 dm³ mol⁻¹).}\\\\"
            f"&\\quad V(\\text{{CO}}_2) = {round(self.moles_co2, 5)} \\times 24 = {round(self.volume_co2_dm3, 5)} \\text{{ dm}}^3\\\\"
            "&\\text{Step 5: Convert the volume from dm³ to cm³.}\\\\"
            f"&\\quad V(\\text{{CO}}_2) = {round(self.volume_co2_dm3, 5)} \\times 1000 = {self.answer} \\text{{ cm}}^3\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
            f"as shown on the image.\n"
            "Calculate the pH of the solution."
        )

        self.topic = "Acids and bases"
        self.subtopic = "Strong acid pH calculation"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the acid concentration from the diagram.}\\\\"
            f"&\\quad c({self.acid_name}) = {self.concentration} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Recall that a strong acid fully dissociates in water.}\\\\"
            f"&\\quad [\\text{{H}}^+] = c = {self.concentration} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 3: Apply the pH formula.}\\\\"
            "&\\quad \\text{pH} = -\\log_{10}[\\text{H}^+]\\\\"
            f"&\\quad \\text{{pH}} = -\\log_{{10}}({self.concentration}) = {self.answer}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the volume and concentration of HNO₃ from the diagram.}\\\\"
            f"&\\quad V(\\text{{HNO}}_3) = {self.volume_cm3} \\text{{ cm}}^3, \\; c = {self.concentration} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Convert volume to dm³ and calculate moles of HNO₃.}\\\\"
            f"&\\quad V = \\frac{{{self.volume_cm3}}}{{1000}} = {round(self.volume_dm3, 5)} \\text{{ dm}}^3\\\\"
            f"&\\quad n(\\text{{HNO}}_3) = {self.concentration} \\times {round(self.volume_dm3, 5)} = {round(self.moles_acid, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 1:1 mole ratio to find moles of NaNO₃.}\\\\"
            "&\\quad \\text{HNO}_3 + \\text{NaOH} \\rightarrow \\text{NaNO}_3 + \\text{H}_2\\text{O} \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{NaNO}}_3) = {round(self.moles_salt, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the molar mass of NaNO₃.}\\\\"
            f"&\\quad M_r(\\text{{NaNO}}_3) = {self.mr_nano3} \\text{{ g mol}}^{{-1}}\\\\"
            "&\\text{Step 5: Calculate the mass of NaNO₃ formed.}\\\\"
            f"&\\quad m = n \\times M_r = {round(self.moles_salt, 5)} \\times {self.mr_nano3} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem139:
    def __init__(self):

        variations = [
            (5.00, 0.96),   # purity = 80.0%
            (4.00, 0.72),   # purity = 75.0%
            (5.00, 1.08),   # purity = 90.0%
            (5.00, 0.84),   # purity = 70.0%
            (5.00, 1.02),   # purity = 85.0%
            (8.00, 1.44),   # purity = 75.0%
            (8.00, 1.68),   # purity = 87.5%
            (10.00, 2.16),  # purity = 90.0%
            (10.00, 1.80),  # purity = 75.0%
            (6.00, 1.20),   # purity = 83.3%
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the volume of CO₂ produced and the sample mass from the diagram.}\\\\"
            f"&\\quad V(\\text{{CO}}_2) = {self.co2_volume_dm3} \\text{{ dm}}^3, \\; \\text{{Sample mass}} = {self.sample_mass} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate the moles of CO₂ produced.}\\\\"
            f"&\\quad n(\\text{{CO}}_2) = \\frac{{{self.co2_volume_dm3}}}{{24}} = {round(self.moles_co2, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 1:1 mole ratio to find moles of CaCO₃.}\\\\"
            "&\\quad \\text{CaCO}_3 \\rightarrow \\text{CaO + CO}_2 \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{CaCO}}_3) = {round(self.moles_caco3, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the mass of pure CaCO₃.}\\\\"
            f"&\\quad M_r(\\text{{CaCO}}_3) = {self.mr_caco3} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad m(\\text{{CaCO}}_3) = {round(self.moles_caco3, 5)} \\times {self.mr_caco3} = {round(self.mass_pure, 5)} \\text{{ g}}\\\\"
            "&\\text{Step 5: Calculate the percentage purity.}\\\\"
            "&\\quad \\% \\text{ purity} = \\frac{\\text{mass of pure compound}}{\\text{mass of sample}} \\times 100\\\\"
            f"&\\quad \\% \\text{{ purity}} = \\frac{{{round(self.mass_pure, 5)}}}{{{self.sample_mass}}} \\times 100 = {self.answer} \\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the mass of Al₂O₃ from the diagram.}\\\\"
            f"&\\quad m(\\text{{Al}}_2\\text{{O}}_3) = {self.mass_al2o3} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate the molar mass of Al₂O₃ and find moles.}\\\\"
            f"&\\quad M_r(\\text{{Al}}_2\\text{{O}}_3) = {self.mr_al2o3} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad n(\\text{{Al}}_2\\text{{O}}_3) = \\frac{{{self.mass_al2o3}}}{{{self.mr_al2o3}}} = {round(self.moles_al2o3, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 1:2 mole ratio from the equation to find moles of AlCl₃.}\\\\"
            "&\\quad \\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O} \\implies 1:2 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{AlCl}}_3) = 2 \\times {round(self.moles_al2o3, 5)} = {round(self.moles_alcl3, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the molar mass of AlCl₃ and find the mass.}\\\\"
            f"&\\quad M_r(\\text{{AlCl}}_3) = {self.mr_alcl3} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad m(\\text{{AlCl}}_3) = {round(self.moles_alcl3, 5)} \\times {self.mr_alcl3} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the mass of magnesium from the diagram.}\\\\"
            f"&\\quad m(\\text{{Mg}}) = {self.mass_mg} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate the moles of magnesium.}\\\\"
            f"&\\quad n(\\text{{Mg}}) = \\frac{{{self.mass_mg}}}{{{self.mr_mg}}} = {round(self.moles_mg, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 1:1 mole ratio to find moles of MgSO₄.}\\\\"
            "&\\quad \\text{Mg + H}_2\\text{SO}_4 \\rightarrow \\text{MgSO}_4 + \\text{H}_2 \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{MgSO}}_4) = {round(self.moles_mgso4, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the molar mass of MgSO₄ and find the mass.}\\\\"
            f"&\\quad M_r(\\text{{MgSO}}_4) = {self.mr_mgso4} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad m(\\text{{MgSO}}_4) = {round(self.moles_mgso4, 5)} \\times {self.mr_mgso4} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read volumes and concentrations of both reactants from the diagram.}\\\\"
            f"&\\quad V(\\text{{Ba(NO}}_3)_2) = {self.v1} \\text{{ cm}}^3, \\; c = {self.c1} \\text{{ mol dm}}^{{-3}}\\\\"
            f"&\\quad V(\\text{{Na}}_2\\text{{SO}}_4) = {self.v2} \\text{{ cm}}^3, \\; c = {self.c2} \\text{{ mol dm}}^{{-3}}\\\\"
            "&\\text{Step 2: Calculate moles of each reactant.}\\\\"
            f"&\\quad n(\\text{{Ba(NO}}_3)_2) = \\frac{{{self.v1}}}{{1000}} \\times {self.c1} = {round(self.moles_ba, 5)} \\text{{ mol}}\\\\"
            f"&\\quad n(\\text{{Na}}_2\\text{{SO}}_4) = \\frac{{{self.v2}}}{{1000}} \\times {self.c2} = {round(self.moles_so4, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Identify the limiting reactant using the 1:1 ratio.}\\\\"
            "&\\quad \\text{Ba(NO}_3)_2 + \\text{Na}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{NaNO}_3 \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{BaSO}}_4) = \\min({round(self.moles_ba, 5)}, {round(self.moles_so4, 5)}) = {round(self.moles_baso4, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the mass of BaSO₄ precipitate formed.}\\\\"
            f"&\\quad M_r(\\text{{BaSO}}_4) = {self.mr_baso4} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad m(\\text{{BaSO}}_4) = {round(self.moles_baso4, 5)} \\times {self.mr_baso4} = {self.answer} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the initial and anhydrous masses from the diagram.}\\\\"
            f"&\\quad \\text{{Initial mass (hydrated)}} = {self.initial_mass} \\text{{ g}}\\\\"
            f"&\\quad \\text{{Mass after heating (anhydrous CuSO}}_4) = {self.anhydrous_mass} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate the mass of water lost.}\\\\"
            f"&\\quad m(\\text{{H}}_2\\text{{O}}) = {self.initial_mass} - {self.anhydrous_mass} = {round(self.water_mass, 5)} \\text{{ g}}\\\\"
            "&\\text{Step 3: Calculate the moles of CuSO₄ and H₂O.}\\\\"
            f"&\\quad n(\\text{{CuSO}}_4) = \\frac{{{self.anhydrous_mass}}}{{{self.mr_cuso4}}} = {round(self.moles_cuso4, 5)} \\text{{ mol}}\\\\"
            f"&\\quad n(\\text{{H}}_2\\text{{O}}) = \\frac{{{round(self.water_mass, 5)}}}{{{self.mr_h2o}}} = {round(self.moles_h2o, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the ratio to find x.}\\\\"
            f"&\\quad x = \\frac{{n(\\text{{H}}_2\\text{{O}})}}{{n(\\text{{CuSO}}_4)}} = \\frac{{{round(self.moles_h2o, 5)}}}{{{round(self.moles_cuso4, 5)}}} = {self.answer}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the mass of ZnO and the actual mass of product from the diagram.}\\\\"
            f"&\\quad m(\\text{{ZnO}}) = {self.mass_zno} \\text{{ g}}, \\; m_{{\\text{{actual}}}}(\\text{{Zn(NO}}_3)_2) = {self.actual_mass} \\text{{ g}}\\\\"
            "&\\text{Step 2: Calculate moles of ZnO.}\\\\"
            f"&\\quad M_r(\\text{{ZnO}}) = {self.mr_zno} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad n(\\text{{ZnO}}) = \\frac{{{self.mass_zno}}}{{{self.mr_zno}}} = {round(self.moles_zno, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 3: Use the 1:1 ratio to find moles of product.}\\\\"
            "&\\quad \\text{ZnO + 2HNO}_3 \\rightarrow \\text{Zn(NO}_3)_2 + \\text{H}_2\\text{O} \\implies 1:1 \\text{ ratio}\\\\"
            f"&\\quad n(\\text{{Zn(NO}}_3)_2) = {round(self.moles_product, 5)} \\text{{ mol}}\\\\"
            "&\\text{Step 4: Calculate the theoretical mass.}\\\\"
            f"&\\quad M_r(\\text{{Zn(NO}}_3)_2) = {self.mr_znno3_2} \\text{{ g mol}}^{{-1}}\\\\"
            f"&\\quad m_{{\\text{{theoretical}}}} = {round(self.moles_product, 5)} \\times {self.mr_znno3_2} = {round(self.theoretical_mass, 5)} \\text{{ g}}\\\\"
            "&\\text{Step 5: Calculate the percentage yield.}\\\\"
            "&\\quad \\% \\text{ yield} = \\frac{\\text{Actual mass}}{\\text{Theoretical mass}} \\times 100\\\\"
            f"&\\quad \\% \\text{{ yield}} = \\frac{{{self.actual_mass}}}{{{round(self.theoretical_mass, 5)}}} \\times 100 = {self.answer} \\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
            "The image shows a redox reaction equation.\n"
            "What is the oxidation number of the highlighted element?"
        )

        self.topic = "Redox"
        self.subtopic = "Oxidation numbers"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the species whose oxidation number is required.}\\\\"
            f"&\\quad \\text{{Species: }} {self.species}\\\\"
            "&\\text{Step 2: Determine the state of this species in the reaction.}\\\\"
            f"&\\quad {self.species} \\text{{ appears as a free, uncombined element on the left side of the equation.}}\\\\"
            "&\\text{Step 3: Apply the rule for free elements.}\\\\"
            "&\\quad \\text{The oxidation number of any element in its free state is always 0.}\\\\"
            f"&\\quad \\text{{Oxidation number of }} {self.species} = 0\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        highlight_width = 3.0
        highlight_height = 1.0

        highlight = Rectangle((6 - highlight_width/2, 2.5),
                            highlight_width,
                            highlight_height,
                            facecolor="gold",
                            edgecolor="black",
                            linewidth=2)
        ax.add_patch(highlight)

        ax.text(6, 3.0,
                f"{self.species}",
                ha='center',
                va='center',
                fontsize=14,
                fontweight='bold')

        ax.text(6, 2.0,
                "Find the oxidation number of this species.",
                ha='center',
                fontsize=11,
                style='italic')

        
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
            f"In the reaction the image\n"
            f"How many moles of {self.product} are formed from 1 mole of {self.reactant}?"
        )

        self.topic = "Stoichiometry"
        self.subtopic = "Mole ratio"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Write out the balanced equation and identify the mole coefficients.}\\\\"
            f"&\\quad \\text{{Equation: }} {self.equation}\\\\"
            "&\\text{Step 2: Identify the stoichiometric ratio from the equation.}\\\\"
            f"&\\quad {self.reactant_coeff} \\text{{ mol }} {self.reactant} \\rightarrow {self.product_coeff} \\text{{ mol }} {self.product}\\\\"
            "&\\text{Step 3: Scale the ratio to find the moles of product per 1 mole of reactant.}\\\\"
            f"&\\quad \\text{{From 1 mol }} {self.reactant}: \\quad \\frac{{{self.product_coeff}}}{{{self.reactant_coeff}}} = {self.product_coeff/self.reactant_coeff} \\text{{ mol }} {self.product}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem147:
    def __init__(self):

        variations = [
            (1,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 1, 2),
            (1,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    1, 2),
            (2,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 2, 4),
            (2,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    2, 4),
            (3,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 3, 6),
            (3,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    3, 6),
            (4,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 4, 8),
            (4,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    4, 8),
            (5,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 5, 10),
            (5,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    5, 10),
            (6,   "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 6, 12),
            (6,   "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    6, 12),
            (10,  "glucose", "ethanol",         "C₆H₁₂O₆", "C₂H₅OH", 10, 20),
            (10,  "glucose", "carbon dioxide",  "C₆H₁₂O₆", "CO₂",    10, 20),
        ]

        (
            self.given_amount,
            self.reactant_name,
            self.product_name,
            self.reactant_formula,
            self.product_formula,
            self.reactant_coeff,
            self.product_coeff,
        ) = rnd.choice(variations)

        # Fixed balanced equation (always the same reaction)
        self.equation = "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂"

        # Answer scales with given_amount: n glucose → 2n product molecules
        self.answer = self.product_coeff  # already scaled per variation

        self.description = (
            "Fermentation of glucose produces ethanol.\n"
            "Using the equation shown in the diagram, calculate:\n"
            f"How many molecules of {self.product_name} are formed from "
            f"{self.given_amount} molecule{'s' if self.given_amount > 1 else ''} of {self.reactant_name}?"
        )

        self.topic = "Organic chemistry"
        self.subtopic = "Fermentation stoichiometry"
        self.source = "Adapted from IGCSE Chemistry Past Papers"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Write out the balanced equation for fermentation.}\\\\"
            f"&\\quad \\text{{Equation: }} {self.equation}\\\\"
            "&\\text{Step 2: Read the stoichiometric ratio from the equation.}\\\\"
            f"&\\quad 1 \\text{{ molecule }} {self.reactant_formula} \\rightarrow 2 \\text{{ molecules }} {self.product_formula}\\\\"
            "&\\text{Step 3: Scale the ratio for the given number of reactant molecules.}\\\\"
            f"&\\quad {self.reactant_coeff} \\text{{ molecules }} {self.reactant_formula} \\rightarrow {self.reactant_coeff} \\times 2 = {self.answer} \\text{{ molecules }} {self.product_formula}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Write out the balanced equation shown in the diagram.}\\\\"
            f"&\\quad \\text{{Equation: }} {self.equation}\\\\"
            "&\\text{Step 2: Identify the stoichiometric ratio from the equation.}\\\\"
            f"&\\quad {self.reactant_coeff} \\text{{ mol }} {self.reactant_formula} \\rightarrow {self.product_coeff} \\text{{ mol }} {self.product_formula}\\\\"
            "&\\text{Step 3: Scale the ratio to find moles of product per 1 mole of reactant.}\\\\"
            f"&\\quad \\text{{From 1 mol }} {self.reactant_formula}: \\quad \\frac{{{self.product_coeff}}}{{{self.reactant_coeff}}} = {self.answer} \\text{{ mol }} {self.product_formula}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
            "An element has the electron configuration shown in the image.\n"
            "Determine its group number (IUPAC 1–18)."
        )

        self.topic = "Atomic structure"
        self.subtopic = "Electron configuration → group"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the electron configuration from the diagram.}\\\\"
            f"&\\quad \\text{{Configuration: }} {self.config}\\\\"
            "&\\text{Step 2: Identify the outermost (valence) shell and count electrons.}\\\\"
            "&\\quad \\text{The valence electrons are those in the highest energy sub-shells.}\\\\"
            f"&\\quad \\text{{Number of valence electrons}} = {self.valence}\\\\"
            "&\\text{Step 3: Determine the group number from the valence electron count.}\\\\"
            "&\\quad \\text{For main-group elements, group number equals valence electron count.}\\\\"
            f"&\\quad \\text{{Group number}} = {self.group}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹", 1),
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 4s²", 2),
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s²", 2),
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s¹", 1),
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 5s²", 2),
        ("1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", 2),
    ]

        self.config, self.lost = rnd.choice(variations)
        self.answer = self.lost

        self.description = (
            "An atom has the electron configuration shown on the image.\n"
            "When forming a stable ion, how many electrons are lost?"
        )

        self.topic = "Atomic structure"
        self.subtopic = "Ion formation"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Read the electron configuration from the diagram.}\\\\"
            f"&\\quad \\text{{Configuration: }} {self.config}\\\\"
            "&\\text{Step 2: Identify the outermost electrons (highest energy sub-shell).}\\\\"
            "&\\quad \\text{Metals lose their outermost electrons to achieve a full outer shell.}\\\\"
            "&\\text{Step 3: Count the electrons in the outermost sub-shell.}\\\\"
            f"&\\quad \\text{{Electrons in outermost sub-shell}} = {self.lost}\\\\"
            "&\\text{Step 4: State the number of electrons lost to form the stable ion.}\\\\"
            f"&\\quad \\text{{Electrons lost}} = {self.lost}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
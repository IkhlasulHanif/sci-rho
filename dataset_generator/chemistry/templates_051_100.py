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


class Chem051:
    """
    Topic: 27 Group 2
    Visual: Bar chart showing reactivity trend down Group 2 (x-axis labels removed)
    Task: Multiple question types about the chart - 6 q_types × 4 elements = 24 combinations
    """

    def __init__(self):
        elements = ["Mg", "Ca", "Sr", "Ba"]
        # Randomise bar heights while keeping strict increase
        base = [2, 4, 6, 9]
        reactivity_values = sorted([b + rnd.randint(0, 2) for b in base])
        labels = ["A", "B", "C", "D"]

        self.elements = elements
        self.values = reactivity_values

        idx = rnd.randint(0, 3)
        self.element = elements[idx]
        self.position = idx + 1
        correct_val = reactivity_values[idx]

        wrong_vals = [v for v in reactivity_values if v != correct_val]
        options = wrong_vals + [correct_val]
        options = [str(v) for v in options]
        rnd.shuffle(options)
        self.answer = labels[options.index(str(correct_val))]

        self.description = (
            f"The bar chart shows the relative reactivity of four Group 2 elements with water. "
            f"The elements are arranged in order of atomic number (position 1 to 4). "
            f"What is the reactivity value shown for the element at position {self.position}?"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Group 2 elements and reactivity values:}} &\\\\"
            f"\\text{{Mg = 3, Ca = 5, Sr = 7, Ba = 9}} &\\\\"
            f"\\therefore \\text{{{self.element} = {correct_val}}}"
            "\\end{aligned}\\]"
        )
        self._options = options

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self._options))
        self.topic = "Group 2"
        self.subtopic = "Trends in Group 2"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        x_positions = list(range(1, 5))
        position_labels = ["1", "2", "3", "4"]

        draw_bar_chart(ax, x_positions, self.values, position_labels,
                      colors='skyblue', width=0.6,
                      xlabel='Position (increasing atomic number)',
                      ylabel='Relative Reactivity with Water',
                      title='Reactivity of Group 2 Elements with Water')


        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()

class Chem052:
    """
    Topic: 28.1 General properties of transition elements
    Visual: Electron configuration diagram
    Task: Identify which element(s) are transition elements (MCQ)
    """

    def __init__(self):
        comparisons = [
            {
                'element1': 'Cu', 'element2': 'Zn',
                'config1': '[Ar] 3d\u00b9\u2070 4s\u00b9', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b2',
                'ion1': 'Cu\u00b2\u207a: [Ar] 3d\u2079', 'ion2': 'Zn\u00b2\u207a: [Ar] 3d\u00b9\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'Sc', 'element2': 'Ti',
                'config1': '[Ar] 3d\u00b9 4s\u00b2', 'config2': '[Ar] 3d\u00b2 4s\u00b2',
                'ion1': 'Sc\u00b3\u207a: [Ar] 3d\u2070', 'ion2': 'Ti\u00b3\u207a: [Ar] 3d\u00b9',
                'transition1': False, 'transition2': True,
            },
            {
                'element1': 'Fe', 'element2': 'Zn',
                'config1': '[Ar] 3d\u2076 4s\u00b2', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b2',
                'ion1': 'Fe\u00b2\u207a: [Ar] 3d\u2076', 'ion2': 'Zn\u00b2\u207a: [Ar] 3d\u00b9\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'Sc', 'element2': 'V',
                'config1': '[Ar] 3d\u00b9 4s\u00b2', 'config2': '[Ar] 3d\u00b3 4s\u00b2',
                'ion1': 'Sc\u00b3\u207a: [Ar] 3d\u2070', 'ion2': 'V\u00b3\u207a: [Ar] 3d\u00b2',
                'transition1': False, 'transition2': True,
            },
            {
                'element1': 'Mn', 'element2': 'Zn',
                'config1': '[Ar] 3d\u2075 4s\u00b2', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b2',
                'ion1': 'Mn\u00b2\u207a: [Ar] 3d\u2075', 'ion2': 'Zn\u00b2\u207a: [Ar] 3d\u00b9\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'Co', 'element2': 'Sc',
                'config1': '[Ar] 3d\u2077 4s\u00b2', 'config2': '[Ar] 3d\u00b9 4s\u00b2',
                'ion1': 'Co\u00b2\u207a: [Ar] 3d\u2077', 'ion2': 'Sc\u00b3\u207a: [Ar] 3d\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'Ni', 'element2': 'Cu',
                'config1': '[Ar] 3d\u2078 4s\u00b2', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b9',
                'ion1': 'Ni\u00b2\u207a: [Ar] 3d\u2078', 'ion2': 'Cu\u00b2\u207a: [Ar] 3d\u2079',
                'transition1': True, 'transition2': True,
            },
            {
                'element1': 'Cr', 'element2': 'Zn',
                'config1': '[Ar] 3d\u2075 4s\u00b9', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b2',
                'ion1': 'Cr\u00b3\u207a: [Ar] 3d\u00b3', 'ion2': 'Zn\u00b2\u207a: [Ar] 3d\u00b9\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'Ti', 'element2': 'Zn',
                'config1': '[Ar] 3d\u00b2 4s\u00b2', 'config2': '[Ar] 3d\u00b9\u2070 4s\u00b2',
                'ion1': 'Ti\u00b3\u207a: [Ar] 3d\u00b9', 'ion2': 'Zn\u00b2\u207a: [Ar] 3d\u00b9\u2070',
                'transition1': True, 'transition2': False,
            },
            {
                'element1': 'V', 'element2': 'Sc',
                'config1': '[Ar] 3d\u00b3 4s\u00b2', 'config2': '[Ar] 3d\u00b9 4s\u00b2',
                'ion1': 'V\u00b3\u207a: [Ar] 3d\u00b2', 'ion2': 'Sc\u00b3\u207a: [Ar] 3d\u2070',
                'transition1': True, 'transition2': False,
            },
        ]

        self.comp = rnd.choice(comparisons)
        e1, e2 = self.comp['element1'], self.comp['element2']
        t1, t2 = self.comp['transition1'], self.comp['transition2']

        # Build MCQ options
        options_map = {
            (True, False):  (f"{e1} only",),
            (False, True):  (f"{e2} only",),
            (True, True):   (f"Both {e1} and {e2}",),
            (False, False): ("Neither",),
        }
        correct_text = options_map[(t1, t2)][0]

        # Build 4 options
        all_opts = [
            f"{e1} only",
            f"{e2} only",
            f"Both {e1} and {e2}",
            "Neither"
        ]
        rnd.shuffle(all_opts)
        self.choices = all_opts[:4]
        if correct_text not in self.choices:
            self.choices[0] = correct_text
            rnd.shuffle(self.choices)

        labels = ["A", "B", "C", "D"]
        self.answer = labels[self.choices.index(correct_text)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, self.choices)}

        self.description = (
            f"Using the definition 'a transition element forms one or more stable ions with incomplete d orbitals', "
            f"which of the following is/are transition element(s)? "
            f"The electron configurations of {e1} and {e2} are shown in the diagram."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.1 General physical and chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{e1}: {self.comp['ion1']} - incomplete d: {t1}}} &\\\\"
            f"\\text{{{e2}: {self.comp['ion2']} - incomplete d: {t2}}} &\\\\"
            f"\\text{{Answer: {correct_text}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 6, 7.5, "Transition Element Definition", fontsize=16)

        y_pos = 5.5
        add_formula_label(ax, 2, y_pos, f"{self.comp['element1']} atom:", fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos, self.comp['config1'], fontsize=13,
                         bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.5))

        add_formula_label(ax, 2, y_pos - 0.8, f"{self.comp['ion1'].split(':')[0]}:",
                         fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos - 0.8, self.comp['ion1'].split(': ')[1],
                         fontsize=13, bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))

        y_pos = 3.5
        add_formula_label(ax, 2, y_pos, f"{self.comp['element2']} atom:", fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos, self.comp['config2'], fontsize=13,
                         bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.5))

        add_formula_label(ax, 2, y_pos - 0.8, f"{self.comp['ion2'].split(':')[0]}:",
                         fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos - 0.8, self.comp['ion2'].split(': ')[1],
                         fontsize=13, bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))

        definition = "Transition element:\nForms one or more stable ions\nwith incomplete d orbitals"
        ax.text(9, 4, definition, fontsize=12, ha='center', va='center',
               bbox=dict(boxstyle='round', facecolor='lightgreen',
                        edgecolor='black', linewidth=2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem053:
    """
    Topic: 28.1 General properties of transition elements
    Visual: Colored test tubes WITHOUT oxidation state labels
    Task: Identify oxidation state from color (MCQ)
    """

    def __init__(self):
        metals = {
            "Fe": [("+2", "pale green"), ("+3", "yellow-brown")],
            "Cu": [("+1", "white"), ("+2", "blue")],
            "Mn": [("+2", "pale pink"), ("+4", "brown"), ("+7", "purple")],
            "Cr": [("+3", "green"), ("+6", "orange")],
            "V": [("+2", "violet"), ("+3", "green"), ("+4", "blue"), ("+5", "yellow")],
            "Co": [("+2", "pink"), ("+3", "dark green")],
            "Ni": [("+2", "green")],
            "Ti": [("+3", "purple"), ("+4", "colorless")],
        }

        # Pick a metal with at least 2 states
        metal_choices = [m for m in metals if len(metals[m]) >= 2]
        self.metal = rnd.choice(metal_choices)
        self.oxidation_states = metals[self.metal]

        selected_state = rnd.choice(self.oxidation_states)
        self.shown_color = selected_state[1]
        correct_ox = selected_state[0]

        # Build MCQ - use all oxidation states of this metal as distractors
        all_states = [s[0] for s in self.oxidation_states]
        # Add some plausible wrong answers from other metals if needed
        extra = ["+1", "+2", "+3", "+4", "+5", "+6", "+7"]
        for e in extra:
            if e not in all_states:
                all_states.append(e)
            if len(all_states) >= 4:
                break

        options = rnd.sample([s for s in all_states if s != correct_ox], 3)
        options.append(correct_ox)
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct_ox)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows test tubes containing {self.metal} compounds at different oxidation states. "
            f"The test tubes are shown without colour labels. "
            f"What is the oxidation state of {self.metal} in the highlighted test tube?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "General properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The {self.shown_color} compound contains {self.metal} in oxidation state {correct_ox}}} &"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        color_map = {
            "pale green": "lightgreen", "yellow-brown": "goldenrod",
            "white": "whitesmoke", "blue": "lightblue",
            "pale pink": "lightpink", "brown": "saddlebrown",
            "purple": "mediumpurple", "green": "limegreen",
            "orange": "orange", "violet": "violet",
            "dark green": "darkgreen", "pink": "pink",
            "yellow": "yellow", "colorless": "aliceblue",
        }

        x_start = 2
        spacing = 3

        selected_idx = next(i for i,(ox,col) in enumerate(self.oxidation_states)
                              if col == self.shown_color)
        for i, (ox_state, color) in enumerate(self.oxidation_states):
            x = x_start + i * spacing
            draw_test_tube(ax, x, 1, width=1, height=3.5, solution_height=2.5,
                          solution_color=color_map.get(color, 'lightgray'))
            if i == selected_idx:
                ax.annotate("?", xy=(x + 0.5, 4.6), xytext=(x + 0.5, 5.3),
                            fontsize=16, fontweight='bold', color='red', ha='center',
                            arrowprops=dict(arrowstyle='->', color='red', lw=2))

        add_title_box(ax, 6, 5.5, f"Compounds of {self.metal}", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem054:
    """
    Topic: 28.2 Ligands and complex formation
    Visual: Diagram of octahedral, tetrahedral, or square planar complex
    Task: Determine coordination number from structure (numerical answer)
    10+ variations
    """

    def __init__(self):
        complexes = [
            ("[Cu(H\u2082O)\u2086]\u00b2\u207a", 6, "octahedral", 6),
            ("[Fe(CN)\u2086]\u00b3\u207b", 6, "octahedral", 6),
            ("[Co(NH\u2083)\u2086]\u00b3\u207a", 6, "octahedral", 6),
            ("[Ni(H\u2082O)\u2086]\u00b2\u207a", 6, "octahedral", 6),
            ("[CoCl\u2084]\u00b2\u207b", 4, "tetrahedral", 4),
            ("[CuCl\u2084]\u00b2\u207b", 4, "tetrahedral", 4),
            ("[Zn(NH\u2083)\u2084]\u00b2\u207a", 4, "tetrahedral", 4),
            ("[Ni(CN)\u2084]\u00b2\u207b", 4, "square planar", 4),
            ("[Pt(NH\u2083)\u2084]\u00b2\u207a", 4, "square planar", 4),
            ("[Ag(NH\u2083)\u2082]\u207a", 2, "linear", 2),
            ("[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a", 6, "octahedral", 6),
            ("[Fe(H\u2082O)\u2086]\u00b3\u207a", 6, "octahedral", 6),
            ("[Cr(H\u2082O)\u2086]\u00b3\u207a", 6, "octahedral", 6),
            ("[Mn(H\u2082O)\u2086]\u00b2\u207a", 6, "octahedral", 6),
        ]

        self.complex_data = rnd.choice(complexes)
        self.formula = self.complex_data[0]
        self.coordination_number = self.complex_data[1]
        self.shape = self.complex_data[2]

        self.answer = self.coordination_number

        self.description = (
            f"The diagram shows the structure of a transition metal complex ion. "
            f"What is the coordination number of the central metal ion?"
        )

        self.topic = "Chemistry of transition elements"
        self.subtopic = "Ligands and complex formation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Coordination number}} &= \\text{{number of ligands bonded to central metal}}\\\\"
            f"&= {self.coordination_number}\\\\"
            f"\\text{{Shape: {self.shape}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.axis('off')
        ax.set_aspect('equal')

        draw_circle_atom(ax, 0, 0, "M", radius=0.3, color='orange',
                        edgecolor='black', linewidth=2, fontsize=18)

        if self.coordination_number == 6:
            positions = [
                (0.8, 0), (-0.8, 0), (0, 0.8), (0, -0.8),
                (0.6, 0.6), (-0.6, -0.6)
            ]
        elif self.coordination_number == 4 and self.shape == "square planar":
            positions = [(0.8, 0), (-0.8, 0), (0, 0.8), (0, -0.8)]
        elif self.coordination_number == 4:
            positions = [(0.7, 0.7), (-0.7, 0.7), (0.7, -0.7), (-0.7, -0.7)]
        else:  # linear, 2
            positions = [(0.9, 0), (-0.9, 0)]

        for x, y in positions:
            draw_bond(ax, 0, 0, x, y, bond_type='dashed', linewidth=2)
            draw_circle_atom(ax, x, y, "L", radius=0.2, color='lightblue', fontsize=12)

        add_title_box(ax, 0, 1.8, self.formula, fontsize=16)
        add_formula_label(ax, 0, -1.8, f"Shape: {self.shape}", fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem055:
    """
    Topic: 28.2 Ligands and complex formation - Ligand exchange
    Visual: Two test tubes with initial complex color and arrow (product NOT shown)
    Task: MCQ - predict formula and color of product
    10+ variations
    """

    def __init__(self):
        complexes = [
            {
                'metal': 'Cu\u00b2\u207a',
                'initial_complex': '[Cu(H\u2082O)\u2086]\u00b2\u207a',
                'initial_color': 'pale blue',
                'initial_color_hex': '#ADD8E6',
                'final_complex': '[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a',
                'final_color': 'deep blue',
                'ligand': 'NH\u2083(aq)',
                'ligand_name': 'ammonia',
            },
            {
                'metal': 'Cu\u00b2\u207a',
                'initial_complex': '[Cu(H\u2082O)\u2086]\u00b2\u207a',
                'initial_color': 'pale blue',
                'initial_color_hex': '#ADD8E6',
                'final_complex': '[CuCl\u2084]\u00b2\u207b',
                'final_color': 'yellow-green',
                'ligand': 'Cl\u207b(aq)',
                'ligand_name': 'chloride ions',
            },
            {
                'metal': 'Co\u00b2\u207a',
                'initial_complex': '[Co(H\u2082O)\u2086]\u00b2\u207a',
                'initial_color': 'pink',
                'initial_color_hex': '#FFC0CB',
                'final_complex': '[CoCl\u2084]\u00b2\u207b',
                'final_color': 'blue',
                'ligand': 'Cl\u207b(aq)',
                'ligand_name': 'chloride ions',
            },
            {
                'metal': 'Fe\u00b3\u207a',
                'initial_complex': '[Fe(H\u2082O)\u2086]\u00b3\u207a',
                'initial_color': 'yellow-brown',
                'initial_color_hex': '#DAA520',
                'final_complex': '[Fe(SCN)(H\u2082O)\u2085]\u00b2\u207a',
                'final_color': 'blood red',
                'ligand': 'SCN\u207b(aq)',
                'ligand_name': 'thiocyanate',
            },
            {
                'metal': 'Ni\u00b2\u207a',
                'initial_complex': '[Ni(H\u2082O)\u2086]\u00b2\u207a',
                'initial_color': 'pale green',
                'initial_color_hex': '#90EE90',
                'final_complex': '[Ni(NH\u2083)\u2086]\u00b2\u207a',
                'final_color': 'violet',
                'ligand': 'NH\u2083(aq)',
                'ligand_name': 'ammonia',
            },
            {
                'metal': 'Cr\u00b3\u207a',
                'initial_complex': '[Cr(H\u2082O)\u2086]\u00b3\u207a',
                'initial_color': 'violet',
                'initial_color_hex': '#EE82EE',
                'final_complex': '[Cr(NH\u2083)\u2086]\u00b3\u207a',
                'final_color': 'yellow',
                'ligand': 'NH\u2083(aq)',
                'ligand_name': 'ammonia',
            },
            {
                'metal': 'Fe\u00b3\u207a',
                'initial_complex': '[Fe(H\u2082O)\u2086]\u00b3\u207a',
                'initial_color': 'yellow-brown',
                'initial_color_hex': '#DAA520',
                'final_complex': '[FeCl\u2084]\u207b',
                'final_color': 'yellow',
                'ligand': 'Cl\u207b(aq)',
                'ligand_name': 'chloride ions',
            },
            {
                'metal': 'Mn\u00b2\u207a',
                'initial_complex': '[Mn(H\u2082O)\u2086]\u00b2\u207a',
                'initial_color': 'pale pink',
                'initial_color_hex': '#FFB6C1',
                'final_complex': '[Mn(EDTA)]\u00b2\u207b',
                'final_color': 'pale pink',
                'ligand': 'EDTA\u2074\u207b',
                'ligand_name': 'EDTA',
            },
            {
                'metal': 'Cu\u00b2\u207a',
                'initial_complex': '[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a',
                'initial_color': 'deep blue',
                'initial_color_hex': '#00008B',
                'final_complex': '[Cu(EDTA)]\u00b2\u207b',
                'final_color': 'blue',
                'ligand': 'EDTA\u2074\u207b',
                'ligand_name': 'EDTA',
            },
            {
                'metal': 'Co\u00b2\u207a',
                'initial_complex': '[Co(NH\u2083)\u2086]\u00b2\u207a',
                'initial_color': 'yellow',
                'initial_color_hex': '#FFFF00',
                'final_complex': '[Co(H\u2082O)\u2086]\u00b2\u207a',
                'final_color': 'pink',
                'ligand': 'H\u2082O(l)',
                'ligand_name': 'water (excess)',
            },
        ]

        self.reaction = rnd.choice(complexes)

        # Build MCQ with formula as option
        correct = self.reaction['final_complex']
        all_formulas = [r['final_complex'] for r in complexes]
        wrong_opts = [f for f in all_formulas if f != correct]
        options = rnd.sample(wrong_opts, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a ligand exchange reaction. "
            f"The starting complex and the ligand being added are shown. "
            f"What is the formula of the final complex ion?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.2 Characteristic chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Ligand exchange reaction:}} &\\\\"
            f"\\text{{{self.reaction['initial_complex']} + excess {self.reaction['ligand']}}} "
            f"&\\rightarrow \\text{{{correct}}}\\\\"
            f"\\text{{Color changes: {self.reaction['initial_color']} to {self.reaction['final_color']}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Ligand Exchange Reaction", fontsize=16)

        draw_test_tube(ax, 1.5, 1.5, width=1.5, height=3.5, solution_height=2.5,
                      solution_color=self.reaction['initial_color_hex'])
        add_formula_label(ax, 2.25, 0.8, self.reaction['initial_complex'], fontsize=11)
        add_formula_label(ax, 2.25, 0.3, self.reaction['initial_color'], fontsize=10, color='blue')

        draw_arrow(ax, 3.5, 3.5, 5.5, 3.5, label=f"+ excess {self.reaction['ligand']}",
                  label_position='above', color='black', linewidth=3)

        draw_test_tube(ax, 9, 1.5, width=1.5, height=3.5, solution_height=2.5,
                      solution_color='lightgray')
        add_formula_label(ax, 9.75, 0.8, "?", fontsize=20, weight='bold', color='red')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem056:
    """
    Topic: 28.3 Ligand substitution reactions
    Visual: Initial test tube only; product test tube is blank
    Task: MCQ - predict the color of the product solution
    """

    def __init__(self):
        reactions = [
            ("[Cu(H\u2082O)\u2086]\u00b2\u207a", "#ADD8E6", "blue", "[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a", "deep blue", "excess NH\u2083(aq)"),
            ("[Fe(H\u2082O)\u2086]\u00b3\u207a", "#DAA520", "yellow-brown", "[Fe(SCN)(H\u2082O)\u2085]\u00b2\u207a", "blood red", "SCN\u207b(aq)"),
            ("[Co(H\u2082O)\u2086]\u00b2\u207a", "#FFC0CB", "pink", "[CoCl\u2084]\u00b2\u207b", "blue", "excess Cl\u207b(aq)"),
            ("[Ni(H\u2082O)\u2086]\u00b2\u207a", "#90EE90", "pale green", "[Ni(NH\u2083)\u2086]\u00b2\u207a", "violet", "excess NH\u2083(aq)"),
            ("[Cr(H\u2082O)\u2086]\u00b3\u207a", "#EE82EE", "violet", "[Cr(NH\u2083)\u2086]\u00b3\u207a", "yellow", "excess NH\u2083(aq)"),
            ("[Cu(H\u2082O)\u2086]\u00b2\u207a", "#ADD8E6", "pale blue", "[CuCl\u2084]\u00b2\u207b", "yellow-green", "excess Cl\u207b(aq)"),
            ("[Fe(H\u2082O)\u2086]\u00b2\u207a", "#90EE90", "pale green", "[Fe(CN)\u2086]\u2074\u207b", "yellow", "CN\u207b(aq)"),
            ("[Mn(H\u2082O)\u2086]\u00b2\u207a", "#FFB6C1", "pale pink", "[Mn(EDTA)]\u00b2\u207b", "pale pink", "EDTA\u2074\u207b"),
            ("[Co(H\u2082O)\u2086]\u00b2\u207a", "#FFC0CB", "pink", "[Co(NH\u2083)\u2086]\u00b3\u207a", "yellow", "excess NH\u2083(aq)"),
            ("[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a", "#00008B", "deep blue", "[Cu(EDTA)]\u00b2\u207b", "blue", "EDTA\u2074\u207b"),
        ]

        self.reaction = rnd.choice(reactions)
        (self.reactant, self.color1_hex, self.color1, self.product,
         self.color2, self.ligand) = self.reaction

        # MCQ based on color
        all_colors = ["deep blue", "blood red", "blue", "violet", "yellow",
                      "yellow-green", "pale green", "pink", "pale pink", "pale blue", "colorless"]
        correct = self.color2
        wrong = [c for c in all_colors if c != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a ligand substitution reaction where {self.ligand} is added "
            f"to a complex ion. The starting solution colour is shown in the left test tube. "
            f"What colour will the resulting solution be?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Ligand substitution"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Ligand substitution:}} &\\\\"
            f"\\text{{{self.reactant}}} &\\rightarrow \\text{{{self.product}}}\\\\"
            f"\\text{{Color: {self.color1}}} &\\rightarrow \\text{{{self.color2}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        color_map = {
            "blue": "lightblue", "deep blue": "dodgerblue",
            "yellow": "yellow", "blood red": "darkred",
            "pink": "lightpink", "pale green": "lightgreen",
            "violet": "mediumpurple", "yellow-green": "yellowgreen",
            "pale blue": "#ADD8E6", "pale pink": "#FFB6C1",
            "colorless": "white",
        }

        draw_test_tube(ax, 2, 1, width=1.2, height=3.5, solution_height=2.5,
                      solution_color=self.color1_hex)
        add_formula_label(ax, 2.6, 0.3, self.reactant, fontsize=10)

        draw_arrow(ax, 4, 3, 8, 3, label=f"+ {self.ligand}", label_position='above',
                  color='black', linewidth=2.5)

        draw_test_tube(ax, 9, 1, width=1.2, height=3.5, solution_height=2.5,
                      solution_color='lightgray')
        add_formula_label(ax, 9.6, 0.3, "?", fontsize=16, weight='bold', color='red')

        add_title_box(ax, 6, 5.5, "Ligand Substitution", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem057:
    """
    Topic: 28.3 Ligand substitution - colour of complexes
    Visual: d-orbital splitting diagram with ΔE labelled
    Task: Calculate wavelength of light absorbed (numerical answer in nm)
    Expanded to 10+ variations
    """

    def __init__(self):
        h = 6.626e-34
        c = 3.00e8
        Na = 6.022e23
        self.delta_E = rnd.choice(range(130, 410, 10))
        lambda_m = h * c * Na / (self.delta_E * 1000)
        self.wavelength = round(lambda_m * 1e9)

        self.answer = self.wavelength

        self.description = (
            f"The d-orbital splitting diagram shows a transition metal complex. "
            f"The value of \u0394E is annotated on the diagram. "
            f"Calculate the wavelength (in nm) of light absorbed by this complex. "
            f"(Given: h = 6.626\u00d710\u207b\u00b3\u2074 J\u00b7s, c = 3.00\u00d710\u2078 m/s, N\u2090 = 6.022\u00d710\u00b2\u00b3 mol\u207b\u00b9)"
        )

        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.3 Colour of complexes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\Delta E &= {self.delta_E}\\text{{ kJ/mol}}\\\\"
            "E &= \\frac{hc}{\\lambda}\\\\"
            "\\lambda &= \\frac{hc \\times N_A}{\\Delta E}\\\\"
            f"&= \\frac{{6.626 \\times 10^{{-34}} \\times 3.00 \\times 10^8 \\times 6.022 \\times 10^{{23}}}}{{{self.delta_E} \\times 10^3}}\\\\"
            f"&\\approx {self.wavelength} \\times 10^{{-9}}\\text{{ m}}\\\\"
            f"&= {self.wavelength}\\text{{ nm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 5, 7.5, "d-Orbital Splitting Diagram", fontsize=16)

        y_lower = 2.5
        for i, label in enumerate(['dxy', 'dyz', 'dxz']):
            line_x = 2 + i * 0.8
            ax.plot([line_x, line_x + 0.6], [y_lower, y_lower], 'b-', linewidth=3)
            ax.text(line_x + 0.3, y_lower - 0.3, label, fontsize=10, ha='center')

        y_higher = 4.5
        for i, label in enumerate(['dz\u00b2', 'dx\u00b2-y\u00b2']):
            line_x = 3 + i * 1.2
            ax.plot([line_x, line_x + 0.6], [y_higher, y_higher], 'r-', linewidth=3)
            ax.text(line_x + 0.3, y_higher + 0.3, label, fontsize=10, ha='center')

        draw_vertical_annotation(ax, 6.5, y_lower, y_higher, f"\u0394E = {self.delta_E} kJ/mol",
                                color='purple', linewidth=2.5, fontsize=12)

        ax.text(0.5, 3.5, 'Energy', fontsize=14, fontweight='bold', rotation=90, ha='center')

        calc_text = f"\u03bb = hc\u00d7N\u2090/\u0394E\n\u03bb = ? nm"
        ax.text(5, 1, calc_text, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black', linewidth=2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem058:
    """
    Topic: 28.5 Redox reactions and catalysis
    Visual: Catalytic cycle diagram WITHOUT oxidation state labels
    Task: MCQ - what oxidation states does the catalyst cycle between?
    """

    def __init__(self):
        catalysts = [
            ("Fe\u00b2\u207a", "+2", "Fe\u00b3\u207a", "+3", "Fe"),
            ("V\u00b3\u207a", "+3", "V\u2074\u207a", "+4", "V"),
            ("Cu\u207a", "+1", "Cu\u00b2\u207a", "+2", "Cu"),
            ("Mn\u00b2\u207a", "+2", "Mn\u00b3\u207a", "+3", "Mn"),
            ("Ce\u00b3\u207a", "+3", "Ce\u2074\u207a", "+4", "Ce"),
            ("Co\u00b2\u207a", "+2", "Co\u00b3\u207a", "+3", "Co"),
            ("Fe\u00b2\u207a", "+2", "Fe\u2074\u207a", "+4", "Fe"),
            ("Cr\u00b3\u207a", "+3", "Cr\u2076\u207a", "+6", "Cr"),
            ("V\u00b2\u207a", "+2", "V\u00b3\u207a", "+3", "V"),
            ("Mn\u00b4\u207a", "+4", "Mn\u2077\u207a", "+7", "Mn"),
        ]

        self.catalyst = rnd.choice(catalysts)
        self.species1, self.ox1, self.species2, self.ox2, self.element = self.catalyst

        correct = f"{self.ox1} and {self.ox2}"

        # Build MCQ
        all_ox = ["+1", "+2", "+3", "+4", "+5", "+6", "+7"]
        wrong_pairs = []
        for a in all_ox:
            for b in all_ox:
                if a != b and f"{a} and {b}" != correct and f"{b} and {a}" != correct:
                    wrong_pairs.append(f"{a} and {b}")

        options = rnd.sample(wrong_pairs, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a catalytic cycle involving a {self.element} compound. "
            f"Between which two oxidation states does the catalyst cycle?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Redox and catalysis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Oxidation:}} &\\quad {self.species1} \\rightarrow {self.species2}\\\\"
            f"\\text{{Reduction:}} &\\quad {self.species2} \\rightarrow {self.species1}\\\\"
            f"\\text{{Oxidation states: {self.ox1} \\rightleftharpoons {self.ox2}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        draw_labeled_box(ax, 1, 5, 3, 1.2, self.species1, facecolor='lightblue')
        draw_labeled_box(ax, 6, 5, 3, 1.2, self.species2, facecolor='lightcoral')

        draw_arrow(ax, 4, 5.6, 6, 5.6, label="Oxidation",
                  label_position='above', color='red', linewidth=2.5)
        draw_arrow(ax, 6, 5.4, 4, 5.4, label="Reduction",
                  label_position='below', color='blue', linewidth=2.5)

        add_title_box(ax, 5, 7.5, "Catalytic Cycle", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem059:
    """
    Topic: 28.5 Ligand exchange feasibility using Kstab
    Visual: Two complex boxes with Kstab values shown
    Task: MCQ - is the ligand exchange feasible? (A=Yes, B=No)
    Expanded to 10+ variations
    """

    def __init__(self):
        exchanges = [
            {
                'initial': '[Cu(H\u2082O)\u2086]\u00b2\u207a',
                'final': '[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a',
                'ligand': 'NH\u2083',
                'Kstab_initial': '1.0\u00d710\u00b9',
                'Kstab_final': '1.2\u00d710\u00b9\u00b3',
                'feasible': True,
            },
            {
                'initial': '[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a',
                'final': '[Cu(EDTA)]\u00b2\u207b',
                'ligand': 'EDTA\u2074\u207b',
                'Kstab_initial': '1.2\u00d710\u00b9\u00b3',
                'Kstab_final': '6.3\u00d710\u00b9\u2078',
                'feasible': True,
            },
            {
                'initial': '[Fe(H\u2082O)\u2086]\u00b3\u207a',
                'final': '[Fe(CN)\u2086]\u00b3\u207b',
                'ligand': 'CN\u207b',
                'Kstab_initial': '1.0\u00d710\u00b3',
                'Kstab_final': '1.0\u00d710\u2074\u00b2',
                'feasible': True,
            },
            {
                'initial': '[Ni(H\u2082O)\u2086]\u00b2\u207a',
                'final': '[Ni(EDTA)]\u00b2\u207b',
                'ligand': 'EDTA\u2074\u207b',
                'Kstab_initial': '1.0\u00d710\u00b2',
                'Kstab_final': '3.6\u00d710\u00b9\u2078',
                'feasible': True,
            },
            {
                'initial': '[Cu(EDTA)]\u00b2\u207b',
                'final': '[Cu(H\u2082O)\u2086]\u00b2\u207a',
                'ligand': 'H\u2082O',
                'Kstab_initial': '6.3\u00d710\u00b9\u2078',
                'Kstab_final': '1.0\u00d710\u00b9',
                'feasible': False,
            },
            {
                'initial': '[Fe(CN)\u2086]\u00b3\u207b',
                'final': '[Fe(H\u2082O)\u2086]\u00b3\u207a',
                'ligand': 'H\u2082O',
                'Kstab_initial': '1.0\u00d710\u2074\u00b2',
                'Kstab_final': '1.0\u00d710\u00b3',
                'feasible': False,
            },
            {
                'initial': '[Co(H\u2082O)\u2086]\u00b2\u207a',
                'final': '[Co(EDTA)]\u00b2\u207b',
                'ligand': 'EDTA\u2074\u207b',
                'Kstab_initial': '1.0\u00d710\u00b2',
                'Kstab_final': '2.0\u00d710\u00b9\u2076',
                'feasible': True,
            },
            {
                'initial': '[Cr(H\u2082O)\u2086]\u00b3\u207a',
                'final': '[Cr(EDTA)]\u207b',
                'ligand': 'EDTA\u2074\u207b',
                'Kstab_initial': '1.0\u00d710\u00b2',
                'Kstab_final': '1.0\u00d710\u00b2\u00b9',
                'feasible': True,
            },
            {
                'initial': '[Mn(H\u2082O)\u2086]\u00b2\u207a',
                'final': '[Mn(EDTA)]\u00b2\u207b',
                'ligand': 'EDTA\u2074\u207b',
                'Kstab_initial': '1.0\u00d710\u00b9',
                'Kstab_final': '6.3\u00d710\u00b9\u00b3',
                'feasible': True,
            },
            {
                'initial': '[Ni(EDTA)]\u00b2\u207b',
                'final': '[Ni(H\u2082O)\u2086]\u00b2\u207a',
                'ligand': 'H\u2082O',
                'Kstab_initial': '3.6\u00d710\u00b9\u2078',
                'Kstab_final': '1.0\u00d710\u00b2',
                'feasible': False,
            },
        ]

        self.exchange = rnd.choice(exchanges)
        correct = "Yes" if self.exchange['feasible'] else "No"
        options = ["Yes", "No",
                   "Cannot be determined from Kstab",
                   "Only at high temperature"]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows two complex ions and their stability constants (Kstab). "
            f"Is the ligand exchange shown feasible when {self.exchange['ligand']} is added?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.5 Stability constants"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"K_{{stab}}\\text{{(initial)}} &= {self.exchange['Kstab_initial']}\\\\"
            f"K_{{stab}}\\text{{(final)}} &= {self.exchange['Kstab_final']}\\\\"
            f"\\text{{Feasible if }} K_{{stab}}\\text{{(final)}} > K_{{stab}}\\text{{(initial)}}\\\\"
            f"\\text{{Answer: {correct}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Ligand Exchange Feasibility", fontsize=16)

        draw_labeled_box(ax, 0.5, 3.5, 4, 1.5, self.exchange['initial'],
                        f"Kstab = {self.exchange['Kstab_initial']}",
                        facecolor='lightblue')

        draw_arrow(ax, 4.7, 4.3, 7, 4.3, label=f"+ {self.exchange['ligand']}",
                  label_position='above', color='black', linewidth=3)

        draw_labeled_box(ax, 7.5, 3.5, 4, 1.5, self.exchange['final'],
                        f"Kstab = {self.exchange['Kstab_final']}",
                        facecolor='lightgreen')


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem060:
    """
    Topic: 29.1 Hydrocarbons nomenclature
    Visual: Structural formula of branched alkane
    Task: MCQ - name the compound using IUPAC nomenclature
    10+ variations
    """

    def __init__(self):
        structures = [
            ("2-methylpropane", "CH\u2083-CH(CH\u2083)-CH\u2083"),
            ("2-methylbutane", "CH\u2083-CH(CH\u2083)-CH\u2082-CH\u2083"),
            ("2,2-dimethylpropane", "C(CH\u2083)\u2084"),
            ("3-methylpentane", "CH\u2083-CH\u2082-CH(CH\u2083)-CH\u2082-CH\u2083"),
            ("2,3-dimethylbutane", "CH\u2083-CH(CH\u2083)-CH(CH\u2083)-CH\u2083"),
            ("2-methylpentane", "CH\u2083-CH(CH\u2083)-CH\u2082-CH\u2082-CH\u2083"),
            ("3-methylhexane", "CH\u2083-CH\u2082-CH(CH\u2083)-CH\u2082-CH\u2082-CH\u2083"),
            ("2,2-dimethylbutane", "CH\u2083-C(CH\u2083)\u2082-CH\u2082-CH\u2083"),
            ("2,4-dimethylpentane", "CH\u2083-CH(CH\u2083)-CH\u2082-CH(CH\u2083)-CH\u2083"),
            ("2,2,3-trimethylbutane", "CH\u2083-C(CH\u2083)\u2082-CH(CH\u2083)-CH\u2083"),
            ("4-methylheptane", "CH\u2083CH\u2082CH\u2082CH(CH\u2083)CH\u2082CH\u2082CH\u2083"),
            ("2,3-dimethylpentane", "CH\u2083-CH(CH\u2083)-CH(CH\u2083)-CH\u2082-CH\u2083"),
        ]

        self.compound = rnd.choice(structures)
        self.name = self.compound[0]
        self.formula = self.compound[1]

        # Build MCQ
        all_names = [s[0] for s in structures]
        wrong = [n for n in all_names if n != self.name]
        options = rnd.sample(wrong, 3) + [self.name]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(self.name)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"Name the alkane shown in the structural formula using IUPAC nomenclature."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Nomenclature"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Following IUPAC rules:}} &\\\\"
            f"\\text{{1. Find longest carbon chain}} &\\\\"
            f"\\text{{2. Number to give substituents lowest numbers}} &\\\\"
            f"\\text{{3. Name: {self.name}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis('off')

        add_title_box(ax, 5, 5.5, "Structural Formula", fontsize=16)

        add_formula_label(ax, 5, 3, self.formula, fontsize=18, weight='bold',
                         bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=1))

        add_formula_label(ax, 5, 1, "Name this compound using IUPAC nomenclature", fontsize=13)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem061:
    """
    Topic: 29.4 Isomerism - structural isomers
    Visual: Shows isomers (structures only, NO count label)
    Task: Count number of structural isomers (numerical answer)
    10+ variations
    """

    def __init__(self):
        formulas = [
            ("C\u2084H\u2081\u2080", 2, ["butane", "2-methylpropane"]),
            ("C\u2085H\u2081\u2082", 3, ["pentane", "2-methylbutane", "2,2-dimethylpropane"]),
            ("C\u2084H\u2088", 4, ["but-1-ene", "but-2-ene", "2-methylpropene", "cyclobutane"]),
            ("C\u2083H\u2087Cl", 2, ["1-chloropropane", "2-chloropropane"]),
            ("C\u2084H\u2089Cl", 4, ["1-chlorobutane", "2-chlorobutane", "1-chloro-2-methylpropane", "2-chloro-2-methylpropane"]),
            ("C\u2083H\u2086O", 3, ["propanal", "propan-2-one (acetone)", "methoxyethane"]),
            ("C\u2082H\u2086O", 2, ["ethanol", "methoxymethane"]),
            ("C\u2083H\u2088O", 3, ["propan-1-ol", "propan-2-ol", "methoxymethane"]),
            ("C\u2084H\u2089Br", 4, ["1-bromobutane", "2-bromobutane", "1-bromo-2-methylpropane", "2-bromo-2-methylpropane"]),
            ("C\u2085H\u2081\u2080", 5, ["pent-1-ene", "pent-2-ene", "2-methylbut-1-ene", "2-methylbut-2-ene", "3-methylbut-1-ene"]),
            ("C\u2086H\u2081\u2084", 5, ["hexane", "2-methylpentane", "3-methylpentane", "2,2-dimethylbutane", "2,3-dimethylbutane"]),
        ]

        self.compound = rnd.choice(formulas)
        self.formula = self.compound[0]
        self.num_isomers = self.compound[1]
        self.isomer_names = self.compound[2]

        self.answer = self.num_isomers

        self.description = (
            f"The diagram shows structural isomers with the molecular formula {self.formula}. "
            f"How many structural isomers does {self.formula} have?"
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The structural isomers of {self.formula} are:}} &\\\\"
            + "\\\\".join([f"\\text{{{i+1}. {name}}}" for i, name in enumerate(self.isomer_names)]) + "\\\\"
            + f"\\text{{Total}} &= {self.answer}"
            + "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 5, 7.5, f"Structural Isomers of {self.formula}", fontsize=16)

        y_pos = 6.5
        for i, name in enumerate(self.isomer_names):
            add_formula_label(ax, 5, y_pos, f"{i+1}. {name}", fontsize=13,
                            bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.4))
            y_pos -= 1.2

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem062:
    """
    Topic: 29.4 Geometric isomerism
    Visual: E/Z isomer diagram - title shows base name only (not E or Z)
    Task: MCQ - is the shown isomer E or Z?
    10+ variations with more compounds
    """

    def __init__(self):
        # (base_name, E_description, Z_description)
        # E: higher priority groups on opposite sides
        # Z: higher priority groups on same side
        compounds = [
            ("but-2-ene", "CH\u2083 groups opposite", "CH\u2083 groups same side"),
            ("pent-2-ene", "CH\u2083 and C\u2082H\u2085 opposite", "CH\u2083 and C\u2082H\u2085 same side"),
            ("1,2-dichloroethene", "Cl atoms opposite", "Cl atoms same side"),
            ("1-bromoprop-1-ene", "Br and CH\u2083 opposite", "Br and CH\u2083 same side"),
            ("1-chlorobut-1-ene", "Cl and C\u2082H\u2085 opposite", "Cl and C\u2082H\u2085 same side"),
            ("2-chlorobut-2-ene", "Cl and CH\u2083 opposite", "Cl and CH\u2083 same side"),
            ("1,2-dibromoethene", "Br atoms opposite", "Br atoms same side"),
            ("hex-3-ene", "C\u2082H\u2085 groups opposite", "C\u2082H\u2085 groups same side"),
            ("1-fluoroprop-1-ene", "F and CH\u2083 opposite", "F and CH\u2083 same side"),
            ("cinnamic acid (phenylpropenoic acid)", "COOH and C\u2086H\u2085 opposite", "COOH and C\u2086H\u2085 same side"),
            ("maleic acid (butenedioic acid)", "COOH groups opposite", "COOH groups same side"),
        ]

        self.compound = rnd.choice(compounds)
        self.base_name = self.compound[0]

        self.shown_isomer = rnd.choice(["E", "Z"])
        self.answer = self.shown_isomer

        self.description = (
            f"Identify whether the isomer of {self.base_name} shown in the diagram is the E or Z isomer."
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Geometric isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The isomer shown is the {self.shown_isomer}-isomer}} &\\\\"
            f"\\text{{E: higher priority groups on opposite sides of C=C}} &\\\\"
            f"\\text{{Z: higher priority groups on same side of C=C}} &"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 5, 7.5, f"Geometric Isomer of {self.base_name}", fontsize=16)

        # C=C double bond
        ax.plot([3.5, 6.5], [4.2, 4.2], 'k-', linewidth=3)
        ax.plot([3.5, 6.5], [3.8, 3.8], 'k-', linewidth=3)
        ax.plot([3.5, 3.5], [3.8, 4.2], 'k-', linewidth=2)
        ax.plot([6.5, 6.5], [3.8, 4.2], 'k-', linewidth=2)

        ax.text(5, 4, 'C=C', fontsize=14, ha='center', va='center', fontweight='bold')

        if self.shown_isomer == "E":
            # High priority groups on OPPOSITE sides
            ax.text(2.5, 5.0, "High\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
            ax.text(7.5, 3.0, "High\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
            ax.text(2.5, 3.0, "Low\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
            ax.text(7.5, 5.0, "Low\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
        else:
            # High priority groups on SAME side
            ax.text(2.5, 5.0, "High\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
            ax.text(7.5, 5.0, "High\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
            ax.text(2.5, 3.0, "Low\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
            ax.text(7.5, 3.0, "Low\npriority", fontsize=12, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))

        ax.text(5, 1.5, "Is this the E or Z isomer?", fontsize=14, ha='center', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem063:
    """
    Topic: 29.4 Optical isomerism
    Visual: Tetrahedral chiral carbon with 4 groups (mirror image shown)
    Task: Identify chiral center position (numerical - e.g. C2)
    Expanded to 10+ variations
    """

    def __init__(self):
        molecules = [
            {
                'name': 'butan-2-ol',
                'formula': 'CH\u2083CH(OH)CH\u2082CH\u2083',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'OH', 'H', 'CH\u2082CH\u2083']
            },
            {
                'name': '2-aminopropanoic acid (alanine)',
                'formula': 'CH\u2083CH(NH\u2082)COOH',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'NH\u2082', 'H', 'COOH']
            },
            {
                'name': '2-bromobutane',
                'formula': 'CH\u2083CHBrCH\u2082CH\u2083',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'Br', 'H', 'CH\u2082CH\u2083']
            },
            {
                'name': '3-methylhexane',
                'formula': 'CH\u2083CH\u2082CH(CH\u2083)CH\u2082CH\u2082CH\u2083',
                'chiral_position': 3,
                'groups': ['CH\u2083', 'C\u2082H\u2085', 'H', 'C\u2083H\u2087']
            },
            {
                'name': '2-chloropentane',
                'formula': 'CH\u2083CHClCH\u2082CH\u2082CH\u2083',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'Cl', 'H', 'C\u2083H\u2087']
            },
            {
                'name': 'lactic acid (2-hydroxypropanoic acid)',
                'formula': 'CH\u2083CH(OH)COOH',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'OH', 'H', 'COOH']
            },
            {
                'name': '2-iodobutane',
                'formula': 'CH\u2083CHICH\u2082CH\u2083',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'I', 'H', 'CH\u2082CH\u2083']
            },
            {
                'name': '3-bromopentane',
                'formula': 'CH\u2083CH\u2082CHBrCH\u2082CH\u2083',
                'chiral_position': 3,
                'groups': ['C\u2082H\u2085', 'Br', 'H', 'C\u2082H\u2085']
            },
            {
                'name': '2-methylbutan-1-ol',
                'formula': 'CH\u2083CH(C\u2082H\u2085)CH\u2082OH',
                'chiral_position': 2,
                'groups': ['CH\u2083', 'C\u2082H\u2085', 'H', 'CH\u2082OH']
            },
            {
                'name': 'phenylalanine',
                'formula': 'C\u2086H\u2085CH\u2082CH(NH\u2082)COOH',
                'chiral_position': 2,
                'groups': ['C\u2086H\u2085CH\u2082', 'NH\u2082', 'H', 'COOH']
            },
        ]

        self.molecule = rnd.choice(molecules)
        self.rotation = rnd.choice(['+', '-'])
        self.rotation_value = rnd.randint(5, 30)

        self.answer = self.molecule['chiral_position']

        self.description = (
            f"The diagram shows the two enantiomers of {self.molecule['name']}. "
            f"One enantiomer rotates plane-polarized light by {self.rotation}{self.rotation_value}\u00b0. "
            f"At which carbon number is the chiral centre located?"
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "29.4 Isomerism: optical"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: {self.molecule['name']}}}&\\\\"
            f"\\text{{Chiral centre: carbon bonded to 4 different groups}}&\\\\"
            f"\\text{{Groups: {', '.join(self.molecule['groups'])}}}&\\\\"
            f"\\text{{Chiral carbon at position: C{self.molecule['chiral_position']}}}&\\\\"
            f"\\text{{Optical rotation: {self.rotation}{self.rotation_value}\u00b0}}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 6, 7.5, f"Optical Isomerism: {self.molecule['name']}", fontsize=15)

        center_x, center_y = 3, 4
        draw_circle_atom(ax, center_x, center_y, 'C*', radius=0.4,
                        color='yellow', text_color='black', fontsize=16)

        group_positions = [
            (center_x, center_y + 1.5),
            (center_x + 1.5, center_y),
            (center_x, center_y - 1.5),
            (center_x - 1.5, center_y)
        ]

        for i, (gx, gy) in enumerate(group_positions):
            draw_bond(ax, center_x, center_y, gx, gy, linewidth=2.5)
            ax.text(gx, gy, self.molecule['groups'][i], fontsize=12, ha='center', va='center',
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))

        center_x2 = 9
        draw_circle_atom(ax, center_x2, center_y, 'C*', radius=0.4,
                        color='yellow', text_color='black', fontsize=16)

        groups_mirrored = [self.molecule['groups'][0], self.molecule['groups'][3],
                          self.molecule['groups'][2], self.molecule['groups'][1]]

        group_positions2 = [
            (center_x2, center_y + 1.5),
            (center_x2 - 1.5, center_y),
            (center_x2, center_y - 1.5),
            (center_x2 + 1.5, center_y)
        ]

        for i, (gx, gy) in enumerate(group_positions2):
            draw_bond(ax, center_x2, center_y, gx, gy, linewidth=2.5)
            ax.text(gx, gy, groups_mirrored[i], fontsize=12, ha='center', va='center',
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))

        ax.plot([6, 6], [2, 6], 'k--', linewidth=2)
        ax.text(6, 6.5, 'mirror', fontsize=11, ha='center', style='italic')

        ax.text(3, 1.5, f"Rotation: {self.rotation}{self.rotation_value}\u00b0",
               fontsize=12, ha='center', fontweight='bold')
        ax.text(9, 1.5, f"Rotation: {'-' if self.rotation == '+' else '+'}{self.rotation_value}\u00b0",
               fontsize=12, ha='center', fontweight='bold')

        ax.text(6, 0.5, "* = carbon bonded to 4 different groups",
               fontsize=11, ha='center', style='italic')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem064:
    """
    Topic: 30.1 Benzene - Electrophilic Aromatic Substitution
    Visual: Mechanism diagram (benzene → intermediate → product)
    Task: MCQ - identify the electrophile in this reaction
    10+ variations
    """

    def __init__(self):
        reactions = [
            {
                'reaction_name': 'Nitration',
                'electrophile': 'NO\u2082\u207a',
                'reagents': 'conc. HNO\u2083 + conc. H\u2082SO\u2084',
                'temperature': '50-60\u00b0C',
                'product': 'nitrobenzene',
            },
            {
                'reaction_name': 'Bromination',
                'electrophile': 'Br\u207a',
                'reagents': 'Br\u2082 + AlBr\u2083 catalyst',
                'temperature': 'room temperature',
                'product': 'bromobenzene',
            },
            {
                'reaction_name': 'Chlorination',
                'electrophile': 'Cl\u207a',
                'reagents': 'Cl\u2082 + AlCl\u2083 catalyst',
                'temperature': 'room temperature',
                'product': 'chlorobenzene',
            },
            {
                'reaction_name': 'Friedel-Crafts alkylation',
                'electrophile': 'CH\u2083\u207a',
                'reagents': 'CH\u2083Cl + AlCl\u2083 catalyst',
                'temperature': 'room temperature',
                'product': 'methylbenzene (toluene)',
            },
            {
                'reaction_name': 'Friedel-Crafts acylation',
                'electrophile': 'CH\u2083CO\u207a',
                'reagents': 'CH\u2083COCl + AlCl\u2083 catalyst',
                'temperature': 'room temperature',
                'product': 'phenylethanone (acetophenone)',
            },
            {
                'reaction_name': 'Iodination',
                'electrophile': 'I\u207a',
                'reagents': 'I\u2082 + HNO\u2083 or I\u2082 + H\u2082O\u2082',
                'temperature': 'room temperature',
                'product': 'iodobenzene',
            },
            {
                'reaction_name': 'Sulfonation',
                'electrophile': 'SO\u2083',
                'reagents': 'fuming H\u2082SO\u2084 (oleum)',
                'temperature': '100\u00b0C',
                'product': 'benzenesulfonic acid',
            },
            {
                'reaction_name': 'Nitration (toluene)',
                'electrophile': 'NO\u2082\u207a',
                'reagents': 'conc. HNO\u2083 + conc. H\u2082SO\u2084',
                'temperature': '30\u00b0C',
                'product': '2- and 4-nitrotoluene',
            },
            {
                'reaction_name': 'Propylation (Friedel-Crafts)',
                'electrophile': 'C\u2083H\u2087\u207a',
                'reagents': 'C\u2083H\u2087Cl + AlCl\u2083 catalyst',
                'temperature': 'room temperature',
                'product': 'propylbenzene',
            },
            {
                'reaction_name': 'Chlorination (phenol)',
                'electrophile': 'Cl\u207a',
                'reagents': 'Cl\u2082 (no catalyst needed)',
                'temperature': 'room temperature',
                'product': '2,4,6-trichlorophenol',
            },
        ]

        self.reaction = rnd.choice(reactions)
        correct = self.reaction['electrophile']

        all_e = [r['electrophile'] for r in reactions]
        wrong = [e for e in all_e if e != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a benzene electrophilic aromatic substitution mechanism. "
            f"The reagents and conditions are shown on the diagram. "
            f"What is the electrophile in this reaction?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydrocarbons"
        self.subtopic = "30.1 Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.reaction['reaction_name']}}}&\\\\"
            f"\\text{{Electrophile: {self.reaction['electrophile']}}}&\\\\"
            f"\\text{{Reagents: {self.reaction['reagents']}}}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, f"Benzene {self.reaction['reaction_name']} Mechanism", fontsize=14)

        x1, y1 = 2, 4
        hexagon1 = patches.RegularPolygon((x1, y1), 6, radius=0.8,
                                         facecolor='none', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon1)
        from matplotlib.patches import Circle
        circle1 = Circle((x1, y1), 0.5, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle1)
        ax.text(x1, y1 - 1.5, 'Benzene', fontsize=12, ha='center', fontweight='bold')

        draw_arrow(ax, 3.5, 4, 5.5, 4, label="+ electrophile",
                  label_position='above', color='black', linewidth=2.5)

        x2, y2 = 7, 4
        hexagon2 = patches.RegularPolygon((x2, y2), 6, radius=0.8,
                                         facecolor='lightyellow', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon2)
        ax.text(x2 + 0.9, y2 + 0.5, '+', fontsize=16, ha='center', color='red', fontweight='bold')
        ax.text(x2, y2 - 1.5, 'Carbocation\nintermediate', fontsize=11, ha='center', style='italic')

        draw_arrow(ax, 8.5, 4, 10.5, 4, label="- H\u207a",
                  label_position='above', color='black', linewidth=2.5)

        x3, y3 = 12, 4
        hexagon3 = patches.RegularPolygon((x3, y3), 6, radius=0.8,
                                         facecolor='none', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon3)
        circle3 = Circle((x3, y3), 0.5, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle3)
        ax.text(x3, y3 - 1.5, self.reaction['product'], fontsize=11, ha='center', fontweight='bold')

        conditions = f"Reagents: {self.reaction['reagents']}\nTemp: {self.reaction['temperature']}"
        ax.text(7, 1, conditions, fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow',
                        edgecolor='black', linewidth=2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem065:
    """
    Topic: 30.1 Alkane reactions - Free radical substitution
    Visual: Propagation step diagram showing reactants and ? product
    Task: MCQ - what is the organic product?
    10+ variations
    """

    def __init__(self):
        reactions = [
            ("CH\u2084", "Cl\u2022", "CH\u2083Cl", "chloromethane"),
            ("CH\u2084", "Br\u2022", "CH\u2083Br", "bromomethane"),
            ("C\u2082H\u2086", "Cl\u2022", "C\u2082H\u2085Cl", "chloroethane"),
            ("C\u2082H\u2086", "Br\u2022", "C\u2082H\u2085Br", "bromoethane"),
            ("C\u2083H\u2088", "Cl\u2022", "C\u2083H\u2087Cl", "chloropropane"),
            ("C\u2083H\u2088", "Br\u2022", "C\u2083H\u2087Br", "bromopropane"),
            ("CH\u2083Cl", "Cl\u2022", "CH\u2082Cl\u2082", "dichloromethane"),
            ("C\u2084H\u2081\u2080", "Cl\u2022", "C\u2084H\u2089Cl", "chlorobutane"),
            ("C\u2084H\u2081\u2080", "Br\u2022", "C\u2084H\u2089Br", "bromobutane"),
            ("C\u2082H\u2086", "F\u2022", "C\u2082H\u2085F", "fluoroethane"),
            ("CH\u2084", "F\u2022", "CH\u2083F", "fluoromethane"),
        ]

        self.rxn = rnd.choice(reactions)
        self.alkane, self.radical, self.product, self.product_name = self.rxn

        all_products = [r[2] for r in reactions]
        wrong = [p for p in all_products if p != self.product]
        options = rnd.sample(wrong, 3) + [self.product]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(self.product)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a propagation step of free radical substitution. "
            f"The reactants are shown in the diagram. "
            f"What is the organic product formed in this step?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydrocarbons"
        self.subtopic = "Alkane reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Propagation step:}} &\\\\"
            f"\\text{{{self.alkane} + {self.radical}}} &\\rightarrow \\text{{{self.product} + H\u2022}}\\\\"
            f"\\text{{Product: {self.product} ({self.product_name})}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        add_formula_label(ax, 2, 3, self.alkane, fontsize=20, weight='bold')
        add_formula_label(ax, 4.5, 3, "+", fontsize=20, weight='bold')
        add_formula_label(ax, 6, 3, self.radical, fontsize=20, weight='bold')

        draw_arrow(ax, 7.5, 3, 9, 3, label="UV light", label_position='above',
                  color='black', linewidth=3)

        add_formula_label(ax, 10.5, 3, "?", fontsize=20, weight='bold', color='red')

        add_title_box(ax, 6, 5.5, "Free Radical Substitution", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem066:
    """
    Topic: 30.1 Hydrocarbons - Directing effects in arenes
    Visual: Benzene ring with numbered positions, NO highlighting of answer positions
    Task: MCQ - which position(s) does the substituent direct to?
    10+ variations
    """

    def __init__(self):
        substituents = [
            {
                'compound': 'methylbenzene',
                'substituent': 'CH\u2083',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'activating/ortho-para directing',
            },
            {
                'compound': 'phenol',
                'substituent': 'OH',
                'positions': ['2', '4', '6'],
                'correct': '2, 4 and 6',
                'type': 'activating/ortho-para directing',
            },
            {
                'compound': 'nitrobenzene',
                'substituent': 'NO\u2082',
                'positions': ['3'],
                'correct': '3 (meta)',
                'type': 'deactivating/meta directing',
            },
            {
                'compound': 'aniline (aminobenzene)',
                'substituent': 'NH\u2082',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'activating/ortho-para directing',
            },
            {
                'compound': 'chlorobenzene',
                'substituent': 'Cl',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'deactivating/ortho-para directing',
            },
            {
                'compound': 'benzoic acid',
                'substituent': 'COOH',
                'positions': ['3'],
                'correct': '3 (meta)',
                'type': 'deactivating/meta directing',
            },
            {
                'compound': 'methoxybenzene (anisole)',
                'substituent': 'OCH\u2083',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'activating/ortho-para directing',
            },
            {
                'compound': 'bromobenzene',
                'substituent': 'Br',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'deactivating/ortho-para directing',
            },
            {
                'compound': 'acetophenone',
                'substituent': 'COCH\u2083',
                'positions': ['3'],
                'correct': '3 (meta)',
                'type': 'deactivating/meta directing',
            },
            {
                'compound': 'fluorobenzene',
                'substituent': 'F',
                'positions': ['2', '4'],
                'correct': '2 and 4',
                'type': 'deactivating/ortho-para directing',
            },
        ]

        self.subst = rnd.choice(substituents)
        correct = self.subst['correct']

        all_positions = ["2 and 4", "2, 4 and 6", "3 (meta)", "1 and 2", "4 only"]
        wrong = [p for p in all_positions if p != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows a numbered benzene ring with a substituent group. "
            f"When this compound undergoes further electrophilic substitution, "
            f"which position(s) will the new substituent preferentially occupy?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydrocarbons"
        self.subtopic = "30.1 Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Substituent: {self.subst['substituent']}}}&\\\\"
            f"\\text{{Effect: {self.subst['type']}}}&\\\\"
            f"\\text{{Preferred positions: {correct}}}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 5, 7.5, f"Directing Effects: {self.subst['compound']}", fontsize=15)

        import numpy as np
        center_x, center_y = 5, 4
        radius = 1.2

        hexagon = patches.RegularPolygon((center_x, center_y), 6, radius=radius,
                                        facecolor='lightyellow', edgecolor='black', linewidth=3)
        ax.add_patch(hexagon)

        from matplotlib.patches import Circle
        circle = Circle((center_x, center_y), radius*0.6, fill=False,
                       edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle)

        angles = [90, 30, -30, -90, -150, 150]
        for i, angle in enumerate(angles):
            pos_num = i + 1
            rad = np.radians(angle)
            label_x = center_x + (radius + 0.5) * np.cos(rad)
            label_y = center_y + (radius + 0.5) * np.sin(rad)

            # All positions shown in same neutral style (no red highlighting)
            ax.text(label_x, label_y, str(pos_num), fontsize=14, ha='center', va='center',
                   fontweight='bold', color='black',
                   bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=1))

        subst_y = center_y + radius + 0.8
        ax.text(center_x, subst_y, self.subst['substituent'], fontsize=14, ha='center',
               fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.4))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem067:
    """
    Topic: 32.2 Hydroxy compounds - Phenol acidity
    Visual: Table showing compound names and formulas (pKa NOT shown - that would be answer hint)
    Task: MCQ - arrange compounds in order of increasing acidity
    10+ variations
    """

    def __init__(self):
        comparisons = [
            {
                'compounds': ['water', 'ethanol', 'phenol'],
                'formulas': ['H\u2082O', 'C\u2082H\u2085OH', 'C\u2086H\u2085OH'],
                'pKa': [15.7, 15.9, 9.9],
                'order': 'water < ethanol < phenol',
                'correct': 'water < ethanol < phenol (phenol most acidic)',
            },
            {
                'compounds': ['ethanol', 'phenol', '2-nitrophenol'],
                'formulas': ['C\u2082H\u2085OH', 'C\u2086H\u2085OH', '2-NO\u2082C\u2086H\u2084OH'],
                'pKa': [15.9, 9.9, 7.2],
                'order': 'ethanol < phenol < 2-nitrophenol',
                'correct': 'ethanol < phenol < 2-nitrophenol (2-nitrophenol most acidic)',
            },
            {
                'compounds': ['methanol', 'ethanol', 'phenol'],
                'formulas': ['CH\u2083OH', 'C\u2082H\u2085OH', 'C\u2086H\u2085OH'],
                'pKa': [15.5, 15.9, 9.9],
                'order': 'ethanol < methanol < phenol',
                'correct': 'ethanol < methanol < phenol (phenol most acidic)',
            },
            {
                'compounds': ['propanol', 'phenol', '4-nitrophenol'],
                'formulas': ['C\u2083H\u2087OH', 'C\u2086H\u2085OH', '4-NO\u2082C\u2086H\u2084OH'],
                'pKa': [16.1, 9.9, 7.1],
                'order': 'propanol < phenol < 4-nitrophenol',
                'correct': 'propanol < phenol < 4-nitrophenol (4-nitrophenol most acidic)',
            },
            {
                'compounds': ['phenol', '2-chlorophenol', '2,4-dichlorophenol'],
                'formulas': ['C\u2086H\u2085OH', '2-ClC\u2086H\u2084OH', '2,4-Cl\u2082C\u2086H\u2083OH'],
                'pKa': [9.9, 8.5, 7.9],
                'order': 'phenol < 2-chlorophenol < 2,4-dichlorophenol',
                'correct': 'phenol < 2-chlorophenol < 2,4-dichlorophenol',
            },
            {
                'compounds': ['ethanol', 'water', 'ethanoic acid'],
                'formulas': ['C\u2082H\u2085OH', 'H\u2082O', 'CH\u2083COOH'],
                'pKa': [15.9, 15.7, 4.8],
                'order': 'ethanoic acid < water < ethanol',
                'correct': 'ethanoic acid < water < ethanol (ethanoic acid most acidic)',
            },
            {
                'compounds': ['phenol', '4-methylphenol', '4-nitrophenol'],
                'formulas': ['C\u2086H\u2085OH', '4-CH\u2083C\u2086H\u2084OH', '4-NO\u2082C\u2086H\u2084OH'],
                'pKa': [9.9, 10.2, 7.1],
                'order': '4-nitrophenol < phenol < 4-methylphenol',
                'correct': '4-nitrophenol < phenol < 4-methylphenol (4-nitrophenol most acidic)',
            },
            {
                'compounds': ['methanol', 'phenol', 'carbonic acid'],
                'formulas': ['CH\u2083OH', 'C\u2086H\u2085OH', 'H\u2082CO\u2083'],
                'pKa': [15.5, 9.9, 6.4],
                'order': 'carbonic acid < phenol < methanol',
                'correct': 'carbonic acid < phenol < methanol (carbonic acid most acidic)',
            },
            {
                'compounds': ['propanol', 'phenol', 'methanoic acid'],
                'formulas': ['C\u2083H\u2087OH', 'C\u2086H\u2085OH', 'HCOOH'],
                'pKa': [16.1, 9.9, 3.7],
                'order': 'methanoic acid < phenol < propanol',
                'correct': 'methanoic acid < phenol < propanol (methanoic acid most acidic)',
            },
            {
                'compounds': ['phenol', 'benzoic acid', 'nitric acid'],
                'formulas': ['C\u2086H\u2085OH', 'C\u2086H\u2085COOH', 'HNO\u2083'],
                'pKa': [9.9, 4.2, -1.4],
                'order': 'nitric acid < benzoic acid < phenol',
                'correct': 'nitric acid < benzoic acid < phenol (nitric acid most acidic)',
            },
        ]

        self.comp = rnd.choice(comparisons)

        # Build MCQ - shuffle order of compounds
        names = self.comp['compounds']
        from itertools import permutations
        perms = list(permutations(names))
        rnd.shuffle(perms)
        wrong_opts = []
        for p in perms:
            opt = ' < '.join(p)
            if opt != self.comp['order'] and opt not in wrong_opts:
                wrong_opts.append(opt)
            if len(wrong_opts) >= 3:
                break

        options = wrong_opts[:3] + [self.comp['order']]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(self.comp['order'])]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The table shows three compounds. "
            f"Arrange them in order of increasing acidity (weakest acid first)."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydroxy compounds"
        self.subtopic = "32.2 Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Lower pKa = stronger acid}&\\\\"
            + "\\\\".join([f"\\text{{{compound}: pKa = {pKa}}}"
                          for compound, pKa in zip(self.comp['compounds'], self.comp['pKa'])]) + "\\\\"
            f"\\text{{Order: {self.comp['order']}}}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Acidity Comparison", fontsize=16)

        headers = ['Compound', 'Formula']
        col_width = 3
        for i, header in enumerate(headers):
            x = 1.5 + i * col_width
            y = 5.5
            ax.text(x, y, header, fontsize=13, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgray',
                            edgecolor='black', linewidth=2))

        row_height = 0.8
        for row_idx in range(3):
            y = 5.5 - (row_idx + 1) * row_height
            ax.text(1.5, y, self.comp['compounds'][row_idx], fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
            ax.text(4.5, y, self.comp['formulas'][row_idx], fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem068:
    """
    Topic: 32.2 Hydroxy compounds - Phenol reactions
    Visual: Phenol + reagent arrow diagram (product NOT drawn)
    Task: MCQ - what is the organic product?
    10+ variations
    """

    def __init__(self):
        reactions = [
            {
                'name': 'Bromination',
                'reagent': 'Br\u2082(aq)',
                'conditions': 'room temperature, no catalyst',
                'product': '2,4,6-tribromophenol',
                'observation': 'white precipitate; bromine water decolourised',
            },
            {
                'name': 'Nitration',
                'reagent': 'dilute HNO\u2083',
                'conditions': 'room temperature',
                'product': 'mixture of 2-nitrophenol and 4-nitrophenol',
                'observation': 'yellow oil forms',
            },
            {
                'name': 'Nitration (conc.)',
                'reagent': 'conc. HNO\u2083',
                'conditions': 'room temperature',
                'product': '2,4,6-trinitrophenol (picric acid)',
                'observation': 'yellow solid forms',
            },
            {
                'name': 'Reaction with Na',
                'reagent': 'Na(s)',
                'conditions': 'room temperature',
                'product': 'sodium phenoxide (C\u2086H\u2085O\u207bNa\u207a) + H\u2082',
                'observation': 'effervescence (H\u2082 gas)',
            },
            {
                'name': 'Reaction with NaOH',
                'reagent': 'NaOH(aq)',
                'conditions': 'room temperature',
                'product': 'sodium phenoxide (C\u2086H\u2085O\u207bNa\u207a)',
                'observation': 'phenol dissolves to give clear solution',
            },
            {
                'name': 'Esterification',
                'reagent': 'ethanoic anhydride',
                'conditions': 'room temperature',
                'product': 'phenyl ethanoate',
                'observation': 'reaction occurs readily',
            },
            {
                'name': 'Chlorination',
                'reagent': 'Cl\u2082(aq)',
                'conditions': 'room temperature, no catalyst',
                'product': '2,4,6-trichlorophenol',
                'observation': 'chlorine water decolourised; white precipitate',
            },
            {
                'name': 'Phenylazo coupling',
                'reagent': 'diazonium salt (C\u2086H\u2085N\u2082\u207a)',
                'conditions': 'alkaline solution, cold',
                'product': 'yellow-orange azo dye (4-hydroxyazobenzene)',
                'observation': 'bright orange/yellow solution forms',
            },
            {
                'name': 'Esterification with acyl chloride',
                'reagent': 'benzoyl chloride (C\u2086H\u2085COCl)',
                'conditions': 'room temperature',
                'product': 'phenyl benzoate',
                'observation': 'vigorous reaction; HCl fumes',
            },
            {
                'name': 'Reduction',
                'reagent': 'H\u2082/Ni catalyst',
                'conditions': 'high pressure, heat',
                'product': 'cyclohexanol',
                'observation': 'solid product formed',
            },
        ]

        self.rxn = rnd.choice(reactions)
        correct = self.rxn['product']

        all_products = [r['product'] for r in reactions]
        wrong = [p for p in all_products if p != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"Phenol reacts with {self.rxn['reagent']} under the conditions shown. "
            f"What is the organic product formed?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydroxy compounds"
        self.subtopic = "32.2 Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.rxn['name']}}}&\\\\"
            f"\\text{{Product: {self.rxn['product']}}}&\\\\"
            f"\\text{{Observation: {self.rxn['observation']}}}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 6.5, f"Phenol {self.rxn['name']}", fontsize=16)

        x1, y1 = 2.5, 3.5
        hexagon1 = patches.RegularPolygon((x1, y1), 6, radius=0.8,
                                         facecolor='lightyellow', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon1)
        ax.text(x1, y1 + 1.2, 'OH', fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
        ax.text(x1, y1 - 1.5, 'Phenol', fontsize=12, ha='center', fontweight='bold')

        conditions = f"{self.rxn['reagent']}\n{self.rxn['conditions']}"
        draw_arrow(ax, 4, 3.5, 6.5, 3.5, label=conditions,
                  label_position='above', color='black', linewidth=2.5)

        ax.text(10, 3.5, "?", fontsize=30, ha='center', va='center', color='red', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', linewidth=2, pad=1))


        # Observation intentionally omitted – student infers product from reagent shown

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem069:
    """
    Topic: 32.2 Alcohols reactions - oxidation
    Visual: Alcohol oxidation diagram with BLANK product box
    Task: MCQ - what is the organic product?
    10+ variations
    """

    def __init__(self):
        # Format: (type, alcohol_name, alcohol_formula, product_name, product_formula, notes)
        alcohols = [
            ("primary", "methanol", "CH\u2083OH", "methanal (then methanoic acid)", "HCHO \u2192 HCOOH", "distil product to prevent over-oxidation"),
            ("primary", "ethanol", "C\u2082H\u2085OH", "ethanal (then ethanoic acid)", "CH\u2083CHO \u2192 CH\u2083COOH", "distil to get aldehyde; reflux for acid"),
            ("primary", "propan-1-ol", "C\u2083H\u2087OH", "propanal (then propanoic acid)", "C\u2082H\u2085CHO \u2192 C\u2082H\u2085COOH", "distil to get aldehyde"),
            ("primary", "butan-1-ol", "C\u2084H\u2089OH", "butanal (then butanoic acid)", "C\u2083H\u2087CHO \u2192 C\u2083H\u2087COOH", "distil to prevent over-oxidation"),
            ("secondary", "propan-2-ol", "CH\u2083CH(OH)CH\u2083", "propanone (ketone)", "CH\u2083COCH\u2083", "cannot be oxidised further"),
            ("secondary", "butan-2-ol", "CH\u2083CH(OH)CH\u2082CH\u2083", "butanone (ketone)", "CH\u2083COCH\u2082CH\u2083", "cannot be oxidised further"),
            ("secondary", "pentan-2-ol", "CH\u2083CH(OH)C\u2083H\u2087", "pentan-2-one (ketone)", "CH\u2083COC\u2083H\u2087", "cannot be oxidised further"),
            ("secondary", "pentan-3-ol", "C\u2082H\u2085CH(OH)C\u2082H\u2085", "pentan-3-one (ketone)", "C\u2082H\u2085COC\u2082H\u2085", "cannot be oxidised further"),
            ("tertiary", "2-methylpropan-2-ol", "(CH\u2083)\u2083COH", "no reaction", "no oxidation", "tertiary alcohols resist oxidation"),
            ("tertiary", "2-methylbutan-2-ol", "CH\u2083C(OH)(CH\u2083)C\u2082H\u2085", "no reaction", "no oxidation", "tertiary alcohols resist oxidation"),
        ]

        self.rxn = rnd.choice(alcohols)
        (self.classification, self.alcohol_name, self.alcohol_formula,
         self.product_desc, self.product_formula, self.note) = self.rxn

        correct = self.product_desc

        all_products = [r[3] for r in alcohols]
        wrong = [p for p in all_products if p != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"{self.alcohol_name} ({self.alcohol_formula}) is oxidized with acidified potassium dichromate (K\u2082Cr\u2082O\u2087/H\u207a). "
            f"What is the organic product formed?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.classification} alcohol: {self.alcohol_name}}} &\\\\"
            f"\\text{{Product: {self.product_desc}}} &\\\\"
            f"\\text{{Note: {self.note}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, f"{self.classification.capitalize()} Alcohol Oxidation", fontsize=16)

        draw_labeled_box(ax, 0.5, 3, 3.5, 1.5, f"{self.alcohol_formula}\n({self.alcohol_name})",
                        facecolor='lightblue')

        draw_arrow(ax, 4.2, 3.8, 7.5, 3.8,
                  label="[O]\nK\u2082Cr\u2082O\u2087/H\u207a",
                  label_position='above', color='red', linewidth=2.5)

        draw_labeled_box(ax, 8, 3, 3.5, 1.5, "?", facecolor='lightgray')

        if self.classification == "primary":
            add_formula_label(ax, 6, 1.5, "Conditions affect product (distil vs reflux)", fontsize=10)
        elif self.classification == "tertiary":
            add_formula_label(ax, 6, 1.5, "Note: Cr\u2082O\u2087\u00b2\u207b color does NOT change", fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem070:
    """
    Topic: 32.2 Alcohol dehydration
    Visual: Alcohol formula + arrow (product NOT shown)
    Task: MCQ - what is the alkene product?
    10+ variations
    """

    def __init__(self):
        reactions = [
            ("ethanol", "ethene", "CH\u2083CH\u2082OH", "CH\u2082=CH\u2082"),
            ("propan-1-ol", "propene", "CH\u2083CH\u2082CH\u2082OH", "CH\u2083CH=CH\u2082"),
            ("propan-2-ol", "propene", "CH\u2083CH(OH)CH\u2083", "CH\u2083CH=CH\u2082"),
            ("butan-2-ol", "but-2-ene (major)", "CH\u2083CH(OH)CH\u2082CH\u2083", "CH\u2083CH=CHCH\u2083"),
            ("butan-1-ol", "but-1-ene", "CH\u2083CH\u2082CH\u2082CH\u2082OH", "CH\u2083CH\u2082CH=CH\u2082"),
            ("2-methylpropan-2-ol", "2-methylpropene", "(CH\u2083)\u2083COH", "(CH\u2083)\u2082C=CH\u2082"),
            ("2-methylbutan-2-ol", "2-methylbut-2-ene (major)", "CH\u2083C(OH)(CH\u2083)CH\u2082CH\u2083", "CH\u2083C(CH\u2083)=CHCH\u2083"),
            ("pentan-2-ol", "pent-2-ene (major)", "CH\u2083CH(OH)C\u2083H\u2087", "CH\u2083CH=CHC\u2082H\u2085"),
            ("cyclohexanol", "cyclohexene", "C\u2086H\u2081\u2081OH", "C\u2086H\u2081\u2080"),
            ("2-methylpropan-1-ol", "2-methylpropene", "(CH\u2083)\u2082CHCH\u2082OH", "(CH\u2083)\u2082C=CH\u2082"),
            ("pentan-3-ol", "pent-2-ene or pent-3-ene", "C\u2082H\u2085CH(OH)C\u2082H\u2085", "C\u2082H\u2085CH=CHC\u2082H\u2085"),
        ]

        self.reaction = rnd.choice(reactions)
        self.alcohol_name, self.alkene_name, self.alcohol_formula, self.alkene_formula = self.reaction

        correct = self.alkene_name
        all_products = [r[1] for r in reactions]
        wrong = [p for p in all_products if p != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"When {self.alcohol_name} undergoes dehydration with concentrated H\u2082SO\u2084 at 170\u00b0C, "
            f"what is the main alkene product formed?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol dehydration"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Dehydration of {self.alcohol_name}:}} &\\\\"
            f"\\text{{{self.alcohol_formula}}} &\\xrightarrow{{\\text{{H}}_2\\text{{SO}}_4, \\Delta}} "
            f"\\text{{{self.alkene_formula}}} + \\text{{H}}_2\\text{{O}}\\\\"
            f"\\text{{Product: {self.alkene_name}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        add_formula_label(ax, 2.5, 3, self.alcohol_formula, fontsize=18, weight='bold')

        draw_arrow(ax, 4.5, 3, 8, 3,
                  label="conc. H\u2082SO\u2084, 170\u00b0C",
                  label_position='above', color='red', linewidth=3)

        add_formula_label(ax, 10, 3, "?", fontsize=24, weight='bold', color='red')
        add_formula_label(ax, 10, 2.2, "+ H\u2082O", fontsize=13)

        add_title_box(ax, 6, 5.5, "Alcohol Dehydration", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem071:
    """
    Topic: 33.3 Carboxylic acid derivatives - Acyl chloride reactions
    Visual: Acyl chloride + nucleophile → ? (product hidden)
    Task: MCQ - what are the products?
    10+ variations
    """

    def __init__(self):
        reactions = [
            {
                'acyl_chloride': 'CH\u2083COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'H\u2082O',
                'nuc_name': 'water',
                'product': 'CH\u2083COOH',
                'product_name': 'ethanoic acid',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'C\u2082H\u2085OH',
                'nuc_name': 'ethanol',
                'product': 'CH\u2083COOC\u2082H\u2085',
                'product_name': 'ethyl ethanoate (ester)',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'NH\u2083',
                'nuc_name': 'ammonia',
                'product': 'CH\u2083CONH\u2082',
                'product_name': 'ethanamide (amide)',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'CH\u2083NH\u2082',
                'nuc_name': 'methylamine',
                'product': 'CH\u2083CONHCH\u2083',
                'product_name': 'N-methylethanamide',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'C\u2086H\u2085COCl',
                'acyl_name': 'benzoyl chloride',
                'nucleophile': 'H\u2082O',
                'nuc_name': 'water',
                'product': 'C\u2086H\u2085COOH',
                'product_name': 'benzoic acid',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'C\u2086H\u2085COCl',
                'acyl_name': 'benzoyl chloride',
                'nucleophile': 'CH\u2083OH',
                'nuc_name': 'methanol',
                'product': 'C\u2086H\u2085COOCH\u2083',
                'product_name': 'methyl benzoate (ester)',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'C\u2086H\u2085COCl',
                'acyl_name': 'benzoyl chloride',
                'nucleophile': 'NH\u2083',
                'nuc_name': 'ammonia',
                'product': 'C\u2086H\u2085CONH\u2082',
                'product_name': 'benzamide (amide)',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083CH\u2082COCl',
                'acyl_name': 'propanoyl chloride',
                'nucleophile': 'H\u2082O',
                'nuc_name': 'water',
                'product': 'CH\u2083CH\u2082COOH',
                'product_name': 'propanoic acid',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083CH\u2082COCl',
                'acyl_name': 'propanoyl chloride',
                'nucleophile': 'C\u2082H\u2085OH',
                'nuc_name': 'ethanol',
                'product': 'CH\u2083CH\u2082COOC\u2082H\u2085',
                'product_name': 'ethyl propanoate (ester)',
                'by_product': 'HCl',
            },
            {
                'acyl_chloride': 'CH\u2083COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'C\u2086H\u2085OH',
                'nuc_name': 'phenol',
                'product': 'CH\u2083COOC\u2086H\u2085',
                'product_name': 'phenyl ethanoate (ester)',
                'by_product': 'HCl',
            },
        ]

        self.rxn = rnd.choice(reactions)
        correct = f"{self.rxn['product']} + {self.rxn['by_product']}"

        all_combos = [f"{r['product']} + {r['by_product']}" for r in reactions]
        wrong = [c for c in all_combos if c != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"{self.rxn['acyl_name']} reacts with {self.rxn['nuc_name']} at room temperature. "
            f"What are the products of this reaction?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "33.3 Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.rxn['acyl_chloride']} + {self.rxn['nucleophile']}}} "
            f"&\\rightarrow \\text{{{self.rxn['product']} + {self.rxn['by_product']}}}\\\\"
            f"\\text{{Product: {self.rxn['product_name']}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Addition-Elimination Mechanism", fontsize=16)

        y_level = 4.5
        ax.text(2, y_level, self.rxn['acyl_chloride'], fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.5))
        ax.text(2, y_level - 1, 'Acyl chloride', fontsize=11, ha='center', style='italic')

        ax.text(5, y_level + 0.3, "+", fontsize=16, ha='center', fontweight='bold')
        ax.text(5, y_level, self.rxn['nucleophile'], fontsize=13, ha='center',
               bbox=dict(boxstyle='round', facecolor='yellow', pad=0.3))
        ax.text(5, y_level - 0.6, self.rxn['nuc_name'], fontsize=10, ha='center', style='italic')

        draw_arrow(ax, 6.5, y_level, 8.5, y_level, color='black', linewidth=2)

        ax.text(11, y_level, "?", fontsize=28, ha='center', va='center', color='red',
               fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgray', edgecolor='black', linewidth=2, pad=0.5))
        ax.text(11, y_level - 1.2, "Products = ?", fontsize=12, ha='center')

        ax.text(7.5, y_level + 0.8, "addition-elimination", fontsize=10, ha='center', style='italic')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem072:
    """
    Topic: 33.3 Carboxylic acid derivatives - Hydrolysis reactivity
    Visual: Bar chart comparing relative rates of Cl-containing compounds
    Task: MCQ - arrange in order of hydrolysis reactivity
    10+ variations (randomized order of bars)
    """

    def __init__(self):
        # Randomise bar heights so student must READ the highlighted bar value
        self.acyl_rate  = rnd.randint(60, 140)   # acyl chloride: always highest
        self.alkyl_rate = rnd.randint(1, 9)       # alkyl: moderate
        self.aryl_rate  = round(rnd.uniform(0.0001, 0.009), 4)  # aryl: very slow

        compounds_data = [
            ('acyl chloride',  'CH\u2083COCl',   'Ethanoyl chloride\n(acyl chloride)',  self.acyl_rate),
            ('alkyl chloride', 'CH\u2083CH\u2082Cl', 'Chloroethane\n(alkyl chloride)',  self.alkyl_rate),
            ('aryl chloride',  'C\u2086H\u2085Cl',  'Chlorobenzene\n(aryl chloride)',    self.aryl_rate),
        ]
        rnd.shuffle(compounds_data)
        self.display_types     = [d[0] for d in compounds_data]
        self.display_compounds = [d[1] for d in compounds_data]
        self.display_names     = [d[2] for d in compounds_data]
        self.display_rates     = [d[3] for d in compounds_data]

        self.highlighted_idx  = rnd.randint(0, 2)
        self.highlighted_type = self.display_types[self.highlighted_idx]
        self.highlighted_rate = self.display_rates[self.highlighted_idx]
        self.answer = str(self.highlighted_rate)
        self.choices = []
        self.choices_display = {}

        self.description = (
            f"The bar chart shows the relative rates of hydrolysis of three chlorine-containing "
            f"compounds with water at room temperature. The highlighted bar is labelled with its "
            f"compound type. What is the relative rate of hydrolysis shown for the "
            f"{self.highlighted_type}?"
        )
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "33.3 Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Highlighted: {self.highlighted_type}}} &\\\\"
            f"\\text{{Bar height shown on diagram: {self.highlighted_rate}}} &\\\\"
            f"\\therefore \\text{{Answer = {self.highlighted_rate}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))

        x_positions = [1, 3, 5]
        colors = [rnd.choice(['red', 'orange', 'blue']) for _ in range(3)]

        draw_bar_chart(ax, x_positions, self.display_rates,
                      ['A', 'B', 'C'],
                      colors=colors, width=0.8,
                      xlabel='Compound type',
                      ylabel='Relative Rate of Hydrolysis (log scale)',
                      title='Reactivity of C-Cl Bonds towards Hydrolysis')

        for i, (x, compound) in enumerate(zip(x_positions, self.display_compounds)):
            ax.text(x, self.display_rates[i] + 1, compound,
                   fontsize=11, ha='center', fontweight='bold')

        ax.set_ylim(0, 115)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem073:
    """
    Topic: 33.3 Carboxylic acid derivatives - Acyl chloride reactions
    Visual: RCOCl + reagent → ? (product shown as ?)
    Task: MCQ - identify the organic product type
    10+ variations
    """

    def __init__(self):
        reactions = [
            ("water", "carboxylic acid", "H\u2082O", "RCOOH"),
            ("alcohol", "ester", "R'OH", "RCOOR'"),
            ("ammonia", "amide", "NH\u2083", "RCONH\u2082"),
            ("amine", "N-substituted amide", "R'NH\u2082", "RCONHR'"),
            ("phenol", "phenyl ester", "C\u2086H\u2085OH", "RCOOC\u2086H\u2085"),
            ("sodium hydroxide", "sodium salt of carboxylic acid", "NaOH", "RCOONa"),
            ("water (dilute NaOH)", "carboxylate salt", "NaOH(aq)", "RCOONa"),
            ("diamine", "polyamide (nylon)", "H\u2082N-R'-NH\u2082", "-CO-R-CO-NH-R'-NH-"),
            ("diol", "polyester", "HO-R'-OH", "-CO-R-COO-R'-O-"),
            ("secondary amine", "N,N-disubstituted amide", "R'R''NH", "RCON(R')(R'')"),
            ("ethanol", "ethyl ester", "C\u2082H\u2085OH", "RCOOC\u2082H\u2085"),
        ]

        self.reaction = rnd.choice(reactions)
        self.reagent_name = self.reaction[0]
        self.product_name = self.reaction[1]
        self.reagent_formula = self.reaction[2]
        self.products = self.reaction[3]

        correct = self.product_name
        all_products = [r[1] for r in reactions]
        wrong = [p for p in all_products if p != correct]
        options = rnd.sample(wrong, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows an acyl chloride (RCOCl) reacting with a reagent "
            f"whose formula is shown in the diagram. "
            f"What is the organic product formed?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "Acyl chloride reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{RCOCl}} + \\text{{{self.reagent_formula}}} &\\rightarrow \\text{{{self.products}}} + \\text{{HCl}}\\\\"
            f"\\text{{Organic product: {self.product_name}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        add_formula_label(ax, 2, 3, "RCOCl", fontsize=18, weight='bold')
        add_formula_label(ax, 4.5, 3, "+", fontsize=18, weight='bold')
        add_formula_label(ax, 6, 3, self.reagent_formula, fontsize=18, weight='bold')

        draw_arrow(ax, 7.5, 3, 9, 3, color='black', linewidth=3)

        add_formula_label(ax, 10.5, 3, "?", fontsize=24, weight='bold', color='red')

        add_title_box(ax, 6, 5.5, "Acyl Chloride Reactions", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem074:
    """
    Topic: 34.4 Amino acids - Zwitterion structure
    Visual: Three structures at different pH values WITHOUT zwitterion label
    Task: MCQ - which structure (A, B, or C) is the zwitterion?
    10+ variations
    """

    def __init__(self):
        amino_acids = [
            {
                'name': 'glycine',
                'formula': 'H\u2082NCH\u2082COOH',
                'isoelectric_point': 6.0,
                'low_pH': 'H\u2083N\u207aCH\u2082COOH',
                'zwitterion': 'H\u2083N\u207aCH\u2082COO\u207b',
                'high_pH': 'H\u2082NCH\u2082COO\u207b',
                'pI': 6.0,
            },
            {
                'name': 'alanine',
                'formula': 'H\u2082NCH(CH\u2083)COOH',
                'isoelectric_point': 6.0,
                'low_pH': 'H\u2083N\u207aCH(CH\u2083)COOH',
                'zwitterion': 'H\u2083N\u207aCH(CH\u2083)COO\u207b',
                'high_pH': 'H\u2082NCH(CH\u2083)COO\u207b',
                'pI': 6.0,
            },
            {
                'name': 'serine',
                'formula': 'H\u2082NCH(CH\u2082OH)COOH',
                'isoelectric_point': 5.7,
                'low_pH': 'H\u2083N\u207aCH(CH\u2082OH)COOH',
                'zwitterion': 'H\u2083N\u207aCH(CH\u2082OH)COO\u207b',
                'high_pH': 'H\u2082NCH(CH\u2082OH)COO\u207b',
                'pI': 5.7,
            },
            {
                'name': 'valine',
                'formula': 'H\u2082NCH(CH(CH\u2083)\u2082)COOH',
                'isoelectric_point': 6.0,
                'low_pH': 'H\u2083N\u207aCH(CH(CH\u2083)\u2082)COOH',
                'zwitterion': 'H\u2083N\u207aCH(CH(CH\u2083)\u2082)COO\u207b',
                'high_pH': 'H\u2082NCH(CH(CH\u2083)\u2082)COO\u207b',
                'pI': 6.0,
            },
            {
                'name': 'lysine',
                'formula': 'H\u2082N(CH\u2082)\u2084CH(NH\u2082)COOH',
                'isoelectric_point': 9.7,
                'low_pH': 'H\u2083N\u207a(CH\u2082)\u2084CH(NH\u2083\u207a)COOH',
                'zwitterion': 'H\u2082N(CH\u2082)\u2084CH(NH\u2083\u207a)COO\u207b',
                'high_pH': 'H\u2082N(CH\u2082)\u2084CH(NH\u2082)COO\u207b',
                'pI': 9.7,
            },
            {
                'name': 'aspartic acid',
                'formula': 'HOOCCH\u2082CH(NH\u2082)COOH',
                'isoelectric_point': 2.8,
                'low_pH': 'HOOCCH\u2082CH(NH\u2083\u207a)COOH',
                'zwitterion': '\u207bOOCCH\u2082CH(NH\u2083\u207a)COOH',
                'high_pH': '\u207bOOCCH\u2082CH(NH\u2082)COO\u207b',
                'pI': 2.8,
            },
            {
                'name': 'phenylalanine',
                'formula': 'C\u2086H\u2085CH\u2082CH(NH\u2082)COOH',
                'isoelectric_point': 5.5,
                'low_pH': 'C\u2086H\u2085CH\u2082CH(NH\u2083\u207a)COOH',
                'zwitterion': 'C\u2086H\u2085CH\u2082CH(NH\u2083\u207a)COO\u207b',
                'high_pH': 'C\u2086H\u2085CH\u2082CH(NH\u2082)COO\u207b',
                'pI': 5.5,
            },
            {
                'name': 'leucine',
                'formula': '(CH\u2083)\u2082CHCH\u2082CH(NH\u2082)COOH',
                'isoelectric_point': 6.0,
                'low_pH': '(CH\u2083)\u2082CHCH\u2082CH(NH\u2083\u207a)COOH',
                'zwitterion': '(CH\u2083)\u2082CHCH\u2082CH(NH\u2083\u207a)COO\u207b',
                'high_pH': '(CH\u2083)\u2082CHCH\u2082CH(NH\u2082)COO\u207b',
                'pI': 6.0,
            },
            {
                'name': 'glutamic acid',
                'formula': 'HOOCCH\u2082CH\u2082CH(NH\u2082)COOH',
                'isoelectric_point': 3.2,
                'low_pH': 'HOOCCH\u2082CH\u2082CH(NH\u2083\u207a)COOH',
                'zwitterion': '\u207bOOCCH\u2082CH\u2082CH(NH\u2083\u207a)COOH',
                'high_pH': '\u207bOOCCH\u2082CH\u2082CH(NH\u2082)COO\u207b',
                'pI': 3.2,
            },
            {
                'name': 'arginine',
                'formula': 'H\u2082NC(=NH)(CH\u2082)\u2083CH(NH\u2082)COOH',
                'isoelectric_point': 10.8,
                'low_pH': 'H\u2082NC(=NH\u2082\u207a)(CH\u2082)\u2083CH(NH\u2083\u207a)COOH',
                'zwitterion': 'H\u2082NC(=NH)(CH\u2082)\u2083CH(NH\u2083\u207a)COO\u207b',
                'high_pH': 'H\u2082NC(=NH)(CH\u2082)\u2083CH(NH\u2082)COO\u207b',
                'pI': 10.8,
            },
        ]

        self.aa = rnd.choice(amino_acids)

        # Randomize which box shows which structure
        structures = [
            ('A', 'pH 2 (acidic)', self.aa['low_pH'], 'lightcoral', '+1'),
            ('B', f"pH {self.aa['isoelectric_point']} (isoelectric)", self.aa['zwitterion'], 'lightyellow', '0'),
            ('C', 'pH 10 (alkaline)', self.aa['high_pH'], 'lightblue', '-1'),
        ]
        rnd.shuffle(structures)
        self.structures = structures

        # Find which label has the zwitterion (charge 0)
        zwitterion_label = None
        for label, ph_label, formula, color, charge in structures:
            if charge == '0':
                zwitterion_label = label
                break

        correct = zwitterion_label
        options = ["A", "B", "C", "Cannot be determined"]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows the structure of {self.aa['name']} at three different pH values. "
            f"Which structure (A, B, or C) represents the zwitterion?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Nitrogen compounds"
        self.subtopic = "34.4 Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Zwitterion has both NH\u2083\u207a and COO\u207b groups}}&\\\\"
            f"\\text{{Overall charge = 0 at isoelectric point (pH = {self.aa['pI']})}}&\\\\"
            f"\\text{{Answer: {correct}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 6.5, f"{self.aa['name'].capitalize()} at Different pH Values", fontsize=16)

        x_positions = [0.5, 5.0, 9.5]
        for i, (label, ph_label, formula, color, charge) in enumerate(self.structures):
            x = x_positions[i]
            ax.text(x + 2, 5.8, f"Structure {label}", fontsize=13, ha='center',
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgray', pad=0.3))
            draw_labeled_box(ax, x, 3.0, 3.8, 1.8, formula, ph_label,
                            facecolor=color, edgecolor='black', linewidth=2)
            ax.text(x + 1.9, 2.5, f"Charge: {charge}", fontsize=11, ha='center', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem075:
    """
    Topic: 34.4 Amino acids - Electrophoresis
    Visual: Electrophoresis strip with start point (NO arrow showing migration direction)
    Task: MCQ - which direction does the amino acid migrate?
    10+ variations
    """

    def __init__(self):
        scenarios = [
            {
                'pH': 6,
                'amino_acid': 'glycine',
                'pI': 6.0,
                'migration': 'no migration (stays at origin)',
            },
            {
                'pH': 6,
                'amino_acid': 'lysine',
                'pI': 9.7,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 6,
                'amino_acid': 'aspartic acid',
                'pI': 2.8,
                'migration': 'toward anode (positive electrode)',
            },
            {
                'pH': 7,
                'amino_acid': 'glycine',
                'pI': 6.0,
                'migration': 'toward anode (positive electrode)',
            },
            {
                'pH': 4,
                'amino_acid': 'alanine',
                'pI': 6.0,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 8,
                'amino_acid': 'lysine',
                'pI': 9.7,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 4,
                'amino_acid': 'glutamic acid',
                'pI': 3.2,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 5,
                'amino_acid': 'leucine',
                'pI': 6.0,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 8,
                'amino_acid': 'aspartic acid',
                'pI': 2.8,
                'migration': 'toward anode (positive electrode)',
            },
            {
                'pH': 9,
                'amino_acid': 'arginine',
                'pI': 10.8,
                'migration': 'toward cathode (negative electrode)',
            },
            {
                'pH': 10,
                'amino_acid': 'lysine',
                'pI': 9.7,
                'migration': 'toward anode (positive electrode)',
            },
            {
                'pH': 6,
                'amino_acid': 'phenylalanine',
                'pI': 5.5,
                'migration': 'toward anode (positive electrode)',
            },
        ]

        self.scenario = rnd.choice(scenarios)

        correct = self.scenario['migration']
        options = [
            'toward anode (positive electrode)',
            'toward cathode (negative electrode)',
            'no migration (stays at origin)',
            'migration in both directions',
        ]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.description = (
            f"The diagram shows an electrophoresis strip for an amino acid "
            f"at a given pH and isoelectric point (pI). Both values are shown in the diagram. "
            f"In which direction will the amino acid migrate when voltage is applied?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.choices))
        self.topic = "Nitrogen compounds"
        self.subtopic = "34.4 Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{pH of buffer: {self.scenario['pH']}}}&\\\\"
            f"\\text{{Isoelectric point (pI): {self.scenario['pI']}}}&\\\\"
            f"\\text{{If pH > pI: amino acid is negative, migrates to anode}}&\\\\"
            f"\\text{{If pH < pI: amino acid is positive, migrates to cathode}}&\\\\"
            f"\\text{{If pH = pI: no net charge, no migration}}&\\\\"
            f"\\text{{Answer: {correct}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, f"Electrophoresis at pH {self.scenario['pH']}", fontsize=16)

        draw_labeled_box(ax, 12, 3, 1.5, 2, '+', 'Anode\n(positive)',
                        facecolor='lightcoral', edgecolor='red', linewidth=3)

        draw_labeled_box(ax, 0.5, 3, 1.5, 2, '\u2212', 'Cathode\n(negative)',
                        facecolor='lightblue', edgecolor='blue', linewidth=3)

        paper = patches.Rectangle((2.5, 3.5), 9, 1, facecolor='wheat',
                                  edgecolor='black', linewidth=2)
        ax.add_patch(paper)

        ax.plot(7, 4, 'ko', markersize=15)
        ax.text(7, 4.8, 'Start position', fontsize=11, ha='center', fontweight='bold')

        info = (f"Amino acid: {self.scenario['amino_acid']}\n"
               f"pI = {self.scenario['pI']}\n"
               f"Buffer pH = {self.scenario['pH']}")
        ax.text(7, 1.5, info, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow',
                        edgecolor='black', linewidth=2))


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem076:
    """
    Topic: 34.4 Amide formation
    Visual: Reaction scheme for amide synthesis
    Task: Identify reagents for amide formation (MCQ)
    """

    def __init__(self):
        methods = [
            {
                "name": "acyl chloride + ammonia",
                "reagents": "RCOCl + NH\u2083",
                "product": "primary amide (RCONH\u2082) + HCl",
                "conditions": "room temperature",
            },
            {
                "name": "acyl chloride + primary amine",
                "reagents": "RCOCl + RNH\u2082",
                "product": "N-substituted amide (RCONHR) + HCl",
                "conditions": "room temperature",
            },
            {
                "name": "acyl chloride + secondary amine",
                "reagents": "RCOCl + R\u2082NH",
                "product": "N,N-disubstituted amide + HCl",
                "conditions": "room temperature",
            },
            {
                "name": "carboxylic acid + amine + heat",
                "reagents": "RCOOH + RNH\u2082, \u0394",
                "product": "amide + H\u2082O",
                "conditions": "strong heating",
            },
            {
                "name": "acid anhydride + ammonia",
                "reagents": "(RCO)\u2082O + NH\u2083",
                "product": "primary amide + carboxylate salt",
                "conditions": "room temperature",
            },
            {
                "name": "acid anhydride + primary amine",
                "reagents": "(RCO)\u2082O + RNH\u2082",
                "product": "N-substituted amide + RCOOH",
                "conditions": "room temperature",
            },
            {
                "name": "ester + ammonia (ammonolysis)",
                "reagents": "RCOOR + NH\u2083 (excess)",
                "product": "primary amide + ROH",
                "conditions": "excess ammonia, heat",
            },
            {
                "name": "nitrile + partial hydrolysis",
                "reagents": "RCN + H\u2082O (limited), H\u207a cat.",
                "product": "amide (intermediate)",
                "conditions": "dilute acid, limited water, heat",
            },
            {
                "name": "acyl chloride + aniline",
                "reagents": "RCOCl + C\u2086H\u2085NH\u2082",
                "product": "N-phenyl amide + HCl",
                "conditions": "room temperature",
            },
            {
                "name": "acyl chloride + hydrazine",
                "reagents": "RCOCl + H\u2082NNH\u2082",
                "product": "acid hydrazide + HCl",
                "conditions": "room temperature",
            },
        ]

        all_names = [m["name"] for m in methods]
        self.method = rnd.choice(methods)
        self.method_name = self.method["name"]

        distractors = [m["name"] for m in methods if m["name"] != self.method_name]
        rnd.shuffle(distractors)
        options = [self.method_name] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.method_name))

        self.description = (
            f"The diagram shows a reaction scheme for amide formation. "
            f"The conditions are shown on the reaction arrow. "
            f"Which reagents are used in this method?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amide formation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Method: {self.method_name}}} &\\\\"
            f"\\text{{Reagents: {self.method['reagents']}}} &\\\\"
            f"\\text{{Product: {self.method['product']}}} &\\\\"
            f"\\text{{Conditions: {self.method['conditions']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Amide Formation", fontsize=16)

        draw_labeled_box(ax, 1, 3.5, 3, 1.2, "Carboxylic\nacid derivative",
                         facecolor='lightblue')

        draw_arrow(ax, 4, 4.2, 8, 4.2, label=self.method["conditions"],
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 9, 3.5, 2.5, 1.2, "Amide\nRCONH\u2082",
                         facecolor='lightgreen')


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem077:
    """
    Topic: 35.1 Condensation polymerisation - polyamide
    Visual: Diamine + diacid reaction scheme
    Task: Identify the repeat unit of the polyamide (MCQ)
    """

    def __init__(self):
        monomers = [
            {
                'diamine': '1,6-diaminohexane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2086NH\u2082',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2086NHCO(CH\u2082)\u2084CO-]',
                'polymer_name': 'Nylon 6,6',
            },
            {
                'diamine': '1,4-diaminobutane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2084NH\u2082',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2084NHCO(CH\u2082)\u2084CO-]',
                'polymer_name': 'Nylon 4,6',
            },
            {
                'diamine': '1,3-diaminopropane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2083NH\u2082',
                'diacid': 'butanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2082COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2083NHCO(CH\u2082)\u2082CO-]',
                'polymer_name': 'Nylon 3,4',
            },
            {
                'diamine': '1,6-diaminohexane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2086NH\u2082',
                'diacid': 'decanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2088COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2086NHCO(CH\u2082)\u2088CO-]',
                'polymer_name': 'Nylon 6,10',
            },
            {
                'diamine': '1,2-diaminoethane',
                'diamine_formula': 'H\u2082NCH\u2082CH\u2082NH\u2082',
                'diacid': 'propanedioic acid',
                'diacid_formula': 'HOOCCH\u2082COOH',
                'repeat_unit': '[-NHCH\u2082CH\u2082NHCOCH\u2082CO-]',
                'polymer_name': 'polyamide 2,3',
            },
            {
                'diamine': '1,4-diaminobutane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2084NH\u2082',
                'diacid': 'decanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2088COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2084NHCO(CH\u2082)\u2088CO-]',
                'polymer_name': 'Nylon 4,10',
            },
            {
                'diamine': '1,6-diaminohexane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2086NH\u2082',
                'diacid': 'pentanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2083COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2086NHCO(CH\u2082)\u2083CO-]',
                'polymer_name': 'Nylon 6,5',
            },
            {
                'diamine': '1,8-diaminooctane',
                'diamine_formula': 'H\u2082N(CH\u2082)\u2088NH\u2082',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-NH(CH\u2082)\u2088NHCO(CH\u2082)\u2084CO-]',
                'polymer_name': 'Nylon 8,6',
            },
            {
                'diamine': '1,3-diaminobenzene',
                'diamine_formula': 'H\u2082N-C\u2086H\u2084-NH\u2082 (1,3)',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-NH-C\u2086H\u2084-NHCO(CH\u2082)\u2084CO-]',
                'polymer_name': 'semi-aromatic polyamide',
            },
            {
                'diamine': '1,4-diaminobenzene',
                'diamine_formula': 'H\u2082N-C\u2086H\u2084-NH\u2082 (1,4)',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-NH-C\u2086H\u2084-NHCO-C\u2086H\u2084-CO-]',
                'polymer_name': 'Kevlar (aramid)',
            },
        ]

        self.mono = rnd.choice(monomers)
        correct = self.mono['repeat_unit']
        distractors = [m['repeat_unit'] for m in monomers if m['repeat_unit'] != correct]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The diagram shows two monomers reacting to form a polyamide. "
            f"The monomer structures are shown in the diagram. "
            f"Which of the following is the repeat unit of this polymer?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Polymerisation"
        self.subtopic = "35.1 Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diamine: {self.mono['diamine_formula']}}}&\\\\"
            f"\\text{{Diacid: {self.mono['diacid_formula']}}}&\\\\"
            "\\text{Condensation: -NH\u2082 + -COOH \u2192 -CONH- + H\u2082O}&\\\\"
            f"\\text{{Repeat unit: {self.mono['repeat_unit']}}}&\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, f"Polyamide Formation: {self.mono['polymer_name']}", fontsize=16)

        draw_labeled_box(ax, 1, 5.5, 3, 1,
                         self.mono['diamine_formula'],
                         self.mono['diamine'], facecolor='lightblue')

        ax.text(4.8, 6.0, '+', fontsize=20, ha='center', fontweight='bold')

        draw_labeled_box(ax, 5.5, 5.5, 3, 1,
                         self.mono['diacid_formula'],
                         self.mono['diacid'], facecolor='lightyellow')

        draw_arrow(ax, 9, 6.0, 11, 6.0, label="heat\n-H\u2082O",
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 11.5, 5.5, 2, 1, "Polyamide",
                         facecolor='lightgreen')

        ax.text(0.5, 4.5, "Possible repeat units:", fontsize=11,
                fontweight='bold', color='navy')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem078:
    """
    Topic: 35.1 Condensation polymerisation - polyester
    Visual: Diol + diacid reaction scheme
    Task: Identify the repeat unit of the polyester (MCQ)
    """

    def __init__(self):
        monomers = [
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH\u2082CH\u2082OH',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-OCH\u2082CH\u2082OOC-C\u2086H\u2084-CO-]',
                'polymer_name': 'PET (Terylene)',
            },
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH\u2082CH\u2082OH',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-OCH\u2082CH\u2082OOC(CH\u2082)\u2084CO-]',
                'polymer_name': 'polyester (aliphatic)',
            },
            {
                'diol': 'propane-1,3-diol',
                'diol_formula': 'HO(CH\u2082)\u2083OH',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-O(CH\u2082)\u2083OOC(CH\u2082)\u2084CO-]',
                'polymer_name': 'polytrimethylene adipate',
            },
            {
                'diol': 'butane-1,4-diol',
                'diol_formula': 'HO(CH\u2082)\u2084OH',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-O(CH\u2082)\u2084OOC-C\u2086H\u2084-CO-]',
                'polymer_name': 'PBT',
            },
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH\u2082CH\u2082OH',
                'diacid': 'propanedioic acid',
                'diacid_formula': 'HOOCCH\u2082COOH',
                'repeat_unit': '[-OCH\u2082CH\u2082OOCCH\u2082CO-]',
                'polymer_name': 'polyester (malonate)',
            },
            {
                'diol': 'butane-1,4-diol',
                'diol_formula': 'HO(CH\u2082)\u2084OH',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2084COOH',
                'repeat_unit': '[-O(CH\u2082)\u2084OOC(CH\u2082)\u2084CO-]',
                'polymer_name': 'polybutylene adipate',
            },
            {
                'diol': 'propane-1,2-diol',
                'diol_formula': 'HOCH\u2082CH(OH)CH\u2083',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-OCH\u2082CH(CH\u2083)OOC-C\u2086H\u2084-CO-]',
                'polymer_name': 'PTT',
            },
            {
                'diol': 'hexane-1,6-diol',
                'diol_formula': 'HO(CH\u2082)\u2086OH',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-O(CH\u2082)\u2086OOC-C\u2086H\u2084-CO-]',
                'polymer_name': 'PHT',
            },
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH\u2082CH\u2082OH',
                'diacid': 'butanedioic acid',
                'diacid_formula': 'HOOC(CH\u2082)\u2082COOH',
                'repeat_unit': '[-OCH\u2082CH\u2082OOC(CH\u2082)\u2082CO-]',
                'polymer_name': 'polyethylene succinate',
            },
            {
                'diol': 'cyclohexane-1,4-dimethanol',
                'diol_formula': 'HOCH\u2082-C\u2086H\u2081\u2080-CH\u2082OH',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C\u2086H\u2084-COOH',
                'repeat_unit': '[-OCH\u2082-C\u2086H\u2081\u2080-CH\u2082OOC-C\u2086H\u2084-CO-]',
                'polymer_name': 'PCTA',
            },
        ]

        self.mono = rnd.choice(monomers)
        correct = self.mono['repeat_unit']
        distractors = [m['repeat_unit'] for m in monomers if m['repeat_unit'] != correct]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The diagram shows two monomers reacting to form a polyester. "
            f"The monomer structures are shown in the diagram. "
            f"Which of the following is the repeat unit of this polymer?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Polymerisation"
        self.subtopic = "35.1 Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diol: {self.mono['diol_formula']}}}&\\\\"
            f"\\text{{Diacid: {self.mono['diacid_formula']}}}&\\\\"
            "\\text{Condensation: -OH + -COOH \u2192 -COO- + H\u2082O}&\\\\"
            f"\\text{{Repeat unit: {self.mono['repeat_unit']}}}&\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Polyester Formation", fontsize=16)

        draw_labeled_box(ax, 1, 5.5, 3, 1,
                         self.mono['diol_formula'],
                         self.mono['diol'], facecolor='lightblue')

        ax.text(4.8, 6.0, '+', fontsize=20, ha='center', fontweight='bold')

        draw_labeled_box(ax, 5.5, 5.5, 3, 1,
                         self.mono['diacid_formula'],
                         self.mono['diacid'], facecolor='lightyellow')

        draw_arrow(ax, 9, 6.0, 11, 6.0, label="heat\n-H\u2082O",
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 11.5, 5.5, 2, 1, "Polyester",
                         facecolor='lightgreen')

        ax.text(0.5, 4.5, "Possible repeat units:", fontsize=11,
                fontweight='bold', color='navy')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem079:
    """
    Topic: 35.1 Addition polymerization
    Visual: Polymer repeat unit shown in brackets
    Task: Identify the monomer from the polymer structure (MCQ)
    """

    def __init__(self):
        polymers = [
            ("poly(ethene)", "CH\u2082=CH\u2082", "-(CH\u2082-CH\u2082)n-"),
            ("poly(propene)", "CH\u2082=CHCH\u2083", "-(CH\u2082-CH(CH\u2083))n-"),
            ("poly(chloroethene)", "CH\u2082=CHCl", "-(CH\u2082-CHCl)n-"),
            ("poly(tetrafluoroethene)", "CF\u2082=CF\u2082", "-(CF\u2082-CF\u2082)n-"),
            ("poly(phenylethene)", "CH\u2082=CHC\u2086H\u2085", "-(CH\u2082-CH(C\u2086H\u2085))n-"),
            ("poly(acrylonitrile)", "CH\u2082=CHCN", "-(CH\u2082-CH(CN))n-"),
            ("poly(methyl methacrylate)", "CH\u2082=C(CH\u2083)COOCH\u2083", "-(CH\u2082-C(CH\u2083)(COOCH\u2083))n-"),
            ("poly(vinyl acetate)", "CH\u2082=CHOOCCH\u2083", "-(CH\u2082-CH(OOCCH\u2083))n-"),
            ("poly(1,1-difluoroethene)", "CH\u2082=CF\u2082", "-(CH\u2082-CF\u2082)n-"),
            ("poly(but-1-ene)", "CH\u2082=CHCH\u2082CH\u2083", "-(CH\u2082-CH(CH\u2082CH\u2083))n-"),
            ("poly(isoprene)", "CH\u2082=C(CH\u2083)CH=CH\u2082", "-(CH\u2082-C(CH\u2083)=CH-CH\u2082)n-"),
        ]

        self.polymer = rnd.choice(polymers)
        self.polymer_name = self.polymer[0]
        self.monomer_formula = self.polymer[1]
        self.polymer_formula = self.polymer[2]

        distractors = [p[1] for p in polymers if p[1] != self.monomer_formula]
        rnd.shuffle(distractors)
        options = [self.monomer_formula] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.monomer_formula))

        self.description = (
            f"The repeating unit of {self.polymer_name} is shown. "
            f"What is the monomer used to make this polymer?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Polymerisation"
        self.subtopic = "Addition polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Polymer: {self.polymer_formula}}} &\\\\"
            "\\text{Reverse: restore C=C double bond} &\\\\"
            f"\\text{{Monomer: {self.monomer_formula}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')

        add_title_box(ax, 6, 5.5, "Addition Polymerization", fontsize=16)

        draw_bracket(ax, 3.5, 2.5, height=1.5, bracket_type='square', direction='left')
        add_formula_label(ax, 5.5, 3.2, self.polymer_formula, fontsize=16, weight='bold')
        draw_bracket(ax, 7.5, 2.5, height=1.5, bracket_type='square', direction='right',
                     subscript='n')

        ax.text(6, 1.5, "Repeat unit", fontsize=11, ha='center', color='gray', style='italic')


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem080:
    """
    Topic: 35.3 Polymer biodegradability
    Visual: Comparison table of polymers (biodegradable column shown as ?)
    Task: Identify which polymer(s) is/are biodegradable (MCQ)
    """

    def __init__(self):
        scenarios = [
            {
                'question': "Which polymer(s) is/are biodegradable?",
                'answer_key': 'B',
                'options': [
                    "Poly(ethene) only",
                    "Polyester and polyamide only",
                    "All three are biodegradable",
                    "None are biodegradable",
                ],
            },
            {
                'question': "Which polymer cannot be hydrolysed by enzymes?",
                'answer_key': 'A',
                'options': [
                    "Poly(ethene)",
                    "Polyamide",
                    "Polyester",
                    "Both polyester and polyamide",
                ],
            },
            {
                'question': "Which bond type makes condensation polymers biodegradable?",
                'answer_key': 'C',
                'options': [
                    "C-C bonds (non-polar)",
                    "C-H bonds (non-polar)",
                    "Ester and amide linkages (hydrolysable)",
                    "C-F bonds (very strong)",
                ],
            },
            {
                'question': "Why is poly(ethene) not biodegradable?",
                'answer_key': 'D',
                'options': [
                    "It contains ester linkages",
                    "It contains amide linkages",
                    "Its chains are too long",
                    "It only contains C-C and C-H bonds which cannot be hydrolysed",
                ],
            },
            {
                'question': "Which polymer type degrades by hydrolysis of its linkage?",
                'answer_key': 'B',
                'options': [
                    "Poly(ethene) (addition polymer)",
                    "Polyester and polyamide (condensation polymers)",
                    "Poly(chloroethene) (vinyl polymer)",
                    "Poly(styrene) (addition polymer)",
                ],
            },
            {
                'question': "What byproduct is released when a polyester biodegrades?",
                'answer_key': 'A',
                'options': [
                    "Diol and diacid monomers (via hydrolysis)",
                    "Ethene and water only",
                    "Carbon dioxide and water",
                    "HCl gas",
                ],
            },
            {
                'question': "Which statement about polymer degradability is correct?",
                'answer_key': 'C',
                'options': [
                    "All polymers are biodegradable over time",
                    "Only natural polymers are biodegradable",
                    "Condensation polymers can be hydrolysed; addition polymers cannot",
                    "Biodegradability depends only on chain length",
                ],
            },
            {
                'question': "What type of linkage is present in a biodegradable polyamide?",
                'answer_key': 'D',
                'options': [
                    "Ether linkage (-C-O-C-)",
                    "Alkyl linkage (-C-C-)",
                    "Ester linkage (-COO-)",
                    "Amide linkage (-CONH-)",
                ],
            },
            {
                'question': "Which reagent can hydrolyse both polyester and polyamide?",
                'answer_key': 'A',
                'options': [
                    "Aqueous acid or aqueous base (with heat)",
                    "Organic solvent alone",
                    "Concentrated sulfuric acid only",
                    "UV light only",
                ],
            },
            {
                'question': "What linkage is present in PET (polyester) that allows hydrolysis?",
                'answer_key': 'B',
                'options': [
                    "Amide linkage (-CONH-)",
                    "Ester linkage (-COO-)",
                    "Ether linkage (-C-O-C-)",
                    "Carbon-carbon bond (-C-C-)",
                ],
            },
        ]

        self.scenario = rnd.choice(scenarios)
        self.answer = self.scenario['answer_key']
        self.options = self.scenario['options']

        self.description = (
            f"The table compares three types of polymers: poly(ethene), polyester, and polyamide. "
            f"{self.scenario['question']}"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Polymerisation"
        self.subtopic = "35.3 Degradable polymers"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Poly(ethene): Not biodegradable}&\\\\"
            "\\text{- Only C-C and C-H bonds, chemically inert}&\\\\"
            "\\text{Polyester: Biodegradable}&\\\\"
            "\\text{- Ester linkages (-COO-) can be hydrolysed}&\\\\"
            "\\text{Polyamide: Biodegradable}&\\\\"
            "\\text{- Amide linkages (-CONH-) can be hydrolysed}&\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 6.5, 7.5, "Polymer Biodegradability", fontsize=16)

        polymers = ['Poly(ethene)', 'Polyester', 'Polyamide']
        linkages = ['C-C', 'Ester (-COO-)', 'Amide (-CONH-)']
        mechanisms = [
            'Chemically inert\nNo hydrolyzable bonds',
            'Ester hydrolysis\nby enzymes/acid/base',
            'Amide hydrolysis\nby enzymes/acid/base',
        ]

        headers = ['Polymer', 'Linkage', 'Biodegradable?', 'Mechanism']
        col_x = [0.5, 3.5, 6.5, 9.5]
        for i, header in enumerate(headers):
            ax.text(col_x[i], 6.5, header, fontsize=12, ha='center', fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='lightgray',
                              edgecolor='black', linewidth=2))

        for row_idx in range(3):
            y = 6.5 - (row_idx + 1) * 1.0
            color_map = ['lightcoral', 'lightgreen', 'lightblue']
            ax.text(col_x[0], y, polymers[row_idx], fontsize=11, ha='center',
                    bbox=dict(boxstyle='round', facecolor=color_map[row_idx], pad=0.3))
            ax.text(col_x[1], y, linkages[row_idx], fontsize=11, ha='center',
                    bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))
            ax.text(col_x[2], y, "?", fontsize=16, ha='center', fontweight='bold')
            ax.text(col_x[3], y, mechanisms[row_idx], fontsize=9, ha='center',
                    bbox=dict(boxstyle='round', facecolor='wheat', pad=0.3))



        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem081:
    """
    Topic: 35.3 Condensation polymerization
    Visual: Monomers shown without product labeled
    Task: Identify type of polymer formed (MCQ)
    """

    def __init__(self):
        polymers = [
            ("polyester", "diol + dicarboxylic acid", "ester linkage -COO-",
             "HO-R-OH", "HOOC-R\u2019-COOH", 'lightblue', 'lightcoral'),
            ("polyamide", "diamine + dicarboxylic acid", "amide linkage -CONH-",
             "H\u2082N-R-NH\u2082", "HOOC-R\u2019-COOH", 'lightyellow', 'lightcoral'),
            ("polyester (from hydroxy acid)", "hydroxy acid only", "ester linkage -COO-",
             "HO-R-COOH", "(same monomer \u00d72)", 'lightgreen', 'lightgreen'),
            ("polyamide (from amino acid)", "amino acid only", "amide linkage -CONH-",
             "H\u2082N-R-COOH", "(same monomer \u00d72)", 'lavender', 'lavender'),
            ("polyester", "ethane-1,2-diol + benzene-1,4-dicarboxylic acid",
             "ester linkage -COO-", "HOCH\u2082CH\u2082OH", "HOOC-C\u2086H\u2084-COOH",
             'lightblue', 'lightyellow'),
            ("polyamide", "1,6-diaminohexane + hexanedioic acid",
             "amide linkage -CONH-", "H\u2082N(CH\u2082)\u2086NH\u2082", "HOOC(CH\u2082)\u2084COOH",
             'lightyellow', 'lightcoral'),
            ("polyamide", "p-phenylenediamine + benzene-1,4-dicarbonyl chloride",
             "amide linkage -CONH-", "H\u2082N-C\u2086H\u2084-NH\u2082", "ClOC-C\u2086H\u2084-COCl",
             'lightyellow', 'lightgray'),
            ("polyester", "propane-1,3-diol + hexanedioic acid",
             "ester linkage -COO-", "HO(CH\u2082)\u2083OH", "HOOC(CH\u2082)\u2084COOH",
             'lightblue', 'lightcoral'),
            ("polyamide (from amino acid)", "glycine (H\u2082NCH\u2082COOH) only",
             "amide linkage -CONH-", "H\u2082NCH\u2082COOH", "(same monomer \u00d72)",
             'lavender', 'lavender'),
            ("polyester (from hydroxy acid)", "lactic acid (CH\u2083CH(OH)COOH) only",
             "ester linkage -COO-", "CH\u2083CH(OH)COOH", "(same monomer \u00d72)",
             'lightgreen', 'lightgreen'),
        ]

        self.polymer = rnd.choice(polymers)
        self.polymer_type = self.polymer[0]
        self.monomers = self.polymer[1]
        self.linkage = self.polymer[2]

        options = ["polyester", "polyamide", "addition polymer", "polyurethane"]
        correct = self.polymer_type.split()[0] if "from" not in self.polymer_type else self.polymer_type.split("(")[0].strip()
        if "polyester" in self.polymer_type:
            correct = "polyester"
        elif "polyamide" in self.polymer_type:
            correct = "polyamide"

        self.answer = chr(65 + options.index(correct))
        self.options = options

        self.description = (
            f"The diagram shows monomers used in condensation polymerization. "
            f"The functional groups are shown in the diagram. "
            f"What type of polymer is formed?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Polymerisation"
        self.subtopic = "Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Monomers: {self.monomers}}} &\\\\"
            f"\\text{{Linkage: {self.linkage}}} &\\\\"
            f"\\therefore \\text{{Polymer type: {correct}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Condensation Polymerization", fontsize=16)

        draw_labeled_box(ax, 0.5, 4.5, 2.5, 1,
                         self.polymer[3] + "\n(monomer 1)", facecolor=self.polymer[5])
        if self.polymer[4] != "(same monomer x2)":
            draw_labeled_box(ax, 0.5, 2.5, 2.5, 1,
                             self.polymer[4] + "\n(monomer 2)", facecolor=self.polymer[6])

        draw_arrow(ax, 3.5, 3.8, 7.5, 3.8, label="+ heat\n-H\u2082O",
                   label_position='above', color='red', linewidth=2.5)

        ax.text(9, 3.8, "?", fontsize=36, ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='lightgray', pad=0.5))


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem082:
    """
    Topic: 36.1 Organic synthesis routes
    Visual: Multi-step synthesis pathway with intermediate box hidden
    Task: Identify the intermediate compound (MCQ)
    """

    def __init__(self):
        routes = [
            {
                'start': 'benzene',
                'end': 'phenylamine',
                'intermediate': 'nitrobenzene',
                'int_formula': 'C\u2086H\u2085NO\u2082',
                'step1_label': 'conc. HNO\u2083/H\u2082SO\u2084\n50\u201360\u00b0C',
                'step2_label': 'Sn/conc. HCl\nthen NaOH',
                'distractors': ['phenol', 'aniline sulfate', 'benzoic acid'],
            },
            {
                'start': 'ethene',
                'end': 'ethanoic acid',
                'intermediate': 'ethanol',
                'int_formula': 'C\u2082H\u2085OH',
                'step1_label': 'H\u2082O/H\u2083PO\u2084\ncatalyst',
                'step2_label': 'acidified K\u2082Cr\u2082O\u2087\nreflux',
                'distractors': ['ethanal', 'ethene oxide', 'ethyl ethanoate'],
            },
            {
                'start': 'propan-1-ol',
                'end': 'propanoic acid',
                'intermediate': 'propanal',
                'int_formula': 'CH\u2083CH\u2082CHO',
                'step1_label': 'acidified K\u2082Cr\u2082O\u2087\ndistil',
                'step2_label': 'acidified K\u2082Cr\u2082O\u2087\nreflux',
                'distractors': ['propanone', 'propan-2-ol', 'propanoyl chloride'],
            },
            {
                'start': 'methylbenzene',
                'end': '4-nitromethylbenzene',
                'intermediate': 'methylbenzene (activated ring)',
                'int_formula': 'C\u2086H\u2085CH\u2083',
                'step1_label': 'conc. HNO\u2083/H\u2082SO\u2084\n<50\u00b0C',
                'step2_label': '(para product\nformed)',
                'distractors': ['benzaldehyde', 'benzoic acid', 'nitrobenzene'],
            },
            {
                'start': 'ethanol',
                'end': 'bromoethane',
                'intermediate': 'ethene',
                'int_formula': 'CH\u2082=CH\u2082',
                'step1_label': 'conc. H\u2082SO\u2084\n170\u00b0C',
                'step2_label': 'HBr\n(addition)',
                'distractors': ['diethyl ether', 'ethanoic acid', 'ethyl bromide directly'],
            },
            {
                'start': 'bromoethane',
                'end': 'ethylamine',
                'intermediate': 'ethanenitrile',
                'int_formula': 'CH\u2083CN',
                'step1_label': 'NaCN/ethanol\nheat',
                'step2_label': 'LiAlH\u2084\ndry ether',
                'distractors': ['ethanol', 'ethanoic acid', 'diethylamine'],
            },
            {
                'start': 'benzene',
                'end': 'benzoic acid',
                'intermediate': 'bromobenzene',
                'int_formula': 'C\u2086H\u2085Br',
                'step1_label': 'Br\u2082/AlBr\u2083\n(electrophilic sub.)',
                'step2_label': 'Mg, then CO\u2082,\nthen H\u2082O',
                'distractors': ['nitrobenzene', 'phenol', 'benzaldehyde'],
            },
            {
                'start': 'ethanoic acid',
                'end': 'ethyl ethanoate',
                'intermediate': 'ethanoyl chloride',
                'int_formula': 'CH\u2083COCl',
                'step1_label': 'PCl\u2085 or SOCl\u2082',
                'step2_label': 'ethanol\n(ROH)',
                'distractors': ['acetic anhydride', 'ethanol', 'ethanoate ion'],
            },
            {
                'start': 'cyclohexene',
                'end': 'cyclohexanone',
                'intermediate': 'cyclohexanol',
                'int_formula': 'C\u2086H\u2081\u2081OH',
                'step1_label': 'H\u2082O/H\u207a\n(addition)',
                'step2_label': 'acidified K\u2082Cr\u2082O\u2087\nheat',
                'distractors': ['cyclohexane', 'cyclohexanediol', 'cyclohexyl chloride'],
            },
            {
                'start': 'propene',
                'end': 'propan-2-ol',
                'intermediate': '2-bromopropane',
                'int_formula': 'CH\u2083CHBrCH\u2083',
                'step1_label': 'HBr\n(Markovnikov)',
                'step2_label': 'NaOH(aq)\nheat',
                'distractors': ['1-bromopropane', 'propan-1-ol', 'propanone'],
            },
        ]

        self.route = rnd.choice(routes)
        correct = self.route['intermediate']
        options = [correct] + self.route['distractors']
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The diagram shows a two-step synthesis from {self.route['start']} to {self.route['end']}. "
            f"The intermediate compound is hidden. What is the intermediate?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Organic synthesis"
        self.subtopic = "36.1 Organic synthesis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step 1: {self.route['start']} + ({self.route['step1_label'].split(chr(10))[0]}) \u2192 intermediate}} &\\\\"
            f"\\text{{Intermediate: {self.route['intermediate']} ({self.route['int_formula']})}} &\\\\"
            f"\\text{{Step 2: intermediate \u2192 {self.route['end']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 6.5,
                      f"Synthesis: {self.route['start']} \u2192 {self.route['end']}",
                      fontsize=15)

        draw_labeled_box(ax, 0.5, 3.5, 2.5, 1, self.route['start'], facecolor='lightblue')

        draw_arrow(ax, 3.0, 4.0, 5.0, 4.0, label=self.route['step1_label'],
                   label_position='above', color='black', linewidth=2.5)

        ax.text(6.25, 4.0, "?", fontsize=32, ha='center', va='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgray', pad=0.5,
                          edgecolor='black', linewidth=2))
        ax.text(6.25, 3.2, "Intermediate", fontsize=10, ha='center', color='gray', style='italic')

        draw_arrow(ax, 7.5, 4.0, 9.5, 4.0, label=self.route['step2_label'],
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 9.5, 3.5, 2.5, 1, self.route['end'], facecolor='lightgreen')


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem083:
    """
    Topic: 36.1 Organic synthesis routes
    Visual: Three-box pathway with middle box hidden
    Task: Identify intermediate compound (MCQ)
    """

    def __init__(self):
        pathways = [
            {
                'route': "alkane \u2192 ? \u2192 alcohol",
                'start': 'alkane', 'end': 'alcohol',
                'intermediate': 'haloalkane',
                'distractors': ['alkene', 'aldehyde', 'carboxylic acid'],
            },
            {
                'route': "alcohol \u2192 ? \u2192 carboxylic acid",
                'start': 'alcohol', 'end': 'carboxylic acid',
                'intermediate': 'aldehyde',
                'distractors': ['ketone', 'ester', 'alkene'],
            },
            {
                'route': "alkene \u2192 ? \u2192 ketone",
                'start': 'alkene', 'end': 'ketone',
                'intermediate': 'secondary alcohol',
                'distractors': ['primary alcohol', 'aldehyde', 'haloalkane'],
            },
            {
                'route': "benzene \u2192 ? \u2192 phenylamine",
                'start': 'benzene', 'end': 'phenylamine',
                'intermediate': 'nitrobenzene',
                'distractors': ['phenol', 'bromobenzene', 'benzoic acid'],
            },
            {
                'route': "haloalkane \u2192 ? \u2192 amine",
                'start': 'haloalkane', 'end': 'amine',
                'intermediate': 'nitrile',
                'distractors': ['alkene', 'alcohol', 'amide'],
            },
            {
                'route': "alkene \u2192 ? \u2192 diol",
                'start': 'alkene', 'end': 'diol',
                'intermediate': 'halohydrin',
                'distractors': ['epoxide', 'alkane', 'ketone'],
            },
            {
                'route': "carboxylic acid \u2192 ? \u2192 ester",
                'start': 'carboxylic acid', 'end': 'ester',
                'intermediate': 'acyl chloride',
                'distractors': ['anhydride', 'aldehyde', 'amide'],
            },
            {
                'route': "alcohol \u2192 ? \u2192 haloalkane",
                'start': 'alcohol', 'end': 'haloalkane',
                'intermediate': 'alkene',
                'distractors': ['aldehyde', 'ether', 'carboxylic acid'],
            },
            {
                'route': "nitrile \u2192 ? \u2192 amine",
                'start': 'nitrile', 'end': 'amine',
                'intermediate': 'imine (partial reduction intermediate)',
                'distractors': ['amide', 'alcohol', 'aldehyde'],
            },
            {
                'route': "primary alcohol \u2192 ? \u2192 carboxylic acid",
                'start': 'primary alcohol', 'end': 'carboxylic acid',
                'intermediate': 'aldehyde',
                'distractors': ['ketone', 'ester', 'acyl chloride'],
            },
        ]

        self.pathway = rnd.choice(pathways)
        correct = self.pathway['intermediate']
        options = [correct] + self.pathway['distractors']
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The diagram shows a multi-step synthesis route with a hidden intermediate. "
            f"The starting material and final product are shown in the diagram. "
            f"Identify the intermediate compound."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Organic synthesis"
        self.subtopic = "Synthesis routes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Route: {self.pathway['route']}}} &\\\\"
            f"\\text{{Intermediate: {self.pathway['intermediate']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')

        steps = [self.pathway['start'], '?', self.pathway['end']]

        x_pos = 1
        colors = ['lightblue', 'lightgray', 'lightgreen']
        for i, (step, color) in enumerate(zip(steps, colors)):
            draw_labeled_box(ax, x_pos, 2.5, 2.5, 1.2, step, facecolor=color)
            if step == '?':
                ax.text(x_pos + 1.25, 3.1, '?', fontsize=28, ha='center',
                        fontweight='bold', color='gray')

            if i < len(steps) - 1:
                draw_arrow(ax, x_pos + 2.5, 3.1, x_pos + 4, 3.1,
                           color='black', linewidth=2)

            x_pos += 4

        add_title_box(ax, 7, 5.5, "Multi-Step Synthesis", fontsize=16)


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem084:
    """
    Topic: 37.1 Mass spectrometry fragmentation
    Visual: Mass spectrum - questioned peak shown in same colour as others
    Task: Identify fragment ion from m/z value (MCQ)
    """

    def __init__(self):
        fragments = [
            ("CH\u2083\u207a", 15, "methyl cation", ["C\u2082H\u2085\u207a", "CHO\u207a", "C\u2082H\u2083\u207a"]),
            ("C\u2082H\u2085\u207a", 29, "ethyl cation", ["CH\u2083\u207a", "CHO\u207a", "C\u2083H\u2085\u207a"]),
            ("C\u2083H\u2087\u207a", 43, "propyl cation", ["C\u2083H\u2085\u207a", "C\u2082H\u2085\u207a", "CH\u2083CO\u207a"]),
            ("CHO\u207a", 29, "formyl/acyl cation", ["C\u2082H\u2085\u207a", "CH\u2083\u207a", "C\u2082H\u2083\u207a"]),
            ("C\u2086H\u2085\u207a", 77, "phenyl cation", ["C\u2085H\u2085\u207a", "C\u2086H\u2087\u207a", "C\u2087H\u2087\u207a"]),
            ("CH\u2083CO\u207a", 43, "acetyl cation", ["C\u2083H\u2087\u207a", "C\u2082H\u2085\u207a", "C\u2083H\u2085\u207a"]),
            ("C\u2086H\u2085CO\u207a", 105, "benzoyl cation", ["C\u2086H\u2085\u207a", "C\u2087H\u2087\u207a", "C\u2085H\u2085\u207a"]),
            ("C\u2087H\u2087\u207a", 91, "tropylium cation", ["C\u2086H\u2085\u207a", "C\u2086H\u2085CO\u207a", "C\u2087H\u2085\u207a"]),
            ("C\u2084H\u2089\u207a", 57, "butyl cation", ["C\u2084H\u2087\u207a", "C\u2083H\u2087\u207a", "C\u2082H\u2085CO\u207a"]),
            ("OCH\u2083\u207a", 31, "methoxy cation", ["CH\u2083\u207a", "C\u2082H\u2083\u207a", "CHO\u207a"]),
            ("C\u2082H\u2083\u207a", 27, "vinyl cation", ["C\u2082H\u2085\u207a", "CH\u2083\u207a", "CHO\u207a"]),
        ]

        self.fragment = rnd.choice(fragments)
        self.ion = self.fragment[0]
        self.mz = self.fragment[1]
        self.name = self.fragment[2]

        options = [self.ion] + list(self.fragment[3])
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.ion))

        n_other = rnd.randint(2, 3)
        other_mzs = set()
        while len(other_mzs) < n_other:
            candidate = rnd.randint(20, 150)
            if abs(candidate - self.mz) > 5:
                other_mzs.add(candidate)
        self.other_peaks = list(other_mzs)

        self.description = (
            f"The mass spectrum shows several peaks. The annotated peak is indicated "
            f"with an arrow showing its m/z value. "
            f"Identify the fragment ion responsible for this labelled peak."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Analytical techniques"
        self.subtopic = "Mass spectrometry"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{m/z = {self.mz}}} &\\\\"
            f"\\text{{Calculate molecular mass of each option:}} &\\\\"
            f"\\text{{Fragment ion: {self.ion} ({self.name})}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        all_peaks = [(self.mz, 100)] + [(p, rnd.randint(20, 60)) for p in self.other_peaks]

        for mz_val, intensity in all_peaks:
            draw_mass_spectrum_peak(ax, mz_val, intensity, width=2, color='steelblue',
                                    label_offset=3)

        ax.set_xlabel('m/z', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative abundance (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum (identify peak at m/z = {self.mz})',
                     fontsize=14, fontweight='bold')
        ax.set_xlim(0, max([p[0] for p in all_peaks]) + 20)
        ax.set_ylim(0, 120)
        ax.grid(axis='y', alpha=0.3)

        ax.annotate(f'm/z = {self.mz}',
                    xy=(self.mz, 100), xytext=(self.mz + 10, 108),
                    fontsize=10, color='red', fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.5))


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem085:
    """
    Topic: 37.1 Thin-layer chromatography
    Visual: TLC plate with spots and solvent front marked
    Task: Calculate Rf value (numerical)
    """

    def __init__(self):
        self.num_spots = rnd.randint(2, 4)
        self.solvent_front = 10.0

        self.spots = []
        used_heights = set()
        for i in range(self.num_spots):
            while True:
                spot_height = round(rnd.uniform(2.0, 9.0), 1)
                if spot_height not in used_heights:
                    used_heights.add(spot_height)
                    break
            rf_value = round(spot_height / self.solvent_front, 2)
            self.spots.append({
                'name': f'Compound {chr(65+i)}',
                'height': spot_height,
                'rf': rf_value,
            })

        self.spots.sort(key=lambda x: x['height'])
        self.questioned_spot = rnd.choice(self.spots)
        self.answer = self.questioned_spot['rf']

        self.description = (
            f"The diagram shows a TLC plate from a chromatography experiment. "
            f"The distances are annotated on the diagram. "
            f"Calculate the Rf value for {self.questioned_spot['name']}."
        )

        self.topic = "Analytical techniques"
        self.subtopic = "37.1 Thin-layer chromatography"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "R_f &= \\frac{\\text{distance traveled by substance}}{\\text{distance traveled by solvent}}\\\\"
            f"R_f &= \\frac{{{self.questioned_spot['height']}}}{{{self.solvent_front}}}\\\\"
            f"R_f &= {self.questioned_spot['rf']}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.axis('off')

        add_title_box(ax, 5, 11.5, "Thin-Layer Chromatography", fontsize=16)

        plate = patches.Rectangle((2, 1), 6, 9, facecolor='lightgray',
                                   edgecolor='black', linewidth=2)
        ax.add_patch(plate)

        ax.plot([2, 8], [2, 2], 'k-', linewidth=2)
        ax.text(1, 2, 'Baseline', fontsize=11, ha='right', fontweight='bold')

        solvent_y = 2 + (self.solvent_front / 10) * 8
        ax.plot([2, 8], [solvent_y, solvent_y], 'b--', linewidth=2)
        ax.text(8.5, solvent_y, 'Solvent\nfront', fontsize=11, ha='left',
                fontweight='bold', color='blue')

        draw_vertical_annotation(ax, 1.5, 2, solvent_y, f'{self.solvent_front} cm',
                                 color='blue', fontsize=11)

        x_positions = np.linspace(3, 7, self.num_spots)
        for i, (spot_data, x_pos) in enumerate(zip(self.spots, x_positions)):
            spot_y = 2 + (spot_data['height'] / 10) * 8

            circle = Circle((x_pos, spot_y), 0.2, facecolor='purple',
                             edgecolor='black', linewidth=1.5)
            ax.add_patch(circle)

            ax.text(x_pos, spot_y - 0.5, spot_data['name'][9], fontsize=12,
                    ha='center', fontweight='bold')

            if spot_data == self.questioned_spot:
                draw_vertical_annotation(ax, 8.5, 2, spot_y,
                                         f"{spot_data['height']} cm",
                                         color='red', fontsize=11)

        calc_text = f"Calculate Rf for {self.questioned_spot['name']}"
        ax.text(5, 0.5, calc_text, fontsize=12, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                          edgecolor='black', linewidth=2))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem086:
    """
    Topic: 37.2 Gas-liquid chromatography
    Visual: Gas chromatogram with peaks of different areas
    Task: Calculate percentage composition (numerical)
    """

    def __init__(self):
        num_peaks = rnd.randint(2, 4)

        self.peaks = []
        total_area = 0

        for i in range(num_peaks):
            retention_time = round(1.5 + i * 1.5 + rnd.uniform(0, 0.5), 1)
            peak_area = rnd.randint(15, 85)
            total_area += peak_area
            self.peaks.append({
                'name': f'Component {chr(65+i)}',
                'retention_time': retention_time,
                'area': peak_area,
            })

        for peak in self.peaks:
            peak['percentage'] = round((peak['area'] / total_area) * 100, 1)

        self.questioned_peak = rnd.choice(self.peaks)
        self.answer = self.questioned_peak['percentage']

        self.description = (
            f"A gas chromatogram shows {num_peaks} peaks. "
            f"Calculate the percentage composition of {self.questioned_peak['name']} "
            f"given the peak areas shown in the diagram."
        )

        self.topic = "Analytical techniques"
        self.subtopic = "37.2 Gas-liquid chromatography"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        total_area_sum = sum(p['area'] for p in self.peaks)
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Peak area for {self.questioned_peak['name']}: {self.questioned_peak['area']}}}&\\\\"
            f"\\text{{Total peak area: {total_area_sum}}}&\\\\"
            "\\text{Percentage} &= \\frac{\\text{peak area}}{\\text{total area}} \\times 100\\%\\\\"
            f"&= \\frac{{{self.questioned_peak['area']}}}{{{total_area_sum}}} \\times 100\\%\\\\"
            f"&= {self.questioned_peak['percentage']}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 10)

        ax.set_title('Gas Chromatogram', fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Retention Time (min)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Detector Response', fontsize=14, fontweight='bold')
        ax.plot([0, 10], [0, 0], 'k-', linewidth=2)

        for peak in self.peaks:
            rt = peak['retention_time']
            area = peak['area']

            x = np.linspace(rt - 0.4, rt + 0.4, 100)
            height = area / 10
            y = height * np.exp(-((x - rt) ** 2) / (2 * 0.1 ** 2))

            ax.plot(x, y, color='royalblue', linewidth=2.5)
            ax.fill_between(x, 0, y, alpha=0.3, color='royalblue')

            ax.text(rt, height + 0.5, peak['name'][10], fontsize=12,
                    ha='center', fontweight='bold')
            ax.text(rt, -0.8, f"Area: {peak['area']}", fontsize=10, ha='center',
                    bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))

        ax.grid(True, alpha=0.3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem087:
    """
    Topic: 37.2 IR spectroscopy
    Visual: IR spectrum with a characteristic absorption peak
    Task: Identify functional group from IR absorption (MCQ)
    """

    def __init__(self):
        absorptions = [
            ("O-H (alcohol)", 3200, 3550, "broad", ["C=O (carbonyl)", "N-H (amine)", "C-O (ether)"]),
            ("O-H (carboxylic acid)", 2500, 3300, "very broad",
             ["O-H (alcohol)", "C=O (carbonyl)", "N-H (amine)"]),
            ("C=O (carbonyl)", 1680, 1750, "strong, sharp",
             ["C-O (ether/ester)", "O-H (alcohol)", "C=C (alkene)"]),
            ("C-O (ester/ether)", 1000, 1300, "strong",
             ["C=O (carbonyl)", "C-H (alkane)", "O-H (alcohol)"]),
            ("N-H (primary amine)", 3300, 3500, "two sharp peaks",
             ["O-H (alcohol)", "C=O (carbonyl)", "C-H (aldehyde)"]),
            ("C\u2261N (nitrile)", 2200, 2260, "strong, sharp",
             ["C=O (carbonyl)", "C=C (alkene)", "O-H (alcohol)"]),
            ("C-H (aldehyde)", 2700, 2850, "two weak peaks",
             ["O-H (carboxylic acid)", "N-H (amine)", "C\u2261N (nitrile)"]),
            ("N-H (amide)", 3150, 3350, "medium, broad",
             ["O-H (alcohol)", "C=O (carbonyl)", "N-H (amine, primary)"]),
            ("C=C (alkene)", 1620, 1680, "medium",
             ["C=O (carbonyl)", "C-O (ether)", "O-H (alcohol)"]),
            ("C-Cl (chloroalkane)", 600, 800, "strong",
             ["C-O (ether)", "C=O (carbonyl)", "C-H (alkane)"]),
        ]

        self.absorption = rnd.choice(absorptions)
        self.group = self.absorption[0]
        self.wavenumber_min = self.absorption[1]
        self.wavenumber_max = self.absorption[2]
        self.description_text = self.absorption[3]

        self.peak_position = rnd.randint(self.wavenumber_min, self.wavenumber_max)

        options = [self.group] + list(self.absorption[4])
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.group))

        self.description = (
            f"The IR spectrum shows a characteristic absorption. "
            f"The wavenumber is annotated on the diagram. "
            f"Which functional group is responsible for the labelled absorption?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Analytical techniques"
        self.subtopic = "IR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Absorption: {self.peak_position} cm}}^{{-1}} &\\\\"
            f"\\text{{Shape: {self.description_text}}} &\\\\"
            f"\\text{{Characteristic of: {self.group}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))

        wavenumbers = np.linspace(4000, 400, 500)
        transmittance = np.ones_like(wavenumbers) * 80

        peak_width = 50 if "sharp" in self.description_text else 150
        if "broad" in self.description_text:
            peak_width = 250

        for i in range(len(wavenumbers)):
            if abs(wavenumbers[i] - self.peak_position) < peak_width:
                transmittance[i] = 10

        ax.plot(wavenumbers, transmittance, 'b-', linewidth=2)
        ax.fill_between(wavenumbers, transmittance, 100, alpha=0.3)

        ax.annotate(f'{self.peak_position} cm\u207b\u00b9',
                    xy=(self.peak_position, 10),
                    xytext=(self.peak_position + 200, 30),
                    ha='center', fontsize=12, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8))

        ax.set_xlabel('Wavenumber (cm\u207b\u00b9)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Transmittance (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'IR Spectrum ({self.description_text} absorption at '
                     f'{self.peak_position} cm\u207b\u00b9)',
                     fontsize=13, fontweight='bold')
        ax.set_xlim(4000, 400)
        ax.set_ylim(0, 100)
        ax.grid(True, alpha=0.3)


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem088:
    """
    Topic: 37.3 ¹H NMR spectroscopy
    Visual: NMR spectrum with peaks shown (no colour coding)
    Task: Assign peak at given delta to hydrogen environment (MCQ)
    """

    def __init__(self):
        compounds = [
            ("ethanol", [(1.2, 3, "CH\u2083"), (3.7, 2, "CH\u2082"), (5.4, 1, "OH")]),
            ("propanone", [(2.1, 6, "CH\u2083")]),
            ("ethyl ethanoate", [(1.2, 3, "OCH\u2082CH\u2083"), (2.0, 3, "CH\u2083CO"), (4.1, 2, "OCH\u2082")]),
            ("methanol", [(3.4, 3, "CH\u2083"), (4.8, 1, "OH")]),
            ("propan-2-ol", [(1.2, 6, "CH\u2083 (×2)"), (3.9, 1, "CH")]),
            ("ethanoic acid", [(2.1, 3, "CH\u2083"), (11.5, 1, "COOH")]),
            ("dimethyl ether", [(3.3, 6, "CH\u2083")]),
            ("1,4-dimethylbenzene", [(2.3, 6, "CH\u2083"), (7.1, 4, "ArH")]),
            ("methyl methanoate", [(3.8, 3, "OCH\u2083"), (8.1, 1, "CHO")]),
            ("ethanal", [(2.2, 3, "CH\u2083"), (9.8, 1, "CHO")]),
        ]

        self.compound_data = rnd.choice(compounds)
        self.compound_name = self.compound_data[0]
        self.peaks = self.compound_data[1]

        selected_peak = rnd.choice(self.peaks)
        self.peak_shift = selected_peak[0]
        self.peak_integration = selected_peak[1]
        self.peak_assignment = selected_peak[2]

        all_assignments = [p[2] for comp in compounds for p in comp[1]]
        distractors = [a for a in all_assignments if a != self.peak_assignment]
        rnd.shuffle(distractors)
        options = [self.peak_assignment] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.peak_assignment))

        self.description = (
            f"The \u00b9H NMR spectrum of {self.compound_name} is shown. "
            f"One peak is highlighted with its chemical shift (\u03b4) and integration "
            f"annotated on the diagram. "
            f"Which hydrogen environment does the labelled peak represent?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Analytical techniques"
        self.subtopic = "\u00b9H NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Chemical shift: }} \\delta = {self.peak_shift}\\text{{ ppm}} &\\\\"
            f"\\text{{Integration: {self.peak_integration}H}} &\\\\"
            f"\\text{{Assignment: {self.peak_assignment}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))

        for shift, integration, label in self.peaks:
            draw_nmr_peak(ax, shift, integration, splitting='singlet', max_height=100)

        ax.annotate(f'\u03b4 = {self.peak_shift} ppm\n(integration: {self.peak_integration}H)',
                    xy=(self.peak_shift, 102),
                    xytext=(self.peak_shift + 1.5, 110),
                    fontsize=10, color='red', fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                    bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8))

        ax.set_xlabel('Chemical shift \u03b4 (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        ax.set_title(f'\u00b9H NMR Spectrum of {self.compound_name}',
                     fontsize=16, fontweight='bold')
        ax.set_xlim(12, 0)
        ax.set_ylim(0, 125)
        ax.grid(True, alpha=0.3)


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem089:
    """
    Topic: 37.3 ¹³C NMR spectroscopy
    Visual: ¹³C NMR spectrum (peaks only, no environment labels)
    Task: Count number of carbon environments (numerical)
    """

    def __init__(self):
        molecules = [
            {
                'name': 'propanone',
                'formula': 'CH\u2083COCH\u2083',
                'num_peaks': 2,
                'environments': ['CH\u2083 (methyl)', 'C=O (carbonyl)'],
                'shifts': [30, 206],
            },
            {
                'name': 'ethanol',
                'formula': 'CH\u2083CH\u2082OH',
                'num_peaks': 2,
                'environments': ['CH\u2083', 'CH\u2082'],
                'shifts': [18, 58],
            },
            {
                'name': 'ethanoic acid',
                'formula': 'CH\u2083COOH',
                'num_peaks': 2,
                'environments': ['CH\u2083', 'COOH'],
                'shifts': [21, 178],
            },
            {
                'name': 'propan-2-ol',
                'formula': '(CH\u2083)\u2082CHOH',
                'num_peaks': 2,
                'environments': ['CH\u2083 (equivalent)', 'CH'],
                'shifts': [25, 64],
            },
            {
                'name': 'propan-1-ol',
                'formula': 'CH\u2083CH\u2082CH\u2082OH',
                'num_peaks': 3,
                'environments': ['CH\u2083', 'CH\u2082', 'CH\u2082OH'],
                'shifts': [10, 26, 64],
            },
            {
                'name': 'propanal',
                'formula': 'CH\u2083CH\u2082CHO',
                'num_peaks': 3,
                'environments': ['CH\u2083', 'CH\u2082', 'CHO'],
                'shifts': [8, 36, 202],
            },
            {
                'name': 'methyl ethanoate',
                'formula': 'CH\u2083COOCH\u2083',
                'num_peaks': 3,
                'environments': ['CH\u2083CO', 'C=O', 'OCH\u2083'],
                'shifts': [20, 170, 52],
            },
            {
                'name': 'benzene',
                'formula': 'C\u2086H\u2086',
                'num_peaks': 1,
                'environments': ['all CH equivalent'],
                'shifts': [128],
            },
            {
                'name': 'methylbenzene',
                'formula': 'C\u2086H\u2085CH\u2083',
                'num_peaks': 4,
                'environments': ['CH\u2083', 'C-1 (ipso)', 'C-2,6 (ortho)', 'C-3,4,5'],
                'shifts': [21, 137, 126, 128],
            },
            {
                'name': 'butan-2-one',
                'formula': 'CH\u2083COCH\u2082CH\u2083',
                'num_peaks': 4,
                'environments': ['CH\u2083 (left)', 'C=O', 'CH\u2082', 'CH\u2083 (right)'],
                'shifts': [29, 212, 36, 8],
            },
        ]

        self.molecule = rnd.choice(molecules)
        self.answer = str(self.molecule['num_peaks'])

        self.description = (
            f"The \u00b9\u00b3C NMR spectrum of {self.molecule['name']} ({self.molecule['formula']}) "
            f"is shown below. "
            f"How many peaks appear in the spectrum? "
            f"(Give a numerical answer.)"
        )

        self.topic = "Analytical techniques"
        self.subtopic = "37.3 Carbon-13 NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.molecule['name']}}}&\\\\"
            f"\\text{{Number of unique C environments: {self.molecule['num_peaks']}}}&\\\\"
            + "\\\\".join([f"\\text{{Peak {i+1}: {env}}}"
                           for i, env in enumerate(self.molecule['environments'])]) + "\\\\"
            "\\text{Each unique C environment = one peak}&"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(220, 0)
        ax.set_ylim(0, 120)

        ax.set_title(f'\u00b9\u00b3C NMR Spectrum of {self.molecule["name"]}',
                     fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel('Chemical shift \u03b4 (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')

        for shift in self.molecule['shifts']:
            ax.plot([shift, shift], [0, 100], 'b-', linewidth=2.5)
            ax.text(shift, 103, f"\u03b4 {shift}", fontsize=10, ha='center', fontweight='bold')

        ax.grid(True, alpha=0.3, axis='x')
        ax.set_yticks([])

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem090:
    """
    Topic: 37.4 ¹H NMR splitting patterns
    Visual: NMR peak with integration shown, splitting not labeled
    Task: Identify splitting pattern using n+1 rule (MCQ)
    """

    def __init__(self):
        molecules = [
            {
                'name': 'ethanol',
                'formula': 'CH\u2083CH\u2082OH',
                'key_group': 'CH\u2083',
                'neighbors': 2,
                'splitting': 'triplet',
                'shift': 1.2,
                'integration': 3,
            },
            {
                'name': 'ethanol',
                'formula': 'CH\u2083CH\u2082OH',
                'key_group': 'CH\u2082',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 3.7,
                'integration': 2,
            },
            {
                'name': 'propanone',
                'formula': 'CH\u2083COCH\u2083',
                'key_group': 'CH\u2083',
                'neighbors': 0,
                'splitting': 'singlet',
                'shift': 2.1,
                'integration': 6,
            },
            {
                'name': 'propanal',
                'formula': 'CH\u2083CH\u2082CHO',
                'key_group': 'CH\u2082',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 2.4,
                'integration': 2,
            },
            {
                'name': 'propanal',
                'formula': 'CH\u2083CH\u2082CHO',
                'key_group': 'CH\u2083',
                'neighbors': 2,
                'splitting': 'triplet',
                'shift': 1.1,
                'integration': 3,
            },
            {
                'name': 'propanoic acid',
                'formula': 'CH\u2083CH\u2082COOH',
                'key_group': 'CH\u2082',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 2.3,
                'integration': 2,
            },
            {
                'name': 'propanoic acid',
                'formula': 'CH\u2083CH\u2082COOH',
                'key_group': 'CH\u2083',
                'neighbors': 2,
                'splitting': 'triplet',
                'shift': 1.1,
                'integration': 3,
            },
            {
                'name': 'ethyl ethanoate',
                'formula': 'CH\u2083COOCH\u2082CH\u2083',
                'key_group': 'OCH\u2082',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 4.1,
                'integration': 2,
            },
            {
                'name': 'ethyl ethanoate',
                'formula': 'CH\u2083COOCH\u2082CH\u2083',
                'key_group': 'OCH\u2082CH\u2083',
                'neighbors': 2,
                'splitting': 'triplet',
                'shift': 1.3,
                'integration': 3,
            },
            {
                'name': 'ethyl ethanoate',
                'formula': 'CH\u2083COOCH\u2082CH\u2083',
                'key_group': 'CH\u2083CO',
                'neighbors': 0,
                'splitting': 'singlet',
                'shift': 2.0,
                'integration': 3,
            },
            {
                'name': '1,1-dibromoethane',
                'formula': 'CH\u2083CHBr\u2082',
                'key_group': 'CH\u2083',
                'neighbors': 1,
                'splitting': 'doublet',
                'shift': 2.0,
                'integration': 3,
            },
            {
                'name': '1,1-dibromoethane',
                'formula': 'CH\u2083CHBr\u2082',
                'key_group': 'CHBr\u2082',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 5.9,
                'integration': 1,
            },
        ]

        self.mol = rnd.choice(molecules)
        correct = self.mol['splitting']

        all_splittings = ['singlet', 'doublet', 'triplet', 'quartet', 'quintet']
        distractors = [s for s in all_splittings if s != correct]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The \u00b9H NMR spectrum of {self.mol['name']} shows a peak at "
            f"\u03b4 = {self.mol['shift']} ppm "
            f"with integration of {self.mol['integration']}H. "
            f"This peak corresponds to the {self.mol['key_group']} group. "
            f"What is the splitting pattern? (Use the n+1 rule.)"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Analytical techniques"
        self.subtopic = "37.4 Proton (\u00b9H) NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Group: {self.mol['key_group']}}}&\\\\"
            f"\\text{{H on adjacent C: n = {self.mol['neighbors']}}}&\\\\"
            "\\text{n+1 rule: number of lines} &= n + 1\\\\"
            f"&= {self.mol['neighbors']} + 1 = {self.mol['neighbors'] + 1}\\\\"
            f"\\text{{Splitting pattern: {self.mol['splitting']}}}&\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))

        draw_nmr_peak(ax, self.mol['shift'], self.mol['integration'],
                      splitting=self.mol['splitting'], max_height=100)

        ax.set_title(f'\u00b9H NMR: {self.mol["name"]} \u2014 {self.mol["key_group"]} peak',
                     fontsize=16, fontweight='bold')
        ax.set_xlabel('Chemical shift \u03b4 (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        ax.set_xlim(self.mol['shift'] + 1.5, self.mol['shift'] - 1.5)
        ax.set_ylim(0, 130)

        ax.text(self.mol['shift'], 110,
                f"Integration: {self.mol['integration']}H\n\u03b4 = {self.mol['shift']} ppm",
                fontsize=12, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))

        ax.grid(True, alpha=0.3)


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem091:
    """
    Topic: 37.4 Combined spectroscopy
    Visual: Table of spectroscopic data (formula, M+, IR, NMR peaks shown)
    Task: Identify compound from combined data (MCQ)
    """

    def __init__(self):
        compounds = [
            {
                'name': 'ethanol',
                'formula': 'C\u2082H\u2086O',
                'molar_mass': 46,
                'ir': 'broad O-H (~3300), C-O (~1050)',
                'nmr_peaks': '3 (CH\u2083, CH\u2082, OH)',
                'ms_frag': 'm/z 31 (CH\u2082OH\u207a), 45 (M\u221117)',
            },
            {
                'name': 'propanone',
                'formula': 'C\u2083H\u2086O',
                'molar_mass': 58,
                'ir': 'C=O (~1715), no O-H',
                'nmr_peaks': '1 (CH\u2083)',
                'ms_frag': 'm/z 43 (CH\u2083CO\u207a), 15 (CH\u2083\u207a)',
            },
            {
                'name': 'ethanoic acid',
                'formula': 'C\u2082H\u2084O\u2082',
                'molar_mass': 60,
                'ir': 'very broad O-H (2500\u20133300), C=O (~1710)',
                'nmr_peaks': '2 (CH\u2083, COOH)',
                'ms_frag': 'm/z 45 (COOH\u207a), 43 (CH\u2083CO\u207a)',
            },
            {
                'name': 'methyl methanoate',
                'formula': 'C\u2082H\u2084O\u2082',
                'molar_mass': 60,
                'ir': 'C=O (~1725), C-O (~1200), no O-H',
                'nmr_peaks': '2 (CHO, OCH\u2083)',
                'ms_frag': 'm/z 31 (OCH\u2083\u207a), 29 (CHO\u207a)',
            },
            {
                'name': 'propanal',
                'formula': 'C\u2083H\u2086O',
                'molar_mass': 58,
                'ir': 'C=O (~1720), C-H aldehyde (~2720, 2820)',
                'nmr_peaks': '3 (CHO, CH\u2082, CH\u2083)',
                'ms_frag': 'm/z 57 (M\u22121), 29 (CHO\u207a)',
            },
            {
                'name': 'propan-1-ol',
                'formula': 'C\u2083H\u2088O',
                'molar_mass': 60,
                'ir': 'broad O-H (~3350), C-O (~1050)',
                'nmr_peaks': '3 (CH\u2083, CH\u2082, CH\u2082OH)',
                'ms_frag': 'm/z 31 (CH\u2082OH\u207a), 59 (M\u22121)',
            },
            {
                'name': 'dimethyl ether',
                'formula': 'C\u2082H\u2086O',
                'molar_mass': 46,
                'ir': 'C-O-C (~1100), no O-H',
                'nmr_peaks': '1 (CH\u2083)',
                'ms_frag': 'm/z 45 (M\u22121), 31 (CH\u2082OCH\u2083\u207a)',
            },
            {
                'name': 'ethyl methanoate',
                'formula': 'C\u2083H\u2086O\u2082',
                'molar_mass': 74,
                'ir': 'C=O (~1725), C-O (~1180), no O-H',
                'nmr_peaks': '3 (CHO, OCH\u2082, CH\u2083)',
                'ms_frag': 'm/z 29 (CHO\u207a), 45 (OEt\u207a)',
            },
            {
                'name': 'butan-2-one',
                'formula': 'C\u2084H\u2088O',
                'molar_mass': 72,
                'ir': 'C=O (~1715), no O-H',
                'nmr_peaks': '4 (CH\u2083CO, C=O, CH\u2082, CH\u2083)',
                'ms_frag': 'm/z 57 (C\u2084H\u2087O\u207a), 43 (CH\u2083CO\u207a)',
            },
            {
                'name': 'methanol',
                'formula': 'CH\u2084O',
                'molar_mass': 32,
                'ir': 'broad O-H (~3340), C-O (~1030)',
                'nmr_peaks': '2 (CH\u2083, OH)',
                'ms_frag': 'm/z 31 (CH\u2082OH\u207a), 29',
            },
        ]

        self.compound = rnd.choice(compounds)
        correct = self.compound['name']
        distractors = [c['name'] for c in compounds if c['name'] != correct]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"Using the combined spectroscopic data shown in the diagram, identify the compound."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Analytical techniques"
        self.subtopic = "Combined spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Formula: {self.compound['formula']}, M+ = {self.compound['molar_mass']}}} &\\\\"
            f"\\text{{IR: {self.compound['ir']}}} &\\\\"
            f"\\text{{NMR peaks: {self.compound['nmr_peaks']}}} &\\\\"
            f"\\text{{MS fragments: {self.compound['ms_frag']}}} &\\\\"
            f"\\therefore \\text{{Compound: {correct}, Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 6.5, 7.5,
                      f"Spectroscopic Data: M\u207a = {self.compound['molar_mass']}, "
                      f"Formula = {self.compound['formula']}",
                      fontsize=14)

        table_data = [
            ["Technique", "Key Information"],
            ["Mass Spec", f"M\u207a = {self.compound['molar_mass']}\n{self.compound['ms_frag']}"],
            ["IR Spec", self.compound['ir']],
            ["\u00b9H NMR", f"{self.compound['nmr_peaks']} peaks"],
        ]

        draw_data_table(ax, table_data, start_x=1.5, start_y=6.5,
                        cell_width=5, cell_height=0.9, header_color='lightblue')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem092:
    """
    Topic: 23.1 / 23.2 Born-Haber cycle
    Visual: Annotated Born-Haber energy cycle with one step highlighted
    Task: Identify the enthalpy change for the highlighted step (MCQ)
    """

    def __init__(self):
        compounds = [
            {
                "compound": "NaCl",
                "metal": "Na",
                "nonmetal": "Cl",
                "metal_ion": "Na\u207a",
                "nonmetal_ion": "Cl\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Na(s)]", "Enthalpy of atomisation of Na"),
                    "B": ("1st IE of Na", "First ionisation energy of Na"),
                    "C": ("\u00bdx\u0394H\u00b0at[Cl\u2082(g)]", "Enthalpy of atomisation of Cl"),
                    "D": ("Electron affinity of Cl", "First electron affinity of Cl"),
                    "E": ("Lattice enthalpy of NaCl", "Lattice enthalpy (formation) of NaCl"),
                },
            },
            {
                "compound": "MgO",
                "metal": "Mg",
                "nonmetal": "O",
                "metal_ion": "Mg\u00b2\u207a",
                "nonmetal_ion": "O\u00b2\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Mg(s)]", "Enthalpy of atomisation of Mg"),
                    "B": ("1st+2nd IE of Mg", "Sum of 1st and 2nd ionisation energies of Mg"),
                    "C": ("\u00bdx\u0394H\u00b0at[O\u2082(g)]", "Enthalpy of atomisation of O"),
                    "D": ("1st+2nd EA of O", "Sum of 1st and 2nd electron affinities of O"),
                    "E": ("Lattice enthalpy of MgO", "Lattice enthalpy (formation) of MgO"),
                },
            },
            {
                "compound": "KBr",
                "metal": "K",
                "nonmetal": "Br",
                "metal_ion": "K\u207a",
                "nonmetal_ion": "Br\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[K(s)]", "Enthalpy of atomisation of K"),
                    "B": ("1st IE of K", "First ionisation energy of K"),
                    "C": ("\u00bdx\u0394H\u00b0at[Br\u2082(l)]", "Enthalpy of atomisation of Br"),
                    "D": ("Electron affinity of Br", "First electron affinity of Br"),
                    "E": ("Lattice enthalpy of KBr", "Lattice enthalpy (formation) of KBr"),
                },
            },
            {
                "compound": "CaO",
                "metal": "Ca",
                "nonmetal": "O",
                "metal_ion": "Ca\u00b2\u207a",
                "nonmetal_ion": "O\u00b2\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Ca(s)]", "Enthalpy of atomisation of Ca"),
                    "B": ("1st+2nd IE of Ca", "Sum of 1st and 2nd ionisation energies of Ca"),
                    "C": ("\u00bdx\u0394H\u00b0at[O\u2082(g)]", "Enthalpy of atomisation of O"),
                    "D": ("1st+2nd EA of O", "Sum of 1st and 2nd electron affinities of O"),
                    "E": ("Lattice enthalpy of CaO", "Lattice enthalpy (formation) of CaO"),
                },
            },
            {
                "compound": "LiF",
                "metal": "Li",
                "nonmetal": "F",
                "metal_ion": "Li\u207a",
                "nonmetal_ion": "F\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Li(s)]", "Enthalpy of atomisation of Li"),
                    "B": ("1st IE of Li", "First ionisation energy of Li"),
                    "C": ("\u00bdx\u0394H\u00b0at[F\u2082(g)]", "Enthalpy of atomisation of F"),
                    "D": ("Electron affinity of F", "First electron affinity of F"),
                    "E": ("Lattice enthalpy of LiF", "Lattice enthalpy (formation) of LiF"),
                },
            },
            {
                "compound": "NaF",
                "metal": "Na",
                "nonmetal": "F",
                "metal_ion": "Na\u207a",
                "nonmetal_ion": "F\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Na(s)]", "Enthalpy of atomisation of Na"),
                    "B": ("1st IE of Na", "First ionisation energy of Na"),
                    "C": ("\u00bdx\u0394H\u00b0at[F\u2082(g)]", "Enthalpy of atomisation of F"),
                    "D": ("Electron affinity of F", "First electron affinity of F"),
                    "E": ("Lattice enthalpy of NaF", "Lattice enthalpy (formation) of NaF"),
                },
            },
            {
                "compound": "MgCl\u2082",
                "metal": "Mg",
                "nonmetal": "Cl",
                "metal_ion": "Mg\u00b2\u207a",
                "nonmetal_ion": "Cl\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Mg(s)]", "Enthalpy of atomisation of Mg"),
                    "B": ("1st+2nd IE of Mg", "Sum of 1st and 2nd ionisation energies of Mg"),
                    "C": ("\u0394H\u00b0at[Cl\u2082(g)]", "Enthalpy of atomisation of Cl (\u00d72)"),
                    "D": ("2\u00d7EA of Cl", "Sum of two electron affinities of Cl"),
                    "E": ("Lattice enthalpy of MgCl\u2082", "Lattice enthalpy (formation) of MgCl\u2082"),
                },
            },
            {
                "compound": "NaBr",
                "metal": "Na",
                "nonmetal": "Br",
                "metal_ion": "Na\u207a",
                "nonmetal_ion": "Br\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Na(s)]", "Enthalpy of atomisation of Na"),
                    "B": ("1st IE of Na", "First ionisation energy of Na"),
                    "C": ("\u00bdx\u0394H\u00b0at[Br\u2082(l)]", "Enthalpy of atomisation of Br"),
                    "D": ("Electron affinity of Br", "First electron affinity of Br"),
                    "E": ("Lattice enthalpy of NaBr", "Lattice enthalpy (formation) of NaBr"),
                },
            },
            {
                "compound": "CaF\u2082",
                "metal": "Ca",
                "nonmetal": "F",
                "metal_ion": "Ca\u00b2\u207a",
                "nonmetal_ion": "F\u207b",
                "steps": {
                    "A": ("\u0394H\u00b0at[Ca(s)]", "Enthalpy of atomisation of Ca"),
                    "B": ("1st+2nd IE of Ca", "Sum of 1st and 2nd ionisation energies of Ca"),
                    "C": ("\u0394H\u00b0at[F\u2082(g)]", "Enthalpy of atomisation of F (\u00d72)"),
                    "D": ("2\u00d7EA of F", "Sum of two electron affinities of F"),
                    "E": ("Lattice enthalpy of CaF\u2082", "Lattice enthalpy (formation) of CaF\u2082"),
                },
            },
        ]

        self.data = rnd.choice(compounds)
        self.compound = self.data["compound"]
        self.asked_step = rnd.choice(["A", "B", "C", "D", "E"])
        correct = self.data["steps"][self.asked_step][1]

        distractors = [self.data["steps"][s][1]
                       for s in ["A", "B", "C", "D", "E"]
                       if s != self.asked_step]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))

        self.description = (
            f"The diagram shows a Born-Haber cycle for {self.compound}. "
            f"What enthalpy change does step {self.asked_step} represent?"
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Chemical energetics"
        self.subtopic = "Born-Haber cycles and lattice enthalpy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Born-Haber cycle for {self.compound}:}} &\\\\"
            f"\\text{{Step A: enthalpy of atomisation of metal}} &\\\\"
            f"\\text{{Step B: ionisation energy of metal}} &\\\\"
            f"\\text{{Step C: enthalpy of atomisation of non-metal}} &\\\\"
            f"\\text{{Step D: electron affinity of non-metal}} &\\\\"
            f"\\text{{Step E: lattice enthalpy of {self.compound}}} &\\\\"
            f"\\therefore \\text{{Step {self.asked_step} = {correct}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 9))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 9)
        ax.axis("off")

        add_title_box(ax, 6.5, 8.5, f"Born-Haber Cycle for {self.compound}", fontsize=16)

        cmpd = self.data["compound"]
        metal = self.data["metal"]
        nonmetal = self.data["nonmetal"]
        metal_ion = self.data["metal_ion"]
        nonmetal_ion = self.data["nonmetal_ion"]

        levels = {
            "elements": (1.5, 7.2, f"{metal}(s) + \u00bd{nonmetal}\u2082(g)"),
            "atoms": (1.5, 5.4, f"{metal}(g) + {nonmetal}(g)"),
            "ions_pos": (1.5, 3.6, f"{metal_ion}(g) + {nonmetal}(g) + e\u207b"),
            "ions_neg": (6.5, 2.0, f"{metal_ion}(g) + {nonmetal_ion}(g)"),
            "compound": (6.5, 0.7, f"{cmpd}(s)"),
        }

        level_colors = {
            "elements": "royalblue",
            "atoms": "darkorange",
            "ions_pos": "crimson",
            "ions_neg": "purple",
            "compound": "forestgreen",
        }

        for key, (lx, ly, lbl) in levels.items():
            color = level_colors[key]
            ax.plot([lx, lx + 3.5], [ly, ly], color=color, linewidth=2.5,
                    solid_capstyle="round")
            ax.text(lx + 3.65, ly, lbl, fontsize=9, va="center",
                    color=color, fontweight="bold")

        def bh_arrow(x1, y1, x2, y2, label, label_side="left", color="black"):
            arr = FancyArrowPatch((x1, y1), (x2, y2),
                                  arrowstyle="-|>", mutation_scale=18,
                                  linewidth=2, color=color,
                                  connectionstyle="arc3,rad=0")
            ax.add_patch(arr)
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            offset = -0.55 if label_side == "left" else 0.55
            ha = "right" if label_side == "left" else "left"
            step_label = self.data["steps"].get(label, (label, ""))[0]
            is_asked = (label == self.asked_step)
            ax.text(mx + offset, my, f"({label})\n{step_label}",
                    fontsize=8, ha=ha, va="center",
                    bbox=dict(boxstyle="round,pad=0.2",
                              facecolor="lightyellow" if is_asked else "white",
                              edgecolor="red" if is_asked else "grey",
                              linewidth=2.0 if is_asked else 0.8))

        bh_arrow(2.5, 7.2, 2.5, 5.4, "A", label_side="left", color="darkorange")
        bh_arrow(3.0, 5.4, 3.0, 3.6, "B", label_side="left", color="crimson")

        ax.annotate("", xy=(4.5, 3.6), xytext=(4.5, 5.6),
                    arrowprops=dict(arrowstyle="-|>", color="darkorange",
                                    lw=2, mutation_scale=18))
        step_label_c = self.data['steps']['C'][0]
        is_c = ("C" == self.asked_step)
        ax.text(5.05, 4.6, f"(C)\n{step_label_c}",
                fontsize=8, ha="left", va="center",
                bbox=dict(boxstyle="round,pad=0.2",
                          facecolor="lightyellow" if is_c else "white",
                          edgecolor="red" if is_c else "grey",
                          linewidth=2.0 if is_c else 0.8))

        bh_arrow(8.5, 3.6, 8.5, 2.0, "D", label_side="right", color="purple")
        bh_arrow(9.0, 2.0, 9.0, 0.7, "E", label_side="right", color="forestgreen")

        ax.annotate("", xy=(8.0, 0.7), xytext=(3.0, 7.2),
                    arrowprops=dict(arrowstyle="-|>", color="grey",
                                    lw=1.5, linestyle="dashed", mutation_scale=16))
        ax.text(5.0, 3.9, "\u0394H\u00b0f", fontsize=10, ha="center",
                color="grey", style="italic")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()





class Chem093:
    """
    Topic: 24.1 Electrode potentials and electrochemical cells
    Visual: Electrochemical cell diagram (no anode/cathode labels, voltmeter hidden)
    Task: Calculate EMF or identify anode/cathode (MCQ or numerical)
    """

    def __init__(self):
        half_cells = [
            {"electrode": "Zn", "ion": "Zn\u00b2\u207a", "E_std": -0.76,
             "solution": "ZnSO\u2084(aq)", "color": "lightcyan"},
            {"electrode": "Cu", "ion": "Cu\u00b2\u207a", "E_std": +0.34,
             "solution": "CuSO\u2084(aq)", "color": "lightblue"},
            {"electrode": "Fe", "ion": "Fe\u00b2\u207a", "E_std": -0.44,
             "solution": "FeSO\u2084(aq)", "color": "lightyellow"},
            {"electrode": "Ag", "ion": "Ag\u207a", "E_std": +0.80,
             "solution": "AgNO\u2083(aq)", "color": "lightyellow"},
            {"electrode": "Pb", "ion": "Pb\u00b2\u207a", "E_std": -0.13,
             "solution": "Pb(NO\u2083)\u2082(aq)", "color": "lavender"},
            {"electrode": "Ni", "ion": "Ni\u00b2\u207a", "E_std": -0.25,
             "solution": "NiSO\u2084(aq)", "color": "lightgreen"},
        ]

        pair = rnd.sample(half_cells, 2)
        self.hc1, self.hc2 = pair[0], pair[1]

        self.emf = round(self.hc2["E_std"] - self.hc1["E_std"], 2)
        if self.emf < 0:
            self.hc1, self.hc2 = self.hc2, self.hc1
            self.emf = round(self.hc2["E_std"] - self.hc1["E_std"], 2)

        self.anode = self.hc1["electrode"]
        self.cathode = self.hc2["electrode"]

        self.question_type = "emf"  # fixed
        if self.question_type == "emf":
            self.answer = round(self.emf, 2)
            self.options = []
            self.description = (
                f"The diagram shows an electrochemical cell. "
                f"The standard electrode potentials (E\u00b0) for each half-cell "
                f"are shown in the diagram. "
                f"Calculate the standard cell EMF (E\u00b0cell) in V."
            )

        self.topic = "Electrode potentials and electrochemical cells"
        self.subtopic = "Standard electrode potentials"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Anode (negative): {self.anode}}} &\\\\"
            f"\\text{{Cathode (positive): {self.cathode}}} &\\\\"
            f"E\\degree_{{\\text{{cell}}}} &= E\\degree_{{\\text{{cathode}}}} - E\\degree_{{\\text{{anode}}}} \\\\"
            f"&= ({self.hc2['E_std']:+.2f}) - ({self.hc1['E_std']:+.2f}) \\\\"
            f"&= {self.emf:.2f}\\text{{ V}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 6.5, 7.5,
                      f"Electrochemical Cell: "
                      f"{self.hc1['electrode']}/{self.hc1['ion']} || "
                      f"{self.hc2['electrode']}/{self.hc2['ion']}",
                      fontsize=14)

        def draw_half_cell(ax, bx, label_e, label_ion, sol_color, e_std):
            bw, bh = 3.2, 3.0
            by = 1.0
            beaker = patches.Rectangle((bx, by), bw, bh, fill=False,
                                        edgecolor="black", linewidth=2.5)
            ax.add_patch(beaker)
            sol = patches.Rectangle((bx + 0.1, by + 0.1), bw - 0.2, bh * 0.65,
                                     facecolor=sol_color, alpha=0.6, edgecolor="none")
            ax.add_patch(sol)
            rod_x = bx + bw / 2
            ax.plot([rod_x, rod_x], [by + bh * 0.6, by + bh + 0.9],
                    color="dimgrey", linewidth=8, solid_capstyle="round")
            ax.text(rod_x, by + bh + 1.1, label_e, fontsize=14,
                    ha="center", va="bottom", fontweight="bold", color="dimgrey")
            ax.text(bx + bw / 2, by + bh * 0.3, label_ion + "(aq)",
                    fontsize=11, ha="center", va="center", style="italic")
            ax.text(bx + bw / 2, by - 0.35,
                    f"E\u00b0 = {e_std:+.2f} V",
                    fontsize=11, ha="center", va="center",
                    bbox=dict(boxstyle="round", facecolor="lightyellow",
                              edgecolor="black", linewidth=1))
            return rod_x, by + bh + 0.9

        lx = 0.5
        l_rod_x, l_rod_top = draw_half_cell(ax, lx, self.hc1["electrode"],
                                             self.hc1["ion"], self.hc1["color"],
                                             self.hc1["E_std"])
        rx = 8.8
        r_rod_x, r_rod_top = draw_half_cell(ax, rx, self.hc2["electrode"],
                                              self.hc2["ion"], self.hc2["color"],
                                              self.hc2["E_std"])

        wire_y = 5.8
        ax.plot([l_rod_x, l_rod_x], [l_rod_top, wire_y], "k-", linewidth=2.5)
        ax.plot([r_rod_x, r_rod_x], [r_rod_top, wire_y], "k-", linewidth=2.5)
        ax.plot([l_rod_x, 4.8], [wire_y, wire_y], "k-", linewidth=2.5)
        ax.plot([8.2, r_rod_x], [wire_y, wire_y], "k-", linewidth=2.5)

        voltmeter = plt.Circle((6.5, wire_y), 0.8, facecolor="white",
                                edgecolor="black", linewidth=2.5, zorder=5)
        ax.add_patch(voltmeter)
        if self.question_type == "emf":
            ax.text(6.5, wire_y, "?", fontsize=20, ha="center", va="center",
                    fontweight="bold", color="red", zorder=6)
        else:
            ax.text(6.5, wire_y, f"{self.emf:.2f} V", fontsize=12,
                    ha="center", va="center", fontweight="bold", zorder=6)
        ax.text(6.5, wire_y + 1.0, "Voltmeter", fontsize=10,
                ha="center", va="center", zorder=6)

        # Salt bridge
        sb_y1, sb_y2 = 2.5, 3.8
        sb_x1, sb_x2 = 3.6, 8.9
        ax.add_patch(patches.FancyBboxPatch((sb_x1, sb_y1), sb_x2 - sb_x1,
                                             sb_y2 - sb_y1,
                                             boxstyle="round,pad=0.1",
                                             facecolor="lightyellow",
                                             edgecolor="black", linewidth=2))
        ax.text((sb_x1 + sb_x2) / 2, (sb_y1 + sb_y2) / 2,
                "Salt bridge\n(KNO\u2083(aq))",
                fontsize=10, ha="center", va="center", fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem094:
    """
    Topic: 25.1 / 25.2 pH curves and buffer regions
    Visual: Titration pH curve (equivalence point NOT annotated)
    Task: Read equivalence point volume or pH from graph (numerical)
    """

    def __init__(self):
        titration_templates = [
            {
                "type": "strong acid / strong base",
                "acid": "HCl",
                "base": "NaOH",
                "start_ph_range": (0.8, 1.5),
                "end_ph": 13.0,
                "eq_ph": 7.0,
                "has_buffer": False,
            },
            {
                "type": "weak acid / strong base",
                "acid": "CH\u2083COOH",
                "base": "NaOH",
                "start_ph_range": (2.5, 3.2),
                "end_ph": 12.5,
                "eq_ph": 8.7,
                "has_buffer": True,
            },
            {
                "type": "strong acid / weak base",
                "acid": "HCl",
                "base": "NH\u2083",
                "start_ph_range": (0.8, 1.5),
                "end_ph": 11.2,
                "eq_ph": 5.3,
                "has_buffer": False,
            },
            {
                "type": "weak acid / strong base",
                "acid": "HCOOH",
                "base": "NaOH",
                "start_ph_range": (2.2, 2.8),
                "end_ph": 12.5,
                "eq_ph": 8.2,
                "has_buffer": True,
            },
            {
                "type": "strong acid / strong base",
                "acid": "H\u2082SO\u2084",
                "base": "NaOH",
                "start_ph_range": (0.4, 0.9),
                "end_ph": 13.0,
                "eq_ph": 7.0,
                "has_buffer": False,
            },
            {
                "type": "strong acid / weak base",
                "acid": "HNO\u2083",
                "base": "NH\u2083",
                "start_ph_range": (1.2, 1.8),
                "end_ph": 11.0,
                "eq_ph": 5.3,
                "has_buffer": False,
            },
        ]

        tmpl = rnd.choice(titration_templates)
        eq_vol = round(rnd.uniform(15, 35), 1)
        start_ph = round(rnd.uniform(*tmpl["start_ph_range"]), 1)
        # Derive buffer region as (eq_vol*0.3, eq_vol*0.8) for buffered titrations
        if tmpl["has_buffer"]:
            buf_low = round(eq_vol * 0.3, 0)
            buf_high = round(eq_vol * 0.8, 0)
            buffer_region = (int(buf_low), int(buf_high))
        else:
            buffer_region = None
        self.t = {**tmpl,
                  "eq_vol": eq_vol,
                  "start_ph": start_ph,
                  "buffer_region": buffer_region}

        q_types = ["equivalence_vol", "equivalence_ph"]
        self.q_type = rnd.choice(q_types)

        if self.q_type == "equivalence_vol":
            self.answer = round(self.t['eq_vol'], 1)
            self.description = (
                f"The graph shows the pH curve when {self.t['base']} is added to "
                f"{self.t['acid']} solution ({self.t['type']}). "
                f"What volume of {self.t['base']} is required to reach the equivalence point?"
            )
        else:
            self.answer = self.t['eq_ph']
            self.description = (
                f"The graph shows a {self.t['type']} titration curve. "
                f"What is the pH at the equivalence point?"
            )

        self.topic = "Equilibria"
        self.subtopic = "pH curves and buffer solutions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Titration: {self.t['type']}}} &\\\\"
            f"\\text{{Equivalence point: {self.t['eq_vol']:.1f} cm}}^3\\text{{ at pH {self.t['eq_ph']:.1f}}} &\\\\"
            + (f"\\text{{Buffer region: {self.t['buffer_region'][0]}\u2013{self.t['buffer_region'][1]} cm}}^3 &\\\\"
               if self.t["has_buffer"] else "")
            + f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def _ph_curve(self, v_arr, t):
        eq = t["eq_vol"]
        start = t["start_ph"]
        end = t["end_ph"]
        eq_ph = t["eq_ph"]
        ph = np.zeros_like(v_arr, dtype=float)

        for i, v in enumerate(v_arr):
            if v < eq - 2:
                progress = v / (eq - 2)
                if t["has_buffer"] and v > eq * 0.1:
                    ph[i] = start + (eq_ph - 2.5 - start) * (v / (eq * 0.9)) ** 0.5
                else:
                    ph[i] = start + (eq_ph - 3 - start) * (v / (eq - 2)) ** 0.4
            elif v <= eq + 2:
                frac = (v - (eq - 2)) / 4.0
                ph[i] = (eq_ph - 3) + 6 * frac
            else:
                progress = min((v - eq - 2) / 10, 1)
                ph[i] = (eq_ph + 3) + (end - eq_ph - 3) * progress ** 0.4

        return np.clip(ph, 0, 14)

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))

        max_v = max(self.t["eq_vol"] * 2, 50)
        v = np.linspace(0, max_v, 500)
        ph = self._ph_curve(v, self.t)

        ax.plot(v, ph, "royalblue", linewidth=3)
        ax.set_xlim(0, max_v)
        ax.set_ylim(0, 14)
        ax.set_xlabel(f"Volume of {self.t['base']} added / cm\u00b3",
                      fontsize=13, fontweight="bold")
        ax.set_ylabel("pH", fontsize=13, fontweight="bold")
        ax.set_title(f"pH Curve: {self.t['acid']} vs {self.t['base']}\n({self.t['type']})",
                     fontsize=14, fontweight="bold")
        ax.grid(True, alpha=0.3, linestyle="--")
        ax.set_yticks(range(0, 15, 2))

        ax.axhline(y=7, color="gray", linestyle=":", linewidth=1, alpha=0.5)
        ax.text(max_v * 0.97, 7.3, "pH 7", fontsize=9, color="gray", ha='right')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem095:
    """
    Topic: 26.1 / 26.2 Arrhenius equation and activation energy
    Visual: ln(k) vs 1/T graph with gradient annotation but no answer labels
    Task: Calculate Ea or interpret gradient/intercept (MCQ)
    """

    def __init__(self):
        reactions = [
            {"name": "decomposition of H\u2082O\u2082", "Ea": 75.0, "A_ln": 30.2},
            {"name": "hydrolysis of sucrose", "Ea": 108.0, "A_ln": 38.5},
            {"name": "formation of HI from H\u2082 + I\u2082", "Ea": 165.0, "A_ln": 42.1},
            {"name": "decomposition of N\u2082O\u2085", "Ea": 88.0, "A_ln": 35.0},
            {"name": "decomposition of NO\u2082", "Ea": 111.0, "A_ln": 37.0},
            {"name": "esterification of ethanoic acid", "Ea": 51.0, "A_ln": 26.5},
            {"name": "bromination of propanone", "Ea": 83.0, "A_ln": 33.0},
            {"name": "alkaline hydrolysis of bromoethane", "Ea": 89.0, "A_ln": 34.5},
            {"name": "decomposition of ozone", "Ea": 72.0, "A_ln": 28.8},
        ]

        self.rxn = rnd.choice(reactions)
        self.Ea = self.rxn["Ea"]
        self.A_ln = self.rxn["A_ln"]
        R = 8.314
        self.gradient = -self.Ea * 1000 / R

        self.q_type = "Ea_from_gradient"  # fixed
        if self.q_type == "Ea_from_gradient":
            self.answer = int(self.Ea)
            self.options = []
            self.description = (
                f"The graph shows an Arrhenius plot (ln k vs 1/T) for the {self.rxn['name']}. "
                f"The gradient of the line is annotated on the diagram. "
                f"Calculate the activation energy, Ea (in kJ mol\u207b\u00b9)."
            )

        self.topic = "Reaction kinetics"
        self.subtopic = "Arrhenius equation and activation energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{gradient}} &= -\\frac{{E_a}}{{R}} \\\\"
            f"-\\frac{{E_a}}{{R}} &= {self.gradient:.0f}\\text{{ K}} \\\\"
            f"E_a &= -{self.gradient:.0f} \\times 8.314 \\\\"
            f"E_a &= {self.Ea * 1000:.0f}\\text{{ J mol}}^{{-1}} \\\\"
            f"E_a &= {int(self.Ea)}\\text{{ kJ mol}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        R = 8.314
        T_arr = np.linspace(300, 700, 200)
        inv_T = 1 / T_arr
        ln_k = self.A_ln - (self.Ea * 1000 / R) * inv_T

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(inv_T * 1e3, ln_k, "royalblue", linewidth=3)

        ax.set_xlabel("1/T \u00d7 10\u207b\u00b3 / K\u207b\u00b9", fontsize=13, fontweight="bold")
        ax.set_ylabel("ln k", fontsize=13, fontweight="bold")
        ax.set_title(f"Arrhenius Plot: {self.rxn['name']}", fontsize=14, fontweight="bold")
        ax.grid(True, alpha=0.3, linestyle="--")

        i1, i2 = 20, 160
        x1, y1 = inv_T[i1] * 1e3, ln_k[i1]
        x2, y2 = inv_T[i2] * 1e3, ln_k[i2]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="<->", color="red", lw=2))
        ax.text((x1 + x2) / 2 + 0.05, (y1 + y2) / 2,
                f"gradient = {self.gradient:.0f} K",
                fontsize=10, color="red",
                bbox=dict(boxstyle="round", facecolor="mistyrose", alpha=0.9))

        ax.text(0.98, 0.95, "ln k = ln A \u2212 Ea/RT",
                transform=ax.transAxes, fontsize=12,
                ha="right", va="top", fontweight="bold",
                bbox=dict(boxstyle="round", facecolor="lightyellow",
                          edgecolor="black", linewidth=1.5))


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem096:
    """
    Topic: 16.1 Hydroxy compounds — alcohol oxidation
    Visual: Before/after test tubes with K2Cr2O7 (result label removed)
    Task: Identify alcohol class or oxidation product (MCQ)
    """

    def __init__(self):
        alcohols = [
            {
                "name": "methanol",
                "class": "primary",
                "formula": "CH\u2083OH",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "methanal (then methanoic acid with excess)",
            },
            {
                "name": "propan-1-ol",
                "class": "primary",
                "formula": "CH\u2083CH\u2082CH\u2082OH",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "propanal / propanoic acid",
            },
            {
                "name": "butan-1-ol",
                "class": "primary",
                "formula": "CH\u2083(CH\u2082)\u2083OH",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "butanal / butanoic acid",
            },
            {
                "name": "propan-2-ol",
                "class": "secondary",
                "formula": "CH\u2083CH(OH)CH\u2083",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "propanone (ketone)",
            },
            {
                "name": "butan-2-ol",
                "class": "secondary",
                "formula": "CH\u2083CH(OH)CH\u2082CH\u2083",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "butan-2-one (ketone)",
            },
            {
                "name": "2-methylpropan-2-ol",
                "class": "tertiary",
                "formula": "(CH\u2083)\u2083COH",
                "result_heat": "orange (no change)",
                "color_before": "darkorange",
                "color_after": "darkorange",
                "oxidation_product": "no reaction",
            },
            {
                "name": "2-methylbutan-2-ol",
                "class": "tertiary",
                "formula": "(CH\u2083)\u2082C(OH)CH\u2082CH\u2083",
                "result_heat": "orange (no change)",
                "color_before": "darkorange",
                "color_after": "darkorange",
                "oxidation_product": "no reaction",
            },
            {
                "name": "cyclohexanol",
                "class": "secondary",
                "formula": "C\u2086H\u2081\u2081OH",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "cyclohexanone (ketone)",
            },
            {
                "name": "pentan-1-ol",
                "class": "primary",
                "formula": "CH\u2083(CH\u2082)\u2084OH",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "pentanal / pentanoic acid",
            },
            {
                "name": "3-methylbutan-2-ol",
                "class": "secondary",
                "formula": "(CH\u2083)\u2082CHCH(OH)CH\u2083",
                "result_heat": "orange \u2192 green",
                "color_before": "darkorange",
                "color_after": "darkgreen",
                "oxidation_product": "3-methylbutan-2-one (ketone)",
            },
        ]

        self.alcohol = rnd.choice(alcohols)

        correct = self.alcohol["name"] + f" ({self.alcohol['class']} alcohol)"
        all_names = [a["name"] + f" ({a['class']} alcohol)" for a in alcohols]
        distractors = [n for n in all_names if n != correct]
        rnd.shuffle(distractors)
        options = [correct] + distractors[:3]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))
        self.description = (
            f"An unknown alcohol is treated with acidified K\u2082Cr\u2082O\u2087. "
            f"The formula and colour change after heating are shown in the diagram. "
            f"Identify the alcohol."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Hydroxy compounds"
        self.subtopic = "Oxidation of alcohols"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Alcohol: {self.alcohol['name']} ({self.alcohol['class']})}} &\\\\"
            f"\\text{{Result: {self.alcohol['result_heat']}}} &\\\\"
            f"\\text{{Product: {self.alcohol['oxidation_product']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 7))
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 7)
        ax.axis("off")

        add_title_box(ax, 5.5, 6.5,
                      f"Oxidation Test with Acidified K\u2082Cr\u2082O\u2087",
                      fontsize=15)

        draw_test_tube(ax, 1.0, 1.5, width=1.8, height=3.5,
                       solution_height=2.5,
                       solution_color=self.alcohol["color_before"])
        ax.text(1.9, 5.3, "Before heating", fontsize=11, ha="center", fontweight="bold")
        ax.text(1.9, 1.1, "Orange\n(Cr\u2086O\u2087\u00b2\u207b)", fontsize=10,
                ha="center", color="darkorange", fontweight="bold")

        draw_arrow(ax, 3.5, 3.2, 5.5, 3.2,
                   label="Heat /\nreflux", label_position="above",
                   color="red", linewidth=2.5)

        draw_test_tube(ax, 6.0, 1.5, width=1.8, height=3.5,
                       solution_height=2.5,
                       solution_color=self.alcohol["color_after"])
        ax.text(6.9, 5.3, "After heating", fontsize=11, ha="center", fontweight="bold")
        draw_labeled_box(ax, 8.5, 3.5, 2.3, 1.5,
                         f"{self.alcohol['formula']}",
                         facecolor="lightyellow", linewidth=1.5, label_fontsize=12)
        ax.text(9.65, 5.2, self.alcohol["name"], fontsize=10,
                ha="center", fontweight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem097:
    """
    Topic: 17.1 Carbonyl compounds
    Visual: Test tube results for Tollens'/Fehling's/2,4-DNP (result labels removed)
    Task: Identify compound type or test result (MCQ)
    """

    def __init__(self):
        compounds = [
            {
                "name": "ethanal",
                "formula": "CH\u2083CHO",
                "type": "aldehyde",
                "tollens": "silver mirror (positive)",
                "tollens_color": "silver",
                "fehling": "brick-red precipitate (positive)",
                "dnp": "orange precipitate",
            },
            {
                "name": "propanal",
                "formula": "CH\u2083CH\u2082CHO",
                "type": "aldehyde",
                "tollens": "silver mirror (positive)",
                "tollens_color": "silver",
                "fehling": "brick-red precipitate (positive)",
                "dnp": "orange precipitate",
            },
            {
                "name": "butanal",
                "formula": "CH\u2083CH\u2082CH\u2082CHO",
                "type": "aldehyde",
                "tollens": "silver mirror (positive)",
                "tollens_color": "silver",
                "fehling": "brick-red precipitate (positive)",
                "dnp": "orange precipitate",
            },
            {
                "name": "propanone",
                "formula": "CH\u2083COCH\u2083",
                "type": "ketone",
                "tollens": "no reaction (negative)",
                "tollens_color": "lightcyan",
                "fehling": "no reaction (negative)",
                "dnp": "orange precipitate",
            },
            {
                "name": "pentan-3-one",
                "formula": "CH\u2083CH\u2082COCH\u2082CH\u2083",
                "type": "ketone",
                "tollens": "no reaction (negative)",
                "tollens_color": "lightcyan",
                "fehling": "no reaction (negative)",
                "dnp": "orange precipitate",
            },
            {
                "name": "butan-2-one",
                "formula": "CH\u2083COCH\u2082CH\u2083",
                "type": "ketone",
                "tollens": "no reaction (negative)",
                "tollens_color": "lightcyan",
                "fehling": "no reaction (negative)",
                "dnp": "orange precipitate",
            },
            {
                "name": "pentanal",
                "formula": "CH\u2083(CH\u2082)\u2083CHO",
                "type": "aldehyde",
                "tollens": "silver mirror (positive)",
                "tollens_color": "silver",
                "fehling": "brick-red precipitate (positive)",
                "dnp": "orange precipitate",
            },
            {
                "name": "pentan-2-one",
                "formula": "CH\u2083CO(CH\u2082)\u2082CH\u2083",
                "type": "ketone",
                "tollens": "no reaction (negative)",
                "tollens_color": "lightcyan",
                "fehling": "no reaction (negative)",
                "dnp": "orange precipitate",
            },
            {
                "name": "hexanal",
                "formula": "CH\u2083(CH\u2082)\u2084CHO",
                "type": "aldehyde",
                "tollens": "silver mirror (positive)",
                "tollens_color": "silver",
                "fehling": "brick-red precipitate (positive)",
                "dnp": "orange precipitate",
            },
            {
                "name": "hexan-3-one",
                "formula": "CH\u2083CH\u2082CO(CH\u2082)\u2082CH\u2083",
                "type": "ketone",
                "tollens": "no reaction (negative)",
                "tollens_color": "lightcyan",
                "fehling": "no reaction (negative)",
                "dnp": "orange precipitate",
            },
        ]

        self.compound = rnd.choice(compounds)
        self.q_type = "identify_type"  # fixed
        if self.q_type == "identify_type":
            correct = self.compound["type"]
            options = ["aldehyde", "ketone", "carboxylic acid", "ester"]
            rnd.shuffle(options)
            self.options = options
            self.answer = chr(65 + options.index(correct))
            self.description = (
                f"The diagram shows three test tube results after chemical tests "
                f"on an unknown carbonyl compound. "
                f"Is the compound an aldehyde or a ketone?"
            )
        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Carbonyl compounds"
        self.subtopic = "Distinguishing aldehydes and ketones"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.compound['name']} ({self.compound['type']})}} &\\\\"
            f"\\text{{Tollens': {self.compound['tollens']}}} &\\\\"
            f"\\text{{Fehling's: {self.compound['fehling']}}} &\\\\"
            f"\\text{{2,4-DNP: {self.compound['dnp']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 6.5, 7.5,
                      f"Carbonyl Tests: {self.compound['name']} ({self.compound['formula']})",
                      fontsize=14)

        tests = [
            {
                "reagent": "Tollens' Reagent\n(warm in water bath)",
                "tube_color": self.compound["tollens_color"],
            },
            {
                "reagent": "Fehling's Solution\n(heat)",
                "tube_color": "#8B1A1A" if self.compound["type"] == "aldehyde" else "#87CEEB",
            },
            {
                "reagent": "2,4-DNP\n(room temperature)",
                "tube_color": "orange",
            },
        ]

        x_positions = [1.2, 5.0, 8.8]

        for test, xp in zip(tests, x_positions):
            draw_test_tube(ax, xp, 2.0, width=1.6, height=3.5,
                           solution_height=2.6, solution_color=test["tube_color"])
            ax.text(xp + 0.8, 6.0, test["reagent"], fontsize=10,
                    ha="center", va="center", fontweight="bold",
                    bbox=dict(boxstyle="round", facecolor="lightblue",
                              edgecolor="black", linewidth=1))

        ax.text(6.5, 1.2, f"Based on the test results, select the correct answer:",
                fontsize=10, ha='center', color='navy', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem098:
    """
    Topic: 13.1 / 13.4 Electrophilic addition to alkenes
    Visual: Curly arrow mechanism (intermediate/product box hidden)
    Task: Identify intermediate, product, or electrophile (MCQ)
    """

    def __init__(self):
        reactions = [
            {
                "alkene": "ethene",
                "reagent": "HBr",
                "electrophile": "H\u207a (from HBr)",
                "intermediate": "carbocation (CH\u2083CH\u2082\u207a)",
                "product": "bromoethane",
                "product_formula": "CH\u2083CH\u2082Br",
                "alkene_formula": "CH\u2082=CH\u2082",
                "step1_desc": "H\u207a attacks \u03c0 bond of C=C",
                "step2_desc": "Br\u207b attacks carbocation",
                "e_distractors": ["Br\u207b", "HBr (whole molecule)", "Br\u2022 (radical)"],
                "i_distractors": ["carbanion (CH\u2083CH\u2082\u207b)", "free radical", "bromonium ion"],
                "p_distractors": ["dibromoethane", "ethanol", "chloroethane"],
            },
            {
                "alkene": "propene",
                "reagent": "HCl",
                "electrophile": "H\u207a (from HCl)",
                "intermediate": "secondary carbocation (CH\u2083CH\u207aCH\u2083)",
                "product": "2-chloropropane",
                "product_formula": "CH\u2083CHClCH\u2083",
                "alkene_formula": "CH\u2083CH=CH\u2082",
                "step1_desc": "H\u207a attacks less substituted C",
                "step2_desc": "Cl\u207b attacks more stable carbocation",
                "e_distractors": ["Cl\u207b", "HCl (whole molecule)", "Cl\u2022 (radical)"],
                "i_distractors": ["primary carbocation", "carbanion", "free radical"],
                "p_distractors": ["1-chloropropane", "1,2-dichloropropane", "propan-2-ol"],
            },
            {
                "alkene": "ethene",
                "reagent": "Br\u2082",
                "electrophile": "Br\u207a (induced dipole in Br\u2082)",
                "intermediate": "bromonium ion / carbocation",
                "product": "1,2-dibromoethane",
                "product_formula": "BrCH\u2082CH\u2082Br",
                "alkene_formula": "CH\u2082=CH\u2082",
                "step1_desc": "Br\u2082 polarised by \u03c0 electrons; Br\u207a attacks",
                "step2_desc": "Br\u207b attacks carbocation",
                "e_distractors": ["Br\u207b", "Br\u2022 (radical)", "Br\u2082 (whole molecule)"],
                "i_distractors": ["carbanion", "Br\u2022 radical", "secondary carbocation"],
                "p_distractors": ["bromoethane", "ethanol", "dibromoethene"],
            },
            {
                "alkene": "propene",
                "reagent": "HBr",
                "electrophile": "H\u207a (from HBr)",
                "intermediate": "secondary carbocation (CH\u2083CH\u207aCH\u2083)",
                "product": "2-bromopropane",
                "product_formula": "CH\u2083CHBrCH\u2083",
                "alkene_formula": "CH\u2083CH=CH\u2082",
                "step1_desc": "H\u207a attacks less substituted C (Markovnikov)",
                "step2_desc": "Br\u207b attacks secondary carbocation",
                "e_distractors": ["Br\u207b", "HBr (whole molecule)", "Br\u2022"],
                "i_distractors": ["primary carbocation", "carbanion", "bromonium ion"],
                "p_distractors": ["1-bromopropane", "1,2-dibromopropane", "propan-2-ol"],
            },
            {
                "alkene": "but-1-ene",
                "reagent": "HBr",
                "electrophile": "H\u207a (from HBr)",
                "intermediate": "secondary carbocation (CH\u2083CH\u207aCH\u2082CH\u2083)",
                "product": "2-bromobutane",
                "product_formula": "CH\u2083CHBrCH\u2082CH\u2083",
                "alkene_formula": "CH\u2082=CHCH\u2082CH\u2083",
                "step1_desc": "H\u207a adds to terminal C",
                "step2_desc": "Br\u207b attacks secondary carbocation",
                "e_distractors": ["Br\u207b", "HBr molecule", "Br\u2022 radical"],
                "i_distractors": ["primary carbocation", "carbanion", "tertiary carbocation"],
                "p_distractors": ["1-bromobutane", "1,2-dibromobutane", "butan-2-ol"],
            },
            {
                "alkene": "cyclohexene",
                "reagent": "Br\u2082",
                "electrophile": "Br\u207a (induced dipole)",
                "intermediate": "bromonium ion (cyclic)",
                "product": "1,2-dibromocyclohexane",
                "product_formula": "C\u2086H\u2081\u2080Br\u2082",
                "alkene_formula": "C\u2086H\u2081\u2080 (cyclohexene)",
                "step1_desc": "Br\u2082 forms cyclic bromonium ion",
                "step2_desc": "Br\u207b attacks from opposite face (anti addition)",
                "e_distractors": ["Br\u207b", "Br\u2022", "HBr"],
                "i_distractors": ["carbanion", "free radical", "carbocation (open)"],
                "p_distractors": ["bromocyclohexane", "cyclohexane", "cyclohexanol"],
            },
            {
                "alkene": "but-1-ene",
                "reagent": "HBr",
                "electrophile": "H\u207a (from HBr)",
                "intermediate": "secondary carbocation (CH\u2083CH\u207aCH\u2082CH\u2083)",
                "product": "2-bromobutane",
                "product_formula": "CH\u2083CHBrCH\u2082CH\u2083",
                "alkene_formula": "CH\u2082=CHCH\u2082CH\u2083",
                "step1_desc": "H\u207a attacks C-1 (Markovnikov)",
                "step2_desc": "Br\u207b attacks secondary C-2 carbocation",
                "e_distractors": ["Br\u207b", "HBr (whole molecule)", "Br\u2022"],
                "i_distractors": ["primary carbocation", "carbanion", "bromonium ion"],
                "p_distractors": ["1-bromobutane", "1,2-dibromobutane", "butan-2-ol"],
            },
            {
                "alkene": "ethene",
                "reagent": "HCl",
                "electrophile": "H\u207a (from HCl)",
                "intermediate": "carbocation (CH\u2083CH\u2082\u207a)",
                "product": "chloroethane",
                "product_formula": "CH\u2083CH\u2082Cl",
                "alkene_formula": "CH\u2082=CH\u2082",
                "step1_desc": "H\u207a attacks \u03c0 bond",
                "step2_desc": "Cl\u207b attacks carbocation",
                "e_distractors": ["Cl\u207b", "HCl (whole molecule)", "Cl\u2022"],
                "i_distractors": ["carbanion", "free radical", "chloronium ion"],
                "p_distractors": ["dichloroethane", "ethanol", "1,2-dichloroethane"],
            },
            {
                "alkene": "propene",
                "reagent": "Br\u2082",
                "electrophile": "Br\u207a (induced dipole in Br\u2082)",
                "intermediate": "bromonium ion / carbocation",
                "product": "1,2-dibromopropane",
                "product_formula": "CH\u2083CHBrCH\u2082Br",
                "alkene_formula": "CH\u2083CH=CH\u2082",
                "step1_desc": "Br\u2082 polarised; Br\u207a attacks \u03c0 bond",
                "step2_desc": "Br\u207b attacks carbocation from opposite face",
                "e_distractors": ["Br\u207b", "Br\u2022 (radical)", "Br\u2082 (whole molecule)"],
                "i_distractors": ["carbanion", "primary carbocation", "Br\u2022 radical"],
                "p_distractors": ["2-bromopropane", "propan-1-ol", "dibromomethane"],
            },
            {
                "alkene": "but-2-ene",
                "reagent": "HBr",
                "electrophile": "H\u207a (from HBr)",
                "intermediate": "secondary carbocation (CH\u2083CH\u207aCH\u2082CH\u2083 or CH\u2083CH\u2082CH\u207aCH\u2083)",
                "product": "2-bromobutane",
                "product_formula": "CH\u2083CHBrCH\u2082CH\u2083",
                "alkene_formula": "CH\u2083CH=CHCH\u2083",
                "step1_desc": "H\u207a attacks either C (symmetrical carbocations formed)",
                "step2_desc": "Br\u207b attacks the secondary carbocation",
                "e_distractors": ["Br\u207b", "HBr (whole molecule)", "Br\u2022"],
                "i_distractors": ["primary carbocation", "carbanion", "free radical"],
                "p_distractors": ["1-bromobutane", "1,2-dibromobutane", "butan-2-ol"],
            },
        ]

        self.rxn = rnd.choice(reactions)
        self.q_type = "identify_electrophile"
        correct = self.rxn["electrophile"]
        options = [correct] + self.rxn["e_distractors"]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))
        self.description = (
            f"The mechanism diagram shows electrophilic addition to {self.rxn['alkene']}. "
            f"Identify the electrophile that initiates the reaction."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Electrophilic addition mechanisms"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.rxn['alkene']} + {self.rxn['reagent']}}} &\\\\"
            f"\\text{{Electrophile: {self.rxn['electrophile']}}} &\\\\"
            f"\\text{{Step 1: {self.rxn['step1_desc']}}} &\\\\"
            f"\\text{{Intermediate: {self.rxn['intermediate']}}} &\\\\"
            f"\\text{{Step 2: {self.rxn['step2_desc']}}} &\\\\"
            f"\\text{{Product: {self.rxn['product']}}} &\\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 7, 7.5,
                      f"Electrophilic Addition: {self.rxn['alkene']} + {self.rxn['reagent']}",
                      fontsize=14)

        c1x, c1y = 1.8, 4.5
        c2x, c2y = 3.2, 4.5

        draw_bond(ax, c1x, c1y, c2x, c2y, bond_type="double", linewidth=3, color="black")
        ax.text(c1x, c1y, "C", fontsize=20, ha="center", va="center",
                fontweight="bold", color="royalblue")
        ax.text(c2x, c2y, "C", fontsize=20, ha="center", va="center",
                fontweight="bold", color="royalblue")
        ax.text(c1x - 0.6, c1y + 0.5, self.rxn["alkene_formula"],
                fontsize=10, ha="center", color="royalblue", style="italic")

        hx, hy = 3.8, 5.8
        ax.text(hx, hy, self.rxn["reagent"][0],
                fontsize=18, ha="center", va="center",
                fontweight="bold", color="crimson")

        arr1 = FancyArrowPatch((c2x, c2y + 0.25), (hx - 0.2, hy - 0.2),
                               arrowstyle="-|>", mutation_scale=18,
                               linewidth=2, color="blue",
                               connectionstyle="arc3,rad=-0.4")
        ax.add_patch(arr1)
        ax.text(3.4, 5.4, "curly arrow 1\n(\u03c0 \u2192 electrophile)", fontsize=8,
                ha="center", color="blue", style="italic")

        ax.text(2.5, 3.5, "Step 1", fontsize=12, ha="center",
                fontweight="bold", color="darkgreen",
                bbox=dict(boxstyle="round", facecolor="lightgreen", pad=0.3))
        ax.text(2.5, 3.0, self.rxn["step1_desc"], fontsize=9,
                ha="center", color="darkgreen")

        draw_arrow(ax, 5.0, 4.5, 6.5, 4.5, color="black", linewidth=2.5)

        ix = 7.5
        if self.q_type == "identify_intermediate":
            ax.text(ix, 4.5, "?", fontsize=28, ha="center", va="center",
                    fontweight="bold",
                    bbox=dict(boxstyle="round", facecolor="lightgray",
                              edgecolor="black", linewidth=2, pad=0.5))
        else:
            draw_labeled_box(ax, ix - 0.9, 3.8, 1.8, 1.4,
                             f"Carbocation\n{self.rxn['intermediate'][:20]}",
                             facecolor="lightyellow", linewidth=2, label_fontsize=9)
        ax.text(ix, 5.5, "INTERMEDIATE", fontsize=10, ha="center",
                fontweight="bold", color="darkorange")

        nucx, nucy = 7.5, 2.5
        anion = self.rxn["reagent"][-1] + "\u207b"
        ax.text(nucx, nucy, anion, fontsize=16, ha="center",
                fontweight="bold", color="purple")

        arr2 = FancyArrowPatch((nucx, nucy + 0.3), (ix, 3.8),
                               arrowstyle="-|>", mutation_scale=18,
                               linewidth=2, color="purple",
                               connectionstyle="arc3,rad=0.3")
        ax.add_patch(arr2)

        ax.text(7.5, 6.3, "Step 2", fontsize=12, ha="center",
                fontweight="bold", color="navy",
                bbox=dict(boxstyle="round", facecolor="lightblue", pad=0.3))
        ax.text(7.5, 5.9, self.rxn["step2_desc"], fontsize=9,
                ha="center", color="navy")

        draw_arrow(ax, 9.2, 4.5, 10.5, 4.5, color="black", linewidth=2.5)

        if self.q_type == "identify_product":
            ax.text(12, 4.5, "?", fontsize=28, ha="center", va="center",
                    fontweight="bold",
                    bbox=dict(boxstyle="round", facecolor="lightgray",
                              edgecolor="black", linewidth=2, pad=0.5))
        else:
            draw_labeled_box(ax, 10.5, 3.8, 3.0, 1.4,
                             f"PRODUCT\n{self.rxn['product_formula']}",
                             facecolor="lightgreen", linewidth=2, label_fontsize=11)
            ax.text(12, 5.5, self.rxn["product"][:22],
                    fontsize=9, ha="center", color="forestgreen", style="italic")


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem099:
    """
    Topic: 11.1 Group 17 (Halogens)
    Visual: Three test tubes showing AgNO3/NH3 tests (result label and table highlight removed)
    Task: Identify halide ion, predict NH3 result, or give precipitate formula (MCQ)
    """

    def __init__(self):
        halides = [
            {
                "ion": "Cl\u207b",
                "name": "chloride",
                "agno3_ppt": "white precipitate",
                "agno3_color": "white",
                "dil_nh3": "dissolves in dilute NH\u2083",
                "conc_nh3": "dissolves in concentrated NH\u2083",
                "formula": "AgCl",
            },
            {
                "ion": "Br\u207b",
                "name": "bromide",
                "agno3_ppt": "cream precipitate",
                "agno3_color": "#FFFDD0",
                "dil_nh3": "insoluble in dilute NH\u2083",
                "conc_nh3": "dissolves in concentrated NH\u2083",
                "formula": "AgBr",
            },
            {
                "ion": "I\u207b",
                "name": "iodide",
                "agno3_ppt": "pale yellow precipitate",
                "agno3_color": "#FFFAAA",
                "dil_nh3": "insoluble in dilute NH\u2083",
                "conc_nh3": "insoluble in concentrated NH\u2083",
                "formula": "AgI",
            },
        ]

        self.halide = rnd.choice(halides)

        all_ions = [h["ion"] for h in halides] + ["F\u207b"]
        correct = self.halide["ion"]
        options = all_ions[:]
        rnd.shuffle(options)
        self.answer = chr(65 + options.index(correct))
        self.options = options
        self.description = (
            "The diagram shows silver nitrate / ammonia tests on an unknown halide. "
            "The precipitate colour and ammonia solubility results are shown. "
            "Identify the halide ion present."
        )

        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "Group 17 (Halogens)"
        self.subtopic = "Halide ion tests"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Halide: {self.halide['ion']} ({self.halide['name']})}} &\\\\"
            f"\\text{{AgNO}}_3\\text{{: {self.halide['agno3_ppt']}}} &\\\\"
            f"\\text{{Dilute NH}}_3\\text{{: {self.halide['dil_nh3']}}} &\\\\"
            f"\\text{{Conc. NH}}_3\\text{{: {self.halide['conc_nh3']}}} &\\\\"
            f"\\therefore \\text{{Precipitate = {self.halide['formula']}, Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 6.5, 7.5,
                      "Halide Ion Identification with AgNO\u2083 / NH\u2083",
                      fontsize=15)

        tubes = [
            {
                "label": "1. Add AgNO\u2083",
                "solution_color": "lightyellow",
                "ppt_color": self.halide["agno3_color"],
                "x": 0.8,
            },
            {
                "label": "2. Add dilute NH\u2083",
                "solution_color": "lightyellow",
                "ppt_color": (self.halide["agno3_color"]
                              if "insoluble" in self.halide["dil_nh3"]
                              else "lightblue"),
                "x": 4.6,
            },
            {
                "label": "3. Add conc. NH\u2083",
                "solution_color": "lightyellow",
                "ppt_color": (self.halide["agno3_color"]
                              if "insoluble" in self.halide["conc_nh3"]
                              else "lightblue"),
                "x": 8.4,
            },
        ]

        for tube in tubes:
            tx = tube["x"]
            draw_test_tube(ax, tx, 2.2, width=1.8, height=3.5,
                           solution_height=2.8, solution_color=tube["solution_color"])
            ppt = patches.Rectangle((tx + 0.1, 2.3), 1.6, 0.6,
                                     facecolor=tube["ppt_color"],
                                     edgecolor="none", alpha=0.9)
            ax.add_patch(ppt)
            ax.text(tx + 0.9, 6.1, tube["label"],
                    fontsize=10, ha="center", fontweight="bold",
                    bbox=dict(boxstyle="round", facecolor="lightblue",
                              edgecolor="black", linewidth=1))

        table_data = [
            ["Halide", "AgNO\u2083 ppt.", "Dil. NH\u2083", "Conc. NH\u2083"],
            ["Cl\u207b", "White (AgCl)", "Dissolves", "Dissolves"],
            ["Br\u207b", "Cream (AgBr)", "Insoluble", "Dissolves"],
            ["I\u207b", "Pale yellow (AgI)", "Insoluble", "Insoluble"],
        ]

        draw_data_table(ax, table_data, start_x=0.3, start_y=2.0,
                        cell_width=3.1, cell_height=0.45,
                        header_color="steelblue")


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()





class Chem100:
    """
    Topic: 4.1 / 4.2 States of matter — ideal gas behaviour
    Visual: pV vs p graph comparing real vs ideal gas (annotations removed)
    Task: Interpret deviations from ideal behaviour (MCQ)
    """

    def __init__(self):
        gases = [
            {"name": "H\u2082",   "B_prime": +0.00002,  "C_prime": 0.0000005,
             "attractive": "very weak",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV > nRT \u2014 very weak attractions, volume dominates even at low p"},
            {"name": "CO\u2082", "B_prime": -0.00025,  "C_prime": 0.0000008,
             "attractive": "moderate",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV < nRT \u2014 intermolecular attractions dominate"},
            {"name": "N\u2082",  "B_prime": -0.00008,  "C_prime": 0.0000004,
             "attractive": "weak",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV \u2248 nRT \u2014 close to ideal behaviour"},
            {"name": "NH\u2083", "B_prime": -0.00035,  "C_prime": 0.0000007,
             "attractive": "strong (polar, H-bonding)",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV < nRT \u2014 strong intermolecular attractions dominate"},
            {"name": "He",   "B_prime": +0.000012, "C_prime": 0.0000002,
             "attractive": "negligible",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV > nRT \u2014 negligible attractions, volume effect even at low p"},
            {"name": "CH\u2084", "B_prime": -0.00015,  "C_prime": 0.0000006,
             "attractive": "moderate (London dispersion)",
             "high_p_stmt": "pV > nRT \u2014 molecular volume dominates",
             "low_p_stmt":  "pV < nRT \u2014 London dispersion forces cause attraction"},
        ]

        self.gas = rnd.choice(gases)

        self.pressure_region = "high"
        correct = "pV > nRT \u2014 molecular volume becomes significant"
        options = [
            correct,
            "pV < nRT \u2014 intermolecular attractions dominate",
            "pV = nRT \u2014 gas behaves ideally",
            "pV decreases linearly with increasing pressure",
        ]

        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))
        self.description = (
            f"The graph shows pV vs p for {self.gas['name']} (real gas) compared to an ideal gas. "
            f"The high-pressure region of the graph is highlighted. "
            f"Which statement best describes the real gas behaviour in the highlighted region?"
        )
        self.description += "\n\n" + "\n".join(f"{chr(65+_j)}. {_o}" for _j, _o in enumerate(self.options))
        self.topic = "States of matter"
        self.subtopic = "Ideal and real gas behaviour"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "pV &= nRT \\text{ (ideal gas equation)} \\\\"
            "\\text{Ideal gas: } pV &= \\text{constant (horizontal line)} \\\\"
            "\\text{Real gas at low p:} &\\text{ attractions} \\Rightarrow pV < nRT \\\\"
            "\\text{Real gas at high p:} &\\text{ molecular volume} \\Rightarrow pV > nRT \\\\"
            f"\\therefore \\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        nRT = 22.7
        p = np.linspace(0.01, 1000, 1000)

        pv_ideal = np.full_like(p, nRT)

        B_prime = self.gas["B_prime"]
        C_prime = self.gas["C_prime"]
        Z = 1 + B_prime * p + C_prime * p ** 2
        pv_real = nRT * Z

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(p, pv_ideal, "royalblue", linewidth=3,
                linestyle="--", label="Ideal gas", zorder=3)
        ax.plot(p, pv_real, "crimson", linewidth=3,
                label=f"Real gas: {self.gas['name']}", zorder=3)

        ax.set_xlim(0, 1000)
        ax.set_ylim(nRT * 0.7, nRT * 1.5)
        ax.set_xlabel("Pressure / atm", fontsize=13, fontweight="bold")
        ax.set_ylabel("pV / L atm mol\u207b\u00b9", fontsize=13, fontweight="bold")
        ax.set_title(f"pV vs p: Real Gas ({self.gas['name']}) vs Ideal Gas",
                     fontsize=14, fontweight="bold")
        ax.grid(True, alpha=0.3, linestyle="--")
        ax.legend(fontsize=12, loc="upper left")

        ax.axhline(y=nRT, color="royalblue", linewidth=1, linestyle=":", alpha=0.5)
        ax.text(850, nRT + 0.4, "Ideal: pV = nRT", fontsize=10,
                color="royalblue", ha="center")


        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()
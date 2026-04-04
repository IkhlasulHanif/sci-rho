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

        self._options = options
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self._options))

        self.description = (
            f"The bar chart shows the relative reactivity of four Group 2 elements with water. "
            f"The elements are arranged in order of atomic number (position 1 to 4). "
            f"What is the reactivity value shown for the element at position {self.position}?\n\n"
            f"{self.options_text}"
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. The graph shows Group 2 elements in order of increasing atomic number.} \\\\"
            "&\\text{2. These correspond to Mg (1), Ca (2), Sr (3), and Ba (4).} \\\\"
            f"&\\text{{3. The question asks for the reactivity value at position {self.position} ({self.element}).}} \\\\"
            f"&\\text{{4. Reading the height of the bar at position {self.position} on the y-axis gives {correct_val}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )
        
        self.topic = "Group 2"
        self.subtopic = "Trends in Group 2"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

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
        
        # Obscure element identities as X and Y
        e1, e2 = "Element X", "Element Y"
        t1, t2 = self.comp['transition1'], self.comp['transition2']
        
        # Extract the unicode charges (e.g., '²⁺') and configurations (e.g., '[Ar] 3d⁹')
        self.charge1 = self.comp['ion1'].split(':')[0].replace(self.comp['element1'], '')
        self.charge2 = self.comp['ion2'].split(':')[0].replace(self.comp['element2'], '')
        self.ion_config1 = self.comp['ion1'].split(': ')[1]
        self.ion_config2 = self.comp['ion2'].split(': ')[1]

        # Build MCQ options using X and Y
        options_map = {
            (True, False):  (f"{e1} only",),
            (False, True):  (f"{e2} only",),
            (True, True):   (f"Both X and Y",),
            (False, False): ("Neither",),
        }
        correct_text = options_map[(t1, t2)][0]

        # Build 4 options
        all_opts = [f"{e1} only", f"{e2} only", f"Both X and Y", "Neither"]
        rnd.shuffle(all_opts)
        self.choices = all_opts[:4]
        if correct_text not in self.choices:
            self.choices[0] = correct_text
            rnd.shuffle(self.choices)

        labels = ["A", "B", "C", "D"]
        self.answer = labels[self.choices.index(correct_text)]
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "Based on the definition and electron configurations provided in the diagram, "
            "which of the following is/are transition element(s)?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "General physical and chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Determine explanation text for the reasoning block
        exp1 = "an incomplete d subshell, so it IS" if t1 else "a full or empty d subshell, so it is NOT"
        exp2 = "an incomplete d subshell, so it IS" if t2 else "a full or empty d subshell, so it is NOT"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. The definition requires forming a stable ion with an incomplete d subshell.} \\\\"
            f"&\\text{{2. Element X forms the ion X{self.charge1} with configuration {self.ion_config1}.}} \\\\"
            f"&\\quad \\text{{It has {exp1} a transition element.}} \\\\"
            f"&\\text{{3. Element Y forms the ion Y{self.charge2} with configuration {self.ion_config2}.}} \\\\"
            f"&\\quad \\text{{It has {exp2} a transition element.}} \\\\"
            f"&\\text{{4. Therefore, the correct option is: {correct_text}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

        y_pos = 5.5
        add_formula_label(ax, 2, y_pos, "Element X atom:", fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos, self.comp['config1'], fontsize=13,
                         bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.5))

        add_formula_label(ax, 2, y_pos - 0.8, f"X{self.charge1}:",
                         fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos - 0.8, self.ion_config1,
                         fontsize=13, bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))

        y_pos = 3.5
        add_formula_label(ax, 2, y_pos, "Element Y atom:", fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos, self.comp['config2'], fontsize=13,
                         bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.5))

        add_formula_label(ax, 2, y_pos - 0.8, f"Y{self.charge2}:",
                         fontsize=14, ha='right')
        add_formula_label(ax, 5, y_pos - 0.8, self.ion_config2,
                         fontsize=13, bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))

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
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows test tubes containing compounds of a transition metal at different oxidation states. "
            "What is the oxidation state of the metal in the highlighted test tube?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "General properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The title indicates these are compounds of {self.metal}.}} \\\\"
            f"&\\text{{2. The highlighted test tube contains a {self.shown_color} solution.}} \\\\"
            f"&\\text{{3. Aqueous {self.metal} ions exhibit a characteristic {self.shown_color} color}} \\\\"
            f"&\\quad \\text{{when in the {correct_ox} oxidation state.}} \\\\"
            f"&\\text{{4. Therefore, the correct option is {self.answer}.}}"
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
            "The diagram shows the general spatial arrangement of ligands around a central transition metal ion. "
            "What is the coordination number of the central metal ion?"
        )

        self.topic = "Chemistry of transition elements"
        self.subtopic = "Ligands and complex formation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. The coordination number is defined as the total number of coordinate bonds} \\\\"
            "&\\quad \\text{formed between the ligands and the central metal ion.} \\\\"
            "&\\text{2. By counting the ligands (L) bonded to the central metal (M) in the diagram:} \\\\"
            f"&\\quad \\text{{Coordination number}} = {self.coordination_number}"
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
        # Use set to avoid any duplicate distractors if lists overlap
        all_formulas = list(set([r['final_complex'] for r in complexes])) 
        wrong_opts = [f for f in all_formulas if f != correct]
        options = rnd.sample(wrong_opts, 3) + [correct]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a ligand exchange reaction starting from an aqueous metal ion solution. "
            "What is the formula of the final complex ion?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Characteristic chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts/superscripts to LaTeX for math mode
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-', '²': '^2', '³': '^3', '⁴': '^4'
        })
        
        initial_tex = self.reaction['initial_complex'].translate(tex_map)
        final_tex = self.reaction['final_complex'].translate(tex_map)
        ligand_tex = self.reaction['ligand'].translate(tex_map)
        metal_tex = self.reaction['metal'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The starting solution contains aqueous }} \\mathrm{{{metal_tex}}} \\text{{ ions, which exist as}} \\\\"
            f"&\\quad \\text{{the {self.reaction['initial_color']} hexaaqua complex: }} \\mathrm{{{initial_tex}}}. \\\\"
            f"&\\text{{2. Adding {self.reaction['ligand_name']} (}}\\mathrm{{{ligand_tex}}}\\text{{) initiates a ligand exchange reaction.}} \\\\"
            f"&\\text{{3. The stronger or more concentrated ligand replaces the water molecules in}} \\\\"
            "&\\quad \\text{the coordination sphere to form a new, stable complex.} \\\\"
            f"&\\text{{4. For {self.reaction['metal']} with {self.reaction['ligand_name']}, the final product is the}} \\\\"
            f"&\\quad \\text{{{self.reaction['final_color']} complex: }} \\mathrm{{{final_tex}}}. \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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
        
        # Changed to obscure the starting complex formula
        add_formula_label(ax, 2.25, 0.8, f"Aqueous {self.reaction['metal']}", fontsize=13)

        draw_arrow(ax, 3.5, 3.5, 5.5, 3.5, label=f"+ excess {self.reaction['ligand']}",
                  label_position='above', color='black', linewidth=3)

        draw_test_tube(ax, 7, 1.5, width=1.5, height=3.5, solution_height=2.5,
                      solution_color='lightgray')
        add_formula_label(ax, 7.75, 0.8, "?", fontsize=20, weight='bold', color='red')

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
            ("[Cu(H\u2082O)\u2086]\u00b2\u207a", "#ADD8E6", "pale blue", "[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a", "deep blue", "excess NH\u2083(aq)", "Aqueous Cu\u00b2\u207a"),
            ("[Fe(H\u2082O)\u2086]\u00b3\u207a", "#DAA520", "yellow-brown", "[Fe(SCN)(H\u2082O)\u2085]\u00b2\u207a", "blood red", "SCN\u207b(aq)", "Aqueous Fe\u00b3\u207a"),
            ("[Co(H\u2082O)\u2086]\u00b2\u207a", "#FFC0CB", "pink", "[CoCl\u2084]\u00b2\u207b", "blue", "excess Cl\u207b(aq)", "Aqueous Co\u00b2\u207a"),
            ("[Ni(H\u2082O)\u2086]\u00b2\u207a", "#90EE90", "pale green", "[Ni(NH\u2083)\u2086]\u00b2\u207a", "violet", "excess NH\u2083(aq)", "Aqueous Ni\u00b2\u207a"),
            ("[Cr(H\u2082O)\u2086]\u00b3\u207a", "#EE82EE", "violet", "[Cr(NH\u2083)\u2086]\u00b3\u207a", "yellow", "excess NH\u2083(aq)", "Aqueous Cr\u00b3\u207a"),
            ("[Cu(H\u2082O)\u2086]\u00b2\u207a", "#ADD8E6", "pale blue", "[CuCl\u2084]\u00b2\u207b", "yellow-green", "excess Cl\u207b(aq)", "Aqueous Cu\u00b2\u207a"),
            ("[Fe(H\u2082O)\u2086]\u00b2\u207a", "#90EE90", "pale green", "[Fe(CN)\u2086]\u2074\u207b", "yellow", "CN\u207b(aq)", "Aqueous Fe\u00b2\u207a"),
            ("[Mn(H\u2082O)\u2086]\u00b2\u207a", "#FFB6C1", "pale pink", "[Mn(EDTA)]\u00b2\u207b", "pale pink", "EDTA\u2074\u207b", "Aqueous Mn\u00b2\u207a"),
            ("[Co(H\u2082O)\u2086]\u00b2\u207a", "#FFC0CB", "pink", "[Co(NH\u2083)\u2086]\u00b3\u207a", "yellow", "excess NH\u2083(aq)", "Aqueous Co\u00b2\u207a"),
            ("[Cu(NH\u2083)\u2084(H\u2082O)\u2082]\u00b2\u207a", "#00008B", "deep blue", "[Cu(EDTA)]\u00b2\u207b", "blue", "EDTA\u2074\u207b", "Cu\u00b2\u207a/NH\u2083 complex"),
        ]

        self.reaction = rnd.choice(reactions)
        (self.reactant, self.color1_hex, self.color1, self.product,
         self.color2, self.ligand, self.display_name) = self.reaction

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a ligand substitution reaction. "
            "The starting complex and the added ligand are shown in the diagram. "
            "What colour will the resulting solution be?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Ligand substitution"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts/superscripts to LaTeX for math mode
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-', '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5'
        })
        
        reactant_tex = self.reactant.translate(tex_map)
        product_tex = self.product.translate(tex_map)
        ligand_tex = self.ligand.translate(tex_map)
        display_name_tex = self.display_name.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The starting solution is }} \\mathrm{{{display_name_tex}}} \\text{{, which exists as the {self.color1}}} \\\\"
            f"&\\quad \\text{{complex }} \\mathrm{{{reactant_tex}}}. \\\\"
            f"&\\text{{2. Adding {self.ligand} (}}\\mathrm{{{ligand_tex}}}\\text{{) results in a ligand substitution reaction.}} \\\\"
            f"&\\text{{3. The ligands in the coordination sphere are replaced to form: }} \\mathrm{{{product_tex}}}. \\\\"
            f"&\\text{{4. This specific complex is defined by its}} \\\\"
            f"&\\quad \\text{{characteristic {self.color2} color.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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
        add_formula_label(ax, 2.6, 0.3, self.display_name, fontsize=12)

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
            "Based on the d-orbital splitting diagram provided, calculate the wavelength (in nm) "
            "of light absorbed by this complex.\n\n"
            f"(Given: h = 6.626\u00d710\u207b\u00b3\u2074 J\u00b7s, c = 3.00\u00d710\u2078 m/s, N\u2090 = 6.022\u00d710\u00b2\u00b3 mol\u207b\u00b9)"
        )

        self.topic = "Chemistry of transition elements"
        self.subtopic = "Colour of complexes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a catalytic cycle involving a transition metal. "
            "Between which two oxidation states does the catalyst cycle?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Redox and catalysis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts/superscripts to LaTeX for math mode
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-', '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5', '⁶': '^6', '⁷': '^7'
        })
        
        species1_tex = self.species1.translate(tex_map)
        species2_tex = self.species2.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. A transition metal catalyst works by providing an alternative pathway} \\\\"
            "&\\quad \\text{with a lower activation energy, often by changing its oxidation state.} \\\\"
            f"&\\text{{2. The catalytic cycle shown involves the species }} \\mathrm{{{species1_tex}}} \\text{{ and }} \\mathrm{{{species2_tex}}}. \\\\"
            "&\\text{3. For simple monoatomic ions, the oxidation state corresponds directly} \\\\"
            "&\\quad \\text{to the charge on the ion:} \\\\"
            f"&\\quad \\bullet \\, \\mathrm{{{species1_tex}}} \\text{{ represents the {self.ox1} oxidation state.}} \\\\"
            f"&\\quad \\bullet \\, \\mathrm{{{species2_tex}}} \\text{{ represents the {self.ox2} oxidation state.}} \\\\"
            f"&\\text{{4. Therefore, the catalyst cycles between the {self.ox1} and {self.ox2} states.}} \\\\"
            f"&\\text{{5. Consequently, the correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows two complex ions and their stability constants (Kstab). "
            "Is the ligand exchange shown in the diagram feasible?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Stability constants"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        comparison_word = "greater" if self.exchange['feasible'] else "less"
        conclusion = "feasible (Yes)" if self.exchange['feasible'] else "not feasible (No)"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. A ligand exchange is thermodynamically feasible if the new complex} \\\\"
            "&\\quad \\text{is more stable (has a higher } K_{stab} \\text{) than the initial complex.} \\\\"
            f"&\\text{{2. Initial }} K_{{stab}} = \\text{{{self.exchange['Kstab_initial']}}} \\\\"
            f"&\\text{{3. Final }} K_{{stab}} = \\text{{{self.exchange['Kstab_final']}}} \\\\"
            f"&\\text{{4. Because the final value is {comparison_word} than the initial value,}} \\\\"
            f"&\\quad \\text{{the exchange is {conclusion}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "Name the alkane shown in the structural formula using IUPAC nomenclature.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Nomenclature"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Identify the longest continuous carbon chain to find the parent alkane.} \\\\"
            "&\\text{2. Identify the alkyl substituent groups branching off this main chain.} \\\\"
            "&\\text{3. Number the parent chain starting from the end that assigns the lowest} \\\\"
            "&\\quad \\text{possible sequence of numbers (locants) to these substituents.} \\\\"
            "&\\text{4. Assemble the name: use commas between numbers, hyphens between} \\\\"
            "&\\quad \\text{numbers and letters, and list substituents alphabetically.} \\\\"
            f"&\\text{{5. Applying these IUPAC rules to the formula yields: {self.name}.}} \\\\"
            f"&\\text{{6. Therefore, the correct option is {self.answer}.}}"
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
            "The diagram shows structural isomers for a specific molecular formula. "
            "How many structural isomers does the molecular formula shown in the diagram have?"
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        formula_tex = self.formula.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Structural isomers are compounds with the same molecular formula} \\\\"
            "&\\quad \\text{but different structural arrangements (chain, position, or functional group).} \\\\"
            f"&\\text{{2. For the formula }}\\mathrm{{{formula_tex}}}\\text{{, the unique structural isomers are:}} \\\\"
        )
        
        for name in self.isomer_names:
            # Fixing the C3H8O typo if it appears in the text
            display_name = "methoxyethane" if name == "methoxymethane" and "3" in self.formula else name
            self.reasoning += f"&\\quad \\bullet \\, \\text{{{display_name}}} \\\\"
            
        self.reasoning += (
            f"&\\text{{3. Summing these up, we find a total of {self.answer} structural isomers.}} \\\\"
            f"&\\text{{Note: Stereoisomers (like cis-trans) are not counted as structural isomers.}} \\\\"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Shrink the canvas from (10,8) to a neat (6,3) card size
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 3)
        ax.axis('off')

        # Center the formula prominently in the middle of the smaller canvas
        add_formula_label(ax, 3, 1.5, f"Molecular Formula:\n{self.formula}", 
                          fontsize=20, weight='bold', ha='center',
                          bbox_style=dict(boxstyle='round,pad=1', facecolor='lightyellow', edgecolor='black'))

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
            f"Identify whether the isomer shown in the diagram is the E or Z isomer."
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Geometric isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        # Determine the positional description based on the chosen isomer
        if self.shown_isomer == "E":
            position = "opposite sides"
            specific_desc = self.compound[1]
        else:
            position = "the same side"
            specific_desc = self.compound[2]

        # Define the map to turn Unicode subscripts into LaTeX inline math
        tex_map = str.maketrans({
            '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', 
            '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$'
        })
        
        # Apply the map to the variables that actually contain formulas
        base_name_tex = self.base_name.translate(tex_map)
        specific_desc_tex = specific_desc.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Using Cahn-Ingold-Prelog (CIP) rules, assign priorities to the two} \\\\"
            "&\\quad \\text{groups attached to each carbon atom of the C=C double bond.} \\\\"
            f"&\\text{{2. In the given diagram, the high-priority groups are on {position}.}} \\\\"
            f"&\\text{{3. Specifically for {base_name_tex}, this means the {specific_desc_tex}.}} \\\\"
            "&\\text{4. 'E' (entgegen) indicates opposite sides, while 'Z' (zusammen) indicates the same side.} \\\\"
            f"&\\text{{5. Therefore, the diagram represents the {self.answer} isomer.}}"
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
            "The diagram shows the two enantiomers of an organic compound. "
            f"One enantiomer rotates plane-polarized light by {self.rotation}{self.rotation_value}\u00b0. "
            "Based on the groups shown in the diagram, at which carbon number in the main chain is the chiral centre located?"
        )

        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Isomerism: optical"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        # Define the map to turn Unicode subscripts into LaTeX inline math
        tex_map = str.maketrans({
            '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', 
            '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$'
        })
        
        # Translate each group in the list to handle chemical subscripts
        groups_tex = [g.translate(tex_map) for g in self.molecule['groups']]
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. A chiral centre is a carbon atom bonded to four different groups.} \\\\"
            f"&\\text{{2. The diagram shows a central carbon bonded to: {', '.join(groups_tex)}.}} \\\\"
            f"&\\text{{3. Assembling these groups forms the molecule {self.molecule['name']}.}} \\\\"
            "&\\text{4. Numbering the longest carbon chain according to IUPAC rules,} \\\\"
            f"&\\quad \\text{{this specific carbon atom is at position {self.answer}.}} \\\\"
            f"&\\text{{5. Therefore, the chiral centre is at C{self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')

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
        draw_circle_atom(ax, center_x2, center_y, 'C', radius=0.4,
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a benzene electrophilic aromatic substitution mechanism. "
            "The reagents and conditions are shown on the diagram. "
            "What is the electrophile in this reaction?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydrocarbons"
        self.subtopic = "Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts/superscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-', '⁴': '^4', '⁵': '^5', '⁶': '^6', '⁷': '^7'
        })
        
        reagents_tex = self.reaction['reagents'].translate(tex_map)
        electrophile_tex = self.reaction['electrophile'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Identify the reagents provided in the diagram:} \\\\"
            f"&\\quad \\mathrm{{{reagents_tex}}} \\\\"
            f"&\\text{{2. These reagents are used for {self.reaction['reaction_name'].lower()}.}} \\\\"
            f"&\\text{{3. They react together to generate the active electrophile: }} \\mathrm{{{electrophile_tex}}} \\\\"
            f"&\\text{{4. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Electrophilic Aromatic Substitution", fontsize=14)

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
        ax.text(x3, y3 - 1.5, "Substituted Benzene", fontsize=11, ha='center', fontweight='bold')

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a propagation step of free radical substitution. "
            "The reactants are shown in the diagram. "
            "What is the organic product formed in this step?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydrocarbons"
        self.subtopic = "Alkane reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        
        alkane_tex = self.alkane.translate(tex_map)
        product_tex = self.product.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. In free radical substitution, a halogen radical reacts with an alkane} \\\\"
            "&\\quad \\text{by abstracting a hydrogen atom, forming an intermediate alkyl radical.} \\\\"
            "&\\text{2. This alkyl radical then reacts with a halogen molecule to yield the} \\\\"
            "&\\quad \\text{final haloalkane product and regenerate the halogen radical.} \\\\"
            f"&\\text{{3. The net result replaces one hydrogen atom on }} \\mathrm{{{alkane_tex}}} \\text{{ with the halogen.}} \\\\"
            f"&\\text{{4. The organic product formed is therefore }} \\mathrm{{{product_tex}}} \\text{{ ({self.product_name}).}} \\\\"
            f"&\\text{{5. This matches option {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows a numbered benzene ring with a substituent group. "
            "When this compound undergoes further electrophilic substitution, "
            "which position(s) will the new substituent preferentially occupy?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydrocarbons"
        self.subtopic = "Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        subst_tex = self.subst['substituent'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram shows the molecule {self.subst['compound']}.}} \\\\"
            f"&\\text{{2. The substituent group attached to position 1 is }} \\mathrm{{{subst_tex}}}. \\\\"
            f"&\\text{{3. The }} \\mathrm{{{subst_tex}}} \\text{{ group is known to be {self.subst['type']}.}} \\\\"
            f"&\\text{{4. Therefore, an incoming electrophile will preferentially substitute}} \\\\"
            f"&\\quad \\text{{at positions {correct}.}} \\\\"
            f"&\\text{{5. This makes option {self.answer} the correct choice.}}"
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
                'order': 'ethanol < water < phenol',
                'correct': 'ethanol < water < phenol (phenol most acidic)',
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
                'correct': 'phenol < 2-chlorophenol < 2,4-dichlorophenol (2,4-dichlorophenol most acidic)',
            },
            {
                'compounds': ['ethanol', 'water', 'ethanoic acid'],
                'formulas': ['C\u2082H\u2085OH', 'H\u2082O', 'CH\u2083COOH'],
                'pKa': [15.9, 15.7, 4.8],
                'order': 'ethanol < water < ethanoic acid',
                'correct': 'ethanol < water < ethanoic acid (ethanoic acid most acidic)',
            },
            {
                'compounds': ['phenol', '4-methylphenol', '4-nitrophenol'],
                'formulas': ['C\u2086H\u2085OH', '4-CH\u2083C\u2086H\u2084OH', '4-NO\u2082C\u2086H\u2084OH'],
                'pKa': [9.9, 10.2, 7.1],
                'order': '4-methylphenol < phenol < 4-nitrophenol',
                'correct': '4-methylphenol < phenol < 4-nitrophenol (4-nitrophenol most acidic)',
            },
            {
                'compounds': ['methanol', 'phenol', 'carbonic acid'],
                'formulas': ['CH\u2083OH', 'C\u2086H\u2085OH', 'H\u2082CO\u2083'],
                'pKa': [15.5, 9.9, 6.4],
                'order': 'methanol < phenol < carbonic acid',
                'correct': 'methanol < phenol < carbonic acid (carbonic acid most acidic)',
            },
            {
                'compounds': ['propanol', 'phenol', 'methanoic acid'],
                'formulas': ['C\u2083H\u2087OH', 'C\u2086H\u2085OH', 'HCOOH'],
                'pKa': [16.1, 9.9, 3.7],
                'order': 'propanol < phenol < methanoic acid',
                'correct': 'propanol < phenol < methanoic acid (methanoic acid most acidic)',
            },
            {
                'compounds': ['phenol', 'benzoic acid', 'nitric acid'],
                'formulas': ['C\u2086H\u2085OH', 'C\u2086H\u2085COOH', 'HNO\u2083'],
                'pKa': [9.9, 4.2, -1.4],
                'order': 'phenol < benzoic acid < nitric acid',
                'correct': 'phenol < benzoic acid < nitric acid (nitric acid most acidic)',
            },
        ]

        self.comp = rnd.choice(comparisons)
        self.labels_abc = ['A', 'B', 'C']

        # Sort compounds by pKa (highest to lowest = weakest to strongest acid)
        sorted_indices = sorted(range(3), key=lambda i: self.comp['pKa'][i], reverse=True)
        correct_order_str = ' < '.join([self.labels_abc[i] for i in sorted_indices])

        # Build MCQ - shuffle order of compounds
        from itertools import permutations
        perms = list(permutations(self.labels_abc))
        rnd.shuffle(perms)
        wrong_opts = []
        for p in perms:
            opt = ' < '.join(p)
            if opt != correct_order_str and opt not in wrong_opts:
                wrong_opts.append(opt)
            if len(wrong_opts) >= 3:
                break

        options = wrong_opts[:3] + [correct_order_str]
        rnd.shuffle(options)

        labels = ["A", "B", "C", "D"]
        self.choices = options
        self.answer = labels[options.index(correct_order_str)]
        self.choices_display = {lbl: opt for lbl, opt in zip(labels, options)}

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The table shows three compounds. "
            "Arrange them in order of increasing acidity (weakest acid first).\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydroxy compounds"
        self.subtopic = "Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Acidity correlates with } pK_a \\text{: a lower } pK_a \\text{ indicates a stronger acid.} \\\\"
            "&\\text{Based on their relative stabilities (due to electron-donating or} \\\\"
            "&\\quad \\text{withdrawing groups), the approximate } pK_a \\text{ values are:} \\\\"
        )
        
        for i in sorted_indices:
            name = self.comp['compounds'][i]
            lbl = self.labels_abc[i]
            pka = self.comp['pKa'][i]
            self.reasoning += f"&\\quad \\bullet \\, \\text{{Compound {lbl} ({name}): }} pK_a \\approx {pka} \\\\"
            
        # Safely construct the order string so < stays in math mode while letters are in text mode
        safe_order_tex = " < ".join([f"\\text{{{self.labels_abc[i]}}}" for i in sorted_indices])
        
        self.reasoning += (
            "&\\text{Arranging them from highest } pK_a \\text{ to lowest } pK_a \\text{ (weakest to strongest) gives:} \\\\"
            f"&\\quad {safe_order_tex} \\\\"
            f"&\\textbf{{Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, "Acidity Comparison", fontsize=16)

        headers = ['Label', 'Compound', 'Formula']
        x_cols = [2, 6, 10]
        for i, header in enumerate(headers):
            ax.text(x_cols[i], 5.5, header, fontsize=13, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgray',
                            edgecolor='black', linewidth=2))

        row_height = 0.8
        for row_idx in range(3):
            y = 5.5 - (row_idx + 1) * row_height
            ax.text(x_cols[0], y, self.labels_abc[row_idx], fontsize=12, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgreen', pad=0.3))
            ax.text(x_cols[1], y, self.comp['compounds'][row_idx], fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
            ax.text(x_cols[2], y, self.comp['formulas'][row_idx], fontsize=12, ha='center',
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "Phenol reacts with the reagent under the conditions shown in the diagram. "
            "What is the organic product formed?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydroxy compounds"
        self.subtopic = "Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-'
        })
        reagent_tex = self.rxn['reagent'].translate(tex_map)
        product_tex = self.rxn['product'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram shows phenol reacting with }} \\mathrm{{{reagent_tex}}} \\text{{ under {self.rxn['conditions']}.}} \\\\"
            f"&\\text{{2. This specific combination of reagents and conditions causes {self.rxn['name'].lower()}.}} \\\\"
            f"&\\text{{3. The organic product formed in this reaction is }} \\mathrm{{{product_tex}}}. \\\\"
            f"&\\text{{4. As a supplementary note, the expected observation is: {self.rxn['observation']}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 6.5, "Reaction of Phenol", fontsize=16)

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows an alcohol undergoing an oxidation reaction. "
            "Based on the starting alcohol and the reagents shown in the image, what is the organic product formed?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts and arrows to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-', '→': '\\rightarrow', '\u2192': '\\rightarrow'
        })
        
        formula_tex = self.alcohol_formula.translate(tex_map)
        product_tex = self.product_formula.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The starting material, {self.alcohol_name} (}}\\mathrm{{{formula_tex}}}\\text{{), is a {self.classification} alcohol.}} \\\\"
            f"&\\text{{2. When treated with an oxidizing agent like acidified }} \\mathrm{{K_2Cr_2O_7}} \\text{{:}} \\\\"
        )
        
        if self.classification == "primary":
            self.reasoning += "&\\quad \\text{- Primary alcohols oxidize to aldehydes, and further to carboxylic acids.} \\\\"
        elif self.classification == "secondary":
            self.reasoning += "&\\quad \\text{- Secondary alcohols oxidize to ketones and resist further oxidation.} \\\\"
        else:
            self.reasoning += "&\\quad \\text{- Tertiary alcohols resist oxidation under these conditions.} \\\\"

        self.reasoning += (
            f"&\\text{{3. The resulting product is: }} \\mathrm{{{product_tex}}} \\\\"
            f"&\\text{{4. {self.note.capitalize()}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 6, 6.5, f"Oxidation of an Alcohol", fontsize=16)

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "Based on the reaction shown in the diagram, what is the main alkene product formed?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol dehydration"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        
        alc_tex = self.alcohol_formula.translate(tex_map)
        alk_tex = self.alkene_formula.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The starting material is {self.alcohol_name} (}}\\mathrm{{{alc_tex}}}\\text{{).}} \\\\"
            "&\\text{2. Heating an alcohol with concentrated } \\mathrm{H_2SO_4} \\text{ causes an elimination} \\\\"
            "&\\quad \\text{reaction (dehydration), removing an -OH and an adjacent -H.} \\\\"
            "&\\text{3. This elimination forms a C=C double bond.} \\\\"
            f"&\\text{{4. The resulting major organic product is }} \\mathrm{{{alk_tex}}} \\text{{ ({self.alkene_name}).}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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

        add_title_box(ax, 6, 5.5, "Reaction of an Alcohol", fontsize=16)

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "An acyl chloride reacts with a nucleophile at room temperature, as shown in the diagram. "
            "What are the products of this reaction?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        
        acyl_tex = self.rxn['acyl_chloride'].translate(tex_map)
        nuc_tex = self.rxn['nucleophile'].translate(tex_map)
        prod_tex = self.rxn['product'].translate(tex_map)
        byprod_tex = self.rxn['by_product'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The reactants are {self.rxn['acyl_name']} (}}\\mathrm{{{acyl_tex}}}\\text{{) and {self.rxn['nuc_name']} (}}\\mathrm{{{nuc_tex}}}\\text{{).}} \\\\"
            "&\\text{2. Acyl chlorides undergo nucleophilic addition-elimination reactions.} \\\\"
            "&\\text{3. The nucleophile attacks the carbonyl carbon, and the chloride group is eliminated,} \\\\"
            "&\\quad \\text{combining with a proton to release } \\mathrm{HCl} \\text{ as a by-product.} \\\\"
            f"&\\text{{4. The resulting organic product is {self.rxn['product_name']} (}}\\mathrm{{{prod_tex}}}\\text{{).}} \\\\"
            f"&\\text{{5. The overall equation is: }} \\mathrm{{{acyl_tex} + {nuc_tex} \\rightarrow {prod_tex} + {byprod_tex}}} \\\\"
            f"&\\text{{6. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

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
        self.subtopic = "Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

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

        y_ceiling = max(self.display_rates) * 1.1 # Adds a 10% head-room ceiling
        ax.set_ylim(0, y_ceiling)

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows an acyl chloride (RCOCl) reacting with a reagent whose formula is shown in the diagram. "
            "What is the organic product formed?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "Acyl chloride reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-'
        })
        
        reagent_tex = self.reagent_formula.translate(tex_map)
        product_tex = self.products.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram shows an acyl chloride (}}\\mathrm{{RCOCl}}\\text{{) reacting with {self.reagent_name} (}}\\mathrm{{{reagent_tex}}}\\text{{).}} \\\\"
            "&\\text{2. Acyl chlorides undergo nucleophilic addition-elimination reactions} \\\\"
            "&\\quad \\text{where the nucleophile replaces the chlorine atom.} \\\\"
            f"&\\text{{3. The organic product formed has the general structure }} \\mathrm{{{product_tex}}}. \\\\"
            f"&\\text{{4. This corresponds to the {self.product_name} family/type.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows the structure of an amino acid at three different pH values. "
            "Which structure (A, B, or C) represents the zwitterion?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts and superscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '⁺': '^+', '⁻': '^-'
        })
        zwit_tex = self.aa['zwitterion'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. A zwitterion is an ion that contains both positive and negative} \\\\"
            "&\\quad \\text{charge centers, making it overall electrically neutral.} \\\\"
            "&\\text{2. In amino acids, this occurs at the isoelectric point where the} \\\\"
            "&\\quad \\text{amino group is protonated (} \\mathrm{-NH_3^+} \\text{) and the carboxyl group} \\\\"
            "&\\quad \\text{is deprotonated (} \\mathrm{-COO^-} \\text{).} \\\\"
            "&\\text{3. Inspecting the diagram, the structure with both of these charged} \\\\"
            f"&\\quad \\text{{groups is }} \\mathrm{{{zwit_tex}}}. \\\\"
            f"&\\text{{4. This corresponds to Structure {correct}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        x_positions = [0.5, 5.0, 9.5]
        for i, (label, ph_label, formula, color, charge) in enumerate(self.structures):
            x = x_positions[i]
            ax.text(x + 2, 5.8, f"Structure {label}", fontsize=13, ha='center',
                    fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='lightgray', pad=0.3))
            
            draw_labeled_box(ax, x, 3.0, 3.8, 1.8, formula, "",
                             facecolor=color, edgecolor='black', linewidth=2)
            
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.choices))

        self.description = (
            "The diagram shows an electrophoresis strip for an amino acid. "
            "Based on the pH and isoelectric point (pI) shown in the diagram, in which direction will the amino acid migrate when voltage is applied?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Determine the general type of amino acid to teach the logic
        if self.scenario['pI'] > 7:
            aa_type = "a basic"
        elif self.scenario['pI'] < 5:
            aa_type = "an acidic"
        else:
            aa_type = "a neutral"

        # Determine the relative pH vs pI comparison
        if self.scenario['pH'] > self.scenario['pI']:
            comparison = "greater than"
        elif self.scenario['pH'] < self.scenario['pI']:
            comparison = "less than"
        else:
            comparison = "equal to"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram specifies {self.scenario['amino_acid'].capitalize()}, which is {aa_type} amino acid.}} \\\\"
            f"&\\quad \\text{{This means its isoelectric point (pI) is approximately {self.scenario['pI']}.}} \\\\"
            f"&\\text{{2. The buffer pH ({self.scenario['pH']}) is {comparison} the pI of the amino acid.}} \\\\"
        )

        if comparison == "equal to":
            self.reasoning += (
                "&\\text{3. When pH = pI, the amino acid exists as a neutral zwitterion} \\\\"
                "&\\quad \\text{and will not migrate in an electric field.} \\\\"
            )
        elif comparison == "greater than":
            self.reasoning += (
                "&\\text{3. When pH } > \\text{ pI, the amino acid deprotonates and becomes} \\\\"
                "&\\quad \\text{negatively charged, so it migrates toward the positive Anode.} \\\\"
            )
        else:
            self.reasoning += (
                "&\\text{3. When pH } < \\text{ pI, the amino acid protonates and becomes} \\\\"
                "&\\quad \\text{positively charged, so it migrates toward the negative Cathode.} \\\\"
            )

        self.reasoning += (
            f"&\\text{{4. Therefore, the correct option is {self.answer}.}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Amino Acid Electrophoresis", fontsize=16)

        draw_labeled_box(ax, 12, 3, 1.5, 2, 'Anode', '',
                         facecolor='lightcoral', edgecolor='red', linewidth=3)
        draw_labeled_box(ax, 0.5, 3, 1.5, 2, 'Cathode', '',
                         facecolor='lightblue', edgecolor='blue', linewidth=3)

        paper = patches.Rectangle((2.5, 3.5), 9, 1, facecolor='wheat',
                                  edgecolor='black', linewidth=2)
        ax.add_patch(paper)

        ax.plot(7, 4, 'ko', markersize=15)
        ax.text(7, 4.8, 'Start position', fontsize=11, ha='center', fontweight='bold')

        info = (f"Amino acid: {self.scenario['amino_acid'].capitalize()}\n"
                f"Buffer pH = {self.scenario['pH']}")
        
        ax.text(7, 1.5, info, fontsize=14, ha='center',
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows a reaction scheme for amide formation. "
            "Based on the conditions shown on the reaction arrow, which reagents are used in this method?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amide formation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts to inline math for rendering inside \text{}
        tex_map = str.maketrans({
            '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', 
            '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$',
            '⁺': '$^+$', '⁻': '$^-$', 'Δ': '$\\Delta$'
        })
        
        name_tex = self.method_name.translate(tex_map)
        cond_tex = self.method['conditions'].translate(tex_map)
        reagents_tex = self.method['reagents'].translate(tex_map)
        product_tex = self.method['product'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram indicates an amide synthesis under these conditions:}} \\\\"
            f"&\\quad \\text{{{cond_tex}.}} \\\\"
            f"&\\text{{2. These specific conditions map directly to the method: {name_tex}.}} \\\\"
            f"&\\text{{3. The required reagents are {reagents_tex}.}} \\\\"
            f"&\\text{{4. The resulting product profile is {product_tex}.}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows two monomers reacting to form a polyamide. "
            "Based on the monomer structures shown in the diagram, which of the following is the repeat unit of this polymer?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Polymerisation"
        self.subtopic = "Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts to inline math for rendering inside \text{}
        tex_map = str.maketrans({
            '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', 
            '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$',
            '⁺': '$^+$', '⁻': '$^-$', '→': '$\\rightarrow$', '\u2192': '$\\rightarrow$'
        })
        
        repeat_tex = self.mono['repeat_unit'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\textbf{{Correct Option: {self.answer}}} \\\\"
            "&\\text{The initial diamine and diacid parameters follow standard condensation,} \\\\"
            "&\\text{eliminating water to form structural amide (-CONH-) linkages.} \\\\"
            "&\\text{Connecting the dehydrated monomer fragments directly yields the repeat unit:} \\\\"
            f"&\\quad \\mathrm{{{repeat_tex}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Polyamide Formation", fontsize=16)

        draw_labeled_box(ax, 1, 5.5, 3, 1,
                         self.mono['diamine_formula'],
                         "", facecolor='lightblue')

        ax.text(4.8, 6.0, '+', fontsize=20, ha='center', fontweight='bold')

        draw_labeled_box(ax, 5.5, 5.5, 3, 1,
                         self.mono['diacid_formula'],
                         "", facecolor='lightyellow')

        draw_arrow(ax, 9, 6.0, 11, 6.0, label="heat\n-H\u2082O",
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 11.5, 5.5, 2, 1, "Polyamide",
                         facecolor='lightgreen')

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows two monomers reacting to form a polyester. "
            "Based on the monomer structures shown in the diagram, which of the following is the repeat unit of this polymer?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Polymerisation"
        self.subtopic = "Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Safely convert Unicode subscripts to inline math for rendering inside \text{}
        tex_map = str.maketrans({
            '₀': '$_0$', '₁': '$_1$', '₂': '$_2$', '₃': '$_3$', '₄': '$_4$', 
            '₅': '$_5$', '₆': '$_6$', '₇': '$_7$', '₈': '$_8$', '₉': '$_9$',
            '⁺': '$^+$', '⁻': '$^-$', '→': '$\\rightarrow$', '\u2192': '$\\rightarrow$'
        })
        
        diol_tex = self.mono['diol_formula'].translate(tex_map)
        diacid_tex = self.mono['diacid_formula'].translate(tex_map)
        repeat_tex = self.mono['repeat_unit'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Diol: {diol_tex}}} \\\\"
            f"&\\text{{Diacid: {diacid_tex}}} \\\\"
            "&\\text{Condensation: -OH + -COOH } \\rightarrow \\text{ -COO- + H$_2$O} \\\\"
            f"&\\text{{Repeat unit: {repeat_tex}}} \\\\"
            f"&\\therefore \\textbf{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')

        add_title_box(ax, 7, 7.5, "Polyester Formation", fontsize=16)

        draw_labeled_box(ax, 1, 5.5, 3, 1,
                         self.mono['diol_formula'],
                         "", facecolor='lightblue')

        ax.text(4.8, 6.0, '+', fontsize=20, ha='center', fontweight='bold')

        draw_labeled_box(ax, 5.5, 5.5, 3, 1,
                         self.mono['diacid_formula'],
                         "", facecolor='lightyellow')

        draw_arrow(ax, 9, 6.0, 11, 6.0, label="heat\n-H\u2082O",
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 11.5, 5.5, 2, 1, "Polyester",
                         facecolor='lightgreen')

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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The repeating unit of an addition polymer is shown in the diagram. "
            "What is the monomer used to make this polymer?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Polymerisation"
        self.subtopic = "Addition polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        
        poly_tex = self.polymer_formula.translate(tex_map)
        mono_tex = self.monomer_formula.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The diagram shows the repeat unit of an addition polymer: }} \\mathrm{{{poly_tex}}} \\\\"
            "&\\text{2. Addition polymers form when C=C double bonds in the monomers} \\\\"
            "&\\quad \\text{break open to form continuous single bonds linking the units together.} \\\\"
            "&\\text{3. To find the monomer, remove the extension bonds crossing the brackets} \\\\"
            "&\\quad \\text{and restore the original C=C double bond(s) in the carbon backbone.} \\\\"
            f"&\\text{{4. Applying this reverse process yields the monomer: }} \\mathrm{{{mono_tex}}} \\\\"
            f"&\\text{{5. Therefore, the correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The table provides information about the chemical linkages and degradation mechanisms of three polymers. "
            f"{self.scenario['question']}\n\n"
            f"{self.options_text}"
        )
        self.topic = "Polymerisation"
        self.subtopic = "Degradable polymers"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Poly(ethene) is an addition polymer with a backbone of only non-polar} \\\\"
            "&\\quad \\text{C-C and C-H bonds. It is chemically inert and not biodegradable.} \\\\"
            "&\\text{Polyesters are condensation polymers that contain ester linkages (-COO-).} \\\\"
            "&\\quad \\text{These polar bonds can be broken down (hydrolysed) by water, acids, bases, or enzymes.} \\\\"
            "&\\text{Polyamides are condensation polymers containing amide linkages (-CONH-),} \\\\"
            "&\\quad \\text{which are also susceptible to hydrolysis, making them biodegradable.} \\\\"
            f"&\\text{{Addressing the specific question: \"{self.scenario['question']}\"}} \\\\"
            f"&\\text{{The correct option is {self.answer}.}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows monomers used in condensation polymerization. "
            "Based on the functional groups shown in the diagram, what type of polymer is formed?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Polymerisation"
        self.subtopic = "Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the reacting monomers from the given structure.}\\\\"
            f"&\\quad \\text{{Monomers}} = \\text{{{self.monomers}}}\\\\"
            "&\\text{Step 2: Identify the functional group linkage formed during condensation.}\\\\"
            f"&\\quad \\text{{Linkage}} = \\text{{{self.linkage}}}\\\\"
            "&\\text{Step 3: Classify the resulting polymer based on the linkage type.}\\\\"
            f"&\\quad \\text{{Polymer type}} = \\text{{{correct}}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows a two-step organic synthesis with the starting material and final product labelled. "
            "Based on the reaction pathway and conditions shown, what is the hidden intermediate compound?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Organic synthesis"
        self.subtopic = "Organic synthesis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to LaTeX math subscripts
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9'}
        latex_formula = self.route['int_formula']
        for k, v in subs.items():
            latex_formula = latex_formula.replace(k, v)
        
        # Flatten the step 1 label so it prints cleanly without newlines
        step1_reagent = self.route['step1_label'].replace('\n', ' ')

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Analyze the first reaction.}\\\\"
            f"&\\quad \\text{{{self.route['start']} + {step1_reagent} }} \\rightarrow \\text{{ intermediate}}\\\\"
            "&\\text{Step 2: Identify the intermediate compound.}\\\\"
            f"&\\quad \\text{{Intermediate is {self.route['intermediate']} (}}\\mathrm{{{latex_formula}}}\\text{{)}}\\\\"
            "&\\text{Step 3: Confirm the second reaction leads to the final product.}\\\\"
            f"&\\quad \\text{{intermediate }} \\rightarrow \\text{{ {self.route['end']}}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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

        draw_arrow(ax, 7.0, 4.0, 8.5, 4.0, label=self.route['step2_label'],
                   label_position='above', color='black', linewidth=2.5)

        draw_labeled_box(ax, 9.5, 3.5, 3.5, 1, self.route['end'], facecolor='lightgreen')


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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows a multi-step synthesis route with a hidden intermediate. "
            "Based on the starting material and final product shown in the diagram, identify the intermediate compound.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Organic synthesis"
        self.subtopic = "Synthesis routes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the starting material and the final product.}\\\\"
            f"&\\quad \\text{{{self.pathway['start']}}} \\rightarrow \\text{{?}} \\rightarrow \\text{{{self.pathway['end']}}}\\\\"
            "&\\text{Step 2: Determine the required intermediate compound for this route.}\\\\"
            f"&\\quad \\text{{Intermediate is {self.pathway['intermediate']}}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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
                ax.text(x_pos + 1.25, 3.1, '', fontsize=28, ha='center',
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The mass spectrum shows several peaks. Based on the m/z value indicated by the arrow in the diagram, "
            "identify the fragment ion responsible for this peak.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Analytical techniques"
        self.subtopic = "Mass spectrometry"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts and superscripts to LaTeX math format
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9',
                '\u207a':'^+', '\u207b':'^-'}
        
        latex_ion = self.ion
        for k, v in subs.items():
            latex_ion = latex_ion.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Note the mass-to-charge ratio (m/z) of the targeted peak in the spectrum.}\\\\"
            f"&\\quad m/z = {self.mz}\\\\"
            "&\\text{Step 2: Determine which fragment has a molecular mass matching this value.}\\\\"
            f"&\\quad \\text{{A mass of {self.mz} corresponds to the {self.name}.}}\\\\"
            "&\\text{Step 3: Identify the correct chemical formula for this fragment ion.}\\\\"
            f"&\\quad \\text{{Formula}} = \\mathrm{{{latex_ion}}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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
        ax.set_title(f'Mass Spectrum',
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
        self.subtopic = "Thin-layer chromatography"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Step 1: Find the distance traveled by {self.questioned_spot['name']} from the baseline.}}\\\\"
            f"&\\quad \\text{{Distance (substance)}} = {self.questioned_spot['height']} \\text{{ cm}}\\\\"
            "&\\text{Step 2: Find the distance traveled by the solvent front from the baseline.}\\\\"
            f"&\\quad \\text{{Distance (solvent)}} = {self.solvent_front} \\text{{ cm}}\\\\"
            "&\\text{Step 3: Apply the retention factor } (R_f) \\text{ formula.}\\\\"
            "&\\quad R_f = \\frac{\\text{distance traveled by substance}}{\\text{distance traveled by solvent}}\\\\"
            f"&\\quad R_f = \\frac{{{self.questioned_spot['height']}}}{{{self.solvent_front}}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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
        self.subtopic = "Gas-liquid chromatography"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        total_area_sum = sum(p['area'] for p in self.peaks)
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Step 1: Identify the peak area for {self.questioned_peak['name']}.}}\\\\"
            f"&\\quad \\text{{Area (target)}} = {self.questioned_peak['area']}\\\\"
            "&\\text{Step 2: Calculate the total area of all peaks in the chromatogram.}\\\\"
            f"&\\quad \\text{{Total Area}} = {total_area_sum}\\\\"
            "&\\text{Step 3: Calculate the percentage composition.}\\\\"
            "&\\quad \\text{Percentage} = \\frac{\\text{Area (target)}}{\\text{Total Area}} \\times 100\\%\\\\"
            f"&\\quad \\text{{Percentage}} = \\frac{{{self.questioned_peak['area']}}}{{{total_area_sum}}} \\times 100\\%\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}\\%"
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
        self.desc_text = self.absorption[3]

        self.peak_position = rnd.randint(self.wavenumber_min, self.wavenumber_max)

        options = [self.group] + list(self.absorption[4])
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(self.group))

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The IR spectrum shows a characteristic absorption with the wavenumber annotated on the diagram. "
            "Which functional group is responsible for the labelled absorption?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Analytical techniques"
        self.subtopic = "IR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the wavenumber of the marked absorption peak.}\\\\"
            f"&\\quad \\text{{Peak position}} = {self.peak_position} \\text{{ cm}}^{{-1}}\\\\"
            "&\\text{Step 2: Note the characteristic shape and intensity of the peak.}\\\\"
            f"&\\quad \\text{{Peak shape}} = \\text{{{self.desc_text}}}\\\\"
            "&\\text{Step 3: Match these features to the corresponding functional group.}\\\\"
            f"&\\quad \\text{{These properties are characteristic of the }} \\text{{{self.group}}} \\text{{ absorption.}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))

        wavenumbers = np.linspace(4000, 400, 500)
        transmittance = np.ones_like(wavenumbers) * 80

        peak_width = 50 if "sharp" in self.desc_text else 150
        if "broad" in self.desc_text:
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
        ax.set_title(f'IR Spectrum ({self.desc_text} absorption at '
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The ¹H NMR spectrum of an organic compound is shown. "
            "One peak is highlighted with its chemical shift (δ) and integration annotated on the diagram. "
            "Which hydrogen environment does the labelled peak represent?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Analytical techniques"
        self.subtopic = "\u00b9H NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts and special characters to LaTeX math format
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9',
                '×': '\\times '}
        
        latex_assignment = self.peak_assignment
        for k, v in subs.items():
            latex_assignment = latex_assignment.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the chemical shift (}\\delta\\text{) of the highlighted peak.}\\\\"
            f"&\\quad \\delta = {self.peak_shift} \\text{{ ppm}}\\\\"
            "&\\text{Step 2: Note the integration value, which indicates the number of protons.}\\\\"
            f"&\\quad \\text{{Integration}} = {self.peak_integration}\\text{{H}}\\\\"
            "&\\text{Step 3: Match these values to the corresponding proton environment.}\\\\"
            f"&\\quad \\text{{This corresponds to the }} \\mathrm{{{latex_assignment}}} \\text{{ environment.}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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
            "The ¹³C NMR spectrum of an organic compound is shown below. "
            "How many peaks appear in the spectrum? (Give a numerical answer.)"
        )

        self.topic = "Analytical techniques"
        self.subtopic = "Carbon-13 NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Examine the spectrum and count the number of distinct vertical peaks.}\\\\"
            f"&\\quad \\text{{Total peaks visible}} = {self.molecule['num_peaks']}\\\\"
            "&\\text{Step 2: Note that each peak corresponds to a unique carbon environment.}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The image shows a peak from a ¹H NMR spectrum, along with its chemical shift (δ) and integration. "
            "Based on the pattern displayed in the diagram, what is the splitting pattern of this peak?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Analytical techniques"
        self.subtopic = "Proton (\u00b9H) NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to LaTeX math format for the key group
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9'}
        
        latex_group = self.mol['key_group']
        for k, v in subs.items():
            latex_group = latex_group.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Step 1: Identify the proton environment being analyzed.}}\\\\"
            f"&\\quad \\text{{Target group}} = \\mathrm{{{latex_group}}}\\\\"
            "&\\text{Step 2: Determine the number of equivalent protons on adjacent carbon atoms }(n).\\\\"
            f"&\\quad \\text{{Adjacent protons }} (n) = {self.mol['neighbors']}\\\\"
            "&\\text{Step 3: Apply the } n+1 \\text{ rule to find the number of lines in the splitting pattern.}\\\\"
            f"&\\quad \\text{{Number of lines}} = n + 1 = {self.mol['neighbors']} + 1 = {self.mol['neighbors'] + 1}\\\\"
            f"&\\quad \\text{{A peak with {self.mol['neighbors'] + 1} lines is called a }} \\text{{{self.mol['splitting']}}}.\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "An unknown organic compound was analyzed using Mass Spectrometry, IR Spectroscopy, and ¹H NMR. "
            "Based on the combined data provided in the table, identify the compound.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Analytical techniques"
        self.subtopic = "Combined spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode characters to LaTeX math format, and escape spaces so \mathrm renders them properly
        subs = {
            '\u2080': '_0', '\u2081': '_1', '\u2082': '_2', '\u2083': '_3', '\u2084': '_4', 
            '\u2085': '_5', '\u2086': '_6', '\u2087': '_7', '\u2088': '_8', '\u2089': '_9',
            '\u207a': '^+', '\u2211': '-', '\u2212': '-', '–': '-',
            ' ': '\\ ', '~': '\\sim '
        }
        
        latex_formula = self.compound['formula']
        latex_ir = self.compound['ir']
        latex_nmr = self.compound['nmr_peaks']
        latex_ms = self.compound['ms_frag']
        
        for k, v in subs.items():
            latex_formula = latex_formula.replace(k, v)
            latex_ir = latex_ir.replace(k, v)
            latex_nmr = latex_nmr.replace(k, v)
            latex_ms = latex_ms.replace(k, v)

        self.reasoning = (
            r"\[\begin{aligned}"
            r"&\text{Step 1: Use the molecular formula and } M^+ \text{ value to determine the mass.}\\"
            fr"&\quad \mathrm{{Formula:\ {latex_formula}\ (M^+ =\ {self.compound['molar_mass']})}} \\"
            r"&\text{Step 2: Identify functional groups from the IR spectrum.}\\"
            fr"&\quad \mathrm{{IR:\ {latex_ir}}} \\"
            r"&\text{Step 3: Analyze the }^{1}\text{H NMR peaks for proton environments.}\\"
            fr"&\quad \mathrm{{NMR:\ {latex_nmr}}} \\"
            r"&\text{Step 4: Confirm structural fragments from the Mass Spectrum.}\\"
            fr"&\quad \mathrm{{MS:\ {latex_ms}}} \\"
            fr"&\quad \text{{These features identify the compound as }} \text{{{correct}}}.\\"
            fr"&\quad \text{{Final Answer}} = \text{{{self.answer}}}"
            r"\end{aligned}\]"
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

        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram shows a Born-Haber energy cycle for an ionic compound. "
            f"Based on the chemical species and the direction of the arrow in the image, what enthalpy change does step {self.asked_step} represent?\n\n"
            f"{self.options_text}"
        )
        self.topic = "Chemical energetics"
        self.subtopic = "Born-Haber cycles and lattice enthalpy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to LaTeX math format for the compound
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9'}
        
        latex_compound = self.compound
        for k, v in subs.items():
            latex_compound = latex_compound.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{Step 1: Review the standard steps in the Born-Haber cycle for }} \\mathrm{{{latex_compound}}}.\\\\"
            f"&\\quad \\text{{Step A: {self.data['steps']['A'][1]}}}\\\\"
            f"&\\quad \\text{{Step B: {self.data['steps']['B'][1]}}}\\\\"
            f"&\\quad \\text{{Step C: {self.data['steps']['C'][1]}}}\\\\"
            f"&\\quad \\text{{Step D: {self.data['steps']['D'][1]}}}\\\\"
            f"&\\quad \\text{{Step E: {self.data['steps']['E'][1]}}}\\\\"
            f"&\\text{{Step 2: Identify the highlighted enthalpy change.}}\\\\"
            f"&\\quad \\text{{The diagram highlights Step {self.asked_step}, which corresponds to the {correct}.}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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

        self._emf_display_mode = "emf"
        self.answer = round(self.emf, 2)
        self.options = []

        self.description = (
            "An electrochemical cell is constructed using the two half-cells shown in the diagram. "
            "Using the standard electrode potentials (E\u00b0) provided in the image, "
            "calculate the standard cell EMF (E\u00b0cell) in V."
        )

        self.topic = "Electrode potentials and electrochemical cells"
        self.subtopic = "Standard electrode potentials"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Compare the standard electrode potentials } (E^{\\circ}) \\text{ to identify the anode and cathode.}\\\\"
            f"&\\quad \\text{{Anode (oxidation, lower }} E^{{\\circ}}\\text{{): }} \\mathrm{{{self.anode}}} \\; ({self.hc1['E_std']:+.2f} \\text{{ V}})\\\\"
            f"&\\quad \\text{{Cathode (reduction, higher }} E^{{\\circ}}\\text{{): }} \\mathrm{{{self.cathode}}} \\; ({self.hc2['E_std']:+.2f} \\text{{ V}})\\\\"
            "&\\text{Step 2: Calculate the standard cell EMF using the formula.}\\\\"
            "&\\quad E^{\\circ}_{\\text{cell}} = E^{\\circ}_{\\text{cathode}} - E^{\\circ}_{\\text{anode}}\\\\"
            f"&\\quad E^{{\\circ}}_{{\\text{{cell}}}} = ({self.hc2['E_std']:+.2f}) - ({self.hc1['E_std']:+.2f})\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.emf:.2f} \\text{{ V}}"
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
        if self._emf_display_mode == "emf":
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

        self.answer = round(self.t['eq_vol'], 1) if self.q_type == "equivalence_vol" else self.t['eq_ph']

        self.description = (
            "The image displays a titration curve. Based on the graph provided, "
            f"{'what volume of titrant is required to reach the equivalence point?' if self.q_type == 'equivalence_vol' else 'what is the pH at the equivalence point?'}"
        )

        self.topic = "Equilibria"
        self.subtopic = "pH curves and buffer solutions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"

        if self.q_type == "equivalence_vol":
            target_question = "volume of titrant at the equivalence point"
            target_axis = "x-axis"
            target_val = f"{self.t['eq_vol']:.1f} \\text{{ cm}}^3"
        else:
            target_question = "pH at the equivalence point"
            target_axis = "y-axis"
            target_val = f"{self.t['eq_ph']:.1f}"

        buffer_step = ""
        if self.t["has_buffer"]:
            buffer_step = f"&\\text{{(Note: A buffer region is visible around the half-equivalence volume of {self.t['eq_vol']/2:.1f} cm}}^3\\text{{)}}\\\\"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Locate the equivalence point, which is the steepest vertical section of the curve.}\\\\"
            f"&\\text{{Step 2: To find the {target_question}, read the {target_axis} value at this point.}}\\\\"
            f"&\\quad \\text{{Value from graph}} = {target_val}\\\\"
            f"{buffer_step}"
            f"&\\quad \\text{{Final Answer}} = {self.answer}\\\\"
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
        
        # --- Add dotted guidelines for points of interest ---
        for v_poi in [self.t['eq_vol'] / 2, self.t['eq_vol']]:
            ph_poi = self._ph_curve(np.array([v_poi]), self.t)[0]
            # Draw vertical line to x-axis and horizontal line to y-axis in one call
            ax.plot([v_poi, v_poi, 0], [0, ph_poi, ph_poi], color='gray', linestyle=':', linewidth=1)
            
            # Add exact numerical labels for the axes
            bbox_props = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="gray", alpha=0.9)
            ax.text(v_poi, 0.2, f"{v_poi:.1f}", color='black', fontsize=10, ha='center', va='bottom', bbox=bbox_props)
            ax.text(0.2, ph_poi, f"{ph_poi:.1f}", color='black', fontsize=10, ha='left', va='center', bbox=bbox_props)
        # ----------------------------------------------------

        ax.set_xlim(0, max_v)
        ax.set_ylim(0, 14)
        ax.set_xlabel(f"Volume of {self.t['base']} added / cm\u00b3",
                      fontsize=13, fontweight="bold")
        ax.set_ylabel("pH", fontsize=13, fontweight="bold")
        ax.set_title(f"pH Curve Analysis\n({self.t['type']})",
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
    Visual: ln(k) vs 1/T Arrhenius plot with gradient annotation; reaction name NOT shown
    Task:   Read the annotated gradient from the diagram and calculate Ea in kJ/mol
    Variables:
        Ea    = rnd.randint(40, 200)  kJ/mol  -> 161 distinct integer answers
        ln_A  = rnd.uniform(20, 50)          -> changes graph intercept/shape each instance
    """

    def __init__(self):
        R = 8.314
        self.Ea   = rnd.randint(40, 200)           # kJ/mol
        self.ln_A = round(rnd.uniform(20, 50), 2)  # pre-exponential factor (ln A)

        self.gradient = round(-self.Ea * 1000 / R, 0)  # K  (annotated on diagram)
        self.answer   = self.Ea                         # integer kJ/mol

        self.description = (
            "The graph shows an Arrhenius plot (ln k vs 1/T) for a chemical reaction. "
            "The gradient of the line is annotated on the diagram. "
            "Calculate the activation energy, Ea, in kJ mol⁻¹."
        )

        self.topic      = "Reaction kinetics"
        self.subtopic   = "Arrhenius equation and activation energy"
        self.source     = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        self.options    = []

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the gradient of the Arrhenius plot from the given diagram.}\\\\"
            f"&\\quad \\text{{Gradient}} = {self.gradient:.0f} \\text{{ K}}\\\\"
            "&\\text{Step 2: Relate the gradient to the activation energy } (E_a) \\text{ using the Arrhenius equation.}\\\\"
            "&\\quad \\text{Gradient} = -\\frac{E_a}{R}\\\\"
            f"&\\quad {self.gradient:.0f} = -\\frac{{E_a}}{{8.314}}\\\\"
            "&\\text{Step 3: Solve for } E_a \\text{ in } \\mathrm{J\\ mol^{-1}}.\\\\"
            f"&\\quad E_a = {-self.gradient:.0f} \\times 8.314 = {self.Ea * 1000:.0f} \\text{{ J mol}}^{{-1}}\\\\"
            "&\\text{Step 4: Convert the activation energy from Joules to kilojoules.}\\\\"
            f"&\\quad E_a = \\frac{{{self.Ea * 1000:.0f}}}{{1000}} = {self.Ea} \\text{{ kJ mol}}^{{-1}}\\\\"
            f"&\\quad \\text{{Final Answer}} = {self.answer}\\\\"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        R    = 8.314
        T    = np.linspace(300, 800, 300)
        invT = 1 / T
        ln_k = self.ln_A + (self.gradient / 1e3) * invT * 1e3  # = ln_A - Ea*1000/R * 1/T

        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(invT * 1e3, ln_k, color="royalblue", linewidth=3)

        ax.set_xlabel("1/T / K⁻¹  (× 10⁻³)", fontsize=13, fontweight="bold")
        ax.set_ylabel("ln k", fontsize=13, fontweight="bold")
        ax.set_title("Arrhenius Plot", fontsize=15, fontweight="bold")
        ax.grid(True, alpha=0.3, linestyle="--")

        # Annotate gradient using two points on the line
        i1, i2 = 30, 240
        x1, y1 = invT[i1] * 1e3, ln_k[i1]
        x2, y2 = invT[i2] * 1e3, ln_k[i2]

        ax.plot([x1, x2], [y1, y2], "r--", linewidth=1.5, alpha=0.6)
        ax.plot([x1, x2], [y1, y1], "r-",  linewidth=1.5, alpha=0.6)
        ax.plot([x2, x2], [y1, y2], "r-",  linewidth=1.5, alpha=0.6)

        ax.text((x1 + x2) / 2, y1 - 0.6,
                f"gradient = {self.gradient:.0f} K",
                fontsize=11, color="red", ha="center", va="top",
                bbox=dict(boxstyle="round", facecolor="mistyrose", alpha=0.95))

        ax.text(0.98, 0.97, "ln k = ln A − Ea / RT",
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
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "An alcohol undergoes the chemical test shown in the diagram. "
            "Based on the observations and the molecular formula provided in the image, identify the alcohol.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Hydroxy compounds"
        self.subtopic = "Oxidation of alcohols"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to LaTeX math format
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9'}

        latex_formula = self.alcohol['formula']
        for k, v in subs.items():
            latex_formula = latex_formula.replace(k, v)

        # Determine the oxidizability based on class
        ox_status = "primary or secondary" if self.alcohol['class'] != "tertiary" else "tertiary"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Analyze the test result with acidified } \\mathrm{K_2Cr_2O_7}.\\\\"
            f"&\\quad \\text{{Observation: {self.alcohol['result_heat']}}} \\implies \\text{{Alcohol is {ox_status}.}}\\\\"
            "&\\text{Step 2: Use the oxidation product to determine the alcohol's class.}\\\\"
            f"&\\quad \\text{{Product: {self.alcohol['oxidation_product']}}} \\implies \\text{{Confirmed as a {self.alcohol['class']} alcohol.}}\\\\"
            "&\\text{Step 3: Identify the specific isomer using the molecular formula.}\\\\"
            f"&\\quad \\text{{Formula: }} \\mathrm{{{latex_formula}}} \\implies \\text{{The unique structure matching this is {self.alcohol['name']}.}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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

        ax.text(5.5, 5.8, f"Alcohol Formula: {self.alcohol['formula']}", 
                fontsize=13, ha="center", va="center", fontweight="bold", 
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", edgecolor="black", alpha=0.9))

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

        ax.text(6.9, 1.1, f"Product:\n{self.alcohol['oxidation_product']}", 
                fontsize=10, ha="center", va="top", fontweight="bold", 
                color="darkgreen" if self.alcohol["class"] != "tertiary" else "darkorange",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="black", alpha=0.8))

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
        correct = self.compound["type"]
        options = ["aldehyde", "ketone", "carboxylic acid", "ester"]
        rnd.shuffle(options)
        self.options = options
        self.answer = chr(65 + options.index(correct))
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "An unknown organic compound is subjected to the three chemical tests shown in the diagram. "
            "Based on the visual observations of the test tubes, identify the type of compound.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Carbonyl compounds"
        self.subtopic = "Distinguishing aldehydes and ketones"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"
        self.question_type = "MCQ"

        # Deduction logic based on the compound type
        dnp_obs = "an orange precipitate"
        
        if self.compound["type"] == "aldehyde":
            redox_obs = "a silver mirror (Tollens') and a brick-red precipitate (Fehling's)"
            redox_conclusion = "an aldehyde"
        else:
            redox_obs = "no reaction with Tollens' or Fehling's reagents"
            redox_conclusion = "a ketone"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Analyze the result of the 2,4-DNP test.}\\\\"
            f"&\\quad \\text{{Observation: {dnp_obs}}} \\implies \\text{{The compound contains a carbonyl group (C=O).}}\\\\"
            "&\\text{Step 2: Use the Tollens' and Fehling's tests to distinguish between an aldehyde and a ketone.}\\\\"
            f"&\\quad \\text{{Observation: {redox_obs}}} \\implies \\text{{The compound is {redox_conclusion}.}}\\\\"
            "&\\text{Step 3: Combine the observations to select the correct classification.}\\\\"
            f"&\\quad \\text{{Since it is a {self.compound['type']}, it matches option }} \\text{{{self.answer}}}.\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 6.5, 7.5, "Chemical Analysis of Unknown Carbonyl Compound", fontsize=14)

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
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The diagram illustrates the curly arrow mechanism for an electrophilic addition reaction. "
            "Based on the chemical species and the movement of electrons shown in the image, "
            "identify the electrophile that initiates the reaction.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Electrophilic addition mechanisms"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts and special characters to LaTeX math format
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9',
                '\u207a':'^+', '\u207b':'^-', ' ': '\\ '}
        
        latex_electrophile = self.rxn['electrophile']
        for k, v in subs.items():
            latex_electrophile = latex_electrophile.replace(k, v)
        
        latex_intermediate = self.rxn['intermediate']
        for k, v in subs.items():
            latex_intermediate = latex_intermediate.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Identify the reactants and the nature of the reaction.}\\\\"
            f"&\\quad \\text{{Reactants: {self.rxn['alkene']} and {self.rxn['reagent']}}}. \\text{{ This is an electrophilic addition reaction.}}\\\\"
            "&\\text{Step 2: Analyze the electron flow in the first step of the mechanism (curly arrow 1).}\\\\"
            "&\\quad \\text{The arrow shows the electron pair from the alkene } \\pi \\text{ bond being donated to an electron-deficient species.}\\\\"
            "&\\text{Step 3: Identify the electrophile that accepts these electrons.}\\\\"
            f"&\\quad \\text{{The initiating species is the electrophile: }} \\mathrm{{{latex_electrophile}}}.\\\\"
            "&\\text{Step 4: Confirm the formation of the carbocation intermediate before the final product.}\\\\"
            f"&\\quad \\text{{Intermediate stage: }} \\mathrm{{{latex_intermediate}}}.\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis("off")

        add_title_box(ax, 7, 7.5, "Reaction Mechanism Analysis", fontsize=14)

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
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "An unknown halide is subjected to the silver nitrate and ammonia tests shown in the diagram. "
            "Identify the halide ion present by comparing the test tube observations with the reference data provided.\n\n"
            f"{self.options_text}"
        )
        self.topic = "Group 17 (Halogens)"
        self.subtopic = "Halide ion tests"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"
        self.question_type = "MCQ"

        # Convert Unicode to LaTeX for the reasoning block
        subs = {'\u207b': '^-', '\u2083': '_3'}
        latex_ion = self.halide['ion']
        for k, v in subs.items():
            latex_ion = latex_ion.replace(k, v)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{Step 1: Observe the color of the precipitate formed with } \\mathrm{AgNO_3}.\\\\"
            f"&\\quad \\text{{Observation: {self.halide['agno3_ppt']}}}.\\\\"
            "&\\text{Step 2: Test the solubility of the precipitate in dilute ammonia } (\\mathrm{NH_3}).\\\\"
            f"&\\quad \\text{{Result: {self.halide['dil_nh3']}}}.\\\\"
            "&\\text{Step 3: Test the solubility in concentrated ammonia } (\\mathrm{NH_3}).\\\\"
            f"&\\quad \\text{{Result: {self.halide['conc_nh3']}}}.\\\\"
            "&\\text{Step 4: Use the reference table to match the solubility pattern to the halide ion.}\\\\"
            f"&\\quad \\text{{The unique pattern of results confirms the ion is }} \\mathrm{{{latex_ion}}} \\text{{ ({self.halide['name']}).}}\\\\"
            f"&\\quad \\text{{Final Answer}} = \\text{{{self.answer}}}"
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
        self.options_text = "\n".join(f"{chr(65+j)}. {opt}" for j, opt in enumerate(self.options))

        self.description = (
            "The graph displays the relationship between $pV$ and $p$ for a real gas compared to an ideal gas. "
            "Based on the behavior shown in the highlighted region of the diagram, "
            "which statement best explains the observed deviation from ideal behavior?\n\n"
            f"{self.options_text}"
        )
        self.topic = "States of matter"
        self.subtopic = "Ideal and real gas behaviour"
        self.source = "Adapted from Cambridge AS Level Chemistry 9701"
        self.curriculum = "AS Level"
        self.question_type = "MCQ"

        # Convert Unicode subscripts to LaTeX math format for the gas name
        subs = {'\u2080':'_0', '\u2081':'_1', '\u2082':'_2', '\u2083':'_3', '\u2084':'_4', 
                '\u2085':'_5', '\u2086':'_6', '\u2087':'_7', '\u2088':'_8', '\u2089':'_9'}
        
        latex_gas_name = self.gas['name']
        for k, v in subs.items():
            latex_gas_name = latex_gas_name.replace(k, v)

        self.reasoning = (
            r"\[\begin{aligned}"
            r"&\text{Step 1: Identify the graph components and the highlighted region in the image.}\\"
            fr"&\quad \text{{The }} pV \text{{ vs }} p \text{{ plot shows the curve for }} \mathrm{{{latex_gas_name}}} \text{{ rising above the ideal baseline at high pressure.}}\\"
            r"&\text{Step 2: Analyze the mathematical deviation observed in that region.}\\"
            r"&\quad \text{Because the curve is above the horizontal baseline, } pV > nRT \text{ for this real gas.}\\"
            r"&\text{Step 3: Find the solution by determining the physical cause of the deviation.}\\"
            r"&\quad \text{At high pressures, the actual volume of the gas molecules is no longer negligible.}\\"
            r"&\quad \text{This 'fixed' molecular volume increases the total } V, \text{ causing } pV \text{ to be higher than the ideal prediction.}\\"
            fr"&\quad \text{{Final Answer}} = \text{{{self.answer}}}"
            r"\end{aligned}\]"
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

        # Make the title more generic so they have to read the legend
        ax.set_title("Gas Behavior Analysis: Real vs. Ideal", fontsize=14, fontweight="bold")

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
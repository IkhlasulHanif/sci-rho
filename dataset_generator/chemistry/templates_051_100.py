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
    Visual: Bar chart showing reactivity trend down Group 2
    Task: Identify element from reactivity data
    """
    
    def __init__(self):
        elements = ["Mg", "Ca", "Sr", "Ba"]
        reactivity_values = [3, 5, 7, 9]
        
        idx = rnd.randint(0, 3)
        self.element = elements[idx]
        self.reactivity = reactivity_values[idx]
        
        self.elements = elements
        self.values = reactivity_values
        
        self.answer = self.element
        
        self.description = (
            f"The bar chart shows the relative reactivity of Group 2 elements with water. "
            f"Which element has a reactivity value of {self.reactivity}?"
        )
        
        self.topic = "Group 2"
        self.subtopic = "Trends in Group 2"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the bar chart:}} &\\\\"
            f"\\text{{Element with reactivity {self.reactivity} is {self.element}}} &\\\\"
            f"\\text{{Reactivity increases down Group 2.}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        x_positions = list(range(len(self.elements)))
        
        draw_bar_chart(ax, x_positions, self.values, self.elements,
                      colors='skyblue', width=0.6,
                      xlabel='Element', ylabel='Reactivity',
                      title='Reactivity of Group 2 Elements')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem052:
    """
    Topic: 28.1 General properties of transition elements
    """
    
    def __init__(self):
        comparisons = [
            {
                'element1': 'Cu',
                'element2': 'Zn',
                'config1': '[Ar] 3d¹⁰ 4s¹',
                'config2': '[Ar] 3d¹⁰ 4s²',
                'ion1': 'Cu²⁺: [Ar] 3d⁹',
                'ion2': 'Zn²⁺: [Ar] 3d¹⁰',
                'transition1': 'Yes',
                'transition2': 'No',
                'reason1': 'forms stable ion with incomplete d-orbital',
                'reason2': 'forms ion with complete d-orbital'
            },
            {
                'element1': 'Sc',
                'element2': 'Ti',
                'config1': '[Ar] 3d¹ 4s²',
                'config2': '[Ar] 3d² 4s²',
                'ion1': 'Sc³⁺: [Ar] 3d⁰',
                'ion2': 'Ti³⁺: [Ar] 3d¹',
                'transition1': 'No',
                'transition2': 'Yes',
                'reason1': 'forms ion with empty d-orbital',
                'reason2': 'forms stable ion with incomplete d-orbital'
            }
        ]
        
        self.comp = rnd.choice(comparisons)
        self.answer = (f"{self.comp['element1']}: {self.comp['transition1']}, "
                      f"{self.comp['element2']}: {self.comp['transition2']}")
        
        self.description = (
            f"The electron configurations of {self.comp['element1']} and {self.comp['element2']} are shown below. "
            f"Using the definition 'a transition element forms one or more stable ions with incomplete d orbitals', "
            f"determine which element(s) is/are transition element(s)."
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.1 General physical and chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.comp['element1']} atom:}} &\\quad {self.comp['config1']}\\\\"
            f"\\text{{{self.comp['ion1']}}} &\\quad \\text{{incomplete d-orbital: {self.comp['transition1']}}}\\\\"
            f"\\text{{{self.comp['element2']} atom:}} &\\quad {self.comp['config2']}\\\\"
            f"\\text{{{self.comp['ion2']}}} &\\quad \\text{{complete d-orbital: {self.comp['transition2']}}}\\\\"
            f"\\text{{Transition element definition:}}&\\\\"
            f"\\text{{Forms stable ion(s) with incomplete d orbitals}}&"
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
        
        ax.text(6, 1, "Which element(s) is/are transition element(s)?", 
               fontsize=13, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem053:
    """
    Topic: 28.1 General properties of transition elements
    Visual: Diagram showing variable oxidation states of transition metal
    Task: Identify possible oxidation states from colored compounds
    """
    
    def __init__(self):
        metals = {
            "Fe": [("+2", "pale green"), ("+3", "yellow-brown")],
            "Cu": [("+1", "white"), ("+2", "blue")],
            "Mn": [("+2", "pale pink"), ("+4", "brown"), ("+7", "purple")],
            "Cr": [("+3", "green"), ("+6", "orange")]
        }
        
        self.metal = rnd.choice(list(metals.keys()))
        self.oxidation_states = metals[self.metal]
        
        selected_state = rnd.choice(self.oxidation_states)
        self.answer = selected_state[0]
        self.color = selected_state[1]
        
        self.description = (
            f"The diagram shows different oxidation states of {self.metal}. "
            f"What is the oxidation state of {self.metal} in the {self.color} compound?"
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "General properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The {self.color} compound contains {self.metal} in oxidation state {self.answer}}} &"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        color_map = {
            "pale green": "lightgreen",
            "yellow-brown": "goldenrod",
            "white": "whitesmoke",
            "blue": "lightblue",
            "pale pink": "lightpink",
            "brown": "saddlebrown",
            "purple": "mediumpurple",
            "green": "limegreen",
            "orange": "orange"
        }
        
        x_start = 2
        spacing = 3
        
        for i, (ox_state, color) in enumerate(self.oxidation_states):
            x = x_start + i * spacing
            
            draw_test_tube(ax, x, 1, width=1, height=3.5, solution_height=2.5,
                          solution_color=color_map.get(color, 'lightgray'))
            
            add_formula_label(ax, x + 0.5, 0.3, f"{self.metal}{ox_state}", 
                            fontsize=12, weight='bold')
            add_formula_label(ax, x + 0.5, 4.7, color, fontsize=10)
        
        add_title_box(ax, 6, 5.5, f"Oxidation States of {self.metal}", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem054:
    """
    Topic: 28.2 Ligands and complex formation
    Visual: Diagram of octahedral complex
    Task: Determine coordination number from structure
    """
    
    def __init__(self):
        complexes = [
            ("[Cu(H₂O)₆]²⁺", 6, "octahedral"),
            ("[Fe(CN)₆]³⁻", 6, "octahedral"),
            ("[Co(NH₃)₆]³⁺", 6, "octahedral"),
            ("[Ni(H₂O)₆]²⁺", 6, "octahedral")
        ]
        
        self.complex = rnd.choice(complexes)
        self.formula = self.complex[0]
        self.coordination_number = self.complex[1]
        self.shape = self.complex[2]
        
        self.answer = self.coordination_number
        
        self.description = (
            f"The diagram shows the structure of {self.formula}. "
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
        
        positions = [
            (0.8, 0), (-0.8, 0),
            (0, 0.8), (0, -0.8),
            (0.6, 0.6), (-0.6, -0.6)
        ]
        
        for i, (x, y) in enumerate(positions):
            draw_bond(ax, 0, 0, x, y, bond_type='dashed', linewidth=2)
            draw_circle_atom(ax, x, y, "L", radius=0.2, color='lightblue',
                           fontsize=12)
        
        add_title_box(ax, 0, 1.8, self.formula, fontsize=18)
        add_formula_label(ax, 0, -1.8, f"Shape: {self.shape}", fontsize=14)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem055:
    """
    Topic: 28.2 Ligands and complex formation
    """
    
    def __init__(self):
        complexes = [
            {
                'metal': 'Cu²⁺',
                'initial_complex': '[Cu(H₂O)₆]²⁺',
                'initial_color': 'pale blue',
                'initial_color_hex': '#ADD8E6',
                'final_complex': '[Cu(NH₃)₄(H₂O)₂]²⁺',
                'final_color': 'deep blue',
                'final_color_hex': '#00008B',
                'ligand': 'NH₃(aq)',
                'ligand_name': 'ammonia'
            },
            {
                'metal': 'Cu²⁺',
                'initial_complex': '[Cu(H₂O)₆]²⁺',
                'initial_color': 'pale blue',
                'initial_color_hex': '#ADD8E6',
                'final_complex': '[CuCl₄]²⁻',
                'final_color': 'yellow-green',
                'final_color_hex': '#9ACD32',
                'ligand': 'Cl⁻(aq)',
                'ligand_name': 'chloride ions'
            },
            {
                'metal': 'Co²⁺',
                'initial_complex': '[Co(H₂O)₆]²⁺',
                'initial_color': 'pink',
                'initial_color_hex': '#FFC0CB',
                'final_complex': '[CoCl₄]²⁻',
                'final_color': 'blue',
                'final_color_hex': '#0000FF',
                'ligand': 'Cl⁻(aq)',
                'ligand_name': 'chloride ions'
            }
        ]
        
        self.reaction = rnd.choice(complexes)
        self.answer = f"{self.reaction['final_complex']}, {self.reaction['final_color']}"
        
        self.description = (
            f"When excess {self.reaction['ligand_name']} is added to {self.reaction['initial_complex']}, "
            f"a ligand exchange reaction occurs. The initial {self.reaction['initial_color']} solution "
            f"changes color. What is the formula of the final complex and its color?"
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.2 Characteristic chemical properties"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Ligand exchange reaction:}} &\\\\"
            f"{self.reaction['initial_complex']} + \\text{{excess {self.reaction['ligand']}}} "
            f"&\\rightarrow {self.reaction['final_complex']}\\\\"
            f"\\text{{Color change: {self.reaction['initial_color']}}} "
            f"&\\rightarrow \\text{{{self.reaction['final_color']}}}\\\\"
            f"\\text{{The ligand exchange occurs because}}&\\\\"
            f"\\text{{the new ligand forms a more stable complex}}&"
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
        add_formula_label(ax, 2.25, 0.8, self.reaction['initial_complex'], fontsize=13)
        add_formula_label(ax, 2.25, 0.3, self.reaction['initial_color'], fontsize=11, color='blue')
        
        draw_arrow(ax, 3.5, 3.5, 5.5, 3.5, label=f"+ excess {self.reaction['ligand']}", 
                  label_position='above', color='black', linewidth=3)
        
        draw_test_tube(ax, 9, 1.5, width=1.5, height=3.5, solution_height=2.5,
                      solution_color=self.reaction['final_color_hex'])
        add_formula_label(ax, 9.75, 0.8, self.reaction['final_complex'], fontsize=13)
        add_formula_label(ax, 9.75, 0.3, self.reaction['final_color'], fontsize=11, color='blue')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem056:
    """
    Topic: 28.3 Ligand substitution reactions
    Visual: Equation showing ligand exchange
    Task: Predict color change in ligand substitution
    """
    
    def __init__(self):
        reactions = [
            ("[Cu(H₂O)₆]²⁺", "blue", "[Cu(NH₃)₄(H₂O)₂]²⁺", "deep blue"),
            ("[Fe(H₂O)₆]³⁺", "yellow", "[Fe(SCN)(H₂O)₅]²⁺", "blood red"),
            ("[Co(H₂O)₆]²⁺", "pink", "[CoCl₄]²⁻", "blue"),
            ("[Ni(H₂O)₆]²⁺", "green", "[Ni(NH₃)₆]²⁺", "purple")
        ]
        
        self.reaction = rnd.choice(reactions)
        self.reactant = self.reaction[0]
        self.color1 = self.reaction[1]
        self.product = self.reaction[2]
        self.color2 = self.reaction[3]
        
        self.answer = self.color2
        
        self.description = (
            f"When excess ligand is added to {self.reactant} ({self.color1}), "
            f"what color will the resulting solution be?"
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Ligand substitution"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Ligand substitution occurs:}} &\\\\"
            f"\\text{{{self.reactant}}} &\\rightarrow \\text{{{self.product}}}\\\\"
            f"\\text{{Color change: {self.color1} to {self.color2}}}"
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
            "pink": "lightpink", "green": "lightgreen",
            "purple": "mediumpurple"
        }
        
        draw_test_tube(ax, 2, 1, width=1.2, height=3.5, solution_height=2.5,
                      solution_color=color_map.get(self.color1, 'lightgray'))
        add_formula_label(ax, 2.6, 0.3, self.reactant, fontsize=11)
        add_formula_label(ax, 2.6, 4.8, self.color1, fontsize=10)
        
        draw_arrow(ax, 4, 3, 8, 3, label="+ ligand", label_position='above',
                  color='black', linewidth=2.5)
        
        draw_test_tube(ax, 9, 1, width=1.2, height=3.5, solution_height=2.5,
                      solution_color=color_map.get(self.color2, 'lightgray'))
        add_formula_label(ax, 9.6, 0.3, self.product, fontsize=11)
        add_formula_label(ax, 9.6, 4.8, self.color2, fontsize=10)
        
        add_title_box(ax, 6, 5.5, "Ligand Substitution", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem057:
    """
    Topic: 28.3 Ligand substitution reactions
    """
    
    def __init__(self):
        data_sets = [
            {'delta_E': 170, 'wavelength': 704, 'color_absorbed': 'red', 'color_observed': 'green'},
            {'delta_E': 200, 'wavelength': 598, 'color_absorbed': 'orange', 'color_observed': 'blue'},
            {'delta_E': 250, 'wavelength': 478, 'color_absorbed': 'blue-green', 'color_observed': 'red-orange'},
            {'delta_E': 280, 'wavelength': 427, 'color_absorbed': 'violet', 'color_observed': 'yellow'},
        ]
        
        self.data = rnd.choice(data_sets)
        self.delta_E = self.data['delta_E']
        self.wavelength = self.data['wavelength']
        
        self.answer = f"{self.wavelength} nm"
        
        self.description = (
            f"A transition metal complex has a d-orbital splitting energy (ΔE) of {self.delta_E} kJ/mol. "
            f"Calculate the wavelength of light absorbed by this complex. "
            f"(Given: h = 6.626×10⁻³⁴ J·s, c = 3.00×10⁸ m/s, Nₐ = 6.022×10²³ mol⁻¹)"
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
            f"&= {self.wavelength}\\text{{ nm}}\\\\"
            f"\\text{{Color absorbed: {self.data['color_absorbed']}}}&\\\\"
            f"\\text{{Color observed: {self.data['color_observed']}}}&"
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
        for i, label in enumerate(['dz²', 'dx²-y²']):
            line_x = 3 + i * 1.2
            ax.plot([line_x, line_x + 0.6], [y_higher, y_higher], 'r-', linewidth=3)
            ax.text(line_x + 0.3, y_higher + 0.3, label, fontsize=10, ha='center')
        
        draw_vertical_annotation(ax, 6.5, y_lower, y_higher, f"ΔE = {self.delta_E} kJ/mol",
                                color='purple', linewidth=2.5, fontsize=12)
        
        ax.text(0.5, 3.5, 'Energy', fontsize=14, fontweight='bold', rotation=90, ha='center')
        
        calc_text = f"λ = hc×Nₐ/ΔE\nλ = ? nm"
        ax.text(5, 1, calc_text, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem058:
    """
    Topic: 28.5 Redox reactions and catalysis
    Visual: Catalytic cycle diagram
    Task: Identify oxidation state changes in catalysis
    """
    
    def __init__(self):
        catalysts = [
            ("Fe²⁺", "+2", "Fe³⁺", "+3"),
            ("V³⁺", "+3", "V⁴⁺", "+4"),
            ("Cu⁺", "+1", "Cu²⁺", "+2"),
            ("Mn²⁺", "+2", "Mn³⁺", "+3")
        ]
        
        self.catalyst = rnd.choice(catalysts)
        self.species1 = self.catalyst[0]
        self.ox1 = self.catalyst[1]
        self.species2 = self.catalyst[2]
        self.ox2 = self.catalyst[3]
        
        self.answer = f"{self.ox1} to {self.ox2}"
        
        self.description = (
            f"The diagram shows a catalytic cycle involving {self.species1}. "
            f"What are the oxidation state changes during the cycle?"
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "Redox and catalysis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Oxidation:}} &\\quad {self.species1} \\rightarrow {self.species2}\\\\"
            f"\\text{{Reduction:}} &\\quad {self.species2} \\rightarrow {self.species1}\\\\"
            f"\\text{{Oxidation states change: {self.ox1} ⇌ {self.ox2}}}"
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
        
        add_formula_label(ax, 2.5, 3.5, f"Ox. state: {self.ox1}", fontsize=12)
        add_formula_label(ax, 7.5, 3.5, f"Ox. state: {self.ox2}", fontsize=12)
        
        add_title_box(ax, 5, 7.5, "Catalytic Cycle", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem059:
    """
    Topic: 28.5 Redox reactions and catalysis
    """

    def __init__(self):
        ligand_exchanges = [
            {
                'initial': '[Cu(H₂O)₆]²⁺',
                'final': '[Cu(NH₃)₄(H₂O)₂]²⁺',
                'ligand': 'NH₃',
                'Kstab_initial': '1.0×10¹',
                'Kstab_final': '1.2×10¹³',
                'feasible': 'yes',
                'reason': 'Kstab_final >> Kstab_initial'
            },
            {
                'initial': '[Cu(NH₃)₄(H₂O)₂]²⁺',
                'final': '[Cu(EDTA)]²⁻',
                'ligand': 'EDTA⁴⁻',
                'Kstab_initial': '1.2×10¹³',
                'Kstab_final': '6.3×10¹⁸',
                'feasible': 'yes',
                'reason': 'EDTA forms very stable chelate complex'
            }
        ]
        
        self.exchange = rnd.choice(ligand_exchanges)
        self.answer = f"{self.exchange['feasible']} - {self.exchange['final']}"
        
        self.description = (
            f"Given the stability constants:\n"
            f"{self.exchange['initial']}: Kstab = {self.exchange['Kstab_initial']}\n"
            f"{self.exchange['final']}: Kstab = {self.exchange['Kstab_final']}\n\n"
            f"Is the ligand exchange from {self.exchange['initial']} to "
            f"{self.exchange['final']} feasible? Explain using Kstab values."
        )
        
        self.topic = "Chemistry of transition elements"
        self.subtopic = "28.5 Stability constants"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"K_{{stab}}\\text{{(initial)}} &= {self.exchange['Kstab_initial']}\\\\"
            f"K_{{stab}}\\text{{(final)}} &= {self.exchange['Kstab_final']}\\\\"
            f"\\text{{Since }} K_{{stab}}\\text{{(final)}} &>> K_{{stab}}\\text{{(initial)}}\\\\"
            f"\\text{{The ligand exchange is feasible}}&\\\\"
            f"\\text{{Final complex: {self.exchange['final']}}}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 6, 6.5, "Ligand Exchange Feasibility", fontsize=16)
        
        draw_labeled_box(ax, 1, 3.5, 3.5, 1.2, self.exchange['initial'],
                        f"Kstab = {self.exchange['Kstab_initial']}", 
                        facecolor='lightblue')
        
        draw_arrow(ax, 4.8, 4.1, 7, 4.1, label=f"+ {self.exchange['ligand']}", 
                  label_position='above', color='black', linewidth=3)
        
        draw_labeled_box(ax, 7.5, 3.5, 3.5, 1.2, self.exchange['final'],
                        f"Kstab = {self.exchange['Kstab_final']}", 
                        facecolor='lightgreen')
        
        question = "Is this ligand exchange feasible?"
        ax.text(6, 1.5, question, fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem060:
    """
    Topic: 29.1 Hydrocarbons nomenclature
    Visual: Structural formula of alkane
    Task: Name the compound using IUPAC nomenclature
    """
    
    def __init__(self):
        structures = [
            ("2-methylpropane", "CH₃-CH(CH₃)-CH₃"),
            ("2-methylbutane", "CH₃-CH(CH₃)-CH₂-CH₃"),
            ("2,2-dimethylpropane", "C(CH₃)₄"),
            ("3-methylpentane", "CH₃-CH₂-CH(CH₃)-CH₂-CH₃")
        ]
        
        self.compound = rnd.choice(structures)
        self.name = self.compound[0]
        self.formula = self.compound[1]
        
        self.answer = self.name
        
        self.description = (
            f"Name the alkane shown in the structural formula using IUPAC nomenclature."
        )
        
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
        
        add_formula_label(ax, 5, 3, self.formula, fontsize=20, weight='bold',
                         bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=1))
        
        add_formula_label(ax, 5, 1, "Name this compound", fontsize=14)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem061:
    """
    Topic: 29.4 Isomerism
    Visual: Structural isomers
    Task: Identify number of structural isomers
    """
    
    def __init__(self):
        formulas = [
            ("C₄H₁₀", 2, ["butane", "2-methylpropane"]),
            ("C₅H₁₂", 3, ["pentane", "2-methylbutane", "2,2-dimethylpropane"]),
            ("C₄H₈", 3, ["but-1-ene", "but-2-ene", "2-methylpropene"])
        ]
        
        self.compound = rnd.choice(formulas)
        self.formula = self.compound[0]
        self.num_isomers = self.compound[1]
        self.isomer_names = self.compound[2]
        
        self.answer = self.num_isomers
        
        self.description = (
            f"How many structural isomers are there with the molecular formula {self.formula}?"
        )
        
        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The structural isomers of {self.formula} are:}} &\\\\"
            + "\\\\".join([f"\\text{{{i+1}. {name}}}" for i, name in enumerate(self.isomer_names)]) + "\\\\"
            + f"\\text{{Total number of isomers}} &= {self.answer}"
            + "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7.5, f"Structural Isomers of {self.formula}", fontsize=16)
        
        y_pos = 6
        for i, name in enumerate(self.isomer_names):
            add_formula_label(ax, 5, y_pos, f"{i+1}. {name}", fontsize=14,
                            bbox_style=dict(boxstyle='round', facecolor='lightblue', pad=0.5))
            y_pos -= 1.5
        
        add_formula_label(ax, 5, 1, f"Total: {self.num_isomers} isomers", 
                         fontsize=16, weight='bold', color='red')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem062:
    """
    Topic: 29.4 Geometric isomerism
    Visual: E/Z isomers
    Task: Identify E or Z isomer
    """
    
    def __init__(self):
        compounds = [
            ("but-2-ene", "E-but-2-ene", "Z-but-2-ene"),
            ("pent-2-ene", "E-pent-2-ene", "Z-pent-2-ene"),
            ("1,2-dichloroethene", "E-1,2-dichloroethene", "Z-1,2-dichloroethene")
        ]
        
        self.compound = rnd.choice(compounds)
        self.base_name = self.compound[0]
        self.E_isomer = self.compound[1]
        self.Z_isomer = self.compound[2]
        
        self.shown_isomer = rnd.choice([self.E_isomer, self.Z_isomer])
        self.answer = "E" if self.shown_isomer == self.E_isomer else "Z"
        
        self.description = (
            f"Identify whether the isomer shown is the E or Z isomer of {self.base_name}."
        )
        
        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "Geometric isomerism"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The isomer shown is the {self.answer}-isomer}} &\\\\"
            f"\\text{{{self.answer}: higher priority groups on opposite sides}} &"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7.5, self.shown_isomer, fontsize=18)
        
        if self.answer == "E":
            ax.plot([3, 7], [4, 4], 'k-', linewidth=3)
            ax.plot([3, 7], [3.8, 4.2], 'k-', linewidth=3)
            
            add_formula_label(ax, 2, 4.5, "R₁", fontsize=16, weight='bold')
            add_formula_label(ax, 8, 3.5, "R₂", fontsize=16, weight='bold')
            add_formula_label(ax, 2, 3.5, "R₃", fontsize=16, weight='bold')
            add_formula_label(ax, 8, 4.5, "R₄", fontsize=16, weight='bold')
        else:
            ax.plot([3, 7], [4, 4], 'k-', linewidth=3)
            ax.plot([3, 7], [3.8, 4.2], 'k-', linewidth=3)
            
            add_formula_label(ax, 2, 4.5, "R₁", fontsize=16, weight='bold')
            add_formula_label(ax, 8, 4.5, "R₂", fontsize=16, weight='bold')
            add_formula_label(ax, 2, 3.5, "R₃", fontsize=16, weight='bold')
            add_formula_label(ax, 8, 3.5, "R₄", fontsize=16, weight='bold')
        
        add_formula_label(ax, 5, 1.5, "E or Z isomer?", fontsize=14)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem063:
    """
    Topic: 29.4 Geometric isomerism
    """
    
    def __init__(self):
        molecules = [
            {
                'name': 'butan-2-ol',
                'formula': 'CH₃CH(OH)CH₂CH₃',
                'chiral_carbon': 'C2',
                'groups': ['CH₃', 'OH', 'H', 'CH₂CH₃']
            },
            {
                'name': '2-aminopropanoic acid',
                'formula': 'CH₃CH(NH₂)COOH',
                'chiral_carbon': 'C2',
                'groups': ['CH₃', 'NH₂', 'H', 'COOH']
            },
            {
                'name': '2-bromobutane',
                'formula': 'CH₃CHBrCH₂CH₃',
                'chiral_carbon': 'C2',
                'groups': ['CH₃', 'Br', 'H', 'CH₂CH₃']
            }
        ]
        
        self.molecule = rnd.choice(molecules)
        self.rotation = rnd.choice(['+', '-'])
        self.rotation_value = rnd.randint(5, 25)
        
        self.answer = f"{self.molecule['chiral_carbon']} (carbon 2)"
        
        self.description = (
            f"The molecule {self.molecule['name']} ({self.molecule['formula']}) is optically active. "
            f"One enantiomer rotates plane-polarized light by {self.rotation}{self.rotation_value}°. "
            f"Identify the chiral center in this molecule."
        )
        
        self.topic = "Introduction to A Level organic chemistry"
        self.subtopic = "29.4 Isomerism: optical"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: {self.molecule['name']}}}&\\\\"
            f"\\text{{Chiral center: carbon bonded to 4 different groups}}&\\\\"
            f"\\text{{Groups: {', '.join(self.molecule['groups'])}}}&\\\\"
            f"\\text{{Chiral carbon position: {self.molecule['chiral_carbon']}}}&\\\\"
            f"\\text{{Optical rotation: {self.rotation}{self.rotation_value}°}}&\\\\"
            "\\text{Two enantiomers exist (mirror images)}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, f"Optical Isomerism: {self.molecule['name']}", fontsize=16)
        
        center_x, center_y = 3, 4
        
        draw_circle_atom(ax, center_x, center_y, 'C*', radius=0.4, 
                        color='yellow', text_color='black', fontsize=16)
        
        group_positions = [
            (center_x, center_y + 1.5, 'top'),    
            (center_x + 1.5, center_y, 'right'),
            (center_x, center_y - 1.5, 'bottom'),
            (center_x - 1.5, center_y, 'left')
        ]
        
        for i, (gx, gy, pos) in enumerate(group_positions):
            draw_bond(ax, center_x, center_y, gx, gy, linewidth=2.5)
            
            group_text = self.molecule['groups'][i]
            ax.text(gx, gy, group_text, fontsize=13, ha='center', va='center',
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
        
        center_x2 = 9
        draw_circle_atom(ax, center_x2, center_y, 'C*', radius=0.4, 
                        color='yellow', text_color='black', fontsize=16)
        
        group_positions2 = [
            (center_x2, center_y + 1.5, 'top'),
            (center_x2 - 1.5, center_y, 'left'),
            (center_x2, center_y - 1.5, 'bottom'),
            (center_x2 + 1.5, center_y, 'right')
        ]
        
        groups_mirrored = [self.molecule['groups'][0], self.molecule['groups'][3],
                          self.molecule['groups'][2], self.molecule['groups'][1]]
        
        for i, (gx, gy, pos) in enumerate(group_positions2):
            draw_bond(ax, center_x2, center_y, gx, gy, linewidth=2.5)
            group_text = groups_mirrored[i]
            ax.text(gx, gy, group_text, fontsize=13, ha='center', va='center',
                   fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
        
        ax.plot([6, 6], [2, 6], 'k--', linewidth=2)
        ax.text(6, 6.5, 'mirror', fontsize=11, ha='center', style='italic')
        
        ax.text(3, 1.5, f"Rotation: {self.rotation}{self.rotation_value}°", 
               fontsize=12, ha='center', fontweight='bold')
        ax.text(9, 1.5, f"Rotation: {'-' if self.rotation == '+' else '+'}{self.rotation_value}°", 
               fontsize=12, ha='center', fontweight='bold')
        
        ax.text(6, 0.5, "*Chiral center (carbon bonded to 4 different groups)", 
               fontsize=11, ha='center', style='italic', color='red')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem064:
    """
    Topic: 30.1 Alkanes reactions
    """
    
    def __init__(self):
        reactions = [
            {
                'reaction_name': 'Nitration',
                'electrophile': 'NO₂⁺',
                'reagents': 'conc. HNO₃ + conc. H₂SO₄',
                'temperature': '50-60°C',
                'product': 'nitrobenzene',
                'product_formula': 'C₆H₅NO₂'
            },
            {
                'reaction_name': 'Bromination',
                'electrophile': 'Br⁺',
                'reagents': 'Br₂ + AlBr₃ catalyst',
                'temperature': 'room temp',
                'product': 'bromobenzene',
                'product_formula': 'C₆H₅Br'
            },
            {
                'reaction_name': 'Chlorination',
                'electrophile': 'Cl⁺',
                'reagents': 'Cl₂ + AlCl₃ catalyst',
                'temperature': 'room temp',
                'product': 'chlorobenzene',
                'product_formula': 'C₆H₅Cl'
            }
        ]
        
        self.reaction = rnd.choice(reactions)
        self.answer = f"{self.reaction['electrophile']} (electrophile)"
        
        self.description = (
            f"Benzene undergoes {self.reaction['reaction_name'].lower()} with {self.reaction['reagents']} "
            f"at {self.reaction['temperature']} to form {self.reaction['product']}. "
            f"The mechanism proceeds via electrophilic substitution. "
            f"What is the electrophile in this reaction and draw the mechanism showing "
            f"the carbocation intermediate."
        )
        
        self.topic = "Hydrocarbons"
        self.subtopic = "30.1 Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.reaction['reaction_name']}}}&\\\\"
            f"\\text{{Electrophile: {self.reaction['electrophile']}}}&\\\\"
            "\\text{Mechanism:}&\\\\"
            "\\text{1. Electrophile attacks benzene ring}&\\\\"
            "\\text{2. Carbocation intermediate forms}&\\\\"
            "\\text{3. H⁺ is eliminated to restore aromaticity}&\\\\"
            f"\\text{{Product: {self.reaction['product']}}}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 7, 7.5, f"Benzene {self.reaction['reaction_name']} Mechanism", fontsize=16)
        
        x1, y1 = 2, 4
        hexagon1 = patches.RegularPolygon((x1, y1), 6, radius=0.8, 
                                         facecolor='none', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon1)
        circle1 = Circle((x1, y1), 0.5, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle1)
        ax.text(x1, y1 - 1.5, 'Benzene', fontsize=12, ha='center', fontweight='bold')
        
        draw_arrow(ax, 3.5, 4, 5.5, 4, label=f"+ {self.reaction['electrophile']}", 
                  label_position='above', color='black', linewidth=2.5)
        
        x2, y2 = 7, 4
        hexagon2 = patches.RegularPolygon((x2, y2), 6, radius=0.8,
                                         facecolor='lightyellow', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon2)
        add_charge_label(ax, x2 + 0.9, y2 + 0.5, '+', fontsize=16, color='red')
        ax.text(x2, y2 + 1.2, self.reaction['electrophile'].replace('⁺', ''), 
               fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightcoral', pad=0.3))
        ax.text(x2, y2 - 1.5, 'Carbocation\nintermediate', fontsize=11, ha='center', style='italic')
        
        draw_arrow(ax, 8.5, 4, 10.5, 4, label="- H⁺", 
                  label_position='above', color='black', linewidth=2.5)
        
        x3, y3 = 12, 4
        hexagon3 = patches.RegularPolygon((x3, y3), 6, radius=0.8,
                                         facecolor='none', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon3)
        circle3 = Circle((x3, y3), 0.5, fill=False, edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle3)
        ax.text(x3, y3 + 1.2, self.reaction['electrophile'].replace('⁺', ''), 
               fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', pad=0.3))
        ax.text(x3, y3 - 1.5, self.reaction['product'], fontsize=12, ha='center', fontweight='bold')
        
        conditions = f"Reagents: {self.reaction['reagents']}\nTemp: {self.reaction['temperature']}"
        ax.text(7, 1, conditions, fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem065:
    """
    Topic: 30.1 Alkanes reactions
    Visual: Free radical substitution mechanism
    Task: Complete the mechanism equation
    """
    
    def __init__(self):
        self.radical = rnd.choice(["Cl•", "Br•"])
        self.product = "CH₃Cl" if self.radical == "Cl•" else "CH₃Br"
        
        self.answer = self.product
        
        self.description = (
            f"The diagram shows the propagation step of free radical substitution. "
            f"What is the product formed when CH₄ reacts with {self.radical}?"
        )
        
        self.topic = "Hydrocarbons"
        self.subtopic = "Alkane reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Propagation step:}} &\\\\"
            f"\\text{{CH}}_4 + {self.radical} &\\rightarrow {self.product} + \\text{{H}}\\bullet\\\\"
            f"\\text{{Product: {self.product}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_formula_label(ax, 2, 3, "CH₄", fontsize=20, weight='bold')
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
    Topic: 30.1 Hydrocarbons - Arenes
    """
    
    def __init__(self):
        substituents = [
            {
                'compound': 'methylbenzene',
                'substituent': 'CH₃',
                'type': '2,4-directing',
                'positions': ['2', '4'],
                'example_product': '2-nitromethylbenzene and 4-nitromethylbenzene'
            },
            {
                'compound': 'phenol',
                'substituent': 'OH',
                'type': '2,4,6-directing',
                'positions': ['2', '4', '6'],
                'example_product': '2,4,6-tribromophenol'
            },
            {
                'compound': 'nitrobenzene',
                'substituent': 'NO₂',
                'type': '3-directing',
                'positions': ['3'],
                'example_product': '3-nitrobenzoic acid'
            }
        ]
        
        self.subst = rnd.choice(substituents)
        self.answer = f"positions {', '.join(self.subst['positions'])}"
        
        self.description = (
            f"{self.subst['compound']} contains a {self.subst['substituent']} substituent on the benzene ring. "
            f"This substituent directs incoming electrophiles to specific positions. "
            f"When {self.subst['compound']} undergoes further electrophilic substitution, "
            f"which position(s) will the new substituent preferentially occupy? (numbered 1-6)"
        )
        
        self.topic = "Hydrocarbons"
        self.subtopic = "30.1 Arenes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Substituent: {self.subst['substituent']}}}&\\\\"
            f"\\text{{Directing effect: {self.subst['type']}}}&\\\\"
            f"\\text{{Preferred positions: {', '.join(self.subst['positions'])}}}&\\\\"
            f"\\text{{Example product: {self.subst['example_product']}}}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7.5, f"Directing Effects: {self.subst['compound']}", fontsize=16)
        
        center_x, center_y = 5, 4
        radius = 1.2
        
        hexagon = patches.RegularPolygon((center_x, center_y), 6, radius=radius,
                                        facecolor='lightyellow', edgecolor='black', linewidth=3)
        ax.add_patch(hexagon)
        
        circle = Circle((center_x, center_y), radius*0.6, fill=False, 
                       edgecolor='blue', linewidth=2, linestyle='--')
        ax.add_patch(circle)
        
        angles = [90, 30, -30, -90, -150, 150]
        for i, angle in enumerate(angles):
            pos_num = i + 1
            rad = np.radians(angle)
            
            label_x = center_x + (radius + 0.5) * np.cos(rad)
            label_y = center_y + (radius + 0.5) * np.sin(rad)
            
            if str(pos_num) in self.subst['positions']:
                ax.text(label_x, label_y, str(pos_num), fontsize=16, ha='center', va='center',
                       fontweight='bold', color='red',
                       bbox=dict(boxstyle='circle', facecolor='yellow', edgecolor='red', linewidth=2))
            else:
                ax.text(label_x, label_y, str(pos_num), fontsize=14, ha='center', va='center',
                       fontweight='bold', color='black',
                       bbox=dict(boxstyle='circle', facecolor='white', edgecolor='black', linewidth=1))
        
        subst_y = center_y + radius + 0.8
        ax.text(center_x, subst_y, self.subst['substituent'], fontsize=14, ha='center', 
               fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.4))
        
        explanation = (f"{self.subst['type']} substituent\n"
                      f"Directs to: {', '.join(self.subst['positions'])}")
        ax.text(5, 1, explanation, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightgreen', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem067:
    """
    Topic: 32.2 Hydroxy compounds - Phenol
    """
    
    def __init__(self):
        comparisons = [
            {
                'compounds': ['water', 'ethanol', 'phenol'],
                'formulas': ['H₂O', 'C₂H₅OH', 'C₆H₅OH'],
                'pKa': [15.7, 15.9, 9.9],
                'order': 'phenol > ethanol > water'
            },
            {
                'compounds': ['ethanol', 'phenol', '2-nitrophenol'],
                'formulas': ['C₂H₅OH', 'C₆H₅OH', '2-NO₂C₆H₄OH'],
                'pKa': [15.9, 9.9, 7.2],
                'order': '2-nitrophenol > phenol > ethanol'
            }
        ]
        
        self.comp = rnd.choice(comparisons)
        self.answer = self.comp['order']
        
        self.description = (
            f"The table shows pKa values for three compounds. "
            f"Arrange them in order of increasing acidity (weakest to strongest acid)."
        )
        
        self.topic = "Hydroxy compounds"
        self.subtopic = "32.2 Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Lower pKa = stronger acid}&\\\\"
            + "\\\\".join([f"\\text{{{compound}: pKa = {pKa}}}" 
                          for compound, pKa in zip(self.comp['compounds'], self.comp['pKa'])]) + "\\\\"
            f"\\text{{Order of acidity: {self.comp['order']}}}&\\\\"
            "\\text{Phenol is more acidic than alcohols due to}&\\\\"
            "\\text{resonance stabilization of phenoxide ion}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 6, 6.5, "Acidity Comparison", fontsize=16)
        
        col_width = 3
        row_height = 0.8
        
        headers = ['Compound', 'Formula', 'pKa']
        for i, header in enumerate(headers):
            x = 1.5 + i * col_width
            y = 5.5
            ax.text(x, y, header, fontsize=13, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgray', 
                            edgecolor='black', linewidth=2))
        
        for row_idx in range(3):
            y = 5.5 - (row_idx + 1) * row_height
            
            ax.text(1.5, y, self.comp['compounds'][row_idx], fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
            
            ax.text(4.5, y, self.comp['formulas'][row_idx], fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))
            
            pKa_color = 'lightgreen' if self.comp['pKa'][row_idx] < 12 else 'lightcoral'
            ax.text(7.5, y, f"{self.comp['pKa'][row_idx]}", fontsize=12, ha='center',
                   bbox=dict(boxstyle='round', facecolor=pKa_color, pad=0.3))
        
        ax.text(6, 1.5, "Arrange in order of increasing acidity", 
               fontsize=13, ha='center', fontweight='bold')
        ax.text(6, 0.8, "(weakest acid → strongest acid)", 
               fontsize=11, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem068:
    """
    Topic: 32.2 Hydroxy compounds - Phenol
    """
    
    def __init__(self):
        reactions = [
            {
                'name': 'Bromination',
                'reagent': 'Br₂(aq)',
                'conditions': 'room temperature',
                'product': '2,4,6-tribromophenol',
                'product_formula': 'C₆H₂Br₃OH',
                'observation': 'white precipitate forms'
            },
            {
                'name': 'Nitration',
                'reagent': 'dilute HNO₃',
                'conditions': 'room temperature',
                'product': '2-nitrophenol and 4-nitrophenol',
                'product_formula': '2-NO₂C₆H₄OH + 4-NO₂C₆H₄OH',
                'observation': 'yellow oil forms'
            }
        ]
        
        self.rxn = rnd.choice(reactions)
        self.answer = self.rxn['product']
        
        self.description = (
            f"Phenol reacts with {self.rxn['reagent']} at {self.rxn['conditions']}. "
            f"The reaction is much easier than the corresponding reaction of benzene. "
            f"What is the organic product formed? Explain why phenol reacts more readily than benzene."
        )
        
        self.topic = "Hydroxy compounds"
        self.subtopic = "32.2 Phenol"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.rxn['name']}}}&\\\\"
            f"\\text{{Product: {self.rxn['product']}}}&\\\\"
            "\\text{Phenol reacts more readily because:}&\\\\"
            "\\text{- OH group activates benzene ring}&\\\\"
            "\\text{- Lone pair on O delocalizes into ring}&\\\\"
            "\\text{- Increases electron density in ring}&\\\\"
            "\\text{- Directs to 2,4,6 positions}&"
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
        
        x2, y2 = 11, 3.5
        hexagon2 = patches.RegularPolygon((x2, y2), 6, radius=0.8,
                                         facecolor='lightgreen', edgecolor='black', linewidth=2.5)
        ax.add_patch(hexagon2)
        ax.text(x2, y2 + 1.2, 'OH', fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', pad=0.3))
        
        if '2,4,6' in self.rxn['product']:
            positions = [(x2 - 0.7, y2 + 0.4), (x2 + 0.7, y2 + 0.4), (x2, y2 - 0.8)]
            for px, py in positions:
                ax.text(px, py, 'Br', fontsize=11, ha='center', fontweight='bold',
                       bbox=dict(boxstyle='circle', facecolor='orange', pad=0.2))
        else:
            ax.text(x2 - 0.7, y2 + 0.4, 'NO₂', fontsize=10, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='yellow', pad=0.2))
            ax.text(x2 + 0.7, y2 + 0.4, 'NO₂', fontsize=10, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='yellow', pad=0.2))
        
        ax.text(x2, y2 - 1.5, self.rxn['product'], fontsize=11, ha='center', fontweight='bold')
        
        obs_text = f"Observation: {self.rxn['observation']}"
        ax.text(7, 1, obs_text, fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem069:
    """
    Topic: 32.2 Alcohols reactions
    Visual: Oxidation of alcohols diagram
    Task: Identify product of alcohol oxidation
    """
    
    def __init__(self):
        alcohols = [
            ("primary", "aldehyde then carboxylic acid", "RCHO → RCOOH"),
            ("secondary", "ketone", "RCOR'"),
            ("tertiary", "no reaction", "no oxidation")
        ]
        
        self.alcohol_type = rnd.choice(alcohols)
        self.classification = self.alcohol_type[0]
        self.product_desc = self.alcohol_type[1]
        self.product_formula = self.alcohol_type[2]
        
        self.answer = self.product_desc
        
        self.description = (
            f"A {self.classification} alcohol is oxidized with acidified potassium dichromate. "
            f"What is the organic product formed?"
        )
        
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.classification} alcohol oxidation:}} &\\\\"
            f"\\text{{Product: {self.product_desc}}} &\\\\"
            f"\\text{{Formula: {self.product_formula}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 6, 6.5, f"{self.classification.capitalize()} Alcohol Oxidation", fontsize=16)
        
        draw_labeled_box(ax, 1, 3, 3, 1.5, "R-OH\n(alcohol)", facecolor='lightblue')
        
        draw_arrow(ax, 4, 3.8, 8, 3.8, 
                  label="[O]\nK₂Cr₂O₇/H⁺", 
                  label_position='above', color='red', linewidth=2.5)
        
        draw_labeled_box(ax, 9, 3, 3, 1.5, f"{self.product_formula}\n({self.product_desc})",
                        facecolor='lightgreen')
        
        if self.classification == "primary":
            add_formula_label(ax, 6, 1, "Further oxidation possible", fontsize=11)
        elif self.classification == "tertiary":
            add_formula_label(ax, 6, 1, "Resistant to oxidation", fontsize=11)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem070:
    """
    Topic: 32.2 Alcohol dehydration
    Visual: Dehydration reaction mechanism
    Task: Identify alkene product from alcohol dehydration
    """
    
    def __init__(self):
        reactions = [
            ("ethanol", "ethene", "CH₃CH₂OH", "CH₂=CH₂"),
            ("propan-1-ol", "propene", "CH₃CH₂CH₂OH", "CH₃CH=CH₂"),
            ("propan-2-ol", "propene", "CH₃CH(OH)CH₃", "CH₃CH=CH₂"),
            ("butan-2-ol", "but-2-ene", "CH₃CH(OH)CH₂CH₃", "CH₃CH=CHCH₃")
        ]
        
        self.reaction = rnd.choice(reactions)
        self.alcohol_name = self.reaction[0]
        self.alkene_name = self.reaction[1]
        self.alcohol_formula = self.reaction[2]
        self.alkene_formula = self.reaction[3]
        
        self.answer = self.alkene_name
        
        self.description = (
            f"When {self.alcohol_name} undergoes dehydration with concentrated H₂SO₄, "
            f"what is the main alkene product formed?"
        )
        
        self.topic = "Hydroxy compounds"
        self.subtopic = "Alcohol dehydration"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Dehydration reaction:}} &\\\\"
            f"\\text{{{self.alcohol_formula}}} &\\xrightarrow{{\\text{{H}}_2\\text{{SO}}_4, \\Delta}} \\text{{{self.alkene_formula}}} + \\text{{H}}_2\\text{{O}}\\\\"
            f"\\text{{Product: {self.alkene_name}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_formula_label(ax, 2, 3, self.alcohol_formula, fontsize=18, weight='bold')
        
        draw_arrow(ax, 4, 3, 8, 3, 
                  label="H₂SO₄, heat", 
                  label_position='above', color='red', linewidth=3)
        
        add_formula_label(ax, 10, 3, self.alkene_formula, fontsize=18, weight='bold')
        add_formula_label(ax, 10, 2, "+ H₂O", fontsize=14)
        
        add_title_box(ax, 6, 5.5, "Alcohol Dehydration", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem071:
    """
    Topic: 33.3 Carboxylic acid derivatives
    """
    
    def __init__(self):
        reactions = [
            {
                'acyl_chloride': 'CH₃COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'H₂O',
                'nuc_name': 'water',
                'product': 'CH₃COOH',
                'product_name': 'ethanoic acid',
                'by_product': 'HCl'
            },
            {
                'acyl_chloride': 'CH₃COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'C₂H₅OH',
                'nuc_name': 'ethanol',
                'product': 'CH₃COOC₂H₅',
                'product_name': 'ethyl ethanoate',
                'by_product': 'HCl'
            },
            {
                'acyl_chloride': 'CH₃COCl',
                'acyl_name': 'ethanoyl chloride',
                'nucleophile': 'NH₃',
                'nuc_name': 'ammonia',
                'product': 'CH₃CONH₂',
                'product_name': 'ethanamide',
                'by_product': 'HCl'
            }
        ]
        
        self.rxn = rnd.choice(reactions)
        self.answer = f"{self.rxn['product']} + {self.rxn['by_product']}"
        
        self.description = (
            f"{self.rxn['acyl_name']} reacts with {self.rxn['nuc_name']} at room temperature "
            f"via an addition-elimination mechanism. Draw the mechanism showing the tetrahedral "
            f"intermediate and identify the final products."
        )
        
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "33.3 Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Nucleophilic addition}&\\\\"
            "\\text{Nucleophile attacks C=O carbon}&\\\\"
            "\\text{Step 2: Tetrahedral intermediate forms}&\\\\"
            "\\text{Step 3: Cl⁻ eliminated}&\\\\"
            f"\\text{{Products: {self.rxn['product']} + HCl}}&"
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
        
        draw_curly_arrow(ax, 2.8, y_level + 0.3, 3.5, y_level, curvature=0.3, color='blue', linewidth=2)
        ax.text(3.5, y_level + 0.5, self.rxn['nucleophile'], fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='yellow', pad=0.3))
        
        draw_arrow(ax, 4, y_level, 5.5, y_level, color='black', linewidth=2)
        
        intermediate_structure = "    OH\n     |\nCH₃-C-Cl\n     |\n    Nu"
        ax.text(7, y_level, "Tetrahedral\nIntermediate", fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='red', linewidth=2.5, pad=0.5))
        ax.text(7, y_level - 1, '(C bonded to 4 groups)', fontsize=10, ha='center', style='italic')
        
        draw_curly_arrow(ax, 8, y_level, 9, y_level - 0.3, curvature=-0.2, color='red', linewidth=2)
        ax.text(9.3, y_level - 0.5, 'Cl⁻', fontsize=12, ha='center', color='red', fontweight='bold')
        
        draw_arrow(ax, 8.5, y_level, 10, y_level, color='black', linewidth=2)
        
        ax.text(11.5, y_level, self.rxn['product'], fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', pad=0.5))
        ax.text(11.5, y_level - 1, self.rxn['product_name'], fontsize=11, ha='center')
        
        equation = f"{self.rxn['acyl_chloride']} + {self.rxn['nucleophile']} → {self.rxn['product']} + HCl"
        ax.text(7, 1.5, equation, fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightcyan', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem072:
    """
    Topic: 33.3 Carboxylic acid derivatives
    """
    
    def __init__(self):
        self.compounds = ['CH₃COCl', 'CH₃CH₂Cl', 'C₆H₅Cl']
        self.names = ['Ethanoyl chloride\n(acyl chloride)', 
                     'Chloroethane\n(alkyl chloride)', 
                     'Chlorobenzene\n(aryl chloride)']
        self.relative_rates = [100, 1, 0.001]
        
        max_rate = max(self.relative_rates)
        self.display_rates = [r/max_rate * 10 for r in self.relative_rates]
        
        self.answer = "acyl chloride > alkyl chloride > aryl chloride"
        
        self.description = (
            f"The bar chart shows the relative rates of hydrolysis for three chlorine-containing compounds "
            f"with water at room temperature. Explain the order of reactivity in terms of C-Cl bond polarity "
            f"and resonance effects."
        )
        
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "33.3 Acyl chlorides"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Acyl chloride: Most reactive}&\\\\"
            "\\text{- C=O withdraws electrons}&\\\\"
            "\\text{- C-Cl bond highly polarized}&\\\\"
            "\\text{- Easy nucleophilic attack}&\\\\"
            "\\text{Alkyl chloride: Moderate reactivity}&\\\\"
            "\\text{- Some C-Cl bond polarity}&\\\\"
            "\\text{Aryl chloride: Least reactive}&\\\\"
            "\\text{- Lone pair on Cl delocalizes into ring}&\\\\"
            "\\text{- Partial double bond character}&\\\\"
            "\\text{- Stronger C-Cl bond}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        x_positions = [1, 3, 5]
        colors = ['red', 'orange', 'yellow']
        
        bars = draw_bar_chart(ax, x_positions, self.display_rates, 
                             ['Acyl', 'Alkyl', 'Aryl'],
                             colors=colors, width=0.8,
                             xlabel='Type of Chloride', 
                             ylabel='Relative Rate of Hydrolysis',
                             title='Reactivity of C-Cl Bonds')
        
        for i, (x, compound, name) in enumerate(zip(x_positions, self.compounds, self.names)):
            ax.text(x, self.display_rates[i] + 0.5, compound, 
                   fontsize=12, ha='center', fontweight='bold')
            ax.text(x, -1.5, name, fontsize=10, ha='center', style='italic')
        
        ax.set_ylim(0, 12)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem073:
    """
    Topic: 33.3 Carboxylic acid derivatives
    Visual: Acyl chloride reactions
    Task: Identify product of acyl chloride reaction
    """
    
    def __init__(self):
        reactions = [
            ("water", "carboxylic acid", "H₂O", "RCOOH + HCl"),
            ("alcohol", "ester", "R'OH", "RCOOR' + HCl"),
            ("ammonia", "amide", "NH₃", "RCONH₂ + HCl"),
            ("amine", "N-substituted amide", "R'NH₂", "RCONHR' + HCl")
        ]
        
        self.reaction = rnd.choice(reactions)
        self.reagent_name = self.reaction[0]
        self.product_name = self.reaction[1]
        self.reagent_formula = self.reaction[2]
        self.products = self.reaction[3]
        
        self.answer = self.product_name
        
        self.description = (
            f"When an acyl chloride (RCOCl) reacts with {self.reagent_name}, "
            f"what is the organic product formed?"
        )
        
        self.topic = "Carboxylic acids and derivatives"
        self.subtopic = "Acyl chloride reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{RCOCl}} + \\text{{{self.reagent_formula}}} &\\rightarrow \\text{{{self.products}}}\\\\"
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
        
        add_formula_label(ax, 10.5, 3, self.products, fontsize=16, weight='bold')
        
        add_title_box(ax, 6, 5.5, "Acyl Chloride Reactions", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem074:
    
    def __init__(self):
        amino_acids = [
            {
                'name': 'glycine',
                'formula': 'H₂NCH₂COOH',
                'isoelectric_point': 6.0,
                'low_pH': 'H₃N⁺CH₂COOH',
                'zwitterion': 'H₃N⁺CH₂COO⁻',
                'high_pH': 'H₂NCH₂COO⁻'
            },
            {
                'name': 'alanine',
                'formula': 'H₂NCH(CH₃)COOH',
                'isoelectric_point': 6.0,
                'low_pH': 'H₃N⁺CH(CH₃)COOH',
                'zwitterion': 'H₃N⁺CH(CH₃)COO⁻',
                'high_pH': 'H₂NCH(CH₃)COO⁻'
            }
        ]
        
        self.aa = rnd.choice(amino_acids)
        self.answer = f"pH {self.aa['isoelectric_point']}: {self.aa['zwitterion']}"
        
        self.description = (
            f"The diagram shows the structure of {self.aa['name']} at three different pH values. "
            f"Identify which structure represents the zwitterion and state the approximate pH "
            f"at which it exists (isoelectric point = {self.aa['isoelectric_point']})."
        )
        
        self.topic = "Nitrogen compounds"
        self.subtopic = "34.4 Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{At pH 2 (acidic): {self.aa['low_pH']}}}&\\\\"
            f"\\text{{At pH {self.aa['isoelectric_point']} (isoelectric): {self.aa['zwitterion']}}}&\\\\"
            f"\\text{{At pH 10 (alkaline): {self.aa['high_pH']}}}&\\\\"
            "\\text{Zwitterion has both +NH₃⁺ and COO⁻ groups}&\\\\"
            "\\text{Overall charge = 0 at isoelectric point}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 7, 6.5, f"{self.aa['name'].capitalize()} at Different pH", fontsize=16)
        
        draw_labeled_box(ax, 0.5, 3, 3.5, 1.5, self.aa['low_pH'], 'pH 2 (acidic)',
                        facecolor='lightcoral')
        ax.text(2.25, 2, 'Charge: +1', fontsize=11, ha='center', fontweight='bold', color='red')
        
        draw_labeled_box(ax, 5.25, 3, 3.5, 1.5, self.aa['zwitterion'], 
                        f'pH {self.aa["isoelectric_point"]} (isoelectric)',
                        facecolor='yellow', edgecolor='red', linewidth=3)
        ax.text(7, 2, 'Charge: 0', fontsize=11, ha='center', fontweight='bold', color='blue')
        ax.text(7, 1.5, 'ZWITTERION', fontsize=12, ha='center', fontweight='bold', 
               color='red', style='italic')
        
        draw_labeled_box(ax, 10, 3, 3.5, 1.5, self.aa['high_pH'], 'pH 10 (alkaline)',
                        facecolor='lightblue')
        ax.text(11.75, 2, 'Charge: -1', fontsize=11, ha='center', fontweight='bold', color='blue')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem075:
    def __init__(self):
        scenarios = [
            {
                'pH': 6,
                'amino_acid': 'glycine',
                'pI': 6.0,
                'charge': '0',
                'migration': 'no migration',
                'position': 'center'
            },
            {
                'pH': 6,
                'amino_acid': 'lysine',
                'pI': 9.7,
                'charge': '+',
                'migration': 'toward cathode (negative electrode)',
                'position': 'left'
            },
            {
                'pH': 6,
                'amino_acid': 'aspartic acid',
                'pI': 2.8,
                'charge': '-',
                'migration': 'toward anode (positive electrode)',
                'position': 'right'
            }
        ]
        
        self.scenario = rnd.choice(scenarios)
        self.answer = self.scenario['migration']
        
        self.description = (
            f"An electrophoresis experiment is performed at pH {self.scenario['pH']}. "
            f"{self.scenario['amino_acid'].capitalize()} (isoelectric point = {self.scenario['pI']}) "
            f"is applied at the center of the paper. "
            f"In which direction will the amino acid migrate when voltage is applied?"
        )
        
        self.topic = "Nitrogen compounds"
        self.subtopic = "34.4 Amino acids"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{pH of buffer: {self.scenario['pH']}}}&\\\\"
            f"\\text{{Isoelectric point: {self.scenario['pI']}}}&\\\\"
            f"\\text{{At pH {self.scenario['pH']}, charge: {self.scenario['charge']}}}&\\\\"
            f"\\text{{Migration: {self.scenario['migration']}}}&"
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
        
        draw_labeled_box(ax, 0.5, 3, 1.5, 2, '−', 'Cathode\n(negative)', 
                        facecolor='lightblue', edgecolor='blue', linewidth=3)
        
        paper = patches.Rectangle((2.5, 3.5), 9, 1, facecolor='wheat', 
                                  edgecolor='black', linewidth=2)
        ax.add_patch(paper)
        
        ax.plot(7, 4, 'ko', markersize=15)
        ax.text(7, 4.7, 'Start', fontsize=11, ha='center', fontweight='bold')
        
        if self.scenario['position'] == 'center':
            final_x = 7
            arrow_color = 'gray'
            ax.text(7, 2.5, 'No migration\n(charge = 0)', fontsize=11, ha='center', 
                   fontweight='bold', color=arrow_color)
        elif self.scenario['position'] == 'left':
            final_x = 3.5
            arrow_color = 'blue'
            draw_arrow(ax, 7, 4, final_x, 4, color=arrow_color, linewidth=3)
            ax.text(final_x, 2.5, 'Positive charge\nmigrates to cathode', 
                   fontsize=11, ha='center', fontweight='bold', color=arrow_color)
        else:
            final_x = 10.5
            arrow_color = 'red'
            draw_arrow(ax, 7, 4, final_x, 4, color=arrow_color, linewidth=3)
            ax.text(final_x, 2.5, 'Negative charge\nmigrates to anode', 
                   fontsize=11, ha='center', fontweight='bold', color=arrow_color)
        
        if self.scenario['position'] != 'center':
            ax.plot(final_x, 4, 'o', color=arrow_color, markersize=15)
            ax.text(final_x, 4.7, 'Final', fontsize=11, ha='center', fontweight='bold')
        
        info = (f"Amino acid: {self.scenario['amino_acid']}\n"
               f"pI = {self.scenario['pI']}\n"
               f"pH = {self.scenario['pH']}\n"
               f"Charge: {self.scenario['charge']}")
        ax.text(7, 1, info, fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem076:
    """
    Topic: 34.4 Amide formation
    Visual: Reaction scheme for amide synthesis
    Task: Identify reagents for amide formation
    """
    
    def __init__(self):
        methods = [
            ("acyl chloride + ammonia", "RCOCl + NH₃"),
            ("acyl chloride + amine", "RCOCl + R'NH₂"),
            ("carboxylic acid + amine + heat", "RCOOH + R'NH₂, Δ")
        ]
        
        self.method = rnd.choice(methods)
        self.method_name = self.method[0]
        self.reagents = self.method[1]
        
        self.answer = self.method_name
        
        self.description = (
            f"What reagents are needed to form an amide using the method shown?"
        )
        
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amide formation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Method: {self.method_name}}} &\\\\"
            f"\\text{{Reagents: {self.reagents}}}"
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
        
        draw_arrow(ax, 4, 4.2, 8, 4.2, label="?", label_position='above',
                  color='red', linewidth=2.5)
        
        draw_labeled_box(ax, 9, 3.5, 3, 1.2, "Amide\nRCONH₂", 
                        facecolor='lightgreen')
        
        add_formula_label(ax, 6, 2, f"Reagents: {self.reagents}", fontsize=12,
                         bbox_style=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem077:
    """
    Topic: 35.1 Addition polymerization
    """
    
    def __init__(self):
        monomers = [
            {
                'diamine': '1,6-diaminohexane',
                'diamine_formula': 'H₂N(CH₂)₆NH₂',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH₂)₄COOH',
                'repeat_unit': '[-NH(CH₂)₆NHCO(CH₂)₄CO-]',
                'polymer_name': 'Nylon 6,6'
            },
            {
                'diamine': '1,4-diaminobutane',
                'diamine_formula': 'H₂N(CH₂)₄NH₂',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH₂)₄COOH',
                'repeat_unit': '[-NH(CH₂)₄NHCO(CH₂)₄CO-]',
                'polymer_name': 'Nylon 4,6'
            }
        ]
        
        self.mono = rnd.choice(monomers)
        self.answer = self.mono['repeat_unit']
        
        self.description = (
            f"{self.mono['diamine']} reacts with {self.mono['diacid']} to form a polyamide ({self.mono['polymer_name']}). "
            f"Draw the repeat unit of the polymer. Show the amide linkages (peptide bonds) clearly."
        )
        
        self.topic = "Polymerisation"
        self.subtopic = "35.1 Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diamine: {self.mono['diamine_formula']}}}&\\\\"
            f"\\text{{Diacid: {self.mono['diacid_formula']}}}&\\\\"
            "\\text{Condensation: -NH₂ + -COOH → -CONH- + H₂O}&\\\\"
            f"\\text{{Repeat unit: {self.mono['repeat_unit']}}}&\\\\"
            "\\text{Amide/peptide linkage: -CONH-}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 7, 7.5, f"Polyamide Formation: {self.mono['polymer_name']}", fontsize=16)
        
        draw_labeled_box(ax, 1, 5, 3, 1, self.mono['diamine_formula'], 
                        self.mono['diamine'], facecolor='lightblue')
        
        ax.text(4.8, 5.5, '+', fontsize=20, ha='center', fontweight='bold')
        
        draw_labeled_box(ax, 5.5, 5, 3, 1, self.mono['diacid_formula'], 
                        self.mono['diacid'], facecolor='lightyellow')
        
        draw_arrow(ax, 9, 5.5, 11, 5.5, label="heat\n-H₂O", 
                  label_position='above', color='black', linewidth=2.5)
        
        draw_labeled_box(ax, 11.5, 5, 2, 1, "Polyamide", 
                        facecolor='lightgreen')
        
        y_pos = 3
        
        draw_bracket(ax, 2, y_pos - 0.5, 1.5, bracket_type='square', 
                    direction='left', subscript='n')
        
        ax.text(7, y_pos, self.mono['repeat_unit'], fontsize=13, ha='center', 
               fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', pad=0.5))
        
        draw_bracket(ax, 12, y_pos - 0.5, 1.5, bracket_type='square', 
                    direction='right', subscript='n')
        
        ax.text(7, 1.5, "Amide (peptide) linkage: -CONH-", fontsize=12, ha='center',
               fontweight='bold', color='red',
               bbox=dict(boxstyle='round', facecolor='yellow', 
                        edgecolor='red', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem078:
    """
    Topic: 35.1 Addition polymerization
    """
    
    def __init__(self):
        monomers = [
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH₂CH₂OH',
                'diacid': 'benzene-1,4-dicarboxylic acid',
                'diacid_formula': 'HOOC-C₆H₄-COOH',
                'repeat_unit': '[-OCH₂CH₂OOC-C₆H₄-CO-]',
                'polymer_name': 'polyester (PET)'
            },
            {
                'diol': 'ethane-1,2-diol',
                'diol_formula': 'HOCH₂CH₂OH',
                'diacid': 'hexanedioic acid',
                'diacid_formula': 'HOOC(CH₂)₄COOH',
                'repeat_unit': '[-OCH₂CH₂OOC(CH₂)₄CO-]',
                'polymer_name': 'polyester'
            }
        ]
        
        self.mono = rnd.choice(monomers)
        self.answer = self.mono['repeat_unit']
        
        self.description = (
            f"{self.mono['diol']} reacts with {self.mono['diacid']} to form a polyester. "
            f"Draw the repeat unit of the polymer formed. "
            f"Show the ester linkages clearly."
        )
        
        self.topic = "Polymerisation"
        self.subtopic = "35.1 Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diol: {self.mono['diol_formula']}}}&\\\\"
            f"\\text{{Diacid: {self.mono['diacid_formula']}}}&\\\\"
            "\\text{Condensation reaction: -OH + -COOH → -COO- + H₂O}&\\\\"
            f"\\text{{Repeat unit: {self.mono['repeat_unit']}}}&\\\\"
            "\\text{Ester linkage: -COO-}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 7, 7.5, "Polyester Formation", fontsize=16)
        
        draw_labeled_box(ax, 1, 5, 3, 1, self.mono['diol_formula'], 
                        self.mono['diol'], facecolor='lightblue')
        
        ax.text(4.8, 5.5, '+', fontsize=20, ha='center', fontweight='bold')
        
        draw_labeled_box(ax, 5.5, 5, 3, 1, self.mono['diacid_formula'], 
                        self.mono['diacid'], facecolor='lightyellow')
        
        draw_arrow(ax, 9, 5.5, 11, 5.5, label="heat\n-H₂O", 
                  label_position='above', color='black', linewidth=2.5)
        
        draw_labeled_box(ax, 11.5, 5, 2, 1, "Polyester", 
                        facecolor='lightgreen')
        
        y_pos = 3
        
        draw_bracket(ax, 2, y_pos - 0.5, 1.5, bracket_type='square', 
                    direction='left', subscript='n')
        
        ax.text(7, y_pos, self.mono['repeat_unit'], fontsize=13, ha='center', 
               fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', pad=0.5))
        
        draw_bracket(ax, 12, y_pos - 0.5, 1.5, bracket_type='square', 
                    direction='right', subscript='n')
        
        ax.text(7, 1.5, "Ester linkage: -COO-", fontsize=12, ha='center',
               fontweight='bold', color='red',
               bbox=dict(boxstyle='round', facecolor='yellow', 
                        edgecolor='red', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem079:
    """
    Topic: 35.1 Addition polymerization
    Visual: Polymerization of alkene
    Task: Identify monomer from polymer structure
    """
    
    def __init__(self):
        polymers = [
            ("poly(ethene)", "CH₂=CH₂", "-(CH₂-CH₂)n-"),
            ("poly(propene)", "CH₂=CH(CH₃)", "-(CH₂-CH(CH₃))n-"),
            ("poly(chloroethene)", "CH₂=CHCl", "-(CH₂-CHCl)n-"),
            ("poly(tetrafluoroethene)", "CF₂=CF₂", "-(CF₂-CF₂)n-")
        ]
        
        self.polymer = rnd.choice(polymers)
        self.polymer_name = self.polymer[0]
        self.monomer_formula = self.polymer[1]
        self.polymer_formula = self.polymer[2]
        
        self.answer = self.monomer_formula
        
        self.description = (
            f"The repeating unit of {self.polymer_name} is shown. "
            f"What is the monomer used to make this polymer?"
        )
        
        self.topic = "Polymerisation"
        self.subtopic = "Addition polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Polymer: {self.polymer_formula}}} &\\\\"
            f"\\text{{Monomer: {self.monomer_formula}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5.5, "Addition Polymerization", fontsize=16)
        
        add_formula_label(ax, 2.5, 3, "n", fontsize=16, weight='bold')
        add_formula_label(ax, 3.5, 3, self.monomer_formula, fontsize=18, weight='bold')
        
        draw_arrow(ax, 5, 3, 7, 3, label="polymerization", label_position='above',
                  color='blue', linewidth=3)
        
        draw_bracket(ax, 8.5, 2.5, height=1.5, bracket_type='square', direction='left')
        add_formula_label(ax, 9.5, 3, self.polymer_formula, fontsize=16, weight='bold')
        draw_bracket(ax, 10.5, 2.5, height=1.5, bracket_type='square', direction='right', 
                    subscript='n')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem080:
    """
    Topic: 35.3 Condensation polymerization
    """
    
    def __init__(self):
        self.polymers = ['Poly(ethene)', 'Polyester', 'Polyamide']
        self.linkages = ['C-C', 'Ester (-COO-)', 'Amide (-CONH-)']
        self.biodegradable = ['No', 'Yes', 'Yes']
        self.mechanism = [
            'Chemically inert\nNo hydrolyzable bonds',
            'Ester hydrolysis\nby enzymes/acid/base',
            'Amide hydrolysis\nby enzymes/acid/base'
        ]
        
        self.answer = "Polyester and Polyamide (biodegradable)"
        
        self.description = (
            f"The table compares three types of polymers. "
            f"Which polymer(s) is/are biodegradable? "
            f"Explain in terms of bond types and hydrolysis reactions."
        )
        
        self.topic = "Polymerisation"
        self.subtopic = "35.3 Degradable polymers"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Poly(ethene): Not biodegradable}&\\\\"
            "\\text{- Only C-C and C-H bonds}&\\\\"
            "\\text{- Chemically inert}&\\\\"
            "\\text{Polyester: Biodegradable}&\\\\"
            "\\text{- Ester linkages can be hydrolyzed}&\\\\"
            "\\text{- By enzymes, acids, or bases}&\\\\"
            "\\text{Polyamide: Biodegradable}&\\\\"
            "\\text{- Amide linkages can be hydrolyzed}&\\\\"
            "\\text{- Slower than polyesters}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_xlim(0, 13)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6.5, 7.5, "Polymer Biodegradability", fontsize=16)
        
        col_width = 3
        row_height = 1
        headers = ['Polymer', 'Linkage', 'Biodegradable?', 'Mechanism']
        
        for i, header in enumerate(headers):
            x = 0.5 + i * col_width
            y = 6.5
            if i == 3:
                x = 10
            ax.text(x, y, header, fontsize=12, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgray', 
                            edgecolor='black', linewidth=2))
        
        for row_idx in range(3):
            y = 6.5 - (row_idx + 1) * row_height
            
            color_map = ['lightcoral', 'lightgreen', 'lightblue']
            ax.text(0.5, y, self.polymers[row_idx], fontsize=11, ha='center',
                   bbox=dict(boxstyle='round', facecolor=color_map[row_idx], pad=0.3))
            
            ax.text(3.5, y, self.linkages[row_idx], fontsize=11, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))
            
            bio_color = 'lightgreen' if self.biodegradable[row_idx] == 'Yes' else 'lightcoral'
            ax.text(6.5, y, self.biodegradable[row_idx], fontsize=12, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor=bio_color, pad=0.3))
            
            ax.text(10, y, self.mechanism[row_idx], fontsize=9, ha='center',
                   bbox=dict(boxstyle='round', facecolor='wheat', pad=0.3))
        
        ax.text(6.5, 1.5, "Which polymers can be broken down by hydrolysis?", 
               fontsize=13, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem081:
    """
    Topic: 35.3 Condensation polymerization
    Visual: Formation of polyester or polyamide
    Task: Identify type of polymer formed
    """
    
    def __init__(self):
        polymers = [
            ("polyester", "diol + dicarboxylic acid", "ester linkage -COO-"),
            ("polyamide", "diamine + dicarboxylic acid", "amide linkage -CONH-")
        ]
        
        self.polymer = rnd.choice(polymers)
        self.polymer_type = self.polymer[0]
        self.monomers = self.polymer[1]
        self.linkage = self.polymer[2]
        
        self.answer = self.polymer_type
        
        self.description = (
            f"The diagram shows monomers used in condensation polymerization. "
            f"What type of polymer is formed?"
        )
        
        self.topic = "Polymerisation"
        self.subtopic = "Condensation polymerisation"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Monomers: {self.monomers}}} &\\\\"
            f"\\text{{Linkage: {self.linkage}}} &\\\\"
            f"\\text{{Polymer type: {self.polymer_type}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 6, 6.5, "Condensation Polymerization", fontsize=16)
        
        if self.polymer_type == "polyester":
            draw_labeled_box(ax, 1, 4.5, 2.5, 1, "HO-R-OH\n(diol)", facecolor='lightblue')
            draw_labeled_box(ax, 1, 2.5, 2.5, 1, "HOOC-R'-COOH\n(diacid)", facecolor='lightcoral')
        else:
            draw_labeled_box(ax, 1, 4.5, 2.5, 1, "H₂N-R-NH₂\n(diamine)", facecolor='lightblue')
            draw_labeled_box(ax, 1, 2.5, 2.5, 1, "HOOC-R'-COOH\n(diacid)", facecolor='lightcoral')
        
        draw_arrow(ax, 4, 3.8, 8, 3.8, label="+ heat\n- H₂O", label_position='above',
                  color='red', linewidth=2.5)
        
        draw_labeled_box(ax, 9, 3.3, 3, 1.3, f"{self.polymer_type}\n{self.linkage}",
                        facecolor='lightgreen')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem082:
    """
    Topic: 36.1 Organic synthesis routes
    """
    
    def __init__(self):
        routes = [
            {
                'start': 'benzene',
                'end': 'phenylamine',
                'steps': ['Nitration', 'Reduction'],
                'reagents': ['conc. HNO₃/H₂SO₄ 50-60°C', 'Sn/conc. HCl then NaOH'],
                'intermediates': ['nitrobenzene', 'phenylamine']
            },
            {
                'start': 'ethene',
                'end': 'ethanoic acid',
                'steps': ['Hydration', 'Oxidation'],
                'reagents': ['H₂O/H₃PO₄ catalyst', 'acidified K₂Cr₂O₇ reflux'],
                'intermediates': ['ethanol', 'ethanoic acid']
            },
            {
                'start': 'propan-1-ol',
                'end': 'propanoic acid',
                'steps': ['Oxidation to aldehyde', 'Oxidation to acid'],
                'reagents': ['acidified K₂Cr₂O₇ distil', 'acidified K₂Cr₂O₇ reflux'],
                'intermediates': ['propanal', 'propanoic acid']
            }
        ]
        
        self.route = rnd.choice(routes)
        self.answer = f"{' → '.join(self.route['intermediates'])}"
        
        self.description = (
            f"Complete the multi-step synthesis from {self.route['start']} to {self.route['end']}. "
            f"Identify the reagents and conditions for each step, and name the intermediate compound(s)."
        )
        
        self.topic = "Organic synthesis"
        self.subtopic = "36.1 Organic synthesis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            + "\\\\".join([f"\\text{{Step {i+1}: {self.route['steps'][i]}}}" 
                          for i in range(len(self.route['steps']))]) + "\\\\"
            + "\\\\".join([f"\\text{{Reagents: {self.route['reagents'][i]}}}" 
                          for i in range(len(self.route['reagents']))]) + "\\\\"
            + f"\\text{{Overall: {self.route['start']} → {self.route['end']}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 7))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        add_title_box(ax, 7, 6.5, f"Synthesis: {self.route['start']} → {self.route['end']}", fontsize=16)
        
        num_steps = len(self.route['intermediates'])
        spacing = 10 / num_steps
        
        x_pos = 2
        for i in range(num_steps):
            compound = self.route['intermediates'][i]
            color = 'lightblue' if i == 0 else ('lightyellow' if i < num_steps - 1 else 'lightgreen')
            draw_labeled_box(ax, x_pos - 0.8, 3.5, 1.6, 0.8, compound, 
                            facecolor=color)
            
            if i < num_steps - 1:
                arrow_start = x_pos + 0.8
                arrow_end = arrow_start + spacing - 1.6
                
                draw_arrow(ax, arrow_start, 3.9, arrow_end, 3.9, 
                          color='black', linewidth=2.5)
                
                reagent_text = self.route['reagents'][i]
                if len(reagent_text) > 20:
                    words = reagent_text.split()
                    mid = len(words) // 2
                    reagent_text = ' '.join(words[:mid]) + '\n' + ' '.join(words[mid:])
                
                ax.text((arrow_start + arrow_end) / 2, 4.8, reagent_text, 
                       fontsize=9, ha='center', 
                       bbox=dict(boxstyle='round', facecolor='wheat', pad=0.3))
                
                ax.text((arrow_start + arrow_end) / 2, 3, f"Step {i+1}", 
                       fontsize=10, ha='center', fontweight='bold', style='italic')
            
            x_pos += spacing
        
        overall = f"{self.route['start']} → {' → '.join(self.route['intermediates'])}"
        ax.text(7, 1, overall, fontsize=11, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow', 
                        edgecolor='black', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem083:
    """
    Topic: 36.1 Organic synthesis routes
    Visual: Multi-step synthesis pathway
    Task: Identify intermediate compound in synthesis
    """
    
    def __init__(self):
        pathways = [
            ("alkane → haloalkane → alcohol", "haloalkane", "RX"),
            ("alcohol → aldehyde → carboxylic acid", "aldehyde", "RCHO"),
            ("alkene → alcohol → ketone", "alcohol", "ROH"),
            ("benzene → nitrobenzene → aniline", "nitrobenzene", "C₆H₅NO₂")
        ]
        
        self.pathway = rnd.choice(pathways)
        self.route = self.pathway[0]
        self.intermediate_name = self.pathway[1]
        self.intermediate_formula = self.pathway[2]
        
        self.answer = self.intermediate_name
        
        self.description = (
            f"In the synthesis route: {self.route}, "
            f"identify the intermediate compound."
        )
        
        self.topic = "Organic synthesis"
        self.subtopic = "Synthesis routes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Synthesis route: {self.route}}} &\\\\"
            f"\\text{{Intermediate: {self.intermediate_name} ({self.intermediate_formula})}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        steps = self.route.split(" → ")
        
        x_pos = 1
        for i, step in enumerate(steps):
            draw_labeled_box(ax, x_pos, 2.5, 2.5, 1.2, step, 
                            facecolor='lightblue' if i != 1 else 'yellow')
            
            if i < len(steps) - 1:
                draw_arrow(ax, x_pos + 2.5, 3.1, x_pos + 4, 3.1, 
                          color='black', linewidth=2)
            
            x_pos += 4
        
        add_title_box(ax, 7, 5.5, "Multi-Step Synthesis", fontsize=16)
        add_formula_label(ax, 7, 1, f"Intermediate: {self.intermediate_formula}", 
                         fontsize=14, weight='bold', color='red')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem084:
    """
    Topic: 37.1 Mass spectrometry fragmentation
    Visual: Mass spectrum with fragmentation pattern
    Task: Identify fragment ion from m/z value
    """
    
    def __init__(self):
        fragments = [
            ("CH₃⁺", 15, "methyl cation"),
            ("C₂H₅⁺", 29, "ethyl cation"),
            ("C₃H₇⁺", 43, "propyl cation"),
            ("CHO⁺", 29, "acyl cation"),
            ("C₆H₅⁺", 77, "phenyl cation")
        ]
        
        self.fragment = rnd.choice(fragments)
        self.ion = self.fragment[0]
        self.mz = self.fragment[1]
        self.name = self.fragment[2]
        
        self.other_peaks = [rnd.randint(40, 90), rnd.randint(100, 150)]
        
        self.answer = self.ion
        
        self.description = (
            f"The mass spectrum shows a peak at m/z = {self.mz}. "
            f"Identify the fragment ion responsible for this peak."
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "Mass spectrometry"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{m/z = {self.mz}}} &\\\\"
            f"\\text{{Fragment ion: {self.ion}}} &\\\\"
            f"\\text{{({self.name})}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        all_peaks = [(self.mz, 100)] + [(p, rnd.randint(20, 60)) for p in self.other_peaks]
        
        for mz, intensity in all_peaks:
            color = 'red' if mz == self.mz else 'gray'
            draw_mass_spectrum_peak(ax, mz, intensity, width=2, color=color, label_offset=3)
        
        ax.set_xlabel('m/z', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative abundance (%)', fontsize=14, fontweight='bold')
        ax.set_title('Mass Spectrum', fontsize=16, fontweight='bold')
        ax.set_xlim(0, max([p[0] for p in all_peaks]) + 20)
        ax.set_ylim(0, 120)
        ax.grid(axis='y', alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem085:
    """
    Topic: 37.1 Mass spectrometry fragmentation
    """
    
    def __init__(self):
        self.num_spots = rnd.randint(2, 4)
        self.solvent_front = 10.0  # cm
        
        self.spots = []
        for i in range(self.num_spots):
            spot_height = round(rnd.uniform(2.0, 9.0), 1)
            rf_value = round(spot_height / self.solvent_front, 2)
            self.spots.append({
                'name': f'Compound {chr(65+i)}',
                'height': spot_height,
                'rf': rf_value
            })
        
        self.spots.sort(key=lambda x: x['height'])
        
        self.questioned_spot = rnd.choice(self.spots)
        self.answer = f"Rf = {self.questioned_spot['rf']}"
        
        self.description = (
            f"A thin-layer chromatography experiment was performed. "
            f"The solvent front traveled {self.solvent_front} cm from the baseline. "
            f"{self.questioned_spot['name']} traveled {self.questioned_spot['height']} cm. "
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
            
            color = 'red' if spot_data == self.questioned_spot else 'purple'
            circle = Circle((x_pos, spot_y), 0.2, facecolor=color, 
                          edgecolor='black', linewidth=1.5)
            ax.add_patch(circle)
            
            ax.text(x_pos, spot_y - 0.5, spot_data['name'][9], fontsize=12, 
                   ha='center', fontweight='bold')
            
            if spot_data == self.questioned_spot:
                draw_vertical_annotation(ax, 8.5, 2, spot_y, f"{spot_data['height']} cm", 
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
    Topic: 37.2 IR spectroscopy
    """
    
    def __init__(self):
        num_peaks = rnd.randint(2, 4)
        
        self.peaks = []
        total_area = 0
        
        for i in range(num_peaks):
            retention_time = round(1.5 + i * 1.5 + rnd.uniform(0, 0.5), 1)
            peak_area = rnd.randint(20, 80)
            total_area += peak_area
            
            self.peaks.append({
                'name': f'Component {chr(65+i)}',
                'retention_time': retention_time,
                'area': peak_area
            })
        
        for peak in self.peaks:
            peak['percentage'] = round((peak['area'] / total_area) * 100, 1)
        
        self.questioned_peak = rnd.choice(self.peaks)
        self.answer = f"{self.questioned_peak['percentage']}%"
        
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
        ax.set_ylim(0, 10)
        
        ax.set_title('Gas Chromatogram', fontsize=16, fontweight='bold', pad=20)
        
        ax.set_xlabel('Retention Time (min)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Detector Response', fontsize=14, fontweight='bold')
        
        ax.plot([0, 10], [0, 0], 'k-', linewidth=2)
        
        for i, peak in enumerate(self.peaks):
            rt = peak['retention_time']
            area = peak['area']
            
            x = np.linspace(rt - 0.4, rt + 0.4, 100)
            height = area / 10
            y = height * np.exp(-((x - rt)**2) / (2 * 0.1**2))
            
            color = 'red' if peak == self.questioned_peak else 'blue'
            ax.plot(x, y, color=color, linewidth=2.5)
            ax.fill_between(x, 0, y, alpha=0.3, color=color)
            
            ax.text(rt, height + 0.5, peak['name'][10], fontsize=12, 
                   ha='center', fontweight='bold')
            ax.text(rt, -0.8, f"Area: {area}", fontsize=10, ha='center',
                   bbox=dict(boxstyle='round', facecolor='lightyellow' if color == 'red' else 'lightblue', 
                            pad=0.3))
        
        ax.set_ylim(-1.5, 10)
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem087:
    """
    Topic: 37.2 IR spectroscopy
    Visual: IR spectrum with characteristic peaks
    Task: Identify functional group from IR absorption
    """
    
    def __init__(self):
        absorptions = [
            ("O-H (alcohol)", 3300, 3500, "broad"),
            ("O-H (carboxylic acid)", 2500, 3300, "very broad"),
            ("C=O (carbonyl)", 1680, 1750, "strong"),
            ("C-O (ester/ether)", 1000, 1300, "strong"),
            ("N-H (amine)", 3300, 3500, "sharp")
        ]
        
        self.absorption = rnd.choice(absorptions)
        self.group = self.absorption[0]
        self.wavenumber_min = self.absorption[1]
        self.wavenumber_max = self.absorption[2]
        self.description_text = self.absorption[3]
        
        self.peak_position = rnd.randint(self.wavenumber_min, self.wavenumber_max)
        
        self.answer = self.group
        
        self.description = (
            f"The IR spectrum shows a {self.description_text} peak at {self.peak_position} cm⁻¹. "
            f"Which functional group is present?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "IR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Absorption at {self.peak_position} cm}}^{{-1}} &\\\\"
            f"\\text{{Characteristic of: {self.group}}} &\\\\"
            f"\\text{{Peak shape: {self.description_text}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        wavenumbers = np.linspace(4000, 400, 500)
        transmittance = np.ones_like(wavenumbers) * 80
        
        peak_idx = np.argmin(np.abs(wavenumbers - self.peak_position))
        peak_width = 50 if self.description_text == "sharp" else 150
        
        for i in range(len(wavenumbers)):
            if abs(wavenumbers[i] - self.peak_position) < peak_width:
                transmittance[i] = 10
        
        ax.plot(wavenumbers, transmittance, 'b-', linewidth=2)
        ax.fill_between(wavenumbers, transmittance, 100, alpha=0.3)
        
        ax.annotate(f'{self.peak_position} cm⁻¹', 
                   xy=(self.peak_position, 10), 
                   xytext=(self.peak_position, -10),
                   ha='center', fontsize=12, fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color='red', lw=2))
        
        ax.set_xlabel('Wavenumber (cm⁻¹)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Transmittance (%)', fontsize=14, fontweight='bold')
        ax.set_title('IR Spectrum', fontsize=16, fontweight='bold')
        ax.set_xlim(4000, 400)
        ax.set_ylim(0, 100)
        ax.invert_xaxis()
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem088:
    """
    Topic: 37.3 ¹H NMR spectroscopy
    Visual: NMR spectrum with chemical shifts
    Task: Assign peaks to hydrogen environments
    """
    
    def __init__(self):
        compounds = [
            ("ethanol", [(1.2, 3, "CH₃"), (3.7, 2, "CH₂"), (5.4, 1, "OH")]),
            ("propanone", [(2.1, 6, "CH₃")]),
            ("ethyl ethanoate", [(1.2, 3, "OCH₂CH₃"), (2.0, 3, "CH₃CO"), (4.1, 2, "OCH₂")])
        ]
        
        self.compound_data = rnd.choice(compounds)
        self.compound_name = self.compound_data[0]
        self.peaks = self.compound_data[1]
        
        selected_peak = rnd.choice(self.peaks)
        self.peak_shift = selected_peak[0]
        self.peak_integration = selected_peak[1]
        self.peak_assignment = selected_peak[2]
        
        self.answer = self.peak_assignment
        
        self.description = (
            f"The ¹H NMR spectrum of {self.compound_name} shows a peak at δ = {self.peak_shift} ppm. "
            f"Which hydrogen environment does this peak represent?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "¹H NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Chemical shift: }} \\delta = {self.peak_shift}\\text{{ ppm}} &\\\\"
            f"\\text{{Integration: {self.peak_integration}H}} &\\\\"
            f"\\text{{Assignment: {self.peak_assignment}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        for shift, integration, label in self.peaks:
            color = 'red' if shift == self.peak_shift else 'blue'
            draw_nmr_peak(ax, shift, integration, splitting='singlet',
                         max_height=100)
            
            if shift == self.peak_shift:
                ax.annotate(f'δ = {shift}', xy=(shift, 110), 
                           ha='center', fontsize=12, fontweight='bold',
                           color=color)
        
        ax.set_xlabel('Chemical shift δ (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        ax.set_title(f'¹H NMR Spectrum of {self.compound_name}', fontsize=16, fontweight='bold')
        ax.set_xlim(12, 0)
        ax.set_ylim(0, 120)
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem089:
    """
    Topic: 37.3 ¹H NMR spectroscopy
    """
    
    def __init__(self):
        molecules = [
            {
                'name': 'propanone',
                'formula': 'CH₃COCH₃',
                'num_peaks': 2,
                'environments': ['CH₃ (methyl)', 'C=O (carbonyl)'],
                'shifts': [30, 206]
            },
            {
                'name': 'ethanol',
                'formula': 'CH₃CH₂OH',
                'num_peaks': 2,
                'environments': ['CH₃', 'CH₂'],
                'shifts': [18, 58]
            },
            {
                'name': 'ethanoic acid',
                'formula': 'CH₃COOH',
                'num_peaks': 2,
                'environments': ['CH₃', 'COOH'],
                'shifts': [21, 178]
            },
            {
                'name': 'propan-2-ol',
                'formula': '(CH₃)₂CHOH',
                'num_peaks': 2,
                'environments': ['CH₃ (equivalent)', 'CH'],
                'shifts': [25, 64]
            }
        ]
        
        self.molecule = rnd.choice(molecules)
        self.answer = f"{self.molecule['num_peaks']} peaks"
        
        self.description = (
            f"The ¹³C NMR spectrum of {self.molecule['name']} is shown below. "
            f"How many peaks appear in the spectrum? "
            f"Identify the carbon environments responsible for each peak."
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "37.3 Carbon-13 NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.molecule['name']}}}&\\\\"
            f"\\text{{Number of peaks: {self.molecule['num_peaks']}}}&\\\\"
            + "\\\\".join([f"\\text{{Peak {i+1}: {env}}}" 
                          for i, env in enumerate(self.molecule['environments'])]) + "\\\\"
            "\\text{Each peak = one unique C environment}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(220, 0)
        ax.set_ylim(0, 120)
        
        ax.set_title(f'¹³C NMR Spectrum of {self.molecule["name"]}', 
                    fontsize=16, fontweight='bold', pad=20)
        
        ax.set_xlabel('Chemical shift δ (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        
        for i, (shift, env) in enumerate(zip(self.molecule['shifts'], self.molecule['environments'])):
            ax.plot([shift, shift], [0, 100], 'b-', linewidth=2.5)
            
            ax.text(shift, 105, f"δ = {shift}", fontsize=11, ha='center', fontweight='bold')
            ax.text(shift, -10, env, fontsize=10, ha='center', style='italic',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.3))
        
        ax.grid(True, alpha=0.3, axis='x')
        ax.set_yticks([])
        
        fig.text(0.5, 0.02, f"How many peaks? What carbon environments?", 
                fontsize=12, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem090:
    """
    Topic: 37.4 Combined spectroscopy
    """
    
    def __init__(self):
        molecules = [
            {
                'name': 'ethanol',
                'formula': 'CH₃CH₂OH',
                'key_group': 'CH₃',
                'neighbors': 2,
                'splitting': 'triplet',
                'shift': 1.2,
                'integration': 3
            },
            {
                'name': 'ethanol',
                'formula': 'CH₃CH₂OH',
                'key_group': 'CH₂',
                'neighbors': 3,
                'splitting': 'quartet',
                'shift': 3.7,
                'integration': 2
            },
            {
                'name': 'propanone',
                'formula': 'CH₃COCH₃',
                'key_group': 'CH₃',
                'neighbors': 0,
                'splitting': 'singlet',
                'shift': 2.1,
                'integration': 6
            }
        ]
        
        self.mol = rnd.choice(molecules)
        self.answer = f"{self.mol['splitting']} (n+1 rule: {self.mol['neighbors']}+1)"
        
        self.description = (
            f"The ¹H NMR spectrum of {self.mol['name']} shows a peak at δ = {self.mol['shift']} ppm "
            f"with integration of {self.mol['integration']}H. "
            f"This peak corresponds to the {self.mol['key_group']} group. "
            f"What is the splitting pattern of this peak? Use the n+1 rule."
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "37.4 Proton (¹H) NMR spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Group: {self.mol['key_group']}}}&\\\\"
            f"\\text{{Number of H on adjacent C: n = {self.mol['neighbors']}}}&\\\\"
            "\\text{n+1 rule: number of peaks} &= n + 1\\\\"
            f"&= {self.mol['neighbors']} + 1\\\\"
            f"&= {self.mol['neighbors'] + 1}\\\\"
            f"\\text{{Splitting pattern: {self.mol['splitting']}}}&"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        draw_nmr_peak(ax, self.mol['shift'], self.mol['integration'], 
                     splitting=self.mol['splitting'], max_height=100)
        
        ax.set_title(f'¹H NMR: {self.mol["name"]} - {self.mol["key_group"]} peak', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Chemical shift δ (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        ax.set_xlim(self.mol['shift'] + 1, self.mol['shift'] - 1)
        ax.set_ylim(0, 120)
        
        ax.text(self.mol['shift'], 110, f"Integration: {self.mol['integration']}H", 
               fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))
        
        ax.grid(True, alpha=0.3)
        
        fig.text(0.5, 0.02, f"Splitting pattern? (Apply n+1 rule)", 
                fontsize=12, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem091:
    """
    Topic: 37.4 Combined spectroscopy
    Visual: Multiple spectra for compound identification
    Task: Identify compound from combined spectroscopic data
    """
    
    def __init__(self):
        compounds = [
            ("ethanol", "C₂H₆O", 46, "IR: O-H, MS: 46, NMR: 3 peaks"),
            ("propanone", "C₃H₆O", 58, "IR: C=O, MS: 58, NMR: 1 peak"),
            ("ethanoic acid", "C₂H₄O₂", 60, "IR: O-H (broad), C=O, MS: 60, NMR: 2 peaks"),
            ("methyl methanoate", "C₂H₄O₂", 60, "IR: C=O, C-O, MS: 60, NMR: 2 peaks")
        ]
        
        self.compound = rnd.choice(compounds)
        self.name = self.compound[0]
        self.formula = self.compound[1]
        self.molar_mass = self.compound[2]
        self.spectral_data = self.compound[3]
        
        self.answer = self.name
        
        self.description = (
            f"Using the combined spectroscopic data shown, identify the compound. "
            f"Molecular formula: {self.formula}"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "Combined spectroscopy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecular formula: {self.formula}}} &\\\\"
            f"\\text{{Molar mass: {self.molar_mass}}} &\\\\"
            f"\\text{{Spectroscopic data: {self.spectral_data}}} &\\\\"
            f"\\text{{Compound: {self.name}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, f"Spectroscopic Data for {self.formula}", fontsize=16)
        
        table_data = [
            ["Technique", "Key Information"],
            ["Mass Spec", f"M+ = {self.molar_mass}"],
            ["IR Spec", self.spectral_data.split(", ")[0].replace("IR: ", "")],
            ["¹H NMR", self.spectral_data.split(", ")[2].replace("NMR: ", "")]
        ]
        
        draw_data_table(ax, table_data, start_x=2, start_y=6, 
                       cell_width=4, cell_height=0.8, header_color='lightblue')
        
        add_formula_label(ax, 6, 1.5, f"Identity: {self.name}", 
                         fontsize=16, weight='bold', color='green',
                         bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.8))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
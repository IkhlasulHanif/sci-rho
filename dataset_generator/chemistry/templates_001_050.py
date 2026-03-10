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

class Chem001:
    """
    Topic: 1.2 Isotopes / 1.1 Particles in the atom
    Visual: Mass spectrum showing isotope peaks
    Task: Calculate relative atomic mass from mass spectrum
    """
    
    def __init__(self):
        elements = [
            {"symbol": "Cl", "name": "chlorine", "isotopes": [(35, 75.77), (37, 24.23)]},
            {"symbol": "Cu", "name": "copper", "isotopes": [(63, 69.17), (65, 30.83)]},
            {"symbol": "Br", "name": "bromine", "isotopes": [(79, 50.69), (81, 49.31)]},
            {"symbol": "Ag", "name": "silver", "isotopes": [(107, 51.84), (109, 48.16)]},
            {"symbol": "Ga", "name": "gallium", "isotopes": [(69, 60.11), (71, 39.89)]},
            {"symbol": "B", "name": "boron", "isotopes": [(10, 19.9), (11, 80.1)]},
            {"symbol": "Li", "name": "lithium", "isotopes": [(6, 7.59), (7, 92.41)]},
        ]
        
        self.element = rnd.choice(elements)
        self.symbol = self.element["symbol"]
        self.name = self.element["name"]
        
        self.isotopes = []
        total_abundance = 0
        for i, (mass, abundance) in enumerate(self.element["isotopes"]):
            if i < len(self.element["isotopes"]) - 1:
                varied_abundance = round(abundance + rnd.uniform(-2, 2), 1)
                varied_abundance = max(1, min(99, varied_abundance))
            else:
                varied_abundance = round(100 - total_abundance, 1)
            self.isotopes.append((mass, varied_abundance))
            total_abundance += varied_abundance
        
        self.ar = sum(mass * (abundance / 100) for mass, abundance in self.isotopes)
        self.answer = round(self.ar, 2)
        
        self.description = (
            f"The mass spectrum of a sample of {self.name} is shown below. "
            f"Calculate the relative atomic mass of {self.name} to 2 decimal places."
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Isotopes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        isotope_calcs = []
        for mass, abundance in self.isotopes:
            isotope_calcs.append(
                f"^{{{mass}}}\\text{{{self.symbol}}}: {mass} \\times {round(abundance, 10)} &= {round(mass * abundance, 10)}"
            )
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The relative atomic mass is calculated using:}} &\\\\"
            f"A_r &= \\frac{{\\sum(\\text{{isotopic mass}} \\times \\text{{abundance}})}}{{100}}\\\\"
            f"\\text{{From the spectrum:}} &\\\\"
            + "\\\\".join(isotope_calcs) + "\\\\"
            f"\\text{{Sum}} &= {round(sum(mass * abundance for mass, abundance in self.isotopes), 10)}\\\\"
            f"A_r &= \\frac{{{round(sum(mass * abundance for mass, abundance in self.isotopes), 10)}}}{{100}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        for mass, abundance in self.isotopes:
            draw_mass_spectrum_peak(ax, mass, abundance, width=0.8, 
                                   color='black', label_offset=2)
        
        masses = [m for m, _ in self.isotopes]
        abundances = [a for _, a in self.isotopes]
        
        ax.set_xlabel('m/z (mass-to-charge ratio)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative abundance (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum of {self.name.capitalize()}', fontsize=16, fontweight='bold')
        
        ax.set_xlim(min(masses) - 3, max(masses) + 3)
        ax.set_ylim(0, max(abundances) + 15)
        ax.set_xticks(masses)
        
        ax.yaxis.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem002:
    """
    Topic: 1.4 Ionisation energy
    Visual: Graph of successive ionisation energies
    Task: Identify element from successive ionisation energy pattern
    """
    
    def __init__(self):
        elements_ie = {
            "Li": [520, 7298, 11815],
            "Be": [900, 1757, 14848, 21007],
            "B": [801, 2427, 3660, 25026, 32827],
            "C": [1086, 2353, 4621, 6223, 37831, 47277],
            "N": [1402, 2856, 4578, 7475, 9445, 53266, 64360],
            "Na": [496, 4562, 6910, 9543, 13354, 16613, 20117],
            "Mg": [738, 1451, 7733, 10543, 13630, 18020, 21711],
            "Al": [578, 1817, 2745, 11577, 14842, 18379, 23326],
            "Si": [786, 1577, 3232, 4356, 16091, 19805, 23780],
            "P": [1012, 1907, 2914, 4964, 6274, 21267, 25431],
            "S": [1000, 2252, 3357, 4556, 7004, 8496, 27107],
        }
        
        self.element = rnd.choice(list(elements_ie.keys()))
        self.ie_values = elements_ie[self.element]
        
        jumps = []
        for i in range(1, len(self.ie_values)):
            jump_ratio = self.ie_values[i] / self.ie_values[i-1]
            jumps.append((i, jump_ratio))
        
        max_jump_pos = max(jumps, key=lambda x: x[1])[0]
        self.outer_electrons = max_jump_pos
        
        group_map = {1: 1, 2: 2, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17}
        self.group = group_map.get(self.outer_electrons, self.outer_electrons)
        
        self.answer = self.group
        
        self.description = (
            f"The graph shows the successive ionisation energies of an element X. "
            f"Identify the group number of element X in the Periodic Table."
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Ionisation energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701 Past Papers"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Analysing the successive ionisation energies:}} &\\\\"
            f"\\text{{A large jump in IE indicates removal of an electron}} &\\\\"
            f"\\text{{from a shell closer to the nucleus.}} &\\\\"
            f"\\text{{The largest jump occurs between IE}}_{{{self.outer_electrons}}} \\text{{ and IE}}_{{{self.outer_electrons + 1}}} &\\\\"
            f"\\text{{This indicates {self.outer_electrons} electron(s) in the outer shell.}} &\\\\"
            f"\\text{{Therefore, the element is in Group {self.group}.}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        x_values = list(range(1, len(self.ie_values) + 1))
        
        ax.semilogy(x_values, self.ie_values, 'ko-', markersize=8, linewidth=2)
        
        for i, (x, y) in enumerate(zip(x_values, self.ie_values)):
            ax.annotate(f'{y}', xy=(x, y), xytext=(5, 5), 
                       textcoords='offset points', fontsize=10)
        
        ax.set_xlabel('Ionisation number', fontsize=14, fontweight='bold')
        ax.set_ylabel('Ionisation energy (kJ mol⁻¹)', fontsize=14, fontweight='bold')
        ax.set_title('Successive Ionisation Energies of Element X', fontsize=16, fontweight='bold')
        
        ax.set_xticks(x_values)
        ax.set_xticklabels([f'{i}' for i in x_values])
        
        ax.grid(True, which='both', linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem003:
    """
    Topic: 1.3 Electrons, energy levels, and atomic orbitals
    Visual: Orbital box diagram (electrons in boxes representation)
    Task: Identify the element or determine number of unpaired electrons
    """
    
    def __init__(self):
        elements = [
            {"symbol": "C", "Z": 6, "config": "1s² 2s² 2p²", "unpaired": 2,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 0, 0, 0, 0]}},
            {"symbol": "N", "Z": 7, "config": "1s² 2s² 2p³", "unpaired": 3,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 0, 1, 0, 1, 0]}},
            {"symbol": "O", "Z": 8, "config": "1s² 2s² 2p⁴", "unpaired": 2,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 0, 1, 0]}},
            {"symbol": "F", "Z": 9, "config": "1s² 2s² 2p⁵", "unpaired": 1,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 0]}},
            {"symbol": "Si", "Z": 14, "config": "1s² 2s² 2p⁶ 3s² 3p²", "unpaired": 2,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 1], "3s": [1, 1], "3p": [1, 1, 0, 0, 0, 0]}},
            {"symbol": "P", "Z": 15, "config": "1s² 2s² 2p⁶ 3s² 3p³", "unpaired": 3,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 1], "3s": [1, 1], "3p": [1, 0, 1, 0, 1, 0]}},
            {"symbol": "S", "Z": 16, "config": "1s² 2s² 2p⁶ 3s² 3p⁴", "unpaired": 2,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 1], "3s": [1, 1], "3p": [1, 1, 1, 0, 1, 0]}},
            {"symbol": "Cr", "Z": 24, "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁵ 4s¹", "unpaired": 6,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 1], "3s": [1, 1], "3p": [1, 1, 1, 1, 1, 1], 
                      "3d": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], "4s": [1, 0]}},
            {"symbol": "Fe", "Z": 26, "config": "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s²", "unpaired": 4,
             "boxes": {"1s": [1, 1], "2s": [1, 1], "2p": [1, 1, 1, 1, 1, 1], "3s": [1, 1], "3p": [1, 1, 1, 1, 1, 1], 
                      "3d": [1, 1, 1, 0, 1, 0, 1, 0, 1, 0], "4s": [1, 1]}},
        ]
        
        self.element = rnd.choice(elements)
        self.symbol = self.element["symbol"]
        self.Z = self.element["Z"]
        self.config = self.element["config"]
        self.unpaired = self.element["unpaired"]
        self.boxes = self.element["boxes"]
        
        self.question_type = rnd.choice(["unpaired", "element"])
        
        if self.question_type == "unpaired":
            self.answer = self.unpaired
            self.description = (
                f"The orbital box diagram below shows the electron configuration of an atom. "
                f"How many unpaired electrons does this atom have?"
            )
        else:
            self.answer = self.symbol
            self.description = (
                f"The orbital box diagram below shows the electron configuration of a neutral atom. "
                f"Identify the element."
            )
        
        self.topic = "Atomic structure"
        self.subtopic = "Electrons, energy levels, and atomic orbitals"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        if self.question_type == "unpaired":
            self.reasoning = (
                "\\[\\begin{aligned}"
                f"\\text{{The electron configuration is: }} {self.config} &\\\\"
                f"\\text{{Unpaired electrons are those not paired in the same orbital.}} &\\\\"
                f"\\text{{Counting from the diagram, there are {self.unpaired} unpaired electrons.}}"
                "\\end{aligned}\\]"
            )
        else:
            self.reasoning = (
                "\\[\\begin{aligned}"
                f"\\text{{Counting total electrons from the diagram:}} &\\\\"
                f"\\text{{Total electrons}} = {self.Z} &\\\\"
                f"\\text{{For a neutral atom, protons}} = \\text{{electrons}} = {self.Z} &\\\\"
                f"\\text{{Element with atomic number {self.Z} is {self.symbol}.}}"
                "\\end{aligned}\\]"
            )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        box_width = 0.6
        box_height = 0.8
        spacing = 0.1
        y_base = 3
        x_pos = 0.5
        
        for orbital, electrons in self.boxes.items():
            if orbital.endswith('s'):
                n_boxes = 1
            elif orbital.endswith('p'):
                n_boxes = 3
            elif orbital.endswith('d'):
                n_boxes = 5
            else:
                n_boxes = 1
            
            ax.text(x_pos + (n_boxes * (box_width + spacing)) / 2, y_base - 0.8, 
                orbital, ha='center', va='top', fontsize=14, fontweight='bold')
            
            for i in range(n_boxes):
                box_x = x_pos + i * (box_width + spacing)
                
                rect = patches.Rectangle((box_x, y_base), box_width, box_height, 
                                        linewidth=2, edgecolor='black', facecolor='white')
                ax.add_patch(rect)
                
                e_idx = i * 2
                up_electron = electrons[e_idx] if e_idx < len(electrons) else 0
                down_electron = electrons[e_idx + 1] if e_idx + 1 < len(electrons) else 0
                
                if up_electron:
                    ax.annotate('', xy=(box_x + box_width/3, y_base + box_height - 0.15),
                            xytext=(box_x + box_width/3, y_base + 0.15),
                            arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
                
                if down_electron:
                    ax.annotate('', xy=(box_x + 2*box_width/3, y_base + 0.15),
                            xytext=(box_x + 2*box_width/3, y_base + box_height - 0.15),
                            arrowprops=dict(arrowstyle='->', lw=2, color='red'))
            
            x_pos += n_boxes * (box_width + spacing) + 0.5
        
        add_title_box(ax, 7, 5.5, 'Orbital Box Diagram', fontsize=18)
        
        arrow_x = 0.2
        arrow_y_start = 1
        arrow_y_end = 5.5
        
        ax.annotate('', xy=(arrow_x, arrow_y_end), xytext=(arrow_x, arrow_y_start),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='gray'))
        
        ax.text(arrow_x - 0.8, (arrow_y_start + arrow_y_end) / 2, 'Energy', 
            rotation=90, va='center', ha='center', fontsize=16, 
            fontweight='bold', color='gray')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem004:
    """
    Topic: 1.1 Particles in the atom and atomic radius
    Visual: Diagram showing deflection of particles in an electric field
    Task: Identify which particle path corresponds to proton/neutron/electron
    """
    
    def __init__(self):
        particles = ["proton", "neutron", "electron"]
        rnd.shuffle(particles)
        
        self.path_assignments = dict(zip(['A', 'B', 'C'], particles))
        self.asked_particle = rnd.choice(particles)
        
        for path, particle in self.path_assignments.items():
            if particle == self.asked_particle:
                self.answer = path
                break
        
        self.description = (
            f"The diagram shows three beams of particles (A, B, and C) passing through an electric field "
            f"between two charged plates. All particles have the same initial velocity. "
            f"Which path corresponds to the beam of {self.asked_particle}s?"
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Particles in the atom and atomic radius"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        deflection_info = {
            "proton": "deflects towards negative plate (positive charge)",
            "neutron": "no deflection (no charge)",
            "electron": "deflects strongly towards positive plate (negative charge, small mass)"
        }
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{In an electric field:}} &\\\\"
            f"\\text{{- Protons: positive charge, deflect towards negative plate}} &\\\\"
            f"\\text{{- Neutrons: no charge, no deflection (straight path)}} &\\\\"
            f"\\text{{- Electrons: negative charge, deflect towards positive plate}} &\\\\"
            f"\\text{{  (Greater deflection due to smaller mass)}} &\\\\"
            f"\\text{{The {self.asked_particle} {deflection_info[self.asked_particle]}.}} &\\\\"
            f"\\text{{Therefore, the {self.asked_particle} follows path {self.answer}.}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        plate_length = 4
        plate_x_start = 4
        plate_x_end = plate_x_start + plate_length
        
        ax.plot([plate_x_start, plate_x_end], [8, 8], 'r-', linewidth=8)
        ax.text(plate_x_start - 0.5, 8, '+', fontsize=24, color='red', ha='center', va='center', fontweight='bold')
        ax.text(plate_x_end + 0.5, 8, '+', fontsize=24, color='red', ha='center', va='center', fontweight='bold')
        
        ax.plot([plate_x_start, plate_x_end], [2, 2], 'b-', linewidth=8)
        ax.text(plate_x_start - 0.5, 2, '−', fontsize=24, color='blue', ha='center', va='center', fontweight='bold')
        ax.text(plate_x_end + 0.5, 2, '−', fontsize=24, color='blue', ha='center', va='center', fontweight='bold')
        
        entry_x = 2
        entry_y = 5
        
        for path_label in ['A', 'B', 'C']:
            particle = self.path_assignments[path_label]
            
            if particle == "neutron":
                x_coords = [entry_x, 10]
                y_coords = [entry_y, entry_y]
                color = 'green'
            elif particle == "electron":
                x_coords = np.linspace(entry_x, 10, 100)
                y_coords = entry_y + 2.5 * ((x_coords - entry_x) / 8) ** 2
                color = 'purple'
            else:
                x_coords = np.linspace(entry_x, 10, 100)
                y_coords = entry_y - 1.2 * ((x_coords - entry_x) / 8) ** 2
                color = 'orange'
            
            ax.plot(x_coords, y_coords, color=color, linewidth=2.5)
            
            if isinstance(x_coords, np.ndarray):
                end_x, end_y = x_coords[-1], y_coords[-1]
            else:
                end_x, end_y = x_coords[-1], y_coords[-1]
            
            ax.text(end_x + 0.3, end_y, path_label, fontsize=16, fontweight='bold', 
                   va='center', ha='left')
        
        draw_arrow(ax, 0.5, entry_y, entry_x, entry_y, arrowstyle='->', 
                  color='black', linewidth=2, mutation_scale=20)
        ax.text(0.5, entry_y + 0.5, 'Beam of\nparticles', fontsize=12, ha='center')
        
        for x in np.linspace(plate_x_start + 0.5, plate_x_end - 0.5, 4):
            ax.annotate('', xy=(x, 2.5), xytext=(x, 7.5),
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray', alpha=0.5))
        ax.text((plate_x_start + plate_x_end) / 2, 5, 'E', fontsize=14, 
               ha='center', va='center', color='gray', style='italic')
        
        ax.set_title('Deflection of Particles in an Electric Field', fontsize=16, pad=20)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem005:
    """
    Topic: 1.4 Ionisation energy
    Visual: Graph showing first ionisation energy trend across a period
    Task: Explain anomaly or identify element at a specific position
    """
    
    def __init__(self):
        period_data = {
            2: {
                "elements": ["Li", "Be", "B", "C", "N", "O", "F", "Ne"],
                "IE": [520, 900, 801, 1086, 1402, 1314, 1681, 2081]
            },
            3: {
                "elements": ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"],
                "IE": [496, 738, 578, 786, 1012, 1000, 1251, 1521]
            }
        }
        
        self.period = rnd.choice([2, 3])
        self.elements = period_data[self.period]["elements"]
        self.IE_values = period_data[self.period]["IE"]
        
        if self.period == 2:
            anomaly_elements = ["B", "O"]
            anomaly_explanations = {
                "B": "2p¹ electron is in a higher energy sub-shell than 2s², requiring less energy to remove",
                "O": "2p⁴ has electron pairing in one 2p orbital, causing repulsion that makes removal easier"
            }
        else:
            anomaly_elements = ["Al", "S"]
            anomaly_explanations = {
                "Al": "3p¹ electron is in a higher energy sub-shell than 3s², requiring less energy to remove",
                "S": "3p⁴ has electron pairing in one 3p orbital, causing repulsion that makes removal easier"
            }

        self.anomaly_element = rnd.choice(anomaly_elements)
        self.explanation = anomaly_explanations[self.anomaly_element]

        anomaly_idx = self.elements.index(self.anomaly_element)
        self.prev_element = self.elements[anomaly_idx - 1]
        
        self.answer = self.explanation
        
        self.description = (
            f"The graph shows the first ionisation energies of the elements in Period {self.period}. "
            f"Explain why the first ionisation energy of {self.anomaly_element} is lower than "
            f"that of {self.prev_element}."
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Ionisation energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701 Past Papers"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{General trend: IE increases across a period due to:}} &\\\\"
            f"\\text{{- Increasing nuclear charge}} &\\\\"
            f"\\text{{- Decreasing atomic radius}} &\\\\"
            f"\\text{{- Similar shielding (same shell)}} &\\\\"
            f"\\text{{Anomaly at {self.anomaly_element}:}} &\\\\"
            f"\\text{{{self.explanation}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        x_values = list(range(1, len(self.elements) + 1))
        
        ax.plot(x_values, self.IE_values, 'ko-', markersize=10, linewidth=2)
        
        for i, (x, y, elem) in enumerate(zip(x_values, self.IE_values, self.elements)):
            ax.annotate(elem, xy=(x, y), xytext=(0, 15), 
                       textcoords='offset points', fontsize=12, ha='center', fontweight='bold')
        
        anomaly_idx = self.elements.index(self.anomaly_element)
        ax.plot(x_values[anomaly_idx], self.IE_values[anomaly_idx], 'ro', markersize=15, 
               fillstyle='none', linewidth=3)
        
        ax.set_xlabel('Atomic number', fontsize=14, fontweight='bold')
        ax.set_ylabel('First ionisation energy (kJ mol⁻¹)', fontsize=14, fontweight='bold')
        ax.set_title(f'First Ionisation Energies Across Period {self.period}', fontsize=16, fontweight='bold')
        
        ax.set_xticks(x_values)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_axisbelow(True)
        ax.set_ylim(0, max(self.IE_values) * 1.15)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem006:
    """
    Topic: Electronic Configuration - Energy Level Diagrams
    Visual: Perfectly aligned electron configuration diagram
    Task: Determine atomic number from electron arrangement
    """
    
    def __init__(self):
        self.atomic_number = rnd.randint(11, 36)
        self.config = self._get_electron_config(self.atomic_number)
        self.answer = f"{self.atomic_number}"
        
        self.description = (
            f"The diagram shows the arrangement of electrons in an atom. "
            f"Determine the atomic number of this element."
        )
        
        self.topic = "Atomic Structure"
        self.subtopic = "Electronic Configuration"
        self.source = "Adapted from Cambridge International AS & A Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        config_lines = []
        for orbital in ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p']:
            if orbital in self.config:
                config_lines.append(f"\\text{{{orbital}}} &: {self.config[orbital]}\\text{{ electrons}}\\\\")
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Count the total number of electrons shown in the diagram:}} &\\\\"
            + "".join(config_lines)
            + f"\\text{{Total electrons}} &= {self.atomic_number}\\\\"
            f"\\text{{For a neutral atom, atomic number equals number of electrons.}} &\\\\"
            f"\\text{{Therefore, atomic number}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def _get_electron_config(self, atomic_num):
        config = {}
        remaining = atomic_num
        
        orbitals = [
            ('1s', 2), ('2s', 2), ('2p', 6), ('3s', 2), ('3p', 6),
            ('4s', 2), ('3d', 10), ('4p', 6)
        ]
        
        for orbital, max_electrons in orbitals:
            if remaining > 0:
                electrons = min(remaining, max_electrons)
                config[orbital] = electrons
                remaining -= electrons
            else:
                break
        
        return config
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        LEVEL_SPACING = 1.5
        BOX_WIDTH = 0.7
        BOX_HEIGHT = 0.5
        BOX_HORIZONTAL_SPACING = 0.9
        
        ARROW_WIDTH = 0.12
        ARROW_OFFSET = 0.15
        ARROW_HEIGHT = 0.2
        
        START_Y = 1.0
        BOX_START_X = 3.0
        LABEL_X = 8.5
        
        orbital_sequence = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p']
        
        y_positions = {}
        current_y = START_Y
        for orbital in orbital_sequence:
            y_positions[orbital] = current_y
            current_y += LEVEL_SPACING
        
        orbitals_present = []
        
        for orbital in orbital_sequence:
            if orbital not in self.config:
                continue
                
            orbitals_present.append(orbital)
            y_pos = y_positions[orbital]
            num_electrons = self.config[orbital]
            
            if orbital.endswith('s'):
                num_boxes = 1
            elif orbital.endswith('p'):
                num_boxes = 3
            elif orbital.endswith('d'):
                num_boxes = 5
            else:
                num_boxes = 1
            
            for box_idx in range(num_boxes):
                box_x = BOX_START_X + (box_idx * BOX_HORIZONTAL_SPACING)
                
                rect = patches.Rectangle(
                    (box_x, y_pos - BOX_HEIGHT/2), 
                    BOX_WIDTH, BOX_HEIGHT,
                    linewidth=2, 
                    edgecolor='black', 
                    facecolor='none'
                )
                ax.add_patch(rect)
            
            electrons_placed = 0
            
            for box_idx in range(min(num_boxes, num_electrons)):
                box_x = BOX_START_X + (box_idx * BOX_HORIZONTAL_SPACING)
                box_center_x = box_x + BOX_WIDTH / 2
                arrow_x = box_center_x - ARROW_OFFSET
                
                ax.arrow(arrow_x, y_pos - ARROW_HEIGHT/2, 0, ARROW_HEIGHT,
                        head_width=ARROW_WIDTH, head_length=0.08,
                        fc='blue', ec='blue', linewidth=1.5)
                electrons_placed += 1
            
            box_idx = 0
            while electrons_placed < num_electrons and box_idx < num_boxes:
                box_x = BOX_START_X + (box_idx * BOX_HORIZONTAL_SPACING)
                box_center_x = box_x + BOX_WIDTH / 2
                arrow_x = box_center_x + ARROW_OFFSET
                
                ax.arrow(arrow_x, y_pos + ARROW_HEIGHT/2, 0, -ARROW_HEIGHT,
                        head_width=ARROW_WIDTH, head_length=0.08,
                        fc='red', ec='red', linewidth=1.5)
                electrons_placed += 1
                box_idx += 1
            
            ax.text(LABEL_X, y_pos, orbital, 
                   fontsize=18, ha='left', va='center', fontweight='bold')

        if orbitals_present:
            min_y = y_positions[orbitals_present[0]] - 1.0
            max_y = y_positions[orbitals_present[-1]] + 1.0
        else:
            min_y = 0
            max_y = 10
        
        ax.set_xlim(1.5, LABEL_X + 1.5)
        ax.set_ylim(min_y, max_y)

        arrow_x = 2.3
        arrow_y_start = min_y + 1
        arrow_y_end = max_y - 1
        
        ax.annotate('', xy=(arrow_x, arrow_y_end), xytext=(arrow_x, arrow_y_start),
                   arrowprops=dict(arrowstyle='->', lw=2.5, color='black'))

        ax.text(arrow_x - 0.5, (arrow_y_start + arrow_y_end) / 2, 'Energy', 
               rotation=90, va='center', ha='center', fontsize=16, fontweight='bold')

        ax.set_aspect('equal')
        ax.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=150, pad_inches=0.3)
        plt.close()

class Chem007:
    """
    Chapter 2.1: Relative masses (Ar calculation from mass spectrum)
    """
    
    def __init__(self):
        self.element_choices = [
            {'name': 'Chlorine', 'isotopes': [(35, 75.8), (37, 24.2)]},
            {'name': 'Boron', 'isotopes': [(10, 19.9), (11, 80.1)]},
            {'name': 'Copper', 'isotopes': [(63, 69.2), (65, 30.8)]},
            {'name': 'Bromine', 'isotopes': [(79, 50.7), (81, 49.3)]},
        ]
        
        self.element = rnd.choice(self.element_choices)
        self.isotopes = self.element['isotopes']
        
        total = sum(mass * abundance for mass, abundance in self.isotopes)
        self.answer = round(total / 100, 2)
        
        self.description = (
            f"The mass spectrum of {self.element['name']} is shown in the diagram. "
            f"Calculate the relative atomic mass (Ar) of {self.element['name']}."
        )
        
        self.topic = "Atoms, molecules and stoichiometry"
        self.subtopic = "Relative masses"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701 past papers"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Relative atomic mass is calculated using:}} &\\\\"
            "\\text{Ar} &= \\frac{\\sum (\\text{isotope mass} \\times \\text{\\% abundance})}{100}\\\\"
        )
        
        for i, (mass, abundance) in enumerate(self.isotopes):
            if i == 0:
                self.reasoning += f"&= \\frac{{({mass} \\times {abundance})"
            else:
                self.reasoning += f" + ({mass} \\times {abundance})"
        
        self.reasoning += "}{100}\\\\"
        
        sum_products = sum(mass * abundance for mass, abundance in self.isotopes)
        self.reasoning += (
            f"&= \\frac{{{round(sum_products, 2)}}}{{100}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        for mass, abundance in self.isotopes:
            draw_mass_spectrum_peak(ax, mass, abundance, width=0.8, 
                                   color='darkblue')
        
        ax.set_xlabel('m/z (mass-to-charge ratio)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative Intensity (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum of {self.element["name"]}', 
                    fontsize=16, fontweight='bold')
        
        masses = [iso[0] for iso in self.isotopes]
        ax.set_xlim(min(masses) - 2, max(masses) + 2)
        ax.set_ylim(0, 110)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem008:
    """
    Chapter 2.3: Empirical formula from pie chart
    """
    
    def __init__(self):
        compound_choices = [
            {'formula': 'C₂H₆O', 'elements': {'C': 52.1, 'H': 13.1, 'O': 34.8}},
            {'formula': 'CH₄O', 'elements': {'C': 37.5, 'H': 12.5, 'O': 50.0}},
            {'formula': 'C₃H₈', 'elements': {'C': 81.8, 'H': 18.2}},
        ]
        
        self.compound = rnd.choice(compound_choices)
        self.elements = self.compound['elements']
        self.answer = self.compound['formula']
        
        self.description = (
            "The pie chart shows the percentage composition by mass of a compound. "
            "Determine the empirical formula."
        )
        
        self.topic = "Atoms, molecules and stoichiometry"
        self.subtopic = "Chemical formulae"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        atomic_masses = {'C': 12, 'H': 1, 'O': 16, 'N': 14}
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Step 1: Convert mass percentages to moles} &\\\\"
        )
        
        moles = {}
        for elem, percent in self.elements.items():
            mole = percent / atomic_masses[elem]
            moles[elem] = mole
            self.reasoning += f"\\text{{Moles of {elem}}} &= \\frac{{{percent}}}{{{atomic_masses[elem]}}} = {round(mole, 3)}\\\\"
        
        min_moles = min(moles.values())
        
        self.reasoning += "\\text{Step 2: Divide by smallest number of moles} &\\\\"
        
        for elem, mole in moles.items():
            ratio = mole / min_moles
            self.reasoning += f"\\text{{Ratio of {elem}}} &= \\frac{{{round(mole, 3)}}}{{{round(min_moles, 3)}}} = {round(ratio, 1)}\\\\"
        
        self.reasoning += (
            f"\\text{{Empirical formula}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
        labels = list(self.elements.keys())
        sizes = list(self.elements.values())
        
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                           colors=colors[:len(labels)],
                                           startangle=90, textprops={'fontsize': 14, 'fontweight': 'bold'})
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Elemental Composition by Mass (%)', fontsize=16, fontweight='bold')
        
        legend_y = 0.6
        for i, (elem, percent) in enumerate(self.elements.items()):
            draw_labeled_box(ax, -1.8, legend_y - i*0.3, 0.4, 0.2, '', 
                           facecolor=colors[i], edgecolor='black')
            ax.text(-1.2, legend_y - i*0.3 + 0.1, f'{elem}: {percent}%', 
                   fontsize=12, ha='left', va='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem009:
    """
    Chapter 2.4: Limiting reagent calculation
    """
    
    def __init__(self):
        reactions = [
            {'equation': '2H₂ + O₂ → 2H₂O', 'reactants': ['H₂', 'O₂'], 'stoich': [2, 1]},
            {'equation': 'N₂ + 3H₂ → 2NH₃', 'reactants': ['N₂', 'H₂'], 'stoich': [1, 3]},
            {'equation': 'C + O₂ → CO₂', 'reactants': ['C', 'O₂'], 'stoich': [1, 1]},
        ]
        
        self.reaction = rnd.choice(reactions)
        self.moles = [rnd.uniform(0.5, 3.0) for _ in self.reaction['reactants']]
        
        ratios = [m / s for m, s in zip(self.moles, self.reaction['stoich'])]
        limiting_idx = ratios.index(min(ratios))
        self.answer = self.reaction['reactants'][limiting_idx]
        
        self.description = (
            f"The balanced equation is: {self.reaction['equation']}. "
            f"Initial moles are shown in the diagram. Identify the limiting reagent."
        )
        
        self.topic = "Atoms, molecules and stoichiometry"
        self.subtopic = "Stoichiometric relationships"
        self.source = "Original"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Balanced equation: {self.reaction['equation']}}} &\\\\"
            "\\text{Determine limiting reagent by comparing mole ratios:} &\\\\"
        )
        
        for i, (reactant, mole, stoich) in enumerate(zip(self.reaction['reactants'], 
                                                         self.moles, self.reaction['stoich'])):
            ratio = mole / stoich
            self.reasoning += (
                f"\\text{{For {reactant}: }} \\frac{{{round(mole, 2)}}}{{{stoich}}} &= {round(ratio, 3)}\\\\"
            )
        
        self.reasoning += (
            f"\\text{{Smallest ratio indicates limiting reagent: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5, self.reaction['equation'], fontsize=14)
        
        x_positions = [1.5, 4]
        for i, (reactant, mole) in enumerate(zip(self.reaction['reactants'], self.moles)):
            draw_labeled_box(ax, x_positions[i]-0.8, 2, 1.6, 1.2, 
                        reactant, f'{round(mole, 2)} mol', 
                        facecolor='lightblue',
                        edgecolor='black', linewidth=2)
        
        ax.text(2.8, 2.6, '+', fontsize=20, ha='center', fontweight='bold')
        
        draw_arrow(ax, 5.5, 2.6, 7, 2.6, arrowstyle='->', color='black', linewidth=2)
        
        product_formula = self.reaction['equation'].split('→')[1].strip()
        draw_labeled_box(ax, 8.5, 2, 1.6, 1.2, 
                    product_formula, '? mol', 
                    facecolor='lightgreen',
                    edgecolor='black', linewidth=2)
        
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem010:
    """
    Chapter 3.2: Polar bonds with electronegativity
    Visual: Diatomic molecule with EN values shown; student identifies which atom bears δ-
    Answer: A/B/C/D (multiple choice)
    """
    
    def __init__(self):
        self.molecules = [
            {'name': 'HCl', 'atoms': ['H', 'Cl'], 'EN': [2.1, 3.0]},
            {'name': 'HF',  'atoms': ['H', 'F'],  'EN': [2.1, 4.0]},
            {'name': 'HBr', 'atoms': ['H', 'Br'], 'EN': [2.1, 2.8]},
            {'name': 'HI',  'atoms': ['H', 'I'],  'EN': [2.1, 2.5]},
            {'name': 'CO',  'atoms': ['C', 'O'],  'EN': [2.5, 3.4]},
            {'name': 'NO',  'atoms': ['N', 'O'],  'EN': [3.0, 3.4]},
            {'name': 'ClF', 'atoms': ['Cl', 'F'], 'EN': [3.0, 4.0]},
            {'name': 'BrCl','atoms': ['Br', 'Cl'],'EN': [2.8, 3.0]},
            {'name': 'ICl', 'atoms': ['I', 'Cl'], 'EN': [2.5, 3.0]},
            {'name': 'BrF', 'atoms': ['Br', 'F'], 'EN': [2.8, 4.0]},
            {'name': 'NF',  'atoms': ['N', 'F'],  'EN': [3.0, 4.0]},
            {'name': 'PH',  'atoms': ['P', 'H'],  'EN': [2.1, 2.1]},
        ]
        
        self.molecule = rnd.choice(self.molecules)
        self.delta_EN = round(abs(self.molecule['EN'][1] - self.molecule['EN'][0]), 1)

        # Determine correct answer: atom with higher EN bears δ-
        atom0, atom1 = self.molecule['atoms']
        en0, en1 = self.molecule['EN']
        if en0 == en1:
            correct = f"Neither (non-polar bond, ΔEN = 0)"
        elif en1 > en0:
            correct = atom1  # atom1 (right) is δ-
        else:
            correct = atom0  # atom0 (left) is δ-

        # Build 4 MC options
        # Correct answer plus distractors
        options_pool = [
            correct,
            atom0 if correct != atom0 else atom1,
            f"Both equally (non-polar)",
            f"Neither (covalent bond has no polarity)",
        ]
        # Shuffle and assign letters
        rnd.shuffle(options_pool)
        self.options = options_pool[:4]
        self.correct_letter = chr(65 + self.options.index(correct))  # A/B/C/D
        self.answer = self.correct_letter

        self.description = (
            f"The diagram shows the {self.molecule['name']} molecule with electronegativity (EN) values. "
            f"Which atom carries the δ− (partial negative) charge?\n"
            f"A. {self.options[0]}   B. {self.options[1]}   C. {self.options[2]}   D. {self.options[3]}"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Electronegativity and bond polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Electronegativity of {atom0}}} &= {en0}\\\\"
            f"\\text{{Electronegativity of {atom1}}} &= {en1}\\\\"
            f"\\Delta EN &= |{en1} - {en0}| = {self.delta_EN}\\\\"
            f"\\text{{Higher EN atom attracts electrons more:}} &\\\\"
            f"\\text{{δ- on {correct} (higher EN)}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7, f'{self.molecule["name"]} Molecule', fontsize=16)
        
        x1, y1 = 3, 4
        x2, y2 = 7, 4
        
        draw_circle_atom(ax, x1, y1, self.molecule['atoms'][0], 
                        radius=0.5, color='lightblue', text_color='black')
        draw_circle_atom(ax, x2, y2, self.molecule['atoms'][1], 
                        radius=0.5, color='lightcoral', text_color='black')
        
        draw_bond(ax, x1+0.5, y1, x2-0.5, y2, bond_type='single', linewidth=4)
        
        # Show only EN values — NO δ+/δ- labels
        ax.text(x1, y1-0.9, f'EN = {self.molecule["EN"][0]}', 
               fontsize=12, ha='center', fontweight='bold')
        ax.text(x2, y2-0.9, f'EN = {self.molecule["EN"][1]}', 
               fontsize=12, ha='center', fontweight='bold')
        
        ax.text(5, 2.2, 'Which atom carries δ− ?', fontsize=13, ha='center',
               fontweight='bold', color='navy',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='navy'))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem011:
    """
    Chapter 3.3: 3D tetrahedral structure (CH₄)
    """
    
    def __init__(self):
        self.molecule = 'CH₄'
        self.bond_angle = 109.5
        self.shape = 'Tetrahedral'
        self.answer = f'{self.bond_angle}°'
        
        self.description = (
            f"The 3D structure of {self.molecule} is shown. "
            f"State the H-C-H bond angle."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Shapes of molecules (VSEPR)"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: {self.molecule}}} &\\\\"
            "\\text{Central atom: C with 4 bonding pairs, 0 lone pairs} &\\\\"
            f"\\text{{VSEPR shape: {self.shape}}} &\\\\"
            f"\\text{{Bond angle}} &= {self.bond_angle}°"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        central = np.array([0, 0, 0])
        
        angle = np.radians(109.5)
        r = 1.5
        
        h_positions = [
            np.array([r, 0, 0]),
            np.array([-r*np.cos(angle), r*np.sin(angle), 0]),
            np.array([-r*np.cos(angle), -r*np.sin(angle)*np.cos(np.pi/3), r*np.sin(angle)*np.sin(np.pi/3)]),
            np.array([-r*np.cos(angle), -r*np.sin(angle)*np.cos(np.pi/3), -r*np.sin(angle)*np.sin(np.pi/3)]),
        ]
        
        atom_positions = [central] + h_positions
        bonds = [(0, 1), (0, 2), (0, 3), (0, 4)]
        labels = ['C'] + ['H'] * 4
        colors = ['black'] + ['lightblue'] * 4
        
        draw_3d_molecule(ax, atom_positions, bonds, labels=labels, 
                        atom_colors=colors, radius=0.3)
        
        ax.text(0, 0, -2.5, 'Identify the bond angle from this 3D structure', fontsize=11, 
               ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))
        
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-3, 2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem012:
    """
    Chapter 3.3: 3D trigonal pyramidal (NH₃)
    """
    
    def __init__(self):
        self.molecule = 'NH₃'
        self.bond_angle = 107
        self.shape = 'Trigonal Pyramidal'
        self.answer = f'{self.bond_angle}°'
        
        self.description = (
            f"The 3D structure of {self.molecule} is shown with one lone pair. "
            f"State the H-N-H bond angle."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Shapes of molecules (VSEPR)"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: {self.molecule}}} &\\\\"
            "\\text{Central atom: N with 3 bonding pairs, 1 lone pair} &\\\\"
            f"\\text{{VSEPR shape: {self.shape}}} &\\\\"
            "\\text{Lone pair repulsion reduces bond angle from 109.5° to:} &\\\\"
            f"\\text{{Bond angle}} &\\approx {self.bond_angle}°"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        central = np.array([0, 0, 0])
        r = 1.5
        
        h_positions = [
            np.array([r, 0, -0.3]),
            np.array([-r*np.cos(np.radians(120)), r*np.sin(np.radians(120)), -0.3]),
            np.array([-r*np.cos(np.radians(120)), -r*np.sin(np.radians(120)), -0.3]),
        ]
        
        lone_pair_pos = np.array([0, 0, 1.2])
        
        atom_positions = [central] + h_positions
        bonds = [(0, 1), (0, 2), (0, 3)]
        labels = ['N'] + ['H'] * 3
        colors = ['blue'] + ['lightblue'] * 3
        
        draw_3d_molecule(ax, atom_positions, bonds, labels=labels, 
                        atom_colors=colors, radius=0.3)
        
        ax.plot([central[0], lone_pair_pos[0]], 
               [central[1], lone_pair_pos[1]], 
               [central[2], lone_pair_pos[2]], 
               'r--', linewidth=2, alpha=0.5)
        ax.text(lone_pair_pos[0], lone_pair_pos[1], lone_pair_pos[2]+0.2, 
               'Lone\nPair', fontsize=11, ha='center', color='red', fontweight='bold')
        
        ax.text(0, 0, -2.5, 'Identify the bond angle from this 3D structure', fontsize=11, 
               ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))
        
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-3, 2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem013:
    """
    Chapter 3.3: 3D bent structure (H₂O)
    """
    
    def __init__(self):
        self.molecule = 'H₂O'
        self.bond_angle = 104.5
        self.shape = 'Bent (V-shaped)'
        self.answer = f'{self.bond_angle}°'
        
        self.description = (
            f"The 3D structure of {self.molecule} is shown with two lone pairs. "
            f"State the H-O-H bond angle."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Shapes of molecules (VSEPR)"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecule: {self.molecule}}} &\\\\"
            "\\text{Central atom: O with 2 bonding pairs, 2 lone pairs} &\\\\"
            f"\\text{{VSEPR shape: {self.shape}}} &\\\\"
            "\\text{Two lone pairs cause greater repulsion:} &\\\\"
            f"\\text{{Bond angle}} &\\approx {self.bond_angle}°"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        central = np.array([0, 0, 0])
        angle = np.radians(104.5)
        r = 1.5
        
        h_positions = [
            np.array([r*np.sin(angle/2), 0, -r*np.cos(angle/2)]),
            np.array([-r*np.sin(angle/2), 0, -r*np.cos(angle/2)]),
        ]
        
        lone_pair_pos1 = np.array([0.7, 0, 1.0])
        lone_pair_pos2 = np.array([-0.7, 0, 1.0])
        
        atom_positions = [central] + h_positions
        bonds = [(0, 1), (0, 2)]
        labels = ['O'] + ['H'] * 2
        colors = ['red'] + ['lightblue'] * 2
        
        draw_3d_molecule(ax, atom_positions, bonds, labels=labels, 
                        atom_colors=colors, radius=0.3)
        
        for lp_pos in [lone_pair_pos1, lone_pair_pos2]:
            ax.plot([central[0], lp_pos[0]], 
                   [central[1], lp_pos[1]], 
                   [central[2], lp_pos[2]], 
                   'r--', linewidth=2, alpha=0.5)
        
        ax.text(0, 0, 1.5, 'Lone Pairs', fontsize=11, ha='center', 
               color='red', fontweight='bold')
        
        ax.text(0, 0, -2.5, 'Identify the bond angle from this 3D structure', fontsize=11, 
               ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))
        
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-3, 2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem014:
    """
    Chapter 3.4: Hydrogen bonding in water/HF/ammonia
    Visual: Diagram showing dashed hydrogen bond lines between molecules
    Task: MC — identify IMF type, requirements, or effect
    Answer: A/B/C/D
    """
    
    def __init__(self):
        molecules_data = [
            {'name': 'water', 'formula': 'H₂O', 'donor': 'O–H', 'acceptor': 'O lone pair'},
            {'name': 'hydrogen fluoride', 'formula': 'HF', 'donor': 'F–H', 'acceptor': 'F lone pair'},
            {'name': 'ammonia', 'formula': 'NH₃', 'donor': 'N–H', 'acceptor': 'N lone pair'},
        ]
        
        questions = [
            {
                'q': "What type of intermolecular force is shown as dashed lines?",
                'correct': 'Hydrogen bonding',
                'wrong': ['Van der Waals (London dispersion) forces', 'Ionic bonding',
                          'Permanent dipole–dipole forces'],
            },
            {
                'q': "Which element must be directly bonded to hydrogen for this interaction to occur?",
                'correct': 'Nitrogen, Oxygen, or Fluorine (N, O, or F)',
                'wrong': ['Carbon, Oxygen, or Chlorine', 'Any electronegative element',
                          'Oxygen only'],
            },
            {
                'q': "What feature on the acceptor molecule is involved in hydrogen bonding?",
                'correct': 'A lone pair of electrons on a highly electronegative atom',
                'wrong': ['A positive charge on the atom', 'A free radical on the atom',
                          'A double bond'],
            },
            {
                'q': "How is a hydrogen bond represented in diagrams?",
                'correct': 'A dashed line between molecules',
                'wrong': ['A solid line between atoms', 'A wavy arrow',
                          'A double line between atoms'],
            },
            {
                'q': "Why does water have an unusually high boiling point compared to H₂S?",
                'correct': 'Water molecules form hydrogen bonds which require more energy to break',
                'wrong': ['Water molecules are smaller', 'Water has stronger covalent bonds',
                          'Water has more electron pairs'],
            },
            {
                'q': "What partial charge does the hydrogen atom carry in a hydrogen bond donor?",
                'correct': 'δ+ (partial positive)',
                'wrong': ['δ– (partial negative)', 'No partial charge',
                          'Full positive charge (+1)'],
            },
            {
                'q': "Which of the following can form hydrogen bonds with itself?",
                'correct': 'H₂O',
                'wrong': ['CH₄', 'H₂S', 'CCl₄'],
            },
            {
                'q': "How many hydrogen bonds can one water molecule typically form?",
                'correct': 'Up to 4 (2 as donor, 2 as acceptor)',
                'wrong': ['Up to 2 (1 donor, 1 acceptor)', 'Up to 6', 'Exactly 1'],
            },
            {
                'q': "Which of the following cannot form hydrogen bonds with water?",
                'correct': 'CH₄',
                'wrong': ['NH₃', 'HF', 'C₂H₅OH'],
            },
            {
                'q': "Which property is mainly explained by hydrogen bonding in water?",
                'correct': 'Ice being less dense than liquid water',
                'wrong': ['Water being transparent', 'Water having high density',
                          'Water being a good electrical conductor'],
            },
        ]
        
        self.mol_data = rnd.choice(molecules_data)
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows hydrogen bonding between {self.mol_data['name']} molecules "
            f"(dashed lines represent the interaction). "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Hydrogen bonding requires:} &\\\\"
            "\\text{1. H bonded to highly electronegative atom (N, O, or F)} &\\\\"
            "\\text{2. Lone pair on electronegative atom of adjacent molecule} &\\\\"
            "\\text{Shown by dashed lines in structural diagrams} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, 'Hydrogen Bonding in Water', fontsize=16)
        
        molecules = [
            {'O': (2, 4), 'H1': (1, 3.3), 'H2': (3, 3.3)},
            {'O': (6, 5), 'H1': (5, 4.3), 'H2': (7, 4.3)},
            {'O': (10, 4), 'H1': (9, 3.3), 'H2': (11, 3.3)},
        ]
        
        for mol in molecules:
            draw_circle_atom(ax, mol['O'][0], mol['O'][1], 'O', 
                           radius=0.4, color='red', text_color='white')
            draw_circle_atom(ax, mol['H1'][0], mol['H1'][1], 'H', 
                           radius=0.25, color='lightblue', text_color='black')
            draw_circle_atom(ax, mol['H2'][0], mol['H2'][1], 'H', 
                           radius=0.25, color='lightblue', text_color='black')
            
            draw_bond(ax, mol['O'][0], mol['O'][1], mol['H1'][0], mol['H1'][1], 
                     bond_type='single', linewidth=3)
            draw_bond(ax, mol['O'][0], mol['O'][1], mol['H2'][0], mol['H2'][1], 
                     bond_type='single', linewidth=3)
            
            add_charge_label(ax, mol['O'][0], mol['O'][1]+0.6, 'δ-', 
                           fontsize=12, color='red')
            add_charge_label(ax, mol['H1'][0], mol['H1'][1]-0.5, 'δ+', 
                           fontsize=10, color='blue')
            add_charge_label(ax, mol['H2'][0], mol['H2'][1]-0.5, 'δ+', 
                           fontsize=10, color='blue')
        
        draw_bond(ax, molecules[0]['H2'][0], molecules[0]['H2'][1], 
                 molecules[1]['O'][0], molecules[1]['O'][1], 
                 bond_type='dashed', linewidth=2, color='blue')
        draw_bond(ax, molecules[1]['H2'][0], molecules[1]['H2'][1], 
                 molecules[2]['O'][0], molecules[2]['O'][1], 
                 bond_type='dashed', linewidth=2, color='blue')
        
        ax.text(6, 1.5, 'Dashed lines = intermolecular interactions', fontsize=13, 
               ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='blue', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem015:
    """
    Chapter 3.5: Metallic bonding structure
    Visual: Diagram of metal cations in a sea of electrons
    Task: MC — identify what the mobile particles in metallic bonding are
    Answer: A/B/C/D
    """
    
    def __init__(self):
        metals = [
            {'name': 'Sodium',    'symbol': 'Na', 'ion': 'Na⁺', 'valence': 1},
            {'name': 'Magnesium', 'symbol': 'Mg', 'ion': 'Mg²⁺','valence': 2},
            {'name': 'Aluminium', 'symbol': 'Al', 'ion': 'Al³⁺','valence': 3},
            {'name': 'Iron',      'symbol': 'Fe', 'ion': 'Fe²⁺','valence': 2},
            {'name': 'Copper',    'symbol': 'Cu', 'ion': 'Cu²⁺','valence': 2},
            {'name': 'Calcium',   'symbol': 'Ca', 'ion': 'Ca²⁺','valence': 2},
            {'name': 'Potassium', 'symbol': 'K',  'ion': 'K⁺',  'valence': 1},
            {'name': 'Zinc',      'symbol': 'Zn', 'ion': 'Zn²⁺','valence': 2},
            {'name': 'Silver',    'symbol': 'Ag', 'ion': 'Ag⁺', 'valence': 1},
            {'name': 'Lead',      'symbol': 'Pb', 'ion': 'Pb²⁺','valence': 2},
        ]
        
        questions = [
            {
                'q': "What are the mobile particles shown as small yellow circles in the diagram?",
                'correct': 'Delocalized electrons',
                'wrong': ['Protons', 'Metal cations', 'Neutrons'],
            },
            {
                'q': "What type of particles are represented by the large circles in the diagram?",
                'correct': 'Metal cations (positive ions)',
                'wrong': ['Metal atoms', 'Delocalized electrons', 'Anions'],
            },
            {
                'q': "What type of bonding is shown in the diagram?",
                'correct': 'Metallic bonding',
                'wrong': ['Ionic bonding', 'Covalent bonding', 'Hydrogen bonding'],
            },
        ]
        
        self.metal = rnd.choice(metals)
        self.question_data = rnd.choice(questions)
        
        correct = self.question_data['correct']
        opts = [correct] + self.question_data['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows the structure of {self.metal['name']}. "
            f"{self.question_data['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Metallic bonding"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Metallic bonding:} &\\\\"
            "\\text{Large circles = metal cations (M}^{n+}\\text{)} &\\\\"
            "\\text{Small circles = delocalized electrons} &\\\\"
            "\\text{Bonding = electrostatic attraction between them} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title only — no answer hint
        add_title_box(ax, 5, 7.5, f'Structure of {self.metal["name"]}', fontsize=16)
        
        ion_label = self.metal['ion']
        for i in range(1, 10, 2):
            for j in range(1, 8, 2):
                draw_circle_atom(ax, i, j, ion_label, radius=0.35, 
                               color='silver', text_color='black', fontsize=10)
        
        np.random.seed(num % 100)
        for _ in range(40):
            ex = np.random.uniform(0.5, 9.5)
            ey = np.random.uniform(0.5, 7)
            
            skip = False
            for i in range(1, 10, 2):
                for j in range(1, 8, 2):
                    if np.sqrt((ex-i)**2 + (ey-j)**2) < 0.5:
                        skip = True
            
            if not skip:
                ax.plot(ex, ey, 'o', color='yellow', markersize=6, 
                       markeredgecolor='orange', markeredgewidth=1)
        
        # Legend uses neutral labels — no answer reveal
        ax.text(2.5, 0.4, 'Large circles = ions', fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='silver', alpha=0.5))
        ax.text(7.5, 0.4, 'Small yellow circles = mobile particles',
               fontsize=10, ha='center',
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.4))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem016:
    """
    Chapter 3.6: Molecular polarity comparison
    Visual: Two molecule diagrams with dipole arrows but NO polarity labels
    Task: MC — identify which molecule is polar
    Answer: A/B/C/D
    """
    
    def __init__(self):
        # Each scenario: two molecules shown, one polar, one non-polar
        scenarios = [
            {'mol_a': 'CO₂', 'shape_a': 'linear',       'polar_a': False,
             'mol_b': 'H₂O', 'shape_b': 'bent',          'polar_b': True,
             'question': 'Which molecule is polar?',
             'correct': 'H₂O', 'wrong': ['CO₂', 'Both are polar', 'Neither is polar']},
            {'mol_a': 'BF₃', 'shape_a': 'trigonal planar','polar_a': False,
             'mol_b': 'NH₃', 'shape_b': 'trigonal pyramidal','polar_b': True,
             'question': 'Which molecule is polar?',
             'correct': 'NH₃', 'wrong': ['BF₃', 'Both are polar', 'Neither is polar']},
            {'mol_a': 'CCl₄', 'shape_a': 'tetrahedral',  'polar_a': False,
             'mol_b': 'CHCl₃','shape_b': 'tetrahedral',  'polar_b': True,
             'question': 'Which molecule has a net dipole moment?',
             'correct': 'CHCl₃','wrong': ['CCl₄', 'Both', 'Neither']},
            {'mol_a': 'SO₂', 'shape_a': 'bent',           'polar_a': True,
             'mol_b': 'CO₂', 'shape_b': 'linear',         'polar_b': False,
             'question': 'Which molecule is non-polar?',
             'correct': 'CO₂','wrong': ['SO₂', 'Both are non-polar', 'Neither']},
            {'mol_a': 'H₂O', 'shape_a': 'bent',           'polar_a': True,
             'mol_b': 'BeCl₂','shape_b': 'linear',        'polar_b': False,
             'question': 'Which molecule has dipoles that cancel?',
             'correct': 'BeCl₂','wrong': ['H₂O', 'Both', 'Neither']},
            {'mol_a': 'HCl', 'shape_a': 'diatomic',       'polar_a': True,
             'mol_b': 'Cl₂', 'shape_b': 'diatomic',       'polar_b': False,
             'question': 'Which molecule has a permanent dipole?',
             'correct': 'HCl','wrong': ['Cl₂', 'Both', 'Neither']},
            {'mol_a': 'PF₃', 'shape_a': 'trigonal pyramidal','polar_a': True,
             'mol_b': 'BF₃', 'shape_b': 'trigonal planar','polar_b': False,
             'question': 'Which molecule is polar?',
             'correct': 'PF₃','wrong': ['BF₃', 'Both are polar', 'Neither is polar']},
            {'mol_a': 'NF₃', 'shape_a': 'trigonal pyramidal','polar_a': True,
             'mol_b': 'AlF₃','shape_b': 'trigonal planar','polar_b': False,
             'question': 'Which molecule is polar?',
             'correct': 'NF₃','wrong': ['AlF₃', 'Both are polar', 'Neither is polar']},
            {'mol_a': 'H₂S','shape_a': 'bent',             'polar_a': True,
             'mol_b': 'CS₂','shape_b': 'linear',           'polar_b': False,
             'question': 'Which molecule has a net dipole moment?',
             'correct': 'H₂S','wrong': ['CS₂', 'Both', 'Neither']},
            {'mol_a': 'BCl₃','shape_a': 'trigonal planar', 'polar_a': False,
             'mol_b': 'PCl₃','shape_b': 'trigonal pyramidal','polar_b': True,
             'question': 'Which molecule is non-polar?',
             'correct': 'BCl₃','wrong': ['PCl₃', 'Both are non-polar', 'Neither']},
        ]
        
        self.scenario = rnd.choice(scenarios)
        correct = self.scenario['correct']
        opts = [correct] + self.scenario['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagrams show the structures of {self.scenario['mol_a']} and {self.scenario['mol_b']}. "
            f"Dipole arrows are shown for individual bonds. "
            f"{self.scenario['question']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Molecular polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.scenario['mol_a']} ({self.scenario['shape_a']}):}} &\\\\"
            f"\\text{{Polar: {'Yes' if self.scenario['polar_a'] else 'No'}}} &\\\\"
            f"\\text{{{self.scenario['mol_b']} ({self.scenario['shape_b']}):}} &\\\\"
            f"\\text{{Polar: {'Yes' if self.scenario['polar_b'] else 'No'}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title — no answer hint
        add_title_box(ax, 6, 7.5, 'Molecular Structure Comparison', fontsize=16)
        
        # Left molecule: mol_a
        ax.text(2, 7, self.scenario['mol_a'], fontsize=14, ha='center', fontweight='bold')
        ax.text(2, 6.5, f'Shape: {self.scenario["shape_a"]}', fontsize=11, ha='center')
        
        draw_circle_atom(ax, 2, 4, 'C', radius=0.4, color='black', text_color='white')
        draw_circle_atom(ax, 0.5, 4, 'O', radius=0.35, color='red', text_color='white')
        draw_circle_atom(ax, 3.5, 4, 'O', radius=0.35, color='red', text_color='white')
        draw_bond(ax, 0.85, 4, 1.6, 4, bond_type='double', linewidth=3)
        draw_bond(ax, 2.4, 4, 3.15, 4, bond_type='double', linewidth=3)
        # Show bond dipoles only (no net dipole or polarity label)
        draw_arrow(ax, 0.5, 3.4, 1.5, 3.4, arrowstyle='->', color='blue', linewidth=2)
        draw_arrow(ax, 3.5, 3.4, 2.5, 3.4, arrowstyle='->', color='blue', linewidth=2)
        ax.text(2, 2.5, self.scenario['mol_a'], fontsize=11, ha='center', fontweight='bold')
        
        ax.axvline(6, color='gray', linestyle='--', linewidth=1)
        
        # Right molecule: mol_b
        ax.text(9, 7, self.scenario['mol_b'], fontsize=14, ha='center', fontweight='bold')
        ax.text(9, 6.5, f'Shape: {self.scenario["shape_b"]}', fontsize=11, ha='center')
        
        draw_circle_atom(ax, 9, 4.5, 'O', radius=0.4, color='red', text_color='white')
        draw_circle_atom(ax, 8, 3.5, 'H', radius=0.3, color='lightblue', text_color='black')
        draw_circle_atom(ax, 10, 3.5, 'H', radius=0.3, color='lightblue', text_color='black')
        draw_bond(ax, 8.25, 3.65, 8.75, 4.25, bond_type='single', linewidth=3)
        draw_bond(ax, 9.75, 3.65, 9.25, 4.25, bond_type='single', linewidth=3)
        draw_arrow(ax, 8.5, 3.9, 8.8, 4.3, arrowstyle='->', color='blue', linewidth=2)
        draw_arrow(ax, 9.5, 3.9, 9.2, 4.3, arrowstyle='->', color='blue', linewidth=2)
        ax.text(9, 2.5, self.scenario['mol_b'], fontsize=11, ha='center', fontweight='bold')
        
        ax.text(6, 1.2, 'Arrows show individual bond dipoles (δ⁺ → δ⁻)',
               fontsize=11, ha='center', color='blue',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem017:
    """
    Chapter 3.7: Van der Waals forces and boiling points
    Visual: Graph of boiling points vs Mr for noble gases
    Task: MC — identify the noble gas at a specific boiling point, or which property explains trend
    Answer: A/B/C/D
    """
    
    def __init__(self):
        noble_gases = [
            {'symbol': 'He', 'Mr': 4,   'bp': -269},
            {'symbol': 'Ne', 'Mr': 20,  'bp': -246},
            {'symbol': 'Ar', 'Mr': 40,  'bp': -186},
            {'symbol': 'Kr', 'Mr': 84,  'bp': -153},
            {'symbol': 'Xe', 'Mr': 131, 'bp': -108},
        ]
        self.noble_gases_symbols = [g['symbol'] for g in noble_gases]
        self.Mr_values  = [g['Mr']  for g in noble_gases]
        self.bp_values  = [g['bp']  for g in noble_gases]
        
        questions = [
            {
                'q': "Which noble gas has the highest boiling point?",
                'correct': 'Xe', 'wrong': ['He', 'Ar', 'Ne'],
            },
            {
                'q': "Which noble gas has the lowest boiling point?",
                'correct': 'He', 'wrong': ['Xe', 'Ar', 'Ne'],
            },
            {
                'q': "What type of intermolecular force exists between noble gas atoms?",
                'correct': 'Van der Waals (London dispersion) forces',
                'wrong': ['Hydrogen bonds', 'Permanent dipole–dipole forces', 'Ionic bonds'],
            },
            {
                'q': "Why does boiling point increase from He to Xe?",
                'correct': 'Increasing Mr leads to stronger Van der Waals forces',
                'wrong': ['Increasing ionic character', 'Decreasing atomic radius',
                          'Increasing covalent bond strength'],
            },
            {
                'q': "Which noble gas has a boiling point of −186 °C?",
                'correct': 'Ar', 'wrong': ['Kr', 'Ne', 'He'],
            },
            {
                'q': "Which noble gas has a relative molecular mass of 84?",
                'correct': 'Kr', 'wrong': ['Xe', 'Ar', 'Ne'],
            },
            {
                'q': "As Mr increases across the noble gases, what happens to the boiling point?",
                'correct': 'It increases',
                'wrong': ['It decreases', 'It stays constant', 'It first increases then decreases'],
            },
            {
                'q': "What causes the increase in boiling point down Group 18?",
                'correct': 'More electrons → stronger temporary dipoles → stronger Van der Waals forces',
                'wrong': ['Stronger covalent bonds', 'Increased ionic radius', 'Higher electronegativity'],
            },
            {
                'q': "Which noble gas has the second highest boiling point?",
                'correct': 'Kr', 'wrong': ['Ar', 'Ne', 'Xe'],
            },
            {
                'q': "At what temperature (°C) does Ar boil?",
                'correct': '−186', 'wrong': ['−153', '−246', '−108'],
            },
        ]
        
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The graph shows boiling points of noble gases against relative molecular mass. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Noble gases: He < Ne < Ar < Kr < Xe (increasing Mr)} &\\\\"
            "\\text{Only Van der Waals forces present} &\\\\"
            "\\text{More electrons → stronger forces → higher bp} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        draw_line_graph(ax, self.Mr_values, self.bp_values, 
                       color='darkblue', linewidth=3, marker='o', markersize=12,
                       xlabel='Relative Molecular Mass (Mr)', 
                       ylabel='Boiling Point (°C)',
                       title='Boiling Points of Noble Gases vs Mr')
        
        # Label each point with symbol only (no extra info that gives away answer)
        for x, y, label in zip(self.Mr_values, self.bp_values, self.noble_gases_symbols):
            ax.text(x, y + 10, label, fontsize=12, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem018:
    """
    Chapter 4.1: States of matter particle arrangements
    Visual: Three diagrams of particle arrangements (unlabelled as solid/liquid/gas)
    Task: MC — identify the state shown in diagram X, or a property of a specific state
    Answer: A/B/C/D
    """
    
    def __init__(self):
        questions = [
            {
                'q': "Which diagram represents a solid?",
                'correct': 'Diagram A', 'wrong': ['Diagram B', 'Diagram C', 'Diagrams B and C'],
            },
            {
                'q': "Which diagram represents a gas?",
                'correct': 'Diagram C', 'wrong': ['Diagram A', 'Diagram B', 'Diagrams A and B'],
            },
            {
                'q': "Which diagram represents a liquid?",
                'correct': 'Diagram B', 'wrong': ['Diagram A', 'Diagram C', 'Diagrams A and C'],
            },
            {
                'q': "In which state do particles have a fixed, regular arrangement?",
                'correct': 'Solid', 'wrong': ['Liquid', 'Gas', 'Liquid and gas'],
            },
            {
                'q': "In which state are particles furthest apart?",
                'correct': 'Gas', 'wrong': ['Solid', 'Liquid', 'Solid and liquid'],
            },
            {
                'q': "In which state can particles flow past each other but remain close together?",
                'correct': 'Liquid', 'wrong': ['Solid', 'Gas', 'Solid and gas'],
            },
            {
                'q': "Which state has the highest kinetic energy of particles (at the same temperature)?",
                'correct': 'Gas', 'wrong': ['Solid', 'Liquid', 'They are all equal'],
            },
            {
                'q': "Which state has particles that vibrate about fixed positions?",
                'correct': 'Solid', 'wrong': ['Liquid', 'Gas', 'Liquid and gas'],
            },
            {
                'q': "Which state is represented by Diagram A?",
                'correct': 'Solid', 'wrong': ['Liquid', 'Gas', 'Plasma'],
            },
            {
                'q': "Which state has no fixed shape but a fixed volume?",
                'correct': 'Liquid', 'wrong': ['Solid', 'Gas', 'Solid and liquid'],
            },
        ]
        
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            "The diagrams show particle arrangements in three states of matter, labelled A, B, and C. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "States of matter"
        self.subtopic = "Particle model"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Diagram A = Solid: regular, fixed arrangement} &\\\\"
            "\\text{Diagram B = Liquid: close but disordered, mobile} &\\\\"
            "\\text{Diagram C = Gas: far apart, random motion} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        
        # Diagram A = Solid
        for row in range(4):
            for col in range(4):
                x = col * 1.2 + 0.6
                y = row * 1.2 + 0.6
                draw_circle_atom(ax[0], x, y, '', radius=0.25, 
                               color='darkblue', show_symbol=False)
        ax[0].set_title('Diagram A', fontsize=16, fontweight='bold')
        ax[0].set_xlim(0, 5)
        ax[0].set_ylim(0, 5)
        ax[0].axis('off')
        # No state label in subtitle — student must identify it
        
        # Diagram B = Liquid
        np.random.seed(42 + num % 10)
        for _ in range(16):
            x = np.random.uniform(0.5, 4.5)
            y = np.random.uniform(0.5, 4.5)
            draw_circle_atom(ax[1], x, y, '', radius=0.25, 
                           color='green', show_symbol=False)
        ax[1].set_title('Diagram B', fontsize=16, fontweight='bold')
        ax[1].set_xlim(0, 5)
        ax[1].set_ylim(0, 5)
        ax[1].axis('off')
        
        # Diagram C = Gas
        for _ in range(8):
            x = np.random.uniform(0.5, 4.5)
            y = np.random.uniform(0.5, 4.5)
            draw_circle_atom(ax[2], x, y, '', radius=0.2, 
                           color='red', show_symbol=False)
        ax[2].set_title('Diagram C', fontsize=16, fontweight='bold')
        ax[2].set_xlim(0, 5)
        ax[2].set_ylim(0, 5)
        ax[2].axis('off')
        
        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem019:
    """
    Chapter 4.2: Heating curve with phase changes
    Visual: Heating curve WITHOUT temperature labels; student reads melting point from y-axis
    Answer: numerical melting point (°C)
    """
    
    def __init__(self):
        # 12 distinct substance scenarios for variety
        substances = [
            {'name': 'substance X', 'mp': 15,  'bp': 85},
            {'name': 'substance X', 'mp': 22,  'bp': 95},
            {'name': 'substance X', 'mp': 30,  'bp': 105},
            {'name': 'substance X', 'mp': 45,  'bp': 110},
            {'name': 'substance X', 'mp': 10,  'bp': 88},
            {'name': 'substance X', 'mp': 38,  'bp': 100},
            {'name': 'substance X', 'mp': 25,  'bp': 92},
            {'name': 'substance X', 'mp': 50,  'bp': 115},
            {'name': 'substance X', 'mp': 5,   'bp': 80},
            {'name': 'substance X', 'mp': 42,  'bp': 108},
            {'name': 'substance X', 'mp': 18,  'bp': 98},
            {'name': 'substance X', 'mp': 35,  'bp': 102},
        ]
        s = rnd.choice(substances)
        self.melting_point = s['mp']
        self.boiling_point = s['bp']
        self.answer = self.melting_point  # numerical answer
        
        self.description = (
            "The heating curve shows temperature vs time for a pure substance. "
            f"Use the graph to determine the melting point (in °C) of the substance."
        )
        
        self.topic = "States of matter"
        self.subtopic = "Phase changes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Heating curve features:} &\\\\"
            "\\text{- Temperature rises → heating solid} &\\\\"
            f"\\text{{- First plateau (horizontal region) at {self.melting_point}°C → melting}} &\\\\"
            "\\text{- Temperature rises → heating liquid} &\\\\"
            f"\\text{{- Second plateau at {self.boiling_point}°C → boiling}} &\\\\"
            f"\\text{{Melting point}} &= {self.melting_point}\\,°C"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        time = [0, 2, 4, 4, 6, 8, 8, 10]
        temp = [-20, self.melting_point - 5, self.melting_point, self.melting_point,
                self.boiling_point - 10, self.boiling_point, self.boiling_point, self.boiling_point + 20]
        
        draw_line_graph(ax, time, temp, color='darkred', linewidth=3, marker='',
                       xlabel='Time (minutes)', ylabel='Temperature (°C)',
                       title='Heating Curve of a Pure Substance')
        
        # Dashed reference lines only — NO temperature value labels
        ax.axhline(y=self.melting_point, color='blue', linestyle='--', alpha=0.5)
        ax.axhline(y=self.boiling_point, color='green', linestyle='--', alpha=0.5)
        
        # Phase labels (do not reveal temperatures)
        ax.text(1, -12, 'Solid', fontsize=11, ha='center', style='italic', color='gray')
        ax.text(5, (self.melting_point + self.boiling_point) / 2,
                'Liquid', fontsize=11, ha='center', style='italic', color='gray')
        ax.text(9, self.boiling_point + 15, 'Gas', fontsize=11, ha='center', style='italic', color='gray')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem020:
    """
    Chapter 5.1: Enthalpy profile diagram
    Visual: Enthalpy profile with labelled energy levels (no values on arrows)
    Answer: numerical ΔH (kJ/mol)
    """
    
    def __init__(self):
        # 12 varied scenarios
        scenarios = [
            (55, 20, 100), (60, 25, 105), (50, 15, 95),
            (70, 30, 120), (45, 10, 90),  (65, 28, 110),
            (80, 35, 130), (40, 12, 85),  (75, 32, 125),
            (58, 18, 102), (48, 8,  92),  (72, 40, 115),
        ]
        self.reactant_E, self.product_E, self.activation_E = rnd.choice(scenarios)
        
        self.delta_H = self.product_E - self.reactant_E
        self.Ea = self.activation_E - self.reactant_E
        
        self.answer = self.delta_H  # numerical ΔH
        
        self.description = (
            "The enthalpy profile diagram is shown with energy levels marked on the y-axis. "
            "Calculate the enthalpy change ΔH (in kJ mol⁻¹) for this reaction."
        )
        
        self.topic = "Energetics"
        self.subtopic = "Enthalpy changes"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Energy of reactants}} &= {self.reactant_E}\\,\\text{{kJ/mol}}\\\\"
            f"\\text{{Energy of products}} &= {self.product_E}\\,\\text{{kJ/mol}}\\\\"
            "\\Delta H &= E_{{\\text{{products}}}} - E_{{\\text{{reactants}}}}\\\\"
            f"&= {self.product_E} - {self.reactant_E}\\\\"
            f"&= {self.delta_H}\\,\\text{{kJ/mol}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        profile = draw_enthalpy_profile(ax, self.reactant_E, self.product_E,
                                        self.activation_E, x_start=0, x_end=10)
        
        # Show arrows WITHOUT value labels — student must calculate from y-axis
        draw_vertical_annotation(ax, 1, self.reactant_E, self.activation_E,
                                'Ea', color='red', label_offset=0.5)
        
        draw_vertical_annotation(ax, 8.5, self.reactant_E, self.product_E,
                                'ΔH = ?', color='green', label_offset=0.5)
        
        ax.text(profile['reactant_x'], self.reactant_E + 8, 'Reactants',
               fontsize=14, ha='center', fontweight='bold')
        ax.text(profile['product_x'], self.product_E + 8, 'Products',
               fontsize=14, ha='center', fontweight='bold')
        
        # Y-axis tick values are visible and sufficient to calculate ΔH
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        ax.set_ylim(0, self.activation_E + 20)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem021:
    """
    Chapter 5.2: Hess's Law cycle
    """
    
    def __init__(self):
        self.delta_H1 = rnd.randint(-200, -100)
        self.delta_H2 = rnd.randint(-300, -200)
        self.delta_H_target = self.delta_H2 - self.delta_H1
        
        self.answer = f'{self.delta_H_target} kJ/mol'
        
        self.description = (
            "Use Hess's Law and the given enthalpy changes to calculate ΔH for the target reaction."
        )
        
        self.topic = "Energetics"
        self.subtopic = "Hess's Law"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Hess's Law: Total enthalpy change is independent of route} &\\\\"
            "\\text{Route 1 (direct):} &\\\\"
            "\\text{A → B: } \\Delta H_{\\text{target}} &\\\\"
            "\\text{Route 2 (via C):} &\\\\"
            f"\\text{{A → C: }} \\Delta H_1 &= {self.delta_H1}\\,\\text{{kJ/mol}}\\\\"
            f"\\text{{C → B: }} \\Delta H_2 &= {self.delta_H2}\\,\\text{{kJ/mol}}\\\\"
            "\\text{By Hess's Law:} &\\\\"
            "\\Delta H_{\\text{target}} &= \\Delta H_2 - \\Delta H_1\\\\"
            f"&= {self.delta_H2} - ({self.delta_H1})\\\\"
            f"&= {self.delta_H_target}\\,\\text{{kJ/mol}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, "Hess's Law Cycle", fontsize=16)
        
        draw_labeled_box(ax, 1, 5, 2, 1, 'A', 'Reactants', facecolor='lightblue')
        draw_labeled_box(ax, 9, 5, 2, 1, 'B', 'Products', facecolor='lightgreen')
        draw_labeled_box(ax, 5, 2, 2, 1, 'C', 'Intermediate', facecolor='yellow')
        
        draw_arrow(ax, 3.2, 5.5, 8.8, 5.5, label=f'ΔH = ?', 
                  label_position='above', color='red', linewidth=3)
        
        draw_arrow(ax, 2.5, 4.8, 5.5, 3.2, label=f'ΔH₁ = {self.delta_H1} kJ/mol',
                  label_position='side', label_offset=0.5, color='blue', linewidth=2)
        
        draw_arrow(ax, 7.5, 3.2, 9.5, 4.8, label=f'ΔH₂ = {self.delta_H2} kJ/mol',
                  label_position='side', label_offset=0.5, color='blue', linewidth=2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem022:
    """
    Chapter 6.1: Electrochemical cell
    """
    
    def __init__(self):
        metal_pairs = [
            {'anode': 'Zn', 'cathode': 'Cu', 'E_anode': -0.76, 'E_cathode': 0.34},
            {'anode': 'Mg', 'cathode': 'Ag', 'E_anode': -2.37, 'E_cathode': 0.80},
            {'anode': 'Fe', 'cathode': 'Cu', 'E_anode': -0.44, 'E_cathode': 0.34},
        ]
        
        self.cell = rnd.choice(metal_pairs)
        self.E_cell = self.cell['E_cathode'] - self.cell['E_anode']
        self.answer = f'{round(self.E_cell, 2)} V'
        
        self.description = (
            f"The electrochemical cell with {self.cell['anode']} and {self.cell['cathode']} electrodes is shown. "
            f"Calculate the cell potential (E°cell)."
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Redox and electrode potentials"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "E°_{\\text{cell}} &= E°_{\\text{cathode}} - E°_{\\text{anode}}\\\\"
            f"E°_{{{self.cell['cathode']}}} &= {self.cell['E_cathode']}\\,\\text{{V}}\\\\"
            f"E°_{{{self.cell['anode']}}} &= {self.cell['E_anode']}\\,\\text{{V}}\\\\"
            f"E°_{{\\text{{cell}}}} &= {self.cell['E_cathode']} - ({self.cell['E_anode']})\\\\"
            f"&= {round(self.E_cell, 2)}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, 'Electrochemical Cell', fontsize=16)
        
        draw_beaker(ax, 1, 2, 3, 3, liquid_height=2, liquid_color='lightblue')
        ax.text(2.5, 1.5, f'{self.cell["anode"]}²⁺(aq)', fontsize=11, ha='center', fontweight='bold')
        
        draw_beaker(ax, 8, 2, 3, 3, liquid_height=2, liquid_color='lightgreen')
        ax.text(9.5, 1.5, f'{self.cell["cathode"]}²⁺(aq)', fontsize=11, ha='center', fontweight='bold')
        
        ax.plot([2, 2], [5, 6.5], 'k-', linewidth=8)
        ax.text(2, 6.7, f'{self.cell["anode"]}', fontsize=14, ha='center', fontweight='bold')
        
        ax.plot([10, 10], [5, 6.5], 'k-', linewidth=8)
        ax.text(10, 6.7, f'{self.cell["cathode"]}', fontsize=14, ha='center', fontweight='bold')
        
        draw_labeled_box(ax, 4.5, 3.5, 3, 0.8, 'Salt Bridge\n(KNO₃)', 
                        facecolor='lightyellow', edgecolor='black')
        
        draw_arrow(ax, 2.5, 6, 5, 6, arrowstyle='->', color='red', linewidth=2)
        draw_arrow(ax, 7, 6, 9.5, 6, arrowstyle='->', color='red', linewidth=2)
        ax.text(6, 6.3, 'e⁻', fontsize=14, ha='center', fontweight='bold', color='red')
        
        draw_labeled_box(ax, 5, 6.5, 2, 0.6, 'Voltmeter', facecolor='white', edgecolor='black')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem023:
    """
    Chapter 7.1: Equilibrium concentration vs time
    """
    
    def __init__(self):
        self.initial_A = rnd.uniform(1.5, 2.5)
        self.final_A = rnd.uniform(0.5, 1.0)
        self.final_B = self.initial_A - self.final_A
        
        self.answer = f'[A]eq = {round(self.final_A, 2)} M, [B]eq = {round(self.final_B, 2)} M'
        
        self.description = (
            "The graph shows concentration vs time for the reaction A ⇌ B. "
            "State the equilibrium concentrations."
        )
        
        self.topic = "Equilibria"
        self.subtopic = "Dynamic equilibrium"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{At equilibrium:} &\\\\"
            "\\text{- Concentrations become constant} &\\\\"
            "\\text{- Forward and reverse rates are equal} &\\\\"
            f"\\text{{[A]eq}} &= {round(self.final_A, 2)}\\,\\text{{M}}\\\\"
            f"\\text{{[B]eq}} &= {round(self.final_B, 2)}\\,\\text{{M}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        time = np.linspace(0, 10, 100)
        conc_A = self.final_A + (self.initial_A - self.final_A) * np.exp(-0.5 * time)
        conc_B = self.final_B * (1 - np.exp(-0.5 * time))
        
        ax.plot(time, conc_A, 'b-', linewidth=3, label='[A]')
        ax.plot(time, conc_B, 'r-', linewidth=3, label='[B]')
        
        ax.axhline(y=self.final_A, color='b', linestyle='--', alpha=0.5)
        ax.axhline(y=self.final_B, color='r', linestyle='--', alpha=0.5)
        
        ax.axvline(x=7, color='green', linestyle='--', alpha=0.5, linewidth=2)
        ax.text(7, 2.5, 'Equilibrium\nReached', fontsize=12, ha='center', 
               fontweight='bold', color='green')
        
        ax.set_xlabel('Time (s)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (M)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time for A ⇌ B', fontsize=16, fontweight='bold')
        ax.legend(fontsize=14, loc='right')
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem024:
    """
    Chapter 7.2: Equilibrium constant calculation
    """
    
    def __init__(self):
        self.H2_eq = rnd.uniform(0.1, 0.3)
        self.I2_eq = rnd.uniform(0.1, 0.3)
        self.HI_eq = rnd.uniform(1.0, 2.0)
        
        self.Kc = (self.HI_eq ** 2) / (self.H2_eq * self.I2_eq)
        self.answer = round(self.Kc, 2)
        
        self.description = (
            "For the reaction H₂ + I₂ ⇌ 2HI, equilibrium concentrations are shown. "
            "Calculate Kc."
        )
        
        self.topic = "Equilibria"
        self.subtopic = "Equilibrium constant"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Equilibrium expression:} &\\\\"
            "K_c &= \\frac{[\\text{HI}]^2}{[\\text{H}_2][\\text{I}_2]}\\\\"
            "\\text{Substitute equilibrium concentrations:} &\\\\"
            f"K_c &= \\frac{{({round(self.HI_eq, 3)})^2}}{{({round(self.H2_eq, 3)})({round(self.I2_eq, 3)})}}\\\\"
            f"&= \\frac{{{round(self.HI_eq**2, 4)}}}{{{round(self.H2_eq * self.I2_eq, 4)}}}\\\\"
            f"&= {round(self.Kc, 2)}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7.5, 'H₂ + I₂ ⇌ 2HI', fontsize=16)
        
        data = [
            ['Species', 'Equilibrium Conc. (M)'],
            ['H₂', f'{round(self.H2_eq, 3)}'],
            ['I₂', f'{round(self.I2_eq, 3)}'],
            ['HI', f'{round(self.HI_eq, 3)}'],
        ]
        
        draw_data_table(ax, data, start_x=2, start_y=6, cell_width=3, cell_height=0.6)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem025:
    """
    Chapter 8.1: Maxwell-Boltzmann distribution
    """
    
    def __init__(self):
        self.T1 = rnd.randint(300, 400)
        self.T2 = self.T1 + rnd.randint(50, 100)
        self.Ea = rnd.randint(50, 100)
        
        self.answer = f'Higher temperature increases fraction of molecules with E ≥ Ea'
        
        self.description = (
            f"Maxwell-Boltzmann distributions at {self.T1}K and {self.T2}K are shown. "
            f"Explain the effect of temperature on reaction rate."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Effect of temperature"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{At higher temperature:} &\\\\"
            "\\text{1. Curve shifts right (higher average energy)} &\\\\"
            "\\text{2. Curve flattens (broader distribution)} &\\\\"
            "\\text{3. More molecules have } E \\geq E_a &\\\\"
            "\\text{4. More successful collisions} &\\\\"
            "\\text{5. Reaction rate increases}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        E = np.linspace(0, 200, 500)
        
        def maxwell_boltzmann(E, T):
            k = 1
            return (E / T**2) * np.exp(-E / T)
        
        y1 = maxwell_boltzmann(E, self.T1 / 10)
        y2 = maxwell_boltzmann(E, self.T2 / 10)
        
        ax.plot(E, y1, 'b-', linewidth=3, label=f'{self.T1}K')
        ax.plot(E, y2, 'r-', linewidth=3, label=f'{self.T2}K')
        
        ax.axvline(x=self.Ea, color='green', linestyle='--', linewidth=2)
        ax.text(self.Ea + 5, max(y1) * 0.8, f'Ea = {self.Ea}', fontsize=12, 
               color='green', fontweight='bold', rotation=90)
        
        ax.fill_between(E, 0, y1, where=(E >= self.Ea), alpha=0.2, color='blue')
        ax.fill_between(E, 0, y2, where=(E >= self.Ea), alpha=0.2, color='red')
        
        ax.set_xlabel('Energy', fontsize=14, fontweight='bold')
        ax.set_ylabel('Number of Molecules', fontsize=14, fontweight='bold')
        ax.set_title('Maxwell-Boltzmann Distribution', fontsize=16, fontweight='bold')
        ax.legend(fontsize=14)
        ax.set_xticks([])
        ax.set_yticks([])
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem026:
    """
    Chapter 8.2: First-order kinetics graph
    Visual: Concentration vs time curve; student reads off half-life from clean graph
    Answer: numerical half-life (seconds)
    """
    
    def __init__(self):
        # 12 varied half-life / initial-concentration scenarios
        scenarios = [
            (1.8, 5),  (2.0, 6),  (2.2, 7),  (1.5, 8),
            (2.4, 9),  (2.0, 10), (1.6, 11), (2.5, 12),
            (1.9, 13), (2.1, 14), (1.7, 15), (2.3, 6),
        ]
        self.initial_conc, self.half_life = rnd.choice(scenarios)
        self.answer = self.half_life  # numerical answer in seconds
        
        self.description = (
            "The graph shows the concentration vs time profile for a first-order reaction. "
            "Determine the half-life (t½) of the reaction in seconds."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Order of reaction"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{For a first-order reaction, } t_{1/2} \\text{ is constant.} &\\\\"
            f"\\text{{Initial concentration}} &= {round(self.initial_conc, 2)}\\,\\text{{M}}\\\\"
            f"\\text{{After one half-life, concentration}} &= {round(self.initial_conc/2, 2)}\\,\\text{{M}}\\\\"
            "\\text{Read the time at which } [A] = \\frac{{[A]_0}}{{2}} &\\\\"
            f"t_{{1/2}} &= {self.half_life}\\,\\text{{s}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        time = np.linspace(0, 4 * self.half_life, 200)
        conc = self.initial_conc * np.exp(-np.log(2) * time / self.half_life)
        
        draw_line_graph(ax, time, conc, color='darkblue', linewidth=3, marker='',
                       xlabel='Time (s)', ylabel='Concentration (mol dm⁻³)',
                       title='First-Order Reaction: Concentration vs Time')
        
        # Show dashed drop-lines to help student read — but NO t½ label text
        for i in range(1, 4):
            t = i * self.half_life
            c = self.initial_conc / (2 ** i)
            ax.axvline(x=t, color='red', linestyle='--', alpha=0.4)
            ax.axhline(y=c, color='red', linestyle='--', alpha=0.4)
            ax.plot(t, c, 'ro', markersize=8)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem027:
    """
    Chapter 9.1: Ionization energies across Period 3
    Visual: Bar chart of first IE values — plain colours, no annotations revealing deviations
    Task: MC — identify element at a specific position or reason for a trend/dip
    Answer: A/B/C/D
    """
    
    def __init__(self):
        self.elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
        self.IE_values = [496, 738, 578, 787, 1012, 1000, 1251, 1521]
        
        questions = [
            {
                'q': "Which element in Period 3 has the highest first ionization energy?",
                'correct': 'Ar', 'wrong': ['Cl', 'Na', 'P'],
            },
            {
                'q': "Which element in Period 3 has the lowest first ionization energy?",
                'correct': 'Na', 'wrong': ['Mg', 'Al', 'Si'],
            },
            {
                'q': "Why is the first IE of Al lower than that of Mg?",
                'correct': 'Al has its outer electron in the higher-energy 3p subshell',
                'wrong': ['Al has more protons', 'Al is smaller', 'Al has fewer electrons'],
            },
            {
                'q': "Why is the first IE of S lower than that of P?",
                'correct': 'S has a paired electron in 3p which experiences extra repulsion',
                'wrong': ['S has fewer protons', 'S has a larger atomic radius',
                          'S has a lower nuclear charge'],
            },
            {
                'q': "What is the general trend in first IE across Period 3?",
                'correct': 'Generally increases from Na to Ar',
                'wrong': ['Generally decreases from Na to Ar',
                          'Remains constant', 'First decreases then increases'],
            },
            {
                'q': "Which element has a first IE of 578 kJ mol⁻¹?",
                'correct': 'Al', 'wrong': ['Na', 'Mg', 'Si'],
            },
            {
                'q': "Between which two elements is there an unexpected decrease in first IE?",
                'correct': 'Mg and Al', 'wrong': ['Na and Mg', 'P and S', 'Cl and Ar'],
            },
            {
                'q': "Between which two elements is there a second unexpected decrease in first IE?",
                'correct': 'P and S', 'wrong': ['Mg and Al', 'Si and P', 'S and Cl'],
            },
            {
                'q': "Which element in Period 3 has the second highest first IE?",
                'correct': 'Cl', 'wrong': ['Ar', 'S', 'P'],
            },
            {
                'q': "What is the first IE of Na (kJ mol⁻¹)?",
                'correct': '496', 'wrong': ['738', '578', '1012'],
            },
        ]
        
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            "The bar chart shows first ionization energies of Period 3 elements. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in ionization energy"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Period 3 first IE (kJ mol}^{-1}\\text{):} &\\\\"
            "\\text{Na(496) < Mg(738), dip: Al(578) < Si(787) < P(1012),} &\\\\"
            "\\text{dip: S(1000) < Cl(1251) < Ar(1521)} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plain uniform colors — no red highlights that reveal dip positions
        colors = ['steelblue'] * len(self.elements)
        
        x_pos = np.arange(len(self.elements))
        draw_bar_chart(ax, x_pos, self.IE_values, self.elements, 
                      colors=colors, width=0.7,
                      xlabel='Element', ylabel='First Ionization Energy (kJ mol⁻¹)',
                      title='First Ionization Energies — Period 3')
        
        # Value labels on bars
        for x, y in zip(x_pos, self.IE_values):
            ax.text(x, y + 20, str(y), ha='center', fontsize=10, fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem028:
    """
    Chapter 9.2: Atomic radii across period
    Visual: Line graph of atomic radii — Period 3
    Task: MC — read value from graph or identify trend reason
    Answer: A/B/C/D
    """
    
    def __init__(self):
        self.elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']
        self.radii    = [186, 160, 143, 117, 110, 104, 99]
        
        questions = [
            {
                'q': "Which Period 3 element has the largest atomic radius?",
                'correct': 'Na', 'wrong': ['Mg', 'Cl', 'Si'],
            },
            {
                'q': "Which Period 3 element has the smallest atomic radius?",
                'correct': 'Cl', 'wrong': ['Na', 'P', 'S'],
            },
            {
                'q': "What is the atomic radius of Na (pm)?",
                'correct': '186', 'wrong': ['160', '99', '110'],
            },
            {
                'q': "What is the atomic radius of Cl (pm)?",
                'correct': '99', 'wrong': ['104', '143', '117'],
            },
            {
                'q': "Why does atomic radius decrease across Period 3?",
                'correct': 'Increasing nuclear charge pulls electrons closer to the nucleus',
                'wrong': ['Increasing number of electron shells',
                          'Decreasing shielding effect',
                          'Decreasing number of protons'],
            },
            {
                'q': "What is the general trend in atomic radius across Period 3?",
                'correct': 'Decreases from Na to Cl',
                'wrong': ['Increases from Na to Cl',
                          'Remains constant', 'Fluctuates irregularly'],
            },
            {
                'q': "Which element has an atomic radius of 143 pm?",
                'correct': 'Al', 'wrong': ['Mg', 'Si', 'Na'],
            },
            {
                'q': "Which element has an atomic radius of 117 pm?",
                'correct': 'Si', 'wrong': ['P', 'Al', 'S'],
            },
            {
                'q': "How many electrons do all Period 3 elements have in the same number of shells?",
                'correct': '3 shells', 'wrong': ['2 shells', '4 shells', '1 shell'],
            },
            {
                'q': "What is the atomic radius of Mg (pm)?",
                'correct': '160', 'wrong': ['186', '143', '117'],
            },
        ]
        
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            "The graph shows atomic radii of Period 3 elements. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in atomic properties"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Atomic radii (pm): Na(186) > Mg(160) > Al(143) > Si(117)} &\\\\"
            "\\text{> P(110) > S(104) > Cl(99)} &\\\\"
            "\\text{Decreasing: increasing nuclear charge, same shielding} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        x_pos = np.arange(len(self.elements))
        draw_line_graph(ax, x_pos, self.radii, color='darkblue', 
                       linewidth=3, marker='o', markersize=12,
                       xlabel='Element', ylabel='Atomic Radius (pm)',
                       title='Atomic Radii Across Period 3')
        
        ax.set_xticks(x_pos)
        ax.set_xticklabels(self.elements, fontsize=12, fontweight='bold')
        
        for x, y in zip(x_pos, self.radii):
            ax.text(x, y + 5, f'{y}', fontsize=10, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem029:
    """
    Chapter 11.1: Halogen displacement reactions
    Visual: Two test tubes (BEFORE/AFTER) — AFTER tube shows colour change visually
            but no text label describing it
    Answer: A/B/C/D (multiple choice — what colour change is observed?)
    """
    
    def __init__(self):
        reactions = [
            {'reagent': 'Cl₂(aq)', 'salt': 'KBr',  'color_before': 'colorless',
             'color_after': 'orange',  'displaced': 'Br₂',  'color_css': 'darkorange'},
            {'reagent': 'Cl₂(aq)', 'salt': 'KI',   'color_before': 'colorless',
             'color_after': 'brown',   'displaced': 'I₂',   'color_css': 'saddlebrown'},
            {'reagent': 'Br₂(aq)', 'salt': 'KI',   'color_before': 'pale orange',
             'color_after': 'brown',   'displaced': 'I₂',   'color_css': 'saddlebrown'},
            {'reagent': 'Cl₂(aq)', 'salt': 'NaBr', 'color_before': 'colorless',
             'color_after': 'orange',  'displaced': 'Br₂',  'color_css': 'darkorange'},
            {'reagent': 'Br₂(aq)', 'salt': 'NaI',  'color_before': 'pale orange',
             'color_after': 'dark brown','displaced': 'I₂', 'color_css': 'brown'},
            {'reagent': 'Cl₂(aq)', 'salt': 'MgBr₂','color_before': 'colorless',
             'color_after': 'orange',  'displaced': 'Br₂',  'color_css': 'darkorange'},
            {'reagent': 'Cl₂(aq)', 'salt': 'CaI₂', 'color_before': 'colorless',
             'color_after': 'brown',   'displaced': 'I₂',   'color_css': 'saddlebrown'},
            {'reagent': 'Br₂(aq)', 'salt': 'KCl',  'color_before': 'pale orange',
             'color_after': 'pale orange','displaced': 'No reaction','color_css': 'bisque'},
            {'reagent': 'I₂(aq)',  'salt': 'KBr',  'color_before': 'brown',
             'color_after': 'brown',   'displaced': 'No reaction','color_css': 'saddlebrown'},
            {'reagent': 'I₂(aq)',  'salt': 'KCl',  'color_before': 'brown',
             'color_after': 'brown',   'displaced': 'No reaction','color_css': 'saddlebrown'},
            {'reagent': 'Cl₂(aq)', 'salt': 'KF',   'color_before': 'colorless',
             'color_after': 'colorless','displaced': 'No reaction','color_css': 'white'},
        ]
        
        self.reaction = rnd.choice(reactions)
        correct = self.reaction['color_after'].capitalize()
        
        # Build MC options
        all_colors = ['Colorless', 'Orange', 'Brown', 'Yellow-green', 'Purple']
        distractors = [c for c in all_colors if c.lower() != correct.lower()]
        rnd.shuffle(distractors)
        opts = [correct] + distractors[:3]
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + self.options.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"{self.reaction['reagent']} is added to {self.reaction['salt']} solution. "
            f"What colour change is observed in the solution after mixing?\n"
            f"A. {self.options[0]}   B. {self.options[1]}   "
            f"C. {self.options[2]}   D. {self.options[3]}"
        )
        
        self.topic = "Group 17 (Halogens)"
        self.subtopic = "Halogen displacement reactions"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.reaction['reagent']} + {self.reaction['salt']}}} &\\\\"
            f"\\text{{Displaced: {self.reaction['displaced']}}} &\\\\"
            "\\text{More reactive halogen displaces less reactive} &\\\\"
            f"\\text{{Colour change: {self.reaction['color_before']} → {self.reaction['color_after']}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5.5,
                     f'Halogen Displacement: {self.reaction["reagent"]} + {self.reaction["salt"]}',
                     fontsize=14)
        
        color_css = {'colorless': 'white', 'pale orange': 'moccasin',
                     'orange': 'darkorange', 'brown': 'saddlebrown',
                     'dark brown': 'brown', 'yellow-green': 'yellowgreen',
                     'purple': 'purple'}
        
        before_css = color_css.get(self.reaction['color_before'].lower(), 'white')
        after_css  = color_css.get(self.reaction['color_after'].lower(),  'white')
        
        draw_test_tube(ax, 2, 1, width=1.4, height=3, solution_height=2,
                      solution_color=before_css)
        ax.text(2.7, 0.5, 'BEFORE', fontsize=12, ha='center', fontweight='bold')
        # Show only the BEFORE colour label (this is given info, not the answer)
        ax.text(2.7, 4.3, self.reaction['color_before'].capitalize(),
               fontsize=10, ha='center', style='italic', color='gray')
        
        draw_arrow(ax, 4, 3, 5.5, 3, arrowstyle='->', color='black', linewidth=3)
        ax.text(4.75, 3.6, 'Add ' + self.reaction['reagent'],
               fontsize=10, ha='center', fontweight='bold')
        
        draw_test_tube(ax, 8.5, 1, width=1.4, height=3, solution_height=2,
                      solution_color=after_css)
        ax.text(9.2, 0.5, 'AFTER', fontsize=12, ha='center', fontweight='bold')
        # NO text label for after colour — student must interpret the colour shown
        
        ax.text(9.2, 4.3, '?', fontsize=16, ha='center', fontweight='bold', color='navy')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem030:
    """
    Chapter 13.1: Structural isomers
    Visual: Two structural formulae with same molecular formula shown — student identifies isomerism type
    Answer: A/B/C/D (multiple choice)
    """
    
    def __init__(self):
        isomer_sets = [
            {'formula': 'C₄H₁₀', 'isomers': ['CH₃CH₂CH₂CH₃', 'CH₃CH(CH₃)CH₃'],
             'type': 'chain isomerism'},
            {'formula': 'C₅H₁₂', 'isomers': ['CH₃CH₂CH₂CH₂CH₃', 'CH₃CH(CH₃)CH₂CH₃'],
             'type': 'chain isomerism'},
            {'formula': 'C₄H₁₀O', 'isomers': ['CH₃CH₂CH₂OH', 'CH₃CH(OH)CH₃'],
             'type': 'position isomerism'},
            {'formula': 'C₃H₇Cl', 'isomers': ['CH₃CH₂CH₂Cl', 'CH₃CHClCH₃'],
             'type': 'position isomerism'},
            {'formula': 'C₃H₆O', 'isomers': ['CH₃CH₂CHO', 'CH₃COCH₃'],
             'type': 'functional group isomerism'},
            {'formula': 'C₂H₆O', 'isomers': ['CH₃CH₂OH', 'CH₃OCH₃'],
             'type': 'functional group isomerism'},
            {'formula': 'C₄H₈', 'isomers': ['CH₃CH₂CH=CH₂', 'CH₃CH=CHCH₃'],
             'type': 'position isomerism'},
            {'formula': 'C₅H₁₂', 'isomers': ['CH₃CH₂CH₂CH₂CH₃', 'C(CH₃)₄'],
             'type': 'chain isomerism'},
            {'formula': 'C₄H₈O', 'isomers': ['CH₃CH₂CH₂CHO', 'CH₃COCH₂CH₃'],
             'type': 'functional group isomerism'},
            {'formula': 'C₄H₉Br', 'isomers': ['CH₃CH₂CH₂CH₂Br', 'CH₃CH(Br)CH₂CH₃'],
             'type': 'position isomerism'},
            {'formula': 'C₃H₈O', 'isomers': ['CH₃CH₂CH₂OH', 'CH₃OCH₂CH₃'],
             'type': 'functional group isomerism'},
            {'formula': 'C₆H₁₄', 'isomers': ['CH₃(CH₂)₄CH₃', 'CH₃CH₂CH(CH₃)CH₂CH₃'],
             'type': 'chain isomerism'},
        ]
        
        self.set = rnd.choice(isomer_sets)
        correct = self.set['type'].capitalize()
        
        # MC options
        all_types = ['Chain isomerism', 'Position isomerism',
                     'Functional group isomerism', 'E/Z stereoisomerism']
        opts = [correct] + [t for t in all_types if t != correct][:3]
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + self.options.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows two isomers of {self.set['formula']}. "
            f"What type of isomerism do these two structures show?\n"
            f"A. {self.options[0]}   B. {self.options[1]}   "
            f"C. {self.options[2]}   D. {self.options[3]}"
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Isomerism"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecular formula: {self.set['formula']}}} &\\\\"
            f"\\text{{Type: {self.set['type'].capitalize()}}} &\\\\"
            "\\text{Both have the same molecular formula} &\\\\"
            "\\text{but differ in structural arrangement.} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        # Title does NOT reveal isomerism type
        add_title_box(ax, 6, 5.5, f'Isomers of {self.set["formula"]}', fontsize=16)
        
        draw_labeled_box(ax, 1, 2.5, 4, 1.5, self.set['isomers'][0],
                        'Isomer 1', facecolor='lightblue')
        
        draw_labeled_box(ax, 7, 2.5, 4, 1.5, self.set['isomers'][1],
                        'Isomer 2', facecolor='lightgreen')
        
        ax.text(6, 1.2, 'What type of isomerism is shown?', fontsize=12,
               ha='center', fontweight='bold', color='navy')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem031:
    """
    Chapter 13.2: E/Z isomerism
    Visual: Two structural diagrams of an alkene — no E/Z label shown
    Task: MC — identify isomerism type or E/Z designation
    Answer: A/B/C/D
    """
    
    def __init__(self):
        molecules = [
            {'name': 'but-2-ene',   'left_up': 'CH₃', 'left_dn': 'H',
             'right_up': 'H',   'right_dn': 'CH₃', 'e_name': 'E',
             'z_left_up': 'CH₃', 'z_left_dn': 'H',
             'z_right_up': 'CH₃','z_right_dn': 'H'},
            {'name': 'pent-2-ene',  'left_up': 'CH₃', 'left_dn': 'H',
             'right_up': 'H',   'right_dn': 'C₂H₅', 'e_name': 'E',
             'z_left_up': 'CH₃', 'z_left_dn': 'H',
             'z_right_up': 'C₂H₅','z_right_dn': 'H'},
            {'name': '1-bromopropene','left_up': 'Br', 'left_dn': 'H',
             'right_up': 'H',   'right_dn': 'CH₃', 'e_name': 'E',
             'z_left_up': 'Br', 'z_left_dn': 'H',
             'z_right_up': 'CH₃','z_right_dn': 'H'},
            {'name': '1-chloropropene','left_up': 'Cl','left_dn': 'H',
             'right_up': 'H',   'right_dn': 'CH₃', 'e_name': 'E',
             'z_left_up': 'Cl', 'z_left_dn': 'H',
             'z_right_up': 'CH₃','z_right_dn': 'H'},
        ]
        
        questions = [
            {
                'q': "What type of isomerism is shown by the two structures?",
                'correct': 'E/Z (geometric) stereoisomerism',
                'wrong': ['Chain isomerism', 'Optical isomerism', 'Functional group isomerism'],
            },
            {
                'q': "What structural feature allows E/Z isomerism?",
                'correct': 'A C=C double bond with different groups on each carbon',
                'wrong': ['A chiral carbon atom', 'A C–C single bond', 'A carbonyl group'],
            },
            {
                'q': "In the E isomer, where are the higher priority groups?",
                'correct': 'On opposite sides of the C=C bond',
                'wrong': ['On the same side of the C=C bond',
                          'Above the plane of the molecule',
                          'Below the plane of the molecule'],
            },
            {
                'q': "In the Z isomer, where are the higher priority groups?",
                'correct': 'On the same side of the C=C bond',
                'wrong': ['On opposite sides of the C=C bond',
                          'Above the plane of the molecule',
                          'Below the plane of the molecule'],
            },
            {
                'q': "Why is free rotation not possible around the C=C bond?",
                'correct': 'The π bond would need to break for rotation to occur',
                'wrong': ['The bond is too short', 'There are no electrons in the bond',
                          'The atoms are too large'],
            },
            {
                'q': "Which type of bond prevents rotation in E/Z isomers?",
                'correct': 'π (pi) bond', 'wrong': ['σ (sigma) bond', 'Ionic bond', 'Hydrogen bond'],
            },
            {
                'q': "Diagram 1 shows which isomer if the same groups are on opposite sides?",
                'correct': 'E isomer', 'wrong': ['Z isomer', 'Cis isomer', 'Optical isomer'],
            },
            {
                'q': "Which rule is used to assign E/Z configuration?",
                'correct': "Cahn-Ingold-Prelog (CIP) priority rules",
                'wrong': ['Hückel rule', 'Markovnikov rule', 'Zaitsev rule'],
            },
            {
                'q': "Which of the following can show E/Z isomerism?",
                'correct': 'CH₃CH=CHCl',
                'wrong': ['CH₂=CH₂', 'CH₂=CCl₂', 'CH₃CH=CH₂'],
            },
            {
                'q': "What is the relationship between E and Z isomers?",
                'correct': 'They are stereoisomers with the same molecular formula but different spatial arrangements',
                'wrong': ['They are structural isomers with different molecular formulae',
                          'They are identical molecules',
                          'They are optical isomers that are mirror images'],
            },
        ]
        
        self.mol    = rnd.choice(molecules)
        self.qdata  = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows two structural isomers of {self.mol['name']}. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Stereoisomerism"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{E/Z isomerism requirements:} &\\\\"
            "\\text{1. C=C double bond (π bond prevents rotation)} &\\\\"
            "\\text{2. Two different groups on each C of C=C} &\\\\"
            "\\text{E: higher priority groups on opposite sides} &\\\\"
            "\\text{Z: higher priority groups on same side} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        # Title shows molecule name only — no E/Z labels
        add_title_box(ax, 6, 5.5,
                     f'Two isomers of {self.mol["name"]}', fontsize=16)
        
        # Isomer 1 — groups arranged E fashion (different sides)
        draw_circle_atom(ax, 2, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 3.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 2.3, 3, 3.2, 3, bond_type='double', linewidth=3)
        
        ax.text(1.5, 3.5, self.mol['left_up'],  fontsize=12, ha='center', fontweight='bold')
        ax.text(1.5, 2.5, self.mol['left_dn'],  fontsize=12, ha='center', fontweight='bold')
        ax.text(4.0, 3.5, self.mol['right_up'], fontsize=12, ha='center', fontweight='bold')
        ax.text(4.0, 2.5, self.mol['right_dn'], fontsize=12, ha='center', fontweight='bold')
        
        draw_bond(ax, 2, 3, 1.7, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 2, 3, 1.7, 2.6, bond_type='single', linewidth=2)
        draw_bond(ax, 3.5, 3, 3.8, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 3.5, 3, 3.8, 2.6, bond_type='single', linewidth=2)
        
        # Label as "Isomer 1" — no E/Z hint
        ax.text(2.75, 1.5, 'Isomer 1', fontsize=12, ha='center',
               fontweight='bold', color='navy')
        
        # Isomer 2 — groups arranged Z fashion (same sides)
        draw_circle_atom(ax, 8.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 10.0, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 8.8, 3, 9.7, 3, bond_type='double', linewidth=3)
        
        ax.text(8.0, 3.5, self.mol['z_left_up'],  fontsize=12, ha='center', fontweight='bold')
        ax.text(8.0, 2.5, self.mol['z_left_dn'],  fontsize=12, ha='center', fontweight='bold')
        ax.text(10.5, 3.5, self.mol['z_right_up'],fontsize=12, ha='center', fontweight='bold')
        ax.text(10.5, 2.5, self.mol['z_right_dn'],fontsize=12, ha='center', fontweight='bold')
        
        draw_bond(ax, 8.5, 3, 8.2, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 8.5, 3, 8.2, 2.6, bond_type='single', linewidth=2)
        draw_bond(ax, 10, 3, 10.3, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 10, 3, 10.3, 2.6, bond_type='single', linewidth=2)
        
        ax.text(9.25, 1.5, 'Isomer 2', fontsize=12, ha='center',
               fontweight='bold', color='navy')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem032:
    """
    Chapter 13.3: Homologous series
    Visual: Table of formulae for a homologous series (series name NOT shown)
    Task: MC — identify general formula or series name
    Answer: A/B/C/D
    """
    
    def __init__(self):
        series_data = [
            {'series': 'Alkanes',   'formula': 'CₙH₂ₙ₊₂',
             'examples': [('Methane','CH₄'),('Ethane','C₂H₆'),('Propane','C₃H₈'),('Butane','C₄H₁₀')]},
            {'series': 'Alkenes',   'formula': 'CₙH₂ₙ',
             'examples': [('Ethene','C₂H₄'),('Propene','C₃H₆'),('Butene','C₄H₈'),('Pentene','C₅H₁₀')]},
            {'series': 'Alkynes',   'formula': 'CₙH₂ₙ₋₂',
             'examples': [('Ethyne','C₂H₂'),('Propyne','C₃H₄'),('Butyne','C₄H₆'),('Pentyne','C₅H₈')]},
            {'series': 'Alcohols',  'formula': 'CₙH₂ₙ₊₁OH',
             'examples': [('Methanol','CH₃OH'),('Ethanol','C₂H₅OH'),('Propan-1-ol','C₃H₇OH'),('Butan-1-ol','C₄H₉OH')]},
            {'series': 'Carboxylic acids','formula': 'CₙH₂ₙ₊₁COOH',
             'examples': [('Methanoic acid','HCOOH'),('Ethanoic acid','CH₃COOH'),('Propanoic acid','C₂H₅COOH'),('Butanoic acid','C₃H₇COOH')]},
        ]
        
        questions_templates = [
            {
                'q_tmpl': "What is the general formula of the homologous series shown?",
                'correct_attr': 'formula',
                'wrong_pool': ['CₙH₂ₙ₊₂','CₙH₂ₙ','CₙH₂ₙ₋₂','CₙH₂ₙ₊₁OH','CₙH₂ₙ₊₁COOH'],
            },
            {
                'q_tmpl': "What is the name of this homologous series?",
                'correct_attr': 'series',
                'wrong_pool': ['Alkanes','Alkenes','Alkynes','Alcohols','Carboxylic acids'],
            },
        ]
        
        self.series = rnd.choice(series_data)
        self.qt = rnd.choice(questions_templates)
        
        correct = self.series[self.qt['correct_attr']]
        wrong_pool = [w for w in self.qt['wrong_pool'] if w != correct]
        rnd.shuffle(wrong_pool)
        opts = [correct] + wrong_pool[:3]
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The table shows members of a homologous series. "
            f"{self.qt['q_tmpl']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Homologous series"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Series: {self.series['series']}}} &\\\\"
            f"\\text{{General formula: {self.series['formula']}}} &\\\\"
            "\\text{Each member differs by CH}_2 &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        # Title does NOT reveal the series name or formula
        add_title_box(ax, 5, 6.5, 'Members of a Homologous Series', fontsize=16)
        
        table_data = [['Name', 'Molecular Formula']] + \
                     [[name, formula] for name, formula in self.series['examples']]
        
        draw_data_table(ax, table_data, start_x=1.5, start_y=5.5,
                       cell_width=3.5, cell_height=0.7, header_color='lightblue')
        
        ax.text(5, 1.0, 'Each member differs by one —CH₂— unit',
               fontsize=11, ha='center', style='italic',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem033:
    """
    Chapter 14.1: Electrophilic addition mechanism
    Visual: Mechanism diagram showing reactant + reagent + carbocation intermediate ONLY
            Product box is blank/question mark
    Answer: A/B/C/D (MC about mechanism type)
    """
    
    def __init__(self):
        reactions = [
            {'reactant': 'CH₂=CH₂', 'reagent': 'HBr', 'product': 'CH₃CH₂Br',
             'product_name': 'bromoethane',   'electrophile': 'H⁺', 'nucleophile': 'Br⁻'},
            {'reactant': 'CH₂=CH₂', 'reagent': 'HCl', 'product': 'CH₃CH₂Cl',
             'product_name': 'chloroethane',  'electrophile': 'H⁺', 'nucleophile': 'Cl⁻'},
            {'reactant': 'CH₃CH=CH₂','reagent': 'HBr', 'product': 'CH₃CHBrCH₃',
             'product_name': '2-bromopropane','electrophile': 'H⁺', 'nucleophile': 'Br⁻'},
            {'reactant': 'CH₃CH=CH₂','reagent': 'HCl', 'product': 'CH₃CHClCH₃',
             'product_name': '2-chloropropane','electrophile': 'H⁺','nucleophile': 'Cl⁻'},
            {'reactant': 'CH₂=CHCH₃','reagent': 'HI',  'product': 'CH₃CHICH₃',
             'product_name': '2-iodopropane', 'electrophile': 'H⁺', 'nucleophile': 'I⁻'},
            {'reactant': 'CH₂=CH₂', 'reagent': 'Br₂', 'product': 'CH₂BrCH₂Br',
             'product_name': '1,2-dibromoethane','electrophile': 'Br⁺','nucleophile': 'Br⁻'},
            {'reactant': 'CH₂=CH₂', 'reagent': 'Cl₂', 'product': 'CH₂ClCH₂Cl',
             'product_name': '1,2-dichloroethane','electrophile': 'Cl⁺','nucleophile': 'Cl⁻'},
            {'reactant': 'CH₃CH=CH₂','reagent': 'Br₂', 'product': 'CH₃CHBrCH₂Br',
             'product_name': '1,2-dibromopropane','electrophile':'Br⁺','nucleophile':'Br⁻'},
            {'reactant': 'CH₂=CHCH₃','reagent': 'HBr', 'product': 'CH₃CH₂CH₂Br',
             'product_name': '1-bromopropane','electrophile': 'H⁺','nucleophile': 'Br⁻'},
            {'reactant': 'CH₂=CH₂', 'reagent': 'HI',  'product': 'CH₃CH₂I',
             'product_name': 'iodoethane',    'electrophile': 'H⁺', 'nucleophile': 'I⁻'},
            {'reactant': 'CH₂=CHCH₃','reagent': 'Cl₂', 'product': 'CH₃CHClCH₂Cl',
             'product_name': '1,2-dichloropropane','electrophile':'Cl⁺','nucleophile':'Cl⁻'},
        ]
        
        self.rxn = rnd.choice(reactions)
        correct = 'Electrophilic addition'
        opts = [correct, 'Nucleophilic substitution', 'Free radical substitution',
                'Electrophilic substitution']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + self.options.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows the reaction mechanism of {self.rxn['reactant']} with {self.rxn['reagent']}. "
            f"What type of reaction mechanism is shown?\n"
            f"A. {self.options[0]}   B. {self.options[1]}   "
            f"C. {self.options[2]}   D. {self.options[3]}"
        )
        
        self.topic = "Hydrocarbons"
        self.subtopic = "Reactions of alkenes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Mechanism: Electrophilic addition} &\\\\"
            f"\\text{{Step 1: π electrons attack {self.rxn['electrophile']} (electrophile)}} &\\\\"
            "\\text{Step 2: Carbocation intermediate forms} &\\\\"
            f"\\text{{Step 3: {self.rxn['nucleophile']} (nucleophile) attacks carbocation}} &\\\\"
            f"\\text{{Product: {self.rxn['product_name']}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 7, 5.5,
                     f'Reaction Mechanism: {self.rxn["reactant"]} + {self.rxn["reagent"]}',
                     fontsize=13)
        
        # Step 1: alkene
        draw_circle_atom(ax, 1.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 2.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 1.8, 3, 2.2, 3, bond_type='double', linewidth=3)
        ax.text(2, 2, self.rxn['reactant'], fontsize=9, ha='center', style='italic')
        
        ax.text(3.5, 3.5, self.rxn['electrophile'], fontsize=13, ha='center',
               fontweight='bold', color='red')
        ax.text(3.5, 2.5, self.rxn['nucleophile'], fontsize=13, ha='center',
               fontweight='bold', color='blue')
        
        draw_curly_arrow(ax, 2, 3.3, 3.3, 3.4, curvature=0.3, color='blue')
        ax.text(2.7, 3.9, 'Step 1', fontsize=9, color='blue', fontweight='bold')
        
        draw_arrow(ax, 4.1, 3, 5.1, 3, arrowstyle='->', color='black', linewidth=2)
        
        # Step 2: carbocation intermediate
        draw_circle_atom(ax, 6.1, 3, 'C⁺', radius=0.35, color='red', text_color='white')
        draw_circle_atom(ax, 7.3, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 6.45, 3, 7.0, 3, bond_type='single', linewidth=3)
        ax.text(5.1, 3.5, self.rxn['electrophile'].replace('⁺',''),
               fontsize=11, ha='center', fontweight='bold')
        draw_bond(ax, 6.1, 3, 5.4, 3.4, bond_type='single', linewidth=2)
        ax.text(6.7, 2, 'Carbocation\nintermediate', fontsize=9, ha='center', style='italic')
        
        ax.text(8.3, 2.6, self.rxn['nucleophile'], fontsize=13, ha='center',
               fontweight='bold', color='blue')
        draw_curly_arrow(ax, 8.1, 2.8, 6.3, 2.8, curvature=-0.3, color='blue')
        ax.text(7.2, 2.1, 'Step 2', fontsize=9, color='blue', fontweight='bold')
        
        draw_arrow(ax, 9.2, 3, 10.2, 3, arrowstyle='->', color='black', linewidth=2)
        
        # Product box is BLANK — student must identify mechanism, not product
        ax.add_patch(patches.FancyBboxPatch((10.5, 2.3), 2.8, 1.4,
                    boxstyle='round,pad=0.1', facecolor='lightyellow',
                    edgecolor='black', linewidth=2))
        ax.text(11.9, 3.0, '?', fontsize=22, ha='center', va='center',
               fontweight='bold', color='navy')
        ax.text(11.9, 2.1, 'Product', fontsize=9, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem034:
    """
    Chapter 15-17: Functional groups identification
    Visual: Three structural formulae shown; question asks to identify the functional group of ONE compound
    Task: MC — identify functional group or compound class
    Answer: A/B/C/D
    """
    
    def __init__(self):
        scenarios = [
            {
                'compounds': [
                    {'name': 'Chloroethane', 'formula': 'CH₃CH₂Cl', 'group': 'Halogenoalkane', 'fg': '–Cl'},
                    {'name': 'Ethanol',      'formula': 'CH₃CH₂OH', 'group': 'Alcohol',         'fg': '–OH'},
                    {'name': 'Ethanal',      'formula': 'CH₃CHO',   'group': 'Aldehyde',         'fg': '–CHO'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Ethanoic acid','formula': 'CH₃COOH', 'group': 'Carboxylic acid', 'fg': '–COOH'},
                    {'name': 'Ethanol',      'formula': 'CH₃CH₂OH','group': 'Alcohol',          'fg': '–OH'},
                    {'name': 'Propanal',     'formula': 'CH₃CH₂CHO','group': 'Aldehyde',        'fg': '–CHO'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Propanone',    'formula': 'CH₃COCH₃', 'group': 'Ketone',     'fg': 'C=O (internal)'},
                    {'name': 'Propanal',     'formula': 'CH₃CH₂CHO','group': 'Aldehyde',   'fg': '–CHO'},
                    {'name': 'Propanol',     'formula': 'CH₃CH₂CH₂OH','group': 'Alcohol',  'fg': '–OH'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Methylamine',  'formula': 'CH₃NH₂',  'group': 'Amine',       'fg': '–NH₂'},
                    {'name': 'Ethanol',      'formula': 'CH₃CH₂OH','group': 'Alcohol',      'fg': '–OH'},
                    {'name': 'Chloroethane', 'formula': 'CH₃CH₂Cl','group': 'Halogenoalkane','fg': '–Cl'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Ethyl ethanoate','formula': 'CH₃COOC₂H₅','group': 'Ester',   'fg': '–COO–'},
                    {'name': 'Ethanol',       'formula': 'CH₃CH₂OH',  'group': 'Alcohol',  'fg': '–OH'},
                    {'name': 'Ethanoic acid', 'formula': 'CH₃COOH',   'group': 'Carboxylic acid','fg': '–COOH'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Bromoethane',  'formula': 'CH₃CH₂Br',  'group': 'Halogenoalkane','fg': '–Br'},
                    {'name': 'Ethanal',      'formula': 'CH₃CHO',     'group': 'Aldehyde',      'fg': '–CHO'},
                    {'name': 'Propanone',    'formula': 'CH₃COCH₃',   'group': 'Ketone',        'fg': 'C=O'},
                ], 'ask': 0,
            },
            {
                'compounds': [
                    {'name': 'Propanoic acid','formula': 'CH₃CH₂COOH','group': 'Carboxylic acid','fg': '–COOH'},
                    {'name': 'Propanal',      'formula': 'CH₃CH₂CHO', 'group': 'Aldehyde',      'fg': '–CHO'},
                    {'name': 'Methylamine',   'formula': 'CH₃NH₂',    'group': 'Amine',          'fg': '–NH₂'},
                ], 'ask': 2,
            },
            {
                'compounds': [
                    {'name': 'Ethyl ethanoate','formula': 'CH₃COOC₂H₅','group': 'Ester',    'fg': '–COO–'},
                    {'name': 'Methylamine',    'formula': 'CH₃NH₂',    'group': 'Amine',     'fg': '–NH₂'},
                    {'name': 'Chloromethane',  'formula': 'CH₃Cl',     'group': 'Halogenoalkane','fg': '–Cl'},
                ], 'ask': 1,
            },
            {
                'compounds': [
                    {'name': 'Propan-2-ol',   'formula': 'CH₃CHOHCH₃','group': 'Alcohol',        'fg': '–OH'},
                    {'name': 'Propanone',      'formula': 'CH₃COCH₃',  'group': 'Ketone',         'fg': 'C=O'},
                    {'name': 'Propanoic acid', 'formula': 'CH₃CH₂COOH','group': 'Carboxylic acid','fg': '–COOH'},
                ], 'ask': 1,
            },
            {
                'compounds': [
                    {'name': 'Ethanoic acid',  'formula': 'CH₃COOH',  'group': 'Carboxylic acid','fg': '–COOH'},
                    {'name': 'Ethyl ethanoate','formula': 'CH₃COOC₂H₅','group': 'Ester',         'fg': '–COO–'},
                    {'name': 'Ethanamide',     'formula': 'CH₃CONH₂', 'group': 'Amide',          'fg': '–CONH₂'},
                ], 'ask': 2,
            },
        ]
        
        self.scenario = rnd.choice(scenarios)
        self.compounds = self.scenario['compounds']
        ask_idx = self.scenario['ask']
        target = self.compounds[ask_idx]
        
        correct = target['group']
        all_groups = ['Alcohol', 'Aldehyde', 'Ketone', 'Carboxylic acid', 'Ester',
                      'Halogenoalkane', 'Amine', 'Amide']
        wrong = [g for g in all_groups if g != correct]
        rnd.shuffle(wrong)
        opts = [correct] + wrong[:3]
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        names = ['X', 'Y', 'Z']
        self.compound_labels = names
        
        self.description = (
            f"The diagram shows structural formulae of three compounds. "
            f"What is the functional group class of compound {names[ask_idx]} "
            f"({target['formula']})?\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Organic functional groups"
        self.subtopic = "Functional group identification"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Target compound: {target['name']} ({target['formula']})}} &\\\\"
            f"\\text{{Functional group: {target['fg']}}} &\\\\"
            f"\\text{{Class: {target['group']}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 7, 5.5, 'Structural Formulae of Organic Compounds', fontsize=16)
        
        x_positions = [2, 7, 12]
        colors = ['lightcoral', 'lightblue', 'lightgreen']
        labels = self.compound_labels
        
        for i, (comp, x, color, label) in enumerate(
                zip(self.compounds, x_positions, colors, labels)):
            draw_labeled_box(ax, x - 1.5, 3, 3, 1.2,
                           comp['formula'], f'Compound {label}',
                           facecolor=color)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem035:
    """
    Chapter 19: Amide / condensation reactions
    Visual: Reactants → arrow → product diagram (product functional group NOT labelled/highlighted)
    Task: MC — identify the functional group formed or type of reaction
    Answer: A/B/C/D
    """
    
    def __init__(self):
        questions = [
            {
                'q': "What functional group is formed in this reaction?",
                'correct': 'Amide (–CONH–)',
                'wrong': ['Ester (–COO–)', 'Ether (–O–)', 'Alcohol (–OH)'],
            },
            {
                'q': "What type of reaction is shown?",
                'correct': 'Condensation reaction',
                'wrong': ['Addition reaction', 'Elimination reaction', 'Substitution reaction'],
            },
            {
                'q': "What small molecule is eliminated in this reaction?",
                'correct': 'Water (H₂O)',
                'wrong': ['HCl', 'CO₂', 'NH₃'],
            },
            {
                'q': "What are the two functional groups in the reactants that combine?",
                'correct': 'Carboxylic acid (–COOH) and amine (–NH₂)',
                'wrong': ['Alcohol and amine', 'Ketone and amine', 'Carboxylic acid and alcohol'],
            },
            {
                'q': "What is the amide bond also known as in proteins?",
                'correct': 'Peptide bond',
                'wrong': ['Glycosidic bond', 'Phosphodiester bond', 'Disulfide bridge'],
            },
            {
                'q': "Which reagent acts as the nucleophile in amide formation?",
                'correct': 'Amine (R–NH₂)',
                'wrong': ['Carboxylic acid', 'Water', 'Aldehyde'],
            },
            {
                'q': "What bond is present in the amide functional group?",
                'correct': 'C–N bond adjacent to a carbonyl (C=O)',
                'wrong': ['O–H bond', 'C–O single bond only', 'N–O bond'],
            },
            {
                'q': "Which of the following is an amide?",
                'correct': 'CH₃CONH₂',
                'wrong': ['CH₃COOH', 'CH₃COOC₂H₅', 'CH₃NH₂'],
            },
            {
                'q': "Which condition is typically required for amide formation from a carboxylic acid and amine?",
                'correct': 'Heat',
                'wrong': ['UV light', 'Aqueous alkali', 'Concentrated H₂SO₄'],
            },
            {
                'q': "What is the systematic name for CH₃CONH₂?",
                'correct': 'Ethanamide',
                'wrong': ['Methanoic acid', 'Ethanoic acid', 'Ethylamine'],
            },
        ]
        
        self.qdata = rnd.choice(questions)
        correct = self.qdata['correct']
        opts = [correct] + self.qdata['wrong']
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + opts.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            "The diagram shows the reaction between a carboxylic acid and an amine. "
            f"{self.qdata['q']}\n"
            f"A. {opts[0]}   B. {opts[1]}   C. {opts[2]}   D. {opts[3]}"
        )
        
        self.topic = "Nitrogen compounds"
        self.subtopic = "Amides"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Carboxylic acid + Amine} &\\rightarrow \\text{Amide + H}_2\\text{O}\\\\"
            "\\text{Type: Condensation (eliminates H}_2\\text{O)} &\\\\"
            "\\text{Functional group: –CO–NH– (amide)} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        add_title_box(ax, 6, 9, 'Reaction of a Carboxylic Acid with an Amine', fontsize=14)
        
        draw_labeled_box(ax, 0.5, 6.5, 3, 1.5, 'R—COOH', 'Carboxylic acid',
                        facecolor='lightblue')
        
        ax.text(4.5, 7.2, '+', fontsize=20, ha='center', fontweight='bold')
        
        draw_labeled_box(ax, 5.5, 6.5, 3, 1.5, "R'—NH₂", 'Amine',
                        facecolor='lightgreen')
        
        draw_arrow(ax, 6, 6.2, 6, 5,
                  label='Heat',
                  label_position='side', label_offset=1.2, color='red', linewidth=3)
        
        # Product box — NO functional group highlighted or labelled
        draw_labeled_box(ax, 3, 3, 6, 1.5, "R—CO—NH—R'", 'Product',
                        facecolor='lightyellow')
        
        ax.text(9.5, 5.5, '+ H₂O', fontsize=12, ha='center', fontweight='bold')
        ax.text(9.5, 5.0, '(small molecule\neliminated)',
               fontsize=9, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem036:
    """
    Chapter 20: Addition polymerization
    Visual: Monomer units + polymerization arrow + repeat unit in brackets
            Polymer name NOT shown in image
    Answer: A/B/C/D (multiple choice — name of polymer formed)
    """
    
    def __init__(self):
        monomers = [
            {'monomer': 'CH₂=CH₂',    'repeat': '—CH₂—CH₂—',        'name': 'Poly(ethene)',
             'common': 'Polyethylene'},
            {'monomer': 'CH₂=CHCH₃',  'repeat': '—CH₂—CH(CH₃)—',    'name': 'Poly(propene)',
             'common': 'Polypropylene'},
            {'monomer': 'CH₂=CHCl',   'repeat': '—CH₂—CHCl—',        'name': 'Poly(chloroethene)',
             'common': 'PVC'},
            {'monomer': 'CH₂=C(CH₃)₂','repeat': '—CH₂—C(CH₃)₂—',   'name': 'Poly(2-methylpropene)',
             'common': 'Polyisobutylene'},
            {'monomer': 'CH₂=CHCN',   'repeat': '—CH₂—CH(CN)—',      'name': 'Poly(propenenitrile)',
             'common': 'Polyacrylonitrile'},
            {'monomer': 'CH₂=CHC₆H₅','repeat': '—CH₂—CH(C₆H₅)—',   'name': 'Poly(phenylethene)',
             'common': 'Polystyrene'},
            {'monomer': 'CF₂=CF₂',    'repeat': '—CF₂—CF₂—',         'name': 'Poly(tetrafluoroethene)',
             'common': 'PTFE / Teflon'},
            {'monomer': 'CH₂=CHOCOCH₃','repeat':'—CH₂—CH(OCOCH₃)—', 'name': 'Poly(ethenyl ethanoate)',
             'common': 'PVA'},
            {'monomer': 'CH₂=CHF',    'repeat': '—CH₂—CHF—',          'name': 'Poly(fluoroethene)',
             'common': 'PVF'},
            {'monomer': 'CH₂=CBrH',   'repeat': '—CH₂—CHBr—',         'name': 'Poly(bromoethene)',
             'common': 'PVB'},
            {'monomer': 'CH₂=CHOH',   'repeat': '—CH₂—CHOH—',         'name': 'Poly(ethenol)',
             'common': 'Polyvinyl alcohol'},
        ]
        
        self.mono = rnd.choice(monomers)
        self.monomer      = self.mono['monomer']
        self.polymer_name = self.mono['name']
        self.repeating_unit = self.mono['repeat']
        
        correct = self.polymer_name
        all_names = list({m['name'] for m in monomers})
        rnd.shuffle(all_names)
        distractors = [n for n in all_names if n != correct][:3]
        opts = [correct] + distractors
        rnd.shuffle(opts)
        self.options = opts
        self.correct_letter = chr(65 + self.options.index(correct))
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows addition polymerization of {self.monomer}. "
            f"Which polymer is formed?\n"
            f"A. {self.options[0]}   B. {self.options[1]}   "
            f"C. {self.options[2]}   D. {self.options[3]}"
        )
        
        self.topic = "Polymerization"
        self.subtopic = "Addition polymerization"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Type: Addition polymerization} &\\\\"
            f"\\text{{Monomer: {self.monomer}}} &\\\\"
            "\\text{Process: C=C double bond breaks, monomers join} &\\\\"
            f"\\text{{Repeating unit: {self.repeating_unit}}} &\\\\"
            f"\\text{{Polymer: {self.polymer_name}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        add_title_box(ax, 6, 9, 'Addition Polymerization', fontsize=16)
        
        ax.text(2, 7.5, 'MONOMER', fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue'))
        
        for i, x in enumerate([1, 2.5, 4]):
            ax.text(x, 6.5, self.monomer, fontsize=11, ha='center', fontweight='bold')
            if i < 2:
                ax.text(x + 0.7, 6.5, '+', fontsize=14, ha='center')
        ax.text(4.8, 6.5, '+ ...', fontsize=12, ha='center')
        ax.text(2.5, 5.8, 'n monomers', fontsize=10, ha='center', style='italic')
        
        draw_arrow(ax, 6, 6.5, 6, 5, label='Polymerization\n(initiator/catalyst)',
                  label_position='side', label_offset=1.2, color='red', linewidth=3)
        
        ax.text(6, 4, 'POLYMER', fontsize=13, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen'))
        
        ax.text(3, 3, '...', fontsize=14, ha='center', fontweight='bold')
        draw_bracket(ax, 3.5, 2.5, 0.8, bracket_type='square', direction='left', linewidth=3)
        ax.text(5, 3, self.repeating_unit, fontsize=11, ha='center', fontweight='bold')
        draw_bracket(ax, 6.5, 2.5, 0.8, bracket_type='square', direction='right',
                    linewidth=3, subscript='n')
        ax.text(7.5, 3, '...', fontsize=14, ha='center', fontweight='bold')
        
        ax.text(5, 1.8, 'Repeating unit', fontsize=10, ha='center',
               style='italic', color='red', fontweight='bold')
        
        # NO polymer name label — student must answer the MC
        ax.text(5, 1.0, 'Name of polymer = ?', fontsize=11, ha='center',
               fontweight='bold', color='navy')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem037:
    """
    Topic: 21.1 Organic synthesis — multi-step routes
    Visual: Synthesis pathway diagram with one step's reagent hidden
    Task: Identify reagent/conditions for a step (MCQ)
    10+ variations via different pathways and asked step
    """
    
    def __init__(self):
        pathways = [
            {
                'title': 'Ethene → Ethanoic Acid',
                'steps': [
                    {'from': 'CH₂=CH₂',  'to': 'CH₃CH₂Br',  'reagent': 'HBr',           'mech': 'Electrophilic addition'},
                    {'from': 'CH₃CH₂Br', 'to': 'CH₃CH₂OH',  'reagent': 'NaOH(aq), heat', 'mech': 'Nucleophilic substitution'},
                    {'from': 'CH₃CH₂OH', 'to': 'CH₃COOH',   'reagent': 'K₂Cr₂O₇/H₂SO₄, heat','mech': 'Oxidation'},
                ],
            },
            {
                'title': 'Benzene → Nitrobenzene → Phenylamine',
                'steps': [
                    {'from': 'C₆H₆',        'to': 'C₆H₅NO₂',  'reagent': 'HNO₃/H₂SO₄, 55°C',  'mech': 'Electrophilic substitution'},
                    {'from': 'C₆H₅NO₂',     'to': 'C₆H₅NH₂',  'reagent': 'Sn/HCl, then NaOH',  'mech': 'Reduction'},
                ],
            },
            {
                'title': 'Propene → Propan-2-ol → Propanone',
                'steps': [
                    {'from': 'CH₃CH=CH₂',   'to': 'CH₃CHOHCH₃','reagent': 'H₂O/H₂SO₄ (steam)',  'mech': 'Electrophilic addition'},
                    {'from': 'CH₃CHOHCH₃',  'to': 'CH₃COCH₃',  'reagent': 'K₂Cr₂O₇/H₂SO₄',     'mech': 'Oxidation'},
                ],
            },
            {
                'title': 'Bromoethane → Ethanol → Ethanal',
                'steps': [
                    {'from': 'CH₃CH₂Br',    'to': 'CH₃CH₂OH',  'reagent': 'NaOH(aq), heat',     'mech': 'Nucleophilic substitution'},
                    {'from': 'CH₃CH₂OH',    'to': 'CH₃CHO',    'reagent': 'K₂Cr₂O₇/H₂SO₄ (distil)','mech': 'Oxidation'},
                ],
            },
            {
                'title': 'Ethanol → Ethyl ethanoate',
                'steps': [
                    {'from': 'CH₃CH₂OH',    'to': 'CH₃COOC₂H₅','reagent': 'CH₃COOH + H₂SO₄ catalyst','mech': 'Esterification'},
                ],
            },
            {
                'title': 'Chloroethane → Ethanol → Ethanal → Ethanoic acid',
                'steps': [
                    {'from': 'CH₃CH₂Cl',   'to': 'CH₃CH₂OH',  'reagent': 'NaOH(aq), heat',     'mech': 'Nucleophilic substitution'},
                    {'from': 'CH₃CH₂OH',   'to': 'CH₃CHO',    'reagent': 'K₂Cr₂O₇/H₂SO₄ (distil)','mech': 'Oxidation'},
                    {'from': 'CH₃CHO',     'to': 'CH₃COOH',   'reagent': 'K₂Cr₂O₇/H₂SO₄, reflux','mech': 'Oxidation'},
                ],
            },
        ]
        
        self.pathway = rnd.choice(pathways)
        self.steps = self.pathway['steps']
        
        # Ask about one specific step
        step_idx = rnd.randint(0, len(self.steps) - 1)
        self.asked_step_idx = step_idx
        self.asked_step = self.steps[step_idx]
        correct = self.asked_step['reagent']
        
        # Build distractors from all reagents across all pathways
        all_reagents = list({s['reagent'] for p in pathways for s in p['steps'] if s['reagent'] != correct})
        distractors = rnd.sample(all_reagents, min(3, len(all_reagents)))
        options = distractors + [correct]
        rnd.shuffle(options)
        labels = ['A', 'B', 'C', 'D']
        self.options = options
        self.correct_letter = labels[options.index(correct)]
        self.answer = self.correct_letter
        
        self.description = (
            f"The diagram shows a multi-step synthesis: {self.pathway['title']}. "
            f"What reagents/conditions are needed for Step {step_idx + 1} "
            f"({self.asked_step['from']} → {self.asked_step['to']})?\n"
            + "   ".join(f"{labels[i]}. {options[i]}" for i in range(4))
        )
        
        self.topic = "Organic synthesis"
        self.subtopic = "Synthetic routes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Step {step_idx+1}: {self.asked_step['from']} → {self.asked_step['to']}}} &\\\\"
            f"\\text{{Mechanism: {self.asked_step['mech']}}} &\\\\"
            f"\\text{{Reagent: {correct}}} &\\\\"
            f"\\text{{Answer: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 10))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        add_title_box(ax, 6, 9.5, f'Synthesis: {self.pathway["title"]}', fontsize=14)
        
        n_steps = len(self.steps)
        y_start = 8.0
        y_step = 6.5 / (n_steps + 1)
        
        compounds = [self.steps[0]['from']] + [s['to'] for s in self.steps]
        
        for i, comp in enumerate(compounds):
            y = y_start - i * y_step
            draw_labeled_box(ax, 1, y - 0.4, 2.5, 0.8, comp, f'Compound {i}', facecolor='lightblue')
        
        for i, step in enumerate(self.steps):
            y_arrow = y_start - i * y_step - 0.4
            draw_arrow(ax, 2.25, y_arrow, 2.25, y_arrow - y_step + 0.4,
                      arrowstyle='->', color='red', linewidth=2)
            
            # If this is the asked step, show "?" for reagent
            reagent_text = '?' if i == self.asked_step_idx else step['reagent']
            draw_labeled_box(ax, 3.5, y_arrow - y_step/2, 4, 0.7,
                           f'Step {i+1}', reagent_text,
                           facecolor='mistyrose' if i == self.asked_step_idx else 'lightyellow',
                           edgecolor='red' if i == self.asked_step_idx else 'black',
                           label_fontsize=10, sublabel_fontsize=8)
        
        labels_list = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(self.options):
            ax.text(0.3 + i * 3.0, 0.5, f"{labels_list[i]}. {opt}",
                   fontsize=8, ha='left',
                   bbox=dict(boxstyle='round', facecolor='aliceblue', pad=0.2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem038:
    """
    Chapter 22: Mass spectrum of organic molecule
    Visual: Mass spectrum with unlabelled M⁺ peak; student identifies its m/z value
    Answer: numerical M⁺ value
    """
    
    def __init__(self):
        molecules = [
            {'name': 'Methanol',      'formula': 'CH₃OH',      'M_plus': 32,
             'fragments': [{'mz': 31, 'intensity': 80}, {'mz': 29, 'intensity': 30},
                           {'mz': 15, 'intensity': 40}]},
            {'name': 'Ethanol',       'formula': 'C₂H₅OH',     'M_plus': 46,
             'fragments': [{'mz': 45, 'intensity': 25}, {'mz': 31, 'intensity': 60},
                           {'mz': 15, 'intensity': 30}]},
            {'name': 'Propan-1-ol',   'formula': 'C₃H₇OH',     'M_plus': 60,
             'fragments': [{'mz': 59, 'intensity': 20}, {'mz': 31, 'intensity': 70},
                           {'mz': 29, 'intensity': 45}]},
            {'name': 'Propan-2-ol',   'formula': 'C₃H₇OH',     'M_plus': 60,
             'fragments': [{'mz': 45, 'intensity': 75}, {'mz': 43, 'intensity': 55},
                           {'mz': 15, 'intensity': 30}]},
            {'name': 'Ethanal',       'formula': 'CH₃CHO',      'M_plus': 44,
             'fragments': [{'mz': 43, 'intensity': 100},{'mz': 29, 'intensity': 55},
                           {'mz': 15, 'intensity': 40}]},
            {'name': 'Propanone',     'formula': 'C₃H₆O',       'M_plus': 58,
             'fragments': [{'mz': 43, 'intensity': 100},{'mz': 15, 'intensity': 40}]},
            {'name': 'Ethanoic acid', 'formula': 'CH₃COOH',     'M_plus': 60,
             'fragments': [{'mz': 45, 'intensity': 60}, {'mz': 43, 'intensity': 30},
                           {'mz': 15, 'intensity': 25}]},
            {'name': 'Chloroethane',  'formula': 'C₂H₅Cl',      'M_plus': 64,
             'fragments': [{'mz': 29, 'intensity': 90}, {'mz': 27, 'intensity': 50}]},
            {'name': 'Bromoethane',   'formula': 'C₂H₅Br',      'M_plus': 108,
             'fragments': [{'mz': 29, 'intensity': 100},{'mz': 27, 'intensity': 55}]},
            {'name': 'Methylamine',   'formula': 'CH₃NH₂',      'M_plus': 31,
             'fragments': [{'mz': 30, 'intensity': 80}, {'mz': 28, 'intensity': 40}]},
            {'name': 'Ethylamine',    'formula': 'C₂H₅NH₂',     'M_plus': 45,
             'fragments': [{'mz': 44, 'intensity': 40}, {'mz': 30, 'intensity': 100},
                           {'mz': 28, 'intensity': 55}]},
            {'name': 'Butanone',      'formula': 'C₄H₈O',       'M_plus': 72,
             'fragments': [{'mz': 57, 'intensity': 70}, {'mz': 43, 'intensity': 100},
                           {'mz': 29, 'intensity': 60}]},
        ]
        
        self.mol = rnd.choice(molecules)
        self.molecule  = f"{self.mol['name']} ({self.mol['formula']})"
        self.M_plus    = self.mol['M_plus']
        self.fragments = self.mol['fragments']
        self.answer    = self.M_plus  # numerical answer
        
        self.description = (
            f"The mass spectrum of an organic compound is shown. "
            f"The compound is {self.mol['name']}. "
            f"What is the m/z value of the molecular ion peak (M⁺)?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "Mass spectrometry"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.mol['name']}, formula {self.mol['formula']}}} &\\\\"
            "\\text{Molecular ion (M⁺): molecule minus one electron} &\\\\"
            f"M^+ &= {self.M_plus}\\\\"
            "\\text{The highest m/z peak (ignoring isotope peaks)} &\\\\"
            f"\\text{{corresponds to M⁺ = {self.M_plus}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Draw fragment peaks
        for frag in self.fragments:
            draw_mass_spectrum_peak(ax, frag['mz'], frag['intensity'],
                                   width=0.8, color='steelblue', label_offset=3)
        
        # Draw M+ peak — labelled as M⁺ but WITHOUT its m/z value in the label
        draw_mass_spectrum_peak(ax, self.M_plus, 100, width=0.8,
                               color='darkblue', label_offset=5)
        ax.text(self.M_plus, 110, 'M⁺', fontsize=12, ha='center',
               fontweight='bold', color='red')
        
        ax.set_xlabel('m/z (mass-to-charge ratio)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative Intensity (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum', fontsize=16, fontweight='bold')
        
        ax.set_xlim(0, self.M_plus + 15)
        ax.set_ylim(0, 125)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem039:
    """
    Chapter 22: IR spectrum with functional groups
    Visual: IR spectrum with absorption dips but NO text annotation labels
            Student identifies the wavenumber of a specified absorption
    Answer: numerical wavenumber (cm⁻¹)
    """
    
    def __init__(self):
        molecules = [
            {'name': 'Ethanoic acid', 'formula': 'CH₃COOH',
             'peaks': [{'wn': 3000, 'assignment': 'O-H (carboxylic acid, broad)', 'width': 500, 'depth': 65},
                       {'wn': 1715, 'assignment': 'C=O (carbonyl)', 'width': 80, 'depth': 60},
                       {'wn': 1200, 'assignment': 'C-O', 'width': 80, 'depth': 40}],
             'ask': 1, 'ask_group': 'C=O stretch'},
            {'name': 'Ethanol', 'formula': 'CH₃CH₂OH',
             'peaks': [{'wn': 3350, 'assignment': 'O-H (alcohol, broad)', 'width': 300, 'depth': 60},
                       {'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30},
                       {'wn': 1050, 'assignment': 'C-O stretch', 'width': 80, 'depth': 40}],
             'ask': 0, 'ask_group': 'O-H stretch'},
            {'name': 'Propanal', 'formula': 'CH₃CH₂CHO',
             'peaks': [{'wn': 2720, 'assignment': 'C-H (aldehyde)', 'width': 80, 'depth': 40},
                       {'wn': 1725, 'assignment': 'C=O (aldehyde)', 'width': 80, 'depth': 65},
                       {'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30}],
             'ask': 1, 'ask_group': 'C=O stretch'},
            {'name': 'Propan-1-amine', 'formula': 'CH₃CH₂CH₂NH₂',
             'peaks': [{'wn': 3350, 'assignment': 'N-H stretch', 'width': 200, 'depth': 50},
                       {'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30},
                       {'wn': 1590, 'assignment': 'N-H bend', 'width': 80, 'depth': 35}],
             'ask': 0, 'ask_group': 'N-H stretch'},
            {'name': 'Methyl ethanoate', 'formula': 'CH₃COOCH₃',
             'peaks': [{'wn': 1735, 'assignment': 'C=O (ester)', 'width': 80, 'depth': 65},
                       {'wn': 1240, 'assignment': 'C-O-C stretch', 'width': 100, 'depth': 50},
                       {'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30}],
             'ask': 0, 'ask_group': 'C=O stretch (ester)'},
            {'name': 'Propanoic acid', 'formula': 'CH₃CH₂COOH',
             'peaks': [{'wn': 2900, 'assignment': 'O-H (broad)', 'width': 500, 'depth': 60},
                       {'wn': 1710, 'assignment': 'C=O (acid)', 'width': 80, 'depth': 65},
                       {'wn': 1200, 'assignment': 'C-O', 'width': 80, 'depth': 40}],
             'ask': 1, 'ask_group': 'C=O stretch'},
            {'name': 'Benzaldehyde', 'formula': 'C₆H₅CHO',
             'peaks': [{'wn': 3060, 'assignment': 'C-H (aromatic)', 'width': 60, 'depth': 30},
                       {'wn': 2730, 'assignment': 'C-H (aldehyde)', 'width': 60, 'depth': 35},
                       {'wn': 1700, 'assignment': 'C=O (aldehyde)', 'width': 80, 'depth': 65}],
             'ask': 2, 'ask_group': 'C=O stretch'},
            {'name': 'Butanone', 'formula': 'C₄H₈O',
             'peaks': [{'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30},
                       {'wn': 1715, 'assignment': 'C=O (ketone)', 'width': 80, 'depth': 65},
                       {'wn': 1350, 'assignment': 'C-H bend', 'width': 60, 'depth': 25}],
             'ask': 1, 'ask_group': 'C=O stretch (ketone)'},
            {'name': 'Phenol', 'formula': 'C₆H₅OH',
             'peaks': [{'wn': 3300, 'assignment': 'O-H (phenol)', 'width': 200, 'depth': 55},
                       {'wn': 3060, 'assignment': 'C-H (aromatic)', 'width': 60, 'depth': 25},
                       {'wn': 1600, 'assignment': 'C=C (aromatic)', 'width': 80, 'depth': 35}],
             'ask': 0, 'ask_group': 'O-H stretch'},
            {'name': 'Ethylamine', 'formula': 'C₂H₅NH₂',
             'peaks': [{'wn': 3300, 'assignment': 'N-H stretch', 'width': 150, 'depth': 50},
                       {'wn': 2950, 'assignment': 'C-H stretch', 'width': 80, 'depth': 30},
                       {'wn': 1600, 'assignment': 'N-H bend', 'width': 80, 'depth': 35}],
             'ask': 0, 'ask_group': 'N-H stretch'},
        ]
        
        self.mol = rnd.choice(molecules)
        self.peaks      = self.mol['peaks']
        self.ask_idx    = self.mol['ask']
        self.ask_group  = self.mol['ask_group']
        self.answer     = self.peaks[self.ask_idx]['wn']
        
        self.description = (
            f"The IR spectrum of {self.mol['name']} ({self.mol['formula']}) is shown. "
            f"At what wavenumber (cm⁻¹) does the {self.ask_group} absorption appear?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "Infrared spectroscopy"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.mol['name']}}} &\\\\"
            f"\\text{{Target bond: {self.ask_group}}} &\\\\"
            f"\\text{{Absorption wavenumber: {self.answer} cm}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        wavenumbers = np.linspace(4000, 500, 1000)
        transmittance = np.ones_like(wavenumbers) * 90
        
        for peak in self.peaks:
            center = peak['wn']
            width  = peak.get('width', 100)
            depth  = peak.get('depth', 55)
            mask = np.abs(wavenumbers - center) < width
            transmittance[mask] -= depth * np.exp(
                -((wavenumbers[mask] - center) ** 2) / (2 * (width / 3) ** 2))
        
        ax.plot(wavenumbers, transmittance, 'b-', linewidth=2)
        
        for i, peak in enumerate(self.peaks):
            ax.axvline(x=peak['wn'], color='gray', linestyle=':', alpha=0.5, linewidth=1)
            ax.text(peak['wn'], 95, f"{peak['wn']}", fontsize=9, ha='center',
                   color='darkred', rotation=90, va='bottom')
        
        ax.set_xlabel('Wavenumber (cm⁻¹)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Transmittance (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'IR Spectrum of {self.mol["name"]}', fontsize=16, fontweight='bold')
        
        ax.set_xlim(4000, 500)
        ax.set_ylim(0, 100)
        ax.invert_xaxis()
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem040:
    """
    Chapter 22: ¹H NMR spectrum
    Visual: NMR spectrum with peaks at correct positions — NO assignment labels on peaks
    Answer: numerical integration ratio (e.g. how many H in peak at δ X)
    """
    
    def __init__(self):
        molecules = [
            {'name': 'Ethanol',       'formula': 'CH₃CH₂OH',
             'peaks': [{'shift': 1.2, 'integration': 3, 'splitting': 'triplet',  'assignment': 'CH₃'},
                       {'shift': 3.7, 'integration': 2, 'splitting': 'quartet',  'assignment': 'CH₂'},
                       {'shift': 5.3, 'integration': 1, 'splitting': 'singlet',  'assignment': 'OH'}],
             'ask_shift': 1.2, 'ask_H': 3},
            {'name': 'Ethanoic acid', 'formula': 'CH₃COOH',
             'peaks': [{'shift': 2.1, 'integration': 3, 'splitting': 'singlet',  'assignment': 'CH₃'},
                       {'shift': 11.4,'integration': 1, 'splitting': 'singlet',  'assignment': 'COOH'}],
             'ask_shift': 2.1, 'ask_H': 3},
            {'name': 'Methyl ethanoate','formula': 'CH₃COOCH₃',
             'peaks': [{'shift': 2.0, 'integration': 3, 'splitting': 'singlet',  'assignment': 'COCH₃'},
                       {'shift': 3.7, 'integration': 3, 'splitting': 'singlet',  'assignment': 'OCH₃'}],
             'ask_shift': 3.7, 'ask_H': 3},
            {'name': 'Propanone',     'formula': 'CH₃COCH₃',
             'peaks': [{'shift': 2.1, 'integration': 6, 'splitting': 'singlet',  'assignment': '2×CH₃'}],
             'ask_shift': 2.1, 'ask_H': 6},
            {'name': 'Chloroethane',  'formula': 'CH₃CH₂Cl',
             'peaks': [{'shift': 1.5, 'integration': 3, 'splitting': 'triplet',  'assignment': 'CH₃'},
                       {'shift': 3.5, 'integration': 2, 'splitting': 'quartet',  'assignment': 'CH₂Cl'}],
             'ask_shift': 3.5, 'ask_H': 2},
            {'name': 'Ethanal',       'formula': 'CH₃CHO',
             'peaks': [{'shift': 2.2, 'integration': 3, 'splitting': 'doublet',  'assignment': 'CH₃'},
                       {'shift': 9.8, 'integration': 1, 'splitting': 'quartet',  'assignment': 'CHO'}],
             'ask_shift': 2.2, 'ask_H': 3},
            {'name': '1,1-Dichloroethane','formula': 'CH₃CHCl₂',
             'peaks': [{'shift': 2.1, 'integration': 3, 'splitting': 'doublet',  'assignment': 'CH₃'},
                       {'shift': 5.9, 'integration': 1, 'splitting': 'quartet',  'assignment': 'CHCl₂'}],
             'ask_shift': 5.9, 'ask_H': 1},
            {'name': 'Propan-1-ol',   'formula': 'CH₃CH₂CH₂OH',
             'peaks': [{'shift': 0.9, 'integration': 3, 'splitting': 'triplet',  'assignment': 'CH₃'},
                       {'shift': 1.6, 'integration': 2, 'splitting': 'sextet',   'assignment': 'CH₂'},
                       {'shift': 3.4, 'integration': 2, 'splitting': 'triplet',  'assignment': 'CH₂OH'},
                       {'shift': 2.5, 'integration': 1, 'splitting': 'singlet',  'assignment': 'OH'}],
             'ask_shift': 3.4, 'ask_H': 2},
            {'name': 'Bromoethane',   'formula': 'CH₃CH₂Br',
             'peaks': [{'shift': 1.7, 'integration': 3, 'splitting': 'triplet',  'assignment': 'CH₃'},
                       {'shift': 3.4, 'integration': 2, 'splitting': 'quartet',  'assignment': 'CH₂Br'}],
             'ask_shift': 1.7, 'ask_H': 3},
            {'name': 'Dimethyl ether','formula': 'CH₃OCH₃',
             'peaks': [{'shift': 3.2, 'integration': 6, 'splitting': 'singlet',  'assignment': '2×CH₃'}],
             'ask_shift': 3.2, 'ask_H': 6},
        ]
        
        self.mol = rnd.choice(molecules)
        self.peaks     = self.mol['peaks']
        self.ask_shift = self.mol['ask_shift']
        self.answer    = self.mol['ask_H']  # numerical answer
        
        self.description = (
            f"The ¹H NMR spectrum of {self.mol['name']} ({self.mol['formula']}) is shown. "
            f"How many hydrogen atoms are responsible for the peak at δ = {self.ask_shift} ppm?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "NMR spectroscopy"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Compound: {self.mol['name']}}} &\\\\"
            f"\\text{{Peak at }} \\delta = {self.ask_shift}\\text{{ ppm}} &\\\\"
            + "".join([f"\\text{{Assignment: {p['assignment']} ({p['integration']}H)}} &\\\\" 
                       for p in self.peaks if p['shift'] == self.ask_shift]) +
            f"\\text{{Number of H: {self.answer}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        for peak in self.peaks:
            highlight = peak['shift'] == self.ask_shift
            draw_nmr_peak(ax, peak['shift'], peak['integration'],
                         splitting=peak['splitting'],
                         j_coupling=0.007, sigma=0.02, max_height=100)
            # Highlight the queried peak with a red box, others plain
            if highlight:
                ax.axvspan(peak['shift'] - 0.3, peak['shift'] + 0.3,
                          alpha=0.15, color='red')
        
        # Show δ values only (no assignment text)
        for peak in self.peaks:
            ax.text(peak['shift'], 107, f"δ {peak['shift']}", fontsize=10,
                   ha='center', fontweight='bold',
                   color='red' if peak['shift'] == self.ask_shift else 'black')
        
        ax.set_xlabel('δ (ppm)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Intensity', fontsize=14, fontweight='bold')
        ax.set_title(f'¹H NMR Spectrum of {self.mol["name"]}', fontsize=16, fontweight='bold')
        
        ax.set_xlim(12, 0)
        ax.set_ylim(0, 130)
        ax.set_yticks([])
        ax.grid(True, alpha=0.3, axis='x')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem041:
    """
    Topic: 23.1 Standard enthalpy changes
    Visual: Enthalpy profile diagram showing exothermic reaction
    Task: Calculate enthalpy change from profile
    """
    
    def __init__(self):
        self.reactant_E = rnd.randint(50, 100)
        self.product_E = rnd.randint(20, 50)
        self.activation_E = self.reactant_E + rnd.randint(30, 80)
        
        self.delta_H = self.product_E - self.reactant_E
        self.Ea = self.activation_E - self.reactant_E
        
        self.answer = self.delta_H
        
        self.description = (
            f"The enthalpy profile diagram shows an exothermic reaction. "
            f"Calculate the enthalpy change, ΔH, for this reaction in kJ mol⁻¹."
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Standard enthalpy changes"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Enthalpy change is calculated as:}} &\\\\"
            f"\\Delta H &= H_{{\\text{{products}}}} - H_{{\\text{{reactants}}}}\\\\"
            f"&= {self.product_E} - {self.reactant_E}\\\\"
            f"&= {self.delta_H}\\,\\text{{kJ mol}}^{{-1}}\\\\"
            f"\\text{{Since }} \\Delta H < 0, \\text{{ the reaction is exothermic.}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        profile_data = draw_enthalpy_profile(
            ax, self.reactant_E, self.product_E, self.activation_E,
            x_start=0, x_end=10, curve_smoothness=50
        )
        
        draw_vertical_annotation(
            ax, profile_data['reactant_x'] - 1, self.product_E, self.reactant_E,
            f"ΔH = {self.delta_H} kJ/mol", color='red', linewidth=2.5
        )
        
        draw_vertical_annotation(
            ax, profile_data['reactant_x'] + 0.5, self.reactant_E, self.activation_E,
            f"Ea = {self.Ea} kJ/mol", color='blue', linewidth=2.5
        )
        
        ax.set_ylim(0, self.activation_E * 1.2)
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem042:
    """
    Topic: 23.2 Hess's Law
    Visual: Hess's Law cycle diagram
    Task: Calculate enthalpy of formation using Hess's Law
    """
    
    def __init__(self):
        self.delta_Hc_X = -rnd.randint(800, 1200)
        self.delta_Hc_Y = -rnd.randint(1500, 2500)
        self.delta_Hc_Z = -rnd.randint(300, 600)
        
        self.delta_Hf = self.delta_Hc_X - (self.delta_Hc_Y + self.delta_Hc_Z)
        self.answer = round(self.delta_Hf, 1)
        
        self.description = (
            f"The diagram shows a Hess's Law cycle for the formation of compound XYZ. "
            f"Given the enthalpy changes of combustion, calculate ΔH°f for XYZ."
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Hess's Law"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Using Hess's Law:}} &\\\\"
            f"\\Delta H_f &= \\Delta H_c(\\text{{reactants}}) - \\Delta H_c(\\text{{products}})\\\\"
            f"&= [{self.delta_Hc_Y} + {self.delta_Hc_Z}] - {self.delta_Hc_X}\\\\"
            f"&= {self.delta_Hc_Y + self.delta_Hc_Z} - ({self.delta_Hc_X})\\\\"
            f"&= {self.answer}\\,\\text{{kJ mol}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        draw_labeled_box(ax, 1, 6, 3, 1, "X + Y + Z", facecolor='lightblue')
        draw_labeled_box(ax, 8, 6, 3, 1, "XYZ", facecolor='lightgreen')
        draw_labeled_box(ax, 4, 1.5, 4, 1, "CO₂ + H₂O", facecolor='lightyellow')
        
        draw_arrow(ax, 4, 6.5, 8, 6.5, label=f"ΔH°f = ?", 
                  label_position='above', color='red', linewidth=2.5)
        
        draw_arrow(ax, 2.5, 6, 6, 2.5, label=f"ΔH°c(Y+Z)\n{self.delta_Hc_Y + self.delta_Hc_Z} kJ/mol",
                  label_position='side', color='blue', linewidth=2)
        
        draw_arrow(ax, 9.5, 6, 6, 2.5, label=f"ΔH°c(XYZ)\n{self.delta_Hc_X} kJ/mol",
                  label_position='side', color='blue', linewidth=2)
        
        ax.set_title("Hess's Law Cycle", fontsize=16, fontweight='bold', pad=20)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem043:
    """
    Topic: 23.3 Bond energy
    Visual: Molecular structures showing bonds to break and form
    Task: Calculate enthalpy change using bond energies
    """
    
    def __init__(self):
        self.BE_CH = rnd.randint(410, 415)
        self.BE_HH = rnd.randint(435, 438)
        self.BE_CC = rnd.randint(345, 350)
        
        bonds_broken = 4 * self.BE_CH + self.BE_HH
        bonds_formed = self.BE_CC + 6 * self.BE_CH
        
        self.delta_H = bonds_broken - bonds_formed
        self.answer = round(self.delta_H, 1)
        
        self.description = (
            f"Calculate the enthalpy change for the reaction: CH₄ + H₂ → C₂H₆ "
            f"using the bond energies shown in the diagram."
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Bond energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Bonds broken:}} &\\\\"
            f"4 \\times \\text{{C-H}} + 1 \\times \\text{{H-H}} &= 4({self.BE_CH}) + {self.BE_HH}\\\\"
            f"&= {bonds_broken}\\,\\text{{kJ mol}}^{{-1}}\\\\"
            f"\\text{{Bonds formed:}} &\\\\"
            f"1 \\times \\text{{C-C}} + 6 \\times \\text{{C-H}} &= {self.BE_CC} + 6({self.BE_CH})\\\\"
            f"&= {bonds_formed}\\,\\text{{kJ mol}}^{{-1}}\\\\"
            f"\\Delta H &= \\text{{bonds broken}} - \\text{{bonds formed}}\\\\"
            f"&= {bonds_broken} - {bonds_formed}\\\\"
            f"&= {self.answer}\\,\\text{{kJ mol}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_formula_label(ax, 2, 4, "CH₄", fontsize=18, weight='bold')
        add_formula_label(ax, 2, 2.5, f"C-H: {self.BE_CH} kJ/mol", fontsize=12)
        
        add_formula_label(ax, 5, 4, "+", fontsize=20, weight='bold')
        
        add_formula_label(ax, 7, 4, "H₂", fontsize=18, weight='bold')
        add_formula_label(ax, 7, 2.5, f"H-H: {self.BE_HH} kJ/mol", fontsize=12)
        
        draw_arrow(ax, 8.5, 3, 9.5, 3, color='black', linewidth=3)
        
        add_formula_label(ax, 11, 4, "C₂H₆", fontsize=18, weight='bold')
        add_formula_label(ax, 11, 2.5, f"C-C: {self.BE_CC} kJ/mol", fontsize=12)
        add_formula_label(ax, 11, 2, f"C-H: {self.BE_CH} kJ/mol", fontsize=12)
        
        ax.set_title("Bond Energy Calculation", fontsize=16, fontweight='bold', pad=20)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem044:
    """
    Topic: 23.4 Entropy and free energy
    Visual: Graph showing ΔG vs temperature — crossover point NOT labelled
    Answer: numerical temperature T (K) at which ΔG = 0
    """
    
    def __init__(self):
        # 12 varied scenarios
        scenarios = [
            (100, 0.25), (120, 0.30), ( 80, 0.20), (150, 0.50),
            ( 90, 0.45), (110, 0.40), (200, 0.50), ( 60, 0.20),
            (140, 0.35), ( 75, 0.25), (160, 0.40), (130, 0.26),
        ]
        self.delta_H, self.delta_S = rnd.choice(scenarios)
        self.T_equilibrium = self.delta_H / self.delta_S
        self.answer = round(self.T_equilibrium, 0)
        
        self.description = (
            f"The graph shows how Gibbs free energy (ΔG) varies with temperature for a reaction "
            f"where ΔH = +{self.delta_H} kJ mol⁻¹ and ΔS = +{self.delta_S} kJ mol⁻¹ K⁻¹. "
            f"At what temperature (in K, to the nearest whole number) does the reaction become spontaneous?"
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Entropy and free energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{At the crossover: } \\Delta G &= 0\\\\"
            "\\Delta G &= \\Delta H - T\\Delta S\\\\"
            f"0 &= {self.delta_H} - T \\times {self.delta_S}\\\\"
            f"T &= \\frac{{{self.delta_H}}}{{{self.delta_S}}}\\\\"
            f"&= {self.answer}\\,\\text{{K}}\\\\"
            f"\\text{{Reaction is spontaneous when }} T > {self.answer}\\,\\text{{K}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        T_range = np.linspace(0, self.T_equilibrium * 1.6, 200)
        delta_G = self.delta_H - T_range * self.delta_S
        
        draw_line_graph(ax, T_range, delta_G, color='blue', linewidth=3,
                       xlabel='Temperature (K)', ylabel='ΔG (kJ mol⁻¹)',
                       title='Gibbs Free Energy vs Temperature')
        
        ax.axhline(0, color='black', linewidth=2, linestyle='--')
        ax.axvline(self.T_equilibrium, color='red', linewidth=1.5, linestyle='--', alpha=0.5)
        ax.plot(self.T_equilibrium, 0, 'ro', markersize=10)
        
        # Region labels only
        ax.text(self.T_equilibrium * 0.4, self.delta_H * 0.7,
               'Non-spontaneous\n(ΔG > 0)', fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
        ax.text(self.T_equilibrium * 1.25, -self.delta_H * 0.25,
               'Spontaneous\n(ΔG < 0)', fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem045:
    """
    Topic: 24.1 Redox reactions
    Visual: Half-cell diagram
    Task: Calculate standard cell potential
    """
    
    def __init__(self):
        half_cells = [
            ("Zn²⁺/Zn", -0.76),
            ("Fe²⁺/Fe", -0.44),
            ("Cu²⁺/Cu", +0.34),
            ("Ag⁺/Ag", +0.80),
            ("Fe³⁺/Fe²⁺", +0.77),
            ("MnO₄⁻/Mn²⁺", +1.51)
        ]
        
        self.half_cell_1 = rnd.choice(half_cells)
        remaining = [hc for hc in half_cells if hc != self.half_cell_1]
        self.half_cell_2 = rnd.choice(remaining)
        
        self.E_cell = self.half_cell_2[1] - self.half_cell_1[1]
        self.answer = round(self.E_cell, 2)
        
        self.description = (
            f"Calculate the standard cell potential (E°cell) for a cell consisting of "
            f"{self.half_cell_1[0]} and {self.half_cell_2[0]} half-cells."
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Redox reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"E^\\circ_{{\\text{{cell}}}} &= E^\\circ_{{\\text{{cathode}}}} - E^\\circ_{{\\text{{anode}}}}\\\\"
            f"&= {self.half_cell_2[1]} - ({self.half_cell_1[1]})\\\\"
            f"&= {self.answer}\\,\\text{{V}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        draw_beaker(ax, 1, 2, width=3, height=4, liquid_height=3, 
                   liquid_color='lightblue', beaker_linewidth=2)
        add_formula_label(ax, 2.5, 5.5, self.half_cell_1[0], fontsize=14, weight='bold')
        add_formula_label(ax, 2.5, 1, f"E° = {self.half_cell_1[1]} V", fontsize=12)
        
        draw_beaker(ax, 8, 2, width=3, height=4, liquid_height=3, 
                   liquid_color='lightgreen', beaker_linewidth=2)
        add_formula_label(ax, 9.5, 5.5, self.half_cell_2[0], fontsize=14, weight='bold')
        add_formula_label(ax, 9.5, 1, f"E° = {self.half_cell_2[1]} V", fontsize=12)
        
        ax.plot([4, 8], [4, 4], 'k-', linewidth=3)
        add_formula_label(ax, 6, 4.5, "Salt bridge", fontsize=11)
        
        draw_arrow(ax, 6, 7, 7, 7, label=f"e⁻", color='red', linewidth=2.5)
        
        add_title_box(ax, 6, 7.5, "Electrochemical Cell", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem046:
    """
    Topic: 24.2 Electrolysis
    Visual: Electrolysis cell diagram
    Task: Calculate mass of product formed during electrolysis
    """
    
    def __init__(self):
        self.current = rnd.randint(2, 10)
        self.time_min = rnd.randint(20, 60)
        self.time_s = self.time_min * 60
        
        self.charge = self.current * self.time_s
        self.moles_e = self.charge / 96500
        
        self.element = rnd.choice([
            ("Cu", 63.5, 2),
            ("Ag", 108, 1),
            ("Al", 27, 3),
            ("Zn", 65, 2)
        ])
        
        self.mass = (self.moles_e / self.element[2]) * self.element[1]
        self.answer = round(self.mass, 2)
        
        self.description = (
            f"In the electrolysis of {self.element[0]}²⁺ solution, a current of {self.current} A "
            f"flows for {self.time_min} minutes. Calculate the mass of {self.element[0]} deposited."
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"Q &= I \\times t = {self.current} \\times {self.time_s} = {self.charge}\\,\\text{{C}}\\\\"
            f"\\text{{Moles of electrons}} &= \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{96500}} = {round(self.moles_e, 4)}\\\\"
            f"\\text{{Moles of {self.element[0]}}} &= \\frac{{\\text{{moles of e}}^-}}{{{self.element[2]}}} = {round(self.moles_e / self.element[2], 4)}\\\\"
            f"\\text{{Mass}} &= n \\times M = {round(self.moles_e / self.element[2], 4)} \\times {self.element[1]}\\\\"
            f"&= {self.answer}\\,\\text{{g}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        draw_beaker(ax, 2, 2, width=6, height=5, liquid_height=4, 
                   liquid_color='lightblue', beaker_linewidth=3)
        
        ax.plot([3.5, 3.5], [6.5, 2], 'gray', linewidth=8)
        ax.plot([6.5, 6.5], [6.5, 2], 'gray', linewidth=8)
        
        add_formula_label(ax, 3.5, 7, "−", fontsize=24, weight='bold', color='blue')
        add_formula_label(ax, 6.5, 7, "+", fontsize=24, weight='bold', color='red')
        
        add_formula_label(ax, 5, 3.5, f"{self.element[0]}²⁺(aq)", fontsize=14)
        
        ax.plot([3.5, 3.5], [7, 8.5], 'k-', linewidth=3)
        ax.plot([6.5, 6.5], [7, 8.5], 'k-', linewidth=3)
        ax.plot([3.5, 6.5], [8.5, 8.5], 'k-', linewidth=3)
        
        draw_labeled_box(ax, 4, 8.5, 2, 0.8, f"{self.current} A\n{self.time_min} min",
                        facecolor='yellow', edgecolor='black', linewidth=2)
        
        add_title_box(ax, 5, 9.5, "Electrolysis Cell", fontsize=16)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem047:
    """
    Topic: 25.1 Chemical equilibria
    Visual: Concentration vs time graph showing equilibrium
    Task: Determine equilibrium concentrations from graph
    """
    
    def __init__(self):
        self.initial_A = round(rnd.uniform(1.0, 2.0), 2)
        self.initial_B = round(rnd.uniform(1.0, 2.0), 2)
        
        self.eq_A = round(self.initial_A * rnd.uniform(0.3, 0.6), 2)
        self.eq_B = round(self.initial_B * rnd.uniform(0.3, 0.6), 2)
        self.eq_C = round((self.initial_A - self.eq_A), 2)
        
        self.answer = self.eq_C
        
        self.description = (
            f"The graph shows concentration changes for the reaction A + B ⇌ C. "
            f"What is the equilibrium concentration of C?"
        )
        
        self.topic = "Equilibria"
        self.subtopic = "Chemical equilibria"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the graph at equilibrium:}} &\\\\"
            f"[\\text{{A}}]_{{eq}} &= {self.eq_A}\\,\\text{{mol dm}}^{{-3}}\\\\"
            f"[\\text{{B}}]_{{eq}} &= {self.eq_B}\\,\\text{{mol dm}}^{{-3}}\\\\"
            f"[\\text{{C}}]_{{eq}} &= {self.eq_C}\\,\\text{{mol dm}}^{{-3}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        time = np.linspace(0, 10, 100)
        
        conc_A = self.eq_A + (self.initial_A - self.eq_A) * np.exp(-0.5 * time)
        conc_B = self.eq_B + (self.initial_B - self.eq_B) * np.exp(-0.5 * time)
        conc_C = self.eq_C * (1 - np.exp(-0.5 * time))
        
        ax.plot(time, conc_A, 'b-', linewidth=2.5, label='[A]')
        ax.plot(time, conc_B, 'r-', linewidth=2.5, label='[B]')
        ax.plot(time, conc_C, 'g-', linewidth=2.5, label='[C]')
        
        ax.axvline(7, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(7, max(self.initial_A, self.initial_B) * 0.9, 'Equilibrium', 
               rotation=90, va='bottom', fontsize=11)
        
        ax.set_xlabel('Time', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time', fontsize=16, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem048:
    """
    Topic: 25.2 Equilibrium constant Kc
    Visual: Equilibrium expression and data table
    Task: Calculate Kc from equilibrium concentrations
    """
    
    def __init__(self):
        self.eq_A = round(rnd.uniform(0.2, 0.8), 2)
        self.eq_B = round(rnd.uniform(0.2, 0.8), 2)
        self.eq_C = round(rnd.uniform(0.5, 1.5), 2)
        self.eq_D = round(rnd.uniform(0.5, 1.5), 2)
        
        self.Kc = (self.eq_C * self.eq_D) / (self.eq_A * self.eq_B)
        self.answer = round(self.Kc, 2)
        
        self.description = (
            f"For the equilibrium A + B ⇌ C + D, the equilibrium concentrations are shown. "
            f"Calculate the equilibrium constant Kc."
        )
        
        self.topic = "Equilibria"
        self.subtopic = "Equilibrium constant Kc"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"K_c &= \\frac{{[\\text{{C}}][\\text{{D}}]}}{{[\\text{{A}}][\\text{{B}}]}}\\\\"
            f"&= \\frac{{({self.eq_C})({self.eq_D})}}{{({self.eq_A})({self.eq_B})}}\\\\"
            f"&= \\frac{{{round(self.eq_C * self.eq_D, 4)}}}{{{round(self.eq_A * self.eq_B, 4)}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7, "A + B ⇌ C + D", fontsize=18)
        
        table_data = [
            ["Species", "Conc. / mol dm⁻³"],
            ["A", f"{self.eq_A}"],
            ["B", f"{self.eq_B}"],
            ["C", f"{self.eq_C}"],
            ["D", f"{self.eq_D}"]
        ]
        
        draw_data_table(ax, table_data, start_x=2, start_y=5.5, 
                       cell_width=3, cell_height=0.6, header_color='lightblue')
        
        add_formula_label(ax, 5, 1.5, "Kc = [C][D] / [A][B]", fontsize=16, weight='bold',
                         bbox_style=dict(boxstyle='round', facecolor='lightyellow', pad=0.5))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem049:
    """
    Topic: 26.1 Rate of reaction
    Visual: Concentration-time graph with tangent
    Task: Calculate rate of reaction from gradient
    """
    
    def __init__(self):
        self.initial_conc = round(rnd.uniform(1.5, 2.5), 2)
        self.k = round(rnd.uniform(0.1, 0.3), 3)
        
        self.t_point = 5
        self.conc_at_t = self.initial_conc * np.exp(-self.k * self.t_point)
        self.rate = -self.k * self.conc_at_t
        
        self.answer = round(abs(self.rate), 4)
        
        self.description = (
            f"The graph shows how concentration varies with time. "
            f"Calculate the rate of reaction at t = {self.t_point} seconds."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Rate of reaction"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Rate at t = {self.t_point}s is the gradient of the tangent:}} &\\\\"
            f"\\text{{Rate}} &= -\\frac{{d[\\text{{A}}]}}{{dt}}\\\\"
            f"&= {self.answer}\\,\\text{{mol dm}}^{{-3}}\\,\\text{{s}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        time = np.linspace(0, 20, 100)
        conc = self.initial_conc * np.exp(-self.k * time)
        
        ax.plot(time, conc, 'b-', linewidth=2.5)
        
        tangent_x = np.array([self.t_point - 2, self.t_point + 2])
        tangent_y = self.conc_at_t + self.rate * (tangent_x - self.t_point)
        ax.plot(tangent_x, tangent_y, 'r--', linewidth=2, label='Tangent')
        
        ax.plot(self.t_point, self.conc_at_t, 'ro', markersize=10)
        
        ax.set_xlabel('Time (s)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time', fontsize=16, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 20)
        ax.set_ylim(0, self.initial_conc * 1.1)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem050:
    """
    Topic: 26.2 Order of reaction and rate equations
    Visual: Graph showing effect of concentration on rate
    Task: Determine order of reaction from graph
    """
    
    def __init__(self):
        self.order = rnd.choice([0, 1, 2])
        
        concentrations = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        
        if self.order == 0:
            rates = np.full_like(concentrations, 0.05)
            self.answer = 0
            self.explanation = "zero order (rate independent of concentration)"
        elif self.order == 1:
            rates = 0.5 * concentrations
            self.answer = 1
            self.explanation = "first order (rate ∝ [A])"
        else:
            rates = 5 * concentrations**2
            self.answer = 2
            self.explanation = "second order (rate ∝ [A]²)"
        
        self.concentrations = concentrations
        self.rates = rates
        
        self.description = (
            f"The graph shows how the initial rate varies with concentration of reactant A. "
            f"Determine the order of reaction with respect to A."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Order of reaction and rate equations"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the graph:}} &\\\\"
            f"\\text{{The reaction is {self.explanation}}} &\\\\"
            f"\\text{{Order}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        ax.plot(self.concentrations, self.rates, 'bo-', markersize=10, linewidth=2.5)
        
        ax.set_xlabel('[A] (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Rate (mol dm⁻³ s⁻¹)', fontsize=14, fontweight='bold')
        ax.set_title('Rate vs Concentration', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 0.6)
        ax.set_ylim(0, max(self.rates) * 1.2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
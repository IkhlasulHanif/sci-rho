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
        
        # REMOVED: Answer label that gave away the solution
        # Students must calculate which reagent is limiting themselves
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem010:
    """
    Chapter 3.2: Polar bonds with electronegativity
    """
    
    def __init__(self):
        self.molecules = [
            {'name': 'HCl', 'atoms': ['H', 'Cl'], 'EN': [2.1, 3.0]},
            {'name': 'HF', 'atoms': ['H', 'F'], 'EN': [2.1, 4.0]},
            {'name': 'HBr', 'atoms': ['H', 'Br'], 'EN': [2.1, 2.8]},
        ]
        
        self.molecule = rnd.choice(self.molecules)
        self.delta_EN = abs(self.molecule['EN'][1] - self.molecule['EN'][0])
        self.answer = f"δ+ on {self.molecule['atoms'][0]}, δ- on {self.molecule['atoms'][1]}"
        
        self.description = (
            f"The diagram shows the {self.molecule['name']} molecule with electronegativity values. "
            f"Identify the partial charges on each atom."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Electronegativity and bond polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Electronegativity of {self.molecule['atoms'][0]}}} &= {self.molecule['EN'][0]}\\\\"
            f"\\text{{Electronegativity of {self.molecule['atoms'][1]}}} &= {self.molecule['EN'][1]}\\\\"
            f"\\Delta EN &= |{self.molecule['EN'][1]} - {self.molecule['EN'][0]}| = {round(self.delta_EN, 2)}\\\\"
            f"\\text{{Since {self.molecule['atoms'][1]} is more electronegative:}} &\\\\"
            f"\\text{{{self.molecule['atoms'][1]} has partial negative charge (δ-)}} &\\\\"
            f"\\text{{{self.molecule['atoms'][0]} has partial positive charge (δ+)}} &"
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
        
        add_charge_label(ax, x1, y1+0.8, 'δ+', fontsize=16, color='blue')
        add_charge_label(ax, x2, y2+0.8, 'δ-', fontsize=16, color='red')
        
        ax.text(x1, y1-0.9, f'EN = {self.molecule["EN"][0]}', 
               fontsize=12, ha='center', fontweight='bold')
        ax.text(x2, y2-0.9, f'EN = {self.molecule["EN"][1]}', 
               fontsize=12, ha='center', fontweight='bold')
        
        mid_x = (x1 + x2) / 2
        draw_arrow(ax, mid_x-0.5, y1-0.3, mid_x+0.5, y2-0.3, 
                  arrowstyle='->', color='green', linewidth=2, mutation_scale=20)
        ax.text(mid_x, y1-0.6, 'Dipole', fontsize=11, ha='center', 
               color='green', fontweight='bold')
        
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
        
        ax.text(0, 0, -2.5, f'Shape: {self.shape}', fontsize=14, 
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
        
        ax.text(0, 0, -2.5, f'Shape: {self.shape}', fontsize=14, 
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
        
        ax.text(0, 0, -2.5, f'Shape: {self.shape}', fontsize=14, 
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
    Chapter 3.4: Hydrogen bonding in water
    """
    
    def __init__(self):
        self.molecule = 'H₂O'
        self.answer = 'Hydrogen bonds between O and H atoms of adjacent molecules'
        
        self.description = (
            "The diagram shows hydrogen bonding between water molecules. "
            "Identify the type of intermolecular force shown."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Hydrogen bonding requires:} &\\\\"
            "\\text{1. H bonded to highly electronegative atom (O, N, or F)} &\\\\"
            "\\text{2. Lone pair on adjacent molecule} &\\\\"
            "\\text{In water:} &\\\\"
            "\\text{O is highly electronegative, creating δ- on O and δ+ on H} &\\\\"
            "\\text{Hydrogen bonds form between δ+ H and δ- O} &\\\\"
            "\\text{Represented by dashed lines}"
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
        
        ax.text(6, 1.5, 'Dashed lines = Hydrogen bonds', fontsize=13, 
               ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue', edgecolor='blue', linewidth=2))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem015:
    """
    Chapter 3.5: Metallic bonding structure
    """
    
    def __init__(self):
        self.metal = rnd.choice(['Sodium', 'Magnesium', 'Aluminum', 'Iron'])
        self.answer = 'Electrostatic attraction between metal cations and delocalized electrons'
        
        self.description = (
            f"The diagram shows the metallic bonding in {self.metal}. "
            f"Describe the bonding present."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Metallic bonding"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Metallic bonding consists of:} &\\\\"
            "\\text{1. Metal atoms lose valence electrons to form cations} &\\\\"
            "\\text{2. Electrons become delocalized (\"sea of electrons\")} &\\\\"
            "\\text{3. Electrostatic attraction between:} &\\\\"
            "\\text{   - Positive metal ions (cations)} &\\\\"
            "\\text{   - Negative delocalized electrons} &\\\\"
            "\\text{This structure explains electrical conductivity}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 5, 7.5, f'Metallic Bonding: {self.metal}', fontsize=16)
        
        for i in range(1, 10, 2):
            for j in range(1, 8, 2):
                draw_circle_atom(ax, i, j, 'M⁺', radius=0.35, 
                               color='silver', text_color='black', fontsize=12)
        
        np.random.seed(42)
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
                ax.text(ex, ey, 'e⁻', fontsize=7, ha='center', va='center', 
                       color='black', fontweight='bold')
        
        ax.text(5, 0.5, 'Yellow dots = Delocalized electrons ("sea of electrons")', 
               fontsize=11, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem016:
    """
    Chapter 3.6: Molecular polarity comparison
    """
    
    def __init__(self):
        self.molecules = [
            {'name': 'CO₂', 'polar': False, 'reason': 'Symmetrical, dipoles cancel'},
            {'name': 'H₂O', 'polar': True, 'reason': 'Bent shape, net dipole'},
        ]
        
        self.answer = 'CO₂ is non-polar (linear), H₂O is polar (bent)'
        
        self.description = (
            "The diagrams show CO₂ and H₂O molecules. "
            "Explain why one is polar and the other is non-polar."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Molecular polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{CO₂ (Linear):} &\\\\"
            "\\text{Two C=O bonds with dipoles in opposite directions} &\\\\"
            "\\text{Dipoles cancel out → Non-polar molecule} &\\\\[10pt]"
            "\\text{H₂O (Bent):} &\\\\"
            "\\text{Two O-H bonds with dipoles at 104.5° angle} &\\\\"
            "\\text{Dipoles do NOT cancel → Polar molecule} &\\\\"
            "\\text{Net dipole points toward oxygen}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, 'Molecular Polarity Comparison', fontsize=16)
        
        draw_circle_atom(ax, 2, 4, 'C', radius=0.4, color='black', text_color='white')
        draw_circle_atom(ax, 0.5, 4, 'O', radius=0.35, color='red', text_color='white')
        draw_circle_atom(ax, 3.5, 4, 'O', radius=0.35, color='red', text_color='white')
        
        draw_bond(ax, 0.85, 4, 1.6, 4, bond_type='double', linewidth=3)
        draw_bond(ax, 2.4, 4, 3.15, 4, bond_type='double', linewidth=3)
        
        draw_arrow(ax, 0.5, 3.4, 1.5, 3.4, arrowstyle='->', color='blue', linewidth=2)
        draw_arrow(ax, 3.5, 3.4, 2.5, 3.4, arrowstyle='->', color='blue', linewidth=2)
        
        ax.text(2, 2.5, 'CO₂: Linear\nDipoles Cancel\nNON-POLAR', 
               fontsize=11, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen'))
        
        draw_circle_atom(ax, 9, 4.5, 'O', radius=0.4, color='red', text_color='white')
        draw_circle_atom(ax, 8, 3.5, 'H', radius=0.3, color='lightblue', text_color='black')
        draw_circle_atom(ax, 10, 3.5, 'H', radius=0.3, color='lightblue', text_color='black')
        
        draw_bond(ax, 8.25, 3.65, 8.75, 4.25, bond_type='single', linewidth=3)
        draw_bond(ax, 9.75, 3.65, 9.25, 4.25, bond_type='single', linewidth=3)
        
        draw_arrow(ax, 8.5, 3.9, 8.8, 4.3, arrowstyle='->', color='blue', linewidth=2)
        draw_arrow(ax, 9.5, 3.9, 9.2, 4.3, arrowstyle='->', color='blue', linewidth=2)
        draw_arrow(ax, 9, 3, 9, 4, arrowstyle='->', color='red', linewidth=3)
        
        ax.text(9, 2.2, 'H₂O: Bent\nNet Dipole\nPOLAR', 
               fontsize=11, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightcoral'))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem017:
    """
    Chapter 3.7: Van der Waals forces and boiling points
    """
    
    def __init__(self):
        self.noble_gases = ['He', 'Ne', 'Ar', 'Kr', 'Xe']
        self.Mr_values = [4, 20, 40, 84, 131]
        self.bp_values = [-269, -246, -186, -153, -108]
        
        self.answer = 'Boiling point increases with Mr due to stronger Van der Waals forces'
        
        self.description = (
            "The graph shows boiling points of noble gases against relative molecular mass. "
            "Explain the trend observed."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Trend: Boiling point increases with Mr} &\\\\"
            "\\text{Explanation:} &\\\\"
            "\\text{1. Noble gases only have Van der Waals (dispersion) forces} &\\\\"
            "\\text{2. Larger molecules have more electrons} &\\\\"
            "\\text{3. More electrons → stronger temporary dipoles} &\\\\"
            "\\text{4. Stronger Van der Waals forces} &\\\\"
            "\\text{5. More energy needed to overcome forces} &\\\\"
            "\\text{6. Therefore, boiling point increases}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        draw_line_graph(ax, self.Mr_values, self.bp_values, 
                       color='darkblue', linewidth=3, marker='o', markersize=12,
                       xlabel='Relative Molecular Mass (Mr)', 
                       ylabel='Boiling Point (°C)',
                       title='Boiling Points of Noble Gases')
        
        for x, y, label in zip(self.Mr_values, self.bp_values, self.noble_gases):
            ax.text(x, y+10, label, fontsize=12, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem018:
    """
    Chapter 4.1: States of matter particle arrangements
    REFACTORED: Uses draw_circle_atom() for particles
    """
    
    def __init__(self):
        self.answer = 'Solid: fixed arrangement, Liquid: close but mobile, Gas: far apart and random'
        
        self.description = (
            "The diagram shows particle arrangements in three states of matter. "
            "Describe the differences between them."
        )
        
        self.topic = "States of matter"
        self.subtopic = "Particle model"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Solid:} &\\\\"
            "\\text{- Particles in fixed, regular arrangement} &\\\\"
            "\\text{- Vibrate about fixed positions} &\\\\"
            "\\text{- Strong forces between particles} &\\\\[10pt]"
            "\\text{Liquid:} &\\\\"
            "\\text{- Particles close together but can move} &\\\\"
            "\\text{- Random arrangement} &\\\\"
            "\\text{- Weaker forces than solid} &\\\\[10pt]"
            "\\text{Gas:} &\\\\"
            "\\text{- Particles far apart} &\\\\"
            "\\text{- Move randomly at high speed} &\\\\"
            "\\text{- Very weak forces between particles}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(1, 3, figsize=(15, 5))
        
        states = ['Solid', 'Liquid', 'Gas']
        
        for row in range(4):
            for col in range(4):
                x = col * 1.2 + 0.6
                y = row * 1.2 + 0.6
                draw_circle_atom(ax[0], x, y, '', radius=0.25, 
                               color='darkblue', show_symbol=False)
        
        ax[0].set_title('SOLID', fontsize=16, fontweight='bold')
        ax[0].set_xlim(0, 5)
        ax[0].set_ylim(0, 5)
        ax[0].axis('off')
        ax[0].text(2.5, -0.5, 'Regular arrangement\nFixed positions', 
                  fontsize=10, ha='center', style='italic')
        
        np.random.seed(42)
        for _ in range(16):
            x = np.random.uniform(0.5, 4.5)
            y = np.random.uniform(0.5, 4.5)
            draw_circle_atom(ax[1], x, y, '', radius=0.25, 
                           color='green', show_symbol=False)
        
        ax[1].set_title('LIQUID', fontsize=16, fontweight='bold')
        ax[1].set_xlim(0, 5)
        ax[1].set_ylim(0, 5)
        ax[1].axis('off')
        ax[1].text(2.5, -0.5, 'Random arrangement\nParticles mobile', 
                  fontsize=10, ha='center', style='italic')
        
        for _ in range(8):
            x = np.random.uniform(0.5, 4.5)
            y = np.random.uniform(0.5, 4.5)
            draw_circle_atom(ax[2], x, y, '', radius=0.2, 
                           color='red', show_symbol=False)
        
        ax[2].set_title('GAS', fontsize=16, fontweight='bold')
        ax[2].set_xlim(0, 5)
        ax[2].set_ylim(0, 5)
        ax[2].axis('off')
        ax[2].text(2.5, -0.5, 'Far apart\nRandom motion', 
                  fontsize=10, ha='center', style='italic')
        
        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem019:
    """
    Chapter 4.2: Heating curve with phase changes
    REFACTORED: Uses draw_line_graph()
    """
    
    def __init__(self):
        self.melting_point = rnd.randint(0, 50)
        self.boiling_point = rnd.randint(80, 120)
        
        self.answer = f'Melting point: {self.melting_point}°C, Boiling point: {self.boiling_point}°C'
        
        self.description = (
            "The heating curve shows temperature vs time for a pure substance. "
            "Identify the melting and boiling points."
        )
        
        self.topic = "States of matter"
        self.subtopic = "Phase changes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Heating curve features:} &\\\\"
            "\\text{1. Temperature rises → heating solid} &\\\\"
            f"\\text{{2. Plateau at {self.melting_point}°C → melting}} &\\\\"
            "\\text{3. Temperature rises → heating liquid} &\\\\"
            f"\\text{{4. Plateau at {self.boiling_point}°C → boiling}} &\\\\"
            "\\text{5. Temperature rises → heating gas} &\\\\"
            "\\text{Plateaus occur because energy used to break bonds,} &\\\\"
            "\\text{not increase kinetic energy}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        time = [0, 2, 4, 4, 6, 8, 8, 10]
        temp = [-20, self.melting_point-5, self.melting_point, self.melting_point, 
                self.boiling_point-10, self.boiling_point, self.boiling_point, self.boiling_point+20]
        
        draw_line_graph(ax, time, temp, color='darkred', linewidth=3, marker='',
                       xlabel='Time (minutes)', ylabel='Temperature (°C)',
                       title='Heating Curve')
        
        ax.axhline(y=self.melting_point, color='blue', linestyle='--', alpha=0.5)
        ax.axhline(y=self.boiling_point, color='green', linestyle='--', alpha=0.5)
        
        ax.text(3, self.melting_point+5, f'Melting\n{self.melting_point}°C', 
               fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightblue'))
        
        ax.text(7, self.boiling_point+5, f'Boiling\n{self.boiling_point}°C', 
               fontsize=12, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen'))
        
        ax.text(1, -10, 'Solid', fontsize=11, ha='center', style='italic')
        ax.text(5, (self.melting_point + self.boiling_point)/2, 'Liquid', 
               fontsize=11, ha='center', style='italic')
        ax.text(9, self.boiling_point+15, 'Gas', fontsize=11, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem020:
    """
    Chapter 5.1: Enthalpy profile diagram
    REFACTORED: Uses draw_enthalpy_profile() and draw_vertical_annotation()
    """
    
    def __init__(self):
        self.reactant_E = rnd.randint(40, 60)
        self.product_E = rnd.randint(10, 30)
        self.activation_E = rnd.randint(90, 120)
        
        self.delta_H = self.product_E - self.reactant_E
        self.Ea = self.activation_E - self.reactant_E
        
        self.answer = f'ΔH = {self.delta_H} kJ/mol, Ea = {self.Ea} kJ/mol'
        
        self.description = (
            "The enthalpy profile diagram is shown. "
            "Calculate ΔH and the activation energy (Ea)."
        )
        
        self.topic = "Energetics"
        self.subtopic = "Enthalpy changes"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Energy of reactants}} &= {self.reactant_E}\\,\\text{{kJ/mol}}\\\\"
            f"\\text{{Energy of products}} &= {self.product_E}\\,\\text{{kJ/mol}}\\\\"
            f"\\text{{Activation energy peak}} &= {self.activation_E}\\,\\text{{kJ/mol}}\\\\"
            "\\Delta H &= \\text{Products} - \\text{Reactants}\\\\"
            f"&= {self.product_E} - {self.reactant_E}\\\\"
            f"&= {self.delta_H}\\,\\text{{kJ/mol}}\\\\"
            "E_a &= \\text{Peak} - \\text{Reactants}\\\\"
            f"&= {self.activation_E} - {self.reactant_E}\\\\"
            f"&= {self.Ea}\\,\\text{{kJ/mol}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        profile = draw_enthalpy_profile(ax, self.reactant_E, self.product_E, 
                                        self.activation_E, x_start=0, x_end=10)
        
        draw_vertical_annotation(ax, 1, self.reactant_E, self.activation_E, 
                                f'Ea = {self.Ea} kJ/mol', color='red', label_offset=0.5)
        
        draw_vertical_annotation(ax, 8.5, self.reactant_E, self.product_E, 
                                f'ΔH = {self.delta_H} kJ/mol', color='green', label_offset=0.5)
        
        ax.text(profile['reactant_x'], self.reactant_E + 8, 'Reactants', 
               fontsize=14, ha='center', fontweight='bold')
        ax.text(profile['product_x'], self.product_E + 8, 'Products', 
               fontsize=14, ha='center', fontweight='bold')
        
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        ax.set_ylim(0, self.activation_E + 20)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem021:
    """
    Chapter 5.2: Hess's Law cycle
    REFACTORED: Uses draw_labeled_box() and draw_arrow()
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
    REFACTORED: Uses draw_labeled_box(), draw_beaker(), draw_arrow()
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
    REFACTORED: Uses draw_line_graph()
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
    REFACTORED: Uses draw_data_table()
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
    REFACTORED: Custom curve drawing
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
    REFACTORED: Uses draw_line_graph()
    """
    
    def __init__(self):
        self.initial_conc = rnd.uniform(1.5, 2.5)
        self.half_life = rnd.randint(5, 15)
        
        self.answer = f'{self.half_life} seconds'
        
        self.description = (
            "The graph shows concentration vs time for a first-order reaction. "
            "Determine the half-life."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Order of reaction"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{For first-order reaction:} &\\\\"
            "\\text{Half-life is constant} &\\\\"
            f"\\text{{Initial concentration}} &= {round(self.initial_conc, 2)}\\,\\text{{M}}\\\\"
            f"\\text{{After one half-life:}} &= {round(self.initial_conc/2, 2)}\\,\\text{{M}}\\\\"
            f"\\text{{Time taken}} &= {self.half_life}\\,\\text{{s}}\\\\"
            f"\\text{{Half-life}} &= {self.half_life}\\,\\text{{s}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        time = np.linspace(0, 60, 100)
        conc = self.initial_conc * np.exp(-np.log(2) * time / self.half_life)
        
        draw_line_graph(ax, time, conc, color='darkblue', linewidth=3, marker='',
                       xlabel='Time (s)', ylabel='Concentration (M)',
                       title='First-Order Reaction: Concentration vs Time')
        
        for i in range(1, 4):
            t = i * self.half_life
            c = self.initial_conc / (2 ** i)
            ax.axvline(x=t, color='red', linestyle='--', alpha=0.5)
            ax.axhline(y=c, color='red', linestyle='--', alpha=0.5)
            ax.plot(t, c, 'ro', markersize=10)
            ax.text(t, c + 0.1, f't½ = {self.half_life}s', fontsize=10, ha='center')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem027:
    """
    Chapter 9.1: Ionization energies across Period 3
    REFACTORED: Uses draw_bar_chart()
    """
    
    def __init__(self):
        self.elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
        self.IE_values = [496, 738, 578, 787, 1012, 1000, 1251, 1521]
        
        self.answer = 'General increase across period; dips at Al and S due to subshell effects'
        
        self.description = (
            "The bar chart shows first ionization energies across Period 3. "
            "Explain the general trend and deviations."
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in ionization energy"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{General trend: Ionization energy increases} &\\\\"
            "\\text{Reason: Increasing nuclear charge} &\\\\"
            "\\text{Deviation 1: Al lower than Mg} &\\\\"
            "\\text{Reason: Al electron in 3p (higher energy than 3s)} &\\\\"
            "\\text{Deviation 2: S lower than P} &\\\\"
            "\\text{Reason: S has paired electron (repulsion)} &"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        colors = ['white'] * len(self.elements)
        colors[2] = 'red'
        colors[5] = 'red'
        
        x_pos = np.arange(len(self.elements))
        draw_bar_chart(ax, x_pos, self.IE_values, self.elements, 
                      colors=colors, width=0.7,
                      xlabel='Element', ylabel='First Ionization Energy (kJ/mol)',
                      title='First Ionization Energies - Period 3')
        
        ax.annotate('', xy=(2, self.IE_values[2]), xytext=(2, self.IE_values[1]),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(2.3, (self.IE_values[1] + self.IE_values[2])/2, 'Dip\n(3p subshell)', 
               fontsize=10, color='red', fontweight='bold')
        
        ax.annotate('', xy=(5, self.IE_values[5]), xytext=(5, self.IE_values[4]),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(5.3, (self.IE_values[4] + self.IE_values[5])/2, 'Dip\n(paired e⁻)', 
               fontsize=10, color='red', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem028:
    """
    Chapter 9.2: Atomic radii across period
    REFACTORED: Uses draw_line_graph()
    """
    
    def __init__(self):
        self.elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl']
        self.radii = [186, 160, 143, 117, 110, 104, 99]
        
        self.answer = 'Atomic radius decreases across period due to increasing nuclear charge'
        
        self.description = (
            "The graph shows atomic radii across Period 3. "
            "Explain the trend."
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in atomic properties"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Trend: Atomic radius decreases} &\\\\"
            "\\text{Explanation:} &\\\\"
            "\\text{1. Same number of electron shells} &\\\\"
            "\\text{2. Nuclear charge increases} &\\\\"
            "\\text{3. Stronger attraction to outer electrons} &\\\\"
            "\\text{4. Electron cloud pulled closer to nucleus} &\\\\"
            "\\text{5. Atomic radius decreases}"
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
        
        for x, y, elem in zip(x_pos, self.radii, self.elements):
            ax.text(x, y+5, f'{y}', fontsize=10, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem029:
    """
    Chapter 11.1: Halogen displacement reactions
    REFACTORED: Uses draw_test_tube()
    """
    
    def __init__(self):
        reactions = [
            {'reagent': 'Cl₂', 'salt': 'KBr', 'color_before': 'colorless', 
             'color_after': 'orange', 'displaced': 'Br₂'},
            {'reagent': 'Br₂', 'salt': 'KI', 'color_before': 'colorless', 
             'color_after': 'brown', 'displaced': 'I₂'},
        ]
        
        self.reaction = rnd.choice(reactions)
        self.answer = f'{self.reaction["displaced"]} formed (color: {self.reaction["color_after"]})'
        
        self.description = (
            f"{self.reaction['reagent']} is added to {self.reaction['salt']} solution. "
            f"Describe the color change observed."
        )
        
        self.topic = "Group 17 (Halogens)"
        self.subtopic = "Halogen displacement reactions"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Reaction: {self.reaction['reagent']} + {self.reaction['salt']} → {self.reaction['displaced']}}} &\\\\"
            "\\text{Reason: More reactive halogen displaces less reactive} &\\\\"
            f"\\text{{Initial color: {self.reaction['color_before']}}} &\\\\"
            f"\\text{{Final color: {self.reaction['color_after']}}} &\\\\"
            f"\\text{{Product: {self.reaction['displaced']} in solution}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5.5, f'Halogen Displacement: {self.reaction["reagent"]} + {self.reaction["salt"]}', 
                     fontsize=14)
        
        color_map = {
            'colorless': 'white',
            'orange': 'orange',
            'brown': 'brown',
            'yellow': 'yellow'
        }
        
        draw_test_tube(ax, 2, 1, width=1.4, height=3, solution_height=2,
                      solution_color=color_map[self.reaction['color_before']])
        ax.text(2.7, 0.5, 'BEFORE', fontsize=12, ha='center', fontweight='bold')
        ax.text(2.7, 4.3, self.reaction['color_before'].capitalize(), 
               fontsize=11, ha='center', style='italic')
        
        draw_arrow(ax, 4, 3, 5.5, 3, arrowstyle='->', color='black', linewidth=3)
        ax.text(4.75, 3.5, 'Add\n' + self.reaction['reagent'], fontsize=10, ha='center', fontweight='bold')
        
        draw_test_tube(ax, 8.5, 1, width=1.4, height=3, solution_height=2,
                      solution_color=color_map[self.reaction['color_after']])
        ax.text(9.2, 0.5, 'AFTER', fontsize=12, ha='center', fontweight='bold')
        ax.text(9.2, 4.3, self.reaction['color_after'].capitalize(), 
               fontsize=11, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem030:
    """
    Chapter 13.1: Structural isomers
    REFACTORED: Uses draw_labeled_box()
    """
    
    def __init__(self):
        isomer_sets = [
            {'formula': 'C₄H₁₀', 'isomers': ['CH₃-CH₂-CH₂-CH₃', 'CH₃-CH(CH₃)-CH₃']},
            {'formula': 'C₅H₁₂', 'isomers': ['CH₃-CH₂-CH₂-CH₂-CH₃', 'CH₃-CH(CH₃)-CH₂-CH₃']},
        ]
        
        self.set = rnd.choice(isomer_sets)
        self.answer = f'Two structural isomers of {self.set["formula"]}'
        
        self.description = (
            f"The diagram shows two structural isomers of {self.set['formula']}. "
            f"Identify the type of isomerism."
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Isomerism"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Molecular formula: {self.set['formula']}}} &\\\\"
            "\\text{Type: Structural isomerism (chain isomerism)} &\\\\"
            "\\text{Same molecular formula, different structural formulae} &\\\\"
            "\\text{Different carbon skeleton arrangement} &"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5.5, f'Structural Isomers: {self.set["formula"]}', fontsize=16)
        
        draw_labeled_box(ax, 1, 2.5, 4, 1.5, self.set['isomers'][0], 
                        'Isomer 1\n(straight chain)', facecolor='lightblue')
        
        draw_labeled_box(ax, 7, 2.5, 4, 1.5, self.set['isomers'][1], 
                        'Isomer 2\n(branched chain)', facecolor='lightgreen')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem031:
    """
    Chapter 13.2: E/Z isomerism
    REFACTORED: Uses draw_circle_atom(), draw_bond()
    """
    
    def __init__(self):
        self.molecule = 'but-2-ene'
        self.answer = 'E and Z isomers (geometric isomerism)'
        
        self.description = (
            f"Two isomers of {self.molecule} are shown. "
            f"Identify the type of stereoisomerism."
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Stereoisomerism"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Type: E/Z isomerism (geometric isomerism)} &\\\\"
            "\\text{Requirements:} &\\\\"
            "\\text{1. C=C double bond (restricted rotation)} &\\\\"
            "\\text{2. Different groups on each carbon} &\\\\"
            "\\text{E isomer: Higher priority groups on opposite sides} &\\\\"
            "\\text{Z isomer: Higher priority groups on same side}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 6, 5.5, 'E/Z Isomerism: But-2-ene', fontsize=16)
        
        draw_circle_atom(ax, 2, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 3.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 2.3, 3, 3.2, 3, bond_type='double', linewidth=3)
        
        ax.text(1.5, 3.5, 'CH₃', fontsize=12, ha='center', fontweight='bold')
        ax.text(1.5, 2.5, 'H', fontsize=12, ha='center', fontweight='bold')
        ax.text(4, 3.5, 'H', fontsize=12, ha='center', fontweight='bold')
        ax.text(4, 2.5, 'CH₃', fontsize=12, ha='center', fontweight='bold')
        
        draw_bond(ax, 2, 3, 1.7, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 2, 3, 1.7, 2.6, bond_type='single', linewidth=2)
        draw_bond(ax, 3.5, 3, 3.8, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 3.5, 3, 3.8, 2.6, bond_type='single', linewidth=2)
        
        ax.text(2.75, 1.5, 'E-isomer (trans)', fontsize=11, ha='center', 
               fontweight='bold', style='italic')
        
        draw_circle_atom(ax, 8.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 10, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 8.8, 3, 9.7, 3, bond_type='double', linewidth=3)
        
        ax.text(8, 3.5, 'CH₃', fontsize=12, ha='center', fontweight='bold')
        ax.text(8, 2.5, 'H', fontsize=12, ha='center', fontweight='bold')
        ax.text(10.5, 3.5, 'CH₃', fontsize=12, ha='center', fontweight='bold')
        ax.text(10.5, 2.5, 'H', fontsize=12, ha='center', fontweight='bold')
        
        draw_bond(ax, 8.5, 3, 8.2, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 8.5, 3, 8.2, 2.6, bond_type='single', linewidth=2)
        draw_bond(ax, 10, 3, 10.3, 3.4, bond_type='single', linewidth=2)
        draw_bond(ax, 10, 3, 10.3, 2.6, bond_type='single', linewidth=2)
        
        ax.text(9.25, 1.5, 'Z-isomer (cis)', fontsize=11, ha='center', 
               fontweight='bold', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem032:
    """
    Chapter 13.3: Homologous series
    REFACTORED: Uses draw_labeled_box()
    """
    
    def __init__(self):
        self.series = 'Alkenes'
        self.general_formula = 'CₙH₂ₙ'
        self.examples = [
            {'n': 2, 'formula': 'C₂H₄', 'name': 'Ethene'},
            {'n': 3, 'formula': 'C₃H₆', 'name': 'Propene'},
            {'n': 4, 'formula': 'C₄H₈', 'name': 'Butene'},
        ]
        
        self.answer = f'General formula: {self.general_formula}'
        
        self.description = (
            f"The diagram shows members of the {self.series} homologous series. "
            f"State the general formula."
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Homologous series"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Homologous series: {self.series}}} &\\\\"
            f"\\text{{General formula: {self.general_formula}}} &\\\\"
            "\\text{Characteristics:} &\\\\"
            "\\text{- Same functional group} &\\\\"
            "\\text{- Differ by CH₂ unit} &\\\\"
            "\\text{- Similar chemical properties} &\\\\"
            "\\text{- Gradual change in physical properties}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 6, 7.5, f'Homologous Series: {self.series}', fontsize=16)
        
        y_pos = 5.5
        for ex in self.examples:
            draw_labeled_box(ax, 3.5, y_pos, 5, 1, 
                           ex['formula'], f"{ex['name']} (n={ex['n']})", 
                           facecolor='lightblue')
            y_pos -= 1.5
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem033:
    """
    Chapter 14.1: Electrophilic addition mechanism
    REFACTORED: Uses draw_curly_arrow(), draw_circle_atom()
    """
    
    def __init__(self):
        self.reactant = 'CH₂=CH₂'
        self.electrophile = 'HBr'
        self.product = 'CH₃CH₂Br'
        
        self.answer = f'{self.product} formed via electrophilic addition'
        
        self.description = (
            f"The mechanism shows the reaction of {self.reactant} with {self.electrophile}. "
            f"Identify the mechanism type."
        )
        
        self.topic = "Hydrocarbons"
        self.subtopic = "Reactions of alkenes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Mechanism: Electrophilic addition} &\\\\"
            "\\text{Step 1: π electrons attack H⁺ (electrophile)} &\\\\"
            "\\text{Step 2: Carbocation intermediate forms} &\\\\"
            "\\text{Step 3: Br⁻ attacks carbocation} &\\\\"
            f"\\text{{Product: {self.product}}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 7, 5.5, f'Electrophilic Addition: {self.reactant} + {self.electrophile}', 
                     fontsize=14)
        
        draw_circle_atom(ax, 1.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_circle_atom(ax, 2.5, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 1.8, 3, 2.2, 3, bond_type='double', linewidth=3)
        ax.text(2, 2, 'Ethene', fontsize=10, ha='center', style='italic')
        
        ax.text(3.5, 3.5, 'H⁺', fontsize=14, ha='center', fontweight='bold', color='red')
        ax.text(3.5, 2.5, 'Br⁻', fontsize=14, ha='center', fontweight='bold', color='blue')
        
        draw_curly_arrow(ax, 2, 3.3, 3.3, 3.4, curvature=0.3, color='blue')
        ax.text(2.7, 3.8, 'Step 1', fontsize=9, color='blue', fontweight='bold')
        
        draw_arrow(ax, 4, 3, 5, 3, arrowstyle='->', color='black', linewidth=2)
        
        draw_circle_atom(ax, 6, 3, 'C⁺', radius=0.35, color='red', text_color='white')
        draw_circle_atom(ax, 7.2, 3, 'C', radius=0.3, color='black', text_color='white')
        draw_bond(ax, 6.35, 3, 6.9, 3, bond_type='single', linewidth=3)
        ax.text(5, 3.5, 'H', fontsize=12, ha='center', fontweight='bold')
        draw_bond(ax, 6, 3, 5.3, 3.4, bond_type='single', linewidth=2)
        ax.text(6.7, 2, 'Carbocation', fontsize=10, ha='center', style='italic')
        
        ax.text(8.2, 2.5, 'Br⁻', fontsize=14, ha='center', fontweight='bold', color='blue')
        draw_curly_arrow(ax, 8, 2.7, 6.2, 2.7, curvature=-0.3, color='blue')
        ax.text(7, 2, 'Step 2', fontsize=9, color='blue', fontweight='bold')
        
        draw_arrow(ax, 9, 3, 10, 3, arrowstyle='->', color='black', linewidth=2)
        
        ax.text(12, 3, self.product, fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', edgecolor='black'))
        ax.text(12, 2, 'Bromoethane', fontsize=10, ha='center', style='italic')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem034:
    """
    Chapter 15-17: Functional groups identification
    REFACTORED: Uses draw_functional_group(), draw_labeled_box()
    """
    
    def __init__(self):
        self.compounds = [
            {'name': 'Chloroethane', 'formula': 'CH₃CH₂Cl', 'group': 'Halogenoalkane', 'fg': '-Cl'},
            {'name': 'Ethanol', 'formula': 'CH₃CH₂OH', 'group': 'Alcohol', 'fg': '-OH'},
            {'name': 'Ethanal', 'formula': 'CH₃CHO', 'group': 'Aldehyde', 'fg': '-CHO'},
        ]
        
        self.answer = ', '.join([c['group'] for c in self.compounds])
        
        self.description = (
            "Identify the functional groups in the compounds shown."
        )
        
        self.topic = "Organic functional groups"
        self.subtopic = "Functional group identification"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.compounds[0]['name']}: {self.compounds[0]['group']} ({self.compounds[0]['fg']})}} &\\\\"
            f"\\text{{{self.compounds[1]['name']}: {self.compounds[1]['group']} ({self.compounds[1]['fg']})}} &\\\\"
            f"\\text{{{self.compounds[2]['name']}: {self.compounds[2]['group']} ({self.compounds[2]['fg']})}} &"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 7, 5.5, 'Functional Group Identification', fontsize=16)
        
        x_positions = [2, 7, 12]
        colors = ['lightcoral', 'lightblue', 'lightgreen']
        
        for i, (comp, x, color) in enumerate(zip(self.compounds, x_positions, colors)):
            draw_labeled_box(ax, x-1.5, 3, 3, 1.2,
                           comp['formula'], comp['name'],
                           facecolor=color)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
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
                varied_abundance = round(abundance + rnd.uniform(-10, 10), 1)
                varied_abundance = max(5, min(95, varied_abundance))
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
        self.question_type = "Short Answer"
        
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
            # Add the exact value label above the bar
            ax.text(mass, abundance + 1.5, f"{abundance}%", ha='center', va='bottom', 
                    fontsize=12, fontweight='bold', color='black')
        
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
        # Perturb each IE value +-5% so the graph differs meaningfully across instances
        raw = elements_ie[self.element]
        self.ie_values = [round(v * rnd.uniform(0.95, 1.05)) for v in raw]
        
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
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{From the graph, we observe the successive ionisation energies (IE).} &\\\\"
            "\\text{A massive proportional jump in energy indicates an electron is being} &\\\\"
            "\\text{removed from a new, inner principal quantum shell that is closer} &\\\\"
            "\\text{to the nucleus and experiencing significantly less shielding.} &\\\\"
            f"\\text{{Largest energy jump}} &= \\text{{IE}}_{{{self.outer_electrons}}} \\rightarrow \\text{{IE}}_{{{self.outer_electrons + 1}}} \\\\"
            f"\\text{{Valence electrons}} &= {self.outer_electrons} \\text{{ (electrons before the jump)}} \\\\"
            f"\\therefore \\text{{Group number}} &= {self.group}"
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
    Visual: Orbital box diagram built from randomised Z (no element symbol shown)
    Task:  Count total electrons (arrows) across all boxes to determine atomic number Z
    """

    @staticmethod
    def _build_boxes(Z):
        aufbau = [("1s",2),("2s",2),("2p",6),("3s",2),("3p",6),("4s",2)]
        boxes = {}
        remaining = Z
        for name, cap in aufbau:
            if remaining <= 0:
                break
            fill  = min(remaining, cap)
            n_orb = cap // 2
            elec  = [0] * (n_orb * 2)
            for i in range(min(fill, n_orb)):
                elec[i * 2] = 1
            for i in range(max(0, fill - n_orb)):
                elec[i * 2 + 1] = 1
            boxes[name] = elec
            remaining -= fill
        return boxes

    @staticmethod
    def _build_config_str(Z):
        sup = str.maketrans("0123456789","0123456789")
        sup2 = {"0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵",
                "6":"⁶","7":"⁷","8":"⁸","9":"⁹"}
        aufbau = [("1s",2),("2s",2),("2p",6),("3s",2),("3p",6),("4s",2)]
        parts, rem = [], Z
        for name, cap in aufbau:
            if rem <= 0: break
            fill = min(rem, cap)
            sup_fill = "".join(sup2[c] for c in str(fill))
            parts.append(f"{name}{sup_fill}")
            rem -= fill
        return " ".join(parts)

    def __init__(self):
        self.Z      = rnd.randint(3, 20)
        self.boxes  = self.__class__._build_boxes(self.Z)
        self.config = self.__class__._build_config_str(self.Z)
        self.answer = self.Z
        self.description = (
            "The orbital box diagram below represents the electron configuration of a neutral unknown atom. "
            "Based on the visual representation provided, determine the atomic number (Z) of this atom."
        )
        self.topic      = "Atomic structure"
        self.subtopic   = "Electrons, energy levels, and atomic orbitals"
        self.source     = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{In the diagram, each arrow represents one electron.} &\\\\"
            "\\text{For a neutral atom, the total number of electrons equals the atomic number (Z).} &\\\\"
            f"\\text{{Extracted configuration}} &= \\text{{{self.config}}} \\\\"
            f"\\text{{Total electrons counted}} &= {self.Z} \\\\"
            f"\\therefore \\text{{Atomic number (Z)}} &= {self.Z}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14); ax.set_ylim(0, 6); ax.axis("off")

        bw, bh, sp = 0.6, 0.8, 0.1
        y_base = 3.0; x_pos = 0.5

        for orbital, electrons in self.boxes.items():
            n_boxes = 1 if orbital.endswith("s") else 3
            ax.text(x_pos + (n_boxes*(bw+sp))/2, y_base - 0.8, orbital,
                    ha="center", va="top", fontsize=14, fontweight="bold")
            for i in range(n_boxes):
                bx = x_pos + i*(bw+sp)
                ax.add_patch(patches.Rectangle(
                    (bx, y_base), bw, bh,
                    linewidth=2, edgecolor="black", facecolor="white"))
                e_idx = i * 2
                up   = electrons[e_idx]     if e_idx     < len(electrons) else 0
                down = electrons[e_idx + 1] if e_idx + 1 < len(electrons) else 0
                if up:
                    ax.annotate("", xy=(bx+bw/3, y_base+bh-0.15),
                                xytext=(bx+bw/3, y_base+0.15),
                                arrowprops=dict(arrowstyle="->", lw=2, color="blue"))
                if down:
                    ax.annotate("", xy=(bx+2*bw/3, y_base+0.15),
                                xytext=(bx+2*bw/3, y_base+bh-0.15),
                                arrowprops=dict(arrowstyle="->", lw=2, color="red"))
            x_pos += n_boxes*(bw+sp) + 0.5

        add_title_box(ax, 7, 5.5, "Orbital Box Diagram -- Unknown Element", fontsize=16)
        ax.annotate("", xy=(0.2, 5.0), xytext=(0.2, 1.5),
                    arrowprops=dict(arrowstyle="->", lw=2.5, color="gray"))
        ax.text(0.2-0.8, 3.25, "Energy", rotation=90, va="center", ha="center",
                fontsize=14, fontweight="bold", color="gray")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()


class Chem004:
    """
    Topic: 1.1 Particles in the atom and atomic radius
    Visual: Diagram showing deflection of particles in an electric field
    Task: Identify which particle path corresponds to proton/neutron/electron
    """
    
    def __init__(self):
        self.q_mC = rnd.randint(1, 9)          # charge in mC (displayed)
        self.E_NC = rnd.randint(100, 900)       # field strength in N/C (displayed)
        self.F_N = round(self.q_mC / 1000 * self.E_NC, 3)   # force in N
        self.answer = self.F_N
        
        self.description = (
            f"The diagram shows a charged particle in a uniform electric field. "
            f"The charge and field strength are labelled on the diagram. "
            f"Calculate the electrostatic force on the particle (in N, to 3 d.p.)."
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Particles in the atom and atomic radius"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{From the diagram, we extract the given values:} &\\\\"
            f"\\text{{Charge }} (q) &= {self.q_mC} \\,\\text{{mC}} \\\\"
            f"\\text{{Electric field }} (E) &= {self.E_NC} \\,\\text{{N C}}^{{-1}} \\\\"
            "\\text{Convert the charge to Coulombs (C):} &\\\\"
            f"q &= {self.q_mC} \\times 10^{{-3}} \\,\\text{{C}} = {self.q_mC / 1000} \\,\\text{{C}} \\\\"
            "\\text{Using the electrostatic force equation } F = qE: &\\\\"
            f"F &= ({self.q_mC / 1000} \\,\\text{{C}}) \\times ({self.E_NC} \\,\\text{{N C}}^{{-1}}) \\\\"
            f"\\therefore F &= {self.F_N:.3f} \\,\\text{{N}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 8))
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 9)
        ax.axis('off')
        
        add_title_box(ax, 5.5, 8.5, 'Charged Particle in an Electric Field', fontsize=14)
        
        # Plates
        ax.plot([3, 8], [7.5, 7.5], 'r-', linewidth=8)
        ax.text(2.3, 7.5, '+', fontsize=22, color='red', ha='center', va='center', fontweight='bold')
        ax.plot([3, 8], [1.5, 1.5], 'b-', linewidth=8)
        ax.text(2.3, 1.5, '−', fontsize=22, color='blue', ha='center', va='center', fontweight='bold')
        
        ax.text(5.5, 7.2, f'E = {self.E_NC} N C⁻¹', fontsize=12, ha='center', color='gray',
               bbox=dict(boxstyle='round', facecolor='lightyellow'))
        
        # Field arrows
        for x in np.linspace(3.5, 7.5, 4):
            ax.annotate('', xy=(x, 2.0), xytext=(x, 7.0),
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray', alpha=0.5))
        
        # Particle
        draw_circle_atom(ax, 5.5, 4.5, f'q = {self.q_mC} mC', radius=0.6,
                        color='lightcoral', text_color='black')
                
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
        raw_IE = period_data[self.period]["IE"]
        # Perturb +-5% so graph varies meaningfully across instances
        self.IE_values = [round(v * rnd.uniform(0.95, 1.05)) for v in raw_IE]
        
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
        
        self.answer = self.IE_values[anomaly_idx]  # numerical: IE of anomaly element read from graph
        
        self.description = (
            f"The graph shows the first ionisation energies of the elements in Period {self.period}. "
            f"Use the graph to state the first ionisation energy of {self.anomaly_element} "
            f"(in kJ mol⁻¹, to the nearest whole number)."
        )
        
        self.topic = "Atomic structure"
        self.subtopic = "Ionisation energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701 Past Papers"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{From the graph, we observe the general increasing trend of ionisation energies.} &\\\\"
            f"\\text{{A red circle highlights the anomalous drop for {self.anomaly_element}.}} &\\\\"
            "\\text{This lower-than-expected value is physically explained by its electron configuration:} &\\\\"
            f"\\text{{{self.explanation}.}} &\\\\"
            "\\text{By tracing this specific data point to the y-axis, we extract the exact value:} &\\\\"
            f"\\text{{First ionisation energy}} &= {self.answer} \\,\\text{{kJ mol}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        x_values = list(range(1, len(self.elements) + 1))
        
        ax.plot(x_values, self.IE_values, 'ko-', markersize=10, linewidth=2)
        
        x_right = ax.get_xlim()[1]
        for i, (x, y, elem) in enumerate(zip(x_values, self.IE_values, self.elements)):
            ax.annotate(elem, xy=(x, y), xytext=(0, 15), 
                       textcoords='offset points', fontsize=12, ha='center', fontweight='bold')
            ax.axhline(y=y, linestyle='--', linewidth=0.8, alpha=0.3)  # optional guide line
            ax.text(x_right, y, f"{y}", va='center', ha='left', fontsize=9)
        
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
        self.atomic_number = rnd.randint(3, 54)
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
        self.question_type = "Short Answer"
        
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
    Topic: 2.1 Relative masses — Ar from mass spectrum
    Visual: Mass spectrum with randomised peak heights (abundance ±6%)
    Task: Calculate Ar from m/z peak heights read off the spectrum
    Variance: 7 elements × continuous abundance perturbation → effectively infinite
    """

    def __init__(self):
        element_pool = [
            {'name': 'Chlorine',  'isotopes': [(35, 75.8),  (37, 24.2)]},
            {'name': 'Boron',     'isotopes': [(10, 19.9),  (11, 80.1)]},
            {'name': 'Copper',    'isotopes': [(63, 69.2),  (65, 30.8)]},
            {'name': 'Bromine',   'isotopes': [(79, 50.7),  (81, 49.3)]},
            {'name': 'Gallium',   'isotopes': [(69, 60.1),  (71, 39.9)]},
            {'name': 'Lithium',   'isotopes': [(6,   7.6),  (7,  92.4)]},
            {'name': 'Silver',    'isotopes': [(107, 51.8), (109, 48.2)]},
        ]

        base = rnd.choice(element_pool)
        # Perturb first isotope abundance ±6 percentage points (clamped 5–95)
        base_ab = base['isotopes'][0][1]
        ab1 = round(max(5.0, min(95.0, base_ab + rnd.uniform(-6, 6))), 1)
        ab2 = round(100.0 - ab1, 1)
        self.element  = base
        self.isotopes = [(base['isotopes'][0][0], ab1),
                         (base['isotopes'][1][0], ab2)]

        total = sum(m * a for m, a in self.isotopes)
        self.answer = round(total / 100, 2)

        self.description = (
            f"The mass spectrum of {self.element['name']} is shown. "
            f"Read the relative intensities from the diagram and calculate "
            f"the relative atomic mass (Ar) of {self.element['name']}."
        )

        self.topic      = "Atoms, molecules and stoichiometry"
        self.subtopic   = "Relative masses"
        self.source     = "Adapted from Cambridge A-Level Chemistry 9701 past papers"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        # Note: Changed × to proper LaTeX \times
        calc_parts = " + ".join(f"({m} \\times {a})" for m, a in self.isotopes)
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{From the mass spectrum, we read the m/z value and abundance for each isotope:} \\\\"
            f"&\\text{{Isotope 1: m/z = {self.isotopes[0][0]}, Abundance = {self.isotopes[0][1]}\\text{{\\%}}}} \\\\"
            f"&\\text{{Isotope 2: m/z = {self.isotopes[1][0]}, Abundance = {self.isotopes[1][1]}\\text{{\\%}}}} \\\\"
            "&\\text{The relative atomic mass } (A_r) \\text{ is the weighted average:} \\\\"
            "A_r &= \\frac{\\sum(\\text{isotope mass} \\times \\text{abundance})}{100}\\\\"
            f"A_r &= \\frac{{{calc_parts}}}{{100}}\\\\"
            f"A_r &= \\frac{{{round(total, 2)}}}{{100}}\\\\"
            f"A_r &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))

        for mass, abundance in self.isotopes:
            draw_mass_spectrum_peak(ax, mass, abundance, width=0.8, color='darkblue')
            # Add exact abundance numerical text slightly above the peak
            ax.text(mass, abundance + 1.5, f"{abundance}%", 
                    ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkblue')

        masses = [iso[0] for iso in self.isotopes]
        ax.set_xlabel('m/z (mass-to-charge ratio)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative Intensity (%)',     fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum of {self.element["name"]}',
                     fontsize=16, fontweight='bold')
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
            {'formula': 'CH₄O',  'elements': {'C': 37.5, 'H': 12.5, 'O': 50.0}},
            {'formula': 'C₃H₈',  'elements': {'C': 81.8, 'H': 18.2}},
            {'formula': 'C₂H₄O', 'elements': {'C': 54.5, 'H': 9.1,  'O': 36.4}},
            {'formula': 'C₃H₆O', 'elements': {'C': 62.1, 'H': 10.3, 'O': 27.6}},
            {'formula': 'CH₂O',  'elements': {'C': 40.0, 'H': 6.7,  'O': 53.3}},
            {'formula': 'C₄H₈O', 'elements': {'C': 66.6, 'H': 11.1, 'O': 22.2}},
            {'formula': 'C₂H₂',  'elements': {'C': 92.3, 'H': 7.7}},
            {'formula': 'C₃H₄O', 'elements': {'C': 64.3, 'H': 7.1,  'O': 28.6}},
            {'formula': 'C₄H₁₀', 'elements': {'C': 82.8, 'H': 17.2}},
        ]
        
        self.compound = rnd.choice(compound_choices)
        self.elements = self.compound['elements']
        # Answer: moles of C atoms in 100 g = %C / Mr(C) = %C / 12
        self.moles_C = round(self.elements['C'] / 12, 2)
        self.answer = self.moles_C
        
        self.description = (
            "The pie chart shows the percentage composition by mass of a compound. "
            "How many moles of carbon atoms are present in 100 g of this compound? "
            "(Give your answer to 2 decimal places.)"
        )
        
        self.topic = "Atoms, molecules and stoichiometry"
        self.subtopic = "Chemical formulae"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Moles of C in 100 g} &= \\frac{\\%\\text{C}}{M_r(\\text{C})}\\\\"
            f"&= \\frac{{{self.elements['C']}}}{{12}}\\\\"
            f"&= {self.answer}\\,\\text{{mol}}"
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
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem009:
    """
    Chapter 2.4: Limiting reagent calculation
    """
    
    def __init__(self):
        reactions = [
            {'equation': '2H₂ + O₂ → 2H₂O',  'reactants': ['H₂', 'O₂'], 'stoich': [2, 1], 'product': 'H₂O',  'prod_stoich': 2},
            {'equation': 'N₂ + 3H₂ → 2NH₃',   'reactants': ['N₂', 'H₂'], 'stoich': [1, 3], 'product': 'NH₃',  'prod_stoich': 2},
            {'equation': 'C + O₂ → CO₂',       'reactants': ['C', 'O₂'],  'stoich': [1, 1], 'product': 'CO₂',  'prod_stoich': 1},
            {'equation': '2CO + O₂ → 2CO₂',    'reactants': ['CO', 'O₂'], 'stoich': [2, 1], 'product': 'CO₂',  'prod_stoich': 2},
            {'equation': 'H₂ + Cl₂ → 2HCl',    'reactants': ['H₂', 'Cl₂'],'stoich': [1, 1], 'product': 'HCl',  'prod_stoich': 2},
            {'equation': '3H₂ + N₂ → 2NH₃',    'reactants': ['H₂', 'N₂'], 'stoich': [3, 1], 'product': 'NH₃',  'prod_stoich': 2},
            {'equation': '2H₂ + CO → CH₃OH',   'reactants': ['H₂', 'CO'], 'stoich': [2, 1], 'product': 'CH₃OH','prod_stoich': 1},
        ]
        
        self.reaction = rnd.choice(reactions)
        self.moles = [round(rnd.uniform(0.5, 3.0), 2) for _ in self.reaction['reactants']]
        
        ratios = [m / s for m, s in zip(self.moles, self.reaction['stoich'])]
        limiting_ratio = min(ratios)
        self.moles_product = round(limiting_ratio * self.reaction['prod_stoich'], 3)
        self.answer = self.moles_product
        
        self.description = (
            "The diagram shows a chemical reaction along with the initial moles of each reactant. "
            "Calculate the maximum number of moles of the product that can be formed."
        )
        
        self.topic = "Atoms, molecules and stoichiometry"
        self.subtopic = "Stoichiometric relationships"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode characters to LaTeX equivalents
        latex_eq = self.reaction['equation'].replace('₂', '_2').replace('₃', '_3').replace('→', '\\rightarrow')
        latex_prod = self.reaction['product'].replace('₂', '_2').replace('₃', '_3')

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Balanced equation: }} & {latex_eq} \\\\"
            "\\text{{Find mole ratios for each reactant:}} &\\\\"
        )
        
        for reactant, mole, stoich in zip(self.reaction['reactants'], self.moles, self.reaction['stoich']):
            latex_react = reactant.replace('₂', '_2').replace('₃', '_3')
            self.reasoning += f"\\text{{For }} {latex_react}: \\quad \\frac{{{mole}}}{{{stoich}}} &= {round(mole/stoich, 3)}\\\\"
        
        self.reasoning += (
            f"\\text{{Limiting ratio}} &= {round(limiting_ratio, 3)}\\\\"
            f"\\text{{Moles of }} {latex_prod} &= {round(limiting_ratio, 3)} \\times {self.reaction['prod_stoich']} = {self.answer}"
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

        atom0, atom1 = self.molecule['atoms']
        en0, en1 = self.molecule['EN']
        
        self.answer = self.delta_EN
        
        self.description = (
            f"The diagram shows the {self.molecule['name']} molecule with electronegativity (EN) "
            f"values labelled on each atom. Calculate the electronegativity difference "
            f"ΔEN = |EN₂ − EN₁| between the two atoms."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Electronegativity and bond polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Electronegativity of {atom0}}} &= {en0}\\\\"
            f"\\text{{Electronegativity of {atom1}}} &= {en1}\\\\"
            f"\\Delta EN &= |{en1} - {en0}| = {self.delta_EN}"
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
        
        # Show EN values — student computes ΔEN from these
        ax.text(x1, y1-0.9, f'EN = {self.molecule["EN"][0]}', 
               fontsize=12, ha='center', fontweight='bold')
        ax.text(x2, y2-0.9, f'EN = {self.molecule["EN"][1]}', 
               fontsize=12, ha='center', fontweight='bold')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem011:
    """
    Topic: 3.3 Shapes of molecules (VSEPR) -- tetrahedral
    Visual: 3D AX4 structure; atom labels show "A (m)" on center, "B (m)" on terminals.
            Molecule formula NOT given; student must count bonds from 3D structure.
    Task:   Count bonds (= 4), read Ar(A) and Ar(B) from diagram, compute Mr = Ar_A + 4*Ar_B
    Variables: m_center = rnd.randint(4,100), m_terminal = rnd.randint(1,60)
    """

    def __init__(self):
        self.m_center   = rnd.randint(4, 100)
        self.m_terminal = rnd.randint(1, 60)
        self.n_bonds    = 4
        self.answer     = self.m_center + self.n_bonds * self.m_terminal
        self.description = (
            "A 3D ball-and-stick structure of a molecule is shown. "
            "The relative atomic mass of each atom type is labelled on the diagram. "
            "Count the number of bonds from the 3D structure and calculate "
            "the relative molecular mass (Mr) of the molecule."
        )
        self.topic      = "Chemical bonding"
        self.subtopic   = "Shapes of molecules (VSEPR) -- tetrahedral"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Shape: tetrahedral}} \\Rightarrow 4 \\text{{ bonds}} &\\\\"
            f"A_r(A) = {self.m_center},\\; A_r(B) = {self.m_terminal} &\\\\"
            f"M_r &= {self.m_center} + 4 \\times {self.m_terminal} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax  = fig.add_subplot(111, projection="3d")

        angle = np.radians(109.5); r = 1.5
        central   = np.array([0, 0, 0])
        terminals = [
            np.array([r, 0, 0]),
            np.array([-r*np.cos(angle),  r*np.sin(angle), 0]),
            np.array([-r*np.cos(angle), -r*np.sin(angle)*np.cos(np.pi/3),
                       r*np.sin(angle)*np.sin(np.pi/3)]),
            np.array([-r*np.cos(angle), -r*np.sin(angle)*np.cos(np.pi/3),
                      -r*np.sin(angle)*np.sin(np.pi/3)]),
        ]
        atom_positions = [central] + terminals
        bonds  = [(0,1),(0,2),(0,3),(0,4)]
        labels = ["A"] + ["B"]*4
        colors = ["tomato"] + ["steelblue"]*4

        draw_3d_molecule(ax, atom_positions, bonds, labels=labels,
                         atom_colors=colors, radius=0.3)

        ax.text2D(0.05, 0.97,
                  f"Ar(A) = {self.m_center}    Ar(B) = {self.m_terminal}",
                  transform=ax.transAxes, fontsize=13, fontweight="bold",
                  bbox=dict(boxstyle="round", facecolor="lightyellow", edgecolor="black"))

        ax.set_xlim(-2,2); ax.set_ylim(-2,2); ax.set_zlim(-3,2)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()


class Chem012:
    """
    Topic: 3.3 Shapes of molecules (VSEPR) -- trigonal pyramidal
    Visual: 3D AX3 structure with lone pair; Ar values on atom labels; formula hidden.
    Task:   Count bonds (= 3), read Ar(A) and Ar(B), compute Mr = Ar_A + 3*Ar_B
    Variables: m_center = rnd.randint(4,100), m_terminal = rnd.randint(1,60)
    """

    def __init__(self):
        self.m_center   = rnd.randint(4, 101)
        self.m_terminal = rnd.randint(1, 61)
        self.n_bonds    = 3
        self.answer     = self.m_center + self.n_bonds * self.m_terminal
        self.description = (
            "A 3D ball-and-stick structure of a molecule is shown with one lone pair indicated. "
            "The relative atomic mass of each atom type is labelled on the diagram. "
            "Count the number of bonds from the 3D structure and calculate "
            "the relative molecular mass (Mr) of the molecule."
        )
        self.topic      = "Chemical bonding"
        self.subtopic   = "Shapes of molecules (VSEPR) -- trigonal pyramidal"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Shape: trigonal pyramidal}} \\Rightarrow 3 \\text{{ bonds}} &\\\\"
            f"A_r(A) = {self.m_center},\\; A_r(B) = {self.m_terminal} &\\\\"
            f"M_r &= {self.m_center} + 3 \\times {self.m_terminal} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax  = fig.add_subplot(111, projection="3d")

        central   = np.array([0, 0, 0]); r = 1.5
        terminals = [
            np.array([r, 0, -0.3]),
            np.array([-r*np.cos(np.radians(120)),  r*np.sin(np.radians(120)), -0.3]),
            np.array([-r*np.cos(np.radians(120)), -r*np.sin(np.radians(120)), -0.3]),
        ]
        lone_pair = np.array([0, 0, 1.2])

        atom_positions = [central] + terminals
        bonds  = [(0,1),(0,2),(0,3)]
        labels = ["A"] + ["B"]*3
        colors = ["tomato"] + ["steelblue"]*3

        draw_3d_molecule(ax, atom_positions, bonds, labels=labels,
                         atom_colors=colors, radius=0.3)

        ax.plot([central[0], lone_pair[0]],
                [central[1], lone_pair[1]],
                [central[2], lone_pair[2]], "r--", lw=2, alpha=0.5)
        ax.text(lone_pair[0], lone_pair[1], lone_pair[2]+0.2,
                "Lone Pair", fontsize=11, ha="center", color="red", fontweight="bold")

        ax.text2D(0.05, 0.97,
                  f"Ar(A) = {self.m_center}    Ar(B) = {self.m_terminal}",
                  transform=ax.transAxes, fontsize=13, fontweight="bold",
                  bbox=dict(boxstyle="round", facecolor="lightyellow", edgecolor="black"))

        ax.set_xlim(-2,2); ax.set_ylim(-2,2); ax.set_zlim(-3,2)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
        plt.close()


class Chem013:
    """
    Topic: 3.3 Shapes of molecules (VSEPR) -- bent/V-shaped
    Visual: 3D AX2 structure with two lone pairs; Ar values on atom labels; formula hidden.
    Task:   Count bonds (= 2), read Ar(A) and Ar(B), compute Mr = Ar_A + 2*Ar_B
    Variables: m_center = rnd.randint(4,100), m_terminal = rnd.randint(1,60)
    """

    def __init__(self):
        self.m_center   = rnd.randint(4, 102)
        self.m_terminal = rnd.randint(1, 62)
        self.n_bonds    = 2
        self.bond_angle = 104.5
        self.answer     = self.m_center + self.n_bonds * self.m_terminal
        self.description = (
            "A 3D ball-and-stick structure of a molecule is shown with two lone pairs indicated. "
            "The relative atomic mass of each atom type is labelled on the diagram. "
            "Count the number of bonds from the 3D structure and calculate "
            "the relative molecular mass (Mr) of the molecule."
        )
        self.topic      = "Chemical bonding"
        self.subtopic   = "Shapes of molecules (VSEPR) -- bent"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Shape: bent}} \\Rightarrow 2 \\text{{ bonds}} &\\\\"
            f"A_r(A) = {self.m_center},\\; A_r(B) = {self.m_terminal} &\\\\"
            f"M_r &= {self.m_center} + 2 \\times {self.m_terminal} = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(10, 10))
        ax  = fig.add_subplot(111, projection="3d")

        central  = np.array([0, 0, 0])
        angle    = np.radians(self.bond_angle); r = 1.5
        terminals = [
            np.array([ r*np.sin(angle/2), 0, -r*np.cos(angle/2)]),
            np.array([-r*np.sin(angle/2), 0, -r*np.cos(angle/2)]),
        ]
        lp1 = np.array([ 0.7, 0, 1.0])
        lp2 = np.array([-0.7, 0, 1.0])

        atom_positions = [central] + terminals
        bonds  = [(0,1),(0,2)]
        labels = ["A"] + ["B"]*2
        colors = ["tomato"] + ["steelblue"]*2

        draw_3d_molecule(ax, atom_positions, bonds, labels=labels,
                         atom_colors=colors, radius=0.3)

        for lp in [lp1, lp2]:
            ax.plot([central[0], lp[0]],
                    [central[1], lp[1]],
                    [central[2], lp[2]], "r--", lw=2, alpha=0.5)
        ax.text(0, 0, 1.5, "Lone Pairs", fontsize=11, ha="center",
                color="red", fontweight="bold")

        ax.text2D(0.05, 0.97,
                  f"Ar(A) = {self.m_center}    Ar(B) = {self.m_terminal}",
                  transform=ax.transAxes, fontsize=13, fontweight="bold",
                  bbox=dict(boxstyle="round", facecolor="lightyellow", edgecolor="black"))

        ax.set_xlim(-2,2); ax.set_ylim(-2,2); ax.set_zlim(-3,2)
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
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
        
        # Group 16 hydrides: boiling points with small random perturbations
        base_bps = {'H₂S': -60, 'H₂Se': -41, 'H₂Te': -2}
        self.bps = {mol: bp + rnd.randint(-3, 3) for mol, bp in base_bps.items()}
        self.asked_mol = rnd.choice(list(self.bps.keys()))
        self.answer = self.bps[self.asked_mol]
        
        self.description = (
            f"The graph shows the boiling points of the Group 16 hydrides. "
            f"Use the graph to state the boiling point of {self.asked_mol} (°C, to the nearest whole number)."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode subscript to standard LaTeX math syntax
        latex_mol = self.asked_mol.replace('₂', '_2')
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the graph, we locate the data point for }} {latex_mol}. &\\\\"
            "\\text{Tracing this point to the y-axis yields the exact value:} &\\\\"
            f"\\therefore \\text{{Boiling point}} &= {self.answer}\\,^\\circ\\text{{C}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        mol_order = ['H₂S', 'H₂Se', 'H₂Te']
        x = [1, 2, 3]
        y = [self.bps[m] for m in mol_order]
        
        ax.plot(x, y, 'bo-', markersize=10, linewidth=2)
        ax.set_xticks(x)
        ax.set_xticklabels(mol_order, fontsize=13)
        ax.set_ylabel('Boiling point / °C', fontsize=13)
        ax.set_title('Boiling Points of Group 16 Hydrides', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        for xi, yi, mol in zip(x, y, mol_order):
            ax.annotate(f'{yi} °C', (xi, yi), textcoords='offset points',
                       xytext=(8, 5), fontsize=11)
        
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
        self.answer = self.metal['valence']   # numerical: delocalized electrons per atom
        
        self.description = (
            "The diagram shows a metallic lattice with the ion charge labelled. "
            "How many delocalized electrons does each metal atom contribute to the lattice?"
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Metallic bonding"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Dynamically build the LaTeX ion using symbol and valence
        charge_str = "+" if self.metal['valence'] == 1 else f"{self.metal['valence']}+"
        latex_ion = f"{self.metal['symbol']}^{{{charge_str}}}"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{{self.metal['name']} forms }} {latex_ion} \\text{{ ions.}} &\\\\"
            f"\\text{{Each atom loses its {self.metal['valence']} valence electron(s)}} &\\\\"
            "\\text{to form the sea of delocalized electrons.} &\\\\"
            f"\\text{{Delocalized electrons per atom}} &= {self.answer}"
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
        
        from math import cos, radians
        # V-shaped (bent) polar molecules with labelled bond dipoles
        bent_molecules = [
            {'name': 'H₂O',  'bond_angle': 104.5, 'mu_bond': 1.51, 'center': 'O', 'terminal': 'H'},
            {'name': 'H₂S',  'bond_angle': 92.0,  'mu_bond': 0.97, 'center': 'S', 'terminal': 'H'},
            {'name': 'OF₂',  'bond_angle': 103.0, 'mu_bond': 0.94, 'center': 'O', 'terminal': 'F'},
            {'name': 'SCl₂', 'bond_angle': 103.0, 'mu_bond': 1.20, 'center': 'S', 'terminal': 'Cl'},
            {'name': 'SO₂',  'bond_angle': 119.0, 'mu_bond': 1.63, 'center': 'S', 'terminal': 'O'},
            {'name': 'ClF',  'bond_angle': 180.0, 'mu_bond': 0.88, 'center': 'Cl', 'terminal': 'F'},
        ]
        self.mol = rnd.choice(bent_molecules)
        # Add small noise to bond dipole for numerical variance
        self.mu_bond = round(self.mol['mu_bond'] + rnd.uniform(-0.05, 0.05), 2)
        theta = self.mol['bond_angle']
        half_open = (180.0 - theta) / 2.0
        self.mu_net = round(2 * self.mu_bond * cos(radians(half_open)), 2)
        self.answer = self.mu_net
        
        self.description = (
            "A molecule is shown with bond dipole moments and bond angle labelled. "
            "Use the diagram to calculate the net (resultant) dipole moment, μ_net, in Debye (D), to 2 d.p."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Molecular polarity"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\mu_{{\\text{{bond}}}} &= {self.mu_bond}\\,\\text{{D}}\\\\"
            f"\\theta &= {theta}°\\\\"
            f"\\mu_{{\\text{{net}}}} &= 2\\mu_{{\\text{{bond}}}}\\cos\\left(\\frac{{180°-\\theta}}{{2}}\\right)\\\\"
            f"&= 2 \\times {self.mu_bond} \\times \\cos({half_open}°)\\\\"
            f"&= {self.answer}\\,\\text{{D}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        from math import sin, cos, radians
        fig, ax = plt.subplots(figsize=(9, 8))
        ax.set_xlim(0, 9)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        add_title_box(ax, 4.5, 7.5, f'Bond Dipole Moments in {self.mol["name"]}', fontsize=14)
        
        theta = self.mol['bond_angle']
        half = radians(theta / 2)
        cx, cy = 4.5, 4.0
        r = 1.8
        x1 = cx - r * sin(half);  y1 = cy - r * cos(half)
        x2 = cx + r * sin(half);  y2 = cy - r * cos(half)
        
        ax.plot([cx, x1], [cy, y1], 'k-', lw=3)
        ax.plot([cx, x2], [cy, y2], 'k-', lw=3)
        
        draw_circle_atom(ax, cx, cy, self.mol['center'], radius=0.4, color='lightcoral')
        draw_circle_atom(ax, x1, y1, self.mol['terminal'], radius=0.3, color='lightblue')
        draw_circle_atom(ax, x2, y2, self.mol['terminal'], radius=0.3, color='lightblue')
        
        # Bond dipole arrows
        mid1x, mid1y = (cx+x1)/2, (cy+y1)/2
        mid2x, mid2y = (cx+x2)/2, (cy+y2)/2
        ax.annotate('', xy=(cx, cy), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.annotate('', xy=(cx, cy), xytext=(x2, y2),
                   arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        
        ax.text(mid1x-0.4, mid1y, f'{self.mu_bond} D', fontsize=11, color='blue', ha='center')
        ax.text(mid2x+0.4, mid2y, f'{self.mu_bond} D', fontsize=11, color='blue', ha='center')
        
        # Bond angle arc label
        ax.text(cx, cy-0.6, f'{theta}°', fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightyellow'))
        
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
        # Perturb bp values +-3% so graph varies across instances while preserving monotonic trend
        self.bp_values  = [round(g['bp'] * rnd.uniform(0.97, 1.03)) for g in noble_gases]
        
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
        
        self.asked_idx = rnd.randint(0, 4)
        self.asked_symbol = self.noble_gases_symbols[self.asked_idx]
        self.answer = self.bp_values[self.asked_idx]
        
        self.description = (
            "The graph shows the boiling points of the noble gases plotted against "
            "relative molecular mass. "
            f"Use the graph to state the boiling point of {self.asked_symbol} (°C, nearest whole number)."
        )
        
        self.topic = "Chemical bonding"
        self.subtopic = "Intermolecular forces"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Read the boiling point of {self.asked_symbol} from the graph:}} &\\\\"
            f"\\text{{bp}}({self.asked_symbol}) &= {self.answer}\\,^\\circ\\text{{C}}"
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
        
        # Extend x-limit so labels fit
        ax.set_xlim(min(self.Mr_values), max(self.Mr_values) + 5)
        x_right = ax.get_xlim()[1]

        # Add lines + labels for ALL boiling points
        for y in self.bp_values:
            ax.axhline(y=y, linestyle='--', linewidth=0.8, alpha=0.3)
            
            ax.text(
                x_right, y,
                f"{y}°C",
                va='center', ha='left', fontsize=9
            )

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
        
        self.melting_point = rnd.randint(-50, 100)
        self.boiling_point = self.melting_point + rnd.randint(30, 150)
        self.answer = self.boiling_point  # numerical: boiling point read from graph
        
        self.description = (
            "The heating curve shows temperature against time for a pure substance being heated at a "
            "constant rate. "
            "Use the graph to state the boiling point of this substance (°C)."
        )
        
        self.topic = "States of matter"
        self.subtopic = "Changes of state"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{From the graph, we can see that the second (upper) plateau represents boiling.} &\\\\"
            "\\text{Tracing this upper plateau to the y-axis gives the exact temperature.} &\\\\"
            f"\\therefore \\text{{Boiling point}} &= {self.boiling_point}\\,^\\circ\\text{{C}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        t  = [0, 2, 4, 6, 9, 11]
        T  = [self.melting_point - 30, self.melting_point, self.melting_point,
              self.boiling_point, self.boiling_point, self.boiling_point + 40]
        
        ax.plot(t, T, 'b-', linewidth=3)
        
        # Add dashed line and text for the melting (lower) plateau
        ax.axhline(y=self.melting_point, color='g', linestyle='--', linewidth=1.5, alpha=0.5)
        ax.text(11.2, self.melting_point, f'{self.melting_point}', fontsize=11, color='g', va='center')
        
        # Add dashed line and text for the boiling (upper) plateau
        ax.axhline(y=self.boiling_point, color='r', linestyle='--', linewidth=1.5, alpha=0.5)
        ax.text(11.2, self.boiling_point, f'{self.boiling_point}', fontsize=11, color='r', va='center')
        
        # Extend the x-axis limits slightly to prevent text from hitting the right border
        ax.set_xlim(0, 12.5)
        
        ax.set_xlabel('Time / min', fontsize=13)
        ax.set_ylabel('Temperature / °C', fontsize=13)
        ax.set_title('Heating Curve of a Pure Substance', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
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
        # Continuous randomisation: mp 0–120 C, bp always at least 40 C above mp
        self.melting_point = rnd.randint(0, 120)
        self.boiling_point = self.melting_point + rnd.randint(40, 150)
        self.answer = self.melting_point  # numerical answer
        
        self.description = (
            "The heating curve shows temperature vs time for a pure substance. "
            f"Use the graph to determine the melting point (in °C) of the substance."
        )
        
        self.topic = "States of matter"
        self.subtopic = "Phase changes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Heating curve features:} &\\\\"
            "\\text{- Temperature rises } \\rightarrow \\text{ heating solid} &\\\\"
            f"\\text{{- First plateau (horizontal region) at }} {self.melting_point}\\,^\\circ\\text{{C}} \\rightarrow \\text{{ melting}} &\\\\"
            "\\text{- Temperature rises } \\rightarrow \\text{ heating liquid} &\\\\"
            f"\\text{{- Second plateau at }} {self.boiling_point}\\,^\\circ\\text{{C}} \\rightarrow \\text{{ boiling}} &\\\\"
            f"\\text{{Melting point}} &= {self.melting_point}\\,^\\circ\\text{{C}}"
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
        
        ax.axhline(y=self.melting_point, color='blue', linestyle='--', alpha=0.5)
        ax.axhline(y=self.boiling_point, color='green', linestyle='--', alpha=0.5)
        
        ax.text(1, -12, 'Solid', fontsize=11, ha='center', style='italic', color='gray')
        ax.text(5, (self.melting_point + self.boiling_point) / 2,
                'Liquid', fontsize=11, ha='center', style='italic', color='gray')
        ax.text(9, self.boiling_point + 15, 'Gas', fontsize=11, ha='center', style='italic', color='gray')

        # Extend x-limit so text doesn't get cut off
        ax.set_xlim(min(time), max(time) + 1)
        x_right = ax.get_xlim()[1] + 0.2

        # Melting point label (right side)
        ax.text(
            x_right, self.melting_point,
            f"{self.melting_point}",
            va='center', ha='left', fontsize=10, color='blue'
        )

        # Boiling point label (right side)
        ax.text(
            x_right, self.boiling_point,
            f"{self.boiling_point}",
            va='center', ha='left', fontsize=10, color='green'
        )
        
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
        # Continuous randomisation with wide ranges
        self.reactant_E  = rnd.randint(20, 150)
        self.product_E   = rnd.randint(20, 150)
        # Ensure activation energy is always higher than reactant energy
        self.activation_E = self.reactant_E + rnd.randint(15, 100)
        
        self.delta_H = self.product_E - self.reactant_E
        self.Ea = self.activation_E - self.reactant_E
        
        self.answer = self.delta_H
        
        self.description = (
            "The enthalpy profile diagram is shown with energy levels marked on the y-axis. "
            "Calculate the enthalpy change ΔH (in kJ mol⁻¹) for this reaction."
        )
        
        self.topic = "Energetics"
        self.subtopic = "Enthalpy changes"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
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
        
        # NO NEED VERTICAL ANNOTATION TO MAKE PROBLEM HARDER
        # draw_vertical_annotation(ax, 1, self.reactant_E, self.activation_E,
        #                         'Ea', color='red', label_offset=0.5)
        
        # draw_vertical_annotation(ax, 8.5, self.reactant_E, self.product_E,
        #                         'ΔH = ?', color='green', label_offset=0.5)
        
        ax.text(profile['reactant_x'], self.reactant_E + 8, 'Reactants',
               fontsize=14, ha='center', fontweight='bold')
        ax.text(profile['product_x'], self.product_E + 8, 'Products',
               fontsize=14, ha='center', fontweight='bold')
        
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        ax.set_ylim(0, self.activation_E + 20)

        # Extend x-limit so labels fit on the right
        ax.set_xlim(0, 10.5)
        x_right = ax.get_xlim()[1]

        # List of key energy levels
        energy_levels = [
            (self.reactant_E, 'Reactants'),
            (self.product_E, 'Products'),
            (self.activation_E, 'Peak')
        ]

        # Draw dashed lines + right-side labels
        for y, label in energy_levels:
            ax.axhline(y=y, linestyle='--', linewidth=1.0, alpha=0.4)
            
            ax.text(
                x_right, y,
                f"{y}",
                va='center', ha='left', fontsize=10
            )
        
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
        self.delta_H_target = self.delta_H1 + self.delta_H2
        
        self.answer = self.delta_H_target  # numerical only, no units
        
        self.description = (
            "A Hess's Law cycle is shown. Use the enthalpy values labelled on the diagram "
            "to calculate ΔH for the direct route A → B (in kJ mol⁻¹)."
        )
        
        self.topic = "Energetics"
        self.subtopic = "Hess's Law"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Hess's Law: Total enthalpy change is independent of route} &\\\\"
            "\\text{Route 1 (direct):} &\\\\"
            "\\text{A → B: } \\Delta H_{\\text{target}} &\\\\"
            "\\text{Route 2 (via C):} &\\\\"
            f"\\text{{A → C: }} \\Delta H_1 &= {self.delta_H1}\\,\\text{{kJ/mol}}\\\\"
            f"\\text{{C → B: }} \\Delta H_2 &= {self.delta_H2}\\,\\text{{kJ/mol}}\\\\"
            "\\text{By Hess's Law:} &\\\\"
            "\\Delta H_{\\text{target}} &= \\Delta H_1 + \\Delta H_2\\\\"
            f"&= {self.delta_H1} + ({self.delta_H2})\\\\"
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
            {'anode': 'Zn', 'cathode': 'Cu', 'E_anode': -0.76, 'E_cathode':  0.34},
            {'anode': 'Mg', 'cathode': 'Ag', 'E_anode': -2.37, 'E_cathode':  0.80},
            {'anode': 'Fe', 'cathode': 'Cu', 'E_anode': -0.44, 'E_cathode':  0.34},
            {'anode': 'Zn', 'cathode': 'Ag', 'E_anode': -0.76, 'E_cathode':  0.80},
            {'anode': 'Mg', 'cathode': 'Cu', 'E_anode': -2.37, 'E_cathode':  0.34},
            {'anode': 'Fe', 'cathode': 'Ag', 'E_anode': -0.44, 'E_cathode':  0.80},
            {'anode': 'Ni', 'cathode': 'Cu', 'E_anode': -0.25, 'E_cathode':  0.34},
            {'anode': 'Zn', 'cathode': 'Fe', 'E_anode': -0.76, 'E_cathode': -0.44},
            {'anode': 'Mg', 'cathode': 'Ni', 'E_anode': -2.37, 'E_cathode': -0.25},
            {'anode': 'Pb', 'cathode': 'Cu', 'E_anode': -0.13, 'E_cathode':  0.34},
        ]
        
        self.cell = rnd.choice(metal_pairs)
        self.E_cell = self.cell['E_cathode'] - self.cell['E_anode']
        self.answer = round(self.E_cell, 2)
        
        self.description = (
            "The electrochemical cell diagram is shown. "
            "Use the standard electrode potentials labelled in the diagram to "
            "calculate the standard cell potential E°cell (in V, to 2 d.p.)."
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Redox and electrode potentials"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
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
        ax.text(2.5, 0.8, f"E° = {self.cell['E_anode']} V", fontsize=11, ha='center', color='navy')
        
        draw_beaker(ax, 8, 2, 3, 3, liquid_height=2, liquid_color='lightgreen')
        ax.text(9.5, 1.5, f'{self.cell["cathode"]}²⁺(aq)', fontsize=11, ha='center', fontweight='bold')
        ax.text(9.5, 0.8, f"E° = {self.cell['E_cathode']} V", fontsize=11, ha='center', color='navy')
        
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
        self.initial_A = round(rnd.uniform(0.5, 4.0), 2)
        self.final_A   = round(rnd.uniform(0.1, self.initial_A * 0.6), 2)
        self.final_B   = round(self.initial_A - self.final_A, 2)
        
        self.answer = round(self.final_A, 2)
        
        self.description = (
            "The graph shows concentration vs time for the reaction A ⇌ B. "
            "State the equilibrium concentration of A (in mol dm⁻³)."
        )
        
        self.topic = "Equilibria"
        self.subtopic = "Dynamic equilibrium"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{From the diagram, the concentration of A becomes constant at equilibrium, therefore:} \\\\"
            f"&\\text{{[A]eq}} = {self.final_A}\\,\\text{{M}}"
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
        ax.text(7, self.initial_A * 0.8, 'Equilibrium\nReached', fontsize=12, ha='center', 
               fontweight='bold', color='green')
        
        ax.set_xlabel('Time (s)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (M)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time for A ⇌ B', fontsize=16, fontweight='bold')
        ax.legend(fontsize=14, loc='upper right')
        ax.grid(True, alpha=0.3)

        # Extend x-limit slightly so text isn't cut off
        ax.set_xlim(0, max(time) + 1)
        x_right = ax.get_xlim()[1]

        # Add labels for equilibrium concentrations
        ax.text(
            x_right, self.final_A,
            f"{self.final_A}",
            va='center', ha='left', fontsize=10, color='b'
        )

        ax.text(
            x_right, self.final_B,
            f"{self.final_B}",
            va='center', ha='left', fontsize=10, color='r'
        )
        
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
        self.question_type = "Short Answer"
        
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
        self.Ea = rnd.randint(50, 150)
        
        self.answer = self.Ea   # numerical: activation energy read from graph
        
        self.description = (
            f"The Maxwell-Boltzmann distribution curves at {self.T1} K and {self.T2} K are shown. "
            "Use the graph to state the activation energy Ea (in kJ mol⁻¹)."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Effect of temperature"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{In a Maxwell-Boltzmann distribution, the vertical dashed line where} \\\\"
            "&\\text{the shaded region begins represents the activation energy (Ea).} \\\\"
            "&\\text{Reading the marked value on the x-axis:} \\\\"
            f"&E_a = {self.Ea}\\,\\text{{kJ mol}}^{{-1}}"
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
        
        ax.plot(E, y1, 'b-', linewidth=3, label=f'{self.T1} K')
        ax.plot(E, y2, 'r-', linewidth=3, label=f'{self.T2} K')
        
        # Draw the line normally from top to bottom
        ax.axvline(x=self.Ea, color='green', linestyle='--', linewidth=2)
        
        # Calculate a nice high spot for the text (90% up the tallest peak)
        y_max = np.max([y1, y2])
        ax.text(self.Ea, y_max * 0.9, f'$x = {self.Ea}$', fontsize=12, color='green', 
                fontweight='bold', ha='center', va='bottom',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        
        ax.fill_between(E, 0, y1, where=(E >= self.Ea), alpha=0.2, color='blue')
        ax.fill_between(E, 0, y2, where=(E >= self.Ea), alpha=0.2, color='red')
        
        ax.set_xlabel('Energy / kJ mol⁻¹', fontsize=14, fontweight='bold')
        ax.set_ylabel('Number of Molecules', fontsize=14, fontweight='bold')
        ax.set_title('Maxwell-Boltzmann Distribution', fontsize=16, fontweight='bold')
        ax.legend(fontsize=14)
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
        self.question_type = "Short Answer"
        
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
        
        for i in range(4):
            t = i * self.half_life
            c = self.initial_conc / (2 ** i)
            
            # Only draw dashed guide lines for the half-life points (i > 0)
            if i > 0:
                ax.axvline(x=t, color='red', linestyle='--', alpha=0.4)
                ax.axhline(y=c, color='red', linestyle='--', alpha=0.4)
            
            # Plot the orange dot
            ax.plot(t, c, marker='o', color='orange', markersize=8)
            
            # Add the (x, y) coordinate label slightly offset from the dot
            ax.annotate(f'({t}, {c:.4f})', xy=(t, c), xytext=(8, 8), 
                        textcoords='offset points', color='#d97706', fontweight='bold')
        
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
        raw_IE = [496, 738, 578, 787, 1012, 1000, 1251, 1521]
        # Perturb +-3% so graph varies across instances
        self.IE_values = [round(v * rnd.uniform(0.97, 1.03)) for v in raw_IE]
        
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
        
        self.asked_idx = rnd.randint(0, len(self.elements) - 1)
        self.asked_element = self.elements[self.asked_idx]
        self.answer = self.IE_values[self.asked_idx]
        
        self.description = (
            "The bar chart shows the first ionisation energies of the Period 3 elements. "
            f"Use the chart to state the first ionisation energy of {self.asked_element} "
            "(kJ mol⁻¹, to the nearest whole number)."
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in ionization energy"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Read the bar for {self.asked_element} from the chart:}} &\\\\"
            f"\\text{{First IE of {self.asked_element}}} &= {self.answer}\\,\\text{{kJ mol}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
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
        raw_radii = [186, 160, 143, 117, 110, 104, 99]
        # Perturb +-3% so graph varies across instances
        self.radii = [round(v * rnd.uniform(0.97, 1.03)) for v in raw_radii]
        
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
        
        self.asked_idx = rnd.randint(0, len(self.elements) - 1)
        self.asked_element = self.elements[self.asked_idx]
        self.answer = self.radii[self.asked_idx]
        
        self.description = (
            "The graph shows atomic radii of Period 3 elements. "
            f"Use the graph to state the atomic radius of {self.asked_element} (pm, nearest whole number)."
        )
        
        self.topic = "Periodicity"
        self.subtopic = "Trends in atomic properties"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Read the data point for {self.asked_element} from the graph:}} &\\\\"
            f"\\text{{Atomic radius of {self.asked_element}}} &= {self.answer}\\,\\text{{pm}}"
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
        
        self.Mr_Cl2 = 71.0
        self.mass_Cl2 = rnd.randint(5, 50)
        self.moles_Cl2 = round(self.mass_Cl2 / self.Mr_Cl2, 4)
        self.moles_Br2 = round(self.moles_Cl2, 4)   # 1:1 ratio Cl2 : Br2
        self.answer = round(self.moles_Br2, 3)
        
        self.description = (
            "Calculate the number of moles of Br₂ produced in the experiment "
            "shown in the diagram. Give your answer to 3 decimal places."
        )
        
        self.topic = "Group 17 (Halogens)"
        self.subtopic = "Halogen displacement reactions"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Extract information from the diagram:} &\\\\"
            f"\\text{{Mass of Cl}}_2 \\text{{ added}} &= {self.mass_Cl2}\\,\\text{{g}} \\\\"
            f"\\text{{Molar mass (M}}_r\\text{{) of Cl}}_2 &= {self.Mr_Cl2}\\,\\text{{g mol}}^{{-1}} \\\\"
            "\\text{2. Calculate moles of Cl}_2: &\\\\"
            f"n(\\text{{Cl}}_2) &= \\frac{{{self.mass_Cl2}}}{{{self.Mr_Cl2}}} = {self.moles_Cl2}\\,\\text{{mol}} \\\\"
            "\\text{3. Use stoichiometric ratio from the balanced equation:} &\\\\"
            "\\text{Cl}_2 + 2\\text{KBr} &\\rightarrow 2\\text{KCl} + \\text{Br}_2 \\\\"
            "\\text{The molar ratio of Cl}_2 : \\text{Br}_2 &= 1 : 1 \\\\"
            f"\\text{{Therefore, }} n(\\text{{Br}}_2) &= {self.answer}\\,\\text{{mol}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 6))
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 6)
        ax.axis('off')
        
        add_title_box(ax, 5.5, 5.5, 'Halogen Displacement Reaction', fontsize=14)
        
        ax.text(5.5, 4.6, 'Cl₂  +  2KBr  →  2KCl  +  Br₂',
               fontsize=14, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='black'))
        
        draw_test_tube(ax, 1.5, 1, width=1.4, height=3, solution_height=2,
                      solution_color='lightyellow')
        ax.text(2.2, 0.5, 'KBr(aq)', fontsize=11, ha='center')
        
        draw_arrow(ax, 3.5, 3, 5.0, 3, arrowstyle='->', color='black', linewidth=3)
        ax.text(4.25, 3.5, f'Add Cl₂\n({self.mass_Cl2} g)',
               fontsize=11, ha='center', fontweight='bold', color='darkgreen')
        
        draw_test_tube(ax, 6.5, 1, width=1.4, height=3, solution_height=2,
                      solution_color='darkorange')
        ax.text(7.2, 0.5, 'Products', fontsize=11, ha='center')
        
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
        
        # Pool of alkanes with known C-C bond counts: C-C bonds = (n_carbons - 1) for unbranched chains
        alkane_pool = [
            {'name': 'propane',   'formula': 'C₃H₈',  'structure': 'CH₃–CH₂–CH₃',   'cc_bonds': 2},
            {'name': 'butane',    'formula': 'C₄H₁₀', 'structure': 'CH₃–CH₂–CH₂–CH₃','cc_bonds': 3},
            {'name': 'pentane',   'formula': 'C₅H₁₂', 'structure': 'CH₃–(CH₂)₃–CH₃', 'cc_bonds': 4},
            {'name': 'hexane',    'formula': 'C₆H₁₄', 'structure': 'CH₃–(CH₂)₄–CH₃', 'cc_bonds': 5},
            {'name': 'heptane',   'formula': 'C₇H₁₆', 'structure': 'CH₃–(CH₂)₅–CH₃', 'cc_bonds': 6},
            {'name': 'octane',    'formula': 'C₈H₁₈', 'structure': 'CH₃–(CH₂)₆–CH₃', 'cc_bonds': 7},
            {'name': 'isobutane', 'formula': 'C₄H₁₀', 'structure': '(CH₃)₃CH',         'cc_bonds': 3},
            {'name': 'isopentane','formula': 'C₅H₁₂', 'structure': '(CH₃)₂CHCH₂CH₃',  'cc_bonds': 4},
            {'name': '2-methylbutane','formula': 'C₅H₁₂','structure': 'CH₃CH(CH₃)CH₂CH₃','cc_bonds': 4},
            {'name': 'neopentane','formula': 'C₅H₁₂', 'structure': 'C(CH₃)₄',           'cc_bonds': 4},
        ]
        
        self.molecule = rnd.choice(alkane_pool)
        self.answer = self.molecule['cc_bonds']
        
        self.description = (
            "A structural formula is shown. "
            "How many C–C single bonds does this molecule contain?"
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Structural formulae"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode subscripts and en-dashes to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '–': '-'  # Convert en-dash to regular hyphen for math mode bonds
        })
        form_tex = self.molecule['formula'].translate(tex_map)
        struct_tex = self.molecule['structure'].translate(tex_map)
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{By examining the structure of {self.molecule['name']} (}}\\mathrm{{{form_tex}}}\\text{{),}} \\\\"
            f"&\\text{{we can visually trace the carbon chain: }} \\mathrm{{{struct_tex}}} \\\\"
            "&\\text{{Counting the direct connections between the carbon atoms yields:}} \\\\"
            f"&\\text{{C–C single bonds}} = {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 5))
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        draw_labeled_box(ax, 2, 1.5, 7, 1.5,
                        self.molecule['structure'],
                        '(Structural Formula)',
                        facecolor='lightyellow')
        
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
        
        alkenes = [
            {'name': 'ethene',         'formula': 'C₂H₄',  'Mr': 28,  'structure': 'H₂C=CH₂'},
            {'name': 'propene',        'formula': 'C₃H₆',  'Mr': 42,  'structure': 'CH₃CH=CH₂'},
            {'name': 'but-1-ene',      'formula': 'C₄H₈',  'Mr': 56,  'structure': 'CH₃CH₂CH=CH₂'},
            {'name': 'but-2-ene',      'formula': 'C₄H₈',  'Mr': 56,  'structure': 'CH₃CH=CHCH₃'},
            {'name': 'pent-1-ene',     'formula': 'C₅H₁₀', 'Mr': 70,  'structure': 'CH₃(CH₂)₂CH=CH₂'},
            {'name': 'pent-2-ene',     'formula': 'C₅H₁₀', 'Mr': 70,  'structure': 'CH₃CH=CHCH₂CH₃'},
            {'name': 'hex-1-ene',      'formula': 'C₆H₁₂', 'Mr': 84,  'structure': 'CH₃(CH₂)₃CH=CH₂'},
            {'name': '2-methylpropene','formula': 'C₄H₈',  'Mr': 56,  'structure': '(CH₃)₂C=CH₂'},
            {'name': '2-methylbut-2-ene','formula': 'C₅H₁₀','Mr': 70, 'structure': '(CH₃)₂C=CHCH₃'},
            {'name': 'cyclohexene',    'formula': 'C₆H₁₀', 'Mr': 82,  'structure': 'cyclo-C₆H₁₀'},
        ]
        
        self.mol = rnd.choice(alkenes)
        self.answer = self.mol['Mr']
        
        self.description = (
            f"The structural formula of an alkene is shown. "
            f"Calculate the relative molecular mass (Mr) of this compound."
        )
        
        self.topic = "Introduction to organic chemistry"
        self.subtopic = "Hydrocarbons: alkenes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode subscripts and en-dashes to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
            '–': '-'
        })
        form_tex = self.mol['formula'].translate(tex_map)
        struct_tex = self.mol['structure'].translate(tex_map)
        
        # Extract C and H atom counts for the calculation step
        norm_formula = self.mol['formula'].translate(str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789'))
        c_count, h_count = norm_formula.split('C')[-1].split('H')
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{From the structure }}\\mathrm{{{struct_tex}}}\\text{{, we deduce the alkene is {self.mol['name']} with formula }}\\mathrm{{{form_tex}}}\\text{{.}} \\\\"
            "&\\text{{Using the standard atomic masses (C = 12.0, H = 1.0), we calculate the relative molecular mass:}} \\\\"
            f"&M_r = ({c_count} \\times 12.0) + ({h_count} \\times 1.0) \\\\"
            f"&M_r = {self.mol['Mr']}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        draw_labeled_box(ax, 2, 1.5, 6, 1.5,
                        f'{self.mol["structure"]}',
                        f'(Structural Formula)',
                        facecolor='lightblue')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem032:
    """
    Topic: 13.3 Homologous series
    Visual: Table showing first 4 members of a homologous series (series NAME hidden)
    Task: Read the H-atom pattern from the table; predict H count for a larger member
    Variance: 3 series × disjoint n-ranges → 30 unique answer values, no cross-series clash
    """

    def __init__(self):
        # Disjoint n-ranges guarantee no answer overlap across series
        series_pool = [
            {
                'series_key': 'alkane',
                'h_func': lambda n: 2*n + 2,
                'examples': [(1,'CH₄',4),(2,'C₂H₆',6),(3,'C₃H₈',8),(4,'C₄H₁₀',10)],
                'n_range': (16, 25),   
            },
            {
                'series_key': 'alkene',
                'h_func': lambda n: 2*n,
                'examples': [(2,'C₂H₄',4),(3,'C₃H₆',6),(4,'C₄H₈',8),(5,'C₅H₁₀',10)],
                'n_range': (6, 15),    
            },
            {
                'series_key': 'alkyne',
                'h_func': lambda n: 2*n - 2,
                'examples': [(2,'C₂H₂',2),(3,'C₃H₄',4),(4,'C₄H₆',6),(5,'C₅H₈',8)],
                'n_range': (2, 11),    
            },
        ]

        self.series = rnd.choice(series_pool)
        lo, hi      = self.series['n_range']
        self.n      = rnd.randint(lo, hi)
        self.H_count = self.series['h_func'](self.n)
        self.answer  = self.H_count

        self.description = (
            "The table shows the first four members of a homologous series "
            "(the series name is not given). "
            f"Using the pattern in the table, determine how many hydrogen atoms "
            f"the member with {self.n} carbon atoms has."
        )

        self.topic      = "Introduction to organic chemistry"
        self.subtopic   = "Homologous series"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        # Determine the math string for the formula based on the series
        if self.series['series_key'] == 'alkane':
            formula_str = "2n + 2"
            sub_str = f"2({self.n}) + 2"
        elif self.series['series_key'] == 'alkene':
            formula_str = "2n"
            sub_str = f"2({self.n})"
        else:
            formula_str = "2n - 2"
            sub_str = f"2({self.n}) - 2"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Analyze the table to find the general formula relating C atoms (n) to H atoms.} \\\\"
            f"&\\text{{2. The pattern fits the general formula: Number of H}} = {formula_str} \\\\"
            f"&\\text{{3. Substitute }} n = {self.n} \\text{{ into the formula:}} \\\\"
            f"&\\quad \\text{{Number of H}} = {sub_str} \\\\"
            f"&\\quad \\text{{Number of H}} = {self.H_count}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis('off')

        table_data = [['n (C atoms)', 'Molecular Formula', 'H atoms']] +                      [[str(n), fml, str(h)] for n, fml, h in self.series['examples']]

        draw_data_table(ax, table_data, start_x=0.8, start_y=5.5,
                        cell_width=2.8, cell_height=0.7, header_color='lightblue')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()


class Chem033:
    """
    Topic: 14.1 Electrophilic addition -- alkene + HX
    Visual: Two-step mechanism showing CnH2n + HX -> ?
            Alkene formula (with actual n) and reagent HX are labelled in diagram.
            Product box shows only "?".
    Task:   Read n and X from diagram, compute Mr of monohalide product
    Variables: n_C = rnd.randint(2,9), halogen in {Cl,Br,I}
    Answer: Mr = 14*n + 1 + M_X
    """

    _HALOGENS = {
        "Cl": {"mass": 35.5,  "color": "mediumseagreen", "nuc": "Cl-", "elec": "H+"},
        "Br": {"mass": 79.9,  "color": "sienna",         "nuc": "Br-", "elec": "H+"},
        "I":  {"mass": 127.0, "color": "mediumpurple",   "nuc": "I-",  "elec": "H+"},
    }

    def __init__(self):
        self.n_C     = rnd.randint(2, 9)
        self.halogen = rnd.choice(["Cl","Br","I"])
        self.M_X     = self.__class__._HALOGENS[self.halogen]["mass"]

        self.Mr_product = round(14 * self.n_C + 1 + self.M_X, 1)
        self.answer     = self.Mr_product

        sub = str.maketrans("0123456789","0123456789")
        sub2 = {"0":"0","1":"1","2":"2","3":"3","4":"4",
                "5":"5","6":"6","7":"7","8":"8","9":"9"}
        subscript = lambda s: "".join(
            {"0":"0","1":"1","2":"2","3":"3","4":"4",
             "5":"5","6":"6","7":"7","8":"8","9":"9"}.get(c,c) for c in s)
        uni_sub = str.maketrans("0123456789","0123456789")

        sub_map = str.maketrans("0123456789",
                                "₀₁₂₃₄"
                                "₅₆₇₈₉")
        def fmt(n): return str(n).translate(sub_map)

        hn = 2 * self.n_C
        self.alkene_str  = f"C{fmt(self.n_C)}H{fmt(hn)}"
        self.reagent_str = f"H{self.halogen}"
        self.product_str = f"C{fmt(self.n_C)}H{fmt(hn+1)}{self.halogen}"

        self.description = (
            "The diagram shows the electrophilic addition mechanism. "
            "The alkene and reagent formulae are labelled in the diagram. "
            "The product box shows only '?'. "
            "Calculate the relative molecular mass (Mr) of the product. "
            "(Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"
        )
        self.topic      = "Hydrocarbons"
        self.subtopic   = "Reactions of alkenes -- electrophilic addition"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. Identify the reactants: Alkene }} \\mathrm{{C_{{{self.n_C}}}H_{{{hn}}}}} \\text{{ and Reagent }} \\mathrm{{H{self.halogen}}} \\\\"
            f"&\\text{{2. The addition reaction combines them entirely into the product: }} \\mathrm{{C_{{{self.n_C}}}H_{{{hn+1}}}{self.halogen}}} \\\\"
            "&\\text{3. Calculate the relative molecular mass (M}_r\\text{):} \\\\"
            f"&M_r = ({self.n_C} \\times 12.0) + ({hn+1} \\times 1.0) + {self.M_X} \\\\"
            f"&M_r = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.set_xlim(0, 14); ax.set_ylim(0, 6); ax.axis("off")

        hal = self.__class__._HALOGENS[self.halogen]
        add_title_box(ax, 7, 5.5,
                      f"Electrophilic Addition: {self.alkene_str} + {self.reagent_str}",
                      fontsize=13)

        draw_circle_atom(ax, 1.5, 3, "C", radius=0.3, color="black", text_color="white")
        draw_circle_atom(ax, 2.5, 3, "C", radius=0.3, color="black", text_color="white")
        draw_bond(ax, 1.8, 3, 2.2, 3, bond_type="double", linewidth=3)
        ax.text(2.0, 2.1, self.alkene_str, fontsize=11, ha="center",
                fontweight="bold", color="navy")

        ax.text(3.5, 3.5, hal["elec"], fontsize=13, ha="center", fontweight="bold", color="red")
        ax.text(3.5, 2.5, hal["nuc"],  fontsize=13, ha="center", fontweight="bold",
                color=hal["color"])
        draw_curly_arrow(ax, 2, 3.3, 3.3, 3.4, curvature=0.3, color="blue")
        ax.text(2.7, 3.9, "Step 1", fontsize=9, color="blue", fontweight="bold")
        draw_arrow(ax, 4.1, 3, 5.1, 3, arrowstyle="->", color="black", linewidth=2)

        draw_circle_atom(ax, 6.1, 3, "C+", radius=0.35, color="red", text_color="white")
        draw_circle_atom(ax, 7.3, 3, "C",  radius=0.3,  color="black", text_color="white")
        draw_bond(ax, 6.45, 3, 7.0, 3, bond_type="single", linewidth=3)
        ax.text(5.1, 3.5, "H", fontsize=11, ha="center", fontweight="bold")
        draw_bond(ax, 6.1, 3, 5.4, 3.4, bond_type="single", linewidth=2)
        ax.text(6.7, 2.0, "Carbocation intermediate", fontsize=9, ha="center", style="italic")

        ax.text(8.3, 2.6, hal["nuc"], fontsize=13, ha="center",
                fontweight="bold", color=hal["color"])
        draw_curly_arrow(ax, 8.1, 2.8, 6.3, 2.8, curvature=-0.3, color="blue")
        ax.text(7.2, 2.1, "Step 2", fontsize=9, color="blue", fontweight="bold")
        draw_arrow(ax, 9.2, 3, 10.2, 3, arrowstyle="->", color="black", linewidth=2)

        ax.add_patch(patches.FancyBboxPatch(
            (10.5, 2.3), 2.8, 1.4,
            boxstyle="round,pad=0.1", facecolor="lightyellow",
            edgecolor="black", linewidth=2))
        ax.text(11.9, 3.0, "?", fontsize=22, ha="center", va="center",
                fontweight="bold", color="navy")
        ax.text(11.9, 2.1, "Product", fontsize=9, ha="center", style="italic")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches="tight")
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
        
        ch_compounds = [
            {'name': 'methane',     'formula': 'CH₄',       'ch_bonds': 4},
            {'name': 'ethane',      'formula': 'C₂H₆',      'ch_bonds': 6},
            {'name': 'propane',     'formula': 'C₃H₈',      'ch_bonds': 8},
            {'name': 'butane',      'formula': 'C₄H₁₀',     'ch_bonds': 10},
            {'name': 'ethanol',     'formula': 'C₂H₅OH',    'ch_bonds': 5},
            {'name': 'methanol',    'formula': 'CH₃OH',      'ch_bonds': 3},
            {'name': 'propan-1-ol', 'formula': 'C₃H₇OH',    'ch_bonds': 7},
            {'name': 'ethanal',     'formula': 'CH₃CHO',     'ch_bonds': 4},
            {'name': 'propanal',    'formula': 'CH₃CH₂CHO',  'ch_bonds': 6},
            {'name': 'ethanoic acid','formula': 'CH₃COOH',   'ch_bonds': 3},
            {'name': 'propanone',   'formula': 'CH₃COCH₃',  'ch_bonds': 6},
            {'name': 'chloroethane','formula': 'CH₃CH₂Cl',   'ch_bonds': 5},
        ]
        
        self.compound = rnd.choice(ch_compounds)
        self.answer = self.compound['ch_bonds']
        
        self.description = (
            f"The structural formula of a molecule is shown. "
            "How many C–H bonds does this molecule contain?"
        )
        
        self.topic = "Organic functional groups"
        self.subtopic = "Structural formulae and bond counting"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        form_tex = self.compound['formula'].translate(tex_map)
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{For the molecule {self.compound['name']} with formula }}\\mathrm{{{form_tex}}}\\text{{,}} \\\\"
            "&\\text{we count the number of hydrogen atoms directly bonded to carbon atoms:} \\\\"
            f"&\\text{{C–H bonds}} = {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        draw_labeled_box(ax, 2, 1.5, 6, 1.5,
                        self.compound['formula'],
                        '(Structural Formula)',
                        facecolor='lightyellow')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem035:
    """
    Topic: 19 — Amide / condensation reactions
    Visual: Acid + Amine → Amide + H₂O diagram; product Mr NOT shown
    Task: Read reactant formulae from diagram, work out amide formula, calculate Mr
    Variance: n_acid ∈ [0,8], n_amine ∈ [0,4] → 13 unique Mr values (sum s=0..12)
    """

    def __init__(self):
        self.n_acid  = rnd.randint(0, 8)
        self.n_amine = rnd.randint(0, 4)

        acid_name_map = [
            'methanoic acid', 'ethanoic acid', 'propanoic acid', 'butanoic acid',
            'pentanoic acid',  'hexanoic acid', 'heptanoic acid', 'octanoic acid',
            'nonanoic acid',
        ]
        amine_name_map = ['ammonia','methylamine','ethylamine','propylamine','butylamine']

        n  = self.n_acid
        m  = self.n_amine

        if n == 0:
            self.acid_formula = 'HCOOH'
        elif n == 1:
            self.acid_formula = 'CH₃COOH'
        else:
            self.acid_formula = f'C{n}H{2*n+1}COOH'

        if m == 0:
            self.amine_formula = 'NH₃'
        elif m == 1:
            self.amine_formula = 'CH₃NH₂'
        else:
            self.amine_formula = f'C{m}H{2*m+1}NH₂'

        # amide product formula
        total_C = n + 1 + m   # acyl C + amine C
        if m == 0:
            if n == 0:
                self.amide_formula = 'HCONH₂'
            elif n == 1:
                self.amide_formula = 'CH₃CONH₂'
            else:
                self.amide_formula = f'C{n}H{2*n+1}CONH₂'
        else:
            if n == 0:
                self.amide_formula = f'HCONHC{m}H{2*m+1}' if m > 1 else 'HCONHCH₃'
            elif n == 1:
                self.amide_formula = f'CH₃CONHC{m}H{2*m+1}' if m > 1 else 'CH₃CONHCH₃'
            else:
                self.amide_formula = f'C{n}H{2*n+1}CONHC{m}H{2*m+1}' if m > 1                     else f'C{n}H{2*n+1}CONHCH₃'

        self.acid_name  = acid_name_map[n]
        self.amine_name = amine_name_map[m]

        # Mr(amide) = Mr(acid) + Mr(amine) - 18 = 14*(n+m) + 45
        s = n + m
        self.Mr_amide = 14 * s + 45
        self.answer   = self.Mr_amide

        self.description = (
            f"The diagram shows the formation of an amide from a carboxylic acid "
            f"and an amine. The reactant formulae are shown in the diagram. "
            f"Calculate the relative molecular mass (Mr) of the amide product. "
            f"(Ar: H=1, C=12, N=14, O=16)"
        )

        self.topic      = "Nitrogen compounds"
        self.subtopic   = "Amide formation"
        self.source     = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"

        Mr_acid  = 14 * self.n_acid + 46
        Mr_amine = 14 * self.n_amine + 17
        
        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        acid_tex = self.acid_formula.translate(tex_map)
        amine_tex = self.amine_formula.translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Calculate the } M_r \\text{ of the reactants:} \\\\"
            f"&\\quad \\text{{Acid }} (\\mathrm{{{acid_tex}}}): M_r = {Mr_acid} \\\\"
            f"&\\quad \\text{{Amine }} (\\mathrm{{{amine_tex}}}): M_r = {Mr_amine} \\\\"
            "&\\text{2. Amide formation is a condensation reaction that releases water (} \\mathrm{H_2O}\\text{, } M_r = 18 \\text{).} \\\\"
            "&\\text{3. Calculate the } M_r \\text{ of the amide product:} \\\\"
            "&\\quad M_r(\\text{amide}) = M_r(\\text{acid}) + M_r(\\text{amine}) - M_r(\\mathrm{H_2O}) \\\\"
            f"&\\quad M_r(\\text{{amide}}) = {Mr_acid} + {Mr_amine} - 18 \\\\"
            f"&\\quad M_r(\\text{{amide}}) = {self.Mr_amide}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_xlim(0, 12); ax.set_ylim(0, 7); ax.axis('off')

        add_title_box(ax, 6, 6.5, 'Amide Formation Reaction', fontsize=14)

        draw_labeled_box(ax, 0.5, 4.0, 3.0, 1.5, self.acid_formula,
                         'Carboxylic Acid', facecolor='lightblue')
        ax.text(4.2, 4.75, '+', fontsize=20, ha='center', fontweight='bold')
        draw_labeled_box(ax, 5.0, 4.0, 3.0, 1.5, self.amine_formula,
                         'Amine', facecolor='lightgreen')

        draw_arrow(ax, 6, 3.8, 6, 2.5, label='Heat', label_position='side',
                   label_offset=1.2, color='red', linewidth=3)

        draw_labeled_box(ax, 2.0, 1.0, 8.0, 1.5,
                         self.amide_formula + '   +   H₂O',
                         'Amide product  (Mr = ?)', facecolor='lightyellow')

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
        
        monomers = [
            {'monomer': 'CH₂=CH₂',     'repeat': '—CH₂—CH₂—',        'name': 'Poly(ethene)',
             'Mr_repeat': 28},
            {'monomer': 'CH₂=CHCH₃',   'repeat': '—CH₂—CH(CH₃)—',    'name': 'Poly(propene)',
             'Mr_repeat': 42},
            {'monomer': 'CH₂=CHCl',    'repeat': '—CH₂—CHCl—',        'name': 'Poly(chloroethene)',
             'Mr_repeat': 62.5},
            {'monomer': 'CF₂=CF₂',     'repeat': '—CF₂—CF₂—',         'name': 'Poly(tetrafluoroethene)',
             'Mr_repeat': 100},
            {'monomer': 'CH₂=CHCN',    'repeat': '—CH₂—CH(CN)—',      'name': 'Poly(propenenitrile)',
             'Mr_repeat': 53},
            {'monomer': 'CH₂=CHF',     'repeat': '—CH₂—CHF—',          'name': 'Poly(fluoroethene)',
             'Mr_repeat': 46},
            {'monomer': 'CH₂=C(CH₃)₂','repeat': '—CH₂—C(CH₃)₂—',    'name': 'Poly(2-methylpropene)',
             'Mr_repeat': 56},
        ]
        
        self.mono = rnd.choice(monomers)
        self.monomer = self.mono['monomer']
        self.polymer_name = self.mono['name']
        self.repeating_unit = self.mono['repeat']
        self.Mr_repeat = self.mono['Mr_repeat']
        
        # degree of polymerization n
        self.n = rnd.randint(5, 50)
        self.total_Mr = round(self.n * self.Mr_repeat)
        self.answer = self.n
        
        self.description = (
            "The diagram shows an addition polymer. Using the repeating unit "
            "and the total relative molecular mass (Mr) provided in the image, "
            "calculate the degree of polymerization n."
        )
        
        self.topic = "Polymerization"
        self.subtopic = "Addition polymerization"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Polymer: {self.polymer_name}}} &\\\\"
            f"M_r(\\text{{repeating unit}}) &= {self.Mr_repeat}\\\\"
            f"M_r(\\text{{total}}) &= {self.total_Mr}\\\\"
            f"n &= \\frac{{{self.total_Mr}}}{{{self.Mr_repeat}}} = {self.n}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 7))
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 7)
        ax.axis('off')
        
        ax.text(5.5, 5.5, f'Monomer: {self.monomer}', fontsize=13, ha='center', fontweight='bold')
        
        # Repeating unit bracket diagram
        ax.text(2, 4.0, '...', fontsize=14, ha='center')
        draw_bracket(ax, 2.5, 3.6, 0.7, bracket_type='square', direction='left', linewidth=3)
        ax.text(4.5, 4.0, self.repeating_unit, fontsize=12, ha='center', fontweight='bold')
        draw_bracket(ax, 6.5, 3.6, 0.7, bracket_type='square', direction='right',
                    linewidth=3, subscript='n')
        ax.text(7.5, 4.0, '...', fontsize=14, ha='center')
        
        ax.text(5.5, 2.8, f'Mr of repeating unit = {self.Mr_repeat}',
               fontsize=12, ha='center', color='darkblue',
               bbox=dict(boxstyle='round', facecolor='lightblue'))
        ax.text(5.5, 1.8, f'Total Mr of polymer = {self.total_Mr}',
               fontsize=12, ha='center', color='darkgreen',
               bbox=dict(boxstyle='round', facecolor='lightgreen'))
        
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
        
        pathways = [
            {'title': 'Ethene → Ethanoic Acid',
             'steps': [
                 {'from': 'CH₂=CH₂',  'to': 'CH₃CH₂Br',  'reagent': 'HBr'},
                 {'from': 'CH₃CH₂Br', 'to': 'CH₃CH₂OH',  'reagent': 'NaOH(aq)'},
                 {'from': 'CH₃CH₂OH', 'to': 'CH₃COOH',   'reagent': 'K₂Cr₂O₇/H₂SO₄'},
             ]},
            {'title': 'Propene → Propan-2-ol → Propanone',
             'steps': [
                 {'from': 'CH₃CH=CH₂',  'to': 'CH₃CHOHCH₃', 'reagent': 'H₂O/H₂SO₄'},
                 {'from': 'CH₃CHOHCH₃', 'to': 'CH₃COCH₃',   'reagent': 'K₂Cr₂O₇/H₂SO₄'},
             ]},
            {'title': 'Bromoethane → Ethanol → Ethanal',
             'steps': [
                 {'from': 'CH₃CH₂Br', 'to': 'CH₃CH₂OH', 'reagent': 'NaOH(aq)'},
                 {'from': 'CH₃CH₂OH', 'to': 'CH₃CHO',   'reagent': 'K₂Cr₂O₇/H₂SO₄'},
             ]},
            {'title': 'Ethanol → Ethyl Ethanoate',
             'steps': [
                 {'from': 'CH₃CH₂OH', 'to': 'CH₃COOC₂H₅', 'reagent': 'CH₃COOH/H₂SO₄'},
             ]},
            {'title': 'Chloroethane → Ethanol → Ethanal → Ethanoic acid',
             'steps': [
                 {'from': 'CH₃CH₂Cl', 'to': 'CH₃CH₂OH', 'reagent': 'NaOH(aq)'},
                 {'from': 'CH₃CH₂OH', 'to': 'CH₃CHO',   'reagent': 'K₂Cr₂O₇ distil'},
                 {'from': 'CH₃CHO',   'to': 'CH₃COOH',  'reagent': 'K₂Cr₂O₇ reflux'},
             ]},
        ]
        
        self.pathway = rnd.choice(pathways)
        self.steps = self.pathway['steps']
        n_steps = len(self.steps)
        
        # Random yield for each step (60–95%)
        self.step_yields = [rnd.randint(60, 95) for _ in range(n_steps)]
        
        # Overall yield = product of all step yields / 100^(n-1)
        overall = self.step_yields[0]
        for y in self.step_yields[1:]:
            overall = overall * y / 100
        self.answer = round(overall, 1)
        
        self.description = (
            f"The diagram shows a multi-step synthesis: {self.pathway['title']}. "
            f"Each step yield is labelled on the diagram. "
            f"Calculate the overall percentage yield (to 1 d.p.)."
        )
        
        self.topic = "Organic synthesis"
        self.subtopic = "Synthetic routes"
        self.source = "Adapted from Cambridge A-Level Chemistry"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Overall yield} &= "
        )
        reasoning += " \\times ".join([f"\\frac{{{y}}}{{100}}" for y in self.step_yields])
        reasoning += f" \\times 100\\\\ &= {self.answer}\\%"
        reasoning += "\\end{aligned}\\]"
        self.reasoning = reasoning
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 9))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 9)
        ax.axis('off')
        
        add_title_box(ax, 6, 8.5, f'Synthesis: {self.pathway["title"]}', fontsize=13)
        
        compounds = [self.steps[0]['from']] + [s['to'] for s in self.steps]
        n = len(compounds)
        y_positions = [7.5 - i * (6.5 / (n - 1 + 0.0001)) for i in range(n)]
        
        for i, (comp, y) in enumerate(zip(compounds, y_positions)):
            draw_labeled_box(ax, 1, y - 0.4, 3, 0.8, comp, f'Compound {i+1}',
                            facecolor='lightblue')
        
        for i, (step, y_pct) in enumerate(zip(self.steps, self.step_yields)):
            y_mid = (y_positions[i] + y_positions[i + 1]) / 2
            draw_arrow(ax, 2.5, y_positions[i] - 0.5, 2.5, y_positions[i + 1] + 0.5,
                      arrowstyle='->', color='red', linewidth=2)
            ax.text(5.5, y_mid, f'{step["reagent"]}',
                   fontsize=10, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor='lightyellow'))
            ax.text(8.5, y_mid, f'Yield: {y_pct}%',
                   fontsize=11, ha='center', va='center', fontweight='bold', color='darkgreen',
                   bbox=dict(boxstyle='round', facecolor='lightgreen'))

        
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
            "The mass spectrum of an organic compound is shown. "
            "What is the m/z value of the molecular ion peak (M⁺)?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "Mass spectrometry"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. The molecular ion (M}^+\\text{) peak represents the intact molecule that has lost one electron.} \\\\"
            "&\\text{2. In a mass spectrum, this corresponds to the significant peak with the highest m/z value} \\\\"
            "&\\quad \\text{(furthest to the right, ignoring any tiny M+1 isotope peaks).} \\\\"
            f"&\\text{{3. Reading the x-axis for this highest peak gives: M}}^+ = {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Draw fragment peaks
        for frag in self.fragments:
            draw_mass_spectrum_peak(ax, frag['mz'], frag['intensity'],
                                   width=0.8, color='steelblue', label_offset=3)
        
        draw_mass_spectrum_peak(ax, self.M_plus, 100, width=0.8,
                               color='steelblue', label_offset=5)
        
        ax.set_xlabel('m/z (mass-to-charge ratio)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Relative Intensity (%)', fontsize=14, fontweight='bold')
        ax.set_title(f'Mass Spectrum', fontsize=16, fontweight='bold')
        
        ax.set_xlim(0, self.M_plus + 15)
        ax.set_ylim(0, 125)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        # Mark the x-axis exactly at the points of interest
        x_ticks = [frag['mz'] for frag in self.fragments] + [self.M_plus]
        ax.set_xticks(x_ticks)
        
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
        self.question_type = "Short Answer"
        
        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        form_tex = self.mol['formula'].translate(tex_map)
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The compound is {self.mol['name']} (}}\\mathrm{{{form_tex}}}\\text{{).}} \\\\"
            f"&\\text{{2. We are looking for the characteristic absorption peak of the {self.ask_group}.}} \\\\"
            "&\\text{3. By examining the provided IR spectrum, we locate the significant dip} \\\\"
            "&\\quad \\text{corresponding to this functional group's typical frequency range.} \\\\"
            f"&\\text{{4. Reading the marked value on the x-axis gives wavenumber: {self.answer} cm}}^{{-1}}"
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
            f"The ¹H NMR spectrum of an organic compound is shown. "
            f"The highlighted peak (in red) appears at δ = {self.ask_shift} ppm. "
            f"How many hydrogen atoms are responsible for this peak?"
        )
        
        self.topic = "Analytical techniques"
        self.subtopic = "NMR spectroscopy"
        self.source = "Adapted from Cambridge A-Level Chemistry 9701"
        self.curriculum = "A-Level"
        self.question_type = "Short Answer"
        
        # Convert Unicode subscripts to standard LaTeX math format
        tex_map = str.maketrans({
            '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4', 
            '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9'
        })
        form_tex = self.mol['formula'].translate(tex_map)
        
        # Find the specific peak data being asked about to get its assignment
        target_peak = next(p for p in self.peaks if p['shift'] == self.ask_shift)
        assignment_tex = target_peak['assignment'].translate(tex_map)

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"&\\text{{1. The compound is {self.mol['name']} (}}\\mathrm{{{form_tex}}}\\text{{).}} \\\\"
            f"&\\text{{2. We analyze the specific chemical environment at }} \\delta = {self.ask_shift}\\text{{ ppm.}} \\\\"
            f"&\\text{{3. Based on the chemical shift, this peak corresponds to the }} \\mathrm{{{assignment_tex}}} \\text{{ protons.}} \\\\"
            f"&\\text{{4. By counting the protons in this environment, we determine the integration value:}} \\\\"
            f"&\\text{{Number of H atoms responsible for the peak}} = {self.answer}"
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
        self.question_type = "Short Answer"
        
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
        
        ax.set_ylim(0, self.activation_E * 1.2)
        ax.set_title('Enthalpy Profile Diagram', fontsize=16, fontweight='bold')
        ax.set_yticks([self.product_E, self.reactant_E, self.activation_E])
        ax.set_yticklabels([f'{self.product_E}', f'{self.reactant_E}', f'{self.activation_E}'], fontsize=11)
        
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
        self.delta_Hc_X = -rnd.randint(300, 600)
        self.delta_Hc_Y = -rnd.randint(1500, 2500)
        self.delta_Hc_Z = -rnd.randint(300, 600)
        self.delta_Hc_XYZ = -rnd.randint(800, 1200) # Dedicated variable for the product
        
        self.sum_reactants = self.delta_Hc_X + self.delta_Hc_Y + self.delta_Hc_Z
        
        # Hess's Law for combustion data: Reactants - Products
        self.delta_Hf = self.sum_reactants - self.delta_Hc_XYZ
        self.answer = round(self.delta_Hf, 1)
        
        self.description = (
            f"The diagram shows a Hess's Law cycle for the formation of compound XYZ. "
            f"Given the enthalpy changes of combustion, calculate ΔH°f for XYZ."
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Hess's Law"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Using the Hess's Law cycle provided in the diagram:} \\\\"
            "&\\quad \\Delta H_f = \\Sigma \\Delta H_c(\\text{reactants}) - \\Sigma \\Delta H_c(\\text{products}) \\\\"
            "&\\text{2. Substitute the values directly from the blue arrows:} \\\\"
            f"&\\quad \\Delta H_f = ({self.sum_reactants}) - ({self.delta_Hc_XYZ}) \\\\"
            f"&\\quad \\Delta H_f = {self.answer}\\,\\text{{kJ mol}}^{{-1}}"
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
        
        draw_arrow(ax, 2.5, 6, 6, 2.5, label=f"ΔH°c(X+Y+Z)\n{self.sum_reactants} kJ/mol",
                  label_position='side', color='blue', linewidth=2)
        
        draw_arrow(ax, 9.5, 6, 6, 2.5, label=f"ΔH°c(XYZ)\n{self.delta_Hc_XYZ} kJ/mol",
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
        self.BE_CH = rnd.randint(380, 450)
        self.BE_HH = rnd.randint(400, 480)
        self.BE_CC = rnd.randint(300, 400)
        
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
        self.question_type = "Short Answer"
        
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
        self.delta_H = rnd.randint(40, 300)
        self.delta_S = round(rnd.uniform(0.10, 0.80), 2)
        self.T_equilibrium = self.delta_H / self.delta_S
        self.answer = round(self.T_equilibrium, 0)
        
        self.description = (
            "The graph shows how Gibbs free energy (ΔG) varies with temperature for a reaction. "
            "Use the graph to determine the temperature (in K, to the nearest whole number) "
            "at which the reaction becomes spontaneous."
        )
        
        self.topic = "Chemical energetics"
        self.subtopic = "Entropy and free energy"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. A reaction becomes spontaneous when the Gibbs free energy change (}\\Delta G\\text{) drops below zero.} \\\\"
            "&\\text{2. The exact threshold is the crossover point on the x-axis where } \\Delta G = 0\\text{.} \\\\"
            "&\\text{3. Using the equation provided on the graph, we can solve for this temperature (T):} \\\\"
            f"&\\quad \\Delta G = \\Delta H - T\\Delta S \\\\"
            f"&\\quad 0 = {self.delta_H} - T({self.delta_S}) \\\\"
            f"&\\quad T = \\frac{{{self.delta_H}}}{{{self.delta_S}}} = {self.answer}\\,\\text{{K}}"
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
        
        # Add the specific numerical equation to the top right corner
        ax.text(0.95, 0.95, f"$\\Delta G = {self.delta_H} - {self.delta_S}T$", 
                transform=ax.transAxes, fontsize=16, ha='right', va='top',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='none'))
        
        # Region labels
        ax.text(self.T_equilibrium * 0.4, self.delta_H * 0.7,
               '(ΔG > 0)', fontsize=12, ha='center',
               bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
        ax.text(self.T_equilibrium * 1.25, -self.delta_H * 0.25,
               '(ΔG < 0)', fontsize=12, ha='center',
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
            "The standard half-cell diagram is shown with the standard electrode potentials "
            "labelled in each beaker. Calculate the standard cell potential E°cell (in V, to 2 d.p.)."
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Redox reactions"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
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
            "The diagram shows an electrolysis cell for a specific metal ion solution. "
            "Using the data provided in the diagram, calculate the mass of the metal "
            f"deposited at the cathode. (Relative atomic mass = {self.element[1]}, "
            "Faraday's constant F = 96500 C mol⁻¹)"
        )
        
        self.topic = "Electrochemistry"
        self.subtopic = "Electrolysis"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Convert time to seconds and calculate total charge (Q):} \\\\"
            f"&\\quad t = {self.time_min} \\times 60 = {self.time_s}\\,\\text{{s}} \\\\"
            f"&\\quad Q = I \\times t = {self.current} \\times {self.time_s} = {self.charge}\\,\\text{{C}} \\\\"
            "&\\text{2. Calculate moles of electrons using Faraday's constant (F = 96500 C mol}^{-1}\\text{):} \\\\"
            f"&\\quad n(\\text{{e}}^-) = \\frac{{Q}}{{F}} = \\frac{{{self.charge}}}{{96500}} = {round(self.moles_e, 4)}\\,\\text{{mol}} \\\\"
            f"&\\text{{3. The stoichiometry requires {self.element[2]} mole(s) of electrons per mole of }} \\mathrm{{{self.element[0]}}} \\text{{ deposited:}} \\\\"
            f"&\\quad n(\\mathrm{{{self.element[0]}}}) = \\frac{{{round(self.moles_e, 4)}}}{{{self.element[2]}}} = {round(self.moles_e / self.element[2], 4)}\\,\\text{{mol}} \\\\"
            "&\\text{4. Convert moles of metal to mass:} \\\\"
            f"&\\quad \\text{{Mass}} = n \\times A_r = {round(self.moles_e / self.element[2], 4)} \\times {self.element[1]} \\\\"
            f"&\\quad \\text{{Mass}} = {self.answer}\\,\\text{{g}}"
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
        self.initial_A = round(rnd.uniform(0.5, 4.0), 2)
        self.initial_B = round(rnd.uniform(0.5, 4.0), 2)
        
        self.eq_A = round(self.initial_A * rnd.uniform(0.1, 0.7), 2)
        self.eq_B = round(self.initial_B * rnd.uniform(0.1, 0.7), 2)
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
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. Equilibrium is reached when the concentrations become constant over time} \\\\"
            "&\\quad \\text{(the curves flatten into horizontal lines).} \\\\"
            "&\\text{2. The question asks for the equilibrium concentration of C.} \\\\"
            "&\\text{3. By following the [C] curve to its plateau and reading the marked value:} \\\\"
            f"&\\quad [\\text{{C}}]_{{\\text{{eq}}}} = {self.eq_C}\\,\\text{{mol dm}}^{{-3}}"
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
        
        # --- ADDED MULTIPLE ASYMPTOTES AND LABELS ---
        # We'll loop through the equilibrium values and colors to keep it clean
        eq_values = [
            (self.eq_A, 'blue'), 
            (self.eq_B, 'red'), 
            (self.eq_C, 'green')
        ]
        
        for val, col in eq_values:
            # Horizontal dotted line
            ax.axhline(val, color=col, linestyle=':', linewidth=2, alpha=0.5)
            # Label on the right side with space (x=10.2)
            ax.text(10.2, val, f'{val:.2f}', color=col, fontweight='bold', 
                    va='center', ha='left', fontsize=11)
        # --------------------------------------------

        ax.axvline(7, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(7, max(self.initial_A, self.initial_B) * 0.9, 'Equilibrium', 
               rotation=90, va='bottom', fontsize=11)
        
        ax.set_xlabel('Time', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time', fontsize=16, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)

        # Extend x-limit to 11.5 to provide comfortable space for the labels
        ax.set_xlim(0, 11.5) 
        
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
        self.question_type = "Short Answer"
        
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
        self.initial_conc = round(rnd.uniform(0.5, 5.0), 2)
        self.k = round(rnd.uniform(0.05, 0.6), 3)
        
        self.t_point = 5
        self.conc_at_t = self.initial_conc * np.exp(-self.k * self.t_point)
        exact_rate = -self.k * self.conc_at_t
        
        # Calculate exact tangent intersections with the y-axis (x=0) and x-axis (y=0)
        self.x1 = 0.0
        self.y1 = round(self.conc_at_t - exact_rate * self.t_point, 3)
        
        self.y2 = 0.0
        self.x2 = round(self.t_point - self.conc_at_t / exact_rate, 3)
        
        # Answer is calculated from the EXACT labels shown to avoid rounding discrepancies
        self.rate = (self.y2 - self.y1) / (self.x2 - self.x1)
        self.answer = round(abs(self.rate), 3)
        
        self.description = (
            f"The graph shows how concentration varies with time. "
            f"Calculate the rate of reaction at t = {self.t_point} seconds."
        )
        
        self.topic = "Reaction kinetics"
        self.subtopic = "Rate of reaction"
        self.source = "Adapted from Cambridge A Level Chemistry 9701"
        self.curriculum = "A Level"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{1. The rate of reaction at a specific time is the negative gradient of the tangent.} \\\\"
            f"&\\text{{2. Using the marked x and y intercepts of the tangent line: (0, {self.y1}) and ({self.x2}, 0).}} \\\\"
            "&\\text{3. Calculate the gradient (}\\Delta y / \\Delta x\\text{):} \\\\"
            f"&\\quad \\text{{Gradient}} = \\frac{{{self.y2} - {self.y1}}}{{{self.x2} - 0}} \\\\"
            f"&\\quad \\text{{Rate}} = -\\text{{Gradient}} = {self.answer}\\,\\text{{mol dm}}^{{-3}}\\,\\text{{s}}^{{-1}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Extend time array slightly past x2 to ensure the blue curve is drawn fully
        max_time = max(20, self.x2 + 2)
        time = np.linspace(0, max_time, 100)
        conc = self.initial_conc * np.exp(-self.k * time)
        
        ax.plot(time, conc, 'b-', linewidth=2.5)
        
        # Plot the tangent line using our specific x and y coordinates
        tangent_x = np.array([self.x1, self.x2])
        tangent_y = np.array([self.y1, self.y2])
        ax.plot(tangent_x, tangent_y, 'r--', linewidth=2, label='Tangent')
        
        # Mark the endpoints and add coordinate labels
        ax.plot(tangent_x, tangent_y, 'ko', markersize=6) 
        
        offset = self.initial_conc * 0.04 # dynamic vertical offset
        ax.text(self.x1, self.y1 + offset, f'({self.x1}, {self.y1:.3f})', 
                color='red', fontsize=11, ha='left', va='bottom',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        
        ax.text(self.x2, self.y2 + offset, f'({self.x2:.3f}, {self.y2})', 
                color='red', fontsize=11, ha='center', va='bottom',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        
        ax.plot(self.t_point, self.conc_at_t, 'ro', markersize=10)
        
        ax.set_xlabel('Time (s)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Concentration (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_title('Concentration vs Time', fontsize=16, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Dynamically scale axes so both intercepts are always comfortably in frame
        ax.set_xlim(0, max_time)
        ax.set_ylim(0, max(self.initial_conc * 1.1, self.y1 * 1.1))
        
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
        
        concentrations = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0])
        k = round(rnd.uniform(0.2, 2.0), 2)
        
        if self.order == 0:
            rates = np.full_like(concentrations, round(rnd.uniform(0.02, 0.15), 3))
            self.answer = 0
            shape_desc = "a horizontal straight line"
            math_rel = "\\text{Rate is independent of [A]}"
        elif self.order == 1:
            rates = k * concentrations
            self.answer = 1
            shape_desc = "a straight diagonal line through the origin"
            math_rel = "\\text{Rate} \\propto [\\text{A}]^1"
        else:
            rates = k * concentrations**2
            self.answer = 2
            shape_desc = "an upward curve passing through the origin"
            math_rel = "\\text{Rate} \\propto [\\text{A}]^2"
            
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
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\text{The graph plots the initial rate of reaction against the concentration of A.} \\\\"
            f"&\\text{{Visually, the data points form {shape_desc}.}} \\\\"
            f"&\\text{{This specific shape demonstrates that }} {math_rel}\\text{{.}} \\\\"
            f"&\\text{{Therefore, the order of reaction is {self.answer}.}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        
        ax.plot(self.concentrations, self.rates, 'bo-', markersize=10, linewidth=2.5)
        
        ax.set_xlabel('[A] (mol dm⁻³)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Rate (mol dm⁻³ s⁻¹)', fontsize=14, fontweight='bold')
        ax.set_title('Rate vs Concentration', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1.1)
        ax.set_ylim(0, max(self.rates) * 1.2)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
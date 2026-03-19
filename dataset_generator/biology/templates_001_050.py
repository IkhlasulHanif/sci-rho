import random as rnd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Circle
from PIL import Image
from biology.helper import *

# target folder : "root/dataset/biology/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "biology", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Bio001:
    
    def __init__(self):
        self.image_mm = rnd.randint(20, 50)
        self.mags = rnd.choice([400, 500, 800, 1000, 1200, 1500, 2000, 3000])
        self.actual_length_mm = self.image_mm / self.mags
        self.answer = round((self.actual_length_mm) * 1000, 2)

        self.description = (
            f"The photomicrograph shows a plant cell. Line XY shows the image length of the cell. Calculate the actual length of the cell in µm."
        )
        self.topic = "Organisation of the organism"
        self.subtopic = "Size of specimens"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Measured image length (I)}} &= {self.image_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Magnification (M)}} &= \\times{self.mags}\\\\"
            f"\\text{{The formula for actual size is:}} &\\\\"
            f"\\text{{Actual size (A)}} &= \\frac{{\\text{{Image length (I)}}}}{{\\text{{Magnification (M)}}}}\\\\"
            f"&= \\frac{{{self.image_mm}\\,\\text{{mm}}}}{{{self.mags}}}\\\\"
            f"&= {round(self.actual_length_mm, 10)}\\,\\text{{mm}}\\\\"
            f"\\text{{Convert mm to }} \\mu\\text{{m:}} &\\\\"
            f"\\text{{Actual size in }} \\mu\\text{{m}} &= {round(self.actual_length_mm, 10)} \\times 1000\\\\"
            f"&= {self.answer}\\,\\mu\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio001temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(330, 312, f"{self.image_mm} mm", fontsize=8)
        ax.text(800, 274, f"x{self.mags}", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio002:

    def __init__(self):
        self.image_cm = rnd.randint(30, 50)
        self.actual_length_mm = rnd.randint(30, 150)
        self.image_mm = self.image_cm * 10
        self.answer = round(self.image_mm / self.actual_length_mm, 2)

        self.description = (
            f"Karen drew a sketch of a shell. Using the measurements provided, calculate the magnification of the sketch compared to the actual shell."
        )
        self.topic = "Organisation of the organism"
        self.subtopic = "Size of specimens"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length of image (cm)}} &= {self.image_cm}\\,\\text{{cm}}\\\\"
            f"\\text{{Actual length (mm)}} &= {self.actual_length_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Convert image length to mm:}} &\\\\"
            f"\\text{{Length of image (mm)}} &= \\text{{Length (cm)}} \\times 10\\\\"
            f"&= {self.image_cm} \\times 10\\\\"
            f"&= {self.image_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Magnification is given by:}} &\\\\"
            f"M &= \\frac{{\\text{{Length of image}}}}{{\\text{{Actual length}}}}\\\\"
            f"&= \\frac{{{self.image_mm}}}{{{self.actual_length_mm}}}\\\\"
            f"&= {round(self.image_mm / self.actual_length_mm, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio002temp.jpg')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(900, 730, f"{self.image_cm} cm", fontsize=8)
        ax.text(890, 1045, f"{self.actual_length_mm} mm", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio003:
    
    def __init__(self):
        self.dominant_pheno = "Red"
        self.recessive_pheno = "White"
        self.dom_allele= "R"
        self.rec_allele = "r"
        self.parent1 = monohybrid_generate_genotype(self.dom_allele, self.rec_allele)
        self.parent2 = monohybrid_generate_genotype(self.dom_allele, self.rec_allele)
        self.sample_size = rnd.choice([40, 60, 100, 120, 400, 1000])

        p1_gametes = [self.parent1[0], self.parent1[1]]
        p2_gametes = [self.parent2[0], self.parent2[1]]

        offspring = []
        for g1 in p1_gametes:
            for g2 in p2_gametes:
                alleles = [g1, g2]
                alleles.sort(key=lambda a: (a.islower(), a))
                offspring.append("".join(alleles))

        self.offspring = offspring
        self.recessive_genotype = self.rec_allele * 2
        self.recessive_count = self.offspring.count(self.recessive_genotype)
        self.recessive_frac = self.recessive_count / len(self.offspring)
        self.answer = int(round(self.recessive_frac * self.sample_size))

        self.description = f"A geneticist crosses two Red Roses ({self.dominant_pheno} x {self.recessive_pheno}). The resulting Punnett square can be seen below. If the resulting seeds produce a total of {self.sample_size} plants, calculate the expected number of {self.recessive_pheno} roses."
        self.topic = "Inheritance"
        self.subtopic = "Monohybrid inheritance"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Parent 1 Genotype}} &= {self.parent1}\\\\"
            f"\\text{{Parent 2 Genotype}} &= {self.parent2}\\\\"
            f"\\text{{Possible Offspring Genotypes}} &= \\{{ {self.offspring[0]}, {self.offspring[1]}, {self.offspring[2]}, {self.offspring[3]} \\}}\\\\"
            f"\\text{{Recessive Genotype}} &= {self.recessive_genotype}\\\\"
            f"\\text{{Recessive Frequency}} &= \\frac{{\\text{{Count of }} {self.recessive_genotype}}}{{\\text{{Total Offspring}}}}\\\\"
            f"P(\\text{{{self.recessive_pheno}}}) &= \\frac{{{self.recessive_count}}}{{4}} = {round(self.recessive_frac, 10)}\\\\"
            f"\\text{{Expected Number}} &= P(\\text{{{self.recessive_pheno}}}) \\times \\text{{Sample Size}}\\\\"
            f"E &= {round(self.recessive_frac, 10)} \\times {self.sample_size}\\\\"
            f"E &= {self.answer}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_axis_off()

        table_data = [
            ["", self.parent2[0], self.parent2[1]],
            [self.parent1[0], self.offspring[0], self.offspring[1]],
            [self.parent1[1], self.offspring[2], self.offspring[3]],
        ]

        table = ax.table(
            cellText=table_data,
            loc="center",
            cellLoc="center",
            bbox=[0.1, 0.1, 0.8, 0.8],
        )
        table.auto_set_font_size(False)
        table.set_fontsize(24)

        for (row, col), cell in table.get_celld().items():
            if row == 0 or col == 0:
                cell.set_facecolor("#efefef")
                cell.get_text().set_weight("bold")
            cell.set_linewidth(2)

        plt.text(0.5, 0.92, "Parent 2 Gametes", ha="center", fontsize=16, weight="bold")
        plt.text(0.02, 0.5, "Parent 1 Gametes", va="center", rotation=90, fontsize=16, weight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio004:
    
    def __init__(self):
        self.start_year_limit = 1990
        self.end_year_limit = 2004
        self.step = 2
        self.years = list(range(self.start_year_limit, self.end_year_limit + self.step, self.step))
        self.populations = []
        current_pop = rnd.choice([20, 30, 40])
        for _ in self.years:
            self.populations.append(current_pop)
            increase = rnd.randrange(50, 90, 10)
            current_pop = min(current_pop + increase, 600)

        self.selected_years = sorted(rnd.sample(self.years, 2))
        self.year_a = self.selected_years[0]
        self.year_b = self.selected_years[1]
        self.pop_a = self.populations[self.years.index(self.year_a)]
        self.pop_b = self.populations[self.years.index(self.year_b)]

        self.diff = self.pop_b - self.pop_a
        self.decimal_increase = self.diff / self.pop_a
        self.percentage_increase = self.decimal_increase * 100
        self.answer = int(round(self.percentage_increase))

        self.description = f"The graph shows how the population of a species of bird has increased following a conservation programme. Based on the graph, calculate the percentage increase in the number of breeding pairs of birds from {self.year_a} to {self.year_b}. Round the answer to the nearest whole number."
        self.topic = "Organisms and their environment"
        self.subtopic = "Populations"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Population in {self.year_a}}} &= {self.pop_a}\\\\"
            f"\\text{{Population in {self.year_b}}} &= {self.pop_b}\\\\"
            f"\\text{{Increase}} &= \\text{{Population}}_{{{self.year_b}}} - \\text{{Population}}_{{{self.year_a}}}\\\\"
            f"&= {self.pop_b} - {self.pop_a}\\\\"
            f"&= {self.diff}\\\\"
            f"\\text{{Percentage Increase}} &= \\left( \\frac{{\\text{{Increase}}}}{{\\text{{Original Value}}}} \\right) \\times 100\\\\"
            f"&= \\left( \\frac{{{self.diff}}}{{{self.pop_a}}} \\right) \\times 100\\\\"
            f"&= {round(self.decimal_increase, 10)} \\times 100\\\\"
            f"&= {round(self.percentage_increase, 10)}\\%\\\\"
            f"\\text{{Rounding to nearest whole number:}} &\\\\"
            f"\\text{{Percentage Increase}} &= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
    
        ax.bar(self.years, self.populations, color='white', edgecolor='black', linewidth=1.2, width=1.2, zorder=3)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Number of\nbreeding pairs\nof birds', rotation=0, labelpad=50, va='center', fontsize=12)
        ax.set_ylim(0, 600)
        ax.set_xlim(self.start_year_limit - 1, self.end_year_limit + 1)
        
        ax.set_xticks(self.years)
        
        ax.set_box_aspect(1)
        
        ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.4))

        ax.grid(which='major', linestyle='-', linewidth=1.0, color='black', alpha=0.8, zorder=1)
        ax.grid(which='minor', linestyle='-', linewidth=0.5, color='black', alpha=0.5, zorder=1)
        
        ax.set_axisbelow(True)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio005:
    
    def __init__(self):
        self.time_points = np.array([0, 4, 10, 16, 20]) 
        self.lag_pop = rnd.randrange(20, 60, 10)
        self.log_start_pop = self.lag_pop + rnd.randrange(10, 40, 10)
        self.log_end_pop = rnd.randrange(350, 490, 10)
        self.stationary_pop = self.log_end_pop + rnd.choice([-10, 10])
        self.death_pop = rnd.randint(50, 150)
        self.pop_points = np.array([self.lag_pop, self.log_start_pop, self.log_end_pop, self.stationary_pop, self.death_pop])

        self.diff = self.log_end_pop - self.log_start_pop
        self.decimal_increase = self.diff / self.log_start_pop
        self.percentage_increase = self.decimal_increase * 100
        self.answer = round(self.percentage_increase, 2)

        self.description = (
            f"The graph shows the growth curve of a bacterial culture. Calculate the percentage increase in the population during the log phase."
        )
        self.topic = "Organisms and their environment"
        self.subtopic = "Populations"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Population at start of log phase (4h)}} &= {self.log_start_pop}\\\\"
            f"\\text{{Population at end of log phase (10h)}} &= {self.log_end_pop}\\\\"
            f"\\text{{Increase in population}} &= \\text{{Final Population}} - \\text{{Initial Population}}\\\\"
            f"&= {self.log_end_pop} - {self.log_start_pop}\\\\"
            f"&= {self.diff}\\\\"
            f"\\text{{Percentage increase}} &= \\left( \\frac{{\\text{{Increase}}}}{{\\text{{Initial Population}}}} \\right) \\times 100\\\\"
            f"&= \\left( \\frac{{{self.diff}}}{{{self.log_start_pop}}} \\right) \\times 100\\\\"
            f"&= {round(self.decimal_increase, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.figure(figsize=(9, 5))

        x_smooth = np.linspace(self.time_points.min(), self.time_points.max(), 400)
        y_smooth = make_curve_pchip(self.time_points, self.pop_points, x_smooth)

        plt.plot(x_smooth, y_smooth, linewidth=1.8)
        plt.plot(self.time_points, self.pop_points, linestyle="none", marker="o", markersize=6, markeredgewidth=0.8)

        plt.title("Bacterial Growth Curve")
        plt.xlabel("Time")
        plt.ylabel("Population")

        ax = plt.gca()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

        ax.grid(which="major", linestyle="--", linewidth=0.8, alpha=0.7)
        ax.grid(which="minor", linestyle=":", linewidth=0.5, alpha=0.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio006:

    def __init__(self):
        self.maize = "Producer"
        self.locust = "Primary Consumer"
        self.lizard = "Secondary Consumer"
        self.snake = "Tertiary Consumer"
        self.trophics_names = [self.maize, self.locust, self.lizard, self.snake]
        self.maize_energy = rnd.randrange(7000, 10000, 250)
        self.locust_energy = (rnd.randint(8, 12) / 100) * self.maize_energy
        self.lizard_energy = round((rnd.randint(8, 12) / 100) * self.locust_energy, 2)
        self.snake_energy = round((rnd.randint(8, 12) / 100) * self.lizard_energy, 2)
        self.trophics_energy = [self.maize_energy, self.locust_energy, self.lizard_energy, self.snake_energy]

        self.indexA = rnd.randint(0, 2)
        self.indexB = rnd.randint(self.indexA + 1, 3)

        self.trophicA = self.trophics_energy[self.indexA]
        self.trophicB = self.trophics_energy[self.indexB]
        self.energy_transfer = (self.trophicB / self.trophicA)
        self.answer = round(self.energy_transfer * 100, 2)

        self.description = f"This diagram shows a food chain. What is the efficiency of energy transfer between {self.trophics_names[self.indexA] and {self.trophics_names[self.indexB]}}?"
        self.topic = "Organisms and their environment"
        self.subtopic = "Food chains and food webs"
        self.source = "IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Energy at }} {self.trophics_names[self.indexA]} &= {self.trophics_energy[self.indexA]}\\,\\text{{kJ}}\\\\"
            f"\\text{{Energy at }} {self.trophics_names[self.indexB]} &= {self.trophics_energy[self.indexB]}\\,\\text{{kJ}}\\\\"
            f"\\text{{Efficiency of energy transfer is given by:}} &\\\\"
            f"\\text{{Efficiency}} &= \\left( \\frac{{\\text{{Energy at higher trophic level}}}}{{\\text{{Energy at lower trophic level}}}} \\right) \\times 100\\\\"
            f"&= \\left( \\frac{{{self.trophics_energy[self.indexB]}}}{{{self.trophics_energy[self.indexA]}}} \\right) \\times 100\\\\"
            f"&= {round(self.energy_transfer, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio006temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(170, 780, f"{self.maize_energy} kJ", fontsize=8)
        ax.text(650, 780, f"{self.locust_energy} kJ", fontsize=8)
        ax.text(1118, 780, f"{self.lizard_energy} kJ", fontsize=8)
        ax.text(1590, 780, f"{self.snake_energy} kJ", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio007:

    def __init__(self):
        self.cell_width_um = rnd.randint(30, 60)
        self.cell_height_um = rnd.randint(10, 20)
        self.surface_area_cm = rnd.randint(40, 70)
        self.surface_area_um = self.surface_area_cm * 1e8
        self.cell_area_um = self.cell_width_um * self.cell_height_um
        self.answer = round(self.surface_area_um / self.cell_area_um)

        self.description = f"These are part of a continuous layer of cells forming the upper surface of a leaf. Assume that all these cells are identical in size. If the total area of the upper surface of the leaf is {self.surface_area_cm} cm², calculate the number of cells in the upper surface of the leaf. Round the answer to a whole number."
        self.topic = "Cell structure"
        self.subtopic = "The microscope in cell studies"
        self.source = "AQA"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Cell width}} &= {self.cell_width_um}\\,\\mu\\text{{m}}\\\\"
            f"\\text{{Cell height}} &= {self.cell_height_um}\\,\\mu\\text{{m}}\\\\"
            f"\\text{{Surface area of leaf}} &= {self.surface_area_cm}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Convert surface area to }} \\mu\\text{{m}}^2: &\\\\"
            f"\\text{{Surface area (}} \\mu\\text{{m}}^2) &= \\text{{Area (cm}}^2) \\times 10^8\\\\"
            f"&= {self.surface_area_cm} \\times 10^8\\\\"
            f"&= {self.surface_area_um}\\,\\mu\\text{{m}}^2\\\\"
            f"\\text{{Area of one cell:}} &\\\\"
            f"A_{{\\text{{cell}}}} &= \\text{{width}} \\times \\text{{height}}\\\\"
            f"&= {self.cell_width_um} \\times {self.cell_height_um}\\\\"
            f"&= {self.cell_area_um}\\,\\mu\\text{{m}}^2\\\\"
            f"\\text{{Number of cells:}} &\\\\"
            f"N &= \\frac{{\\text{{Total surface area}}}}{{\\text{{Area of one cell}}}}\\\\"
            f"&= \\frac{{{self.surface_area_um}}}{{{self.cell_area_um}}}\\\\"
            f"&= {round(self.surface_area_um / self.cell_area_um, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio007temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(60, 310, f"{self.cell_height_um} μm", fontsize=8)
        ax.text(358, 900, f"{self.cell_width_um} μm", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio008:

    def __init__(self):
        self.species = ["Hydrocotyle vulgaris", "Plantago maritima", "Ranunculus acris", "Hieracium pilosella", "Calliergon cuspidatum", "Prunella vulgaris", "Pseudoscleropodium purum"]
        self.num_individuals = [rnd.randint(5, 22) for _ in self.species]
        self.N = sum(self.num_individuals)
        self.n_n1 = [n*(n - 1) for n in self.num_individuals]
        self.sum_n_n1 = sum(self.n_n1)
        self.answer = round(self.N * (self.N - 1) / self.sum_n_n1, 2)

        self.description = f"The table shows plant species recorded at one site, on one island, in 1975. Calculate the index of diversity for this site!"
        self.topic = "Classification, biodiversity and conservation"
        self.subtopic = "Biodiversity"
        self.source = "AQA"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total number of individuals (N)}} &= {self.N}\\\\"
            f"\\sum n(n-1) &= {self.sum_n_n1}\\\\"
            f"\\text{{Simpson's Index of Diversity (D) is given by:}} &\\\\"
            f"D &= \\frac{{N(N-1)}}{{\\sum n(n-1)}}\\\\"
            f"&= \\frac{{{self.N}({self.N}-1)}}{{{self.sum_n_n1}}}\\\\"
            f"&= \\frac{{{self.N * (self.N - 1)}}}{{{self.sum_n_n1}}}\\\\"
            f"&= {round(self.N * (self.N - 1) / self.sum_n_n1, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots()
        ax.set_axis_off()

        table_data = [[species, number] for species, number in zip(self.species, self.num_individuals)]

        table = ax.table(cellText=table_data, colLabels=['Species', 'Num of Individuals'], bbox=[0.1, 0.1, 0.8, 0.8], colWidths=[0.6, 0.4], cellLoc='left')

        table.auto_set_font_size(False)
        table.set_fontsize(8)

        for cell in table.get_celld().values():
            cell.PAD = 0.03

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio009:

    def __init__(self):
        self.start_A = rnd.randint(8, 14)
        self.start_B = rnd.randint(18, 24)
        self.max_intensity = rnd.choice([46, 48])
        self.half_max = self.max_intensity / 2
        self.C_A_half_max = self.start_A + 6
        self.C_B_half_max = self.start_B + 5

        self.RNA_A = 1 / self.C_A_half_max
        self.RNA_B = 1 / self.C_B_half_max
        self.ratio = self.RNA_A / self.RNA_B
        self.answer = round(self.ratio, 2)

        self.description = f"A quantitative comparison can be made of the amount of RNA in samples A and B. This involves determining the number of cycles required to reach 50% maximum concentration of DNA (C). If the amount of RNA in a sample can be measured as: 1/C, calculate how many times more RNA is present in sample A than in sample B."
        self.topic = "Genetic technology"
        self.subtopic = "Principles of genetic technology"
        self.source = "AQA"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Maximum concentration}} &= {self.max_intensity}\\\\"
            f"\\text{{50\\% of maximum concentration}} &= \\frac{{{self.max_intensity}}}{{2}} = {self.half_max}\\\\"
            f"\\text{{Cycles to reach half-max for A (C}}_A\\text{{)}} &= {self.C_A_half_max}\\\\"
            f"\\text{{Cycles to reach half-max for B (C}}_B\\text{{)}} &= {self.C_B_half_max}\\\\"
            f"\\text{{RNA concentration is defined as }} \\frac{{1}}{{C}} &\\\\"
            f"\\text{{RNA}}_A &= \\frac{{1}}{{{self.C_A_half_max}}} = {round(self.RNA_A, 10)}\\\\"
            f"\\text{{RNA}}_B &= \\frac{{1}}{{{self.C_B_half_max}}} = {round(self.RNA_B, 10)}\\\\"
            f"\\text{{Ratio}} &= \\frac{{\\text{{RNA}}_A}}{{\\text{{RNA}}_B}}\\\\"
            f"&= \\frac{{{round(self.RNA_A, 10)}}}{{{round(self.RNA_B, 10)}}}\\\\"
            f"&= {round(self.ratio, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        L = self.max_intensity / 100 
        x = np.linspace(0, 45, 500)

        y_A = sigmoid(x, self.C_A_half_max, L)
        y_B = sigmoid(x, self.C_B_half_max, L)

        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(x, y_A, color='black', linestyle='-', linewidth=1.5, zorder=2)
        ax.plot(x, y_B, color='black', linestyle='--', linewidth=1.5, zorder=2)

        for spine in ax.spines.values():
            spine.set_linewidth(2) 
            spine.set_color('black')

        ax.set_xlim(0, 45)
        ax.set_ylim(0, 0.50)
        ax.set_xlabel('Number of cycles')
        ax.set_ylabel('Intensity of\nfluorescence', rotation=0, labelpad=35)

        ax.set_xticks(np.arange(0, 46, 5))
        ax.set_yticks(np.arange(0, 0.51, 0.05))
        ax.minorticks_on()

        ax.grid(which='major', color='#888888', linestyle='-', linewidth=0.5)
        ax.grid(which='minor', color='#cccccc', linestyle='-', linewidth=0.3)

        ax.text(self.C_A_half_max + 5, L - 0.03, 'A', fontweight='bold', fontsize=12)
        ax.text(self.C_B_half_max + 4, L - 0.07, 'B', fontweight='bold', fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio010:

    def __init__(self):
        self.distance = rnd.randint(6, 10)
        self.minute = rnd.randint(15, 20)
        self.diameter = round(rnd.uniform(1.0, 1.5), 1)
        self.radius = self.diameter / 2
        self.water_volume = np.pi * self.radius**2 * self.distance
        self.hour = self.minute / 60
        self.answer = round(self.water_volume / self.hour, 2)

        self.description = f"This is an illustration of a potometer. In one experiment, the air bubble moved {self.distance} mm in {self.minute} minutes. Calculate the rate of water uptake by the shoot in this experiment by mm³."
        self.topic = "Transport in plants"
        self.subtopic = "Transport mechanisms"
        self.source = "AQA"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance bubble moved}} &= {self.distance}\\,\\text{{mm}}\\\\"
            f"\\text{{Time taken}} &= {self.minute}\\,\\text{{min}}\\\\"
            f"\\text{{Capillary tube diameter}} &= {self.diameter}\\,\\text{{mm}}\\\\"
            f"\\text{{Capillary tube radius (r)}} &= \\frac{{d}}{{2}} = \\frac{{{self.diameter}}}{{2}} = {self.radius}\\,\\text{{mm}}\\\\"
            f"\\text{{Volume of water uptake (V)}} &= \\pi \\times r^2 \\times \\text{{distance}}\\\\"
            f"&= \\pi \\times ({self.radius})^2 \\times {self.distance}\\\\"
            f"&= {round(self.water_volume, 10)}\\,\\text{{mm}}^3\\\\"
            f"\\text{{Time in hours (t)}} &= \\frac{{\\text{{minutes}}}}{{60}}\\\\"
            f"&= \\frac{{{self.minute}}}{{60}} = {round(self.hour, 10)}\\,\\text{{h}}\\\\"
            f"\\text{{Rate of water uptake}} &= \\frac{{V}}{{t}}\\\\"
            f"&= \\frac{{{round(self.water_volume, 10)}}}{{{round(self.hour, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{mm}}^3/\\text{{h}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio010temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(730, 400, f"{self.distance} mm", fontsize=7)
        ax.text(900, 812, f"{self.diameter} mm", fontsize=6)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio011:

    def __init__(self):
        self.body_masses = [rnd.randrange(10, 20), rnd.randrange(180, 210, 10), rnd.randrange(300, 330, 10), rnd.randrange(460, 490, 10)]
        self.low_temp = rnd.randint(10, 13) 
        self.mid_temp = self.low_temp + 5
        self.high_temp = self.low_temp + 10
        self.temps = [self.high_temp, self.mid_temp, self.low_temp]

        base_high = rnd.randrange(300, 340, 10)
        base_mid = rnd.randrange(230, 270, 10)
        base_low = rnd.randrange(160, 200, 10)
        slope = rnd.uniform(-0.25, -0.2)

        self.y_high = [int(round(slope * x + base_high, -1)) for x in self.body_masses]
        self.y_mid = [int(round(slope * x + base_mid, -1)) for x in self.body_masses]
        self.y_low = [int(round(slope * x + base_low, -1)) for x in self.body_masses]

        self.rate_high = self.y_high[3]
        self.rate_low = self.y_low[3]
        self.answer = round(self.rate_high / self.rate_low, 2)

        self.description = f"The scientists studied the effect of living at different temperatures on respiration in young fish at different stages of growth. Their results are shown below. Calculate the Q₁₀ for respiration in the largest fish."
        self.topic = "Energy and respiration"
        self.subtopic = "Respiration"
        self.source = "OCR"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify mass of the largest fish:}} &\\\\"
            f"m &= {self.body_masses[3]}\\,\\text{{g}}\\\\"
            f"\\text{{Identify respiration rates for largest fish at }} T_1 = {self.low_temp}^\circ\\text{{C and }} T_2 = {self.high_temp}^\circ\\text{{C:}} &\\\\"
            f"R_{{low}} &= {self.rate_low}\\,\\text{{mgO}}_2\\text{{kg}}^{{-1}}\\text{{h}}^{{-1}}\\\\"
            f"R_{{high}} &= {self.rate_high}\\,\\text{{mgO}}_2\\text{{kg}}^{{-1}}\\text{{h}}^{{-1}}\\\\"
            f"\\text{{The formula for }} Q_{{10}} \\text{{ is:}} &\\\\"
            f"Q_{{10}} &= \\left( \\frac{{R_2}}{{R_1}} \\right)^{{\\frac{{10}}{{T_2 - T_1}}}}\\\\"
            f"\\text{{Since }} T_2 - T_1 = {self.high_temp} - {self.low_temp} = 10^\circ\\text{{C, the equation becomes:}} &\\\\"
            f"Q_{{10}} &= \\frac{{R_{{high}}}}{{R_{{low}}}}\\\\"
            f"&= \\frac{{{self.rate_high}}}{{{self.rate_low}}}\\\\"
            f"&= {round(self.rate_high / self.rate_low, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        ax.plot(self.body_masses, self.y_high, label=f"{self.high_temp}°C", marker='^', color='black', linestyle='-')
        ax.plot(self.body_masses, self.y_mid, label=f"{self.mid_temp}°C", marker='s', color='black', linestyle='--')
        ax.plot(self.body_masses, self.y_low, label=f"{self.low_temp}°C", marker='o', color='black', linestyle=':')

        ax.set_xlabel('Body mass (g)')
        ax.set_ylabel('Rate of oxygen consumption\n(mgO₂kg⁻¹h⁻¹)')
        
        ax.set_xlim(0, 600)
        ax.set_ylim(0, 400)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(20))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
        ax.grid(which='major', linestyle='-', linewidth=0.8, color='gray')
        ax.grid(which='minor', linestyle='-', linewidth=0.3, color='gray')
        
        ax.legend(title="Key:", loc='upper right')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio012:
    
    def __init__(self):
        self.M1 = rnd.randint(120, 180)
        self.n1 = rnd.randint(80, 100)
        self.m1 = rnd.randint(45, 60)
        self.M2 = rnd.randint(60, 80)
        self.n2 = rnd.randint(40, 60)
        self.N = round(self.M1 * self.n1 / self.m1)
        self.answer = round(self.M2 * self.n2 / self.N)

        self.description = f"To determine the reliability of the capture-recapture technique and the Lincoln Index, two researchers collected data on a mouse population from the same site at the same time. If the reliability of the technique is high, how many marked mice would be expected in the second capture for researcher II?"
        self.topic = "Classification, biodiversity and conservation"
        self.subtopic = "Biodiversity"
        self.source = "QCAA"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Researcher I:}} &\\\\"
            f"\\text{{Number marked and released (}} M_1) &= {self.M1}\\\\"
            f"\\text{{Total in second capture (}} n_1) &= {self.n1}\\\\"
            f"\\text{{Number marked in second capture (}} m_1) &= {self.m1}\\\\"
            f"\\text{{Estimated population size (}} N) &= \\frac{{M_1 \\times n_1}}{{m_1}}\\\\"
            f"&= \\frac{{{self.M1} \\times {self.n1}}}{{{self.m1}}}\\\\"
            f"&= {round(self.M1 * self.n1 / self.m1, 10)}\\\\"
            f"&= {self.N}\\\\"
            f"\\text{{Researcher II:}} &\\\\"
            f"\\text{{Number marked and released (}} M_2) &= {self.M2}\\\\"
            f"\\text{{Total in second capture (}} n_2) &= {self.n2}\\\\"
            f"\\text{{If reliability is high, the expected number marked (}} m_2) \\text{{ is:}} &\\\\"
            f"m_2 &= \\frac{{M_2 \\times n_2}}{{N}}\\\\"
            f"&= \\frac{{{self.M2} \\times {self.n2}}}{{{self.N}}}\\\\"
            f"&= {round(self.M2 * self.n2 / self.N, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.set_axis_off()

        table_data = [["I", self.M1, self.n1, self.m1], ["II", self.M2, self.n2, "?"]]
        table_labels = ['Researcher', 'Num of Mice\nin First Capture', 'Num of Mice\nin Second Capture', 'Num of Marked Mice\nin Second Capture']

        table = ax.table(cellText=table_data, colLabels=table_labels, bbox=[0.05, 0.05, 0.90, 0.90], colWidths=[0.18, 0.27, 0.27, 0.28], loc='center', cellLoc='center')

        table.auto_set_font_size(False)
        table.set_fontsize(10)

        header_color = "#F9FFBC"
        for c in range(len(table_labels)):
            header = table[(0, c)]
            header.set_facecolor(header_color)
            header.get_text().set_color("black")
            header.get_text().set_weight("bold")

        for cell in table.get_celld().values():
            cell.PAD = 0.05

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio013:

    def __init__(self):
        self.year = 2019
        self.births = rnd.randint(300, 350)
        self.deaths = rnd.randint(200, 240)
        self.immigration = rnd.randint(120, 160)
        self.emmigration = rnd.randint(50, 70)
        self.final_population = rnd.randint(2400, 2800)
        self.prev_population = self.final_population - (self.births - self.deaths + self.immigration - self.emmigration)
        self.growth = (self.final_population - self.prev_population) / self.prev_population
        self.answer = round(self.growth * 100, 2)

        self.description = f"This chart provides information about a population of African buffalo in a national park. If the final population at the end of {self.year} was {self.final_population}, calculate the population growth rate for this population compared to the previous year."
        self.topic = "Organisms and their environment"
        self.subtopic = "Populations"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Final population (P}}_{{\\text{{final}}}}) &= {self.final_population}\\\\"
            f"\\text{{Births (B)}} &= {self.births}\\\\"
            f"\\text{{Deaths (D)}} &= {self.deaths}\\\\"
            f"\\text{{Immigration (I)}} &= {self.immigration}\\\\"
            f"\\text{{Emigration (E)}} &= {self.emmigration}\\\\"
            f"\\text{{Net population change (}}\\Delta P) &= (B - D) + (I - E)\\\\"
            f"&= ({self.births} - {self.deaths}) + ({self.immigration} - {self.emmigration})\\\\"
            f"&= {self.births - self.deaths} + {self.immigration - self.emmigration}\\\\"
            f"&= {self.births - self.deaths + self.immigration - self.emmigration}\\\\"
            f"\\text{{Previous population (P}}_{{\\text{{prev}}}}) &= P_{{\\text{{final}}}} - \\Delta P\\\\"
            f"&= {self.final_population} - {self.births - self.deaths + self.immigration - self.emmigration}\\\\"
            f"&= {self.prev_population}\\\\"
            f"\\text{{Growth rate}} &= \\frac{{P_{{\\text{{final}}}} - P_{{\\text{{prev}}}}}}{{P_{{\\text{{prev}}}}}} \\times 100\\\\"
            f"&= \\frac{{{self.final_population} - {self.prev_population}}}{{{self.prev_population}}} \\times 100\\\\"
            f"&= {round(self.growth, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))

        categories = ["Births", "Deaths", "Immigration", "Emigration"]
        values = [self.births, self.deaths, self.immigration, self.emmigration]
        colors = ["#f4a6b7", "#b0b0b0", "#9ecae1", "#c7a17a",]

        x = np.arange(len(categories))

        ax.bar(x, values, color=colors, edgecolor="black", linewidth=1.2, width=0.6, zorder=3)

        for i, value in enumerate(values):
            ax.text(i, value + 5, str(value), ha="center", va="bottom", fontsize=9)

        ax.set_ylabel("Number of individuals", fontsize=11)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=10)
        ax.set_title(f"Population changes in African buffalo during {self.year}", fontsize=12, pad=10)

        ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

        ax.grid(which="major", linestyle="-", linewidth=0.8, color="black", alpha=0.6, zorder=1)
        ax.grid(which="minor", linestyle="-", linewidth=0.4, color="black", alpha=0.4, zorder=1)

        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio014:
    
    def __init__(self):
        self.quadrat_1 = rnd.randint(2, 6)
        self.quadrat_2 = rnd.randint(2, 6)
        self.quadrat_3 = rnd.randint(2, 6)
        self.field_length = rnd.randint(80, 100)
        self.field_width = rnd.randint(50, 70)
        self.quadrat_length = rnd.randint(20, 25)
        self.quadrat_width = self.quadrat_length
        self.quadrat_area = self.quadrat_width * self.quadrat_length
        self.field_area = self.field_length * self.field_width
        self.quadrat_mean_org = (self.quadrat_1 + self.quadrat_2 + self.quadrat_3) / 3
        self.answer = int(round(self.quadrat_mean_org * self.field_area / self.quadrat_area))

        self.description = f"Some students are conducting a quadrat sampling experiment to estimate the number of flower A growing on a certain field. They placed 3 quadrats randomly on the field, and noted these observations. What is the estimated population size of flower A on that field?"
        self.topic = "Organisms and their environment"
        self.subtopic = "Populations"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Observations in quadrat 1}} &= {self.quadrat_1}\\\\"
            f"\\text{{Observations in quadrat 2}} &= {self.quadrat_2}\\\\"
            f"\\text{{Observations in quadrat 3}} &= {self.quadrat_3}\\\\"
            f"\\text{{Mean number of organisms per quadrat (}}\\bar{{n}}) &= \\frac{{{self.quadrat_1} + {self.quadrat_2} + {self.quadrat_3}}}{{3}}\\\\"
            f"&= {round(self.quadrat_mean_org, 10)}\\\\"
            f"\\text{{Quadrat area (a)}} &= \\text{{length}} \\times \\text{{width}}\\\\"
            f"&= {self.quadrat_length}\\,\\text{{cm}} \\times {self.quadrat_width}\\,\\text{{cm}}\\\\"
            f"&= {self.quadrat_area}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Field area (A)}} &= \\text{{length}} \\times \\text{{width}}\\\\"
            f"&= {self.field_length}\\,\\text{{cm}} \\times {self.field_width}\\,\\text{{m}}\\\\"
            f"&= {self.field_area}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Estimated population size (P)}} &= \\bar{{n}} \\times \\frac{{A}}{{a}}\\\\"
            f"&= {round(self.quadrat_mean_org, 10)} \\times \\frac{{{self.field_area}}}{{{self.quadrat_area}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio014temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(18, 545, f"{self.field_length} cm", fontsize=8)
        ax.text(405, 988, f"{self.field_width} cm", fontsize=8)
        ax.text(1520, 784, f"{self.quadrat_length} cm", fontsize=8)
        ax.text(1783, 558, f"{self.quadrat_width} cm", fontsize=8)
        plt.axis("off")

        quadrat1_box = (752, 1040, 393, 682)
        quadrat2_box = (1088, 1376, 393, 682)
        quadrat3_box = (1424, 1712, 393, 682)
        
        draw_non_overlapping_circles(ax, quadrat1_box, n_type1=self.quadrat_1, radius=12, facecolor1="#ff66b2")
        draw_non_overlapping_circles(ax, quadrat2_box, n_type1=self.quadrat_2, radius=12, facecolor1="#ff66b2")
        draw_non_overlapping_circles(ax, quadrat3_box, n_type1=self.quadrat_3, radius=12, facecolor1="#ff66b2")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio015:

    def __init__(self):
        self.stage_division_mm = 0.1
        self.stage_division_spanned = rnd.randint(8, 14)
        self.graticule_units_spanned = rnd.choice([40, 50, 60])
        self.mm_per_graticule = (self.stage_division_mm * self.stage_division_spanned) / self.graticule_units_spanned
        self.answer = round(self.mm_per_graticule * 1000, 2)

        self.description = f"A stage micrometer is used to calibrate an eyepiece graticule. The stage micrometer has 0.1 mm per division. Calculate the actual length represented by 1 graticule unit in µm."
        self.topic = "Cell structure"
        self.subtopic = "The microscope in cell studies"
        self.source = "Original"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length per stage micrometer division}} &= {self.stage_division_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Number of stage divisions spanned}} &= {self.stage_division_spanned}\\\\"
            f"\\text{{Number of eyepiece graticule units spanned}} &= {self.graticule_units_spanned}\\\\"
            f"\\text{{Total actual length spanned}} &= \\text{{divisions}} \\times \\text{{length per division}}\\\\"
            f"&= {self.stage_division_spanned} \\times {self.stage_division_mm}\\\\"
            f"&= {round(self.stage_division_spanned * self.stage_division_mm, 10)}\\,\\text{{mm}}\\\\"
            f"\\text{{Actual length per graticule unit (mm)}} &= \\frac{{\\text{{Total actual length}}}}{{\\text{{Graticule units}}}}\\\\"
            f"&= \\frac{{{round(self.stage_division_spanned * self.stage_division_mm, 10)}}}{{{self.graticule_units_spanned}}}\\\\"
            f"&= {round(self.mm_per_graticule, 10)}\\,\\text{{mm}}\\\\"
            f"\\text{{Convert to }} \\mu\\text{{m:}} &\\\\"
            f"\\text{{Length in }} \\mu\\text{{m}} &= \\text{{Length in mm}} \\times 1000\\\\"
            f"&= {round(self.mm_per_graticule, 10)} \\times 1000\\\\"
            f"&= {self.answer}\\,\\mu\\text{{m}}"
            "\\end{aligned}\\]"
        )
    
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(9, 3.8))
        ax.axis("off")
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 4)

        stage_x0, stage_x1 = 1.0, 15.0
        stage_y = 2.8

        n_divs_drawn = self.stage_division_spanned + 5
        stage_ticks = draw_stage(ax, stage_x0, stage_x1, stage_y, n_divs_drawn=n_divs_drawn)

        xA = stage_ticks[0]
        xB = stage_ticks[self.stage_division_spanned]

        grat_y = 1.6
        units_total = 100
        U = self.graticule_units_spanned

        unit_dx = (xB - xA) / U
        grat_x0 = xA
        grat_x1 = grat_x0 + unit_dx * units_total

        stage_dx = stage_ticks[1] - stage_ticks[0]
        stage_end = max(stage_x1, grat_x1)

        ax.plot([stage_x1, stage_end], [stage_y, stage_y], color="black", lw=4)

        tick_h = 0.36
        x = stage_ticks[-1]
        while x + stage_dx <= stage_end + 1e-9:
            x += stage_dx
            ax.plot([x, x], [stage_y - tick_h, stage_y + tick_h], color="black", lw=4)

        pad = 0.6
        ax.set_xlim(min(stage_x0, grat_x0) - pad, max(stage_x1, grat_x1) + pad)

        draw_graticule(ax, grat_x0, grat_x1, grat_y, units_total=units_total, major_every=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio016:
    
    def __init__(self):
        self.dominant_shape_pheno = "Smooth"
        self.recessive_shape_pheno = "Wrinkled"
        self.dominant_color_pheno = "Yellow"
        self.recessive_color_pheno = "Green"

        self.dominant_shape_gamet = "R"
        self.recessive_shape_gamet = "r"
        self.dominant_color_gamet = "Y"
        self.recessive_color_gamet = "y"
        self.punnett_square = [
            "RRYY","RRYy","RrYY","RrYy",
            "RRYy","RRyy","RrYy","Rryy",
            "RrYY","RrYy","rrYY","rrYy",
            "RrYy","Rryy","rrYy","rryy"
        ]
        self.smooth_yellow_count = sum(("R" in g[:2]) and ("Y" in g[2:]) for g in self.punnett_square)
        self.smooth_green_count = sum(("R" in g[:2]) and ("Y" not in g[2:]) for g in self.punnett_square)
        self.wrinkled_yellow_count = sum(("R" not in g[:2]) and ("Y" in g[2:]) for g in self.punnett_square)
        self.wrinkled_green_count = sum(("R" not in g[:2]) and ("Y" not in g[2:]) for g in self.punnett_square)
        self.total_count = self.smooth_yellow_count + self.smooth_green_count + self.wrinkled_yellow_count + self.wrinkled_green_count

        self.true_smooth_yellow_frequency = rnd.randint(500, 700)
        self.true_smooth_green_frequency = rnd.randint(200, 300)
        self.true_wrinkled_yellow_frequency = rnd.randint(200, 300)
        self.true_wrinkled_green_frequency = rnd.randint(60, 100)
        self.total_frequency = self.true_smooth_yellow_frequency + self.true_smooth_green_frequency + self.true_wrinkled_yellow_frequency + self.true_wrinkled_green_frequency
        self.observed = [self.true_smooth_yellow_frequency, self.true_smooth_green_frequency, self.true_wrinkled_yellow_frequency, self.true_wrinkled_green_frequency]

        self.expected_smooth_yellow_frequency = (self.smooth_yellow_count / self.total_count) * self.total_frequency
        self.expected_smooth_green_frequency = (self.smooth_green_count / self.total_count) * self.total_frequency
        self.expected_wrinkled_yellow_frequency = (self.wrinkled_yellow_count / self.total_count) * self.total_frequency
        self.expected_wrinkled_green_frequency = (self.wrinkled_green_count / self.total_count) * self.total_frequency
        self.expected = [self.expected_smooth_yellow_frequency, self.expected_smooth_green_frequency, self.expected_wrinkled_yellow_frequency, self.expected_wrinkled_green_frequency]

        self.chi_terms = [((o - e) ** 2) / e for o, e in zip(self.observed, self.expected)]
        self.answer = round(sum(self.chi_terms), 2)

        self.description = f"The trait for smooth peas ({self.dominant_shape_gamet}) is dominant over wrinkled peas ({self.recessive_shape_gamet}) and yellow pea colour ({self.dominant_color_gamet}) is dominant to green ({self.recessive_color_gamet}). A dihybrid cross between two heterozygous pea plants is performed, resulting in this Punnett Square. Then, the following phenotypic frequencies are observed. Calculate the value of chi-square (χ²) for this generation."
        self.topic = "Inheritance"
        self.subtopic = "The roles of genes in determining the phenotype"
        self.source = "My Science Squad"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total observed individuals (n)}} &= {self.total_frequency}\\\\"
            f"\\text{{Dihybrid cross ratio}} &= 9:3:3:1\\\\"
            f"\\text{{Total Punnett square boxes}} &= {self.total_count}\\\\"
            f"\\text{{Expected frequency (E) calculation:}} &\\\\"
            f"E_{{{self.dominant_shape_pheno}\\ {self.dominant_color_pheno}}} &= \\frac{{{self.smooth_yellow_count}}}{{{self.total_count}}} \\times {self.total_frequency} = {round(self.expected_smooth_yellow_frequency, 10)}\\\\"
            f"E_{{{self.dominant_shape_pheno}\\ {self.recessive_color_pheno}}} &= \\frac{{{self.smooth_green_count}}}{{{self.total_count}}} \\times {self.total_frequency} = {round(self.expected_smooth_green_frequency, 10)}\\\\"
            f"E_{{{self.recessive_shape_pheno}\\ {self.dominant_color_pheno}}} &= \\frac{{{self.wrinkled_yellow_count}}}{{{self.total_count}}} \\times {self.total_frequency} = {round(self.expected_wrinkled_yellow_frequency, 10)}\\\\"
            f"E_{{{self.recessive_shape_pheno}\\ {self.recessive_color_pheno}}} &= \\frac{{{self.wrinkled_green_count}}}{{{self.total_count}}} \\times {self.total_frequency} = {round(self.expected_wrinkled_green_frequency, 10)}\\\\"
            f"\\text{{Chi-square formula:}} &\\\\"
            f"\\chi^2 &= \\sum \\frac{{(O - E)^2}}{{E}}\\\\"
            f"\\text{{Calculation of terms:}} &\\\\"
            f"\\text{{Term 1}} &= \\frac{{({self.true_smooth_yellow_frequency} - {round(self.expected_smooth_yellow_frequency, 10)})^2}}{{{round(self.expected_smooth_yellow_frequency, 10)}}} = {round(self.chi_terms[0], 10)}\\\\"
            f"\\text{{Term 2}} &= \\frac{{({self.true_smooth_green_frequency} - {round(self.expected_smooth_green_frequency, 10)})^2}}{{{round(self.expected_smooth_green_frequency, 10)}}} = {round(self.chi_terms[1], 10)}\\\\"
            f"\\text{{Term 3}} &= \\frac{{({self.true_wrinkled_yellow_frequency} - {round(self.expected_wrinkled_yellow_frequency, 10)})^2}}{{{round(self.expected_wrinkled_yellow_frequency, 10)}}} = {round(self.chi_terms[2], 10)}\\\\"
            f"\\text{{Term 4}} &= \\frac{{({self.true_wrinkled_green_frequency} - {round(self.expected_wrinkled_green_frequency, 10)})^2}}{{{round(self.expected_wrinkled_green_frequency, 10)}}} = {round(self.chi_terms[3], 10)}\\\\"
            f"\\chi^2 &= {round(self.chi_terms[0], 10)} + {round(self.chi_terms[1], 10)} + {round(self.chi_terms[2], 10)} + {round(self.chi_terms[3], 10)}\\\\"
            f"\\chi^2 &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio016temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(578, 449, f"{self.true_smooth_yellow_frequency}", fontsize=7)
        ax.text(578, 559, f"{self.true_smooth_green_frequency}", fontsize=7)
        ax.text(578, 669, f"{self.true_wrinkled_yellow_frequency}", fontsize=7)
        ax.text(581, 778, f"{self.true_wrinkled_green_frequency}", fontsize=7)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio017:

    def __init__(self):
        self.dominant_ladybug = "Red"
        self.recessive_ladybug = "Orange"
        self.total_ladybug = 25
        self.orange_ladybug = rnd.randint(4, 10)
        self.red_ladybug = self.total_ladybug - self.orange_ladybug

        self.q2 = self.orange_ladybug / self.total_ladybug
        self.q = np.sqrt(self.q2)
        self.p = 1 - self.q
        self.heterozygous = 2 * self.p * self.q
        self.answer = round(self.heterozygous * 100, 2)

        self.description = f"The image below shows {self.total_ladybug} ladybugs collected from a population. The ladybugs appear either red (dominant trait, R) or orange (recessive trait, r). Based on the image, calculate the percentage of ladybugs that are heterozygous (Rr). Assume the population is in Hardy-Weinberg equilibrium."
        self.topic = "Selection and evolution"
        self.subtopic = "Natural and artificial selection"
        self.source = "Original"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total population size (n)}} &= {self.total_ladybug}\\\\"
            f"\\text{{Number of orange ladybugs (recessive phenotype)}} &= {self.orange_ladybug}\\\\"
            f"\\text{{Hardy-Weinberg equilibrium is defined as:}} &\\\\"
            f"p^2 + 2pq + q^2 &= 1 \\quad \\text{{and}} \\quad p + q = 1\\\\"
            f"\\text{{Frequency of homozygous recessive phenotype (}} q^2 \\text{{)}} &= \\frac{{\\text{{Number of recessive individuals}}}}{{\\text{{Total population}}}}\\\\"
            f"q^2 &= \\frac{{{self.orange_ladybug}}}{{{self.total_ladybug}}}\\\\"
            f"q^2 &= {round(self.q2, 10)}\\\\"
            f"\\text{{Frequency of recessive allele (q)}} &= \\sqrt{{q^2}}\\\\"
            f"q &= \\sqrt{{{round(self.q2, 10)}}}\\\\"
            f"q &= {round(self.q, 10)}\\\\"
            f"\\text{{Frequency of dominant allele (p)}} &= 1 - q\\\\"
            f"p &= 1 - {round(self.q, 10)}\\\\"
            f"p &= {round(self.p, 10)}\\\\"
            f"\\text{{Frequency of heterozygous genotype (2pq)}} &= 2 \\times p \\times q\\\\"
            f"2pq &= 2 \\times {round(self.p, 10)} \\times {round(self.q, 10)}\\\\"
            f"2pq &= {round(self.heterozygous, 10)}\\\\"
            f"\\text{{Percentage of heterozygous individuals}} &= 2pq \\times 100\\\\"
            f"&= {round(self.heterozygous, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio017temp.png').convert('RGBA')
        
        y_min, y_max = 288, 783
        red_bbox = (517, y_min,  930, y_max)
        orange_bbox = (987, y_min, 1404, y_max)

        red_sprite = img.crop(red_bbox)
        orange_sprite = img.crop(orange_bbox)

        total = 25
        labels = (["orange"] * self.orange_ladybug) + (["red"] * (total - self.orange_ladybug))
        rnd.shuffle(labels)

        rows, cols = 5, 5
        cell_w, cell_h = 220, 220
        red_sprite_fit = red_sprite.resize((cell_w, cell_h))
        orange_sprite_fit = orange_sprite.resize((cell_w, cell_h))

        canvas_w, canvas_h = cols * cell_w, rows * cell_h
        canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))

        i = 0
        for r in range(rows):
            for c in range(cols):
                x0 = c * cell_w
                y0 = r * cell_h

                if labels[i] == "orange":
                    canvas.paste(orange_sprite_fit, (x0, y0), orange_sprite_fit)
                else:
                    canvas.paste(red_sprite_fit, (x0, y0), red_sprite_fit)

                i += 1

        rgba = np.array(canvas)
        plt.figure(figsize=(canvas_w / 100, canvas_h / 100), dpi=100)
        plt.imshow(rgba)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0)
        plt.close()

class Bio018:

    def __init__(self):
        self.plants = 16
        self.wo_thio = [round(rnd.uniform(0.85, 1.40), 2) for _ in range(self.plants)]
        self.w_thio = [round(rnd.uniform(0.85, 1.40), 2) for _ in range(self.plants)]
        self.diff = [b - a for a, b in zip(self.wo_thio, self.w_thio)]
        self.diff_square = [x**2 for x in self.diff]
        self.diff_sum = sum(self.diff)
        self.diff_mean = self.diff_sum / self.plants
        self.sd = np.sqrt(sum((x - self.diff_mean)**2 for x in self.diff) / (self.plants - 1))
        self.se = self.sd / np.sqrt(self.plants)
        self.answer = round(self.diff_mean / self.se, 2)

        self.description = f"The plant known as Indian Mustard (Brassica juncea) will accumulate gold from gold salts in the soil in which it grows. It can be used to extract gold from impoverished mine wastes which still contain residual gold which is uneconomical to extract by traditional methods. Addition of ammonium thiocyanate to the mine waste growth substrate is thought to enhance the accumulation of gold by the plants. An investigation was carried out to test whether this was so. The results of the investigation (gold accumulated / mg gold kg⁻¹ dry mass) are shown in the table below. Calculate the value of t."
        self.topic = "Selection and evolution"
        self.subtopic = "Variation"
        self.source = "PhysicsandMathsTutor"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Number of pairs (n)}} &= {self.plants}\\\\"
            f"\\text{{Sum of differences (}}\\sum d) &= {round(self.diff_sum, 10)}\\\\"
            f"\\text{{Mean of differences (}}\\bar{{d}}) &= \\frac{{\\sum d}}{{n}}\\\\"
            f"&= \\frac{{{round(self.diff_sum, 10)}}}{{{self.plants}}}\\\\"
            f"&= {round(self.diff_mean, 10)}\\\\"
            f"\\text{{Standard deviation of differences}} (s_d) &= \\sqrt{{\\frac{{\\sum (d - \\bar{{d}})^2}}{{n - 1}}}}\\\\"
            f"&= {round(self.sd, 10)}\\\\"
            f"\\text{{Standard error of the mean difference (SE)}} &= \\frac{{s_d}}{{\\sqrt{{n}}}}\\\\"
            f"&= \\frac{{{round(self.sd, 10)}}}{{\\sqrt{{{self.plants}}}}}\\\\"
            f"&= {round(self.se, 10)}\\\\"
            f"\\text{{t-value calculation:}} &\\\\"
            f"t &= \\frac{{\\bar{{d}}}}{{SE}}\\\\"
            f"&= \\frac{{{round(self.diff_mean, 10)}}}{{{round(self.se, 10)}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 10))
        ax.set_axis_off()

        table_data = []
        for i in range(self.plants):
            table_data.append([i + 1, f"{self.wo_thio[i]:.2f}", f"{self.w_thio[i]:.2f}"])
        table_labels = ['Plant', 'No thiocyanate', 'With thiocyanate']

        table = ax.table(cellText=table_data, colLabels=table_labels, bbox=[0.02, 0.02, 0.96, 0.90], colWidths=[0.2, 0.4, 0.4], loc='center', cellLoc='center')

        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.15, 1.55)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio019:

    def __init__(self):
        self.solvent_front_cm = rnd.randint(15, 18)
        self.pigments = ["A", "B", "C", "D"]
        self.pigments_mm = [rnd.randint(120, 140), rnd.randint(90, 110), rnd.randint(60, 80), rnd.randint(20, 40)]
        self.pigment = rnd.choice(self.pigments)
        idx = self.pigments.index(self.pigment)
        self.pigment_cm = self.pigments_mm[idx] / 10
        self.answer = round(self.pigment_cm / self.solvent_front_cm, 2)

        self.description = f"A chromatogram of plant pigments was produced using paper chromatography. Determine the Rf value of pigment {self.pigment}."
        self.topic = "Photosynthesis"
        self.subtopic = "Photosynthesis as an energy transfer process"
        self.source = "Original"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance traveled by solvent front}} &= {self.solvent_front_cm}\\,\\text{{cm}}\\\\"
            f"\\text{{Distance traveled by pigment }} {self.pigment} &= {self.pigments_mm[self.pigments.index(self.pigment)]}\\,\\text{{mm}}\\\\"
            f"\\text{{Convert pigment distance to cm:}} &\\\\"
            f"D_{{{self.pigment}}} &= \\frac{{{self.pigments_mm[self.pigments.index(self.pigment)]}}}{{10}}\\\\"
            f"&= {self.pigment_cm}\\,\\text{{cm}}\\\\"
            f"\\text{{The }} R_f \\text{{ value is given by:}} &\\\\"
            f"R_f &= \\frac{{\\text{{Distance traveled by pigment}}}}{{\\text{{Distance traveled by solvent front}}}}\\\\"
            f"&= \\frac{{{self.pigment_cm}}}{{{self.solvent_front_cm}}}\\\\"
            f"&= {round(self.pigment_cm / self.solvent_front_cm, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio019temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(540, 503, f"{self.solvent_front_cm} cm", fontsize=6)
        ax.text(1329, 407, f"{self.pigments_mm[0]} mm", fontsize=6)
        ax.text(1329, 489, f"{self.pigments_mm[1]} mm", fontsize=6)
        ax.text(1329, 570, f"{self.pigments_mm[2]} mm", fontsize=6)
        ax.text(1329, 638, f"{self.pigments_mm[3]} mm", fontsize=6)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio020:

    def __init__(self):
        self.max_rate_L = round(rnd.uniform(1.0, 1.4), 1)
        self.max_rate_C = round(rnd.uniform(0.7, 0.8), 1)
        self.rate_C_2_5 = round(rnd.uniform(0.3, 0.5), 2)
        self.answer = round(self.rate_C_2_5 / self.max_rate_L * 100, 2)

        self.description = f"Another scientist investigated an enzyme that catalyses the following reaction: ATP → ADP + Pi. The scientists set up two experiments, C and L. Experiment C used the enzyme and different concentrations of ATP. Experiment L used the enzyme, different concentrations of ATP, and a sugar called lyxose. The scientists measured the rate of reaction in each experiment. Their results are shown in the graph. Calculate the rate of reaction of the enzyme activity with no lyxose at 2.5mmol dm⁻3 of ATP as a percentage of the maximum rate shown with lyxose."
        self.topic = "Enzymes"
        self.subtopic = "Mode of action of enzymes"
        self.source = "PhysicsandMathsTutor"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Maximum reaction rate with lyxose (Experiment L)}} &= {self.max_rate_L}\\,\\text{{units}}\\\\"
            f"\\text{{Reaction rate without lyxose (Experiment C) at 2.5 mmol dm}}^{{-3}} &= {self.rate_C_2_5}\\,\\text{{units}}\\\\"
            f"\\text{{Percentage calculation:}} &\\\\"
            f"\\text{{Percentage}} &= \\left( \\frac{{\\text{{Rate at 2.5 mmol dm}}^{{-3}}\\text{{ (C)}}}}{{\\text{{Max rate (L)}}}} \\right) \\times 100\\\\"
            f"&= \\left( \\frac{{{self.rate_C_2_5}}}{{{self.max_rate_L}}} \\right) \\times 100\\\\"
            f"&= {round(self.rate_C_2_5 / self.max_rate_L, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        x = np.linspace(0, 10, 500)

        xL = np.array([0, 0.2, 0.5, 1.0, 2.5, 10.0])
        yL = np.array([0.0, 0.75 * self.max_rate_L, 0.88 * self.max_rate_L, 0.93 * self.max_rate_L, 0.96 * self.max_rate_L, self.max_rate_L])

        xC = np.array([0, 0.5, 1.0, 2.5, 5.0, 10.0])
        yC1 = 0.55 * self.rate_C_2_5 
        yC0 = 0.25 * self.rate_C_2_5
        yC5 = self.rate_C_2_5 + 0.55 * (self.max_rate_C - self.rate_C_2_5)
        yC = np.array([0.0, yC0, yC1, self.rate_C_2_5, yC5, self.max_rate_C])

        y_L = make_curve_pchip(xL, yL, x)
        y_C = make_curve_pchip(xC, yC, x)

        ax.plot(x, y_L, label="L", linewidth=1.2)
        ax.plot(x, y_C, label="C", linewidth=1.2)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 1.6)

        ax.set_xlabel("Concentration of ATP / mmol dm⁻³")
        ax.set_ylabel("Rate of reaction / units of Pi min⁻¹")

        ax.xaxis.set_major_locator(ticker.MultipleLocator(2.5))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.02))

        ax.grid(which="major", linewidth=0.8, color='black', alpha=0.6)
        ax.grid(which="minor", linewidth=0.4, color='black', alpha=0.35)
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio021:

    def __init__(self):
        self.bases = 22
        self.nucleotides = self.bases * 2
        self.A = rnd.randint(8, 12)
        self.T = self.A
        self.remaining = self.nucleotides - self.A - self.T
        self.C = self.remaining // 2
        self.G = self.C
        self.C_ratio = self.C / self.nucleotides
        self.answer = round(self.C_ratio * 100, 2)

        self.description = f"The diagram represents the entire length of a double-stranded DNA molecule, showing the positions of adenine (A) nucleotides. Calculate the percentage of cytosine nucleotides present."
        self.topic = "Nucleic acids and protein synthesis"
        self.subtopic = "Structure of nucleic acids and replication of DNA"
        self.source = "Original"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Number of base pairs}} &= {self.bases}\\\\"
            f"\\text{{Total nucleotides}} &= \\text{{Base pairs}} \\times 2\\\\"
            f"&= {self.bases} \\times 2 = {self.nucleotides}\\\\"
            f"\\text{{Number of Adenine (A) nucleotides}} &= {self.A}\\\\"
            f"\\text{{Since A pairs with T, Thymine (T)}} &= {self.T}\\\\"
            f"\\text{{Remaining nucleotides (C + G)}} &= \\text{{Total}} - (A + T)\\\\"
            f"&= {self.nucleotides} - ({self.A} + {self.T}) = {self.remaining}\\\\"
            f"\\text{{Since C pairs with G, Cytosine (C)}} &= \\frac{{\\text{{Remaining}}}}{{2}}\\\\"
            f"&= \\frac{{{self.remaining}}}{{2}} = {self.C}\\\\"
            f"\\text{{Percentage of Cytosine}} &= \\left( \\frac{{C}}{{\\text{{Total nucleotides}}}} \\right) \\times 100\\\\"
            f"&= \\left( \\frac{{{self.C}}}{{{self.nucleotides}}} \\right) \\times 100\\\\"
            f"&= {round(self.C_ratio, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio021temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.axis("off")

        n_boxes = 22
        x_start = 126
        x_gap = 80
        y_top = 462
        y_bottom = 606

        x_centers = [x_start + i * x_gap for i in range(n_boxes)]

        indices = rnd.sample(range(n_boxes), self.A)

        for i in indices:
            row = rnd.choice(["top", "bottom"])
            if row == "top":
                y = y_top
            else:
                y = y_bottom

            ax.text(x_centers[i], y, "A", ha="center", va="center", fontsize=6, fontweight="bold", color="black")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio022:

    def __init__(self):
        self.dominant_eye_pheno = "Brown"
        self.recessive_eye_pheno = "Blue"
        self.dominant_hair_pheno = "Curly"
        self.recessive_hair_pheno = "Straight"
        self.dom_eye_allele= "B"
        self.rec_eye_allele = "b"
        self.dom_hair_allele= "C"
        self.rec_hair_allele = "c"
        self.parent1 = dihybrid_generate_genotype(self.dom_eye_allele, self.rec_eye_allele, self.dom_hair_allele, self.rec_hair_allele)
        self.parent2 = dihybrid_generate_genotype(self.dom_eye_allele, self.rec_eye_allele, self.dom_hair_allele, self.rec_hair_allele)
        self.sample_size = rnd.choice([40, 60, 100, 120, 400, 1000])

        self.p1_gametes = get_dihybrid_gametes(self.parent1)
        self.p2_gametes = get_dihybrid_gametes(self.parent2)

        offspring = []
        for g1 in self.p1_gametes:
            for g2 in self.p2_gametes:
                eye_alleles = sorted([g1[0], g2[0]], key=lambda a: (a.islower(), a))
                hair_alleles = sorted([g1[1], g2[1]], key=lambda a: (a.islower(), a))
                child_genotype = "".join(eye_alleles) + "".join(hair_alleles)
                offspring.append(child_genotype)

        self.offspring = offspring
        self.curly_count = 0
        for child in self.offspring:
            if self.dom_hair_allele in child[2:]:
                self.curly_count += 1

        self.curly_frac = self.curly_count / len(self.offspring)
        self.answer = int(round(self.curly_frac * self.sample_size))

        self.description = f"Brown eyes (B) are dominant over blue eyes (b). Curly hair (C) is dominant over straight hair (c). Based on a cross between a father and a mother with both having a certain genotype (provided in this Punnett Square), determine the number of individuals expected to have curly hair in a total sample of {self.sample_size}."
        self.topic = "Inheritance"
        self.subtopic = "The roles of genes indetermining the phenotype"
        self.source = "Original"
        self.curriculum = "A & AS Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Dominant hair allele}} &= {self.dom_hair_allele}\\,({self.dominant_hair_pheno})\\\\"
            f"\\text{{Recessive hair allele}} &= {self.rec_hair_allele}\\,({self.recessive_hair_pheno})\\\\"
            f"\\text{{Total boxes in Punnett Square}} &= {len(self.offspring)}\\\\"
            f"\\text{{Count of offspring with curly hair (}} {self.dom_hair_allele}\\text{{-)}} &= {self.curly_count}\\\\"
            f"\\text{{Probability of curly hair phenotype (P)}} &= \\frac{{\\text{{Curly count}}}}{{\\text{{Total boxes}}}}\\\\"
            f"P &= \\frac{{{self.curly_count}}}{{{len(self.offspring)}}}\\\\"
            f"&= {round(self.curly_frac, 10)}\\\\"
            f"\\text{{Total sample size (N)}} &= {self.sample_size}\\\\"
            f"\\text{{Expected number}} &= P \\times N\\\\"
            f"&= {round(self.curly_frac, 10)} \\times {self.sample_size}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.set_axis_off()

        table_data = [[""] + self.p2_gametes]
        for g1 in self.p1_gametes:
            table_data.append([g1, "?", "?", "?", "?"])

        table = ax.table(cellText=table_data, loc="center", cellLoc="center", bbox=[0.1, 0.1, 0.8, 0.8])

        table.auto_set_font_size(False)
        table.set_fontsize(18)

        for (row, col), cell in table.get_celld().items():
            if row == 0 or col == 0:
                cell.set_facecolor("#efefef")
                cell.get_text().set_weight("bold")
            else:
                cell.get_text().set_color("#999999") 
            cell.set_linewidth(2)

        plt.text(0.5, 0.92, f"Parent 2: {self.parent2}", ha="center", fontsize=14, weight="bold")
        plt.text(0.02, 0.5, f"Parent 1: {self.parent1}", va="center", rotation=90, fontsize=14, weight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio023:

    def __init__(self):
        self.grid_length_mm = round(rnd.uniform(0.2, 0.5), 1)
        self.grid_width_mm = self.grid_length_mm
        self.depth_mm = 0.2
        self.stained_cells = rnd.randint(12, 25)
        self.unstained_cells = round(0.2 * self.stained_cells)
        self.volume_mm3 = round(self.grid_length_mm * self.grid_width_mm * self.depth_mm, 3)
        self.cells_per_mm3 = self.stained_cells / self.volume_mm3
        self.cells_per_cm3 = self.cells_per_mm3 * 1000
        self.answer = round(self.cells_per_cm3)

        self.description = f"A haemocytometer is used to estimate the population of live yeast in a sample of undiluted cider. The stain methylene blue is added to the sample. Only live yeast cells will take up this stain. This image shows the haemocytometer chamber containing the cider sample when viewed under a light microscope. The grid measures {self.grid_length_mm} mm x {self.grid_width_mm} mm and has a depth of {self.depth_mm} mm. Calculate the number of live yeast cells in 1 cm³ of the cider sample. Assume that there are no boundary rules, and round the answer to a whole number."
        self.topic = "Cell structure"
        self.subtopic = "The microscope in cell studies"
        self.source = "OCR H422/03 2016"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Grid Length}} &= {self.grid_length_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Grid Width}} &= {self.grid_width_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Chamber Depth}} &= {self.depth_mm}\\,\\text{{mm}}\\\\"
            f"\\text{{Count of Stained (Live) Cells}} &= {self.stained_cells}\\\\"
            f"\\text{{Volume of counted area (V)}} &= \\text{{length}} \\times \\text{{width}} \\times \\text{{depth}}\\\\"
            f"&= {self.grid_length_mm} \\times {self.grid_width_mm} \\times {self.depth_mm}\\\\"
            f"&= {round(self.volume_mm3, 10)}\\,\\text{{mm}}^3\\\\"
            f"\\text{{Cells per mm}}^3 &= \\frac{{\\text{{Number of stained cells}}}}{{V}}\\\\"
            f"&= \\frac{{{self.stained_cells}}}{{{round(self.volume_mm3, 10)}}}\\\\"
            f"&= {round(self.cells_per_mm3, 10)}\\,\\text{{cells/mm}}^3\\\\"
            f"\\text{{Convert to cells per cm}}^3\\text{{ (1 cm}}^3 = 1000\\,\\text{{mm}}^3\\text{{):}} &\\\\"
            f"\\text{{Cells per cm}}^3 &= \\text{{Cells per mm}}^3 \\times 1000\\\\"
            f"&= {round(self.cells_per_mm3, 10)} \\times 1000\\\\"
            f"&= {round(self.cells_per_cm3, 10)}\\\\"
            f"\\text{{Final Answer (rounded)}} &= {self.answer}\\,\\text{{cells/cm}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio023temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(1518, 536, f"{self.grid_length_mm} mm", fontsize=8)
        ax.text(928, 1005, f"{self.grid_width_mm} mm", fontsize=8)
        plt.axis("off")

        grid_box = (540, 1387, 155, 877)
        
        draw_non_overlapping_circles(ax, grid_box, self.stained_cells, self.unstained_cells, radius=14, facecolor1="#444bd9", facecolor2="#ffffff")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Bio024:

    def __init__(self):
        self.total_cells = 50
        self.interphase = rnd.randint(16, 18)
        self.prophase = rnd.randint(9, 11)
        self.metaphase = rnd.randint(7, 9)
        self.anaphase = rnd.randint(7, 9)
        self.telophase = self.total_cells - self.interphase - self.prophase - self.metaphase - self.anaphase
        self.mitosis_cells = self.prophase + self.metaphase + self.anaphase + self.telophase
        self.mitotic_index = self.mitosis_cells / self.total_cells
        self.answer = round(self.mitotic_index * 100, 2)

        self.description = f"This image shows {self.total_cells} cells in different stages of the cell cycle. From this image, calculate the mitotic index (as a percentage)."
        self.topic = "The mitotic cell cycle"
        self.subtopic = "Chromosome behaviour in mitosis"
        self.source = "Original"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Number of cells in Interphase}} &= {self.interphase}\\\\"
            f"\\text{{Number of cells in Prophase}} &= {self.prophase}\\\\"
            f"\\text{{Number of cells in Metaphase}} &= {self.metaphase}\\\\"
            f"\\text{{Number of cells in Anaphase}} &= {self.anaphase}\\\\"
            f"\\text{{Number of cells in Telophase}} &= {self.telophase}\\\\"
            f"\\text{{Total cells in Mitosis (}} n_m) &= \\text{{Prophase}} + \\text{{Metaphase}} + \\text{{Anaphase}} + \\text{{Telophase}}\\\\"
            f"n_m &= {self.prophase} + {self.metaphase} + {self.anaphase} + {self.telophase} = {self.mitosis_cells}\\\\"
            f"\\text{{Total cells observed (}} N) &= {self.total_cells}\\\\"
            f"\\text{{Mitotic Index (MI) is given by:}} &\\\\"
            f"\\text{{MI}} &= \\frac{{n_m}}{{N}} \\times 100\\\\"
            f"&= \\frac{{{self.mitosis_cells}}}{{{self.total_cells}}} \\times 100\\\\"
            f"&= {round(self.mitotic_index, 10)} \\times 100\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('biology/temp_image/Bio024temp.png').convert('RGBA')

        bboxes = {
            "interphase": (93,  350,  430,  731),
            "prophase":   (442, 350,  779,  731),
            "metaphase":  (791, 350, 1128,  731),
            "anaphase":   (1140,350, 1476,  731),
            "telophase":  (1488,350, 1825,  731),
        }

        rows, cols = 5, 10
        cell_w, cell_h = 500, 500

        sprites = {}
        for phase, bbox in bboxes.items():
            sprite = img.crop(bbox).resize((cell_w, cell_h))
            sprites[phase] = sprite

        labels = (
            ["interphase"] * self.interphase +
            ["prophase"]   * self.prophase +
            ["metaphase"]  * self.metaphase +
            ["anaphase"]   * self.anaphase +
            ["telophase"]  * self.telophase
        )
        rnd.shuffle(labels)

        canvas_w, canvas_h = cols * cell_w, rows * cell_h
        canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))

        i = 0
        for r in range(rows):
            for c in range(cols):
                x0 = c * cell_w
                y0 = r * cell_h
                phase = labels[i]
                sprite = sprites[phase]
                canvas.paste(sprite, (x0, y0), sprite)
                i += 1

        rgba = np.array(canvas)
        plt.figure(figsize=(canvas_w / 100, canvas_h / 100), dpi=100)
        plt.imshow(rgba)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()


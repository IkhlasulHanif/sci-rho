import numpy as np
import random as rnd
import math
import os
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles
from mathematics.helper import *

# target folder : "root/dataset/mathematics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "mathematics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Mat001:
    
    def __init__(self):
        total = rnd.randint(180, 220)
        self.coffee_only = rnd.randint(40, 90)
        self.tea_only = rnd.randint(40, 90)
        self.both_beverages = rnd.randint(0, abs(total - self.coffee_only - self.tea_only))
        remainder = total - (self.coffee_only + self.tea_only + self.both_beverages)
        self.neither = remainder
        self.total = total
        self.answer = self.coffee_only + self.tea_only

        self.description = (
            f"{self.total} people were surveyed about their beverage preferences. The results are displayed in the Venn diagram below. What is the sum of people who prefer only Coffee or only Tea?"
        )
        self.topic = "Number"
        self.subtopic = "Sets"
        self.source = "DynaMath"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total surveyed}} &= {self.total}\\\\"
            f"\\text{{Only Coffee}} &= {self.coffee_only}\\\\"
            f"\\text{{Only Tea}} &= {self.tea_only}\\\\"
            f"\\text{{Both beverages}} &= {self.both_beverages}\\\\"
            f"\\text{{Neither}} &= {self.neither}\\\\"
            f"\\text{{Sum of only Coffee and only Tea:}} &\\\\"
            f"S &= C + T\\\\"
            f"&= {self.coffee_only} + {self.tea_only}\\\\"
            f"&= {round(self.coffee_only + self.tea_only, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.coffee_only, self.tea_only, self.both_beverages), set_labels=('Coffee', 'Tea'))
        venn_circles = venn2_circles(subsets=(self.coffee_only, self.tea_only, self.both_beverages), linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, -0.6, f'Neither: {self.neither}', fontsize=20, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat002:
    
    def __init__(self):
        self.math = rnd.randint(50, 100)
        self.science = rnd.randint(50, 100)
        self.english = rnd.randint(50, 100)
        self.math_science = rnd.randint(20, 40)
        self.science_english = rnd.randint(20, 40)
        self.math_english = rnd.randint(20, 40)
        self.all_subjects = rnd.randint(0, 10)
        self.neither = rnd.randint(0, 10)
        self.total = self.math + self.science + self.english + self.math_science + self.science_english + self.math_english + self.all_subjects + self.neither
        
        self.answer = self.math + self.math_science + self.math_english + self.all_subjects

        self.description = (
            f"In a survey of {self.total} students, the following information was gathered regarding their preference for three subjects: Math, Science, and English. The results are shown in the Venn diagram below. How many students like Math?"
        )

        self.topic = "Number"
        self.subtopic = "Sets"
        self.source = "Original" # TODO: REMOVED
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{To find the total number of students who like Math, we sum the distinct regions}&\\\\"
            "\\text{within the Math circle of the Venn diagram:}&\\\\"
            f"\\text{{1. Students who like \\textbf{{only}} Math}} &= {self.math}\\\\"
            f"\\text{{2. Students who like Math and Science (but not English)}} &= {self.math_science}\\\\"
            f"\\text{{3. Students who like Math and English (but not Science)}} &= {self.math_english}\\\\"
            f"\\text{{4. Students who like all three subjects}} &= {self.all_subjects}\\\\"
            "\\text{Total Math} &= \\text{Only Math} + (\\text{Math} \\cap \\text{Science})_{\\text{only}} + (\\text{Math} \\cap \\text{English})_{\\text{only}} + \\text{All three}\\\\"
            f"&= {self.math} + {self.math_science} + {self.math_english} + {self.all_subjects}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 6))

        venn_data = {
            '100': self.math,               # Only Math
            '010': self.science,            # Only Science
            '001': self.english,            # Only English
            '110': self.math_science,       # Math and Science, not English
            '011': self.science_english,    # Science and English, not Math
            '101': self.math_english,       # Math and English, not Science
            '111': self.all_subjects,       # All three subjects
        }
        venn = venn3(subsets=venn_data, set_labels=('Math', 'Science', 'English'))
        venn_circles = venn3_circles(subsets=venn_data, linestyle='solid', linewidth=1.5, color='black')
        plt.title("Venn Diagram: Math, Science, and English")
        plt.figtext(0.5, 0.02, f"Students who like neither Math, Science, nor English: {self.neither}", ha="center", fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat003:
    
    def __init__(self):
        self.length = round(rnd.uniform(30, 60), 1)
        self.width = round(rnd.uniform(20, 40), 1)
        self.height = round(rnd.uniform(10, 20), 1)

        # Round to 1 significant figure
        rounded_length = int(100 * round(self.length / 100 + 0.0001, 1))
        rounded_width = int(100 * round(self.width / 100 + 0.0001, 1))
        rounded_height = int(100 * round(self.height / 100 + 0.0001, 1))

        self.answer = rounded_length * rounded_width * rounded_height

        self.description = (
            f"By rounding each dimension to 1 significant figure, estimate the volume of the box."
        )

        self.topic = "Number"
        self.subtopic = "Estimation"
        self.source = "Adapted from Complete Mathematics for Cambridge IGCSE (David Rayner)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original dimensions:}} &\\\\"
            f"\\text{{Length}} &= {self.length}\\\\"
            f"\\text{{Width}} &= {self.width}\\\\"
            f"\\text{{Height}} &= {self.height}\\\\"
            f"\\text{{Rounding to 1 significant figure:}} &\\\\"
            f"L &\\approx {rounded_length}\\\\"
            f"W &\\approx {rounded_width}\\\\"
            f"H &\\approx {rounded_height}\\\\"
            f"\\text{{Estimated Volume}} &= L \\times W \\times H\\\\"
            f"&= {rounded_length} \\times {rounded_width} \\times {rounded_height}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Define the vertices of the box
        points = np.array([
            [0, 0, 0], [self.length, 0, 0], [self.length, self.width, 0], [0, self.width, 0],       # Bottom
            [0, 0, self.height], [self.length, 0, self.height], [self.length, self.width, self.height], [0, self.width, self.height] # Top
        ])

        # Define the edges
        edges = [
            [0, 1], [1, 2], [2, 3], [3, 0], # Bottom
            [4, 5], [5, 6], [6, 7], [7, 4], # Top
            [0, 4], [1, 5], [2, 6], [3, 7]  # Vertical
        ]

        # Plot the edges
        for edge in edges:
            p1, p2 = points[edge[0]], points[edge[1]]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='b', alpha=0.6)

        # Add Labels with CONSISTENT offsets
        # Calculate a scaling factor based on the largest dimension
        max_dim = max(self.length, self.width, self.height)
        offset = max_dim * 0.15  # 15% buffer relative to the scene size

        # Length Label (along X axis):
        # Position: Middle of X, offset in negative Y (front of box)
        ax.text(self.length / 2, -offset, 0, f"Length\n{self.length}", 
                color='red', ha='center', va='center')

        # Width Label (along Y axis):
        # Position: Offset in positive X (right of box), Middle of Y
        ax.text(self.length + offset, self.width / 2, 0, f"Width\n{self.width}", 
                color='red', ha='center', va='center')

        # Height Label (along Z axis):
        # Position: Offset in negative X (left of box), Middle of Z
        ax.text(-offset, 0, self.height / 2, f"Height\n{self.height}", 
                color='red', ha='center', va='center')
        
        # Formatting
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        plt.axis('off')

        # Set explicit limits including the offset so labels aren't cut off
        ax.set_xlim([-offset * 2, self.length + offset * 2])
        ax.set_ylim([-offset * 2, self.width + offset * 2])
        ax.set_zlim([0, self.height + offset])

        # Fix aspect ratio
        ax.set_box_aspect((self.length, self.width, self.height))

        # plt.title("Box Dimensions Representation")
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat004:
    
    def __init__(self):
        self.length = rnd.randint(15, 30)
        self.width = rnd.randint(10, min(self.length, 20))

        length_upper = self.length + 0.5
        width_upper = self.width + 0.5

        self.answer = length_upper * width_upper

        self.description = (
            f"Given a garden below whose measurements are correct to the nearest meter. Calculate the upper bound of the area of the garden."
        )

        self.topic = "Number"
        self.subtopic = "Limits of accuracy"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Since measurements are to the nearest meter, the error is }} \\pm 0.5\\,\\text{{m}}.\\\\"
            f"\\text{{Upper bound of length}} &= {self.length} + 0.5 = {round(self.length + 0.5, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Upper bound of width}} &= {self.width} + 0.5 = {round(self.width + 0.5, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Upper bound of Area}} &= \\text{{Length}}_{{upper}} \\times \\text{{Width}}_{{upper}}\\\\"
            f"&= {round(self.length + 0.5, 10)} \\times {round(self.width + 0.5, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))

        # Create the Rectangle
        # (0, 0) is the bottom-left anchor point
        rect = patches.Rectangle((0, 0), self.length, self.width, 
                                linewidth=2, 
                                edgecolor='black', 
                                facecolor='#e6f2ff') # Light blue fill
        
        # Add the rectangle to the plot
        ax.add_patch(rect)

        # Set the limits of the plot to ensure everything fits
        # Adding some padding around the shape
        ax.set_xlim(-2, self.length + 2)
        ax.set_ylim(-2, self.width + 2)

        # Add Labels
        # Label for Length (Bottom)
        ax.text(self.length / 2, -0.8, f'{self.length} m', 
                ha='center', va='top', fontsize=12, fontweight='bold')

        # Label for Width (Left)
        ax.text(-0.8, self.width / 2, f'{self.width} m', 
                ha='right', va='center', rotation='vertical', fontsize=12, fontweight='bold')

        # Add the Caption
        # Using figtext to place it at the bottom center of the figure, independent of axis coordinates
        plt.figtext(0.5, 0.01, "Measurements are correct to the nearest meter.", 
                    ha='center', fontsize=10, style='italic', 
                    bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

        # Formatting
        ax.set_aspect('equal') # Ensure 1m x 1m looks square
        ax.axis('off')         # Turn off the X/Y axis grid and numbers
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat005:
    
    def __init__(self):
        self.vol_a = 100 * rnd.randint(2, 8) # In ml
        self.price_a = round(rnd.uniform(1, 2), 2) # In dollars
        
        self.vol_b = rnd.randint(12, 18) / 10 # In liters
        self.price_b = round(rnd.uniform(2, 3), 2) # In dollars

        value_a = self.vol_a / self.price_a
        value_b = (self.vol_b * 1000) / self.price_b # Convert liters to ml

        self.answer = 'A'

        if value_b > value_a:
            self.answer = 'B'

        self.description = (
            f"Which bottle offers the better value for money? Show how you decided."
        )

        self.topic = "Number"
        self.subtopic = "Ratio and proportion"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{To determine the better value, we calculate the unit rate (ml per dollar) for each bottle.}} &\\\\"
            f"\\text{{For Bottle A:}} &\\\\"
            f"\\text{{Value}}_A &= \\frac{{\\text{{Volume}}}}{{\\text{{Price}}}} \\\\"
            f"&= \\frac{{{self.vol_a}\\,\\text{{ml}}}}{{\\${self.price_a}}} \\\\"
            f"&= {round(self.vol_a / self.price_a, 10)}\\,\\text{{ml/\\$}}\\\\[10pt]"
            f"\\text{{For Bottle B:}} &\\\\"
            f"\\text{{First, convert liters to ml:}} &\\\\"
            f"{self.vol_b}\\,\\text{{L}} &= {self.vol_b} \\times 1000 = {round(self.vol_b * 1000, 10)}\\,\\text{{ml}}\\\\"
            f"\\text{{Value}}_B &= \\frac{{{round(self.vol_b * 1000, 10)}\\,\\text{{ml}}}}{{\\${self.price_b}}} \\\\"
            f"&= {round((self.vol_b * 1000) / self.price_b, 10)}\\,\\text{{ml/\\$}}\\\\[10pt]"
            f"\\text{{Conclusion:}} &\\\\"
            f"\\text{{Since }} {round((self.vol_b * 1000) / self.price_b, 10)} \\{' > ' if ((self.vol_b * 1000) / self.price_b) > (self.vol_a / self.price_a) else ' < '} {round(self.vol_a / self.price_a, 10)}, \\text{{ Bottle {self.answer} offers better value.}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # 1. Setup the figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))

        # Hide axes for a cleaner "figure" look
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        label_text_a = f"Bottle A\n{self.vol_a} ml\n${self.price_a:.2f}"
        label_text_b = f"Bottle B\n{self.vol_b} liters\n${self.price_b:.2f}"

        # ---------------------------------------------------------
        # DRAWING BOTTLE A (Short and Wide)
        # ---------------------------------------------------------
        # Body: width=3, height=4
        body_a = patches.Rectangle((1, 1), 3, 4, linewidth=2, edgecolor='black', facecolor='#aaddff')
        # Neck: narrower, on top
        neck_a = patches.Rectangle((2, 5), 1, 1, linewidth=2, edgecolor='black', facecolor='#aaddff')
        
        ax.add_patch(body_a)
        ax.add_patch(neck_a)
        
        # Label for A
        ax.text(2.5, 3, label_text_a, ha='center', va='center', fontsize=12, 
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
        
        # ---------------------------------------------------------
        # DRAWING BOTTLE B (Tall and Thin)
        # ---------------------------------------------------------
        # Body: width=1.5, height=7
        body_b = patches.Rectangle((6, 1), 2, 7, linewidth=2, edgecolor='black', facecolor='#ffddaa')
        # Neck: narrower, on top
        neck_b = patches.Rectangle((6.5, 8), 1, 1, linewidth=2, edgecolor='black', facecolor='#ffddaa')

        ax.add_patch(body_b)
        ax.add_patch(neck_b)

        # Label for B
        ax.text(7, 4.5, label_text_b, ha='center', va='center', fontsize=12,
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
        
        # Title
        plt.title("Bottle Description", fontsize=16)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat006:
    
    def __init__(self):
        self.eur_rate = rnd.randint(80, 110) / 100 # 1 USD = eur_rate EUR
        self.jpy_rate = rnd.randint(100, 160) # 1 USD = jpy_rate JPY
        self.total_eur = 100 * rnd.randint(2, 20) # Total Euros to convert to JPY

        usd_from_eur = self.total_eur / self.eur_rate # Convert from EUR to USD
        jpy_from_usd = usd_from_eur * self.jpy_rate # Convert from USD to JPY

        self.answer = round(jpy_from_usd, 2) # Round the result to two decimal places

        self.description = (
            f"A tourist wants to exchange {self.total_eur} Euros (EUR) into Japanese Yen (JPY) using the rates shown on the board. How much Yen will they receive? Round the result to two decimal places."
        )

        self.topic = "Number"
        self.subtopic = "Rates"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given amount}} &= {self.total_eur}\\,\\text{{EUR}}\\\\"
            f"\\text{{Exchange rates:}} &\\\\"
            f"1\\,\\text{{USD}} &= {self.eur_rate}\\,\\text{{EUR}}\\\\"
            f"1\\,\\text{{USD}} &= {self.jpy_rate}\\,\\text{{JPY}}\\\\"
            f"\\text{{First, convert EUR to USD:}} &\\\\"
            f"\\text{{USD}} &= \\frac{{\\text{{EUR}}}}{{\\text{{Rate}}_{{\\text{{EUR}}}}}}\\\\"
            f"&= \\frac{{{self.total_eur}}}{{{self.eur_rate}}}\\\\"
            f"&= {round(self.total_eur / self.eur_rate, 10)}\\,\\text{{USD}}\\\\"
            f"\\text{{Next, convert USD to JPY:}} &\\\\"
            f"\\text{{JPY}} &= \\text{{USD}} \\times \\text{{Rate}}_{{\\text{{JPY}}}}\\\\"
            f"&= {round(self.total_eur / self.eur_rate, 10)} \\times {self.jpy_rate}\\\\"
            f"&= {self.answer}\\,\\text{{JPY}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        header_text = "Today's Exchange Rates"
        row1_text = f"1 USD = {self.eur_rate:.2f} EUR"  # .2f ensures 2 decimal places
        row2_text = f"1 USD = {self.jpy_rate} JPY"

        # figsize is (width, height) in inches
        fig, ax = plt.subplots(figsize=(8, 6))

        ax.axis('off')

        # Parameters: (x, y, string, alignment settings...)
        # Coordinates (0.5, 0.8) means centered horizontally, near the top vertically
        ax.text(0.5, 0.8, header_text, 
                fontsize=16, 
                weight='bold', 
                ha='center', 
                va='center')

        ax.text(0.5, 0.6, row1_text, 
                fontsize=12, 
                ha='center', 
                va='center')

        ax.text(0.5, 0.45, row2_text, 
                fontsize=12, 
                ha='center', 
                va='center')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat007:
    
    def __init__(self):
        self.width = rnd.randint(4, 8) # Width (columns)
        self.height = rnd.randint(3, 6) # Height (rows)
        self.total_squares = self.width * self.height
        self.shaded = rnd.randint(0, self.total_squares) # Number of shaded squares

        self.answer = round((self.shaded / self.total_squares) * 100, 2)

        self.description = (
            f"Calculate what percentage of the grid is shaded. Round the result to two decimal places."
        )

        self.topic = "Number"
        self.subtopic = "Percentages"
        self.source = "Adapted from Complete Mathematics for Cambridge IGCSE (David Rayner)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total squares}} &= \\text{{width}} \\times \\text{{height}}\\\\"
            f"&= {self.width} \\times {self.height}\\\\"
            f"&= {self.total_squares}\\\\"
            f"\\text{{Shaded squares}} &= {self.shaded}\\\\"
            f"\\text{{Percentage}} &= \\frac{{\\text{{Shaded squares}}}}{{\\text{{Total squares}}}} \\times 100\\%\\\\"
            f"&= \\frac{{{self.shaded}}}{{{self.total_squares}}} \\times 100\\%\\\\"
            f"&= {self.answer}\\%"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create a flat array of Zeros (White)
        data = np.zeros(self.total_squares)
        
        # Set the first 'shaded' elements to One (Grey)
        data[:self.shaded] = 1
        
        # Shuffle the array to randomize which specific squares are shaded
        # (Comment this line out if you want the shaded squares to be contiguous)
        np.random.shuffle(data)
        
        # Reshape into a 2D grid (Height x Width)
        grid_matrix = data.reshape((self.height, self.width))

        # Determine figure size based on grid dimensions to keep squares square
        fig, ax = plt.subplots(figsize=(8, 6))

        # Define colors: 0 -> White, 1 -> Grey
        cmap = colors.ListedColormap(['white', 'gray'])
        
        # Display the matrix
        # extent=[0, width, 0, height] maps the pixels to integer coordinates
        ax.imshow(grid_matrix, cmap=cmap, origin='upper', extent=[0, self.width, 0, self.height])

        # Set ticks at integer intervals
        ax.set_xticks(np.arange(0, self.width + 1, 1))
        ax.set_yticks(np.arange(0, self.height + 1, 1))
        
        # Enable grid on those ticks
        ax.grid(which='major', color='black', linestyle='-', linewidth=1)
        
        # Hide the tick labels (numbers) for a cleaner look
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        
        # Remove axis ticks (the small protruding lines) but keep the grid
        ax.tick_params(axis='both', which='both', length=0)

        # Add Title
        plt.title(f"{self.width} x {self.height} Grid")
        
        # Tight layout to remove excess whitespace
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
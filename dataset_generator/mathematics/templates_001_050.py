import numpy as np
import random as rnd
import math
import os
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.transforms import blended_transform_factory
from matplotlib.ticker import MultipleLocator, FuncFormatter
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles
from mathematics.helper import *
from fractions import Fraction

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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"

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
        self.question_type = "Short Answer"
        
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
        self.question_type = "MCQ"
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
        self.question_type = "Short Answer"
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
        self.question_type = "Short Answer"
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

class Mat008:
    
    def __init__(self):
        self.start_hour = rnd.randint(8, 11)
        self.start_minute = rnd.choice([0, 15, 30, 45])

        self.finish_hour = rnd.randint(self.start_hour + 1, 14)
        self.finish_minute = rnd.choice([0, 15, 30, 45])

        minute_result = (self.finish_minute - self.start_minute) % 60
        hour_result = self.finish_hour - self.start_hour - (self.start_minute > self.finish_minute)

        self.answer = f"{hour_result} {'hours' if hour_result != 1 else 'hour'} {minute_result} minutes"

        self.description = (
            f"The clocks show the start and finish times of a mathematics examination. Calculate the total length of the examination in hours and minutes."
        )

        self.topic = "Number"
        self.subtopic = "Time"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.question_type = "Free-form"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Start Time}} &= {self.start_hour}:{self.start_minute:02d}\\\\"
            f"\\text{{Finish Time}} &= {self.finish_hour}:{self.finish_minute:02d}\\\\"
            f"\\text{{Duration}} &= \\text{{Finish Time}} - \\text{{Start Time}}\\\\"
            + (
                f"&= {self.finish_hour}:{self.finish_minute:02d} - {self.start_hour}:{self.start_minute:02d}\\\\"
                f"&= ({self.finish_hour - 1}:{self.finish_minute + 60}) - {self.start_hour}:{self.start_minute:02d} \\quad \\text{{(Borrow 60 min)}}\\\\"
                f"&= ({self.finish_hour - 1} - {self.start_hour})\\,\\text{{hours}} \\; ({self.finish_minute + 60} - {self.start_minute})\\,\\text{{minutes}}\\\\"
                if self.finish_minute < self.start_minute else
                f"&= {self.finish_hour}:{self.finish_minute:02d} - {self.start_hour}:{self.start_minute:02d}\\\\"
                f"&= ({self.finish_hour} - {self.start_hour})\\,\\text{{hours}} \\; ({self.finish_minute} - {self.start_minute})\\,\\text{{minutes}}\\\\"
            )
            + f"&= \\text{{{self.answer}}}"
            + "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Figure
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        # Draw Clocks
        self.draw_clock(axs[0], self.start_hour, self.start_minute, "Clock A (Start)")
        self.draw_clock(axs[1], self.finish_hour, self.finish_minute, "Clock B (Finish)")

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

    def draw_clock(self, ax, hour, minute, title):
        """
        Draws an analog clock on the given Matplotlib axis.
        """
        # Draw the Clock Face
        # Circle
        circle = plt.Circle((0, 0), 1, color='white', ec='black', lw=3)
        ax.add_artist(circle)
        
        # Draw Hour Numbers (1-12)
        # 0 degrees is usually East in plotting, but 12 o'clock is North (90 degrees).
        # We use sin/cos swapped to map 0 to North.
        for i in range(1, 13):
            angle_rad = np.radians(i * 30)  # 360 / 12 = 30 degrees per hour
            x = 0.85 * np.sin(angle_rad)
            y = 0.85 * np.cos(angle_rad)
            ax.text(x, y, str(i), ha='center', va='center', fontsize=12, fontweight='bold')

        # Calculate Hand Angles
        # Minute hand: 360 degrees / 60 minutes = 6 degrees per minute
        minute_angle = np.radians(minute * 6)
        
        # Hour hand: 360 degrees / 12 hours = 30 degrees per hour
        # PLUS the fractional movement based on minutes
        hour_display = hour % 12  # Convert 13/14 to 1/2 for display
        hour_angle = np.radians((hour_display * 30) + (minute * 0.5))

        # Draw Hands
        # Plotting (0,0) to (x,y). 
        # Using (sin, cos) so that 0 radians is North (12 o'clock)
        
        # Hour Hand (Shorter and Thicker)
        hx = 0.5 * np.sin(hour_angle)
        hy = 0.5 * np.cos(hour_angle)
        ax.plot([0, hx], [0, hy], color='black', lw=6, solid_capstyle='round')
        
        # Minute Hand (Longer and Thinner)
        mx = 0.8 * np.sin(minute_angle)
        my = 0.8 * np.cos(minute_angle)
        ax.plot([0, mx], [0, my], color='black', lw=3, solid_capstyle='round')

        # Center Point
        ax.add_artist(plt.Circle((0, 0), 0.05, color='black'))

        # Formatting
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f"{title}", y=-0.1, fontsize=12)
        
class Mat009:
    
    def __init__(self):
        # Town positions (distance from Town A in km)
        self.min_distance = 10
        self.max_distance = 25
        self.town_a_pos = 0
        self.town_b_pos = self.town_a_pos + rnd.randint(self.min_distance, self.max_distance)
        self.town_c_pos = self.town_b_pos + rnd.randint(self.min_distance, self.max_distance)
        self.town_d_pos = self.town_c_pos + rnd.randint(self.min_distance, self.max_distance)

        self.departure_time = rnd.randint(0, 8)

        # Use a 12-minute base unit (0.2 hours).
        unit = 0.2
        self.min_travel_time = 0.2 # hours
        self.max_travel_time = 3.0
        self.min_rest_time = 0.0 # hours
        self.max_rest_time = self.max_travel_time
        
        self.time_at_b = round(self.departure_time + randrange_float(self.min_travel_time, self.max_travel_time + unit, unit), 2)
        self.time_leave_b = round(self.time_at_b + randrange_float(self.min_rest_time, self.max_rest_time + unit, unit), 2)

        self.time_at_c = round(self.time_leave_b + randrange_float(self.min_travel_time, self.max_travel_time + unit, unit), 2)
        self.time_leave_c = round(self.time_at_c + randrange_float(self.min_rest_time, self.max_rest_time + unit, unit), 2)
        
        self.time_at_d = round(self.time_leave_c + randrange_float(self.min_travel_time, self.max_travel_time + unit, unit), 2)
        self.arrival_time = self.time_at_d

        dist_ab = round(self.town_b_pos - self.town_a_pos, 10)
        time_ab = round(self.time_at_b - self.departure_time, 10)
        speed_ab = round(dist_ab / time_ab, 10)
        dist_cd = round(self.town_d_pos - self.town_c_pos, 10)
        time_cd = round(self.time_at_d - self.time_leave_c, 10)
        speed_cd = round(dist_cd / time_cd, 10)

        self.answer = round(abs(speed_ab - speed_cd), 10)
        
        self.description = (
            f"Jason leaves Town A at {self.departure_time}.00 and cycles to Town D, The travel graph shows Jason’s journey. Find the difference of Jason's Average Speed from A to B and C to D."
        )
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs in practical situations"
        self.source = "Adapted from 2025-specimen-paper-3"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Average Speed from A to B:}} & \\\\"
            f"v_{{AB}} &= \\frac{{\\text{{Distance}}}}{{\\text{{Time}}}} \\\\"
            f"&= \\frac{{{self.town_b_pos} - {self.town_a_pos}}}{{{self.time_at_b} - {self.departure_time}}} \\\\"
            f"&= \\frac{{{dist_ab}}}{{{time_ab}}} \\\\"
            f"&= {speed_ab}\\,\\text{{km/h}} \\\\"
            f"\\text{{2. Average Speed from C to D:}} & \\\\"
            f"v_{{CD}} &= \\frac{{\\text{{Distance}}}}{{\\text{{Time}}}} \\\\"
            f"&= \\frac{{{self.town_d_pos} - {self.town_c_pos}}}{{{self.time_at_d} - {self.time_leave_c}}} \\\\"
            f"&= \\frac{{{dist_cd}}}{{{time_cd}}} \\\\"
            f"&= {speed_cd}\\,\\text{{km/h}} \\\\"
            f"\\text{{3. Difference in Speeds:}} & \\\\"
            f"\\text{{Difference}} &= |v_{{AB}} - v_{{CD}}| \\\\"
            f"&= |{speed_ab} - {speed_cd}| \\\\"
            f"&= {self.answer}\\,\\text{{km/h}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))

        # Build time and distance sequences including resting periods and final arrival at D
        times = [
            self.departure_time,                      # depart A
            self.time_at_b,                           # arrive B
            self.time_leave_b,  # leave B
            self.time_at_c,                           # arrive C
            self.time_leave_c,  # leave C
            self.time_at_d                            # arrive D
        ]

        distances = [
            self.town_a_pos,
            self.town_b_pos,
            self.town_b_pos,
            self.town_c_pos,
            self.town_c_pos,
            self.town_d_pos,
        ]

        # Plot the piecewise journey (lines between the points)
        ax.plot(times, distances, color='black', linewidth=2)

        # Configure grid and tick locators: x-major=1 hour, x-minor=5 minutes; y-major=5 units, y-minor=1
        from matplotlib.ticker import MultipleLocator, FuncFormatter
        ax.set_axisbelow(True)
        x_major = MultipleLocator(1.0)
        # Minor ticks: 5 minor divisions per hour -> 12 minutes each -> 12/60 = 0.2 hours
        x_minor = MultipleLocator(12.0 / 60.0)
        # Y axis: major every 10 km, minor every 1 km
        y_major = MultipleLocator(10)
        y_minor = MultipleLocator(1)

        ax.xaxis.set_major_locator(x_major)
        ax.xaxis.set_minor_locator(x_minor)
        ax.yaxis.set_major_locator(y_major)
        ax.yaxis.set_minor_locator(y_minor)

        ax.grid(which='major', linestyle='-', linewidth=0.6, color='gray', alpha=0.8)
        ax.grid(which='minor', linestyle='-', linewidth=0.25, color='gray', alpha=0.5)

        # Format x-axis ticks as HH:MM
        def fmt_time(x, pos=None):
            total_minutes = int(round(x * 60))
            hh = (total_minutes // 60) % 24
            mm = total_minutes % 60
            return f"{hh:02d}:{mm:02d}"

        ax.xaxis.set_major_formatter(FuncFormatter(fmt_time))

        # Set axis limits with small padding
        xmin = min(times)
        xmax = max(times) + 0.25
        ymin = 0
        ymax = max(distances) + 5
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

        # Town labels placed in left margin using blended transform so they don't overlap ticks
        trans = blended_transform_factory(ax.transAxes, ax.transData)

        towns = [
            ('Town A', self.town_a_pos),
            ('Town B', self.town_b_pos),
            ('Town C', self.town_c_pos),
            ('Town D', self.town_d_pos),
        ]

        for name, pos in towns:
            ax.text(-0.06, pos, f"{name} →", transform=trans,
                    fontsize=11, ha='right', va='center')

        # Axis labels
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Distance from\nTown A (km)', fontsize=12, rotation=90, va='center', labelpad=60)

        # Tweak tick label padding
        ax.tick_params(axis='y', which='major', pad=6)

        # Draw arrowheads at the ends of axes
        ax.annotate('', xy=(xmax, 0), xytext=(xmax - 0.001, 0), arrowprops=dict(arrowstyle='->', lw=1.2))
        ax.annotate('', xy=(xmin, ymax), xytext=(xmin, ymax - 0.001), arrowprops=dict(arrowstyle='->', lw=1.2))

        # Make room on the left for town labels
        plt.subplots_adjust(left=0.22, bottom=0.12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Mat010:
    
    def __init__(self):
        self.v0 = rnd.randint(2,20)       # m/s (horizontal portion)
        self.t_flat = rnd.randint(2,20) # seconds (time at constant speed)
        self.t_decel = rnd.randint(2,20) # seconds (time to come to rest)
        self.t_end = self.t_flat + self.t_decel

        # Distances: rectangle + triangle
        self.distance_flat = self.v0 * self.t_flat
        self.distance_decel = 0.5 * self.v0 * self.t_decel
        self.answer = round(self.distance_flat + self.distance_decel, 10)

        self.description = (
            f"The diagram shows the speed–time graph of part of a car journey. Calculate the total distance travelled during the {self.t_end} seconds."
        )

        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs in practical situations"
        self.source = "Adapted from 2025-specimen-paper-4"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Total Distance} &= \\text{Area under the speed-time graph} \\\\"
            "&= \\text{Area of Rectangle (constant speed)} + \\text{Area of Triangle (deceleration)} \\\\"
            "\\text{Area of Rectangle} &= \\text{speed} \\times \\text{time} \\\\"
            f"&= {round(self.v0, 10)}\\,\\text{{m/s}} \\times {round(self.t_flat, 10)}\\,\\text{{s}} \\\\"
            f"&= {round(self.distance_flat, 10)}\\,\\text{{m}} \\\\"
            "\\text{Area of Triangle} &= \\frac{1}{2} \\times \\text{base} \\times \\text{height} \\\\"
            f"&= \\frac{{1}}{{2}} \\times {round(self.t_decel, 10)}\\,\\text{{s}} \\times {round(self.v0, 10)}\\,\\text{{m/s}} \\\\"
            f"&= {round(self.distance_decel, 10)}\\,\\text{{m}} \\\\"
            "\\text{Total Distance} &= \\text{Area of Rectangle} + \\text{Area of Triangle} \\\\"
            f"&= {round(self.distance_flat, 10)}\\,\\text{{m}} + {round(self.distance_decel, 10)}\\,\\text{{m}} \\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Draw the speed-time graph
        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot the piecewise graph
        ax.plot([0, self.t_flat], [self.v0, self.v0], color='black', lw=2)
        ax.plot([self.t_flat, self.t_end], [self.v0, 0], color='black', lw=2)

        # Dashed vertical at t_flat as in the original diagram
        ax.vlines(self.t_flat, 0, self.v0, linestyles='dashed', colors='black', lw=1)

        # Labels and axis limits
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Speed (m/s)')

        ax.set_xlim(0, max(self.t_end + 0.5, 13))
        ax.set_ylim(0, max(self.v0 * 1.2, 10))

        ax.set_xticks([0, self.t_flat, self.t_end])
        ax.set_xticklabels([f'0', f'{self.t_flat} s', f'{self.t_end} s'])

        ax.set_yticks([0, self.v0])
        ax.set_yticklabels([f'0', f'{self.v0} m/s'])

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        
        ax.annotate('', xy=(xmax, 0), xytext=(xmax - 0.001 * (xmax - xmin + 1), 0), arrowprops=dict(arrowstyle='->', lw=1.2))
        ax.annotate('', xy=(0, ymax), xytext=(0, ymax - 0.001 * (ymax - ymin + 1)), arrowprops=dict(arrowstyle='->', lw=1.2))

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150)
        plt.close()

class Mat011:
    
    def __init__(self):
        self.distance_meeting = int(rnd.randint(4, 14))  # km
        
        self.leave_office_hour = rnd.randint(4, 9)
        self.leave_office_minute = rnd.choice([0, 10, 20, 30, 40, 50])
        
        self.travel_time_hour = rnd.randint(1, 2)
        self.travel_time_minute = rnd.choice([0, 10, 20, 30, 40, 50])
        
        self.arrive_meeting_hour = self.leave_office_hour + self.travel_time_hour
        self.arrive_meeting_minute = self.leave_office_minute + self.travel_time_minute
        if self.arrive_meeting_minute >= 60:
            self.arrive_meeting_hour += 1
            self.arrive_meeting_minute -= 60

        self.meeting_duration_hour = rnd.randint(1, 2)
        self.meeting_duration_minute = rnd.choice([0, 10, 20, 30, 40, 50])
        
        self.leave_meeting_hour = self.arrive_meeting_hour + self.meeting_duration_hour
        self.leave_meeting_minute = self.arrive_meeting_minute + self.meeting_duration_minute
        if self.leave_meeting_minute >= 60:
            self.leave_meeting_hour += 1
            self.leave_meeting_minute -= 60
            
        self.arrive_office_hour = self.leave_meeting_hour + self.travel_time_hour
        self.arrive_office_minute = self.leave_meeting_minute + self.travel_time_minute
        if self.arrive_office_minute >= 60:
            self.arrive_office_hour += 1
            self.arrive_office_minute -= 60            
        
        self.speed = round(self.distance_meeting / (self.travel_time_hour + self.travel_time_minute / 60.0), 2)  # km/h
                
        self.answer = f"{self.leave_office_hour}:{self.leave_office_minute:02d}"

        self.description = (
            f"Ky cycles from his office to a meeting and back again. The travel graph shows his time at the meeting and his journey back. Ky cycles from his office to the meeting at a constant speed of {self.speed:.2f} km/h. What time does Ky leave his office?"
        )

        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs in practical situations"
        self.source = "Adapted from IGCSE June 2025 Question Paper 11"
        self.curriculum = "IGCSE"
        self.question_type = "Free-form"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Identify meeting arrival time from the graph:} &\\\\"
            f"\\text{{Arrival at meeting}} &= {self.arrive_meeting_hour:02d}:{self.arrive_meeting_minute:02d}\\\\"
            f"\\text{{Distance from office to meeting}} &= {self.distance_meeting}\\,\\text{{km}}\\\\"
            "\\text{2. Calculate travel time to the meeting:} &\\\\"
            "\\text{Time} &= \\frac{\\text{Distance}}{\\text{Speed}}\\\\"
            f"&= \\frac{{{self.distance_meeting}\\,\\text{{km}}}}{{{self.speed}\\,\\text{{km/h}}}}\\\\"
            f"&= {round(self.travel_time_hour + self.travel_time_minute / 60.0, 10)}\\,\\text{{hours}}\\\\"
            "\\text{Convert decimal hours to hours and minutes:} &\\\\"
            f"\\text{{Hours}} &= \\lfloor{round(self.travel_time_hour + self.travel_time_minute / 60.0, 10)}\\rfloor = {self.travel_time_hour}\\,\\text{{h}}\\\\"
            f"\\text{{Minutes}} &= ({round(self.travel_time_hour + self.travel_time_minute / 60.0, 10)} - {self.travel_time_hour}) \\times 60 = {self.travel_time_minute}\\,\\text{{min}}\\\\"
            f"\\text{{Total Travel Time}} &= {self.travel_time_hour}\\,\\text{{h}} \\, {self.travel_time_minute}\\,\\text{{min}}\\\\"
            "\\text{3. Calculate departure time from office:} &\\\\"
            "\\text{Departure Time} &= \\text{Arrival Time} - \\text{Travel Time}\\\\"
            f"&= {self.arrive_meeting_hour:02d}:{self.arrive_meeting_minute:02d} - {self.travel_time_hour}\\,\\text{{h}} \\, {self.travel_time_minute}\\,\\text{{min}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Compute key times in decimal hours
        depart_time = self.leave_office_hour + self.leave_office_minute / 60.0
        arrive_time = self.arrive_meeting_hour + self.arrive_meeting_minute / 60.0
        leave_time = self.leave_meeting_hour + self.leave_meeting_minute / 60.0

        # Travel back takes same duration as travel there (constant speed)
        travel_minutes = int(round((arrive_time - depart_time) * 60))
        back_time = leave_time + travel_minutes / 60.0

        times = [arrive_time, leave_time, back_time]
        distances = [self.distance_meeting, self.distance_meeting, 0]

        fig, ax = plt.subplots(figsize=(10, 8))

        # Plot path
        ax.plot(times, distances, color='black', linewidth=2)

        # Grid: major = 1 hour, minor = 10 minutes
        ax.set_axisbelow(True)
        x_major = MultipleLocator(1.0)
        x_minor = MultipleLocator(10.0 / 60.0)
        y_major = MultipleLocator(1)
        y_minor = MultipleLocator(1)

        ax.xaxis.set_major_locator(x_major)
        ax.xaxis.set_minor_locator(x_minor)
        ax.yaxis.set_major_locator(y_major)
        ax.yaxis.set_minor_locator(y_minor)

        ax.grid(which='major', linestyle='-', linewidth=0.6, color='gray', alpha=0.9)
        ax.grid(which='minor', linestyle=':', linewidth=0.6, color='gray', alpha=0.9)

        ax.xaxis.set_major_formatter(FuncFormatter(fmt_time))

        xmin = self.leave_office_hour - 1.0
        xmax = self.arrive_office_hour + 1.0
        ymin = 0
        ymax = self.distance_meeting + 2
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

        trans = blended_transform_factory(ax.transAxes, ax.transData)
        ax.text(-0.06, ymax / 2, 'Distance from\noffice (km)', transform=trans,
                fontsize=11, ha='right', va='center')

        # Office label and axis arrows
        label_x = -0.03
        ax.text(label_x, 0, 'Office →', transform=trans, ha='right', va='center', fontsize=11)
        ax.annotate('', xy=(xmax, 0), xytext=(xmax - 0.001, 0), arrowprops=dict(arrowstyle='->', lw=1.2))
        ax.annotate('', xy=(xmin, ymax), xytext=(xmin, ymax - 0.001), arrowprops=dict(arrowstyle='->', lw=1.2))

        plt.subplots_adjust(left=0.18, bottom=0.12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
        
class Mat012:
    
    def __init__(self):
        # Parameter Selection with Perfect Square Discriminant
        # This ensures roots snap perfectly to the grid.
        while True:
            r1 = rnd.randint(-3, 1)
            r2 = rnd.randint(r1 + 1, 3)
            self.a = 1
            self.b = -(r1 + r2)
            self.c = r1 * r2
            
            gap = abs(r1 - r2)
            gap_sq = gap**2
            
            # Logic: gap_sq + 4d = k^2 to ensure integer roots for the intersection
            valid_ds = []
            for k in range(gap + 2, gap + 10, 2):
                d_val = (k**2 - gap_sq) // 4
                if 1 <= d_val <= 6: 
                    valid_ds.append(d_val)
            
            if valid_ds:
                self.d = rnd.choice(valid_ds)
                discriminant = self.b**2 - 4 * (self.c - self.d)
                k_val = int(np.round(np.sqrt(discriminant)))
                
                r1_f = (-self.b - k_val) / 2
                r2_f = (-self.b + k_val) / 2
                self.roots = sorted([int(r1_f), int(r2_f)])
                break

        self.answer = f"x = {self.roots[0]} or x = {self.roots[1]}"
        
        # Polynomial formatting helper
        def fmt_poly(coeff, var):
            if coeff == 0: return ""
            sign = "+" if coeff > 0 else "-"
            val = abs(coeff)
            val_str = "" if (val == 1 and var != "") else str(val)
            return f" {sign} {val_str}{var}"

        # Equations for reasoning
        graph_eq_y = f"y = x^2{fmt_poly(self.b, 'x')}{fmt_poly(self.c, '')}"
        self.target_eq = f"x^2{fmt_poly(self.b, 'x')}{fmt_poly(self.c - self.d, '')} = 0"
        
        self.description = (
            f"The graph of a quadratic function is shown on the grid. "
            f"By first determining the equation of the graph, use it to solve ${self.target_eq}$."
        )
        
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 12"
        self.curriculum = "IGCSE"
        self.question_type = "Free-form"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Determine the equation of the graph:} & \\\\"
            f"\\text{{Identify intercepts: }} & x_1 = {r1}, \\, x_2 = {r2}, \\, y\\text{{-intercept}} = {self.c} \\\\"
            "\\text{Function form: } y &= (x - r_1)(x - r_2) \\\\"
            f"y &= (x - ({r1}))(x - ({r2})) \\\\"
            f"{graph_eq_y} & \\\\"
            "\\text{2. Solve the target equation using the graph:} & \\\\"
            f"\\text{{Target: }} x^2 {fmt_poly(self.b, 'x')} {fmt_poly(self.c - self.d, '')} &= 0 \\\\"
            "\\text{Rearrange to match the graph function: } & \\\\"
            f"x^2 {fmt_poly(self.b, 'x')} {fmt_poly(self.c, '')} &= {self.d} \\\\"
            f"\\text{{Find intersections of the curve and line }} y &= {self.d} \\\\"
            f"\\text{{From the graph, at }} y = {self.d}, \\text{{ we find:}} & \\\\"
            f"x_1 &= {self.roots[0]}, \\quad x_2 = {self.roots[1]} \\\\"
            f"\\text{{Final Result: }} & x_1 = {self.roots[0]} \\text{{ or }} x_2 = {self.roots[1]}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))

        x = np.linspace(-5, 5, 400)
        y = self.a * x**2 + self.b * x + self.c

        ax.axhline(0, color='black', linewidth=1.2)
        ax.axvline(0, color='black', linewidth=1.2)
        ax.plot(x, y, color='black', linewidth=1.8)

        # Draw the intersection line y=d as a faint guide
        ax.axhline(self.d, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

        # Configuration for IGCSE dense grid
        ax.set_xlim(-4, 4)
        ax.set_ylim(-7, 7)
        ax.set_xticks(np.arange(-4, 5, 1))
        ax.set_yticks(np.arange(-7, 8, 1))
        ax.minorticks_on()
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        
        ax.grid(which='major', linestyle='-', linewidth=0.8, color='gray', alpha=0.5)
        ax.grid(which='minor', linestyle=':', linewidth=0.4, color='gray', alpha=0.3)

        ax.set_xlabel('x', loc='right')
        ax.set_ylabel('y', loc='top', rotation=0)

        # Annotate intercepts to help candidates determine the equation
        # x-intercepts
        ax.plot([-(self.b/2 - np.sqrt(self.b**2 - 4*self.c)/2), -(self.b/2 + np.sqrt(self.b**2 - 4*self.c)/2)], 
                [0, 0], 'ko', markersize=4)
        # y-intercept
        ax.plot(0, self.c, 'ko', markersize=4)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=200, bbox_inches='tight')
        plt.close(fig)
        
class Mat013:
    
    def __init__(self):
        # Define roots for the graphed cubic function
        # Selecting roots within a range that keeps the graph visible and centered
        g_r = rnd.sample([-2, -1, 0, 1, 2, 3, 4], 3)
        g_r.sort()
        self.graph_roots = g_r
        
        # Leading coefficient
        self.a = rnd.choice([1, -1])
        
        # Calculate coefficients for Graph: y = a(x - r1)(x - r2)(x - r3)
        # Expanded: y = a*x^3 + b*x^2 + c*x + d
        sum_g = sum(self.graph_roots)
        sum_prod_g = (g_r[0]*g_r[1] + g_r[0]*g_r[2] + g_r[1]*g_r[2])
        prod_g = (g_r[0]*g_r[1]*g_r[2])
        
        self.b = int(-self.a * sum_g)
        self.c = int(self.a * sum_prod_g)
        self.d = int(-self.a * prod_g)

        # Define TARGET roots (the solution to the equation)
        # To ensure the student draws a STRAIGHT LINE, the x^2 coefficient of the target equation must equal 'self.b'.
        # Since b = -a * (sum of roots), the target roots must have the same sum.
        while True:
            t_r = rnd.sample([-3, -2, -1, 0, 1, 2, 3, 4, 5], 3)
            if sum(t_r) == sum_g and sorted(t_r) != self.graph_roots:
                t_r.sort()
                self.target_roots = t_r
                break
        
        # Multiplier forced to 1 as requested
        self.e = 1
        
        # Target Equation coefficients (e=1, so T_A=a, T_B=b)
        t_sum_prod = (self.target_roots[0]*self.target_roots[1] + 
                      self.target_roots[0]*self.target_roots[2] + 
                      self.target_roots[1]*self.target_roots[2])
        t_prod = (self.target_roots[0]*self.target_roots[1]*self.target_roots[2])
        
        T_A = self.a
        T_B = self.b # Guaranteed by sum(target_roots) == sum_g
        T_C = int(self.a * t_sum_prod)
        T_D = int(-self.a * t_prod)

        # Calculate the line y = mx + k
        # Target Equation: ax^3 + bx^2 + T_C*x + T_D = 0
        # Graph Equation:  y = ax^3 + bx^2 + cx + d
        # Subtracting:     y - (cx + d) = -(T_C*x + T_D)
        # Resulting Line:  y = (c - T_C)x + (d - T_D)
        self.m = int(self.c - T_C)
        self.k = int(self.d - T_D)

        # LaTeX strings for equations
        graph_eq_str = f"y = {fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')}"
        self.target_eq_str = f"{fmt_poly(T_A, 'x^3', True)}{fmt_poly(T_B, 'x^2')}{fmt_poly(T_C, 'x')}{fmt_poly(T_D, '')} = 0"
        
        self.answer = " or ".join([f"x = {r}" for r in self.target_roots])
        
        self.description = f"By drawing a suitable straight line on the grid, solve the equation ${self.target_eq_str}$."
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 41"
        self.curriculum = "IGCSE"
        self.question_type = "Free-form"
        
        # Revised Reasoning
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Determine the cubic equation from the x-intercepts on the graph:} & \\\\"
            f"\\text{{Roots from grid: }} x_1 &= {round(float(self.graph_roots[0]), 10)}, \\, x_2 = {round(float(self.graph_roots[1]), 10)}, \\, x_3 = {round(float(self.graph_roots[2]), 10)} \\\\"
            "\\text{The equation is in the form: } y &= a(x - x_1)(x - x_2)(x - x_3) \\\\"
            f"y &= {self.a}(x - ({round(float(self.graph_roots[0]), 10)}))(x - ({round(float(self.graph_roots[1]), 10)}))(x - ({round(float(self.graph_roots[2]), 10)})) \\\\"
            f"\\text{{Expanded function: }} y &= {fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')} \\\\"
            "\\text{2. Rearrange the target equation to involve the graph function:} & \\\\"
            f"\\text{{Target: }} {fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(int(self.c - self.m), 'x')}{fmt_poly(int(self.d - self.k), '')} &= 0 \\\\"
            "\\text{Observe that the cubic and quadratic terms already match the graph's coefficients:} & \\\\"
            f"{fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')} &= -({round(float(self.c - self.m), 10)})x - ({round(float(self.d - self.k), 10)}) \\\\"
            "\\text{3. Add } cx + d \\text{ to both sides to form the full graph function } y: & \\\\"
            f"{fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')} &= ({round(float(self.c), 10)})x + ({round(float(self.d), 10)}) - ({round(float(self.c - self.m), 10)})x - ({round(float(self.d - self.k), 10)}) \\\\"
            f"y &= ({round(float(self.c), 10)} - {round(float(self.c - self.m), 10)})x + ({round(float(self.d), 10)} - {round(float(self.d - self.k), 10)}) \\\\"
            f"y &= {fmt_poly(self.m, 'x', True)}{fmt_poly(self.k, '')} \\\\"
            f"\\text{{The solutions are the x-coordinates where the curve and the line }} y &= {fmt_poly(self.m, 'x', True)}{fmt_poly(self.k, '')} \\text{{ intersect.}} \\\\"
            "\\text{4. Identify the x-coordinates of these intersection points from the grid:} & \\\\"
            f"x_1 &= {round(float(self.target_roots[0]), 10)}, \\, x_2 = {round(float(self.target_roots[1]), 10)}, \\, x_3 = {round(float(self.target_roots[2]), 10)} \\\\"
            f"\\text{{Final Result: }} & x = {round(float(self.target_roots[0]), 10)} \\text{{ or }} x = {round(float(self.target_roots[1]), 10)} \\text{{ or }} x = {round(float(self.target_roots[2]), 10)}"
            "\\end{aligned}\\]"
        )
                        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        x_plot = np.linspace(-3.5, 5.5, 500)
        y_cubic = self.a * x_plot**3 + self.b * x_plot**2 + self.c * x_plot + self.d

        # Axis information and major/minor lines
        ax.axhline(0, color='black', linewidth=2)
        ax.axvline(0, color='black', linewidth=2)
        ax.plot(x_plot, y_cubic, color='black', linewidth=1)

        for root in self.graph_roots:
            ax.plot(root, 0, 'ko', markersize=5)  # Plot a black dot at the root
            ax.annotate(f'({root}, 0)', 
                        xy=(root, 0), 
                        xytext=(0, 10), 
                        textcoords='offset points', 
                        ha='center', 
                        fontsize=10, 
                        fontweight='bold')

        # Ensure axis markings are clear for candidates to identify roots
        ax.set_xticks(np.arange(-3, 6, 1))
        ax.set_yticks(np.arange(-30, 51, 10))
        ax.set_xlim(-3, 5.5)
        ax.set_ylim(-30, 50)
        
        ax.minorticks_on()
        ax.grid(which='major', linestyle='-', linewidth=1, color='black', alpha=0.3)
        ax.grid(which='minor', linestyle=':', linewidth=0.5, color='gray', alpha=0.2)

        ax.set_xlabel('x', loc='right', fontweight='bold')
        ax.set_ylabel('y', loc='top', rotation=0, fontweight='bold')

        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=150, bbox_inches='tight')
        plt.close(fig)
        
class Mat014:
    
    def __init__(self):
        # Randomized Parameters
        self.a = rnd.randint(5, 50)  # Random initial population
        # Random growth factor between 1.1 and 2.5
        self.b = round(rnd.uniform(1.1, 2.5), 1)
            
        # Select t_sol (0.5 increments) to ensure clean grid identification
        self.t_sol = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
        self.k = round(self.a * (self.b ** self.t_sol), 2)
        
        self.answer = self.t_sol
        
        self.description = (
            f"The population of a bacterial culture, $P$, increases exponentially over time $t$ hours.\n"
            f"The graph of this growth is shown on the grid.\n"
            f"Use the graph to find how many hours it takes for the number of bacteria to reach {round(float(self.k), 10)}."
        )
        
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Original" # Comply to syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Determine the initial population } a \\text{ from the graph at } t = 0: &\\\\"
            "P(t) &= a \\times b^t \\\\"
            "P(0) &= a \\times b^0 = a \\\\"
            f"a &= {round(float(self.a), 10)} \\\\"
            "\\text{2. Identify the growth factor } b \\text{ using the point at } t = 1: &\\\\"
            "P(1) &= a \\times b^1 \\\\"
            f"{round(float(self.a * self.b), 10)} &= {round(float(self.a), 10)} \\times b \\\\"
            f"b &= \\frac{{{round(float(self.a * self.b), 10)}}}{{{round(float(self.a), 10)}}} \\\\"
            f"b &= {round(float(self.b), 10)} \\\\"
            "\\text{3. Form the exponential growth equation:} &\\\\"
            f"P &= {round(float(self.a), 10)} \\times ({round(float(self.b), 10)})^t \\\\"
            f"\\text{{4. Solve for time }} t \\text{{ when the population reaches }} {round(float(self.k), 10)}: &\\\\"
            "a \\times b^t &= P \\\\"
            f"{round(float(self.a), 10)} \\times ({round(float(self.b), 10)})^t &= {round(float(self.k), 10)} \\\\"
            f"({round(float(self.b), 10)})^t &= \\frac{{{round(float(self.k), 10)}}}{{{round(float(self.a), 10)}}} \\\\"
            f"({round(float(self.b), 10)})^t &= {round(float(self.k / self.a), 10)} \\\\"
            "\\text{Apply natural logarithms to both sides to isolate } t: &\\\\"
            f"\\ln(({round(float(self.b), 10)})^t) &= \\ln({round(float(self.k / self.a), 10)}) \\\\"
            f"t \\ln({round(float(self.b), 10)}) &= \\ln({round(float(self.k / self.a), 10)}) \\\\"
            f"t &= \\frac{{\\ln({round(float(self.k / self.a), 10)})}}{{\\ln({round(float(self.b), 10)})}} \\\\"
            f"t &= {round(float(self.t_sol), 10)} \\\\"
            f"\\text{{Final Result: }} & t = {self.answer}\\,\\text{{hours}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        t_plot = np.linspace(0, 5, 500)
        p_plot = self.a * (self.b ** t_plot)
        p_max = max(p_plot)

        # Dynamic Grid Logic for Big P
        if p_max > 500:
            tick_spacing = 100
        elif p_max > 200:
            tick_spacing = 50
        elif p_max > 100:
            tick_spacing = 20
        else:
            tick_spacing = 10
            
        y_limit = (int(p_max / tick_spacing) + 1) * tick_spacing

        # Plotting the curve and key identification points
        ax.plot(t_plot, p_plot, color='black', linewidth=1.5)
        
        # Point (0, a) and (1, a*b)
        for t_pt in [0, 1]:
            p_pt = round(self.a * (self.b ** t_pt), 2)
            ax.plot(t_pt, p_pt, 'ko', markersize=5)
            ax.annotate(f'({t_pt}, {p_pt})', xy=(t_pt, p_pt), xytext=(10, -10), 
                        textcoords='offset points', fontsize=10, fontweight='bold')

        # IGCSE style axes and grid
        ax.axhline(0, color='black', linewidth=2)
        ax.axvline(0, color='black', linewidth=2)
        
        ax.set_xticks(np.arange(0, 6, 1))
        ax.set_yticks(np.arange(0, y_limit + 1, tick_spacing))
            
        ax.set_xlim(-0.5, 5.5)
        ax.set_ylim(-y_limit * 0.05, y_limit)
        
        ax.minorticks_on()
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax.grid(which='major', linestyle='-', linewidth=0.8, color='black', alpha=0.3)
        ax.grid(which='minor', linestyle=':', linewidth=0.4, color='gray', alpha=0.2)

        ax.set_xlabel('t (hours)', loc='right', fontweight='bold')
        ax.set_ylabel('P (population)', loc='top', rotation=0, fontweight='bold')

        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=150, bbox_inches='tight')
        plt.close(fig)
        
class Mat015:
    
    def __init__(self):
        # Randomized Parameters for Decay
        # Initial value 'a' is set higher to allow for visible decay over time
        self.a = rnd.randint(50, 200) 
        # Decay factor 'b' must be between 0 and 1 (e.g., 0.5 to 0.9)
        self.b = round(rnd.uniform(0.5, 0.9), 1)
            
        # Select t_sol to ensure it lands on visible grid increments
        self.t_sol = rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
        self.k = round(self.a * (self.b ** self.t_sol), 2)
        
        self.answer = self.t_sol
        
        self.description = (
            f"The mass, $M$ grams, of a radioactive substance decreases exponentially over time $t$ years.\n"
            f"The graph of this decay is shown on the grid.\n"
            f"Use the graph to find how many years it takes for the mass to reach {round(float(self.k), 10)} grams."
        )
        
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Original" # Comply to syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Determine the initial mass } a \\text{ from the graph at } t = 0: &\\\\"
            "M(t) &= a \\times b^t \\\\"
            "M(0) &= a \\times b^0 = a \\\\"
            f"a &= {round(float(self.a), 10)} \\\\"
            "\\text{2. Identify the decay factor } b \\text{ using the point at } t = 1: &\\\\"
            "M(1) &= a \\times b^1 \\\\"
            f"{round(float(self.a * self.b), 10)} &= {round(float(self.a), 10)} \\times b \\\\"
            f"b &= \\frac{{{round(float(self.a * self.b), 10)}}}{{{round(float(self.a), 10)}}} \\\\"
            f"b &= {round(float(self.b), 10)} \\\\"
            "\\text{3. Form the exponential decay equation:} &\\\\"
            f"M &= {round(float(self.a), 10)} \\times ({round(float(self.b), 10)})^t \\\\"
            f"\\text{{4. Solve for time }} t \\text{{ when the mass reaches }} {round(float(self.k), 10)} \\text{{ g:}} &\\\\"
            "a \\times b^t &= M \\\\"
            f"{round(float(self.a), 10)} \\times ({round(float(self.b), 10)})^t &= {round(float(self.k), 10)} \\\\"
            f"({round(float(self.b), 10)})^t &= \\frac{{{round(float(self.k), 10)}}}{{{round(float(self.a), 10)}}} \\\\"
            f"({round(float(self.b), 10)})^t &= {round(float(self.k / self.a), 10)} \\\\"
            "\\text{Apply natural logarithms to both sides to isolate } t: &\\\\"
            f"\\ln(({round(float(self.b), 10)})^t) &= \\ln({round(float(self.k / self.a), 10)}) \\\\"
            f"t \\ln({round(float(self.b), 10)}) &= \\ln({round(float(self.k / self.a), 10)}) \\\\"
            f"t &= \\frac{{\\ln({round(float(self.k / self.a), 10)})}}{{\\ln({round(float(self.b), 10)})}} \\\\"
            f"t &= {round(float(self.t_sol), 10)} \\\\"
            f"\\text{{Final Result: }} & t = {self.answer}\\,\\text{{years}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        t_plot = np.linspace(0, 5, 500)
        m_plot = self.a * (self.b ** t_plot)
        
        # Decay plot
        ax.plot(t_plot, m_plot, color='black', linewidth=1.5)
        
        # Identification points (0, a) and (1, ab)
        for t_pt in [0, 1]:
            m_pt = round(self.a * (self.b ** t_pt), 2)
            ax.plot(t_pt, m_pt, 'ko', markersize=5)
            ax.annotate(f'({t_pt}, {m_pt})', xy=(t_pt, m_pt), xytext=(10, 5), 
                        textcoords='offset points', fontsize=10, fontweight='bold')

        # Axis and Grid logic
        y_limit = (int(self.a / 20) + 1) * 20
        tick_spacing = 20 if y_limit > 100 else 10
        
        ax.axhline(0, color='black', linewidth=2)
        ax.axvline(0, color='black', linewidth=2)
        ax.set_xticks(np.arange(0, 6, 1))
        ax.set_yticks(np.arange(0, y_limit + 1, tick_spacing))
            
        ax.set_xlim(-0.5, 5.5)
        ax.set_ylim(-y_limit * 0.05, y_limit)
        
        ax.minorticks_on()
        ax.xaxis.set_minor_locator(MultipleLocator(0.1))
        ax.grid(which='major', linestyle='-', linewidth=0.8, color='black', alpha=0.3)
        ax.grid(which='minor', linestyle=':', linewidth=0.4, color='gray', alpha=0.2)

        ax.set_xlabel('t (years)', loc='right', fontweight='bold')
        ax.set_ylabel('M (grams)', loc='top', rotation=0, fontweight='bold')

        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), dpi=150, bbox_inches='tight')
        plt.close(fig)
        
class Mat016:
    def __init__(self):
        # Generate three distinct float roots using deterministic ranges to avoid overlap
        self.r1 = round(randrange_float(-5.0, -2.5, 0.01), 2)
        self.r2 = round(randrange_float(-1.0, 1.5, 0.01), 2)
        self.r3 = round(randrange_float(3.0, 5.5, 0.01), 2)
        
        # Scaling factor a (non-integer)
        self.a = round(randrange_float(0.4, 1.2, 0.01) * rnd.choice([-1, 1]), 2)
        
        # Point k to evaluate, placed outside the roots for clarity
        self.k = round(self.r3 + randrange_float(0.5, 1.5, 0.01), 2)
        
        # Calculation logic
        # f(x) = a(x - r1)(x - r2)(x - r3)
        self.y_int = round(self.a * (-self.r1) * (-self.r2) * (-self.r3), 2)
        self.answer = round(self.a * (self.k - self.r1) * (self.k - self.r2) * (self.k - self.r3), 2)

        self.description = (
            "The figure shows the graph of a cubic function with its intercepts labeled. "
            f"A vertical line is drawn. Based on the information in the "
            "graph, determine the value of $y$ at the intersection point labeled $(k, ?)$."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Sketching curves"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The cubic function can be expressed in factored form using the roots }} r_1, r_2, r_3: &\\\\"
            f"y &= a(x - r_1)(x - r_2)(x - r_3)\\\\"
            f"\\text{{From the graph, the roots are }} x_1 = {round(self.r1, 10)}, x_2 = {round(self.r2, 10)}, \\text{{ and }} x_3 = {round(self.r3, 10)}: &\\\\"
            f"y &= a(x - ({round(self.r1, 10)}))(x - ({round(self.r2, 10)}))(x - ({round(self.r3, 10)}))\\\\"
            f"\\text{{Using the }} y\\text{{-intercept at }} (0, {round(self.y_int, 10)}) \\text{{ to find }} a: &\\\\"
            f"{round(self.y_int, 10)} &= a(0 - ({round(self.r1, 10)}))(0 - ({round(self.r2, 10)}))(0 - ({round(self.r3, 10)}))\\\\"
            f"{round(self.y_int, 10)} &= a({round(-self.r1, 10)})({round(-self.r2, 10)})({round(-self.r3, 10)})\\\\"
            f"a &= \\frac{{{round(self.y_int, 10)}}}{{{round((-self.r1)*(-self.r2)*(-self.r3), 10)}}}\\\\"
            f"a &= {round(self.a, 10)}\\\\"
            f"\\text{{Now, find }} y \\text{{ when }} x = {round(self.k, 10)}: &\\\\"
            f"y &= {round(self.a, 10)}({round(self.k, 10)} - ({round(self.r1, 10)}))({round(self.k, 10)} - ({round(self.r2, 10)}))({round(self.k, 10)} - ({round(self.r3, 10)}))\\\\"
            f"y &= {round(self.a, 10)}({round(self.k - self.r1, 10)})({round(self.k - self.r2, 10)})({round(self.k - self.r3, 10)})\\\\"
            f"y &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Function for plotting
        f = lambda x: self.a * (x - self.r1) * (x - self.r2) * (x - self.r3)

        # Plot setup
        x_min, x_max = self.r1 - 1.5, self.k + 1.5
        x_vals = np.linspace(x_min, x_max, 500)
        y_vals = f(x_vals)
        
        ax.plot(x_vals, y_vals, color='blue', lw=2, label='f(x)')
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        # Labeling the three zeros
        roots = [self.r1, self.r2, self.r3]
        for r in roots:
            ax.plot(r, 0, 'ro')
            ax.text(r, 0.5 if self.a < 0 else -0.8, f"{r}", ha='center', fontweight='bold')
            
        # Labeling the y-intercept
        ax.plot(0, self.y_int, 'ro')
        ax.text(0.3, self.y_int, f"{self.y_int}", va='center', fontweight='bold')

        # Draw the line x = k and the intersection point
        ax.axvline(self.k, color='green', linestyle='--', lw=1.5)
        ax.plot(self.k, self.answer, 'go', markersize=8)
        ax.text(self.k+ (1 if self.answer > 0 else -1), self.answer + (1.5 if self.answer > 0 else -1.5), 
                f"({self.k}, ?)", ha='center', color='green', fontsize=12, fontweight='bold')

        # Formatting
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_xlim(x_min, x_max)
        # Dynamic y-limit to ensure all points are visible
        y_buffer = abs(self.answer) * 0.2 + 2
        ax.set_ylim(min(y_vals) - y_buffer, max(y_vals) + y_buffer)
        
        ax.set_xlabel('$x$', loc='right')
        ax.set_ylabel('$y$', loc='top', rotation=0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat017:
    def __init__(self):
        # p is the vertical asymptote (horizontal translation)
        self.p = round(randrange_float(-3.0, 3.0, 0.5), 2)
        # q is the horizontal asymptote (vertical translation)
        self.q = round(randrange_float(-2.0, 2.0, 0.5), 2)
        
        # k is the stretch factor (ensuring it's not zero)
        self.k = round(randrange_float(1.5, 4.5, 0.1) * rnd.choice([-1, 1]), 2)
        
        # A point (x_val, y_val) used to identify the specific curve
        self.x_val = round(self.p + rnd.choice([-2, -1, 1, 2]), 2)
        self.y_val = round((self.k / (self.x_val - self.p)) + self.q, 2)
        
        # The target x-coordinate for the final question (implicit in image)
        self.target_x = round(self.p + randrange_float(3.0, 5.0, 0.1) * rnd.choice([-1, 1]), 2)
        # Avoid overlap with the provided point
        if abs(self.target_x - self.x_val) < 0.5:
            self.target_x += 2.0
            
        self.answer = round((self.k / (self.target_x - self.p)) + self.q, 2)

        self.description = (
            "The figure shows the graph of a reciprocal function in the form $y = \\frac{k}{x - p} + q$. "
            "The vertical and horizontal asymptotes are shown as dashed lines, and one point on the curve is given. "
            "Based on the information provided in the diagram, find the missing $y$-value at the point indicated."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Sketching curves"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the asymptotes from the dashed lines in the figure:}} &\\\\"
            f"\\text{{Vertical asymptote: }} x &= {round(self.p, 10)} \\implies p = {round(self.p, 10)}\\\\"
            f"\\text{{Horizontal asymptote: }} y &= {round(self.q, 10)} \\implies q = {round(self.q, 10)}\\\\"
            f"\\text{{The equation of the curve is of the form:}} &\\\\"
            f"y &= \\frac{{k}}{{x - p}} + q\\\\"
            f"\\text{{Substitute the given point }} ({round(self.x_val, 10)}, {round(self.y_val, 10)}) \\text{{ into the equation:}} &\\\\"
            f"{round(self.y_val, 10)} &= \\frac{{k}}{{{round(self.x_val, 10)} - ({round(self.p, 10)})}} + {round(self.q, 10)}\\\\"
            f"{round(self.y_val, 10)} - {round(self.q, 10)} &= \\frac{{k}}{{{round(self.x_val - self.p, 10)}}}\\\\"
            f"{round(self.y_val - self.q, 10)} &= \\frac{{k}}{{{round(self.x_val - self.p, 10)}}}\\\\"
            f"k &= {round(self.k, 10)}\\\\"
            f"\\text{{The full equation is: }} y &= \\frac{{{round(self.k, 10)}}}{{x - ({round(self.p, 10)})}} + {round(self.q, 10)}\\\\"
            f"\\text{{Identify the target }} x\\text{{-coordinate from the figure: }} x &= {round(self.target_x, 10)}\\\\"
            f"\\text{{Substitute }} x = {round(self.target_x, 10)} \\text{{ to find the missing }} y\\text{{-value:}} &\\\\"
            f"y &= \\frac{{{round(self.k, 10)}}}{{{round(self.target_x, 10)} - ({round(self.p, 10)})}} + {round(self.q, 10)}\\\\"
            f"y &= \\frac{{{round(self.k, 10)}}}{{{round(self.target_x - self.p, 10)}}} + {round(self.q, 10)}\\\\"
            f"y &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        f = lambda x: (self.k / (x - self.p)) + self.q

        x1 = np.linspace(self.p - 10, self.p - 0.1, 500)
        x2 = np.linspace(self.p + 0.1, self.p + 10, 500)
        
        ax.plot(x1, f(x1), color='blue', lw=2.5)
        ax.plot(x2, f(x2), color='blue', lw=2.5)
        
        # Drawing Asymptotes
        ax.axvline(self.p, color='red', linestyle='--', lw=1.5)
        ax.axhline(self.q, color='red', linestyle='--', lw=1.5)
        
        # Labels for asymptotes on the graph
        ax.text(self.p + 0.2, self.q + 4.5, f'$x = {self.p}$', color='red', fontsize=12, fontweight='bold')
        ax.text(self.p + 4.5, self.q + 0.2, f'$y = {self.q}$', color='red', fontsize=12, fontweight='bold')

        # Marking the known point
        ax.scatter(self.x_val, self.y_val, color='blue', s=60, zorder=5)
        ax.text(self.x_val, self.y_val + (0.4 if self.k > 0 else -0.8), 
                f'({self.x_val}, {self.y_val})', ha='center', fontsize=11, fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

        # Marking the query point with target_x value
        ax.scatter(self.target_x, self.answer, color='green', s=100, edgecolors='black', zorder=6)
        ax.axvline(self.target_x, color='green', linestyle=':', lw=1.2)
        ax.text(self.target_x, self.answer + (0.5 if self.answer > self.q else -0.8), 
                f'({self.target_x}, ?)', color='green', ha='center', fontsize=13, fontweight='bold')

        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        ax.grid(True, which='both', linestyle=':', alpha=0.3)
        
        ax.set_xlim(self.p - 6, self.p + 6)
        ax.set_ylim(self.q - 6, self.q + 6)
        
        ax.set_xlabel('$x$', loc='right', fontsize=12)
        ax.set_ylabel('$y$', loc='top', rotation=0, fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat018:
    def __init__(self):
        # f'(x) = a_prime * (x - x1)(x - x2)
        # Using randrange_float with step 0.01 for maximum variety in stationary point locations
        self.root1 = round(randrange_float(-3.0, 0.5, 0.01), 2)
        self.root2 = round(self.root1 + randrange_float(1.5, 4.0, 0.01), 2)
        
        # Leading multiplier for the derivative. +/- 3 ensures integer x^3 coefficient.
        a_prime = rnd.choice([-3, 3])
        
        # Integrated coefficients: f(x) = (a_prime/3)x^3 + ...
        self.a = float(a_prime // 3)
        self.b = round(-(a_prime * (self.root1 + self.root2)) / 2, 2)
        self.c = round(a_prime * self.root1 * self.root2, 2)
        self.d = float(rnd.randint(-5, 5))
        
        def f(x):
            return self.a * x**3 + self.b * x**2 + self.c * x + self.d
        
        # Select target point M
        self.m_x = rnd.choice([self.root1, self.root2])
        self.m_y = round(f(self.m_x), 2)
        
        # Determine nature of M for description logic
        is_max = (6 * self.a * self.m_x + 2 * self.b) < 0
        self.m_type = "maximum" if is_max else "minimum"
        
        self.ask_for = rnd.choice(['x', 'y'])
        self.answer = self.m_x if self.ask_for == 'x' else self.m_y
        
        # Format the equation string for the graph
        t1 = fmt_poly(self.a, "x^3", True)
        t2 = fmt_poly(self.b, "x^2")
        t3 = fmt_poly(self.c, "x")
        t4 = fmt_poly(self.d, "")
        self.eq_latex = f"$y = {t1}{t2}{t3}{t4}$"

        self.description = (
            f"The diagram shows the graph of a cubic function. "
            f"Point $M$ is a local {self.m_type} of the curve. "
            f"Based on the figure, find the {self.ask_for}-coordinate of $M$."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        # Identification of M (used in both cases)
        m_x_rounded = round(self.m_x, 10)
        m_y_rounded = round(self.m_y, 10)

        # Build the conditional steps
        if self.ask_for == 'x':
            final_steps = (
                f"\\text{{The point }} M \\text{{ is the local {self.m_type} shown on the graph.}} \\\\"
                f"\\text{{From the roots of the derivative, we identify }} x = {m_x_rounded} \\text{{ as the location of }} M. \\\\"
                f"\\text{{Therefore, the }} x\\text{{-coordinate is }} {self.answer}"
            )
        else:
            final_steps = (
                f"\\text{{The point }} M \\text{{ is the local {self.m_type} shown on the graph, located at }} x = {m_x_rounded}. \\\\"
                f"\\text{{To find the corresponding }} y\\text{{-coordinate, substitute }} x = {m_x_rounded} \\text{{ into the original function:}} \\\\"
                f"y &= {self.a}({m_x_rounded})^3 + {fmt_poly(self.b, f'({m_x_rounded})^2')}{fmt_poly(self.c, f'({m_x_rounded})')}{fmt_poly(self.d, '')} \\\\"
                f"y &= {m_y_rounded} \\\\"
                f"\\text{{Therefore, the }} y\\text{{-coordinate is }} {self.answer}"
            )

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The function is: }} y &= {fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')} \\\\"
            f"\\text{{1. Differentiate to find the gradient function:}} \\\\"
            f"\\frac{{dy}}{{dx}} &= {round(3 * self.a, 10)}x^2 {fmt_poly(round(2 * self.b, 10), 'x')}{fmt_poly(self.c, '')} \\\\"
            f"\\text{{2. Set }} \\frac{{dy}}{{dx}} = 0 \\text{{ to find stationary points:}} \\\\"
            f"0 &= {round(3 * self.a, 10)}x^2 {fmt_poly(round(2 * self.b, 10), 'x')}{fmt_poly(self.c, '')} \\\\"
            f"\\text{{Solving for }} x \\text{{ gives: }} x = {round(self.root1, 10)} \\text{{ and }} x = {round(self.root2, 10)} \\\\"
            f"{final_steps}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        pad = 1.2
        x_vals = np.linspace(self.root1 - pad, self.root2 + pad, 400)
        y_vals = self.a * x_vals**3 + self.b * x_vals**2 + self.c * x_vals + self.d
        
        # Plot curve and axes
        ax.plot(x_vals, y_vals, color='blue', lw=2.5, zorder=3)
        ax.axhline(0, color='black', lw=1.2, zorder=2)
        ax.axvline(0, color='black', lw=1.2, zorder=2)
        
        # Plot equation text on the graph (top center/left depending on curve)
        ax.text(0.05, 0.95, self.eq_latex, transform=ax.transAxes, fontsize=16, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Mark point M
        ax.scatter(self.m_x, self.m_y, color='red', s=100, zorder=5)
        
        # Dynamic label positioning
        label_offset = 1.0 if self.m_type == "minimum" else -1.5
        ax.text(self.m_x, self.m_y - label_offset, 'M', 
                color='red', fontsize=22, fontweight='bold', ha='center', zorder=6)
        
        ax.grid(True, which='both', linestyle='--', alpha=0.4)
        ax.set_xlabel('$x$', loc='right', fontsize=14)
        ax.set_ylabel('$y$', loc='top', rotation=0, fontsize=14)
        
        ax.set_xlim(self.root1 - pad, self.root2 + pad)
        y_range = max(y_vals) - min(y_vals)
        ax.set_ylim(min(y_vals) - 0.15 * y_range, max(y_vals) + 0.15 * y_range)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat019:
    def __init__(self):
        # f'(x) = a_prime * (x - x1)(x - x2)
        # Root-based construction for precise curvature
        self.root1 = round(randrange_float(-3.0, 0.5, 0.01), 2)
        self.root2 = round(self.root1 + randrange_float(1.5, 4.0, 0.01), 2)
        
        a_prime = rnd.choice([-3, 3])
        
        # Integrated coefficients for f(x)
        self.a = float(a_prime // 3)
        self.b = round(-(a_prime * (self.root1 + self.root2)) / 2, 2)
        self.c = round(a_prime * self.root1 * self.root2, 2)
        self.d = float(rnd.randint(-5, 5))
        
        def f(x):
            return self.a * x**3 + self.b * x**2 + self.c * x + self.d
        
        def f_prime(x):
            return 3 * self.a * x**2 + 2 * self.b * x + self.c

        # M is a known point on the curve
        self.m_x = round(randrange_float(self.root1, self.root2, 0.01), 2)
        self.m_y = round(f(self.m_x), 2)
        
        # Mathematical properties of line l
        self.gradient = round(f_prime(self.m_x), 2)
        self.intercept = round(self.m_y - (self.gradient * self.m_x), 2)
        
        # The answer is the numerical gradient
        self.answer = self.gradient
        
        # Formatting for display
        t1 = fmt_poly(self.a, "x^3", True)
        t2 = fmt_poly(self.b, "x^2")
        t3 = fmt_poly(self.c, "x")
        t4 = fmt_poly(self.d, "")
        self.curve_eq = f"$y = {t1}{t2}{t3}{t4}$"
        
        # The line is now represented as a variable equation in the diagram
        self.line_label = "$l: y = mx + c$"

        self.description = (
            f"The diagram shows the graph of a cubic function and a tangent line $l$ "
            f"touching the curve at point $M$ as shown in the figure. "
            f"Based on the figure, find the value of the gradient $m$."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The cubic function is: }} y &= {fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')} \\\\"
            f"\\text{{The gradient of the tangent line }} l \\text{{ at point }} M \\text{{ is equal to the derivative }} \\frac{{dy}}{{dx}} \\text{{ evaluated at }} x_M. \\\\"
            f"\\text{{1. Differentiate the function:}} \\\\"
            f"\\frac{{dy}}{{dx}} &= \\frac{{d}}{{dx}}({fmt_poly(self.a, 'x^3', True)}{fmt_poly(self.b, 'x^2')}{fmt_poly(self.c, 'x')}{fmt_poly(self.d, '')}) \\\\"
            f"&= {round(3 * self.a, 10)}x^2 {fmt_poly(round(2 * self.b, 10), 'x')}{fmt_poly(self.c, '')} \\\\"
            f"\\text{{2. Substitute the }} x\\text{{-coordinate of point }} M({self.m_x}, {self.m_y}) \\text{{ into }} \\frac{{dy}}{{dx}}: \\\\"
            f"m &= {round(3 * self.a, 10)}({round(self.m_x, 10)})^2 {fmt_poly(round(2 * self.b, 10), f'({round(self.m_x, 10)})')}{fmt_poly(self.c, '')} \\\\"
            f"&= {self.answer} \\\\"
            f"\\text{{Therefore, the gradient }} m \\text{{ is }} {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        pad = 1.2
        x_vals = np.linspace(self.root1 - pad, self.root2 + pad, 400)
        y_curve = self.a * x_vals**3 + self.b * x_vals**2 + self.c * x_vals + self.d
        y_line = self.gradient * x_vals + self.intercept
        
        # Plot curve and tangent line
        ax.plot(x_vals, y_curve, color='blue', lw=2.5, zorder=3)
        ax.plot(x_vals, y_line, color='green', lw=1.5, linestyle='--', zorder=4)
        
        ax.axhline(0, color='black', lw=1.2, zorder=2)
        ax.axvline(0, color='black', lw=1.2, zorder=2)
        
        # Mark point M and label its coordinates
        ax.scatter(self.m_x, self.m_y, color='red', s=100, zorder=5)
        ax.annotate(f"M({self.m_x}, {self.m_y})", (self.m_x, self.m_y), 
                    textcoords="offset points", xytext=(15, 10), 
                    fontsize=12, color='red', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='red', alpha=0.8))
        
        # Display the Curve equation (Known) and Line equation (Symbolic)
        ax.text(0.05, 0.95, self.curve_eq, transform=ax.transAxes, fontsize=15, 
                verticalalignment='top', color='blue', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
        ax.text(0.05, 0.88, self.line_label, transform=ax.transAxes, fontsize=15, 
                verticalalignment='top', color='green', bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
        
        ax.grid(True, which='both', linestyle='--', alpha=0.4)
        ax.set_xlabel('$x$', loc='right', fontsize=14)
        ax.set_ylabel('$y$', loc='top', rotation=0, fontsize=14)
        
        ax.set_xlim(self.root1 - pad, self.root2 + pad)
        y_range = max(y_curve) - min(y_curve)
        ax.set_ylim(min(y_curve) - 0.15 * y_range, max(y_curve) + 0.15 * y_range)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat020:
    def __init__(self):
        # f(x) = ax^2 + bx + c
        # Use simple integers for coefficients to keep the parabola readable
        self.a = float(rnd.choice([-2, -1, 1, 2]))
        self.b = float(rnd.randint(-4, 4))
        self.c = float(rnd.randint(-3, 3))
        
        # Define two x-coordinates for the secant line points A and B
        # Use randrange_float for variation
        self.x_a = round(randrange_float(-3.0, -0.5, 0.01), 2)
        self.x_b = round(randrange_float(0.5, 3.0, 0.01), 2)
        
        def f(x):
            return self.a * x**2 + self.b * x + self.c
        
        self.y_a = round(f(self.x_a), 2)
        self.y_b = round(f(self.x_b), 2)
        
        # Secant Gradient (m_secant) = (y_b - y_a) / (x_b - x_a)
        # For a parabola f(x) = ax^2 + bx + c, f'(x) = 2ax + b
        # Parallel tangent means f'(x_tan) = m_secant
        # 2a(x_tan) + b = m_secant  => x_tan = (m_secant - b) / (2a)
        
        self.m_secant = (self.y_b - self.y_a) / (self.x_b - self.x_a)
        self.x_tan = round((self.m_secant - self.b) / (2 * self.a), 2)
        self.y_tan = round(f(self.x_tan), 2)
        
        # Randomly choose to ask for x or y coordinate of the point of tangency
        self.ask_for = rnd.choice(['x', 'y'])
        self.answer = self.x_tan if self.ask_for == 'x' else self.y_tan
        
        # Equation formatting for the plot
        t1 = fmt_poly(self.a, "x^2", True)
        t2 = fmt_poly(self.b, "x")
        t3 = fmt_poly(self.c, "")
        self.curve_eq = f"$g(x) = {t1}{t2}{t3}$"

        self.description = (
            f"The diagram shows the graph of the parabola $g(x)$ and a secant line "
            f"intersecting the curve at points $A$ and $B$. There is a point $T$ on the curve "
            f"where the tangent line is parallel to the secant $AB$. "
            f"Based on the information provided in the figure, find the {self.ask_for}-coordinate of point $T$."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Find the gradient of the secant line passing through }} A({self.x_a}, {self.y_a}) \\text{{ and }} B({self.x_b}, {self.y_b}): \\\\"
            f"m_{{secant}} &= \\frac{{y_B - y_A}}{{x_B - x_A}} \\\\"
            f"&= \\frac{{{round(self.y_b, 10)} - ({round(self.y_a, 10)})}}{{{round(self.x_b, 10)} - ({round(self.x_a, 10)})}} \\\\"
            f"&= {round(self.m_secant, 10)} \\\\"
            f"\\text{{2. Find the derivative of the parabola }} g(x) = {fmt_poly(self.a, 'x^2', True)}{fmt_poly(self.b, 'x')}{fmt_poly(self.c, '')}: \\\\"
            f"g'(x) &= {round(2 * self.a, 10)}x {fmt_poly(self.b, '')} \\\\"
            f"\\text{{3. The tangent line at }} T \\text{{ is parallel to the secant, so }} g'(x_T) = m_{{secant}}: \\\\"
            f"{round(2 * self.a, 10)}x_T {fmt_poly(self.b, '')} &= {round(self.m_secant, 10)} \\\\"
            f"{round(2 * self.a, 10)}x_T &= {round(self.m_secant - self.b, 10)} \\\\"
            f"x_T &= {round(self.x_tan, 10)} \\\\"
            + (f"\\text{{4. Substitute }} x_T \\text{{ into }} g(x) \\text{{ to find the }} y\\text{{-coordinate:}} \\\\"
            f"y_T &= {self.a}({round(self.x_tan, 10)})^2 {fmt_poly(self.b, f'({round(self.x_tan, 10)})')}{fmt_poly(self.c, '')} \\\\"
            f"&= {round(self.y_tan, 10)} \\\\" if self.ask_for == 'y' else "") +
            f"\\text{{Therefore, the }} {self.ask_for}\\text{{-coordinate of point }} T \\text{{ is }} {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Use x_range for both the curve and the secant line
        x_range = np.linspace(-4, 4, 400)
        y_curve = self.a * x_range**2 + self.b * x_range + self.c
        
        # Plotting the curve
        ax.plot(x_range, y_curve, color='blue', lw=2, zorder=3)
        
        # Calculate the intercept of the secant line: c = y - mx
        secant_intercept = self.y_a - (self.m_secant * self.x_a)

        # Use x_range here to make the secant line "endless" across the plot
        ax.plot(x_range, self.m_secant * x_range + secant_intercept, color='green', linestyle='--', lw=1.5, zorder=4)

        # Re-add the specific dots for A and B
        ax.scatter([self.x_a, self.x_b], [self.y_a, self.y_b], color='green', s=40, zorder=5)
        
        # Label points A and B
        ax.text(self.x_a, self.y_a, f' A({self.x_a}, {self.y_a})', verticalalignment='bottom', horizontalalignment='right', fontsize=10)
        ax.text(self.x_b, self.y_b, f' B({self.x_b}, {self.y_b})', verticalalignment='bottom', horizontalalignment='left', fontsize=10)
        
        # Mark Point T (Tangency)
        ax.scatter(self.x_tan, self.y_tan, color='red', s=100, zorder=5)
        ax.text(self.x_tan, self.y_tan, ' T ', color='red', verticalalignment='top', fontweight='bold', fontsize=14)
        
        # Equations and Axes
        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        ax.text(0.05, 0.95, self.curve_eq, transform=ax.transAxes, fontsize=16, 
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_xlabel('$x$', loc='right')
        ax.set_ylabel('$y$', loc='top', rotation=0)
        
        # Set limits
        ax.set_xlim(-4, 4)
        y_vals = [self.y_a, self.y_b, self.y_tan]
        ax.set_ylim(min(y_vals) - 5, max(y_vals) + 5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat021:
    def __init__(self):
        # f(x) = a(x - p)(x - q)
        # Defining clear intercepts for the student to read from the graph
        self.p = round(randrange_float(-5.0, -2.0, 0.5), 2)
        self.q = round(randrange_float(2.0, 5.0, 0.5), 2)
        
        # Leading coefficient 'a' can now be positive (upward) or negative (downward)
        # We choose a range that ensures the parabola is visible and distinct
        self.a_magnitude = round(randrange_float(0.8, 1.3, 0.01), 2)
        self.a_sign = rnd.choice([-1, 1])
        self.a = round(self.a_magnitude * self.a_sign, 2)
        
        self.y_int = round(self.a * (-self.p) * (-self.q), 2)
        
        # Vertex defines the start of the one-to-one branch for the inverse
        self.vertex_x = (self.p + self.q) / 2
        
        # Pick a target x-value for the answer (staying close to q for better zoom)
        self.target_x = round(randrange_float(self.q + 1.2, self.q + 2.8, 0.1), 2)
        
        # Calculate k = f(target_x), the input for f^-1(k)
        self.k = round(self.a * (self.target_x - self.p) * (self.target_x - self.q), 2)
        
        self.answer = self.target_x

        self.description = (
            f"The figure shows the graph of a quadratic function $f(x)$ as a solid line and its inverse function $f^{{-1}}(x)$ as a dashed line. "
            f"Based on the coordinates provided in the diagram, find the value of $f^{{-1}}({self.k})$."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Determine the equation of }} f(x) \\text{{ from the roots and }} y\\text{{-intercept:}} &\\\\"
            f"x_1 &= {self.p}, \\quad x_2 = {self.q}, \\quad y_{{\\text{{int}}}} = {self.y_int}\\\\"
            f"f(x) &= a(x - x_1)(x - x_2)\\\\"
            f"{self.y_int} &= a(0 - ({self.p}))(0 - ({self.q}))\\\\"
            f"{self.y_int} &= {round(self.p * self.q, 10)}a \\implies a = {self.a}\\\\"
            f"f(x) &= {self.a}(x - {self.p})(x - {self.q})\\\\"
            f"\\text{{2. Express }} f(x) \\text{{ in the completed square form }} a(x - h)^2 + k: &\\\\"
            f"h &= \\frac{{x_1 + x_2}}{{2}} = \\frac{{{self.p} + {self.q}}}{{2}} = {round(self.vertex_x, 10)}\\\\"
            f"k_{{\\text{{vertex}}}} &= f(h) = {self.a}({round(self.vertex_x, 10)} - ({self.p}))({round(self.vertex_x, 10)} - ({self.q})) = {round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)}\\\\"
            f"f(x) &= {self.a}(x - {round(self.vertex_x, 10)})^2 + {round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)}\\\\"
            f"\\text{{3. Find the inverse function }} f^{{-1}}(x): &\\\\"
            f"y &= {self.a}(x - {round(self.vertex_x, 10)})^2 + {round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)}\\\\"
            f"\\frac{{y - ({round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)})}}{{{self.a}}} &= (x - {round(self.vertex_x, 10)})^2\\\\"
            f"x &= {round(self.vertex_x, 10)} \\pm \\sqrt{{\\frac{{y - ({round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)})}}{{{self.a}}}}}\\\\"
            f"\\text{{4. Substitute }} y = {self.k} \\text{{ and select the branch }} x \\ge {round(self.vertex_x, 10)}: &\\\\"
            f"f^{{-1}}({self.k}) &= {round(self.vertex_x, 10)} + \\sqrt{{\\frac{{{self.k} - ({round(self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q), 10)})}}{{{self.a}}}}}\\\\"
            f"&= {round(self.vertex_x, 10)} + \\sqrt{{{round((self.k - (self.a * (self.vertex_x - self.p) * (self.vertex_x - self.q))) / self.a, 10)}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Framing logic: ensure all key features (roots, y-int, target point) are visible
        limit = max(abs(self.p), abs(self.q), abs(self.k), abs(self.target_x), abs(self.y_int)) + 2
        
        # Define Curves
        xs_f = np.linspace(-limit, limit, 1000)
        def f(x): return self.a * (x - self.p) * (x - self.q)
        ys_f = f(xs_f)
        
        # Only reflect the branch from the vertex to the limit
        xs_inv_branch = np.linspace(self.vertex_x, limit, 1000)
        ys_inv_branch = f(xs_inv_branch)
        
        # Plotting
        ax.plot(xs_f, ys_f, 'k-', lw=2.5, label='$f(x)$') 
        ax.plot(ys_inv_branch, xs_inv_branch, 'k--', lw=2, alpha=0.7, label='$f^{-1}(x)$') 
        
        # Target Point Label (k, ?)
        ax.plot(self.k, self.target_x, 'ro', markersize=8)
        # Position label slightly above or below the point based on direction
        offset = limit * 0.05 if self.a_sign < 0 else -limit * 0.07
        ax.text(self.k, self.target_x + offset, f'({self.k}, ?)', 
                fontsize=14, fontweight='bold', color='red', ha='center')
        
        # Implicit Coordinate Labels for f(x)
        ax.plot([self.p, self.q, 0], [0, 0, self.y_int], 'ko', markersize=6)
        label_offset = limit * 0.03
        ax.text(self.p, label_offset, f'({self.p}, 0)', ha='center', va='bottom', fontsize=11)
        ax.text(self.q, label_offset, f'({self.q}, 0)', ha='center', va='bottom', fontsize=11)
        ax.text(label_offset, self.y_int, f'(0, {self.y_int})', ha='left', va='center', fontsize=11)
        
        # Visual Styling
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        # Identity line y=x
        ax.plot([-limit, limit], [-limit, limit], color='gray', lw=0.8, ls='-.', alpha=0.3)
        
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.4)
        ax.legend(loc='upper left', fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
class Mat022:
    def __init__(self):
        # f(u) = mu + c (Linear) - using 'u' as per request
        # g(x) = p / (qx + r) (Reciprocal)
        # Sequence: x (Raw Material) -> g(x) = u (Intermediate) -> f(u) (Final Product)
        
        # Parameters for g(x)
        self.p = round(randrange_float(5, 15, 0.01), 2)
        self.q = round(randrange_float(0.5, 2.5, 0.01), 2)
        self.r = round(randrange_float(1, 10, 0.01), 2)
        
        # Parameters for f(u)
        self.m = round(randrange_float(2, 6, 0.01), 2)
        self.c = round(randrange_float(5, 25, 0.01), 2)
        
        # Input value x (Raw material in kg)
        self.input_x = round(randrange_float(1, 10, 0.01), 2)
        
        # Calculations
        intermediate_den = self.q * self.input_x + self.r
        self.intermediate_val = self.p / intermediate_den
        
        # Final result = m * intermediate_val + c
        self.answer = round(self.m * self.intermediate_val + self.c, 2)
        
        # Implicit description: value is in the figure
        self.description = (
            "A factory uses a two-stage processing system as shown in the diagram. "
            "Based on the input of raw material and the functions of each machine, "
            "determine the value of the final product in liters."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Determine the intermediate product }} u = g(x) \\text{{ where }} x = {self.input_x}\\,\\text{{kg:}} &\\\\"
            f"g(x) &= \\frac{{{self.p}}}{{{self.q}x + {self.r}}}\\\\"
            f"u = g({self.input_x}) &= \\frac{{{self.p}}}{{{self.q}({self.input_x}) + {self.r}}}\\\\"
            f"&= \\frac{{{self.p}}}{{{round(self.q * self.input_x, 10)} + {self.r}}}\\\\"
            f"&= \\frac{{{self.p}}}{{{round(self.q * self.input_x + self.r, 10)}}}\\\\"
            f"&= {round(self.intermediate_val, 10)}\\\\"
            f"\\text{{2. Substitute }} u \\text{{ into the reactor function }} f(u) \\text{{ to find the final pressure:}} &\\\\"
            f"f(u) &= {self.m}u + {self.c}\\\\"
            f"f({round(self.intermediate_val, 10)}) &= {self.m}({round(self.intermediate_val, 10)}) + {self.c}\\\\"
            f"&= {round(self.m * self.intermediate_val, 10)} + {self.c}\\\\"
            f"&= {self.answer}\\,\\text{{liters}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis('off')

        # Box dimensions
        box_w, box_h = 3.2, 2.2
        
        # --- Machine g ---
        g_x, g_y = 1.5, 1.8
        g_box = patches.FancyBboxPatch((g_x, g_y), box_w, box_h, boxstyle="round,pad=0.2", 
                                       ec="black", fc="#e3f2fd", lw=2)
        ax.add_patch(g_box)
        
        ax.text(g_x + box_w/2, g_y + box_h - 0.4, "Machine $g$", fontsize=14, ha='center', fontweight='bold')
        g_eqn_str = f"$g(x) = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$"
        ax.text(g_x + box_w/2, g_y + box_h/2 - 0.2, g_eqn_str, fontsize=13, ha='center')

        # --- Machine f ---
        f_x, f_y = 7.0, 1.8
        f_box = patches.FancyBboxPatch((f_x, f_y), box_w, box_h, boxstyle="round,pad=0.2", 
                                       ec="black", fc="#fffde7", lw=2)
        ax.add_patch(f_box)

        ax.text(f_x + box_w/2, f_y + box_h - 0.4, "Machine $f$", fontsize=14, ha='center', fontweight='bold')
        # Using f(u) label inside the machine
        f_eqn_str = f"$f(u) = {self.m}u + {self.c}$"
        ax.text(f_x + box_w/2, f_y + box_h/2 - 0.2, f_eqn_str, fontsize=13, ha='center')

        # --- Input, Intermediate, Output Arrows ---
        
        # 1. Input: Raw Material x
        ax.annotate("", xy=(g_x, g_y + box_h/2), xytext=(g_x - 1.5, g_y + box_h/2),
                    arrowprops=dict(arrowstyle="->", lw=2, color="black"))
        ax.text(g_x - 1.6, g_y + box_h/2, f"Raw Material\n$x = {self.input_x}$ kg", 
                ha='right', va='center', fontsize=11, fontweight='bold')
        
        # 2. Intermediate: u = # intermediate product
        ax.annotate("", xy=(f_x, f_y + box_h/2), xytext=(g_x + box_w, g_y + box_h/2),
                    arrowprops=dict(arrowstyle="->", lw=2, color="black"))
        ax.text((g_x + box_w + f_x)/2, g_y + box_h/2 + 0.3, "$u = $\n # Intermediate Product", 
                ha='center', va='bottom', fontsize=11, color="#1565c0")

        # 3. Output: Final Product
        # Fixed arrow direction: From second machine to final product
        ax.annotate("", xy=(f_x + box_w + 1.5, f_y + box_h/2), xytext=(f_x + box_w, f_y + box_h/2),
                    arrowprops=dict(arrowstyle="->", lw=2, color="black"))
        ax.text(f_x + box_w + 1.6, f_y + box_h/2, "Final Product\n(liters)", 
                ha='left', va='center', fontsize=11, fontweight='bold', color="#2e7d32")

        # Save the figure
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat023:
    def __init__(self):
        # f(x) = n / (x - h) + k
        # Asymptotes: x = h (vertical), y = k (horizontal)
        # Using randrange_float for high variability
        self.h = round(randrange_float(-5.0, 5.0, 0.01), 2)
        self.k = round(randrange_float(-5.0, 5.0, 0.01), 2)
        
        # Ensure n is an integer for cleaner point identification
        self.n = rnd.choice([-4, -3, -2, 2, 3, 4])
        
        # Pick a helper point P(x_p, y_p) that the student can see on the graph
        # This allows them to calculate 'n'
        self.x_p = round(self.h + 1, 2)
        self.y_p = round(self.n / (self.x_p - self.h) + self.k, 2)
        
        # Question types: 0 = Domain restriction, 1 = Range restriction, 2 = Coordinate Mapping
        self.q_type = rnd.randint(0, 2)
        
        if self.q_type == 0:
            self.answer = float(self.h)
            self.target_text = "the value of $x$ that is excluded from the domain"
        elif self.q_type == 1:
            self.answer = float(self.k)
            self.target_text = "the value of $y$ that is excluded from the range"
        else:
            # f(a) = target_y => find a
            self.diff = rnd.choice([-2, -1, 1, 2])
            self.target_y = round(float(self.k + (self.n / self.diff)), 2)
            self.a_val = round(float(self.h + self.diff), 2)
            self.answer = self.a_val
            self.target_text = f"the value of $a$ given that $f(a) = {self.target_y}$"

        # Implicit description: forces the user to look at the figure
        self.description = (
            f"The figure shows the graph of a reciprocal function $f(x)$ which passes through the point $P$. "
            f"Based on the information provided in the diagram, determine {self.target_text}."
        )
        
        self.topic = "Algebra and graphs"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        if self.q_type == 0:
            self.reasoning = (
                "\\[\\begin{aligned}"
                f"\\text{{The function is of the form: }} f(x) &= \\frac{{n}}{{x - h}} + k\\\\"
                f"\\text{{Identify the asymptotes from the graph:}} &\\\\"
                f"\\text{{Vertical asymptote: }} x &= {self.h}\\\\"
                f"\\text{{Horizontal asymptote: }} y &= {self.k}\\\\"
                f"\\text{{The domain is restricted where the denominator equals zero:}} &\\\\"
                f"x - h &= 0\\\\"
                f"x - {self.h} &= 0\\\\"
                f"x &= {self.answer}"
                "\\end{aligned}\\]"
            )
        elif self.q_type == 1:
            self.reasoning = (
                "\\[\\begin{aligned}"
                f"\\text{{The function is of the form: }} f(x) &= \\frac{{n}}{{x - h}} + k\\\\"
                f"\\text{{Identify the asymptotes from the graph:}} &\\\\"
                f"\\text{{Vertical asymptote: }} x &= {self.h}\\\\"
                f"\\text{{Horizontal asymptote: }} y &= {self.k}\\\\"
                f"\\text{{The range restriction occurs at the horizontal asymptote where the term }} \\frac{{n}}{{x-h}} \\neq 0: &\\\\"
                f"f(x) &= \\frac{{n}}{{x - h}} + k\\\\"
                f"f(x) &\\neq k\\\\"
                f"f(x) &\\neq {self.answer}"
                "\\end{aligned}\\]"
            )
        else:
            self.reasoning = (
                "\\[\\begin{aligned}"
                f"\\text{{The function is of the form: }} f(x) &= \\frac{{n}}{{x - h}} + k\\\\"
                f"\\text{{1. Identify the asymptotes from the graph: }} h = {self.h}, \\, k = {self.k}\\\\"
                f"\\text{{2. Use point }} P({self.x_p}, {self.y_p}) \\text{{ to determine the constant }} n: &\\\\"
                f"f(x_p) &= \\frac{{n}}{{x_p - h}} + k\\\\"
                f"{self.y_p} &= \\frac{{n}}{{{self.x_p} - ({self.h})}} + {self.k}\\\\"
                f"{round(self.y_p - self.k, 10)} &= \\frac{{n}}{{{round(self.x_p - self.h, 10)}}}\\\\"
                f"n &= {self.n}\\\\"
                f"\\text{{3. Solve for }} a \\text{{ such that }} f(a) = {self.target_y}: &\\\\"
                f"{self.target_y} &= \\frac{{{self.n}}}{{a - {self.h}}} + {self.k}\\\\"
                f"{round(self.target_y - self.k, 10)} &= \\frac{{{self.n}}}{{a - {self.h}}}\\\\"
                f"a - {self.h} &= \\frac{{{self.n}}}{{{round(self.target_y - self.k, 10)}}}\\\\"
                f"a - {self.h} &= {round(self.n / (self.target_y - self.k), 10)}\\\\"
                f"a &= {self.answer}"
                "\\end{aligned}\\]"
            )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        limit = max(abs(self.h), abs(self.k), 8) + 2
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        
        x1 = np.linspace(-limit, self.h - 0.1, 500)
        x2 = np.linspace(self.h + 0.1, limit, 500)
        def f_func(x_v): return self.n / (x_v - self.h) + self.k
            
        ax.plot(x1, f_func(x1), 'k-', lw=2.5)
        ax.plot(x2, f_func(x2), 'k-', lw=2.5)
        
        # Visual Asymptotes
        ax.axvline(self.h, color='gray', ls='--', lw=1, alpha=0.5)
        ax.axhline(self.k, color='gray', ls='--', lw=1, alpha=0.5)
        
        # Equation Template Label
        ax.text(-limit + 1, limit - 1.5, r"$f(x) = \frac{n}{x - h} + k$", 
                fontsize=16, color='darkred', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))
        
        # Key Point P
        ax.plot(self.x_p, self.y_p, 'ro', markersize=8)
        ax.annotate(f"$P({self.x_p}, {self.y_p})$", (self.x_p, self.y_p), 
                    textcoords="offset points", xytext=(10, 10), fontsize=12, fontweight='bold', color='red')
        
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, linestyle=':', alpha=0.4)
        ax.set_aspect('equal')
        
        # Asymptote indicator labels
        ax.text(self.h + 0.2, -limit + 1, f"$x={self.h}$", color='blue', rotation=90, alpha=0.7)
        ax.text(-limit + 1, self.k + 0.2, f"$y={self.k}$", color='blue', alpha=0.7)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat024:
    def __init__(self):
        # Generate integer coordinates for point D and E
        # Ensure they are not the same and have a decent distance for zig-zagging
        self.xd = rnd.randint(-8, 8)
        self.yd = rnd.randint(-8, 8)
        
        self.xe = rnd.randint(-8, 8)
        self.ye = rnd.randint(-8, 8)
        
        # Ensure a minimum distance to allow for a visible zig-zag path
        while abs(self.xe - self.xd) < 3 or abs(self.ye - self.yd) < 3:
            self.xe = rnd.randint(-8, 8)
            self.ye = rnd.randint(-8, 8)
        
        # Calculate Manhattan distance (total steps)
        self.dist_x = abs(self.xe - self.xd)
        self.dist_y = abs(self.ye - self.yd)
        self.answer = self.dist_x + self.dist_y

        # Metadata properties in the required order
        self.description = (
            "A robot travels from point $D$ to point $E$ along the grid lines as shown in the figure. "
            "The robot's path consists of horizontal and vertical steps, and it moves monotonically "
            "(it never moves away from its destination). Based on the coordinates provided in the diagram, "
            "find the total distance traveled by the robot."
        )
        self.topic = "Coordinate geometry"
        self.subtopic = "Coordinates"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Starting point }} D &= (x_D, y_D) = ({self.xd}, {self.yd})\\\\"
            f"\\text{{Ending point }} E &= (x_E, y_E) = ({self.xe}, {self.ye})\\\\"
            f"\\text{{Horizontal distance }} d_x &= |x_E - x_D|\\\\"
            f"&= |{self.xe} - ({self.xd})|\\\\"
            f"&= {round(self.dist_x, 10)}\\,\\text{{units}}\\\\"
            f"\\text{{Vertical distance }} d_y &= |y_E - y_D|\\\\"
            f"&= |{self.ye} - ({self.yd})|\\\\"
            f"&= {round(self.dist_y, 10)}\\,\\text{{units}}\\\\"
            f"\\text{{Since the robot moves monotonically along grid lines, total distance is:}} &\\\\"
            f"d_{{total}} &= d_x + d_y\\\\"
            f"&= {round(self.dist_x, 10)} + {round(self.dist_y, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{units}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Set integer grid
        limit = 10
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        # Major ticks at every integer
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.grid(True, which='both', linestyle='-', color='lightgray', alpha=0.5)
        
        # Bold axes
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)

        # Generate a random monotonic zig-zag path
        # Steps are either +1 or -1 in x/y direction
        step_x = 1 if self.xe > self.xd else -1
        step_y = 1 if self.ye > self.yd else -1
        
        # Pool of steps
        steps = (['x'] * self.dist_x) + (['y'] * self.dist_y)
        rnd.shuffle(steps)
        
        curr_x, curr_y = self.xd, self.yd
        path_points = [(curr_x, curr_y)]
        
        for move in steps:
            if move == 'x':
                curr_x += step_x
            else:
                curr_y += step_y
            path_points.append((curr_x, curr_y))
            
        # Draw the path
        px, py = zip(*path_points)
        ax.plot(px, py, color='red', lw=4, alpha=0.8, zorder=3, label='Robot Path')
        
        # Plot points D and E
        ax.scatter([self.xd, self.xe], [self.yd, self.ye], color='black', s=150, zorder=5)
        
        # Dynamic label placement for D and E
        # Offset them slightly 'away' from the path origin/end
        off_d_y = 0.5 if self.yd < self.ye else -0.8
        off_e_y = -0.8 if self.yd < self.ye else 0.5
        
        ax.text(self.xd, self.yd + off_d_y, f"D({self.xd}, {self.yd})", 
                fontsize=16, ha='center', fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.9, edgecolor='black', boxstyle='round,pad=0.2'))
        
        ax.text(self.xe, self.ye + off_e_y, f"E({self.xe}, {self.ye})", 
                fontsize=16, ha='center', fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.9, edgecolor='black', boxstyle='round,pad=0.2'))

        ax.set_xlabel('x', fontsize=14, loc='right')
        ax.set_ylabel('y', fontsize=14, loc='top', rotation=0)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat025:
    def __init__(self):
        # Base length along the x-axis
        self.base_val = rnd.randint(6, 20)
        self.height_val = rnd.randint(4, 15)
        self.area = 0.5 * self.base_val * self.height_val
        
        # Quadrant logic: 1=(+,+), 2=(-,+), 3=(-,-), 4=(+,-)
        quad = rnd.randint(1, 4)
        
        # Determine signs based on quadrant
        if quad == 1:
            self.base, self.height = self.base_val, self.height_val
        elif quad == 2:
            self.base, self.height = -self.base_val, self.height_val
        elif quad == 3:
            self.base, self.height = -self.base_val, -self.height_val
        else:
            self.base, self.height = self.base_val, -self.height_val
        
        # O is origin (0,0), N is on x-axis (base, 0), M is (base, height)
        # Gradient of MO = (y2 - y1) / (x2 - x1) = (height - 0) / (base - 0)
        self.answer = self.height / self.base

        self.description = (
            "The diagram shows a right-angled triangle $MNO$. Point $O$ is at the origin $(0,0)$ and point $N$ is on the $x$-axis. "
            f"The area of triangle $MNO$ is {self.area} square units. Based on the coordinates shown in the figure, "
            "calculate the gradient of the line segment $MO$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Gradient of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        # Pre-calculating values for reasoning
        m_val = round(self.answer, 10)
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The area of triangle }} MNO \\text{{ is }} {self.area} \\text{{ square units.}} &\\\\"
            f"\\text{{Area}} &= \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\\\"
            f"{self.area} &= \\frac{{1}}{{2}} \\times |{round(self.base, 10)}| \\times \\text{{height}} \\\\"
            f"\\text{{height}} &= \\frac{{2 \\times {self.area}}}{{{abs(round(self.base, 10))}}} = {abs(round(self.height, 10))} \\\\"
            f"\\text{{From the figure, point }} M \\text{{ is at }} ({self.base}, {self.height}) \\text{{ and }} O \\text{{ is at }} (0,0). &\\\\"
            f"\\text{{The gradient }} m \\text{{ of segment }} MO \\text{{ is:}} &\\\\"
            f"m &= \\frac{{y_M - y_O}}{{x_M - x_O}} \\\\"
            f"&= \\frac{{{self.height} - 0}}{{{self.base} - 0}} \\\\"
            f"&= {round(self.height / self.base, 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Coordinates
        ox, oy = 0, 0
        nx, ny = self.base, 0
        mx, my = self.base, self.height
        
        # Set dynamic plot limits
        x_min, x_max = min(0, self.base), max(0, self.base)
        y_min, y_max = min(0, self.height), max(0, self.height)
        ax.set_xlim(x_min - 5, x_max + 5)
        ax.set_ylim(y_min - 5, y_max + 5)
        ax.set_aspect('equal')
        
        # Draw axes
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        ax.grid(True, linestyle=':', alpha=0.5)
        
        # Draw Triangle
        triangle = plt.Polygon([[ox, oy], [nx, ny], [mx, my]], fill=False, edgecolor='black', lw=2.5)
        ax.add_patch(triangle)
        
        # Labels
        ax.text(ox, oy - 1.5, "O(0,0)", fontsize=15, ha='center', fontweight='bold')
        ax.text(nx, ny - 1.5, f"N({self.base}, 0)", fontsize=15, ha='center', fontweight='bold')
        ax.text(mx, my + 1, "M", fontsize=15, ha='center', fontweight='bold')
        
        # Area Annotation
        ax.text(self.base * 0.5, self.height * 0.3, f"Area = {self.area}", 
                fontsize=14, ha='center', fontstyle='italic', bbox=dict(facecolor='white', alpha=0.7))

        

        plt.text(0.95, 0.05, "NOT TO SCALE", transform=ax.transAxes, fontsize=12, ha='right', alpha=0.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat026:
    def __init__(self):
        # Generate points Q and R first to establish a gradient
        self.q_x = rnd.randint(-10, 10)
        self.q_y = rnd.randint(-10, 10)
        
        # Ensure R is distinct from Q to avoid zero-division in gradient
        off_rx = rnd.choice([-1, 1]) * rnd.randint(3, 8)
        off_ry = rnd.choice([-1, 1]) * rnd.randint(3, 8)
        self.r_x = self.q_x + off_rx
        self.r_y = self.q_y + off_ry
        
        # Calculate Gradient of QR
        m = (self.r_y - self.q_y) / (self.r_x - self.q_x)
        
        # Calculate P such that it lies on the same line
        # P(k, y_p)
        self.p_y = self.q_y + (off_ry * 2.5)
        
        # Since m = (y_q - y_p) / (x_q - k)
        # k = x_q - (y_q - y_p) / m
        self.answer = self.q_x - (self.q_y - self.p_y) / m

        self.description = (
            "The diagram shows three collinear points $P$, $Q$, and $R$ on a coordinate grid. "
            "Point $P$ has an unknown $x$-coordinate, $k$. Based on the coordinates shown, "
            "calculate the value of $k$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Gradient of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Since points }} P(k, {self.p_y}), Q({self.q_x}, {self.q_y}), \\text{{ and }} R({self.r_x}, {self.r_y}) \\text{{ are collinear,}} &\\\\"
            f"\\text{{the gradient of segment }} QR \\text{{ must equal the gradient of segment }} PQ. &\\\\"
            f"\\text{{Gradient of }} QR \\text{{ (}} m_{{QR}} \\text{{):}} &\\\\"
            f"m_{{QR}} &= \\frac{{y_R - y_Q}}{{x_R - x_Q}} \\\\"
            f"&= \\frac{{{self.r_y} - ({self.q_y})}}{{{self.r_x} - ({self.q_x})}} \\\\"
            f"&= {round((self.r_y - self.q_y) / (self.r_x - self.q_x), 10)} \\\\"
            f"\\text{{Gradient of }} PQ \\text{{ (}} m_{{PQ}} \\text{{):}} &\\\\"
            f"m_{{PQ}} &= \\frac{{y_Q - y_P}}{{x_Q - x_P}} \\\\"
            f"&= \\frac{{{self.q_y} - ({self.p_y})}}{{{self.q_x} - k}} \\\\"
            f"\\text{{Equating gradients:}} &\\\\"
            f"{round((self.r_y - self.q_y) / (self.r_x - self.q_x), 10)} &= \\frac{{{round(self.q_y - self.p_y, 10)}}}{{{self.q_x} - k}} \\\\"
            f"{self.q_x} - k &= \\frac{{{round(self.q_y - self.p_y, 10)}}}{{{round((self.r_y - self.q_y) / (self.r_x - self.q_x), 10)}}} \\\\"
            f"k &= {self.q_x} - \\left( \\frac{{{round(self.q_y - self.p_y, 10)}}}{{{round((self.r_y - self.q_y) / (self.r_x - self.q_x), 10)}}} \\right) \\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Determine plot limits
        points_x = [self.p_x, self.q_x, self.r_x] if hasattr(self, 'p_x') else [self.answer, self.q_x, self.r_x]
        points_y = [self.p_y, self.q_y, self.r_y]
        
        pad = 5
        ax.set_xlim(min(points_x) - pad, max(points_x) + pad)
        ax.set_ylim(min(points_y) - pad, max(points_y) + pad)
        ax.set_aspect('equal')
        
        # Draw Cartesian axes and grid
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, linestyle=':', alpha=0.6)

        # Coordinates for plotting
        px = self.answer
        py = self.p_y
        qx, qy = self.q_x, self.q_y
        rx, ry = self.r_x, self.r_y

        # Draw the line passing through all points
        m = (ry - qy) / (rx - qx)
        c = qy - m * qx
        x_vals = np.array([min(points_x) - 2, max(points_x) + 2])
        ax.plot(x_vals, m * x_vals + c, color='black', lw=1.5, zorder=1)

        # Plot points
        ax.scatter([px, qx, rx], [py, qy, ry], color='red', s=60, zorder=2)

        # Labels
        # P is shown with unknown k
        ax.text(px, py + 0.8, f"$P(k, {py})$", fontsize=14, ha='center', fontweight='bold')
        ax.text(qx, qy + 0.8, f"$Q({qx}, {qy})$", fontsize=14, ha='center')
        ax.text(rx, ry + 0.8, f"$R({rx}, {ry})$", fontsize=14, ha='center')

        plt.text(0.95, 0.05, "NOT TO SCALE", transform=ax.transAxes, fontsize=12, ha='right', fontweight='bold', alpha=0.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat027:
    def __init__(self):
        # Broad range for x-coordinates to ensure crossing the y-axis
        self.x1 = rnd.randint(-20, -10)
        self.x2 = rnd.randint(10, 20)
        
        # Broad range for y-coordinates
        self.y1 = rnd.randint(-15, 15)
        self.y2 = rnd.randint(-15, 15)
        
        # Prevent zero gradient to avoid division by zero in perpendicular calculation
        if self.y1 == self.y2:
            self.y2 += rnd.choice([-2, -1, 1, 2])
        
        # Gradient m1 of L1
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)
        
        # Gradient m2 of perpendicular line L2 (m1 * m2 = -1)
        self.answer = round(-1 / m1, 2)
        
        self.description = (
            "The diagram shows line $L_1$ passing through points $A$ and $B$. "
            "Line $L_2$ is perpendicular to $L_1$ and intersects the $y$-axis at the same point as $L_1$. "
            "Based on the figure, calculate the gradient of line $L_2$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Gradient of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
        "\\[\\begin{aligned}"
        f"\\text{{Point }} A = ({self.x1}, {self.y1}), \\text{{ Point }} B = ({self.x2}, {self.y2}) &\\\\"
        f"\\text{{Gradient of line }} L_1 \\text{{ (}} m_1 \\text{{):}} &\\\\"
        f"m_1 &= \\frac{{y_2 - y_1}}{{x_2 - x_1}} \\\\"
        f"&= \\frac{{{self.y2} - ({self.y1})}}{{{self.x2} - ({self.x1})}} \\\\"
        f"&= {round((self.y2 - self.y1) / (self.x2 - self.x1), 10)} \\\\"
        f"\\text{{Line }} L_2 \\text{{ is perpendicular to }} L_1 \\text{{, so:}} &\\\\"
        f"m_1 \\times m_2 &= -1 \\\\"
        f"m_2 &= -\\frac{{1}}{{m_1}} \\\\"
        f"&= -\\frac{{1}}{{{round((self.y2 - self.y1) / (self.x2 - self.x1), 10)}}} \\\\"
        f"&= {self.answer}"
        "\\end{aligned}\\]"
    )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Calculate intersection with y-axis (0, c1)
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)
        c1 = self.y1 - m1 * self.x1
        
        # Set tight axis limits to keep the graph "big"
        x_min, x_max = self.x1 - 5, self.x2 + 5
        y_min, y_max = min(self.y1, self.y2, c1) - 5, max(self.y1, self.y2, c1) + 5
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_aspect('equal')
        
        # Axes and Grid
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, linestyle=':', alpha=0.5)
        
        # Draw L1
        x_vals = np.array([x_min, x_max])
        y_vals1 = m1 * x_vals + c1
        ax.plot(x_vals, y_vals1, color='blue', lw=2.5)
        
        # Draw L2 (Perpendicular)
        m2 = -1 / m1
        y_vals2 = m2 * x_vals + c1
        ax.plot(x_vals, y_vals2, color='red', linestyle='--', lw=2.5)
        
        # Labels for A and B
        ax.scatter([self.x1, self.x2], [self.y1, self.y2], color='black', s=80, zorder=5)
        ax.text(self.x1, self.y1 + 1, f"A({self.x1}, {self.y1})", fontsize=14, ha='center', fontweight='bold')
        ax.text(self.x2, self.y2 + 1, f"B({self.x2}, {self.y2})", fontsize=14, ha='center', fontweight='bold')
        
        # FIXED LABELS: Use Axes Coordinates (0 to 1) to prevent "Small Graph" bug
        ax.text(0.05, 0.92, "$L_2$", color='red', transform=ax.transAxes, fontsize=18, fontweight='bold')
        ax.text(0.90, 0.05, "$L_1$", color='blue', transform=ax.transAxes, fontsize=18, fontweight='bold')

        plt.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='right', va='top', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat028:
    def __init__(self):
        # Generate base on a horizontal line (y = y_base)
        x1 = rnd.randint(-20, 0)
        x2 = x1 + rnd.randint(8, 20)
        y_base = rnd.randint(-10, 5)
        
        # Calculate base length
        base = x2 - x1
        
        # Use randrange_float for the height to ensure k is a float
        # k = y_base + height
        height = randrange_float(5.0, 15.0, 0.01)
        self.answer = round(y_base + height, 2)
        
        # Calculated area will be used in the description
        self.area = round(0.5 * base * (self.answer - y_base), 2)
        
        # Peak point C(x_peak, k)
        x_peak = rnd.randint(x1, x2)
        
        self.pts = {
            'A': (x1, y_base),
            'B': (x2, y_base),
            'C': (x_peak, self.answer)
        }

        # Implicit description relying on k in the figure
        self.description = (
            f"The diagram shows triangle $ABC$ plotted on a coordinate grid. "
            f"The area of the triangle is ${self.area}$ square units. "
            f"Based on the figure, find the value of $k$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Length and midpoint"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the figure, the vertices are }} A({self.pts['A'][0]}, {self.pts['A'][1]}), B({self.pts['B'][0]}, {self.pts['B'][1]}), \\text{{ and }} C({self.pts['C'][0]}, k). \\\\"
            f"\\text{{The base of the triangle }} AB \\text{{ is horizontal, as }} y_A = y_B = {self.pts['A'][1]}. \\\\"
            f"\\text{{Length of base }} b &= |x_B - x_A| \\\\"
            f"&= |{self.pts['B'][0]} - ({self.pts['A'][0]})| \\\\"
            f"&= {round(float(self.pts['B'][0] - self.pts['A'][0]), 10)} \\\\"
            f"\\text{{The area of a triangle is given by:}} & \\\\"
            f"\\text{{Area}} &= \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\\\"
            f"{round(float(0.5 * (self.pts['B'][0] - self.pts['A'][0]) * (self.answer - self.pts['A'][1])), 10)} &= \\frac{{1}}{{2}} \\times {round(float(self.pts['B'][0] - self.pts['A'][0]), 10)} \\times h \\\\"
            f"h &= \\frac{{2 \\times {round(float(0.5 * (self.pts['B'][0] - self.pts['A'][0]) * (self.answer - self.pts['A'][1])), 10)}}}{{{round(float(self.pts['B'][0] - self.pts['A'][0]), 10)}}} \\\\"
            f"h &= {round(float(self.answer - self.pts['A'][1]), 10)} \\\\"
            f"\\text{{The height }} h \\text{{ is the vertical distance from the base }} y = {self.pts['A'][1]} \\text{{ to the vertex }} C(x, k): & \\\\"
            f"h &= k - y_A \\\\"
            f"{round(float(self.answer - self.pts['A'][1]), 10)} &= k - ({self.pts['A'][1]}) \\\\"
            f"k &= {round(float(self.answer - self.pts['A'][1]), 10)} + ({self.pts['A'][1]}) \\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        xs = [p[0] for p in self.pts.values()]
        ys = [p[1] for p in self.pts.values()]
        
        # Dynamic axis limits with consistent margins
        margin = 5
        ax.set_xlim(min(xs) - margin, max(xs) + margin)
        ax.set_ylim(min(ys) - margin, max(ys) + margin)
        
        # Grid and Axes
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
        ax.axhline(0, color='black', linewidth=1.2)
        ax.axvline(0, color='black', linewidth=1.2)
        ax.set_aspect('equal')

        # Draw Triangle with fill for better visualization
        tri_x = [self.pts['A'][0], self.pts['B'][0], self.pts['C'][0], self.pts['A'][0]]
        tri_y = [self.pts['A'][1], self.pts['B'][1], self.pts['C'][1], self.pts['A'][1]]
        ax.plot(tri_x, tri_y, color='teal', linewidth=2)
        ax.fill(tri_x, tri_y, color='teal', alpha=0.1)

        # Labels mapping
        labels = {
            'A': f"A({self.pts['A'][0]}, {self.pts['A'][1]})",
            'B': f"B({self.pts['B'][0]}, {self.pts['B'][1]})",
            'C': f"C({self.pts['C'][0]}, k)"
        }

        for label, coord_text in labels.items():
            px, py = self.pts[label]
            ax.plot(px, py, 'ko', markersize=6)
            
            # Smart positioning to avoid overlapping triangle lines
            va = 'bottom' if py >= sum(ys)/3 else 'top'
            ha = 'center'
            
            ax.text(px, py + (0.6 if va == 'bottom' else -0.6), 
                    coord_text, fontsize=14, fontweight='bold', 
                    ha=ha, va=va, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat029:
    def __init__(self):
        # Broad range for Point A
        self.x1 = rnd.randint(-50, 50)
        self.y1 = rnd.randint(-50, 50)
        
        # Use offsets that can be positive or negative to allow for any gradient
        # We use a minimum offset of 20 to ensure the line is long enough to see sub-points
        off_x = rnd.choice([-1, 1]) * rnd.randint(20, 60)
        off_y = rnd.choice([-1, 1]) * rnd.randint(20, 60)
        
        self.x2 = self.x1 + off_x
        self.y2 = self.y1 + off_y
        
        # Coordinate calculations (Deterministic logic)
        # C is midpoint of AB
        cx, cy = (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2
        # D is midpoint of AC
        dx, dy = (self.x1 + cx) / 2, (self.y1 + cy) / 2
        # E is midpoint of DB
        ex, ey = (dx + self.x2) / 2, (dy + self.y2) / 2
        
        # Pre-calculate delta values to keep the f-string clean
        dx_val = round(((self.x1 + (self.x1 + self.x2) / 2) / 2 + self.x2) / 2 - self.x1, 10)
        dy_val = round(((self.y1 + (self.y1 + self.y2) / 2) / 2 + self.y2) / 2 - self.y1, 10)
        
        # Length AE calculation
        dist = math.sqrt((ex - self.x1)**2 + (ey - self.y1)**2)
        
        self.answer = round(dist, 2)
        self.description = (
            "The diagram shows a line segment $AB$. Point $C$ is the midpoint of $AB$, "
            "point $D$ is the midpoint of $AC$, and point $E$ is the midpoint of $DB$. "
            "Based on the coordinates provided in the figure, calculate the length of the segment $AE$."
        )
        self.topic = "Coordinate geometry"
        self.subtopic = "Length and midpoint"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Let }} A = ({self.x1}, {self.y1}) \\text{{ and }} B = ({self.x2}, {self.y2}). &\\\\"
            f"\\text{{Point }} C \\text{{ is the midpoint of }} AB: &\\\\"
            f"C &= \\left( \\frac{{{self.x1} + {self.x2}}}{{2}}, \\frac{{{self.y1} + {self.y2}}}{{2}} \\right)\\\\"
            f"&= ({round((self.x1 + self.x2) / 2, 10)}, {round((self.y1 + self.y2) / 2, 10)})\\\\"
            f"\\text{{Point }} D \\text{{ is the midpoint of }} AC: &\\\\"
            f"D &= \\left( \\frac{{{self.x1} + {round((self.x1 + self.x2) / 2, 10)}}}{{2}}, \\frac{{{self.y1} + {round((self.y1 + self.y2) / 2, 10)}}}{{2}} \\right)\\\\"
            f"&= ({round((self.x1 + (self.x1 + self.x2) / 2) / 2, 10)}, {round((self.y1 + (self.y1 + self.y2) / 2) / 2, 10)})\\\\"
            f"\\text{{Point }} E \\text{{ is the midpoint of }} DB: &\\\\"
            f"E &= \\left( \\frac{{{round((self.x1 + (self.x1 + self.x2) / 2) / 2, 10)} + {self.x2}}}{{2}}, \\frac{{{round((self.y1 + (self.y1 + self.y2) / 2) / 2, 10)} + {self.y2}}}{{2}} \\right)\\\\"
            f"&= ({round(((self.x1 + (self.x1 + self.x2) / 2) / 2 + self.x2) / 2, 10)}, {round(((self.y1 + (self.y1 + self.y2) / 2) / 2 + self.y2) / 2, 10)})\\\\"
            f"\\text{{Length of }} AE \\text{{ is given by the distance formula:}} &\\\\"
            f"AE &= \\sqrt{{(x_E - x_A)^2 + (y_E - y_A)^2}}\\\\"
            f"&= \\sqrt{{({round(((self.x1 + (self.x1 + self.x2) / 2) / 2 + self.x2) / 2, 10)} - ({self.x1}))^2 + ({round(((self.y1 + (self.y1 + self.y2) / 2) / 2 + self.y2) / 2, 10)} - ({self.y1}))^2}}\\\\"
            f"&= \\sqrt{{({dx_val})^2 + ({dy_val})^2}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Determine plot limits based on min/max of coordinates with padding
        all_x = [self.x1, self.x2]
        all_y = [self.y1, self.y2]
        padding = 10
        ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
        ax.set_ylim(min(all_y) - padding, max(all_y) + padding)
        ax.set_aspect('equal')
        
        # Draw the segment AB
        ax.plot([self.x1, self.x2], [self.y1, self.y2], color='black', lw=2, zorder=1)
        
        # Points A and B
        ax.scatter([self.x1, self.x2], [self.y1, self.y2], color='black', s=60, zorder=2)
        
        # Coordinate labels for A and B
        # Dynamic vertical offset so labels don't overlap the line
        va_a = 'bottom' if self.y2 < self.y1 else 'top'
        va_b = 'bottom' if self.y1 < self.y2 else 'top'
        
        ax.text(self.x1, self.y1, f" A({self.x1}, {self.y1}) ", fontsize=14, ha='right', va=va_a)
        ax.text(self.x2, self.y2, f" B({self.x2}, {self.y2}) ", fontsize=14, ha='left', va=va_b)
        
        # Calculate intermediate points for the visual marks
        cx, cy = (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2
        dx, dy = (self.x1 + cx) / 2, (self.y1 + cy) / 2
        ex, ey = (dx + self.x2) / 2, (dy + self.y2) / 2
        
        # Draw and label midpoints C, D, E
        pts_to_draw = {'C': (cx, cy), 'D': (dx, dy), 'E': (ex, ey)}
        for label, pos in pts_to_draw.items():
            ax.scatter(pos[0], pos[1], color='blue', s=40, zorder=3)
            ax.text(pos[0], pos[1] + 1.5, label, fontsize=12, ha='center', color='blue', fontweight='bold')

        ax.grid(True, linestyle=':', alpha=0.5)
        ax.axhline(0, color='black', lw=1, alpha=0.3)
        ax.axvline(0, color='black', lw=1, alpha=0.3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat030:
    def __init__(self):
        # Broad range for Point P
        self.p_x = rnd.randint(-40, 40)
        self.p_y = rnd.randint(-40, 40)
        
        # Ensure Q is distinct and allows for different slopes
        off_x = rnd.choice([-1, 1]) * rnd.randint(15, 50)
        off_y = rnd.choice([-1, 1]) * rnd.randint(15, 50)
        
        self.q_x = self.p_x + off_x
        self.q_y = self.p_y + off_y
        
        # Calculate Midpoint M
        m_x = (self.p_x + self.q_x) / 2
        m_y = (self.p_y + self.q_y) / 2
        
        # Randomly choose target axis
        self.target_axis = rnd.choice(['x-axis', 'y-axis'])
        
        # Distance to x-axis is |y|, distance to y-axis is |x|
        if self.target_axis == 'x-axis':
            self.answer = abs(m_y)
        else:
            self.answer = abs(m_x)
            
        self.description = (
            f"The diagram shows a line segment $PQ$ on a coordinate plane. "
            f"Based on the figure, find the perpendicular distance from the "
            f"midpoint of $PQ$ to the {self.target_axis}."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Length and midpoint"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Let }} P = ({self.p_x}, {self.p_y}) \\text{{ and }} Q = ({self.q_x}, {self.q_y}). &\\\\"
            f"\\text{{The coordinates of the midpoint }} M(x, y) \\text{{ are:}} &\\\\"
            f"x_M &= \\frac{{x_P + x_Q}}{{2}} = \\frac{{{self.p_x} + {self.q_x}}}{{2}}\\\\"
            f"&= {round((self.p_x + self.q_x) / 2, 10)}\\\\"
            f"y_M &= \\frac{{y_P + y_Q}}{{2}} = \\frac{{{self.p_y} + {self.q_y}}}{{2}}\\\\"
            f"&= {round((self.p_y + self.q_y) / 2, 10)}\\\\"
            f"\\text{{The perpendicular distance from a point }} (x, y) \\text{{ to the {self.target_axis} is:}} &\\\\"
            f"d &= {'|x_M|' if self.target_axis == 'y-axis' else '|y_M|'}\\\\"
            f"&= {'|' + str(round((self.p_x + self.q_x) / 2, 10)) + '|' if self.target_axis == 'y-axis' else '|' + str(round((self.p_y + self.q_y) / 2, 10)) + '|'}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Plot limits based on endpoints with padding
        all_x = [self.p_x, self.q_x]
        all_y = [self.p_y, self.q_y]
        pad = 10
        ax.set_xlim(min(all_x) - pad, max(all_x) + pad)
        ax.set_ylim(min(all_y) - pad, max(all_y) + pad)
        ax.set_aspect('equal')
        
        # Draw axes and grid
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        ax.grid(True, linestyle=':', alpha=0.6)
        
        # Plot segment PQ
        ax.plot([self.p_x, self.q_x], [self.p_y, self.q_y], color='black', lw=2.5, zorder=1)
        ax.scatter([self.p_x, self.q_x], [self.p_y, self.q_y], color='black', s=80, zorder=2)
        
        # Coordinate labels with dynamic positioning
        va_p = 'bottom' if self.q_y < self.p_y else 'top'
        va_q = 'bottom' if self.p_y < self.q_y else 'top'
        
        ax.text(self.p_x, self.p_y, f" P({self.p_x}, {self.p_y}) ", fontsize=14, ha='right', va=va_p)
        ax.text(self.q_x, self.q_y, f" Q({self.q_x}, {self.q_y}) ", fontsize=14, ha='left', va=va_q)
        
        # Plot midpoint M
        m_x, m_y = (self.p_x + self.q_x) / 2, (self.p_y + self.q_y) / 2
        ax.scatter(m_x, m_y, color='red', s=60, zorder=3)
        ax.text(m_x, m_y + 1.5, "M", color='red', fontsize=14, fontweight='bold', ha='center')

        plt.text(0.95, 0.05, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='right', va='bottom', fontweight='bold', alpha=0.7)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat031:
    def __init__(self):
        # self.answer must be numeric
        # Use randrange_float for the gradient to ensure c is a float
        self.m = round(randrange_float(-3.0, 3.0, 0.01), 2)
        if self.m == 0: self.m = 1.25 # Avoid zero gradient
        
        # Random integer point to keep the visual grid intersection clean
        self.x1 = rnd.randint(-6, 6)
        if self.x1 == 0: self.x1 = 2 # Avoid x=0 to ensure they don't just see 'c'
        self.y1 = rnd.randint(-6, 6)
        
        # Calculate c: y = mx + c => c = y1 - (m * x1)
        self.c = round(self.y1 - (self.m * self.x1), 2)
        
        self.answer = self.c

        # Description is now implicit as requested
        self.description = (
            "The figure shows the graph of a straight line. "
            "Based on the information provided in the diagram, find the value of the $y$-intercept, $c$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Equations of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the figure, the gradient is: }} m &= {round(self.m, 10)}\\\\"
            f"\\text{{The line passes through the point: }} (x_1, y_1) &= ({self.x1}, {self.y1})\\\\"
            "\\text{{The equation of a straight line is: }} y &= mx + c\\\\"
            "\\text{{Substitute the known values to solve for }} c: &\\\\"
            f"{self.y1} &= ({round(self.m, 10)})({self.x1}) + c\\\\"
            f"{self.y1} &= {round(self.m * self.x1, 10)} + c\\\\"
            f"c &= {self.y1} - ({round(self.m * self.x1, 10)})\\\\"
            f"c &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Set dynamic bounds based on the point and intercept
        padding = 5
        x_min, x_max = -10, 10
        y_min, y_max = min(self.y1, self.c) - padding, max(self.y1, self.c) + padding

        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Configure axes and grid to standard IGCSE conventions
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.set_aspect('equal')

        # Generate the line for the figure
        x_plot = np.array([x_min, x_max])
        y_plot = self.m * x_plot + self.c
        
        # 
        ax.plot(x_plot, y_plot, color='blue', lw=2)
        
        # Mark and label the point implicitly
        ax.scatter(self.x1, self.y1, color='red', s=60, zorder=5)
        ax.text(self.x1 + 0.3, self.y1 + 0.3, f'$({self.x1}, {self.y1})$', 
                fontsize=14, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', alpha=0.9))

        # Add the equation to the figure implicitly
        # Placing it at a slight offset from the center of the line
        text_x = (x_min + x_max) / 4
        text_y = self.m * text_x + self.c + 1.5
        ax.text(text_x, text_y, f'$y = {self.m}x + c$', fontsize=16, 
                color='blue', rotation=np.degrees(np.arctan(self.m)), ha='center')

        ax.set_xlabel('$x$', loc='right', fontsize=14)
        ax.set_ylabel('$y$', loc='top', rotation=0, fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat032:
    def __init__(self):
        # Randomized intercepts (ensuring non-zero to avoid vertical/horizontal lines)
        self.x_int = rnd.choice([i for i in range(-6, 7) if i != 0])
        self.y_int = rnd.choice([i for i in range(-6, 7) if i != 0])
        
        a = self.x_int
        b = self.y_int
        
        self.m = Fraction(-b, a)
        self.c = b
        
        # Formatting the equation string
        m_num, m_den = self.m.numerator, self.m.denominator
        if m_den == 1:
            m_str = f"{m_num}" if m_num != 1 else ""
            m_str = f"-{abs(m_num)}" if m_num == -1 else m_str
        else:
            m_str = f"{m_num}/{m_den}"
            
        sign = "+" if self.c > 0 else "-"
        self.answer = f"y = {m_str}x {sign} {abs(self.c)}"
        
        self.description = f"The line L is shown on the grid. Find the equation of line L in the form y = mx + c."
        self.topic = "Coordinate geometry"
        self.subtopic = "Equations of linear graphs"
        self.source = "Adapted from 2025-specimen-paper-1"
        self.curriculum = "IGCSE"
        self.question_type = "Free-form"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the intercepts from the graph:}} &\\\\"
            f"\\text{{x-intercept}} &= ({self.x_int}, 0)\\\\"
            f"\\text{{y-intercept}} &= (0, {self.y_int})\\\\"
            "\\text{The gradient } m \\text{ is given by:} &\\\\"
            "m &= \\frac{y_2 - y_1}{x_2 - x_1}\\\\"
            f"&= \\frac{{{self.y_int} - 0}}{{0 - ({self.x_int})}}\\\\"
            f"&= {m_str}\\\\"
            "\\text{The y-intercept } c \\text{ is the value where the line crosses the y-axis:} &\\\\"
            f"c &= {self.y_int}\\\\"
            "\\text{Substitute } m \\text{ and } c \\text{ into the equation } y = mx + c: &\\\\"
            f"{self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Intercepts and line parameters
        a = float(self.x_int)
        b = float(self.y_int)
        m = float(self.m)
        c = float(self.c)

        xmin, xmax = -7, 7

        # Draw axes (x and y) through origin
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)

        # Annotate intercepts (offset so text doesn't overlap points)
        ax.annotate(f'({int(a) if a.is_integer() else a}, 0)', xy=(a, 0), xytext=(6, -12),
                    textcoords='offset points', fontsize=10)
        ax.annotate(f'(0, {int(b) if b.is_integer() else b})', xy=(0, b), xytext=(6, 6),
                    textcoords='offset points', fontsize=10)

        # Configure ticks and limits so intercepts are clearly visible
        ax.set_xticks(list(range(-7, 8)))
        ax.set_yticks(list(range(-7, 8)))
        ax.set_xlim(xmin - 0.5, xmax + 0.5)
        ax.set_ylim(-7.5, 7.5)

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        # Draw the line
        x0, x1 = ax.get_xlim()
        ax.plot([x0, x1], [m*x0 + c, m*x1 + c], color='black', linewidth=1)
        
        # Mark intercept points clearly
        ax.plot([a], [0], marker='o', color='red')
        ax.plot([0], [b], marker='o', color='red')

        ax.grid(which='major', linestyle=':', linewidth=0.5)

        # Save image
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close(fig)

class Mat033:
    def __init__(self):
        # Determine if intersecting with x=k or y=k
        self.is_vertical_k = rnd.choice([True, False])
        
        # Line coefficients for ax + by = c form
        self.a = rnd.randint(-8, 8)
        if self.a == 0: self.a = 3
        self.b = rnd.randint(-8, 8)
        if self.b == 0: self.b = -2
        
        # Generate float c to avoid 'spoiling' the y-intercept visually
        self.c = round(randrange_float(-10.0, 10.0, 0.01), 2)
        
        # Intersecting constant k
        self.k = rnd.randint(-5, 5)

        if self.is_vertical_k:
            # Intersection with x = k: a(k) + by = c => y = (c - ak) / b
            self.answer = round((self.c - self.a * self.k) / self.b, 2)
            self.find_coord = "y"
            self.line_m_eq = f"x = {self.k}"
            self.label_fmt = f"({self.k}, ?)"
        else:
            # Intersection with y = k: ax + b(k) = c => x = (c - bk) / a
            self.answer = round((self.c - self.b * self.k) / self.a, 2)
            self.find_coord = "x"
            self.line_m_eq = f"y = {self.k}"
            self.label_fmt = f"(?, {self.k})"

        self.description = (
            f"The figure displays a straight line $L$ and a dashed line $M$ with the equation ${self.line_m_eq}$. "
            f"As shown in the figure, find the ${self.find_coord}$-coordinate of the intersection point."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Equations of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The equation of line }} L \\text{{ is:}} &\\\\"
            f"{fmt_poly(self.a, 'x', True)}{fmt_poly(self.b, 'y')} &= {round(self.c, 10)}\\\\"
            f"\\text{{The equation of line }} M \\text{{ is:}} &\\\\"
            f"{self.line_m_eq} \\\\"
            "\\text{{To find the intersection, substitute the value from line }} M \\text{{ into line }} L: &\\\\"
            + (
                f"\\text{{Substitute }} x = {self.k} \\text{{ into the equation:}} \\\\"
                f"{self.a}({self.k}) + {self.b}y &= {round(self.c, 10)} \\\\"
                f"{round(self.a * self.k, 10)} + {self.b}y &= {round(self.c, 10)} \\\\"
                f"{self.b}y &= {round(self.c, 10)} - ({round(self.a * self.k, 10)}) \\\\"
                f"{self.b}y &= {round(self.c - self.a * self.k, 10)} \\\\"
                f"y &= \\frac{{{round(self.c - self.a * self.k, 10)}}}{{{self.b}}} \\\\"
                f"y &= {self.answer}"
                if self.is_vertical_k else
                f"\\text{{Substitute }} y = {self.k} \\text{{ into the equation:}} \\\\"
                f"{self.a}x + {self.b}({self.k}) &= {round(self.c, 10)} \\\\"
                f"{self.a}x + {round(self.b * self.k, 10)} &= {round(self.c, 10)} \\\\"
                f"{self.a}x &= {round(self.c, 10)} - ({round(self.b * self.k, 10)}) \\\\"
                f"{self.a}x &= {round(self.c - self.b * self.k, 10)} \\\\"
                f"x &= \\frac{{{round(self.c - self.b * self.k, 10)}}}{{{self.a}}} \\\\"
                f"x &= {self.answer}"
            ) +
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Calculate intersection for plotting
        inter_x = self.k if self.is_vertical_k else self.answer
        inter_y = self.answer if self.is_vertical_k else self.k
        
        padding = 6
        x_min, x_max = -12, 12
        y_min, y_max = min(inter_y, self.c/self.b if self.b != 0 else 0) - padding, max(inter_y, self.c/self.b if self.b != 0 else 0) + padding

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.set_aspect('equal')

        # Line L plotting (ax + by = c)
        if self.b != 0:
            x_vals = np.array([x_min, x_max])
            y_vals = (self.c - self.a * x_vals) / self.b
            ax.plot(x_vals, y_vals, color='blue', lw=2, label='$L$')
        else:
            ax.axvline(self.c / self.a, color='blue', lw=2, label='$L$')

        # Dashed line M plotting
        if self.is_vertical_k:
            ax.axvline(self.k, color='red', linestyle='--', lw=2)
        else:
            ax.axhline(self.k, color='red', linestyle='--', lw=2)

        # Mark intersection
        ax.scatter(inter_x, inter_y, color='green', marker='x', s=100, zorder=6)
        ax.text(inter_x + 0.4, inter_y + 0.4, f'${self.label_fmt}$', color='green', 
                fontsize=14, fontweight='bold', bbox=dict(facecolor='white', edgecolor='green', alpha=0.9))

        # Implicit Equation Label on Line L
        eq_label = f"${fmt_poly(self.a, 'x', True)}{fmt_poly(self.b, 'y')} = {self.c}$"
        # Determine placement based on gradient
        grad = -self.a / self.b if self.b != 0 else 10
        text_x = (x_min + x_max) / 3
        text_y = (self.c - self.a * text_x) / self.b if self.b != 0 else 2
        
        ax.text(text_x, text_y + 1, eq_label, fontsize=14, color='blue', 
                rotation=np.degrees(np.arctan(grad)) if self.b != 0 else 90, ha='center', weight='bold')

        ax.set_xlabel('$x$', loc='right')
        ax.set_ylabel('$y$', loc='top', rotation=0)
        plt.text(0.95, 0.02, "NOT TO SCALE", transform=ax.transAxes, fontsize=10, ha='right', weight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat034:
    def __init__(self):
        # Deterministic logic for variations
        self.m = round(randrange_float(-3, 3, 0.01), 2)
        if abs(self.m) < 0.2: self.m = 1.5 # Avoid near-horizontal lines
        
        self.c1 = rnd.randint(-5, 5)
        self.c2 = rnd.randint(-5, 5)
        if abs(self.c1 - self.c2) < 2: self.c2 += 3 # Ensure visual separation
            
        # Point on L2 to show in figure
        self.x_p = rnd.randint(-4, 4)
        self.y_p = round(self.m * self.x_p + self.c2, 2)
        
        # Decide question type: find y given x, or find x given y
        self.q_type = rnd.choice(["find_y", "find_x"])
        self.const_val = rnd.randint(-10, 10)
        
        # Ensure the target value isn't too close to the provided point P
        while abs(self.const_val - (self.x_p if self.q_type == "find_y" else self.y_p)) < 2:
            self.const_val = rnd.randint(-10, 10)

        if self.q_type == "find_y":
            # Finding y given x = k
            self.target_var = "y"
            self.given_var = "x"
            self.answer = round(self.m * (self.const_val - self.x_p) + self.y_p, 2)
            self.calc_step = f"y &= {round(self.m, 10)}({self.const_val} - ({round(self.x_p, 10)})) + {round(self.y_p, 10)}"
        else:
            # Finding x given y = k
            self.target_var = "x"
            self.given_var = "y"
            self.answer = round((self.const_val - self.y_p) / self.m + self.x_p, 2)
            self.calc_step = (
                f"{self.const_val} - {round(self.y_p, 10)} &= {round(self.m, 10)}(x - {round(self.x_p, 10)}) \\\\"
                f"{round(self.const_val - self.y_p, 10)} &= {round(self.m, 10)}(x - {round(self.x_p, 10)}) \\\\"
                f"x - {round(self.x_p, 10)} &= {round((self.const_val - self.y_p)/self.m, 10)} \\\\"
                f"x &= {self.answer}"
            )

        self.description = (
            f"The figure shows two parallel lines, $L_1$ and $L_2$. "
            f"Based on the information provided in the diagram, find the {self.target_var}-coordinate "
            f"of the point on $L_2$ where the {self.given_var}-coordinate is {self.const_val}."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Parallel lines"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The equation of line }} L_1 \\text{{ is }} y &= {round(self.m, 10)}x {fmt_poly(round(self.c1, 10), '')} \\\\"
            f"\\text{{Since }} L_2 \\parallel L_1, \\text{{ they have the same gradient:}} & \\\\"
            f"m_2 &= m_1 = {round(self.m, 10)} \\\\"
            f"\\text{{Using the point }} P({round(self.x_p, 10)}, {round(self.y_p, 10)}) \\text{{ on }} L_2, \\text{{ the equation in point-slope form is:}} & \\\\"
            f"y - y_p &= m_2(x - x_p) \\\\"
            f"y - ({round(self.y_p, 10)}) &= {round(self.m, 10)}(x - ({round(self.x_p, 10)})) \\\\"
            f"\\text{{Substitute the given value }} {self.given_var} = {self.const_val}: & \\\\"
            f"{self.calc_step}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        limit = 15
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        ax.grid(True, which='both', linestyle='--', alpha=0.6)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        x_plot = np.linspace(-limit, limit, 100)
        
        # Helper logic for dynamic text placement
        # Find a x-value that is guaranteed to be within the visible plot
        x_text = limit * 0.6 if self.m <= 0 else -limit * 0.8
        
        # Plot Line 1 (Blue)
        y1_plot = self.m * x_plot + self.c1
        ax.plot(x_plot, y1_plot, color='blue', lw=2)
        
        # Position equation label dynamically along the line
        y_text1 = self.m * x_text + self.c1
        # Clamp label within visible area
        y_text1 = max(-limit+2, min(limit-2, y_text1))
        
        eq_text = f"$y = {self.m}x {fmt_poly(self.c1, '')}$"
        ax.text(x_text, y_text1, eq_text, fontsize=16, color='blue', 
                fontweight='bold', bbox=dict(facecolor='white', edgecolor='blue', alpha=0.9),
                ha='center', va='center')

        # Plot Line 2 (Red)
        y2_plot = self.m * x_plot + self.c2
        ax.plot(x_plot, y2_plot, color='red', lw=2)
        
        # Plot and Label the known point
        ax.plot(self.x_p, self.y_p, 'ko', markersize=8, zorder=5)
        
        # Offset the point label based on the gradient to avoid overlapping the line
        offset_x = 1.5 if self.m < 0 else -1.5
        offset_y = 1.5
        
        ax.text(self.x_p + offset_x, self.y_p + offset_y, f"({self.x_p}, {self.y_p})", 
                fontsize=16, color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.9),
                ha='center' if abs(offset_x) < 0.1 else ('left' if offset_x > 0 else 'right'))

        # Dynamic Line Identifiers (L1, L2)
        # Place at the very edge of the plot
        for line_name, c_val, color in [('$L_1$', self.c1, 'blue'), ('$L_2$', self.c2, 'red')]:
            # Calculate where the line exits the top or bottom of the plot
            edge_x = (limit*0.9 if self.m > 0 else -limit*0.9)
            edge_y = self.m * edge_x + c_val
            # Ensure identifiers stay within the box
            edge_y = max(-limit+1, min(limit-1, edge_y))
            
            ax.text(edge_x, edge_y, line_name, fontsize=22, color=color, 
                    fontweight='bold', ha='center', va='bottom')

        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat035:
    def __init__(self):
        # Deterministic logic for variations
        self.m = round(randrange_float(-4, 4, 0.01), 2)
        if abs(self.m) < 0.2: self.m = 1.2  # Avoid near-horizontal lines
        
        # Line k: Established by two points
        self.x1 = rnd.randint(-9, -2)
        self.y1 = rnd.randint(-9, 9)
        self.x2 = self.x1 + rnd.randint(3, 7)
        self.y2 = round(self.y1 + self.m * (self.x2 - self.x1), 2)
        
        # Line m: Parallel to k (same gradient)
        self.c2 = round(randrange_float(-6, 6, 0.01), 2)
        if abs(self.c2 - (self.y1 - self.m * self.x1)) < 3: 
            self.c2 += 5
            
        # Determine question type: find x or find y
        self.q_type = rnd.choice(["find_x", "find_y"])
        self.const_val = round(randrange_float(-10, 10, 0.01), 2)
        
        if self.q_type == "find_y":
            self.target_var, self.given_var = "y", "x"
            self.answer = round(self.m * self.const_val + self.c2, 2)
            self.calc_step = f"y &= {round(self.m, 10)}({self.const_val}) + {round(self.c2, 10)}"
        else:
            self.target_var, self.given_var = "x", "y"
            self.answer = round((self.const_val - self.c2) / self.m, 2)
            self.calc_step = (
                f"{self.const_val} &= {round(self.m, 10)}x + {round(self.c2, 10)} \\\\"
                f"{round(self.m, 10)}x &= {round(self.const_val - self.c2, 10)} \\\\"
                f"x &= {self.answer}"
            )

        # Metadata properties in required order
        self.description = (
            f"The figure shows two lines, line $k$ and line $m$, where line $m$ is parallel to line $k$. "
            f"Based on the coordinates and information provided in the diagram, find the {self.target_var}-coordinate "
            f"on line $m$ when the {self.given_var}-coordinate is {self.const_val}."
        )
        self.topic = "Coordinate geometry"
        self.subtopic = "Parallel lines"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Find the gradient of line }} k \\text{{ using points }} ({self.x1}, {self.y1}) \\text{{ and }} ({self.x2}, {round(self.y2, 10)}): &\\\\"
            f"m_k &= \\frac{{y_2 - y_1}}{{x_2 - x_1}} \\\\"
            f"&= \\frac{{{round(self.y2, 10)} - ({self.y1})}}{{{self.x2} - ({self.x1})}} \\\\"
            f"&= {round(self.m, 10)} \\\\"
            f"\\text{{Since line }} m \\parallel k, \\text{{ they have the same gradient:}} &\\\\"
            f"m_m &= m_k = {round(self.m, 10)} \\\\"
            f"\\text{{Line }} m \\text{{ has y-intercept }} (0, {round(self.c2, 10)}), \\text{{ so its equation is:}} &\\\\"
            f"y &= m_m x + c \\\\"
            f"y &= {round(self.m, 10)}x + {round(self.c2, 10)} \\\\"
            f"\\text{{Substitute the given value }} {self.given_var} = {self.const_val} \\text{{ into the equation:}} &\\\\"
            f"{self.calc_step} \\\\"
            f"{self.target_var} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Logic for creating the Cartesian coordinate system
        fig, ax = plt.subplots(figsize=(10, 10))
        limit = 15
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        # Grid and axes setup
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        
        x_plot = np.linspace(-limit, limit, 100)
        
        # Plot Line k (Blue)
        y_k = self.y1 + self.m * (x_plot - self.x1)
        ax.plot(x_plot, y_k, color='blue', lw=2.5)
        
        # Implicit markers for k: Label points
        ax.plot([self.x1, self.x2], [self.y1, self.y2], 'bo', markersize=8)
        off = 0.8
        ax.text(self.x1 - off, self.y1 + off, f"({self.x1}, {self.y1})", color='blue', 
                fontsize=14, fontweight='bold', ha='right', bbox=dict(facecolor='white', alpha=0.8))
        ax.text(self.x2 + off, self.y2 - off, f"({self.x2}, {self.y2})", color='blue', 
                fontsize=14, fontweight='bold', ha='left', bbox=dict(facecolor='white', alpha=0.8))
        ax.text(self.x1, self.y1 + 3, "$k$", fontsize=22, color='blue', fontweight='bold')

        # Plot Line m (Red)
        y_m = self.m * x_plot + self.c2
        ax.plot(x_plot, y_m, color='red', lw=2.5)
        
        # Implicit marker for m: Label y-intercept
        ax.plot(0, self.c2, 'ro', markersize=8)
        ax.text(0.8, self.c2, f"(0, {self.c2})", color='red', 
                fontsize=14, fontweight='bold', ha='left', bbox=dict(facecolor='white', alpha=0.8))
        ax.text(0.5, self.c2 + 3, "$m$", fontsize=22, color='red', fontweight='bold')

        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat036:
    def __init__(self):
        # Gradient of line L (m1) - kept steep for visual clarity
        self.m1 = round(randrange_float(-3.0, 3.0, 0.2), 1)
        if abs(self.m1) < 0.5: self.m1 = 2.0 
        
        self.c1 = round(randrange_float(-3.0, 3.0, 0.5), 1)
        
        # Point P(px, py) on line M
        self.px = round(randrange_float(-5.0, 5.0, 0.5), 1)
        self.py = round(randrange_float(-5.0, 5.0, 0.5), 1)
        
        # Perpendicular Gradient (m2 = -1/m1) and Intercept (c2)
        self.m2 = -1 / self.m1
        self.c2 = self.py - (self.m2 * self.px)
        
        # Question Logic (Intersection with x=k or y=k)
        self.q_type = rnd.choice(["find_x", "find_y"])
        # Random integer constant for the intersection line
        self.const_val = rnd.randint(-6, 6)
        
        if self.q_type == "find_y":
            # Intersection with vertical line x = k
            self.answer = round(self.m2 * self.const_val + self.c2, 2)
            self.find_var, self.given_line = "y", f"x = {self.const_val}"
        else:
            # Intersection with horizontal line y = k
            self.answer = round((self.const_val - self.c2) / self.m2, 2)
            self.find_var, self.given_line = "x", f"y = {self.const_val}"

        # Fully implicit description relying on visual evidence
        self.description = (
            f"As shown in the diagram, line $M$ is perpendicular to line $L$. "
            f"Find the {self.find_var}-coordinate of the point where line $M$ intersects the line ${self.given_line}$."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Equations of linear graphs"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the gradient of line }} L, m_1: &\\\\"
            f"m_1 &= {round(self.m1, 10)}\\\\"
            f"\\text{{The gradient of a perpendicular line }} m_2 \\text{{ satisfies }} m_1 \\times m_2 = -1: &\\\\"
            f"m_2 &= -\\frac{{1}}{{{round(self.m1, 10)}}} = {round(self.m2, 10)}\\\\"
            f"\\text{{Use the point }} P({round(self.px, 10)}, {round(self.py, 10)}) \\text{{ and }} m_2 \\text{{ in the equation }} y - y_1 = m_2(x - x_1): &\\\\"
            f"y - {round(self.py, 10)} &= {round(self.m2, 10)}(x - ({round(self.px, 10)}))\\\\"
            f"y &= {round(self.m2, 10)}x + {round(self.c2, 10)}\\\\"
            f"\\text{{Substitute the given line equation }} {self.given_line} \\text{{ into the equation of line }} M: &\\\\"
            + (
                f"{self.find_var} &= {round(self.m2, 10)}({round(self.const_val, 10)}) + {round(self.c2, 10)}\\\\"
                if self.q_type == "find_y" else
                f"{round(self.const_val, 10)} &= {round(self.m2, 10)}x + {round(self.c2, 10)}\\\\"
                f"{round(self.m2, 10)}x &= {round(self.const_val - self.c2, 10)}\\\\"
            ) +
            f"{self.find_var} &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        limit = 10
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        # Grid and axes per Cambridge IGCSE conventions
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        x_plot = np.linspace(-limit, limit, 100)
        
        # --- Line L (Blue) ---
        y_l = self.m1 * x_plot + self.c1
        ax.plot(x_plot, y_l, color='blue', lw=2.5)
        
        # Dynamic placement for L label at the edge of the visible area
        label_x_l = -limit + 1.5 if self.m1 > 0 else limit - 1.5
        label_y_l = self.m1 * label_x_l + self.c1
        label_y_l = max(-limit + 1, min(limit - 1, label_y_l)) # Clamping
        
        ax.text(label_x_l, label_y_l, '$L$', color='blue', fontsize=24, 
                fontweight='bold', ha='center', va='bottom')
        
        # --- Line M (Red) ---
        y_m = self.m2 * x_plot + self.c2
        ax.plot(x_plot, y_m, color='red', lw=2.5)
        
        # Dynamic placement for M label
        label_x_m = limit - 1.5 if self.m2 > 0 else -limit + 1.5
        label_y_m = self.m2 * label_x_m + self.c2
        label_y_m = max(-limit + 1, min(limit - 1, label_y_m))
        
        ax.text(label_x_m, label_y_m, '$M$', color='red', fontsize=24, 
                fontweight='bold', ha='center', va='bottom')
        
        # --- Point P Marking ---
        ax.plot(self.px, self.py, 'ko', markersize=8, zorder=5)
        
        # Offset logic: Place label 'away' from both lines based on m2
        # If m2 is negative, place top-right or bottom-left
        dx = 1.0 if self.m2 < 0 else -1.0
        dy = 1.0
        
        ax.text(self.px + dx, self.py + dy, f"$P({self.px}, {self.py})$", 
                fontsize=16, fontweight='bold', ha='center' if dx==0 else ('left' if dx>0 else 'right'),
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.8))

        # --- Line L Equation Label ---
        # Position equation text at a predictable spot that doesn't overlap P
        eq_x = -limit * 0.7 if self.m1 < 0 else limit * 0.3
        eq_y = self.m1 * eq_x + self.c1
        eq_y = max(-limit + 2, min(limit - 2, eq_y))
        
        ax.text(eq_x, eq_y, f"$y = {self.m1}x {fmt_poly(self.c1, '')}$", 
                color='blue', fontsize=18, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='blue', alpha=0.9), ha='center')

        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

    def _draw_perpendicular_square(self, ax, x0, y0, m1, m2, size=0.6):
        """Draws a geometrically accurate perpendicular square at the intersection."""
        ang1 = np.arctan(m1)
        ang2 = np.arctan(m2)
        
        # Vertices of the square relative to the intersection point
        v1 = [x0 + size * np.cos(ang1), y0 + size * np.sin(ang1)]
        v2 = [v1[0] + size * np.cos(ang2), v1[1] + size * np.sin(ang2)]
        v3 = [x0 + size * np.cos(ang2), y0 + size * np.sin(ang2)]
        
        ax.plot([v1[0], v2[0], v3[0]], [v1[1], v2[1], v3[1]], color='black', lw=1.2, zorder=4)
        
class Mat037:
    def __init__(self):
        # Gradient of line L (m1). Varied significantly.
        self.m1 = round(randrange_float(-4.0, 4.0, 0.01), 2)
        if abs(self.m1) < 0.5: self.m1 = 2.0 
        
        # Equation form: y = m1 * x + c1. c1 is y-intercept of L.
        self.c1 = rnd.randint(-5, 5)
        
        # Two points on L for implicit visual data.
        self.x1_L = rnd.randint(-4, 0)
        self.y1_L = round(self.m1 * self.x1_L + self.c1, 2)
        self.x2_L = self.x1_L + rnd.randint(2, 5)
        self.y2_L = round(self.m1 * self.x2_L + self.c1, 2)
        
        # Perpendicular Gradient (m2 = -1/m1)
        self.m2 = round(-1 / self.m1, 2)
        
        # Point P(px, py) on line P
        self.px = rnd.randint(-5, 5)
        self.py = rnd.randint(-5, 5)
        
        # Target logic: Vary asking for x or y
        self.q_type = rnd.choice(["find_y", "find_x"])
        self.const_val = rnd.randint(-10, 10)
        
        # Ensure target is not too close to point P
        while abs(self.const_val - (self.px if self.q_type == "find_y" else self.py)) < 2:
            self.const_val = rnd.randint(-10, 10)

        # Calculation logic
        # Equation of P: y - py = m2 * (x - px)
        if self.q_type == "find_y":
            self.target_var, self.given_var = "y", "x"
            self.answer = round(self.m2 * (self.const_val - self.px) + self.py, 2)
            calc_step = f"y &= {round(self.m2, 10)}({self.const_val} - ({self.px})) + {self.py}"
        else:
            self.target_var, self.given_var = "x", "y"
            self.answer = round((self.const_val - self.py) / self.m2 + self.px, 2)
            calc_step = (
                f"{self.const_val} - {self.py} &= {round(self.m2, 10)}(x - {self.px}) \\\\"
                f"{round(self.const_val - self.py, 10)} &= {round(self.m2, 10)}(x - {self.px}) \\\\"
                f"x - {self.px} &= {round((self.const_val - self.py)/self.m2, 10)} \\\\"
                f"x &= {self.answer}"
            )

        self.description = (
            f"The figure shows line $L$ and line $P$, where line $P$ is perpendicular to line $L$. "
            f"Based on the coordinates provided in the diagram, find the {self.target_var}-coordinate "
            f"of the point on line $P$ where the {self.given_var}-coordinate is {self.const_val}."
        )
        
        self.topic = "Coordinate geometry"
        self.subtopic = "Perpendicular lines"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Find the gradient of line }} L, m_1, \\text{{ using points }} ({self.x1_L}, {self.y1_L}) \\text{{ and }} ({self.x2_L}, {self.y2_L}): &\\\\"
            f"m_1 &= \\frac{{{self.y2_L} - ({self.y1_L})}}{{{self.x2_L} - ({self.x1_L})}} = {round(self.m1, 10)} \\\\"
            f"\\text{{Since }} P \\perp L, \\text{{ the gradient of }} P, m_2, \\text{{ satisfies }} m_1 \\times m_2 = -1: &\\\\"
            f"m_2 &= -\\frac{{1}}{{{round(self.m1, 10)}}} = {round(self.m2, 10)} \\\\"
            f"\\text{{Using point }} ({self.px}, {self.py}) \\text{{ on line }} P, \\text{{ the point-slope equation is:}} &\\\\"
            f"y - y_p &= m_2(x - x_p) \\\\"
            f"y - {self.py} &= {round(self.m2, 10)}(x - {self.px}) \\\\"
            f"\\text{{Substitute the given value }} {self.given_var} = {self.const_val}: &\\\\"
            f"{calc_step}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        limit = 15
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        x_plot = np.linspace(-limit, limit, 100)
        
        # Line L (Blue)
        y_l = self.m1 * x_plot + self.c1
        ax.plot(x_plot, y_l, color='blue', lw=2.5)
        
        # Label points for L
        ax.plot([self.x1_L, self.x2_L], [self.y1_L, self.y2_L], 'bo', markersize=8)
        ax.text(self.x1_L + 0.5, self.y1_L + 0.5, f"({self.x1_L}, {self.y1_L})", color='blue', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))
        ax.text(self.x2_L + 0.5, self.y2_L + 0.5, f"({self.x2_L}, {self.y2_L})", color='blue', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))

        # Line P (Red)
        c2 = self.py - self.m2 * self.px
        y_p = self.m2 * x_plot + c2
        ax.plot(x_plot, y_p, color='red', lw=2.5)
        
        # Label point for P
        ax.plot(self.px, self.py, 'ro', markersize=8, zorder=5)
        
        # Dynamic placement of P label
        dx = 1.0 if self.m2 < 0 else -1.0
        ax.text(self.px + dx, self.py + 1, f"({self.px}, {self.py})", color='red', fontsize=12, fontweight='bold', ha='center' if dx==0 else ('left' if dx>0 else 'right'), bbox=dict(facecolor='white', alpha=0.8))

        # Intersection square for perpendicularity
        ix = (c2 - self.c1) / (self.m1 - self.m2)
        iy = self.m1 * ix + self.c1
        if -limit < ix < limit and -limit < iy < limit:
            size = 0.7
            v1 = np.array([1, self.m1]) / np.sqrt(1 + self.m1**2)
            v2 = np.array([1, self.m2]) / np.sqrt(1 + self.m2**2)
            p1 = np.array([ix, iy]) + size * v1
            p2 = p1 + size * v2
            p3 = np.array([ix, iy]) + size * v2
            ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color='black', lw=1.5)

        # Labels L and P at edges
        for line_name, m, c, color in [('$L$', self.m1, self.c1, 'blue'), ('$P$', self.m2, c2, 'red')]:
            edge_x = limit * 0.8 if m > 0 else -limit * 0.8
            edge_y = m * edge_x + c
            edge_y = max(-limit + 1, min(limit - 1, edge_y))
            ax.text(edge_x, edge_y, line_name, fontsize=24, color=color, fontweight='bold', ha='center', va='bottom')

        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat038:
    def __init__(self):
        # Gradient for line k (m_k). Varied for visual clarity.
        self.m_k = round(randrange_float(-3.0, 3.0, 0.01), 2)
        if abs(self.m_k) < 0.4: self.m_k = 1.5
        
        # Equation of line k: y = m_k * x + c_k
        self.c_k = rnd.randint(-5, 5)
        
        # Perpendicular Gradient for line l (m_l = -1/m_k)
        self.m_l = round(-1 / self.m_k, 2)
        
        # Define Intersection point C (cx, cy)
        self.cx = rnd.randint(-4, 4)
        self.cy = round(self.m_k * self.cx + self.c_k, 2)
        
        # Intercept for line l: c_l = cy - m_l * cx
        self.c_l = round(self.cy - self.m_l * self.cx, 2)
        
        # Define Point A on line k and Point B on line l
        # Points are shifted from C to ensure triangle existence
        self.ax_val = self.cx + rnd.choice([-1, 1]) * rnd.randint(3, 6)
        self.ay_val = round(self.m_k * self.ax_val + self.c_k, 2)
        
        self.bx_val = self.cx + rnd.choice([-1, 1]) * rnd.randint(3, 6)
        self.by_val = round(self.m_l * self.bx_val + self.c_l, 2)
        
        # Area calculation: 0.5 * distance(AC) * distance(BC)
        dist_ac = math.sqrt((self.ax_val - self.cx)**2 + (self.ay_val - self.cy)**2)
        dist_bc = math.sqrt((self.bx_val - self.cx)**2 + (self.by_val - self.cy)**2)
        
        self.answer = round(0.5 * dist_ac * dist_bc, 2)

        # Metadata properties
        self.description = (
            "The figure shows two perpendicular lines, line $k$ and line $l$, "
            "which intersect at a point $C$. Based on the coordinates of points "
            "$A$ and $B$ and the equations provided in the diagram, find the area of triangle $ABC$."
        )
        self.topic = "Coordinate geometry"
        self.subtopic = "Perpendicular lines"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Equations of the lines:}} & \\\\"
            f"k: y &= {round(self.m_k, 10)}x {fmt_poly(round(self.c_k, 10), '')} \\\\"
            f"l: y &= {round(self.m_l, 10)}x {fmt_poly(round(self.c_l, 10), '')} \\\\"
            f"\\text{{Find the intersection point }} C(x, y) \\text{{ by solving the system:}} & \\\\"
            f"{round(self.m_k, 10)}x {fmt_poly(round(self.c_k, 10), '')} &= {round(self.m_l, 10)}x {fmt_poly(round(self.c_l, 10), '')} \\\\"
            f"{round(self.m_k - self.m_l, 10)}x &= {round(self.c_l - self.c_k, 10)} \\\\"
            f"x &= {round(self.cx, 10)}, \\quad y = {round(self.cy, 10)} \\implies C({round(self.cx, 10)}, {round(self.cy, 10)}) \\\\"
            f"\\text{{Identify points }} A \\text{{ and }} B \\text{{ from the figure:}} & \\\\"
            f"A &= ({round(self.ax_val, 10)}, {round(self.ay_val, 10)}), \\quad B = ({round(self.bx_val, 10)}, {round(self.by_val, 10)}) \\\\"
            f"\\text{{Calculate base }} AC \\text{{ and height }} BC \\text{{ using the distance formula:}} & \\\\"
            f"AC &= \\sqrt{{({round(self.ax_val, 10)} - {round(self.cx, 10)})^2 + ({round(self.ay_val, 10)} - {round(self.cy, 10)})^2}} \\\\"
            f"&= {round(math.sqrt((self.ax_val - self.cx)**2 + (self.ay_val - self.cy)**2), 10)} \\\\"
            f"BC &= \\sqrt{{({round(self.bx_val, 10)} - {round(self.cx, 10)})^2 + ({round(self.by_val, 10)} - {round(self.cy, 10)})^2}} \\\\"
            f"&= {round(math.sqrt((self.bx_val - self.cx)**2 + (self.by_val - self.cy)**2), 10)} \\\\"
            f"\\text{{Since lines }} k \\text{{ and }} l \\text{{ are perpendicular, Area }} ABC = \\frac{1}{2} \\times AC \\times BC: & \\\\"
            f"\\text{{Area}} &= 0.5 \\times {round(math.sqrt((self.ax_val - self.cx)**2 + (self.ay_val - self.cy)**2), 10)} \\times {round(math.sqrt((self.bx_val - self.cx)**2 + (self.by_val - self.cy)**2), 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        limit = 15
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        x_plot = np.linspace(-limit, limit, 100)
        
        # Plot Lines k and l
        ax.plot(x_plot, self.m_k * x_plot + self.c_k, color='blue', lw=2.5)
        ax.plot(x_plot, self.m_l * x_plot + self.c_l, color='red', lw=2.5)
        
        # Triangle vertices and connecting line AB
        pts = {'A': [self.ax_val, self.ay_val], 'B': [self.bx_val, self.by_val]}
        ax.plot([pts['A'][0], pts['B'][0]], [pts['A'][1], pts['B'][1]], color='black', lw=1.5, linestyle='-')
        
        # Dynamic Point Labeling for A and B
        for label, pos in pts.items():
            ax.plot(pos[0], pos[1], 'ko', markersize=8, zorder=5)
            off_x = 1.5 if pos[0] >= self.cx else -1.5
            off_y = 1.5 if pos[1] >= self.cy else -1.5
            ax.text(pos[0] + off_x, pos[1] + off_y, f"{label}({pos[0]}, {pos[1]})", 
                    fontsize=14, fontweight='bold', ha='center', 
                    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2', alpha=0.9))

        # Intersection point C (visual marker only, label is just "C")
        ax.plot(self.cx, self.cy, 'ko', markersize=8, zorder=5)
        ax.text(self.cx - 1.5, self.cy - 1.5, "C", fontsize=16, fontweight='bold', color='black')

        # Dynamic Equation Placement
        for line_name, m, c, color in [('k', self.m_k, self.c_k, 'blue'), ('l', self.m_l, self.c_l, 'red')]:
            edge_x = -limit + 3 if m > 0 else limit - 8
            edge_y = m * edge_x + c
            edge_y = max(-limit + 2, min(limit - 2, edge_y))
            
            eq_text = f"${line_name}: y = {m}x {fmt_poly(c, '')}$"
            ax.text(edge_x, edge_y, eq_text, color=color, fontsize=16, fontweight='bold', 
                    bbox=dict(facecolor='white', edgecolor=color, alpha=0.9))

        # Perpendicular marker at C
        size = 0.8
        v_k = np.array([1, self.m_k]) / np.sqrt(1 + self.m_k**2)
        v_l = np.array([1, self.m_l]) / np.sqrt(1 + self.m_l**2)
        s_k = np.sign(self.ax_val - self.cx)
        s_l = np.sign(self.bx_val - self.cx)
        
        corner1 = np.array([self.cx, self.cy]) + s_k * size * v_k
        corner2 = corner1 + s_l * size * v_l
        corner3 = np.array([self.cx, self.cy]) + s_l * size * v_l
        ax.plot([corner1[0], corner2[0], corner3[0]], [corner1[1], corner2[1], corner3[1]], color='black', lw=1.5)

        ax.set_xlabel('x', fontsize=14)
        ax.set_ylabel('y', fontsize=14)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat039:
    def __init__(self):
        self.length_b = round(randrange_float(2.2, 5.8, 0.1), 2)
        self.width_b = round(randrange_float(1.4, 4.6, 0.1), 2)
        
        # Scale factor as a decimal
        self.scale_factor = round(randrange_float(1.2, 3.4, 0.1), 2)
        
        # Calculate A dimensions and round to ensure consistency
        self.length_a = round(self.length_b * self.scale_factor, 2)
        self.width_a = round(self.width_b * self.scale_factor, 2)
        
        self.answer = self.width_a

        self.description = (
            f"Rectangle $A$ is mathematically similar to rectangle $B$. "
            f"Work out the value of $x$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Similarity"
        self.source = "Adapted from IGCSE June 2025 Question Paper 13"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Scale Factor }} (k) &= \\frac{{\\text{{Length}}_A}}{{\\text{{Length}}_B}}\\\\"
            f"&= \\frac{{{self.length_a}}}{{{self.length_b}}}\\\\"
            f"&= {round(self.length_a / self.length_b, 10)}\\\\"
            f"\\text{{Since the rectangles are similar, the width }} x \\text{{ is:}} &\\\\"
            f"x &= \\text{{Width}}_B \\times k\\\\"
            f"&= {self.width_b} \\times {round(self.length_a / self.length_b, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw Rectangle A
        rect_a_w, rect_a_h = 5, 3
        rect_a = patches.Rectangle((1, 1.5), rect_a_w, rect_a_h, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(rect_a)
        
        # Use :g formatting to strip unnecessary decimals in labels
        ax.text(1 + rect_a_w/2, 1.5 + rect_a_h + 0.2, f"{self.length_a:g} cm", ha='center', fontsize=14)
        ax.text(1 + rect_a_w + 0.2, 1.5 + rect_a_h/2, f"$x$ cm", va='center', fontsize=14)
        ax.text(1 + rect_a_w/2, 1.1, "Rectangle $A$", ha='center', fontsize=14)

        # Draw Rectangle B
        rect_b_w, rect_b_h = 2.5, 1.5
        rect_b = patches.Rectangle((8, 1.5), rect_b_w, rect_b_h, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(rect_b)
        
        # Use :g formatting here as well for the labels
        ax.text(8 + rect_b_w/2, 1.5 + rect_b_h + 0.2, f"{self.length_b:g} cm", ha='center', fontsize=14)
        ax.text(8 + rect_b_w + 0.2, 1.5 + rect_b_h/2, f"{self.width_b:g} cm", va='center', fontsize=14)
        ax.text(8 + rect_b_w/2, 1.1, "Rectangle $B$", ha='center', fontsize=14)

        ax.text(11, 5, "NOT TO\nSCALE", ha='center', fontsize=12)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat040:
    def __init__(self):
        self.k = randrange_float(1.5, 8.5, 0.5) 
        self.height_a = rnd.randint(3, 60)
        self.height_b = round(self.height_a * self.k, 4)
        self.area_a = rnd.randint(5, 1000)
        self.area_b = round(self.area_a * (self.k ** 2), 4)
        self.answer = self.height_b

        self.description = (
            f"Solid $A$ is mathematically similar to solid $B$. "
            f"The diagram shows the heights and surface areas ($S_A$ and $S_B$) for both solids. "
            f"Calculate the height, $H$, of solid $B$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Similarity"
        self.source = "Adapted from IGCSE June 2025 Question Paper 23"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Let }} k \\text{{ be the linear scale factor between Solid }} A \\text{{ and Solid }} B: & \\\\"
            f"\\text{{The relationship between surface areas is:}} & \\\\"
            f"k^2 &= \\frac{{S_B}}{{S_A}} \\\\"
            f"k^2 &= \\frac{{{self.area_b}}}{{{self.area_a}}} \\\\"
            f"k &= \\sqrt{{\\frac{{{self.area_b}}}{{{self.area_a}}}}} \\\\"
            f"k &= {round(self.k, 10)} \\\\"
            f"\\text{{The relationship between heights is:}} & \\\\"
            f"\\frac{{H}}{{\\text{{height}}_A}} &= k \\\\"
            f"H &= \\text{{height}}_A \\times k \\\\"
            f"H &= {self.height_a} \\times {round(self.k, 10)} \\\\"
            f"H &= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        shape_type = rnd.choice(['prism', 'pyramid', 'cylinder', 'cone'])
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 12)
        ax.set_aspect('equal')
        ax.axis('off')

        visual_scale_a = 0.8
        visual_scale_b = 2.2

        # Draw Solid A
        offset_a_x, offset_a_y = 2, 2
        label_y_a = draw_solid(ax, offset_a_x, offset_a_y, visual_scale_a, f"{self.height_a} cm", shape_type)
        label_x_a = offset_a_x + 1.5 * visual_scale_a
        ax.text(label_x_a, label_y_a, "Solid $A$", ha='center', fontsize=14, fontweight='bold')
        # Place Surface Area label below "Solid A"
        ax.text(label_x_a, label_y_a - 0.7, f"$S_A = {self.area_a}$ cm$^2$", ha='center', fontsize=12)

        # Draw Solid B
        offset_b_x = 9 
        offset_b_y = 1
        label_y_b = draw_solid(ax, offset_b_x, offset_b_y, visual_scale_b, "$H$ cm", shape_type)
        label_x_b = offset_b_x + 1.5 * visual_scale_b
        ax.text(label_x_b, label_y_b, "Solid $B$", ha='center', fontsize=14, fontweight='bold')
        # Place Surface Area label below "Solid B"
        ax.text(label_x_b, label_y_b - 0.7, f"$S_B = {self.area_b}$ cm$^2$", ha='center', fontsize=12)

        plt.text(14, 10.5, "NOT TO\nSCALE", fontsize=10, ha='center')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat041:
    def __init__(self):
        self.k = randrange_float(1.5, 5.5, 0.5) 
        self.height_a = rnd.randint(5, 40)
        self.height_b = round(self.height_a * self.k, 4)
        self.volume_a = rnd.randint(10, 500)
        self.volume_b = round(self.volume_a * (self.k ** 3), 4)
        self.answer = self.volume_b

        self.description = (
            f"Solid $A$ and solid $B$ are mathematically similar. "
            f"The diagram shows the heights and volumes ($V_A$ and $V_B$) for both solids. "
            f"Calculate the volume, $V_B$, of solid $B$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Similarity"
        self.source = "Adapted from IGCSE June 2025 Question Paper 23"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Let }} k \\text{{ be the linear scale factor:}} & \\\\"
            f"k &= \\frac{{\\text{{height}}_B}}{{\\text{{height}}_A}} \\\\"
            f"&= \\frac{{{self.height_b}}}{{{self.height_a}}} \\\\"
            f"&= {round(self.k, 10)} \\\\"
            f"\\text{{The relationship between volumes is given by:}} & \\\\"
            f"\\frac{{V_B}}{{V_A}} &= k^3 \\\\"
            f"V_B &= V_A \\times k^3 \\\\"
            f"&= {self.volume_a} \\times ({round(self.k, 10)})^3 \\\\"
            f"&= {self.volume_a} \\times {round(self.k**3, 10)} \\\\"
            f"&= {self.answer}\\,\\text{{cm}}^3"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        shape_type = rnd.choice(['prism', 'pyramid', 'cylinder', 'cone'])
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 12)
        ax.set_aspect('equal')
        ax.axis('off')

        visual_scale_a = 0.8
        visual_scale_b = 2.2

        # Draw Solid A
        offset_a_x, offset_a_y = 2, 2
        label_y_a = draw_solid(ax, offset_a_x, offset_a_y, visual_scale_a, f"{self.height_a} cm", shape_type)
        label_x_a = offset_a_x + 1.5 * visual_scale_a
        ax.text(label_x_a, label_y_a, "Solid $A$", ha='center', fontsize=14, fontweight='bold')
        # Place Volume label below "Solid A"
        ax.text(label_x_a, label_y_a - 0.7, f"$V_A = {self.volume_a}$ cm$^3$", ha='center', fontsize=12)

        # Draw Solid B
        offset_b_x = 9
        offset_b_y = 1
        label_y_b = draw_solid(ax, offset_b_x, offset_b_y, visual_scale_b, f"{self.height_b} cm", shape_type)
        label_x_b = offset_b_x + 1.5 * visual_scale_b
        ax.text(label_x_b, label_y_b, "Solid $B$", ha='center', fontsize=14, fontweight='bold')
        # Place Volume label below "Solid B"
        ax.text(label_x_b, label_y_b - 0.7, f"$V_B = ?$ cm$^3$", ha='center', fontsize=12)

        plt.text(14, 10.5, "NOT TO\nSCALE", fontsize=10, ha='center')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat042:
    
    def __init__(self):
        # Property: In a rhombus, adjacent angles sum to 180 degrees.
        # We define angles as k1*a and k2*a such that (k1 + k2) * a = 180.
        
        # Randomize coefficients to vary the angles
        # Allowing k1 and k2 to vary freely allows the shape to lean left or right.
        self.k1 = rnd.randint(1, 5)
        self.k2 = rnd.randint(1, 5)
        total_k = self.k1 + self.k2
        
        # alpha = 180 / total_k. Result can be non-integer.
        self.alpha = 180 / total_k

        # Randomize side length to vary the base and overall size
        self.side_length = rnd.uniform(4.5, 7.5)

        # Calculate actual angles for drawing geometry
        self.angle_a_deg = self.k1 * self.alpha
        self.angle_2a_deg = self.k2 * self.alpha
        
        # Formatting labels for the diagram
        self.label1 = f"{self.k1}a" if self.k1 > 1 else "a"
        self.label2 = f"{self.k2}a" if self.k2 > 1 else "a"
        
        # Final answer rounded for display
        self.answer = self.alpha
        
        self.description = f"The diagram shows a quadrilateral with sides of equal length. Work out the value of $a$."
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from IGCSE March 2025 Question Paper 13"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The quadrilateral has four equal sides, identifying it as a rhombus.}} &\\\\"
            f"\\text{{In a rhombus, adjacent angles are supplementary (sum to }} 180^\\circ\\text{{).}} &\\\\"
            f"\\text{{Setting up the equation for the sum of adjacent angles:}} &\\\\"
            f"\\text{{Angle 1}} + \\text{{Angle 2}} &= 180^\\circ \\\\"
            f"{self.label1}^\\circ + {self.label2}^\\circ &= 180^\\circ \\\\"
            f"{self.k1}a + {self.k2}a &= 180 \\\\"
            f"({self.k1} + {self.k2})a &= 180 \\\\"
            f"{self.k1 + self.k2}a &= 180 \\\\"
            f"a &= \\frac{{180}}{{{self.k1 + self.k2}}} \\\\"
            f"a &= {round(self.alpha, 10)} \\\\"
            f"a &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        angle_rad = np.radians(self.angle_a_deg)
        L = self.side_length
        
        # Vertices of the rhombus
        # p1 (origin), p2 (base), p3 (top right), p4 (top left)
        p1 = np.array([0, 0])
        p2 = np.array([L, 0])
        p3 = np.array([L + L * np.cos(angle_rad), L * np.sin(angle_rad)])
        p4 = np.array([L * np.cos(angle_rad), L * np.sin(angle_rad)])
        
        pts = np.array([p1, p2, p3, p4])
        rhombus = patches.Polygon(pts, closed=True, fill=None, edgecolor='black', linewidth=2)
        ax.add_patch(rhombus)
        
        # Add equal length markings on each side using helper
        for i in range(4):
            add_marking(ax, pts[i], pts[(i+1)%4])
        
        # Angle arcs and Dynamic Labels
        # arc_radius scales with side length
        arc_radius = L * 0.3
        
        # Vertex p1 Arc
        arc1 = patches.Arc(p1, arc_radius, arc_radius, theta1=0, theta2=self.angle_a_deg, color='black', lw=1.5)
        ax.add_patch(arc1)
        
        # Vertex p2 Arc (interior angle is 180 - angle_a_deg)
        arc2 = patches.Arc(p2, arc_radius, arc_radius, theta1=180 - self.angle_2a_deg, theta2=180, color='black', lw=1.5)
        ax.add_patch(arc2)

        # Dynamic Bisector Positioning for Labels
        # offset_dist also scales with side length
        offset_dist = L * 0.25
        
        # Label at p1 (Bisects angle_a)
        bisect1 = np.radians(self.angle_a_deg / 2)
        ax.text(offset_dist * np.cos(bisect1), offset_dist * np.sin(bisect1), 
                f"${self.label1}^\\circ$", fontsize=16, ha='center', va='center')
        
        # Label at p2 (Bisects angle_2a)
        bisect2 = np.radians((180 - self.angle_2a_deg / 2))
        ax.text(L + offset_dist * np.cos(bisect2), offset_dist * np.sin(np.pi - bisect2), 
                f"${self.label2}^\\circ$", fontsize=16, ha='center', va='center')
        
        # Placing "NOT TO SCALE" outside the rhombus
        # Positions it to the right of the furthest x-coordinate
        ax.text(max(pts[:,0]) + 1.2, max(pts[:,1]) / 2, "NOT TO\nSCALE", fontsize=12, ha='left', va='center')

        ax.set_aspect('equal')
        ax.axis('off')
        
        # Dynamic axis limits
        ax.set_xlim(min(pts[:,0]) - 2, max(pts[:,0]) + 4)
        ax.set_ylim(min(pts[:,1]) - 2, max(pts[:,1]) + 2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
        
class Mat043:
    
    def __init__(self):
        # Base angles of isosceles triangle ABC
        # AB = AC implies base angles ABC and ACB are equal
        self.angle_B = randrange_float(40.0, 70.0, 0.01)
        self.angle_C = self.angle_B
        
        # Calculate max bound for ADC to maintain DAC > 5 degrees
        # Sum of angles in triangle ADC: DAC + ADC + ACD = 180
        max_ADC = 175.0 - self.angle_C
        self.angle_ADC = randrange_float(self.angle_C + 5.0, max_ADC, 0.01)
        
        # Calculate target angle DAC using triangle sum property
        target_raw = 180.0 - self.angle_ADC - self.angle_C
        self.target_angle = round(target_raw, 2)
        
        self.answer = self.target_angle
        self.description = (
            f"$BDC$ is a straight line, $AB = AC$, angle $ABD = {round(self.angle_B, 2)}^\\circ$ "
            f"and angle $ADC = {round(self.angle_ADC, 2)}^\\circ$. \\\\ Work out angle $DAC$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from 2025-specimen-paper-2"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given that }} AB = AC, \\text{{ triangle }} ABC \\text{{ is an isosceles triangle.}} &\\\\"
            f"\\text{{The base angles of an isosceles triangle are equal:}} &\\\\"
            f"\\angle ACB &= \\angle ABC\\\\"
            f"&= {round(self.angle_B, 10)}^\\circ\\\\"
            f"\\text{{Since }} BDC \\text{{ is a straight line, }} \\angle ACD = \\angle ACB. &\\\\"
            f"\\text{{In triangle }} ADC, \\text{{ the sum of interior angles is }} 180^\\circ: &\\\\"
            f"\\angle DAC + \\angle ADC + \\angle ACD &= 180^\\circ\\\\"
            f"\\angle DAC + {round(self.angle_ADC, 10)}^\\circ + {round(self.angle_C, 10)}^\\circ &= 180^\\circ\\\\"
            f"\\angle DAC + {round(self.angle_ADC + self.angle_C, 10)}^\\circ &= 180^\\circ\\\\"
            f"\\angle DAC &= 180^\\circ - {round(self.angle_ADC + self.angle_C, 10)}^\\circ\\\\"
            f"\\angle DAC &= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        base_w = 10
        B = np.array([0, 0])
        C = np.array([base_w, 0])
        
        # Geometric construction of the isosceles triangle
        rad_B = np.radians(self.angle_B)
        h = (base_w / 2) * np.tan(rad_B)
        A = np.array([base_w / 2, h])
        
        # Position D on BC segment via Sine Rule in triangle ADC
        AC_len = np.linalg.norm(A - C)
        DC_len = (AC_len * np.sin(np.radians(self.target_angle))) / np.sin(np.radians(self.angle_ADC))
        D = np.array([base_w - DC_len, 0])
        
        # Drawing segments
        lines = [[A, B], [B, C], [C, A], [A, D]]
        for line in lines:
            ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], color='black', lw=1)
            
        # Labeling vertices
        ax.text(A[0], A[1] + 0.3, "A", fontsize=14, ha='center')
        ax.text(B[0] - 0.3, B[1] - 0.5, "B", fontsize=14, ha='center')
        ax.text(C[0] + 0.3, C[1] - 0.5, "C", fontsize=14, ha='center')
        ax.text(D[0], D[1] - 0.5, "D", fontsize=14, ha='center')
        
        # Marks for equal side lengths
        add_marking(ax, A, B)
        add_marking(ax, A, C)
        
        # Use raw f-strings (rf) to fix SyntaxWarning with LaTeX backslashes
        arc_B = patches.Arc(B, 2, 2, theta1=0, theta2=self.angle_B, color='black')
        ax.add_patch(arc_B)
        ax.text(B[0] + 1.2, B[1] + 0.4, rf"{round(self.angle_B, 2)}$^\circ$", fontsize=12)
        
        arc_D = patches.Arc(D, 1.5, 1.5, theta1=0, theta2=self.angle_ADC, color='black')
        ax.add_patch(arc_D)
        ax.text(D[0] + 0.4, D[1] + 0.7, rf"{round(self.angle_ADC, 2)}$^\circ$", fontsize=12)
        
        ax.text(base_w + 1, h / 2, "NOT TO\nSCALE", fontsize=10, ha='center')
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-1, base_w + 3)
        ax.set_ylim(-1, h + 1)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close(fig)

class Mat044:

    def __init__(self):
        self.angle_top = randrange_float(40.0, 80.0, 0.01)
        self.angle_ext = randrange_float(min(self.angle_top, 100-self.angle_top), max(self.angle_top, 100-self.angle_top), 0.01)
        
        self.answer = round(self.angle_ext, 10)

        self.description = (
            f"Lines $AB$ and $CD$ are parallel. $EF$ and $EG$ are straight lines. "
            f"The angle formed at the intersection of $EF$ and $CD$ is {self.angle_top:.2f}°. "
            f"Find the value of $a$."
        )
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from 2025-specimen-paper-1"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify that lines }} AB \\text{{ and }} CD \\text{{ are parallel, and }} EG \\text{{ is a transversal line.}} \\\\"
            f"\\text{{According to the Alternate Interior Angles Theorem, alternate interior angles are equal.}} \\\\"
            f"\\text{{The angle }} a \\text{{ and the given angle at }} E \\text{{ (}} \\angle GEA \\text{{) are alternate interior angles.}} \\\\"
            f"a &= \\angle GEA \\\\"
            f"a &= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_aspect('equal')
        ax.axis('off')

        # Parallel lines distance
        dist = 4.0
        
        # Line AB (bottom parallel) at y = 0
        # Line CD (top parallel) at y = dist
        y_ab = 0
        y_cd = dist
        
        # Define intersection E on line AB
        E = np.array([2.0, y_ab])
        
        # Calculate intersection I on line CD for EF
        theta_ef = np.radians(180-self.angle_top) 
        x_i = E[0] + dist / np.tan(theta_ef)
        I = np.array([x_i, y_cd])
        
        # Calculate intersection C on line CD for EG
        C = np.array([I[0] + 5.0, y_cd])
        
        # Define endpoints for all lines
        A = np.array([C[0] + 3, y_ab])
        B = np.array([E[0] - 4, y_ab])
        D = np.array([I[0] - 4, y_cd])
        G_end = np.array([C[0], y_cd]) # End of line CD
        
        # Transversal EF
        F = I + (I - E) * 0.5
        
        # Transversal EG
        G = E + (C - E) * 1.3
        
        BEA = get_angle(E, A)
        DIC = BEA
        GEA = get_angle(E, G)
        FEA = get_angle(E, F)
        BEF = 180 - GEA - FEA
        FEG = 180 - BEF - GEA
        EIC = 180 - FEA

        # Draw Parallel Lines
        ax.plot([B[0], A[0]], [B[1], A[1]], 'black', lw=1) # Line AB
        ax.plot([D[0], G_end[0]], [D[1], G_end[1]], 'black', lw=1) # Line CD

        # Draw Transversals
        ax.plot([E[0], F[0]], [E[1], F[1]], 'black', lw=1) # Line EF
        ax.plot([E[0], G[0]], [E[1], G[1]], 'black', lw=1) # Line EG

        # Add Labels
        label_offset = 0.4
        ax.text(A[0], A[1] - label_offset, 'A', fontsize=12)
        ax.text(B[0], B[1] + label_offset, 'B', fontsize=12)
        ax.text(C[0] + label_offset, C[1], 'C', fontsize=12, ha='center')
        ax.text(D[0], D[1] + label_offset - label_offset, 'D', fontsize=12)
        ax.text(E[0] - label_offset, E[1] - label_offset, 'E', fontsize=12)
        ax.text(F[0], F[1] + label_offset, 'F', fontsize=12)
        ax.text(G[0] + label_offset, G[1], 'G', fontsize=12)

        # Parallel markings (Arrows)
        ax.annotate('', xy=A - np.array([1.0, 0]), xytext=A - np.array([1.6, 0]), 
                    arrowprops=dict(arrowstyle='->', lw=1))
        
        ax.annotate('', xy=G_end - np.array([1.0, 0]), xytext=G_end - np.array([1.6, 0]), 
                    arrowprops=dict(arrowstyle='->', lw=1))

        # Add Angle Arcs and Labels
        r_label = 1  # Distance to push text away from vertex
        
        # Known angle at I
        t1, t2 = FEG+180, 360+BEA
        mid = np.radians((t1+t2) / 2)
        ax.add_patch(patches.Arc(I, 1.2, 1.2, theta1=t1, theta2=t2, color='black'))
        ax.text(I[0] + r_label * 1.2 * np.cos(mid), I[1] + r_label * 0.8 * np.sin(mid), 
                f'{self.angle_top:.2f}°', fontsize=10, ha='center', va='center')

        # Known angle at E
        t1, t2 = BEA, GEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(E, 1.2, 1.2, theta1=t1, theta2=t2, color='black'))
        ax.text(E[0] + r_label * 1.2* np.cos(mid), E[1] + r_label * 0.8 *np.sin(mid), 
                f'{self.angle_ext:.2f}°', fontsize=10, ha='center', va='center')
        
        # Angle a at C
        t1, t2 = 180+BEA, 180+GEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(C, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(C[0] + r_label * 0.8 * np.cos(mid), C[1] + r_label * 0.8 * np.sin(mid), 
                '$a°$', fontsize=11, ha='center', va='center')
        
        # Angle b at C
        t1, t2 = GEA, 180+DIC
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(C, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(C[0] + r_label * 0.8 * np.cos(mid), C[1] + r_label * 0.8 * np.sin(mid), 
                '$b°$', fontsize=11, ha='center', va='center')
        
        # Angle c at E
        t1, t2 = GEA, FEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(E, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(E[0] + r_label * 0.8 * np.cos(mid), E[1] + r_label * 0.8 *np.sin(mid), 
                '$c°$', fontsize=11, ha='center', va='center')

        # NOT TO SCALE label
        ax.text(0.95, 0.9, 'NOT TO\nSCALE', transform=ax.transAxes, ha='center', fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close(fig)

class Mat045:
    def __init__(self):
        # Generalize to n sides (3 to 9)
        self.n = rnd.randint(3, 9)
        total_sum = (self.n - 2) * 180
        
        # Regenerate all parameters together to avoid infinite loops
        while True:
            # Target can be non-integer (stepping by 0.5)
            self.x_val = rnd.randint(20, 80) / 2.0 
            
            # Increase coeff range (1, 10)
            self.coeffs = [rnd.randint(1, 10) for _ in range(self.n)]
            sum_a = sum(self.coeffs)
            
            # Calculate sum_b to satisfy: sum_a * x + sum_b = total_sum
            sum_b = total_sum - (sum_a * self.x_val)
            
            # Distribute sum_b into n parts
            self.consts = [0] * self.n
            current_sum_b = 0
            for i in range(self.n - 1):
                val = rnd.randint(-20, 40)
                self.consts[i] = val
                current_sum_b += val
            self.consts[self.n - 1] = int(sum_b - current_sum_b)
            
            # Ensure all individual angles are positive
            if all(self.coeffs[i] * self.x_val + self.consts[i] > 0 for i in range(self.n)):
                break
        
        self.answer = self.x_val
        
        name_map = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 
                    6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon"}
        self.shape_name = name_map[self.n]
        
        self.description = (
            f"The diagram shows the interior angles of a {self.shape_name}, written in terms of $x$. "
            f"Find the value of $x$."
        )
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from IGCSE March 2025 Question Paper 32"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            r"\[\begin{aligned}"
            fr"\text{{The sum of the interior angles of an }} n\text{{-sided polygon is given by:}} \\"
            fr"S &= (n - 2) \times 180^\circ \\"
            fr"\text{{For a {self.shape_name} where }} n = {self.n}\text{{:}} \\"
            fr"S &= ({self.n} - 2) \times 180^\circ \\"
            fr"&= {round((self.n - 2) * 180, 10)}^\circ \\"
            fr"\text{{The sum of the given interior angles in terms of }} x \text{{ is:}} \\"
            fr"\sum \text{{Angles}} &= {' + '.join(['(' + fmt_poly(c, 'x', True) + fmt_poly(b, '') + ')' for c, b in zip(self.coeffs, self.consts)])} \\"
            fr"&= ({' + '.join(map(str, self.coeffs))})x + ({' + '.join([str(b) if b >= 0 else f'({b})' for b in self.consts])}) \\"
            fr"&= {round(sum(self.coeffs), 10)}x {'+' if sum(self.consts) >= 0 else '-'} {abs(round(sum(self.consts), 10))} \\"
            fr"\text{{Equating the sum to }} {round((self.n - 2) * 180, 10)}^\circ\text{{:}} \\"
            fr"{round(sum(self.coeffs), 10)}x {'+' if sum(self.consts) >= 0 else '-'} {abs(round(sum(self.consts), 10))} &= {round((self.n - 2) * 180, 10)} \\"
            fr"{round(sum(self.coeffs), 10)}x &= {round((self.n - 2) * 180, 10)} - ({round(sum(self.consts), 10)}) \\"
            fr"{round(sum(self.coeffs), 10)}x &= {round((self.n - 2) * 180 - sum(self.consts), 10)} \\"
            fr"x &= \frac{{{round((self.n - 2) * 180 - sum(self.consts), 10)}}}{{{round(sum(self.coeffs), 10)}}} \\"
            fr"x &= {self.answer}"
            r"\end{aligned}\]"
        )
        
    def generate(self, num):
        # Generate random n-polygon
        # Divide the circle into n equal sectors and pick a random point in each
        # This guarantees a minimum angular distance between points
        r = 3
        sector_width = (2 * math.pi) / self.n
        buffer = sector_width * 0.2
        
        angles = []
        for i in range(self.n):
            start = i * sector_width + buffer
            end = (i + 1) * sector_width - buffer
            angles.append(rnd.uniform(start, end))
            
        pts = np.array([[r * math.cos(a), r * math.sin(a)] for a in angles])
        
        fig, ax = plt.subplots(figsize=(8, 8))
        polygon = patches.Polygon(pts, closed=True, fill=None, edgecolor='black', linewidth=2)
        ax.add_patch(polygon)
        
        for i in range(self.n):
            p_prev = pts[i-1]
            p_curr = pts[i]
            p_next = pts[(i+1) % self.n]
            
            # Label Placement using Vector Bisector
            v1 = (p_prev - p_curr) / np.linalg.norm(p_prev - p_curr)
            v2 = (p_next - p_curr) / np.linalg.norm(p_next - p_curr)
            
            # Use unit vectors to find the interior bisector
            bisector = v1 + v2
            bisector_unit = bisector / np.linalg.norm(bisector)
            
            # Position labels inside the polygon
            text_pos = p_curr + bisector_unit * 0.8
            
            # Angle Arcs
            ang_start = get_angle(p_curr, p_next)
            ang_end = get_angle(p_curr, p_prev)
            
            # Ensure the arc draws the interior angle
            if (ang_end - ang_start) % 360 > 180:
                ang_start, ang_end = ang_end, ang_start
                
            arc = patches.Arc(p_curr, 0.6, 0.6, theta1=ang_start, theta2=ang_end, color='black')
            ax.add_patch(arc)
            
            # Using Raw f-string (fr"") to prevent SyntaxWarning for LaTeX
            # Reusing fmt_poly from your helper
            label_str = f"{fmt_poly(self.coeffs[i], 'x', True)}{fmt_poly(self.consts[i], '')}"
            ax.text(text_pos[0], text_pos[1], fr"${label_str}^\circ$", 
                    fontsize=10, ha='center', va='center')

        # Formatting
        limit = r + 1.5
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.axis('off')
        ax.set_aspect('equal')
        
        plt.text(limit-0.5, -limit+0.5, "NOT TO\nSCALE", fontsize=10, ha='center', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=150)
        plt.close()
        
class Mat046:
    def __init__(self):
        self.angle_bad = randrange_float(60, 90, 0.01)
        self.angle_bca = randrange_float(30, 45, 0.01)
        
        self.answer = (180 - self.angle_bad) - self.angle_bca

        self.description = (
            f"The diagram shows a cyclic quadrilateral $ABCD$. The diagonals $BD$ and $AC$ intersect. "
            f"Angle $BAD = {self.angle_bad}^\\circ$ and angle $BCA = {self.angle_bca}^\\circ$. "
            f"Find the value of angle $ABD$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems I"
        self.source = "Adapted from 2025-specimen-paper-2"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"
        
        self.reasoning = (
            f"\\[\\begin{{aligned}} "
            f"\\text{{Since }} ABCD \\text{{ is a cyclic quadrilateral, opposite angles sum to }} 180^\\circ: & \\\\"
            f"\\angle BCD &= 180^\\circ - \\angle BAD \\\\"
            f"&= 180^\\circ - {round(self.angle_bad, 10)}^\\circ \\\\"
            f"&= {round(180 - self.angle_bad, 10)}^\\circ \\\\"
            f"\\text{{The angle }} \\angle BCD \\text{{ is composed of }} \\angle BCA \\text{{ and }} \\angle ACD: & \\\\"
            f"\\angle ACD &= \\angle BCD - \\angle BCA \\\\"
            f"&= {round(180 - self.angle_bad, 10)}^\\circ - {round(self.angle_bca, 10)}^\\circ \\\\"
            f"&= {self.answer}^\\circ \\\\"
            f"\\text{{By the circle theorem, angles subtended by the same arc }} AD \\text{{ are equal:}} & \\\\"
            f"\\angle ABD &= \\angle ACD \\\\"
            f"&= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal')
        ax.axis('off')

        r = 1.0
        circle = plt.Circle((0, 0), r, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        # Define vertex angles in degrees (Counter-Clockwise order: A < B < C < D)
        ang_a = randrange_float(210, 240, 0.01)
        ang_b = ang_a + randrange_float(40, 70, 0.01)
        ang_c = ang_b + randrange_float(60, 90, 0.01)
        ang_d = ang_c + randrange_float(60, 90, 0.01)
        
        # Coordinate calculation (Direct logic)
        pts = {
            'A': np.array([r * np.cos(np.radians(ang_a)), r * np.sin(np.radians(ang_a))]),
            'B': np.array([r * np.cos(np.radians(ang_b)), r * np.sin(np.radians(ang_b))]),
            'C': np.array([r * np.cos(np.radians(ang_c)), r * np.sin(np.radians(ang_c))]),
            'D': np.array([r * np.cos(np.radians(ang_d)), r * np.sin(np.radians(ang_d))])
        }

        # Draw Geometry
        poly = plt.Polygon([pts['A'], pts['B'], pts['C'], pts['D']], fill=False, lw=1, edgecolor='black')
        ax.add_patch(poly)

        # Diagonals
        ax.plot([pts['A'][0], pts['C'][0]], [pts['A'][1], pts['C'][1]], color='black', lw=1)
        ax.plot([pts['B'][0], pts['D'][0]], [pts['B'][1], pts['D'][1]], color='black', lw=1)

        # Labels
        label_r = 1.12
        for label, angle in zip(['A', 'B', 'C', 'D'], [ang_a, ang_b, ang_c, ang_d]):
            lx = label_r * np.cos(np.radians(angle))
            ly = label_r * np.sin(np.radians(angle))
            ax.text(lx, ly, label, fontsize=20, ha='center', va='center', fontweight='bold')

        # Markings
        # Angle BAD marking
        ang_start_bad = get_angle(pts['A'], pts['B'])
        ang_end_bad = get_angle(pts['A'], pts['D'])
        arc_bad = patches.Arc(pts['A'], 0.4, 0.4, theta1=ang_start_bad, theta2=ang_end_bad, color='black', lw=1)
        ax.add_patch(arc_bad)
        
        mid_bad = 180 + (ang_start_bad + ang_end_bad) / 2
        tx_bad = pts['A'][0] + 0.4 * np.cos(np.radians(mid_bad))
        ty_bad = pts['A'][1] + 0.4 * np.sin(np.radians(mid_bad))
        ax.text(tx_bad, ty_bad, f"{self.angle_bad}°", fontsize=14, ha='center')

        # Angle BCA marking
        ang_start_bca = get_angle(pts['C'], pts['A'])
        ang_end_bca = get_angle(pts['C'], pts['B'])
        arc_bca = patches.Arc(pts['C'], 0.5, 0.5, theta1=ang_start_bca, theta2=ang_end_bca, color='black', lw=1)
        ax.add_patch(arc_bca)
        
        mid_bca = (ang_start_bca + ang_end_bca) / 2
        tx_bca = pts['C'][0] + 0.4 * np.cos(np.radians(mid_bca))
        ty_bca = pts['C'][1] + 0.4 * np.sin(np.radians(mid_bca))
        ax.text(tx_bca, ty_bca, f"{self.angle_bca}°", fontsize=14, ha='center')

        plt.text(1.1, 1.1, "NOT TO\nSCALE", fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat047:
    def __init__(self):
        self.angle_ops = randrange_float(20, 35, 0.01)
        
        self.answer = 90 + (2 * self.angle_ops)

        self.description = (
            f"The diagram shows a circle, centre $O$. $P$ and $S$ are points on the circle. "
            f"$POR$ is a straight line. $QRST$ is a tangent to the circle at $S$. "
            f"Angle $OPS = {self.angle_ops}^\\circ$. "
            f"Find the value of $y$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems I"
        self.source = "Adapted from IGCSE June 2025 Question Paper 13"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{In }}\\triangle OPS, OP = OS \\text{{ (radii), so the triangle is isosceles:}} &\\\\"
            f"\\angle OSP &= \\angle OPS = {round(self.angle_ops, 10)}^\\circ\\\\"
            f"\\text{{The sum of angles in }}\\triangle OPS\\text{{ is }} 180^\\circ: &\\\\"
            f"\\angle POS &= 180^\\circ - (\\angle OPS + \\angle OSP)\\\\"
            f"&= 180^\\circ - (2 \\times {round(self.angle_ops, 10)}^\\circ) = {round(180 - 2 * self.angle_ops, 10)}^\\circ\\\\"
            f"\\text{{Angles on the straight line }} POR \\text{{ sum to }} 180^\\circ: &\\\\"
            f"\\angle SOR &= 180^\\circ - \\angle POS\\\\"
            f"&= 180^\\circ - {round(180 - 2 * self.angle_ops, 10)}^\\circ = {round(2 * self.angle_ops, 10)}^\\circ\\\\"
            f"\\text{{Since }} ST \\text{{ is a tangent at }} S, \\text{{the radius}} OS \\perp ST: &\\\\"
            f"\\angle OSR &= 90^\\circ\\\\"
            f"\\text{{In }}\\triangle OSR, \\text{{ the interior angle }} \\angle ORS \\text{{ is:}} &\\\\"
            f"\\angle ORS &= 180^\\circ - (\\angle OSR + \\angle SOR)\\\\"
            f"&= 180^\\circ - (90^\\circ + {round(2 * self.angle_ops, 10)}^\\circ) = {round(90 - 2 * self.angle_ops, 10)}^\\circ\\\\"
            f"\\text{{Finally, }} y \\text{{ and }} \\angle ORS \\text{{ are supplementary on the straight line }} QR: &\\\\"
            f"y &= 180^\\circ - \\angle ORS\\\\"
            f"&= 180^\\circ - {round(90 - 2 * self.angle_ops, 10)}^\\circ\\\\"
            f"&= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        r = 1.0
        O = np.array([0, 0])
        S = np.array([0, -r]) # Fixed at bottom

        # Calculate P based on angle_ops
        angle_p_deg = 90 - 2 * self.angle_ops
        angle_p_rad = np.radians(angle_p_deg)
        P = np.array([r * np.cos(angle_p_rad), r * np.sin(angle_p_rad)])

        # Calculate R
        x_r = -1.0 / np.tan(angle_p_rad)
        R = np.array([x_r, -1.0])

        # Define Tangent Line Endpoints (Q and T)
        Q = np.array([x_r - 1.2, -1.0]) 
        T = np.array([1.2, -1.0])       

        # Dynamic Plot Limits (Zoom Logic)
        all_x = [Q[0], T[0], P[0], R[0], -1.0, 1.0] # Include circle width
        all_y = [S[1], P[1], 1.0, -1.0]             # Include circle height
        
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)
        
        padding_x = 0.5
        padding_y = 0.5
        
        ax.set_xlim(min_x - padding_x, max_x + padding_x)
        ax.set_ylim(min_y - padding_y, max_y + padding_y)
        ax.set_aspect('equal')
        ax.axis('off')

        # Drawing Elements
        # Circle
        circle = plt.Circle((0, 0), r, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        # Lines
        ax.plot([Q[0], T[0]], [Q[1], T[1]], 'k-', lw=1.5) # Tangent
        ax.plot([P[0], R[0]], [P[1], R[1]], 'k-', lw=1) # Secant
        ax.plot([O[0], S[0]], [O[1], S[1]], 'k-', lw=1) # Radius
        ax.plot([P[0], S[0]], [P[1], S[1]], 'k-', lw=1) # Chord

        # Labels
        text_offset = 0.15 * (r) # Scale offset relative to radius
        ax.text(O[0], O[1] + text_offset, 'O', fontsize=16, ha='right', va='bottom', fontweight='bold')
        ax.text(P[0] + text_offset, P[1], 'P', fontsize=16, ha='left', va='center', fontweight='bold')
        ax.text(S[0], S[1] - 0.2, 'S', fontsize=16, ha='center', va='top', fontweight='bold')
        ax.text(R[0], R[1] - 0.2, 'R', fontsize=16, ha='center', va='top', fontweight='bold')
        ax.text(Q[0], Q[1] - 0.2, 'Q', fontsize=16, ha='center', va='top', fontweight='bold')
        ax.text(T[0], T[1] - 0.2, 'T', fontsize=16, ha='center', va='top', fontweight='bold')

        # Angle Markings
        
        # OPS
        angle_start = get_angle(P, O)
        angle_end = get_angle(P, S)
        if angle_end < angle_start: angle_end += 360
        
        arc_ops = patches.Arc(P, 0.5, 0.5, theta1=angle_start, theta2=angle_end, color='black')
        ax.add_patch(arc_ops)
        
        mid_angle = np.radians((angle_start + angle_end) / 2)
        # Position label slightly inward
        lx = P[0] + 0.5 * np.cos(mid_angle)
        ly = P[1] + 0.5 * np.sin(mid_angle) 
        ax.text(lx - 0.1, ly, f"{self.angle_ops}°", fontsize=12)

        # OSP (x)
        angle_start_x = get_angle(S, P)
        angle_end_x = get_angle(S, O)
        arc_osp = patches.Arc(S, 0.5, 0.5, theta1=angle_start_x, theta2=angle_end_x, color='black')
        ax.add_patch(arc_osp)
        
        mid_angle_x = np.radians((angle_start_x + angle_end_x) / 2)
        lx_x = S[0] + 0.45 * np.cos(mid_angle_x)
        ly_x = S[1] + 0.45 * np.sin(mid_angle_x)
        ax.text(lx_x, ly_x, "$x^\\circ$", fontsize=14, ha='center')

        # Exterior Angle y
        angle_rq = 180 # Left direction
        angle_rp = get_angle(R, P)
        arc_y = patches.Arc(R, 0.6, 0.6, theta1=angle_rp, theta2=angle_rq, color='black')
        ax.add_patch(arc_y)
        
        mid_angle_y = np.radians((angle_rp + angle_rq) / 2)
        lx_y = R[0] + 0.45 * np.cos(mid_angle_y)
        ly_y = R[1] + 0.45 * np.sin(mid_angle_y)
        ax.text(lx_y+0.1, ly_y, "$y^\\circ$", fontsize=14, ha='center')

        # "Not to Scale" - Anchored to Top Right of the axes
        ax.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='right', va='top')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat048:
    def __init__(self):
        self.angle_aco = randrange_float(25, 60, 0.01)
        self.angle_bco = randrange_float(25, 60, 0.01)
        
        self.answer = 90 - self.angle_aco

        self.description = (
            f"The diagram shows a circle, centre $O$. $A$, $B$ and $C$ are three points on the circle. "
            f"Angle $ACO = {self.angle_aco}^\\circ$ and angle $BCO = {self.angle_bco}^\\circ$. "
            f"Find the value of angle $ABC$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems I"
        self.source = "Adapted from IGCSE June 2025 Question Paper 21"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{In }} \\triangle AOC, OA &= OC \\text{{ (radii of the circle)}}\\\\"
            f"\\text{{Since }} OA = OC, \\triangle AOC &\\text{{ is an isosceles triangle.}}\\\\"
            f"\\text{{Therefore, the base angles are equal:}} &\\\\"
            f"\\angle OAC &= \\angle ACO = {round(self.angle_aco, 10)}^\\circ\\\\"
            f"\\text{{The angle at the centre, }} \\angle AOC, \\text{{ is:}} &\\\\"
            f"\\angle AOC &= 180^\\circ - (\\angle OAC + \\angle ACO)\\\\"
            f"&= 180^\\circ - (2 \\times {round(self.angle_aco, 10)}^\\circ)\\\\"
            f"&= {round(180 - 2 * self.angle_aco, 10)}^\\circ\\\\"
            f"\\text{{The angle at the centre is twice the angle at the}} &\\\\"
            f"\\text{{circumference subtended by the same arc (arc }} AC\\text{{):}} &\\\\"
            f"\\angle AOC &= 2 \\times \\angle ABC\\\\"
            f"\\angle ABC &= \\frac{1}{2} \\angle AOC\\\\"
            f"&= \\frac{{ {round(180 - 2 * self.angle_aco, 10)}^\\circ }}{{2}}\\\\"
            f"&= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
    
        limit = 1.6
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.axis('off')

        # Geometry Setup
        r = 1.0
        O = np.array([0, 0])
        
        # Introduce a global rotation to vary the position of point A
        global_rotation = randrange_float(-20, 20, 1)
        
        # Point A: Primary point of tangency
        theta_a_deg = 90 + global_rotation
        rad_a = np.radians(theta_a_deg)
        A = np.array([r * np.cos(rad_a), r * np.sin(rad_a)])
        
        # Point C calculation (dependent on angle_aco)
        # Position relative to A based on the isosceles triangle AOC center angle
        theta_c_deg = theta_a_deg + 180 - (2 * self.angle_aco)
        rad_c = np.radians(theta_c_deg)
        C = np.array([r * np.cos(rad_c), r * np.sin(rad_c)])
        
        # Point B calculation (dependent on angle_bco)
        # Position relative to C based on the isosceles triangle BOC center angle
        theta_b_deg = theta_c_deg + 180 - (2 * self.angle_bco)
        rad_b = np.radians(theta_b_deg)
        B = np.array([r * np.cos(rad_b), r * np.sin(rad_b)])

        # Tangent Line D-E (perpendicular to OA)
        # Direction vector of tangent is (-sin(theta), cos(theta))
        tangent_dir = np.array([-np.sin(rad_a), np.cos(rad_a)])
        D = A + 1.3 * tangent_dir
        E = A - 1.3 * tangent_dir

        # Draw Elements
        circle = plt.Circle((0, 0), r, color='black', fill=False, lw=2)
        ax.add_artist(circle)
        
        # Triangle ABC
        ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1)
        ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1)
        ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1)
        
        # Radii lines
        ax.plot([O[0], A[0]], [O[1], A[1]], 'k-', lw=1)
        ax.plot([O[0], C[0]], [O[1], C[1]], 'k-', lw=1)
        
        # Labels
        # Using a helper to place labels at a distance of 1.15r from the center
        def get_label_pos(angle_deg, dist=1.15):
            rad = np.radians(angle_deg)
            return np.array([dist * np.cos(rad), dist * np.sin(rad)])

        ax.text(O[0] + 0.05, O[1] - 0.05, 'O', fontsize=14, ha='left', va='top', fontweight='bold')
        
        pos_a = get_label_pos(theta_a_deg)
        ax.text(pos_a[0], pos_a[1], 'A', fontsize=14, ha='center', va='bottom', fontweight='bold')
        
        pos_c = get_label_pos(theta_c_deg)
        ax.text(pos_c[0], pos_c[1], 'C', fontsize=14, ha='right', va='center', fontweight='bold')
        
        pos_b = get_label_pos(theta_b_deg)
        ax.text(pos_b[0], pos_b[1], 'B', fontsize=14, ha='left', va='top', fontweight='bold')

        ax.plot(O[0], O[1], 'k.', markersize=5)

        # Angle Markings
        # Angle ACO
        angle_start_aco = get_angle(C, O)
        angle_end_aco = get_angle(C, A)
        if angle_end_aco < angle_start_aco: angle_end_aco += 360
        arc_aco = patches.Arc(C, 0.4, 0.4, theta1=angle_start_aco, theta2=angle_end_aco, color='black')
        ax.add_patch(arc_aco)
        
        mid_aco = np.radians((angle_start_aco + angle_end_aco) / 2)
        ax.text(C[0] + 0.4 * np.cos(mid_aco), C[1] + 0.4 * np.sin(mid_aco), f"{self.angle_aco}°", fontsize=10, ha='center')

        # Angle BCO
        angle_start_bco = get_angle(C, B)
        angle_end_bco = get_angle(C, O)
        if angle_end_bco < angle_start_bco: angle_end_bco += 360
        arc_bco = patches.Arc(C, 0.5, 0.5, theta1=angle_start_bco, theta2=angle_end_bco, color='black')
        ax.add_patch(arc_bco)
        
        mid_bco = np.radians((angle_start_bco + angle_end_bco) / 2)
        ax.text(C[0] + 0.4 * np.cos(mid_bco), C[1] + 0.4 * np.sin(mid_bco), f"{self.angle_bco}°", fontsize=10, ha='center')

        # NOT TO SCALE
        ax.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='right', va='top')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat049:
    def __init__(self):
        self.angle_adb = round(randrange_float(15, 25, 0.01), 2)
        self.angle_bec = round(randrange_float(40, 50, 0.01), 2)
        self.angle_dab = round(randrange_float(100, 120, 0.01), 2)
        
        self.answer = round(self.angle_dab - self.angle_bec, 2)

        self.description = (
            "The points $A, B, C, D$ and $E$ lie on a circle. "
            "$FG$ is a tangent to the circle at $C$. "
            "Using the information provided in the diagram, find the value of angle $DCG$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems I"
        self.source = "Adapted from IGCSE March 2025 Question Paper 22"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Angles in the same segment subtended by the same arc } BC \\text{ are equal:} &\\\\"
            f"\\angle BAC &= \\angle BEC \\\\"
            f"&= {round(self.angle_bec, 10)}^\\circ \\\\"
            "\\text{2. Using the given value for } \\angle DAB \\text{, we calculate } \\angle DAC: &\\\\"
            f"\\angle DAC &= \\angle DAB - \\angle BAC \\\\"
            f"&= {round(self.angle_dab, 10)}^\\circ - {round(self.angle_bec, 10)}^\\circ \\\\"
            f"&= {round(self.angle_dab - self.angle_bec, 10)}^\\circ \\\\"
            "\\text{3. Angles in the same segment subtended by arc } DC \\text{ are equal:} &\\\\"
            f"\\angle DBC &= \\angle DAC \\\\"
            f"&= {round(self.angle_dab - self.angle_bec, 10)}^\\circ \\\\"
            "\\text{4. By the Alternate Segment Theorem, the angle between the tangent } FG \\text{ and chord } CD \\text{ is equal to } \\angle DBC: &\\\\"
            f"\\angle DCG &= \\angle DBC \\\\"
            f"&= {self.answer}^\\circ"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')

        r = 1.0
        circle = plt.Circle((0, 0), r, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        # Global rotation to vary the entire figure's orientation
        base_rot = rnd.uniform(0, 360)
        
        # Define vertex angles with jitter while maintaining relative order
        # Angles roughly correspond to: A(Left), B(Bottom), C(Bottom-Right), D(Top), E(Top-Left)
        ang_a = (190 + randrange_float(-12, 12, 0.1) + base_rot) % 360
        ang_b = (265 + randrange_float(-12, 12, 0.1) + base_rot) % 360
        ang_c = (335 + randrange_float(-12, 12, 0.1) + base_rot) % 360
        ang_d = (85 + randrange_float(-12, 12, 0.1) + base_rot) % 360
        ang_e = (140 + randrange_float(-10, 10, 0.1) + base_rot) % 360
        
        pts = {
            'A': np.array([r * np.cos(np.radians(ang_a)), r * np.sin(np.radians(ang_a))]),
            'B': np.array([r * np.cos(np.radians(ang_b)), r * np.sin(np.radians(ang_b))]),
            'C': np.array([r * np.cos(np.radians(ang_c)), r * np.sin(np.radians(ang_c))]),
            'D': np.array([r * np.cos(np.radians(ang_d)), r * np.sin(np.radians(ang_d))]),
            'E': np.array([r * np.cos(np.radians(ang_e)), r * np.sin(np.radians(ang_e))])
        }

        # Chords: Segments ED and AE are removed as requested
        chords = [('A','B'), ('B','C'), ('C','D'), ('B','D'), ('A','D'), ('E','B'), ('E','C')]
        for p1, p2 in chords:
            ax.plot([pts[p1][0], pts[p2][0]], [pts[p1][1], pts[p2][1]], color='black', lw=1)

        # Tangent FG at C (perpendicular to radius OC)
        tangent_angle = ang_c + 90
        # Dynamic placement of F and G
        f_pt = pts['C'] + np.array([0.8 * np.cos(np.radians(tangent_angle + 180)), 0.8 * np.sin(np.radians(tangent_angle + 180))])
        g_pt = pts['C'] + np.array([0.8 * np.cos(np.radians(tangent_angle)), 0.8 * np.sin(np.radians(tangent_angle))])
        ax.plot([f_pt[0], g_pt[0]], [f_pt[1], g_pt[1]], color='black', lw=1.5)

        # Dynamic Point Labels (placed radially outward from center)
        for label, pt in pts.items():
            rad_angle = np.arctan2(pt[1], pt[0])
            lx, ly = pt[0] + 0.15 * np.cos(rad_angle), pt[1] + 0.15 * np.sin(rad_angle)
            ax.text(lx, ly, label, fontsize=20, ha='center', va='center', style='italic')
        
        # Tangent Labels (F and G)
        ax.text(f_pt[0] + 0.1 * np.cos(np.radians(tangent_angle + 180)), 
                f_pt[1] + 0.1 * np.sin(np.radians(tangent_angle + 180)), 'F', fontsize=18, ha='center')
        ax.text(g_pt[0] + 0.1 * np.cos(np.radians(tangent_angle)), 
                g_pt[1] + 0.1 * np.sin(np.radians(tangent_angle)), 'G', fontsize=18, ha='center')

        # Angle Markings (Removed int() casting to show decimals)
        # ADB Angle Marking (angle at vertex D)
        self._draw_angle(ax, pts['D'], pts['B'], pts['A'], f"{self.angle_adb:.2f}°", radius=0.25)
        # BEC Angle Marking (angle at vertex E)
        self._draw_angle(ax, pts['E'], pts['C'], pts['B'], f"{self.angle_bec:.2f}°", radius=0.25)
        # DAB Angle Marking (angle at vertex A)
        self._draw_angle(ax, pts['A'], pts['B'], pts['D'], f"{self.angle_dab:.2f}°", radius=0.3)

        # "Not to Scale" note positioned relative to the plot area
        plt.text(1.2, 1.3, "NOT TO\nSCALE", fontsize=12, ha='center', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

    def _draw_angle(self, ax, p_vertex, p1, p2, text, radius=0.3):
        ang1 = get_angle(p_vertex, p1)
        ang2 = get_angle(p_vertex, p2)
        
        if abs(ang1 - ang2) > 180:
            if ang1 > ang2: ang2 += 360
            else: ang1 += 360
        
        theta1, theta2 = min(ang1, ang2), max(ang1, ang2)
        arc = patches.Arc(p_vertex, radius*2, radius*2, theta1=theta1, theta2=theta2, color='black', lw=1)
        ax.add_patch(arc)
        
        mid_ang = np.radians((theta1 + theta2) / 2)
        tx = p_vertex[0] + (radius + 0.15) * np.cos(mid_ang)
        ty = p_vertex[1] + (radius + 0.15) * np.sin(mid_ang)
        ax.text(tx, ty, text, fontsize=14, ha='center', va='center')
        
class Mat050:
    def __init__(self):
        self.r = round(randrange_float(10.0, 20.0, 0.01), 2)
        # Ensure chord length is logically valid (less than diameter)
        self.chord_len = round(randrange_float(12.0, self.r * 1.8, 0.01), 2)
        
        # d = sqrt(r^2 - (chord_len/2)^2)
        half_chord = self.chord_len / 2
        self.answer = round(math.sqrt(self.r**2 - half_chord**2), 2)

        self.description = (
            f"The diagram shows a circle with center $O$. The radius and chord $AB$ have lengths as shown in the image. "
            f"Calculate the shortest distance from the center of the circle to the chord."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems II"
        self.source = "Original" # Complies with syllabus"
        self.curriculum = "IGCSE"
        self.question_type = "Short Answer"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Radius, }} r &= {round(self.r, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Chord length, }} AB &= {round(self.chord_len, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Let }} d \\text{{ be the shortest distance from the center }} O \\text{{ to the chord }} AB. &\\\\"
            f"\\text{{The perpendicular bisector of a chord passes through the center:}} &\\\\"
            f"\\text{{Half-chord length, }} h &= \\frac{{AB}}{{2}}\\\\"
            f"&= \\frac{{{round(self.chord_len, 10)}}}{{2}}\\\\"
            f"&= {round(self.chord_len / 2, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Using Pythagoras' Theorem in the resulting right-angled triangle:}} &\\\\"
            f"r^2 &= d^2 + h^2\\\\"
            f"d &= \\sqrt{{r^2 - h^2}}\\\\"
            f"&= \\sqrt{{{round(self.r, 10)}^2 - {round(self.chord_len / 2, 10)}^2}}\\\\"
            f"&= \\sqrt{{{round(self.r**2, 10)} - {round((self.chord_len / 2)**2, 10)}}}\\\\"
            f"&= \\sqrt{{{round(self.r**2 - (self.chord_len / 2)**2, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        limit = 1.3
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.axis('off')

        vis_r = 1.0
        circle = plt.Circle((0, 0), vis_r, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        rotation = rnd.uniform(0, 360)
        rad = np.radians(rotation)
        rot_mat = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])

        d_plot = (self.answer / self.r) * vis_r
        h = math.sqrt(max(0, vis_r**2 - d_plot**2))
        
        p1_local = np.array([h, d_plot])
        p2_local = np.array([-h, d_plot])
        
        # Apply rotation to chord endpoints
        p1 = rot_mat @ p1_local
        p2 = rot_mat @ p2_local

        rand_ang_r = np.radians(rnd.uniform(0, 360))
        pr_local = np.array([vis_r * np.cos(rand_ang_r), vis_r * np.sin(rand_ang_r)])
        pr = rot_mat @ pr_local

        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='black', lw=2) # Chord AB
        ax.plot([0, pr[0]], [0, pr[1]], color='black', lw=1.5)

        centroid = np.array([0, 0])
        put_vertex_label(ax, centroid, "O", pr, 0.12) # Offset O away from the radius line
        put_vertex_label(ax, p1, "A", centroid, 0.12)
        put_vertex_label(ax, p2, "B", centroid, 0.12)

        # Radius label
        r_mid = pr * 0.5
        ax.text(r_mid[0], r_mid[1] + 0.05, f"{self.r:.2f} cm", fontsize=14, fontweight='bold')
        
        # Chord label (offset from midpoint of chord)
        mid_chord = (p1 + p2) / 2
        # Offset label outward from the center
        c_label_offset = mid_chord / np.linalg.norm(mid_chord) * 0.15 if np.linalg.norm(mid_chord) > 0 else [0, 0.15]
        c_label_pos = mid_chord + c_label_offset
        ax.text(c_label_pos[0], c_label_pos[1], f"{self.chord_len:.2f} cm", 
                fontsize=14, ha='center', fontweight='bold')

        plt.text(1.1, 1.1, "NOT TO\nSCALE", fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
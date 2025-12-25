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
        
        self.speed = round(self.distance_meeting / (self.travel_time_hour + self.travel_time_minute / 60.0), 10)  # km/h
                
        self.answer = f"{self.leave_office_hour}:{self.leave_office_minute:02d}"

        self.description = (
            f"Ky cycles from his office to a meeting and back again. The travel graph shows his time at the meeting and his journey back. Ky cycles from his office to the meeting at a constant speed of {self.speed} km/h. What time does Ky leave his office?"
        )

        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs in practical situations"
        self.source = "Adapted from IGCSE June 2025 Question Paper 11"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Identify meeting arrival time from the graph:} &\\\\"
            f"\\text{{Arrival at meeting}} &= {self.arrive_meeting_hour:02d}:{self.arrive_meeting_minute:02d}\\\\"
            f"\\text{{Distance from office to meeting}} &= {self.distance_meeting}\\,\\text{{km}}\\\\"
            "\\text{2. Calculate travel time to the meeting:} &\\\\"
            "\\text{Time} &= \\frac{\\text{Distance}}{\\text{Speed}}\\\\"
            f"&= \\frac{{{self.distance_meeting}\\,\\text{{km}}}}{{{round(self.speed, 10)}\\,\\text{{km/h}}}}\\\\"
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
        plt.close()

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
        target_eq = f"x^2{fmt_poly(self.b, 'x')}{fmt_poly(self.c - self.d, '')} = 0"
        
        self.description = (
            f"The graph of a quadratic function is shown on the grid. "
            f"By first determining the equation of the graph, use it to solve ${target_eq}$."
        )
        
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 12"
        self.curriculum = "IGCSE"

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
        
        print(self.reasoning)

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
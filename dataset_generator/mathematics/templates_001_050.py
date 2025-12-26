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
        target_eq_str = f"{fmt_poly(T_A, 'x^3', True)}{fmt_poly(T_B, 'x^2')}{fmt_poly(T_C, 'x')}{fmt_poly(T_D, '')} = 0"
        
        self.answer = " or ".join([f"x = {r}" for r in self.target_roots])
        
        self.description = f"By drawing a suitable straight line on the grid, solve the equation ${target_eq_str}$."
        self.topic = "Algebra and Graphs"
        self.subtopic = "Graphs of functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 41"
        self.curriculum = "IGCSE"
        
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
        self.answer = f"{round(self.alpha, 2) if not self.alpha.is_integer() else int(self.alpha)}"
        
        self.description = f"The diagram shows a quadrilateral with sides of equal length. Work out the value of $a$."
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from IGCSE March 2025 Question Paper 13"
        self.curriculum = "IGCSE"

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
        
        self.answer = int(self.target_angle) if self.target_angle.is_integer() else self.target_angle

        self.description = (
            f"$BDC$ is a straight line, $AB = AC$, angle $ABD = {round(self.angle_B, 2)}^\\circ$ "
            f"and angle $ADC = {round(self.angle_ADC, 2)}^\\circ$. \\\\ Work out angle $DAC$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Angles"
        self.source = "Adapted from 2025-specimen-paper-2"
        self.curriculum = "IGCSE"
        
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
        DCG = 180 - GEA
        EIC = 180 - FEA
        ICE = 180 - EIC - FEG

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
        ax.text(C[0], C[1] - label_offset, 'C', fontsize=12, ha='center')
        ax.text(D[0], D[1] + label_offset, 'D', fontsize=12)
        ax.text(E[0] - label_offset, E[1] - label_offset, 'E', fontsize=12)
        ax.text(F[0], F[1] + label_offset, 'F', fontsize=12)
        ax.text(G[0] + label_offset, G[1], 'G', fontsize=12)

        # Parallel markings (Arrows)
        ax.annotate('', xy=B + (A-B)*0.2, xytext=B + (A-B)*0.15, arrowprops=dict(arrowstyle='->', lw=1.5))
        ax.annotate('', xy=D + (G_end-D)*0.4, xytext=D + (G_end-D)*0.35, arrowprops=dict(arrowstyle='->', lw=1.5))

        # Add Angle Arcs and Labels
        r_label = 1  # Distance to push text away from vertex
        
        # Known angle at I
        t1, t2 = FEG+180, 360+BEA
        mid = np.radians((t1+t2) / 2)
        ax.add_patch(patches.Arc(I, 1.2, 1.2, theta1=t1, theta2=t2, color='black'))
        ax.text(I[0] + r_label*np.cos(mid), I[1] + r_label*np.sin(mid), 
                f'{self.angle_top:.2f}°', fontsize=10, ha='center', va='center')

        # Known angle at E
        t1, t2 = BEA, GEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(E, 1.2, 1.2, theta1=t1, theta2=t2, color='black'))
        ax.text(E[0] + r_label*np.cos(mid), E[1] + r_label*np.sin(mid), 
                f'{self.angle_ext:.2f}°', fontsize=10, ha='center', va='center')
        
        # Angle a at C
        t1, t2 = 180+BEA, 180+GEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(C, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(C[0] + r_label*np.cos(mid), C[1] + r_label*np.sin(mid), 
                '$a°$', fontsize=11, ha='center', va='center')
        
        # Angle b at C
        t1, t2 = GEA, 180+DIC
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(C, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(C[0] + r_label*np.cos(mid), C[1] + r_label*np.sin(mid), 
                '$b°$', fontsize=11, ha='center', va='center')
        
        # Angle c at E
        t1, t2 = GEA, FEA
        mid = np.radians((t1 + t2) / 2)
        ax.add_patch(patches.Arc(E, 1.0, 1.0, theta1=t1, theta2=t2, color='black'))
        ax.text(E[0] + r_label*np.cos(mid), E[1] + r_label*np.sin(mid), 
                '$c°$', fontsize=11, ha='center', va='center')

        # NOT TO SCALE label
        ax.text(0.95, 0.9, 'NOT TO\nSCALE', transform=ax.transAxes, ha='center', fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close(fig)
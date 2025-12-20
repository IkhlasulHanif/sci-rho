import numpy as np
import random as rnd
import math
import os
import matplotlib.pyplot as plt
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
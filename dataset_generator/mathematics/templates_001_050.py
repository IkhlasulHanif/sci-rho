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
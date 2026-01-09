import numpy as np
import pandas as pd
import random as rnd
import os
import matplotlib.pyplot as plt
from mathematics.helper import *

# target folder : "root/dataset/mathematics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "mathematics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Mat101:
    
    def __init__(self):
        # Randomized Variables
        self.colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
        self.total_spins = rnd.choice([100, 200, 250, 400, 500])
        
        # Generate random frequencies that sum up to total_spins
        # We create 5 random numbers, normalize them, then scale to total_spins
        raw_freqs = [rnd.random() for _ in range(5)]
        sum_raw = sum(raw_freqs)
        self.frequencies = [int((f / sum_raw) * self.total_spins) for f in raw_freqs]
        
        # Adjust the last frequency to ensure the sum is exactly total_spins due to rounding
        self.frequencies[-1] = self.total_spins - sum(self.frequencies[:-1])
        
        # Select a target color for the question
        self.target_index = rnd.randint(0, 4)
        self.target_color = self.colors[self.target_index]
        self.target_freq = self.frequencies[self.target_index]
        
        # Relative frequency = Frequency of Event / Total Trials
        relative_frequency = self.target_freq / self.total_spins
        self.answer = round(relative_frequency, 3)

        self.description = (
            f"Based on the results in the figure, what is the relative frequency "
            f"that the spinner lands on the color {self.target_color}? "
            "Give your answer correct to 3 decimal places."
        )

        self.topic = "Probability"
        self.subtopic = "Relative and expected frequencies"
        self.source = "Adapted from Cambridge IGCSE Mathematics (0580)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency of {self.target_color}}} &= {self.target_freq}\\\\"
            f"\\text{{Total spins}} &= {self.total_spins}\\\\"
            f"\\text{{Relative Frequency}} &= \\frac{{\\text{{Frequency of {self.target_color}}}}}{{\\text{{Total spins}}}}\\\\"
            f"&= \\frac{{{self.target_freq}}}{{{self.total_spins}}}\\\\"
            f"&= {round(self.target_freq / self.total_spins, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create a DataFrame for the table
        data = {
            'Color': self.colors,
            'Frequency': self.frequencies
        }
        df = pd.DataFrame(data)

        # Plotting the table
        fig, ax = plt.subplots(figsize=(6, 2)) # Adjust size as needed
        ax.axis('off')
        ax.axis('tight')
        
        # Create table
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        
        # Style the table
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 1.5) # Scale width and height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat102:
    
    def __init__(self):
        # We need 6 numbers that sum to 100 to represent the frequencies
        # We will generate random weights and normalize them
        weights = [rnd.randint(1, 10) for _ in range(6)]
        total_weight = sum(weights)
        
        # Calculate initial frequencies based on weights
        self.frequencies = [int((w / total_weight) * 100) for w in weights]
        
        # Adjust to ensure the sum is exactly 100 (distribute the remainder)
        remainder = 100 - sum(self.frequencies)
        for i in range(remainder):
            self.frequencies[i % 6] += 1
            
        self.faces = [1, 2, 3, 4, 5, 6]
        
        # Select a target face for the question (e.g., face 6)
        target_face = 6
        target_freq = self.frequencies[target_face - 1]
        
        # Calculate the solution for the question
        total_rolls_scenario = rnd.randint(2, 10) * 100
        expected_freq = (target_freq / 100) * total_rolls_scenario

        self.answer = int(round(expected_freq, 0))

        self.description = (
            f"Using the relative frequency from the chart, calculate the expected frequency of rolling a {target_face} if the die is rolled {total_rolls_scenario} times."
        )

        self.topic = "Probability"
        self.subtopic = "Relative and expected frequencies"
        self.source = "Adapted from Edexcel GCSE Mathematics"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency of rolling a {target_face}}} &= {target_freq}\\\\"
            f"\\text{{Total initial rolls}} &= 100\\\\"
            f"\\text{{Relative frequency}} &= \\frac{{\\text{{Frequency}}}}{{\\text{{Total initial rolls}}}}\\\\"
            f"&= \\frac{{{target_freq}}}{{100}}\\\\"
            f"&= {round(target_freq / 100, 10)}\\\\"
            f"\\text{{Expected frequency}} &= \\text{{Relative frequency}} \\times \\text{{Target rolls}}\\\\"
            f"&= {round(target_freq / 100, 10)} \\times {total_rolls_scenario}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # 2. Create the Figure
        plt.figure(figsize=(8, 6))
        
        # Create bar chart
        bars = plt.bar(self.faces, self.frequencies, color='skyblue', edgecolor='black', zorder=3)
        
        # Formatting
        plt.xlabel('Die Face', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(self.faces)
        plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
        plt.ylim(0, max(self.frequencies) + 5) # Dynamic y-limit based on max value

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height}',
                    ha='center', va='bottom', fontsize=10)

        # Display the plot
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
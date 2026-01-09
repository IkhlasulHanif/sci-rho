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
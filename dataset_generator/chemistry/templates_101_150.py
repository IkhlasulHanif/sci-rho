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


class Chem101:
    """
    Topic: States of matter
    Visual: Cooling curve showing gas condensing to liquid
    Task: Determine duration of phase change
    """

    def __init__(self):
        self.start_temp = rnd.randint(95, 110)
        self.plateau_temp = rnd.randint(70, 85)
        self.end_temp = rnd.randint(55, 70)

        self.t_A = 0
        self.t_B = rnd.randint(2, 3)
        self.t_C = self.t_B + rnd.randint(3, 5)
        self.t_D = self.t_C + rnd.randint(2, 3)

        self.answer = self.t_C - self.t_B

        self.description = (
            "A gas is left to cool and forms a liquid. "
            "The graph shows how the temperature of the substance changes with time.\n\n"
            "From A to B the substance is a gas.\n"
            "From C to D the substance is a liquid.\n\n"
            "Calculate how long it takes for the substance to become completely liquid."
        )

        self.topic = "States of matter"
        self.subtopic = "Solids, liquids and gases"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Condensation occurs during the constant temperature (plateau) region of the graph.}} &\\\\"
            f"\\text{{Start time of condensation}} &= t_B = {self.t_B}\\,\\text{{minutes}}\\\\"
            f"\\text{{End time of condensation}} &= t_C = {self.t_C}\\,\\text{{minutes}}\\\\"
            f"\\text{{Duration of condensation is given by:}} &\\\\"
            f"t_{{\\text{{duration}}}} &= t_C - t_B\\\\"
            f"&= {self.t_C} - {self.t_B}\\\\"
            f"&= {round(self.t_C - self.t_B, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{minutes}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        times = [self.t_A, self.t_B, self.t_C, self.t_D]
        temps = [self.start_temp, self.plateau_temp, self.plateau_temp, self.end_temp]

        ax.plot(times, temps, 'k-', linewidth=2)
        ax.scatter(times, temps, color='black', zorder=3)

        labels = ["A", "B", "C", "D"]
        for t, temp, label in zip(times, temps, labels):
            ax.text(t, temp + 2, label, fontsize=12, fontweight='bold', ha='center')

        ax.set_xlabel("Time (minutes)", fontsize=14, fontweight='bold')
        ax.set_ylabel("Temperature (°C)", fontsize=14, fontweight='bold')
        ax.set_title("Cooling Curve of a Substance", fontsize=16, fontweight='bold')

        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_axisbelow(True)

        ax.set_xlim(self.t_A, self.t_D + 1)
        ax.set_ylim(self.end_temp - 10, self.start_temp + 10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()

class Chem102:
    """
    Topic: States of matter
    Subtopic: Diffusion
    Visual: Two chambers showing gas diffusion over time
    Task: Calculate diffusion rate
    """

    def __init__(self):
        self.distance = rnd.randint(4, 12)
        self.time = rnd.randint(2, 8)

        self.rate = self.distance / self.time
        self.answer = round(self.rate, 2)

        self.description = (
            "A gas diffuses across a chamber as shown in the diagram. "
            "The gas travels a measured distance over a period of time.\n\n"
            "Calculate the rate of diffusion of the gas."
        )

        self.topic = "States of matter"
        self.subtopic = "Diffusion"
        self.source = "GCSE Chemistry Past Papers"
        self.curriculum = "GCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance travelled}} &= {self.distance}\\,\\text{{cm}}\\\\"
            f"\\text{{Time taken}} &= {self.time}\\,\\text{{s}}\\\\"
            f"\\text{{Diffusion rate is given by:}} &\\\\"
            f"\\text{{Rate}} &= \\frac{{\\text{{distance}}}}{{\\text{{time}}}}\\\\"
            f"&= \\frac{{{self.distance}}}{{{self.time}}}\\\\"
            f"&= {round(self.distance / self.time, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):

        fig, ax = plt.subplots(figsize=(10, 7))

        chamber = Rectangle((0, 0), 10, 4, fill=False, linewidth=2)
        ax.add_patch(chamber)

        divider_x = 3
        ax.plot([divider_x, divider_x], [0, 4], linestyle='--', color='black')

        for _ in range(20):
            x = rnd.uniform(0.3, divider_x - 0.3)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black'))

        for _ in range(15):
            x = rnd.uniform(divider_x + 0.3, 9.7)
            y = rnd.uniform(0.3, 3.7)
            ax.add_patch(Circle((x, y), 0.1, color='black'))

        ax.arrow(divider_x, 2, 3, 0, head_width=0.3, head_length=0.4, fc='black', ec='black')

        ax.text(1.5, 4.3, "High concentration", ha='center', fontsize=11)
        ax.text(7.5, 4.3, "Low concentration", ha='center', fontsize=11)

        ax.text(5, -0.7, f"Distance travelled = {self.distance} cm", ha='center', fontsize=11)
        ax.text(5, -1.3, f"Time taken = {self.time} s", ha='center', fontsize=11)

        ax.set_xlim(-1, 11)
        ax.set_ylim(-2, 5.5)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.set_title("Diffusion of a Gas in a Chamber", fontsize=16, fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=150, bbox_inches='tight')
        plt.close()
import random as rnd
import os
import matplotlib.pyplot as plt

from PIL import Image
from physics.helper import *

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

# TODO: REMOVE THIS EXAMPLE LATER
class Phy051:

    def __init__(self):
        self.load_mass = rnd.randint(5, 20) * 10
        self.height = rnd.randint(6, 10) * 5
        self.energy_transfered = self.load_mass * self.height * 10 # assume g = 10 m/s²
        self.efficiency =  rnd.choice([20, 25, 40, 50])
        self.energy_used = self.energy_transfered / (self.efficiency / 100)
        self.answer = round(self.efficiency, 2)
        
        self.description = (
            f"A crane is used to lift a load to the height shown in the diagram. "
            f"The motor of the crane uses {self.energy_used} J of energy. "
            f"The efficiency of the motor is ... % (assume g = 10 m/s²)"
        )
        self.topic = "Motion, forces and energy"
        self.subtopic = "Energy, work and power"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of load}} &= {self.load_mass}\\,\\text{{kg}}\\\\"
            f"\\text{{Height lifted}} &= {self.height}\\,\\text{{m}}\\\\"
            f"g &= 10\\,\\text{{m/s}}^2\\\\"
            f"\\text{{Energy transferred to the load:}} &\\\\"
            f"E_\\text{{useful}} &= m g h\\\\"
            f"&= ({self.load_mass})({10})({self.height})\\\\"
            f"&= {round(self.energy_transfered, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Energy supplied by the motor:}} &\\\\"
            f"E_\\text{{input}} &= {round(self.energy_used, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Efficiency is given by:}} &\\\\"
            f"\\eta &= \\frac{{E_\\text{{useful}}}}{{E_\\text{{input}}}} \\times 100\\\\"
            f"&= \\frac{{{round(self.energy_transfered, 10)}}}{{{round(self.energy_used, 10)}}} \\times 100\\\\"
            f"&= {self.answer}\\,\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy019temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(212, 454, f"{self.load_mass} kg", fontsize=8)
        ax.text(351, 341, f"{self.height} m", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()
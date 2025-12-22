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

class Mat054:
    
    def __init__(self):
        # Left Edge (Total Height)
        self.H = rnd.randint(10, 20) # in cm
        
        # Bottom Edge (Total Width)
        self.W = rnd.randint(10, 20) # in cm
        
        # Top Edge (Width of the top vertical stem) - must be thinner than total width
        self.w_top = rnd.randint(4, self.W - 4) # in cm
        
        # Inner Vertical Edge (The length of the vertical cut)
        # This determines the height of the "foot" -> h_foot = H - h_inner
        self.h_inner = rnd.randint(4, self.H - 4) # in cm
        self.h_foot = self.H - self.h_inner # in cm

        # Let's split into two vertical rectangles:
        #   Part A (Left full height bar): w_top * H
        #   Part B (Right small foot): (W - w_top) * h_foot        
        self.answer = (self.w_top * self.H) + ((self.W - self.w_top) * self.h_foot)

        self.description = (
            f"Calculate the total area of the shape shown."
        )

        self.topic = "Mensuration"
        self.subtopic = "Area and perimeter"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{We split the shape into two rectangles:}} &\\\\"
            f"\\text{{1. Left vertical rectangle (Part A):}} &\\\\"
            f"\\text{{Width}}_A &= w_{{\\text{{top}}}} = {self.w_top}\\,\\text{{cm}}\\\\"
            f"\\text{{Height}}_A &= H = {self.H}\\,\\text{{cm}}\\\\"
            f"A_A &= {self.w_top} \\times {self.H} = {self.w_top * self.H}\\,\\text{{cm}}^2\\\\"
            f"\\text{{2. Right bottom rectangle (Part B):}} &\\\\"
            f"\\text{{Width}}_B &= W - w_{{\\text{{top}}}} = {self.W} - {self.w_top} = {self.W - self.w_top}\\,\\text{{cm}}\\\\"
            f"\\text{{Height}}_B &= h_{{\\text{{foot}}}} = {self.h_foot}\\,\\text{{cm}}\\\\"
            f"A_B &= ({self.W - self.w_top}) \\times {self.h_foot} = {(self.W - self.w_top) * self.h_foot}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Total Area:}} &\\\\"
            f"A &= A_A + A_B\\\\"
            f"&= {self.w_top * self.H} + {(self.W - self.w_top) * self.h_foot}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Vertices for the Polygon
        # Starting from bottom-left (0,0) and going counter-clockwise
        vertices = [
            (0, 0),                         # Bottom-left
            (self.W, 0),                    # Bottom-right corner
            (self.W, self.h_foot),          # Top of the foot (right side)
            (self.w_top, self.h_foot),      # Inner corner
            (self.w_top, self.H),           # Top-right of the vertical stem
            (0, self.H)                     # Top-left
        ]

        # Create the Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Draw the shape
        # 'ec' is edge color, 'fc' is face color (fill), 'lw' is line width
        shape = patches.Polygon(vertices, closed=True, ec='black', fc='#d0e0ff', lw=2)
        ax.add_patch(shape)

        # Add Labels (Dynamic Positioning)
        # We use simple offsets to place text near the middle of the lines
        
        # Label: Left Edge (Total Height)
        ax.text(-1, self.H/2, f"{self.H} cm", ha='right', va='center', fontsize=12, fontweight='bold', color='darkred')
        
        # Label: Top Edge (Width of stem)
        ax.text(self.w_top/2, self.H + 0.5, f"{self.w_top} cm", ha='center', va='bottom', fontsize=12, fontweight='bold', color='darkred')
        
        # Label: Bottom "foot" width (Total Width)
        ax.text(self.W/2, -1, f"{self.W} cm", ha='center', va='top', fontsize=12, fontweight='bold', color='darkred')
        
        # Label: Inner Vertical Edge
        # Located at x = w_top, vertical mid-point of the inner edge
        # We place it slightly to the right of the line
        inner_mid_y = self.h_foot + (self.h_inner / 2)
        ax.text(self.w_top + 0.5, inner_mid_y, f"{self.h_inner} cm", ha='left', va='center', fontsize=12, fontweight='bold', color='darkred')

        # 5. Formatting the Graph to look like a Diagram
        ax.set_aspect('equal')
        
        # Set limits with some padding
        ax.set_xlim(-3, self.W + 3)
        ax.set_ylim(-3, self.H + 3)
        
        # Remove axes (ticks and spines) for a clean geometry look
        ax.axis('off')
        
        plt.title("Calculate the Area of the Composite Shape", fontsize=14, pad=20)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
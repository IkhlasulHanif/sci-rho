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
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

class Mat055:
    
    def __init__(self):
        # Randomized Variables
        # We use Pythagorean triples (a, b, c) to ensure the 'slant' and 'height'
        # create a nice integer geometry, making the numbers cleaner for students.
        # Triple format: (x_offset, height, slant_side)
        self.triples = [
            (3, 4, 5),
            (5, 12, 13),
            (6, 8, 10),
            (7, 24, 25),
            (8, 15, 17),
            (9, 40, 41),
        ]
        
        # Pick a random triple
        self.x_offset, self.h, self.s = rnd.choice(self.triples)
        
        # Randomize base (b)
        # Ensure base is larger than the offset to maintain standard shape
        self.b = rnd.randint(self.x_offset + 6, self.x_offset + 16)

        self.answer = self.b * self.h

        self.description = (
            f"Calculate the area of the parallelogram."
        )

        self.topic = "Mensuration"
        self.subtopic = "Area and perimeter"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Base }} (b) &= {self.b} \\\\"
            f"\\text{{Height }} (h) &= {self.h} \\\\"
            f"\\text{{Area}} &= b \\times h \\\\"
            f"&= {self.b} \\times {self.h} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Vertices for Plotting
        # Coordinates: (x, y)
        vertices = np.array([
            [0, 0],                                 # Bottom-left
            [self.b, 0],                            # Bottom-right
            [self.b + self.x_offset, self.h],       # Top-right
            [self.x_offset, self.h]                 # Top-left
        ])
        
        # Create Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Draw the main Parallelogram shape
        polygon = patches.Polygon(vertices, closed=True, 
                                facecolor='#E0F7FA', edgecolor='black', linewidth=2)
        ax.add_patch(polygon)
        
        # Draw Perpendicular Height (Dotted Line)
        # Dropping from Top-Left vertex (x_offset, h) straight down to (x_offset, 0)
        ax.plot([self.x_offset, self.x_offset], [0, self.h], color='red', linestyle='--', linewidth=1.5)
        
        # Add Right Angle Marker
        rect_size = min(self.b, self.h) * 0.05
        rect = patches.Rectangle((self.x_offset, 0), rect_size, rect_size, 
                                linewidth=1, edgecolor='red', facecolor='none')
        ax.add_patch(rect)
        
        # Add Labels
        
        # Label Base
        ax.text(self.b / 2, -self.h * 0.15, f"Base = {self.b}", 
                ha='center', va='top', fontsize=12, fontweight='bold')
        
        # Label Slant Side
        # Place label near the midpoint of the left slant edge
        ax.text(self.x_offset / 2 - 0.5, self.h / 2, f"Slant = {self.s}", 
                ha='right', va='center', fontsize=12)
        
        # Label Height
        ax.text(self.x_offset + 0.2, self.h / 2, f"h = {self.h}", 
                ha='left', va='center', color='red', fontsize=12)
        
        # Formatting the canvas
        ax.set_xlim(-2, self.b + self.x_offset + 2)
        ax.set_ylim(-1, self.h + 2)
        ax.set_aspect('equal')
        ax.axis('off')  # Hide standard axes
        # plt.title("Example 2: Parallelogram (Area vs Perimeter)", fontsize=14)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat056:
    
    def __init__(self):
        # We ensure bottom_b is significantly larger than top_a for a clear shape
        self.top_a = rnd.randint(4, 10)       # Top parallel side (e.g., 4 to 9 cm)
        self.bottom_b = self.top_a + rnd.randint(4, 10) # Bottom side (ensures it's wider)
        self.height_h = rnd.randint(4, 10)    # Vertical height
        
        # Randomize the "skew" (how far left/right the top is shifted)
        # 0.5 centers it perfectly (Isosceles). 
        # slightly randomizing this makes it look more distinct.
        self.skew_factor = rnd.uniform(0.3, 0.7) 
        self.x_offset = (self.bottom_b - self.top_a) * self.skew_factor

        self.answer = 0.5 * (self.top_a + self.bottom_b) * self.height_h # in cm^2

        self.description = (
            f"Calculate the area of the trapezium."
        )

        self.topic = "Mensuration"
        self.subtopic = "Area and perimeter"
        self.source = "Adapted from Complete Mathematics for Cambridge IGCSE (David Rayner)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Top side }} (a) &= {self.top_a}\\,\\text{{cm}}\\\\"
            f"\\text{{Bottom side }} (b) &= {self.bottom_b}\\,\\text{{cm}}\\\\"
            f"\\text{{Height }} (h) &= {self.height_h}\\,\\text{{cm}}\\\\"
            f"\\text{{Area}} &= \\frac{{1}}{{2}}(a + b)h\\\\"
            f"&= \\frac{{1}}{{2}}({self.top_a} + {self.bottom_b}) \\times {self.height_h}\\\\"
            f"&= 0.5 \\times ({self.top_a + self.bottom_b}) \\times {self.height_h}\\\\"
            f"&= {round(0.5 * (self.top_a + self.bottom_b), 10)} \\times {self.height_h}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Vertices (Counter-clockwise from bottom-left)
        # (0,0) -> (b, 0) -> (x_offset + a, h) -> (x_offset, h)
        vertices = np.array([
            [0, 0],
            [self.bottom_b, 0],
            [self.x_offset + self.top_a, self.height_h],
            [self.x_offset, self.height_h]
        ])

        # Create Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Draw the Trapezium
        trapezium = patches.Polygon(vertices, closed=True, 
                                    edgecolor='black', facecolor='#e6f2ff', 
                                    linewidth=2)
        ax.add_patch(trapezium)

        # Annotations
        
        # Label: Bottom side (b)
        ax.text(self.bottom_b / 2, -0.05 * self.height_h, f"{self.bottom_b} cm", 
                ha='center', va='top', fontsize=12, fontweight='bold')

        # Label: Top side (a)
        ax.text(self.x_offset + self.top_a / 2, self.height_h + 0.05 * self.height_h, f"{self.top_a} cm", 
                ha='center', va='bottom', fontsize=12, fontweight='bold')

        # Draw Height Indicator (Dashed Line)
        # We drop a line from the top-left vertex (index 3) straight down
        height_x = self.x_offset
        ax.plot([height_x, height_x], [0, self.height_h], color='red', linestyle='--', linewidth=1.5)
        
        # Label: Height (h) - placed slightly to the left of the dashed line
        ax.text(height_x - 0.2, self.height_h / 2, f"{self.height_h} cm", 
                ha='right', va='center', color='red', fontsize=12, fontweight='bold')

        # Add a small right-angle symbol at the base of the height line
        rect_size = min(self.bottom_b, self.height_h) * 0.05
        rect = patches.Rectangle((height_x, 0), rect_size, rect_size, 
                                linewidth=1, edgecolor='red', facecolor='none')
        ax.add_patch(rect)

        # Styling
        ax.set_aspect('equal')
        ax.axis('off') # Turn off X/Y axis for clean look
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat057:
    
    def __init__(self):
        # Inner rectangle (Lawn) dimensions
        self.inner_length = rnd.randint(5, 12)
        self.inner_width = rnd.randint(3, 8)
        
        # Path width (uniform around the lawn)
        self.path_width = round(rnd.uniform(0.5, 2.0), 1)
        
        # Calculate outer dimensions
        self.outer_length = self.inner_length + 2 * self.path_width
        self.outer_width = self.inner_width + 2 * self.path_width

        self.answer = round(
            self.outer_length * self.outer_width -\
            self.inner_length * self.inner_width,
            2
        )

        self.description = (
            f"Calculate the area of the path."
        )

        self.topic = "Mensuration"
        self.subtopic = "Area and perimeter"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Inner Area}} &= {self.inner_length} \\times {self.inner_width} = {round(self.inner_length * self.inner_width, 10)}\\\\"
            f"\\text{{Outer Length}} &= {self.inner_length} + 2({self.path_width}) = {round(self.outer_length, 10)}\\\\"
            f"\\text{{Outer Width}} &= {self.inner_width} + 2({self.path_width}) = {round(self.outer_width, 10)}\\\\"
            f"\\text{{Outer Area}} &= {round(self.outer_length, 10)} \\times {round(self.outer_width, 10)} = {round(self.outer_length * self.outer_width, 10)}\\\\"
            f"\\text{{Path Area}} &= \\text{{Outer Area}} - \\text{{Inner Area}}\\\\"
            f"&= {round(self.outer_length * self.outer_width, 10)} - {round(self.inner_length * self.inner_width, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Define colors
        lawn_color = '#90EE90'  # LightGreen
        path_color = '#D3D3D3'  # LightGray
        
        # Center coordinates
        center_x, center_y = 0, 0
        
        # Draw Outer Rectangle (Path base)
        outer_rect = patches.Rectangle(
            (center_x - self.outer_length/2, center_y - self.outer_width/2),
            self.outer_length, self.outer_width,
            edgecolor='black',
            facecolor=path_color,
            linewidth=2
        )
        ax.add_patch(outer_rect)
        
        # Draw Inner Rectangle (Lawn) on top
        inner_rect = patches.Rectangle(
            (center_x - self.inner_length/2, center_y - self.inner_width/2),
            self.inner_length, self.inner_width,
            edgecolor='black',
            facecolor=lawn_color,
            linewidth=2
        )
        ax.add_patch(inner_rect)
        
        # Add Text Labels
        ax.text(center_x, center_y, 'Lawn\n(Inner)', 
                ha='center', va='center', fontsize=12, fontweight='bold', color='darkgreen')
        
        ax.text(center_x, center_y + self.inner_width/2 + self.path_width/2, 'Path', 
                ha='center', va='center', fontsize=12, fontweight='bold', color='black')

        # Add Dimension Annotations
        
        # Outer Length (Bottom)
        ax.annotate('', xy=(-self.outer_length/2, -self.outer_width/2 - 0.5), 
                    xytext=(self.outer_length/2, -self.outer_width/2 - 0.5),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(center_x, -self.outer_width/2 - 1.2, f'Outer Length = {self.outer_length:.1f}', 
                ha='center', va='center')

        # Outer Width (Left)
        ax.annotate('', xy=(-self.outer_length/2 - 0.5, -self.outer_width/2), 
                    xytext=(-self.outer_length/2 - 0.5, self.outer_width/2),
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(-self.outer_length/2 - 1.2, center_y, f'Outer Width = {self.outer_width:.1f}', 
                ha='center', va='center', rotation=90)
        
        # Inner Dimensions (Inside)
        ax.text(center_x, center_y - self.inner_width/4, f'{self.inner_length} x {self.inner_width}', 
                ha='center', va='center', fontsize=10, color='darkgreen')

        # Path Width indicator (Right side)
        # Draw a line spanning the path width
        ax.annotate('', xy=(self.inner_length/2, 0), xytext=(self.outer_length/2, 0),
                    arrowprops=dict(arrowstyle='<->', color='blue', linewidth=1.5))
        ax.text((self.inner_length/2 + self.outer_length/2)/2, 0.8, f'Path Width\n{self.path_width}', 
                ha='center', va='bottom', color='blue', fontsize=9)
        
        # Set plot limits with margin
        margin = 3
        ax.set_xlim(-self.outer_length/2 - margin, self.outer_length/2 + margin)
        ax.set_ylim(-self.outer_width/2 - margin, self.outer_width/2 + margin)
        ax.set_aspect('equal')
        ax.axis('off') # Turn off standard axes
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat058:
    
    def __init__(self):
        # Constraints are applied to ensure the shape looks proportional
        self.bottom_edge = rnd.randint(12, 20)  # Total Width
        self.height = rnd.randint(10, 15)       # Left/Right Height
        
        # Inner width (notch width) must be less than bottom_edge
        self.inner_width = rnd.randint(4, self.bottom_edge - 4)
        
        # Depth of U must be less than height
        self.depth = rnd.randint(3, self.height - 3)
        
        # Calculate widths of the top "legs"
        self.remaining_width = self.bottom_edge - self.inner_width
        self.left_leg_width = rnd.randint(2, self.remaining_width - 2)
        self.right_leg_width = self.remaining_width - self.left_leg_width

        self.answer = 2 * (self.bottom_edge + self.height + self.depth)

        self.description = (
            f"Calculate the perimeter of the shape."
        )

        self.topic = "Mensuration"
        self.subtopic = "Area and perimeter"
        self.source = "Common style in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Perimeter}} &= 2 \\times (\\text{{Width}} + \\text{{Height}} + \\text{{Depth}}) \\\\"
            f"&= 2 \\times ({self.bottom_edge} + {self.height} + {self.depth}) \\\\"
            f"&= 2 \\times ({self.bottom_edge + self.height + self.depth}) \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Vertices (Rectilinear Shape)
        # Starting from bottom-left (0,0) and going counter-clockwise
        vertices = [
            (0, 0),                                     # Bottom-Left
            (self.bottom_edge, 0),                           # Bottom-Right
            (self.bottom_edge, self.height),                      # Top-Right Outer
            (self.bottom_edge - self.right_leg_width, self.height),    # Top-Right Inner Start
            (self.bottom_edge - self.right_leg_width, self.height - self.depth), # Inner Bottom-Right
            (self.left_leg_width, self.height - self.depth),           # Inner Bottom-Left
            (self.left_leg_width, self.height),                   # Top-Left Inner Start
            (0, self.height),                                # Top-Left Outer
            (0, 0)                                      # Close Polygon
        ]
        
        # Plotting
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Draw the shape
        poly = patches.Polygon(vertices, closed=True, edgecolor='black', 
                            facecolor='#AEC6CF', linewidth=2)
        ax.add_patch(poly)
        
        # Configure plot limits and remove axes
        ax.set_xlim(-3, self.bottom_edge + 3)
        ax.set_ylim(-3, self.height + 3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Helper function to add dimension lines
        def add_dimension(x1, y1, x2, y2, text, offset=1.0, color='black'):
            # Midpoint for text
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            
            # Calculate arrow positions based on offset
            if y1 == y2: # Horizontal dimension
                axy = (0, offset) # Offset direction
                text_y = y1 - offset - 0.5 if offset > 0 else y1 - offset + 0.5
                text_x = mid_x
                va = 'top' if offset > 0 else 'bottom'
                ha = 'center'
                
                # Draw annotation line
                ax.annotate('', xy=(x1, y1 - offset), xytext=(x2, y2 - offset),
                            arrowprops=dict(arrowstyle='<->', color=color))
                # Draw extension lines (dotted)
                ax.plot([x1, x1], [y1, y1 - offset], color=color, linestyle='--', linewidth=0.5)
                ax.plot([x2, x2], [y2, y2 - offset], color=color, linestyle='--', linewidth=0.5)
                # Add text
                ax.text(text_x, text_y, text, ha=ha, va=va, fontsize=12, fontweight='bold', color=color)
                
            elif x1 == x2: # Vertical dimension
                text_y = mid_y
                text_x = x1 - offset - 0.5 if offset > 0 else x1 - offset + 0.5
                va = 'center'
                ha = 'right' if offset > 0 else 'left'
                
                # Draw annotation line
                ax.annotate('', xy=(x1 - offset, y1), xytext=(x2 - offset, y2),
                            arrowprops=dict(arrowstyle='<->', color=color))
                # Draw extension lines (dotted)
                ax.plot([x1 - offset, x1], [y1, y1], color=color, linestyle='--', linewidth=0.5)
                ax.plot([x2 - offset, x2], [y2, y2], color=color, linestyle='--', linewidth=0.5)
                # Add text
                ax.text(text_x, text_y, text, ha=ha, va=va, fontsize=12, fontweight='bold', color=color)

        # Add Labels
        
        # Bottom Edge
        add_dimension(0, 0, self.bottom_edge, 0, str(self.bottom_edge), offset=1.5)
        
        # Left Vertical Edge
        add_dimension(0, self.height, 0, 0, str(self.height), offset=1.5)
        
        # Right Vertical Edge
        add_dimension(self.bottom_edge, 0, self.bottom_edge, self.height, str(self.height), offset=-1.5)
        
        # Top Inner Width
        # Located at the bottom of the "U" notch
        inner_start_x = self.left_leg_width
        inner_end_x = self.bottom_edge - self.right_leg_width
        inner_y = self.height - self.depth
        add_dimension(inner_start_x, inner_y, inner_end_x, inner_y, str(self.inner_width), offset=1.0, color='blue')
        
        # Depth of the 'U'
        # Located inside the notch on the left side
        add_dimension(self.left_leg_width, self.height, self.left_leg_width, self.height - self.depth, str(self.depth), offset=-0.5, color='red')
        
        # plt.title("Example 5: The 'Compound Perimeter' (Missing Sides)", fontsize=14)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat059:
    
    def __init__(self):
        self.radius = rnd.randint(4, 12)  # Radius between 4 and 12 cm
        self.gap_angle = rnd.randint(30, 90) # The 'mouth' angle between 30 and 90 degrees
        self.major_angle = 360 - self.gap_angle

        self.answer = round((self.major_angle / 360) * (self.radius**2), 2) # In terms of π cm²

        self.description = (
            f"Calculate the area of the shaded major sector. Give your answer in terms of π. Round the result to two decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Circles, arcs and sectors"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Radius }} (r) &= {self.radius} \\,\\text{{cm}} \\\\"
            f"\\text{{Angle of gap}} &= {self.gap_angle}^\\circ \\\\"
            f"\\text{{Angle of major sector }} (\\theta) &= 360^\\circ - {self.gap_angle}^\\circ \\\\"
            f"&= {self.major_angle}^\\circ \\\\"
            f"\\text{{Area of sector}} &= \\frac{{\\theta}}{{360}} \\times \\pi r^2 \\\\"
            f"&= \\frac{{{self.major_angle}}}{{360}} \\times \\pi \\times ({self.radius})^2 \\\\"
            f"&= {round(self.major_angle / 360, 10)} \\times \\pi \\times {self.radius**2} \\\\"
            f"&= {self.answer}\\pi \\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_aspect('equal')
        ax.axis('off') # Hide axes for a clean geometric figure
        
        # Define the center
        center = (0, 0)
        
        # Draw the Major Sector (The Pac-Man)
        # We center the gap at angle 0 for the classic "eating right" look.
        # So the sector starts at gap_angle/2 and goes to 360 - gap_angle/2
        theta1 = self.gap_angle / 2
        theta2 = 360 - (self.gap_angle / 2)
        
        pacman = patches.Wedge(
            center, 
            self.radius, 
            theta1, 
            theta2, 
            color='#4CAF50', # A nice green
            alpha=0.3,       # Transparency
            ec='black',      # Edge color
            lw=2             # Line width
        )
        ax.add_patch(pacman)

        # Draw the dashed lines for the "missing" wedge (to visualize the gap angle)
        # We draw lines from center to the start and end of the wedge
        x_gap_top = center[0] + self.radius * np.cos(np.radians(theta1))
        y_gap_top = center[1] + self.radius * np.sin(np.radians(theta1))
        
        x_gap_bot = center[0] + self.radius * np.cos(np.radians(theta2))
        y_gap_bot = center[1] + self.radius * np.sin(np.radians(theta2))
        
        # Draw dashed radii for the gap
        ax.plot([center[0], x_gap_top], [center[1], y_gap_top], 'k--', alpha=0.5)
        ax.plot([center[0], x_gap_bot], [center[1], y_gap_bot], 'k--', alpha=0.5)

        # Annotations
        
        # Label Radius
        # Place label halfway along the top radius edge of the Pac-Man
        label_r_x = center[0] + (self.radius * 0.6) * np.cos(np.radians(theta1))
        label_r_y = center[1] + (self.radius * 0.6) * np.sin(np.radians(theta1))
        
        # Rotate text to align with the radius line
        ax.text(label_r_x, label_r_y + 0.5, f"r = {self.radius} cm", 
                ha='center', va='bottom', rotation=theta1, fontsize=12, fontweight='bold')

        # Label the small angle (the gap)
        # Draw a small arc for the gap angle
        gap_arc = patches.Arc(center, self.radius*0.3, self.radius*0.3, angle=0, theta1=theta2-360, theta2=theta1, color='red')
        ax.add_patch(gap_arc)
        ax.text(self.radius * 0.25, 0, f"{self.gap_angle}°", color='red', va='center', ha='left', fontsize=10)

        # Label the Reflex Angle (The Major Sector)
        # Draw a larger arc for the reflex angle
        major_arc = patches.Arc(center, self.radius*0.5, self.radius*0.5, angle=0, theta1=theta1, theta2=theta2, color='blue', linestyle=':')
        ax.add_patch(major_arc)
        
        # Position the reflex angle label in the "back" of the Pac-Man
        # Angle 180 is directly left
        lbl_x = center[0] + (self.radius * 0.35) * np.cos(np.radians(180))
        lbl_y = center[1] + (self.radius * 0.35) * np.sin(np.radians(180))
        ax.text(lbl_x, lbl_y, f"{self.major_angle}°", color='blue', ha='center', va='center', fontweight='bold')

        # Set Limits to ensure everything fits
        limit_buffer = 1
        ax.set_xlim(-self.radius - limit_buffer, self.radius + limit_buffer)
        ax.set_ylim(-self.radius - limit_buffer, self.radius + limit_buffer)
        
        # plt.title(f"Find the Area of the Shaded Major Sector\n(Answer in terms of $\pi$)", fontsize=14)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat060:
    
    def __init__(self):
        # We choose multiples of 7 for the diameter to make the math (22/7) cleaner for students
        self.diameter = 7 * rnd.randint(1, 6)
        self.radius = self.diameter / 2

        self.answer = self.diameter * 22 // 7 // 2 # Half arc in terms of m

        self.description = (
            f"Calculate the length of the curved arc. Use $\\pi = \\frac{{22}}{{7}}$."
        )

        self.topic = "Mensuration"
        self.subtopic = "Circles, arcs and sectors"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Diameter }} (d) &= {self.diameter}\\,\\text{{m}} \\\\"
            f"\\text{{Circumference }} (C) &= \\pi d \\\\"
            f"&= \\frac{{22}}{{7}} \\times {self.diameter} \\\\"
            f"&= {self.diameter * 22 // 7}\\,\\text{{m}} \\\\"
            f"\\text{{Length of curved arc (semicircle)}} &= \\frac{{1}}{{2}} \\times C \\\\"
            f"&= \\frac{{1}}{{2}} \\times {self.diameter * 22 // 7} \\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_aspect('equal')
        ax.axis('off')  # Hide axes for a clean geometry diagram look

        # Draw the Semi-Circle (The "Track")
        # Generate angles from 0 to 180 degrees (0 to pi radians)
        theta = np.linspace(0, np.pi, 100)
        x_arc = self.radius * np.cos(theta)
        y_arc = self.radius * np.sin(theta)
        
        # Plot the curved arc
        ax.plot(x_arc, y_arc, color='black', linewidth=2.5, label='Track')

        # Draw the Dashed Diameter Line
        ax.plot([-self.radius, self.radius], [0, 0], color='black', linestyle='--', linewidth=1.5)

        # Add Labels
        # Label the diameter
        ax.text(0, -0.15 * self.radius, f"{self.diameter} m", ha='center', va='top', fontsize=14, fontweight='bold')

        plt.tight_layout(rect=[0, 0.1, 1, 1]) # Adjust layout to make room for text

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat061:
    
    def __init__(self):
        self.width = rnd.randint(4, 12) # In cm
        self.height = rnd.randint(4, 10) # In cm
        
        self.radius = self.width / 2 # In cm

        self.answer = round(self.width + (2 * self.height) + (0.5 * math.pi * self.width), 2) # In cm

        self.description = (
            f"Calculate the total perimeter of the window frame. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Circles, arcs and sectors"
        self.source = "Adapted from Complete Mathematics for Cambridge IGCSE (David Rayner)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Width }} (w) &= {self.width}\\,\\text{{cm}} \\\\"
            f"\\text{{Height }} (h) &= {self.height}\\,\\text{{cm}} \\\\"
            f"\\text{{Perimeter}} &= w + 2h + \\frac{{1}}{{2}}\\pi w \\\\"
            f"&= {self.width} + 2({self.height}) + 0.5 \\pi ({self.width}) \\\\"
            f"&= {self.width} + {2 * self.height} + {round(0.5 * math.pi * self.width, 10)} \\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(6, 8))
        
        # Create Shapes
        # Rectangle: Origin at (0,0)
        rect = patches.Rectangle(
            (0, 0), self.width, self.height, 
            linewidth=2, edgecolor='black', facecolor='#d9ebf9'
        )
        
        # Semicircle: Center at (width/2, height), Radius = width/2
        # Theta from 0 to 180 degrees
        semicircle = patches.Wedge(
            (self.radius, self.height), self.radius, 0, 180, 
            linewidth=2, edgecolor='black', facecolor='#d9ebf9'
        )
        
        # Add patches to the axes
        ax.add_patch(rect)
        ax.add_patch(semicircle)
        
        # Add Dimension Annotations (Arrows and Text)
        
        # Width Annotation (Bottom)
        ax.annotate(
            text='', 
            xy=(0, -0.5), xytext=(self.width, -0.5),
            arrowprops=dict(arrowstyle='<->', lw=1.5),
            ha='center', va='center', fontsize=12,
            xycoords='data', textcoords='data'
        )
        # Label position correction (centering text on the arrow)
        ax.text(self.width/2, -1.0, f'Width = {self.width} cm', ha='center', va='center', fontsize=12)

        # Height Annotation (Right Side)
        ax.annotate(
            text='', 
            xy=(self.width + 0.5, 0), xytext=(self.width + 0.5, self.height),
            arrowprops=dict(arrowstyle='<->', lw=1.5),
            xycoords='data', textcoords='data'
        )
        ax.text(self.width + 1.0, self.height/2, f'Height = {self.height} cm', ha='left', va='center', rotation=270, fontsize=12)

        # Set Limits and Hide Axes
        # Add some padding to the limits so annotations fit
        ax.set_xlim(-1, self.width + 2) 
        ax.set_ylim(-2, self.height + self.radius + 1)
        ax.set_aspect('equal')
        ax.axis('off') # Turn off the X and Y axis grid/numbers
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat062:
    
    def __init__(self):
        # Random Outer Radius (R) between 6 and 15
        self.R = rnd.randint(6, 15)
        # Random Inner Radius (r) between 2 and R-3 (ensures distinct gap)
        self.r = rnd.randint(2, self.R - 3)

        area_outer = self.R**2
        area_inner = self.r**2
        self.answer = area_outer - area_inner # In terms of π

        self.description = (
            f"Calculate the area of the shaded region. Leave your answer in terms of π."
        )

        self.topic = "Mensuration"
        self.subtopic = "Circles, arcs and sectors"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Outer radius }} (R) &= {self.R} \\\\"
            f"\\text{{Inner radius }} (r) &= {self.r} \\\\"
            "\\text{Area of the shaded region} &= \\text{Area of outer circle} - \\text{Area of inner circle} \\\\"
            "A &= \\pi R^2 - \\pi r^2 \\\\"
            "&= \\pi (R^2 - r^2) \\\\"
            f"&= \\pi ({self.R}^2 - {self.r}^2) \\\\"
            f"&= \\pi ({self.R**2} - {self.r**2}) \\\\"
            f"&= {self.answer}\\pi"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # 2. Setup the Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # 3. Create Shapes
        # Outer Circle (The "Shaded" part)
        # We color this one. When we place the white one on top, it creates the ring.
        outer_circle = patches.Circle((0, 0), radius=self.R, facecolor='skyblue', 
                                    edgecolor='black', linewidth=2, label='Outer')
        
        # Inner Circle (The "Hole")
        # Facecolor matches background (white) to look like a hole
        inner_circle = patches.Circle((0, 0), radius=self.r, facecolor='white', 
                                    edgecolor='black', linewidth=2, label='Inner')

        # Add patches to the plot
        ax.add_patch(outer_circle)
        ax.add_patch(inner_circle)

        # 4. Add Visual Annotations (Radii lines)
        
        # Line for Outer Radius (R) - Drawn horizontally
        ax.plot([0, self.R], [0, 0], color='black', linestyle='-', linewidth=1.5)
        ax.text(self.R / 2, 0.5, f'$R={self.R}$', ha='center', fontsize=12, fontweight='bold')

        # Line for Inner Radius (r) - Drawn at 45 degrees to avoid clutter
        angle = np.pi / 4  # 45 degrees
        r_x = self.r * np.cos(angle)
        r_y = self.r * np.sin(angle)
        ax.plot([0, r_x], [0, r_y], color='black', linestyle='-', linewidth=1.5)
        
        # Label for r (slightly offset so it doesn't overlap the line)
        ax.text(r_x / 2 - 0.5, r_y / 2 + 1, f'$r={self.r}$', ha='center', fontsize=12, fontweight='bold')

        # Center point dot
        ax.plot(0, 0, 'ko', markersize=5)

        # 5. Plot Formatting
        limit = self.R + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal') # Crucial so circles don't look like ovals
        ax.axis('off') # Hide the XY axes for a clean geometry look
        plt.title(f"R={self.R}, r={self.r}")
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat063:
    
    def __init__(self):
        # Total length (radius of the outer edge)
        self.total_length = rnd.randint(40, 60)  # cm
        
        # Length of the rubber blade (the outer cleaning part)
        # Ensure it's substantial but less than total length
        self.blade_length = rnd.randint(20, self.total_length - 10) 
        
        # Inner length (the metal arm part that doesn't clean)
        self.inner_length = self.total_length - self.blade_length
        
        # Angle swept
        self.angle_deg = rnd.choice([90, 100, 110, 120, 135])
        
        area_outer = self.angle_deg / 360 * self.total_length**2
        area_inner = self.angle_deg / 360 * self.inner_length**2

        self.answer = round(area_outer - area_inner, 2) # In terms of π cm^2

        self.description = (
            f"Calculate the area of the windshield cleaned by the blade. Give your answer in terms of π. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Circles, arcs and sectors"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Outer radius }} (R) &= {self.total_length}\\,\\text{{cm}}\\\\"
            f"\\text{{Inner radius }} (r) &= {self.total_length} - {self.blade_length} = {self.inner_length}\\,\\text{{cm}}\\\\"
            f"\\text{{Angle }} (\\theta) &= {self.angle_deg}^\\circ\\\\"
            f"\\text{{Area cleaned}} &= \\frac{{\\theta}}{{360}} \\pi (R^2 - r^2)\\\\"
            f"&= \\frac{{{self.angle_deg}}}{{360}} \\pi (({self.total_length})^2 - ({self.inner_length})^2)\\\\"
            f"&= {round(self.angle_deg / 360, 10)} \\pi ({self.total_length**2} - {self.inner_length**2})\\\\"
            f"&= {round(self.angle_deg / 360, 10)} \\pi ({self.total_length**2 - self.inner_length**2})\\\\"
            f"&= {self.answer}\\pi\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Center the wiper vertically (pointing up)
        start_angle = (180 - self.angle_deg) / 2
        end_angle = start_angle + self.angle_deg
        
        # Draw the Geometry
        
        # The "Cleaned Area" (The Blade)
        # We use a Wedge with a 'width' parameter to create the ring sector directly
        cleaned_area = patches.Wedge(
            center=(0, 0), 
            r=self.total_length, 
            theta1=start_angle, 
            theta2=end_angle, 
            width=self.blade_length, # This makes it a ring (annulus)
            color='skyblue', 
            alpha=0.6,
            label='Cleaned Area'
        )
        ax.add_patch(cleaned_area)
        
        # The "Metal Arm" (Inner part)
        # Draw a line from pivot to the start of the blade to represent the arm
        # We draw it at the bisector angle for clarity
        mid_angle_rad = np.radians(90)
        
        # Pivot point
        ax.plot(0, 0, 'ko', markersize=8, label='Pivot')
        
        # Draw the arm lines (left and right limits) to show the sweep
        # Inner boundaries
        x_inner_start = self.inner_length * np.cos(np.radians(start_angle))
        y_inner_start = self.inner_length * np.sin(np.radians(start_angle))
        x_inner_end = self.inner_length * np.cos(np.radians(end_angle))
        y_inner_end = self.inner_length * np.sin(np.radians(end_angle))
        
        # Outer boundaries
        x_outer_start = self.total_length * np.cos(np.radians(start_angle))
        y_outer_start = self.total_length * np.sin(np.radians(start_angle))
        x_outer_end = self.total_length * np.cos(np.radians(end_angle))
        y_outer_end = self.total_length * np.sin(np.radians(end_angle))
        
        # Dash lines for the full sweep boundaries
        ax.plot([0, x_outer_start], [0, y_outer_start], 'k--', alpha=0.3)
        ax.plot([0, x_outer_end], [0, y_outer_end], 'k--', alpha=0.3)

        # Annotations
        
        # Annotate Angle
        # Draw a small arc for the angle
        arc_radius = self.inner_length * 0.4
        angle_arc = patches.Arc((0, 0), arc_radius*2, arc_radius*2, 
                                theta1=start_angle, theta2=end_angle, 
                                color='black', linewidth=1.5)
        ax.add_patch(angle_arc)
        ax.text(0, arc_radius + 2, f"{self.angle_deg}°", ha='center', fontsize=12, fontweight='bold')

        # Annotate Total Length
        # We'll put this on the right side boundary
        ax.annotate(
            '', xy=(x_outer_start, y_outer_start), xytext=(0, 0),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5)
        )
        # Label position for total length (midpoint of the arrow)
        mid_x_total = x_outer_start / 2
        mid_y_total = y_outer_start / 2
        ax.text(mid_x_total - 2, mid_y_total + 2, f"Total: {self.total_length} cm", 
                color='blue', rotation=start_angle, ha='right', fontweight='bold')

        # Annotate Blade Length (The cleaning part)
        # We'll put this on the left side boundary
        ax.annotate(
            '', xy=(x_outer_end, y_outer_end), xytext=(x_inner_end, y_inner_end),
            arrowprops=dict(arrowstyle='<->', color='red', lw=1.5)
        )
        # Label position
        mid_x_blade = (x_outer_end + x_inner_end) / 2
        mid_y_blade = (y_outer_end + y_inner_end) / 2
        ax.text(mid_x_blade + 2, mid_y_blade + 2, f"Blade: {self.blade_length} cm", 
                color='red', rotation=end_angle-180, ha='left', fontweight='bold')

        # Final Formatting
        ax.set_aspect('equal')
        ax.set_xlim(-self.total_length - 5, self.total_length + 5)
        ax.set_ylim(-5, self.total_length + 10)
        ax.axis('off') # Turn off axis numbers/frame for a cleaner diagram look
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat064:
    
    def __init__(self):
        # Radius between 2 and 6 (so Diameter is 4 to 12)
        self.radius = rnd.randint(2, 6)
        self.diameter = self.radius * 2
        
        # Cylinder height usually larger than radius for a silo look
        self.cyl_height = rnd.randint(self.radius + 2, self.radius + 10)

        vol_cyl = self.radius**2 * self.cyl_height
        vol_hemi = (2 / 3) * self.radius**3

        self.answer = round(vol_cyl + vol_hemi, 2) # In terms of π m³

        self.description = (
            f"Calculate the total volume of the silo. Give your answer in terms of π. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Surface area and volume"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook (Pimentel & Wall)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Radius }} (r) &= {self.radius}\\\\"
            f"\\text{{Height }} (h) &= {self.cyl_height}\\\\"
            f"\\text{{Volume of Cylinder}} &= \\pi r^2 h\\\\"
            f"&= \\pi ({self.radius})^2 ({self.cyl_height})\\\\"
            f"&= {round(self.radius**2 * self.cyl_height, 10)}\\pi\\\\"
            f"\\text{{Volume of Hemisphere}} &= \\frac{{2}}{{3}} \\pi r^3\\\\"
            f"&= \\frac{{2}}{{3}} \\pi ({self.radius})^3\\\\"
            f"&= {round((2/3) * self.radius**3, 10)}\\pi\\\\"
            f"\\text{{Total Volume}} &= V_{{cyl}} + V_{{hemi}}\\\\"
            f"&= {round(self.radius**2 * self.cyl_height, 10)}\\pi + {round((2/3) * self.radius**3, 10)}\\pi\\\\"
            f"&= {self.answer}\\pi\\,\\text{{m}}^3"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Plot
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # --- Generate Cylinder Data ---
        # Angle (theta) and Height (z)
        theta = np.linspace(0, 2 * np.pi, 50)
        z_cyl = np.linspace(0, self.cyl_height, 20)
        theta_grid, z_grid = np.meshgrid(theta, z_cyl)
        
        x_cyl = self.radius * np.cos(theta_grid)
        y_cyl = self.radius * np.sin(theta_grid)
        
        # --- Generate Hemisphere Data ---
        # Phi (elevation) from 0 to pi/2 (top half), Theta (azimuth) 0 to 2pi
        phi = np.linspace(0, np.pi / 2, 20)
        phi_grid, theta_grid_sphere = np.meshgrid(phi, theta)
        
        x_sphere = self.radius * np.sin(phi_grid) * np.cos(theta_grid_sphere)
        y_sphere = self.radius * np.sin(phi_grid) * np.sin(theta_grid_sphere)
        z_sphere = self.radius * np.cos(phi_grid) + self.cyl_height # Shift up by cylinder height
        
        # --- Plotting ---
        # Plot Cylinder
        ax.plot_surface(x_cyl, y_cyl, z_grid, color='cyan', alpha=0.25, edgecolor='k', linewidth=0.2)
        
        # Plot Hemisphere
        ax.plot_surface(x_sphere, y_sphere, z_sphere, color='orange', alpha=0.25, edgecolor='k', linewidth=0.2)
        
        # Plot Bottom Circle (to close the silo)
        r_bottom = np.linspace(0, self.radius, 10)
        r_grid, theta_grid_bottom = np.meshgrid(r_bottom, theta)
        x_bottom = r_grid * np.cos(theta_grid_bottom)
        y_bottom = r_grid * np.sin(theta_grid_bottom)
        z_bottom = np.zeros_like(x_bottom)
        ax.plot_surface(x_bottom, y_bottom, z_bottom, color='cyan', alpha=0.6)

        # --- Annotations ---
        # Draw a line indicating Height
        ax.plot([self.radius * 1.5, self.radius * 1.5], [0, 0], [0, self.cyl_height], color='black', linestyle='--')
        ax.text(self.radius * 1.6, 0, self.cyl_height / 2, f'h = {self.cyl_height}m', color='black', fontsize=12)
        
        # Draw a line indicating Diameter
        # We draw it at the bottom or top of the cylinder
        ax.plot([-self.radius, self.radius], [0, 0], [0, 0], color='red', linestyle='-', linewidth=2)
        ax.text(0, 0, -1, f'd = {self.diameter}m', color='red', fontsize=12)

        # Formatting the Plot
        ax.set_box_aspect((self.diameter, self.diameter, self.cyl_height + self.radius))  # Aspect ratio to look realistic
        ax.set_axis_off() # Turn off the grid box for a cleaner "diagram" look
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat065:
    
    def __init__(self):
        self.length = round(rnd.uniform(15.0, 25.0), 1)   # Length: 15m - 25m
        self.width = round(rnd.uniform(6.0, 10.0), 1)     # Width: 6m - 10m
        
        # Ensure deep end is actually deeper than shallow end
        self.shallow_depth = round(rnd.uniform(0.8, 1.2), 1) 
        self.deep_depth = round(rnd.uniform(1.8, 2.5), 1)

        cross_section_area = ((self.shallow_depth + self.deep_depth) / 2) * self.length
        volume = cross_section_area * self.width

        self.answer = round(volume, 2)

        self.description = (
            f"Calculate the capacity of the pool in cubic meters. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Surface area and volume"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Cross-Section Area}} &= \\left( \\frac{{{self.shallow_depth} + {self.deep_depth}}}{{2}} \\right) \\times {self.length}\\\\"
            f"&= {round(((self.shallow_depth + self.deep_depth) / 2) * self.length, 10)}\\,\\text{{m}}^2\\\\"
            f"\\text{{Volume}} &= \\text{{Cross-Section Area}} \\times \\text{{Width}}\\\\"
            f"&= {round(((self.shallow_depth + self.deep_depth) / 2) * self.length, 10)} \\times {self.width}\\\\"
            f"&= {self.answer}\\,\\text{{m}}^3"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Vertices (x, y, z)
        # Coordinate system: x=Length, y=Width, z=Depth (negative)
        # Surface is at z=0
        
        # Top Surface (Water Level)
        p0 = [0, 0, 0]          # Shallow, Front-Left
        p1 = [self.length, 0, 0]     # Deep, Front-Right
        p2 = [self.length, self.width, 0] # Deep, Back-Right
        p3 = [0, self.width, 0]      # Shallow, Back-Left

        # Bottom Surface (Floor)
        p4 = [0, 0, -self.shallow_depth]          # Shallow Bottom, Front-Left
        p5 = [self.length, 0, -self.deep_depth]        # Deep Bottom, Front-Right
        p6 = [self.length, self.width, -self.deep_depth]    # Deep Bottom, Back-Right
        p7 = [0, self.width, -self.shallow_depth]      # Shallow Bottom, Back-Left

        vertices = np.array([p0, p1, p2, p3, p4, p5, p6, p7])

        # Define Faces (Polygons)
        # Each face is a list of vertices
        faces = [
            [p0, p1, p2, p3], # Top (Surface)
            [p4, p5, p6, p7], # Bottom (Sloped Floor)
            [p0, p1, p5, p4], # Front Side (Trapezium cross-section)
            [p2, p3, p7, p6], # Back Side (Trapezium cross-section)
            [p0, p3, p7, p4], # Left Side (Shallow End Wall)
            [p1, p2, p6, p5]  # Right Side (Deep End Wall)
        ]

        # Plotting
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')

        # Create the 3D polygon object
        pool_poly = Poly3DCollection(faces, alpha=0.3, linewidths=1, edgecolors='k')
        pool_poly.set_facecolor('cyan')
        ax.add_collection3d(pool_poly)

        # Labeling Dimensions
        # Offset text slightly for readability
        
        # Length Label
        ax.text(self.length / 2, -self.width * 0.2, 0, f"Length: {self.length}m", color='red', fontsize=10, fontweight='bold')
        
        # Width Label
        ax.text(self.length * 1.05, self.width / 2, 0, f"Width: {self.width}m", color='red', fontsize=10, fontweight='bold')
        
        # Shallow Depth Label
        ax.text(0, -self.width * 0.1, -self.shallow_depth/2, f"{self.shallow_depth}m", color='blue')
        ax.plot([0, 0], [0, 0], [0, -self.shallow_depth], color='blue', linestyle='--') # Indicator line

        # Deep Depth Label
        ax.text(self.length, -self.width * 0.1, -self.deep_depth/2, f"{self.deep_depth}m", color='blue')
        ax.plot([self.length, self.length], [0, 0], [0, -self.deep_depth], color='blue', linestyle='--') # Indicator line

        # Formatting the Plot
        # Auto-scale limits
        ax.set_xlim(-2, self.length + 2)
        ax.set_ylim(-2, self.width + 2)
        ax.set_zlim(-self.deep_depth - 1, 1)
        
        ax.set_xlabel('Length (x)')
        ax.set_ylabel('Width (y)')
        ax.set_zlabel('Depth (z)')
        
        # Set view angle to emphasize the Trapezoidal Cross-Section (Front view-ish)
        ax.view_init(elev=15, azim=-110)
        
        # Remove pane backgrounds for a cleaner "textbook" look
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.grid(False)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat066:
    
    def __init__(self):
        self.radius = rnd.randint(3, 8)       # Random radius between 3 cm and 8 cm
        self.height = rnd.randint(5, 12)      # Random height between 5 cm and 12 cm

        slant_height = np.sqrt(self.radius**2 + self.height**2)
        pi_val = 3.142
        curved_area = pi_val * self.radius * slant_height
        base_area = pi_val * self.radius**2
        total_area = curved_area + base_area

        self.answer = round(total_area, 2)

        self.description = (
            f"Calculate the total surface area of the cone. Use π = 3.142. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Surface area and volume"
        self.source = "Adapted from Complete Mathematics for Cambridge IGCSE (David Rayner)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given: Radius }} (r) &= {self.radius}\\,\\text{{cm}}, \\text{{ Height }} (h) = {self.height}\\,\\text{{cm}}\\\\"
            f"\\text{{Slant Height }} (l) &= \\sqrt{{r^2 + h^2}}\\\\"
            f"&= \\sqrt{{{self.radius}^2 + {self.height}^2}}\\\\"
            f"&= \\sqrt{{{self.radius**2} + {self.height**2}}}\\\\"
            f"&= \\sqrt{{{self.radius**2 + self.height**2}}}\\\\"
            f"&= {round(slant_height, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Base Area }} (A_{{base}}) &= \\pi r^2\\\\"
            f"&= {pi_val} \\times {self.radius}^2\\\\"
            f"&= {round(base_area, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Curved Surface Area }} (A_{{curved}}) &= \\pi r l\\\\"
            f"&= {pi_val} \\times {self.radius} \\times {round(slant_height, 10)}\\\\"
            f"&= {round(curved_area, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Total Surface Area}} &= A_{{base}} + A_{{curved}}\\\\"
            f"&= {round(base_area, 10)} + {round(curved_area, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the 3D Figure
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Create the Cone Surface Data
        # Resolution of the mesh
        n_theta = 50
        n_z = 20
        
        theta = np.linspace(0, 2 * np.pi, n_theta)
        v = np.linspace(0, 1, n_z) # v goes from 0 (base) to 1 (tip)
        
        Theta, V = np.meshgrid(theta, v)
        
        # Parametric equations for the cone surface
        # x = r * (1-v) * cos(theta)
        # y = r * (1-v) * sin(theta)
        # z = h * v
        X = self.radius * (1 - V) * np.cos(Theta)
        Y = self.radius * (1 - V) * np.sin(Theta)
        Z = self.height * V
        
        # Plot the curved surface
        ax.plot_surface(X, Y, Z, color='cyan', alpha=0.3, edgecolor='none')
        
        # Create the Base (Circle) Data
        # Z = 0 for the base
        r_base = np.linspace(0, self.radius, 10)
        theta_base = np.linspace(0, 2 * np.pi, 50)
        R_base, Theta_base = np.meshgrid(r_base, theta_base)
        
        X_base = R_base * np.cos(Theta_base)
        Y_base = R_base * np.sin(Theta_base)
        Z_base = np.zeros_like(X_base)
        
        # Plot the base
        ax.plot_surface(X_base, Y_base, Z_base, color='blue', alpha=0.5)
        
        # Add Annotations (The "Figure" logic)
        
        # Draw the Height (h) line: from (0,0,0) to (0,0,h)
        ax.plot([0, 0], [0, 0], [0, self.height], color='red', linewidth=2, linestyle='--', label=f'Height (h) = {self.height} cm')
        
        # Draw the Radius (r) line: from (0,0,0) to (r,0,0)
        # We choose a specific angle (theta=0) for clarity
        ax.plot([0, self.radius], [0, 0], [0, 0], color='black', linewidth=2, label=f'Radius (r) = {self.radius} cm')
        
        # Formatting the plot
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.tight_layout()
        
        # Hide grid and panes for a cleaner "textbook" look
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.grid(False)
        
        # Equal aspect ratio hack for 3D
        # (Matplotlib 3D doesn't strictly support "axis equal" easily, so we set limits)
        max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
        mid_x = (X.max()+X.min()) * 0.5
        mid_y = (Y.max()+Y.min()) * 0.5
        mid_z = (Z.max()+Z.min()) * 0.5
        ax.set_xlim(mid_x - max_range, mid_x + max_range)
        ax.set_ylim(mid_y - max_range, mid_y + max_range)
        ax.set_zlim(0, self.height + 1) # Start Z at 0

        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat067:
    
    def __init__(self):
        # Radius between 3 and 10
        self.radius = rnd.randint(3, 10)
        
        # Constants
        pi_approx = 3.14
        
        # Calculate Total Surface Area (TSA)
        # TSA = Curved Surface Area (2*pi*r^2) + Base Area (pi*r^2) = 3*pi*r^2
        tsa = 3 * pi_approx * (self.radius ** 2)

        self.answer = round(tsa, 2)

        self.description = (
            f"Calculate the total surface area of the solid hemisphere. Use π = 3.14. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Surface area and volume"
        self.source = "Common question type in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given radius (r)}} &= {self.radius} \\\\"
            f"\\text{{Total Surface Area of a solid hemisphere}} &= 3\\pi r^2 \\\\"
            f"&= 3 \\times 3.14 \\times ({self.radius})^2 \\\\"
            f"&= 3 \\times 3.14 \\times {self.radius**2} \\\\"
            f"&= {round(3 * 3.14 * self.radius**2, 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Figure
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # -- A. Create the hemisphere (Curved Surface) --
        # Phi goes from 0 (top) to pi/2 (equator)
        phi = np.linspace(0, np.pi/2, 30) 
        theta = np.linspace(0, 2 * np.pi, 60)
        phi_grid, theta_grid = np.meshgrid(phi, theta)
        
        x_dome = self.radius * np.sin(phi_grid) * np.cos(theta_grid)
        y_dome = self.radius * np.sin(phi_grid) * np.sin(theta_grid)
        z_dome = self.radius * np.cos(phi_grid)
        
        # Plot the curved surface
        ax.plot_surface(x_dome, y_dome, z_dome, color='skyblue', alpha=0.5, 
                        rstride=1, cstride=1, edgecolor='none', shade=True)
        
        # -- B. Create the base (Flat Circular Disk) --
        # r goes from 0 to radius
        r_base = np.linspace(0, self.radius, 20)
        theta_base = np.linspace(0, 2*np.pi, 60)
        r_grid, theta_grid_base = np.meshgrid(r_base, theta_base)
        
        x_base = r_grid * np.cos(theta_grid_base)
        y_base = r_grid * np.sin(theta_grid_base)
        z_base = np.zeros_like(x_base) # Base is at z=0
        
        # Plot the flat base
        ax.plot_surface(x_base, y_base, z_base, color='royalblue', alpha=0.5, edgecolor='none')
        
        # -- C. Visual Enhancements --
        # Draw a dark circle at the boundary to distinguish the "solid" edge
        theta_edge = np.linspace(0, 2*np.pi, 100)
        x_edge = self.radius * np.cos(theta_edge)
        y_edge = self.radius * np.sin(theta_edge)
        z_edge = np.zeros_like(x_edge)
        ax.plot(x_edge, y_edge, z_edge, color='darkblue', linewidth=2)

        # Draw the radius line
        # From center (0,0,0) to a point on the edge (radius, 0, 0)
        ax.plot([0, self.radius], [0, 0], [0, 0], 'r-', linewidth=3)
        ax.text(self.radius/2, 0, self.radius*0.1, f'r = {self.radius}', color='red', 
                fontsize=14, fontweight='bold', ha='center')
        
        # Mark the center
        ax.scatter([0], [0], [0], color='black', s=50)

        # Set aspect ratio to be accurate
        ax.set_box_aspect([1,1,0.5]) 
        ax.set_axis_off()
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat068:
    
    def __init__(self):
        # We randomize the base and the vertical height first to ensure a valid shape,
        # then calculate the Slant Edge to display as the "known" value.
        self.side_length = rnd.randint(10, 20) # In m
        self.vertical_height_real = rnd.randint(10, 20) # In m
        
        # Calculate half diagonal (center to corner) needed for Pythagoras
        # d^2 = (s/2)^2 + (s/2)^2
        self.half_base_diagonal = np.sqrt((self.side_length/2)**2 + (self.side_length/2)**2) # In m
        
        # Calculate Slant Edge (Edge from corner to top)
        self.slant_edge_len = round(np.sqrt(self.vertical_height_real**2 + self.half_base_diagonal**2), 2) # In m

        # Calculate the height
        vertical_height = np.sqrt(self.slant_edge_len**2 - self.half_base_diagonal**2) # In m

        # Calculate the volume
        self.answer = round((1/3) * self.side_length**2 * vertical_height, 2)

        self.description = (
            f"Calculate the vertical height of the pyramid and then use it to find the volume. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Surface area and volume"
        self.source = "Common \"high-mark\" question in IGCSE Mathematics 0580 Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Side length }} (s) &= {self.side_length}\\,\\text{{m}}\\\\"
            f"\\text{{Slant edge }} (l) &= {self.slant_edge_len}\\,\\text{{m}}\\\\"
            f"\\text{{Half base diagonal }} (d) &= \\sqrt{{\\left(\\frac{{s}}{{2}}\\right)^2 + \\left(\\frac{{s}}{{2}}\\right)^2}}\\\\"
            f"&= \\sqrt{{\\left(\\frac{{{self.side_length}}}{{2}}\\right)^2 + \\left(\\frac{{{self.side_length}}}{{2}}\\right)^2}}\\\\"
            f"&= {round(self.half_base_diagonal, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Vertical height }} (h) &= \\sqrt{{l^2 - d^2}}\\\\"
            f"&= \\sqrt{{{self.slant_edge_len}^2 - {round(self.half_base_diagonal, 10)}^2}}\\\\"
            f"&= {round(vertical_height, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Volume }} (V) &= \\frac{{1}}{{3}} \\times s^2 \\times h\\\\"
            f"&= \\frac{{1}}{{3}} \\times {self.side_length}^2 \\times {round(vertical_height, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}^3"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Coordinates
        # Center is at (0,0,0)
        r = self.side_length / 2
        
        # Base corners
        corners = np.array([
            [-r, -r, 0], # Rear Left
            [ r, -r, 0], # Rear Right
            [ r,  r, 0], # Front Right
            [-r,  r, 0]  # Front Left
        ])
        
        apex = np.array([0, 0, self.vertical_height_real])
        center = np.array([0, 0, 0])

        # Setup Plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Hide axes ticks for a cleaner diagram look
        ax.set_axis_off()

        # Plot Geometry
        
        # Plot Base (Square)
        # We reorder indices to draw a closed loop: 0->1->2->3->0
        base_x = np.append(corners[:,0], corners[0,0])
        base_y = np.append(corners[:,1], corners[0,1])
        base_z = np.append(corners[:,2], corners[0,2])
        ax.plot(base_x, base_y, base_z, color='black', linewidth=1.5)
        
        # Plot Slant Edges (Connecting corners to Apex)
        # We make the front edges solid and back edges dashed for depth perception
        for i, corner in enumerate(corners):
            # Determine if "front" or "back" based on y-coordinate roughly
            style = '-'
            alpha = 1.0
            if corner[1] < 0: # Back vertices in this view
                style = '--'
                alpha = 0.5
            ax.plot([corner[0], apex[0]], [corner[1], apex[1]], [corner[2], apex[2]], 
                    color='blue', linestyle=style, alpha=alpha, linewidth=1.5)

        # Plot Vertical Height (The Unknown 'h')
        ax.plot([center[0], apex[0]], [center[1], apex[1]], [center[2], apex[2]], 
                color='red', linestyle='--', linewidth=2, label='Height (h)')

        # Plot Half-Diagonal (dashed line on floor to show the Right Triangle relation)
        # Connecting Center to Corner 2 (Front Right)
        target_corner = corners[2] 
        ax.plot([center[0], target_corner[0]], [center[1], target_corner[1]], [center[2], target_corner[2]], 
                color='gray', linestyle=':', linewidth=1)

        # Add Labels
        
        # Label Base Side
        # Place label between Corner 2 and Corner 3 (Front side)
        mid_base = (corners[2] + corners[3]) / 2
        ax.text(mid_base[0], mid_base[1] - self.side_length - 2, mid_base[2], 
                f"{self.side_length} m", color='black', fontsize=12, fontweight='bold', ha='center')

        # Label Slant Edge
        # Place label on the edge connecting Corner 2 to Apex
        mid_slant = (corners[2] + apex) / 2
        ax.text(mid_slant[0]+1, mid_slant[1], mid_slant[2], 
                f"{self.slant_edge_len:.2f} m", color='blue', fontsize=12, fontweight='bold')

        # Label Vertical Height
        mid_height = (center + apex) / 2
        ax.text(mid_height[0]+0.5, mid_height[1], mid_height[2], 
                "h = ?", color='red', fontsize=14, fontweight='bold')

        # # Title with the question
        # plt.title(f"Example 8: Calculate Vertical Height (h)\nand Volume of the Pyramid", fontsize=14)
        
        # Adjust aspect ratio so it looks like a real pyramid
        # Scaling to make axes equal
        max_range = np.array([base_x.max()-base_x.min(), base_y.max()-base_y.min(), apex[2]]).max() / 2.0
        mid_x = (base_x.max()+base_x.min()) * 0.5
        mid_y = (base_y.max()+base_y.min()) * 0.5
        mid_z = apex[2] * 0.5
        ax.set_xlim(mid_x - max_range, mid_x + max_range)
        ax.set_ylim(mid_y - max_range, mid_y + max_range)
        ax.set_zlim(0, apex[2] + 2)
        ax.set_box_aspect((1, 1, self.vertical_height_real/self.side_length)) # Approximate aspect ratio

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat069:
    
    def __init__(self):
        # Length between 6 and 18, Width between 4 and 12 (even numbers preferred for easy radius)
        self.length = rnd.randint(6, 18) # In cm
        self.width = rnd.randrange(4, 12, 2) # In cm
        self.radius = self.width / 2 # In cm

        PI = 3.1416

        perimeter = 2 * self.length + 2 * PI * self.radius

        self.answer = round(perimeter, 2)

        self.description = (
            f"Calculate the total perimeter of the shape. Use π = 3.1416. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Compound shapes and parts of shapes"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length }} (l) &= {self.length}\\,\\text{{cm}}\\\\"
            f"\\text{{Width }} (w) &= {self.width}\\,\\text{{cm}}\\\\"
            f"\\text{{Radius }} (r) &= \\frac{{{self.width}}}{{2}} = {round(self.radius, 10)}\\,\\text{{cm}}\\\\"
            f"\\pi &= 3.1416\\\\"
            f"\\text{{Perimeter}} &= 2l + 2\\pi r\\\\"
            f"&= 2({self.length}) + 2(3.1416)({round(self.radius, 10)})\\\\"
            f"&= {round(2 * self.length, 10)} + {round(2 * 3.1416 * self.radius, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_aspect('equal')
        ax.axis('off')  # Hide axis ticks
        
        # Define colors
        shape_color = '#E0F7FA'  # Light Cyan fill
        line_color = '#006064'   # Dark Cyan outline
        dim_color = 'black'

        # Draw Shapes
        # We construct the shape using specific patches to avoid drawing the "internal" vertical lines
        
        # A. Central Rectangle (Fill only)
        rect = patches.Rectangle((0, 0), self.length, self.width, color=shape_color, ec='none')
        ax.add_patch(rect)
        
        # B. Right Semicircle (Fill)
        right_wedge = patches.Wedge((self.length, self.radius), self.radius, -90, 90, color=shape_color, ec='none')
        ax.add_patch(right_wedge)

        # C. Left Semicircle (Fill)
        left_wedge = patches.Wedge((0, self.radius), self.radius, 90, 270, color=shape_color, ec='none')
        ax.add_patch(left_wedge)

        # D. Draw the OUTLINE (Top, Bottom, and Arcs)
        # Top Line
        ax.plot([0, self.length], [self.width, self.width], color=line_color, linewidth=2)
        # Bottom Line
        ax.plot([0, self.length], [0, 0], color=line_color, linewidth=2)
        # Right Arc
        right_arc = patches.Arc((self.length, self.radius), self.width, self.width, theta1=-90, theta2=90, color=line_color, linewidth=2)
        ax.add_patch(right_arc)
        # Left Arc
        left_arc = patches.Arc((0, self.radius), self.width, self.width, theta1=90, theta2=270, color=line_color, linewidth=2)
        ax.add_patch(left_arc)

        # E. Internal Dashed Lines (Optional, to show it was a rectangle)
        ax.plot([0, 0], [0, self.width], color='gray', linestyle='--', alpha=0.5)
        ax.plot([self.length, self.length], [0, self.width], color='gray', linestyle='--', alpha=0.5)

        # Add Dimensions (Labels)
        
        # Label Length (L)
        ax.annotate(
            text='', xy=(0, -0.5 * self.radius), xytext=(self.length, -0.5 * self.radius),
            arrowprops=dict(arrowstyle='<->', color=dim_color)
        )
        ax.text(self.length/2, -0.5 * self.radius - 0.5, f"{self.length} cm", ha='center', va='top', fontsize=12, color=dim_color)
        
        # Label Width (W) - inside the shape or on the side
        # Drawing a vertical dimension line at x = length + radius + offset
        dim_x = self.length + self.radius + 1
        ax.annotate(
            text='', xy=(dim_x, 0), xytext=(dim_x, self.width),
            arrowprops=dict(arrowstyle='<->', color=dim_color)
        )
        ax.text(dim_x + 0.2, self.radius, f"{self.width} cm", ha='left', va='center', fontsize=12, color=dim_color)

        # Set plot limits with some padding
        ax.set_xlim(-self.radius - 2, self.length + self.radius + 3)
        ax.set_ylim(-self.radius - 2, self.width + 2)
        
        # plt.title("Geometry Problem: Compound Shape", fontsize=14, pad=20)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat070:
    
    def __init__(self):
        # Length between 6 and 18, Width between 4 and 12 (even numbers preferred for easy radius)
        self.length = rnd.randint(6, 18) # In cm
        self.width = rnd.randrange(4, 12, 2) # In cm
        self.radius = self.width / 2 # In cm

        PI = 3.1416

        area = self.length * self.width + PI * self.radius ** 2

        self.answer = round(area, 2)

        self.description = (
            f"Calculate the total area of the shape. Use π = 3.1416. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Compound shapes and parts of shapes"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given Length }} (l) &= {self.length}\\,\\text{{cm}}\\\\"
            f"\\text{{Given Width }} (w) &= {self.width}\\,\\text{{cm}}\\\\"
            f"\\text{{Radius }} (r) &= \\frac{{w}}{{2}} = \\frac{{{self.width}}}{{2}} = {round(self.radius, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Area of Rectangle}} &= l \\times w\\\\"
            f"&= {self.length} \\times {self.width}\\\\"
            f"&= {round(self.length * self.width, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Area of Circular Parts}} &= \\pi r^2\\\\"
            f"&= 3.1416 \\times ({round(self.radius, 10)})^2\\\\"
            f"&= 3.1416 \\times {round(self.radius**2, 10)}\\\\"
            f"&= {round(3.1416 * self.radius**2, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Total Area}} &= \\text{{Area of Rectangle}} + \\text{{Area of Circular Parts}}\\\\"
            f"&= {round(self.length * self.width, 10)} + {round(3.1416 * self.radius**2, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_aspect('equal')
        ax.axis('off')  # Hide axis ticks
        
        # Define colors
        shape_color = '#E0F7FA'  # Light Cyan fill
        line_color = '#006064'   # Dark Cyan outline
        dim_color = 'black'

        # Draw Shapes
        # We construct the shape using specific patches to avoid drawing the "internal" vertical lines
        
        # A. Central Rectangle (Fill only)
        rect = patches.Rectangle((0, 0), self.length, self.width, color=shape_color, ec='none')
        ax.add_patch(rect)
        
        # B. Right Semicircle (Fill)
        right_wedge = patches.Wedge((self.length, self.radius), self.radius, -90, 90, color=shape_color, ec='none')
        ax.add_patch(right_wedge)

        # C. Left Semicircle (Fill)
        left_wedge = patches.Wedge((0, self.radius), self.radius, 90, 270, color=shape_color, ec='none')
        ax.add_patch(left_wedge)

        # D. Draw the OUTLINE (Top, Bottom, and Arcs)
        # Top Line
        ax.plot([0, self.length], [self.width, self.width], color=line_color, linewidth=2)
        # Bottom Line
        ax.plot([0, self.length], [0, 0], color=line_color, linewidth=2)
        # Right Arc
        right_arc = patches.Arc((self.length, self.radius), self.width, self.width, theta1=-90, theta2=90, color=line_color, linewidth=2)
        ax.add_patch(right_arc)
        # Left Arc
        left_arc = patches.Arc((0, self.radius), self.width, self.width, theta1=90, theta2=270, color=line_color, linewidth=2)
        ax.add_patch(left_arc)

        # E. Internal Dashed Lines (Optional, to show it was a rectangle)
        ax.plot([0, 0], [0, self.width], color='gray', linestyle='--', alpha=0.5)
        ax.plot([self.length, self.length], [0, self.width], color='gray', linestyle='--', alpha=0.5)

        # Add Dimensions (Labels)
        
        # Label Length (L)
        ax.annotate(
            text='', xy=(0, -0.5 * self.radius), xytext=(self.length, -0.5 * self.radius),
            arrowprops=dict(arrowstyle='<->', color=dim_color)
        )
        ax.text(self.length/2, -0.5 * self.radius - 0.5, f"{self.length} cm", ha='center', va='top', fontsize=12, color=dim_color)
        
        # Label Width (W) - inside the shape or on the side
        # Drawing a vertical dimension line at x = length + radius + offset
        dim_x = self.length + self.radius + 1
        ax.annotate(
            text='', xy=(dim_x, 0), xytext=(dim_x, self.width),
            arrowprops=dict(arrowstyle='<->', color=dim_color)
        )
        ax.text(dim_x + 0.2, self.radius, f"{self.width} cm", ha='left', va='center', fontsize=12, color=dim_color)

        # Set plot limits with some padding
        ax.set_xlim(-self.radius - 2, self.length + self.radius + 3)
        ax.set_ylim(-self.radius - 2, self.width + 2)
        
        # plt.title("Geometry Problem: Compound Shape", fontsize=14, pad=20)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat071:
    
    def __init__(self):
        # Randomize the variable (Side length between 6 and 30, even numbers preferred for cleaner radius)
        self.side = rnd.randrange(6, 31, 2) # In cm
        self.radius = self.side / 2.0 # In cm
        
        # Calculate the answer
        area_square = self.side ** 2
        area_circle = np.pi * (self.radius ** 2)
        area_shaded = area_square - area_circle

        self.answer = round(area_shaded, 2)

        self.description = (
            f"Calculate the area of the shaded region. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Compound shapes and parts of shapes"
        self.source = "Standard Geometry Problem (Common in GCSE Mathematics past papers)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Side length, }} s &= {self.side}\\,\\text{{cm}}\\\\"
            f"\\text{{Radius, }} r &= \\frac{{s}}{{2}} = \\frac{{{self.side}}}{{2}} = {round(self.radius, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Area of Square}} &= s^2 = ({self.side})^2 = {round(self.side**2, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Area of Circle}} &= \\pi r^2 = \\pi ({round(self.radius, 10)})^2 \\approx {round(np.pi * self.radius**2, 10)}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Shaded Area}} &= \\text{{Area of Square}} - \\text{{Area of Circle}}\\\\"
            f"&= {round(self.side**2, 10)} - {round(np.pi * self.radius**2, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Create the Shapes
        # A. The Square (This acts as the shaded background)
        # We use 'lightgray' for color and '//' for hatching to represent "shading"
        square = patches.Rectangle(
            (0, 0), self.side, self.side, 
            edgecolor='black', 
            facecolor='lightgray', 
            hatch='//',       # The hatching pattern
            label='Square'
        )
        
        # B. The Circle (This masks the center of the square)
        # Facecolor must be 'white' to hide the square's hatching behind it
        circle = patches.Circle(
            (self.radius, self.radius), self.radius, 
            edgecolor='black', 
            facecolor='white', 
            label='Inscribed Circle'
        )
        
        # Add patches to the plot (Order matters: Square first, then Circle)
        ax.add_patch(square)
        ax.add_patch(circle)
        
        # Add Dimensions and Annotations
        # Draw a line for the side length
        plt.plot([0, self.side], [-1, -1], color='black', marker='|', markersize=10, linewidth=1.5)
        plt.text(self.side/2, -2, f'{self.side} cm', ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Plot Styling
        padding = self.side * 0.2
        ax.set_xlim(-padding, self.side + padding)
        ax.set_ylim(-padding, self.side + padding)
        ax.set_aspect('equal') # Crucial to make the circle look like a circle
        ax.axis('off')         # Hide the graph axis numbers
        
        # # Title and Question Display
        # plt.title(f"Find the Area of the Shaded Region\n(Square Side: {side} cm)", fontsize=14)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat072:
    
    def __init__(self):
        # Radius between 2.0 and 6.0
        self.r = round(rnd.uniform(2.0, 6.0), 2) # In m
        # Cylinder height between 4.0 and 12.0
        self.h_cyl = round(rnd.uniform(4.0, 12.0), 2) # In m
        # Cone height between 4.0 and 12.0
        self.h_cone = round(rnd.uniform(4.0, 12.0), 2) # In m

        volume_cylinder = np.pi * (self.r ** 2) * self.h_cyl
        volume_cone = (1 / 3) * np.pi * (self.r ** 2) * self.h_cone
        volume = volume_cylinder + volume_cone

        self.answer = round(volume, 2)

        self.description = (
            f"Calculate the total volume of the tank. Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Compound shapes and parts of shapes"
        self.source = "Adapted from Haese Mathematics for IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Volume of cylinder}} &= \\pi r^2 h_{{cyl}}\\\\"
            f"&= \\pi ({self.r})^2 ({self.h_cyl})\\\\"
            f"&= {round(np.pi * (self.r ** 2) * self.h_cyl, 10)}\\,\\text{{m}}^3\\\\"
            f"\\text{{Volume of cone}} &= \\frac{{1}}{{3}} \\pi r^2 h_{{cone}}\\\\"
            f"&= \\frac{{1}}{{3}} \\pi ({self.r})^2 ({self.h_cone})\\\\"
            f"&= {round((1 / 3) * np.pi * (self.r ** 2) * self.h_cone, 10)}\\,\\text{{m}}^3\\\\"
            f"\\text{{Total Volume}} &= V_{{cylinder}} + V_{{cone}}\\\\"
            f"&= {round(np.pi * (self.r ** 2) * self.h_cyl, 10)} + {round((1 / 3) * np.pi * (self.r ** 2) * self.h_cone, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}^3"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Resolution for the shapes
        theta = np.linspace(0, 2*np.pi, 50)
        
        # --- PART A: THE CYLINDER ---
        # z goes from 0 to h_cyl
        z_cyl = np.linspace(0, self.h_cyl, 10)
        theta_grid, z_cyl_grid = np.meshgrid(theta, z_cyl)
        x_cyl = self.r * np.cos(theta_grid)
        y_cyl = self.r * np.sin(theta_grid)
        
        # Plot Cylinder Surface
        ax.plot_surface(x_cyl, y_cyl, z_cyl_grid, color='skyblue', alpha=0.6, edgecolor='none')
        
        # Draw bottom and top circles of cylinder for clarity
        ax.plot(self.r * np.cos(theta), self.r * np.sin(theta), 0, color='blue')       # Bottom
        ax.plot(self.r * np.cos(theta), self.r * np.sin(theta), self.h_cyl, color='blue')   # Top (Interface)

        # --- PART B: THE CONE ---
        # z goes from h_cyl to (h_cyl + h_cone)
        # Radius shrinks from r to 0 as z increases
        u = np.linspace(0, 1, 10) # 0 to 1 relative height of cone
        theta_grid_cone, u_grid = np.meshgrid(theta, u)
        
        # Current height at step u
        z_cone_grid = self.h_cyl + u_grid * self.h_cone
        # Current radius at step u (Linear interpolation)
        current_r = self.r * (1 - u_grid)
        
        x_cone = current_r * np.cos(theta_grid_cone)
        y_cone = current_r * np.sin(theta_grid_cone)
        
        # Plot Cone Surface
        ax.plot_surface(x_cone, y_cone, z_cone_grid, color='orange', alpha=0.6, edgecolor='none')

        # --- PART C: ANNOTATIONS & FORMATTING ---
        
        # Add a vertical line through the center to visualize height better
        total_height = self.h_cyl + self.h_cone
        ax.plot([0, 0], [0, 0], [0, total_height], 'k--', lw=1)
        
        # Add text labels for the variables
        info_text = (
            f"Radius: {self.r} m\n"
            f"Cylinder Height: {self.h_cyl} m\n"
            f"Cone Height: {self.h_cone} m"
        )
        
        # Place text in the figure (outside the 3D box to avoid rotation issues)
        plt.figtext(0.05, 0.8, info_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        # # Dimension lines visualizers (Approximate placement)
        # # Radius label
        # ax.text(r/2, 0, 0, f"r={r}", color='blue')
        # # Cylinder height label (placed slightly outside)
        # ax.text(r + 0.5, 0, h_cyl/2, f"h_cyl={h_cyl}", color='blue')
        # # Cone height label
        # ax.text(r + 0.5, 0, h_cyl + h_cone/2, f"h_cone={h_cone}", color='orange')

        # Axis limits and labels
        limit = max(self.r, total_height/2) + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(0, total_height + 1)
        
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Height (Z)')
        # ax.set_title('Randomized Grain Silo (Compound Solid)')
        
        # Ensure aspect ratio is correct so the cylinder looks round
        ax.set_box_aspect([1, 1, total_height / (2*limit)]) 

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat073:
    
    def __init__(self):
        # Radius between 2.0 and 6.0
        self.r = round(rnd.uniform(2.0, 6.0), 2) # In m
        # Cylinder height between 4.0 and 12.0
        self.h_cyl = round(rnd.uniform(4.0, 12.0), 2) # In m
        # Cone height between 4.0 and 12.0
        self.h_cone = round(rnd.uniform(4.0, 12.0), 2) # In m

        base_area = np.pi * (self.r ** 2)
        cylinder_lateral_area = 2 * np.pi * self.r * self.h_cyl
        slant = np.sqrt(self.r ** 2 + self.h_cone ** 2)
        cone_lateral_area = np.pi * self.r * slant
        surface_area = base_area + cylinder_lateral_area + cone_lateral_area

        self.answer = round(surface_area, 2)

        self.description = (
            f"Calculate the total exterior surface area of the tank (assuming the base is flat and closed). Give your answer correct to 2 decimal places."
        )

        self.topic = "Mensuration"
        self.subtopic = "Compound shapes and parts of shapes"
        self.source = "Adapted from Haese Mathematics for IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{First, calculate the slant height }} s \\text{{ of the cone:}} &\\\\"
            f"s &= \\sqrt{{r^2 + h_{{\\text{{cone}}}}^2}} \\\\"
            f"&= \\sqrt{{({self.r})^2 + ({self.h_cone})^2}} \\\\"
            f"&= {round(np.sqrt(self.r**2 + self.h_cone**2), 10)}\\,\\text{{m}} \\\\[1em]"
            f"\\text{{Now, calculate the total surface area:}} &\\\\"
            f"\\text{{Area}} &= \\text{{Base}} + \\text{{Cylinder Lateral}} + \\text{{Cone Lateral}} \\\\"
            f"&= \\pi r^2 + 2 \\pi r h_{{\\text{{cyl}}}} + \\pi r s \\\\"
            f"&= \\pi({self.r})^2 + 2 \\pi({self.r})({self.h_cyl}) + \\pi({self.r})({round(np.sqrt(self.r**2 + self.h_cone**2), 10)}) \\\\"
            f"&= {self.answer}\\,\\text{{m}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Resolution for the shapes
        theta = np.linspace(0, 2*np.pi, 50)
        
        # --- PART A: THE CYLINDER ---
        # z goes from 0 to h_cyl
        z_cyl = np.linspace(0, self.h_cyl, 10)
        theta_grid, z_cyl_grid = np.meshgrid(theta, z_cyl)
        x_cyl = self.r * np.cos(theta_grid)
        y_cyl = self.r * np.sin(theta_grid)
        
        # Plot Cylinder Surface
        ax.plot_surface(x_cyl, y_cyl, z_cyl_grid, color='skyblue', alpha=0.6, edgecolor='none')
        
        # Draw bottom and top circles of cylinder for clarity
        ax.plot(self.r * np.cos(theta), self.r * np.sin(theta), 0, color='blue')       # Bottom
        ax.plot(self.r * np.cos(theta), self.r * np.sin(theta), self.h_cyl, color='blue')   # Top (Interface)

        # --- PART B: THE CONE ---
        # z goes from h_cyl to (h_cyl + h_cone)
        # Radius shrinks from r to 0 as z increases
        u = np.linspace(0, 1, 10) # 0 to 1 relative height of cone
        theta_grid_cone, u_grid = np.meshgrid(theta, u)
        
        # Current height at step u
        z_cone_grid = self.h_cyl + u_grid * self.h_cone
        # Current radius at step u (Linear interpolation)
        current_r = self.r * (1 - u_grid)
        
        x_cone = current_r * np.cos(theta_grid_cone)
        y_cone = current_r * np.sin(theta_grid_cone)
        
        # Plot Cone Surface
        ax.plot_surface(x_cone, y_cone, z_cone_grid, color='orange', alpha=0.6, edgecolor='none')

        # --- PART C: ANNOTATIONS & FORMATTING ---
        
        # Add a vertical line through the center to visualize height better
        total_height = self.h_cyl + self.h_cone
        ax.plot([0, 0], [0, 0], [0, total_height], 'k--', lw=1)
        
        # Add text labels for the variables
        info_text = (
            f"Radius: {self.r} m\n"
            f"Cylinder Height: {self.h_cyl} m\n"
            f"Cone Height: {self.h_cone} m"
        )
        
        # Place text in the figure (outside the 3D box to avoid rotation issues)
        plt.figtext(0.05, 0.8, info_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        # # Dimension lines visualizers (Approximate placement)
        # # Radius label
        # ax.text(r/2, 0, 0, f"r={r}", color='blue')
        # # Cylinder height label (placed slightly outside)
        # ax.text(r + 0.5, 0, h_cyl/2, f"h_cyl={h_cyl}", color='blue')
        # # Cone height label
        # ax.text(r + 0.5, 0, h_cyl + h_cone/2, f"h_cone={h_cone}", color='orange')

        # Axis limits and labels
        limit = max(self.r, total_height/2) + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(0, total_height + 1)
        
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Height (Z)')
        # ax.set_title('Randomized Grain Silo (Compound Solid)')
        
        # Ensure aspect ratio is correct so the cylinder looks round
        ax.set_box_aspect([1, 1, total_height / (2*limit)]) 

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
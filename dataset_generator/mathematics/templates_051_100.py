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
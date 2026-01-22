import numpy as np
import random as rnd
import math
import os
import matplotlib.pyplot as plt
import sympy
from matplotlib import colors
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from PIL import Image, ImageDraw, ImageFont
from matplotlib.ticker import MultipleLocator, FuncFormatter
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles
from mathematics.helper import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# target folder : "root/dataset/mathematics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "mathematics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Mat051:
    def __init__(self):
        # r is radius, c_len is the length of both chords
        self.r = randrange_float(10.0, 15.0, 0.01)
        self.c_len = randrange_float(8.0, self.r * 1.5, 0.01)
        
        # d is the fixed distance from center for both chords
        # d = sqrt(r^2 - (c_len/2)^2)
        self.d = math.sqrt(self.r**2 - (self.c_len / 2)**2)
        
        # Create algebraic expression: distance = ax + b
        # Let's solve for x
        self.x_val = rnd.randint(2, 10)
        self.a = rnd.randint(1, 5)
        # b = distance - a*x
        self.b = self.d - (self.a * self.x_val)
        
        self.answer = self.x_val
        
        # Format the expression for the description
        self.expr = fmt_poly(self.a, "x", is_leading=True) + fmt_poly(round(self.b, 2), "")
        
        self.description = (
            f"The diagram shows a circle with center $O$. Two chords, $AB$ and $CD$, "
            f"each have a length of ${round(self.c_len, 2)}$ cm. "
            f"Chord $AB$ is ${round(self.d, 2)}$ cm from the center. "
            f"The distance from the center to chord $CD$ is $({self.expr.strip()})$ cm. "
            f"Find the value of $x$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems II"
        self.source = "Original" # Complies with syllabus
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length of chord }} AB &= {round(self.c_len, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Length of chord }} CD &= {round(self.c_len, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Since }} AB = CD, \\text{{ the chords are equidistant from the center }} O. &\\\\"
            f"\\text{{Distance to }} AB &= \\text{{Distance to }} CD \\\\"
            f"{round(self.d, 10)} &= {self.a}x + ({round(self.b, 10)})\\\\"
            f"{self.a}x &= {round(self.d, 10)} - ({round(self.b, 10)})\\\\"
            f"{self.a}x &= {round(self.d - self.b, 10)}\\\\"
            f"x &= \\frac{{{round(self.d - self.b, 10)}}}{{{self.a}}}\\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        limit = 1.3
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.axis('off')

        vis_r = 1.0
        circle = plt.Circle((0, 0), vis_r, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        # Plot a point at the center O
        ax.plot(0, 0, 'ko', markersize=6)

        # Geometric distance for plotting
        d_plot = (self.d / self.r) * vis_r
        h = math.sqrt(max(0, vis_r**2 - d_plot**2))

        # Randomize positions of the two chords
        rot1 = rnd.uniform(0, 360)
        rot2 = rot1 + rnd.uniform(90, 270) 

        def get_chord_pts(rotation, dist, half_len):
            rad = np.radians(rotation)
            rot_mat = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
            
            # The chord is horizontal in local space at y = dist
            p1_local = np.array([half_len, dist])
            p2_local = np.array([-half_len, dist])
            mid_local = np.array([0, dist])
            
            p1 = rot_mat @ p1_local
            p2 = rot_mat @ p2_local
            mid = rot_mat @ mid_local
            
            return p1, p2, mid

        pA, pB, midAB = get_chord_pts(rot1, d_plot, h)
        pC, pD, midCD = get_chord_pts(rot2, d_plot, h)

        # Draw Chords
        ax.plot([pA[0], pB[0]], [pA[1], pB[1]], color='black', lw=2)
        ax.plot([pC[0], pD[0]], [pC[1], pD[1]], color='black', lw=2)

        # Draw Dashed Distance Lines (precise from 0,0 to midpoints)
        ax.plot([0, midAB[0]], [0, midAB[1]], 'k--', lw=1.5)
        ax.plot([0, midCD[0]], [0, midCD[1]], 'k--', lw=1.5)

        # Labels for vertices
        centroid = np.array([0, 0])
        # Position 'O' label away from both dashed lines
        o_label_dir = -(midAB + midCD)
        if np.linalg.norm(o_label_dir) > 0:
            o_label_dir = o_label_dir / np.linalg.norm(o_label_dir)
        else:
            o_label_dir = np.array([0, -1])
            
        put_vertex_label(ax, centroid, "O", centroid + o_label_dir, 0.12)
        
        put_vertex_label(ax, pA, "A", centroid, 0.12)
        put_vertex_label(ax, pB, "B", centroid, 0.12)
        put_vertex_label(ax, pC, "C", centroid, 0.12)
        put_vertex_label(ax, pD, "D", centroid, 0.12)

        # Expressions with white background for clarity
        props = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.8)
        ax.text(midAB[0]*0.5, midAB[1]*0.5, f"{self.d:.2f}", fontsize=12, fontweight='bold', ha='center', bbox=props)
        ax.text(midCD[0]*0.5, midCD[1]*0.5, f"{self.expr}", fontsize=12, fontweight='bold', ha='center', bbox=props)

        plt.text(1.1, 1.1, "NOT TO\nSCALE", fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat052:
    def __init__(self):
        # Property: Tangents from an external point are equal in length
        # They form two congruent right-angled triangles (OAP and OBP)
        self.radius = randrange_float(5.0, 10.0, 0.01)
        self.angle_apb = randrange_float(40.0, 70.0, 0.01)
        
        half_angle = self.angle_apb / 2
        # tan(half_angle) = radius / tangent_length
        self.tan_len = self.radius / math.tan(math.radians(half_angle))
        self.answer = round(self.tan_len, 2)

        self.description = (
            f"The diagram shows a circle with center $O$. $PA$ and $PB$ are tangents to the circle "
            f"from an external point $P$, touching the circle at $A$ and $B$. "
            f"The radius of the circle is ${self.radius} cm and angle $\\angle APB = {self.angle_apb}^\\circ$. "
            f"Calculate the length of the tangent $PA$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems II"
        self.source = "Original" # Complies with syllabus
        self.curriculum = "IGCSE"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Angle }} \\angle APB &= {round(self.angle_apb, 10)}^\\circ\\\\"
            f"\\text{{Radius, }} r &= {round(self.radius, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Since tangents from an external point are equal, }} PA &= PB. &\\\\"
            f"\\text{{The line }} OP \\text{{ bisects }} \\angle APB: &\\\\"
            f"\\angle APO &= \\frac{{\\angle APB}}{{2}}\\\\"
            f"&= \\frac{{{round(self.angle_apb, 10)}^\\circ}}{{2}}\\\\"
            f"&= {round(self.angle_apb / 2, 10)}^\\circ\\\\"
            f"\\text{{The radius }} OA \\text{{ is perpendicular to the tangent }} PA: &\\\\"
            f"\\angle OAP &= 90^\\circ\\\\"
            f"\\text{{In right-angled triangle }} OAP: &\\\\"
            f"\\tan(\\angle APO) &= \\frac{{OA}}{{PA}}\\\\"
            f"\\tan({round(self.angle_apb / 2, 10)}^\\circ) &= \\frac{{{round(self.radius, 10)}}}{{PA}}\\\\"
            f"PA &= \\frac{{{round(self.radius, 10)}}}{{\\tan({round(self.angle_apb / 2, 10)}^\\circ)}}\\\\"
            f"PA &= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Calculate geometric distance for plotting
        half_ang_rad = np.radians(self.angle_apb / 2)
        # Scale the plot so P fits in the frame
        vis_r = 0.5
        dist_op = vis_r / np.sin(half_ang_rad)
        
        limit = dist_op * 1.3
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.axis('off')

        # Global rotation for variety
        rotation = rnd.uniform(0, 360)
        rad_rot = np.radians(rotation)
        rot_mat = np.array([[np.cos(rad_rot), -np.sin(rad_rot)], [np.sin(rad_rot), np.cos(rad_rot)]])

        # Define points in local space
        p_local = np.array([dist_op, 0])
        ang_aop = np.pi/2 - half_ang_rad
        a_local = np.array([vis_r * np.cos(ang_aop), vis_r * np.sin(ang_aop)])
        b_local = np.array([vis_r * np.cos(ang_aop), -vis_r * np.sin(ang_aop)])
        o_local = np.array([0, 0])

        # Apply rotation
        P = rot_mat @ p_local
        A = rot_mat @ a_local
        B = rot_mat @ b_local
        O = o_local

        # Draw Geometry
        circle = plt.Circle(O, vis_r, color='black', fill=False, lw=2)
        ax.add_artist(circle)
        ax.plot(O[0], O[1], 'ko', markersize=6) # Center O point
        
        # Draw tangents and radii
        ax.plot([P[0], A[0]], [P[1], A[1]], color='black', lw=2) # Tangent PA
        ax.plot([P[0], B[0]], [P[1], B[1]], color='black', lw=2) # Tangent PB
        ax.plot([O[0], A[0]], [O[1], A[1]], color='black', lw=1.5) # Radius OA
        ax.plot([O[0], B[0]], [O[1], B[1]], color='black', lw=1.5) # Radius OB
        ax.plot([O[0], P[0]], [O[1], P[1]], color='black', lw=1, linestyle='--') # Line OP

        # Labels
        centroid = (O + A + B + P) / 4
        put_vertex_label(ax, O, "O", P, 0.1)
        put_vertex_label(ax, P, "P", O, 0.1)
        put_vertex_label(ax, A, "A", O, 0.12)
        put_vertex_label(ax, B, "B", O, 0.12)

        # Angle APB marking
        ang_p = get_angle(P, O) 
        arc_p = patches.Arc(P, 0.4, 0.4, theta1=ang_p - (self.angle_apb/2), 
                            theta2=ang_p + (self.angle_apb/2), color='black', lw=1)
        ax.add_patch(arc_p)
        
        t_pos = P + (O - P) / np.linalg.norm(O - P) * 0.5
        ax.text(t_pos[0], t_pos[1], f"{self.angle_apb}°", 
                fontsize=14, ha='center', fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

        plt.text(limit*0.8, limit*0.8, "NOT TO\nSCALE", fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat053:
    def __init__(self):
        # Property: Tangents from an external point are equal in length.
        # AR=AQ (x), BR=BP (y), CP=CQ (z)
        self.x = randrange_float(4.0, 7.0, 0.1)
        self.y = randrange_float(5.0, 8.0, 0.1)
        self.z = randrange_float(3.0, 6.0, 0.1)
        
        # Calculate full side lengths
        self.side_ab = self.x + self.y
        self.side_bc = self.y + self.z
        self.side_ac = self.x + self.z
        
        # Calculate Perimeter
        self.perimeter = self.side_ab + self.side_bc + self.side_ac
        
        # Problem setup: Known perimeter, known AR and BP, find side AC
        self.answer = self.side_ac

        self.description = (
            f"The diagram shows a circle inscribed in triangle $ABC$, touching the sides at $P$, $Q$, and $R$. "
            f"The perimeter of triangle $ABC$ is ${self.perimeter:.1f}$ cm. "
            f"Given that the tangent segments $AR = {self.x:.1f}$ cm and $BP = {self.y:.1f}$ cm, "
            f"calculate the length of the side $AC$."
        )
        
        self.topic = "Geometry"
        self.subtopic = "Circle theorems II"
        self.source = "Original" # Complies with syllabus
        self.curriculum = "IGCSE"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Perimeter of triangle }} ABC &= {round(self.perimeter, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Tangents from the same external point are equal in length:}} &\\\\"
            f"AQ &= AR = {round(self.x, 10)}\\,\\text{{cm}}\\\\"
            f"BR &= BP = {round(self.y, 10)}\\,\\text{{cm}}\\\\"
            f"CP &= CQ = z\\\\"
            f"\\text{{The perimeter is the sum of all tangent segments:}} &\\\\"
            f"P &= 2(AR + BP + CQ)\\\\"
            f"{round(self.perimeter, 10)} &= 2({round(self.x, 10)} + {round(self.y, 10)} + z)\\\\"
            f"\\frac{{{round(self.perimeter, 10)}}}{{2}} &= {round(self.x + self.y, 10)} + z\\\\"
            f"{round(self.perimeter / 2, 10)} &= {round(self.x + self.y, 10)} + z\\\\"
            f"z &= {round(self.perimeter / 2, 10)} - {round(self.x + self.y, 10)}\\\\"
            f"z &= {round(self.z, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Side }} AC \\text{{ is the sum of segments }} AQ \\text{{ and }} QC: &\\\\"
            f"AC &= AQ + QC = AR + CQ\\\\"
            f"&= {round(self.x, 10)} + {round(self.z, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # --- Mathematical Accuracy for Incircle Plotting ---
        a, b, c = self.side_bc, self.side_ac, self.side_ab
        s = self.perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        r_in = area / s
        
        # Base Coordinates (Local Space)
        B_local = np.array([0, 0])
        C_local = np.array([a, 0])
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        sin_B = math.sqrt(1 - cos_B**2)
        A_local = np.array([c * cos_B, c * sin_B])
        incenter_local = (a*A_local + b*B_local + c*C_local) / (self.perimeter)

        # Apply Global Random Rotation for Variety
        rotation_deg = rnd.uniform(0, 360)
        rad = np.radians(rotation_deg)
        rot_mat = np.array([[np.cos(rad), -np.sin(rad)], 
                            [np.sin(rad), np.cos(rad)]])

        A_coord = rot_mat @ A_local
        B_coord = rot_mat @ B_local
        C_coord = rot_mat @ C_local
        incenter = rot_mat @ incenter_local

        # Mathematically Derived Tangency Points
        P_coord = B_coord + (self.y / a) * (C_coord - B_coord)
        R_coord = B_coord + (self.y / c) * (A_coord - B_coord)
        Q_coord = A_coord + (self.x / b) * (C_coord - A_coord)

        # Draw Geometry
        triangle = plt.Polygon([A_coord, B_coord, C_coord], fill=False, lw=2, edgecolor='black')
        ax.add_patch(triangle)
        circle = plt.Circle(incenter, r_in, color='black', fill=False, lw=1.5)
        ax.add_artist(circle)
        
        all_pts = np.array([A_coord, B_coord, C_coord])
        min_x, min_y = np.min(all_pts, axis=0) - 1.5
        max_x, max_y = np.max(all_pts, axis=0) + 1.5
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)
        ax.set_aspect('equal')
        ax.axis('off')

        # Labels
        put_vertex_label(ax, A_coord, "A", incenter, 0.4)
        put_vertex_label(ax, B_coord, "B", incenter, 0.4)
        put_vertex_label(ax, C_coord, "C", incenter, 0.4)
        put_vertex_label(ax, P_coord, "P", incenter, -0.3)
        put_vertex_label(ax, Q_coord, "Q", incenter, -0.3)
        put_vertex_label(ax, R_coord, "R", incenter, -0.3)

        # Annotations
        def get_outside_pos(p1, p2, offset=0.4):
            mid = (p1 + p2) / 2
            vec = p2 - p1
            perp = np.array([-vec[1], vec[0]])
            # Ensure perp vector points away from incenter
            if np.dot(perp, mid - incenter) < 0:
                perp = -perp
            return mid + (perp / np.linalg.norm(perp)) * offset

        # Numeric Labels for AR and BP
        pos_ar = get_outside_pos(A_coord, R_coord, 0.3)
        ax.text(pos_ar[0], pos_ar[1], f"{self.x:.1f} cm", fontsize=11, fontweight='bold', ha='center')
        
        pos_bp = get_outside_pos(B_coord, P_coord, 0.3)
        ax.text(pos_bp[0], pos_bp[1], f"{self.y:.1f} cm", fontsize=11, fontweight='bold', ha='center')

        # Question Mark for Asked Side AC
        pos_ac = get_outside_pos(A_coord, C_coord, 0.5)
        ax.text(pos_ac[0], pos_ac[1], "?", fontsize=18, fontweight='bold', ha='center')

        # Perimeter and Scale Labels
        plt.text(min_x + 0.5, max_y - 0.5, f"Perimeter = {self.perimeter:.1f} cm", 
                 fontsize=13, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8))
        plt.text(max_x - 1.0, max_y - 0.5, "NOT TO\nSCALE", fontsize=11, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

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
        
        
class Mat074:
    def __init__(self):
        self.ab = randrange_float(10.0, 60.0, 0.01)
        self.bc = randrange_float(10.0, 60.0, 0.01)
        
        self.ac = round(math.sqrt(self.ab**2 + self.bc**2), 2)
        
        self.answer = self.bc

        self.description = (
            f"The diagram shows a right-angled triangle $ABC$. "
            f"Calculate $BC$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Pythagoras’ theorem"
        self.source = "Adapted from IGCSE June 2025 Question Paper 31"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given: }} AB &= {round(self.ab, 10)}\\,\\text{{cm}} \\\\"
            f"\\text{{Hypotenuse }} AC &= {round(self.ac, 10)}\\,\\text{{cm}} \\\\"
            "\\text{{Using Pythagoras' theorem:}} & \\\\"
            "AC^2 &= AB^2 + BC^2 \\\\"
            "BC^2 &= AC^2 - AB^2 \\\\"
            f"BC^2 &= ({round(self.ac, 10)})^2 - ({round(self.ab, 10)})^2 \\\\"
            f"BC^2 &= {round(self.ac**2, 10)} - {round(self.ab**2, 10)} \\\\"
            f"BC^2 &= {round(self.ac**2 - self.ab**2, 10)} \\\\"
            f"BC &= \\sqrt{{{round(self.ac**2 - self.ab**2, 10)}}} \\\\"
            f"BC &= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Generate a random rotation angle
        rotation = rnd.uniform(0, 360)
        theta = np.radians(rotation)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        # Define triangle vertices in local coordinates (B at origin)
        pB_local = np.array([0.0, 0.0])
        pA_local = np.array([0.0, self.ab])
        pC_local = np.array([self.bc, 0.0])

        # Apply rotation to the vertices
        pB = R @ pB_local
        pA = R @ pA_local
        pC = R @ pC_local
        
        all_pts = np.array([pA, pB, pC])

        # --- Centering the figure ---
        min_x, min_y = np.min(all_pts, axis=0)
        max_x, max_y = np.max(all_pts, axis=0)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        span_x = (max_x - min_x) / 2
        span_y = (max_y - min_y) / 2
        max_span = max(span_x, span_y)
        padding = max_span * 0.5 
        
        ax.set_xlim(center_x - max_span - padding, center_x + max_span + padding)
        ax.set_ylim(center_y - max_span - padding, center_y + max_span + padding)
        ax.set_aspect('equal')
        ax.axis('off')

        triangle = plt.Polygon(all_pts, fill=False, lw=2, edgecolor='black')
        ax.add_patch(triangle)

        # --- Add Right Angle Symbol ---
        size = min(self.ab, self.bc) * 0.12
        ra_local = np.array([[0, size], [size, size], [size, 0]])
        ra = (R @ ra_local.T).T
        ax.plot(ra[:, 0], ra[:, 1], color='black', lw=1.5)

        # --- Label Placement (Collision Avoidance) ---
        centroid = np.mean(all_pts, axis=0)
        vertex_offset_dist = max_span * 0.25

        put_vertex_label(ax, pA, 'A', centroid, vertex_offset_dist)
        put_vertex_label(ax, pB, 'B', centroid, vertex_offset_dist)
        put_vertex_label(ax, pC, 'C', centroid, vertex_offset_dist)

        side_label_offset_dist = max_span * 0.2

        mid_ab = (pA + pB) / 2
        offset_ab_local = np.array([-1.0, 0.0])
        pos_ab = mid_ab + (R @ offset_ab_local) * side_label_offset_dist
        ax.text(pos_ab[0], pos_ab[1], f"{self.ab:.1f} cm", fontsize=16, 
                ha='center', va='center')

        mid_ac = (pA + pC) / 2
        dir_ac = mid_ac - pB 
        dir_ac_unit = dir_ac / np.linalg.norm(dir_ac)
        pos_ac = mid_ac + dir_ac_unit * side_label_offset_dist
        ax.text(pos_ac[0], pos_ac[1], f"{self.ac:.1f} cm", fontsize=16, 
                ha='center', va='center')

        # --- "NOT TO SCALE" Label ---
        ax.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, 
                 fontsize=12, ha='right', va='top')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat075:
    def __init__(self):
        self.ground_dist = round(randrange_float(1.5, 8.5, 0.01), 2)
        self.wall_height = round(randrange_float(5.0, 15.0, 0.01), 2)
        
        # Calculate ladder length (hypotenuse)
        self.ladder_length = round(math.sqrt(self.ground_dist**2 + self.wall_height**2), 2)
        
        self.answer = self.ladder_length

        self.description = (
            f"A ladder rests against a vertical wall. The bottom of the ladder is ${self.ground_dist}$ m "
            f"from the bottom of the wall, on horizontal ground. The ladder reaches ${self.wall_height}$ m "
            f"up the wall. Calculate the length of the ladder."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Pythagoras’ theorem"
        self.source = "Adapted from 2025-specimen-paper-3"
        self.curriculum = "IGCSE"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance from wall (base), }} a &= {round(self.ground_dist, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Height reached (vertical), }} b &= {round(self.wall_height, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{The ladder length }} L \\text{{ is the hypotenuse:}} &\\\\"
            f"L^2 &= a^2 + b^2\\\\"
            f"L^2 &= ({round(self.ground_dist, 10)})^2 + ({round(self.wall_height, 10)})^2\\\\"
            f"L^2 &= {round(self.ground_dist**2, 10)} + {round(self.wall_height**2, 10)}\\\\"
            f"L^2 &= {round(self.ground_dist**2 + self.wall_height**2, 10)}\\\\"
            f"L &= \\sqrt{{{round(self.ground_dist**2 + self.wall_height**2, 10)}}}\\\\"
            f"L &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Coordinates: corner at origin, top of ladder on y-axis, base on x-axis
        p_corner = np.array([0, 0])
        p_top = np.array([0, self.wall_height])
        p_base = np.array([self.ground_dist, 0])
        
        # Wall and ground extensions for visual context
        wall_ext = self.wall_height + 1.5
        ground_ext = self.ground_dist + 2.0

        # Draw Wall (vertical) and Ground (horizontal)
        ax.plot([0, 0], [0, wall_ext], color='black', lw=2)
        ax.plot([0, ground_ext], [0, 0], color='black', lw=2)
        
        # Draw Ladder (hypotenuse)
        ax.plot([p_top[0], p_base[0]], [p_top[1], p_base[1]], color='black', lw=3.5)

        # Right angle symbol at origin
        ra_size = 0.5
        ra_rect = patches.Rectangle((0, 0), ra_size, ra_size, fill=False, edgecolor='black', lw=1.2)
        ax.add_patch(ra_rect)

        # --- Labels and Dimension Lines ---
        
        # Wall Height Label (placed left of the wall)
        ax.text(-0.6, self.wall_height / 2, f"{self.wall_height} m", 
                fontsize=14, ha='right', va='center')

        # Ground Distance Label and Arrows (placed below ground)
        arrow_y = -0.8
        ax.text(self.ground_dist / 2, arrow_y - 0.5, f"{self.ground_dist} m", 
                fontsize=14, ha='center', va='top')
        
        # Double-headed arrow for ground distance
        ax.annotate('', xy=(0, arrow_y), xytext=(self.ground_dist, arrow_y),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))

        # Ladder Label (placed offset from the ladder line)
        mid_ladder = (p_top + p_base) / 2
        ax.text(mid_ladder[0] + 0.5, mid_ladder[1] + 0.5, "$L$ m", 
                fontsize=16, fontweight='bold', ha='left', va='bottom')

        # Formatting
        ax.set_xlim(-2, ground_ext + 1)
        ax.set_ylim(-2, wall_ext + 1)
        ax.set_aspect('equal')
        ax.axis('off')

        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, 
                 fontsize=12, ha='center', va='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        
        plt.close()
        
class Mat076:
    def __init__(self):
        # 3D Pythagoras: Calculate the internal diagonal of a cuboid
        self.length = round(randrange_float(5.0, 15.0, 0.01), 2)
        self.width = round(randrange_float(5.0, 15.0, 0.01), 2)
        self.height = round(randrange_float(5.0, 15.0, 0.01), 2)
        
        # Internal diagonal formula: d = sqrt(l^2 + w^2 + h^2)
        self.diag_val = math.sqrt(self.length**2 + self.width**2 + self.height**2)
        self.answer = round(self.diag_val, 2)

        self.description = (
            f"The diagram shows a cuboid with length, width, height as shown in the figure cm. "
            f"Calculate the length of the internal diagonal from corner $A$ to corner $G$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Pythagoras’ theorem"
        self.source = "Common questions"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Length (l)}} &= {self.length}\\,\\text{{ cm}}\\\\"
            f"\\text{{Width (w)}} &= {self.width}\\,\\text{{ cm}}\\\\"
            f"\\text{{Height (h)}} &= {self.height}\\,\\text{{ cm}}\\\\"
            f"\\text{{The internal diagonal }} d \\text{{ of a cuboid is calculated using:}} &\\\\"
            f"d &= \\sqrt{{l^2 + w^2 + h^2}}\\\\"
            f"&= \\sqrt{{{self.length}^2 + {self.width}^2 + {self.height}^2}}\\\\"
            f"&= \\sqrt{{{round(self.length**2, 10)} + {round(self.width**2, 10)} + {round(self.height**2, 10)}}}\\\\"
            f"&= \\sqrt{{{round(self.length**2 + self.width**2 + self.height**2, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{ cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Isometric-style projection factors
        iso_x = 0.5
        iso_y = 0.5
        
        # Define 8 vertices of the cuboid
        # Bottom face
        A = np.array([0, 0])
        B = np.array([self.length, 0])
        C = np.array([self.length + self.width * iso_x, self.width * iso_y])
        D = np.array([self.width * iso_x, self.width * iso_y])
        
        # Top face
        E = A + np.array([0, self.height])
        F = B + np.array([0, self.height])
        G = C + np.array([0, self.height])
        H = D + np.array([0, self.height])

        # Draw Hidden Lines (Dashed)
        ax.plot([D[0], A[0]], [D[1], A[1]], color='black', lw=1, ls='--')
        ax.plot([D[0], C[0]], [D[1], C[1]], color='black', lw=1, ls='--')
        ax.plot([D[0], H[0]], [D[1], H[1]], color='black', lw=1, ls='--')

        # Draw Visible Lines (Solid)
        ax.plot([A[0], B[0]], [A[1], B[1]], color='black', lw=2)
        ax.plot([B[0], C[0]], [B[1], C[1]], color='black', lw=2)
        ax.plot([E[0], F[0]], [E[1], F[1]], color='black', lw=2)
        ax.plot([F[0], G[0]], [F[1], G[1]], color='black', lw=2)
        ax.plot([G[0], H[0]], [G[1], H[1]], color='black', lw=2)
        ax.plot([H[0], E[0]], [H[1], E[1]], color='black', lw=2)
        ax.plot([A[0], E[0]], [A[1], E[1]], color='black', lw=2)
        ax.plot([B[0], F[0]], [B[1], F[1]], color='black', lw=2)
        ax.plot([C[0], G[0]], [C[1], G[1]], color='black', lw=2)

        # Draw the internal diagonal (A to G)
        ax.plot([A[0], G[0]], [A[1], G[1]], color='red', lw=2, ls='-')

        # Vertex Labels
        ax.text(A[0]-0.5, A[1]-0.5, "A", fontsize=15, fontweight='bold')
        ax.text(G[0]+0.5, G[1]+0.5, "G", fontsize=15, fontweight='bold')

        # Dimension Labels
        ax.text(self.length/2, -1, f"{self.length} cm", fontsize=12, ha='center')
        ax.text(self.length + (self.width*iso_x)/2 + 0.5, (self.width*iso_y)/2, f"{self.width} cm", fontsize=12, rotation=30)
        ax.text(-1.5, self.height/2, f"{self.height} cm", fontsize=12, rotation=90, va='center')

        # Final Plot adjustments
        ax.set_aspect('equal')
        ax.axis('off')
        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
    
class Mat077:
    def __init__(self):
        # mode: 0 (sin), 1 (cos), 2 (tan)
        self.mode = rnd.choice([0, 1, 2])
        self.config = rnd.choice([0, 1])
        
        self.angle = round(randrange_float(25.0, 65.0, 0.01), 2)
        val_main = round(randrange_float(5.0, 15.0, 0.01), 2)

        if self.mode == 0: # SINE (Opp / Hyp)
            self.ratio_name = "\\sin"
            if self.config == 0: # Find Opposite
                self.hyp = val_main
                self.opp = self.hyp * math.sin(math.radians(self.angle))
                self.adj = self.hyp * math.cos(math.radians(self.angle))
                self.known_label, self.known_val = "hypotenuse", self.hyp
                self.asked_label, self.ans_val = "opposite", self.opp
            else: # Find Hypotenuse
                self.opp = val_main
                self.hyp = self.opp / math.sin(math.radians(self.angle))
                self.adj = self.hyp * math.cos(math.radians(self.angle))
                self.known_label, self.known_val = "opposite", self.opp
                self.asked_label, self.ans_val = "hypotenuse", self.hyp

        elif self.mode == 1: # COSINE (Adj / Hyp)
            self.ratio_name = "\\cos"
            if self.config == 0: # Find Adjacent
                self.hyp = val_main
                self.adj = self.hyp * math.cos(math.radians(self.angle))
                self.opp = self.hyp * math.sin(math.radians(self.angle))
                self.known_label, self.known_val = "hypotenuse", self.hyp
                self.asked_label, self.ans_val = "adjacent", self.adj
            else: # Find Hypotenuse
                self.adj = val_main
                self.hyp = self.adj / math.cos(math.radians(self.angle))
                self.opp = self.hyp * math.sin(math.radians(self.angle))
                self.known_label, self.known_val = "adjacent", self.adj
                self.asked_label, self.ans_val = "hypotenuse", self.hyp

        else: # TANGENT (Opp / Adj)
            self.ratio_name = "\\tan"
            if self.config == 0: # Find Opposite
                self.adj = val_main
                self.opp = self.adj * math.tan(math.radians(self.angle))
                self.hyp = math.sqrt(self.opp**2 + self.adj**2)
                self.known_label, self.known_val = "adjacent", self.adj
                self.asked_label, self.ans_val = "opposite", self.opp
            else: # Find Adjacent
                self.opp = val_main
                self.adj = self.opp / math.tan(math.radians(self.angle))
                self.hyp = math.sqrt(self.opp**2 + self.adj**2)
                self.known_label, self.known_val = "opposite", self.opp
                self.asked_label, self.ans_val = "adjacent", self.adj

        self.answer = self.ans_val

        self.description = "The diagram shows a right-angled triangle. Calculate the value of $x$."
        self.topic = "Trigonometry"
        self.subtopic = "Right-angled triangles"
        self.curriculum = "IGCSE", 
        self.source = "Adapted from IGCSE June 2025"

        # Dynamic Reasoning
        ratio_def = {
            0: "\\frac{\\text{Opposite}}{\\text{Hypotenuse}}",
            1: "\\frac{\\text{Adjacent}}{\\text{Hypotenuse}}",
            2: "\\frac{\\text{Opposite}}{\\text{Adjacent}}"
        }[self.mode]

        subst_step = (
            f"\\frac{{x}}{{{round(self.known_val, 10)}}}" 
            if self.config == 0 else 
            f"\\frac{{{round(self.known_val, 10)}}}{{x}}"
        )

        rearrange_step = (
            f"{round(self.known_val, 10)} \\times {self.ratio_name}({round(self.angle, 10)}^\\circ)" 
            if self.config == 0 else 
            f"\\frac{{{round(self.known_val, 10)}}}{{{self.ratio_name}({round(self.angle, 10)}^\\circ)}}"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the given parts relative to the angle }} {round(self.angle, 10)}^\\circ: &\\\\"
            f"\\text{{{self.known_label.capitalize()}}} &= {round(self.known_val, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{{self.asked_label.capitalize()}}} &= x\\\\"
            f"\\text{{Using the trigonometric ratio }} {self.ratio_name}: &\\\\"
            f"{self.ratio_name}(\\theta) &= {ratio_def}\\\\"
            f"{self.ratio_name}({round(self.angle, 10)}^\\circ) &= {subst_step}\\\\"
            f"x &= {rearrange_step}\\\\"
            f"x &= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        fx, fy = rnd.choice([-1, 1]), rnd.choice([-1, 1])
        
        # Base Vertices
        pA = np.array([0, 0]) # Angle vertex
        pB = np.array([self.adj * fx, 0]) # Right angle vertex
        pC = np.array([self.adj * fx, self.opp * fy]) # Top vertex
        pts = np.array([pA, pB, pC])
        
        ax.add_patch(plt.Polygon(pts, fill=False, lw=1, edgecolor='black'))

        # Right Angle Symbol
        ra = min(self.adj, self.opp) * 0.15
        ax.plot([pB[0]-ra*fx, pB[0]-ra*fx, pB[0]], [pB[1], pB[1]+ra*fy, pB[1]+ra*fy], color='black', lw=1.5)

        # Angle Arc at A
        arc_r = self.adj * 0.25
        t1 = 0 if fx > 0 else 180
        t2 = t1 + (self.angle if fx*fy > 0 else -self.angle)
        ax.add_patch(patches.Arc(pA, arc_r*2, arc_r*2, theta1=min(t1,t2), theta2=max(t1,t2), lw=1.5))
        
        mid_t = np.radians((t1 + t2) / 2)
        ax.text(arc_r*1.7*np.cos(mid_t), arc_r*1.7*np.sin(mid_t), f"{self.angle}°", fontsize=15, ha='center')

        # Label Placement
        labels = {
            "hypotenuse": ( (pA+pC)/2, np.array([-fy*self.opp, fx*self.adj])/self.hyp * 0.8 ),
            "adjacent": ( (pA+pB)/2, np.array([0, -0.7*fy]) ),
            "opposite": ( (pB+pC)/2, np.array([0.6*fx, 0]) )
        }

        for side, (pos, off) in labels.items():
            content = ""
            if side == self.known_label: content = f"{self.known_val} cm"
            elif side == self.asked_label: content = "$x$ cm"
            if content:
                ax.text(pos[0]+off[0], pos[1]+off[1], content, fontsize=16, ha='center', va='center')

        # Viewport
        buff = self.hyp * 0.3
        ax.set_xlim(min(pts[:,0])-buff, max(pts[:,0])+buff)
        ax.set_ylim(min(pts[:,1])-buff, max(pts[:,1])+buff)
        ax.set_aspect('equal'); ax.axis('off')
        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='center')
        plt.savefig(os.path.join(DESTINATION_FOLDER, f"image{num}.png"), bbox_inches='tight', dpi=100)
        plt.close()

class Mat078:
    def __init__(self):
        self.person_height = round(randrange_float(1.5, 1.9, 0.01), 2)
        self.distance = round(randrange_float(20.0, 50.0, 0.5), 1)
        self.angle_elevation = round(randrange_float(25.0, 45.0, 0.01), 2)
        
        self.opp_height = self.distance * math.tan(math.radians(self.angle_elevation))
        
        # Total tower height = height from eye level + person's height
        self.total_height = self.opp_height + self.person_height
        self.answer = round(self.total_height, 2)

        self.description = (
            f"A person of height {self.person_height} m stands on horizontal ground, "
            f"{self.distance} m from the base of a vertical tower. The angle of elevation "
            f"from the person's eyes to the top of the tower is {self.angle_elevation}^\\circ. "
            f"Calculate the total height of the tower."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Right-angled triangles"
        self.source = "Original question"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Height of person}} &= {round(self.person_height, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Distance from tower (Adjacent)}} &= {round(self.distance, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Angle of elevation (}} \\theta \\text{{)}} &= {round(self.angle_elevation, 10)}^\\circ\\\\"
            f"\\text{{Let }} h_{{opp}} \\text{{ be the height from eye level to the top of the tower:}} &\\\\"
            f"\\tan(\\theta) &= \\frac{{\\text{{Opposite}}}}{{\\text{{Adjacent}}}}\\\\"
            f"\\tan({round(self.angle_elevation, 10)}^\\circ) &= \\frac{{h_{{opp}}}}{{{round(self.distance, 10)}}}\\\\"
            f"h_{{opp}} &= {round(self.distance, 10)} \\times \\tan({round(self.angle_elevation, 10)}^\\circ)\\\\"
            f"h_{{opp}} &= {round(self.opp_height, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Total height (H)}} &= h_{{opp}} + \\text{{height of person}}\\\\"
            f"H &= {round(self.opp_height, 10)} + {round(self.person_height, 10)}\\\\"
            f"H &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        p_foot = np.array([0, 0])
        p_eye = np.array([0, self.person_height])
        p_tower_base = np.array([self.distance, 0])
        p_tower_top = np.array([self.distance, self.total_height])
        p_eye_level_base = np.array([self.distance, self.person_height])

        # Ground
        ax.plot([-5, self.distance + 10], [0, 0], color='black', lw=2)
        # Tower (represented as a thick rectangle or line)
        tower_width = 2
        tower_rect = patches.Rectangle((self.distance - tower_width/2, 0), tower_width, 
                                       self.total_height, color='gray', alpha=0.3)
        ax.add_patch(tower_rect)
        ax.plot([self.distance, self.distance], [0, self.total_height], color='black', lw=3)

        # Body
        ax.plot([0, 0], [0.5, self.person_height - 0.3], color='black', lw=2)
        # Legs
        ax.plot([0, -0.3], [0.5, 0], color='black', lw=2)
        ax.plot([0, 0.3], [0.5, 0], color='black', lw=2)
        # Arms
        ax.plot([0, -0.4], [self.person_height - 0.7, self.person_height - 0.5], color='black', lw=1.5)
        ax.plot([0, 0.4], [self.person_height - 0.7, self.person_height - 0.5], color='black', lw=1.5)
        # Head
        head = patches.Circle((0, self.person_height - 0.15), 0.15, color='black', fill=False, lw=2)
        ax.add_patch(head)

        # Line of sight (hypotenuse)
        ax.plot([p_eye[0], p_tower_top[0]], [p_eye[1], p_tower_top[1]], color='blue', ls='--', lw=2)
        # Horizontal eye level line (adjacent)
        ax.plot([p_eye[0], p_eye_level_base[0]], [p_eye[1], p_eye_level_base[1]], color='black', ls=':', lw=1.5)
        # Vertical tower segment (opposite)
        ax.plot([p_eye_level_base[0], p_tower_top[0]], [p_eye_level_base[1], p_tower_top[1]], color='red', lw=2)

        # Right angle symbol at p_eye_level_base
        ra_size = 1.0
        ax.plot([p_eye_level_base[0] - ra_size, p_eye_level_base[0] - ra_size, p_eye_level_base[0]], 
                [p_eye_level_base[1], p_eye_level_base[1] + ra_size, p_eye_level_base[1] + ra_size], 
                color='black', lw=1)

        # Angle of elevation arc
        arc_r = 3.0
        arc = patches.Arc(p_eye, arc_r*2, arc_r*2, theta1=0, theta2=self.angle_elevation, color='black', lw=1.5)
        ax.add_patch(arc)
        ax.text(arc_r + 1, self.person_height + 0.5, f"{self.angle_elevation}°", fontsize=12)

        # Dimension Labels
        # Ground distance
        ax.annotate('', xy=(0, -1), xytext=(self.distance, -1), arrowprops=dict(arrowstyle='<->'))
        ax.text(self.distance/2, -2, f"{self.distance} m", ha='center', fontsize=14)
        
        # Person height
        ax.text(-1, self.person_height/2, f"{self.person_height} m", ha='right', fontsize=12)
        
        # Total height asked
        ax.annotate('', xy=(self.distance + 4, 0), xytext=(self.distance + 4, self.total_height), 
                    arrowprops=dict(arrowstyle='<->'))
        ax.text(self.distance + 5, self.total_height/2, "$H$", fontsize=16, fontweight='bold')

        # Formatting
        ax.set_xlim(-10, self.distance + 15)
        ax.set_ylim(-5, self.total_height + 10)
        ax.set_aspect('equal')
        ax.axis('off')

        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat079:
    def __init__(self):
        # Triangle ACD
        self.angle_a = round(randrange_float(35.0, 55.0, 0.01), 2)
        self.side_ac = round(randrange_float(10.0, 20.0, 0.01), 2)
        
        # CD = AC * sin(A)
        self.height_cd = self.side_ac * math.sin(math.radians(self.angle_a))
        # AD = AC * cos(A)
        self.side_ad = self.side_ac * math.cos(math.radians(self.angle_a))
        
        # Triangle BCD
        # We provide side BC and ask for AB (which is AD + DB)
        # We must ensure BC > CD
        self.side_bc = round(self.height_cd + randrange_float(2.0, 8.0, 0.1), 1)
        
        # DB^2 = BC^2 - CD^2
        self.side_db = math.sqrt(self.side_bc**2 - self.height_cd**2)
        
        self.total_ab = self.side_ad + self.side_db
        self.answer = round(self.total_ab, 2)

        self.description = (
            f"In triangle $ABC$, $AC = {self.side_ac}$ cm and $BC = {self.side_bc}$ cm. "
            f"The angle $BAC = {self.angle_a}^\\circ$. A perpendicular is dropped from $C$ "
            f"to meet $AB$ at $D$. Calculate the length of $AB$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Right-angled triangles"
        self.source = "Original question"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{In triangle }} ACD: &\\\\"
            f"CD &= AC \\times \\sin(A)\\\\"
            f"&= {round(self.side_ac, 10)} \\times \\sin({round(self.angle_a, 10)}^\\circ)\\\\"
            f"&= {round(self.height_cd, 10)}\\,\\text{{cm}}\\\\"
            f"AD &= AC \\times \\cos(A)\\\\"
            f"&= {round(self.side_ac, 10)} \\times \\cos({round(self.angle_a, 10)}^\\circ)\\\\"
            f"&= {round(self.side_ad, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{In triangle }} BCD \\text{{ (using Pythagoras' theorem):}} &\\\\"
            f"DB &= \\sqrt{{BC^2 - CD^2}}\\\\"
            f"&= \\sqrt{{{round(self.side_bc, 10)}^2 - {round(self.height_cd, 10)}^2}}\\\\"
            f"&= \\sqrt{{{round(self.side_bc**2, 10)} - {round(self.height_cd**2, 10)}}}\\\\"
            f"&= {round(self.side_db, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{The total length }} AB \\text{{ is:}} &\\\\"
            f"AB &= AD + DB\\\\"
            f"&= {round(self.side_ad, 10)} + {round(self.side_db, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Coordinates
        pA = np.array([0, 0])
        pD = np.array([self.side_ad, 0])
        pB = np.array([self.total_ab, 0])
        pC = np.array([self.side_ad, self.height_cd])
        
        # Draw triangle ABC and height CD
        ax.plot([pA[0], pB[0], pC[0], pA[0]], [pA[1], pB[1], pC[1], pA[1]], color='black', lw=2)
        ax.plot([pD[0], pC[0]], [pD[1], pC[1]], color='black', ls='--', lw=1.5) # Height
        
        # Points and Right Angle
        ax.scatter([pA[0], pB[0], pC[0], pD[0]], [pA[1], pB[1], pC[1], pD[1]], color='black')
        for pt, txt in zip([pA, pB, pC, pD], ['A', 'B', 'C', 'D']):
            ax.text(pt[0], pt[1] + (0.5 if txt=='C' else -1), txt, fontsize=14, ha='center')

        # Right angle symbol at D
        ra_size = 0.5
        ax.plot([pD[0]-ra_size, pD[0]-ra_size, pD[0]], [pD[1], pD[1]+ra_size, pD[1]+ra_size], color='black')

        # Angle arc at A
        arc_r = 1.5
        ax.add_patch(patches.Arc(pA, arc_r*2, arc_r*2, theta1=0, 
                                 theta2=self.angle_a, color='black', lw=1.5))
        ax.text(arc_r+0.5, 0.5, f"{self.angle_a}°", fontsize=12)

        # Dimension Labels
        ax.text(pA[0] + self.side_ad/2 - 1, self.height_cd/2, f"{self.side_ac} cm", rotation=self.angle_a)
        ax.text(pD[0] + self.side_db/2 + 1, self.height_cd/2, f"{self.side_bc} cm", 
                rotation=-np.degrees(np.arctan2(self.height_cd, self.side_db)))

        # Final Formatting
        ax.set_xlim(-2, self.total_ab + 2)
        ax.set_ylim(-3, self.height_cd + 3)
        ax.set_aspect('equal')
        ax.axis('off')

        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat080:
    def __init__(self):
        self.func_type = rnd.choice(["sin", "cos"])
        self.a = rnd.randint(2, 5)            
        self.b = rnd.choice([1, 2, 3])        
        self.c = rnd.choice([-30, -45, -60, -90]) 
        self.d = rnd.randint(-4, 4)           
        
        self.func_name = f"\\{self.func_type}"
        self.answer = f"{self.a}, {self.b}, {self.c}, {self.d}"
        
        self.x_anchor = round(-self.c / self.b, 10)

        self.description = (
            f"The diagram shows the graph of a trigonometric function of the form "
            f"$y = a {self.func_name}(bx + c) + d$. "
            f"Find the values of $a$, $b$, $c$, and $d$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Trigonometric functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 43"
        self.curriculum = "IGCSE"

        # Branching Reasoning Logic
        common_start = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Find vertical shift (}} d \\text{{): midline of the wave}} & \\\\"
            f"\\text{{Identify the maximum }} y\\text{{-value (peak) and minimum }} y\\text{{-value (trough) on the y-axis.}} & \\\\"
            f"\\text{{Max}} = {self.a + self.d}, \\, \\text{{Min}} = {self.d - self.a} & \\\\"
            f"d &= \\frac{{\\text{{Max}} + \\text{{Min}}}}{{2}} = \\frac{{{self.a + self.d} + ({self.d - self.a})}}{{2}} = {self.d} \\\\"
            f"\\text{{2. Find coefficient (}} a \\text{{): vertical stretch/amplitude}} & \\\\"
            f"\\text{{Calculate the distance from the midline (}} d = {self.d} \\text{{) to the peak (}} y = {self.a + self.d} \\text{{).}} & \\\\"
            f"a &= \\text{{Max}} - d = {self.a + self.d} - {self.d} = {self.a} \\\\"
        )

        if self.func_type == "sin":
            self.reasoning = common_start + (
                f"\\text{{3. Find period (}} P \\text{{) and frequency (}} b \\text{{):}} & \\\\"
                f"\\text{{Standard period for sin is }} 360^\\circ. \\text{{ Measure the distance for one full cycle on the x-axis.}} & \\\\"
                f"\\text{{Observed Period }} P &= {round(360/self.b, 10)}^\\circ \\\\"
                f"b &= \\frac{{360^\\circ}}{{P}} = \\frac{{360^\\circ}}{{{round(360/self.b, 10)}^\\circ}} = {self.b} \\\\"
                f"\\text{{4. Find phase shift (}} c \\text{{) using the midline crossing:}} & \\\\"
                f"\\text{{The graph crosses the midline moving upwards at }} x = {self.x_anchor}^\\circ. & \\\\"
                f"\\text{{In }} y = a \\sin(bx + c) + d, \\text{{ the argument equals 0 at this point:}} & \\\\"
                f"b(x) + c &= 0 \\implies {self.b}({self.x_anchor}) + c = 0 \\\\"
                f"c &= {self.c}^\\circ \\\\"
                f"\\text{{5. Final parameters identified: }} a, b, c, d &= {self.answer}"
                "\\end{aligned}\\]"
            )
        else: # cos
            self.reasoning = common_start + (
                f"\\text{{3. Find period (}} P \\text{{) and frequency (}} b \\text{{):}} & \\\\"
                f"\\text{{Standard period for cos is }} 360^\\circ. \\text{{ Measure the distance between two consecutive peaks.}} & \\\\"
                f"\\text{{Observed Period }} P &= {round(360/self.b, 10)}^\\circ \\\\"
                f"b &= \\frac{{360^\\circ}}{{P}} = \\frac{{360^\\circ}}{{{round(360/self.b, 10)}^\\circ}} = {self.b} \\\\"
                f"\\text{{4. Find phase shift (}} c \\text{{) using the first peak:}} & \\\\"
                f"\\text{{The first visible peak is located at }} x = {self.x_anchor}^\\circ. & \\\\"
                f"\\text{{In }} y = a \\cos(bx + c) + d, \\text{{ the argument equals 0 at a peak:}} & \\\\"
                f"b(x) + c &= 0 \\implies {self.b}({self.x_anchor}) + c = 0 \\\\"
                f"c &= {self.c}^\\circ \\\\"
                f"\\text{{5. Final parameters identified: }} a, b, c, d &= {self.answer}"
                "\\end{aligned}\\]"
            )
            
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.linspace(0, 360, 1000)
        x_rad = np.radians(x)
        
        if self.func_type == "sin":
            y = self.a * np.sin(self.b * x_rad + np.radians(self.c)) + self.d
        elif self.func_type == "cos":
            y = self.a * np.cos(self.b * x_rad + np.radians(self.c)) + self.d

        ax.plot(x, y, color='black', lw=2.5)
        ax.axhline(0, color='black', lw=1.2)
        ax.axvline(0, color='black', lw=1.2)
        
        # Grid and Ticks
        ax.grid(True, which='major', ls='--', alpha=0.6, color='gray')
        ax.grid(True, which='minor', ls=':', alpha=0.4, color='lightgray')
        ax.set_xlim(0, 360)
        
        # Adaptive y-limits
        if self.func_type == "tan":
            ax.set_ylim(-10, 10)
        else:
            ax.set_ylim(self.d - self.a - 2, self.d + self.a + 2)

        major_ticks = np.arange(0, 361, 90)
        special_ticks = [30, 45, 60]
        all_tick_pos = np.sort(np.unique(np.concatenate([major_ticks, special_ticks])))
        
        ax.set_xticks(all_tick_pos)
        ax.set_xticklabels([f'{int(t)}°' for t in all_tick_pos], fontsize=10)
        ax.xaxis.set_minor_locator(MultipleLocator(15))
        
        plt.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=10, ha='right', va='top')
        ax.set_xlabel("x (degrees)")
        ax.set_ylabel("y")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat081:
    def __init__(self):
        self.a = rnd.choice([1, 2, 3])
        self.b = rnd.choice([1, 2])
        self.c = rnd.choice([0, 45, -45, 90, -90])
        self.d = rnd.randint(-3, 3)
        
        target_inner = rnd.choice([-1, 0, 1])
        self.k_total = self.a * target_inner + self.d
        
        def get_fmt_func(a, b, c, d):
            a_str = f"{a}" if a != 1 else ""
            b_str = f"{b}x" if b != 1 else "x"
            c_str = ""
            if c > 0: c_str = f" + {c}"
            elif c < 0: c_str = f" - {abs(c)}"
            
            d_str = ""
            if d > 0: d_str = f" + {d}"
            elif d < 0: d_str = f" - {abs(d)}"
            
            return f"{a_str}\\tan({b_str}{c_str}){d_str}"

        self.func_display = get_fmt_func(self.a, self.b, self.c, self.d)
        lhs_implicit = get_fmt_func(self.a, self.b, self.c, 0)
        rhs_implicit = self.k_total - self.d
        self.implicit_eq = f"{lhs_implicit} = {rhs_implicit}"
        
        # Solve for x
        inner_angle_deg = np.degrees(np.arctan(target_inner))
        sols = []
        period = 180 / self.b
        first_sol = (inner_angle_deg - self.c) / self.b
        
        for n in range(-5, 10):
            s = first_sol + n * period
            if 0 <= s <= 360:
                sols.append(int(round(s)))
        
        sorted_sols = sorted(list(set(sols)))
        self.answer = ", ".join([f"{s}^\\circ" for s in sorted_sols])

        self.description = (
            f"The diagram shows the graph of $y = f(x)$ where $f(x) = {self.func_display}$. "
            f"Using the visual information provided, find all solutions for ${self.implicit_eq}$ "
            f"in the range $0^\\circ \\leqslant x \\leqslant 360^\\circ$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Trigonometric functions"
        self.source = "Adapted from IGCSE June 2025 Question Paper 43"
        self.curriculum = "IGCSE"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Start with the given equation:}} & \\\\"
            f"{self.implicit_eq} & \\\\"
            f"\\text{{2. To use the graph, transform the equation into the form }} f(x) = k: & \\\\"
            f"\\text{{The function is defined as }} f(x) &= {self.func_display} \\\\"
            f"\\text{{Add the vertical shift }} ({self.d}) \\text{{ to both sides of the equation:}} & \\\\"
            f"{lhs_implicit} + ({self.d}) &= {rhs_implicit} + ({self.d}) \\\\"
            f"f(x) &= {self.k_total} \\\\"
            f"\\text{{3. Identify intersection points visually:}} & \\\\"
            f"\\text{{Locate the line }} y = {self.k_total} \\text{{ on the y-axis and find where it intersects the curve.}} & \\\\"
            f"\\text{{At }} y = {self.k_total}, \\text{{ the horizontal line crosses }} f(x) \\text{{ at:}} & \\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )
                
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x = np.linspace(0, 360, 3000)
        y = self.a * np.tan(np.radians(self.b * x + self.c)) + self.d
        y[np.abs(y) > 20] = np.nan 

        ax.plot(x, y, color='black', lw=2)
        
        # Styling and Grid
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        ax.grid(True, which='major', ls='-', alpha=0.5, color='gray')
        ax.grid(True, which='minor', ls=':', alpha=0.3, color='gray')
        
        ax.set_xlim(0, 360)
        ax.set_ylim(self.d - 6, self.d + 6)
        
        ax.set_xticks(np.arange(0, 361, 45))
        ax.xaxis.set_minor_locator(MultipleLocator(15))
        ax.yaxis.set_major_locator(MultipleLocator(2))
        
        ax.set_xlabel("$x$ (degrees)")
        ax.set_ylabel("$y$")
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=150)
        plt.close()
        
class Mat082:
    def __init__(self):
        # Generate side lengths and area
        self.side_a = randrange_float(10.0, 20.0, 0.01)
        self.side_b = randrange_float(10.0, 20.0, 0.01)
        
        # Ensure sin(x) is valid (0 < sin(x) <= 1)
        # Area = 0.5 * a * b * sin(x) -> sin(x) = (2 * Area) / (a * b)
        # Max possible area for these sides is when sin(x) = 1
        max_area = 0.5 * self.side_a * self.side_b
        self.area = randrange_float(max_area * 0.4, max_area * 0.9, 0.01)
        
        # Calculate sin(x) as the answer
        self.answer = (2 * self.area) / (self.side_a * self.side_b)

        self.description = (
            f"Based on the image, calculate the value of $\\sin x$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Non-right-angled triangles"
        self.source = "Adapted from 2025-specimen-paper-4"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The formula for the area of a triangle is:}} &\\\\"
            f"\\text{{Area}} &= \\frac{{1}}{{2}}ab \\sin C \\\\"
            f"\\text{{Given:}} &\\\\"
            f"\\text{{Area}} &= {round(self.area, 10)}\\,\\text{{cm}}^2 \\\\"
            f"\\text{{Side }} a &= {round(self.side_a, 10)}\\,\\text{{cm}} \\\\"
            f"\\text{{Side }} b &= {round(self.side_b, 10)}\\,\\text{{cm}} \\\\"
            f"\\text{{Substitute the values into the formula:}} &\\\\"
            f"{round(self.area, 10)} &= \\frac{{1}}{{2}} \\times {round(self.side_a, 10)} \\times {round(self.side_b, 10)} \\times \\sin x \\\\"
            f"{round(self.area, 10)} &= {round(0.5 * self.side_a * self.side_b, 10)} \\times \\sin x \\\\"
            f"\\sin x &= \\frac{{{round(self.area, 10)}}}{{{round(0.5 * self.side_a * self.side_b, 10)}}} \\\\"
            f"\\sin x &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_aspect('equal')
        ax.axis('off')

        # Calculate the angle x for drawing purposes
        angle_x_rad = math.asin(self.answer)
        
        # Define vertices
        # V1 is at origin (where angle x is)
        # V2 is along the x-axis (length side_a)
        # V3 is at (side_b * cos(x), side_b * sin(x))
        p1 = np.array([0, 0])
        p2 = np.array([self.side_a, 0])
        p3 = np.array([self.side_b * math.cos(angle_x_rad), self.side_b * math.sin(angle_x_rad)])

        # Random rotation and translation for variation
        rot_angle = rnd.uniform(0, 2 * math.pi)
        rot_matrix = np.array([
            [math.cos(rot_angle), -math.sin(rot_angle)],
            [math.sin(rot_angle), math.cos(rot_angle)]
        ])
        
        pts = np.array([p1, p2, p3]) @ rot_matrix.T
        
        # Draw triangle
        triangle = plt.Polygon(pts, fill=False, lw=2, edgecolor='black')
        ax.add_patch(triangle)

        # Re-extract rotated points
        rp1, rp2, rp3 = pts[0], pts[1], pts[2]

        # Labels for sides
        # Side a (between p1 and p2)
        mid_12 = (rp1 + rp2) / 2
        offset_12 = 0.5 * np.array([-(rp2[1]-rp1[1]), rp2[0]-rp1[0]]) / np.linalg.norm(rp2-rp1)
        ax.text(mid_12[0] + offset_12[0], mid_12[1] + offset_12[1], 
                f"{round(self.side_a, 2)} cm", fontsize=12, ha='center', va='center')

        # Side b (between p1 and p3)
        mid_13 = (rp1 + rp3) / 2
        offset_13 = 0.5 * np.array([rp3[1]-rp1[1], -(rp3[0]-rp1[0])]) / np.linalg.norm(rp3-rp1)
        ax.text(mid_13[0] + offset_13[0], mid_13[1] + offset_13[1], 
                f"{round(self.side_b, 2)} cm", fontsize=12, ha='center', va='center')

        # Label for angle x at p1
        ang_start = get_angle(rp1, rp2)
        ang_end = get_angle(rp1, rp3)
        
        # Adjust arc angles to ensure it's drawn correctly
        if (ang_end - ang_start) % 360 > 180:
            ang_start, ang_end = ang_end, ang_start
            
        arc_radius = min(self.side_a, self.side_b) * 0.2
        arc = patches.Arc(rp1, arc_radius*2, arc_radius*2, theta1=ang_start, theta2=ang_end, color='black', lw=1.5)
        ax.add_patch(arc)
        
        mid_angle = math.radians((ang_start + ang_end) / 2)
        if abs(ang_end - ang_start) > 180: mid_angle += math.pi
            
        tx = rp1[0] + arc_radius * 1.5 * math.cos(mid_angle)
        ty = rp1[1] + arc_radius * 1.5 * math.sin(mid_angle)
        ax.text(tx, ty, "$x^\\circ$", fontsize=14, ha='center', va='center')

        # Add metadata text
        ax.text(0.95, 0.95, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=10, ha='right', va='top')
        ax.text(0.05, 0.05, f"Area = {round(self.area, 2)} $cm^2$", transform=ax.transAxes, fontsize=12)

        # Set limits
        all_x, all_y = pts[:, 0], pts[:, 1]
        ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
        ax.set_ylim(min(all_y) - 2, max(all_y) + 2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat083:
    def __init__(self):
        # Using Cosine Rule: a^2 = b^2 + c^2 - 2bc cos(A)
        # Side b (AC), side c (BC), Angle C (ACB)
        self.side_ac = randrange_float(50.0, 80.0, 0.01)
        self.side_bc = randrange_float(85.0, 110.0, 0.01)
        self.angle_c = randrange_float(30.0, 50.0, 0.01)
        
        # Calculate AB
        self.answer = math.sqrt(
            self.side_ac**2 + self.side_bc**2 - 
            2 * self.side_ac * self.side_bc * math.cos(math.radians(self.angle_c))
        )

        self.description = (
            "The diagram shows the positions of three points $A$, $B$ and $C$. "
            "Based on the information in the figure, calculate the distance $AB$."
        )
        
        self.topic = "Trigonometry"
        self.subtopic = "Non-right-angled triangles"
        self.source = "Adapted from IGCSE June 2025 Question Paper 42"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the given values in }} \\triangle ABC: &\\\\"
            f"b = AC &= {round(self.side_ac, 10)}\\,\\text{{m}}\\\\"
            f"a = BC &= {round(self.side_bc, 10)}\\,\\text{{m}}\\\\"
            f"C = \\angle ACB &= {round(self.angle_c, 10)}^\\circ\\\\"
            f"\\text{{To find the distance }} AB \\text{{ (side }} c \\text{{), use the Cosine Rule:}} &\\\\"
            f"c^2 &= a^2 + b^2 - 2ab \\cos(C)\\\\"
            f"c^2 &= ({round(self.side_bc, 10)})^2 + ({round(self.side_ac, 10)})^2 - 2({round(self.side_bc, 10)})({round(self.side_ac, 10)}) \\cos({round(self.angle_c, 10)}^\\circ)\\\\"
            f"c^2 &= {round(self.side_bc**2, 10)} + {round(self.side_ac**2, 10)} - {round(2 * self.side_bc * self.side_ac, 10)} \\cos({round(self.angle_c, 10)}^\\circ)\\\\"
            f"c &= \\sqrt{{{round(self.side_bc**2 + self.side_ac**2, 10)} - {round(2 * self.side_bc * self.side_ac * math.cos(math.radians(self.angle_c)), 10)}}}\\\\"
            f"c &= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect('equal')
        ax.axis('off')

        # Triangle construction in local space
        # C is at origin
        # B is on x-axis
        # A is at (ac*cos(c), ac*sin(c))
        p_c = np.array([0, 0])
        p_b = np.array([self.side_bc, 0])
        p_a = np.array([
            self.side_ac * math.cos(math.radians(self.angle_c)),
            self.side_ac * math.sin(math.radians(self.angle_c))
        ])

        # Random global rotation
        rot_angle = rnd.uniform(0, 360)
        rot_rad = math.radians(rot_angle)
        rot_mat = np.array([
            [math.cos(rot_rad), -math.sin(rot_rad)],
            [math.sin(rot_rad), math.cos(rot_rad)]
        ])

        pts = {
            'A': p_a @ rot_mat.T,
            'B': p_b @ rot_mat.T,
            'C': p_c @ rot_mat.T
        }

        # Draw triangle
        triangle = plt.Polygon([pts['A'], pts['B'], pts['C']], fill=False, lw=1, edgecolor='black')
        ax.add_patch(triangle)

        # Draw North arrow at A
        arrow_dirs = ["North", "East", "South", "West"]
        arrow_label = rnd.choice(arrow_dirs)
        # Randomize north arrow direction (0: Up, 90: Right, etc)
        arrow_rot = {"North": 90, "East": 0, "South": 270, "West": 180}[arrow_label]
        
        arrow_len = self.side_ac * 0.4
        arrow_end = pts['A'] + np.array([
            arrow_len * math.cos(math.radians(arrow_rot)),
            arrow_len * math.sin(math.radians(arrow_rot))
        ])
        
        ax.annotate('', xy=arrow_end, xytext=pts['A'],
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        ax.text(arrow_end[0], arrow_end[1] + (arrow_len*0.1), arrow_label, 
                ha='center', va='bottom', fontsize=14)

        # Labels for points
        label_dist = self.side_ac * 0.1
        for label, pt in pts.items():
            # simple outward vector from centroid
            centroid = (pts['A'] + pts['B'] + pts['C']) / 3
            vec = pt - centroid
            vec = vec / np.linalg.norm(vec) * label_dist
            ax.text(pt[0] + vec[0], pt[1] + vec[1], label, 
                    fontsize=16, ha='center', va='center', fontweight='bold', style='italic')

        # Side labels
        # AC
        mid_ac = (pts['A'] + pts['C']) / 2
        perp_ac = np.array([-(pts['A'][1]-pts['C'][1]), pts['A'][0]-pts['C'][0]])
        perp_ac = perp_ac / np.linalg.norm(perp_ac) * label_dist
        ax.text(mid_ac[0] + perp_ac[0], mid_ac[1] + perp_ac[1], f"{round(self.side_ac, 2)} m", 
                ha='center', va='center', fontsize=12)

        # BC
        mid_bc = (pts['B'] + pts['C']) / 2
        perp_bc = np.array([-(pts['B'][1]-pts['C'][1]), pts['B'][0]-pts['C'][0]])
        perp_bc = perp_bc / np.linalg.norm(perp_bc) * label_dist
        # Flip if it goes inside
        centroid = (pts['A'] + pts['B'] + pts['C']) / 3
        if np.linalg.norm((mid_bc + perp_bc) - centroid) < np.linalg.norm(mid_bc - centroid):
            perp_bc = -perp_bc
        ax.text(mid_bc[0] + perp_bc[0], mid_bc[1] + perp_bc[1], f"{round(self.side_bc, 2)} m", 
                ha='center', va='center', fontsize=12)

        # Angle marking at C
        ang_start = get_angle(pts['C'], pts['B'])
        ang_end = get_angle(pts['C'], pts['A'])
        
        # Ensure counter-clockwise arc
        if (ang_end - ang_start) % 360 > 180:
            ang_start, ang_end = ang_end, ang_start
            
        arc_r = self.side_ac * 0.25
        arc = patches.Arc(pts['C'], arc_r, arc_r, theta1=ang_start, theta2=ang_end, color='black', lw=1)
        ax.add_patch(arc)
        
        mid_ang = math.radians((ang_start + ang_end) / 2)
        tx = pts['C'][0] + arc_r * 0.8 * math.cos(mid_ang)
        ty = pts['C'][1] + arc_r * 0.8 * math.sin(mid_ang)
        ax.text(tx, ty, f"{round(self.angle_c, 2)}°", ha='center', va='center', fontsize=12)

        plt.text(0.9, 0.9, "NOT TO\nSCALE", transform=ax.transAxes, fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

        # Set limits
        all_pts = np.array(list(pts.values()))
        x_min, x_max = all_pts[:, 0].min(), all_pts[:, 0].max()
        y_min, y_max = all_pts[:, 1].min(), all_pts[:, 1].max()
        pad = self.side_bc * 0.3
        ax.set_xlim(x_min - pad, x_max + pad)
        ax.set_ylim(y_min - pad, y_max + pad)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()        
        
class Mat089:
    
    def __init__(self):
        # Randomize base and height for Triangle A (small)
        self.base_a = rnd.randint(2, 5)
        self.height_a = rnd.randint(2, 5)
        
        # Randomize scale factor (integer for simplicity)
        self.scale_factor = rnd.randint(2, 5)
        
        # Calculate dimensions for Triangle B (large)
        self.base_b = self.base_a * self.scale_factor
        self.height_b = self.height_a * self.scale_factor

        # Either of these
        self.answer = self.scale_factor
        self.answer = self.base_b // self.base_a
        self.answer = self.height_b // self.height_a

        self.description = (
            f"What is the scale factor of the enlargement?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Transformations"
        self.source = "Adapted from Cambridge IGCSE Mathematics (0580) Past Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Scale Factor}} &= \\frac{{\\text{{Base of Triangle B}}}}{{\\text{{Base of Triangle A}}}}\\\\"
            f"&= \\frac{{{self.base_b}}}{{{self.base_a}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define Coordinates
        # Using right-angled triangles for clear grid alignment
        
        # Triangle A (Small)
        start_ax, start_ay = 1, 1
        triangle_a_coords = [
            (start_ax, start_ay),                  # Bottom-left
            (start_ax + self.base_a, start_ay),         # Bottom-right
            (start_ax, start_ay + self.height_a)        # Top-left
        ]
        
        # Triangle B (Large) - Shifted to the right to avoid overlap
        padding = 2
        start_bx = start_ax + self.base_a + padding
        start_by = 1
        triangle_b_coords = [
            (start_bx, start_by),
            (start_bx + self.base_b, start_by),
            (start_bx, start_by + self.height_b)
        ]
        
        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Draw Triangles
        poly_a = patches.Polygon(triangle_a_coords, closed=True, 
                                facecolor='#87CEEB', edgecolor='blue', alpha=0.7, label='Triangle A')
        poly_b = patches.Polygon(triangle_b_coords, closed=True, 
                                facecolor='#FA8072', edgecolor='red', alpha=0.7, label='Triangle B')
        
        ax.add_patch(poly_a)
        ax.add_patch(poly_b)
        
        # Grid and Axes Configuration
        # Determine plot limits
        max_x = start_bx + self.base_b + 2
        max_y = max(start_ay + self.height_a, start_by + self.height_b) + 2
        
        ax.set_xlim(0, max_x)
        ax.set_ylim(0, max_y)
        ax.set_aspect('equal')
        
        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
        ax.set_xticks(range(0, int(max_x) + 1))
        ax.set_yticks(range(0, int(max_y) + 1))
        
        # Annotations
        # Label the triangles
        # Centroid-ish position for label
        ax.text(start_ax + self.base_a/3, start_ay + self.height_a/3, "A", 
                fontsize=15, fontweight='bold', color='darkblue')
        ax.text(start_bx + self.base_b/3, start_by + self.height_b/3, "B", 
                fontsize=15, fontweight='bold', color='darkred')

        # Adjust layout to make room for text
        plt.subplots_adjust(bottom=0.25)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat090:
    
    def __init__(self):
        # Choose a base side length for P (so Area P is a perfect square for simplicity, or just simple int)
        self.side_p = rnd.randint(2, 5) # In cm
        self.area_p = self.side_p ** 2 # In cm
        
        # Choose a scale factor (k)
        self.scale_factor = round(rnd.uniform(2, 4), 1) # In cm
        
        # Calculate Shape Q properties
        self.side_q = self.side_p * self.scale_factor # In cm
        self.area_q = self.area_p * (self.scale_factor ** 2) # In cm

        self.answer = round(self.area_q, 2)

        self.description = (
            f"What is the area of shape Q in cm²?, Give your answer correct to 2 decimal places."
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Transformations"
        self.source = "Based on standard IGCSE/O Level \"Area Scale Factor\" questions"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area of shape P}} &= {self.area_p}\\,\\text{{cm}}^2\\\\"
            f"\\text{{Scale factor (k)}} &= {self.scale_factor}\\\\"
            f"\\text{{Area of shape Q is given by:}} &\\\\"
            f"\\text{{Area}}_Q &= k^2 \\times \\text{{Area}}_P\\\\"
            f"&= ({self.scale_factor})^2 \\times {self.area_p}\\\\"
            f"&= {round(self.scale_factor**2, 10)} \\times {self.area_p}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # --- 2. Setup Plot ---
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Determine canvas limits based on larger shape
        spacing = self.side_p * 1.5
        total_width = self.side_p + spacing + self.side_q
        max_height = max(self.side_p, self.side_q)
        
        ax.set_xlim(-1, total_width + 1)
        ax.set_ylim(-1, max_height + 2)
        ax.set_aspect('equal')
        ax.axis('off')  # Turn off axis numbers

        # --- 3. Draw Shape P (Original) ---
        # Draw a square for P
        rect_p = patches.Rectangle((0, 0), self.side_p, self.side_p, 
                                edgecolor='blue', facecolor='skyblue', alpha=0.6, linewidth=2)
        ax.add_patch(rect_p)
        
        # Label P
        cx_p = self.side_p / 2
        cy_p = self.side_p / 2
        ax.text(cx_p, cy_p, f"Shape P\nArea = {self.area_p} cm²", 
                ha='center', va='center', fontsize=10, fontweight='bold', color='darkblue')

        # --- 4. Draw Shape Q (Enlarged) ---
        # Draw a square for Q, offset to the right
        start_x_q = self.side_p + spacing
        rect_q = patches.Rectangle((start_x_q, 0), self.side_q, self.side_q, 
                                edgecolor='red', facecolor='salmon', alpha=0.6, linewidth=2)
        ax.add_patch(rect_q)

        # Label Q
        cx_q = start_x_q + (self.side_q / 2)
        cy_q = self.side_q / 2
        ax.text(cx_q, cy_q, "Shape Q\nArea = ?", 
                ha='center', va='center', fontsize=12, fontweight='bold', color='darkred')

        # --- 5. Annotations (Arrow & Scale Factor) ---
        # Draw an arrow from P to Q
        arrow_start = (self.side_p + 0.5, self.side_p / 2)
        arrow_end = (start_x_q - 0.5, self.side_q / 2)
        
        # If the arrow is slanted (because Q is taller), keep it horizontal centered on P
        arrow_y = self.side_p / 2
        arrow_end_adj = (start_x_q - 0.5, arrow_y)
        
        ax.annotate("", xy=arrow_end_adj, xytext=arrow_start,
                    arrowprops=dict(arrowstyle="->", lw=2, color='black'))
        
        # Text for Scale Factor
        mid_x = (arrow_start[0] + arrow_end_adj[0]) / 2
        ax.text(mid_x, arrow_y + 0.5, f"Enlargement\nScale Factor = {self.scale_factor}", 
                ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat091:
    
    def __init__(self):
        # We choose range 2 to 8 to keep points distinct from origin and clearly visible
        self.x = rnd.randint(2, 8) 
        self.y = rnd.randint(2, 8)
        
        # Calculate New Coordinates (90 degrees clockwise)
        # Formula: (x, y) -> (y, -x)
        self.x_prime = self.y
        self.y_prime = -self.x

        self.answer = self.y_prime

        self.description = (
            f"What is the new y-coordinate of point A′?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Transformations"
        self.source = "Common transformation coordinate rule found in GCSE/IGCSE revision guides"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original point }} A \\text{{ has coordinates:}} &\\quad (x, y) = ({self.x}, {self.y})\\\\"
            f"\\text{{A }} 90^{{\\circ}} \\text{{ clockwise rotation about the origin follows the rule:}} &\\quad (x, y) \\to (y, -x)\\\\"
            f"\\text{{Thus, the new coordinates }} (x', y') \\text{{ are:}} &\\\\"
            f"x' &= y = {self.y}\\\\"
            f"y' &= -x\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Set plot limits with some padding
        limit = max(abs(self.x), abs(self.y), abs(self.x_prime), abs(self.y_prime)) + 2
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        
        # Draw Cartesian axes centered at (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.grid(True, linestyle=':', alpha=0.6)
        
        # Ensure 1 unit on x equals 1 unit on y (crucial for rotation to look correct)
        ax.set_aspect('equal')

        # Plot the Points and Lines
        # Original Point A
        ax.plot([0, self.x], [0, self.y], linestyle='--', color='blue', alpha=0.5)
        ax.scatter(self.x, self.y, color='blue', s=100, label='Start')
        ax.text(self.x + 0.5, self.y + 0.5, f"A({self.x}, {self.y})", color='blue', fontsize=12, fontweight='bold')

        # Rotated Point A'
        ax.plot([0, self.x_prime], [0, self.y_prime], linestyle='--', color='red', alpha=0.5)
        ax.scatter(self.x_prime, self.y_prime, color='red', s=100, label='End')
        ax.text(self.x_prime + 0.5, self.y_prime - 1, f"A'(?, ?)", color='red', fontsize=12, fontweight='bold')

        # Draw the Rotation Arc/Arrow
        # Calculate angles in degrees
        angle_start = np.degrees(np.arctan2(self.y, self.x))
        angle_end = np.degrees(np.arctan2(self.y_prime, self.x_prime))
        
        # Create an arrow depicting the rotation
        # We use FancyArrowPatch to create a curved arrow
        radius = min(np.sqrt(self.x**2 + self.y**2) / 2, 3) # Place arrow halfway or at radius 3
        
        arrow = patches.FancyArrowPatch(
            (radius * np.cos(np.radians(angle_start)), radius * np.sin(np.radians(angle_start))),
            (radius * np.cos(np.radians(angle_end)), radius * np.sin(np.radians(angle_end))),
            connectionstyle=f"arc3,rad=-0.3", # Negative rad for clockwise curvature
            arrowstyle="Simple, tail_width=0.5, head_width=4, head_length=8",
            color="green"
        )
        ax.add_patch(arrow)
        
        # Label the rotation
        mid_angle = (angle_start + angle_end) / 2
        if abs(angle_start - angle_end) > 180: # Handle crossing the -180/180 line if necessary
            mid_angle += 180
                
        ax.text((1.2 * radius) * np.cos(np.radians(mid_angle)), (1.2 * radius) * np.sin(np.radians(mid_angle)), "90°", color='green', fontsize=10, ha='center')
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat092:
    
    def __init__(self):
        # Generate a random triangle (3 vertices)
        # Keeping coordinates between -5 and 5 for better visibility on a standard grid
        v1 = [rnd.randint(-4, 4), rnd.randint(-4, 4)]
        v2 = [rnd.randint(-4, 4), rnd.randint(-4, 4)]
        v3 = [rnd.randint(-4, 4), rnd.randint(-4, 4)]
        
        self.triangle_orig = np.array([v1, v2, v3])

        # Generate a random translation vector
        # Ensure it's not (0,0)
        tx, ty = 0, 0
        while tx == 0 and ty == 0:
            tx = rnd.randint(-6, 6)  # spacing it out a bit
            ty = rnd.randint(-3, 3)
        translation_vector = np.array([tx, ty])

        # Calculate new triangle vertices
        self.triangle_new = self.triangle_orig + translation_vector

        # Select one random vertex to be the focus of the question
        target_index = rnd.randint(0, 2)
        self.target_vertex_orig = self.triangle_orig[target_index]
        self.target_vertex_new = self.triangle_new[target_index]
        
        # Calculate the answer (Sum of x and y of the new vertex)
        self.answer = int(self.target_vertex_new[0] + self.target_vertex_new[1])

        self.description = (
            f"One of the vertices of the original triangle is highlighted. After it got translate it, what is the sum of the x and y coordinates of the new vertex?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Transformations"
        self.source = "Modeled after standard vector translation questions in IGCSE Mathematics (0580) Papers"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original Vertex Coordinates: }} P &= ({round(self.target_vertex_orig[0], 10)}, {round(self.target_vertex_orig[1], 10)})\\\\"
            f"\\text{{Translation Vector: }} \\vec{{v}} &= \\begin{{pmatrix}} {round(translation_vector[0], 10)} \\\\ {round(translation_vector[1], 10)} \\end{{pmatrix}}\\\\"
            f"\\text{{New Vertex Coordinates }} P' &= P + \\vec{{v}}\\\\"
            f"&= \\begin{{pmatrix}} {round(self.target_vertex_orig[0], 10)} \\\\ {round(self.target_vertex_orig[1], 10)} \\end{{pmatrix}} + \\begin{{pmatrix}} {round(translation_vector[0], 10)} \\\\ {round(translation_vector[1], 10)} \\end{{pmatrix}}\\\\"
            f"&= \\begin{{pmatrix}} {round(self.target_vertex_orig[0], 10)} + ({round(translation_vector[0], 10)}) \\\\ {round(self.target_vertex_orig[1], 10)} + ({round(translation_vector[1], 10)}) \\end{{pmatrix}}\\\\"
            f"&= \\begin{{pmatrix}} {round(self.target_vertex_new[0], 10)} \\\\ {round(self.target_vertex_new[1], 10)} \\end{{pmatrix}}\\\\"
            f"\\text{{Sum of coordinates}} &= x' + y'\\\\"
            f"&= {round(self.target_vertex_new[0], 10)} + ({round(self.target_vertex_new[1], 10)})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Figure
        fig, ax = plt.subplots(figsize=(6, 6))

        # Grid and Axis setup
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        ax.axhline(y=0, color='k', linewidth=1)
        ax.axvline(x=0, color='k', linewidth=1)

        # Plot Original Triangle (Blue)
        poly_orig = Polygon(self.triangle_orig, facecolor='skyblue', edgecolor='blue', alpha=0.5, label='Original')
        ax.add_patch(poly_orig)

        # Plot Translated Triangle (Red/Orange, Dashed)
        poly_new = Polygon(self.triangle_new, facecolor='none', edgecolor='red', linestyle='--', linewidth=2, label='Translated')
        ax.add_patch(poly_new)

        # Visualizing the Translation Vector (Arrow)
        # We draw an arrow from the target vertex to its new position
        ax.annotate("", 
                    xy=(self.target_vertex_new[0], self.target_vertex_new[1]), 
                    xytext=(self.target_vertex_orig[0], self.target_vertex_orig[1]),
                    arrowprops=dict(arrowstyle="->", color="green", lw=2))

        # Label the vector
        mid_x = (self.target_vertex_orig[0] + self.target_vertex_new[0]) / 2
        mid_y = (self.target_vertex_orig[1] + self.target_vertex_new[1]) / 2
        ax.text(mid_x, mid_y, f"v", color="green", fontsize=12, fontweight='bold', ha='right')

        # Highlight the specific vertex mentioned in the question
        ax.plot(self.target_vertex_orig[0], self.target_vertex_orig[1], 'bo') # Blue dot
        ax.text(self.target_vertex_orig[0] + 0.2, self.target_vertex_orig[1] + 0.2, 
                f"({self.target_vertex_orig[0]}, {self.target_vertex_orig[1]})", fontsize=10, color='blue')

        # Set Limits (dynamic based on points)
        all_x = np.concatenate((self.triangle_orig[:,0], self.triangle_new[:,0]))
        all_y = np.concatenate((self.triangle_orig[:,1], self.triangle_new[:,1]))
        buffer = 2
        ax.set_xlim(min(all_x)-buffer, max(all_x)+buffer)
        ax.set_ylim(min(all_y)-buffer, max(all_y)+buffer)
        ax.set_aspect('equal')
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat093:
    
    def __init__(self):
        # Random half-length of the side (e.g., between 2 and 6)
        self.s = rnd.randint(2, 6) 
        
        # Define the original vertices (A, B, C, D)
        # A=(s,s), B=(s,-s), C=(-s,-s), D=(-s,s)
        self.vertices = {
            'A': (self.s, self.s),
            'B': (self.s, -self.s),
            'C': (-self.s, -self.s),
            'D': (-self.s, self.s)
        }

        self.answer = 2

        self.description = (
            f"How many vertices remain in the exact same position (invariant) after the reflection?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Transformations"
        self.source = "Adapted from \"Symmetry and Transformations\" conceptual questions in Cambridge IGCSE / O Level Mathematics"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The vertices of the square are defined as:}} \\\\"
            f"A &= ({self.s}, {self.s}) \\\\"
            f"B &= ({self.s}, {-self.s}) \\\\"
            f"C &= ({-self.s}, {-self.s}) \\\\"
            f"D &= ({-self.s}, {self.s}) \\\\"
            f"\\text{{For a reflection across the main diagonal }} y = x, \\text{{ the transformation is }} (x, y) \\to (y, x). \\\\"
            f"\\text{{Applying the reflection to each vertex:}} \\\\"
            f"A' &= ({self.s}, {self.s}) = A \\quad (\\text{{Invariant}}) \\\\"
            f"B' &= ({-self.s}, {self.s}) = D \\neq B \\\\"
            f"C' &= ({-self.s}, {-self.s}) = C \\quad (\\text{{Invariant}}) \\\\"
            f"D' &= ({self.s}, {-self.s}) = B \\neq D \\\\"
            f"\\text{{Counting the invariant vertices (A and C):}} \\\\"
            f"\\text{{Total}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the Plot
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Set plot limits with some padding
        limit = self.s + 2
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        
        # Draw axes
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(True, linestyle=':', alpha=0.6)
        
        # Plot the Reflection Line (y = x)
        # Generate points for the line
        line_range = np.linspace(-limit, limit, 100)
        ax.plot(line_range, line_range, color='green', linestyle='--', linewidth=2, label='Reflection Line (y=x)')
        
        # Plot the Square
        # Extract coordinates for plotting shapes (append first point at end to close the square)
        pts = [self.vertices['A'], self.vertices['B'], self.vertices['C'], self.vertices['D'], self.vertices['A']]
        xs, ys = zip(*pts)
        
        # Fill the square
        ax.fill(xs, ys, color='skyblue', alpha=0.3, label='Original Square')
        # Draw edges
        ax.plot(xs, ys, color='blue', linewidth=2)
        
        # Calculate and Plot Vertices (and Reflections)
        invariant_count = 0
        
        for label, (x, y) in self.vertices.items():
            # Reflection across y=x simply swaps coordinates: (x, y) -> (y, x)
            x_new, y_new = y, x
        
            # Plot non-invariant points in Blue
            ax.scatter(x, y, color='blue', s=80, zorder=5)
            ax.text(x + 0.1, y + 0.1, f"{label}({x},{y})", fontsize=10, color='blue')
            
            # Optional: Show where they reflect to with an arrow
            ax.annotate("", xy=(x_new, y_new), xytext=(x, y),
                        arrowprops=dict(arrowstyle="->", color='gray', linestyle='dashed'))

        # Final Formatting
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend(loc='upper left')
        ax.set_aspect('equal') # Essential for geometry figures
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat094:
    
    def __init__(self):
        # Base vectors (keep u horizontal and v vertical as per description)
        self.u_mag = rnd.randint(1, 3)  # Magnitude of u (e.g., 1, 2, or 3)
        self.v_mag = rnd.randint(1, 3)  # Magnitude of v
        
        # Scalars (coefficients)
        self.a = rnd.randint(2, 4)      # Scalar for u
        self.b = rnd.randint(2, 4)      # Scalar for v
        
        # Define vectors
        self.u_vec = np.array([self.u_mag, 0])
        self.v_vec = np.array([0, self.v_mag])
        
        # Scaled vectors
        self.scaled_u = self.a * self.u_vec
        self.scaled_v = self.b * self.v_vec
        
        # Resultant vector
        self.r_vec = self.scaled_u + self.scaled_v
        
        # Calculate Answer
        # The question asks for the x-component of r
        self.answer= int(self.r_vec[0])

        self.description = (
            f"What is the value of the x-component of the resultant vector $\\mathbf{{r}}$?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vectors in two dimensions"
        self.source = "OpenStax Precalculus"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given vectors:}} &\\\\"
            f"\\mathbf{{u}} &= \\binom{{{self.u_mag}}}{{0}}, \\quad \\mathbf{{v}} = \\binom{{0}}{{{self.v_mag}}}\\\\"
            f"\\text{{Calculate the resultant vector }} \\mathbf{{r}}: &\\\\"
            f"\\mathbf{{r}} &= {self.a}\\mathbf{{u}} + {self.b}\\mathbf{{v}}\\\\"
            f"&= {self.a}\\binom{{{self.u_mag}}}{{0}} + {self.b}\\binom{{0}}{{{self.v_mag}}}\\\\"
            f"&= \\binom{{{self.a} \\cdot {self.u_mag}}}{{0}} + \\binom{{0}}{{{self.b} \\cdot {self.v_mag}}}\\\\"
            f"&= \\binom{{{self.a * self.u_mag}}}{{0}} + \\binom{{0}}{{{self.b * self.v_mag}}}\\\\"
            f"&= \\binom{{{self.a * self.u_mag} + 0}}{{0 + {self.b * self.v_mag}}}\\\\"
            f"&= \\binom{{{self.answer}}}{{{self.b * self.v_mag}}}\\\\"
            f"\\text{{The x-component is:}} &\\\\"
            f"r_x &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Determine plot limits with some padding
        max_val = max(self.r_vec[0], self.r_vec[1]) + 2
        ax.set_xlim(-1, max_val)
        ax.set_ylim(-1, max_val)
        
        # Add grid (at integer intervals for easy reading)
        ax.grid(True, which='both', linestyle='--', alpha=0.6)
        ax.set_xticks(np.arange(0, max_val, 1))
        ax.set_yticks(np.arange(0, max_val, 1))
        ax.set_aspect('equal')
        
        # Plot Vectors (Tip-to-Tail Method)
        # Helper to plot quiver arrows
        def plot_arrow(start, direction, color, label):
            ax.quiver(start[0], start[1], direction[0], direction[1], 
                    angles='xy', scale_units='xy', scale=1, color=color, label=label, width=0.015, headwidth=4)

        # Vector 1: Scaled u (Horizontal) starting from origin
        plot_arrow([0, 0], self.scaled_u, 'blue', label=f'${self.a}\\mathbf{{u}}$')
        
        # Vector 2: Scaled v (Vertical) starting from tip of u
        plot_arrow(self.scaled_u, self.scaled_v, 'green', label=f'${self.b}\\mathbf{{v}}$')
        
        # Vector 3: Resultant r (Origin to tip of v)
        plot_arrow([0, 0], self.r_vec, 'red', label=r'$\mathbf{r}$')

        # Annotations & Aesthetics
        # Label the base vector definitions in the title or text
        question_text = (
            f"Find x-component of $\\mathbf{{r}} = {self.a}\\mathbf{{u}} + {self.b}\\mathbf{{v}}$"
        )
        
        ax.set_title(question_text, fontsize=14, pad=15)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        
        # Show legend
        ax.legend()
        
        # Dashed lines to show components on axes (optional visual aid)
        ax.plot([self.r_vec[0], self.r_vec[0]], [0, self.r_vec[1]], 'k:', alpha=0.3) # Drop to x-axis
        ax.plot([0, self.r_vec[0]], [self.r_vec[1], self.r_vec[1]], 'k:', alpha=0.3) # Drop to y-axis

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat095:
    
    def __init__(self):
        # Define Vector p (keep components small for readability)
        self.px = rnd.randint(1, 3)
        self.py = rnd.randint(1, 4)
        
        # Define Scalar Multiplier (m)
        # This determines how much larger q is compared to p
        self.scalar = rnd.randint(2, 4) 
        
        # Define Vector q based on scalar
        self.qx = self.px * self.scalar
        self.real_k = self.py * self.scalar  # This is the hidden value 'k'

        self.answer = self.real_k

        self.description = (
            f"Vector $\\mathbf{{p}} = \\binom{{{self.px}}}{{{self.py}}}$ and Vector $\\mathbf{{q}} = \\binom{{{self.qx}}}{{k}}$. If vectors $\\mathbf{{p}}$ and $\\mathbf{{q}}$ are parallel, what is the value of $k$?"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vectors in two dimensions"
        self.source = "Haese Mathematics: Mathematics for the International Student"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Since vectors }} \\mathbf{{p}} \\text{{ and }} \\mathbf{{q}} \\text{{ are parallel, their components must be proportional:}} &\\\\"
            f"\\frac{{p_x}}{{q_x}} &= \\frac{{p_y}}{{q_y}}\\\\"
            f"\\frac{{{self.px}}}{{{self.qx}}} &= \\frac{{{self.py}}}{{k}}\\\\"
            f"\\text{{Cross-multiplying to solve for }} k: &\\\\"
            f"{self.px} \\cdot k &= {self.py} \\cdot {self.qx}\\\\"
            f"{self.px}k &= {self.py * self.qx}\\\\"
            f"k &= \\frac{{{self.py * self.qx}}}{{{self.px}}}\\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Generate Figure
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Coordinates:
        # Vector p starts at origin (0,0)
        start_p = np.array([0, 0])
        vec_p = np.array([self.px, self.py])
        
        # Vector q starts offset so they look parallel but don't overlap
        # Offset x by 1 and y by -2 (visual preference)
        start_q = np.array([1, -1]) 
        vec_q = np.array([self.qx, self.real_k])
        
        # Plot Vectors using quiver
        # angles='xy', scale_units='xy', scale=1 ensures accurate grid representation
        ax.quiver(start_p[0], start_p[1], vec_p[0], vec_p[1], 
                angles='xy', scale_units='xy', scale=1, color='blue', label=r'$\mathbf{p}$')
        
        ax.quiver(start_q[0], start_q[1], vec_q[0], vec_q[1], 
                angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathbf{q}$')
        
        # Add labels near the vectors
        ax.text(start_p[0] + vec_p[0]/2, start_p[1] + vec_p[1]/2 + 0.5, 
                r'$\mathbf{p}$', color='blue', fontsize=14, fontweight='bold')
        ax.text(start_q[0] + vec_q[0]/2, start_q[1] + vec_q[1]/2 + 0.5, 
                r'$\mathbf{q}$', color='red', fontsize=14, fontweight='bold')
        
        # Configure Grid and Aspect Ratio
        # Calculate limits dynamically to ensure vectors fit
        max_coord = max(self.qx + start_q[0], self.real_k + start_q[1]) + 2
        
        ax.set_xlim(-1, max_coord)
        ax.set_ylim(-2, max_coord)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_aspect('equal')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat096:
    
    def __init__(self):
        # We choose integers between 3 and 8 to keep the graph readable
        self.x = rnd.choice([-1, 1]) * rnd.randint(3, 8) 
        self.y = rnd.choice([-1, 1]) * rnd.randint(3, 8)
        
        # Calculate the answer (Magnitude)
        self.magnitude = np.sqrt(self.x**2 + self.y**2)

        self.answer = round(self.magnitude, 2)

        self.description = (
            f"Calculate the magnitude (length) of the vector. Give your answer correct to 2 decimal places."
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Magnitude of a vector"
        self.source = "Cambridge IGCSE® Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given vector components:}}&\\\\"
            f"x &= {self.x}\\\\"
            f"y &= {self.y}\\\\"
            f"\\text{{The magnitude is calculated as:}}&\\\\"
            f"|\\mathbf{{v}}| &= \\sqrt{{x^2 + y^2}}\\\\"
            f"&= \\sqrt{{({self.x})^2 + ({self.y})^2}}\\\\"
            f"&= \\sqrt{{{self.x**2} + {self.y**2}}}\\\\"
            f"&= \\sqrt{{{self.x**2 + self.y**2}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Set plot limits with some padding
        limit = max(abs(self.x), abs(self.y)) + 1
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        
        # Add Grid and Axes at center
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_aspect('equal')
        
        # Move left and bottom spines to x = 0 and y = 0
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # Add arrows to the axes ends (optional aesthetic)
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

        # Draw the Vector and Components
        # Draw the main Vector 'a' (Red arrow)
        ax.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color='red', label=r'$\mathbf{a}$')
        
        # Draw the components (Dashed Blue Lines forming the triangle)
        # Horizontal component line
        ax.plot([0, self.x], [0, 0], 'b--', alpha=0.5, linewidth=1.5)
        # Vertical component line
        ax.plot([self.x, self.x], [0, self.y], 'b--', alpha=0.5, linewidth=1.5)

        # Annotations
        # Label the vector
        ax.text(self.x/2, self.y/2 + 0.5, r'$\mathbf{a}$', color='red', fontsize=14, fontweight='bold')
        
        # Label the coordinates
        ax.text(self.x, self.y, f' ({self.x}, {self.y})', fontsize=10, verticalalignment='bottom')
        
        # Label the components lengths
        ax.text(self.x/2, -0.5 if self.y > 0 else 0.5, f'{self.x}', color='blue', ha='center')
        ax.text(self.x + (0.2 if self.x > 0 else -0.8), self.y/2, f'{self.y}', color='blue', va='center')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat097:
    
    def __init__(self):
        # Start with a random "middle" point B (using integers for cleaner math)
        # Range -10 to 10
        self.B = np.random.randint(-10, 11, size=3)

        # Create a random Direction Vector (dx, dy, dz)
        # We avoid (0,0,0) to ensure a line exists
        direction = np.random.randint(-5, 6, size=3)
        while np.all(direction == 0):
            direction = np.random.randint(-5, 6, size=3)

        # Generate scalars (multipliers) for A and C
        # We make sure they aren't 0 (same as B) and are distinct
        t_a = np.random.randint(-3, 4)
        while t_a == 0: t_a = np.random.randint(-3, 4)

        t_c = np.random.randint(-3, 4)
        while t_c == 0 or t_c == t_a: t_c = np.random.randint(-3, 4)

        # Calculate points A and C based on the direction vector
        # A = B + t_a * direction
        # C = B + t_c * direction
        self.A = self.B + t_a * direction
        self.C = self.B + t_c * direction

        # The "Secret" Answer
        k_answer = self.A[0]

        vec_bc = self.C - self.B
        dy_ba = self.A[1] - self.B[1]
        dz_ba = self.A[2] - self.B[2]

        # Determine which component to use for ratio (prefer y, fallback to z to avoid zero division)
        if vec_bc[1] != 0:
            comp_name = "y"
            numerator = dy_ba
            denominator = vec_bc[1]
        else:
            comp_name = "z"
            numerator = dz_ba
            denominator = vec_bc[2]

        m = numerator / denominator
        x_term = m * vec_bc[0]

        self.answer = int(k_answer)

        self.description = (
            f"Using vectors, find the value of the scalar $k$ such that the points $A$, $B$, and $C$ are collinear."
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vector geometry"
        self.source = "Allen - Vector Geometry Questions"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{First, determine the vector }} \\vec{{BC}}: &\\\\"
            f"\\vec{{BC}} &= C - B\\\\"
            f"&= ({self.C[0]} - {self.B[0]}, {self.C[1]} - {self.B[1]}, {self.C[2]} - {self.B[2]})\\\\"
            f"&= ({vec_bc[0]}, {vec_bc[1]}, {vec_bc[2]})\\\\"
            f"\\text{{Next, express the vector }} \\vec{{BA}} \\text{{ in terms of }} k: &\\\\"
            f"\\vec{{BA}} &= A - B\\\\"
            f"&= (k - {self.B[0]}, {self.A[1]} - {self.B[1]}, {self.A[2]} - {self.B[2]})\\\\"
            f"&= (k - {self.B[0]}, {dy_ba}, {dz_ba})\\\\"
            f"\\text{{Since the points are collinear, }} \\vec{{BA}} = m \\cdot \\vec{{BC}}. &\\\\"
            f"\\text{{Find the scalar }} m \\text{{ using the {comp_name}-components:}} &\\\\"
            f"{numerator} &= m({denominator})\\\\"
            f"m &= \\frac{{{numerator}}}{{{denominator}}}"
            f" = {round(m, 10)}\\\\"
            f"\\text{{Now, substitute }} m \\text{{ into the x-component equation to find }} k: &\\\\"
            f"k - {self.B[0]} &= m({vec_bc[0]})\\\\"
            f"k - {self.B[0]} &= {round(m, 10)} \\cdot {vec_bc[0]}\\\\"
            f"k &= {self.B[0]} + {round(x_term, 10)}\\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Plot the line connecting the furthest points to show the path
        # We stack the points to easily plot the line
        points_matrix = np.vstack((self.A, self.B, self.C))
        # Sort points by X-coordinate simply to draw a neat line from end-to-end
        points_sorted = points_matrix[points_matrix[:,0].argsort()]
        ax.plot(points_sorted[:,0], points_sorted[:,1], points_sorted[:,2],
                color='gray', linestyle='--', alpha=0.5, label='Line of Collinearity')

        # Plot the specific points
        ax.scatter(*self.A, color='red', s=100, label='Point A (Target)')
        ax.scatter(*self.B, color='blue', s=100, label='Point B')
        ax.scatter(*self.C, color='green', s=100, label='Point C')

        # Add Text Labels (The Question)
        # Note: We display 'k' for A's x-coordinate
        ax.text(self.A[0], self.A[1], self.A[2], f'  A(k, {self.A[1]}, {self.A[2]})', color='red', fontsize=11, fontweight='bold')
        ax.text(self.B[0], self.B[1], self.B[2], f'  B({self.B[0]}, {self.B[1]}, {self.B[2]})', color='blue', fontsize=10)
        ax.text(self.C[0], self.C[1], self.C[2], f'  C({self.C[0]}, {self.C[1]}, {self.C[2]})', color='green', fontsize=10)

        # Remove all axis elements
        ax.set_axis_off()

        # Force equal aspect ratio so the vectors don't look distorted
        try:
            ax.set_box_aspect([1,1,1])
        except:
            pass # Older matplotlib versions might not support this

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat098:
    
    def __init__(self):
        # Coefficients for OA = c1*a and OB = c2*b
        self.c1 = rnd.randint(2, 6)
        self.c2 = rnd.randint(2, 6)
        
        # Ratio AP:PB = m:n
        self.m = rnd.randint(1, 4)
        self.n = rnd.randint(1, 4)
        
        # Calculate terms for the Question Text to ensure math works
        # Section Formula: OP = (n*OA + m*OB) / (m+n)
        # OP = (n*(c1*a) + m*(c2*b)) / (m+n)
        # OP = (1/(m+n)) * ( (n*c1)a + (m*c2)b )
        
        term_a = self.n * self.c1
        term_b = self.m * self.c2
        k_solution = 1 / (self.m + self.n)

        self.answer = round(k_solution, 3)

        self.description = (
            f"Trapezium OABC where OA is parallel to CB. "
            f"OA = {self.c1}a and OB = {self.c2}b. "
            f"Point P is on AB such that AP:PB = {self.m}:{self.n}. "
            f"If vector OP = k({term_a}a + {term_b}b), find k. "
            "Give your answer correct to 3 decimal places."
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vector geometry"
        self.source = "Maths Genie - Vectors Proof Questions"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Using the Section Formula for vector }} \\vec{{OP}} \\text{{ with ratio }} {self.m}:{self.n}:&\\\\"
            f"\\vec{{OP}} &= \\frac{{{self.n}\\vec{{OA}} + {self.m}\\vec{{OB}}}}{{{self.m} + {self.n}}}\\\\"
            f"\\text{{Substitute }} \\vec{{OA}} = {self.c1}\\mathbf{{a}} \\text{{ and }} \\vec{{OB}} = {self.c2}\\mathbf{{b}}:&\\\\"
            f"\\vec{{OP}} &= \\frac{{{self.n}({self.c1}\\mathbf{{a}}) + {self.m}({self.c2}\\mathbf{{b}})}}{{{self.m + self.n}}}\\\\"
            f"&= \\frac{{{self.n * self.c1}\\mathbf{{a}} + {self.m * self.c2}\\mathbf{{b}}}}{{{self.m + self.n}}}\\\\"
            f"&= \\frac{{1}}{{{self.m + self.n}}} ({term_a}\\mathbf{{a}} + {term_b}\\mathbf{{b}})\\\\"
            f"\\text{{Comparing with the given }} \\vec{{OP}} = k({term_a}\\mathbf{{a}} + {term_b}\\mathbf{{b}}):&\\\\"
            f"k &= \\frac{{1}}{{{self.m + self.n}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Define basis vectors (arbitrary visual choices)
        # a points right (1, 0), b points up-right (angle 60 degrees)
        vec_a = np.array([1, 0])
        vec_b = np.array([0.5, 0.866]) 
        
        # Define Points O, A, B
        O = np.array([0, 0])
        A = self.c1 * vec_a
        B = self.c2 * vec_b
        
        # Define P using the vector ratio logic
        # P divides AB in ratio m:n
        P = (self.n * A + self.m * B) / (self.m + self.n)
        
        # Define C to make it a Trapezium (OA || CB)
        # CB is parallel to OA, so C is shifted from B by some amount of 'a'
        # We pick a random length for CB to make the shape look nice
        scale_cb = rnd.uniform(0.3, 0.8) * self.c1
        C = B - (scale_cb * vec_a)

        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Function to draw line segments
        def draw_line(p1, p2, style='-', label=None):
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], style, linewidth=1.5, label=label)

        # Draw Trapezium OABC
        draw_line(O, A, 'k') # OA
        draw_line(A, B, 'k') # AB
        draw_line(B, C, 'k') # BC
        draw_line(C, O, 'k') # CO
        
        # Draw Vector OP
        draw_line(O, P, 'b--') # OP dashed
        
        # Plot Points
        points = {'O': O, 'A': A, 'B': B, 'C': C, 'P': P}
        for label, coord in points.items():
            ax.plot(coord[0], coord[1], 'ko', markersize=5)
            # Offset label slightly
            xytext = (5, 5)
            if label == 'P': xytext = (5, 0)
            if label == 'O': xytext = (-15, -10)
            ax.annotate(r'$' + label + '$', (coord[0], coord[1]), 
                        xytext=xytext, textcoords='offset points', fontsize=14)

        # Label vectors OA and OB
        ax.annotate(rf'$2\mathbf{{a}}$' if self.c1==2 else rf'${self.c1}\mathbf{{a}}$', 
                    (A[0]/2 + 0.3, A[1]/2 + 0.1), color='green', fontsize=12)
        ax.annotate(rf'$3\mathbf{{b}}$' if self.c2==3 else rf'${self.c2}\mathbf{{b}}$', 
                    (B[0]/2 - 0.2, B[1]/2 + 0.2), color='green', fontsize=12)
        
        # Annotate Ratio on line AB
        # Midpoints of AP and PB for labels
        mid_AP = (A + P) / 2
        mid_PB = (P + B) / 2
        ax.annotate(f'{self.m}', mid_AP + 0.1, color='red', fontsize=10, ha='center')
        ax.annotate(f'{self.n}', mid_PB + 0.1, color='red', fontsize=10, ha='center')

        # Set graphical limits and remove axes for "Geometry Figure" look
        ax.set_aspect('equal')
        ax.axis('off')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat099:
    
    def __init__(self):
        # We pick the answer first to ensure the graph looks nice, 
        # but we hide 'k' in the final output.
        self.val_x = rnd.randint(3, 8)       # The known i component
        self.val_k = rnd.randint(3, 10)      # The unknown j component (the answer)

        # Calculate Magnitude symbolically to get the exact sqrt string (e.g., 3sqrt(17))
        self.magnitude_sym = sympy.sqrt(self.val_x**2 + self.val_k**2)
        self.magnitude_latex = sympy.latex(self.magnitude_sym)

        self.answer = self.val_k

        self.description = (
            f"Find positive $k$ given $\\vec{{v}} = {self.val_x}\\mathbf{{i}} + k\\mathbf{{j}}$ "
            f"and $|\\vec{{v}}| = {self.magnitude_latex}$"
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vector geometry"
        self.source = "Maths Genie - A Level Vectors Questions"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"|\\vec{{v}}| &= \\sqrt{{x^2 + k^2}}\\\\"
            f"{self.magnitude_latex} &= \\sqrt{{({self.val_x})^2 + k^2}}\\\\"
            f"\\text{{Squaring both sides:}} &\\\\"
            f"({self.magnitude_latex})^2 &= ({self.val_x})^2 + k^2\\\\"
            f"{self.val_x**2 + self.val_k**2} &= {self.val_x**2} + k^2\\\\"
            f"k^2 &= {self.val_x**2 + self.val_k**2} - {self.val_x**2}\\\\"
            f"k^2 &= {self.val_k**2}\\\\"
            f"k &= \\sqrt{{{self.val_k**2}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup Plot
        fig, ax = plt.subplots(figsize=(8, 8))

        # Coordinates for the triangle
        origin = np.array([0, 0])
        point_x = np.array([self.val_x, 0])
        point_v = np.array([self.val_x, self.val_k])

        # Draw the Triangle Components
        # X-component (Horizontal)
        ax.annotate('', xy=point_x, xytext=origin,
                    arrowprops=dict(facecolor='blue', shrink=0, width=2, headwidth=8))
        
        # Y-component (Vertical - represented as k)
        # Drawn from the tip of the x-component to the tip of the vector
        ax.annotate('', xy=point_v, xytext=point_x,
                    arrowprops=dict(facecolor='red', shrink=0, width=2, headwidth=8))
        
        # Vector v (Hypotenuse)
        ax.annotate('', xy=point_v, xytext=origin,
                    arrowprops=dict(facecolor='green', shrink=0, width=3, headwidth=10))

        # Labeling
        # Label x-component
        ax.text(self.val_x / 2, -self.val_k * 0.05, f"${self.val_x}$", 
                fontsize=14, color='blue', ha='center', va='top')

        # Label y-component (The Unknown 'k')
        ax.text(self.val_x + 0.3, self.val_k / 2, "$k$", 
                fontsize=14, color='red', ha='left', va='center')

        # Label Hypotenuse (The Magnitude)
        # Calculate rotation for text so it aligns with the hypotenuse
        angle = np.degrees(np.arctan2(self.val_k, self.val_x))
        ax.text(self.val_x/2 - 0.2, self.val_k/2 + 0.5, f"$|\\vec{{v}}| = {self.magnitude_latex}$", 
                fontsize=14, color='green', ha='right', va='bottom', rotation=angle)

        # Right Angle Marker
        rect_size = min(self.val_x, self.val_k) * 0.1
        rect = plt.Rectangle((self.val_x - rect_size, 0), rect_size, rect_size, 
                            fill=False, edgecolor='black', linewidth=1)
        ax.add_patch(rect)

        # Styling
        ax.set_xlim(-1, self.val_x + 2)
        ax.set_ylim(-1, self.val_k + 2)
        ax.set_aspect('equal') # Important for geometry to look correct
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        
        # Draw axes lines
        ax.axhline(y=0, color='k', linewidth=1)
        ax.axvline(x=0, color='k', linewidth=1)
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat100:
    
    def __init__(self):
        # Define Origin
        self.O = np.array([0, 0])
        
        # Randomize vertices A and B to create different triangle shapes
        # A in upper-left-ish area, B in lower-right-ish area
        self.A = np.array([rnd.uniform(1, 3), rnd.uniform(4, 6)])
        self.B = np.array([rnd.uniform(4, 7), rnd.uniform(1, 3)])
        
        # Randomize the ratio AP:PB = m:n
        self.m = rnd.randint(1, 5)
        self.n = rnd.randint(1, 5)
        
        # Calculate Point P using the Section Formula
        # P = (n*A + m*B) / (m + n)
        # Note: For internal division AP:PB = m:n, the weight for A is n and B is m
        self.P = (self.n * self.A + self.m * self.B) / (self.m + self.n)

        k = 1 / (self.m + self.n)

        self.answer = round(k, 3)

        self.description = (
            f"In triangle OAB, vector OA = a and vector OB = b. "
            f"Point P is on AB such that AP:PB = {self.m}:{self.n}. "
            f"The vector OP can be expressed as k({self.n}a + {self.m}b). "
            "Find the value of k. "
            "Give your answer correct to 3 decimal places."
        )

        self.topic = "Transformations and vectors"
        self.subtopic = "Vector geometry"
        self.source = "Maths Genie - Vectors Proof Questions"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given ratio }} AP:PB &= {self.m}:{self.n}\\\\"
            f"\\text{{Using the section formula for internal division:}}&\\\\"
            f"\\vec{{OP}} &= \\frac{{{self.n}\\vec{{OA}} + {self.m}\\vec{{OB}}}}{{{self.m} + {self.n}}}\\\\"
            f"\\text{{Substitute }} \\vec{{OA}} = \\mathbf{{a}} \\text{{ and }} \\vec{{OB}} = \\mathbf{{b}}:&\\\\"
            f"\\vec{{OP}} &= \\frac{{{self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}}}}{{{self.m + self.n}}}\\\\"
            f"&= \\frac{{1}}{{{self.m + self.n}}} ({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})\\\\"
            f"\\text{{Comparing with the given expression }} \\vec{{OP}} &= k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}}):&\\\\"
            f"k &= \\frac{{1}}{{{self.m + self.n}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Plotting the Figure
        plt.figure(figsize=(6, 6))
        
        # Plot Points
        points = {'O': self.O, 'A': self.A, 'B': self.B, 'P': self.P}
        for label, coord in points.items():
            plt.scatter(coord[0], coord[1], color='black', s=50, zorder=5)
            
            # Dynamic label positioning to avoid overlap
            offset = np.array([0.1, 0.1])
            if label == 'O': offset = np.array([-0.3, -0.3])
            elif label == 'A': offset = np.array([-0.2, 0.2])
            elif label == 'B': offset = np.array([0.1, -0.3])
            elif label == 'P': offset = np.array([0.1, 0.2])
            
            plt.text(coord[0]+offset[0], coord[1]+offset[1], f'${label}$', fontsize=14)

        # Draw Line Segment AB
        plt.plot([self.A[0], self.B[0]], [self.A[1], self.B[1]], 'k-', lw=1, zorder=1)
        
        # Draw Vectors with Quiver (Arrows)
        def draw_vector(start, end, text, color='blue'):
            vec = end - start
            plt.quiver(start[0], start[1], vec[0], vec[1], 
                    angles='xy', scale_units='xy', scale=1, 
                    color=color, width=0.008, headwidth=4, zorder=2)
            # Label position at midpoint
            mid = start + vec * 0.5
            plt.text(mid[0] - 0.25, mid[1] + 0.1, text, fontsize=12, color=color, fontweight='bold')

        draw_vector(self.O, self.A, r'$\vec{a}$', 'blue')
        draw_vector(self.O, self.B, r'$\vec{b}$', 'blue')
        draw_vector(self.O, self.P, r'$\vec{OP}$', 'red')
        
        # Annotate the Ratio on the segment
        # Label positions for m and n
        mid_AP = (self.A + self.P) / 2
        mid_PB = (self.P + self.B) / 2
        plt.text(mid_AP[0], mid_AP[1] + 0.2, f'{self.m}', color='green', fontsize=12, fontweight='bold', ha='center')
        plt.text(mid_PB[0], mid_PB[1] + 0.2, f'{self.n}', color='green', fontsize=12, fontweight='bold', ha='center')

        # Figure styling
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
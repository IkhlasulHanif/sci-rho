import numpy as np
import pandas as pd
import random as rnd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.optimize import brentq
from mathematics.helper import *

# target folder : "root/dataset/mathematics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "mathematics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Mat151:
    
    def __init__(self):
        # We want integer coordinates for the graph to make the calculation clean for students.
        # Equation: ln y = ax + ln k
        # This is in the form Y = mX + c
        
        # 'a' is the gradient (slope)
        self.slope_a = rnd.choice([2, 3, 4, 5, -2, -3])
        
        # 'ln k' is the y-intercept
        self.intercept_c = rnd.randint(1, 5)
        
        # Generate a second point x2 (ensure it's not 0)
        self.x2 = rnd.randint(2, 6)
        
        # Calculate the corresponding Y value for the second point (Y = ax + c)
        self.y2_log = self.slope_a * self.x2 + self.intercept_c

        self.answer = self.slope_a

        self.description = (
            f"Variables $x$ and $y$ are related by the equation $y = k e^{{ax}}$, "
            f"where $k$ and $a$ are constants. "
            f"A straight line graph is plotted on axes labeled $x$ (horizontal) "
            f"and $\\ln y$ (vertical). The line passes through the y-intercept "
            f"at (0, {self.intercept_c}) and a second point at ({self.x2}, {self.y2_log}). "
            f"Using the linear graph described above, determine the value of the constant $a$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 2 & 3 Coursebook by Sue Pemberton"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given equation:}} &\\quad y = k e^{{ax}} \\\\"
            f"\\text{{Take natural logs:}} &\\quad \\ln y = \\ln(k e^{{ax}}) \\\\"
            f"&\\quad \\ln y = ax + \\ln k \\\\"
            f"\\text{{Compare to }} Y = mX + c: &\\quad Y = \\ln y, \\; X = x, \\; m = a, \\; c = \\ln k \\\\"
            f"\\text{{The constant }} a \\text{{ represents the gradient.}} &\\\\"
            f"\\text{{Using points }} (0, {self.intercept_c}) \\text{{ and }} ({self.x2}, {self.y2_log}): &\\\\"
            f"a &= \\frac{{Y_2 - Y_1}}{{x_2 - x_1}} \\\\"
            f"&= \\frac{{{self.y2_log} - {self.intercept_c}}}{{{self.x2} - 0}} \\\\"
            f"&= \\frac{{{round(self.y2_log - self.intercept_c, 10)}}}{{{self.x2}}} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.figure(figsize=(7, 5))
        
        # Create line data
        x_range = np.linspace(-1, self.x2 + 1, 100)
        y_range = self.slope_a * x_range + self.intercept_c
        
        # Plot line
        plt.plot(x_range, y_range, 'b-', label=r'$\ln y = ax + \ln k$')
        
        # Plot and annotate the specific points
        points_x = [0, self.x2]
        points_y = [self.intercept_c, self.y2_log]
        plt.scatter(points_x, points_y, color='red', zorder=5)
        
        # Annotate (0, c)
        plt.annotate(f'(0, {self.intercept_c})', 
                    (0, self.intercept_c), 
                    textcoords="offset points", 
                    xytext=(10,-10), 
                    ha='left')
        
        # Annotate (x2, y2)
        plt.annotate(f'({self.x2}, {self.y2_log})', 
                    (self.x2, self.y2_log), 
                    textcoords="offset points", 
                    xytext=(-10, 10), 
                    ha='right')

        # Formatting axes
        plt.title("Linear Law Graph")
        plt.xlabel(r'$x$')
        plt.ylabel(r'$\ln y$')
        plt.axhline(0, color='black', linewidth=0.8)
        plt.axvline(0, color='black', linewidth=0.8)
        plt.grid(True, linestyle='--', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat152:
    
    def __init__(self):
        # We generate integer coordinates for the log-log plot so the math is clean.
        # Let (X1, Y1) be the first point and (X2, Y2) be the second point on the lg-lg axes.
        
        self.x1 = rnd.randint(0, 3)
        self.y1 = rnd.randint(1, 5)
        
        # Ensure the second point is distinct and to the right
        delta_x = rnd.randint(1, 4) 
        
        # Allow positive or negative gradients (n can be negative), but keep coordinates reasonable
        delta_y = rnd.randint(-4, 4)
        if delta_y == 0: delta_y = 2 # Avoid horizontal lines for this specific problem type
        
        self.x2 = self.x1 + delta_x
        self.y2 = self.y1 + delta_y
        
        # Calculate the power n (gradient)
        n = (self.y2 - self.y1) / (self.x2 - self.x1)

        self.answer = round(n, 3)

        self.description = (
            f"Variables $x$ and $y$ satisfy the relationship $y = Ax^n$. "
            f"The figure shows a straight line plotted on axes labeled $\\lg x$ (horizontal) "
            f"and $\\lg y$ (vertical), where $\\lg$ denotes $\\log_{{10}}$. "
            f"The line passes through the points $({self.x1}, {self.y1})$ and $({self.x2}, {self.y2})$. "
            f"Find the value of $n$. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Pure Mathematics 3 by Sophie Goldie"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{Taking logs of both sides of } y = Ax^n:\\\\"
            "\\lg y &= \\lg(Ax^n) \\\\"
            "\\lg y &= n \\lg x + \\lg A \\\\"
            "\\text{This is a linear equation } Y &= mX + C \\text{ where } Y=\\lg y, X=\\lg x.\\\\"
            "\\text{Thus, the gradient (slope) of the line represents } n.\\\\"
            f"\\text{{Points given on the }} \\lg y \\text{{ vs }} \\lg x \\text{{ graph: }} &({self.x1}, {self.y1}) \\text{{ and }} ({self.x2}, {self.y2})\\\\"
            "n &= \\frac{\\text{change in vertical axis}}{\\text{change in horizontal axis}} \\\\"
            f"&= \\frac{{{self.y2} - {self.y1}}}{{{self.x2} - {self.x1}}} \\\\"
            f"&= \\frac{{{self.y2 - self.y1}}}{{{self.x2 - self.x1}}} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Plot the line
        ax.plot([self.x1, self.x2], [self.y1, self.y2], color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
        
        # Annotate points
        ax.text(self.x1, self.y1 + 0.2, f'({self.x1}, {self.y1})', fontsize=10, ha='center', color='black')
        ax.text(self.x2, self.y2 + 0.2, f'({self.x2}, {self.y2})', fontsize=10, ha='center', color='black')
        
        # Styling the graph
        ax.set_xlabel(r'$\lg x$', fontsize=12)
        ax.set_ylabel(r'$\lg y$', fontsize=12)
        ax.set_title('Logarithmic Transformation of Power Law', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.6)
        
        # Set limits with some padding
        ax.set_xlim(min(self.x1, self.x2) - 1, max(self.x1, self.x2) + 1)
        ax.set_ylim(min(self.y1, self.y2) - 1, max(self.y1, self.y2) + 1)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat153:
    
    def __init__(self):
        base_sym = "e" 
        
        # Generate coefficients for the exponents (e.g., length = e^(ax), width = e^(bx))
        # We ensure length coefficient is usually positive and width can be negative
        a = rnd.randint(4, 8)           # Coefficient for length (e.g., 5 means 5x)
        b = rnd.choice([-1, -2, -3, 1]) # Coefficient for width (e.g., -1 means -x)
        
        # Decide on the hidden numerical value for x
        actual_x = rnd.randint(1, 5)
        
        # Calculate the exponent for the Area
        # Area = Length * Width = e^(ax) * e^(bx) = e^((a+b)x)
        # The displayed area power 'k' is the result of (a+b) * actual_x
        total_exponent_val = (a + b) * actual_x
        
        # Formatting strings for LaTeX display
        self.len_label = f"${base_sym}^{{{a}x}}$"
        
        # Handle the width label sign specifically for cleaner formatting
        if b == -1:
            self.wid_label = f"${base_sym}^{{-x}}$"
        elif b == 1:
            self.wid_label = f"${base_sym}^{{x}}$"
        else:
            self.wid_label = f"${base_sym}^{{{b}x}}$"
            
        self.area_label = f"${base_sym}^{{{total_exponent_val}}}$"

        self.answer = actual_x

        self.description = (
            f"A rectangle is shown with Length = {self.len_label} and Width = {self.wid_label}. "
            f"The Area of this rectangle is given as {self.area_label}. "
            f"Calculate the numerical value of $x$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Khan Academy"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\text{{Length}} \\times \\text{{Width}} \\\\"
            f"{base_sym}^{{{total_exponent_val}}} &= {base_sym}^{{{a}x}} \\times {base_sym}^{{{b}x}} \\\\"
            f"&= {base_sym}^{{({a} + ({b}))x}} \\\\"
            f"\\text{{Equating the exponents:}} & \\\\"
            f"{total_exponent_val} &= ({a} + ({b}))x \\\\"
            f"{total_exponent_val} &= {a + b}x \\\\"
            f"x &= \\frac{{{total_exponent_val}}}{{{a + b}}} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Draw Rectangle
        # Note: We use fixed visual dimensions for clarity. 
        # Using actual mathematical dimensions (e.g., e^10) would make the plot unreadable.
        rect_width_visual = 6
        rect_height_visual = 3
        rect = patches.Rectangle((1, 1), rect_width_visual, rect_height_visual, 
                                linewidth=2, edgecolor='black', facecolor='#e6f2ff')
        ax.add_patch(rect)
        
        # Add Labels
        # Top (Length)
        ax.text(1 + rect_width_visual/2, 1 + rect_height_visual + 0.2, self.len_label, 
                ha='center', va='bottom', fontsize=14, color='blue')
        
        # Right (Width)
        ax.text(1 + rect_width_visual + 0.2, 1 + rect_height_visual/2, self.wid_label, 
                ha='left', va='center', fontsize=14, color='red')
        
        # Center (Area)
        ax.text(1 + rect_width_visual/2, 1 + rect_height_visual/2, f"Area = {self.area_label}", 
                ha='center', va='center', fontsize=16, fontweight='bold')

        # Plot settings
        ax.set_xlim(0, 9)
        ax.set_ylim(0, 6)
        ax.axis('off') # Hide axes for a clean geometry look

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat154:
    
    def __init__(self):
        # Equation: y = log_base(x - b)
        
        # Choose a base (e.g., 2, 3, 4, 5)
        self.base = rnd.choice([2, 3, 4, 5])
        
        # Choose the vertical asymptote 'b' (shift)
        self.b = rnd.randint(-3, 5)
        
        # Choose the target answer 'k' (y-value) to ensure x is an integer
        # We want a clean point, so we pick k first, then calculate x.
        # Range [-1, 3] ensures the point isn't too far off the chart.
        self.k_target = rnd.choice([-1, 1, 2, 3])
        
        # Calculate x based on k: k = log_base(x - b)  -> base^k = x - b -> x = b + base^k
        self.x_point = self.b + (self.base ** self.k_target)

        self.answer = self.k_target

        self.description = (
            f"The graph shows the function $y = \\log_{{{self.base}}}(x - b)$. "
            f"The graph has a vertical asymptote indicated by a dashed line at $x = {self.b}$. "
            f"The curve passes through the point $({self.x_point}, k)$. "
            f"Determine the value of $k$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Nelson Mathematics for Cambridge International A Level: Pure Mathematics 2 & 3 by L. Bostock"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given the function:}} &\\\\"
            f"y &= \\log_{{{self.base}}}(x - b)\\\\"
            f"\\text{{Substitute }} x = {self.x_point} \\text{{ and }} b = {self.b} \\text{{ to find }} k:\\\\"
            f"k &= \\log_{{{self.base}}}({self.x_point} - {self.b})\\\\"
            f"&= \\log_{{{self.base}}}({round(self.x_point - self.b, 10)})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Define domain for plotting
        # Start slightly right of asymptote (b) to avoid log(0) error
        x_start = self.b + 0.01 
        x_end = self.x_point + (self.base if self.base < 5 else 2) # extend slightly past the point of interest
        
        x_values = np.linspace(x_start, x_end, 500)
        
        # Calculate y values using change of base formula: log_n(x) = ln(x) / ln(n)
        y_values = np.log(x_values - self.b) / np.log(self.base)
        
        # Plot the curve
        ax.plot(x_values, y_values, label=f'$y = \\log_{{{self.base}}}(x - b)$', linewidth=2)
        
        # Plot the Asymptote (Dashed Line)
        ax.axvline(x=self.b, color='red', linestyle='--', label=f'Asymptote ($x={self.b}$)')
        
        # Plot the specific point (x_point, k)
        ax.plot(self.x_point, self.k_target, 'ko') # 'ko' = black circle
        ax.annotate(f'({self.x_point}, k)', 
                    (self.x_point, self.k_target), 
                    textcoords="offset points", 
                    xytext=(-10, 10), 
                    ha='right',
                    fontsize=12,
                    weight='bold')

        # Grid and Axis formatting
        ax.grid(True, which='both', linestyle='--', alpha=0.6)
        ax.axhline(0, color='black', linewidth=1) # x-axis
        ax.axvline(0, color='black', linewidth=1) # y-axis
        
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        
        # Limit y-axis to keep graph focused (don't show infinite drop near asymptote)
        y_min_plot = min(self.k_target - 2, -3)
        y_max_plot = max(self.k_target + 2, 3)
        ax.set_ylim(y_min_plot, y_max_plot)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat155:
    
    def __init__(self):
        # Equation: y = e^(kx)
        self.k = rnd.randint(1, 4)  # Random coefficient k (e.g., 2, 3, 4)
        
        # Limit: x = ln(a)
        self.a = rnd.randint(2, 6)  # Random base for the log limit (e.g., ln(3), ln(5))
        
        # Calculate the exact limit value for plotting
        self.x_limit = np.log(self.a)

        # Integral of e^(kx) is (1/k) * e^(kx)
        # Definite integral from 0 to ln(a):
        # = (1/k) * (e^(k * ln(a)) - e^(k * 0))
        # = (1/k) * (a^k - 1)
        
        numerator = (self.a**self.k) - 1
        denominator = self.k

        self.answer = round(numerator / denominator, 3)

        self.description = (
            f"The figure displays the curve $y = e^{{{self.k}x}}$. "
            f"The region $R$ is shaded and is bounded by the curve, the x-axis, "
            f"the y-axis (where $x=0$), and the vertical line $x = \\ln({self.a})$. "
            f"Calculate the exact area of the shaded region $R$. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 3"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{0}}^{{\\ln({self.a})}} e^{{{self.k}x}} \\, dx\\\\"
            f"&= \\left[ \\frac{{1}}{{{self.k}}} e^{{{self.k}x}} \\right]_{{0}}^{{\\ln({self.a})}}\\\\"
            f"&= \\frac{{1}}{{{self.k}}} \\left( e^{{{self.k} \\ln({self.a})}} - e^{{0}} \\right)\\\\"
            f"&= \\frac{{1}}{{{self.k}}} \\left( {self.a}^{{{self.k}}} - 1 \\right)\\\\"
            f"&= \\frac{{{self.a**self.k} - 1}}{{{self.k}}}\\\\"
            f"&= \\frac{{{self.a**self.k - 1}}}{{{self.k}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Create data points
        # Plot slightly beyond the limit for better visuals
        x = np.linspace(-0.2, self.x_limit + 0.5, 400)
        y = np.exp(self.k * x)
        
        plt.figure(figsize=(8, 6))
        
        # Plot the main curve
        plt.plot(x, y, label=f'$y = e^{{{self.k}x}}$', color='#1f77b4', linewidth=2)
        
        # Shade the region R
        x_fill = np.linspace(0, self.x_limit, 200)
        y_fill = np.exp(self.k * x_fill)
        plt.fill_between(x_fill, y_fill, color='orange', alpha=0.3, label='Region R')
        
        # Add boundary lines
        plt.axvline(x=0, color='black', linewidth=1.5) # y-axis
        plt.axhline(y=0, color='black', linewidth=1.5) # x-axis
        plt.axvline(x=self.x_limit, color='red', linestyle='--', linewidth=1.5, label=f'$x = \\ln({self.a})$')
        
        # Labels and Title
        plt.title(f"The Exponential Region ($y=e^{{{self.k}x}}$)", fontsize=14)
        plt.xlabel("$x$", fontsize=12)
        plt.ylabel("$y$", fontsize=12)
        plt.legend(loc="upper left")
        plt.grid(True, linestyle=':', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat156:
    
    def __init__(self):
        # Equation form: y = a * x * sin(b * x)
        self.a = rnd.randint(1, 5)      # Coefficient for x (e.g., 2x, 3x)
        self.b = rnd.randint(1, 3)      # Coefficient inside sin (e.g., sin(2x))
        
        # Randomize Upper Limit (limit) to be a "nice" fraction of Pi
        # Options: pi/6, pi/4, pi/3, pi/2
        self.denom_options = {
            6: r"\frac{\pi}{6}",
            4: r"\frac{\pi}{4}",
            3: r"\frac{\pi}{3}", 
            2: r"\frac{\pi}{2}"
        }
        self.denom = rnd.choice(list(self.denom_options.keys()))
        self.limit_val = np.pi / self.denom
        self.limit_str = self.denom_options[self.denom]

        # Calculate definite integral from 0 to limit_val    
        numerator = self.a * (np.sin(self.b * self.limit_val) - self.b * self.limit_val * np.cos(self.b * self.limit_val))
        denominator = self.b**2

        area = numerator / denominator

        self.answer = round(area, 3)

        self.description = (
            f"The figure shows the curve $y = {self.a}x \\sin({self.b}x)$ for $0 \\leq x \\leq {self.limit_str}$. "
            f"The shaded region represents the area between the curve and the x-axis from the origin to $x = {self.limit_str}$. "
            f"Find the area of the shaded region. Give your answer as a decimal rounded to three decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Calculus: Early Transcendentals by James Stewart"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{0}}^{{{self.limit_str}}} {self.a}x \\sin({self.b}x) \\, dx \\\\"
            f"&= \\left[ -\\frac{{{self.a}x}}{{{self.b}}} \\cos({self.b}x) + \\frac{{{self.a}}}{{{self.b**2}}} \\sin({self.b}x) \\right]_{{0}}^{{{self.limit_str}}} \\\\"
            f"&= \\left( -\\frac{{{self.a}}}{{{self.b}}} \\left({self.limit_str}\\right) \\cos\\left({self.b} \\cdot {self.limit_str}\\right) + \\frac{{{self.a}}}{{{self.b**2}}} \\sin\\left({self.b} \\cdot {self.limit_str}\\right) \\right) - 0 \\\\"
            f"&= {round(-self.a * self.limit_val / self.b, 10)} \\cdot {round(np.cos(self.b * self.limit_val), 10)} + {round(self.a / self.b**2, 10)} \\cdot {round(np.sin(self.b * self.limit_val), 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Define the function
        func = lambda x: self.a * x * np.sin(self.b * x)

        # Create x values for the curve (go slightly past the limit for visual context)
        x = np.linspace(0, self.limit_val * 1.2, 400)
        y = func(x)
        
        plt.figure(figsize=(8, 5))
        
        # Plot the main curve
        plt.plot(x, y, label=f'$y = {self.a}x \\sin({self.b}x)$', color='#1f77b4', linewidth=2)
        
        # Shade the region (0 to limit)
        x_fill = np.linspace(0, self.limit_val, 200)
        y_fill = func(x_fill)
        plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label='Target Area')
        
        # Add vertical line at the limit
        plt.axvline(x=self.limit_val, color='gray', linestyle='--', alpha=0.7)
        
        # Formatting the graph
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        
        # Add custom tick for the limit on x-axis
        current_xticks = list(plt.xticks()[0])
        # Filter out ticks that might overlap too closely with our custom label
        filtered_ticks = [t for t in current_xticks if abs(t - self.limit_val) > 0.1 and t >= 0]
        plt.xticks(
            filtered_ticks + [self.limit_val], 
            [f"{t:.1f}" if t != 0 else "0" for t in filtered_ticks] + [f"${self.limit_str}$"]
        )
        
        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.legend(loc='upper right')
        plt.grid(True, linestyle=':', alpha=0.6)
        
        # Display the plot
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat157:
    
    def __init__(self):
        # Form: f(x) = NUM / ((x + a)(x + b))
        # We want partial fraction decomposition to look like: C/(x+a) - C/(x+b)
        # This implies NUM = C * (b - a).
        
        while True:
            self.a = rnd.randint(1, 5)
            self.b = rnd.randint(1, 5)
            
            # Ensure distinct roots to avoid repeated roots case (different technique)
            if self.a != self.b: 
                break
                
        # Calculate difference for the numerator scaling
        self.diff = self.b - self.a
        
        # Choose a scalar C (how "tall" the fractions are). 
        # To keep numbers integer-friendly, we usually pick C=1 or C=2.
        self.C = rnd.choice([1, 2, 3])
        
        # Calculate the Numerator constant
        # Decomposition: A/(x+a) + B/(x+b)
        # A = C, B = -C  =>  f(x) = C(b-a) / ((x+a)(x+b))
        self.NUM = self.C * self.diff
        
        # Randomize Integration Bounds (x1, x2)
        # Constraint: The function has vertical asymptotes at x = -a and x = -b.
        # To ensure the area is finite and valid, the integration interval [x1, x2]
        # must NOT contain -a or -b.
        # Since a, b > 0, asymptotes are negative. We can safely pick positive bounds.
        self.x1 = rnd.randint(0, 3)
        self.x2 = self.x1 + rnd.randint(1, 4) # Ensure x2 > x1

        # Integral of C/(x+a) - C/(x+b) is C*ln|x+a| - C*ln|x+b| = C * ln|(x+a)/(x+b)|
        # Evaluated from x1 to x2
        
        term_upper = (self.x2 + self.a) / (self.x2 + self.b)
        term_lower = (self.x1 + self.a) / (self.x1 + self.b)
        
        # Value inside the log before raising to power C
        ratio = term_upper / term_lower
        
        # Since answer form is ln(k), k = (ratio)^C
        k_fraction = ratio ** self.C

        self.answer = round(abs(np.log(k_fraction)), 3)

        self.description = (
            f"The figure depicts the graph of the function "
            f"$f(x) = \\frac{{{self.NUM}}}{{(x+{self.a})(x+{self.b})}}$. "
            f"The area of interest is bounded by the curve, the x-axis, and the vertical lines $x={self.x1}$ and $x={self.x2}$. "
            f"Calculate the definite integral $\\int_{{{self.x1}}}^{{{self.x2}}} f(x) \\, dx$. "
            f"Round your answer to three decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Pure Mathematics 2 & 3 by Hugh Neill & Douglas Quadling"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The integrand is:}} &\\\\"
            f"f(x) &= \\frac{{{self.NUM}}}{{(x + {self.a})(x + {self.b})}}\\\\"
            f"\\text{{Perform Partial Fraction Decomposition:}} &\\\\"
            f"\\frac{{{self.NUM}}}{{(x + {self.a})(x + {self.b})}} &= \\frac{{A}}{{x + {self.a}}} + \\frac{{B}}{{x + {self.b}}}\\\\"
            f"\\text{{Solving for A and B (with }} \\text{{NUM}} = {self.NUM} \\text{{):}} &\\\\"
            f"A &= {self.C}, \\quad B = -{self.C}\\\\"
            f"\\text{{Thus:}} &\\\\"
            f"f(x) &= \\frac{{{self.C}}}{{x + {self.a}}} - \\frac{{{self.C}}}{{x + {self.b}}}\\\\"
            f"\\text{{Evaluate the Definite Integral:}} &\\\\"
            f"I &= \\int_{{{self.x1}}}^{{{self.x2}}} \\left( \\frac{{{self.C}}}{{x + {self.a}}} - \\frac{{{self.C}}}{{x + {self.b}}} \\right) \\, dx\\\\"
            f"&= {self.C} \\left[ \\ln|x + {self.a}| - \\ln|x + {self.b}| \\right]_{{{self.x1}}}^{{{self.x2}}}\\\\"
            f"&= {self.C} \\left[ \\ln\\left| \\frac{{x + {self.a}}}{{x + {self.b}}} \\right| \\right]_{{{self.x1}}}^{{{self.x2}}}\\\\"
            f"\\text{{Substitute limits }} x_2={self.x2} \\text{{ and }} x_1={self.x1}: &\\\\"
            f"I &= {self.C} \\left( \\ln\\left( \\frac{{{self.x2} + {self.a}}}{{{self.x2} + {self.b}}} \\right) - \\ln\\left( \\frac{{{self.x1} + {self.a}}}{{{self.x1} + {self.b}}} \\right) \\right)\\\\"
            f"&= {self.C} \\left( \\ln\\left( \\frac{{{self.x2 + self.a}}}{{{self.x2 + self.b}}} \\right) - \\ln\\left( \\frac{{{self.x1 + self.a}}}{{{self.x1 + self.b}}} \\right) \\right)\\\\"
            f"&= {self.C} \\ln\\left( \\frac{{{self.x2 + self.a}}}{{{self.x2 + self.b}}} \\cdot \\frac{{{self.x1 + self.b}}}{{{self.x1 + self.a}}} \\right)\\\\"
            f"&= {self.C} \\ln\\left( {round(((self.x2 + self.a) * (self.x1 + self.b)) / ((self.x2 + self.b) * (self.x1 + self.a)), 10)} \\right)\\\\"
            f"\\text{{Since we calculate the area (magnitude):}} &\\\\"
            f"I &= |{self.answer}| = {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # 2. Define the Function for plotting and calculation
        def f(x):
            return self.NUM / ((x + self.a) * (x + self.b))

        # 3. Create the Figure
        x_plot = np.linspace(self.x1 - 1, self.x2 + 1, 400)
        # Filter out potential asymptote points for clean plotting (though bounds are safe here)
        y_plot = f(x_plot)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_plot, y_plot, 'b-', label=f'$f(x)$', linewidth=2)
        
        # Fill the area
        x_fill = np.linspace(self.x1, self.x2, 200)
        y_fill = f(x_fill)
        ax.fill_between(x_fill, y_fill, alpha=0.3, color='orange', label='Area')

        # Formatting plot
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'Graph of $f(x) = \\frac{{{self.NUM}}}{{(x+{self.a})(x+{self.b})}}$')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)
        
        # Add vertical lines for bounds
        ax.axvline(self.x1, color='red', linestyle='--', alpha=0.5)
        ax.axvline(self.x2, color='red', linestyle='--', alpha=0.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat158:
    
    def __init__(self):
        # Model: y = (m*x) / (x^2 + c)
        # Integral is (m/2) * ln(x^2 + c)
        
        # Choose c (constant in denominator)
        self.c = rnd.randint(1, 5)
        
        # Choose upper limit (b) such that the log argument (b^2 + c)/c is clean if possible
        # We define x=0 as the lower limit (a)
        self.lower_limit = 0
        self.upper_limit = rnd.randint(2, 6)
        
        # Choose numerator coefficient (m). 
        # We ensure m is even so A = m/2 is an integer integer.
        self.m = rnd.randint(1, 6) * 2 
        
        # Function string for display
        self.func_latex = fr"\frac{{{self.m}x}}{{x^2 + {self.c}}}"
        
        # Calculate A (The coefficient outside the natural log)
        # Integral of mx/(x^2+c) -> (m/2) * ln(x^2+c)
        val_A = self.m // 2
        
        # Calculate the Log Argument
        # Definite integral from 0 to b: (m/2) * [ln(b^2+c) - ln(0^2+c)]
        # = (m/2) * ln( (b^2+c) / c )
        numerator_arg = self.upper_limit**2 + self.c
        denominator_arg = self.c
        
        self.answer = round(abs(val_A * np.log(numerator_arg / denominator_arg)), 3)

        self.description = (
            f"The figure shows the curve $y = {self.func_latex}$ in the first quadrant. A shaded region is defined between $x={self.lower_limit}$ and $x={self.upper_limit}$. "
            f"Determine the area of the shaded region. Round to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Thomas' Calculus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{{self.lower_limit}}}^{{{self.upper_limit}}} \\frac{{{self.m}x}}{{x^2 + {self.c}}} \\, dx\\\\"
            f"&= \\frac{{{self.m}}}{{2}} \\left[ \\ln(x^2 + {self.c}) \\right]_{{{self.lower_limit}}}^{{{self.upper_limit}}}\\\\"
            f"&= {val_A} \\left[ \\ln(({self.upper_limit})^2 + {self.c}) - \\ln(({self.lower_limit})^2 + {self.c}) \\right]\\\\"
            f"&= {val_A} \\left( \\ln({numerator_arg}) - \\ln({denominator_arg}) \\right)\\\\"
            f"&= {val_A} \\ln\\left( \\frac{{{numerator_arg}}}{{{denominator_arg}}} \\right)\\\\"
            f"&= {val_A} \\ln({round(numerator_arg / denominator_arg, 10)})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Define x range for the curve (go slightly beyond limits for aesthetics)
        x = np.linspace(0, self.upper_limit + 1, 400)
        y = (self.m * x) / (x**2 + self.c)
        
        # Plot the curve
        ax.plot(x, y, 'b-', linewidth=2, label=f'$y={self.func_latex}$')
        
        # Shade the region
        # Create x and y arrays specifically for the shaded area
        ix = np.linspace(self.lower_limit, self.upper_limit, 200)
        iy = (self.m * ix) / (ix**2 + self.c)
        
        # Create vertices for the polygon (shade to the x-axis)
        verts = [(self.lower_limit, 0), *zip(ix, iy), (self.upper_limit, 0)]
        poly = Polygon(verts, facecolor='skyblue', edgecolor='none', alpha=0.5)
        ax.add_patch(poly)
        
        # Add boundary lines
        ax.axvline(x=self.upper_limit, color='k', linestyle='--', alpha=0.6, label=f'$x={self.upper_limit}$')
        
        # Labels and Title
        ax.set_title(f"Region under $y = {self.func_latex}$")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_ylim(bottom=0)
        ax.set_xlim(left=0)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat159:
    
    def __init__(self):
        # a: Determine the denominator (x^2 + a^2). Using integers 2-6.
        self.a = rnd.randint(2, 6)
        self.a_sq = self.a**2

        # numerator: Make it a multiple of 'a' to keep the coefficient simple.
        # Corresponds to '12' in the original example (where a=3, so 12 is 4*a).
        self.multiplier = rnd.randint(1, 6)
        self.numerator = self.multiplier * self.a

        # x_limit: The integration limit.
        # Setting x_limit = a ensures the result involves arctan(1) = pi/4.
        self.x_limit = self.a

        # --- 2. Calculate Hidden Answer ---
        # Integral of k/(x^2 + a^2) dx is (k/a) * arctan(x/a)
        # Definite integral from 0 to a: (numerator/a) * arctan(a/a) - 0
        # = multiplier * arctan(1)
        # = multiplier * (pi/4)

        # Calculate numerical answer
        numerical_answer = self.multiplier * (np.pi / 4)

        self.answer = round(numerical_answer, 3)

        self.description = (
            f"The figure illustrates the bell-shaped curve of the "
            f"function $y = \\frac{{{self.numerator}}}{{x^2+{self.a_sq}}}$. The region extends "
            f"from the y-axis ($x=0$) to the vertical line $x={self.x_limit}$. "
            f"Calculate the area of this region. "
            f"Round your answer to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Khan Academy"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{0}}^{{{self.x_limit}}} \\frac{{{self.numerator}}}{{x^2 + {self.a_sq}}} \\, dx\\\\"
            f"&= {self.numerator} \\cdot \\left[ \\frac{{1}}{{{self.a}}} \\arctan\\left(\\frac{{x}}{{{self.a}}}\\right) \\right]_{{0}}^{{{self.x_limit}}}\\\\"
            f"&= \\frac{{{self.numerator}}}{{{self.a}}} \\left( \\arctan\\left(\\frac{{{self.x_limit}}}{{{self.a}}}\\right) - \\arctan\\left(\\frac{{0}}{{{self.a}}}\\right) \\right)\\\\"
            f"&= {self.multiplier} \\cdot (\\arctan(1) - 0)\\\\"
            f"&= {self.multiplier} \\cdot \\frac{{\\pi}}{{4}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Create data points
        # x range from slightly left of y-axis to slightly right of limit
        x = np.linspace(-1, self.x_limit + 1, 400)
        y = self.numerator / (x**2 + self.a_sq)

        plt.figure(figsize=(8, 5))

        # Plot the function curve
        plt.plot(x, y, label=f'$y = \\frac{{{self.numerator}}}{{x^2+{self.a_sq}}}$', color='blue', linewidth=2)

        # Shade the integration region
        x_fill = np.linspace(0, self.x_limit, 200)
        y_fill = self.numerator / (x_fill**2 + self.a_sq)
        plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='Target Region')

        # Draw reference lines
        plt.axvline(x=0, color='black', linewidth=1) # y-axis
        plt.axhline(y=0, color='black', linewidth=1) # x-axis
        plt.axvline(x=self.x_limit, color='red', linestyle='--', label=f'$x={self.x_limit}$')

        # Labels
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='upper right')
        plt.grid(True, linestyle=':', alpha=0.6)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat160:
    
    def __init__(self):
        # Equation form: y = A * func^2(B * x)
        self.amplitude = rnd.randint(1, 5)  # A
        self.freq = rnd.randint(1, 3)       # B
        self.func_type = rnd.choice(['sin', 'cos'])
        
        # Randomize interval [0, upper_limit]
        # We choose limits that result in clean answers (multiples of pi/4 or pi/2)
        # limit_coeff represents the multiplier of pi (e.g., 0.5 means pi/2, 1 means pi)
        self.limit_choices = [0.5, 1.0, 1.5, 2.0] 
        self.limit_coeff = rnd.choice(self.limit_choices) 
        self.upper_limit = self.limit_coeff * np.pi
        
        # Integral of A*cos^2(Bx) dx = A * [ x/2 + sin(2Bx)/(4B) ]
        # Integral of A*sin^2(Bx) dx = A * [ x/2 - sin(2Bx)/(4B) ]
        # Evaluated from 0 to upper_limit.
        
        # The term sin(2*B*limit) usually becomes 0 if limit is a multiple of pi/2 and B is int.
        # Let's compute exact float first, then format nicely.
        
        term1 = self.upper_limit / 2.0
        term2 = np.sin(2 * self.freq * self.upper_limit) / (4 * self.freq)
        
        if self.func_type == 'cos':
            area_val = self.amplitude * (term1 + term2)
        else:
            area_val = self.amplitude * (term1 - term2)

        # Format the function string for LaTeX
        # e.g. 3 \cos^2(2x)
        amp_str = str(self.amplitude) if self.amplitude > 1 else ""
        freq_str = str(self.freq) if self.freq > 1 else ""
        self.func_latex = f"{amp_str} \\{self.func_type}^2({freq_str}x)"
        
        # Format limit string
        if self.limit_coeff == 1:
            self.limit_text = r"\pi"
        elif self.limit_coeff == 0.5:
            self.limit_text = r"\frac{\pi}{2}"
        elif self.limit_coeff == 1.5:
            self.limit_text = r"\frac{3\pi}{2}"
        elif self.limit_coeff == 2:
            self.limit_text = r"2\pi"
        else:
            self.limit_text = f"{self.limit_coeff}\\pi"

        sign_op = "+" if self.func_type == 'cos' else "-"
        double_freq = 2 * self.freq

        self.answer = round(area_val, 3)

        self.description = (
            f"The figure shows the graph of $y = {self.func_latex}$ "
            f"over the interval $[0, {self.limit_text}]$. The area under the curve is shaded. "
            f"Find the area of the shaded region. Round to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Integration"
        self.source = "Adapted from Oxford International AQA Examinations: International A Level Mathematics"
        self.curriculum = "AS & A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{0}}^{{{self.limit_text}}} {self.func_latex} \\, dx\\\\"
            f"&= \\int_{{0}}^{{{self.limit_text}}} {self.amplitude} \\left( \\frac{{1 {sign_op} \\cos({double_freq}x)}}{{2}} \\right) \\, dx\\\\"
            f"&= \\frac{{{self.amplitude}}}{{2}} \\left[ x {sign_op} \\frac{{\\sin({double_freq}x)}}{{{double_freq}}} \\right]_{{0}}^{{{self.limit_text}}}\\\\"
            f"&= \\frac{{{self.amplitude}}}{{2}} \\left( \\left( {self.limit_text} {sign_op} \\frac{{\\sin({double_freq} \\cdot {self.limit_text})}}{{{double_freq}}} \\right) - 0 \\right)\\\\"
            f"&= \\frac{{{self.amplitude}}}{{2}} \\left( {round(self.upper_limit, 10)} {sign_op} 0 \\right)\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        x = np.linspace(0, self.upper_limit, 400)
        if self.func_type == 'cos':
            y = self.amplitude * (np.cos(self.freq * x) ** 2)
        else:
            y = self.amplitude * (np.sin(self.freq * x) ** 2)

        fig, ax = plt.subplots(figsize=(6, 4))
        
        # Plot line
        ax.plot(x, y, color='blue', linewidth=2, label=f'$y={self.func_latex}$')
        
        # Shade area
        ax.fill_between(x, y, alpha=0.3, color='skyblue', hatch='//')
        
        # Formatting axes
        ax.set_xlim(0, self.upper_limit * 1.1)
        ax.set_ylim(0, self.amplitude * 1.2)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Custom ticks for X-axis (0 and the upper limit)
        tick_vals = [0, self.upper_limit]
        tick_labels = ['$0$', f'${self.limit_text}$']
        
        # Optional: Add midpoint tick if interval is large
        if self.limit_coeff >= 1:
            midpoint = self.upper_limit / 2
            tick_vals.insert(1, midpoint)
            # Determine midpoint label
            if self.limit_coeff == 1: mid_lbl = r"\frac{\pi}{2}"
            elif self.limit_coeff == 2: mid_lbl = r"\pi"
            else: mid_lbl = " "
            tick_labels.insert(1, f"${mid_lbl}$")

        ax.set_xticks(tick_vals)
        ax.set_xticklabels(tick_labels)
        
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, linestyle='--', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat161:
    
    def __init__(self):
        # Function form: y = A / (x + B)
        # We choose ranges that generally ensure a visible intersection in the positive quadrant
        self.A = rnd.randint(2, 10)
        self.B = rnd.randint(1, 3)

        # Starting x1 (ensure it's not exactly the fixed point for visual interest)
        self.x1 = rnd.randint(1, 5)

        # 2. Calculate Iterations (The Logic)
        # x_n+1 = A / (x_n + B)
        self.iterations = [float(self.x1)]

        # Calculate up to x_3 for the answer, but more for the plot
        current_x = self.x1
        for _ in range(10):
            next_x = self.A / (current_x + self.B)
            self.iterations.append(next_x)
            current_x = next_x

        x2 = self.iterations[1]
        x3 = self.iterations[2]

        self.answer = round(x3, 3)

        self.description = (
            f"The diagram shows the graphs of $y = x$ and $y = \frac{{{self.A}}}{{x + {self.B}}}$ for $x > 0$. "
            f"A 'cobweb' sequence is drawn to illustrate the convergence of the iteration "
            f"$x_{{n+1}} = \frac{{{self.A}}}{{x_n + {self.B}}}$, starting from an initial value $x_1 = {self.x1}$, "
            f"which is marked on the x-axis. "
            f"Using the iterative formula suggested by the figure, calculate the value of the third iteration, $x_3$. "
            f"Round to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Numerical solution of equations"
        self.source = "Adapted from Visualizing convergence using cobweb diagrams"
        self.curriculum = "AS & A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The recurrence relation is given by:}} &\\\\"
            f"x_{{n+1}} &= \\frac{{{self.A}}}{{x_n + {self.B}}}\\\\"
            f"\\text{{First, calculate }} x_2 \\text{{ using }} x_1 = {self.x1}: &\\\\"
            f"x_2 &= \\frac{{{self.A}}}{{x_1 + {self.B}}}\\\\"
            f"&= \\frac{{{self.A}}}{{{self.x1} + {self.B}}}\\\\"
            f"&= \\frac{{{self.A}}}{{{self.x1 + self.B}}}\\\\"
            f"&= {round(self.iterations[1], 10)}\\\\"
            f"\\text{{Next, calculate }} x_3 \\text{{ using }} x_2: &\\\\"
            f"x_3 &= \\frac{{{self.A}}}{{x_2 + {self.B}}}\\\\"
            f"&= \\frac{{{self.A}}}{{{round(self.iterations[1], 10)} + {self.B}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))

        # Determine plot limits based on the trajectory
        max_val = max(max(self.iterations[:4]), self.x1) * 1.5
        x_vals = np.linspace(0.1, max_val, 400)

        # Plot y = x
        ax.plot(x_vals, x_vals, 'k--', label='$y=x$', alpha=0.5)

        # Plot Curve y = A / (x + B)
        y_vals = self.A / (x_vals + self.B)
        ax.plot(x_vals, y_vals, 'b-', label=f'$y = \\frac{{{self.A}}}{{x + {self.B}}}$')

        # Plot Cobweb path
        # Path coordinates: (x1,0) -> (x1, y1) -> (y1, y1) -> (y1, y2) -> ...
        px, py = [], []
        px.append(self.x1); py.append(0) # Start at axis

        curr = self.x1
        for _ in range(5): # Draw a few steps of the cobweb
            val = self.A / (curr + self.B)
            # Vertical move to curve
            px.append(curr); py.append(val)
            # Horizontal move to y=x
            px.append(val); py.append(val)
            curr = val

        ax.plot(px, py, 'r.-', alpha=0.6, linewidth=1.5, label='Cobweb sequence')

        # Formatting
        ax.set_title("Cobweb Diagram Iteration")
        ax.set_xlim(0, max_val)
        ax.set_ylim(0, max_val)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        ax.grid(True, alpha=0.3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat162:
    
    def __init__(self):
        # We loop until we find coefficients that create a visually clear graph
        # with a root that isn't ambiguous (i.e., not too close to an integer line).
        while True:
            # Equation form: y = a*ln(x) - x + b
            # Randomize coefficients (using integers for cleaner problem text)
            self.a = rnd.randint(2, 5) 
            self.b = rnd.randint(1, 6)
            
            # Define the function
            # Note: function is valid for x > 0
            def f(x):
                return self.a * np.log(x) - x + self.b
            
            # The maximum of this function occurs at x = a.
            # We need f(a) > 0 to ensure the curve crosses the x-axis twice.
            # We also want it reasonably high (> 0.5) so the "hump" is visible.
            self.peak_y = f(self.a)
            if self.peak_y < 0.5:
                continue
                
            # 2. Find the roots
            # The larger root (alpha) will be to the right of the peak (x > a).
            # We search from the peak 'a' up to a reasonable upper bound (e.g., 20).
            try:
                self.alpha = brentq(f, self.a + 0.01, 20)
            except ValueError:
                # If root finding fails (no root in range), re-roll variables
                continue
                
            # 3. Validation
            # Ensure the root is not too close to an integer (within 0.15)
            # to avoid visual ambiguity for the student.
            if abs(self.alpha - round(self.alpha)) < 0.15:
                continue
                
            # If we pass all checks, we have our variables.
            # The answer n is the floor of alpha.
            n = int(np.floor(self.alpha))
            break

        self.answer = n

        self.description = (
            f"The Figure shows a sketch of the curve $y = {self.a}\\ln(x) - x + {self.b}$. "
            f"The curve intersects the $x$-axis at two points. The larger root, $\\alpha$, "
            f"is shown to lie between two consecutive integers on the $x$-axis grid, "
            f"which is marked with unit intervals. "
            f"Based on the visual location of the larger root $\\alpha$ in the figure, "
            f"identify the integer $n$ such that $n < \\alpha < n+1$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Numerical solution of equations"
        self.source = "Adapted from Locating roots graphically and by searching for a sign change"
        self.curriculum = "AS & A Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The function is given by:}} &\\\\"
            f"f(x) &= {self.a} \\ln(x) - x + {self.b}\\\\"
            f"\\text{{To find the integer }} n \\text{{ such that }} n < \\alpha < n+1, \\text{{ we evaluate }} f(x) \\text{{ at consecutive integers.}} &\\\\"
            f"\\text{{Testing }} x &= {self.answer}:\\\\"
            f"f({self.answer}) &= {self.a} \\ln({self.answer}) - {self.answer} + {self.b}\\\\"
            f"&= {self.a}({round(np.log(self.answer), 10)}) - {self.answer} + {self.b}\\\\"
            f"&= {round(self.a * np.log(self.answer) - self.answer + self.b, 10)} \\quad (\\text{{positive}})\\\\"
            f"\\text{{Testing }} x &= {self.answer + 1}:\\\\"
            f"f({self.answer + 1}) &= {self.a} \\ln({self.answer + 1}) - ({self.answer + 1}) + {self.b}\\\\"
            f"&= {self.a}({round(np.log(self.answer + 1), 10)}) - {self.answer + 1} + {self.b}\\\\"
            f"&= {round(self.a * np.log(self.answer + 1) - (self.answer + 1) + self.b, 10)} \\quad (\\text{{negative}})\\\\"
            f"\\text{{Since the sign changes from positive to negative, the root }} \\alpha \\text{{ lies between }} {self.answer} \\text{{ and }} {self.answer + 1}. &\\\\"
            f"n &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Define the function
        # Note: function is valid for x > 0
        def f(x):
            return self.a * np.log(x) - x + self.b

        # Create domain for plotting: slightly above 0 to past the root
        x_max = int(self.alpha) + 2
        x_vals = np.linspace(0.1, x_max, 400)
        y_vals = f(x_vals)

        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot curve
        ax.plot(x_vals, y_vals, color='blue', linewidth=2, label=f'$y = {self.a}\\ln(x) - x + {self.b}$')
        
        # Style the axes to look like a standard math problem
        ax.axhline(0, color='black', linewidth=1.5) # x-axis
        ax.axvline(0, color='black', linewidth=1.5) # y-axis
        
        # Grid settings: Major ticks at every integer
        ax.set_xticks(np.arange(0, x_max + 1, 1))
        ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
        
        # Limits
        ax.set_ylim(bottom=-3, top=self.peak_y + 1)
        ax.set_xlim(left=0, right=x_max)
        
        # Labels
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_title("Sketch of the curve")
        ax.legend(loc='upper right')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat163:
    
    def __init__(self):
        while True:
            # Generate random components for a (full) and b (partial)
            # We limit the range to keep the numbers friendly (-8 to 8)
            self.ax = rnd.choice([i for i in range(-8, 9) if i != 0])
            self.ay = rnd.randint(-8, 8)
            self.az = rnd.randint(-8, 8)

            self.by = rnd.randint(-8, 8)
            self.bz = rnd.randint(-8, 8)

            # Calculate the dot product of the known Y and Z parts
            partial_dot = (self.ay * self.by) + (self.az * self.bz)

            # We need: ax*p + ay*by + az*bz = 0  =>  ax*p = -partial_dot
            # To ensure 'p' is an integer, 'ax' must divide '-partial_dot' perfectly.
            target = -partial_dot

            if target == 0:
                # If target is 0, p would be 0 (if ax != 0).
                # We accept this but ensure vectors aren't zero vectors.
                self.p = 0
            elif target % self.ax == 0:
                self.p = target // self.ax
            else:
                # If division isn't clean, re-roll the random numbers
                continue

            # Ensure neither vector is a zero vector [0,0,0]
            if (self.ax==0 and self.ay==0 and self.az==0) or (self.p==0 and self.by==0 and self.bz==0):
                continue

            # If we got here, we found valid numbers
            break

        vec_a_str = self.format_vec_str(self.ax, self.ay, self.az)
        vec_b_str = self.format_vec_str(self.p, self.by, self.bz, unknown_axis='i')

        self.answer = self.p

        self.description = (
            f"The figure displays two vectors originating from a common point $O$ in 3D space. "
            f"Vector $\\mathbf{{a}}$ is defined as ${vec_a_str}$. "
            f"Vector $\\mathbf{{b}}$ is defined as ${vec_b_str}$. "
            f"A right-angle symbol indicates that the two vectors are perpendicular to each other. "
            f"Given that the vectors $\\mathbf{{a}}$ and $\\mathbf{{b}}$ are perpendicular, "
            f"calculate the value of the constant $p$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Vectors"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 3"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Two vectors are perpendicular if their dot product is zero:}} &\\\\"
            f"\\mathbf{{a}} \\cdot \\mathbf{{b}} &= 0\\\\"
            f"a_x b_x + a_y b_y + a_z b_z &= 0\\\\"
            f"({self.ax})(p) + ({self.ay})({self.by}) + ({self.az})({self.bz}) &= 0\\\\"
            f"{self.ax}p + ({self.ay * self.by}) + ({self.az * self.bz}) &= 0\\\\"
            f"{self.ax}p + ({self.ay * self.by + self.az * self.bz}) &= 0\\\\"
            f"{self.ax}p &= {-(self.ay * self.by + self.az * self.bz)}\\\\"
            f"p &= \\frac{{{-(self.ay * self.by + self.az * self.bz)}}}{{{self.ax}}}\\\\"
            f"p &= {self.answer}"
            "\\end{aligned}\\]"
        )


    def format_vec_str(self, x, y, z, unknown_axis=None):
        components = []

        # Helper to format individual terms like "- 2j" or "+ k"
        def add_term(val, label, is_unknown=False):
            if is_unknown:
                return f"p\\mathbf{{{label}}}"
            if val == 0: return None

            abs_val = abs(val)
            val_str = "" if abs_val == 1 else str(abs_val)
            sign = "+" if val > 0 else "-"
            return (sign, f"{val_str}\\mathbf{{{label}}}")

        # Process X
        is_p = (unknown_axis == 'i')
        term_x = add_term(x, 'i', is_p)

        # Process Y
        term_y = add_term(y, 'j')

        # Process Z
        term_z = add_term(z, 'k')

        # Build list
        raw_terms = []
        if is_p:
            raw_terms.append(term_x) # just the string for p
        elif term_x:
            raw_terms.append(term_x) # (sign, string)

        if term_y: raw_terms.append(term_y)
        if term_z: raw_terms.append(term_z)

        # Construct final string
        final_str = ""
        for i, item in enumerate(raw_terms):
            if isinstance(item, str): # This is the 'p' case
                final_str += item
            else:
                sign, text = item
                if i == 0: # First term
                    if sign == "-": final_str += "-" + text
                    else: final_str += text
                else: # Subsequent terms need spacing
                    final_str += f" {sign} {text}"

        return final_str if final_str else "\\mathbf{0}"

    def generate(self, num):
        fig = plt.figure(figsize=(6, 6))
        ax_plot = fig.add_subplot(111, projection='3d')

        # Vector data
        origin = [0, 0, 0]
        # We plot the actual numeric solution for 'b'
        V = np.array([[self.ax, self.ay, self.az], [self.p, self.by, self.bz]])
        colors = ['r', 'b']
        labels = [r'$\mathbf{a}$', r'$\mathbf{b}$']

        # Quiver plot
        for i in range(2):
            ax_plot.quiver(0, 0, 0, V[i, 0], V[i, 1], V[i, 2],
                        color=colors[i], label=labels[i], arrow_length_ratio=0.1, linewidth=2)

        # Setting plot limits to ensure vectors are visible
        limit = max(np.max(np.abs(V)), 1) * 1.2
        ax_plot.set_xlim([-limit, limit])
        ax_plot.set_ylim([-limit, limit])
        ax_plot.set_zlim([-limit, limit])

        # Labels and Title
        ax_plot.set_xlabel('x')
        ax_plot.set_ylabel('y')
        ax_plot.set_zlabel('z')
        ax_plot.legend()

        # Visual helper for origin
        ax_plot.scatter(0,0,0, color='k', s=50)
        ax_plot.text(0, 0, -limit*0.1, "$O$", fontsize=12)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat164:
    
    def __init__(self):
        # To guarantee the problem is solvable, we start with the intersection point (X)
        # and work backward to find A and B.
        
        # Random Intersection Point X
        self.X = np.random.randint(-5, 6, 3) # [x, y, z]

        # Random Direction Vectors (d1, d2)
        # Ensure they are not parallel (cross product != 0)
        while True:
            self.d1 = np.random.randint(-3, 4, 3)
            self.d2 = np.random.randint(-3, 4, 3)
            # Avoid zero vectors and parallel vectors
            if (np.linalg.norm(self.d1) > 0 and np.linalg.norm(self.d2) > 0 and 
                np.linalg.norm(np.cross(self.d1, self.d2)) > 0.1):
                break

        # Random scalar multipliers (t and s) to define positions of A and B relative to X
        # We ensure A and B are not the same point as X (multiplier != 0)
        t_val = rnd.choice([-2, -1, 1, 2])
        s_val = rnd.choice([-2, -1, 1, 2])

        # Calculate Points A and B based on the logic: Point = Intersection - (scalar * direction)
        # If A + t*d1 = X, then A = X - t*d1
        self.A = self.X - (t_val * self.d1)
        self.B = self.X - (s_val * self.d2)
        
        # The "hidden" variable m is the z-component of B
        m_answer = self.B[2]

        d1_str = f"{self.d1[0]}i + {self.d1[1]}j + {self.d1[2]}k".replace("+-", "- ").replace("+ -", "- ")
        d2_str = f"{self.d2[0]}i + {self.d2[1]}j + {self.d2[2]}k".replace("+-", "- ").replace("+ -", "- ")

        self.answer = int(m_answer)

        self.description = (
            f"A diagram shows two straight lines, $L_1$ and $L_2$, "
            f"intersecting at a single point $X$ in three-dimensional space.\n\n"
            f"**Line $L_1$** passes through point $A({self.A[0]}, {self.A[1]}, {self.A[2]})$ and is parallel "
            f"to the vector $\\mathbf{{d_1}} = {d1_str}$.\n\n"
            f"**Line $L_2$** passes through point $B({self.B[0]}, {self.B[1]}, m)$ and is parallel "
            f"to the vector $\\mathbf{{d_2}} = {d2_str}$.\n\n"
            f"By solving for the intersection of these two lines, determine the numerical value of the constant $m$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Vectors"
        self.source = "Adapted from Nelson Mathematics for Cambridge International A Level: Pure Mathematics 2 & 3"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The parametric equations for line }} L_1 \\text{{ are:}} \\\\"
            f"\\mathbf{{r}}_1 &= \\begin{{pmatrix}} {self.A[0]} \\\\ {self.A[1]} \\\\ {self.A[2]} \\end{{pmatrix}} + t \\begin{{pmatrix}} {self.d1[0]} \\\\ {self.d1[1]} \\\\ {self.d1[2]} \\end{{pmatrix}} \\\\"
            f"\\text{{The parametric equations for line }} L_2 \\text{{ are:}} \\\\"
            f"\\mathbf{{r}}_2 &= \\begin{{pmatrix}} {self.B[0]} \\\\ {self.B[1]} \\\\ m \\end{{pmatrix}} + s \\begin{{pmatrix}} {self.d2[0]} \\\\ {self.d2[1]} \\\\ {self.d2[2]} \\end{{pmatrix}} \\\\"
            f"\\text{{Since the lines intersect, we equate the }} x \\text{{ and }} y \\text{{ components:}} \\\\"
            f"{self.A[0]} + ({self.d1[0]})t &= {self.B[0]} + ({self.d2[0]})s \\\\"
            f"{self.A[1]} + ({self.d1[1]})t &= {self.B[1]} + ({self.d2[1]})s \\\\"
            f"\\text{{Solving this system for }} t \\text{{ and }} s \\text{{ yields:}} \\\\"
            f"t &= {t_val}, \\quad s = {s_val} \\\\"
            f"\\text{{Now, equate the }} z \\text{{ components to find }} m: \\\\"
            f"{self.A[2]} + ({self.d1[2]})t &= m + ({self.d2[2]})s \\\\"
            f"\\text{{Substituting }} t={t_val} \\text{{ and }} s={s_val}: \\\\"
            f"{self.A[2]} + ({self.d1[2]})({t_val}) &= m + ({self.d2[2]})({s_val}) \\\\"
            f"{round(self.A[2] + self.d1[2] * t_val, 10)} &= m + ({round(self.d2[2] * s_val, 10)}) \\\\"
            f"m &= {round(self.A[2] + self.d1[2] * t_val, 10)} - ({round(self.d2[2] * s_val, 10)}) \\\\"
            f"m &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Generate line points for plotting
        # We plot a segment from (X - 3*d) to (X + 3*d) to ensure visual coverage
        line1_pts = np.array([self.X - 3*self.d1, self.X + 3*self.d1])
        line2_pts = np.array([self.X - 3*self.d2, self.X + 3*self.d2])

        # Plot Lines
        ax.plot(line1_pts[:,0], line1_pts[:,1], line1_pts[:,2], label='$L_1$', color='blue', alpha=0.6)
        ax.plot(line2_pts[:,0], line2_pts[:,1], line2_pts[:,2], label='$L_2$', color='red', alpha=0.6)

        # Plot Points
        ax.scatter(*self.A, color='blue', s=100, label='Point A', edgecolors='black')
        ax.scatter(*self.B, color='red', s=100, label='Point B', edgecolors='black')
        ax.scatter(*self.X, color='green', s=150, marker='X', label='Intersection X', edgecolors='black')

        # Add Direction Vectors (Quivers) starting at A and B
        ax.quiver(self.A[0], self.A[1], self.A[2], self.d1[0], self.d1[1], self.d1[2], length=1.5, normalize=True, color='blue', linestyle='--')
        ax.quiver(self.B[0], self.B[1], self.B[2], self.d2[0], self.d2[1], self.d2[2], length=1.5, normalize=True, color='red', linestyle='--')

        # Labels and Legend
        ax.text(self.A[0], self.A[1], self.A[2], f" A", fontsize=10)
        ax.text(self.B[0], self.B[1], self.B[2], f" B", fontsize=10)
        ax.text(self.X[0], self.X[1], self.X[2], f" X", fontsize=10)
        
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.legend()
        
        # Auto-scale adjustment for better view
        all_pts = np.vstack([self.A, self.B, self.X])
        center = np.mean(all_pts, axis=0)
        radius = np.max(np.linalg.norm(all_pts - center, axis=1)) + 2
        
        ax.set_xlim(center[0] - radius, center[0] + radius)
        ax.set_ylim(center[1] - radius, center[1] + radius)
        ax.set_zlim(center[2] - radius, center[2] + radius)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat165:
    
    def __init__(self):
        # Randomize Variables (Use even numbers for a and b to keep M clean, optionally)
        self.a_val = rnd.randint(2, 8)  # Coefficient for i (x-axis)
        self.b_val = rnd.randint(2, 8)  # Coefficient for j (y-axis)
        self.c_val = rnd.randint(2, 8)  # Coefficient for k (z-axis)

        # Define Coordinates
        self.origin = np.array([0, 0, 0])
        self.A = np.array([self.a_val, 0, 0])
        self.B = np.array([0, self.b_val, 0])
        self.C = np.array([0, 0, self.c_val])

        # Midpoint M of edge AB
        self.M = (self.A + self.B) / 2

        # Vector MC = C - M
        vec_MC = self.C - self.M

        # Squared Magnitude = x^2 + y^2 + z^2
        magnitude_squared = vec_MC[0]**2 + vec_MC[1]**2 + vec_MC[2]**2

        self.answer = magnitude_squared

        self.description = (
            f"A triangular pyramid $OABC$ is shown with the origin at $O(0,0,0)$.\n"
            f"The vertices are located at position vectors $\\mathbf{{a}} = {self.a_val}\\mathbf{{i}}$, "
            f"$\\mathbf{{b}} = {self.b_val}\\mathbf{{j}}$, and $\\mathbf{{c}} = {self.c_val}\\mathbf{{k}}$.\n"
            f"A point $M$ is marked as the exact midpoint of the edge $AB$.\n"
            f"A vector $\vec{{MC}}$ connects $M$ to the top vertex $C$.\n\n"
            f"Calculate the squared magnitude of the vector $\vec{{MC}}$ (i.e., calculate $|\vec{{MC}}|^2$)."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Vectors"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 3 Coursebook"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Coordinates of vertices:}} &\\\\"
            f"A &= ({self.a_val}, 0, 0), \\quad B = (0, {self.b_val}, 0), \\quad C = (0, 0, {self.c_val})\\\\"
            f"\\text{{Midpoint }} M \\text{{ of edge }} AB: &\\\\"
            f"M &= \\frac{{A + B}}{{2}}\\\\"
            f"&= \\left( \\frac{{{self.a_val} + 0}}{{2}}, \\frac{{0 + {self.b_val}}}{{2}}, \\frac{{0 + 0}}{{2}} \\right)\\\\"
            f"&= ({round(self.M[0], 10)}, {round(self.M[1], 10)}, 0)\\\\"
            f"\\text{{Vector }} \\vec{{MC}} \\text{{ is given by }} C - M: &\\\\"
            f"\\vec{{MC}} &= (0, 0, {self.c_val}) - ({round(self.M[0], 10)}, {round(self.M[1], 10)}, 0)\\\\"
            f"&= ({round(vec_MC[0], 10)}, {round(vec_MC[1], 10)}, {round(vec_MC[2], 10)})\\\\"
            f"\\text{{Squared magnitude }} |\\vec{{MC}}|^2: &\\\\"
            f"|\\vec{{MC}}|^2 &= x^2 + y^2 + z^2\\\\"
            f"&= ({round(vec_MC[0], 10)})^2 + ({round(vec_MC[1], 10)})^2 + ({round(vec_MC[2], 10)})^2\\\\"
            f"&= {round(vec_MC[0]**2, 10)} + {round(vec_MC[1]**2, 10)} + {round(vec_MC[2]**2, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Plot Vertices
        vertices = {'O': self.origin, 'A': self.A, 'B': self.B, 'C': self.C}
        for name, point in vertices.items():
            ax.scatter(*point, color='black', s=50)
            ax.text(point[0], point[1], point[2]+0.2, f" {name}", fontsize=12, fontweight='bold')

        # Plot Edges of the Pyramid
        # Base: OA, OB, AB
        ax.plot([self.origin[0], self.A[0]], [self.origin[1], self.A[1]], [self.origin[2], self.A[2]], 'k-', alpha=0.5) # OA
        ax.plot([self.origin[0], self.B[0]], [self.origin[1], self.B[1]], [self.origin[2], self.B[2]], 'k-', alpha=0.5) # OB
        ax.plot([self.A[0], self.B[0]], [self.A[1], self.B[1]], [self.A[2], self.B[2]], 'k-', alpha=0.5)      # AB

        # Sides: OC, AC, BC
        ax.plot([self.origin[0], self.C[0]], [self.origin[1], self.C[1]], [self.origin[2], self.C[2]], 'k-', alpha=0.5) # OC
        ax.plot([self.A[0], self.C[0]], [self.A[1], self.C[1]], [self.A[2], self.C[2]], 'k-', alpha=0.5)      # AC
        ax.plot([self.B[0], self.C[0]], [self.B[1], self.C[1]], [self.B[2], self.C[2]], 'k-', alpha=0.5)      # BC

        # Plot Midpoint M
        ax.scatter(*self.M, color='red', s=60, label='M (Midpoint)')
        ax.text(self.M[0], self.M[1], self.M[2]-0.5, " M", color='red', fontsize=12, fontweight='bold')

        # Plot Vector MC
        # We use quiver for the vector arrow, but a simple line often looks cleaner in static 3D plots
        ax.plot([self.M[0], self.C[0]], [self.M[1], self.C[1]], [self.M[2], self.C[2]], color='red', linewidth=3, linestyle='--', label='Vector MC')

        # Formatting the Plot
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Triangular Pyramid OABC')

        # Ensure aspect ratio is roughly equal so geometry isn't distorted
        max_range = max(self.a_val, self.b_val, self.c_val)
        ax.set_xlim(0, max_range)
        ax.set_ylim(0, max_range)
        ax.set_zlim(0, max_range)
        ax.legend()

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat166:
    
    def __init__(self):
        # Using numpy arrays for easy vector math
        self.a = np.array([rnd.randint(0, 10) for _ in range(3)])
        self.b = np.array([rnd.randint(0, 10) for _ in range(3)])
        self.c = np.array([rnd.randint(0, 10) for _ in range(3)])

        # Property: Vector AB = Vector DC
        # (B - A) = (C - D)  =>  D = C - B + A
        self.d = self.c - self.b + self.a

        # Calculate the answer (sum of x, y, z of D)
        self.answer_sum = np.sum(self.d)

        self.answer = int(self.answer_sum)

        self.description = (
            f"A parallelogram $ABCD$ is plotted in a 3D coordinate system. "
            f"The coordinates for three of the vertices are provided:\n"
            f"$A = ({self.a[0]}, {self.a[1]}, {self.a[2]})$\n"
            f"$B = ({self.b[0]}, {self.b[1]}, {self.b[2]})$\n"
            f"$C = ({self.c[0]}, {self.c[1]}, {self.c[2]})$\n"
            f"The fourth vertex $D$ is labeled with unknown coordinates $(x, y, z)$. "
            f"Using vector addition/subtraction properties for a parallelogram "
            f"find the sum of the coordinates of vertex $D$ (i.e., calculate $x + y + z$)."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Vectors"
        self.source = "Adapted from Pure Mathematics by Bostock and Chandler"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given vertices:}} &\\\\"
            f"A &= ({self.a[0]}, {self.a[1]}, {self.a[2]})\\\\"
            f"B &= ({self.b[0]}, {self.b[1]}, {self.b[2]})\\\\"
            f"C &= ({self.c[0]}, {self.c[1]}, {self.c[2]})\\\\"
            f"\\text{{For parallelogram }} ABCD, \\text{{ we use the vector property:}} &\\\\"
            f"\\vec{{AB}} &= \\vec{{DC}}\\\\"
            f"B - A &= C - D\\\\"
            f"\\text{{Solving for vertex }} D: &\\\\"
            f"D &= C - B + A\\\\"
            f"&= ({self.c[0]}, {self.c[1]}, {self.c[2]}) - ({self.b[0]}, {self.b[1]}, {self.b[2]}) + ({self.a[0]}, {self.a[1]}, {self.a[2]})\\\\"
            f"&= ({self.c[0]} - {self.b[0]} + {self.a[0]},\\; {self.c[1]} - {self.b[1]} + {self.a[1]},\\; {self.c[2]} - {self.b[2]} + {self.a[2]})\\\\"
            f"&= ({self.d[0]}, {self.d[1]}, {self.d[2]})\\\\"
            f"\\text{{Summing the coordinates of }} D: &\\\\"
            f"\\text{{Sum}} &= {self.d[0]} + {self.d[1]} + {self.d[2]}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Combine points for plotting order: A -> B -> C -> D -> A
        # We stack them to make drawing the lines easier
        points = np.vstack([self.a, self.b, self.c, self.d, self.a])

        # Plot the lines
        x_vals, y_vals, z_vals = points[:, 0], points[:, 1], points[:, 2]
        ax.plot(x_vals, y_vals, z_vals, color='blue', linewidth=2, label='Parallelogram ABCD')

        # Plot the vertices (scatter)
        ax.scatter(x_vals[:-1], y_vals[:-1], z_vals[:-1], color='red', s=50)

        # Add Labels
        labels = ['A', 'B', 'C', 'D']
        coords = [self.a, self.b, self.c, self.d]
        for lbl, coord in zip(labels, coords):
            if lbl == 'D':
                ax.text(coord[0], coord[1], coord[2], f'  {lbl} (x, y, z)', fontsize=10)
            else:
                ax.text(coord[0], coord[1], coord[2], f'  {lbl} {tuple(map(int, coord))}', fontsize=10)

        # Styling the graph
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat167:
    
    def __init__(self):
        # We choose integers between -8 and 8, excluding 0, for clearer visualization
        self.real_part = rnd.choice([i for i in range(-8, 9) if i != 0])
        self.imag_part = rnd.choice([i for i in range(-8, 9) if i != 0])

        # Define complex number z1 (Vertex P)
        self.z1 = complex(self.real_part, self.imag_part)

        # In a square OPQR (Counter-Clockwise), R is obtained by rotating P
        # 90 degrees (pi/2) counter-clockwise about the origin O.
        # Mathematically, this is multiplication by i (j in Python).
        self.z_o = 0j
        self.z_p = self.z1
        self.z_r = self.z1 * 1j
        self.z_q = self.z_p + self.z_r # Vector addition to find the far corner

        # Format the complex number string (e.g., "4 + 2i" or "3 - 5i")
        self.operator = "+" if self.z1.imag >= 0 else "-"
        self.z1_str = f"{self.z1.real} {self.operator} {abs(int(self.z1.imag))}i"

        self.answer = int(self.z_r.imag)

        self.description = (
            f"The figure shows a square in the Argand diagram with vertices "
            f"labeled $O$, $P$, $Q$, and $R$ in counter-clockwise order. $O$ is the origin $(0,0)$. "
            f"The vertex $P$ represents the complex number $z_1 = {self.z1_str}$.\n\n"
            f"If the vertices form a square $OPQR$, determine the imaginary part of "
            f"the complex number represented by vertex $R$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Complex numbers"
        self.source = "Adapted from Pure Mathematics 2 & 3, Cambridge University Press"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given vertex }} P, z_P &= {self.z1_str}\\\\"
            f"\\text{{Since }} OPQR \\text{{ is a square in counter-clockwise order,}}\\\\"
            f"\\text{{vertex }} R \\text{{ is obtained by rotating }} P \\text{{ by }} 90^\\circ \\text{{ counter-clockwise about }} O.\\\\"
            f"\\text{{Rotation by }} 90^\\circ \\text{{ corresponds to multiplication by }} i:\\\\"
            f"z_R &= z_P \\cdot i\\\\"
            f"&= ({self.z1_str}) \\cdot i\\\\"
            f"&= {self.real_part}i {self.operator} {abs(self.imag_part)}i^2\\\\"
            f"&= {self.real_part}i {self.operator} {abs(self.imag_part)}(-1)\\\\"
            f"&= {int(-self.imag_part)} + {self.real_part}i\\\\"
            f"\\text{{The imaginary part of }} z_R &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Order of vertices for drawing lines: O -> P -> Q -> R -> O
        vertices = [self.z_o, self.z_p, self.z_q, self.z_r, self.z_o]
        X = [v.real for v in vertices]
        Y = [v.imag for v in vertices]

        # Plot square
        ax.plot(X, Y, 'b-', linewidth=2, label='Square OPQR')
        ax.fill(X, Y, 'blue', alpha=0.1) # Light shading inside

        # Plot points
        ax.scatter(X[:-1], Y[:-1], color='red', zorder=5)

        # Label vertices
        labels = ['O', 'P', 'Q', 'R']
        for i, txt in enumerate(labels):
            # Add a small offset to text so it doesn't overlap the dot
            ax.text(X[i] + 0.5, Y[i] + 0.5, txt, fontsize=12, fontweight='bold', color='darkred')

        # Formatting the Graph
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        ax.set_aspect('equal') # Crucial so the square looks like a square
        ax.set_title(f"Argand Diagram")
        ax.set_xlabel("Real Axis")
        ax.set_ylabel("Imaginary Axis")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

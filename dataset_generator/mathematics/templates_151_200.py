import numpy as np
import pandas as pd
import random as rnd
import os
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from scipy.optimize import brentq
from scipy.stats import binom, norm
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
            f"at $(0, {self.intercept_c})$ and a second point at $({self.x2}, {self.y2_log})$. "
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
            else: mid_lbl = ""
            tick_labels.insert(1, f"{"$" + mid_lbl + "$" if mid_lbl else ""}")

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

class Mat168:
    
    def __init__(self):
        # Randomize radius (integer between 2 and 5)
        self.r = rnd.randint(2, 5)

        # Randomize center of circle (cx, cy)
        # Keeping cx within a range so the tangent doesn't go too far off screen
        self.cx = rnd.randint(-2, 5)
        self.cy = rnd.randint(-4, 4)

        # Calculate the solution 'k'
        # Condition: The vertical line is tangent to the circle on the RIGHT-hand side.
        # Therefore, k = center_x + radius
        self.k = self.cx + self.r

        # Format the complex number string for the center text: |z - (a + bi)|
        # We need to handle signs gracefully for the text display
        if self.cy == 0:
            self.center_str = f"{self.cx}"
        elif self.cy < 0:
            self.center_str = f"{self.cx} - {abs(self.cy)}i"
        else:
            self.center_str = f"{self.cx} + {self.cy}i"

        self.answer = self.k

        self.description = (
            f"The figure displays an Argand diagram with a circle and a vertical line.\n"
            f"The circle represents the locus defined by $|z - ({self.center_str})| = {self.r}$.\n"
            f"The line represents the locus of points where the real part of $z$ is $k$.\n"
            f"The line is tangent to the circle on the right-hand side.\n\n"
            f"Determine the value of the real number $k$ represented by the vertical line."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Complex numbers"
        self.source = "Adapted from Oxford International AQA Examinations: Pure Mathematics"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the circle equation }} |z - ({self.center_str})| &= {self.r}:\\\\"
            f"\\text{{Center real part }} (x_c) &= {self.cx}\\\\"
            f"\\text{{Radius }} (r) &= {self.r}\\\\"
            f"\\text{{For a vertical line tangent to the right side:}} &\\\\"
            f"k &= x_c + r\\\\"
            f"&= {self.cx} + {self.r}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Set up the Argand Diagram (ComplexPlane)
        ax.set_aspect('equal')
        ax.set_xlabel('Re(z)')
        ax.set_ylabel('Im(z)')
        ax.set_title('Argand Diagram')
        ax.grid(True, linestyle='--', alpha=0.6)

        # Plot the Circle
        # Create circle patch
        circle = plt.Circle((self.cx, self.cy), self.r, color='blue', fill=False, linewidth=2, label=f'$|z - ({self.center_str})| = {self.r}$');
        ax.add_patch(circle)
        # Plot center point
        ax.plot(self.cx, self.cy, 'bo', markersize=5)

        # Plot the Vertical Line (Tangent)
        # We add some padding to y-limits for the line drawing
        line_min_y = self.cy - self.r - 2
        line_max_y = self.cy + self.r + 2
        ax.vlines(x=self.k, ymin=line_min_y, ymax=line_max_y, color='red', linewidth=2, label=f'Re(z) = k')

        # Annotate the tangency point
        ax.plot(self.k, self.cy, 'ro', markersize=5)
        ax.annotate(f'k', xy=(self.k, self.cy), xytext=(self.k + 1, self.cy + 1),
                    arrowprops=dict(facecolor='black', arrowstyle='->'))

        # Set Axis limits dynamically to ensure everything is visible
        padding = 2
        ax.set_xlim(self.cx - self.r - padding, self.k + padding)
        ax.set_ylim(self.cy - self.r - padding, self.cy + self.r + padding)

        # Add legend
        ax.legend(loc='upper left', fontsize='small', framealpha=0.9)

        # Prevent overlap
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat169:
    
    def __init__(self):
        self.real_part = rnd.randint(2, 8)  # a
        self.imag_part = rnd.randint(2, 8)  # b
        
        # Define points
        # Origin
        self.O = np.array([0, 0])
        # Point A (z)
        self.A = np.array([self.real_part, self.imag_part])
        # Point B (z conjugate)
        self.B = np.array([self.real_part, -self.imag_part])

        self.z_str = f"{self.real_part} + {self.imag_part}i"

        # Calculate Area
        # Base is distance between z and z_conjugate = 2 * imag_part
        # Height is distance from Origin to real_part = real_part
        self.base = 2 * self.imag_part
        self.height = self.real_part
        self.area = 0.5 * self.base * self.height

        self.answer = int(self.area)

        self.description = (
            f"The figure shows an Argand diagram with three points plotted: the origin $O$, "
            f"a point $A$ representing the complex number $z = {self.z_str}$, "
            f"and a point $B$ representing the complex conjugate $\\bar{{z}}$.\n"
            f"A shaded triangle connects these three points ($O$, $A$, and $B$).\n\n"
            f"Calculate the area of the shaded triangle $OAB$."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Complex numbers"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 3 Coursebook"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Coordinates of }} A &= ({self.real_part}, {self.imag_part})\\\\"
            f"\\text{{Coordinates of }} B &= ({self.real_part}, -{self.imag_part})\\\\"
            f"\\text{{Base (distance }} AB\\text{{)}} &= |{self.imag_part} - (-{self.imag_part})|\\\\"
            f"&= {self.imag_part} + {self.imag_part}\\\\"
            f"&= {self.base}\\\\"
            f"\\text{{Height (real part)}} &= {self.real_part}\\\\"
            f"\\text{{Area}} &= \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}\\\\"
            f"&= \\frac{{1}}{{2}} \\times {self.base} \\times {self.height}\\\\"
            f"&= {round(0.5 * self.base, 10)} \\times {self.height}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Plot the points
        ax.scatter([self.O[0], self.A[0], self.B[0]], [self.O[1], self.A[1], self.B[1]], color='black', zorder=5)
        
        # Label the points
        ax.text(self.O[0] - 0.5, self.O[1], '$O$', fontsize=12, ha='right')
        ax.text(self.A[0] + 0.3, self.A[1], '$A (z)$', fontsize=12)
        ax.text(self.B[0] + 0.3, self.B[1], '$B (\\bar{z})$', fontsize=12)
        
        # Draw the Triangle and Shade it
        triangle_points = np.array([self.O, self.A, self.B])
        tri = Polygon(triangle_points, closed=True, color='skyblue', alpha=0.4, label='Triangle OAB')
        ax.add_patch(tri)
        
        # Draw edges of the triangle
        ax.plot([self.O[0], self.A[0]], [self.O[1], self.A[1]], 'b--', lw=1) # O to A
        ax.plot([self.O[0], self.B[0]], [self.O[1], self.B[1]], 'b--', lw=1) # O to B
        ax.plot([self.A[0], self.B[0]], [self.A[1], self.B[1]], 'b-', lw=1.5) # A to B (Vertical)

        # 3. Axis Formatting (Make it look like an Argand Diagram)
        limit = max(self.real_part, self.imag_part) + 2
        ax.set_xlim(-1, limit)
        ax.set_ylim(-limit, limit)
        
        # Move left and bottom spines to x = 0 and y = 0
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # Add grid and labels
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.set_xlabel('Real ($Re$)', loc='right')
        ax.set_ylabel('Imaginary ($Im$)', loc='top', rotation=0)
        ax.set_aspect('equal') # Crucial for geometry to look correct

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat170:
    
    def __init__(self):
        # Randomize the starting point A on the imaginary axis (0, y_start)
        # We pick an integer between 2 and 8 to keep the scale reasonable.
        self.y_start = rnd.randint(2, 8)
        
        # Randomize the angle (argument). 
        # We choose standard angles so the math is "cleaner" for students, 
        # but strictly negative to go "downwards".
        angle_options = [
            (30, r"-\frac{\pi}{6}", np.pi/6),
            (45, r"-\frac{\pi}{4}", np.pi/4),
            (60, r"-\frac{\pi}{3}", np.pi/3)
        ]
        self.deg_val, self.latex_angle, self.rad_val = rnd.choice(angle_options)
        
        # The actual geometric angle is negative
        self.theta = -self.rad_val
        
        # The ray starts at (0, y_start). Slope m = tan(theta).
        # Equation of line: y - y_start = m(x - 0)  =>  y = mx + y_start
        # To find x-intercept, set y = 0:
        # 0 = mx + y_start  =>  x = -y_start / m
        self.m = np.tan(self.theta)
        self.x_intercept = -self.y_start / self.m

        self.answer = round(self.x_intercept, 3)

        self.description = (
            f"The figure shows a ray (half-line) originating from "
            f"the point $A$ at coordinates $(0, {self.y_start})$ on the imaginary axis. "
            f"The ray extends downwards and to the right, representing the locus "
            f"$\\arg(z - {self.y_start}i) = {self.latex_angle}$.\n\n"
            f"Find the value of the $x$-intercept where this locus, "
            f"if extended as a full line, would cross the real axis. "
            f"Round to 3 decimal places."
        )

        self.topic = "Pure Mathematics 3"
        self.subtopic = "Complex numbers"
        self.source = "Adapted from Edexcel A Level Mathematics: Pure Mathematics Year 2"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The ray starts at point }} A &= (0, {self.y_start})\\\\"
            f"\\text{{The angle is }} \\theta &= {self.latex_angle}\\\\"
            f"\\text{{The slope }} m \\text{{ is calculated as:}} &\\\\"
            f"m &= \\tan(\\theta) = \\tan\\left({self.latex_angle}\\right)\\\\"
            f"&= {round(self.m, 10)}\\\\"
            f"\\text{{Using the point-slope equation }} y - y_1 &= m(x - x_1):\\\\"
            f"y - {self.y_start} &= {round(self.m, 10)}(x - 0)\\\\"
            f"\\text{{To find the x-intercept, set }} y &= 0:\\\\"
            f"0 - {self.y_start} &= {round(self.m, 10)}x\\\\"
            f"-{self.y_start} &= {round(self.m, 10)}x\\\\"
            f"x &= \\frac{{-{self.y_start}}}{{{round(self.m, 10)}}}\\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Set plot limits based on the calculated intercept to ensure everything fits
        limit_x = self.x_intercept * 1.5
        limit_y = self.y_start * 1.2
        
        # Plot X and Y axes (Real and Imaginary)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Plot the Ray
        # We plot from x=0 to x=limit_x to show the ray extending past the axis
        x_vals = np.linspace(0, limit_x, 100)
        y_vals = self.m * x_vals + self.y_start
        ax.plot(x_vals, y_vals, color='blue', linewidth=2, label=f'$arg(z - {self.y_start}i) = {self.latex_angle}$')
        
        # Plot Point A
        ax.plot(0, self.y_start, 'ro', zorder=5) # Red dot
        ax.text(0.2, self.y_start, f'$A(0, {self.y_start})$', fontsize=12, verticalalignment='bottom')
        
        # Plot the X-intercept (The solution point) - purely visual, optional to hide
        ax.plot(self.x_intercept, 0, 'go') 
        
        # Formatting the ComplexPlane
        ax.set_title("ComplexPlane Locus", fontsize=14)
        ax.set_xlabel("Re(z)", fontsize=12, loc='right')
        ax.set_ylabel("Im(z)", fontsize=12, loc='top')
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.set_aspect('equal') # Crucial for angles to look correct
        ax.legend(loc='upper right')
        
        # Remove standard ticks for a cleaner geometry-problem look, or keep them for reference
        # Here we keep them but ensure the view is centered roughly
        ax.set_xlim(-1, limit_x)
        ax.set_ylim(-1, limit_y)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
        
class Mat171:
    def __init__(self):
        # Varying forces using randrange_float with step 0.01
        self.force_horizontal = round(randrange_float(35.0, 55.0, 0.01), 2)
        self.force_vertical = round(randrange_float(25.0, 45.0, 0.01), 2)
        
        # Solving for X and theta for equilibrium
        # X = sqrt(H^2 + V^2)
        # theta = arctan(V/H)
        x_val = math.sqrt(self.force_horizontal**2 + self.force_vertical**2)
        theta_val = math.degrees(math.atan2(self.force_vertical, self.force_horizontal))
        
        # Answer is the magnitude X, rounded to 2 dp
        self.answer = round(x_val, 2)

        self.description = (
            "Three coplanar forces act at a point in the directions shown in the diagram. "
            "Given that the forces are in equilibrium, find the value of $X$."
        )
        
        self.topic = "Mechanics"
        self.subtopic = "Forces and equilibrium"
        self.source = "Adapted from AS & A level March 2025 Question Paper 42"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Resolving forces horizontally (}} \\sum F_x = 0 \\text{{):}} &\\\\"
            f"X \\cos \\theta - {self.force_horizontal} &= 0\\\\"
            f"X \\cos \\theta &= {self.force_horizontal} \\quad (1)\\\\"
            f"\\text{{Resolving forces vertically (}} \\sum F_y = 0 \\text{{):}} &\\\\"
            f"{self.force_vertical} - X \\sin \\theta &= 0\\\\"
            f"X \\sin \\theta &= {self.force_vertical} \\quad (2)\\\\"
            f"\\text{{Dividing equation (2) by (1) to find }} \\theta: &\\\\"
            f"\\frac{{X \\sin \\theta}}{{X \\cos \\theta}} &= \\frac{{{self.force_vertical}}}{{{self.force_horizontal}}}\\\\"
            f"\\tan \\theta &= {round(self.force_vertical / self.force_horizontal, 10)}\\\\"
            f"\\theta &= \\arctan({round(self.force_vertical / self.force_horizontal, 10)})\\\\"
            f"\\theta &= {round(theta_val, 2)}^\\circ\\\\"
            f"\\text{{Finding magnitude }} X \\text{{ using }} X = \\sqrt{{F_x^2 + F_y^2}}: &\\\\"
            f"X &= \\sqrt{{{self.force_horizontal}^2 + {self.force_vertical}^2}}\\\\"
            f"X &= \\sqrt{{{round(self.force_horizontal**2, 10)} + {round(self.force_vertical**2, 10)}}}\\\\"
            f"X &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.6, 1.6)
        ax.set_aspect('equal')
        ax.axis('off')

        origin = np.array([0, 0])
        
        # Proportional scaling: longest vector will be approx 1.3 units
        x_mag = math.sqrt(self.force_horizontal**2 + self.force_vertical**2)
        max_f = max(self.force_horizontal, self.force_vertical, x_mag)
        scale = 1.3 / max_f

        # Force 1: Horizontal to the left (length proportional to self.force_horizontal)
        len1 = self.force_horizontal * scale
        p1 = np.array([-len1, 0])
        ax.annotate('', xy=p1, xytext=origin, arrowprops=dict(arrowstyle='->', lw=2))
        ax.text(p1[0] - 0.1, p1[1], f"{self.force_horizontal} N", ha='right', va='center', fontsize=16)

        # Force 2: Vertical upwards (length proportional to self.force_vertical)
        len2 = self.force_vertical * scale
        p2 = np.array([0, len2])
        ax.annotate('', xy=p2, xytext=origin, arrowprops=dict(arrowstyle='->', lw=2))
        ax.text(p2[0], p2[1] + 0.1, f"{self.force_vertical} N", ha='center', va='bottom', fontsize=16)

        # Force 3: Vector X (length proportional to magnitude x_mag)
        len3 = x_mag * scale
        draw_theta = math.degrees(math.atan2(self.force_vertical, self.force_horizontal))
        rad_theta = np.radians(-draw_theta)
        p3 = np.array([len3 * np.cos(rad_theta), len3 * np.sin(rad_theta)])
        ax.annotate('', xy=p3, xytext=origin, arrowprops=dict(arrowstyle='->', lw=2))
        ax.text(p3[0] + 0.05, p3[1] - 0.05, "$X$ N", ha='left', va='top', fontsize=16)

        # Reference dotted line
        ax.plot([0, 1.3], [0, 0], color='black', linestyle='--', lw=1)
        
        # Right angle box
        rect = patches.Rectangle((-0.15, 0), 0.15, 0.15, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        # Angle arc
        arc = patches.Arc(origin, 0.6, 0.6, theta1=-draw_theta, theta2=0, color='black', lw=1)
        ax.add_patch(arc)
        
        # Theta label
        mid_angle = -draw_theta / 2
        tx = 0.45 * np.cos(np.radians(mid_angle))
        ty = 0.45 * np.sin(np.radians(mid_angle))
        ax.text(tx + 0.1, ty, "$\\theta^\\circ$", fontsize=16, va='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat172:
    def __init__(self):
        # Motion parameters
        # Stage 1: Accelerates from initial_v
        self.u1 = rnd.randint(4, 8) 
        self.a1 = round(randrange_float(0.4, 1.2, 0.05), 2)
        self.t1 = rnd.randint(15, 25)
        self.v_max = self.u1 + self.a1 * self.t1
        
        # Stage 2: Decelerates to zero
        self.t2_duration = rnd.randint(25, 35)
        self.t2_end = self.t1 + self.t2_duration
        self.a2 = -self.v_max / self.t2_duration
        
        # Area under graph Stage 1 + 2 (Distance from O)
        self.dist_out = 0.5 * (self.u1 + self.v_max) * self.t1 + 0.5 * self.v_max * self.t2_duration
        
        # Stage 3: Travel back to O
        # Particle reaches some negative velocity at t3_fixed, then slows to rest at T
        self.t3_fixed = self.t2_end + rnd.randint(8, 15)
        self.a3_accel = round(randrange_float(-1.5, -0.5, 0.1), 2)
        self.v_min = self.a3_accel * (self.t3_fixed - self.t2_end)
        
        # Distance Stage 3 (negative area) must equal dist_out to return to O
        # Area = 0.5 * base * height => Area = 0.5 * (T - t2_end) * v_min
        # Since area is negative and we want magnitude: dist_out = 0.5 * (T - t2_end) * abs(v_min)
        self.T_minus_t2 = (2 * self.dist_out) / abs(self.v_min)
        
        self.answer = self.t2_end + self.T_minus_t2

        self.description = (
            "The diagram shows a velocity-time graph which models the motion of a particle. "
            "The particle leaves $O$ and eventually returns to $O$ at time $T$. "
            "Based on the figure and the information provided, find the value of $T$."
        )
        
        self.topic = "Mechanics"
        self.subtopic = "Kinematics of motion in a straight line"
        self.source = "Adapted from AS & A level June 2025 Question Paper 43"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Distance traveled away from }} O \\text{{ (Area Stage 1 and 2):}} &\\\\"
            f"d_{{out}} &= \\text{{Area of trapezium}} + \\text{{Area of triangle}}\\\\"
            f"d_{{out}} &= \\frac{1}{2}(u_1 + v_{{max}})t_1 + \\frac{1}{2}(v_{{max}})(t_{{2,end}} - t_1)\\\\"
            f"d_{{out}} &= \\frac{1}{2}({self.u1} + {round(self.v_max, 10)})({self.t1}) + \\frac{1}{2}({round(self.v_max, 10)})({self.t2_duration})\\\\"
            f"d_{{out}} &= {round(self.dist_out, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{For the particle to return to }} O \\text{{, the area below the }} t\\text{{-axis must equal }} d_{{out}}: &\\\\"
            f"d_{{out}} &= \\text{{Area of triangle Stage 3}}\\\\"
            f"d_{{out}} &= \\frac{1}{2} \\times \\text{{base}} \\times |\\text{{height}}|\\\\"
            f"{round(self.dist_out, 10)} &= \\frac{1}{2} \\times (T - {self.t2_end}) \\times |{round(self.v_min, 10)}|\\\\"
            f"T - {self.t2_end} &= \\frac{{2 \\times {round(self.dist_out, 10)}}}{{{round(abs(self.v_min), 10)}}}\\\\"
            f"T - {self.t2_end} &= {round(self.T_minus_t2, 10)}\\\\"
            f"T &= {self.t2_end} + {round(self.T_minus_t2, 10)}\\\\"
            f"T &= {self.answer}\\,\\text{{s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # X and Y data points
        # (0, u1), (t1, v_max), (t2_end, 0), (t3_fixed, v_min), (answer, 0)
        t_pts = [0, self.t1, self.t2_end, self.t3_fixed, self.answer]
        v_pts = [self.u1, self.v_max, 0, self.v_min, 0]
        
        ax.plot(t_pts, v_pts, color='black', lw=2)
        
        # Axes
        ax.axhline(0, color='black', lw=1.5)
        ax.axvline(0, color='black', lw=1.5)
        
        # Limits
        ax.set_xlim(-5, self.answer * 1.1)
        ax.set_ylim(min(v_pts) - 5, max(v_pts) + 5)
        ax.axis('off')

        # Axis labels
        ax.text(self.answer * 1.1, 0, '$t$ (s)', ha='left', va='center', fontsize=12)
        ax.text(0, max(v_pts) + 5, '$v$ (m s$^{-1}$)', ha='center', va='bottom', fontsize=12)

        # Labels for points
        # Initial velocity
        ax.text(-1, self.u1, f"{self.u1}", ha='right', va='center', fontsize=11)
        
        # Time 20 (t1)
        ax.plot([self.t1, self.t1], [0, self.v_max], color='black', linestyle='--', lw=1)
        ax.text(self.t1, -1.5, f"{self.t1}", ha='center', va='top', fontsize=11)
        
        # Time 40 (t2_end)
        ax.text(self.t2_end - 1, 1.5, f"{self.t2_end}", ha='right', va='bottom', fontsize=11)
        
        # Time 50 (t3_fixed)
        ax.plot([self.t3_fixed, self.t3_fixed], [0, self.v_min], color='black', linestyle='--', lw=1)
        ax.text(self.t3_fixed, 1.5, f"{self.t3_fixed}", ha='center', va='bottom', fontsize=11)
        
        # Time T
        ax.text(self.answer, 1.5, '$T$', ha='center', va='bottom', fontsize=12)

        # Origin
        ax.text(-1.5, -1.5, '0', ha='right', va='top')

        # Context text in figure
        context_str = (
            f"Particle leaves $O$ at $t=0$ with $v={self.u1}$ m s$^{{-1}}$.\n"
            f"Accelerates at {self.a1} m s$^{{-2}}$ for {self.t1} s.\n"
            f"Decelerates to rest at $t={self.t2_end}$.\n"
            f"Returns to $O$ at time $T$."
        )
        plt.text(self.answer * 0.7, max(v_pts) * 0.8, context_str, fontsize=10, 
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='gray'))

        # Arrows for axes
        ax.annotate('', xy=(self.answer * 1.15, 0), xytext=(self.answer * 1.1, 0),
                    arrowprops=dict(arrowstyle='->', color='black'))
        ax.annotate('', xy=(0, max(v_pts) + 7), xytext=(0, max(v_pts) + 5),
                    arrowprops=dict(arrowstyle='->', color='black'))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat173:
    def __init__(self):
        # Varying numeric weights (masses) and speed by step 0.01 and rounding to 2
        self.mass_p = round(randrange_float(0.4, 0.8, 0.01), 2)
        self.mass_q = round(randrange_float(0.2, 0.5, 0.01), 2)
        self.mass_r = round(randrange_float(0.6, 1.0, 0.01), 2)
        
        self.speed_p_initial = round(randrange_float(2.0, 5.0, 0.01), 2)
        self.speed_p_after = round(randrange_float(0.5, 1.8, 0.01), 2)
        
        # Part (a): Find speed of Q after first collision (P and Q)
        # mP * uP + mQ * uQ = mP * vP + mQ * vQ
        # uQ = 0, so: vQ = (mP * uP - mP * vP) / mQ
        self.speed_q_after_1 = (self.mass_p * self.speed_p_initial - self.mass_p * self.speed_p_after) / self.mass_q
        
        # Part (b): Find speed of coalesced particle after second collision (Q and R)
        # mQ * vQ + mR * uR = (mQ + mR) * V
        # uR = 0, so: V = (mQ * vQ) / (mQ + mR)
        self.answer = (self.mass_q * self.speed_q_after_1) / (self.mass_q + self.mass_r)

        self.description = (
            "Three particles $P, Q$ and $R$ are at rest in a straight line on a smooth horizontal plane as shown in the figure. "
            "The mass of $P$ is $m_P$, $Q$ is $m_Q$, and $R$ is $m_R$. $P$ is projected directly towards $Q$ with an initial speed. "
            "After $P$ and $Q$ collide, $P$ continues to move in the same direction with a reduced speed. "
            "In the subsequent collision between $Q$ and $R$, these particles coalesce. "
            "Find the speed of the combined particle after this second collision."
        )
        
        self.topic = "Mechanics"
        self.subtopic = "Momentum"
        self.source = "Adapted from AS & A level March 2025 Question Paper 42"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Collision between }} P \\text{{ and }} Q: &\\\\"
            f"m_P u_P + m_Q u_Q &= m_P v_P + m_Q v_Q\\\\"
            f"({self.mass_p})({self.speed_p_initial}) + ({self.mass_q})(0) &= ({self.mass_p})({self.speed_p_after}) + ({self.mass_q})v_Q\\\\"
            f"{round(self.mass_p * self.speed_p_initial, 10)} &= {round(self.mass_p * self.speed_p_after, 10)} + {self.mass_q} v_Q\\\\"
            f"v_Q &= \\frac{{{round(self.mass_p * self.speed_p_initial - self.mass_p * self.speed_p_after, 10)}}}{{{self.mass_q}}}\\\\"
            f"v_Q &= {round(self.speed_q_after_1, 10)}\\,\\text{{m s}}^{{-1}}\\\\"
            f"\\text{{Collision between }} Q \\text{{ and }} R \\text{{ (coalescence):}} &\\\\"
            f"m_Q v_Q + m_R u_R &= (m_Q + m_R) V\\\\"
            f"({self.mass_q})({round(self.speed_q_after_1, 10)}) + ({self.mass_r})(0) &= ({self.mass_q} + {self.mass_r}) V\\\\"
            f"{round(self.mass_q * self.speed_q_after_1, 10)} &= {round(self.mass_q + self.mass_r, 10)} V\\\\"
            f"V &= \\frac{{{round(self.mass_q * self.speed_q_after_1, 10)}}}{{{round(self.mass_q + self.mass_r, 10)}}}\\\\"
            f"V &= {self.answer}\\,\\text{{m s}}^{{-1}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.set_xlim(-1, 9)
        ax.set_ylim(-1, 2)
        ax.set_aspect('equal')
        ax.axis('off')

        # Floor line
        ax.plot([-0.5, 8.5], [0, 0], color='black', lw=2)

        # Positions
        pos_p = 1
        pos_q = 4
        pos_r = 7

        # Draw particles as circles
        circle_p = patches.Circle((pos_p, 0.15), 0.15, color='black')
        circle_q = patches.Circle((pos_q, 0.15), 0.15, color='black')
        circle_r = patches.Circle((pos_r, 0.15), 0.15, color='black')
        ax.add_patch(circle_p)
        ax.add_patch(circle_q)
        ax.add_patch(circle_r)

        # Labels
        ax.text(pos_p, 0.45, f"$P$\n{self.mass_p} kg", ha='center', fontsize=12)
        ax.text(pos_q, 0.45, f"$Q$\n{self.mass_q} kg", ha='center', fontsize=12)
        ax.text(pos_r, 0.45, f"$R$\n{self.mass_r} kg", ha='center', fontsize=12)

        # Distance markings
        ax.annotate('', xy=(pos_p, -0.4), xytext=(pos_q, -0.4), arrowprops=dict(arrowstyle='<->'))
        ax.text((pos_p + pos_q)/2, -0.7, "3 m", ha='center', fontsize=10)
        
        ax.annotate('', xy=(pos_q, -0.4), xytext=(pos_r, -0.4), arrowprops=dict(arrowstyle='<->'))
        ax.text((pos_q + pos_r)/2, -0.7, "3 m", ha='center', fontsize=10)

        # Initial speed arrow for P
        ax.annotate('', xy=(pos_p + 0.8, 0.15), xytext=(pos_p + 0.2, 0.15), 
                    arrowprops=dict(arrowstyle='->', lw=1.5))
        ax.text(pos_p + 0.5, 0.7, f"{self.speed_p_initial} m s$^{{-1}}$", ha='center', fontsize=10)
        
        # Text for post-collision speed in diagram
        ax.text(4, 1.5, f"Speed of $P$ after collision: {self.speed_p_after} m s$^{{-1}}$", ha='center', fontsize=11, fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat174:
    def __init__(self):
        # Varying physical properties
        self.mass = round(randrange_float(8.0, 15.0, 0.01), 2)
        # alpha = tan^-1(slope). Using slope values between 0.3 and 0.7
        self.slope = round(randrange_float(0.3, 0.7, 0.01), 2)
        self.alpha_deg = math.degrees(math.atan(self.slope))
        
        self.force_up = round(randrange_float(15.0, 30.0, 0.01), 2)
        self.mu = round(randrange_float(0.1, 0.25, 0.01), 2)
        self.distance = round(randrange_float(1.5, 5.0, 0.01), 2)
        
        # Solving for time t
        g = 10
        rad = math.atan(self.slope)
        normal = self.mass * g * math.cos(rad)
        friction = self.mu * normal
        weight_parallel = self.mass * g * math.sin(rad)
        
        resultant_down = weight_parallel - friction - self.force_up
        acceleration = resultant_down / self.mass
        
        # Ensure acceleration is positive for downward motion from rest
        if acceleration <= 0:
            self.mass += 10.0
            normal = self.mass * g * math.cos(rad)
            friction = self.mu * normal
            weight_parallel = self.mass * g * math.sin(rad)
            resultant_down = weight_parallel - friction - self.force_up
            acceleration = resultant_down / self.mass
            
        # s = 0.5 * a * t^2 => t = sqrt(2s / a)
        self.answer = math.sqrt((2 * self.distance) / acceleration)

        self.description = (
            "Based on the figure, a block is placed on a rough plane inclined at an angle $\\alpha$ to the horizontal. "
            "A constant force is applied to the block directly up the plane. "
            "Find the time that it takes for the block to move from rest for the specified distance down the plane."
        )
        
        self.topic = "Mechanics"
        self.subtopic = "Newton’s laws of motion"
        self.source = "Adapted from AS & A level March 2025 Question Paper 42"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Normal force (}} R \\text{{) perpendicular to the plane:}} &\\\\"
            f"R &= m g \\cos \\alpha\\\\"
            f"&= {self.mass} \\times 10 \\times \\cos(\\arctan({self.slope}))\\\\"
            f"&= {round(self.mass * 10 * math.cos(math.atan(self.slope)), 10)}\\,\\text{{N}}\\\\"
            f"\\text{{Frictional force (}} F \\text{{) opposing the motion:}} &\\\\"
            f"F &= \\mu R\\\\"
            f"&= {self.mu} \\times {round(self.mass * 10 * math.cos(math.atan(self.slope)), 10)}\\\\"
            f"&= {round(self.mu * self.mass * 10 * math.cos(math.atan(self.slope)), 10)}\\,\\text{{N}}\\\\"
            f"\\text{{Net force down the plane:}} &\\\\"
            f"F_{{net}} &= m g \\sin \\alpha - F - F_{{up}}\\\\"
            f"&= ({self.mass} \\times 10 \\times \\sin(\\arctan({self.slope}))) - {round(self.mu * self.mass * 10 * math.cos(math.atan(self.slope)), 10)} - {self.force_up}\\\\"
            f"&= {round(self.mass * 10 * math.sin(math.atan(self.slope)) - (self.mu * self.mass * 10 * math.cos(math.atan(self.slope))) - self.force_up, 10)}\\,\\text{{N}}\\\\"
            f"\\text{{Acceleration (}} a \\text{{) down the plane:}} &\\\\"
            f"a &= \\frac{{F_{{net}}}}{{m}}\\\\"
            f"&= \\frac{{{round(self.mass * 10 * math.sin(math.atan(self.slope)) - (self.mu * self.mass * 10 * math.cos(math.atan(self.slope))) - self.force_up, 10)}}}{{{self.mass}}}\\\\"
            f"&= {round((self.mass * 10 * math.sin(math.atan(self.slope)) - (self.mu * self.mass * 10 * math.cos(math.atan(self.slope))) - self.force_up) / self.mass, 10)}\\,\\text{{m s}}^{{-2}}\\\\"
            f"\\text{{Using }} s = ut + \\frac{{1}}{{2}}at^2 \\text{{ where }} u = 0: &\\\\"
            f"t &= \\sqrt{{\\frac{{2s}}{{a}}}}\\\\"
            f"&= \\sqrt{{\\frac{{2 \\times {self.distance}}}{{{round((self.mass * 10 * math.sin(math.atan(self.slope)) - (self.mu * self.mass * 10 * math.cos(math.atan(self.slope))) - self.force_up) / self.mass, 10)}}}}}\\\\"
            f"&= {self.answer}\\,\\text{{s}}"
            "\\end{aligned}\\]"
    )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 8)
        ax.set_aspect('equal')
        ax.axis('off')

        angle_rad = math.atan(self.slope)
        
        # Inclined Plane
        p_start = np.array([0, 0])
        p_end = np.array([10, 10 * self.slope])
        ax.plot([p_start[0], p_end[0]], [p_start[1], p_end[1]], color='black', lw=2)
        ax.plot([0, 3], [0, 0], color='black', linestyle='--', lw=1)
        
        # Angle alpha arc and label
        arc = patches.Arc((0, 0), 2, 2, theta1=0, theta2=math.degrees(angle_rad), color='black')
        ax.add_patch(arc)
        ax.text(1.2, 0.3, r"$\alpha$", fontsize=18)

        # Block
        b_width = randrange_float(1.5, 2.5, 0.1)
        b_height = b_width * 0.6
        c_dist = 6
        block_center = np.array([c_dist * math.cos(angle_rad), c_dist * math.sin(angle_rad)])
        
        rot = np.array([[math.cos(angle_rad), -math.sin(angle_rad)], 
                        [math.sin(angle_rad), math.cos(angle_rad)]])
        
        corners = np.array([[-b_width/2, 0], [b_width/2, 0], [b_width/2, b_height], [-b_width/2, b_height]])
        block_pts = np.dot(corners, rot.T) + block_center
        poly = plt.Polygon(block_pts, closed=True, facecolor='lightgray', edgecolor='black', lw=1.5)
        ax.add_patch(poly)

        # Labels on block
        ax.text(block_center[0] - 0.5 * math.sin(angle_rad), 
                block_center[1] + (b_height + 0.3) * math.cos(angle_rad), 
                f"{self.mass} kg", fontsize=14, ha='center')

        # Upward Force Arrow
        arrow_start = block_center + np.dot(np.array([b_width/2, b_height/2]), rot.T)
        arrow_end = arrow_start + np.dot(np.array([2, 0]), rot.T)
        ax.annotate('', xy=arrow_end, xytext=arrow_start, 
                    arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
        ax.text(arrow_end[0] + 0.2, arrow_end[1], f"{self.force_up} N", fontsize=14)

        # Variable Info (Bottom Right for clarity)
        info_text = (
            f"$\\alpha = \\tan^{{-1}}({self.slope})$\n"
            f"$\\mu = {self.mu}$\n"
            f"Distance to move: {self.distance} m"
        )
        ax.text(9.5, 0.5, info_text, fontsize=13, ha='right', va='bottom', 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat175:
    def __init__(self):
        # Setup randomized parameters for Section AB
        self.mass = rnd.randint(65, 85) 
        self.l_ab = randrange_float(4.5, 6.5, 0.1) 
        self.sin_theta = round(randrange_float(0.6, 0.85, 0.05), 2)
        self.mu = round(randrange_float(0.08, 0.15, 0.01), 2)
        self.g = 10 # G value standard for A-level mechanics

        # Derived physics values
        self.theta_rad = math.asin(self.sin_theta)
        self.cos_theta = math.cos(self.theta_rad)
        
        # Energy calculation at B
        # KE_B = PE_gain_AB - Work_friction_AB
        v_b_sq = 2 * self.g * self.l_ab * (self.sin_theta - self.mu * self.cos_theta)
        self.v_b = math.sqrt(max(0.1, v_b_sq))

        # Setup randomized parameters for Section BC
        self.h_bc = randrange_float(2.0, 3.0, 0.1) 
        # Theoretical speed at C if frictionless
        v_c_ideal = math.sqrt(v_b_sq + 2 * self.g * self.h_bc)
        # Define real speed at C to force positive work done against resistance
        self.v_c = round(v_c_ideal - randrange_float(0.8, 1.4, 0.1), 1)
        
        # Energy balance for Work Done against resistance (B to C)
        # Total Energy at B = KE_B + PE_B = 0.5*m*v_B^2 + m*g*h_BC
        # Total Energy at C = KE_C = 0.5*m*v_C^2
        # Work Done = E_B - E_C
        ke_b = 0.5 * self.mass * v_b_sq
        pe_b = self.mass * self.g * self.h_bc
        ke_c = 0.5 * self.mass * (self.v_c**2)
        
        self.answer = ke_b + pe_b - ke_c

        self.description = (
            "The diagram shows the vertical cross-section $ABC$ of a rough waterslide. "
            "A man modeled as a particle slides down from rest at $A$. "
            "Based on the information provided in the figure, find the work done against "
            "the resistance force as the man moves from $B$ to $C$."
        )
        
        self.topic = "Mechanics"
        self.subtopic = "Energy, work and power"
        self.source = "Adapted from AS & A level June 2025 Question Paper 43"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{1. Motion from }} A \\text{{ to }} B: & \\\\"
            f"\\text{{Initial energy at }} A \\text{{ is purely potential energy:}} & \\\\"
            f"PE_A &= mgh_{{AB}} = mg(L_{{AB}} \\sin \\theta) \\\\"
            f"&= {self.mass} \\times {self.g} \\times ({self.l_ab} \\times {self.sin_theta}) \\\\"
            f"&= {round(self.mass * self.g * self.l_ab * self.sin_theta, 10)}\\,\\text{{J}} \\\\"
            f"\\text{{Work done against friction on section }} AB: & \\\\"
            f"WD_{{f}} &= \\mu R L_{{AB}} = \\mu (mg \\cos \\theta) L_{{AB}} \\\\"
            f"\\cos \\theta &= \\sqrt{{1 - \\sin^2 \\theta}} = \\sqrt{{1 - {self.sin_theta}^2}} = {round(self.cos_theta, 10)} \\\\"
            f"WD_{{f}} &= {self.mu} \\times ({self.mass} \\times {self.g} \\times {round(self.cos_theta, 10)}) \\times {self.l_ab} \\\\"
            f"&= {round(self.mu * self.mass * self.g * self.cos_theta * self.l_ab, 10)}\\,\\text{{J}} \\\\"
            f"\\text{{Using the work-energy principle for }} AB: & \\\\"
            f"KE_B &= PE_A - WD_{{f}} \\\\"
            f"&= {round(self.mass * self.g * self.l_ab * self.sin_theta, 10)} - {round(self.mu * self.mass * self.g * self.cos_theta * self.l_ab, 10)} \\\\"
            f"&= {round(0.5 * self.mass * (self.v_b**2), 10)}\\,\\text{{J}} \\\\"
            f"\\text{{2. Motion from }} B \\text{{ to }} C: & \\\\"
            f"\\text{{Total energy at }} B \\text{{ (Kinetic + Potential relative to }} C\\text{{):}} & \\\\"
            f"E_B &= KE_B + mgh_{{BC}} \\\\"
            f"&= {round(0.5 * self.mass * (self.v_b**2), 10)} + ({self.mass} \\times {self.g} \\times {self.h_bc}) \\\\"
            f"&= {round(0.5 * self.mass * (self.v_b**2) + self.mass * self.g * self.h_bc, 10)}\\,\\text{{J}} \\\\"
            f"\\text{{Kinetic energy at }} C: & \\\\"
            f"KE_C &= \\frac{{1}}{{2}} m v_C^2 = 0.5 \\times {self.mass} \\times {self.v_c}^2 \\\\"
            f"&= {round(0.5 * self.mass * (self.v_c**2), 10)}\\,\\text{{J}} \\\\"
            f"\\text{{Work done against resistance from }} B \\text{{ to }} C: & \\\\"
            f"WD_{{res}} &= E_B - KE_C \\\\"
            f"&= {round(0.5 * self.mass * (self.v_b**2) + self.mass * self.g * self.h_bc, 10)} - {round(0.5 * self.mass * (self.v_c**2), 10)} \\\\"
            f"&= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_aspect('equal')
        ax.axis('off')

        # Coordinates for plotting
        x_b, y_b = 0, self.h_bc
        x_a = -self.l_ab * self.cos_theta
        y_a = self.h_bc + self.l_ab * self.sin_theta
        x_c, y_c = 4.0, 0 
        
        # Draw the waterslide paths
        ax.plot([x_a, x_b], [y_a, y_b], color='black', lw=3) # Section AB (Straight)
        t = np.linspace(0, 1, 100)
        curve_x = x_b + t * (x_c - x_b)
        curve_y = y_b * (1 - t)**1.8 # Quadratic-style descent
        ax.plot(curve_x, curve_y, color='black', lw=3) # Section BC (Curve)

        # Baseline horizontal markers
        ax.plot([x_b - 2.5, x_b], [y_b, y_b], color='gray', linestyle='--', lw=1)
        ax.plot([x_b - 2.5, x_c + 0.5], [y_c, y_c], color='gray', linestyle='--', lw=1)

        # Labels for points
        ax.text(x_a - 0.3, y_a + 0.3, 'A', fontsize=16, fontweight='bold')
        ax.text(x_b + 0.1, y_b + 0.2, 'B', fontsize=16, fontweight='bold')
        ax.text(x_c + 0.2, y_c + 0.2, 'C', fontsize=16, fontweight='bold')

        # Dimensioning: AB section length
        off = 0.6
        dx, dy = off * self.sin_theta, off * self.cos_theta
        ax.annotate('', xy=(x_a + dx, y_a + dy), xytext=(x_b + dx, y_b + dy),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text((x_a + x_b)/2 + dx + 0.1, (y_a + y_b)/2 + dy + 0.1, f"{self.l_ab:.1f} m", 
                rotation=math.degrees(self.theta_rad), ha='left', va='bottom', fontsize=12)

        # Dimensioning: BC vertical height
        ax.annotate('', xy=(x_b - 1.8, y_b), xytext=(x_b - 1.8, y_c),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text(x_b - 1.9, (y_b + y_c)/2, f"{self.h_bc:.1f} m", ha='right', va='center', fontsize=12)

        # Fix the angle mark arc (theta)
        arc_r = 0.8
        angle_deg = math.degrees(self.theta_rad)
        # Draw arc from line BA (180 - theta) to the horizontal (180)
        arc = patches.Arc((x_b, y_b), arc_r*2, arc_r*2, theta1=180 - angle_deg, theta2=180, color='black', lw=1.5)
        ax.add_patch(arc)
        # Place label theta at the center of the arc span
        mid_angle = 180 - (angle_deg / 2)
        lx = x_b + (arc_r + 0.4) * math.cos(math.radians(mid_angle))
        ly = y_b + (arc_r + 0.4) * math.sin(math.radians(mid_angle))
        ax.text(lx, ly, r"$\theta$", fontsize=15, ha='center', va='center')

        # Floating info box for parameters
        info_text = (
            f"Given Information:\n"
            f"• Mass of man: {self.mass} kg\n"
            f"• $\\sin \\theta = {self.sin_theta:.2f}$\n"
            f"• Friction on AB: $\\mu = {self.mu:.2f}$\n"
            f"• Speed at C: $v_C = {self.v_c}$ m s$^{{-1}}$\n"
            f"• Starts from rest at A"
        )
        ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=12,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.9))

        # Adjust axes to ensure no cutoff
        ax.set_xlim(x_a - 2.0, x_c + 2.0)
        ax.set_ylim(y_c - 1.5, y_a + 2.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat176:
    def __init__(self):
        # Configuration: Randomize the range of scores by shifting the start stem
        start_stem = rnd.randint(3, 5)
        self.stems = [start_stem + i for i in range(4)]
        
        self.data_a = []
        self.data_b = []
        self.leaves_a = {s: [] for s in self.stems}
        self.leaves_b = {s: [] for s in self.stems}
        
        # Populate data for each class across all stems
        for s in self.stems:
            num_items_a = rnd.randint(3, 5)
            num_items_b = rnd.randint(3, 5)
            for _ in range(num_items_a):
                leaf = rnd.randint(0, 9)
                self.data_a.append(s * 10 + leaf)
                self.leaves_a[s].append(leaf)
            for _ in range(num_items_b):
                leaf = rnd.randint(0, 9)
                self.data_b.append(s * 10 + leaf)
                self.leaves_b[s].append(leaf)
        
        # Sort leaves for display: Class A leaves grow left (descending), Class B right (ascending)
        for s in self.stems:
            self.leaves_a[s].sort(reverse=True)
            self.leaves_b[s].sort()
            
        # Calculate medians using numpy
        med_a = float(np.median(self.data_a))
        med_b = float(np.median(self.data_b))
        
        # Must properties
        self.answer = abs(med_b - med_a)
        self.description = (
            "The back-to-back stem-and-leaf diagram shows the test scores of students in Class A and Class B. "
            "Based on the figure, calculate the positive difference between the median score of Class B and the median score of Class A."
        )
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Representation of data"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Ordered data for Class A:}} &= {sorted(self.data_a)}\\\\"
            f"\\text{{Number of items in Class A (}} n_A \\text{{):}} &= {len(self.data_a)}\\\\"
            f"\\text{{Median of Class A (}} M_A \\text{{):}} &= {round(float(np.median(self.data_a)), 10)}\\\\"
            f"\\text{{Ordered data for Class B:}} &= {sorted(self.data_b)}\\\\"
            f"\\text{{Number of items in Class B (}} n_B \\text{{):}} &= {len(self.data_b)}\\\\"
            f"\\text{{Median of Class B (}} M_B \\text{{):}} &= {round(float(np.median(self.data_b)), 10)}\\\\"
            f"\\text{{Positive difference}} &= |M_B - M_A|\\\\"
            f"&= |{round(float(np.median(self.data_b)), 10)} - {round(float(np.median(self.data_a)), 10)}|\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.set_xlim(-6, 6)
        ax.set_ylim(-1.5, len(self.stems) + 2)
        ax.axis('off')

        # Draw Headers
        y_head = len(self.stems) + 0.8
        ax.text(-2.5, y_head, "Class A", fontsize=22, ha='center', weight='bold')
        ax.text(0, y_head, "Stem", fontsize=22, ha='center', weight='bold')
        ax.text(2.5, y_head, "Class B", fontsize=22, ha='center', weight='bold')

        # Draw Vertical Separators
        ax.plot([-0.8, -0.8], [0.3, y_head - 0.2], color='black', lw=2)
        ax.plot([0.8, 0.8], [0.3, y_head - 0.2], color='black', lw=2)

        # Plot Stems and Leaves
        for i, s in enumerate(reversed(self.stems)):
            y_pos = i + 1
            # Center Stem
            ax.text(0, y_pos, str(s), fontsize=20, ha='center', weight='bold')
            
            # Class A Leaves (Growing Left)
            l_a_str = "  ".join(map(str, self.leaves_a[s]))
            ax.text(-1.1, y_pos, l_a_str, fontsize=18, ha='right')
            
            # Class B Leaves (Growing Right)
            l_b_str = "  ".join(map(str, self.leaves_b[s]))
            ax.text(1.1, y_pos, l_b_str, fontsize=18, ha='left')

        # Draw Key
        sample_s = self.stems[1]
        sample_la = self.leaves_a[sample_s][0]
        sample_lb = self.leaves_b[sample_s][0]
        key_text = (
            f"Key: {sample_la} | {sample_s} | {sample_lb} means a score of "
            f"{sample_s*10 + sample_la} for Class A and {sample_s*10 + sample_lb} for Class B"
        )
        ax.text(0, -0.8, key_text, fontsize=16, ha='center', style='italic',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black'))

        # Save result
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat177:
    def __init__(self):
        # Generate base values for the box plot
        # Using randrange_float for variation as requested
        self.q1 = round(randrange_float(15, 20, 0.01), 2)
        self.median = round(self.q1 + randrange_float(5, 10, 0.01), 2)
        self.q3 = round(self.median + randrange_float(5, 10, 0.01), 2)
        
        # Calculate IQR
        self.iqr = round(self.q3 - self.q1, 2)
        
        # Determine the upper boundary for outliers based on subsection 5.1 rules
        # Criterion: Outlier > Q3 + 1.5 * IQR
        self.answer = round(self.q3 + 1.5 * self.iqr, 2)

        # Plot boundary limits
        self.min_val = round(self.q1 - randrange_float(3, 8, 0.01), 2)
        self.max_val = round(self.q3 + randrange_float(3, 8, 0.01), 2)

        self.description = (
            "The box-and-whisker plot summarizes the heights of a specific plant species. "
            "Based on the figure, calculate the minimum numerical value a plant height must reach "
            "to be considered an outlier according to the standard $Q_3 + 1.5 \\times (IQR)$ criterion."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Representation of data"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Upper Quartile (}} Q_3 \\text{{)}} &= {round(self.q3, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Lower Quartile (}} Q_1 \\text{{)}} &= {round(self.q1, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Interquartile Range (IQR)}} &= Q_3 - Q_1\\\\"
            f"&= {round(self.q3, 10)} - {round(self.q1, 10)}\\\\"
            f"&= {round(self.iqr, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{The upper boundary for outliers is defined as:}} &\\\\"
            f"\\text{{Boundary}} &= Q_3 + 1.5 \\times IQR\\\\"
            f"&= {round(self.q3, 10)} + 1.5 \\times ({round(self.iqr, 10)})\\\\"
            f"&= {round(self.q3, 10)} + {round(1.5 * self.iqr, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 4))
        
        # Plot styling
        ax.set_ylim(0, 1)
        ax.set_xlim(math.floor(self.min_val - 2), math.ceil(self.max_val + 2))
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Draw Box (Q1 to Q3)
        box_height = 0.4
        box_bottom = 0.3
        box = patches.Rectangle((self.q1, box_bottom), self.iqr, box_height, linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(box)
        
        # Draw Median line
        ax.plot([self.median, self.median], [box_bottom, box_bottom + box_height], color='black', lw=3)
        
        # Draw Whiskers
        ax.plot([self.min_val, self.q1], [0.5, 0.5], color='black', lw=1.5)
        ax.plot([self.q3, self.max_val], [0.5, 0.5], color='black', lw=1.5)
        
        # Draw Whisker caps
        cap_size = 0.1
        ax.plot([self.min_val, self.min_val], [0.5 - cap_size, 0.5 + cap_size], color='black', lw=2)
        ax.plot([self.max_val, self.max_val], [0.5 - cap_size, 0.5 + cap_size], color='black', lw=2)
        
        # Add numeric labels at the key points
        label_y = 0.8
        points = [
            (self.min_val, "Min"),
            (self.q1, "$Q_1$"),
            (self.median, "Med"),
            (self.q3, "$Q_3$"),
            (self.max_val, "Max")
        ]
        
        for val, label in points:
            ax.text(val, label_y, f"{val}", ha='center', fontsize=12, fontweight='bold')
            ax.plot([val, val], [0.75, 0.55 if val in [self.min_val, self.max_val] else 0.7], color='gray', linestyle='--', alpha=0.5)

        ax.set_xlabel("Height (cm)", fontsize=14, labelpad=15)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat178:
    def __init__(self):
        # Configuration for data distribution
        self.total_students = rnd.choice([100, 200, 400, 500])
        self.percentile_rank = rnd.choice([25, 65, 75, 80, 90])
        
        # Define sigmoid-like points for cumulative frequency curve
        # x: time in minutes, y: percentage of total students
        self.t_min = round(randrange_float(10, 20, 0.01), 2)
        self.t_mid1 = round(self.t_min + randrange_float(15, 25, 0.01), 2)
        self.t_mid2 = round(self.t_mid1 + randrange_float(15, 25, 0.01), 2)
        self.t_max = round(self.t_mid2 + randrange_float(15, 25, 0.01), 2)
        
        # Cumulative frequencies at these points
        self.cf_points = [
            (self.t_min, 0),
            (self.t_mid1, 0.2 * self.total_students),
            (self.t_mid2, 0.8 * self.total_students),
            (self.t_max, self.total_students)
        ]
        
        # Interpolation logic for the specific percentile
        target_cf = (self.percentile_rank / 100) * self.total_students
        
        # Simple linear interpolation between the sigmoid anchor points for the answer
        if target_cf <= self.cf_points[1][1]:
            # Between t_min and t_mid1
            p0, p1 = self.cf_points[0], self.cf_points[1]
        elif target_cf <= self.cf_points[2][1]:
            # Between t_mid1 and t_mid2
            p0, p1 = self.cf_points[1], self.cf_points[2]
        else:
            # Between t_mid2 and t_max
            p0, p1 = self.cf_points[2], self.cf_points[3]
            
        # Linear interpolation formula: x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
        self.answer = round(p0[0] + (target_cf - p0[1]) * (p1[0] - p0[0]) / (p1[1] - p0[1]), 2)

        self.description = (
            f"The cumulative frequency graph displays the time spent by {self.total_students} students on a homework assignment. "
            f"Based on the figure, estimate the {self.percentile_rank}th percentile time for this distribution."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Representation of data"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total frequency (}} n \\text{{)}} &= {self.total_students} \\\\"
            f"\\text{{Target percentile}} &= {self.percentile_rank}\\text{{th}} \\\\"
            f"\\text{{Cumulative frequency value (}} CF \\text{{)}} &= \\frac{{{self.percentile_rank}}}{{100}} \\times {self.total_students} \\\\"
            f"&= {round((self.percentile_rank / 100) * self.total_students, 10)} \\\\"
            f"\\text{{From the graph, this }} CF \\text{{ falls between the points }} ({p0[0]}, {int(p0[1])}) \\text{{ and }} ({p1[0]}, {int(p1[1])}). \\\\"
            f"\\text{{Using linear interpolation:}} & \\\\"
            f"x &= x_0 + (CF - y_0) \\times \\frac{p1[0] - p0[0]}{p1[1] - p0[1]} \\\\"
            f"&= {round(p0[0], 10)} + ({round((self.percentile_rank / 100) * self.total_students, 10)} - {int(p0[1])}) \\times \\frac{{{round(p1[0], 10)} - {round(p0[0], 10)}}}{{{int(p1[1])} - {int(p0[1])}}} \\\\"
            f"&= {round(p0[0], 10)} + {round((self.percentile_rank / 100) * self.total_students - p0[1], 10)} \\times \\frac{{{round(p1[0] - p0[0], 10)}}}{{{int(p1[1] - p0[1])}}} \\\\"
            f"&= {self.answer}\\,\\text{{minutes}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create a smooth curve through the anchor points
        x_anchor = [p[0] for p in self.cf_points]
        y_anchor = [p[1] for p in self.cf_points]
        
        from scipy.interpolate import interp1d
        f = interp1d(x_anchor, y_anchor, kind='quadratic', bounds_error=False, fill_value=(0, self.total_students))
        x_smooth = np.linspace(self.t_min, self.t_max, 200)
        y_smooth = np.clip(f(x_smooth), 0, self.total_students)
        
        # Plot the cumulative frequency curve
        ax.plot(x_smooth, y_smooth, color='black', lw=2.5)
        
        # Grid and Axes
        ax.set_xlabel("Time (minutes)", fontsize=14)
        ax.set_ylabel("Cumulative Frequency", fontsize=14)
        ax.set_xlim(0, math.ceil(self.t_max / 10) * 10 + 10)
        ax.set_ylim(0, self.total_students + (0.1 * self.total_students))
        
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.yaxis.set_major_locator(MultipleLocator(self.total_students / 10))
        ax.grid(True, which='major', linestyle='--', alpha=0.6)
        
        # Explicit data labels to make the graph "necessary" and solveable
        # Marking the specific points clearly
        for x, y in self.cf_points:
            ax.plot(x, y, 'ko', markersize=4)
            ax.text(x, y + (0.02 * self.total_students), f"({x}, {int(y)})", fontsize=10, ha='center')

        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat179:
    def __init__(self):
        # Configuration: Randomize distribution of parcels with varying class widths
        self.total_n = rnd.choice([80, 100, 120, 150, 160, 200, 240, 300])
        
        # Define 4 class intervals with varying unequal widths
        self.w1 = rnd.randint(3, 6)
        self.w2 = self.w1 + rnd.randint(5, 10)
        self.w3 = self.w2 + rnd.randint(8, 15)
        self.w4 = self.w3 + rnd.randint(15, 30)
        
        # Randomize frequency densities for the first three bars
        self.fd1 = round(randrange_float(1.50, 5.00, 0.01), 2)
        self.fd2 = round(randrange_float(5.00, 10.00, 0.01), 2)
        self.fd3 = round(randrange_float(0.50, 3.00, 0.01), 2)
        
        # Calculate frequencies: Frequency = Frequency Density * Class Width
        f1 = self.fd1 * self.w1
        f2 = self.fd2 * (self.w2 - self.w1)
        f3 = self.fd3 * (self.w3 - self.w2)
        
        # Ensure deterministic logic: if current sum exceeds total_n, adjust total_n
        current_sum = f1 + f2 + f3
        if current_sum >= self.total_n - 5:
            self.total_n = math.ceil(current_sum + rnd.randint(20, 50))
            
        remaining_f = self.total_n - current_sum
        
        # The answer is the frequency density of the final class interval
        self.answer = round(remaining_f / (self.w4 - self.w3), 2)

        self.description = (
            f"The histogram illustrates the distribution of masses for a set of {self.total_n} parcels in a delivery warehouse. "
            f"Based on the figure, calculate the frequency density of the final class interval."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Representation of data"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total number of parcels }} (N) &= {self.total_n}\\\\"
            "\\text{The frequency of each class is calculated as: } &\\\\"
            "\\text{Frequency} &= \\text{Frequency Density} \\times \\text{Class Width}\\\\"
            f"\\text{{Frequency of class 1:}} &= {round(self.fd1, 10)} \\times {self.w1} = {round(self.fd1 * self.w1, 10)}\\\\"
            f"\\text{{Frequency of class 2:}} &= {round(self.fd2, 10)} \\times ({self.w2} - {self.w1}) = {round(self.fd2 * (self.w2 - self.w1), 10)}\\\\"
            f"\\text{{Frequency of class 3:}} &= {round(self.fd3, 10)} \\times ({self.w3} - {self.w2}) = {round(self.fd3 * (self.w3 - self.w2), 10)}\\\\"
            f"\\text{{Remaining frequency for the final class:}} &= N - (f_1 + f_2 + f_3)\\\\"
            f"&= {self.total_n} - ({round(self.fd1 * self.w1 + self.fd2 * (self.w2 - self.w1) + self.fd3 * (self.w3 - self.w2), 10)})\\\\"
            f"&= {round(self.total_n - (self.fd1 * self.w1 + self.fd2 * (self.w2 - self.w1) + self.fd3 * (self.w3 - self.w2)), 10)}\\\\"
            f"\\text{{Final class width}} &= {self.w4} - {self.w3} = {self.w4 - self.w3}\\\\"
            "\\text{Frequency density of the final class } (x) &= \\frac{\\text{Remaining Frequency}}{\\text{Class Width}}\\\\"
            f"x &= \\frac{{{round(self.total_n - (self.fd1 * self.w1 + self.fd2 * (self.w2 - self.w1) + self.fd3 * (self.w3 - self.w2)), 10)}}}{{{self.w4 - self.w3}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Define the bars
        intervals = [0, self.w1, self.w2, self.w3, self.w4]
        densities = [self.fd1, self.fd2, self.fd3, self.answer]
        
        # Draw the histogram bars
        for i in range(len(densities)):
            width = intervals[i+1] - intervals[i]
            rect = patches.Rectangle((intervals[i], 0), width, densities[i], 
                                     linewidth=2.5, edgecolor='black', facecolor='whitesmoke', alpha=0.8)
            ax.add_patch(rect)
            
        # Plot limits
        ax.set_xlim(0, math.ceil(self.w4 * 1.05))
        ax.set_ylim(0, math.ceil(max(densities) * 1.2))
        ax.set_xlabel("Mass ($m$ in kg)", fontsize=16)
        ax.set_ylabel("Frequency Density", fontsize=16)
        
        # Major ticks every 10 units
        ax.xaxis.set_major_locator(MultipleLocator(10))
        # Minor ticks every 1 unit (makes boundaries like 21 or 46 readable)
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        
        ax.yaxis.set_major_locator(MultipleLocator(2))
        
        # Enable major and minor grids
        ax.grid(True, which='major', linestyle='-', color='lightgray', alpha=0.7)
        ax.grid(True, which='minor', linestyle=':', color='gray', alpha=0.3)
        # ---------------------------
        
        # Labels for the first three bars
        for i in range(len(densities) - 1):
            ax.text(intervals[i] + (intervals[i+1]-intervals[i])/2, densities[i] + 0.2, 
                    f"{densities[i]}", ha='center', fontsize=14, weight='bold')
        
        # Visual cue for the question target
        ax.text(self.w3 + (self.w4 - self.w3)/2, self.answer + 0.2, "$x$", 
                ha='center', fontsize=22, weight='bold', color='darkblue')

        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat180:
    def __init__(self):
        # Configuration: total chairs (n) and the pair of twins
        self.total_students = rnd.randint(5, 15)
        
        # Calculate permutations: Total - Together
        # Total permutations = n!
        # Together permutations = (n-1)! * 2! (treat twins as one block)
        total_p = math.factorial(self.total_students)
        together_p = math.factorial(self.total_students - 1) * 2
        
        self.answer = total_p - together_p

        self.description = (
            f"A group of students is to be seated in the row of chairs shown in the figure. "
            f"Among the students is a pair of twins who must not sit next to each other. "
            f"Find the total number of different ways all the students can be seated such that the twins are separated."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Permutations and combinations"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total number of students, }} n &= {self.total_students}\\\\"
            "\\text{{Total ways to arrange all students without restriction:}} &\\\\"
            "P_{\\text{total}} &= n!\\\\"
            f"&= {self.total_students}!\\\\"
            f"&= {math.factorial(self.total_students)}\\\\"
            "\\text{{Ways to arrange students where the twins sit together:}} &\\\\"
            "\\text{{Treat the twins as 1 unit; total units to arrange}} &= (n - 1)\\\\"
            "P_{\\text{together}} &= (n - 1)! \\times 2!\\\\"
            f"&= ({self.total_students} - 1)! \\times 2\\\\"
            f"&= {math.factorial(self.total_students - 1)} \\times 2\\\\"
            f"&= {math.factorial(self.total_students - 1) * 2}\\\\"
            "\\text{{Ways where the twins are separated:}} &\\\\"
            "P_{\\text{separated}} &= P_{\\text{total}} - P_{\\text{together}}\\\\"
            f"&= {math.factorial(self.total_students)} - {math.factorial(self.total_students - 1) * 2}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Create a visualization of a row of chairs
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.set_xlim(-1, self.total_students)
        ax.set_ylim(-1, 2)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw chairs as simple square patches with a backrest
        for i in range(self.total_students):
            # Seat
            seat = patches.Rectangle((i - 0.4, 0), 0.8, 0.6, linewidth=2, edgecolor='black', facecolor='none')
            ax.add_patch(seat)
            # Backrest
            back = patches.Rectangle((i - 0.4, 0.6), 0.8, 0.4, linewidth=2, edgecolor='black', facecolor='none')
            ax.add_patch(back)
            # Chair Numbering
            ax.text(i, -0.5, str(i + 1), fontsize=14, ha='center', va='center', fontweight='bold')

        # Add a title label for context
        ax.text((self.total_students - 1) / 2, 1.5, f"Assembly Seating: {self.total_students} Students", 
                fontsize=18, ha='center', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat181:
    def __init__(self):
        # Configuration for group sizes to ensure variations
        self.num_women = rnd.randint(6, 12)
        self.num_men = rnd.randint(5, 10)
        
        # Committee requirements
        self.req_women = rnd.randint(2, 4)
        self.req_men = rnd.randint(2, 4)
        
        # Calculate combinations using nCr = n! / (r! * (n-r)!)
        comb_women = math.comb(self.num_women, self.req_women)
        comb_men = math.comb(self.num_men, self.req_men)
        
        self.answer = comb_women * comb_men

        self.description = (
            f"A committee is to be chosen from the group of people shown in the figure. "
            f"The committee must consist of exactly {self.req_women} women and {self.req_men} men. "
            f"Determine the number of different ways this committee can be selected."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Permutations and combinations"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Number of women available, }} n_w &= {self.num_women} \\\\"
            f"\\text{{Number of men available, }} n_m &= {self.num_men} \\\\"
            f"\\text{{Requirement: }} r_w &= {self.req_women} \\text{{ women and }} r_m = {self.req_men} \\text{{ men}} \\\\"
            "\\text{{Ways to select the women:}} & \\\\"
            "\\binom{n_w}{r_w} &= \\frac{n_w!}{r_w!(n_w - r_w)!} \\\\"
            f"&= \\binom{{{self.num_women}}}{{{self.req_women}}} \\\\"
            f"&= {math.comb(self.num_women, self.req_women)} \\\\"
            "\\text{{Ways to select the men:}} & \\\\"
            "\\binom{n_m}{r_m} &= \\frac{n_m!}{r_m!(n_m - r_m)!} \\\\"
            f"&= \\binom{{{self.num_men}}}{{{self.req_men}}} \\\\"
            f"&= {math.comb(self.num_men, self.req_men)} \\\\"
            "\\text{{Total number of ways:}} & \\\\"
            "\\text{{Total}} &= \\binom{n_w}{r_w} \\times \\binom{n_m}{r_m} \\\\"
            f"&= {math.comb(self.num_women, self.req_women)} \\times {math.comb(self.num_men, self.req_men)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Organized jittered layout
        fig, ax = plt.subplots(figsize=(10, 8))
        total_people = self.num_women + self.num_men
        cols = 6
        rows = math.ceil(total_people / cols)
        
        ax.set_xlim(-0.5, cols)
        ax.set_ylim(-1, rows)
        ax.set_aspect('equal')
        ax.axis('off')

        def draw_stickman(x, y, color):
            # Head
            head = plt.Circle((x, y + 0.5), 0.12, color=color, fill=True)
            ax.add_artist(head)
            # Body
            ax.plot([x, x], [y + 0.15, y + 0.38], color=color, lw=2.5)
            # Arms
            ax.plot([x - 0.15, x, x + 0.15], [y + 0.25, y + 0.35, y + 0.25], color=color, lw=2.5)
            # Legs
            ax.plot([x - 0.12, x, x + 0.12], [y, y + 0.15, y], color=color, lw=2.5)

        # Prepare population
        people = [('lightpink', 'Woman')] * self.num_women + [('lightskyblue', 'Man')] * self.num_men
        rnd.shuffle(people)

        # Draw in a grid with organization + randomness
        for i, (color, _) in enumerate(people):
            r = i // cols
            c = i % cols
            # Add jitter for "random but organized" look
            jx = rnd.uniform(-0.2, 0.2)
            jy = rnd.uniform(-0.2, 0.2)
            draw_stickman(c + jx, rows - 1 - r + jy, color)

        # Legend
        pink_patch = patches.Patch(color='lightpink', label='Woman')
        blue_patch = patches.Patch(color='lightskyblue', label='Man')
        ax.legend(handles=[pink_patch, blue_patch], loc='lower center', 
                   bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=12, frameon=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat182:
    def __init__(self):
        # Configuration for total items in the arrangement
        self.n = rnd.randint(6, 20)
        
        # Logic: Circular symmetry broken by making it an 'open' arrangement (Line)
        # However, we apply the 'Together' constraint for specific items
        # Answer: (n-1)! * 2!
        self.answer = math.factorial(self.n - 1) * 2

        self.description = (
            f"A set of {self.n} unique ornaments is being arranged in a straight line on a display shelf. "
            f"Two specific ornaments, indicated by the colored labels in the figure, must always be placed side-by-side. "
            f"Determine the total number of different ways the ornaments can be arranged."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Permutations and combinations"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total unique ornaments, }} n &= {self.n} \\\\"
            "\\text{{Treat the two specific ornaments as a single unit:}} & \\\\"
            f"\\text{{Remaining units to arrange}} &= (n - 2) + 1 = {self.n - 1} \\\\"
            "\\text{{Number of ways to arrange these units in a line:}} & \\\\"
            "P_{1} &= (n - 1)! \\\\"
            f"&= ({self.n} - 1)! \\\\"
            f"&= {math.factorial(self.n - 1)} \\\\"
            "\\text{{Number of ways to arrange the two ornaments within the unit:}} & \\\\"
            "P_{2} &= 2! = 2 \\\\"
            "\\text{{Total number of different arrangements:}} & \\\\"
            "\\text{{Total}} &= P_{1} \\times P_{2} \\\\"
            f"&= {math.factorial(self.n - 1)} \\times 2 \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
    )

    def generate(self, num):
        # Organized layout with informative captions
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.set_xlim(-1, self.n)
        ax.set_ylim(-1, 2)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw a shelf line 
        ax.plot([-0.8, self.n - 0.2], [-0.05, -0.05], color='saddlebrown', lw=4, zorder=0)

        def draw_ornament(x, y, color, is_special=False):
            # Base/Pedestal
            ax.plot([x - 0.3, x + 0.3], [y, y], color='black', lw=2)
            # Ornament Body 
            body = patches.RegularPolygon((x, y + 0.4), numVertices=6, radius=0.3, 
                                          orientation=np.radians(30), color=color, ec='black', lw=1.5)
            ax.add_patch(body)
            if is_special:
                # Add indicator label as requested in the description 
                ax.text(x, y + 0.9, "!", fontsize=16, ha='center', color='red', fontweight='bold',
                        bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', pad=1))

        # Randomly choose two indices for the restricted pair 
        special_indices = rnd.sample(range(self.n), 2)

        for i in range(self.n):
            is_special = i in special_indices
            color = 'gold' if is_special else 'lightblue'
            # Add organized jitter for a realistic display look
            jx = rnd.uniform(-0.05, 0.05)
            draw_ornament(i + jx, 0, color, is_special)

        # Main Title Caption
        plt.title(f"Display Shelf Arrangement: {self.n} Unique Ornaments", 
                  fontsize=16, pad=20, fontweight='bold')

        # Legend/Caption for the restricted pair 
        special_patch = patches.Patch(color='gold', label='Special Ornament (!)')
        normal_patch = patches.Patch(color='lightblue', label='Standard Ornament')
        ax.legend(handles=[special_patch, normal_patch], loc='lower center', 
                   bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=11, frameon=True)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat183:
    def __init__(self):
        # Range set to provide problem variations as per instructions
        self.num_members = rnd.randint(8, 15)
        
        # Logic for linear permutation with 2 specific members together:
        # 1. Treat the 2 specific members as 1 block.
        # 2. Arrange (n - 1) items in a row: (n-1)!
        # 3. Multiply by 2! for internal arrangement of the block.
        self.answer = math.factorial(self.num_members - 1) * 2

        self.description = (
            "A group of board members, including a Chairperson and a Secretary, are meeting at the long table "
            "shown in the figure. For this specific meeting, the Chairperson and the Secretary must sit in adjacent seats. "
            "Calculate the total number of different ways the members can be seated."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Permutations and combinations"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total number of board members, }} n &= {self.num_members}\\\\"
            "\\text{{Treat Chairperson and Secretary as 1 single block.}} &\\\\"
            f"\\text{{Number of items to arrange in a row, }} n' &= n - 1 = {self.num_members - 1}\\\\"
            "\\text{{Ways to arrange }} n' \\text{{ items in a row:}} &\\\\"
            "P_{\\text{row}} &= n'!\\\\"
            f"&= {self.num_members - 1}!\\\\"
            f"&= {math.factorial(self.num_members - 1)}\\\\"
            "\\text{{Ways to arrange Chairperson and Secretary within the block:}} &\\\\"
            "P_{\\text{internal}} &= 2! = 2\\\\"
            "\\text{{Total number of arrangements:}} &\\\\"
            "\\text{{Total}} &= P_{\\text{row}} \\times P_{\\text{internal}}\\\\"
            f"&= {math.factorial(self.num_members - 1)} \\times 2\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(-0.5, self.num_members + 0.5)
        ax.set_ylim(-1.5, 2.5)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw a long rectangular table
        table_width = self.num_members * 0.8
        table_x = (self.num_members - table_width) / 2
        table = patches.FancyBboxPatch((table_x, -0.3), table_width, 0.6, 
                                       boxstyle="round,pad=0.1",
                                       color='peru', ec='black', lw=2, alpha=0.8)
        ax.add_patch(table)

        # Calculate chair positions (evenly spaced along the table)
        spacing = table_width / self.num_members
        for i in range(self.num_members):
            x = table_x + spacing * (i + 0.5)
            y = 0.8 if i % 2 == 0 else -1.0
            
            # Draw chair icon as a rectangle
            chair = patches.Rectangle((x - 0.15, y - 0.15), 0.3, 0.3,
                                     color='darkslategrey', ec='black', lw=1)
            ax.add_patch(chair)
            
            # Label Chairperson and Secretary on two adjacent chairs
            if i == 0:
                label_y = y + 0.4 if y > 0 else y - 0.4
                ax.text(x, label_y, "Chairperson", fontsize=9, ha='center', va='bottom' if y > 0 else 'top', fontweight='bold')
            elif i == 1:
                label_y = y + 0.4 if y > 0 else y - 0.4
                ax.text(x, label_y, "Secretary", fontsize=9, ha='center', va='bottom' if y > 0 else 'top', fontweight='bold')

        # Central label
        ax.text(self.num_members / 2, 0, "Meeting Table", ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat184:
    def __init__(self):
        # Increased variety for x-values: number of points varies from 3 to 5
        num_points = rnd.randint(3, 5)
        
        # Generating a strictly increasing sequence of x-values with larger gaps
        self.x_values = []
        current_x = rnd.randint(1, 10)
        for _ in range(num_points):
            self.x_values.append(current_x)
            current_x += rnd.randint(2, 6)
        
        # Generating probabilities that sum to exactly 1.0 using randrange_float
        # We generate n-1 probabilities and the last one is the remainder
        self.probs = []
        remaining_p = 1.0
        for i in range(num_points - 1):
            # Ensure the remaining probability allows for at least 0.05 per remaining bar
            upper_bound = remaining_p - (0.05 * (num_points - 1 - i))
            p_val = round(randrange_float(0.05, max(0.06, upper_bound), 0.05), 2)
            self.probs.append(p_val)
            remaining_p = round(remaining_p - p_val, 2)
        
        self.probs.append(remaining_p)
        
        # Calculate Expected Value E(X) = sum(x * p)
        mu = sum(x * p for x, p in zip(self.x_values, self.probs))
        # Calculate E(X^2) = sum(x^2 * p)
        mu_sq = sum((x**2) * p for x, p in zip(self.x_values, self.probs))
        
        # Variance Var(X) = E(X^2) - [E(X)]^2
        self.answer = mu_sq - (mu**2)

        self.description = (
            "The figure displays the probability mass function of a discrete random variable $X$. "
            "Based on the heights of the segments shown, calculate the variance $Var(X)$."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Discrete random variables"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        
        # LaTeX Reasoning aligned with 9709 Syllabus expectations
        # Using double backslashes for f-string compatibility and rounding to 10 decimal places
        steps_mu = " + ".join([f"({x} \\times {round(p, 10)})" for x, p in zip(self.x_values, self.probs)])
        steps_mu_sq = " + ".join([f"({x}^2 \\times {round(p, 10)})" for x, p in zip(self.x_values, self.probs)])
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{1. Calculate the expected value } E(X): &\\\\"
            "E(X) &= \\sum x \\cdot P(X=x) \\\\"
            f"&= {steps_mu} \\\\"
            f"&= {round(mu, 10)} \\\\"
            "\\text{2. Calculate } E(X^2): &\\\\"
            "E(X^2) &= \\sum x^2 \\cdot P(X=x) \\\\"
            f"&= {steps_mu_sq} \\\\"
            f"&= {round(mu_sq, 10)} \\\\"
            "\\text{3. Calculate the variance } Var(X): &\\\\"
            "Var(X) &= E(X^2) - [E(X)]^2 \\\\"
            f"&= {round(mu_sq, 10)} - ({round(mu, 10)})^2 \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 6))
        
        x_min, x_max = min(self.x_values) - 2, max(self.x_values) + 2
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(0, max(self.probs) + 0.15)
        
        # Horizontal baseline
        ax.axhline(0, color='#2c3e50', lw=2)
        
        # Visualizing the PMF as vertical segments
        for x, p in zip(self.x_values, self.probs):
            ax.vlines(x, 0, p, color='royalblue', lw=5, alpha=0.8)
            ax.plot(x, p, 'ro', markersize=10, markeredgecolor='black')
            # Implicit probability value from figure
            ax.text(x, p + 0.02, f"{p:.2f}", ha='center', va='bottom', fontsize=12, fontweight='bold')
            # Discrete x values
            ax.text(x, -0.05, str(x), ha='center', va='top', fontsize=14, fontweight='bold')

        ax.set_ylabel('$P(X = x)$', fontsize=14)
        ax.set_xlabel('$x$', fontsize=14)
        ax.set_title('Probability Distribution of $X$', fontsize=16, pad=20)
        ax.grid(True, axis='y', linestyle=':', alpha=0.4)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat185:
    def __init__(self):
        # Define 4 scores
        self.scores = [1, 2, 3, 4]
        
        # Define angles (must sum to 360)
        # We vary angles while ensuring they are multiples of 5 for easier reading
        # angle1 will be roughly a right angle, angle2 roughly a straight angle
        angle1 = rnd.randint(12, 24) * 5 # 60 to 120
        angle2 = rnd.randint(24, 36) * 5 # 120 to 180
        remaining = 360 - angle1 - angle2
        
        # Split remaining into two
        angle3 = rnd.randint(4, remaining // 10) * 5
        angle4 = 360 - angle1 - angle2 - angle3
        
        self.angles = [angle1, angle2, angle3, angle4]
        self.probs = [a / 360 for a in self.angles]
        
        # Calculate expected value E(X) = sum(x * p)
        self.answer = sum(s * p for s, p in zip(self.scores, self.probs))

        self.description = (
            "A discrete random variable $X$ represents the score on the weighted four-sided spinner shown in the figure. "
            "If the spinner is spun once, find the expected value $E(X)$."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Discrete random variables"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\text{The probability } P(X=x) \\text{ is calculated by: } & \\\\"
            "P(X=x) &= \\frac{\\text{Sector Angle}}{360^\\circ} \\\\"
            f"P(X={self.scores[0]}) &= \\frac{{{self.angles[0]}^\\circ}}{{360^\\circ}} = {round(self.probs[0], 10)} \\\\"
            f"P(X={self.scores[1]}) &= \\frac{{{self.angles[1]}^\\circ}}{{360^\\circ}} = {round(self.probs[1], 10)} \\\\"
            f"P(X={self.scores[2]}) &= \\frac{{{self.angles[2]}^\\circ}}{{360^\\circ}} = {round(self.probs[2], 10)} \\\\"
            f"P(X={self.scores[3]}) &= \\frac{{{self.angles[3]}^\\circ}}{{360^\\circ}} = {round(self.probs[3], 10)} \\\\"
            "\\text{The expected value } E(X) \\text{ is given by: } & \\\\"
            "E(X) &= \\sum x \\cdot P(X=x) \\\\"
            f"&= ({self.scores[0]} \\cdot {round(self.probs[0], 10)}) + ({self.scores[1]} \\cdot {round(self.probs[1], 10)}) + ({self.scores[2]} \\cdot {round(self.probs[2], 10)}) + ({self.scores[3]} \\cdot {round(self.probs[3], 10)}) \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw circle
        circle = plt.Circle((0, 0), 1.0, color='black', fill=False, lw=2)
        ax.add_artist(circle)

        # Draw sectors and labels
        current_angle = 0
        colors_list = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        
        for i, (score, angle) in enumerate(zip(self.scores, self.angles)):
            # Draw wedge
            wedge = patches.Wedge((0, 0), 1.0, current_angle, current_angle + angle, 
                                  facecolor=colors_list[i], edgecolor='black', alpha=0.6)
            ax.add_patch(wedge)
            
            # Label the score
            mid_angle = current_angle + angle / 2
            lx = 0.7 * math.cos(math.radians(mid_angle))
            ly = 0.7 * math.sin(math.radians(mid_angle))
            ax.text(lx, ly, str(score), fontsize=24, ha='center', va='center', fontweight='bold')
            
            # Label the angle
            ax.annotate(f"{angle}$^\\circ$", xy=(0,0), xytext=(1.2 * math.cos(math.radians(mid_angle)), 1.2 * math.sin(math.radians(mid_angle))),
                        fontsize=14, ha='center', va='center')
            
            current_angle += angle

        # Draw center point and arrow (pointer)
        ax.plot(0, 0, 'ko', markersize=8)
        ax.arrow(0, 0, 0.4, 0.4, head_width=0.05, head_length=0.1, fc='k', ec='k')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat186:
    def __init__(self):
        # p is the probability of success on the first trial P(X=1)
        # Using a range that ensures visible decay in the bar chart
        self.p = round(randrange_float(0.2, 0.6, 0.01), 2)
        
        self.answer = self.p

        self.description = (
            f"A discrete random variable $X$ follows a geometric distribution $X \\sim \\text{{Geo}}(p)$. "
            f"The figure shows the probability mass function for the first few values of $x$. "
            f"Based on the figure, determine the value of $p$ as a decimal."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Discrete random variables"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The figure displays the probability mass function for a geometric distribution }} X \\sim \\text{{Geo}}(p). \\\\"
            f"\\text{{For a geometric distribution, the probability of the first success on the }} r^{{\\text{{th}}}} \\text{{ trial is:}} \\\\"
            f"P(X = r) &= p(1 - p)^{{r - 1}} \\\\"
            f"\\text{{From the figure, the probability for the first trial (}} r = 1 \\text{{) is given as:}} \\\\"
            f"P(X = 1) &= {self.p} \\\\"
            f"\\text{{Substituting }} r = 1 \\text{{ into the geometric formula:}} \\\\"
            f"P(X = 1) &= p(1 - p)^{{1 - 1}} \\\\"
            f"{self.p} &= p(1 - p)^0 \\\\"
            f"{self.p} &= p(1) \\\\"
            f"p &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Data for the first 4 values of x
        x_values = [1, 2, 3, 4]
        # P(X=r) = p * (1-p)^(r-1)
        probs = [self.p * ((1 - self.p) ** (r - 1)) for r in x_values]

        # Draw bar chart
        bars = ax.bar(x_values, probs, color='skyblue', edgecolor='black', width=0.6)
        
        # Grid and axes configuration
        ax.set_xlabel('$x$', fontsize=14)
        ax.set_ylabel('$P(X=x)$', fontsize=14)
        ax.set_xticks(x_values)
        ax.set_ylim(0, max(probs) * 1.2)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add text annotation for the first bar to provide the implicit value
        # This makes the answer 'implicit' from the figure
        ax.text(bars[0].get_x() + bars[0].get_width()/2, bars[0].get_height() + 0.01, 
                f"{self.p}", ha='center', va='bottom', fontsize=12, fontweight='bold')

        # Formatting title or identifying info
        ax.set_title('Probability Mass Function of $X \\sim \\text{Geo}(p)$', fontsize=16)

        # Save the figure
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat187:
    def __init__(self):
        # n is the number of trials, p is the success probability
        self.n = rnd.randint(5, 10)
        self.p = round(randrange_float(0.1, 0.4, 0.05), 2)
        
        # Pre-calculating the exact probability values used for both the reasoning and the graph
        # P(W=0) = (1-p)^n
        self.prob_0 = round(math.comb(self.n, 0) * (self.p**0) * ((1 - self.p)**(self.n - 0)), 4)
        # P(W=1) = n * p * (1-p)^(n-1)
        self.prob_1 = round(math.comb(self.n, 1) * (self.p**1) * ((1 - self.p)**(self.n - 1)), 4)
        
        # The ratio calculation used in the reasoning steps
        self.ratio = round(self.prob_1 / self.prob_0, 10)
        
        self.answer = self.p

        self.description = (
            f"The histogram shows the probability distribution of a discrete random variable $W$ "
            f"where $W \\sim B(n, p)$. Based on the heights of the bars shown in the figure, "
            f"find the numerical value of the success probability $p$."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "Discrete random variables"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the figure, the probabilities for the first two bars are:}} &\\\\"
            f"P(W=0) &= {self.prob_0}\\\\"
            f"P(W=1) &= {self.prob_1}\\\\"
            f"\\text{{The formula for a binomial distribution }} B(n, p) \\text{{ is:}} &\\\\"
            f"P(W=k) &= \\binom{{n}}{{k}} p^k (1-p)^{{n-k}}\\\\"
            f"\\text{{For }} k=0 \\text{{ and }} k=1: &\\\\"
            f"P(W=0) &= (1-p)^{{{self.n}}}\\\\"
            f"P(W=1) &= {self.n}p(1-p)^{{{self.n-1}}}\\\\"
            f"\\text{{Taking the ratio }} \\frac{{P(W=1)}}{{{{P(W=0)}}}}: &\\\\"
            f"\\frac{{P(W=1)}}{{P(W=0)}} &= \\frac{{{self.n}p(1-p)^{{{self.n-1}}}}}{{(1-p)^{{{self.n}}}}}\\\\"
            f"\\frac{{P(W=1)}}{{P(W=0)}} &= \\frac{{{self.n}p}}{{1-p}}\\\\"
            f"\\text{{Substituting the values from the figure:}} &\\\\"
            f"\\frac{{{self.prob_1}}}{{{self.prob_0}}} &= \\frac{{{self.n}p}}{{1-p}}\\\\"
            f"{round(self.ratio, 10)} &= \\frac{{{self.n}p}}{{1-p}}\\\\"
            f"{round(self.ratio, 10)}(1-p) &= {self.n}p\\\\"
            f"{round(self.ratio, 10)} - {round(self.ratio, 10)}p &= {self.n}p\\\\"
            f"{round(self.ratio, 10)} &= {self.n}p + {round(self.ratio, 10)}p\\\\"
            f"{round(self.ratio, 10)} &= ({self.n} + {round(self.ratio, 10)})p\\\\"
            f"p &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x = np.arange(0, self.n + 1)
        # Re-calculating full distribution for the bars 
        y = [math.comb(self.n, k) * (self.p**k) * ((1 - self.p)**(self.n - k)) for k in x]

        bars = ax.bar(x, y, width=0.8, color='lightgreen', edgecolor='black', alpha=0.8)
        
        # Using the exact variables defined in __init__ for the labels 
        ax.text(0, y[0] + 0.01, f"{self.prob_0}", ha='center', va='bottom', fontsize=10)
        ax.text(1, y[1] + 0.01, f"{self.prob_1}", ha='center', va='bottom', fontsize=10)
        
        ax.set_xlabel('Number of successes ($w$)', fontsize=12)
        ax.set_ylabel('$P(W=w)$', fontsize=12)
        ax.set_xticks(x)
        ax.set_title(f"Binomial Distribution Histogram ($n={self.n}$)", fontsize=14)
        
        ax.set_ylim(0, max(y) * 1.2)
        ax.grid(axis='y', linestyle='--', alpha=0.6)

        plt.text(self.n, max(y) * 1.1, "NOT TO SCALE", fontsize=9, ha='right', style='italic')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
class Mat188:
    def __init__(self):
        # Parameters for X ~ N(mu, sigma^2)
        # Using large ranges for variation
        self.mu = rnd.randint(50, 150)
        self.sigma = randrange_float(5.0, 20.0, 0.5)
        self.variance = round(self.sigma ** 2, 2)
        
        # Choosing a z-score to calculate x1
        self.z = randrange_float(0.5, 2.5, 0.01)
        self.x1 = round(self.mu + (self.z * self.sigma), 2)
        
        # Calculate P(X > x1) using real cumulative distribution function
        # P(X > x1) = 1 - Phi(z)
        self.answer = round(1 - norm.cdf(self.z), 4)

        # Implicit description 
        self.description = (
            "The figure illustrates a continuous random variable $X$ that follows a normal distribution. "
            "Based on the parameters and the shaded region shown in the diagram, calculate the value of the "
            "indicated probability."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "The normal distribution"
        self.source = "Cambridge International AS & A Level Mathematics Probability & Statistics 1 Coursebook (Chapter on Normal Distribution)."
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given distribution: }} X &\\sim N(\\mu, \\sigma^2) = N({self.mu}, {self.variance})\\\\"
            f"\\text{{Identify parameters from figure: }} \\mu &= {self.mu}, \\sigma^2 = {self.variance}, x_1 = {self.x1}\\\\"
            f"\\text{{Calculate standard deviation }} \\sigma: \\sigma &= \\sqrt{{{self.variance}}} = {round(self.sigma, 10)}\\\\"
            f"\\text{{Standardize }} x_1 \\text{{ to find the }} z\\text{{-score:}} &\\\\"
            f"z &= \\frac{{x_1 - \\mu}}{{\\sigma}}\\\\"
            f"&= \\frac{{{self.x1} - {self.mu}}}{{{round(self.sigma, 10)}}}\\\\"
            f"&= {round(self.z, 10)}\\\\"
            f"\\text{{The required probability is }} P(X > x_1): &\\\\"
            f"P(X > {self.x1}) &= P(Z > {round(self.z, 10)})\\\\"
            f"&= 1 - \\Phi({round(self.z, 10)})\\\\"
            f"&= 1 - {round(norm.cdf(self.z), 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Generate Normal Curve Data for the specific distribution X
        x_min = self.mu - 4 * self.sigma
        x_max = self.mu + 4 * self.sigma
        x = np.linspace(x_min, x_max, 1000)
        y = (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.sigma)**2)
        
        ax.plot(x, y, color='black', lw=2)
        
        # Shading the area P(X > x1)
        x_fill = np.linspace(self.x1, x_max, 500)
        y_fill = (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_fill - self.mu) / self.sigma)**2)
        ax.fill_between(x_fill, y_fill, color='gray', alpha=0.4)
        
        # Displaying Parameters in the Figure
        # X ~ N(mu, sigma^2) notation
        ax.text(x_min, max(y) * 0.9, f"$X \\sim N({self.mu}, {self.variance})$", fontsize=16, fontweight='bold')
        
        # Boundary line and label for x1
        ax.axvline(self.x1, color='red', linestyle='--', lw=1.5)
        ax.text(self.x1, -max(y)*0.05, f"$x_1 = {self.x1}$", fontsize=14, ha='center', color='red')
        
        # Probability notation for the shaded area
        ax.text(self.x1 + 0.5 * self.sigma, max(y) * 0.2, "$P(X > x_1)$", fontsize=14, ha='center')

        # Clean up axes
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xticks([self.mu])
        ax.set_xticklabels([f"$\mu = {self.mu}$"], fontsize=12)
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(-max(y)*0.1, max(y)*1.1)
        
        # Save image
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat189:
    def __init__(self):
        self.mu = rnd.randint(80, 200)
        self.z_val = randrange_float(-2.5, -0.5, 0.01)
        self.sigma = float(rnd.randint(4, 25))
        self.x_val = round(self.mu + (self.z_val * self.sigma), 2)
        self.prob = round(norm.cdf(self.z_val), 4)
        self.answer = self.sigma

        self.description = (
            "A random variable $X$ follows a normal distribution with the mean shown in the figure. "
            "Given the probability represented by the shaded area, calculate the value of the standard deviation $\\sigma$."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "The normal distribution"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify parameters from the figure:}} &\\\\"
            f"\\mu &= {self.mu}\\\\"
            f"x &= {self.x_val}\\\\"
            f"P(X < {self.x_val}) &= {self.prob}\\\\"
            f"\\text{{The formula for standardizing }} X \\text{{ is:}} &\\\\"
            f"Z &= \\frac{{X - \\mu}}{{\\sigma}}\\\\"
            f"\\text{{Using the given probability, find the corresponding }} z\\text{{-score:}} &\\\\"
            f"P(Z < z) &= {self.prob}\\\\"
            f"z &= \\Phi^{{-1}}({self.prob})\\\\"
            f"z &= {round(self.z_val, 10)}\\\\"
            f"\\text{{Substitute }} \\mu, x, \\text{{ and }} z \\text{{ into the standardization formula:}} &\\\\"
            f"{round(self.z_val, 10)} &= \\frac{{{self.x_val} - {self.mu}}}{{\\sigma}}\\\\"
            f"{round(self.z_val, 10)} &= \\frac{{{round(self.x_val - self.mu, 10)}}}{{\\sigma}}\\\\"
            f"\\sigma &= \\frac{{{round(self.x_val - self.mu, 10)}}}{{{round(self.z_val, 10)}}}\\\\"
            f"\\sigma &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Standard normal curve range
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x)
        
        ax.plot(x, y, color='black', lw=2)
        
        # Shade P(Z < z_val)
        x_fill = np.linspace(-4, self.z_val, 500)
        y_fill = norm.pdf(x_fill)
        ax.fill_between(x_fill, y_fill, color='gray', alpha=0.5)
        
        # Lines and Labels
        ax.axvline(0, color='black', linestyle='--', lw=1)
        ax.axvline(self.z_val, color='black', lw=1.5)
        
        # Implicitly provide mu and x_val via axis labels
        # We transform z-coordinates to "X" scale labels for the user
        ax.set_xticks([0, self.z_val])
        ax.set_xticklabels([f"$\mu = {int(self.mu)}$", ""], fontsize=14)
        
        # Add probability text
        # Position it slightly above the shaded area
        ax.text(self.z_val - 0.5, 0.05, f"$P(X < {self.x_val}) = {self.prob}$", 
                fontsize=12, ha='right', bbox=dict(facecolor='white', alpha=0.7))

        # Visual styling
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xlim(-4, 4)
        ax.set_ylim(0, 0.45)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat190:
    def __init__(self):
        # Deterministic generation for normal distribution parameters
        # Standard deviation generated within a continuous range
        self.sigma = randrange_float(5.0, 20.0, 0.5)
        self.variance = round(self.sigma ** 2, 2)
        
        # Generated mu as the target answer
        self.mu_true = rnd.randint(100, 1000)
        
        # Symmetric boundaries: use the same z-score for both sides
        # This makes the problem algebraically solvable: mu = (x1 + x2) / 2
        self.z_val = round(randrange_float(0.5, 2.5, 0.01), 2)
        self.z_lower = -self.z_val
        self.z_upper = self.z_val
        
        # Calculate symmetric boundaries: x = mu +/- z*sigma
        self.lower_x = round(self.mu_true - (self.z_val * self.sigma), 2)
        self.upper_x = round(self.mu_true + (self.z_val * self.sigma), 2)
        
        # Calculate area between x_lower and x_upper
        # P(x_lower < X < x_upper) = 2*Phi(z) - 1
        self.area = round(2 * norm.cdf(self.z_val) - 1, 4)
        
        self.answer = self.mu_true

        self.description = (
            "The figure shows a normal distribution where the shaded region represents a specific probability. "
            "Based on the boundary values of the shaded area and the variance of the distribution, find the value of the mean $\\mu$."
        )
        
        self.topic = "Probability & Statistics 1"
        self.subtopic = "The normal distribution" 
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus" 
        self.curriculum = "AS & A Level" 
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            rf"\text{{Identify parameters from the figure:}} &\\"
            rf"\sigma^2 &= {self.variance} \implies \sigma = \sqrt{{{self.variance}}} = {round(self.sigma, 10)}\\"
            rf"x_1 &= {self.lower_x}, \quad x_2 = {self.upper_x}\\"
            rf"P(x_1 < X < x_2) &= {self.area}\\"
            rf"\text{{Since the shaded region is symmetric about the mean:}} &\\"
            rf"x_1 &= \mu - z\sigma, \quad x_2 = \mu + z\sigma\\"
            rf"\text{{Adding these two equations:}} &\\"
            rf"x_1 + x_2 &= 2\mu\\"
            rf"\mu &= \frac{{x_1 + x_2}}{{2}}\\"
            rf"&= \frac{{{self.lower_x} + {self.upper_x}}}{{2}}\\"
            rf"&= \frac{{{round(self.lower_x + self.upper_x, 10)}}}{{2}}\\"
            rf"&= {self.answer}\\"
            rf"\text{{Verification: }} z &= \frac{{x_2 - \mu}}{{\sigma}} = \frac{{{self.upper_x} - {self.answer}}}{{{round(self.sigma, 10)}}} = {round(self.z_val, 10)}\\"
            rf"P(x_1 < X < x_2) &= 2\Phi({round(self.z_val, 10)}) - 1 = {self.area} \checkmark"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Range of 4 standard deviations from a 0-center for visualization
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x)
        ax.plot(x, y, color='black', lw=2)
        
        # Shade asymmetric central area between z_lower and z_upper
        x_fill = np.linspace(self.z_lower, self.z_upper, 500)
        y_fill = norm.pdf(x_fill)
        ax.fill_between(x_fill, y_fill, color='gray', alpha=0.5)
        
        # Visual indicators for boundaries and the unknown mean
        ax.axvline(0, color='black', linestyle='--', lw=1)
        ax.axvline(self.z_lower, color='black', lw=1.5)
        ax.axvline(self.z_upper, color='black', lw=1.5)
        
        # Mean label above the line
        ax.text(0, 0.015, "$\\mu = ?$", ha='center', va='bottom', fontsize=14, fontweight='bold')
        
        # Area probability label inside the shaded region
        ax.text((self.z_lower + self.z_upper)/2, 0.12, f"$P({self.lower_x} < X < {self.upper_x}) = {self.area}$", 
                fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round'))
        
        # Variance information provided implicitly
        ax.text(-3.8, 0.35, f"$X \\sim N(\\mu, {self.variance})$", fontsize=15, fontweight='bold')

        # Formatting axes
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xticks([]) 
        ax.set_xlim(-4, 4)
        ax.set_ylim(-0.02, 0.45)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat191:
    def __init__(self):
        # n is the sample size
        self.n = rnd.randint(10, 40)
        # standard_error represents the distance from mean to inflection point in sampling distribution
        self.standard_error = round(randrange_float(0.5, 3.0, 0.01), 2)
        # population mean mu
        self.mu = rnd.randint(40, 100)
        
        # Formula: Standard Error = sigma / sqrt(n)
        # Therefore: sigma = Standard Error * sqrt(n)
        self.answer = round(self.standard_error * math.sqrt(self.n), 2)

        self.description = (
            f"The figure illustrates the probability density function of the sample mean $\\overline{{X}}$ "
            f"for samples of size $n = {self.n}$ taken from a normally distributed population with mean $\\mu$ and variance $\\sigma^2$. "
            f"Based on the parameters shown in the figure, calculate the standard deviation of the population, $\\sigma$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The distance from the mean to the inflection point represents the standard error (SE):}} &\\\\"
            f"\\text{{SE}} &= {round(self.standard_error, 10)}\\\\"
            f"\\text{{The sample size is given as:}} &\\\\"
            f"n &= {self.n}\\\\"
            f"\\text{{The formula for the standard error of the sample mean is:}} &\\\\"
            f"\\text{{SE}} &= \\frac{{\\sigma}}{{\\sqrt{{n}}}}\\\\"
            f"\\text{{Rearranging to solve for the population standard deviation }} \\sigma: &\\\\"
            f"\\sigma &= \\text{{SE}} \\times \\sqrt{{n}}\\\\"
            f"&= {round(self.standard_error, 10)} \\times \\sqrt{{{self.n}}}\\\\"
            f"&= {round(self.standard_error, 10)} \\times {round(math.sqrt(self.n), 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Define the range for the normal curve based on standard error
        x = np.linspace(self.mu - 4 * self.standard_error, self.mu + 4 * self.standard_error, 1000)
        y = (1 / (self.standard_error * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.standard_error)**2)
        
        ax.plot(x, y, color='black', lw=2)
        
        # Mark the mean
        ax.axvline(self.mu, color='black', linestyle='--', lw=1)
        ax.text(self.mu, -0.02 * np.max(y), f"{self.mu}", ha='center', fontsize=12)
        
        # Mark the inflection point (1 standard error away)
        inflection_x = self.mu + self.standard_error
        ax.plot([self.mu, inflection_x], [np.max(y) * 0.606, np.max(y) * 0.606], color='red', lw=1.5)
        
        # Add label for the distance (standard error)
        ax.text((self.mu + inflection_x) / 2, np.max(y) * 0.62, f"{self.standard_error}", 
                ha='center', va='bottom', fontsize=12, color='red', fontweight='bold')
        
        # Vertical line at inflection point for clarity
        ax.axvline(inflection_x, ymin=0, ymax=0.606, color='red', linestyle=':', lw=1)

        # Styling
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xlabel(r"Sample Mean $\overline{X}$", fontsize=12)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat192:
    def __init__(self):
        # Generate a random base and a list of offsets to create data points
        # Using a set of unique locations then adding some duplicates (stacks)
        base = rnd.randint(10, 50)
        num_unique = rnd.randint(4, 7)
        unique_offsets = sorted(rnd.sample(range(0, 25), num_unique))
        
        self.data_points = []
        for offset in unique_offsets:
            val = base + offset
            # Randomly decide to stack 1, 2, or 3 points at this location
            count = rnd.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
            self.data_points.extend([val] * count)
        
        # Shuffle for logic, though visualization will be ordered
        rnd.shuffle(self.data_points)
        
        n = len(self.data_points)
        sum_x = sum(self.data_points)
        sum_x2 = sum(x**2 for x in self.data_points)
        
        # Calculate unbiased estimate of population variance (s^2)
        # s^2 = (1 / (n-1)) * (sum_x2 - (sum_x^2 / n))
        self.answer = round((sum_x2 - (sum_x**2 / n)) / (n - 1), 2)

        self.description = (
            "The dot plot shows the wingspan measurements (in cm) of a random sample of birds. "
            "Based on the visual data provided in the figure, calculate the unbiased estimate of the population variance ($s^2$)."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the dot plot, the data set is:}} &\\\\"
            f"x &= \\{{ {', '.join(map(str, sorted(self.data_points)))} \\}}\\\\"
            f"\\text{{The sample size is:}} &\\\\"
            f"n &= {len(self.data_points)}\\\\"
            f"\\text{{Calculate the sum of the observations }} \\sum x: &\\\\"
            f"\\sum x &= {sum(self.data_points)}\\\\"
            f"\\text{{Calculate the sum of the squares }} \\sum x^2: &\\\\"
            f"\\sum x^2 &= {sum(x**2 for x in self.data_points)}\\\\"
            f"\\text{{The formula for the unbiased estimate of population variance }} s^2 \\text{{ is:}} &\\\\"
            f"s^2 &= \\frac{{1}}{{n-1}} \\left( \\sum x^2 - \\frac{{(\\sum x)^2}}{{n}} \\right)\\\\"
            f"&= \\frac{{1}}{{{len(self.data_points)} - 1}} \\left( {sum(x**2 for x in self.data_points)} - \\frac{{{sum(self.data_points)}^2}}{{{len(self.data_points)}}} \\right)\\\\"
            f"&= \\frac{{1}}{{{len(self.data_points) - 1}}} \\left( {sum(x**2 for x in self.data_points)} - {round(sum(self.data_points)**2 / len(self.data_points), 10)} \\right)\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))
        
        # Count frequencies for stacking
        from collections import Counter
        counts = Counter(self.data_points)
        sorted_vals = sorted(counts.keys())
        
        # Plotting the dot plot
        for val in sorted_vals:
            for i in range(counts[val]):
                ax.plot(val, i + 1, 'ko', markersize=12)
        
        # Set axis limits and labels
        padding = 2
        ax.set_xlim(min(self.data_points) - padding, max(self.data_points) + padding)
        ax.set_ylim(0, max(counts.values()) + 1)
        
        # Clean up the appearance
        ax.get_yaxis().set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel("Wingspan (cm)", fontsize=14)
        
        # Ensure only integer ticks on x-axis
        ax.xaxis.set_major_locator(MultipleLocator(2))
        ax.tick_params(axis='x', labelsize=12)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat193:
    def __init__(self):
        # We pick sqrt_n first to ensure n is a perfect square for a clean numeric answer
        self.sqrt_n = rnd.randint(5, 12) 
        self.n = self.sqrt_n**2
        
        # Standard deviation of population (sigma)
        # Using randrange_float with step 0.5 for clean variability
        self.sigma = round(randrange_float(5.0, 25.0, 0.5), 2)
        
        # Standard error (SE) = sigma / sqrt(n)
        self.standard_error = round(self.sigma / self.sqrt_n, 2)
        
        # Re-verify sigma to maintain mathematical consistency with the displayed SE
        self.sigma = round(self.standard_error * self.sqrt_n, 2)

        self.answer = self.n

        self.description = (
            "The figure shows the distribution of a population and the corresponding sampling distribution "
            "of the sample mean $\\overline{X}$ for samples of size $n$. Based on the statistical parameters "
            "provided in the figure, determine the value of the sample size $n$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the population distribution legend, the standard deviation is:}} &\\\\"
            f"\\sigma &= {round(self.sigma, 10)}\\\\"
            f"\\text{{From the sampling distribution figure, the standard error (SE) is:}} &\\\\"
            f"\\text{{SE}} &= {round(self.standard_error, 10)}\\\\"
            f"\\text{{The formula for the standard error of the sample mean is:}} &\\\\"
            f"\\text{{SE}} &= \\frac{{\\sigma}}{{\\sqrt{{n}}}}\\\\"
            f"\\text{{Rearranging the formula to solve for }} \\sqrt{{n}}: &\\\\"
            f"\\sqrt{{n}} &= \\frac{{\\sigma}}{{\\text{{SE}}}}\\\\"
            f"&= \\frac{{{round(self.sigma, 10)}}}{{{round(self.standard_error, 10)}}}\\\\"
            f"&= {round(self.sigma / self.standard_error, 10)}\\\\"
            f"\\text{{Squaring both sides to find the sample size }} n: &\\\\"
            f"n &= ({round(self.sigma / self.standard_error, 10)})^2\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Population Distribution (Skewed)
        from scipy.stats import gamma, norm
        x_pop = np.linspace(0, 20, 1000)
        y_pop = gamma.pdf(x_pop, a=2)
        
        ax1.plot(x_pop, y_pop, color='black', lw=2, label=f"$\\sigma = {self.sigma}$")
        ax1.fill_between(x_pop, y_pop, color='lightgray', alpha=0.3)
        ax1.set_title("Population Distribution", fontsize=14, fontweight='bold')
        ax1.legend(loc='upper right', fontsize=12, frameon=True)
        
        # Clean axes for population
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_visible(False)

        # Sampling Distribution (Normal)
        mu_sample = 10
        x_sample = np.linspace(mu_sample - 4, mu_sample + 4, 1000)
        visual_se = 1.0  # Constant visual scale for standardized appearance
        y_sample = norm.pdf(x_sample, mu_sample, visual_se)
        
        ax2.plot(x_sample, y_sample, color='blue', lw=2)
        ax2.set_title("Sampling Distribution of $\\overline{X}$", fontsize=14, fontweight='bold')
        
        # Center line (Mean)
        ax2.axvline(mu_sample, color='black', linestyle='--', lw=1)
        
        # Mark Standard Error distance (Mean to Inflection point)
        inflection_x = mu_sample + visual_se
        ax2.annotate('', xy=(mu_sample, max(y_sample)*0.5), xytext=(inflection_x, max(y_sample)*0.5),
                     arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
        
        # Label the SE value directly on the graph
        ax2.text((mu_sample + inflection_x)/2, max(y_sample)*0.55, f"SE = {self.standard_error}", 
                 ha='center', color='black', fontsize=12, fontweight='bold')

        # Clean axes for sampling distribution
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat194:
    def __init__(self):
        # Generate alpha/2 value as a clean decimal (e.g., 0.005, 0.025, 0.05)
        # alpha_half is the area of one tail
        self.alpha_half = round(randrange_float(0.005, 0.05, 0.005), 3)
        
        # Calculate total alpha and then the confidence level
        alpha = 2 * self.alpha_half
        self.answer = round((1 - alpha) * 100, 2)

        self.description = (
            "The figure shows a standard normal distribution used to determine the critical value $z$ "
            "for a confidence interval. Based on the indicated area in the shaded tails, "
            "calculate the confidence level of the interval as a percentage."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = ""

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Standard Normal Distribution (mu=0, sigma=1)
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x, 0, 1)
        ax.plot(x, y, color='black', lw=2)
        
        # Calculate z-critical value for the shaded regions
        z_crit = norm.ppf(1 - self.alpha_half)
        
        # Shade Right Tail
        x_right = np.linspace(z_crit, 4, 200)
        y_right = norm.pdf(x_right, 0, 1)
        ax.fill_between(x_right, y_right, color='gray', alpha=0.5)
        
        # Shade Left Tail
        x_left = np.linspace(-4, -z_crit, 200)
        y_left = norm.pdf(x_left, 0, 1)
        ax.fill_between(x_left, y_left, color='gray', alpha=0.5)
        
        # Labels for the tail areas
        # Put the text above the tails
        ax.text(z_crit + 0.3, 0.05, f"{self.alpha_half}", ha='left', fontsize=12, fontweight='bold')
        ax.text(-z_crit - 0.3, 0.05, f"{self.alpha_half}", ha='right', fontsize=12, fontweight='bold')
        
        # Axis formatting
        ax.set_xticks([-z_crit, 0, z_crit])
        ax.set_xticklabels(['$-z$', '$0$', '$z$'], fontsize=12)
        ax.set_yticks([])
        
        # Horizontal line for x-axis
        ax.axhline(0, color='black', lw=1)
        
        # Remove spines
        for spine in ['top', 'right', 'left']:
            ax.spines[spine].set_visible(False)
            
        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
    
class Mat195:
    def __init__(self):
        # Generate random boundaries for the confidence interval
        # Using plant height context (e.g., 10cm to 25cm)
        self.lower_bound = round(randrange_float(10.0, 15.0, 0.01), 2)
        self.width = round(randrange_float(1.0, 3.0, 0.01), 2)
        self.upper_bound = round(self.lower_bound + self.width, 2)
        
        # The sample mean is the midpoint of the confidence interval
        self.answer = round((self.lower_bound + self.upper_bound) / 2, 2)

        self.description = (
            "A confidence interval for the mean height of a plant species was calculated from a large sample. "
            "Based on the normal distribution curve and the interval shown in the figure, find the sample mean $\\overline{x}$ "
            "used to construct this interval."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Lower bound of the confidence interval}} &= {round(self.lower_bound, 10)}\\\\"
            f"\\text{{Upper bound of the confidence interval}} &= {round(self.upper_bound, 10)}\\\\"
            f"\\text{{The sample mean }} \\overline{{x}} \\text{{ is the midpoint of the confidence interval:}} &\\\\"
            f"\\overline{{x}} &= \\frac{{\\text{{Lower bound}} + \\text{{Upper bound}}}}{{2}}\\\\"
            f"&= \\frac{{{round(self.lower_bound, 10)} + {round(self.upper_bound, 10)}}}{{2}}\\\\"
            f"&= \\frac{{{round(self.lower_bound + self.upper_bound, 10)}}}{{2}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Setup the normal curve parameters for visualization
        mu = self.answer
        sigma = self.width / 4  # Scale sigma so the interval looks natural
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
        y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
        
        # Plot the normal curve
        ax.plot(x, y, color='black', lw=2)
        
        # Shade the confidence interval area
        x_fill = np.linspace(self.lower_bound, self.upper_bound, 500)
        y_fill = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_fill - mu) / sigma)**2)
        ax.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4)
        
        # Draw vertical lines at boundaries
        ax.vlines([self.lower_bound, self.upper_bound], 0, 
                  [(1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((self.lower_bound - mu) / sigma)**2),
                   (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((self.upper_bound - mu) / sigma)**2)],
                  color='black', lw=1.5)

        # Labels for the boundaries
        ax.text(self.lower_bound, -0.05 * max(y), f"{self.lower_bound}", ha='center', fontsize=12, fontweight='bold')
        ax.text(self.upper_bound, -0.05 * max(y), f"{self.upper_bound}", ha='center', fontsize=12, fontweight='bold')
        
        # Add "Confidence Interval" arrow/text
        arrow = patches.FancyArrowPatch((self.lower_bound, -0.12 * max(y)), (self.upper_bound, -0.12 * max(y)),
                                        arrowstyle='<->', mutation_scale=15, color='black')
        ax.add_patch(arrow)
        ax.text(mu, -0.18 * max(y), "Confidence Interval", ha='center', fontsize=11)

        # Style cleanup
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_ylim(-0.25 * max(y), 1.1 * max(y))
        
        # Save image
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat196:
    def __init__(self):
        # Generate a continuous range for confidence levels (e.g., 85% to 99%)
        self.conf_level_pct = round(randrange_float(85.0, 99.0, 0.01), 2)
        self.conf_level = self.conf_level_pct / 100
        
        # Calculate z-critical value based on the confidence level
        # alpha = 1 - conf_level; tail = alpha / 2; z = norm.ppf(1 - tail)
        self.z_critical = norm.ppf(1 - (1 - self.conf_level) / 2)
        
        # Standard Error (SE) using randrange_float
        self.se = round(randrange_float(0.5, 5.0, 0.01), 2)
        
        # Width = 2 * z * SE
        self.answer = round(2 * self.z_critical * self.se, 2)

        self.description = (
            "The figure shows the areas under the standard normal curve used for a specific confidence interval. "
            "Based on the shaded area and the given standard error (SE), calculate the width of the confidence interval "
            "for the population mean $\\mu$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}",
            f"\\text{{Confidence Level (CL)}} &= {round(self.conf_level_pct, 10)}\\% = {round(self.conf_level, 10)}\\\\"
            f"\\alpha &= 1 - CL = 1 - {round(self.conf_level, 10)} = {round(1 - self.conf_level, 10)}\\\\"
            f"\\text{{Tail Area }} \\left(\\frac{{\\alpha}}{{2}}\\right) &= \\frac{{{round(1 - self.conf_level, 10)}}}{{2}} = {round((1 - self.conf_level) / 2, 10)}\\\\"
            f"z^* &= \\Phi^{{-1}}\\left(1 - \\frac{{\\alpha}}{{2}}\\right) = \\Phi^{{-1}}\\left(1 - {round((1 - self.conf_level) / 2, 10)}\\right)\\\\"
            f"z^* &= \\Phi^{{-1}}\\left({round(1 - (1 - self.conf_level) / 2, 10)}\\right) = {round(self.z_critical, 10)}\\\\"
            f"\\text{{Standard Error (SE)}} &= {self.se}\\\\"
            f"\\text{{Width}} &= 2 \\times z^* \\times SE\\\\"
            f"&= 2 \\times {round(self.z_critical, 10)} \\times {self.se}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Standard Normal Distribution
        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x)
        ax.plot(x, y, color='black', lw=2)
        
        # Central Shading (Confidence Level)
        z = self.z_critical
        x_conf = np.linspace(-z, z, 500)
        y_conf = norm.pdf(x_conf)
        ax.fill_between(x_conf, y_conf, color='skyblue', alpha=0.5)
        
        # Annotations
        ax.text(0, 0.15, f"{self.conf_level_pct}%", ha='center', fontsize=14, fontweight='bold')
        
        # SE Info
        plt.text(2.2, 0.35, f"SE = {self.se}", bbox=dict(facecolor='white', alpha=0.8), fontsize=12)
        
        # Width Indicator
        ax.annotate('', xy=(-z, -0.02), xytext=(z, -0.02), 
                    arrowprops=dict(arrowstyle='<->', color='black'))
        ax.text(0, -0.07, "Interval Width", ha='center', fontsize=11)

        ax.set_xlim(-4, 4)
        ax.set_ylim(-0.1, 0.45)
        ax.axis('off')
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat197:
    def __init__(self):
        # Randomize sample size nA and the ratio of standard errors (k = SEA / SEB)
        self.nA = rnd.randint(16, 100)
        self.k = rnd.randint(2, 5) # ratio SEA : SEB = k : 1
        
        # Since SE = sigma / sqrt(n):
        # SEA / SEB = (sigma / sqrt(nA)) / (sigma / sqrt(nB)) = sqrt(nB) / sqrt(nA)
        # k = sqrt(nB / nA) => nB = nA * k^2
        self.answer = self.nA * (self.k**2)

        self.description = (
            "The figure shows two sampling distributions, $A$ and $B$, for the same population mean "
            "but with different sample sizes, $n_A$ and $n_B$. Based on the relationship shown and the "
            "parameters in the legend, calculate the value of $n_B$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Sample size of }} A, n_A &= {self.nA}\\\\"
            f"\\text{{Ratio of standard errors, }} SE_A : SE_B &= {self.k} : 1\\\\"
            f"\\text{{The standard error (SE) is defined as:}} &\\\\"
            f"SE &= \\frac{{\\sigma}}{{\\sqrt{{n}}}}\\\\"
            f"\\text{{The ratio of standard errors for distributions }} A \\text{{ and }} B \\text{{ is:}} &\\\\"
            f"\\frac{{SE_A}}{{SE_B}} &= \\frac{{\\sigma / \\sqrt{{n_A}}}}{{\\sigma / \\sqrt{{n_B}}}}\\\\"
            f"\\frac{{SE_A}}{{SE_B}} &= \\sqrt{{\\frac{{n_B}}{{n_A}}}}\\\\"
            f"\\text{{Substituting the known values:}} &\\\\"
            f"{self.k} &= \\sqrt{{\\frac{{n_B}}{{{self.nA}}}}}\\\\"
            f"\\text{{Squaring both sides to solve for }} n_B: &\\\\"
            f"{round(self.k**2, 10)} &= \\frac{{n_B}}{{{self.nA}}}\\\\"
            f"n_B &= {round(self.k**2, 10)} \\times {self.nA}\\\\"
            f"n_B &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Define parameters for visual distribution
        mu = 0
        se_a = 1.0
        se_b = se_a / self.k
        
        x = np.linspace(-4, 4, 1000)
        y_a = norm.pdf(x, mu, se_a)
        y_b = norm.pdf(x, mu, se_b)
        
        # Plot the normal distribution curves
        ax.plot(x, y_a, color='blue', lw=2, label=f'Distribution A ($n_A = {self.nA}$)')
        ax.plot(x, y_b, color='red', lw=2, label='Distribution B ($n_B$)')
        
        # Add legend with implicit numerical information
        legend_text = (
            f"$n_A = {self.nA}$\n"
            f"$SE_A : SE_B = {self.k}:1$"
        )
        ax.text(0.95, 0.95, legend_text, transform=ax.transAxes, verticalalignment='top', 
                horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                fontsize=12)
        
        # Formatting
        ax.set_title("Comparison of Sampling Distributions", fontsize=14)
        ax.set_xlabel("Sample Mean ($\\overline{X}$)", fontsize=12)
        ax.set_ylabel("Probability Density", fontsize=12)
        ax.legend(loc='upper left')
        ax.grid(True, linestyle=':', alpha=0.6)
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat198:
    def __init__(self):
        # Randomly select a confidence level percentage (e.g., 80% to 99%)
        self.conf_level_pct = round(randrange_float(80.0, 99.0, 0.01), 2)
        self.conf_level = self.conf_level_pct / 100
        
        # Calculate the corresponding z-critical value
        alpha = 1 - self.conf_level
        self.z = round(norm.ppf(1 - alpha / 2), 3)
        
        # Generate random sample proportion p_hat
        self.p_hat = round(randrange_float(0.15, 0.85, 0.01), 2)
        
        # Target Margin of Error (E)
        self.E_target = round(randrange_float(0.02, 0.05, 0.01), 2)
        
        # Solve for n: E = z * sqrt(p_hat * (1 - p_hat) / n)
        # n = (z^2 * p_hat * (1 - p_hat)) / E^2
        self.answer = math.ceil((self.z**2 * self.p_hat * (1 - self.p_hat)) / (self.E_target**2))

        self.description = (
            "The figure illustrates the relationship between the margin of error ($E$) and the sample size ($n$) "
            "for a survey result. Based on the parameters provided in the figure legend and the marked point on the curve, "
            "determine the required sample size $n$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the figure legend:}} &\\\\"
            f"\\text{{Sample proportion }} (\\hat{{p}}) &= {round(self.p_hat, 10)}\\\\"
            f"\\text{{Target margin of error }} (E) &= {round(self.E_target, 10)}\\\\"
            f"\\text{{Critical value }} (z) &= {round(self.z, 10)}\\\\"
            f"\\text{{The margin of error formula for a proportion is:}} &\\\\"
            f"E &= z \\times \\sqrt{{\\frac{{\\hat{{p}}(1 - \\hat{{p}})}}{{n}}}}\\\\"
            f"\\text{{Rearranging for }} n: &\\\\"
            f"n &= \\frac{{z^2 \\times \\hat{{p}}(1 - \\hat{{p}})}}{{E^2}}\\\\"
            f"&= \\frac{{({round(self.z, 10)})^2 \\times {round(self.p_hat, 10)}(1 - {round(self.p_hat, 10)})}}{{({round(self.E_target, 10)})^2}}\\\\"
            f"&= \\frac{{{round(self.z**2, 10)} \\times {round(self.p_hat * (1 - self.p_hat), 10)}}}{{{round(self.E_target**2, 10)}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plotting range for n based on the answer
        n_start = max(50, self.answer - 800)
        n_end = self.answer + 1200
        n_vals = np.linspace(n_start, n_end, 500)
        E_vals = self.z * np.sqrt((self.p_hat * (1 - self.p_hat)) / n_vals)
        
        # Plot the main curve
        ax.plot(n_vals, E_vals, color='darkblue', lw=2)
        
        # Mark target E and corresponding n
        ax.scatter(self.answer, self.E_target, color='red', s=60, zorder=5)
        
        # Dashed projection lines
        ax.axhline(y=self.E_target, xmin=0, xmax=(self.answer - n_start)/(n_end - n_start), 
                   color='gray', linestyle='--', alpha=0.6)
        ax.axvline(x=self.answer, ymin=0, ymax=(self.E_target - min(E_vals))/(max(E_vals) - min(E_vals)), 
                   color='gray', linestyle='--', alpha=0.6)
        
        # Legend with all necessary implicit information
        legend_info = (
            f"$\\hat{{p}} = {self.p_hat}$\n"
            f"Confidence Level = {self.conf_level_pct}%\n"
            f"Target $E = {self.E_target}$\n"
            f"Critical Value $z = {self.z}$"
        )
        ax.text(0.95, 0.95, legend_info, transform=ax.transAxes, verticalalignment='top', 
                horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                fontsize=11)
        
        # Formatting
        ax.set_xlabel('Sample Size ($n$)', fontsize=12)
        ax.set_ylabel('Margin of Error ($E$)', fontsize=12)
        ax.set_title('Margin of Error $E$ as a Function of Sample Size $n$', fontsize=13)
        ax.grid(True, which='both', linestyle=':', alpha=0.5)
        
        # Annotate target E on axis
        ax.text(n_start + (n_end-n_start)*0.02, self.E_target + 0.001, f"$E={self.E_target}$", 
                color='red', fontweight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat199:
    def __init__(self):
        # Randomize sample sizes n1 and n2
        self.n1 = rnd.randint(8, 25)
        self.n2 = rnd.randint(8, 25)
        
        # Randomize sample means x1 and x2
        self.x1 = round(randrange_float(15.0, 30.0, 0.1), 1)
        self.x2 = round(randrange_float(15.0, 30.0, 0.1), 1)
        
        # Calculate the combined unbiased estimate (weighted mean)
        # Combined Mean = (n1*x1 + n2*x2) / (n1 + n2)
        self.answer = round((self.n1 * self.x1 + self.n2 * self.x2) / (self.n1 + self.n2), 2)

        self.description = (
            "Two independent samples are taken from the same population. "
            "Based on the boxplots and the sample sizes provided in the figure legend, "
            "calculate the unbiased estimate of the population mean by combining all observations."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Sample sizes: }} n_1 &= {self.n1}, \\quad n_2 = {self.n2}\\\\"
            f"\\text{{Sample means from figure: }} \\bar{{x}}_1 &= {round(self.x1, 10)}, \\quad \\bar{{x}}_2 = {round(self.x2, 10)}\\\\"
            f"\\text{{The unbiased estimate of the combined population mean is the weighted mean:}} &\\\\"
            f"\\bar{{x}}_{{combined}} &= \\frac{{n_1\\bar{{x}}_1 + n_2\\bar{{x}}_2}}{{n_1 + n_2}}\\\\"
            f"&= \\frac{{{self.n1}({round(self.x1, 10)}) + {self.n2}({round(self.x2, 10)})}}{{{self.n1} + {self.n2}}}\\\\"
            f"&= \\frac{{{round(self.n1 * self.x1, 10)} + {round(self.n2 * self.x2, 10)}}}{{{self.n1 + self.n2}}}\\\\"
            f"&= \\frac{{{round(self.n1 * self.x1 + self.n2 * self.x2, 10)}}}{{{self.n1 + self.n2}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create dummy data for boxplots to reflect the means
        # Boxplot doesn't show mean by default, so we add a marker
        data1 = np.random.normal(self.x1, 3, 100)
        data2 = np.random.normal(self.x2, 3, 100)
        
        box = ax.boxplot([data1, data2], vert=False, patch_artist=True, 
                         labels=['Sample 1', 'Sample 2'],
                         showmeans=True, meanprops={"marker":"x", "markeredgecolor":"red", "markersize":10})

        # Colors
        colors = ['#add8e6', '#90ee90']
        for patch, color in zip(box['boxes'], colors):
            patch.set_facecolor(color)

        # Annotate the means next to the 'x' markers
        ax.text(self.x1, 1.15, f"{self.x1}", color='red', fontweight='bold', ha='center')
        ax.text(self.x2, 2.15, f"{self.x2}", color='red', fontweight='bold', ha='center')

        # Legend with sample sizes (implicit info required for calculation)
        legend_info = (
            f"Sample 1: $n_1 = {self.n1}$\n"
            f"Sample 2: $n_2 = {self.n2}$\n"
            "x = Sample Mean"
        )
        ax.text(0.95, 0.05, legend_info, transform=ax.transAxes, verticalalignment='bottom', 
                horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                fontsize=12)

        ax.set_title("Boxplots of Independent Samples", fontsize=14)
        ax.set_xlabel("Value", fontsize=12)
        ax.grid(True, linestyle=':', alpha=0.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()

class Mat200:
    def __init__(self):
        # 1. Generate a large sample size n (integer)
        self.n = rnd.randint(150, 500)
        
        # 2. Generate a random count of successes x (integer)
        # Ensure the proportion is within a reasonable range (e.g., 0.1 to 0.9)
        self.x = rnd.randint(int(0.15 * self.n), int(0.85 * self.n))
        
        # 3. Calculate the unbiased point estimate (sample proportion)
        # p_hat = x / n
        self.answer = round(self.x / self.n, 4)

        self.description = (
            "A survey was conducted with a large sample size. "
            "The frequency bar chart illustrates the count of 'success' and 'failure' outcomes. "
            "Based on the figure, calculate the unbiased point estimate for the population proportion $p$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Sample size }} (n) &= {self.n}\\\\"
            f"\\text{{Number of successes }} (x) &= {self.x}\\\\"
            f"\\text{{The unbiased point estimate for }} p \\text{{ is the sample proportion }} \\hat{{p}}:\\\\"
            f"\\hat{{p}} &= \\frac{{x}}{{n}}\\\\"
            f"&= \\frac{{{self.x}}}{{{self.n}}}\\\\"
            f"&= {round(self.x / self.n, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        categories = ['Success', 'Failure']
        # 'Failure' count is the remaining from the total sample size n
        counts = [self.x, self.n - self.x]
        
        # Draw the bar chart
        bars = ax.bar(categories, counts, color=['#3498db', '#ecf0f1'], edgecolor='black', linewidth=1.5)
        
        # Shading the 'Success' bar to match the requirement of the prompt
        bars[0].set_hatch('//')
        bars[0].set_alpha(0.8)

        # Legend and Labeling
        ax.set_ylabel('Frequency (Count)', fontsize=12, fontweight='bold')
        ax.set_title(f'Outcome Frequency (Total $n = {self.n}$)', fontsize=14, pad=20)
        
        # Add frequency labels on top of the bars for clarity
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + (0.01 * self.n),
                    f'{int(height)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

        # Formatting the chart
        ax.set_ylim(0, max(counts) * 1.2)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

        # Add a text box for the sample size to make it implicit but visible in the legend/figure
        textstr = f"Sample Size: $n = {self.n}$"
        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,
                verticalalignment='top', bbox=props)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat201:
    def __init__(self):
        # Population parameters
        self.mu = rnd.randint(60, 180)
        self.variance = rnd.randint(25, 225) # Variances like 25, 36, 49... 225
        self.sigma = math.sqrt(self.variance)
        self.n = rnd.randint(30, 80)
        
        # Fundamental property: E(X_bar) = mu
        self.answer = self.mu

        self.description = (
            "The figure illustrates the distribution of a population $X$ and the distribution "
            "of the sample mean $\\bar{X}$ for a sample size $n = " + str(self.n) + "$. "
            "Based on the statistical properties shown, determine the value of $E(\\bar{X})$."
        )
        
        self.topic = "Probability & Statistics 2"
        self.subtopic = "Sampling and estimation"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the figure, the population mean is given as:}} &\\\\"
            f"\\mu &= {round(self.mu, 10)}\\\\"
            f"\\text{{The population variance is given as:}} &\\\\"
            f"\\sigma^2 &= {round(self.variance, 10)}\\\\"
            f"\\text{{For a random sample of size }} n, \\text{{ the sample mean }} \\bar{{X}} \\text{{ is a random variable.}} &\\\\"
            f"\\text{{The expectation of the sample mean, }} E(\\bar{{X}}), \\text{{ is equal to the population mean:}} &\\\\"
            f"E(\\bar{{X}}) &= \\mu\\\\"
            f"\\text{{Substituting the value of }} \\mu: &\\\\"
            f"E(\\bar{{X}}) &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # X-axis range based on mu and sigma
        x = np.linspace(self.mu - 4 * self.sigma, self.mu + 4 * self.sigma, 500)
        
        # Distributions
        y_pop = (1 / (self.sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / self.sigma)**2)
        
        sigma_bar = self.sigma / np.sqrt(self.n)
        y_sample = (1 / (sigma_bar * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mu) / sigma_bar)**2)
        
        # Use legend to pass implicit information
        ax.plot(x, y_pop, label=f'Population $X$ ($\\mu={self.mu}, \\sigma^2={self.variance}$)', color='blue', lw=2)
        ax.plot(x, y_sample, label='Sample Mean $\\bar{X}$', color='red', lw=2, linestyle='--')
        
        # Visual markers
        ax.axvline(self.mu, color='gray', linestyle=':', lw=1.5)
        
        # Plot formatting
        ax.set_yticks([])
        ax.set_title("Population vs. Sampling Distribution", fontsize=14, pad=15)
        ax.legend(loc='upper right', fontsize=10, frameon=True)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        plt.tight_layout()
        
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
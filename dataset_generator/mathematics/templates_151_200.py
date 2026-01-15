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
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
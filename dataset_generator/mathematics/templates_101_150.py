import numpy as np
import pandas as pd
import random as rnd
import os
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrowPatch
from scipy.interpolate import PchipInterpolator
from mathematics.helper import *

# target folder : "root/dataset/mathematics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "mathematics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Mat101:
    
    def __init__(self):
        # Randomized Variables
        self.colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
        self.total_spins = rnd.choice([100, 200, 250, 400, 500])
        
        # Generate random frequencies that sum up to total_spins
        # We create 5 random numbers, normalize them, then scale to total_spins
        raw_freqs = [rnd.random() for _ in range(5)]
        sum_raw = sum(raw_freqs)
        self.frequencies = [int((f / sum_raw) * self.total_spins) for f in raw_freqs]
        
        # Adjust the last frequency to ensure the sum is exactly total_spins due to rounding
        self.frequencies[-1] = self.total_spins - sum(self.frequencies[:-1])
        
        # Select a target color for the question
        self.target_index = rnd.randint(0, 4)
        self.target_color = self.colors[self.target_index]
        self.target_freq = self.frequencies[self.target_index]
        
        # Relative frequency = Frequency of Event / Total Trials
        relative_frequency = self.target_freq / self.total_spins
        self.answer = round(relative_frequency, 3)

        self.description = (
            f"Based on the results in the figure, what is the relative frequency "
            f"that the spinner lands on the color {self.target_color}? "
            "Give your answer correct to 3 decimal places."
        )

        self.topic = "Probability"
        self.subtopic = "Relative and expected frequencies"
        self.source = "Adapted from Cambridge IGCSE Mathematics (0580)"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency of {self.target_color}}} &= {self.target_freq}\\\\"
            f"\\text{{Total spins}} &= {self.total_spins}\\\\"
            f"\\text{{Relative Frequency}} &= \\frac{{\\text{{Frequency of {self.target_color}}}}}{{\\text{{Total spins}}}}\\\\"
            f"&= \\frac{{{self.target_freq}}}{{{self.total_spins}}}\\\\"
            f"&= {round(self.target_freq / self.total_spins, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create a DataFrame for the table
        data = {
            'Color': self.colors,
            'Frequency': self.frequencies
        }
        df = pd.DataFrame(data)

        # Plotting the table
        fig, ax = plt.subplots(figsize=(6, 2)) # Adjust size as needed
        ax.axis('off')
        ax.axis('tight')
        
        # Create table
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        
        # Style the table
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 1.5) # Scale width and height

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat102:
    
    def __init__(self):
        # We need 6 numbers that sum to 100 to represent the frequencies
        # We will generate random weights and normalize them
        weights = [rnd.randint(1, 10) for _ in range(6)]
        total_weight = sum(weights)
        
        # Calculate initial frequencies based on weights
        self.frequencies = [int((w / total_weight) * 100) for w in weights]
        
        # Adjust to ensure the sum is exactly 100 (distribute the remainder)
        remainder = 100 - sum(self.frequencies)
        for i in range(remainder):
            self.frequencies[i % 6] += 1
            
        self.faces = [1, 2, 3, 4, 5, 6]
        
        # Select a target face for the question (e.g., face 6)
        target_face = 6
        target_freq = self.frequencies[target_face - 1]
        
        # Calculate the solution for the question
        total_rolls_scenario = rnd.randint(2, 10) * 100
        expected_freq = (target_freq / 100) * total_rolls_scenario

        self.answer = int(round(expected_freq, 0))

        self.description = (
            f"Using the relative frequency from the chart, calculate the expected frequency of rolling a {target_face} if the die is rolled {total_rolls_scenario} times."
        )

        self.topic = "Probability"
        self.subtopic = "Relative and expected frequencies"
        self.source = "Adapted from Edexcel GCSE Mathematics"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency of rolling a {target_face}}} &= {target_freq}\\\\"
            f"\\text{{Total initial rolls}} &= 100\\\\"
            f"\\text{{Relative frequency}} &= \\frac{{\\text{{Frequency}}}}{{\\text{{Total initial rolls}}}}\\\\"
            f"&= \\frac{{{target_freq}}}{{100}}\\\\"
            f"&= {round(target_freq / 100, 10)}\\\\"
            f"\\text{{Expected frequency}} &= \\text{{Relative frequency}} \\times \\text{{Target rolls}}\\\\"
            f"&= {round(target_freq / 100, 10)} \\times {total_rolls_scenario}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # 2. Create the Figure
        plt.figure(figsize=(8, 6))
        
        # Create bar chart
        bars = plt.bar(self.faces, self.frequencies, color='skyblue', edgecolor='black', zorder=3)
        
        # Formatting
        plt.xlabel('Die Face', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(self.faces)
        plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
        plt.ylim(0, max(self.frequencies) + 5) # Dynamic y-limit based on max value

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height}',
                    ha='center', va='bottom', fontsize=10)

        # Display the plot
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat103:
    
    def __init__(self):
        # M: First catch (marked and released)
        M = rnd.randint(10, 40)
        
        # n: Second catch (total fish in the net)
        self.n = rnd.randint(20, 50)
        
        # m: Recaptured (marked fish found in the second catch)
        # Ensure m is reasonable (less than n and less than M)
        self.m = rnd.randint(3, min(15, M-1, self.n-1))
        
        # Calculate uncaptured in the second catch
        n_uncaptured = self.n - self.m

        approx = (M * self.n) / self.m

        self.answer = int(round(approx, 0))

        self.description = (
            f"A ranger catches {M} fish from the lake, marks them with a tag, and releases them. "
            f"Later, the ranger catches a new sample (shown in the figure above). "
            f"Using the relative frequency of marked fish in the second catch, "
            "estimate the total expected number of fish in the lake."
        )

        self.topic = "Probability"
        self.subtopic = "Relative and expected frequencies"
        self.source = "Adapted from Oxford International AQA Examinations"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Marked fish in first catch }} (M) &= {M}\\\\"
            f"\\text{{Total fish in second catch }} (n) &= {self.n}\\\\"
            f"\\text{{Recaptured marked fish }} (m) &= {self.m}\\\\"
            f"\\text{{Using the capture-recapture formula:}} &\\\\"
            f"\\frac{{m}}{{n}} &= \\frac{{M}}{{N}}\\\\"
            f"N &= \\frac{{M \\times n}}{{m}}\\\\"
            f"&= \\frac{{{M} \\times {self.n}}}{{{self.m}}}\\\\"
            f"&= \\frac{{{M * self.n}}}{{{self.m}}}\\\\"
            f"&= {round((M * self.n) / self.m, 10)}\\\\"
            f"N &\\approx {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # 2. Setup the Plot (The Net)
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Hide axes
        ax.set_axis_off()
        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 11)

        # Draw "The Net" (A circular patch)
        net_circle = patches.Circle((5, 5), 4.5, linewidth=2, edgecolor='#555', facecolor='#e0f7fa', alpha=0.5)
        ax.add_patch(net_circle)
        ax.text(5, 9.8, "The Second Catch (The Net)", ha='center', fontsize=12, fontweight='bold', color='#333')

        # 3. Generate Fish Positions
        # We use rejection sampling or simple random within radius to keep them inside the net
        def get_random_points_in_circle(num_points, center_x, center_y, radius):
            points = []
            while len(points) < num_points:
                x = rnd.uniform(center_x - radius, center_x + radius)
                y = rnd.uniform(center_y - radius, center_y + radius)
                if (x - center_x)**2 + (y - center_y)**2 > (radius - 0.5)**2: # Buffer of 0.5
                    continue
                add = True
                for p in points:
                    if (x - p[0])**2 + (y - p[1])**2 <= 0.5:
                        add = False
                        break
                if add:
                    points.append((x, y))
            return np.array(points)

        # Generate positions for all fish
        all_positions = get_random_points_in_circle(self.n, 5, 5, 4.5)
        
        # Split positions into marked and unmarked
        marked_positions = all_positions[:self.m]
        unmarked_positions = all_positions[self.m:]

        # 4. Draw the Fish
        # Plot Unmarked Fish (Blue)
        ax.scatter(unmarked_positions[:, 0], unmarked_positions[:, 1], 
                s=200, c='#1f77b4', marker='o', edgecolors='black', label='Unmarked Fish', alpha=0.9)
        # Add a simple 'tail' or detail to make it look less like a dot (optional simple visualization)
        ax.scatter(unmarked_positions[:, 0]-0.15, unmarked_positions[:, 1], 
                s=100, c='#1f77b4', marker='<', alpha=0.9) # Tail

        # Plot Marked Fish (Red/Orange with a "Tag")
        ax.scatter(marked_positions[:, 0], marked_positions[:, 1], 
                s=200, c='#ff7f0e', marker='o', edgecolors='red', linewidth=2, label='Marked Fish (Recaptured)', alpha=1.0)
        ax.scatter(marked_positions[:, 0]-0.15, marked_positions[:, 1], 
                s=100, c='#ff7f0e', marker='<', alpha=1.0) # Tail
        
        # 5. Legend and Layout
        ax.legend(loc='lower center', ncol=2, frameon=True, bbox_to_anchor=(0.5, -0.1))
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat104:
    
    def __init__(self):
        # Randomize the core variables (e.g., between 5 and 25 students)
        g9_sci = rnd.randint(5, 25)
        g9_art = rnd.randint(5, 25)
        
        g10_sci = rnd.randint(5, 25)
        g10_art_actual = rnd.randint(5, 25) # This is 'x'
        
        g11_sci = rnd.randint(5, 25)
        g11_art = rnd.randint(5, 25)

        # Row Totals
        total_g9 = g9_sci + g9_art
        total_g10 = g10_sci + g10_art_actual
        total_g11 = g11_sci + g11_art
        
        # Column Totals
        total_sci = g9_sci + g10_sci + g11_sci
        total_art = g9_art + g10_art_actual + g11_art
        
        # Grand Total
        grand_total = total_sci + total_art

        # We replace the actual value of Grade 10 Art with 'x' for the display
        self.data = [
            ["Grade 9", g9_sci, g9_art, total_g9],
            ["Grade 10", g10_sci, "$x$", total_g10],
            ["Grade 11", g11_sci, g11_art, total_g11],
            ["Total", total_sci, total_art, grand_total]
        ]

        self.columns = ["Grade Level", "Science Club", "Art Club", "Total"]

        self.answer = g10_art_actual

        self.description = (
            "Using the data in the figure, determine the number of students in Grade 10 who joined the Art Club (represented by $x$)."
        )

        self.topic = "Statistics"
        self.subtopic = "Interpreting statistical data"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Using the row totals for Grade 10:}} &\\\\"
            f"\\text{{Science}} + \\text{{Art}} &= \\text{{Total}}\\\\"
            f"{g10_sci} + x &= {total_g10}\\\\"
            f"x &= {total_g10} - {g10_sci}\\\\"
            f"x &= {self.answer}\\,\\text{{students}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Figure using Matplotlib
        fig, ax = plt.subplots(figsize=(8, 4)) # Adjust size as needed
        
        # Hide axes (we only want the table)
        ax.axis('tight')
        ax.axis('off')

        # Create the table
        the_table = ax.table(cellText=self.data,
                            colLabels=self.columns,
                            loc='center',
                            cellLoc='center')

        # Styling the Table
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(12)
        the_table.scale(1.2, 2) # Scale width and height of cells

        # Highlight the headers (optional)
        for (i, j), cell in the_table.get_celld().items():
            if i == 0: # Header row
                cell.set_text_props(weight='bold')
                cell.set_facecolor('#e6e6e6') # Light gray background

        # Add Figure Title
        plt.title("Club Membership Data", fontsize=14, pad=20, weight='bold')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat105:
    
    def __init__(self):
        # Define the time slots
        self.times = ["08:00", "10:00", "12:00", "14:00", "16:00"]
        
        # Generate random temperatures in degrees Celsius with a realistic daily pattern
        # (Rise in the morning, peak around noon, drop in the afternoon)
        start_temp = rnd.randint(15, 25)
        
        t1 = start_temp
        t2 = t1 + rnd.randint(1, 4)      # 10:00 (Rising)
        t3 = t2 + rnd.randint(1, 3)      # 12:00 (Peak)
        t4 = t3 - rnd.randint(1, 3)      # 14:00 (Starting to drop or plateau)
        t5 = t4 - rnd.randint(1, 4)      # 16:00 (Dropping)
        
        self.temps = [t1, t2, t3, t4, t5]

        hottest_point = max(self.temps)
        final_point = self.temps[-1]

        self.answer = hottest_point - final_point

        self.description = (
            "The line graph above represents the temperature recorded every two hours in a city over an 8-hour period. "
            "Calculate the total drop in temperature, in degrees Celsius, between the hottest point recorded and the temperature at 16:00."
        )

        self.topic = "Statistics"
        self.subtopic = "Interpreting statistical data"
        self.source = "Adapted from Cambridge IGCSE® Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Hottest point}} &= \\max({self.temps[0]}, {self.temps[1]}, {self.temps[2]}, {self.temps[3]}, {self.temps[4]})\\,^\\circ\\text{{C}}\\\\"
            f"&= {hottest_point}\\,^\\circ\\text{{C}}\\\\"
            f"\\text{{Temperature at 16:00}} &= {final_point}\\,^\\circ\\text{{C}}\\\\"
            f"\\text{{Total drop}} &= \\text{{Hottest point}} - \\text{{Temperature at 16:00}}\\\\"
            f"&= {hottest_point} - {final_point}\\\\"
            f"&= {self.answer}\\,^\\circ\\text{{C}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 6))
        
        # Plotting the line graph with star markers
        plt.plot(self.times, self.temps, marker='*', markersize=12, color='navy', linestyle='-', linewidth=2, label='Temp (°C)')
        
        # Adding titles and labels
        plt.title("Temperature Fluctuation", fontsize=14)
        plt.xlabel("Time", fontsize=12)
        plt.ylabel("Temperature (°C)", fontsize=12)
        
        # Adding a grid for easier reading (similar to graph paper)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Set Y-axis ticks to be integers only
        plt.yticks(range(min(self.temps) - 2, max(self.temps) + 3))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat106:
    
    def __init__(self):
        self.weeks = ['Week 1', 'Week 2', 'Week 3']
        
        # Generate random sales between 20 and 80 for each week
        self.store_a_sales = [rnd.randint(20, 80) for _ in range(3)]
        self.store_b_sales = [rnd.randint(20, 80) for _ in range(3)]

        total_a = sum(self.store_a_sales)
        total_b = sum(self.store_b_sales)
        difference = abs(total_a - total_b)

        self.answer = difference

        self.description = (
            "Using the figure, calculate the difference between the total number of laptops sold by Store A and the total number of laptops sold by Store B over the entire three-week period."
        )

        self.topic = "Statistics"
        self.subtopic = "Interpreting statistical data"
        self.source = "Adapted from Extended Mathematics for IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total Sales (Store A)}} &= {self.store_a_sales[0]} + {self.store_a_sales[1]} + {self.store_a_sales[2]} \\\\"
            f"&= {total_a} \\\\"
            f"\\text{{Total Sales (Store B)}} &= {self.store_b_sales[0]} + {self.store_b_sales[1]} + {self.store_b_sales[2]} \\\\"
            f"&= {total_b} \\\\"
            f"\\text{{Difference}} &= |\\text{{Total Store A}} - \\text{{Total Store B}}| \\\\"
            f"&= |{total_a} - {total_b}| \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        x = np.arange(len(self.weeks))  # Label locations
        width = 0.35  # Width of the bars

        fig, ax = plt.subplots(figsize=(8, 5))
        rects1 = ax.bar(x - width/2, self.store_a_sales, width, label='Store A')
        rects2 = ax.bar(x + width/2, self.store_b_sales, width, label='Store B')

        # Add labels, title, and custom x-axis tick labels
        ax.set_ylabel('Number of Laptops Sold')
        ax.set_title('Weekly Sales Comparison')
        ax.set_xticks(x)
        ax.set_xticklabels(self.weeks)
        ax.legend()

        # Add value labels on top of the bars for clarity
        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat107:
    
    def __init__(self):
        # Generate 11 random test scores between 0 and 100
        self.n_students = 11
        self.scores = [rnd.randint(0, 100) for _ in range(self.n_students)]
        self.scores.sort() # Important: Data must be sorted for quartiles

        # For N=11 (odd):
        # Median is the 6th value.
        # Q1 is the median of the lower 5 values.
        # Q3 is the median of the upper 5 values.

        median_index = len(self.scores) // 2
        # Lower half indices: 0 to 4. Median is at index 2.
        q1 = self.scores[median_index // 2] 
        # Upper half indices: 6 to 10. Median is at index 8.
        q3 = self.scores[median_index + 1 + (median_index // 2)]
        iqr = q3 - q1

        self.answer = iqr

        self.description = (
            "Refer to the figure, which lists the test scores of 11 students sorted in ascending order. Calculate the Interquartile Range (IQR) of this data set."
        )

        self.topic = "Statistics"
        self.subtopic = "Averages and measures of spread"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Sorted Data}} &= \\{{ {', '.join(map(str, self.scores))} \\}}\\\\"
            f"\\text{{The dataset has }} N={self.n_students} \\text{{ values. The median is the 6th value.}}\\\\"
            f"\\text{{Lower Half (first 5 values)}} &= \\{{ {', '.join(map(str, self.scores[:5]))} \\}}\\\\"
            f"Q_1 &= \\text{{Median of Lower Half}} = {self.scores[2]}\\\\"
            f"\\text{{Upper Half (last 5 values)}} &= \\{{ {', '.join(map(str, self.scores[6:]))} \\}}\\\\"
            f"Q_3 &= \\text{{Median of Upper Half}} = {self.scores[8]}\\\\"
            f"IQR &= Q_3 - Q_1\\\\"
            f"&= {self.scores[8]} - {self.scores[2]}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(12, 2))
        ax.axis('off') # Turn off x/y axis

        # Create a table with a single row of data
        the_table = ax.table(cellText=[[str(x) for x in self.scores]],
                            loc='center',
                            cellLoc='center')

        # Style the table
        the_table.scale(1, 2.5) # Stretch height
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(14)

        # Add title
        plt.title(f"Test Scores of {self.n_students} Students", fontsize=16, y=0.8)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat108:
    
    def __init__(self):
        # Random number of categories (rows) between 4 and 6
        num_categories = rnd.randint(4, 6)

        # Generate 'Number of Books' (x) - sequential starting from 1
        self.x_values = np.arange(1, num_categories + 1)

        # Generate 'Frequency' (f) - random integers between 1 and 20
        self.f_values = np.random.randint(1, 20, size=num_categories)

        # Create the Table
        df = pd.DataFrame({
            'Number of Books (x)': self.x_values,
            'Frequency (f)': self.f_values
        })

        # Formula: Mean = sum(x * f) / sum(f)
        total_frequency = np.sum(self.f_values)
        weighted_sum = np.sum(self.x_values * self.f_values)
        mean_books = weighted_sum / total_frequency

        f_expansion = " + ".join([str(f) for f in self.f_values])
        xf_expansion = " + ".join([f"({x} \\cdot {f})" for x, f in zip(self.x_values, self.f_values)])

        self.answer = round(mean_books, 3)

        self.description = (
            "Refer to the figure. Calculate the mean number of books read by the students. Give your answer correct to 3 decimal places."
        )

        self.topic = "Statistics"
        self.subtopic = "Averages and measures of spread"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total Frequency }} (\\sum f) &= {f_expansion}\\\\"
            f"&= {total_frequency}\\\\"
            f"\\text{{Sum of Products }} (\\sum x \\cdot f) &= {xf_expansion}\\\\"
            f"&= {weighted_sum}\\\\"
            f"\\text{{Mean }} (\\bar{{x}}) &= \\frac{{\\sum x \\cdot f}}{{\\sum f}}\\\\"
            f"&= \\frac{{{weighted_sum}}}{{{total_frequency}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 5))
        bars = plt.bar(self.x_values, self.f_values, color='skyblue', edgecolor='black', zorder=3)

        # Add labels and title
        plt.xlabel('Number of Books ($x$)')
        plt.ylabel('Frequency ($f$)')
        plt.title('Number of Books Read by Students')

        # Customize ticks and grid
        plt.xticks(self.x_values)
        plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

        # Optional: Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                    f'{height}', ha='center', va='bottom')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat109:
    
    def __init__(self):
        # Generating random frequencies between 2 and 15 for each group
        freq1 = rnd.randint(2, 15)
        freq2 = rnd.randint(2, 15)
        freq3 = rnd.randint(2, 15)

        self.frequencies = [freq1, freq2, freq3]
        self.intervals = [r'$10 < h \leq 20$', r'$20 < h \leq 30$', r'$30 < h \leq 40$']

        # Calculate an estimate of the mean height
        # For grouped data, we use the midpoint of each class interval.
        # Midpoints: 10-20 -> 15, 20-30 -> 25, 30-40 -> 35
        midpoints = [15, 25, 35]

        # Formula: Sum(Frequency * Midpoint) / Total Frequency
        sum_f_x = sum(f * x for f, x in zip(self.frequencies, midpoints))
        total_frequency = sum(self.frequencies)
        estimated_mean = sum_f_x / total_frequency

        self.answer = round(estimated_mean, 3)

        self.description = (
            "Refer to the figure. Calculate the mean number of books read by the students. Give your answer correct to 3 decimal places."
        )

        self.topic = "Statistics"
        self.subtopic = "Averages and measures of spread"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Midpoints }} (x) &= 15, 25, 35\\\\"
            f"\\text{{Mean }} (\\bar{{x}}) &= \\frac{{\\sum f \\cdot x}}{{\\sum f}}\\\\"
            f"&= \\frac{{({self.frequencies[0]} \\times 15) + ({self.frequencies[1]} \\times 25) + ({self.frequencies[2]} \\times 35)}}{{{self.frequencies[0]} + {self.frequencies[1]} + {self.frequencies[2]}}}\\\\"
            f"&= \\frac{{{self.frequencies[0] * 15} + {self.frequencies[1] * 25} + {self.frequencies[2] * 35}}}{{{sum(self.frequencies)}}}\\\\"
            f"&= \\frac{{{sum(f * x for f, x in zip(self.frequencies, [15, 25, 35]))}}}{{{sum(self.frequencies)}}}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 6))
        bars = plt.bar(self.intervals, self.frequencies, color='#66b3ff', edgecolor='black', width=0.6)

        # Add labels and title
        plt.xlabel(r'Height ($h$ in cm)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.title('Height of Saplings', fontsize=14, fontweight='bold')

        # Add the frequency count on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, height + 0.2, 
                    f'{int(height)}', ha='center', va='bottom', fontsize=11)

        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat110:
    
    def __init__(self):
        # Generate a random number of members (between 10 and 20)
        num_members = np.random.randint(10, 21)
        # Generate random ages between 15 and 65
        self.ages = np.random.randint(15, 66, size=num_members)
        self.ages.sort()

        lowest = self.ages[0]
        highest = self.ages[-1]

        self.answer = int(highest - lowest)

        self.description = (
            "The stem-and-leaf diagram below displays the ages of members in a book club. "
            "Using the provided key, calculate the range of the ages."
        )

        self.topic = "Statistics"
        self.subtopic = "Statistical charts and diagrams"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Highest age}} &= {highest}\\\\"
            f"\\text{{Lowest age}} &= {lowest}\\\\"
            f"\\text{{Range}} &= \\text{{Highest}} - \\text{{Lowest}}\\\\"
            f"&= {highest} - {lowest}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Process Data into Stems and Leaves
        stems = {}
        for age in self.ages:
            stem = age // 10
            leaf = age % 10
            if stem not in stems:
                stems[stem] = []
            stems[stem].append(leaf)
        
        sorted_stems = sorted(stems.keys())

        # Construct the Diagram Text
        # Calculate padding based on the largest stem (usually 1 or 2 digits)
        max_stem_width = len(str(max(sorted_stems)))
        
        diagram_lines = []
        for stem in sorted_stems:
            leaves = stems[stem]
            # Use double spaces to mimic the LaTeX \, spacing
            leaves_str = "  ".join(str(l) for l in leaves)
            # Format: "Stem | Leaves"
            line = f"{stem:>{max_stem_width}} | {leaves_str}"
            diagram_lines.append(line)
        
        diagram_text = "\n".join(diagram_lines)

        # Generate the Key
        # Select a stem/leaf pair from the data to serve as the key (e.g., from the middle)
        key_stem = sorted_stems[len(sorted_stems) // 2]
        key_leaf = stems[key_stem][0]
        key_value = key_stem * 10 + key_leaf
        key_text = f"Key: {key_stem} | {key_leaf} = {key_value} years old"

        # Create the Figure
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')  # Turn off the axis lines

        # Add the Diagram
        # Using 'monospace' font is critical for the stem and leaf alignment
        ax.text(0.2, 0.60, diagram_text, fontsize=16, family='monospace', va='top')

        # Add the Key
        # Position the key below the diagram. 
        # (Adjust the y-coordinate 0.35 if the diagram is very long)
        ax.text(0.2, 0.30, key_text, fontsize=12, va='top')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat111:
    
    def __init__(self):
        # Day names
        self.days = ['Friday', 'Saturday', 'Sunday']
        
        # Generate random data for Friday (The focus of the question)
        # Ensure numbers are nice integers (e.g., steps of 10 or 50) for readability
        self.friday_total = rnd.randint(40, 80) * 10  # e.g., 400 to 800
        self.friday_food = rnd.randint(20, (self.friday_total // 10) - 10) * 10 # Ensure food < total
        friday_drink = self.friday_total - self.friday_food
        
        # Generate random data for other days (Background context)
        saturday_food = rnd.randint(20, 60) * 10
        saturday_drink = rnd.randint(10, 40) * 10
        
        sunday_food = rnd.randint(20, 60) * 10
        sunday_drink = rnd.randint(10, 40) * 10

        # Organize data into lists
        self.food_sales = np.array([self.friday_food, saturday_food, sunday_food])
        self.drink_sales = np.array([friday_drink, saturday_drink, sunday_drink])

        self.answer = friday_drink

        self.description = (
            f"The composite bar chart below shows the total revenue of a store over three days. "
            f"On Friday, the total height of the bar represents ${self.friday_total}. "
            f"What is the value of the 'Drink' sales for that day?"
        )

        self.topic = "Statistics"
        self.subtopic = "Statistical charts and diagrams"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total sales on Friday}} &= \\${self.friday_total}\\\\"
            f"\\text{{Food sales on Friday}} &= \\${self.friday_food}\\\\"
            f"\\text{{Drink sales}} &= \\text{{Total sales}} - \\text{{Food sales}}\\\\"
            f"&= {self.friday_total} - {self.friday_food}\\\\"
            f"&= \\${self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 6))
        
        # Plot 'Food' first (bottom layer)
        p1 = plt.bar(self.days, self.food_sales, color='#4e79a7', label='Food', width=0.5)
        
        # Plot 'Drink' on top of 'Food' (bottom=food_sales)
        p2 = plt.bar(self.days, self.drink_sales, bottom=self.food_sales, color='#f28e2b', label='Drink', width=0.5)

        # 4. Formatting the Figure
        plt.ylabel('Revenue ($)')
        plt.title('Store Revenue: Food vs Drink Sales')
        plt.legend(loc='upper right')
        
        # Add grid on y-axis for easier reading
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Optional: Annotate the specific bar mentioned in the question for clarity
        # Label the Total Height of Friday
        plt.text(0, self.friday_total + 10, f"${self.friday_total}", ha='center', fontweight='bold')
        
        # Label the Food Section of Friday
        plt.text(0, self.friday_food / 2, f"${self.friday_food}", ha='center', color='white', fontweight='bold')

        # Set appropriate y-limit
        max_height = max(self.food_sales + self.drink_sales)
        plt.ylim(0, max_height * 1.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat112:
    
    def __init__(self):
        # Randomize the key (1 symbol = X pizzas). Common pictogram keys: 4, 8, 12, etc.
        self.key_value = rnd.choice([4, 8, 12, 16])
        
        # Define possible partial fractions for the problem (Quarter, Half, Three-Quarters, Full)
        fractions = [0.25, 0.5, 0.75, 1.0]
        fraction_names = {0.25: "one quarter-symbol", 0.5: "half-symbol", 
                        0.75: "three quarter-symbol", 1.0: "full symbol"}
        
        # Randomize Tuesday's sales
        full_symbols_tuesday = rnd.randint(1, 4)  # Between 1 and 4 full pizzas
        fraction_tuesday = rnd.choice(fractions)
        
        total_pizzas_tuesday = (full_symbols_tuesday + fraction_tuesday) * self.key_value
        
        # Generate random data for other days to flesh out the chart
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
        self.data = {}
        
        for day in self.days:
            if day == 'Tuesday':
                self.data[day] = full_symbols_tuesday + fraction_tuesday
            else:
                # Random other days (integers or simple halves for visual variety)
                self.data[day] = rnd.randint(1, 5) + rnd.choice([0, 0.5])

        self.answer = int(total_pizzas_tuesday)

        self.description = (
            f"The pictogram shows pizzas sold on four evenings. "
            f"The key indicates that one full symbol represents {self.key_value} pizzas. "
            f"How many pizzas were sold on Tuesday?"
        )

        self.topic = "Statistics"
        self.subtopic = "Statistical charts and diagrams"
        self.source = "Adapted from Cambridge IGCSE Mathematics 0580 Syllabus"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Value of 1 symbol}} &= {self.key_value}\\,\\text{{pizzas}}\\\\"
            f"\\text{{Symbols on Tuesday}} &= {full_symbols_tuesday} + {fraction_tuesday}\\\\"
            f"&= {round(full_symbols_tuesday + fraction_tuesday, 10)}\\\\"
            f"\\text{{Total pizzas}} &= \\text{{Symbols on Tuesday}} \\times \\text{{Value of 1 symbol}}\\\\"
            f"&= {round(full_symbols_tuesday + fraction_tuesday, 10)} \\times {self.key_value}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Create a simple "Pizza" marker using a circle patch or text
        # Note: For a real image, we would load a .png. Here we draw circles.
        
        y_positions = range(len(self.days))
        ax.set_yticks(y_positions)
        ax.set_yticklabels(self.days[::-1], fontsize=12, fontweight='bold')
        ax.set_xlim(0, max(self.data.values()) + 1)
        ax.set_ylim(-0.5, len(self.days) - 0.5)
        
        # Hide X axis
        ax.get_xaxis().set_visible(False)
        
        # Remove spines
        for spine in ['top', 'right', 'bottom', 'left']:
            ax.spines[spine].set_visible(False)

        # 3. Draw Pictogram
        # We will draw circles to represent pizzas.
        # A full circle is a full pizza. Partial wedges for fractions.
        
        for i, day in enumerate(self.days[::-1]):
            value = self.data[day]
            full_count = int(value)
            partial = value - full_count
            
            # Draw full symbols
            for j in range(full_count):
                # Draw a yellow circle with orange border (Pizza-ish)
                circle = Circle((j + 0.5, i), 0.35, facecolor='gold', edgecolor='orange', linewidth=2)
                ax.add_patch(circle)
                
                # Add "pepperoni" dots for detail
                ax.scatter([j+0.5-0.1, j+0.5+0.1, j+0.5], [i+0.1, i+0.1, i-0.15], 
                        color='darkred', s=20, zorder=2)

            # Draw partial symbol if exists
            if partial > 0:
                # Theta1, Theta2 for wedge (0 to 360)
                # 0.25 -> 90 deg, 0.5 -> 180 deg, etc.
                theta = partial * 360
                wedge = Wedge((full_count + 0.5, i), 0.35, 0, theta, facecolor='gold', edgecolor='orange', linewidth=2)
                ax.add_patch(wedge)

        # 4. Add Key and Text
        plt.title("Pizzas Sold", fontsize=16, pad=20)
        
        # Add Key at the bottom
        key_text = f"KEY:   = {self.key_value} Pizzas"
        # Draw a small example pizza for the key
        key_circle = Circle((0, -1.2), 0.35, facecolor='gold', edgecolor='orange', linewidth=2, clip_on=False)
        ax.add_patch(key_circle)
        # Since we can't easily place patches outside axes in relative coords, we use text annotation for the label
        ax.text(0.5, -1.3, f"= {self.key_value} Pizzas", fontsize=12, ha='left', va='center', transform=ax.transData)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat113:
    
    def __init__(self):
        # Randomize the Target Point P
        # Age between 2 and 8 years, Value between 5k and 20k
        self.target_age = rnd.randint(2, 8)
        self.target_value = 5 * rnd.randint(1, 4)
        
        # Generate Random Data Points (Background Noise)
        # Create 9 other points with a general downward trend (older = cheaper)
        num_points = 9
        self.ages = np.random.uniform(1, 10, num_points)
        
        # Simple linear trend + noise for realism
        # Base formula: Value starts high and decreases by ~2k per year
        self.values = 25 - (2 * self.ages) + np.random.normal(0, 2, num_points)
        
        # Ensure values are positive and reasonable
        self.values = np.clip(self.values, 2, 28)
        
        # Add target point to lists for plotting
        all_ages = np.append(self.ages, self.target_age)
        all_values = np.append(self.values, self.target_value)

        self.answer = self.target_value

        self.description = (
            f"According to the scatter diagram, what is the resale value (in thousands of dollars) of the {self.target_age}-year-old car represented by point P?"
        )

        self.topic = "Statistics"
        self.subtopic = "Scatter diagrams"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the age of the car represented by point P:}} &\\\\"
            f"\\text{{Age (x-axis)}} &= {self.target_age}\\,\\text{{years}}\\\\"
            f"\\text{{Locate point P on the scatter diagram at }} x &= {self.target_age}.\\\\"
            f"\\text{{Read the corresponding value on the vertical axis (y-axis):}} &\\\\"
            f"\\text{{Value}} &= {self.target_value}\\\\"
            f"\\text{{Thus, the resale value is:}} &\\\\"
            f"&= {self.answer}\\,\\text{{thousand dollars}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot background points (blue)
        ax.scatter(self.ages, self.values, color='cornflowerblue', s=80, alpha=0.7, label='Other Cars')
        
        # Plot target point P (red, larger)
        ax.scatter(self.target_age, self.target_value, color='crimson', s=120, zorder=5, label=f'Point P')
        
        # Annotation and Formatting
        # Label Point P
        ax.annotate(f' P', (self.target_age, self.target_value), 
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=14, fontweight='bold', color='crimson')

        # Add dashed lines to axes for readability
        ax.vlines(self.target_age, 0, self.target_value, linestyle='--', color='gray', alpha=0.5)
        ax.hlines(self.target_value, 0, self.target_age, linestyle='--', color='gray', alpha=0.5)

        # Labels and Title
        ax.set_title("Car Age vs. Resale Value", fontsize=16)
        ax.set_xlabel("Age of Car (Years)", fontsize=12)
        ax.set_ylabel("Resale Value ($1000s)", fontsize=12)
        
        # Set Limits and Grid
        ax.set_xlim(0, 11)
        ax.set_ylim(0, 30)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat114:
    
    def __init__(self):
        # Randomize the two key points for the line of best fit
        # Ensure x2 > x1 and y2 > y1 to simulate positive growth (fertilizer effect)
        self.x1 = rnd.randint(5, 15)
        self.y1 = rnd.randint(15, 30)
        
        self.x2 = self.x1 + rnd.randint(15, 25)  # Gap of 15-25 units
        self.y2 = self.y1 + rnd.randint(20, 40)  # Significant growth
        
        # Calculate slope (m) and intercept (c) for the line: y = mx + c
        self.m = (self.y2 - self.y1) / (self.x2 - self.x1)
        self.c = self.y1 - self.m * self.x1
        
        # Randomize the query point (x_query)
        # Pick a value somewhere between x1 and x2
        x_query = rnd.randint(self.x1 + 2, self.x2 - 2)
        y_query = self.m * x_query + self.c

        # Generate "Scatter" data around this line
        # We create random x values and calculate y based on the line + random noise
        num_points = 20
        self.scatter_x = np.linspace(self.x1 - 5, self.x2 + 5, num_points)
        
        # Add randomness to x (so they aren't perfectly spaced)
        self.scatter_x = self.scatter_x + np.random.uniform(-1, 1, size=num_points)
        
        # Calculate y with noise
        noise_level = (self.y2 - self.y1) * 0.15 # Noise relative to the data range
        self.scatter_y = (self.m * self.scatter_x + self.c) + np.random.normal(0, noise_level, size=num_points)

        self.answer = round(y_query, 3)

        self.description = (
            f"Using the line of best fit shown in the figure, calculate the "
            f"predicted height (in cm) of a plant when {x_query} grams of fertilizer are used. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Statistics"
        self.subtopic = "Scatter diagrams"
        self.source = "Adapted from Extended Mathematics for Cambridge IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify two points on the line:}} &\\\\"
            f"(x_1, y_1) &= ({self.x1}, {self.y1})\\\\"
            f"(x_2, y_2) &= ({self.x2}, {self.y2})\\\\"
            f"\\text{{Calculate the slope }} m: &\\\\"
            f"m &= \\frac{{y_2 - y_1}}{{x_2 - x_1}}\\\\"
            f"&= \\frac{{{self.y2} - {self.y1}}}{{{self.x2} - {self.x1}}}\\\\"
            f"&= \\frac{{{self.y2 - self.y1}}}{{{self.x2 - self.x1}}}\\\\"
            f"&= {round(self.m, 10)}\\\\"
            f"\\text{{Calculate the y-intercept }} c: &\\\\"
            f"c &= y_1 - m \\cdot x_1\\\\"
            f"&= {self.y1} - ({round(self.m, 10)})({self.x1})\\\\"
            f"&= {self.y1} - {round(self.m * self.x1, 10)}\\\\"
            f"&= {round(self.c, 10)}\\\\"
            f"\\text{{Equation of the line:}} &\\\\"
            f"y &= {round(self.m, 10)}x + {round(self.c, 10)}\\\\"
            f"\\text{{Calculate height for }} x = {x_query}\\,\\text{{g:}} &\\\\"
            f"y &= {round(self.m, 10)}({x_query}) + {round(self.c, 10)}\\\\"
            f"&= {round(self.m * x_query, 10)} + {round(self.c, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Plot
        plt.figure(figsize=(8, 6))
        
        # Plot Scatter Data
        plt.scatter(self.scatter_x, self.scatter_y, color='gray', alpha=0.6, label='Observed Data')
        
        # Plot the Line of Best Fit (extend slightly beyond x1 and x2)
        line_x = np.array([min(self.scatter_x), max(self.scatter_x)])
        line_y = self.m * line_x + self.c
        plt.plot(line_x, line_y, color='blue', linewidth=2, label='Line of Best Fit')
        
        # Highlight the two specific points mentioned in the problem
        plt.plot([self.x1, self.x2], [self.y1, self.y2], 'ro', zorder=5, label='Reference Points')
        plt.text(self.x1, self.y1 + 2, f'({self.x1}, {self.y1})', fontsize=10, ha='center', color='red')
        plt.text(self.x2, self.y2 - 4, f'({self.x2}, {self.y2})', fontsize=10, ha='center', color='red')

        # Formatting
        plt.title("Plant Height vs. Fertilizer Amount")
        plt.xlabel("Fertilizer (grams)")
        plt.ylabel("Height (cm)")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat115:
    
    def __init__(self):
        # Randomize the "Line of Best Fit" parameters
        # Equation: y = mx + c
        self.slope = round(rnd.uniform(0.8, 1.2), 2)     # Random slope roughly around 1
        self.intercept = rnd.randint(0, 10)              # Random intercept
        
        # Generate Background Data (to make the scatter plot look real)
        # We create random scores for 50 students around the line
        num_students = 50
        self.x_data = np.random.randint(40, 95, num_students)  # Math scores
        noise = np.random.normal(0, 3, num_students)      # Natural variance
        self.y_data = self.slope * self.x_data + self.intercept + noise       # Physics scores
        
        # Define "Student A" (The Target)
        # Pick a Math score (x) within a reasonable middle range
        self.student_a_x = rnd.randint(50, 85)
        
        # Calculate the PREDICTED score (on the line)
        self.student_a_y_predicted = self.slope * self.student_a_x + self.intercept
        
        # Randomize the ACTUAL score (off the line)
        # Ensure the residual is noticeable (at least +/- 8 points away)
        residual_offset = rnd.choice([-1, 1]) * rnd.randint(8, 15)
        self.student_a_y_actual = round(self.student_a_y_predicted + residual_offset, 1)

        self.answer = round(abs(self.student_a_y_actual - self.student_a_y_predicted), 3)

        self.description = (
            f"What is the vertical difference (residual) between Student A's actual Physics score and the score predicted by the line of best fit for a Math score of {self.student_a_x}?"
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Statistics"
        self.subtopic = "Scatter diagrams"
        self.source = "Adapted from Mathematics for the International Student: Mathematics SL"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Line of Best Fit Equation:}} &\\\\"
            f"y &= mx + c\\\\"
            f"y &= {self.slope}x + {self.intercept}\\\\"
            f"\\text{{Calculate the predicted score for }} x &= {self.student_a_x}:\\\\"
            f"y_{{\\text{{predicted}}}} &= {self.slope}({self.student_a_x}) + {self.intercept}\\\\"
            f"&= {round(self.slope * self.student_a_x, 10)} + {self.intercept}\\\\"
            f"&= {round(self.student_a_y_predicted, 10)}\\\\"
            f"\\text{{Identify the actual score:}} &\\\\"
            f"y_{{\\text{{actual}}}} &= {self.student_a_y_actual}\\\\"
            f"\\text{{Calculate the vertical difference (residual):}} &\\\\"
            f"\\text{{Residual}} &= |y_{{\\text{{actual}}}} - y_{{\\text{{predicted}}}}|\\\\"
            f"&= |{self.student_a_y_actual} - {round(self.student_a_y_predicted, 10)}|\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Setup the Plot
        plt.figure(figsize=(10, 6))
        
        # Plot Background Scatter
        plt.scatter(self.x_data, self.y_data, color='lightgray', label='Other Students', alpha=0.6)
        
        # Plot Line of Best Fit
        x_line = np.array([30, 100])
        y_line = self.slope * x_line + self.intercept
        plt.plot(x_line, y_line, color='blue', linewidth=2, label=f'Best Fit: $y = {self.slope}x + {self.intercept}$')
        
        # Plot Student A
        plt.scatter(self.student_a_x, self.student_a_y_actual, color='red', s=100, zorder=5, label='Student A')
        
        # Visualize the Residual (Vertical Line)
        # Draw a dashed line from the actual point to the predicted point on the line
        plt.vlines(x=self.student_a_x, 
                ymin=min(self.student_a_y_actual, self.student_a_y_predicted), 
                ymax=max(self.student_a_y_actual, self.student_a_y_predicted), 
                colors='red', linestyles='--', linewidth=2, label='Residual')

        # Formatting and Annotations
        plt.xlabel("Math Score ($x$)", fontsize=12)
        plt.ylabel("Physics Score ($y$)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.xlim(30, 100)
        plt.ylim(30, 110)
        plt.legend()
        
        # Annotate Student A's coordinates
        sign = abs(self.student_a_y_actual - self.student_a_y_predicted) / (self.student_a_y_actual - self.student_a_y_predicted)
        plt.text(self.student_a_x, self.student_a_y_actual + 3 * sign, 
                f'({self.student_a_x}, {self.student_a_y_actual})', 
                fontsize=10, verticalalignment='center')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat116:
    
    def __init__(self):
        # Random total number of students (e.g., between 150 and 300)
        self.total_students = rnd.randint(150, 300)

        # X-axis points (Marks): Fixed milestones to keep the graph structure similar to the prompt
        self.x_points = np.array([0, 20, 40, 50, 70, 90, 100])

        # Y-axis points (Cumulative Frequency):
        # We need 5 intermediate points between 0 and total_students that are strictly increasing
        intermediate_points = sorted(rnd.sample(range(10, self.total_students - 10), 5))

        # Combine to form the full coordinate set
        self.y_points = np.array([0] + intermediate_points + [self.total_students])

        # Create Smooth Curve (Interpolation)
        # We use PchipInterpolator because it guarantees the curve is monotonic (always goes up),
        # which is required for cumulative frequency.
        interpolator = PchipInterpolator(self.x_points, self.y_points)

        # Generate smooth line data
        self.x_smooth = np.linspace(0, 100, 500)
        self.y_smooth = interpolator(self.x_smooth)

        # Calculate Median
        self.median_y = self.total_students / 2

        # Find the index where y_smooth is closest to median_y
        idx_median = np.argmin(np.abs(self.y_smooth - self.median_y))
        self.median_x = self.x_smooth[idx_median]

        # There'll be a green line showing the median_x and median_y
        # It had to be seen at the graph
        self.answer = round(self.median_x, 1)

        self.description = (
            f"Using the coordinate points provided in the figure, determine the median mark for the students."
            f"Give your answer correct to 1 decimal places."
        )

        self.topic = "Statistics"
        self.subtopic = "Cumulative frequency diagrams"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Total number of students (}} N \\text{{)}} &= {self.total_students}\\\\"
            f"\\text{{The median occurs at half of the total cumulative frequency:}} &\\\\"
            f"\\text{{Median Position}} &= \\frac{{N}}{{2}}\\\\"
            f"&= \\frac{{{self.total_students}}}{{2}}\\\\"
            f"&= {round(self.total_students / 2, 10)}\\\\"
            f"\\text{{Locate }} y &= {round(self.total_students / 2, 10)} \\text{{ on the vertical axis (Cumulative Frequency).}} &\\\\"
            f"\\text{{Read the corresponding value on the horizontal axis (Marks):}} &\\\\"
            f"\\text{{Median}} &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Plotting
        plt.figure(figsize=(10, 6))

        # Plot the smooth curve
        plt.plot(self.x_smooth, self.y_smooth, color='blue', linewidth=1, label='Cumulative Frequency')

        # Plot the specific coordinate points used
        plt.scatter(self.x_points, self.y_points, color='red', zorder=5)

        # Draw Median Lines (Dashed)
        # Horizontal line from Y-axis to curve
        plt.hlines(self.median_y, -10, self.median_x, colors='green', linestyles='dashed')
        # Vertical line from curve to X-axis
        plt.vlines(self.median_x, -10, self.median_y, colors='green', linestyles='dashed')

        # Formatting
        plt.title(f"Cumulative Frequency Diagram (N={self.total_students})", fontsize=14)
        plt.xlabel("Marks (0-100)", fontsize=12)
        plt.ylabel("Cumulative Frequency", fontsize=12)

        # Set limits
        plt.xlim(-10, 110)
        plt.ylim(-10, self.total_students + 10)

        # Set x-axis ticks to increments of 10
        plt.xticks(np.arange(-10, 111, 5))

        # Add Grid
        plt.grid(True, which='both', linestyle='--', alpha=0.7)

        # Show the specific points as text
        for i, (x, y) in enumerate(zip(self.x_points, self.y_points)):
            plt.text(x, y + (self.total_students*0.025), f"({x},{y})", fontsize=8, ha='center')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat117:
    
    def __init__(self):
        self.total_frequency = 80
        
        # Calculate Y-axis positions for quartiles
        self.y_q1 = 0.25 * self.total_frequency  # Lower Quartile position (25% of 80 = 20)
        self.y_median = 0.50 * self.total_frequency # Median position
        self.y_q3 = 0.75 * self.total_frequency  # Upper Quartile position (75% of 80 = 60)

        # Randomize X-axis values (Heights in cm)
        # We ensure they are strictly increasing: Min < Q1 < Median < Q3 < Max
        self.h_min = rnd.randint(5, 15)
        self.h_q1 = rnd.randint(self.h_min + 5, self.h_min + 15)      # Q1 Height
        self.h_median = rnd.randint(self.h_q1 + 5, self.h_q1 + 15)    # Median Height
        self.h_q3 = rnd.randint(self.h_median + 10, self.h_median + 20) # Q3 Height
        self.h_max = rnd.randint(self.h_q3 + 5, self.h_q3 + 15)

        # Calculate the Answer (IQR)
        iqr = self.h_q3 - self.h_q1

        # For Q1, it will be shown by a green dashed line
        # For Q3, it will be shown by a red dashed line
        self.answer = iqr

        self.description = (
            f"Calculate the Interquartile Range (IQR) of the plant heights based on the data provided in the figure."
        )

        self.topic = "Statistics"
        self.subtopic = "Cumulative frequency diagrams"
        self.source = "Adapted from Extended Mathematics for IGCSE"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Position of Lower Quartile }} (Q_1) &= 0.25 \\times {self.total_frequency} = {round(self.y_q1, 10)}\\\\"
            f"\\text{{Reading from the graph at frequency }} {round(self.y_q1, 10)}: &\\\\"
            f"Q_1 &= {self.h_q1}\\,\\text{{cm}}\\\\"
            f"\\text{{Position of Upper Quartile }} (Q_3) &= 0.75 \\times {self.total_frequency} = {round(self.y_q3, 10)}\\\\"
            f"\\text{{Reading from the graph at frequency }} {round(self.y_q3, 10)}: &\\\\"
            f"Q_3 &= {self.h_q3}\\,\\text{{cm}}\\\\"
            f"\\text{{Interquartile Range (IQR)}} &= Q_3 - Q_1\\\\"
            f"&= {self.h_q3} - {self.h_q1}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Curve Data
        # Define the key anchor points (x, y)
        x_points = [self.h_min, self.h_q1, self.h_median, self.h_q3, self.h_max]
        y_points = [0, self.y_q1, self.y_median, self.y_q3, self.total_frequency]

        # Create a smooth curve using PchipInterpolator (preserves monotonicity)
        # This ensures the graph never goes "down", which is impossible for cumulative freq.
        interpolator = PchipInterpolator(x_points, y_points)
        
        # Generate dense points for plotting the smooth line
        x_smooth = np.linspace(self.h_min, self.h_max, 300)
        y_smooth = interpolator(x_smooth)

        # Plotting
        plt.figure(figsize=(10, 6))
        
        # Plot the main curve
        plt.plot(x_smooth, y_smooth, color='blue', linewidth=2, label='Cumulative Frequency')

        # Add guidelines for Q1
        plt.hlines(y=self.y_q1, xmin=0, xmax=self.h_q1, colors='green', linestyles='dashed')
        plt.vlines(x=self.h_q1, ymin=0, ymax=self.y_q1, colors='green', linestyles='dashed')
        plt.text(0, self.y_q1 + 1, f'20 (25%)', color='green', va='bottom', fontsize=9)

        # Add guidelines for Q3
        plt.hlines(y=self.y_q3, xmin=0, xmax=self.h_q3, colors='red', linestyles='dashed')
        plt.vlines(x=self.h_q3, ymin=0, ymax=self.y_q3, colors='red', linestyles='dashed')
        plt.text(0, self.y_q3 + 1, f'60 (75%)', color='red', va='bottom', fontsize=9)

        # Formatting the Graph
        plt.title(f"Cumulative Frequency of Plant Heights (N={self.total_frequency})")
        plt.xlabel("Height (cm)")
        plt.ylabel("Cumulative Frequency")
        plt.xlim(0, self.h_max + 5)
        plt.xticks(np.arange(0, self.h_max + 6, 2)) # Set x-axis ticks to increments of 2
        plt.ylim(0, self.total_frequency + 5)
        plt.grid(True, alpha=0.3)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat118:
    
    def __init__(self):
        # Random start for the class interval (e.g., between 0 and 50)
        self.start_x = rnd.randint(0, 50)

        # Random width for the class interval (e.g., between 5 and 30)
        self.width = rnd.randint(5, 30)
        self.end_x = self.start_x + self.width

        # Random Frequency Density (e.g., between 0.5 and 5.0, rounded to 1 decimal)
        self.freq_density = round(rnd.uniform(0.5, 5.0), 1)

        # Calculate the Answer (Frequency)
        # Formula: Frequency = Frequency Density * Class Width
        frequency = self.freq_density * self.width

        self.answer = round(frequency, 1)

        self.description = (
            f"Calculate the frequency of the data represented by this bar. Give your answer correct to 1 decimal place."
        )

        self.topic = "Statistics"
        self.subtopic = "Histograms"
        self.source = "Adapted from Cambridge IGCSE Mathematics Core and Extended Coursebook"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Class Width}} &= {self.end_x} - {self.start_x}\\\\"
            f"&= {self.width}\\\\"
            f"\\text{{Frequency}} &= \\text{{Frequency Density}} \\times \\text{{Class Width}}\\\\"
            f"&= {self.freq_density} \\times {self.width}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Create the Figure
        fig, ax = plt.subplots(figsize=(8, 6))

        # Plot the bar
        # We use align='edge' so the bar starts exactly at 'start_x'
        ax.bar(self.start_x, self.freq_density, width=self.width, align='edge',
            color='skyblue', edgecolor='black', alpha=0.7)

        # Add freq_density text at the top of the bar
        ax.text(self.start_x + self.width / 2, self.freq_density + 0.1, f'{self.freq_density}',
                ha='center', va='bottom', fontsize=10, color='black')

        # Formatting the Plot to look like a Textbook Question
        ax.set_xlabel("Class Interval ($x$)", fontsize=12)
        ax.set_ylabel("Frequency Density", fontsize=12)

        # Set axis limits to give some breathing room
        ax.set_xlim(0, self.start_x + self.end_x)
        ax.set_ylim(0, self.freq_density + 1)

        # Add grid for easier reading
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Add specific ticks for the interval start and end
        current_xticks = list(ax.get_xticks())
        # Ensure our start and end points are explicitly labeled
        important_ticks = sorted(list(set([0, self.start_x, self.end_x])))
        ax.set_xticks(important_ticks)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat119:
    
    def __init__(self):
        # Define 3 random widths (e.g., between 5 and 20)
        self.widths = [rnd.randint(2, 4) * 5 for _ in range(3)] 
        
        # Define 3 random densities (e.g., 0.5, 1.0, ..., 5.0)
        self.densities = [rnd.choice([x / 5 for x in range(1, 26)]) for _ in range(3)]
        
        # Calculate Interval Boundaries
        self.boundaries = [0]
        current_x = 0
        for w in self.widths:
            current_x += w
            self.boundaries.append(current_x)
            
        # Calculate Total Frequency (The Answer)
        # Frequency = Width * Frequency Density
        frequencies = [w * h for w, h in zip(self.widths, self.densities)]
        total_frequency = sum(frequencies)

        self.answer = int(round(total_frequency, 0))

        self.description = (
            f"What is the total frequency of the data represented by these three bars?"
        )

        self.topic = "Statistics"
        self.subtopic = "Histograms"
        self.source = "Adapted from Cambridge IGCSE Mathematics"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency}} &= \\text{{Width}} \\times \\text{{Frequency Density}} \\\\"
            f"\\text{{Total Frequency}} &= ({self.widths[0]} \\times {self.densities[0]}) + ({self.widths[1]} \\times {self.densities[1]}) + ({self.widths[2]} \\times {self.densities[2]}) \\\\"
            f"&= {round(self.widths[0] * self.densities[0], 10)} + {round(self.widths[1] * self.densities[1], 10)} + {round(self.widths[2] * self.densities[2], 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        # Generate the Plot
        fig, ax = plt.subplots(figsize=(8, 5))

        # Plot bars: x needs the left edges, width needs the specific bar widths
        # align='edge' makes the bar start at x and extend right by 'width'
        ax.bar(x=self.boundaries[:-1], height=self.densities, width=self.widths, 
            align='edge', color='skyblue', edgecolor='black', alpha=0.7)

        # Formatting to match Exam Style
        ax.set_title("Frequency Density vs Interval", fontsize=14)
        ax.set_xlabel("Variable $x$ (Intervals)", fontsize=12)
        ax.set_ylabel("Frequency Density", fontsize=12)
        
        # Set X-ticks exactly at the boundaries so students can read widths easily
        ax.set_xticks(self.boundaries)
        
        # Add grid for readability
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        
        for i, (w, h) in enumerate(zip(self.widths, self.densities)):
            mid_point = self.boundaries[i] + (w / 2)
            ax.text(mid_point, h + 0.05, f"{h}", ha='center', fontweight='bold')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat120:
    
    def __init__(self):
        # We choose specific widths common in exams (5, 10, 15, 20)
        possible_widths = [5, 10, 15, 20]
        
        # Generate Group A
        self.width_a = rnd.choice(possible_widths)
        self.height_a = rnd.randint(2, 8) # Randomize height (Freq Density) directly for integer results
        self.freq_a = self.width_a * self.height_a
        
        # Generate Group B (ensure it's different enough to be interesting)
        self.width_b = rnd.choice(possible_widths)
        self.height_b = rnd.randint(2, 8)
        
        # Ensure heights are not equal so there is always a difference
        while self.height_b == self.height_a:
            self.height_b = rnd.randint(2, 8)
        
        self.freq_b = self.width_b * self.height_b

        # Calculate the answer
        diff = abs(self.height_b - self.height_a)

        self.answer = diff

        self.description = (
            f"If these groups are plotted on the same histogram, "
            f"what is the positive difference between the height of the bar for Group B and Group A?"
        )

        self.topic = "Statistics"
        self.subtopic = "Histograms"
        self.source = "Adapted from Cambridge Assessment International Education"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Frequency Density (Height)}} &= \\frac{{\\text{{Frequency}}}}{{\\text{{Width}}}}\\\\"
            f"\\text{{Height}}_A &= \\frac{{{self.freq_a}}}{{{self.width_a}}} = {round(self.freq_a / self.width_a, 10)}\\\\"
            f"\\text{{Height}}_B &= \\frac{{{self.freq_b}}}{{{self.width_b}}} = {round(self.freq_b / self.width_b, 10)}\\\\"
            f"\\text{{Difference}} &= |\\text{{Height}}_B - \\text{{Height}}_A|\\\\"
            f"&= |{round(self.freq_b / self.width_b, 10)} - {round(self.freq_a / self.width_a, 10)}|\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))

        # Data for plotting
        # We plot Group A starting at x=0, and Group B starting immediately after A
        x_start_a = 0
        x_start_b = self.width_a 
        
        # Plot Bar A
        ax.bar(x=x_start_a, height=self.height_a, width=self.width_a, align='edge', 
            color='#4c72b0', edgecolor='black', alpha=0.7, label='Group A')
        
        # Plot Bar B
        ax.bar(x=x_start_b, height=self.height_b, width=self.width_b, align='edge', 
            color='#dd8452', edgecolor='black', alpha=0.7, label='Group B')

        # Annotations to help visualize the math
        # Label for Group A
        ax.text(x_start_a + self.width_a/2, self.height_a/2, 
                f'Freq= {self.freq_a}', 
                ha='center', va='center', color='white', fontweight='bold')

        # Label for Group B
        ax.text(x_start_b + self.width_b/2, self.height_b/2, 
                f'Freq= {self.freq_b}', 
                ha='center', va='center', color='white', fontweight='bold')

        # Visualizing the difference line
        max_h = max(self.height_a, self.height_b)
        min_h = min(self.height_a, self.height_b)
        
        # Draw a dashed line to show the difference
        ax.hlines(y=min_h, xmin=0, xmax=self.width_a+self.width_b, colors='gray', linestyles='dashed')
        
        # Formatting
        ax.set_title("Frequency Density Comparison")
        ax.set_xlabel("Class Interval (Variable)")
        ax.set_ylabel("Frequency Density (Height)")
        ax.set_xlim(-2, self.width_a + self.width_b + 10) # Add space for the arrow
        ax.set_ylim(0, max_h + 2)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        ax.legend()

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat121:
    
    def __init__(self):
        # We work backwards to ensure the solution lies on integer coordinates (readable graph)

        # The question asks for f(g(start_x))
        self.start_x = rnd.randint(1, 6)

        # Define g(x) logic
        # g(x) must take start_x and output an 'intermediate' integer
        self.intermediate_val = rnd.randint(1, 6)

        # Pick a second point for g(x) to define the line
        # Ensure x2 is different from start_x
        self.g_x2 = self.start_x
        while self.g_x2 == self.start_x:
            self.g_x2 = rnd.randint(0, 8)
        self.g_y2 = rnd.randint(0, 8)

        # Points for g(x): (start_x, intermediate_val) and (g_x2, g_y2)
        # Equation g(x): y - y1 = m(x - x1)
        self.m_g = (self.g_y2 - self.intermediate_val) / (self.g_x2 - self.start_x)
        self.c_g = self.intermediate_val - (self.m_g * self.start_x)

        # Define f(x) logic
        # f(x) must take 'intermediate_val' (which is the output of g) as its input
        # and produce a 'final_ans'
        self.final_ans = rnd.randint(0, 8)

        # Pick a second point for f(x) to define the line
        # Ensure f_x2 is different from intermediate_val
        self.f_x2 = self.intermediate_val
        while self.f_x2 == self.intermediate_val:
            self.f_x2 = rnd.randint(0, 8)
        self.f_y2 = rnd.randint(0, 8)

        # Points for f(x): (intermediate_val, final_ans) and (f_x2, f_y2)
        self.m_f = (self.f_y2 - self.final_ans) / (self.f_x2 - self.intermediate_val)
        self.c_f = self.final_ans - (self.m_f * self.intermediate_val)

        self.answer = self.final_ans

        self.description = (
            f"Using the graphs described in the figure, evaluate the composite function $f(g({self.start_x}))$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{To evaluate the composite function }} f(g({self.start_x})), \\text{{ we work from the inside out.}}\\\\"
            f"\\text{{Step 1: Evaluate the inner function, }} g(x), \\text{{ at }} x = {self.start_x}.\\\\"
            f"\\text{{From the graph of }} g(x), \\text{{ the corresponding y-value is:}}\\\\"
            f"g({self.start_x}) &= {self.intermediate_val}\\\\"
            f"\\text{{Step 2: Substitute this result into the outer function, }} f(x).\\\\"
            f"f(g({self.start_x})) &= f({self.intermediate_val})\\\\"
            f"\\text{{Step 3: Evaluate }} f(x) \\text{{ at }} x = {self.intermediate_val}.\\\\"
            f"\\text{{From the graph of }} f(x), \\text{{ the corresponding y-value is:}}\\\\"
            f"f({self.intermediate_val}) &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        plt.figure(figsize=(8, 8))

        # Define x range for plotting lines
        x_range = np.linspace(-2, 10, 100)

        # Calculate y values
        y_f = self.m_f * x_range + self.c_f
        y_g = self.m_g * x_range + self.c_g

        # Plot Lines
        plt.plot(x_range, y_f, label=f'$f(x)$', color='blue', linewidth=2)
        plt.plot(x_range, y_g, label=f'$g(x)$', color='red', linewidth=2)

        # Plot the specific integer points (to make it look like a textbook problem)
        # f(x) points
        plt.scatter([self.intermediate_val, self.f_x2], [self.final_ans, self.f_y2], color='blue', zorder=5)
        # g(x) points
        plt.scatter([self.start_x, self.g_x2], [self.intermediate_val, self.g_y2], color='red', zorder=5)

        # Add text labels for the scatter points
        plt.text(self.intermediate_val, self.final_ans + 0.2, f'({self.intermediate_val}, {self.final_ans})', color='blue', fontsize=9)
        plt.text(self.f_x2, self.f_y2 + 0.2, f'({self.f_x2}, {self.f_y2})', color='blue', fontsize=9)
        plt.text(self.start_x, self.intermediate_val + 0.2, f'({self.start_x}, {self.intermediate_val})', color='red', fontsize=9)
        plt.text(self.g_x2, self.g_y2 + 0.2, f'({self.g_x2}, {self.g_y2})', color='red', fontsize=9)


        # Grid configuration
        plt.grid(True, which='both', linestyle='--', linewidth=0.7)
        plt.axhline(0, color='black', linewidth=1.5)
        plt.axvline(0, color='black', linewidth=1.5)

        # Limits and Ticks (Integer ticks are crucial for reading graphs)
        plt.xticks(np.arange(-2, 11, 1))
        plt.yticks(np.arange(-5, 11, 1))
        plt.xlim(-1, 9)
        plt.ylim(-2, 9)

        plt.legend(fontsize=12)
        plt.title("Graphs of $f(x)$ and $g(x)$")
        plt.xlabel("$x$")
        plt.ylabel("$y$")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat122:
    
    def __init__(self):
        # Randomize variables (Ensure a != b for clarity)
        self.a = rnd.randint(2, 4)
        self.b = rnd.randint(6, 9)
        if self.a == self.b: self.b += 2  # Force difference if they collide

        # x = f(a) = b
        self.answer = self.b

        self.description = (
            f"Based on the relationship between a function and its inverse shown in the figure, determine the value of $x$ such that $f^{{-1}}(x) = {self.a}$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Functions"
        self.source = "Adapted from Pure Mathematics 1 for Cambridge International AS & A Level"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the graph of }} f(x), \\text{{ we identify the point:}}\\\\"
            f"(x, y) &= ({self.a}, {self.b})\\\\"
            f"\\text{{This relationship can be written as:}}\\\\"
            f"f({self.a}) &= {self.b}\\\\"
            f"\\text{{By the definition of an inverse function:}}\\\\"
            f"y = f(x) &\\iff x = f^{{-1}}(y)\\\\"
            f"\\text{{Applying this to our values:}}\\\\"
            f"{self.a} &= f^{{-1}}({self.b})\\\\"
            f"\\text{{The problem asks for }} x \\text{{ such that }} f^{{-1}}(x) = {self.a}.\\\\"
            f"\\text{{By comparison:}}\\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )

    # Define the function f(x) and its inverse
    # We use a shifted cubic function to ensure it is one-to-one (monotonic) 
    # and passes exactly through (a, b).
    # Formula: f(x) = (x - a)^3 + b
    # Inverse: f^-1(x) = cbrt(x - b) + a
    def f(self, x):
        return 0.5 * (x - self.a)**3 + self.b

    def f_inv(self, x):
        # np.cbrt handles negative cube roots correctly
        return np.cbrt((x - self.b) / 0.5) + self.a

    def generate(self, num):
        # Setup Plot Range
        limit = max(self.a, self.b) + 3
        x = np.linspace(-1, limit, 400)
        
        plt.figure(figsize=(10, 8))
        
        # Filter y-values to keep plot within reasonable bounds
        y_f = self.f(x)
        mask_f = (y_f > -5) & (y_f < limit + 2)
        plt.plot(x[mask_f], y_f[mask_f], 'b-', linewidth=2, label='$y = f(x)$')
        
        y_inv = self.f_inv(x)
        mask_inv = (y_inv > -5) & (y_inv < limit + 2)
        plt.plot(x[mask_inv], y_inv[mask_inv], 'r-', linewidth=2, label='$y = f^{-1}(x)$')

        # Add Key Points and Annotations
        
        # Point on f(x): (a, b)
        plt.plot(self.a, self.b, 'bo', markersize=8)
        plt.text(self.a - 0.5, self.b + 0.5, f'({self.a}, {self.b})', color='blue', fontsize=12, fontweight='bold')
        
        # Point on f^-1(x): (b, a) -> The target of the question
        plt.plot(self.b, self.a, 'ro', markersize=8)
        plt.text(self.b + 0.5, self.a, f'(?, {self.a})', color='red', fontsize=12, fontweight='bold')

        # Visual Guide Lines (Dotted)
        plt.vlines(self.a, 0, self.b, colors='blue', linestyles=':', alpha=0.5)
        plt.hlines(self.b, 0, self.a, colors='blue', linestyles=':', alpha=0.5)
        
        plt.vlines(self.b, 0, self.a, colors='red', linestyles=':', alpha=0.5)
        plt.hlines(self.a, 0, self.b, colors='red', linestyles=':', alpha=0.5)

        # Styling and Question Text
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xlim(-1, limit)
        plt.ylim(-1, limit)
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat123:
    
    def __init__(self):
        # Original Vertex (h, k)
        self.h = rnd.randint(-4, 4)
        self.k = rnd.randint(-4, 4)
        
        # Transformation parameters: f(x - a) + b
        # Shift 'a' (horizontal) and 'b' (vertical)
        # Excluding 0 to ensure a visible transformation
        self.a = rnd.choice([i for i in range(-5, 6) if i != 0])
        self.b = rnd.choice([i for i in range(-5, 6) if i != 0])
        
        # Calculate new vertex for the transformed graph g(x)
        self.new_h = self.h + self.a
        self.new_k = self.k + self.b

        self.answer = self.new_k

        sign_a = '-' if self.a > 0 else '+'
        sign_b = '+' if self.b > 0 else '-'
        label_g = f'$g(x) = f(x {sign_a} {abs(self.a)}) {sign_b} {abs(self.b)}$'

        self.description = (
            f"The figure illustrates the graph of a quadratic function $y = f(x)$ which has a minimum turning point at the coordinate $({self.h}, {self.k})$. The figure also indicates a second dashed curve representing a transformation {label_g}. "
            f"Calculate the $y$-coordinate of the minimum point of the transformed graph $g(x)$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge International AS and A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Original vertex coordinates}} &= ({self.h}, {self.k})\\\\"
            f"\\text{{Vertical translation }} (b) &= {self.b}\\\\"
            f"\\text{{The new }} y\\text{{-coordinate is given by:}} &\\\\"
            f"y_{{new}} &= k + b\\\\"
            f"&= {self.k} + ({self.b})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Define range for x
        # Center the plot between the two vertices and add padding
        center_x = (self.h + self.new_h) / 2
        span_x = max(abs(self.new_h - self.h), 4) * 1.5
        x = np.linspace(center_x - span_x, center_x + span_x, 500)
        
        # f(x) = (x - h)^2 + k  (Base quadratic)
        f_x = (x - self.h)**2 + self.k
        
        # g(x) = f(x - a) + b
        #      = ((x - a) - h)^2 + k + b
        #      = (x - (h + a))^2 + (k + b)
        g_x = (x - self.new_h)**2 + self.new_k

        # Create Figure
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot f(x) (Original)
        ax.plot(x, f_x, label=r'$f(x)$', color='blue', linewidth=2)
        # Mark original vertex
        ax.plot(self.h, self.k, 'o', color='blue')
        ax.text(self.h, self.k - 0.5 if self.k < 0 else self.k + 0.5, f'({self.h}, {self.k})', 
                ha='center', va='top' if self.k < 0 else 'bottom', color='blue', fontweight='bold')

        # Plot g(x) (Transformed)
        # Determine sign for label: f(x - 3) vs f(x + 3)
        sign_a = '-' if self.a > 0 else '+'
        sign_b = '+' if self.b > 0 else '-'
        label_g = f'$g(x) = f(x {sign_a} {abs(self.a)}) {sign_b} {abs(self.b)}$'
        
        ax.plot(x, g_x, label=label_g, linestyle='--', color='red', linewidth=2)
        
        # Formatting
        ax.set_xlabel("$x$", fontsize=12)
        ax.set_ylabel("$y$", fontsize=12)
        
        # Draw axes through origin
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        
        # Grid and limits
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(fontsize=11)
        
        # Adjust Y-limits to make the graph look nice
        y_min = min(self.k, self.new_k) - 5
        y_max = max(self.k, self.new_k) + 10
        ax.set_ylim(y_min, y_max)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat124:
    
    def __init__(self):
        # We use the vertex form: f(x) = a(x - h)^2 + v
        # To ensure integer arithmetic is clean, we stick to integers.
        self.h = rnd.choice([i for i in range(-8, 9) if i != 0])   # x-coordinate of vertex (axis of symmetry)
        self.v = rnd.randint(-5, 5)   # y-coordinate of vertex
        self.a = rnd.choice([1])      # Coefficient (kept as 1 for simplicity, like the example)
        
        # Format the equation string for display
        # Handles signs: e.g., (x - (-2)) becomes (x + 2)
        op = "+" if self.h < 0 else "-"
        v_op = "+" if self.v >= 0 else "-"
        
        self.equation_latex = f"f(x) = (x {op} {abs(self.h)})^2 {v_op} {abs(self.v)}"

        self.answer = self.h

        self.description = (
            f"The figure shows the full parabola of the function: ${self.equation_latex}$. "
            f"The axis of symmetry $x = {self.h}$ is marked with a dotted line. "
            f"Determine the smallest integer value for $k$ such that the "
            f"function $f(x)$ is a one-one function for the domain $x \\ge k$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Functions"
        self.source = "Adapted from Nelson Mathematics for Cambridge International A Level: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given the function:}} &\\\\"
            f"{self.equation_latex.replace('=', '&=')}\\\\"
            f"\\text{{The function is in the vertex form:}} &\\\\"
            f"f(x) &= a(x - h)^2 + v\\\\"
            f"\\text{{Identifying the axis of symmetry }} x = h: &\\\\"
            f"h &= {self.h}\\\\"
            f"\\text{{A parabola is a one-to-one function on the domain }} x \\ge h. &\\\\"
            f"\\text{{Therefore, the smallest integer }} k \\text{{ is:}} &\\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Generate x values centered around the axis of symmetry
        x = np.linspace(self.h - 6, self.h + 6, 400)
        y = self.a * (x - self.h)**2 + self.v
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot the full parabola
        ax.plot(x, y, label=f'${self.equation_latex}$', linewidth=2, color='blue')
        
        # Plot the Axis of Symmetry
        ax.axvline(x=self.h, color='red', linestyle='--', label=f'Axis of Symmetry $x={self.h}$')
        
        # Styling the plot
        ax.set_title(f"Graph of ${self.equation_latex}$")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right')
        
        # Ensure axes are readable based on random values
        ax.set_xlim(self.h - 7, self.h + 7)
        ax.set_ylim(min(y) - 2, max(y) + 2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat125:
    
    def __init__(self):
        # We work backwards to ensure integer answers.
        # Choose a scale factor 'k' for y = h(kx) (e.g., 2, 3, or 0.5)
        k_options = [2, 3, 4] 
        self.k = rnd.choice(k_options)
        
        # Choose the 'new' intercept first (the answer), so the 'original' intercept is a multiple of k
        answer_intercept = rnd.randint(1, 4)
        self.original_intercept = answer_intercept * self.k

        self.answer = answer_intercept

        self.description = (
            f"The blue solid line in the figure displays the graph of y = h(x), "
            f"which intersects the positive x-axis at x = {self.original_intercept}. "
            f"The red dashed line represents the transformation y = h({self.k}x). "
            f"Find the x-intercept of the transformed graph y = h({self.k}x)."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Functions"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The x-intercept of the original function }} y = h(x) \\text{{ is }} x &= {self.original_intercept}\\\\"
            f"\\text{{This implies that:}} &\\\\"
            f"h({self.original_intercept}) &= 0\\\\"
            f"\\text{{For the transformed function }} y = h({self.k}x)\\text{{, we find the x-intercept by setting }} y &= 0:\\\\"
            f"h({self.k}x) &= 0\\\\"
            f"\\text{{Since }} h({self.original_intercept}) = 0\\text{{, we equate the arguments:}} &\\\\"
            f"{self.k}x &= {self.original_intercept}\\\\"
            f"x &= \\frac{{{self.original_intercept}}}{{{self.k}}}\\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )

    # Define the abstract function h(x). 
    # A simple inverted parabola shifted to hit the original_intercept works well visually.
    # h(x) = -(x - original_intercept) * np.cbrt(x + 16)
    def h(self, x):
        return -1 * (x - self.original_intercept) * np.cbrt(x + 16)

    def generate(self, num):
        # Setup the Plot
        x_max = self.original_intercept + 2
        x = np.linspace(-3, x_max, 400)
        
        plt.figure(figsize=(10, 6))
        
        # Plot Original Graph y = h(x)
        plt.plot(x, self.h(x), label=r'$y = h(x)$', color='blue', linewidth=2)
        
        # Plot Transformed Graph y = h(kx)
        # We calculate the y values by passing (k*x) into the function h
        plt.plot(x, self.h(self.k * x), label=fr'$y = h({self.k}x)$', color='red', linestyle='--', linewidth=2)
        
        # Styling the Axes
        ax = plt.gca()
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        plt.grid(True, linestyle=':', alpha=0.6)
        
        # Annotate the known intercept (Original)
        plt.plot(self.original_intercept, 0, 'bo') # Blue dot
        plt.annotate(f'{self.original_intercept}', 
                    (self.original_intercept, 0), 
                    textcoords="offset points", 
                    xytext=(5, 10), 
                    ha='center', color='blue', fontweight='bold')

        # Add limits to make it look nice
        plt.xlim(-3, x_max + 1)
        # Dynamic y-limits based on the peak of the curve
        y_peak = np.max(self.h(x))
        plt.ylim(-y_peak/2, y_peak + (y_peak/4))
        
        plt.legend(loc='upper right')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat126:
    
    def __init__(self):
        # Triples format: (a, b, r) where a^2 + b^2 = r^2
        triples = [(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (8, 15, 17), (6, 8, 10)]
        dx, dy, self.r = rnd.choice(triples)
        
        # Randomly flip signs to vary the quadrant relative to center
        dx = dx * rnd.choice([1, -1])
        dy = dy * rnd.choice([1, -1])
        
        # Randomize Center (h, k) within a reasonable range for plotting
        self.h = rnd.randint(2, 8)
        self.k = rnd.randint(5, 10)
        
        # Calculate Point P coordinates
        self.px = self.h + dx
        self.py = self.k + dy
        
        # Slope of the radius line (center to P): m_radius = dy / dx
        m_radius = dy / dx
        
        # Slope of the tangent (perpendicular to radius): m_tangent = -1 / m_radius
        self.m_tangent = -1 / m_radius
        
        # Equation of tangent: y - py = m_tangent * (x - px)
        # To find y-intercept, set x = 0: y_int = py - m_tangent * px
        self.y_intercept = self.py - (self.m_tangent * self.px)

        self.answer = round(self.y_intercept, 3)

        self.description = (
            f"A circle is defined by the equation $(x - {self.h})^2 + (y - {self.k})^2 = {self.r**2}$. "
            f"A tangent line touches this circle at the point $P({self.px}, {self.py})$. "
            f"Determine the $y$-intercept of this tangent line. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Coordinate geometry"
        self.source = "Adapted from Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Identify the center }} (h, k) \\text{{ and point }} P(x_1, y_1):&\\\\"
            f"C &= ({self.h}, {self.k})\\\\"
            f"P &= ({self.px}, {self.py})\\\\"
            f"\\text{{Find the slope of the radius }} (m_r):&\\\\"
            f"m_r &= \\frac{{y_1 - k}}{{x_1 - h}} = \\frac{{{self.py} - {self.k}}}{{{self.px} - {self.h}}} = \\frac{{{self.py - self.k}}}{{{self.px - self.h}}}\\\\"
            f"\\text{{The tangent is perpendicular to the radius, so }} m_t \\cdot m_r = -1:&\\\\"
            f"m_t &= -\\frac{{1}}{{m_r}} = -\\frac{{{self.px - self.h}}}{{{self.py - self.k}}}\\\\"
            f"&= {round(self.m_tangent, 10)}\\\\"
            f"\\text{{Find the y-intercept }} (c) \\text{{ using }} y = m_t x + c:&\\\\"
            f"c &= y_1 - m_t x_1\\\\"
            f"&= {self.py} - ({round(self.m_tangent, 10)})({self.px})\\\\"
            f"&= {self.py} - ({round(self.m_tangent * self.px, 10)})\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Plot Circle
        circle = Circle((self.h, self.k), self.r, fill=False, color='blue', linewidth=1.5, label='Circle')
        ax.add_patch(circle)
        ax.plot(self.h, self.k, 'bo', markersize=5) # Center dot
        ax.text(self.h, self.k-0.1*self.r, f'C({self.h}, {self.k})', ha='center', va='top', fontsize=10, color='blue')
        
        # Plot Point P
        ax.plot(self.px, self.py, 'ro', markersize=5, zorder=5) # Point P
        ax.text(self.px + 0.5, self.py, f'P({self.px}, {self.py})', ha='left', va='center', fontsize=10, color='red')
        
        # Plot Tangent Line
        # We create x-values for the line to span across the y-axis
        x_line = np.linspace(min(-2, self.px-self.r-2), max(self.px+5, self.h+self.r+2), 100)
        y_line = self.m_tangent * (x_line - self.px) + self.py
        ax.plot(x_line, y_line, 'r--', linewidth=1.5, label='Tangent Line')
        
        # Plot Radius (dashed, for visual context)
        ax.plot([self.h, self.px], [self.k, self.py], 'b:', linewidth=1)
        
        # Highlight Y-intercept
        ax.plot(0, self.y_intercept, 'go', markersize=5)
        ax.text(0.5, self.y_intercept + 0.5, f'y-int?', ha='left', va='center', fontsize=10, color='green')

        # Formatting plot
        ax.axhline(0, color='black', linewidth=1) # X-axis
        ax.axvline(0, color='black', linewidth=1) # Y-axis
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.6)
        
        ax.legend()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat127:
    
    def __init__(self):
        # Random radius (integer between 3 and 10)
        self.r = rnd.randint(3, 10)
        
        # Random slope (m) between -3 and 3 (avoiding 0 for better visual)
        self.m = rnd.choice([-3, -2, -1, 1, 2, 3])
        
        # Random y-intercept (c)
        # To ensure the line intersects the circle at two distinct points,
        # the distance from origin to line (d) must be < radius.
        # d = |c| / sqrt(m^2 + 1)  =>  |c| < r * sqrt(m^2 + 1)
        limit_c = int(self.r * np.sqrt(self.m**2 + 1)) - 1
        self.c = rnd.randint(-limit_c, limit_c)

        # Circle: x^2 + y^2 = r^2
        # Line: y = mx + c
        # Substitute y: x^2 + (mx + c)^2 = r^2
        # Quadratic form: (1 + m^2)x^2 + (2mc)x + (c^2 - r^2) = 0
        
        A_quad = 1 + self.m**2
        B_quad = 2 * self.m * self.c
        C_quad = self.c**2 - self.r**2
        
        delta = B_quad**2 - 4 * A_quad * C_quad
        
        # Calculate x coordinates of intersections
        self.x1 = (-B_quad - np.sqrt(delta)) / (2 * A_quad)
        self.x2 = (-B_quad + np.sqrt(delta)) / (2 * A_quad)
        
        # Calculate y coordinates
        self.y1 = self.m * self.x1 + self.c
        self.y2 = self.m * self.x2 + self.c
        
        # Calculate Squared Length of Chord AB: (x2-x1)^2 + (y2-y1)^2
        answer_ab_squared = (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2

        self.answer = round(answer_ab_squared, 3)
        
        # Format the equation strings for display
        line_eq = f"y = {self.m}x + {self.c}" if self.c >= 0 else f"y = {self.m}x - {abs(self.c)}"
        circle_eq = f"x^2 + y^2 = {self.r**2}"

        self.description = (
            f"The straight line ${line_eq}$ intersects the circle ${circle_eq}$ "
            f"at two distinct points, $A$ and $B$. "
            f"Calculate the squared length of the chord $AB$ (i.e., find $AB^2$). "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Coordinate geometry"
        self.source = "Adapted from Cambridge International AS and A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Line equation:}} &\\quad y = {self.m}x + {self.c} \\\\"
            f"\\text{{Circle equation:}} &\\quad x^2 + y^2 = {self.r**2} \\\\"
            f"\\text{{Substitute }} y \\text{{ into the circle equation:}} &\\\\"
            f"x^2 + ({self.m}x + {self.c})^2 &= {self.r**2} \\\\"
            f"x^2 + ({self.m**2}x^2 + {2*self.m*self.c}x + {self.c**2}) - {self.r**2} &= 0 \\\\"
            f"({1 + self.m**2})x^2 + {2*self.m*self.c}x + ({self.c**2 - self.r**2}) &= 0 \\\\"
            f"\\text{{Identify coefficients }} A, B, C: &\\\\"
            f"A = {1 + self.m**2}, \\quad B = {2*self.m*self.c}, \\quad C &= {self.c**2 - self.r**2} \\\\"
            f"\\text{{Calculate discriminant }} \\Delta: &\\\\"
            f"\\Delta = B^2 - 4AC &= ({2*self.m*self.c})^2 - 4({1 + self.m**2})({self.c**2 - self.r**2}) \\\\"
            f"&= {round((2*self.m*self.c)**2 - 4*(1 + self.m**2)*(self.c**2 - self.r**2), 10)} \\\\"
            f"\\text{{Solve for }} x \\text{{ using quadratic formula:}} &\\\\"
            f"x &= \\frac{{-B \\pm \\sqrt{{\\Delta}}}}{{2A}} \\\\"
            f"x_1 &= \\frac{{-{2*self.m*self.c} - \\sqrt{{{round((2*self.m*self.c)**2 - 4*(1 + self.m**2)*(self.c**2 - self.r**2), 10)}}}}}{{2({1 + self.m**2})}} \\approx {round(self.x1, 10)} \\\\"
            f"x_2 &= \\frac{{-{2*self.m*self.c} + \\sqrt{{{round((2*self.m*self.c)**2 - 4*(1 + self.m**2)*(self.c**2 - self.r**2), 10)}}}}}{{2({1 + self.m**2})}} \\approx {round(self.x2, 10)} \\\\"
            f"\\text{{Find corresponding }} y \\text{{ coordinates:}} &\\\\"
            f"y_1 &= {self.m}({round(self.x1, 10)}) + {self.c} \\approx {round(self.y1, 10)} \\\\"
            f"y_2 &= {self.m}({round(self.x2, 10)}) + {self.c} \\approx {round(self.y2, 10)} \\\\"
            f"\\text{{Calculate squared length }} AB^2: &\\\\"
            f"AB^2 &= (x_2 - x_1)^2 + (y_2 - y_1)^2 \\\\"
            f"&= ({round(self.x2, 10)} - {round(self.x1, 10)})^2 + ({round(self.y2, 10)} - {round(self.y1, 10)})^2 \\\\"
            f"&= {round((self.x2 - self.x1)**2, 10)} + {round((self.y2 - self.y1)**2, 10)} \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Draw Circle
        circle_patch = Circle((0, 0), self.r, fill=False, color='teal', linewidth=2, label='Circle')
        ax.add_patch(circle_patch)
        
        # Draw Line
        # Create x-range slightly larger than radius for the line
        x_vals = np.linspace(-self.r-2, self.r+2, 100)
        y_vals = self.m * x_vals + self.c
        ax.plot(x_vals, y_vals, color='orange', linewidth=2, label='Line')
        
        # Draw Chord AB (connect the dots)
        ax.plot([self.x1, self.x2], [self.y1, self.y2], color='red', linestyle='--', linewidth=2, label='Chord AB')
        
        # Mark Points A and B
        ax.scatter([self.x1, self.x2], [self.y1, self.y2], color='black', s=50, zorder=5)
        
        # Annotate Points with offset
        offset = self.r * 0.1
        ax.text(self.x1 + offset, self.y1, '$A$', fontsize=12, fontweight='bold')
        ax.text(self.x2 + offset, self.y2, '$B$', fontsize=12, fontweight='bold')

        # Grid and Setup
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.6)
        
        # Set limits with some padding
        ax.set_xlim(-self.r-3, self.r+3)
        ax.set_ylim(-self.r-3, self.r+3)
        
        ax.legend(loc='upper right')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat128:
    
    def __init__(self):
        # We ensure x1 != x2 to avoid division by zero (vertical line segment)
        # We ensure y1 != y2 to avoid a horizontal segment (which results in a vertical bisector)
        while True:
            self.x1 = rnd.randint(1, 9)
            self.y1 = rnd.randint(2, 8)
            self.x2 = self.x1 + rnd.choice([-1, 1]) * rnd.randint(3, 7)
            self.y2 = self.y1 + rnd.choice([-1, 1]) * rnd.randint(3, 7)
            
            if self.x1 != self.x2 and self.y1 != self.y2:
                break
                
        A = np.array([self.x1, self.y1])
        B = np.array([self.x2, self.y2])

        # Midpoint
        midpoint = (A + B) / 2
        self.mx, self.my = midpoint

        # Slope of AB (m1)
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)
        
        # Slope of Perpendicular Bisector (m2)
        # Perpendicular slope is negative reciprocal
        self.m2 = -1 / m1
        
        # Calculate Intersection with x-axis (Point P)
        # Equation of bisector: y - my = m2(x - mx)
        # Set y = 0 to find x-intercept: -my = m2(x - mx) -> x = mx - (my/m2)
        self.p_x = self.mx - (self.my / self.m2)

        self.answer = round(self.p_x, 3)

        self.description = (
            f"Consider the line segment connecting points $A({self.x1}, {self.y1})$ and $B({self.x2}, {self.y2})$. "
            f"The perpendicular bisector of the line segment $AB$ intersects the x-axis at a point $P$. "
            f"Determine the x-coordinate of $P$. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Coordinate geometry"
        self.source = "Adapted from Pure Mathematics 1 for Cambridge International AS & A Level"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Midpoint }} M &= \\left(\\frac{{x_1 + x_2}}{{2}}, \\frac{{y_1 + y_2}}{{2}}\\right)\\\\"
            f"&= \\left(\\frac{{{self.x1} + {self.x2}}}{{2}}, \\frac{{{self.y1} + {self.y2}}}{{2}}\\right)\\\\"
            f"&= ({round(self.mx, 10)}, {round(self.my, 10)})\\\\"
            f"\\text{{Slope of }} AB, m_1 &= \\frac{{y_2 - y_1}}{{x_2 - x_1}}\\\\"
            f"&= \\frac{{{self.y2} - {self.y1}}}{{{self.x2} - {self.x1}}}\\\\"
            f"&= {round(m1, 10)}\\\\"
            f"\\text{{Slope of bisector, }} m_2 &= -\\frac{{1}}{{m_1}}\\\\"
            f"&= {round(self.m2, 10)}\\\\"
            f"\\text{{Equation of bisector:}} &\\\\"
            f"y - y_M &= m_2(x - x_M)\\\\"
            f"y - {round(self.my, 10)} &= {round(self.m2, 10)}(x - {round(self.mx, 10)})\\\\"
            f"\\text{{At x-axis (}}y=0\\text{{):}} &\\\\"
            f"-{round(self.my, 10)} &= {round(self.m2, 10)}(x - {round(self.mx, 10)})\\\\"
            f"x &= {round(self.mx, 10)} - \\frac{{{round(self.my, 10)}}}{{{round(self.m2, 10)}}}\\\\"
            f"x &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Create Figure
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot Segment AB
        ax.plot([self.x1, self.x2], [self.y1, self.y2], 'o-', color='blue', label='Segment AB', markersize=6)
        ax.text(self.x1, self.y1 + 0.5, f' A({self.x1},{self.y1})', color='blue', fontsize=10, fontweight='bold')
        ax.text(self.x2, self.y2 + 0.5, f' B({self.x2},{self.y2})', color='blue', fontsize=10, fontweight='bold')

        # Plot Midpoint
        ax.plot(self.mx, self.my, 'o', color='green', markersize=6)
        ax.text(self.mx, self.my + 0.5, ' M', color='green', fontsize=10)

        # Plot Perpendicular Bisector Line
        # We calculate plotting limits to ensure the line looks nice
        x_range_min = min(self.x1, self.x2, self.p_x) - 2
        x_range_max = max(self.x1, self.x2, self.p_x) + 2
        
        line_x = np.linspace(x_range_min, x_range_max, 100)
        line_y = self.m2 * (line_x - self.mx) + self.my
        
        ax.plot(line_x, line_y, '--', color='red', label='Perpendicular Bisector')

        # Plot Point P (x-intercept)
        ax.plot(self.p_x, 0, 'o', color='red', markersize=8, label='Point P')
        ax.text(self.p_x, -1, f'P', color='red', fontsize=10, ha='center', fontweight='bold')

        # Formatting the Graph
        ax.axhline(0, color='black', linewidth=1) # x-axis
        ax.axvline(0, color='black', linewidth=1) # y-axis
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        ax.set_aspect('equal') # Important to make perpendicular lines look perpendicular
        ax.set_title("Perpendicular Bisector Visualization")
        
        # Dynamic limits
        ax.set_ylim(min(0, self.y1, self.y2, np.min(line_y)) - 2, max(self.y1, self.y2, np.max(line_y)) + 2)
        ax.set_xlim(x_range_min, x_range_max)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat129:
    
    def __init__(self):
        # Random radius between 2 and 9
        self.r = rnd.randint(2, 9)
        
        # Random y-coordinate for the center (y_c). 
        # We ensure it's > r so the circle doesn't touch the x-axis (strictly touching y-axis only for this problem logic)
        self.y_c = rnd.randint(self.r + 2, self.r + 8)
        
        # Calculate values for the equation (x - k)^2 + (y - b)^2 = r^2
        r_squared = self.r**2
        
        # The logic: If a circle in the 1st quadrant touches the y-axis, 
        # the x-coordinate of the center (k) must equal the radius (r).
        self.k_hidden = self.r

        self.answer = self.k_hidden

        self.description = (
            f"A circle with the equation $(x-k)^2 + (y-{self.y_c})^2 = {r_squared}$ "
            f"lies entirely in the first quadrant and touches the y-axis at exactly one point. "
            f"Find the value of $k$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Coordinate geometry"
        self.source = "Adapted from AS and A Level Mathematics Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The equation of the circle is given by:}} &\\\\"
            f"(x - k)^2 + (y - {self.y_c})^2 &= {self.r**2}\\\\"
            f"\\text{{Comparing this to the standard circle equation }} (x - x_c)^2 + (y - y_c)^2 = r^2: &\\\\"
            f"r^2 &= {self.r**2} \\implies r = \\sqrt{{{self.r**2}}} = {self.r}\\\\"
            f"\\text{{The center of the circle is }} (k, {self.y_c}). &\\\\"
            f"\\text{{Since the circle lies in the first quadrant and touches the y-axis,}} &\\\\"
            f"\\text{{the x-coordinate of the center must be equal to the radius.}} &\\\\"
            f"k &= r\\\\"
            f"k &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Draw the Circle
        # Center is at (k_hidden, y_c)
        circle = Circle((self.k_hidden, self.y_c), self.r, color='#3498db', fill=True, alpha=0.2, linewidth=0)
        circle_outline = Circle((self.k_hidden, self.y_c), self.r, color='#2980b9', fill=False, linewidth=2)
        ax.add_patch(circle)
        ax.add_patch(circle_outline)
        
        # Draw Center Point
        ax.plot(self.k_hidden, self.y_c, 'ro', markersize=6, label='Center $(k, y_{center})$')
        
        # Draw Radius Line (showing distance to y-axis)
        ax.hlines(self.y_c, 0, self.k_hidden, colors='green', linestyles='--', label=f'Radius = {self.r}')
        
        # Draw Tangent Point on Y-axis
        ax.plot(0, self.y_c, 'go', markersize=6) # Tangent point
        
        # Annotations
        ax.text(self.k_hidden + 0.5, self.y_c, f'Center\n(k, {self.y_c})', fontsize=10, verticalalignment='center')
        ax.text(self.k_hidden / 2, self.y_c + 0.5, 'r', fontsize=12, color='green', fontweight='bold')
        
        # Set Axis Limits & Spines
        limit = max(self.k_hidden + self.r, self.y_c + self.r) + 2
        ax.set_xlim(-1, limit)
        ax.set_ylim(-1, limit)
        ax.set_aspect('equal')
        
        # Move left and bottom spines to x = 0 and y = 0
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # Add grid and labels
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right')
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat130:
    
    def __init__(self):
        while True:
            # Generate random coordinates between -8 and 8 to keep plot readable
            self.ax, self.ay = rnd.randint(-8, 8), rnd.randint(-8, 8)
            self.bx, self.by = rnd.randint(-8, 8), rnd.randint(-8, 8)
            self.cx, self.cy = rnd.randint(-8, 8), rnd.randint(-8, 8)
            
            # Calculate Area using the Shoelace Formula
            # Area = 0.5 * |x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B)|
            determinant = (self.ax * (self.by - self.cy) + self.bx * (self.cy - self.ay) + self.cx * (self.ay - self.by))
            area = 0.5 * abs(determinant)
            
            # Ensure area is not 0 (collinear) and reasonably large for visibility
            if area > 20.0:
                break

        self.answer = area

        self.description = (
            f"A triangle is formed by the vertices $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, and $C({self.cx}, {self.cy})$. "
            f"Calculate the exact area of triangle $ABC$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Coordinate geometry"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\frac{{1}}{{2}} |x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B)|\\\\"
            f"&= \\frac{{1}}{{2}} |{self.ax}({self.by} - {self.cy}) + {self.bx}({self.cy} - {self.ay}) + {self.cx}({self.ay} - {self.by})|\\\\"
            f"&= \\frac{{1}}{{2}} |{self.ax}({self.by - self.cy}) + {self.bx}({self.cy - self.ay}) + {self.cx}({self.ay - self.by})|\\\\"
            f"&= \\frac{{1}}{{2}} |{round(self.ax * (self.by - self.cy), 10)} + {round(self.bx * (self.cy - self.ay), 10)} + {round(self.cx * (self.ay - self.by), 10)}|\\\\"
            f"&= \\frac{{1}}{{2}} |{round(self.ax * (self.by - self.cy) + self.bx * (self.cy - self.ay) + self.cx * (self.ay - self.by), 10)}|\\\\"
            f"&= \\frac{{1}}{{2}} \\times {abs(round(self.ax * (self.by - self.cy) + self.bx * (self.cy - self.ay) + self.cx * (self.ay - self.by), 10))}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, plot_ax = plt.subplots(figsize=(6, 6))
        
        # Coordinates list (repeat first point at the end to close the shape)
        x_vals = [self.ax, self.bx, self.cx, self.ax]
        y_vals = [self.ay, self.by, self.cy, self.ay]
        
        # Plot edges and vertices
        plot_ax.plot(x_vals, y_vals, marker='o', color='blue', linewidth=2, markersize=6)
        
        # Fill the triangle area
        plot_ax.fill(x_vals, y_vals, color='skyblue', alpha=0.3)
        
        # Annotate vertices with labels and coordinates
        # We add a small offset to text so it doesn't overlap the dot perfectly
        text_offset = 0.5
        plot_ax.text(self.ax, self.ay + text_offset, f'$A({self.ax}, {self.ay})$', fontsize=10, ha='center', fontweight='bold')
        plot_ax.text(self.bx, self.by + text_offset, f'$B({self.bx}, {self.by})$', fontsize=10, ha='center', fontweight='bold')
        plot_ax.text(self.cx, self.cy + text_offset, f'$C({self.cx}, {self.cy})$', fontsize=10, ha='center', fontweight='bold')
        
        # Configure Axes (Grid, Origin lines, Aspect Ratio)
        plot_ax.axhline(0, color='black', linewidth=1)
        plot_ax.axvline(0, color='black', linewidth=1)
        plot_ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        plot_ax.set_aspect('equal') # Essential for geometry figures to look correct
        
        # Set dynamic limits with some padding
        all_x = [self.ax, self.bx, self.cx]
        all_y = [self.ay, self.by, self.cy]
        padding = 2
        plot_ax.set_xlim(min(all_x) - padding, max(all_x) + padding)
        plot_ax.set_ylim(min(all_y) - padding, max(all_y) + padding)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat131:
    
    def __init__(self):
        # Radius: integer between 3 and 15
        self.r_val = rnd.randint(3, 15)
        # Theta: float between 1.0 and 5.0 (rounded to 1 decimal place)
        # Avoiding extremely small or large angles for better visualization
        self.theta_val = round(rnd.uniform(1.0, 5.0), 1)
        
        # 2. Calculate Properties
        # Perimeter of Sector = 2*r + arc_length = 2*r + r*theta
        perimeter = 2 * self.r_val + (self.r_val * self.theta_val)
        
        # Square side length (Perimeter = 4*s)
        self.square_side = perimeter / 4.0
        
        # Area of the Square
        square_area = self.square_side ** 2

        self.answer = round(square_area, 3)

        self.description = (
            f"A sector of a circle is defined by a radius r = {self.r_val} cm "
            f"and a central angle θ = {self.theta_val} radians. "
            f"A separate square is constructed such that its total perimeter "
            f"is exactly equal to the total perimeter of the sector. "
            f"Determine the area of the square in cm². "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Circular measure"
        self.source = "Adapted from Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Perimeter of sector}} &= 2r + r\\theta\\\\"
            f"&= 2({self.r_val}) + ({self.r_val})({self.theta_val})\\\\"
            f"&= {2 * self.r_val} + {round(self.r_val * self.theta_val, 10)}\\\\"
            f"&= {round(2 * self.r_val + self.r_val * self.theta_val, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Perimeter of square}} &= 4s\\\\"
            f"4s &= {round(2 * self.r_val + self.r_val * self.theta_val, 10)}\\\\"
            f"s &= \\frac{{{round(2 * self.r_val + self.r_val * self.theta_val, 10)}}}{{4}}\\\\"
            f"s &= {round((2 * self.r_val + self.r_val * self.theta_val) / 4, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Area of square}} &= s^2\\\\"
            f"&= ({round((2 * self.r_val + self.r_val * self.theta_val) / 4, 10)})^2\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^2"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_aspect('equal')
        ax.axis('off')
        
        # --- Draw Sector (Left Side) ---
        # Center of sector
        sector_center = (0, 0)
        # Visual scaling factor (to keep plot bounds reasonable regardless of random values)
        scale = 1.0 
        
        # Matplotlib Wedge takes degrees. 
        # We center the angle around 90 degrees (vertical) for a nice look, 
        # or start at 0. Let's start at 0 for standard math diagram look.
        theta_deg = np.degrees(self.theta_val)
        
        wedge = patches.Wedge(
            center=sector_center, 
            r=self.r_val, 
            theta1=0, 
            theta2=theta_deg, 
            color='#a8dadc', 
            alpha=0.6,
            lw=2, ec='#1d3557' # Edge color
        )
        ax.add_patch(wedge)
        
        # Label r and theta
        # Label radius on the bottom line
        ax.text(self.r_val/2, -0.15 * self.r_val, f"r={self.r_val}", ha='center', va='top', fontsize=12, color='#1d3557')
        # Label angle
        angle_text_r = self.r_val * 0.3
        angle_text_x = angle_text_r * np.cos(self.theta_val/2)
        angle_text_y = angle_text_r * np.sin(self.theta_val/2)
        ax.text(angle_text_x, angle_text_y, f"θ={self.theta_val}", ha='center', va='center', fontsize=10)

        # --- Draw Equals Sign and Text (Middle) ---
        # Calculate an offset based on r_val to place the square
        offset_x = self.r_val * 2.5
        
        ax.text(self.r_val * 1.5, self.r_val/2, "=", ha='center', va='center', fontsize=30, fontweight='bold')
        ax.text(self.r_val * 1.5, self.r_val/2 + self.r_val*0.2, "Equal Perimeters", ha='center', va='bottom', fontsize=10, style='italic')

        # --- Draw Square (Right Side) ---
        # Bottom left corner of the square
        sq_x = offset_x
        sq_y = 0 
        
        square = patches.Rectangle(
            (sq_x, sq_y), 
            self.square_side, 
            self.square_side, 
            color='#f4a261', 
            alpha=0.6,
            lw=2, ec='#e76f51'
        )
        ax.add_patch(square)
        
        # Label the square
        ax.text(sq_x + self.square_side/2, -0.15 * self.square_side, f"s = ?", ha='center', va='top', fontsize=12, color='#e76f51')
        ax.text(sq_x + self.square_side/2, self.square_side/2, "Square", ha='center', va='center', fontsize=10, color='white', fontweight='bold')

        # Adjust Plot Limits to fit everything nicely
        all_x = [0, self.r_val, sq_x + self.square_side]
        all_y = [0, self.r_val, self.square_side]
        
        # Add a buffer
        buff = max(self.r_val, self.square_side) * 1
        ax.set_xlim(min(all_x) - buff, max(all_x) + buff)
        ax.set_ylim(min(all_y) - buff, max(all_y) + buff)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat132:
    
    def __init__(self):
        # We pick the 'answer' (r) first to ensure the math works out cleanly.
        self.r_answer = rnd.randint(10, 25)        # The hidden inner radius (e.g., 10 to 25 cm)
        self.width = rnd.randint(4, 10)            # The width of the wiper blade (e.g., 4 to 10 cm)
        self.theta_rad = round(rnd.uniform(1.2, 2.0), 1) # Central angle in radians (e.g., 1.2 to 2.0)

        # Formula for Area of Annulus Sector: A = 0.5 * theta * (R_outer^2 - R_inner^2)
        # Where R_outer = r + width, R_inner = r
        self.outer_radius = self.r_answer + self.width
        area = 0.5 * self.theta_rad * (self.outer_radius**2 - self.r_answer**2)
        
        # Format area to 2 decimal places to look like a textbook problem
        self.area_display = f"{area:.2f}"

        self.answer = self.r_answer

        self.description = (
            f"A rear window wiper for a car clears a region shaped like part of an annulus (a ring). "
            f"This region is formed by two concentric arcs with the same central angle: "
            f"θ = {self.theta_rad} radians. "
            f"The inner radius of the cleaned region is 'r' cm. "
            f"The outer radius is (r + {self.width}) cm. "
            f"If the total area of the cleaned region (the shaded area) is exactly {self.area_display} cm², "
            f"calculate the value of the inner radius 'r'."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Circular measure"
        self.source = "Adapted from Cambridge International AS and A Level Mathematics: Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Formula for Area of Annulus Sector:}} &\\\\"
            f"A &= \\frac{{1}}{{2}} \\theta (R_{{\\text{{outer}}}}^2 - R_{{\\text{{inner}}}}^2) \\\\"
            f"\\text{{Given: }} R_{{\\text{{inner}}}} &= r, \\quad R_{{\\text{{outer}}}} = r + {self.width} \\\\"
            f"\\text{{Substitute values:}} &\\\\"
            f"{self.area_display} &= \\frac{{1}}{{2}} ({self.theta_rad}) \\left( (r + {self.width})^2 - r^2 \\right) \\\\"
            f"{self.area_display} &= {round(0.5 * self.theta_rad, 10)} \\left( (r^2 + {2 * self.width}r + {self.width**2}) - r^2 \\right) \\\\"
            f"{self.area_display} &= {round(0.5 * self.theta_rad, 10)} ({2 * self.width}r + {self.width**2}) \\\\"
            f"\\frac{{{self.area_display}}}{{{round(0.5 * self.theta_rad, 10)}}} &= {2 * self.width}r + {self.width**2} \\\\"
            f"{round(float(self.area_display) / (0.5 * self.theta_rad), 10)} &= {2 * self.width}r + {self.width**2} \\\\"
            f"{2 * self.width}r &= {round(float(self.area_display) / (0.5 * self.theta_rad), 10)} - {self.width**2} \\\\"
            f"{2 * self.width}r &= {round((float(self.area_display) / (0.5 * self.theta_rad)) - self.width**2, 10)} \\\\"
            f"r &= \\frac{{{round((float(self.area_display) / (0.5 * self.theta_rad)) - self.width**2, 10)}}}{{{2 * self.width}}} \\\\"
            f"r &= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 5))
        
        # Define angles to center the wiper upwards (90 degrees)
        theta_deg = np.degrees(self.theta_rad)
        start_angle = 90 - (theta_deg / 2)
        end_angle = 90 + (theta_deg / 2)
        
        # Draw the Shaded Annulus Sector (The "Wiper" path)
        # Wedge(center, r, theta1, theta2, width=width_of_ring)
        # Note: 'r' in Wedge is the OUTER radius, 'width' is the thickness moving inward.
        wiper_patch = patches.Wedge(
            center=(0, 0), 
            r=self.outer_radius, 
            theta1=start_angle, 
            theta2=end_angle, 
            width=self.width, 
            facecolor='#AEEEEE',  # Light Cyan
            edgecolor='black',
            linewidth=1.5,
            alpha=0.8
        )
        ax.add_patch(wiper_patch)

        # Draw an arrow from center to the start of the inner arc
        inner_arc_x = self.r_answer * np.cos(np.radians(start_angle))
        inner_arc_y = self.r_answer * np.sin(np.radians(start_angle))
        ax.annotate(
            text='', xy=(inner_arc_x, inner_arc_y), xytext=(0, 0),
            arrowprops=dict(arrowstyle='<->', color='blue')
        )
        # Place text 'r' at midpoint of that line
        ax.text(inner_arc_x/2 - 1, inner_arc_y/2, 'r', color='blue', fontsize=12, weight='bold')

        # Draw arrow extending from inner arc to outer arc on the right side
        outer_arc_x = self.outer_radius * np.cos(np.radians(end_angle))
        outer_arc_y = self.outer_radius * np.sin(np.radians(end_angle))
        inner_arc_end_x = self.r_answer * np.cos(np.radians(end_angle))
        inner_arc_end_y = self.r_answer * np.sin(np.radians(end_angle))
        
        ax.annotate(
            text='', xy=(outer_arc_x, outer_arc_y), xytext=(inner_arc_end_x, inner_arc_end_y),
            arrowprops=dict(arrowstyle='<->', color='red')
        )
        # Label the width value
        mid_width_x = (self.r_answer + self.width/2) * np.cos(np.radians(end_angle))
        mid_width_y = (self.r_answer + self.width/2) * np.sin(np.radians(end_angle))
        ax.text(mid_width_x + 1, mid_width_y, f'{self.width} cm', color='red', fontsize=10, weight='bold')

        # Draw a small arc near the origin
        arc_radius = self.r_answer * 0.4
        angle_arc = patches.Arc((0,0), arc_radius*2, arc_radius*2, 
                                theta1=start_angle, theta2=end_angle, color='green', linestyle='--')
        ax.add_patch(angle_arc)
        ax.text(0, arc_radius + 2, f'θ = {self.theta_rad}', ha='center', color='green', fontsize=10)

        # Label Area
        mid_radius = self.r_answer + (self.width / 2)
        ax.text(0, mid_radius, f"Area\n{self.area_display}", ha='center', va='center', fontsize=9)

        # Chart Cleanup
        ax.set_xlim(-self.outer_radius - 5, self.outer_radius + 5)
        ax.set_ylim(-2, self.outer_radius + 5)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat133:
    
    def __init__(self):
        # Radius R between 10 and 50 cm
        self.R = rnd.randint(10, 50) 
        
        # Angle theta (fraction of pi). We want a major sector (e.g., 1.1pi to 1.9pi)
        # to make the cone look substantial.
        self.theta_factor = round(rnd.uniform(1.1, 1.9), 1)
        theta_rad = self.theta_factor * np.pi
        self.theta_deg = np.degrees(theta_rad)

        # Circumference of cone base = Arc length of sector
        # 2 * pi * r = R * theta
        self.r = (self.R * theta_rad) / (2 * np.pi)
        
        # Height of the cone (Pythagoras: R is the slant height)
        # h^2 + r^2 = R^2
        self.h = np.sqrt(self.R**2 - self.r**2)

        self.answer = round(self.r, 3)

        self.description = (
            f"A paper sector with a radius of R = {self.R} cm and a central angle of theta = {self.theta_factor}π radians "
            f"is cut out. The straight edges (radii) of the sector are joined together with no overlap "
            f"to form the curved surface of a right circular cone. "
            f"Calculate the base radius (r) of the resulting cone in cm. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Circular measure"
        self.source = "Adapted from Understanding Pure Mathematics"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given: Radius of sector (Slant height) }} R &= {self.R}\\,\\text{{cm}}\\\\"
            f"\\text{{Central angle }} \\theta &= {self.theta_factor}\\pi\\,\\text{{rad}}\\\\"
            f"\\text{{The arc length of the sector equals the circumference of the base:}} &\\\\"
            f"\\text{{Arc Length}} &= \\text{{Circumference}}\\\\"
            f"R \\cdot \\theta &= 2\\pi r\\\\"
            f"r &= \\frac{{R \\cdot \\theta}}{{2\\pi}}\\\\"
            f"&= \\frac{{{self.R} \\cdot {self.theta_factor}\\pi}}{{2\\pi}}\\\\"
            f"&= \\frac{{{self.R} \\cdot {self.theta_factor}}}{{2}}\\\\"
            f"&= \\frac{{{round(self.R * self.theta_factor, 10)}}}{{2}}\\\\"
            f"&= {self.answer}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(12, 6))
        
        # --- LEFT SUBPLOT: The 2D Sector ---
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.set_title("Paper Sector (2D)", fontsize=14, pad=20)
        
        # Center the sector visually by rotating start angle
        start_angle = (360 - self.theta_deg) / 2
        sector = Wedge((0, 0), self.R, start_angle, start_angle + self.theta_deg, 
                    facecolor='lightblue', edgecolor='navy', alpha=0.6, linewidth=2)
        ax1.add_patch(sector)
        
        # Label R (Radius)
        mid_angle_rad = np.radians(start_angle + self.theta_deg/2)
        # Put label on one of the straight edges
        edge_angle_rad = np.radians(start_angle)
        ax1.text(self.R/2 * np.cos(edge_angle_rad), self.R/2 * np.sin(edge_angle_rad) + 1, 
                f"$R={self.R}$", fontsize=12, color='navy', fontweight='bold')

        # Label Theta (Angle)
        ax1.text(0, -self.R*0.3, f"$\\theta = {self.theta_factor}\\pi$", 
                fontsize=12, ha='center', color='darkred')
        
        # Draw an arc for the angle to make it clear
        # Small arc near center
        angle_arc = Wedge((0, 0), self.R*0.2, start_angle, start_angle + self.theta_deg, 
                        facecolor='none', edgecolor='darkred', linestyle='--')
        ax1.add_patch(angle_arc)

        ax1.set_xlim(-self.R*1.1, self.R*1.1)
        ax1.set_ylim(-self.R*1.1, self.R*1.1)
        ax1.set_aspect('equal')
        ax1.axis('off')

        # Add a transition arrow between plots
        # (We use figure coordinates for this usually, but plain text arrow works simply)
        fig.text(0.5, 0.5, "Rolls up\ninto", ha='center', va='center', fontsize=12, fontweight='bold')
        fig.text(0.5, 0.45, "------------>", ha='center', va='center', fontsize=16)

        # --- RIGHT SUBPLOT: The 3D Cone ---
        ax2 = fig.add_subplot(1, 2, 2, projection='3d')
        ax2.set_title("Right Circular Cone (3D)", fontsize=14, pad=20)

        # Create mesh for cone
        # parametric eq: x = u*cos(v), y = u*sin(v), z = h*(1 - u/r) ... scaling appropriately
        u = np.linspace(0, self.r, 50)      # radius variable from 0 to r
        v = np.linspace(0, 2*np.pi, 60) # angle variable
        U, V = np.meshgrid(u, v)
        
        X = U * np.cos(V)
        Y = U * np.sin(V)
        Z = self.h * (1 - U/self.r) # Height decreases as radius increases toward edge? No, tip is at 0,0,h usually.
        # Let's do: Base at z=0, Tip at z=h
        # Cone surface logic: at height z, radius is r*(h-z)/h
        # Let's stick to U as radial distance from center of base:
        # Z = h * (1 - U/r) -> When U=0 (center), Z=h. When U=r (edge), Z=0.
        
        ax2.plot_surface(X, Y, Z, alpha=0.6, color='orange', edgecolor='none')
        
        # Add wireframe for definition
        ax2.plot_wireframe(X, Y, Z, color='brown', rstride=10, cstride=10, alpha=0.3)

        # Draw the base circle explicitly for clarity
        theta_base = np.linspace(0, 2*np.pi, 100)
        x_base = self.r * np.cos(theta_base)
        y_base = self.r * np.sin(theta_base)
        z_base = np.zeros_like(x_base)
        ax2.plot(x_base, y_base, z_base, color='brown', linewidth=2)

        # Draw Radius r line
        ax2.plot([0, self.r], [0, 0], [0, 0], color='black', linewidth=2, linestyle='--')
        ax2.text(self.r/2, 0, -self.h*0.05, "$r=?$", fontsize=12, color='black', fontweight='bold')
        
        # Draw Height h line (optional, but good for context)
        ax2.plot([0, 0], [0, 0], [0, self.h], color='blue', linestyle='--')

        # Draw Slant Height s (which is R)
        ax2.plot([self.r, 0], [0, 0], [0, self.h], color='navy', linestyle='-', alpha=0.5)
        ax2.text(self.r/2, 0, self.h/2, f"$s=R={self.R}$", fontsize=10, color='navy')

        # Adjust 3D view
        ax2.set_box_aspect((self.r, self.r, self.h)) # Aspect ratio to make it look realistic
        ax2.axis('off')
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat134:
    
    def __init__(self):
        # We want y = sqrt(ax - b) at x_p to result in an integer y_p
        # Equation: y_p = sqrt(a * x_p - b)  =>  y_p^2 = a * x_p - b
        
        self.x_p = rnd.randint(2, 6)       # Pick a manageable x coordinate
        self.y_p = rnd.randint(2, 6)       # Pick a resulting y coordinate
        self.a = rnd.randint(2, 8)         # Coefficient 'a'
        
        # Calculate 'b' to satisfy the equation
        self.b = self.a * self.x_p - self.y_p**2
        
        # Ensure 'b' is reasonable (keep the root valid and positive)
        # If b is negative, the equation becomes sqrt(ax + |b|), which is fine but
        # let's try to keep format sqrt(ax - b) or sqrt(ax + b) clean.
        self.sign_str = "-" if self.b > 0 else "+"
        self.b_disp = abs(self.b)
        
        # Function: f(x) = (ax - b)^(1/2)
        # Derivative: f'(x) = a / (2 * sqrt(ax - b))
        # At P: f'(x_p) = a / (2 * y_p)
        
        m_tangent = self.a / (2 * self.y_p)
        m_normal = -1 / m_tangent  # Normal is perpendicular
        
        # Normal Line Equation: y - y_p = m_normal * (x - x_p)
        # y = m_normal * (x - x_p) + y_p
        
        # Find Intercept A (y = 0):
        # 0 = m_normal * (x_A - x_p) + y_p
        # -y_p / m_normal = x_A - x_p
        # x_A = x_p - (y_p / m_normal)
        self.x_A = self.x_p - (self.y_p / m_normal)
        
        # Find Intercept B (x = 0):
        # y_B = m_normal * (0 - x_p) + y_p
        self.y_B = m_normal * (-self.x_p) + self.y_p
        
        # Area of Triangle AOB (Vertices: Origin, A, B)
        # Since it's in the first quadrant/positive axes usually:
        area = 0.5 * abs(self.x_A) * abs(self.y_B)

        self.answer = round(area, 3)

        self.description = (
            f"The figure displays the curve $y = \\sqrt{{{self.a}x {self.sign_str} {self.b_disp}}}$ in the first quadrant. "
            f"A normal line is drawn to the curve at the point $P$ where $x = {self.x_p}$. "
            f"This normal line intersects the x-axis at point $A$ and the y-axis at point $B$, "
            f"forming a triangle $AOB$ with the coordinate axes. "
            f"Calculate the area of the triangle $AOB$. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Cambridge International AS & A Level Mathematics: Pure Mathematics 1 Coursebook"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Equation of curve:}} &\\quad y = \\sqrt{{{self.a}x {self.sign_str} {self.b_disp}}} \\\\"
            f"\\text{{Differentiating w.r.t }} x: &\\quad \\frac{{dy}}{{dx}} = \\frac{{{self.a}}}{{2\\sqrt{{{self.a}x {self.sign_str} {self.b_disp}}}}} \\\\"
            f"\\text{{At point }} P({self.x_p}, {self.y_p}), \\text{{ slope }} m_t: &\\quad m_t = \\frac{{{self.a}}}{{2({self.y_p})}} = {round(m_tangent, 10)} \\\\"
            f"\\text{{Slope of normal }} m_n: &\\quad m_n = -\\frac{{1}}{{m_t}} = -\\frac{{1}}{{{round(m_tangent, 10)}}} = {round(m_normal, 10)} \\\\"
            f"\\text{{Equation of normal line:}} &\\quad y - {self.y_p} = {round(m_normal, 10)}(x - {self.x_p}) \\\\"
            f"\\text{{x-intercept }} A \\text{{ (set }} y=0): &\\quad -{self.y_p} = {round(m_normal, 10)}(x_A - {self.x_p}) \\\\"
            f"x_A &= {self.x_p} - \\frac{{{self.y_p}}}{{{round(m_normal, 10)}}} = {round(self.x_A, 10)} \\\\"
            f"\\text{{y-intercept }} B \\text{{ (set }} x=0): &\\quad y_B = {round(m_normal, 10)}(0 - {self.x_p}) + {self.y_p} \\\\"
            f"y_B &= {round(self.y_B, 10)} \\\\"
            f"\\text{{Area of }} \\Delta AOB: &\\quad \\text{{Area}} = \\frac{{1}}{{2}} |OA| |OB| \\\\"
            f"&= 0.5 \\times |{round(self.x_A, 10)}| \\times |{round(self.y_B, 10)}| \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Domain for plotting curve
        # Start slightly after the root to avoid imaginary numbers if strictly > 0 needed
        root_x = self.b / self.a
        x_vals = np.linspace(root_x, self.x_A + 2, 400)
        y_vals = np.sqrt(self.a * x_vals - self.b)
        
        # Plot Curve
        ax.plot(x_vals, y_vals, 'b-', lw=2, label=f'$y=\\sqrt{{{self.a}x {self.sign_str} {self.b_disp}}}$')
        
        # Plot Normal Line (from B to A)
        # We extend it slightly past A and B for visual clarity
        line_x = np.array([0, self.x_A])
        line_y = np.array([self.y_B, 0])
        ax.plot(line_x, line_y, 'r-', lw=2, label='Normal Line')
        
        # Highlight Triangle AOB
        triangle_x = [0, self.x_A, 0]
        triangle_y = [0, 0, self.y_B]
        ax.fill(triangle_x, triangle_y, color='green', alpha=0.2, label='Triangle AOB')
        
        # Plot Points
        ax.plot(self.x_p, self.y_p, 'ko') # Point P
        ax.text(self.x_p, self.y_p + 0.5, '$P$', fontsize=12, fontweight='bold')
        
        ax.plot(self.x_A, 0, 'ko')   # Point A
        ax.text(self.x_A, 0.5, '$A$', fontsize=12, fontweight='bold')
        
        ax.plot(0, self.y_B, 'ko')   # Point B
        ax.text(0.2, self.y_B, '$B$', fontsize=12, fontweight='bold')
        
        ax.plot(0, 0, 'ko')     # Origin
        ax.text(-0.5, -0.5, '$O$', fontsize=12, fontweight='bold')

        # Formatting
        ax.set_xlim(-1, self.x_A + 2)
        ax.set_ylim(-1, max(y_vals[-1], self.y_B) + 1)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend(loc='upper right')
        ax.grid(True, linestyle='--', alpha=0.6)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat135:
    
    def __init__(self):
        self.radius_val = rnd.randint(5, 20)      # Radius in meters
        self.dr_dt_val = round(rnd.uniform(0.1, 2.0), 1) # Rate of radius change in m/s
        
        # Area A = pi * r^2
        # dA/dt = 2 * pi * r * (dr/dt)
        # The question asks for the answer divided by pi, so: Result = 2 * r * dr/dt
        answer_raw = 2 * self.radius_val * self.dr_dt_val
        self.answer = round(answer_raw, 2)

        self.description = (
            f"The figure illustrates a circular oil spill on the ocean surface. "
            f"The spill is expanding such that its radius r is increasing "
            f"at a constant rate. "
            f"Given:\n"
            f"• Instantaneous Radius (r): {self.radius_val} m\n"
            f"• Rate of radius increase (dr/dt): {self.dr_dt_val} m/s\n\n"
            f"Find the rate of increase of the area (dA/dt) in m²/s "
            f"at this instant. (Divide your final answer by π). "
            f"Give your answer correct to 2 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Calculus: Early Transcendentals"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given parameters:}} &\\\\"
            f"r &= {self.radius_val}\\,\\text{{m}}\\\\"
            f"\\frac{{dr}}{{dt}} &= {self.dr_dt_val}\\,\\text{{m/s}}\\\\"
            f"\\text{{The area of a circle is }} A = \\pi r^2. \\text{{ Differentiating with respect to time:}} &\\\\"
            f"\\frac{{dA}}{{dt}} &= \\frac{{d}}{{dt}}(\\pi r^2) = 2\\pi r \\frac{{dr}}{{dt}}\\\\"
            f"\\text{{Substituting the known values:}} &\\\\"
            f"\\frac{{dA}}{{dt}} &= 2\\pi ({self.radius_val})({self.dr_dt_val})\\\\"
            f"&= 2\\pi ({round(self.radius_val * self.dr_dt_val, 10)})\\\\"
            f"&= {round(2 * self.radius_val * self.dr_dt_val, 10)}\\pi\\,\\text{{m}}^2/\\text{{s}}\\\\"
            f"\\text{{The question asks for the rate divided by }} \\pi: &\\\\"
            f"\\text{{Result}} &= \\frac{{1}}{{\\pi}} \\left( {round(2 * self.radius_val * self.dr_dt_val, 10)}\\pi \\right)\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Set limits clearly around the circle
        limit = self.radius_val * 1.5
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        
        # Remove axes for a cleaner diagram look
        ax.axis('off')

        # Draw the "Ocean" (background mostly white/light blue implicitly) 
        # and the "Oil Spill" (Circle)
        oil_spill = patches.Circle((0, 0), self.radius_val, color='black', alpha=0.7, label='Oil Spill')
        ax.add_patch(oil_spill)

        # Draw Radius Line
        plt.plot([0, self.radius_val], [0, 0], color='white', linewidth=2, linestyle='--')
        plt.text(self.radius_val/2, -limit*0.1, f'r = {self.radius_val} m', color='black', 
                fontsize=12, ha='center', fontweight='bold')

        # Draw Expansion Arrows (Vectors)
        # We put 4 arrows indicating outward expansion
        directions = [(limit*0.8, 0), (-limit*0.8, 0), (0, limit*0.8), (0, -limit*0.8)]
        for dx, dy in directions:
            # Scale arrow start point to be just outside the circle
            norm = np.sqrt(dx**2 + dy**2)
            start_x, start_y = (dx/norm) * self.radius_val, (dy/norm) * self.radius_val
            end_x, end_y = (dx/norm) * (self.radius_val + self.radius_val*0.3), (dy/norm) * (self.radius_val + self.radius_val*0.3)
            
            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2))

        # Label for dr/dt
        plt.text(self.radius_val * 0.7, self.radius_val * 0.7, f'dr/dt = {self.dr_dt_val} m/s', 
                color='red', fontsize=12, fontweight='bold')

        # Add Title
        plt.title("Oil Spill Expansion", fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat136:
    
    def __init__(self):
        # Random side length (S) between 6 and 30.
        # We allow floats but round for cleaner display, or stick to even integers.
        self.side_length = rnd.choice(range(6, 32, 2)) 
        
        # The math for the solution:
        # V(x) = x(S - 2x)^2
        # V'(x) = 12x^2 - 8Sx + S^2
        # Roots for critical points are x = S/2 (min) and x = S/6 (max).
        optimal_x = self.side_length / 6.0
        max_volume = optimal_x * (self.side_length - 2*optimal_x)**2

        self.answer = round(max_volume, 3)

        self.description = (
            f"The figure above shows a net for an open-topped box made from a square sheet of metal of side **{self.side_length} cm** "
            f"by cutting equal squares of side $x$ from the corners and folding up the flaps. "
            f"Find the value of $x$ for which the volume $V$ is a maximum. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Pure Mathematics 1"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Let the side length }} S &= {self.side_length}\\,\\text{{cm}}\\\\"
            f"\\text{{Volume of the box is given by:}} &\\\\"
            f"V(x) &= x(S - 2x)^2\\\\"
            f"V(x) &= x({self.side_length} - 2x)^2\\\\"
            f"\\text{{To find the maximum, differentiate }} V(x): &\\\\"
            f"V'(x) &= \\frac{{d}}{{dx}}\\left[ x({self.side_length} - 2x)^2 \\right]\\\\"
            f"&= 1 \\cdot ({self.side_length} - 2x)^2 + x \\cdot 2({self.side_length} - 2x) \\cdot (-2)\\\\"
            f"&= ({self.side_length} - 2x) [ ({self.side_length} - 2x) - 4x ]\\\\"
            f"&= ({self.side_length} - 2x) ({self.side_length} - 6x)\\\\"
            f"\\text{{Set }} V'(x) = 0 \\text{{ to find critical points:}} &\\\\"
            f"0 &= ({self.side_length} - 2x) ({self.side_length} - 6x)\\\\"
            f"\\text{{Possible values: }} x &= \\frac{{{self.side_length}}}{{2}} \\text{{ or }} x = \\frac{{{self.side_length}}}{{6}}\\\\"
            f"\\text{{Since }} x = S/2 \\text{{ gives }} V=0, \\text{{ we choose:}} &\\\\"
            f"x &= \\frac{{{self.side_length}}}{{6}} \\approx {round(self.side_length/6.0, 10)}\\,\\text{{cm}}\\\\"
            f"\\text{{Max Volume:}} &\\\\"
            f"V_{{max}} &= {round(self.side_length/6.0, 10)} \\left({self.side_length} - 2({round(self.side_length/6.0, 10)})\\right)^2\\\\"
            f"&= {self.answer}\\,\\text{{cm}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Visual setup (we draw the cut 'x' as proportional to the real solution S/6 for accuracy)
        vis_cut = self.side_length / 6.0 
        
        # Draw the main sheet (background square)
        sheet = patches.Rectangle((0, 0), self.side_length, self.side_length, 
                                linewidth=2, edgecolor='black', facecolor='#E0F7FA')
        ax.add_patch(sheet)
        
        # Define the 4 corners to be cut out
        corners = [
            (0, 0),                                   # Bottom-left
            (self.side_length - vis_cut, 0),               # Bottom-right
            (0, self.side_length - vis_cut),               # Top-left
            (self.side_length - vis_cut, self.side_length - vis_cut) # Top-right
        ]
        
        # Draw the corners (shaded differently to indicate removal)
        for (cx, cy) in corners:
            corner_rect = patches.Rectangle((cx, cy), vis_cut, vis_cut, 
                                            linewidth=1, edgecolor='#D32F2F', 
                                            facecolor='#FFCDD2', hatch='//')
            ax.add_patch(corner_rect)
            
            # Label 'x' inside the corners
            # We put the label slightly centered in the corner box
            ax.text(cx + vis_cut/2, cy + vis_cut/2, '$x$', 
                    ha='center', va='center', fontsize=12, color='#D32F2F', fontweight='bold')

        # Draw dashed fold lines for the inner box base
        # Vertical lines
        ax.vlines([vis_cut, self.side_length - vis_cut], 0, self.side_length, colors='black', linestyles='--')
        # Horizontal lines
        ax.hlines([vis_cut, self.side_length - vis_cut], 0, self.side_length, colors='black', linestyles='--')

        # Add dimensions arrows/labels
        # Bottom dimension arrow for total Side Length
        ax.annotate(
            '', xy=(0, -self.side_length*0.08), xytext=(self.side_length, -self.side_length*0.08),
            arrowprops=dict(arrowstyle='<->', color='black')
        )
        ax.text(self.side_length/2, -self.side_length*0.15, f"{self.side_length} cm", ha='center', fontsize=12)

        # Set plot limits and aspect
        offset = self.side_length * 0.2
        ax.set_xlim(-offset, self.side_length + offset)
        ax.set_ylim(-offset, self.side_length + offset)
        ax.set_aspect('equal')
        ax.axis('off') # Turn off axes coordinates
        plt.title("Net for Open-Topped Box", fontsize=14)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat137:
    
    def __init__(self):
        # We generate integer coordinates to make the visual slope calculation 'nice'
        # Range of coordinates
        low, high = 0, 8
        
        # Generate points for f(x)
        self.fx1, self.fy1 = rnd.randint(low, high), rnd.randint(low, high)
        self.fx2, self.fy2 = rnd.randint(low, high), rnd.randint(low, high)
        # Ensure x values are different to avoid undefined slope
        while self.fx1 == self.fx2 or self.fy1 == self.fy2:
            self.fx2 = rnd.randint(low, high)
            self.fy2 = rnd.randint(low, high)

        # Generate points for g(x)
        self.gx1, self.gy1 = rnd.randint(low, high), rnd.randint(low, high)
        self.gx2, self.gy2 = rnd.randint(low, high), rnd.randint(low, high)
        while self.gx1 == self.gx2 or self.gy1 == self.gy2:
            self.gx2 = rnd.randint(low, high)
            self.gy2 = rnd.randint(low, high)
            
        # Randomize the x value to evaluate h'(x) at
        self.x_target = rnd.randint(low, high)

        # Slope of f (m_f)
        self.m_f = (self.fy2 - self.fy1) / (self.fx2 - self.fx1)
        # Slope of g (m_g)
        self.m_g = (self.gy2 - self.gy1) / (self.gx2 - self.gx1)
        
        # h(x) = f(g(x))
        # Chain rule: h'(x) = f'(g(x)) * g'(x)
        # Since f and g are linear, their derivatives are their slopes (constants).
        # h'(x) = m_f * m_g
        self.answer = round(self.m_f * self.m_g, 3)

        self.description = (
            f"The figure displays two linear functions. "
            f"Line f(x) passes through ({self.fx1}, {self.fy1}) and ({self.fx2}, {self.fy2}). "
            f"Line g(x) passes through ({self.gx1}, {self.gy1}) and ({self.gx2}, {self.gy2}). "
            f"Let h(x) = f(g(x)). "
            f"Calculate the value of h'({self.x_target}). "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Differentiation"
        self.source = "Adapted from Active Calculus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Using the Chain Rule for }} h(x) = f(g(x)): &\\\\"
            f"h'(x) &= f'(g(x)) \\cdot g'(x) \\\\"
            f"\\text{{Since }} f(x) \\text{{ and }} g(x) \\text{{ are linear, their derivatives are their slopes.}} &\\\\"
            f"\\text{{Finding slope }} m_f \\text{{ for }} f(x): &\\\\"
            f"m_f &= \\frac{{y_2 - y_1}}{{x_2 - x_1}} \\\\"
            f"&= \\frac{{{self.fy2} - {self.fy1}}}{{{self.fx2} - {self.fx1}}} \\\\"
            f"&= \\frac{{{self.fy2 - self.fy1}}}{{{self.fx2 - self.fx1}}} \\approx {round(self.m_f, 10)} \\\\"
            f"\\text{{Finding slope }} m_g \\text{{ for }} g(x): &\\\\"
            f"m_g &= \\frac{{y_2 - y_1}}{{x_2 - x_1}} \\\\"
            f"&= \\frac{{{self.gy2} - {self.gy1}}}{{{self.gx2} - {self.gx1}}} \\\\"
            f"&= \\frac{{{self.gy2 - self.gy1}}}{{{self.gx2 - self.gx1}}} \\approx {round(self.m_g, 10)} \\\\"
            f"\\text{{Calculating }} h'({self.x_target}): &\\\\"
            f"h'({self.x_target}) &= f'(g({self.x_target})) \\cdot g'({self.x_target}) \\\\"
            f"&= m_f \\cdot m_g \\\\"
            f"&= ({round(self.m_f, 10)}) \\cdot ({round(self.m_g, 10)}) \\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Create x range for plotting (add some padding)
        x_vals = np.linspace(min(self.fx1, self.fx2, self.gx1, self.gx2) - 1, max(self.fx1, self.fx2, self.gx1, self.gx2) + 1, 100)
        
        # Define line equations: y = m(x - x1) + y1
        y_f = self.m_f * (x_vals - self.fx1) + self.fy1
        y_g = self.m_g * (x_vals - self.gx1) + self.gy1

        plt.figure(figsize=(8, 6))
        
        # Plot Lines
        plt.plot(x_vals, y_f, label=f'$f(x)$', color='blue', linewidth=2)
        plt.plot(x_vals, y_g, label=f'$g(x)$', color='orange', linewidth=2)
        
        # Plot Points
        plt.scatter([self.fx1, self.fx2], [self.fy1, self.fy2], color='blue', zorder=5)
        plt.scatter([self.gx1, self.gx2], [self.gy1, self.gy2], color='orange', zorder=5)
        
        # Annotate Points
        plt.text(self.fx1, self.fy1, f' ({self.fx1},{self.fy1})', fontsize=9, verticalalignment='bottom')
        plt.text(self.fx2, self.fy2, f' ({self.fx2},{self.fy2})', fontsize=9, verticalalignment='bottom')
        plt.text(self.gx1, self.gy1, f' ({self.gx1},{self.gy1})', fontsize=9, verticalalignment='bottom')
        plt.text(self.gx2, self.gy2, f' ({self.gx2},{self.gy2})', fontsize=9, verticalalignment='bottom')

        # Formatting
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat138:
    
    def __init__(self):
        # We use the form f(x) = ax(b - x) to ensure roots at 0 and b
        # This expands to f(x) = (ab)x - ax^2
        
        self.scale_a = rnd.randint(1, 3)      # Vertical scaling factor
        self.root_b = rnd.randint(3, 8)       # The second root (upper bound of integration)
        
        # Coefficients for standard form: cx - dx^2
        self.coeff_linear = self.scale_a * self.root_b
        self.coeff_quad = self.scale_a

        # Integral of (ab)x - ax^2 dx = (ab)x^2/2 - ax^3/3
        # Evaluated at root_b: (ab)(b^2)/2 - a(b^3)/3 = a*b^3/2 - a*b^3/3 = a*b^3/6
        
        exact_area = (self.scale_a * (self.root_b ** 3)) / 6

        self.answer = round(exact_area, 3)
        
        # Format the equation string for display
        if self.coeff_quad == 1:
            self.eq_str = f"{self.coeff_linear}x - x^2"
        else:
            self.eq_str = f"{self.coeff_linear}x - {self.coeff_quad}x^2"

        self.description = (
            f"The figure displays a shaded region in the first quadrant bounded above by the "
            f"parabolic function f(x) = {self.eq_str} and below by the x-axis. "
            f"The region extends from x = 0 to x = {self.root_b}. "
            f"Calculate the total area of the shaded region shown in the figure. "
            f"Give your answer correct to 3 decimal places."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Integration"
        self.source = "Adapted from Calculus: Early Transcendentals"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Area}} &= \\int_{{0}}^{{{self.root_b}}} \\left( {self.eq_str} \\right) \\, dx\\\\"
            f"&= \\left[ \\frac{{{self.coeff_linear}x^2}}{{2}} - \\frac{{{self.coeff_quad}x^3}}{{3}} \\right]_{{0}}^{{{self.root_b}}}\\\\"
            f"&= \\left( \\frac{{{self.coeff_linear}({self.root_b})^2}}{{2}} - \\frac{{{self.coeff_quad}({self.root_b})^3}}{{3}} \\right) - 0\\\\"
            f"&= \\frac{{{self.coeff_linear * (self.root_b**2)}}}{{2}} - \\frac{{{self.coeff_quad * (self.root_b**3)}}}{{3}}\\\\"
            f"&= {round((self.coeff_linear * self.root_b**2)/2, 10)} - {round((self.coeff_quad * self.root_b**3)/3, 10)}\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        # Define the function for calculation
        def func(x):
            return (self.coeff_linear * x) - (self.coeff_quad * x**2)

        x = np.linspace(-1, self.root_b + 1, 400)
        y = func(x)
        
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot the main function line
        ax.plot(x, y, label=f'$f(x) = {self.eq_str}$', color='blue', linewidth=2)
        
        # Shade the region under the curve
        x_fill = np.linspace(0, self.root_b, 200)
        y_fill = func(x_fill)
        ax.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label='Target Area')
        
        # Setup graph aesthetics
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)
        
        # Set dynamic limits based on the curve size
        peak_y = func(self.root_b / 2)
        ax.set_ylim(-peak_y * 0.2, peak_y * 1.2)
        ax.set_xlim(-1, self.root_b + 1)
        
        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat139:
    
    def __init__(self):
        # t1: Time where triangle ends (base of triangle)
        self.t1 = np.random.randint(2, 6) 
        
        # rect_duration: Duration of the constant velocity phase (width of rectangle)
        self.rect_duration = np.random.randint(3, 7)
        self.t2 = self.t1 + self.rect_duration
        
        # v_max: Peak velocity (height of triangle and rectangle)
        # We multiply by 2 to often get integer results for the triangle area
        self.v_max = np.random.randint(3, 9) * 2

        # Area of Triangle = 0.5 * base * height
        area_triangle = 0.5 * self.t1 * self.v_max
        
        # Area of Rectangle = width * height
        area_rectangle = (self.t2 - self.t1) * self.v_max
        
        # Total Displacement = Sum of areas
        total_displacement = area_triangle + area_rectangle

        self.answer = int(round(total_displacement, 0))

        self.description = (
            f"The figure shows the graph of a velocity function $v(t)$ (in m/s) over the interval $t = [0, {self.t2}]$. "
            f"The graph formed a line of $(0,0) \\rightarrow ({self.t1},{self.v_max}) \\rightarrow ({self.t2},{self.v_max})$. "
            f"Calculate the total displacement of the object from $t=0$ to $t={self.t2}$."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Integration"
        self.source = "Adapted from Strang, G. (1991). Calculus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Displacement}} &= \\text{{Area under the }} v(t) \\text{{ graph}}\\\\"
            f"\\text{{Area}}_{{\\text{{triangle}}}} &= \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}\\\\"
            f"&= \\frac{{1}}{{2}} \\times {self.t1} \\times {self.v_max}\\\\"
            f"&= {round(0.5 * self.t1 * self.v_max, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Area}}_{{\\text{{rectangle}}}} &= \\text{{width}} \\times \\text{{height}}\\\\"
            f"&= ({self.t2} - {self.t1}) \\times {self.v_max}\\\\"
            f"&= {self.t2 - self.t1} \\times {self.v_max}\\\\"
            f"&= {round((self.t2 - self.t1) * self.v_max, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Total Displacement}} &= \\text{{Area}}_{{\\text{{triangle}}}} + \\text{{Area}}_{{\\text{{rectangle}}}}\\\\"
            f"&= {round(0.5 * self.t1 * self.v_max, 10)} + {round((self.t2 - self.t1) * self.v_max, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot Triangle part: (0,0) to (t1, v_max)
        ax.plot([0, self.t1], [0, self.v_max], 'b-', linewidth=2, label='$v(t)$')
        
        # Plot Rectangle part: (t1, v_max) to (t2, v_max)
        ax.plot([self.t1, self.t2], [self.v_max, self.v_max], 'b-', linewidth=2)
        
        # Drop vertical lines for visual reference
        ax.vlines(x=self.t1, ymin=0, ymax=self.v_max, colors='gray', linestyles='--', alpha=0.5)
        ax.vlines(x=self.t2, ymin=0, ymax=self.v_max, colors='gray', linestyles='--', alpha=0.5)
        
        # Shade the areas
        # Triangle shading
        x_tri = np.linspace(0, self.t1, 100)
        y_tri = (self.v_max / self.t1) * x_tri
        ax.fill_between(x_tri, y_tri, color='skyblue', alpha=0.4, label='Area')
        
        # Rectangle shading
        x_rect = np.linspace(self.t1, self.t2, 100)
        y_rect = np.full_like(x_rect, self.v_max)
        ax.fill_between(x_rect, 0, y_rect, color='skyblue', alpha=0.4)

        # Formatting
        ax.set_xlim(0, self.t2 + 1)
        ax.set_ylim(0, self.v_max + (self.v_max * 0.5)) # Add some headroom
        ax.set_xlabel('Time $t$ (s)')
        ax.set_ylabel('Velocity $v(t)$ (m/s)')
        ax.set_title(f'Velocity Function over $t = [0, {self.t2}]$')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right')
        
        # Annotate key vertices
        ax.plot([0, self.t1, self.t2], [0, self.v_max, self.v_max], 'ro', markersize=5) # Mark points
        ax.text(self.t1, self.v_max + (self.v_max * 0.05), f'({self.t1}, {self.v_max})', ha='center', fontsize=10, fontweight='bold')
        ax.text(self.t2, self.v_max + (self.v_max * 0.05), f'({self.t2}, {self.v_max})', ha='center', fontsize=10, fontweight='bold')
        ax.text(0, (self.v_max * 0.05), '(0, 0)', ha='left', fontsize=10, fontweight='bold')

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

class Mat140:
    
    def __init__(self):
        # We will vary the coefficient 'a' in y = a*sqrt(x) and the upper limit 'b' in x = b
        self.a = rnd.randint(1, 3)  # Random coefficient between 1 and 3
        self.b = rnd.randint(2, 6)  # Random upper limit x between 2 and 6
        
        # Function string for display
        self.func_str = f"{self.a}\\sqrt{{x}}" if self.a > 1 else "\\sqrt{x}"
        
        # Volume V = integral from 0 to b of pi * (f(x))^2 dx
        # f(x) = a*sqrt(x)  =>  (f(x))^2 = a^2 * x
        # Integral of a^2 * x is (a^2 * x^2) / 2
        # Evaluated at b: (a^2 * b^2) / 2
        PI = 3.14159
        exact_volume_coeff = (self.a**2 * self.b**2) / 2
        decimal_answer = exact_volume_coeff * PI

        self.answer = round(decimal_answer, 3)

        self.description = (
            f"The figure illustrates a solid 3D shape formed by rotating a specific 2D region around the x-axis. "
            f"The 2D region is defined by the function $y = {self.func_str}$, the vertical line $x = {self.b}$, and the x-axis. "
            f"Calculate the volume of the solid generated by the rotation shown in the figure. "
            f"Give your answer as a decimal rounded to three places. "
            f"(Use $\\pi \\approx 3.14159$)."
        )

        self.topic = "Pure Mathematics 1"
        self.subtopic = "Integration"
        self.source = "Adapted from Thomas' Calculus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Volume of revolution formula:}} &\\\\"
            f"V &= \\pi \\int_{{0}}^{{{self.b}}} [f(x)]^2 \\, dx\\\\"
            f"\\text{{Substitute }} f(x) = {self.func_str}: &\\\\"
            f"V &= \\pi \\int_{{0}}^{{{self.b}}} \\left({self.func_str}\\right)^2 \\, dx\\\\"
            f"&= \\pi \\int_{{0}}^{{{self.b}}} {self.a**2} x \\, dx\\\\"
            f"\\text{{Integrate with respect to }} x: &\\\\"
            f"&= \\pi \\left[ \\frac{{{self.a**2} x^2}}{{2}} \\right]_{{0}}^{{{self.b}}}\\\\"
            f"\\text{{Evaluate at the limits:}} &\\\\"
            f"&= \\pi \\left( \\frac{{{self.a**2} ({self.b})^2}}{{2}} - 0 \\right)\\\\"
            f"&= \\pi \\left( \\frac{{{self.a**2 * self.b**2}}}{{2}} \\right)\\\\"
            f"&= {round((self.a**2 * self.b**2) / 2, 10)} \\pi\\\\"
            f"\\text{{Substitute }} \\pi \\approx 3.14159: &\\\\"
            f"&= {round((self.a**2 * self.b**2) / 2, 10)} \\times 3.14159\\\\"
            f"&= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig = plt.figure(figsize=(12, 5))
        
        # Subplot 1: The 2D Region
        ax1 = fig.add_subplot(1, 2, 1)
        x_vals = np.linspace(0, self.b + 0.5, 200)
        y_vals = self.a * np.sqrt(x_vals)
        
        # Plot curve
        ax1.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'$y={self.func_str}$')
        
        # Fill area
        x_fill = np.linspace(0, self.b, 100)
        y_fill = self.a * np.sqrt(x_fill)
        ax1.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='Region to rotate')
        
        # Plot vertical line x=b
        ax1.vlines(self.b, 0, self.a * np.sqrt(self.b), colors='r', linestyles='--', label=f'x={self.b}')
        
        # Add rotation arrow
        # Creating a curved arrow to indicate rotation around x-axis
        style = "Simple, tail_width=0.5, head_width=4, head_length=8"
        kw = dict(arrowstyle=style, color="k")
        # An arc representing rotation
        arrow = FancyArrowPatch((self.b/2, -1), (self.b/2, 1), connectionstyle="arc3,rad=.5", **kw)
        ax1.add_patch(arrow)
        ax1.text(self.b/2, -1.5, "Rotate x-axis", ha='center', fontsize=9)
        
        ax1.set_title("2D Region")
        ax1.set_xlabel("x")
        ax1.set_ylabel("y")
        ax1.axhline(0, color='black', linewidth=1)
        ax1.axvline(0, color='black', linewidth=1)
        ax1.legend()
        ax1.grid(True, linestyle=':', alpha=0.6)

        # Subplot 2: The 3D Solid (Wireframe)
        ax2 = fig.add_subplot(1, 2, 2, projection='3d')
        u = np.linspace(0, self.b, 30)   # x values
        v = np.linspace(0, 2 * np.pi, 30) # rotation angle
        U, V = np.meshgrid(u, v)
        
        # Parametric equations for the surface
        # X is simply u (distance along axis)
        # Y is radius * cos(angle) -> radius is function value a*sqrt(u)
        # Z is radius * sin(angle)
        X = U
        R = self.a * np.sqrt(U)
        Y = R * np.cos(V)
        Z = R * np.sin(V)
        
        # Plot surface
        ax2.plot_surface(X, Y, Z, color='skyblue', alpha=0.6, rstride=1, cstride=1, edgecolor='blue', linewidth=0.2)
        
        # Plot the circular face at the end (the disk at x=b)
        v_disk = np.linspace(0, 2*np.pi, 50)
        r_disk = np.linspace(0, self.a * np.sqrt(self.b), 10)
        V_disk, R_disk = np.meshgrid(v_disk, r_disk)
        X_disk = np.full_like(V_disk, self.b)
        Y_disk = R_disk * np.cos(V_disk)
        Z_disk = R_disk * np.sin(V_disk)
        ax2.plot_surface(X_disk, Y_disk, Z_disk, color='red', alpha=0.3)

        ax2.set_title("Generated 3D Solid")
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        ax2.set_zlabel("z")
        
        # Set equal aspect ratio for 3D plot to make it look realistic
        max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
        mid_x = (X.max()+X.min()) * 0.5
        mid_y = (Y.max()+Y.min()) * 0.5
        mid_z = (Z.max()+Z.min()) * 0.5
        ax2.set_xlim(mid_x - max_range, mid_x + max_range)
        ax2.set_ylim(mid_y - max_range, mid_y + max_range)
        ax2.set_zlim(mid_z - max_range, mid_z + max_range)

        plt.tight_layout()

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
        
class Mat141:
    def __init__(self):
        # Relationship: y = k * a^x
        # Linearized: ln(y) = ln(k) + x * ln(a)
        # We define a slope (ln_a) and intercept (ln_k)
        self.ln_k = round(randrange_float(0.5, 1.5, 0.01), 2)
        self.ln_a = round(randrange_float(0.3, 0.8, 0.01), 2)
        
        # x-values for points in the diagram
        self.x1 = 0
        self.x2 = round(randrange_float(2.0, 4.0, 0.01), 2)
        
        # ln(y) values
        self.lny1 = self.ln_k
        self.lny2 = round(self.ln_k + self.ln_a * self.x2, 2)
        
        self.answer = math.exp(self.ln_a)

        self.description = (
            f"The variables $x$ and $y$ satisfy the relationship $y = k a^x$, where $k$ and $a$ are constants. "
            f"As shown in the figure, the graph of $\\ln y$ against $x$ is a straight line passing through "
            f"the points $({self.x1}, {self.lny1})$ and $({self.x2}, {self.lny2})$. "
            f"Find the value of $a$."
        )
        
        self.topic = "Pure Mathematics 2"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The given relationship is: }} y &= k a^x \\\\"
            f"\\text{{Taking the natural logarithm of both sides: }} \\ln y &= \\ln(k a^x) \\\\"
            f"\\ln y &= \\ln k + \\ln(a^x) \\\\"
            f"\\ln y &= \\ln k + x \\ln a \\\\"
            f"\\text{{This is in the form }} Y = mX + c, \\text{{ where }} Y = \\ln y, X = x, \\text{{ and gradient }} m = \\ln a. \\\\"
            f"\\text{{The gradient }} m \\text{{ can be calculated from the two points }} ({self.x1}, {self.lny1}) \\text{{ and }} ({self.x2}, {self.lny2}): \\\\"
            f"m &= \\frac{{\\ln y_2 - \\ln y_1}}{{x_2 - x_1}} \\\\"
            f"&= \\frac{{{self.lny2} - {self.lny1}}}{{{self.x2} - {self.x1}}} \\\\"
            f"&= \\frac{{{round(self.lny2 - self.lny1, 10)}}}{{{round(self.x2 - self.x1, 10)}}} \\\\"
            f"&= {round((self.lny2 - self.lny1) / (self.x2 - self.x1), 10)} \\\\"
            f"\\text{{Since }} m = \\ln a: \\\\"
            f"\\ln a &= {round(self.ln_a, 10)} \\\\"
            f"a &= e^{{{round(self.ln_a, 10)}}} \\\\"
            f"a &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plotting range
        x_min, x_max = -0.5, self.x2 + 1
        y_min, y_max = 0, self.lny2 + 1
        
        # Draw axes
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # Plot the line
        x_vals = np.array([0, self.x2])
        y_vals = np.array([self.lny1, self.lny2])
        ax.plot([x_min, x_max], [self.ln_k + self.ln_a * x_min, self.ln_k + self.ln_a * x_max], color='black', lw=2)
        
        # Plot points and labels
        ax.scatter(x_vals, y_vals, color='black', s=50, zorder=5)
        ax.text(self.x1 + 0.1, self.lny1, f"({self.x1}, {self.lny1})", fontsize=12, va='bottom')
        ax.text(self.x2 + 0.1, self.lny2, f"({self.x2}, {self.lny2})", fontsize=12, va='bottom')
        
        # Axis labels
        ax.set_xlabel('$x$', loc='right', fontsize=14)
        ax.set_ylabel('$\\ln y$', loc='top', fontsize=14, rotation=0)
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid(True, linestyle='--', alpha=0.6)
        
        plt.text(x_max*0.8, y_max*0.1, "NOT TO\nSCALE", fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.5))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat142:
    def __init__(self):
        # Parameters for N = N0 * b^(kt)
        self.n0 = round(randrange_float(50, 150, 10), 2)
        self.b = round(randrange_float(2.0, 4.0, 0.1), 2)
        self.k = round(randrange_float(0.4, 0.6, 0.01), 2)
        
        # Threshold for the population
        self.threshold = round(randrange_float(800, 1200, 50), 2)
        
        # Solve N0 * b^(kt) = threshold
        # kt * ln(b) = ln(threshold / N0)
        # t = ln(threshold / N0) / (k * ln(b))
        self.t_exact = math.log(self.threshold / self.n0) / (self.k * math.log(self.b))
        
        # The answer is the smallest integer t such that N > threshold
        self.answer = math.ceil(self.t_exact + 1e-9)

        self.description = (
            f"As shown in the figure, the growth of a bacterial culture is modeled by $N = {self.n0} \\times {self.b}^{{{self.k}t}}$, "
            f"where $N$ is the number of bacteria after $t$ hours. "
            f"Based on the figure, find the smallest integer value of $t$ for which the population exceeds {self.threshold}."
        )
        
        self.topic = "Pure Mathematics 2"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The population growth model is given by: }} N &= N_0 \\times b^{{kt}} \\\\"
            f"\\text{{Substitute the given values: }} {self.threshold} &< {self.n0} \\times {self.b}^{{{self.k}t}} \\\\"
            f"\\text{{Divide both sides by }} {self.n0}: \\frac{{{self.threshold}}}{{{self.n0}}} &< {self.b}^{{{self.k}t}} \\\\"
            f"{round(self.threshold / self.n0, 10)} &< {self.b}^{{{self.k}t}} \\\\"
            f"\\text{{Take the natural logarithm (ln) of both sides: }} \\ln({round(self.threshold / self.n0, 10)}) &< \\ln({self.b}^{{{self.k}t}}) \\\\"
            f"\\ln({round(self.threshold / self.n0, 10)}) &< {self.k}t \\ln({self.b}) \\\\"
            f"\\text{{Rearrange to solve for }} t: t &> \\frac{{\\ln({round(self.threshold / self.n0, 10)})}}{{{self.k} \\ln({self.b})}} \\\\"
            f"t &> \\frac{{{round(math.log(self.threshold / self.n0), 10)}}}{{{round(self.k * math.log(self.b), 10)}}} \\\\"
            f"t &> {round(self.t_exact, 10)} \\\\"
            f"\\text{{The smallest integer }} t \\text{{ satisfying this inequality is: }} t &= {self.answer}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # t range for plotting
        t_max = math.ceil(self.t_exact) + 2
        t_vals = np.linspace(0, t_max, 100)
        n_vals = self.n0 * (self.b ** (self.k * t_vals))
        
        # Plot growth curve
        ax.plot(t_vals, n_vals, color='black', lw=2, label='Population Growth')
        
        # Plot threshold line
        ax.axhline(y=self.threshold, color='red', linestyle='--', lw=1.5)
        
        # Shading the region above threshold
        t_fill = np.linspace(self.t_exact, t_max, 50)
        n_fill = self.n0 * (self.b ** (self.k * t_fill))
        ax.fill_between(t_fill, n_fill, self.threshold, color='gray', alpha=0.3)
        
        # Axis labels
        ax.set_xlabel('Time $t$ (hours)', fontsize=12)
        ax.set_ylabel('Number of bacteria $N$', fontsize=12)
        
        # Threshold label
        ax.text(0.2, self.threshold + 20, f"$N = {self.threshold}$", color='red', fontsize=10, fontweight='bold')
        
        # Limits and styling
        ax.set_xlim(0, t_max)
        ax.set_ylim(0, max(n_vals) * 1.1)
        ax.grid(True, linestyle=':', alpha=0.7)
        
        plt.text(t_max * 0.85, max(n_vals) * 0.05, "NOT TO\nSCALE", fontsize=10, ha='center', bbox=dict(facecolor='white', alpha=0.8))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
        
class Mat143:
    def __init__(self):
        # Substance decays according to N = N0 * e^(-lambda * t)
        # N0 is set to 100% for the percentage remaining model
        self.n0 = 100
        # Vary the half-life (t when N = 50)
        self.half_life = round(randrange_float(20.0, 80.0, 1.0), 2)
        
        # Calculate lambda based on half-life: 
        # 50 = 100 * e^(-lambda * half_life) -> 0.5 = e^(-lambda * half_life)
        # ln(0.5) = -lambda * half_life -> lambda = -ln(0.5) / half_life
        self.lambda_val = -math.log(0.5) / self.half_life
        
        # The answer is the decay constant lambda
        self.answer = round(self.lambda_val, 4)

        self.description = (
            f"As shown in the figure, a radioactive substance decays according to the model $N = 100e^{{-\\lambda t}}$, "
            f"where $N$ is the percentage of the substance remaining after $t$ years. "
            f"Based on the coordinate of the indicated point on the curve, find the value of the decay constant $\\lambda$. "
            f"Give your answer correct to four decimal places."
        )
        
        self.topic = "Pure Mathematics 2"
        self.subtopic = "Logarithmic and exponential functions"
        self.source = "Adapted from Cambridge AS & A level Mathematics 9709 Syllabus"
        self.curriculum = "AS & A Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{The decay model is given by: }} N &= 100e^{{-\\lambda t}} \\\\"
            f"\\text{{Based on the graph, when }} t &= {self.half_life}\\,\\text{{years}}, N = 50\\% \\\\"
            f"\\text{{Substitute these values into the model:}} & \\\\"
            f"50 &= 100e^{{-\\lambda({self.half_life})}} \\\\"
            f"\\text{{Divide by 100:}} & \\\\"
            f"\\frac{{50}}{{100}} &= e^{{-{self.half_life}\\lambda}} \\\\"
            f"0.5 &= e^{{-{self.half_life}\\lambda}} \\\\"
            f"\\text{{Take the natural logarithm (ln) of both sides:}} & \\\\"
            f"\\ln(0.5) &= \\ln(e^{{-{self.half_life}\\lambda}}) \\\\"
            f"\\ln(0.5) &= -{self.half_life}\\lambda \\\\"
            f"\\lambda &= \\frac{{\\ln(0.5)}}{{-{self.half_life}}} \\\\"
            f"\\lambda &= \\frac{{{round(math.log(0.5), 10)}}}{{-{self.half_life}}} \\\\"
            f"\\lambda &= {round(self.lambda_val, 10)} \\\\"
            f"\\text{{To four decimal places:}} & \\\\"
            f"\\lambda &= {self.answer}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Time range for plotting: show a bit more than two half-lives
        t_max = self.half_life * 2.2
        t_vals = np.linspace(0, t_max, 500)
        n_vals = self.n0 * np.exp(-self.lambda_val * t_vals)
        
        # Draw the exponential decay curve
        ax.plot(t_vals, n_vals, color='black', lw=2)
        
        # Mark the specific point (half-life, 50%)
        ax.scatter(self.half_life, 50, color='black', s=50, zorder=5)
        
        # Draw dashed lines to the axes to make the reading implicit
        ax.plot([self.half_life, self.half_life], [0, 50], color='gray', linestyle='--', lw=1)
        ax.plot([0, self.half_life], [50, 50], color='gray', linestyle='--', lw=1)
        
        # Label the marked point
        ax.text(self.half_life + (t_max * 0.02), 52, f"({self.half_life}, 50)", fontsize=12, fontweight='bold')
        
        # Axis setup
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        
        # Labels and limits
        ax.set_xlabel('Time $t$ (years)', loc='right', fontsize=12)
        ax.set_ylabel('Percentage $N$', loc='top', fontsize=12, rotation=0)
        
        ax.set_xlim(0, t_max)
        ax.set_ylim(0, 110)
        
        # Highlight initial value
        ax.text(- (t_max * 0.05), 100, "100", fontsize=10, weight='bold')
        
        ax.grid(True, linestyle=':', alpha=0.6)
        
        plt.text(t_max * 0.8, 100, "NOT TO\nSCALE", fontsize=10, ha='center', 
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight', dpi=100)
        plt.close()
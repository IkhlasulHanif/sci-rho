import numpy as np
import pandas as pd
import random as rnd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
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
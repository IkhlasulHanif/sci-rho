import numpy as np
import pandas as pd
import random as rnd
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
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
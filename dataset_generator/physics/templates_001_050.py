import random as rnd
import os
import matplotlib.pyplot as plt
import math

from PIL import Image
from physics.helper import *

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Phy001:

    def __init__(self):
        self.lower_bound = rnd.randint(1,10)
        self.upper_bound = rnd.randint(15,29)
        self.length = self.upper_bound - self.lower_bound
        self.start = 60 * self.lower_bound
        self.end = 60 * (self.lower_bound + self.length)
        self.answer = self.length

        self.description = "Move the ruler to measure the length of the line to the nearest centimeter. The line is about (_) centimeters long."
        self.topic = "Motion, forces and energy"
        self.subtopic = "Physical quantities and measurement techniques"
        self.source = "DynaMath"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Left point}} &= {self.lower_bound}\\,\\text{{cm}}\\\\"
            f"\\text{{Right point}} &= {self.upper_bound}\\,\\text{{cm}}\\\\"
            f"\\text{{The length of the line is given by:}} &\\\\"
            f"Length &= Right - Left\\\\"
            f"&= {self.upper_bound} - {self.lower_bound}\\\\"
            f"&= {self.length}\\,\\text{{cm}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy001temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.hlines(200, self.start, self.end, colors="black", linewidth=4)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy002:

    def __init__(self):
        self.water_volume_default = rnd.randint(5, 25)
        self.object_volume = rnd.randint(5, 15)
        self.water_volume_filled = self.water_volume_default + self.object_volume
        self.answer = self.object_volume

        self.description = "A measuring cylinder initially contains the amount of water shown in the left image. When a piece of stone is placed into the cylinder, the water level rises as shown in the right image. The volume of the stone is ... ml"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Physical quantities and measurement techniques"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Initial volume of water}} &= {self.water_volume_default}\\,\\text{{ml}}\\\\"
            f"\\text{{Final volume after object is immersed}} &= {self.water_volume_filled}\\,\\text{{ml}}\\\\"
            f"\\text{{Volume of object is given by:}} &\\\\"
            f"V_{{\\text{{object}}}} &= V_{{\\text{{final}}}} - V_{{\\text{{initial}}}}\\\\"
            f"&= {self.water_volume_filled} - {self.water_volume_default}\\\\"
            f"&= {self.object_volume}\\,\\text{{ml}}"
            "\\end{aligned}\\]"
        )
    
    def _draw_rectangle(self, ax, x_left, x_right, volume, y_min, y_max, value_min=0, value_max=30, color="skyblue"):
        """Draw a rectangle representing water / stone up to given volume."""
        y_top = val_mapper(volume, y_min, y_max, value_min, value_max)
        y_bottom = val_mapper(0, y_min, y_max, value_min, value_max)
        ax.fill_betweenx([y_bottom, y_top], x_left, x_right, color=color, alpha=0.7)

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy002temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)

        # Common axis setup
        y_min, y_max = 178, 965
        value_min, value_max = 0, 50

        # Draw vertical axes
        draw_axis(ax, 330, y_min, y_max, value_min, value_max, 5, 2, "v")
        draw_axis(ax, 814, y_min, y_max, value_min, value_max, 5, 2, "v")

        # Beaker 1 (water, initial)
        self._draw_rectangle(ax, x_left=107, x_right=288,
                          volume=self.water_volume_default,
                          y_min=y_min, y_max=y_max,
                          value_min=value_min, value_max=value_max,
                          color="skyblue")

        # Beaker 2 (water, final)
        self._draw_rectangle(ax, x_left=592, x_right=773,
                          volume=self.water_volume_filled,
                          y_min=y_min, y_max=y_max,
                          value_min=value_min, value_max=value_max,
                          color="skyblue")

        # Object inside beaker 2 (overlapping the previously drawn water)
        self._draw_rectangle(ax, x_left=592, x_right=773,
                          volume=self.object_volume,
                          y_min=y_min, y_max=y_max,
                          value_min=value_min, value_max=value_max,
                          color="#655353")
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy003:

    def __init__(self):
        self.x_direction = rnd.randint(-18, 18)
        self.y_direction = rnd.randint(-18, 18)
        while self.x_direction in range(-5, 6) or self.y_direction in range(-5, 6):
            self.x_direction = rnd.randint(-18, 18)
            self.y_direction = rnd.randint(-18, 18)
        self.resultant = math.sqrt(self.x_direction**2 + self.y_direction**2)
        self.answer = round(self.resultant, 2)

        self.description = "A box experiences two perpendicular forces as shown in the diagram. The magnitude of the resultant force is (_) N"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Physical quantities and measurement techniques"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Horizontal component}} &= {self.x_direction}\\,\\text{{N}}\\\\"
            f"\\text{{Vertical component}} &= {self.y_direction}\\,\\text{{N}}\\\\"
            f"\\text{{Resultant force is given by:}} &\\\\"
            f"R &= \\sqrt{{F_x^2 + F_y^2}}\\\\"
            f"&= \\sqrt{{({self.x_direction})^2 + ({self.y_direction})^2}}\\\\"
            f"&= \\sqrt{{{self.x_direction**2} + {self.y_direction**2}}}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def _draw_forces(self, ax):
        """Draw force vectors acting on the box."""
        if self.x_direction < 0:
            ax.arrow(0, 0, self.x_direction + 1, 0,
                    head_width=0.4, head_length=0.9, fc="red", ec="red", linewidth=2)
        else:
            ax.arrow(0, 0, self.x_direction - 1, 0,
                    head_width=0.4, head_length=0.9, fc="red", ec="red", linewidth=2)
        if self.y_direction < 0:
            ax.arrow(0, 0, 0, self.y_direction + 1,
                    head_width=0.4, head_length=0.9, fc="blue", ec="blue", linewidth=2)
        else:
            ax.arrow(0, 0, 0, self.y_direction - 1,
                 head_width=0.4, head_length=0.9, fc="blue", ec="blue", linewidth=2)

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, tickrange=2)

        # draw rectangle
        rect = plt.Rectangle((-1, -1), 2, 2, linewidth=2, edgecolor="black", facecolor="lightgray")
        ax.add_patch(rect)

        self._draw_forces(ax)

        plt.title("Forces Acting on the Box")
        plt.gca().set_aspect('equal', adjustable='box')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy004:

    def __init__(self):
        self.speed = rnd.randint(50, 120) / 10
        self.time = rnd.randint(3, 10)
        self.distance = round(self.speed * self.time, 2)
        self.answer = round(self.speed, 2)

        self.description = f"A cat moves from point A to point B to reach its meal within {self.time} seconds. Assuming it moves with constant velocity, the speed of the cat is ... m/s"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Time taken}} &= {self.time}\\,\\text{{s}}\\\\"
            f"\\text{{Distance covered}} &= {self.distance}\\,\\text{{m}}\\\\"
            f"\\text{{Speed is given by:}} &\\\\"
            f"v &= \\frac{{d}}{{t}}\\\\"
            f"&= \\frac{{{self.distance}}}{{{self.time}}}\\\\"
            f"&= {self.speed}\\,\\text{{m/s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy004temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis("off")
        ax.text(680, 325, f"{self.distance} m", fontsize=10)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Phy005:

    def __init__(self):
        self.first_distance = rnd.randint(4, 15)
        self.first_time = rnd.randint(4, 15)
        self.second_distance = rnd.randint(4, 15)
        self.second_time = rnd.randint(4, 15)
        self.third_distance = rnd.randint(-15, -5)
        self.third_time = rnd.randint(4, 15)
        self.total_distance = abs(self.first_distance) + \
                             abs(self.second_distance) + \
                             abs(self.third_distance)
        self.total_time = self.first_time + self.second_time + self.third_time
        self.answer = round(self.total_distance / self.total_time, 2)
        self.description = f"Andy walks along the path shown in the diagram. The first, second, and third paths are traveled in {self.first_time}, {self.second_time}, and {self.third_time} seconds, respectively. His average speed is ... m/s"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{First distance}} &= {self.first_distance}\\,\\text{{m}},\\quad \\text{{Time}} = {self.first_time}\\,\\text{{s}}\\\\"
            f"\\text{{Second distance}} &= {self.second_distance}\\,\\text{{m}},\\quad \\text{{Time}} = {self.second_time}\\,\\text{{s}}\\\\"
            f"\\text{{Third distance}} &= {self.third_distance}\\,\\text{{m}},\\quad \\text{{Time}} = {self.third_time}\\,\\text{{s}}\\\\"
            f"\\text{{Total distance travelled}} &= |d_1| + |d_2| + |d_3|\\\\"
            f"&= |{self.first_distance}| + |{self.second_distance}| + |{self.third_distance}|\\\\"
            f"&= {abs(self.first_distance)} + {abs(self.second_distance)} + {abs(self.third_distance)}\\\\"
            f"&= {self.total_distance}\\,\\text{{m}}\\\\"
            f"\\text{{Total time taken}} &= t_1 + t_2 + t_3\\\\"
            f"&= {self.first_time} + {self.second_time} + {self.third_time}\\\\"
            f"&= {self.total_time}\\,\\text{{s}}\\\\"
            f"\\text{{Average speed is given by:}} &\\\\"
            f"v_{{\\text{{avg}}}} &= \\frac{{\\text{{total distance}}}}{{\\text{{total time}}}}\\\\"
            f"&= \\frac{{{self.total_distance}}}{{{self.total_time}}}\\\\"
            f"&= {self.answer}\\,\\text{{m/s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        plt.axis("off")
        draw_labeled_arrow(ax, (0, 0), (self.first_distance, 0), f'{self.first_distance} m')
        draw_labeled_arrow(ax, (self.first_distance, 0), (self.first_distance, self.second_distance), f'{self.second_distance} m')
        draw_labeled_arrow(ax, (self.first_distance, self.second_distance), (self.first_distance + self.third_distance, self.second_distance), f'{abs(self.third_distance)} m')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight")
        plt.close()

class Phy006:

    def __init__(self):
        self.m = rnd.randint(3, 15) / 5
        self.c = rnd.randint(1, 6)
        self.answer = round(self.m, 2)

        self.description = f"An object moves with a constant velocity. The distance-time graph below represents its motion. According to the graph, the velocity of the object is (_) m/s"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the distance-time graph, the gradient represents the velocity.}} &\\\\"
            f"v &= \\frac{{\\Delta d}}{{\\Delta t}}\\\\"
            f"\\text{{Given that the gradient of the graph is}} &= {self.m}\\\\"
            f"\\text{{Therefore, the velocity of the object is:}} &\\\\"
            f"v &= {self.m}\\,\\text{{m/s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, xmin=0, ymin=0, xmax=10, ymax=int(self.m*10+self.c)+1, tickrange=2, xlabel="time (s)", ylabel="distance (m)")
        ax.plot([0, 10], [self.c, self.m*10 + self.c], color="blue", linewidth=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy007:

    def __init__(self):
        self.m = rnd.randint(3, 15) / 5
        self.c = rnd.randint(1, 6)
        self.t1 = rnd.randint(10, 40) / 10
        self.t2 = rnd.randint(50, 90) / 10
        self.answer = round(self.m * (self.t2 - self.t1), 2)

        self.description = f"An object moves with a constant velocity. The distance-time graph below represents its motion. According to the graph, the displacement of the object between t={self.t1} and t={self.t2} is (_) m"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the distance-time graph, the gradient represents velocity.}} &\\\\"
            f"v &= \\frac{{\\Delta d}}{{\\Delta t}} = m\\\\"
            f"\\text{{Displacement between }} t_1 \\text{{ and }} t_2 \\text{{ is given by:}} &\\\\"
            f"\\Delta d &= v (t_2 - t_1)\\\\"
            f"&= m (t_2 - t_1)\\\\"
            f"&= {self.m} ({self.t2} - {self.t1})\\\\"
            f"&= {self.m * (self.t2 - self.t1)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, xmin=0, ymin=0, xmax=10, ymax=int(self.m*10+self.c)+1, tickrange=2, xlabel="time (s)", ylabel="distance (m)")
        ax.plot([0, 10], [self.c, self.m*10 + self.c], color="blue", linewidth=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy008:

    def __init__(self):
        self.m = rnd.randint(3, 15) / 5
        self.c = rnd.randint(1, 6)
        self.t = rnd.randint(2, 9)
        self.answer = round(self.m * self.t + self.c, 2)

        self.description = f"An object moves with a constant acceleration. The velocity-time graph below represents its motion. According to the graph, the velocity of the object at t={self.t} is (_) m/s"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}} &\\\\"
            f"a &= {self.m}\\,\\text{{m/s}}^2\\\\"
            f"u &= {self.c}\\,\\text{{m/s}}\\\\"
            f"t &= {self.t}\\,\\text{{s}}\\\\"
            f"\\text{{The velocity is given by:}} &\\\\"
            f"v &= u + at\\\\"
            f"&= {self.c} + ({self.m})({self.t})\\\\"
            f"&= {round(self.c + self.m * self.t,10)}\\\\"
            f"&= {self.answer}\\,\\text{{m/s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, xmin=0, ymin=0, xmax=10, ymax=int(self.m*10+self.c)+1, tickrange=2, xlabel="time (s)", ylabel="velocity (m/s)")
        ax.plot([0, 10], [self.c, self.m*10 + self.c], color="blue", linewidth=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy009:

    def __init__(self):
        self.m = rnd.randint(3, 15) / 5
        self.c = rnd.randint(1, 6)
        self.t1 = rnd.randint(0, 40) / 10
        self.t2 = rnd.randint(50, 100) / 10
        delta_t = round(self.t2 - self.t1, 5)
        self.answer = self.c * delta_t + (self.m * delta_t**2)/2 # v0 . t + 1/2 a . t^2 formula
        self.answer = round(self.answer, 2)

        self.description = f"An object moves with a constant acceleration. The velocity-time graph below represents its motion. According to the graph, the displacement of the object between t={self.t1} and t={self.t2} is (_) m"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Motion"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}} &\\\\"
            f"a &= {self.m}\\,\\text{{m/s}}^2\\\\"
            f"u &= {self.c}\\,\\text{{m/s}}\\\\"
            f"t_1 &= {self.t1}\\,\\text{{s}}\\\\"
            f"t_2 &= {self.t2}\\,\\text{{s}}\\\\"
            f"\\text{{Change in time:}} &\\\\"
            f"\\Delta t &= t_2 - t_1\\\\"
            f"&= {self.t2} - {self.t1}\\\\"
            f"&= {round(self.t2 - self.t1,10)}\\,\\text{{s}}\\\\"
            f"\\text{{Displacement is given by:}} &\\\\"
            f"s &= ut + \\tfrac{{1}}{{2}}at^2\\\\"
            f"&= {self.c}\\times({round(self.t2 - self.t1,10)}) + \\tfrac{{1}}{{2}}\\times{self.m}\\times({round(self.t2 - self.t1,10)})^2\\\\"
            f"&= {round(self.c * (self.t2 - self.t1),10)} + {round((self.m * (self.t2 - self.t1)**2)/2,10)}\\\\"
            f"&= {self.answer}\\,\\text{{m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, xmin=0, ymin=0, xmax=10, ymax=int(self.m*10+self.c)+1, tickrange=2, xlabel="time (s)", ylabel="velocity (m/s)")
        ax.plot([0, 10], [self.c, self.m*10 + self.c], color="blue", linewidth=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy010:

    def __init__(self):
        self.r = rnd.randint(50, 150) / 5
        self.h = 2 * self.r + rnd.randint(-2, 2)
        self.m = rnd.randint(1, 10) * 10
        volume = 3.14 * ((self.r/100)**2) * (self.h/100) # cylinder volume formula, adjust from cm to m
        self.answer = round(self.m / volume, 2)

        self.description = f"A solid cylinder of mass m={self.m} kg has the dimension given in the image. The density of the cylinder is ... kg/m^3 (use π=3.14)"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Density"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}} &\\\\"
            f"m &= {self.m}\\,\\text{{kg}}\\\\"
            f"r &= {self.r}\\,\\text{{cm}} = {round(self.r/100,10)}\\,\\text{{m}}\\\\"
            f"h &= {self.h}\\,\\text{{cm}} = {round(self.h/100,10)}\\,\\text{{m}}\\\\"
            f"\\text{{Volume of a cylinder is given by:}} &\\\\"
            f"V &= \\pi r^2 h\\\\"
            f"&= 3.14 \\times ({round(self.r/100,10)})^2 \\times ({round(self.h/100,10)})\\\\"
            f"&= 3.14 \\times {round((self.r/100)**2,10)} \\times {round(self.h/100,10)}\\\\"
            f"&= {round(3.14 * ((self.r/100)**2) * (self.h/100),10)}\\,\\text{{m}}^3\\\\"
            f"\\text{{Density is given by:}} &\\\\"
            f"\\rho &= \\frac{{m}}{{V}}\\\\"
            f"&= \\frac{{{self.m}}}{{{round(3.14 * ((self.r/100)**2) * (self.h/100),10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{kg/m}}^3"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy010temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(300, 35, f"r = {self.r} cm", fontsize=10)
        ax.text(420, 326, f"h = {self.h} cm", fontsize=10)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy011:

    def __init__(self):
        self.f1 = rnd.randint(2, 12)
        self.f2 = rnd.randint(-12, -2)
        self.f3 = rnd.choice([-5, -4, -3, 3, 4, 5])
        self.mass = rnd.choice([1, 2, 4, 5, 8, 10])
        while self.f1 + self.f2 + self.f3 == 0:
            self.f3 = rnd.randint(-4, 4)
        self.acceleration = (self.f1 + self.f2 + self.f3) / self.mass
        self.answer = round(self.acceleration, 2)

        self.description = f"A {self.mass} kg box is being pulled by three forces along the horizontal axis, as shown in the diagram. The box is accelerating at ... m/s² (a positive value indicates acceleration toward the positive horizontal axis, and a negative value indicates the opposite)."
        self.topic = "Motion, forces and energy"
        self.subtopic = "Forces"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Force 1}} &= {self.f1}\\,\\text{{N}}\\\\"
            f"\\text{{Force 2}} &= {self.f2}\\,\\text{{N}}\\\\"
            f"\\text{{Force 3}} &= {self.f3}\\,\\text{{N}}\\\\"
            f"\\text{{Mass}} &= {self.mass}\\,\\text{{kg}}\\\\"
            f"\\text{{Net force is given by:}} &\\\\"
            f"F_\\text{{net}} &= F_1 + F_2 + F_3\\\\"
            f"&= ({self.f1}) + ({self.f2}) + ({self.f3})\\\\"
            f"&= {round(self.f1 + self.f2 + self.f3, 10)}\\,\\text{{N}}\\\\"
            f"\\text{{From Newton's Second Law:}} &\\\\"
            f"F_\\text{{net}} &= m a\\\\"
            f"a &= \\frac{{F_\\text{{net}}}}{{m}}\\\\"
            f"&= \\frac{{{round(self.f1 + self.f2 + self.f3, 10)}}}{{{self.mass}}}\\\\"
            f"&= {self.answer}\\,\\text{{m/s}}^2"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        rect = plt.Rectangle((-1, -1), 2, 2, linewidth=2, edgecolor="black", facecolor="lightgray")
        ax.add_patch(rect)
        draw_cartesian(ax, -20, 20, -20, 20, 5, "X", "Y")
        
        # draw f1, f2, and f3
        draw_labeled_arrow(ax, (0, 1), (self.f1, 1), f"{self.f1} N")
        draw_labeled_arrow(ax, (0, 0), (self.f2, 0), f"{self.f2} N")
        draw_labeled_arrow(ax, (0, -1), (self.f3, -1), f"{self.f3} N")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy012:

    def __init__(self):
        self.mass = rnd.randint(10, 100) / 10
        self.weight = self.mass * 10 # assume g = 10 m/s²
        self.spring_displacement = rnd.choice([2, 4, 5, 8, 10, 20, 40, 50])
        spring_displacement_in_meters = self.spring_displacement / 100
        self.spring_constant = self.weight / spring_displacement_in_meters
        self.answer = round(self.spring_constant, 2)
        
        self.description = f"A spring is hung from the ceiling and is initially relaxed. A box is then attached to the spring, causing it to stretch as shown in the image. The spring constant (k) is ... N/m (assume g = 10 m/s²)"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Forces"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}} &\\\\"
            f"m &= {self.mass}\\,\\text{{kg}}\\\\"
            f"g &= 10\\,\\text{{m/s}}^2\\\\"
            f"\\text{{Spring displacement}} &= {self.spring_displacement}\\,\\text{{cm}} = {round(self.spring_displacement / 100, 10)}\\,\\text{{m}}\\\\"
            f"\\text{{Weight of the box:}} &\\\\"
            f"W &= m g\\\\"
            f"&= ({self.mass})({10})\\\\"
            f"&= {round(self.weight, 10)}\\,\\text{{N}}\\\\"
            f"\\text{{From Hooke's Law:}} &\\\\"
            f"F &= kx\\\\"
            f"k &= \\frac{{F}}{{x}}\\\\"
            f"&= \\frac{{{round(self.weight, 10)}}}{{{round(self.spring_displacement / 100, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{N/m}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy012temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(450, 380, f"{self.spring_displacement} cm", fontsize=10)
        ax.text(217, 460, f"{self.mass} kg", fontsize=16)
        
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy013:

    def __init__(self):
        self.breaking_point = rnd.randint(10, 20)
        self.answer = rnd.randint(6, 28)
        self.spring_constant = self.answer / self.breaking_point

        self.description = f"The graph shows the load-extension relationship of a spring under an applied force. From the graph, we can conclude that at F = ... N, the spring no longer obeys Hooke's law."
        self.topic = "Motion, forces and energy"
        self.subtopic = "Forces"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{From the graph, the spring obeys Hooke's law only up to }} x = {self.breaking_point}\\,\\text{{m.}}\\\\"
            f"\\text{{At this point,}}\\ F &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )
        
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 10))
        draw_cartesian(ax, xmin=0, ymin=0, xmax=30, ymax=30, tickrange=2, xlabel="Displacement (m)", ylabel="Force (kN)")
        ax.plot([0, self.breaking_point], [0, self.spring_constant * self.breaking_point], color="blue", linewidth=2)

        # --- Yielding region (logarithmic curve) ---
        x1 = self.breaking_point
        F1 = self.spring_constant * x1

        x_yield = np.linspace(x1, 30, 200)

        # Scale logarithmically from F1 to F1 + 1
        F_yield = F1 + np.log1p(x_yield - x1) * (1 / np.log1p(30 - x1))

        ax.plot(x_yield, F_yield, color="blue", linewidth=2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy014:

    def __init__(self):
        self.box_mass = rnd.randint(2, 10)
        self.plank_mass = rnd.randint(15, 30)
        self.pivot_to_plank_com = rnd.randint(15, 20) * 10
        self.plank_com_to_rope = rnd.randint(5, 10) * 10
        self.rope_to_box = rnd.randint(1, 4) * 10

        # assume g = 10 m/s².
        # the net torque at the pivot must be zero
        box_torque = (self.box_mass * 10) * (self.pivot_to_plank_com + self.plank_com_to_rope + self.rope_to_box)
        plank_torque = (self.plank_mass * 10) * (self.pivot_to_plank_com)
        rope_tension = (box_torque + plank_torque) / (self.pivot_to_plank_com + self.plank_com_to_rope) # tension = torque / distance
        self.answer = round(rope_tension, 2)
        
        self.description = f"A wooden plank of mass {self.plank_mass} kg is pivoted at one end and held stationary. A box is attached to the other end of the plank. Between the box and the pivot, a rope is also tied to the plank. The distances between the pivot, the plank's center of mass, the rope, and the box are shown in the diagram. Determine the tension in the rope (assume g = 10 m/s²)!"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Forces"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Given:}} &\\\\"
            f"m_\\text{{box}} &= {self.box_mass}\\,\\text{{kg}}\\\\"
            f"m_\\text{{plank}} &= {self.plank_mass}\\,\\text{{kg}}\\\\"
            f"d_1 &= {self.pivot_to_plank_com}\\,\\text{{cm}} = {round(self.pivot_to_plank_com/100,10)}\\,\\text{{m}}\\\\"
            f"d_2 &= {self.plank_com_to_rope}\\,\\text{{cm}} = {round(self.plank_com_to_rope/100,10)}\\,\\text{{m}}\\\\"
            f"d_3 &= {self.rope_to_box}\\,\\text{{cm}} = {round(self.rope_to_box/100,10)}\\,\\text{{m}}\\\\"
            f"g &= 10\\,\\text{{m/s}}^2\\\\"
            f"\\text{{At equilibrium, net torque about the pivot is zero:}} &\\\\"
            f"T (d_1 + d_2) &= (m_\\text{{box}} g)(d_1 + d_2 + d_3) + (m_\\text{{plank}} g)(d_1)\\\\"
            f"T &= \\frac{{(m_\\text{{box}} g)(d_1 + d_2 + d_3) + (m_\\text{{plank}} g)(d_1)}}{{(d_1 + d_2)}}\\\\"
            f"&= \\frac{{({self.box_mass})(10)({round((self.pivot_to_plank_com + self.plank_com_to_rope + self.rope_to_box)/100,10)}) + ({self.plank_mass})(10)({round(self.pivot_to_plank_com/100,10)})}}{{{round((self.pivot_to_plank_com + self.plank_com_to_rope)/100,10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy014temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(30, 234, f"{self.box_mass} kg", fontsize=8)
        ax.text(102, 106, f"{self.rope_to_box} cm", fontsize=6)
        ax.text(272, 106, f"{self.plank_com_to_rope} cm", fontsize=6)
        ax.text(500, 106, f"{self.pivot_to_plank_com} cm", fontsize=6)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy015:

    def __init__(self):
        self.mass_first_cart = rnd.randint(5, 40) / 10
        self.velocity_first_cart = rnd.randint(4, 12) / 4
        self.mass_second_cart = rnd.randint(5, 40) / 10
        self.final_velocity = self.mass_first_cart * self.velocity_first_cart / (self.mass_first_cart + self.mass_second_cart)
        self.answer = round(self.final_velocity, 2)
        
        self.description = f"Two carts are on a frictionless track. Cart A moves toward cart B, which is initially at rest, as shown in the image. After they collide, the carts stick together and move as one. Determine their common velocity after the collision!"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Momentum"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of cart A}} &= {self.mass_first_cart}\\,\\text{{kg}}\\\\"
            f"\\text{{Velocity of cart A before collision}} &= {self.velocity_first_cart}\\,\\text{{m/s}}\\\\"
            f"\\text{{Mass of cart B}} &= {self.mass_second_cart}\\,\\text{{kg}}\\\\"
            f"\\text{{Velocity of cart B before collision}} &= 0\\,\\text{{m/s}}\\\\"
            f"\\text{{After collision (perfectly inelastic), both carts move together with velocity }} v_f. &\\\\"
            f"\\text{{By conservation of momentum:}} &\\\\"
            f"m_1 v_1 + m_2 v_2 &= (m_1 + m_2)v_f\\\\"
            f"v_f &= \\frac{{m_1 v_1 + m_2 v_2}}{{m_1 + m_2}}\\\\"
            f"&= \\frac{{({self.mass_first_cart})({self.velocity_first_cart}) + ({self.mass_second_cart})(0)}}{{({self.mass_first_cart}) + ({self.mass_second_cart})}}\\\\"
            f"&= \\frac{{{round(self.mass_first_cart * self.velocity_first_cart, 10)}}}{{{round(self.mass_first_cart + self.mass_second_cart, 10)}}}\\\\"
            f"&= {self.answer}\\,\\text{{m/s}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy015temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(262, 111, f"{self.velocity_first_cart} m/s", fontsize=6)
        ax.text(125, 70, f"{self.mass_first_cart} kg", fontsize=8)
        ax.text(645, 70, f"{self.mass_second_cart} kg", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy016:

    def __init__(self):
        self.ball_mass = rnd.randint(1, 20) / 2
        self.initial_height = rnd.randint(8, 30)
        self.final_height = self.initial_height / 2 + rnd.randint(-1, 1)
        self.final_kinetic_energy = self.ball_mass * (self.initial_height - self.final_height) * 10 # assume g = 10 m/s²
        self.answer = round(self.final_kinetic_energy, 2)
        
        self.description = f"A ball is released from rest at the top of a smooth (frictionless) inclined plane, as shown in the figure. It slides down to a point at height h = {self.final_height} m above the ground. Assuming g = 10 m/s², what is the kinetic energy of the ball at this point?"
        self.topic = "Motion, forces and energy"
        self.subtopic = "Energy, work and power"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of the ball}} &= {self.ball_mass}\\,\\text{{kg}}\\\\"
            f"\\text{{Initial height}} &= {self.initial_height}\\,\\text{{m}}\\\\"
            f"\\text{{Final height}} &= {self.final_height}\\,\\text{{m}}\\\\"
            f"g &= 10\\,\\text{{m/s}}^2\\\\"
            f"\\text{{Loss in potential energy equals gain in kinetic energy:}} &\\\\"
            f"E_k &= m g (h_1 - h_2)\\\\"
            f"&= ({self.ball_mass})({10})(({self.initial_height}) - ({self.final_height}))\\\\"
            f"&= {round(self.ball_mass * 10 * (self.initial_height - self.final_height), 10)}\\\\"
            f"&= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy016temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(28, 370, f"{self.initial_height} m", fontsize=6)
        ax.text(195, 70, f"{self.ball_mass} kg", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy017:

    def __init__(self):
        self.horizontal_force = rnd.randint(3, 10) * 5
        self.friction_force = rnd.randint(2, 10)
        self.distance_travelled = rnd.randint(5, 20)
        self.box_mass = rnd.randint(5, 15)
        self.work_by_horizontal_force = self.horizontal_force * self.distance_travelled
        self.work_by_friction_force = self.friction_force * self.distance_travelled
        self.net_work = self.work_by_horizontal_force - self.work_by_friction_force
        self.answer = round(self.net_work, 2)
        
        self.description = (
            f"A box of mass {self.box_mass} kg is pulled along a rough horizontal surface by a constant horizontal force. "
            f"The frictional force acting on the box is shown in the diagram. "
            f"The box moves the distance indicated in the diagram. "
            f"Determine the net work done on the box!"
        )
        self.topic = "Motion, forces and energy"
        self.subtopic = "Energy, work and power"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Applied force}} &= {self.horizontal_force}\\,\\text{{N}}\\\\"
            f"\\text{{Frictional force}} &= {self.friction_force}\\,\\text{{N}}\\\\"
            f"\\text{{Displacement}} &= {self.distance_travelled}\\,\\text{{m}}\\\\"
            f"\\text{{Work done by the applied force:}} &\\\\"
            f"W_1 &= F_\\text{{applied}} \\times s\\\\"
            f"&= ({self.horizontal_force})({self.distance_travelled})\\\\"
            f"&= {round(self.work_by_horizontal_force, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Work done against friction:}} &\\\\"
            f"W_2 &= F_\\text{{friction}} \\times s\\\\"
            f"&= ({self.friction_force})({self.distance_travelled})\\\\"
            f"&= {round(self.work_by_friction_force, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Net work done on the box:}} &\\\\"
            f"W_\\text{{net}} &= W_1 - W_2\\\\"
            f"&= {round(self.work_by_horizontal_force, 10)} - {round(self.work_by_friction_force, 10)}\\\\"
            f"&= {self.answer}\\,\\text{{J}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy017temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(628, 280, f"{self.friction_force} N", fontsize=8)
        ax.text(1148, 241, f"{self.horizontal_force} N", fontsize=8)
        ax.text(572, 95, f"{self.distance_travelled} m", fontsize=6)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy018:

    def __init__(self):
        self.load_mass = rnd.randint(5, 20) * 10
        self.height = rnd.randint(6, 10) * 5
        self.energy_transfered = self.load_mass * self.height * 10 # assume g = 10 m/s²
        self.efficiency =  rnd.choice([20, 25, 40, 50])
        self.energy_used = self.energy_transfered / (self.efficiency / 100)
        self.answer = round(self.efficiency, 2)
        
        self.description = (
            f"A crane is used to lift a load to the height shown in the diagram. "
            f"The motor of the crane uses {self.energy_used} J of energy. "
            f"The efficiency of the motor is ... % (assume g = 10 m/s²)"
        )
        self.topic = "Motion, forces and energy"
        self.subtopic = "Energy, work and power"
        self.source = "Original"
        self.curriculum = "IGCSE"
        self.reasoning = (
            "\\[\\begin{aligned}"
            f"\\text{{Mass of load}} &= {self.load_mass}\\,\\text{{kg}}\\\\"
            f"\\text{{Height lifted}} &= {self.height}\\,\\text{{m}}\\\\"
            f"g &= 10\\,\\text{{m/s}}^2\\\\"
            f"\\text{{Energy transferred to the load:}} &\\\\"
            f"E_\\text{{useful}} &= m g h\\\\"
            f"&= ({self.load_mass})({10})({self.height})\\\\"
            f"&= {round(self.energy_transfered, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Energy supplied by the motor:}} &\\\\"
            f"E_\\text{{input}} &= {round(self.energy_used, 10)}\\,\\text{{J}}\\\\"
            f"\\text{{Efficiency is given by:}} &\\\\"
            f"\\eta &= \\frac{{E_\\text{{useful}}}}{{E_\\text{{input}}}} \\times 100\\\\"
            f"&= \\frac{{{round(self.energy_transfered, 10)}}}{{{round(self.energy_used, 10)}}} \\times 100\\\\"
            f"&= {self.answer}\\,\\%"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        img = Image.open('physics/temp_image/Phy018temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.text(212, 454, f"{self.load_mass} kg", fontsize=8)
        ax.text(351, 341, f"{self.height} m", fontsize=8)
        plt.axis("off")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

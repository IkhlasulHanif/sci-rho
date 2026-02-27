import random as rnd
import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PIL import Image
from physics.helper import *
from fractions import Fraction

# target folder : "root/dataset/physics/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "physics", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

class Phy126:
    """
    Circular Motion on a Banked Curve.
    Calculates Centripetal Force: Fc = (m * v^2) / r.
    Reference: Cambridge International AS & A Level Physics (Sang, Jones, et al.)
    """

    def __init__(self):
        
        self.mass = rnd.randint(10, 18) * 100       # 1000 - 1800 kg
        self.velocity = rnd.randint(20, 35)         # 20 - 35 m/s
        self.radius = rnd.randint(25, 50) * 10      # 250 - 500 m
        
        
        self.fc = (self.mass * (self.velocity**2)) / self.radius
        self.answer = round(self.fc, 2)

        self.description = (
            f"A car of mass {self.mass} kg travels at a constant speed of {self.velocity} m/s "
            f"around a curved section of road with a radius of curvature of {self.radius} m. "
            "The road is banked so that no friction is required for the turn. "
            "Calculate the centripetal force acting on the car. (_) N"
        )

        self.topic = "Motion in a circle"
        self.subtopic = "Centripetal Acceleration"
        self.source = "Past Papers"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Identify the given physical quantities} \\\\"
            f"\\text{{Mass, }} m &= {round(self.mass, 10)}\\,\\text{{kg}} \\\\"
            f"\\text{{Velocity, }} v &= {round(self.velocity, 10)}\\,\\text{{m s}}^{{-1}} \\\\"
            f"\\text{{Radius, }} r &= {round(self.radius, 10)}\\,\\text{{m}} \\\\[10pt]"
            "\\textbf{Step 2: State the formula for centripetal force} \\\\"
            "F_c &= \\frac{mv^2}{r} \\\\[10pt]"
            "\\textbf{Step 3: Substitute the values into the equation} \\\\"
            f"F_c &= \\frac{{{round(self.mass, 10)} \\times ({round(self.velocity, 10)})^2}}{{{round(self.radius, 10)}}} \\\\"
            f"F_c &= \\frac{{{round(self.mass, 10)} \\times {round(self.velocity**2, 10)}}}{{{round(self.radius, 10)}}} \\\\[10pt]"
            "\\textbf{Step 4: Calculate the final resultant force} \\\\"
            f"F_c &= {self.answer}\\,\\text{{N}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')

        theta_deg = 15
        theta_rad = math.radians(theta_deg)
        
        road_x = [1, 9]
        road_y = [2, 2 + 8 * math.tan(theta_rad)]
        ax.plot([1, 9], [2, 2], color='black', lw=1.5, linestyle='--')
        ax.plot(road_x, road_y, color='black', lw=3)
        
        arc = patches.Arc((1, 2), 3, 3, theta1=0, theta2=theta_deg, color='red', lw=1.5)
        ax.add_patch(arc)
        ax.text(2.8, 2.3, f"{theta_deg}°", fontsize=14, color='red')

        car_center_x = 5
        car_center_y = 2 + (car_center_x - 1) * math.tan(theta_rad)
    
        car = patches.Rectangle((car_center_x-0.7, car_center_y), 1.4, 0.8, 
                                angle=theta_deg, color='darkgray', ec='black', zorder=3)
        ax.add_patch(car)

        ax.annotate('', xy=(car_center_x, car_center_y-1.5), xytext=(car_center_x, car_center_y+0.4),
                    arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
        ax.text(car_center_x + 0.2, car_center_y - 1.4, r"$W$", fontsize=12, color='blue')

        n_len = 1.8
        n_dx = -n_len * math.sin(theta_rad)
        n_dy = n_len * math.cos(theta_rad)
        ax.annotate('', xy=(car_center_x + n_dx, car_center_y + n_dy + 0.4), xytext=(car_center_x, car_center_y+0.4),
                    arrowprops=dict(arrowstyle='->', lw=2, color='green'))
        ax.text(car_center_x + n_dx - 0.3, car_center_y + n_dy + 0.5, f"$N$", fontsize=12, color='green')

        ax.text(5, 7.5, f"Radius ($r$) = {self.radius} m", fontsize=11, ha='center', fontweight='bold')
        ax.text(5, 0.5, "Banked Curve Cross-Section", fontsize=10, ha='center', style='italic')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0)
        plt.close()

class Phy127:
    """
    Calculates the orbital radius given the gravitational force and masses of two bodies.
    Standard A-Level problem using Newton's Law of Gravitation.
    """
    def __init__(self):
        self.G = 6.67430e-11
        self.mass_sun = rnd.uniform(1.98, 2.02) * 1e30 
        self.mass_earth = rnd.uniform(5.97, 5.99) * 1e24 
        self.force = rnd.uniform(3.4, 3.6) * 1e22
        self.r_val = math.sqrt((self.G * self.mass_sun * self.mass_earth) / self.force)
        self.answer = f"{self.r_val:.2e}"
        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational force between point masses"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.description = (
            f"The gravitational force of attraction between a planet and its sun is {self.force:.2e} N. "
            f"Calculate the distance between the centres of the planet and the sun.\n\n"
            f"Mass of planet = {self.mass_earth:.2e} kg\n"
            f"Mass of star = {self.mass_sun:.2e} kg"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ given\ quantities} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M_1 = {self.mass_sun:.2e}\\,\\text{{kg}},\ M_2 = {self.mass_earth:.2e}\\,\\text{{kg}} \\\\"
            f"&F = {self.force:.2e}\\,\\text{{N}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Newton's\ Law\ of\ Gravitation} \\\\"
            "&F = \\frac{G M_1 M_2}{r^2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ distance\ (r)} \\\\"
            "&r = \\sqrt{\\frac{G M_1 M_2}{F}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ solve} \\\\"
            f"&r = \\sqrt{{\\frac{{(6.67 \\times 10^{{-11}})({self.mass_sun:.2e})({self.mass_earth:.2e})}}{{{self.force:.2e}}}}} \\\\"
            f"&r = \\mathbf{{{self.answer}\\,\\text{{m}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_orbit_vis = 1.8
        sun_radius = 0.3
        earth_radius = 0.12

        sun = plt.Circle((0, 0), sun_radius, color='none', ec='black', lw=2)
        ax.add_patch(sun)
        ax.text(0, 0, "Sun\n$M_1$", ha='center', va='center', fontweight='bold', fontsize=10)
        
        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=0.8, alpha=0.3, fill=False)
        ax.add_patch(orbit)

        ax.plot(r_orbit_vis, 0, 'ko', markersize=10)
        ax.text(r_orbit_vis, 0.2, "Planet\n$M_2$", ha='center', fontweight='bold', fontsize=9)

        ax.annotate('', xy=(r_orbit_vis, -0.5), xytext=(0, -0.5),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1.2))
        ax.text(r_orbit_vis/2, -0.7, "$r = ?$", ha='center', fontsize=12, fontweight='bold')
        
        ax.plot([0, 0], [0, -0.6], 'k:', lw=1)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.6], 'k:', lw=1)

        ax.annotate('', xy=(r_orbit_vis - 0.7, 0), xytext=(r_orbit_vis, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=2, mutation_scale=15))
        ax.text(r_orbit_vis - 0.35, 0.15, f"$F = {self.force:.2e}$ N", 
                ha='center', fontsize=10, fontweight='bold')

        data_text = (
            f"Sun mass: ${self.mass_sun:.2e}$ kg\n"
            f"Planet mass: ${self.mass_earth:.2e}$ kg\n"
            f"$G: 6.67 \times 10^{{-11}}$ N m$^2$ kg$^{-2}$"
        )
        ax.text(-0.5, 1.3, data_text, fontsize=9, verticalalignment='top',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8'))
        ax.set_xlim(-0.8, r_orbit_vis + 0.6)
        ax.set_ylim(-1.0, 1.6)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy128:
    """
    Calculates the mass of a planet given the gravitational force acting on a satellite,
    its mass, and its altitude above the surface.
    Formula: M = (F * r^2) / (G * m)
    """
    def __init__(self):
        self.G = 6.67430e-11 
        self.mass_sat = rnd.randint(50, 80) * 100        # 5000 - 8000 kg
        self.altitude_km = rnd.randint(15, 25) * 100     # 1500 - 2500 km
        self.radius_planet_km = 6400                     # Earth radius
        self.force_kn = rnd.uniform(30.0, 45.0)          # 30 - 45 kN

        self.r_surface = self.radius_planet_km * 1e3
        self.h = self.altitude_km * 1e3
        self.r_total = self.r_surface + self.h
        self.F = self.force_kn * 1e3
        self.m = self.mass_sat
        mass_earth_val = (self.F * (self.r_total**2)) / (self.G * self.m)

        self.answer = f"{mass_earth_val:.2e}"
        self.topic = "Gravitational Fields"
        self.subtopic = "Newton's Law of Gravitation"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            f"A satellite of mass {self.m:,} kg is in a circular orbit at an altitude of "
            f"{self.altitude_km:,} km above the surface of a planet. The gravitational force "
            f"exerted by the planet on the satellite is {self.force_kn:.1f} kN. "
            f"Given that the radius of the planet is {self.radius_planet_km:,} km, "
            f"calculate the mass of the planet."
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ units\ to\ SI} \\\\"
            f"&r = R + h = {self.radius_planet_km}\\,\\text{{km}} + {self.altitude_km}\\,\\text{{km}} = {self.r_total:.2e}\\,\\text{{m}} \\\\"
            f"&F = {self.force_kn:.1f}\\,\\text{{kN}} = {self.F:.2e}\\,\\text{{N}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ Newton's\ Law\ of\ Gravitation} \\\\"
            "&F = \\frac{GMm}{r^2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ to\ solve\ for\ planet\ mass\ (M)} \\\\"
            "&M = \\frac{Fr^2}{Gm} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ values} \\\\"
            f"&M = \\frac{{({self.F:.2e})({self.r_total:.2e})^2}}{{(6.67 \\times 10^{{-11}})({self.m})}} \\\\"
            f"&M = \\mathbf{{{self.answer}\\,\\text{{kg}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        r_earth_vis = 1.0
        h_vis = 0.6
        r_orbit_vis = r_earth_vis + h_vis
        limit = r_orbit_vis * 1.4

        planet = plt.Circle((0, 0), r_earth_vis, color='#f0f0f0', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        ax.text(0, 0, "PLANET\n(Mass $M$)", ha='center', va='center', fontsize=10, fontweight='bold')

        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=0.8, fill=False, alpha=0.5)
        ax.add_patch(orbit)

        ax.plot(r_orbit_vis, 0, 'ko', markersize=6, zorder=5)
        ax.text(r_orbit_vis, 0.15, f"Satellite\n$m = {self.m}$ kg", ha='center', fontsize=9, fontweight='bold')

        ax.annotate('', xy=(r_orbit_vis - 0.5, 0), xytext=(r_orbit_vis, 0),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5, mutation_scale=15))
        ax.text(r_orbit_vis - 0.25, 0.1, f"$F = {self.force_kn:.1f}$ kN", ha='center', fontsize=9)

        ax.annotate('', xy=(r_earth_vis, -0.2), xytext=(0, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(r_earth_vis/2, -0.35, f"$R = {self.radius_planet_km}$ km", ha='center', fontsize=9)

        ax.annotate('', xy=(r_orbit_vis, -0.2), xytext=(r_earth_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=1.2))
        ax.text((r_earth_vis + r_orbit_vis)/2, -0.35, f"$h = {self.altitude_km}$ km", 
                ha='center', color='#e67e22', fontsize=9, fontweight='bold')

        ax.annotate('', xy=(r_orbit_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=1.2))
        ax.text(r_orbit_vis/2, -1.0, "$r = R + h$", ha='center', color='#2563eb', fontsize=10, fontweight='bold')

        ax.plot([0, 0], [0, -0.85], 'k:', lw=0.8)
        ax.plot([r_earth_vis, r_earth_vis], [0, -0.25], 'k:', lw=0.8)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.85], 'k:', lw=0.8)

        ax.text(limit*0.7, limit*0.7, "Diagram not to scale", style='italic', fontsize=8, ha='right')

        ax.set_xlim(-0.5, limit)
        ax.set_ylim(-1.2, limit)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy129:
    def __init__(self):
        possible_densities = [(3, 5), (2, 3), (4, 5), (1, 2)]
        possible_g = [(1, 6), (1, 4), (1, 5), (3, 8)]
        
        d_num, d_den = rnd.choice(possible_densities)
        g_num, g_den = rnd.choice(possible_g)
        
        self.rho_m_rho_e = Fraction(d_num, d_den)
        self.g_m_g_e = Fraction(g_num, g_den)

        self.radius_ratio = self.g_m_g_e / self.rho_m_rho_e
        self.answer = f"{self.radius_ratio.numerator} : {self.radius_ratio.denominator}"

        self.description = (
            f"The mean density of the Moon is {self.rho_m_rho_e} times the mean density of the Earth. "
            f"The gravitational field strength at the surface of the Moon is {self.g_m_g_e} of "
            f"the gravitational field strength at the surface of the Earth. "
            f"Determine the ratio of the Moon’s radius $r_M$ to the Earth’s radius $r_E$."
        )

        self.topic = "Gravitational Field"
        self.subtopic = "Gravitational field strength"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Express field strength } g \\text{ in terms of density } \\rho \\\\"
            "&g = \\frac{GM}{r^2}, \\quad M = \\rho \\left(\\frac{4}{3}\\pi r^3\\right) \\\\"
            "&g = \\frac{G \\cdot \\rho \\cdot \\frac{4}{3}\\pi r^3}{r^2} = \\frac{4}{3}\\pi G \\rho r \\\\[8pt]"
            "&\\textbf{Step 2: Establish the proportionality} \\\\"
            "&g \\propto \\rho r \\implies \\frac{g_M}{g_E} = \\frac{\\rho_M}{\\rho_E} \\times \\frac{r_M}{r_E} \\\\[8pt]"
            "&\\textbf{Step 3: Substitute the given ratios} \\\\"
            f"&\\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} = \\frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}} \\times \\frac{{r_M}}{{r_E}} \\\\[8pt]"
            "&\\textbf{Step 4: Solve for } \\frac{r_M}{r_E} \\\\"
            f"&\\frac{{r_M}}{{r_E}} = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} \\div \\frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}} = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}} \\times \\frac{{{self.rho_m_rho_e.denominator}}}{{{self.rho_m_rho_e.numerator}}} \\\\"
            f"&\\frac{{r_M}}{{r_E}} = \\frac{{{self.radius_ratio.numerator}}}{{{self.radius_ratio.denominator}}} \\\\[8pt]"
            "&\\textbf{Step 5: Final Ratio} \\\\"
            f"&r_M : r_E = \\mathbf{{{self.answer}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_E = 1.2
        r_M = r_E * (float(self.radius_ratio.numerator) / float(self.radius_ratio.denominator))
        r_M_vis = max(r_M, 0.3) 

        earth = plt.Circle((0, 0), r_E, color='#2a78d0', alpha=0.7, ec='#1a4d80', lw=2)
        ax.add_artist(earth)
        ax.plot([0, r_E], [0, 0], color='black', lw=1.5)
        ax.text(r_E/2, 0.1, "$r_E$", ha='center', fontsize=12)
        ax.text(0, -r_E-0.3, "EARTH\n" + r"$\rho_E, g_E$", ha='center', weight='bold')

        moon_x = 3.0
        moon = plt.Circle((moon_x, 0), r_M_vis, color='#95a5a6', alpha=0.7, ec='#7f8c8d', lw=2)
        ax.add_artist(moon)
        ax.plot([moon_x, moon_x + r_M_vis], [0, 0], color='black', lw=1.5)
        ax.text(moon_x + r_M_vis/2, 0.1, "$r_M$", ha='center', fontsize=12)
        ax.text(moon_x, -r_E-0.3, "MOON\n" + rf"$\rho_M = \frac{{{self.rho_m_rho_e.numerator}}}{{{self.rho_m_rho_e.denominator}}}\rho_E$", ha='center', weight='bold')

        ax.text((moon_x)/2, 1.5, f"Given: $g_M = \\frac{{{self.g_m_g_e.numerator}}}{{{self.g_m_g_e.denominator}}}g_E$", 
                ha='center', fontsize=13, bbox=dict(facecolor='none', edgecolor='gray', boxstyle='round,pad=0.5'))

        ax.text((moon_x)/2, -1.8, "*Diagram not to scale", fontsize=10, style='italic', color='gray')

        ax.set_xlim(-1.5, moon_x + 1.5)
        ax.set_ylim(-2.2, 2.2)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.05)
        plt.close()

class Phy130:
    def __init__(self):
        self.G = 6.67430e-11
        self.planet_diameter_km = rnd.randint(60, 90) * 100 
        self.planet_mass = rnd.uniform(2.0, 5.0) * 1e23
        self.height_km = rnd.randint(2, 6) * 100
        self.rock_mass = rnd.randint(400, 800)

        self.planet_radius_km = self.planet_diameter_km / 2
        self.r_total_m = (self.planet_radius_km + self.height_km) * 1e3

        self.potential = - (self.G * self.planet_mass) / self.r_total_m
        self.answer = f"{self.potential:.2e}"

        self.topic = "Gravitational fields"
        self.subtopic = "Gravitational field of a point mass"
        self.source = "Original"
        self.curriculum = "A-Level"
        self.description = (
            f"A planet has a diameter of {self.planet_diameter_km} km and a mass of {self.planet_mass:.2e} kg. "
            f"A rock of mass {self.rock_mass} kg is located at a distance of {self.height_km} km "
            f"above the planet’s surface. Calculate the gravitational potential at this point."
        )
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Identify given values and convert to SI units} \\\\"
            f"&G = {self.G}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.planet_mass:.2e}\\,\\text{{kg}} \\\\"
            f"&R = \\frac{{{self.planet_diameter_km}}}{{2}} = {self.planet_radius_km}\\,\\text{{km}} \\\\"
            f"&h = {self.height_km}\\,\\text{{km}} \\\\[8pt]"
            "&\\textbf{Step 2: Calculate total distance from center } (r) \\\\"
            "&r = R + h \\\\"
            f"&r = ({self.planet_radius_km} + {self.height_km}) \\times 10^3\\,\\text{{m}} \\\\"
            f"&r = {round(self.r_total_m, 10)}\\,\\text{{m}} \\\\[8pt]"
            "&\\textbf{Step 3: Apply the gravitational potential formula} \\\\"
            "&\\phi = -\\frac{GM}{r} \\quad \\text{(Note: independent of rock mass)} \\\\"
            f"&\\phi = -\\frac{{({self.G})({self.planet_mass:.2e})}}{{{round(self.r_total_m, 10)}}} \\\\[8pt]"
            "&\\textbf{Step 4: Final calculation} \\\\"
            f"&\\phi = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )
    def generate(self, num):
        fig, ax = plt.subplots(figsize=(6, 6), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        r_planet = 1.0
        h_vis = (self.height_km / self.planet_radius_km) * r_planet
        r_total_vis = r_planet + h_vis

        planet = plt.Circle((0, 0), r_planet, color='none', ec='black', lw=2)
        ax.add_patch(planet)

        ax.plot(0, 0, 'k+', markersize=10)
        ax.plot(r_total_vis, 0, 'ko', markersize=4) 
        ax.text(r_total_vis, 0.1, "rock", ha='center', fontsize=10)

        theta_r = np.radians(135) 
        ax.plot([0, r_planet * np.cos(theta_r)], [0, r_planet * np.sin(theta_r)], 'k--', lw=1)
        ax.text(r_planet * 0.5 * np.cos(theta_r) - 0.1, r_planet * 0.5 * np.sin(theta_r) + 0.1, 
                f"$R$ = {self.planet_radius_km:.2e}", fontsize=11, ha='right')

        ax.annotate('', xy=(r_total_vis, -0.1), xytext=(r_planet, -0.1),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text((r_planet + r_total_vis)/2, -0.25, f"$h$", ha='center', fontsize=11)

        ax.annotate('', xy=(r_total_vis, -0.5), xytext=(0, -0.5),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(r_total_vis/2, -0.65, f"$r$", ha='center', fontsize=11)

        ax.plot([0, 0], [0, -0.55], 'k:', lw=0.8)
        ax.plot([r_planet, r_planet], [0, -0.15], 'k:', lw=0.8)
        ax.plot([r_total_vis, r_total_vis], [0, -0.55], 'k:', lw=0.8)

        ax.text(-1.4, 1.2, f"Mass of planet $= M$\nRadius of planet $= R$", 
                fontsize=10, bbox=dict(facecolor='none', edgecolor='black', pad=5))

        limit = r_total_vis * 1.3
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy131:
    """
    Calculates the Gravitational Potential (V) at a specific height above a planet's surface.
    Formula: V = -GM / r, where r = R + h.
    """
    def __init__(self):
        self.G = 6.67430e-11
        self.planet_diameter_km = rnd.randint(60, 85) * 100 
        self.planet_mass = rnd.uniform(3.0, 6.0) * 1e23
        self.height_km = rnd.randint(3, 7) * 100        
        self.rock_mass = rnd.randint(450, 650)

        self.planet_radius_km = self.planet_diameter_km / 2
        self.total_distance_m = (self.planet_radius_km + self.height_km) * 1e3

        potential_val = -(self.G * self.planet_mass) / self.total_distance_m
        self.answer = f"{potential_val:.2e}"

        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational Potential"
        self.source = "Save My Exam"
        self.curriculum = "A-Level"

        self.description = (
            f"A planet has a diameter of {self.planet_diameter_km} km and a mass of {self.planet_mass:.2e} kg. "
            f"A rock of mass {self.rock_mass} kg is located at a height of {self.height_km} km "
            f"above the planet's surface. Calculate the gravitational potential at the rock's position."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ given\ quantities\ and\ convert\ to\ SI\ units} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.planet_mass:.2e}\\,\\text{{kg}} \\\\"
            f"&R = \\frac{{{self.planet_diameter_km}}}{{2}} = {self.planet_radius_km}\\,\\text{{km}} = {self.planet_radius_km * 1e3:.2e}\\,\\text{{m}} \\\\"
            f"&h = {self.height_km}\\,\\text{{km}} = {self.height_km * 1e3:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ the\ total\ distance\ from\ the\ centre\ (r)} \\\\"
            "&r = R + h \\\\"
            f"&r = {self.planet_radius_km * 1e3:.2e} + {self.height_km * 1e3:.2e} = {self.total_distance_m:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ the\ gravitational\ potential\ formula} \\\\"
            "&V = -\\frac{GM}{r} \\\\"
            f"&V = -\\frac{{(6.67 \\times 10^{{-11}})({self.planet_mass:.2e})}}{{{self.total_distance_m:.2e}}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Result} \\\\"
            f"&V = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        r_planet_vis = 1.0
        h_vis = 0.6
        r_orbit_vis = r_planet_vis + h_vis
        limit = r_orbit_vis * 1.3 

        # Draw Planet
        planet = plt.Circle((0, 0), r_planet_vis, color='#f0f0f0', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        ax.text(0, 0, "PLANET\n$M = " + f"{self.planet_mass:.1e}" + "$ kg", ha='center', va='center', fontsize=9, fontweight='bold')

        # Draw Orbit Path
        orbit = plt.Circle((0, 0), r_orbit_vis, color='black', ls='--', lw=0.8, fill=False, alpha=0.5)
        ax.add_patch(orbit)

        # Rock Position
        ax.plot(r_orbit_vis, 0, 'ko', markersize=6, zorder=5)
        ax.text(r_orbit_vis, 0.15, f"Rock\n$m = {self.rock_mass}$ kg", ha='center', fontsize=9, fontweight='bold')

        # Dimension Lines
        ax.annotate('', xy=(r_planet_vis, -0.2), xytext=(0, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(r_planet_vis/2, -0.35, f"$R = {self.planet_radius_km:g}$ km", ha='center', fontsize=9)

        # Height (h)
        ax.annotate('', xy=(r_orbit_vis, -0.2), xytext=(r_planet_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=1.2))
        ax.text((r_planet_vis + r_orbit_vis)/2, -0.35, f"$h = {self.height_km:g}$ km", 
                ha='center', color='#e67e22', fontsize=9, fontweight='bold')

        # Total Distance (r)
        ax.annotate('', xy=(r_orbit_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=1.2))
        ax.text(r_orbit_vis/2, -1.0, "$r = R + h$", ha='center', color='#2563eb', fontsize=10, fontweight='bold')

        # Extension Lines
        ax.plot([0, 0], [0, -0.85], 'k:', lw=0.8)
        ax.plot([r_planet_vis, r_planet_vis], [0, -0.25], 'k:', lw=0.8)
        ax.plot([r_orbit_vis, r_orbit_vis], [0, -0.85], 'k:', lw=0.8)

        # Metadata Box
        info_text = f"$G = 6.67 \\times 10^{{-11}}$ N m$^2$ kg$^{-2}$"
        ax.text(-limit*0.4, limit*0.9, info_text, fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.set_xlim(-limit*0.5, limit)
        ax.set_ylim(-1.2, limit)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy132:
    """
    Calculates the change in gravitational potential (delta V) when an object 
    moves from the surface of a planet to a specific altitude.
    Formula: delta V = V2 - V1 = -GM(1/r2 - 1/r1)
    """
    def __init__(self):
    
        self.G = 6.67430e-11 
        # Radius: 6000km to 7000km
        self.radius_km = rnd.randint(60, 70) * 100 
        # Mass: 5.0e24 to 6.5e24 kg
        self.mass_earth = rnd.uniform(5.0, 6.5) * 1e24
        # Altitude: 10,000km to 25,000km
        self.altitude_km = rnd.randint(10, 25) * 1000

        # Derived Values (SI Units)
        self.r1 = self.radius_km * 1e3
        self.r2 = (self.radius_km + self.altitude_km) * 1e3

        # Calculation
        self.delta_V = -self.G * self.mass_earth * (1/self.r2 - 1/self.r1)
        self.answer = f"{self.delta_V:.2e}"

        # 5. Metadata
        self.topic = "Gravitational Fields"
        self.subtopic = "Gravitational Potential Change"
        self.source = "Original / A-Level Physics"
        self.curriculum = "Cambridge A-Level"

        # 6. Structured Description
        self.description = (
            f"A planet is modeled as an isolated sphere of radius {self.radius_km:,} km "
            f"with a mass of {self.mass_earth:.2e} kg concentrated at its centre. "
            f"An object is projected vertically from the surface of the planet "
            f"until it reaches an altitude of {self.altitude_km:,} km.\n\n"
            "Calculate the change in gravitational potential for this movement."
        )

        # 7. Enhanced Step-by-Step Reasoning
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\textbf{Step 1: Convert all units to SI (meters)} \\\\"
            f"&r_1 = R = {self.radius_km:,}\\,\\text{{km}} = {self.r1:.2e}\\,\\text{{m}} \\\\"
            f"&r_2 = R + h = ({self.radius_km:,} + {self.altitude_km:,})\\,\\text{{km}} = {self.r2:.2e}\\,\\text{{m}} \\\\[8pt]"
            "&\\textbf{Step 2: State the formula for change in potential } (\\Delta V) \\\\"
            "&\\Delta V = V_2 - V_1 = \\left(-\\frac{GM}{r_2}\\right) - \\left(-\\frac{GM}{r_1}\\right) \\\\"
            "&\\Delta V = GM \\left( \\frac{1}{r_1} - \\frac{1}{r_2} \\right) \\\\[8pt]"
            "&\\textbf{Step 3: Substitute known values} \\\\"
            f"&G = 6.67 \\times 10^{{-11}}\\,\\text{{N m}}^2\\,\\text{{kg}}^{{-2}} \\\\"
            f"&M = {self.mass_earth:.2e}\\,\\text{{kg}} \\\\"
            f"&\\Delta V = (6.67 \\times 10^{{-11}})({self.mass_earth:.2e}) \\left( \\frac{1}{{{self.r1:.2e}}} - \\frac{1}{{{self.r2:.2e}}} \\right) \\\\[8pt]"
            "&\\textbf{Step 4: Final calculation} \\\\"
            f"&\\Delta V = \\mathbf{{{self.answer}\\,\\text{{J kg}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")
        R_val = self.radius_km
        h_val = self.altitude_km
        total_r_val = R_val + h_val
        
        R_vis = 1.0
        h_vis = 1.2 
        total_r_vis = R_vis + h_vis

        # Planet
        planet = plt.Circle((0, 0), R_vis, color='none', ec='black', lw=2, zorder=2)
        ax.add_patch(planet)
        
        # Centre of Planet
        ax.plot(0, 0, 'k+', markersize=10)
        ax.text(0.1, -0.1, "centre of\nplanet", fontsize=9, va='top')

        # Orbit
        orbit = plt.Circle((0, 0), total_r_vis, color='black', ls='--', lw=0.8, fill=False, alpha=0.5)
        ax.add_patch(orbit)

        ax.plot(R_vis, 0, 'ro', markersize=6, label='Surface', zorder=5)
        ax.text(R_vis, 0.15, "Surface", ha='center', color='red', fontsize=9)
        
        ax.plot(total_r_vis, 0, 'bo', markersize=6, label='Altitude', zorder=5)
        ax.text(total_r_vis, 0.15, "Final\nPosition", ha='center', color='blue', fontsize=9)

        ax.annotate('', xy=(R_vis * np.cos(np.radians(135)), R_vis * np.sin(np.radians(135))), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(-0.4, 0.4, f"$R = {R_val:,}$ km", ha='right', fontsize=10)

        ax.annotate('', xy=(total_r_vis, -0.2), xytext=(R_vis, -0.2),
                    arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=1.5))
        ax.text((R_vis + total_r_vis)/2, -0.4, f"$h = {h_val:,}$ km", 
                ha='center', color='#e67e22', fontweight='bold', fontsize=10)
        ax.annotate('', xy=(total_r_vis, -0.8), xytext=(0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='black', lw=1))
        ax.text(total_r_vis/2, -1.0, f"$r_2 = {total_r_val:,}$ km", ha='center', fontsize=10)

        ax.plot([0, 0], [0, -0.9], 'k:', lw=0.8)
        ax.plot([R_vis, R_vis], [0, -0.3], 'k:', lw=0.8)
        ax.plot([total_r_vis, total_r_vis], [0, -0.9], 'k:', lw=0.8)
        limit = total_r_vis * 1.3
        
        ax.text(-limit*0.8, limit*0.8, f"Mass of planet, $M = {self.mass_earth:.2e}$ kg", 
                fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        limit = total_r_vis * 1.3
        ax.set_xlim(-limit*0.5, limit)
        ax.set_ylim(-1.5, 1.5)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()


class Phy133:
    def __init__(self):
        self.mass_g = rnd.choice([4, 8, 12, 16]) 
        self.temperature_c = rnd.choice([20, 50, 100, 200]) 
        self.volume_l = rnd.randint(2, 10)
        
        self.molar_mass_he = 4.003e-3  # kg/mol
        self.R = 8.314
        self.N_A = 6.022e23
        self.k_B = 1.381e-23
        self.m_atom_he = self.molar_mass_he / self.N_A

        self.temperature_k = self.temperature_c + 273.15
        
        # Mean square speed: <c^2> = 3kT / m
        self.c_rms = math.sqrt((3 * self.k_B * self.temperature_k) / self.m_atom_he)
        self.answer = f"{self.c_rms:.1f}"

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic Theory of Gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            f"A rigid vessel contains {self.mass_g} g of Helium-4 gas at a constant temperature of "
            f"{self.temperature_c}\u00b0C. Assuming Helium behaves as an ideal gas, calculate the "
            f"root-mean-square (r.m.s.) speed of the helium atoms."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Conversion\ to\ SI\ Units} \\\\"
            f"&T = {self.temperature_c} + 273.15 = {self.temperature_k:.2f}\\,\\text{{K}} \\\\"
            f"&m_{{atom}} = \\frac{{M_{{molar}}}}{{N_A}} = \\frac{{4.003 \\times 10^{{-3}}}}{{6.022 \\times 10^{{23}}}} = {self.m_atom_he:.3e}\\,\\text{{kg}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Kinetic\ Theory\ Formula} \\\\"
            "&\\frac{1}{2} m \\langle c^2 \\rangle = \\frac{3}{2} k_B T \\implies c_{rms} = \\sqrt{\\frac{3 k_B T}{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculation} \\\\"
            f"&c_{{rms}} = \\sqrt{{\\frac{{3(1.38 \\times 10^{{-23}})({self.temperature_k:.2f})}}{{{self.m_atom_he:.3e}}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Result} \\\\"
            f"&c_{{rms}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(7, 7), dpi=300)
        ax.set_aspect("equal")
        ax.axis("off")

        # Cylinder Tank
        tank = patches.FancyBboxPatch((0.3, 0.2), 0.4, 0.6, boxstyle="round,pad=0.02", 
                                      fc='none', ec='black', lw=2)
        ax.add_patch(tank)
        
        # Gas particles with velocity vectors
        for _ in range(15):
            px = rnd.uniform(0.35, 0.65)
            py = rnd.uniform(0.25, 0.75)
            ax.plot(px, py, 'o', color='black', markersize=4)
            # Velocity arrows
            dx, dy = rnd.uniform(-0.05, 0.05), rnd.uniform(-0.05, 0.05)
            ax.arrow(px, py, dx, dy, head_width=0.01, fc='black', ec='black', alpha=0.6)
            
        ax.text(0.5, 0.85, "Helium-4 Gas", ha='center', fontsize=12, fontweight='bold')
        
        # Spatial labels
        ax.text(0.75, 0.5, f"$T = {self.temperature_c}^\circ$C", va='center', fontsize=11)
        ax.text(0.25, 0.5, f"$m = {self.mass_g}$ g", ha='right', va='center', fontsize=11)
        ax.text(0.5, 0.15, r"$c_{rms} = \ ?$ ", ha='center', fontsize=13, fontweight='bold', color='blue')

        # Constants Box
        info_box = (
            f"Molar mass = 4.003 g mol$^{{-1}}$\n"
            f"$N_A = 6.02 x 10^{{23}}$ mol$^{{-1}}$\n"
            f"$k_B = 1.38 x 10^{{-23}}$ J K$^{{-1}}$"
        )
        ax.text(0.03, 0.95, info_box, fontsize=9, verticalalignment='top', 
                bbox=dict(facecolor='none', edgecolor='black', linestyle='-', boxstyle='round,pad=0.5'))

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy134:
    def __init__(self):
        while True:
            self.V = rnd.uniform(2.0e-3, 8.0e-3)
            self.T1_c = rnd.randint(10, 40)
            self.delta_T = rnd.randint(15, 50)
            self.T2_c = self.T1_c + self.delta_T
            self.P1 = rnd.uniform(2.0e5, 5.0e5)

            self.T1_k = self.T1_c + 273.15
            self.T2_k = self.T2_c + 273.15

            if 280 <= self.T1_k <= 350:
                break

        self.P2 = self.P1 * self.T2_k / self.T1_k
        self.answer = f"{self.P2:.2e}"

        self.topic = "Ideal gases"
        self.subtopic = "Equation of state"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.description = (
            f"A rigid container of fixed volume {self.V:.2e} m\u00b3 contains an ideal gas at a "
            f"temperature of {self.T1_c}\u00b0C and a pressure of {self.P1:.2e} Pa. "
            f"The gas is heated until its temperature reaches {self.T2_c}\u00b0C. "
            f"Calculate the final pressure of the gas, assuming the volume remains constant."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ temperatures\ to\ Kelvin} \\\\"
            f"&T_1 = {self.T1_c} + 273.15 = {self.T1_k:.2f}\\,\\text{{K}} \\\\"
            f"&T_2 = {self.T2_c} + 273.15 = {self.T2_k:.2f}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ Gay-Lussac's\ Law\ (Constant\ Volume)} \\\\"
            "&\\frac{P_1}{T_1} = \\frac{P_2}{T_2} \\implies P_2 = P_1 \\times \\frac{T_2}{T_1} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ final\ pressure} \\\\"
            f"&P_2 = ({self.P1:.2e}) \\times \\frac{{{self.T2_k:.2f}}}{{{self.T1_k:.2f}}} \\\\"
            f"&P_2 = \\mathbf{{{self.answer}\\,\\text{{Pa}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        tank_1 = patches.Rectangle((1, 1.5), 2.5, 3, fc='#f8f9fa', ec='black', lw=2)
        ax.add_patch(tank_1)
        for _ in range(20):
            ax.plot(rnd.uniform(1.2, 3.3), rnd.uniform(1.7, 4.3), 'o', color='black', markersize=3, alpha=0.6)
        
        ax.text(2.25, 5, "Initial State", ha='center', fontweight='bold')
        ax.text(2.25, 1.1, f"$P_1 = {self.P1:.2e}$ Pa\n$T_1 = {self.T1_c}^\circ$C", ha='center', va='top')

        ax.annotate("", xy=(6, 3), xytext=(4, 3),
                    arrowprops=dict(arrowstyle="->", lw=2, color='#e67e22'))
        ax.text(5, 3.3, "HEATING\n($V = const$)", ha='center', color='#e67e22', fontweight='bold', fontsize=9)

        tank_2 = patches.Rectangle((6.5, 1.5), 2.5, 3, fc='#fff5f0', ec='black', lw=2)
        ax.add_patch(tank_2)
        for _ in range(20):
            px, py = rnd.uniform(6.7, 8.8), rnd.uniform(1.7, 4.3)
            ax.plot(px, py, 'o', color='black', markersize=3, alpha=0.6)
            ax.arrow(px, py, rnd.uniform(-0.1, 0.1), rnd.uniform(-0.1, 0.1), head_width=0.03, alpha=0.4)

        ax.text(7.75, 5, "Final State", ha='center', fontweight='bold')
        ax.text(7.75, 1.1, f"$P_2 = ?$\n$T_2 = {self.T2_c}^\circ$C", ha='center', va='top')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy135:
    def __init__(self):
        while True:
            self.p1 = rnd.uniform(2.0e5, 5.0e5)
            self.v1 = rnd.uniform(1.0e-3, 3.0e-3)
            self.p2 = rnd.uniform(1.0e5, 3.0e5)
            self.v2 = rnd.uniform(4.0e-3, 6.0e-3)
            
            self.v_total = self.v1 + self.v2
            self.p_final = (self.p1 * self.v1 + self.p2 * self.v2) / self.v_total
            self.answer = f"{self.p_final:.2e}"

            if self.p_final > 0:
                break

        self.topic = "Thermal physics"
        self.subtopic = "Ideal gas - Dalton's Law"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "The diagram shows two rigid cylinders, A and B, connected by a tube of "
            "negligible volume with a closed valve. Cylinder A contains gas at "
            f"pressure P_A = {self.p1:.2e} Pa and volume V_A = {self.v1:.2e} m\u00b3. "
            f"Cylinder B contains gas at pressure P_B = {self.p2:.2e} Pa and volume V_B = {self.v2:.2e} m\u00b3. "
            "Calculate the final pressure of the system after the valve is opened and "
            "equilibrium is reached at a constant temperature."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Extract\ Data\ from\ Diagram} \\\\"
            f"&\\text{{Cylinder A: }} P_A = {self.p1:.2e}\\,\\text{{Pa}}, \\ V_A = {self.v1:.2e}\\,\\text{{m}}^3 \\\\"
            f"&\\text{{Cylinder B: }} P_B = {self.p2:.2e}\\,\\text{{Pa}}, \\ V_B = {self.v2:.2e}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ Governing\ Principle} \\\\"
            "&\\text{{At constant temperature, the total }} PV \\text{{ product is conserved:}} \\\\"
            "&P_{1}V_{1} + P_{2}V_{2} = P_{f}V_{f} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Total\ Volume} \\\\"
            f"&V_{{total}} = V_A + V_B = {self.v1:.2e} + {self.v2:.2e} = {self.v_total:.2e}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ Solve\ for\ } P_{{final}} \\\\"
            "&P_{{final}} = \\frac{{P_A V_A + P_B V_B}}{{V_{{total}}}} \\\\"
            f"&P_{{final}} = \\frac{{({self.p1:.2e} \\times {self.v1:.2e}) + ({self.p2:.2e} \\times {self.v2:.2e})}}{{{self.v_total:.2e}}} \\\\"
            f"&P_{{final}} = \\mathbf{{{self.answer}\\,\\text{{Pa}}}}"
            "\\end{aligned}\\]"
        )

    def draw_cylinder(self, ax, x_center, width, height, color_base):
        x_left = x_center - width/2
        rect = patches.Rectangle((x_left, 1.5), width, height, fc=color_base, ec='black', lw=1.5, zorder=2)
        ax.add_patch(rect)
        top = patches.Ellipse((x_center, 1.5 + height), width, width*0.2, fc=color_base, ec='black', lw=1.5, zorder=3)
        bottom = patches.Ellipse((x_center, 1.5), width, width*0.2, fc=color_base, ec='black', lw=1.5, zorder=1)
        ax.add_patch(top)
        ax.add_patch(bottom)
        light_effect = patches.Rectangle((x_center - width/4, 1.5), width/6, height, fc='white', alpha=0.3, zorder=2)
        ax.add_patch(light_effect)
        gauge_stem = patches.Rectangle((x_center - 0.05, 1.5 + height + 0.05), 0.1, 0.2, fc='gray', ec='black', zorder=1)
        ax.add_patch(gauge_stem)
        gauge_circle = plt.Circle((x_center, 1.5 + height + 0.4), 0.25, fc='white', ec='black', lw=1.5, zorder=4)
        ax.add_patch(gauge_circle)
        ax.text(x_center, 1.5 + height + 0.4, "P", ha='center', va='center', fontweight='bold', fontsize=10, zorder=5)

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.axis("off")

        self.draw_cylinder(ax, 2.5, 1.8, 3.0, '#add8e6')
        ax.text(2.5, 3, f"A\n$V_A = {self.v1:.2e}$ m$^3$\n$P_A = {self.p1:.2e}$ Pa", ha='center', fontsize=9)

        self.draw_cylinder(ax, 7.5, 2.2, 3.5, '#98fb98')
        ax.text(7.5, 3, f"B\n$V_B = {self.v2:.2e}$ m$^3$\n$P_B = {self.p2:.2e}$ Pa", ha='center', fontsize=9)

        ax.add_patch(patches.Rectangle((3.4, 2.9), 1.3, 0.3, fc='gray', ec='black', zorder=1))
        ax.add_patch(patches.Rectangle((5.3, 2.9), 1.1, 0.3, fc='gray', ec='black', zorder=1))
        valve_body = plt.Circle((5, 3.05), 0.35, fc='red', ec='black', lw=1.5, zorder=5)
        ax.add_patch(valve_body)
        ax.plot([4.7, 5.3], [3.5, 3.5], color='black', lw=4, zorder=6) 
        ax.text(5, 2.4, "Valve (Closed)", ha='center', fontweight='bold', color='red', fontsize=8)

        ax.text(5, 6.2, "Gas Mixing Equilibrium", ha='center', fontsize=14, fontweight='bold')
        ax.text(5, 5.6, r" $P_{final}$ = ?", ha='center', 
                style='italic', bbox=dict(facecolor='yellow', alpha=0.2, boxstyle='round'))

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy136:
    def __init__(self):
        while True:
            self.density = rnd.uniform(1.5, 5.0)
            self.pressure = rnd.uniform(2.0e5, 8.0e5)
            self.temperature = rnd.randint(300, 600)

            if self.density > 0 and self.pressure > 0:
                break

        self.v_rms = math.sqrt((3 * self.pressure) / self.density)
        self.answer = f"{self.v_rms:.2f}"

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            f"A sample of an ideal gas is maintained at a pressure of {self.pressure:.2e} Pa "
            f"and a temperature of {self.temperature} K. The density of the gas under these "
            f"conditions is {self.density:.2f} kg m\u207b\u00b3. Calculate the root-mean-square "
            f"(r.m.s.) speed of the gas atoms."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ the\ given\ parameters} \\\\"
            f"&P = {self.pressure:.2e}\\,\\text{{Pa}} \\\\"
            f"&\\rho = {self.density:.2f}\\,\\text{{kg m}}^{{-3}} \\\\"
            f"&T = {self.temperature}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ kinetic\ theory\ pressure\ equation} \\\\"
            "&P = \\frac{1}{3} \\rho \\langle c^2 \\rangle \\quad \\text{where } \\sqrt{\\langle c^2 \\rangle} = c_{rms} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ r.m.s.\ speed\ (} c_{rms} \\mathbf{)} \\\\"
            "&c_{rms} = \\sqrt{\\frac{3P}{\\rho}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ values\ and\ calculate} \\\\"
            f"&c_{{rms}} = \\sqrt{{\\frac{{3 \\times {self.pressure:.2e}}}{{{self.density:.2f}}}}} \\\\"
            f"&c_{{rms}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis("off")

        tank_width = 4
        tank_height = 5
        x_start = 3
        y_start = 1.5

        rect = patches.Rectangle((x_start, y_start), tank_width, tank_height, fc='#f8f9fa', ec='black', lw=2, zorder=1)
        ax.add_patch(rect)
        
        top_ellipse = patches.Ellipse((x_start + tank_width/2, y_start + tank_height), tank_width, 0.8, fc='#f8f9fa', ec='black', lw=2, zorder=2)
        ax.add_patch(top_ellipse)
        
        bottom_ellipse = patches.Ellipse((x_start + tank_width/2, y_start), tank_width, 0.8, fc='#f8f9fa', ec='black', lw=2, zorder=0)
        ax.add_patch(bottom_ellipse)

        for _ in range(25):
            px = rnd.uniform(x_start + 0.3, x_start + tank_width - 0.3)
            py = rnd.uniform(y_start + 0.3, y_start + tank_height - 0.3)
            ax.plot(px, py, 'o', color='black', markersize=3, alpha=0.7)
            
            angle = rnd.uniform(0, 2 * math.pi)
            length = rnd.uniform(0.2, 0.5)
            ax.arrow(px, py, length * math.cos(angle), length * math.sin(angle), 
                     head_width=0.08, fc='black', ec='black', alpha=0.4)

        ax.text(x_start + tank_width/2, y_start + tank_height + 1.0, "Ideal Gas in Rigid Container", 
                ha='center', fontsize=12, fontweight='bold')

        info_box = (
            f"Pressure ($P$) = {self.pressure:.2e} Pa\n"
            f"Density ($\\rho$) = {self.density:.2f} kg m$^{{-3}}$\n"
            f"Temperature ($T$) = {self.temperature} K"
        )
        ax.text(x_start + tank_width + 0.5, y_start + tank_height/2, info_box, 
                va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.text(x_start - 0.5, y_start + tank_height/2, r"$c_{rms} = ?$", 
                ha='right', va='center', fontsize=14, fontweight='bold', color='#c0392b')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy137:
    def __init__(self):
        while True:
            self.v1 = rnd.randint(400, 1200)
            self.T1_c = rnd.randint(10, 50)
            self.delta_T = rnd.randint(100, 300)
            self.T2_c = self.T1_c + self.delta_T

            self.T1_k = self.T1_c + 273.15
            self.T2_k = self.T2_c + 273.15

            if self.T2_k > self.T1_k:
                break

        self.v2 = self.v1 * math.sqrt(self.T2_k / self.T1_k)
        self.answer = f"{self.v2:.2f}"
        
        t1_val = f"{self.T1_k:.2f}"
        t2_val = f"{self.T2_k:.2f}"

        self.topic = "Thermal physics"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            f"Helium, behaving as an ideal gas, has molecules with a root-mean-square (r.m.s.) speed "
            f"of {self.v1} m s\u207b\u00b9 at a temperature of {self.T1_c}\u00b0C. "
            f"Calculate the r.m.s. speed of the molecules when the gas is heated to {self.T2_c}\u00b0C."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ temperatures\ to\ Kelvin} \\\\"
            f"&T_1 = {self.T1_c} + 273.15 = {t1_val}\\,\\text{{K}} \\\\"
            f"&T_2 = {self.T2_c} + 273.15 = {t2_val}\\,\\text{{K}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ proportional\ relationship} \\\\"
            "&c_{rms} = \\sqrt{\\frac{3kT}{m}} \\implies c_{rms} \\propto \\sqrt{T} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Set\ up\ the\ ratio\ equation} \\\\"
            "&\\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} \\implies v_2 = v_1 \\sqrt{\\frac{T_2}{T_1}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ and\ calculate} \\\\"
            f"&v_2 = {self.v1} \\times \\sqrt{{\\frac{{{t2_val}}}{{{t1_val}}}}} \\\\"
            f"&v_2 = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        def draw_state(x_offset, temp_c, v_rms, label, color):
            rect = patches.FancyBboxPatch((x_offset, 2), 2.5, 2.5, boxstyle="round,pad=0.1", fc='#fdfdfd', ec='black', lw=1.5)
            ax.add_patch(rect)
            ax.text(x_offset + 1.25, 5.0, label, ha='center', fontweight='bold', fontsize=12)
            
            for _ in range(12):
                px = rnd.uniform(x_offset + 0.3, x_offset + 2.2)
                py = rnd.uniform(2.3, 4.2)
                ax.plot(px, py, 'o', color='black', markersize=3, alpha=0.6)
                scale = 0.3 if label == "Initial State" else 0.5
                ax.arrow(px, py, rnd.uniform(-scale, scale), rnd.uniform(-scale, scale), 
                         head_width=0.03, color=color, alpha=0.7)

            v_display = f"{v_rms}" if isinstance(v_rms, int) else "v_2"
            info = f"$T = {temp_c}^\circ$C\n$v_{{rms}} = {v_display}$ m/s"
            ax.text(x_offset + 1.25, 1.8, info, ha='center', va='top', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

        draw_state(1, self.T1_c, self.v1, "Initial State", "blue")
        draw_state(6.5, self.T2_c, "v2", "Final State", "red")

        ax.annotate("", xy=(6, 3.25), xytext=(4, 3.25),
                    arrowprops=dict(arrowstyle="->", lw=2, color='orange'))
        ax.text(5, 3.5, "HEATING", ha='center', fontweight='bold', color='orange')

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
        plt.close()

class Phy138:
    def __init__(self):
        while True:
            self.t_low = rnd.randint(300, 500)
            self.t_high = self.t_low + rnd.randint(400, 700)
            self.m_mass_g = 32.0  # Oxygen in g/mol
            self.m_mass_kg = self.m_mass_g / 1000  # kg/mol
            self.R = 8.31
            
            self.vp_low = np.sqrt(2 * self.R * self.t_low / self.m_mass_kg)
            self.vp_high = np.sqrt(2 * self.R * self.t_high / self.m_mass_kg)
            
            self.answer = f"{self.vp_high:.0f}"
            
            if self.vp_high > 500:
                break

        self.topic = "Ideal Gases"
        self.subtopic = "Kinetic theory of gases"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            "The provided graph illustrates the distribution of molecular speeds for oxygen gas at two different temperatures. "
            f"Curve A corresponds to T1 = {self.t_low} K. Curve B corresponds to a higher temperature T2 = {self.t_high} K. "
            "Identify the characteristics of the distribution and calculate the most probable speed (v_p) for the gas at T2."
        )

        # Pre-formatting strings to avoid backslash issues in f-strings
        t2_val = f"{self.t_high}"
        m_val = f"{self.m_mass_kg:.3f}"
        
        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Information\ from\ Graph\ and\ Text} \\\\"
            f"&\\text{{Initial Temperature (}} T_1 \\text{{): }} {self.t_low}\\,\\text{{K}} \\\\"
            f"&\\text{{Target Temperature (}} T_2 \\text{{): }} {t2_val}\\,\\text{{K}} \\\\"
            f"&\\text{{Molar Mass of Oxygen (}} M \\text{{): }} {self.m_mass_g}\\,\\text{{g mol}}^{{-1}} = {m_val}\\,\\text{{kg mol}}^{{-1}} \\\\"
            "&\\text{{Gas Constant (}} R \\text{{): }} 8.31\\,\\text{{J mol}}^{{-1}}\\,\\text{{K}}^{{-1}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Qualitative\ Analysis\ of\ the\ Curves} \\\\"
            "&\\text{{Curve B is broader and its peak is shifted to the right compared to Curve A.}} \\\\"
            "&\\text{{This confirms Curve B represents the higher temperature, }} T_2. \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Apply\ Formula\ for\ Most\ Probable\ Speed\ (} v_p \\mathbf{)} \\\\"
            "&v_p = \\sqrt{\\frac{2RT}{M}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitution\ and\ Calculation\ for\ } T_2 \\\\"
            f"&v_p = \\sqrt{{\\frac{{2 \\times 8.31 \\times {t2_val}}}{{{m_val}}}}} \\\\"
            f"&v_p = \\sqrt{{{2 * 8.31 * self.t_high / self.m_mass_kg:.2f}}} \\\\"
            f"&v_p \\approx \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        v = np.linspace(0, 2500, 500)
        
        def maxwell_boltzmann(v, T, M):
            return (M / (2 * np.pi * 8.31 * T))**1.5 * 4 * np.pi * v**2 * np.exp(-M * v**2 / (2 * 8.31 * T))

        f_low = maxwell_boltzmann(v, self.t_low, self.m_mass_kg)
        f_high = maxwell_boltzmann(v, self.t_high, self.m_mass_kg)

        ax.plot(v, f_low, color='#1f77b4', lw=2.5, label=f'Curve A ($T_1 = {self.t_low}$ K)')
        ax.plot(v, f_high, color='#d62728', lw=2.5, label=f'Curve B ($T_2 = {self.t_high}$ K)')

        ax.set_xlabel('Molecular Speed $v$ / m s$^{-1}$', fontsize=11)
        ax.set_ylabel('Relative Probability $f(v)$', fontsize=11)
        ax.set_title('Maxwell-Boltzmann Speed Distribution', fontweight='bold', fontsize=13)
        
        ax.legend(frameon=True, loc='upper right')
        ax.grid(True, linestyle=':', alpha=0.7)
        
        ax.set_xlim(0, 1800)
        ax.set_ylim(0, max(f_low) * 1.15)
        
        # Mark peak for T2
        ax.vlines(self.vp_high, 0, max(f_high), colors='gray', linestyles='dashed', alpha=0.5)
        ax.text(self.vp_high, max(f_high)*1.02, '$v_p$', ha='center', fontweight='bold', color='#d62728')

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300)
        plt.close()

class Phy139:
    def __init__(self):
        while True:
            # Menggunakan nilai yang menghasilkan perbedaan signifikan untuk arah kerja
            self.delta_U_kJ = rnd.randint(30, 80)  # Kenaikan energi internal
            self.Q_kJ = rnd.randint(10, 60)        # Panas yang masuk
            
            # W = Q - deltaU
            self.W_kJ = self.Q_kJ - self.delta_U_kJ
            self.answer = f"{abs(self.W_kJ):.1f}"
            self.work_direction = "on the gas" if self.W_kJ < 0 else "by the gas"

            if self.Q_kJ != self.delta_U_kJ:
                break

        self.topic = "Thermal physics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            f"A monatomic gas is contained within a flexible balloon. The gas undergoes a process where "
            f"its internal energy increases by {self.delta_U_kJ} kJ while {self.Q_kJ} kJ of thermal energy "
            f"is transferred into the gas. Calculate the magnitude of the work done and determine "
            f"whether the work is done by the gas or on the gas."
        )

        # Pre-formatting for LaTeX
        du_val = f"{self.delta_U_kJ}"
        q_val = f"{self.Q_kJ}"
        w_val = f"{self.W_kJ}"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters\ (Sign\ Convention)} \\\\"
            f"&\\text{{Heat supplied to the gas (}} Q \\text{{): }} +{q_val}\\,\\text{{kJ}} \\\\"
            f"&\\text{{Change in internal energy (}} \\Delta U \\text{{): }} +{du_val}\\,\\text{{kJ}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ First\ Law\ of\ Thermodynamics} \\\\"
            "&\\Delta U = Q - W \\quad \\text{{(where }} W \\text{{ is work done by the gas)}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Work\ Done\ (} W \\mathbf{)} \\\\"
            f"&W = Q - \\Delta U \\\\"
            f"&W = {q_val} - {du_val} = {w_val}\\,\\text{{kJ}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Interpret\ the\ Result} \\\\"
            f"&\\text{{Since }} W \\text{{ is negative (}}{w_val}\\,\\text{{kJ), work of }} \\mathbf{{{self.answer}\\,\\text{{kJ}}}} \\\\"
            f"&\\text{{is actually done }} \\mathbf{{{self.work_direction}}}\\text{{ (compression).}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")

        # Representasi Balon yang lebih realistis
        balloon_body = patches.Ellipse((5, 4.5), 4, 4.5, fc='#ff6666', ec='#990000', lw=2, alpha=0.7, zorder=2)
        ax.add_patch(balloon_body)
        
        # Simpul balon
        nodes = [[4.8, 2.3], [5.2, 2.3], [5, 2.6]]
        polygon = patches.Polygon(nodes, fc='#ff6666', ec='#990000', lw=1.5, zorder=1)
        ax.add_patch(polygon)

        # Panas Masuk (Q)
        ax.annotate("", xy=(3.5, 4.5), xytext=(1, 4.5),
                    arrowprops=dict(arrowstyle="->", lw=3, color='black', mutation_scale=20))
        ax.text(1.2, 4.8, f"$Q = +{self.Q_kJ}$ kJ\n(Heat In)", color='black', fontweight='bold', ha='center')

        # Kerja (W) - Ditandai dengan tanda tanya untuk memicu penalaran
        ax.annotate("", xy=(8.5, 4.5), xytext=(6.5, 4.5),
                    arrowprops=dict(arrowstyle="<-", lw=3, color='black', mutation_scale=20))
        ax.text(8.5, 4.5, "$W = ?$", color='black', fontsize=14, fontweight='bold', va='center')

        # Label Energi Internal di Tengah
        ax.text(5, 4.5, f"$\\Delta U = +{self.delta_U_kJ}$ kJ", 
                ha='center', va='center', fontweight='bold', color='white',
                bbox=dict(facecolor='black', alpha=0.3, boxstyle='round,pad=0.3'))

        ax.set_title("Thermodynamic System: Balloon", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()
        
class Phy140:
    def __init__(self):
        while True:
            self.pressure_kPa = rnd.randint(100, 400)
            self.delta_U_kJ = rnd.randint(10, 80)
            self.Q_kJ = rnd.randint(100, 200)

            if self.Q_kJ > self.delta_U_kJ:
                break

        self.pressure = self.pressure_kPa * 1000
        self.delta_U = self.delta_U_kJ * 1000
        self.Q = self.Q_kJ * 1000

        self.W = self.Q - self.delta_U
        self.delta_V = self.W / self.pressure
        self.answer = f"{abs(self.delta_V):.2f}"

        self.topic = "Thermodynamics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        p_val = f"{self.pressure}"
        du_val = f"{self.delta_U}"
        q_val = f"{self.Q}"
        w_val = f"{self.W}"

        self.description = (
            f"An ideal gas is held in a cylinder and expands at a constant pressure of {self.pressure_kPa} kPa. "
            f"The internal energy of the gas increases by {self.delta_U_kJ} kJ "
            f"while {self.Q_kJ} kJ of heat is transferred to the gas. "
            "Calculate the magnitude of the change in volume of the gas."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters\ (SI\ Units)} \\\\"
            f"&Q = +{q_val}\\,\\text{{J}} \\\\"
            f"&\\Delta U = +{du_val}\\,\\text{{J}} \\\\"
            f"&P = {p_val}\\,\\text{{Pa}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Work\ Done\ using\ First\ Law} \\\\"
            "&\\Delta U = Q - W \\implies W = Q - \\Delta U \\\\"
            f"&W = {q_val} - {du_val} = {w_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Relate\ Work\ to\ Volume\ Change} \\\\"
            "&\\text{{At constant pressure, }} W = P\\Delta V \\implies \\Delta V = \\frac{W}{P} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitution\ and\ Final\ Calculation} \\\\"
            f"&\\Delta V = \\frac{{{w_val}}}{{{p_val}}} \\\\"
            f"&\\Delta V = \\mathbf{{{self.answer}\\,\\text{{m}}^3}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        cylinder_back = patches.Rectangle((3, 1.5), 4, 6, fc='#f0f0f0', ec='black', lw=2, zorder=0)
        ax.add_patch(cylinder_back)
        
        gas_region = patches.Rectangle((3, 1.5), 4, 3.5, fc='#ffcccc', alpha=0.5, zorder=1)
        ax.add_patch(gas_region)
        
        for _ in range(20):
            ax.plot(rnd.uniform(3.2, 6.8), rnd.uniform(1.7, 4.8), 'o', color='#cc0000', markersize=3, alpha=0.6, zorder=2)

        piston = patches.Rectangle((3, 4.8), 4, 0.4, fc='gray', ec='black', lw=1.5, zorder=3)
        ax.add_patch(piston)
        piston_rod = patches.Rectangle((4.8, 5.2), 0.4, 2.5, fc='gray', ec='black', lw=1.5, zorder=3)
        ax.add_patch(piston_rod)

        ax.plot([3, 7], [3.5, 3.5], '--', color='black', alpha=0.4)
        ax.annotate("", xy=(8, 5), xytext=(8, 3.5),
                    arrowprops=dict(arrowstyle="<->", lw=2, color='blue'))
        ax.text(8.2, 4.25, "$\\Delta V$", color='blue', fontweight='bold', fontsize=12)

        ax.annotate("", xy=(3.5, 3), xytext=(1.5, 2),
                    arrowprops=dict(arrowstyle="fancy", fc="orange", ec="none", mutation_scale=20))
        ax.text(1.0, 1.5, f"$Q = +{self.Q_kJ}$ kJ", color='#e67e22', fontweight='bold', ha='center')

        ax.text(5, 3.2, f"$\\Delta U = +{self.delta_U_kJ}$ kJ", ha='center', fontweight='bold', color='white',
                bbox=dict(facecolor='black', alpha=0.4, boxstyle='round,pad=0.3'))

        ax.text(5, 9, f"Constant Pressure\n$P = {self.pressure_kPa}$ kPa", 
                ha='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', ec='black', boxstyle='round'))

        ax.set_title("GAS IN CYLINDER", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy141:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.1, 0.5)
            self.latent_heat = rnd.uniform(2.2e6, 2.3e6)
            self.pressure = rnd.uniform(1.0e5, 1.02e5)
            self.delta_volume = self.mass * rnd.uniform(1.6, 1.7)

            if self.mass > 0 and self.latent_heat > 0:
                break

        self.Q = self.mass * self.latent_heat
        self.W = self.pressure * self.delta_volume
        self.delta_U = self.Q - self.W
        self.answer = f"{self.delta_U:.2e}"

        self.topic = "Thermal physics"
        self.subtopic = "First law of thermodynamics"
        self.source = "Original"
        self.curriculum = "A-Level"

        m_str = f"{self.mass:.2f}"
        l_str = f"{self.latent_heat:.2e}"
        p_str = f"{self.pressure:.2e}"
        dv_str = f"{self.delta_volume:.2f}"
        q_val = f"{self.Q:.2e}"
        w_val = f"{self.W:.2e}"

        self.description = (
            f"A mass of {m_str} kg of liquid water at 100°C is completely converted to steam at the same temperature. "
            f"The specific latent heat of vaporisation is {l_str} J kg\u207b\u00b9. "
            f"The process occurs against a constant atmospheric pressure of {p_str} Pa, "
            f"resulting in a volume increase of {dv_str} m\u00b3. "
            f"Calculate the increase in the internal energy of the system."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Quantities} \\\\"
            f"&m = {m_str}\\,\\text{{kg}}, \\quad L = {l_str}\\,\\text{{J kg}}^{{-1}} \\\\"
            f"&P = {p_str}\\,\\text{{Pa}}, \\quad \\Delta V = {dv_str}\\,\\text{{m}}^3 \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Thermal\ Energy\ Supplied\ (} Q \\mathbf{)} \\\\"
            "&Q = mL \\\\"
            f"&Q = {m_str} \\times {l_str} = {q_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Work\ Done\ Against\ Atmosphere\ (} W \\mathbf{)} \\\\"
            "&W = P\\Delta V \\\\"
            f"&W = ({p_str}) \\times ({dv_str}) = {w_val}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Apply\ the\ First\ Law\ of\ Thermodynamics} \\\\"
            "&\\Delta U = Q - W \\\\"
            f"&\\Delta U = {q_val} - {w_val} \\\\"
            f"&\\Delta U = \\mathbf{{{self.answer}\\,\\text{{J}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        beaker = patches.Rectangle((3, 1), 4, 7, fc='none', ec='black', lw=2, zorder=3)
        ax.add_patch(beaker)

        water_level = 2.5
        water = patches.Rectangle((3, 1), 4, water_level - 1, fc='#3498db', alpha=0.5, zorder=2)
        ax.add_patch(water)

        for _ in range(15):
            bx = rnd.uniform(3.2, 6.8)
            by = rnd.uniform(1.2, water_level - 0.2)
            ax.add_patch(patches.Circle((bx, by), 0.1, color='white', alpha=0.8, zorder=3))

        for i in range(5):
            sx = 3.5 + i * 0.75
            ax.annotate("", xy=(sx, 7), xytext=(sx, 3),
                        arrowprops=dict(arrowstyle="->", color='#95a5a6', lw=1.5, alpha=0.6))

        ax.annotate("", xy=(5, 1), xytext=(5, -0.5),
                    arrowprops=dict(arrowstyle="<-", color='red', lw=3))
        ax.text(5, -0.8, f"$L = {self.latent_heat:.2e}$ J/kg", 
                color='red', fontweight='bold', ha='center')

        data_box = (
            f"Mass ($m$) = {self.mass:.2f} kg\n"
            f"Pressure ($P$) = {self.pressure:.2e} Pa\n"
            f"$\\Delta V = {self.delta_volume:.2f}$ m$^3$"
        )
        ax.text(0.5, 8.5, data_box, fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        ax.annotate("", xy=(5, 8.5), xytext=(5, 7.5),
                    arrowprops=dict(arrowstyle="->", lw=2, color='blue'))
        ax.text(5, 8.8, "Work against $P_{atm}$", color='blue', ha='center', fontweight='bold')

        ax.text(5, 9.5, "VAPORISATION", ha='center', fontsize=14, fontweight='bold')

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy142:
    def __init__(self):
        while True:
            self.length = rnd.uniform(0.8, 1.4)
            self.g = 9.81
            self.theta_degrees = rnd.randint(6, 12)
            
            self.period = 2 * math.pi * math.sqrt(self.length / self.g)
            self.omega = 2 * math.pi / self.period
            
            self.theta_rad = math.radians(self.theta_degrees)
            self.max_speed = self.omega * (self.length * self.theta_rad)
            
            if self.max_speed > 0.1:
                break

        self.answer = f"{self.max_speed:.3f}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        l_str = f"{self.length:.2f}"
        g_str = f"{self.g:.2f}"
        ang_str = f"{self.theta_degrees}"
        om_str = f"{self.omega:.3f}"
        arc_str = f"{self.length * self.theta_rad:.4f}"

        self.description = (
            f"A simple pendulum consists of a small bob attached to a string of length {l_str} m. "
            f"The pendulum is released from rest at an angle of {ang_str}\u00b0 to the vertical. "
            f"Assuming the motion is simple harmonic, calculate the maximum speed of the bob "
            f"during its oscillation. (g = {g_str} m s\u207b\u00b2)"
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Information} \\\\"
            f"&L = {l_str}\\,\\text{{m}}, \\quad g = {g_str}\\,\\text{{m s}}^{{-2}}, \\quad \\theta_{{max}} = {ang_str}^\\circ \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Angular\ Frequency\ (} \\omega \\mathbf{)} \\\\"
            f"&\\omega = \\sqrt{{\\frac{{g}}{{L}}}} = \\sqrt{{\\frac{{{g_str}}}{{{l_str}}}}} = {om_str}\\,\\text{{rad s}}^{{-1}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Determine\ Amplitude\ of\ Displacement\ (} x_0 \\mathbf{)} \\\\"
            "&\\text{{For small angles, }} x_0 = L \\theta_{{rad}} \\\\"
            f"&\\theta_{{rad}} = {ang_str} \\times \\frac{{\\pi}}{{180}} \\approx {(self.theta_rad):.4f}\\,\\text{{rad}} \\\\"
            f"&x_0 = {l_str} \\times {(self.theta_rad):.4f} = {arc_str}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Calculate\ Maximum\ Speed\ (} v_{{max}} \\mathbf{)} \\\\"
            "&v_{{max}} = \\omega x_0 \\\\"
            f"&v_{{max}} = {om_str} \\times {arc_str} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 8), dpi=300)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-3, 8), 6, 0.4, facecolor='#dfe6e9', edgecolor='#2d3436', hatch='///', zorder=1))
        ax.plot([-3, 3], [8, 8], color='#2d3436', lw=2.5, zorder=2)

        pivot_x, pivot_y = 0, 8
        v_scale = 6.5  
        angle_rad = math.radians(self.theta_degrees)
        bob_x = v_scale * math.sin(angle_rad)
        bob_y = pivot_y - v_scale * math.cos(angle_rad)

        ax.plot([0, 0], [pivot_y, pivot_y - v_scale - 0.7], color='#b2bec3', linestyle='--', lw=1.2, alpha=0.8)

        ax.plot([pivot_x, bob_x], [pivot_y, bob_y], color='#2d3436', lw=2, zorder=3)

        ax.text(bob_x/2 + 0.4, (pivot_y + bob_y)/2, f"$L = {self.length:.2f}$ m", 
                color='#2d3436', rotation=-self.theta_degrees, fontweight='bold', fontsize=11, 
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1))

 
        bob = patches.Circle((bob_x, bob_y), 0.4, facecolor='#d63031', edgecolor='#831010', lw=1.5, zorder=5)
        ax.add_patch(bob)

        highlight = patches.Circle((bob_x - 0.12, bob_y + 0.12), 0.1, facecolor='white', alpha=0.4, zorder=6)
        ax.add_patch(highlight)

        arc_radius = 1.8
        angle_arc = patches.Arc((pivot_x, pivot_y), arc_radius*2, arc_radius*2, 
                                theta1=270, theta2=270+self.theta_degrees, 
                                color='#0984e3', lw=2.5)
        ax.add_patch(angle_arc)
        ax.text(0.4, pivot_y - arc_radius - 0.4, f"$\\theta = {self.theta_degrees}^\\circ$", 
                color='#0984e3', fontsize=12, fontweight='bold')

        ax.text(0, pivot_y - v_scale - 1.2, f"$v_{{max}}$\n$g = {self.g}$ m/s$^2$", 
                color='white', fontsize=11, fontweight='bold', ha='center', 
                style='italic', bbox=dict(facecolor='black', edgecolor='black', boxstyle='round,pad=0.5'))
        
        ax.set_title("SIMPLE PENDULUM OSCILLATION", 
                     fontsize=15, fontweight='bold', color='#2d3436', pad=25)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy143:
    def __init__(self):
        while True:
            self.num_oscillations = rnd.randint(10, 25)
            self.total_time = rnd.uniform(15.0, 50.0)
            self.period = self.total_time / self.num_oscillations
            self.frequency = 1 / self.period 
            if self.period > 0.4:
                break

        self.answer = f"{self.frequency:.3f}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        t_str = f"{self.total_time:.2f}"
        n_str = f"{self.num_oscillations}"
        T_val = f"{self.period:.4f}"

        self.description = (
            f"A simple pendulum is observed undergoing small-angle oscillations. "
            f"A student uses a stopwatch to measure the time taken for {n_str} complete oscillations, "
            f"recording a value of {t_str} s. Determine the frequency of the oscillation."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Known\ Parameters} \\\\"
            f"&\\text{{Total time, }} t = {t_str}\\,\\text{{s}} \\\\"
            f"&\\text{{Number of oscillations, }} N = {n_str} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ the\ Time\ Period\ (} T \\mathbf{)} \\\\"
            "&T = \\frac{t}{N} \\\\"
            f"&T = \\frac{{{t_str}}}{{{n_str}}} = {T_val}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Frequency\ (} f \\mathbf{)} \\\\"
            "&f = \\frac{1}{T} \\\\"
            f"&f = \\frac{1}{{{T_val}}} = \\mathbf{{{self.answer}\\,\\text{{Hz}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-2.5, 8), 5, 0.3, facecolor='#dfe6e9', edgecolor='#2d3436', hatch='///'))
        ax.plot([-2.5, 2.5], [8, 8], color='#2d3436', lw=2)

        pivot_x, pivot_y = 0, 8
        v_length = 6.0
        angle_deg = 12
        angle_rad = math.radians(angle_deg)
        
        bob_x = v_length * math.sin(angle_rad)
        bob_y = pivot_y - v_length * math.cos(angle_rad)

        ax.plot([0, 0], [pivot_y, pivot_y - v_length - 0.5], color='#b2bec3', linestyle='--', lw=1)

        ax.plot([pivot_x, bob_x], [pivot_y, bob_y], color='#2d3436', lw=1.5, zorder=2)
        
        path_arc = patches.Arc((pivot_x, pivot_y), v_length*2, v_length*2, 
                               theta1=270-angle_deg, theta2=270+angle_deg, 
                               color='#b2bec3', linestyle=':', lw=1)
        ax.add_patch(path_arc)

        bob = patches.Circle((bob_x, bob_y), 0.35, facecolor='#d63031', edgecolor='#831010', lw=1.5, zorder=5)
        ax.add_patch(bob)
        highlight = patches.Circle((bob_x - 0.1, bob_y + 0.1), 0.08, facecolor='white', alpha=0.4, zorder=6)
        ax.add_patch(highlight)

        ax.annotate("", xy=(-bob_x, bob_y), xytext=(bob_x, bob_y),
                    arrowprops=dict(arrowstyle="<->", connectionstyle="arc3,rad=-0.15", 
                    color='#0984e3', lw=1.5, alpha=0.6))

        info_box = (
            f"$\\mathbf{{Measurement\ Data:}}$\n"
            f"Total time ($t$) = {self.total_time:.2f} s\n"
            f"Oscillations ($N$) = {self.num_oscillations}"
        )
        ax.text(-4.5, 0.5, info_box, fontsize=11, 
                bbox=dict(facecolor='white', edgecolor='#bdc3c7', boxstyle='round,pad=0.8', alpha=0.9))

        ax.set_title("PENDULUM FREQUENCY MEASUREMENT", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy144:
    def __init__(self):
        while True:
            self.omega = rnd.uniform(1.5, 5.0)
            self.x_max = rnd.uniform(0.02, 0.05)
            self.gradient = -self.omega**2
            self.a_max = abs(self.gradient * self.x_max)
            
            if self.a_max <= 5:
                break

        self.answer = f"{self.omega:.2f}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        x_str = f"{self.x_max:.3f}"
        a_str = f"{self.a_max:.3f}"
        grad_abs = f"{abs(self.gradient):.4f}"

        self.description = (
            f"A block of mass $m$ is attached to a horizontal spring and undergoes simple harmonic motion. "
            f"The illustration shows the block at its maximum displacement of $x = {x_str}$ m. "
            f"At this instantaneous position, the block experiences an acceleration of magnitude $a = {a_str}$ m s$^{{-2}}$. "
            f"Calculate the angular frequency $\omega$ of the oscillation."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Given\ Parameters} \\\\"
            f"&\\text{{Maximum displacement, }} x_{{max}} = {x_str}\\,\\text{{m}} \\\\"
            f"&\\text{{Magnitude of acceleration, }} |a| = {a_str}\\,\\text{{m s}}^{{-2}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Relate\ Acceleration\ to\ Displacement} \\\\"
            "&\\text{{For a system in SHM: }} a = -\\omega^2 x \\\\"
            "&\\text{{Taking the magnitude: }} |a| = \\omega^2 |x| \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ } \\omega^2 \\\\"
            f"&\\omega^2 = \\frac{{|a|}}{{|x|}} = \\frac{{{a_str}}}{{{x_str}}} = {grad_abs}\\,\\text{{rad}}^2\\,\\text{{s}}^{{-2}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Final\ Answer} \\\\"
            f"&\\omega = \\sqrt{{{grad_abs}}} = \\mathbf{{{self.answer}\\,\\text{{rad s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
        ax.set_xlim(-0.1, 1.2)
        ax.set_ylim(-0.6, 0.8)
        ax.set_aspect('equal')
        ax.axis('off')

        ax.add_patch(patches.Rectangle((-0.05, -0.1), 0.05, 0.6, facecolor='#636e72', alpha=0.3, hatch='///'))
        ax.plot([0, 0], [-0.1, 0.5], color='#2d3436', lw=4) 
        ax.plot([0, 1.1], [-0.1, -0.1], color='#2d3436', lw=2) 

        eq_x = 0.4
        ax.plot([eq_x, eq_x], [-0.2, 0.6], color='#b2bec3', linestyle='--', lw=1.5)
        ax.text(eq_x, 0.65, "Equilibrium\n($x = 0$)", ha='center', fontsize=9, color='#636e72', fontweight='bold')

        target_x = 0.85 
        num_coils = 15
        spring_x = np.linspace(0, target_x, 300)
        spring_y = 0.08 * np.sin(2 * np.pi * num_coils * (spring_x / target_x))
        ax.plot(spring_x, spring_y, color='#7f8c8d', lw=2)

        block_w, block_h = 0.2, 0.2
        rect = patches.Rectangle((target_x, -0.1), block_w, block_h, facecolor='#fab1a0', edgecolor='#d63031', lw=2, zorder=5)
        ax.add_patch(rect)
        ax.text(target_x + block_w/2, 0, "$m$", ha='center', va='center', fontsize=12, fontweight='bold', color='#d63031')

        ax.annotate("", xy=(target_x + block_w/2, -0.3), xytext=(eq_x, -0.3),
                    arrowprops=dict(arrowstyle='<->', color='#0984e3', lw=2))
        ax.text((target_x + eq_x)/2 + 0.1, -0.45, f"$x = {self.x_max:.3f}$ m", 
                ha='center', color='#0984e3', fontsize=11, fontweight='bold', 
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        ax.annotate("", xy=(target_x - 0.1, 0.3), xytext=(target_x + 0.2, 0.3),
                    arrowprops=dict(arrowstyle='->', color='#d63031', lw=3, mutation_scale=20))
        ax.text(target_x + 0.05, 0.45, f"$a = {self.a_max:.3f}$ m s$^{{-2}}$", 
                ha='center', color='#d63031', fontsize=11, fontweight='bold')

        ax.set_title("HORIZONTAL MASS-SPRING SYSTEM (SHM)", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy145:
    def __init__(self):
        while True:
            self.time_first_peak = rnd.uniform(0.5, 1.2)
            self.delta_t = rnd.uniform(0.8, 1.5)
            self.time_second_peak = self.time_first_peak + self.delta_t
            self.period = 2 * self.delta_t

            if self.period > 1.0:
                break

        self.answer = f"{self.period:.2f}"
        self.topic = "Oscillations"
        self.subtopic = "Simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        t1_str = f"{self.time_first_peak:.2f}"
        t2_str = f"{self.time_second_peak:.2f}"
        dt_str = f"{self.delta_t:.2f}"

        self.description = (
            f"A pendulum bob oscillates with simple harmonic motion. The variation with time $t$ "
            f"of its kinetic energy $E_k$ is shown in the graph. Successive maxima in kinetic energy "
            f"occur at $t_1 = {t1_str}$ s and $t_2 = {t2_str}$ s. Determine the time period $T$ of the pendulum."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Time\ Interval\ between\ Maxima} \\\\"
            f"&\\Delta t = t_2 - t_1 = {t2_str} - {t1_str} = {dt_str}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Relate\ Energy\ Cycle\ to\ Oscillation\ Cycle} \\\\"
            "&\\text{{In SHM, kinetic energy reaches a maximum twice during one complete oscillation.}} \\\\"
            "&\\text{{(Once at the equilibrium position moving right, once moving left).}} \\\\"
            "&\\text{{Therefore, the period of energy variation is half the period of oscillation:}} \\\\"
            "&\\Delta t = \\frac{T}{2} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Time\ Period\ (} T \\mathbf{)} \\\\"
            "&T = 2 \\times \\Delta t \\\\"
            f"&T = 2 \\times {dt_str} = \\mathbf{{{self.answer}\\,\\text{{s}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
        
        T_osc = self.period
        t_plot = np.linspace(0, 1.8 * T_osc, 1000)
        
        # Penyesuaian fase agar puncak pertama berada tepat di self.time_first_peak
        # Ek = Ek_max * cos^2(omega_energy * t + phi)
        omega_osc = 2 * np.pi / T_osc
        phi = (np.pi / 2) - (omega_osc * self.time_first_peak)
        KE = 15 * (np.sin(omega_osc * t_plot + phi))**2

        ax.plot(t_plot, KE, color='#2c3e50', linewidth=2.5, zorder=3)
        
        # Grid dan gaya sumbu
        ax.grid(True, which='both', linestyle='--', alpha=0.5)
        ax.set_xlabel("Time $t$ / s", fontsize=12, fontweight='bold')
        ax.set_ylabel("Kinetic Energy $E_k$ / J", fontsize=12, fontweight='bold')
        ax.set_title("Kinetic Energy vs Time Graph", fontsize=14, fontweight='bold', pad=15)

        # Menandai Puncak (Parameter Diketahui)
        peak_y = 15
        points = [self.time_first_peak, self.time_second_peak]
        labels = [f"$t_1 = {self.time_first_peak:.2f}$ s", f"$t_2 = {self.time_second_peak:.2f}$ s"]

        for p, l in zip(points, labels):
            ax.scatter(p, peak_y, color='#e74c3c', s=60, zorder=5, edgecolor='black')
            ax.annotate(l, xy=(p, peak_y), xytext=(p + 0.05 * T_osc, peak_y + 0.5),
                        fontsize=10, fontweight='bold', color='#e74c3c',
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
            ax.vlines(p, 0, peak_y, colors='#e74c3c', linestyles=':', alpha=0.6)

        # Indikator Delta t (T/2)
        ax.annotate('', xy=(self.time_first_peak, peak_y-2), xytext=(self.time_second_peak, peak_y-2),
                    arrowprops=dict(arrowstyle='<->', color='#3498db', lw=2))
        ax.text((self.time_first_peak + self.time_second_peak)/2, peak_y-1.5, r"$\frac{T}{2}$", 
                ha='center', fontsize=14, color='#3498db', fontweight='bold')

        ax.set_xlim(0, max(t_plot))
        ax.set_ylim(0, 18)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy146:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.05, 0.25)
            self.KE_mJ = rnd.uniform(15.0, 60.0)
            if self.mass > 0 and self.KE_mJ > 0:
                break

        self.KE = self.KE_mJ * 1e-3
        self.v_max = math.sqrt((2 * self.KE) / self.mass)
        self.answer = f"{self.v_max:.2f}"
        
        self.topic = "Oscillations"
        self.subtopic = "Energy in simple harmonic motion"
        self.source = "Original"
        self.curriculum = "A Level"

        m_str = f"{self.mass:.3f}"
        ke_str = f"{self.KE_mJ:.1f}"

        self.description = (
            f"A pendulum bob of mass {m_str} kg oscillates with simple harmonic motion. "
            f"The maximum kinetic energy of the bob during its motion is {ke_str} mJ. "
            f"Calculate the maximum speed of the pendulum bob."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Convert\ Units\ to\ SI} \\\\"
            f"&E_{{k,max}} = {ke_str}\\,\\text{{mJ}} = {ke_str} \\times 10^{{-3}}\\,\\text{{J}} = {self.KE:.4f}\\,\\text{{J}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ State\ the\ Kinetic\ Energy\ Equation} \\\\"
            "&E_k = \\frac{1}{2} m v^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Rearrange\ for\ Maximum\ Speed\ (} v_{{max}} \\mathbf{)} \\\\"
            "&v_{{max}} = \\sqrt{\\frac{2 E_{{k,max}}}{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 4:\ Substitute\ Values\ and\ Solve} \\\\"
            f"&v_{{max}} = \\sqrt{{\\frac{{2 \\times {self.KE:.4f}}}{{{m_str}}}}} \\\\"
            f"&v_{{max}} = \\sqrt{{{ (2*self.KE)/self.mass :.6f}}} \\\\"
            f"&v_{{max}} = \\mathbf{{{self.answer}\\,\\text{{m s}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-1, 9)
        ax.set_aspect('equal')
        ax.axis("off")

        ax.add_patch(patches.Rectangle((-2.5, 8), 5, 0.3, facecolor='#dfe6e9', edgecolor='#2d3436', hatch='///'))
        ax.plot([-2.5, 2.5], [8, 8], color='#2d3436', lw=2)
        
        pivot_x, pivot_y = 0, 8
        length = 6.0
        
        ax.plot([pivot_x, 0], [pivot_y, pivot_y - length], color='#2d3436', lw=1.2, zorder=2)
        ax.plot([pivot_x, -2], [pivot_y, pivot_y - 5.5], color='#b2bec3', linestyle='--', alpha=0.5)
        ax.plot([pivot_x, 2], [pivot_y, pivot_y - 5.5], color='#b2bec3', linestyle='--', alpha=0.5)
        
        bob = patches.Circle((0, pivot_y - length), 0.4, facecolor='#0984e3', edgecolor='#2d3436', lw=1.5, zorder=5)
        ax.add_patch(bob)
        highlight = patches.Circle((-0.1, pivot_y - length + 0.1), 0.1, facecolor='white', alpha=0.3, zorder=6)
        ax.add_patch(highlight)

        ax.annotate("", xy=(1.8, pivot_y - length), xytext=(-1.8, pivot_y - length),
                    arrowprops=dict(arrowstyle="<->", color='#d63031', lw=2, connectionstyle="arc3,rad=0.15"))
        
        ax.annotate("", xy=(1.2, pivot_y - length), xytext=(0, pivot_y - length),
                    arrowprops=dict(arrowstyle="->", color='#00b894', lw=3, mutation_scale=20))
        ax.text(0.6, pivot_y - length + 0.5, "$v_{max}$", color='#00b894', fontsize=12, fontweight='bold')

        info_box = (
            f"Mass ($m$) = {self.mass:.3f} kg\n"
            f"Max $E_k$ = {self.KE_mJ:.1f} mJ"
        )
        ax.text(-4.5, 0.5, info_box, fontsize=11, 
                bbox=dict(facecolor='white', edgecolor='#bdc3c7', boxstyle='round,pad=0.8'))

        ax.set_title("CONSERVATION OF ENERGY IN PENDULUM", fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy147:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.20, 0.45)
            self.k = rnd.uniform(25.0, 55.0)
            self.amplitude_cm = rnd.uniform(5.0, 7.0)
            self.time_interval = 10.0 
            self.gamma = rnd.uniform(0.15, 0.25) 

            self.amplitude = self.amplitude_cm / 100
            self.omega_0 = math.sqrt(self.k / self.mass)
            
            if (self.omega_0**2 - self.gamma**2) > 0:
                self.omega_d = math.sqrt(self.omega_0**2 - self.gamma**2)
                self.frequency = self.omega_d / (2 * math.pi)
                self.period = 1 / self.frequency
                break

        self.energy_initial = 0.5 * self.k * self.amplitude**2
        self.answer = f"{self.frequency:.2f}"
        self.topic = "Oscillations"
        self.subtopic = "Damped oscillations"
        self.source = "Original"
        self.curriculum = "A Level"

        self.description = (
            f"The figure shows the displacement-time graph for a damped oscillating system. "
            f"The mass of the oscillator is {self.mass:.2f} kg and the spring constant is {self.k:.1f} N m$^{{-1}}$. "
            f"Determine the frequency of the oscillation from the graph and the initial total energy."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Determine\ Period\ (T)\ from\ Peaks} \\\\"
            f"&\\text{{Time of 1st peak }} (t_0) = 0.00\\,\\text{{s}} \\\\"
            f"&\\text{{Time of 2nd peak }} (t_1) \\approx {self.period:.2f}\\,\\text{{s}} \\\\"
            f"&T = t_1 - t_0 = {self.period:.2f}\\,\\text{{s}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Calculate\ Frequency\ (f)} \\\\"
            "&f = \\frac{1}{T} = \\frac{1}{" + f"{self.period:.2f}" + "} \\\\"
            f"&f = \\mathbf{{{self.answer}\\,\\text{{Hz}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ Initial\ Energy} \\\\"
            "&E = \\frac{1}{2} k A_0^2 = 0.5 \\times " + f"{self.k:.1f} \\times ({self.amplitude:.4f})^2" + " \\\\"
            f"&E = \\mathbf{{{self.energy_initial:.4f}\\,\\text{{J}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
        
        t = np.linspace(0, self.time_interval, 1200)
        env_upper = self.amplitude_cm * np.exp(-self.gamma * t)
        x_t = env_upper * np.cos(self.omega_d * t)
        
        ax.plot(t, env_upper, color='#e67e22', linestyle='--', lw=1.2, alpha=0.5)
        ax.plot(t, -env_upper, color='#e67e22', linestyle='--', lw=1.2, alpha=0.5)
        ax.plot(t, x_t, color='#2c3e50', lw=2.2, zorder=3)
        ax.axhline(0, color='black', lw=1.5)
        
        t0, t1 = 0, self.period
        ax.vlines([t0, t1], -1.5, [self.amplitude_cm, env_upper[np.abs(t-t1).argmin()]], 
                  colors='#27ae60', linestyles='--', lw=1.5, alpha=0.8)
        
        ax.annotate('', xy=(t1, -1.2), xytext=(t0, -1.2),
                    arrowprops=dict(arrowstyle='<->', color='#27ae60', lw=2))
        ax.text((t0+t1)/2, -1.0, f'$T = {self.period:.2f}$ s', 
                ha='center', fontsize=11, fontweight='bold', color='#27ae60',
                bbox=dict(facecolor='white', alpha=0.9, edgecolor='none'))

        for i in range(2):
            tp = i * self.period
            ap = self.amplitude_cm * np.exp(-self.gamma * tp)
            ax.scatter(tp, ap, color='#c0392b', s=50, zorder=5)
            ax.text(tp, ap + 0.4, f'$A_{i}$', ha='center', fontsize=11, fontweight='bold', color='#c0392b')

        ax.set_xlabel("Time $t$ / s", fontsize=12, fontweight='bold')
        ax.set_ylabel("Displacement $x$ / cm", fontsize=12, fontweight='bold')
        ax.grid(True, which='both', linestyle=':', alpha=0.5)
        ax.minorticks_on()
        
        ax.set_xlim(0, self.time_interval)
        ax.set_ylim(-self.amplitude_cm - 2, self.amplitude_cm + 2)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy148:
    def __init__(self):
        while True:
            self.mass = rnd.uniform(0.8, 2.0)
            self.k = rnd.uniform(20.0, 50.0)
            self.beta = rnd.uniform(0.10, 0.25)

            self.omega0_sq = (2 * self.k) / self.mass
            self.omega_d_sq = self.omega0_sq - self.beta**2

            if self.omega_d_sq > 0:
                self.omega_d = math.sqrt(self.omega_d_sq)
                self.period = 2 * math.pi / self.omega_d
                self.amplitude_cm = rnd.uniform(4.0, 6.0)
                self.amplitude = self.amplitude_cm / 100
                break

        self.answer = f"{self.omega_d:.2f}"
        self.topic = "Oscillations"
        self.subtopic = "Damped oscillations"
        self.source = "Original"
        self.curriculum = "A-Level"

        self.description = (
            f"A block of mass {self.mass:.2f} kg is connected between two identical springs. "
            f"The system undergoes damped oscillations. The resulting displacement–time graph "
            f"is shown. The damping constant is $\\beta = {self.beta:.2f}$ s$^{{-1}}$. "
            f"Determine the damped angular frequency $\\omega_d$ and calculate the spring constant $k$ of one spring."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Determine\ Damped\ Angular\ Frequency\ (\\omega_d)} \\\\"
            "&\\text{From the graph, the period } T = " + f"{self.period:.2f}\\,\\text{{s}}. \\\\"
            "&\\omega_d = \\frac{2\\pi}{T} = \\frac{2\\pi}{" + f"{self.period:.2f}" + "} \\\\"
            f"&\\omega_d = \\mathbf{{{self.answer}\\,\\text{{rad s}}^{{-1}}}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Apply\ the\ Damped\ Oscillation\ Formula} \\\\"
            "&\\text\\omega_0^2 = \\frac{2k}{M}. \\\\"
            "&\\text{The damped frequency relation is: } \\omega_d^2 = \\omega_0^2 - \\beta^2 \\\\"
            "&\\omega_d^2 = \\frac{2k}{M} - \\beta^2 \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Calculate\ the\ Spring\ Constant\ (k)} \\\\"
            "&\\frac{2k}{M} = \\omega_d^2 + \\beta^2 \\\\"
            "&k = \\frac{M(\\omega_d^2 + \\beta^2)}{2} \\\\"
            f"&k = \\frac{{{self.mass:.2f} \\times ({float(self.answer)**2:.3f} + {self.beta**2:.4f})}}{{2}} \\\\"
            f"&k = \\mathbf{{{self.k:.2f}\\,\\text{{N m}}^{{-1}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({"font.size": 10, "axes.linewidth": 1.5})
        fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

        t_end = 3.5 * self.period
        t = np.linspace(0, t_end, 1500)
        envelope = self.amplitude_cm * np.exp(-self.beta * t)
        y = envelope * np.cos(self.omega_d * t)

        ax.plot(t, y, color='#2c3e50', lw=2.5, zorder=3, label='Displacement')
        ax.plot(t, envelope, color='#e67e22', ls='--', lw=1.5, alpha=0.7, label='Envelope')
        ax.plot(t, -envelope, color='#e67e22', ls='--', lw=1.5, alpha=0.7)
        ax.axhline(0, color='black', lw=1.5)

        t0, t1 = 0, self.period
        ax.vlines([t0, t1], -1.0, [self.amplitude_cm, envelope[np.abs(t-t1).argmin()]], 
                  colors='#27ae60', ls=':', lw=2, alpha=0.8)
        
        ax.annotate('', xy=(t1, -0.8), xytext=(t0, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='#27ae60', lw=2))
        ax.text((t0+t1)/2, -0.6, f'$T = {self.period:.2f}$ s', 
                ha='center', fontsize=10, fontweight='bold', color='#27ae60',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

        ax.annotate(f'$A_0 = {self.amplitude_cm:.1f}$ cm', 
                    xy=(0, self.amplitude_cm), xytext=(0.5, self.amplitude_cm + 0.3),
                    arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.5),
                    fontsize=10, fontweight='bold', color='#c0392b')

        ax.set_xlabel("Time $t$ / s", fontweight='bold')
        ax.set_ylabel("Displacement $x$ / cm", fontweight='bold')
        ax.set_title("DAMPED OSCILLATION ANALYSIS ($M + 2k$ System)", fontsize=12, fontweight='bold', pad=15)
        
        ax.minorticks_on()
        ax.grid(True, which='major', color='#bdc3c7', ls='-', alpha=0.5)
        ax.grid(True, which='minor', color='#bdc3c7', ls=':', alpha=0.3)

        info_text = (f"Mass $M = {self.mass:.2f}$ kg\n"
                     f"$\\beta = {self.beta:.2f}$ s$^{{-1}}$")
        ax.text(0.97, 0.95, info_text, transform=ax.transAxes, ha='right', va='top',
                fontsize=9, fontweight='bold', bbox=dict(facecolor='#f8f9fa', edgecolor='#2c3e50', boxstyle='round,pad=0.5'))

        ax.set_xlim(0, t_end)
        ax.set_ylim(-self.amplitude_cm - 1.5, self.amplitude_cm + 1.5)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy149:
    def __init__(self):
        k_e = 8.99e9 

        while True:
            self.separation_cm = rnd.uniform(10.0, 15.0)
            self.offset_cm = rnd.uniform(2.0, self.separation_cm/2 - 1.5)

            self.separation = self.separation_cm / 100
            self.offset = self.offset_cm / 100

            self.r1 = self.offset
            self.r2 = self.separation - self.offset

            self.Q_true = rnd.uniform(5e-8, 5e-7)

            self.E_given = k_e * self.Q_true * (
                (1 / self.r1**2) - (1 / self.r2**2)
            )

            if 5e3 < abs(self.E_given) < 5e5:
                break

        self.Q = self.E_given / (
            k_e * ((1 / self.r1**2) - (1 / self.r2**2))
        )

        self.answer = "{:.2e}".format(self.Q)
        self.topic = "Electric fields"
        self.subtopic = "Electric fields and field lines"
        self.source = "Save my Exam"
        self.curriculum = "A-Level"

        self.description = (
            f"Two identical positive point charges $+Q$ are fixed in a vacuum with a separation of "
            f"{self.separation_cm:.1f} cm. Point $A$ is located on the line connecting the two charges, "
            f"at a distance of {self.offset_cm:.1f} cm from the left-hand charge. "
            f"The resultant electric field strength at point $A$ is {self.E_given:.2e} V m$^{{-1}}$. "
            f"Calculate the magnitude of the charge $Q$."
        )

        self.reasoning = (
            "\\[\\begin{aligned}"
            "&\\mathbf{Step\ 1:\ Identify\ Distances\ in\ SI\ Units} \\\\"
            f"&r_1 = {self.offset:.3f}\\,\\text{{m}} \\\\"
            f"&r_2 = {self.separation:.3f} - {self.offset:.3f} = {self.r2:.3f}\\,\\text{{m}} \\\\[8pt]"
            "&\\mathbf{Step\ 2:\ Formulate\ Resultant\ Electric\ Field} \\\\"
            "&\\text{Field from left charge (rightwards): } E_1 = \\frac{k Q}{r_1^2} \\\\"
            "&\\text{Field from right charge (leftwards): } E_2 = \\frac{k Q}{r_2^2} \\\\"
            "&E_{net} = E_1 - E_2 = k Q \\left( \\frac{1}{r_1^2} - \\frac{1}{r_2^2} \\right) \\\\[8pt]"
            "&\\mathbf{Step\ 3:\ Substitute\ Known\ Values} \\\\"
            f"&{self.E_given:.2e} = (8.99 \\times 10^9) Q \\left( \\frac{1}{{({self.r1:.3f})^2}} - \\frac{1}{{({self.r2:.3f})^2}} \\right) \\\\"
            "&\\mathbf{Step\ 4:\ Solve\ for\ } Q \\\\"
            f"&Q = \\frac{{{self.E_given:.2e}}}{{(8.99 \\times 10^9) ({1/self.r1**2 - 1/self.r2**2:.3f})}} \\\\"
            f"&Q = \\mathbf{{{self.answer}\\,\\text{{C}}}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
        ax.set_xlim(-1, 11)
        ax.set_ylim(-2, 2.5)
        ax.set_aspect('equal')
        ax.axis("off")

        x1, x2 = 1, 9
        x_a = x1 + (self.offset_cm / self.separation_cm) * (x2 - x1)

        ax.plot([x1, x2], [0, 0], color='#b2bec3', linestyle='--', lw=1, zorder=1)

        for x in [x1, x2]:
            charge = plt.Circle((x, 0), 0.25, color='#d63031', zorder=5)
            ax.add_patch(charge)
            ax.text(x, 0.5, "$+Q$", ha='center', fontsize=12, fontweight='bold', color='#d63031')

        ax.scatter(x_a, 0, color='#0984e3', s=100, marker='x', zorder=6, lw=3)
        ax.text(x_a, 0.4, "Point A", ha='center', fontsize=11, fontweight='bold', color='#0984e3')

        ax.annotate('', xy=(x1, -0.8), xytext=(x2, -0.8),
                    arrowprops=dict(arrowstyle='<->', color='#2d3436', lw=1.5))
        ax.text((x1+x2)/2, -1.2, f"$d = {self.separation_cm:.1f}$ cm", ha='center', fontweight='bold')

        ax.annotate('', xy=(x1, 1.2), xytext=(x_a, 1.2),
                    arrowprops=dict(arrowstyle='<->', color='#636e72', lw=1.2))
        ax.text((x1+x_a)/2, 1.5, f"${self.offset_cm:.1f}$ cm", ha='center', color='#636e72')

        ax.set_title("ELECTRIC FIELD SUPERPOSITION", fontsize=14, fontweight='bold', pad=10)

        plt.tight_layout()
        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches="tight")
        plt.close()

class Phy150:
    def __init__(self):
        self.e = 1.60e-19
        self.m_e = 9.11e-31

        while True:
            self.E_pN = rnd.uniform(1.0, 5.0)
            self.E = self.E_pN * 1e-12
            self.force = self.e * self.E
            self.acceleration = self.force / self.m_e
            if self.acceleration > 0:
                break

        self.answer = round(self.acceleration, 2)
        self.description = (
            f"A uniform electric field has strength {self.E_pN:.2f} pN C⁻¹. "
            "Calculate the acceleration of an electron placed in this field. "
            "( _ ) m s⁻²"
        )

        self.topic = "Electric fields"
        self.subtopic = "Electric fields and field lines"
        self.source = "Save My Exams"
        self.curriculum = "A-Level"

        self.reasoning = (
            "\\[\\begin{aligned}"
            "\\textbf{Step 1: Convert electric field to SI units}\\\\"
            f"E &= {self.E_pN:.5f}\\,\\text{{pN C}}^{{-1}}\\\\"
            "\\text{Since } 1\\,\\text{pN} = 10^{-12}\\,\\text{N},\\\\"
            f"E &= {self.E_pN:.5f} \\times 10^{{-12}}\\\\"
            f"E &= {self.E:.5e}\\,\\text{{N C}}^{{-1}}\\\\"
            "\\textbf{Step 2: Electric force on the electron}\\\\"
            "F &= qE\\\\"
            "q &= 1.60 \\times 10^{-19}\\,\\text{C}\\\\"
            f"F &= (1.60 \\times 10^{{-19}})({self.E:.5e})\\\\"
            f"F &= {self.force:.5e}\\,\\text{{N}}\\\\"
            "\\textbf{Step 3: Apply Newton's Second Law}\\\\"
            "F &= ma\\\\"
            "a &= \\frac{F}{m}\\\\"
            "m &= 9.11 \\times 10^{-31}\\,\\text{kg}\\\\"
            f"a &= \\frac{{{self.force:.5e}}}{{9.11 \\times 10^{{-31}}}}\\\\"
            f"a &= {self.acceleration:.5e}\\,\\text{{m s}}^{{-2}}"
            "\\end{aligned}\\]"
        )

    def generate(self, num):
        plt.rcParams.update({
            "font.size": 12,
            "font.family": "serif",
            "text.usetex": False,
            "axes.linewidth": 1.2
        })

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.axis("off")

        ax.text(0.5, 4.9, f"Electric field strength, $E = {self.E_pN:.2f}$ pN C$^{-1}$", fontsize=12)
        ax.text(0.5, 4.5, r"Charge of electron, $e = 1.60 \times 10^{-19}$ C", fontsize=12)
        ax.text(0.5, 4.1, r"Mass of electron, $m_e = 9.11 \times 10^{-31}$ kg", fontsize=12)

        y_positions = np.linspace(1.0, 3.5, 6)
        for y in y_positions:
            ax.arrow(9.0, y, -8.0, 0,
                    head_width=0.15,
                    head_length=0.3,
                    length_includes_head=True,
                    linewidth=1.8,
                    color="#2c6faa",
                    alpha=0.8)
        
        ax.text(9.1, 2.25, r"$\vec{E}$", color="#2c6faa", fontsize=16, weight="bold")

        electron_x, electron_y = 6.0, 2.25
        electron = plt.Circle((electron_x, electron_y), 0.25, 
                            facecolor="#fdfdfd", edgecolor="black", linewidth=1.5, zorder=5)
        ax.add_patch(electron)
        ax.text(electron_x, electron_y, "-", fontsize=20, ha="center", va="center", weight="bold")
        
        ax.text(electron_x, electron_y + 0.4, "Electron", fontsize=12, ha="center", weight="bold")

        dest_image_path = os.path.join(DESTINATION_FOLDER, f"image{num}.png")
        plt.savefig(dest_image_path, dpi=600, bbox_inches="tight", pad_inches=0.2)
        plt.close()
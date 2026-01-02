# helper functions
import numpy as np
import random as rnd
from matplotlib.patches import Circle
from scipy.interpolate import PchipInterpolator
from PIL import Image

def monohybrid_generate_genotype(dom, rec):
    alleles = [rnd.choice([dom, rec]), rnd.choice([dom, rec])]
    alleles.sort() 
    return "".join(alleles)

def dihybrid_generate_genotype(dom_A, rec_A, dom_B, rec_B):
    pair_A = [rnd.choice([dom_A, rec_A]), rnd.choice([dom_A, rec_A])]
    pair_B = [rnd.choice([dom_B, rec_B]), rnd.choice([dom_B, rec_B])]

    pair_A.sort() 
    pair_B.sort() 
    return "".join(pair_A) + "".join(pair_B)

def get_dihybrid_gametes(genotype):
    A = [genotype[0], genotype[1]]
    B = [genotype[2], genotype[3]]
    gametes = []
    for a in A:
        for b in B:
            gametes.append(a + b)
    return gametes

def sigmoid(x, midpoint, L, k=0.7):
    """
    L: Max intensity (as a decimal, e.g., 0.48)
    midpoint: The C value where intensity is 50%
    k: Steepness of the curve
    """
    return L / (1 + np.exp(-k * (x - midpoint)))

def make_curve_pchip(x_knots, y_knots, x_dense):
    f = PchipInterpolator(x_knots, y_knots)
    y = f(x_dense)
    return y

def draw_non_overlapping_circles(ax, box, n_type1, n_type2=0, radius=12, max_tries=3000, facecolor1=None, facecolor2=None, edgecolor="black", linewidth=0.8):
    """
    Draw n circles inside a rectangle box = (x_min, x_max, y_min, y_max)
    in image pixel coordinates, avoiding overlaps as much as possible.
    """
    x_min, x_max, y_min, y_max = box

    x_min2, x_max2 = x_min + radius, x_max - radius
    y_min2, y_max2 = y_min + radius, y_max - radius

    total = n_type1 + n_type2
    centers = []
    tries = 0

    while len(centers) < total and tries < max_tries:
        tries += 1
        x = rnd.uniform(x_min2, x_max2)
        y = rnd.uniform(y_min2, y_max2)

        ok = True
        for (cx, cy) in centers:
            dx = x - cx
            dy = y - cy
            
            if dx*dx + dy*dy < (2*radius)**2:
                ok = False
                break

        if ok:
            centers.append((x, y))

    for i, (x, y) in enumerate(centers):
        fc = facecolor1 if i < n_type1 else facecolor2

        ax.add_patch(Circle((x, y), radius=radius, facecolor=fc, edgecolor=edgecolor, linewidth=linewidth))

    # for (x, y) in centers:
    #     ax.add_patch(Circle((x, y), radius=radius, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth))

def draw_stage(ax, x0, x1, y, n_divs_drawn=12, tick_h=0.35, lw=4):
    """
    Draw a stage micrometer as a thick baseline with thick ticks.
    Returns list of tick x-positions (len = n_divs_drawn+1).
    """
    ax.plot([x0, x1], [y, y], color="black", lw=lw)
    xs = [x0 + i * (x1 - x0) / n_divs_drawn for i in range(n_divs_drawn + 1)]
    for x in xs:
        ax.plot([x, x], [y - tick_h, y + tick_h], color="black", lw=lw)
    return xs

def draw_graticule(ax, x0, x1, y, units_total, major_every=10, minor_h=0.18, mid_h=0.26, major_h=0.34, lw=2):
    """
    Draw an eyepiece graticule baseline + ticks.
    """
    ax.plot([x0, x1], [y, y], color="black", lw=lw)

    for u in range(units_total + 1):
        x = x0 + (x1 - x0) * (u / units_total)

        if u % major_every == 0:
            h = major_h
            w = lw
            ax.text(x, y - h - 0.1, str(u), ha='center', va='top', fontsize=9, fontweight='bold')
        elif u % 5 == 0:
            h = mid_h
            w = lw * 0.8
        else:
            h = minor_h
            w = lw * 0.6

        ax.plot([x, x], [y - h, y + h], color="black", lw=w)
        
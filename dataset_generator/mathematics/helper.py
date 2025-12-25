import random as rnd
import numpy as np

# write helper functions here
def randrange_float(start, stop, step):
    """
    Generates a random float number N such that start <= N < stop, 
    with a specific step size.
    """
    num_steps = int((stop - start) / step)
    random_step = rnd.randint(0, num_steps)
    return start + random_step * step

def fmt_time(x, pos=None):
    total_minutes = int(round(x * 60))
    hh = (total_minutes // 60) % 24
    mm = total_minutes % 60
    return f"{hh:02d}:{mm:02d}"

# Helper for clean formatting (prevents "+ -", "1x", or "0x")
def fmt_poly(coeff, var, is_leading=False):
    if coeff == 0: return ""
    sign = "+" if coeff > 0 else "-"
    val = abs(coeff)
    str_val = str(val) if (val != 1 or var == "") else ""
    if is_leading:
        return f"{'' if coeff > 0 else '-'}{str_val}{var}"
    return f" {sign} {str_val}{var}"

def add_marking(ax, start, end):
    """
    Adds a single slash marking to the midpoint of a line segment 
    to indicate equal length sides in a geometric diagram.
    """
    # Calculate the midpoint of the segment
    mid = (start + end) / 2
    
    # Calculate the direction vector of the side
    vec = end - start
    
    # Calculate the unit vector for the side
    unit_vec = vec / np.linalg.norm(vec)
    
    # Calculate the perpendicular vector for the slash marking.
    # The multiplier 0.15 ensures the mark is short.
    perp = np.array([-unit_vec[1], unit_vec[0]]) * 0.15 
    
    # Plot the slash mark across the midpoint
    ax.plot([mid[0] - perp[0], mid[0] + perp[0]], 
            [mid[1] - perp[1], mid[1] + perp[1]], 
            color='black', lw=2)
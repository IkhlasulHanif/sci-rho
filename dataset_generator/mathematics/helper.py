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
    
def get_angle(p1, p2):
    # Returns angle in degrees (0 to 360)
    dy = p2[1] - p1[1]
    dx = p2[0] - p1[0]
    angle = np.degrees(np.arctan2(dy, dx))
    return angle if angle >= 0 else angle + 360

def draw_solid(ax, x_offset, y_offset, scale, val_h, shape_type):
    """
    Draws a 3D solid (prism, pyramid, cylinder, or cone) with a height label.
    Returns the y-coordinate for placing the "Solid X" label underneath.
    """
    lw_visible = 1.5
    lw_hidden = 1.0
    color = 'black'

    dim_x = x_offset
    h_top = 0
    h_bottom = 0
    label_y_pos = 0

    if shape_type == 'prism':
        p1 = np.array([0, 0]) * scale + [x_offset, y_offset]
        p2 = np.array([1.5, 0.5]) * scale + [x_offset, y_offset]
        p3 = np.array([1.5, 2.5]) * scale + [x_offset, y_offset]
        p4 = np.array([0, 3.5]) * scale + [x_offset, y_offset]
        shift = np.array([1.2, 0.8]) * scale
        b1, b2, b3, b4 = p1+shift, p2+shift, p3+shift, p4+shift

        ax.plot([b1[0], b2[0]], [b1[1], b2[1]], 'k--', lw=lw_hidden)
        ax.plot([b1[0], b4[0]], [b1[1], b4[1]], 'k--', lw=lw_hidden)
        ax.plot([p1[0], b1[0]], [p1[1], b1[1]], 'k--', lw=lw_hidden)
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', lw=lw_visible)
        ax.plot([p2[0], p3[0]], [p2[1], p3[1]], 'k-', lw=lw_visible)
        ax.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-', lw=lw_visible)
        ax.plot([p4[0], p1[0]], [p4[1], p1[1]], 'k-', lw=lw_visible)
        ax.plot([p2[0], b2[0]], [p2[1], b2[1]], 'k-', lw=lw_visible)
        ax.plot([p3[0], b3[0]], [p3[1], b3[1]], 'k-', lw=lw_visible)
        ax.plot([p4[0], b4[0]], [p4[1], b4[1]], 'k-', lw=lw_visible)
        ax.plot([b2[0], b3[0]], [b2[1], b3[1]], 'k-', lw=lw_visible)
        ax.plot([b3[0], b4[0]], [b3[1], b4[1]], 'k-', lw=lw_visible)

        dim_x, h_top, h_bottom = x_offset - 0.8 * scale, p4[1], p1[1]
        label_y_pos = y_offset - 0.5 * scale

    elif shape_type == 'pyramid':
        bw, bh, hp = 3.0*scale, 1.5*scale, 4.0*scale
        cx, cy = x_offset + bw/2, y_offset + bh/2
        v1 = np.array([-bw/2, -bh/2]) + [cx, cy]
        v2 = np.array([bw/2, -bh/2]) + [cx, cy]
        v3 = np.array([bw/2, bh/2]) + [cx, cy]
        v4 = np.array([-bw/2, bh/2]) + [cx, cy]
        apex, center_base = np.array([cx, cy + hp]), np.array([cx, cy])

        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], 'k-', lw=lw_visible)
        ax.plot([v2[0], v3[0]], [v2[1], v3[1]], 'k-', lw=lw_visible)
        ax.plot([v3[0], v4[0]], [v3[1], v4[1]], 'k--', lw=lw_hidden)
        ax.plot([v4[0], v1[0]], [v4[1], v1[1]], 'k--', lw=lw_hidden)
        ax.plot([v1[0], apex[0]], [v1[1], apex[1]], 'k-', lw=lw_visible)
        ax.plot([v2[0], apex[0]], [v2[1], apex[1]], 'k-', lw=lw_visible)
        ax.plot([v3[0], apex[0]], [v3[1], apex[1]], 'k-', lw=lw_visible)
        ax.plot([v4[0], apex[0]], [v4[1], apex[1]], 'k--', lw=lw_hidden)
        ax.plot([center_base[0], apex[0]], [center_base[1], apex[1]], 'k--', lw=1, alpha=0.5)

        dim_x, h_top, h_bottom = v1[0] - 0.5 * scale, apex[1], center_base[1]
        label_y_pos = y_offset - 0.2 * scale

    elif shape_type == 'cylinder':
        r, h_cyl, eh = 1.5 * scale, 4.0 * scale, 0.8 * scale
        cb = np.array([x_offset + r, y_offset + eh/2])
        ct = cb + [0, h_cyl]
        ax.add_patch(patches.Ellipse(ct, 2*r, eh, edgecolor=color, facecolor='none', lw=lw_visible))
        ax.add_patch(patches.Arc(cb, 2*r, eh, theta1=180, theta2=360, edgecolor=color, lw=lw_visible))
        ax.add_patch(patches.Arc(cb, 2*r, eh, theta1=0, theta2=180, edgecolor=color, ls='--', lw=lw_hidden))
        ax.plot([cb[0]-r, ct[0]-r], [cb[1], ct[1]], 'k-', lw=lw_visible)
        ax.plot([cb[0]+r, ct[0]+r], [cb[1], ct[1]], 'k-', lw=lw_visible)

        dim_x, h_top, h_bottom = cb[0] - r - 0.5 * scale, ct[1], cb[1]
        label_y_pos = y_offset - 0.2 * scale

    elif shape_type == 'cone':
        r, h_cone, eh = 1.5 * scale, 4.0 * scale, 0.8 * scale
        cb = np.array([x_offset + r, y_offset + eh/2])
        apex = cb + [0, h_cone]
        ax.add_patch(patches.Arc(cb, 2*r, eh, theta1=180, theta2=360, edgecolor=color, lw=lw_visible))
        ax.add_patch(patches.Arc(cb, 2*r, eh, theta1=0, theta2=180, edgecolor=color, ls='--', lw=lw_hidden))
        ax.plot([cb[0]-r, apex[0]], [cb[1], apex[1]], 'k-', lw=lw_visible)
        ax.plot([cb[0]+r, apex[0]], [cb[1], apex[1]], 'k-', lw=lw_visible)
        ax.plot([cb[0], apex[0]], [cb[1], apex[1]], 'k--', lw=1, alpha=0.5)

        dim_x, h_top, h_bottom = cb[0] - r - 0.5 * scale, apex[1], cb[1]
        label_y_pos = y_offset - 0.2 * scale

    # Height Dimension Arrow and Label
    ax.annotate('', xy=(dim_x, h_top), xytext=(dim_x, h_bottom), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(dim_x - 0.2 * scale, (h_top + h_bottom)/2, f"{val_h}", ha='right', va='center', fontsize=12)
    
    return label_y_pos
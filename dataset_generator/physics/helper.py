# helper functions
import numpy as np
import matplotlib.patches as patches

def val_mapper(val, new_min, new_max, old_min, old_max):
    """Convert a value from a range to another range (e.g., real world measurements to pixel ranges of an image)"""
    return new_max - (new_max - new_min) * (val - old_min) / (old_max - old_min)

def draw_axis(ax, pivot_point, min_point, max_point, value_min, value_max, tick_interval, linewidth=2, direction="v"):
    """Draw a custom axis with major and minor ticks."""
    if direction == "v":
        ax.vlines(x=pivot_point, ymin=min_point, ymax=max_point, colors="black", linewidth=linewidth)
    elif direction == "h":
        ax.hlines(y=pivot_point, xmin=min_point, xmax=max_point, colors="black", linewidth=linewidth)
    else:
        raise ValueError(f"ERROR: {direction} should be either 'v' or 'h'")

    for val in range(value_min, value_max + 1):
        point_coords = val_mapper(val, min_point, max_point, value_min, value_max)
        if val % tick_interval == 0:  # Major tick
            if direction == "v":
                ax.hlines(y=point_coords, xmin=pivot_point-20, xmax=pivot_point+20, colors="black", linewidth=1.5)
                ax.text(pivot_point+25, point_coords, str(val), va="center", ha="left", fontsize=10)
            elif direction == "h":
                ax.vlines(x=point_coords, ymin=pivot_point-20, ymax=pivot_point+20, colors="black", linewidth=1.5)
                ax.text(point_coords, pivot_point+25, str(val), ha="center", va="bottom", fontsize=10)
        else:  # Minor tick
            if direction == "v":
                ax.hlines(y=point_coords, xmin=pivot_point-10, xmax=pivot_point+10, colors="black", linewidth=1)
            elif direction == "h":
                ax.vlines(x=point_coords, ymin=pivot_point-10, ymax=pivot_point+10, colors="black", linewidth=1)

def draw_cartesian(ax, xmin=-20, xmax=20, ymin=-20, ymax=20, tickrange=1, xlabel="X", ylabel="Y", xtickrange=None, ytickrange=None):
    """Draw Cartesian axes with ticks and labels."""
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    if xtickrange is None:
        ax.set_xticks(range(xmin, xmax+1, tickrange))
    else:
        ax.set_xticks(range(xmin, xmax+1, xtickrange))
    if ytickrange is None:
        ax.set_yticks(range(ymin, ymax+1, tickrange))
    else:
        ax.set_yticks(range(ymin, ymax+1, ytickrange))
    ax.grid(True, linestyle="--", alpha=0.5)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def draw_labeled_arrow(ax, start, end, label, 
                       color='black', linewidth=2, 
                       head_width=0.3, head_length=0.4,
                       label_position='top', label_offset=0.3,
                       fontsize=12, fontweight='bold'):
    """
    Draw an arrow with an automatic label placement relative to its direction.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis on which to draw.
    start : tuple (x0, y0)
        Starting point of the arrow.
    end : tuple (x1, y1)
        Ending point of the arrow.
    label : str
        The label text.
    color : str, optional
        Arrow and text color (default: 'black').
    linewidth : float, optional
        Arrow line width (default: 2).
    head_width, head_length : float, optional
        Arrow head size (default: 0.3, 0.4).
    label_position : {'top', 'bottom', 'left', 'right'}, optional
        Where to place the label relative to the arrow direction (default: 'top').
    label_offset : float, optional
        Distance between arrow and label (default: 0.3).
    fontsize : int, optional
        Label font size (default: 12).
    fontweight : str, optional
        Font weight (default: 'bold').
    """

    # Compute arrow direction
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    mid_x = start[0] + dx / 2
    mid_y = start[1] + dy / 2
    angle = np.arctan2(dy, dx)

    # Draw arrow
    ax.arrow(start[0], start[1], dx, dy, 
             head_width=head_width, head_length=head_length,
             fc=color, ec=color, linewidth=linewidth, length_includes_head=True)

    # Determine offset direction for label placement
    if label_position in ['top', 'bottom']:
        # Perpendicular offset
        perp_angle = angle + (np.pi/2 if label_position == 'top' else -np.pi/2)
        offset_x = label_offset * np.cos(perp_angle)
        offset_y = label_offset * np.sin(perp_angle)
    elif label_position in ['left', 'right']:
        along_angle = angle + (0 if label_position == 'right' else np.pi)
        offset_x = label_offset * np.cos(along_angle)
        offset_y = label_offset * np.sin(along_angle)
    else:
        raise ValueError("label_position must be one of: 'top', 'bottom', 'left', 'right'")

    # Draw label
    ax.text(mid_x + offset_x, mid_y + offset_y, label,
            color=color, fontsize=fontsize, fontweight=fontweight,
            ha='center', va='center',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1.5))


# Layering (wires behind, components in front, text on top)
Z_WIRE = 1
Z_COMP = 3
Z_TEXT = 5

def setup_ax(ax, xlim=(0, 10), ylim=(0, 10)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")


def draw_wire(ax, pts, lw=2):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(
        xs, ys,
        linewidth=lw,
        color="black",
        solid_capstyle="projecting",
        solid_joinstyle="miter",
        antialiased=True,
        zorder=Z_WIRE
    )


def draw_text(ax, x, y, s, fontsize=11, ha="center", va="center", boxed=False):
    kw = dict(ha=ha, va=va, fontsize=fontsize, zorder=Z_TEXT)
    if boxed:
        kw["bbox"] = dict(facecolor="white", edgecolor="none", pad=0.35)
    ax.text(x, y, s, **kw)


def draw_circle_meter(ax, x, y, letter, r=0.45, fontsize=14):
    circ = patches.Circle((x, y), r, fill=False, linewidth=2, edgecolor="black", zorder=Z_COMP)
    ax.add_patch(circ)
    draw_text(ax, x, y, letter, fontsize=fontsize, boxed=False)

    return {
        "left": (x - r, y),
        "right": (x + r, y),
        "top": (x, y + r),
        "bottom": (x, y - r),
        "r": r
    }


def draw_resistor_box(ax, x, y, label, w=1.2, h=0.6, value_text=None, fontsize=11):
    rect = patches.Rectangle((x - w/2, y - h/2), w, h, fill=False, linewidth=2,
                             edgecolor="black", zorder=Z_COMP)
    ax.add_patch(rect)
    draw_text(ax, x, y, label, fontsize=fontsize, boxed=False)

    if value_text is not None:
        # Value below: boxed, so wires behind don’t visually run through digits
        draw_text(ax, x, y - h/2 - 0.45, value_text, fontsize=fontsize, va="top", boxed=True)

    return (y + h/2, y - h/2)  # top_y, bottom_y


def draw_thermistor(ax, x, y, label="NTC", w=1.2, h=0.6, value_text=None, fontsize=11):
    rect = patches.Rectangle((x - w/2, y - h/2), w, h, fill=False, linewidth=2,
                             edgecolor="black", zorder=Z_COMP)
    ax.add_patch(rect)

    ax.plot([x - w/2, x + w/2], [y + h/2, y - h/2],
            linewidth=2, color="black", zorder=Z_COMP)

    draw_text(ax, x, y, label, fontsize=fontsize, boxed=False)

    if value_text is not None:
        # Value below: boxed for readability
        draw_text(ax, x, y - h/2 - 0.45, value_text, fontsize=fontsize, va="top", boxed=True)

    return (y + h/2, y - h/2)  # top_y, bottom_y


def draw_cell_vertical(ax, x, y_bottom, y_top, value_text=None, fontsize=11):
    """
    Draw a single cell in a vertical wire segment.
    Uses draw_wire() (projecting caps) so it connects cleanly.
    """
    y_mid = (y_bottom + y_top) / 2
    gap = 0.25
    y_long = y_mid + gap
    y_short = y_mid - gap

    # wires above and below plates
    draw_wire(ax, [(x, y_top), (x, y_long)], lw=2)
    draw_wire(ax, [(x, y_short), (x, y_bottom)], lw=2)

    # plates
    ax.plot([x - 0.55, x + 0.55], [y_long, y_long], linewidth=2, color="black", zorder=Z_COMP)
    ax.plot([x - 0.35, x + 0.35], [y_short, y_short], linewidth=2, color="black", zorder=Z_COMP)

    # + and - marks
    draw_text(ax, x + 0.8, y_long, "+", fontsize=fontsize, boxed=False)
    draw_text(ax, x + 0.8, y_short, "−", fontsize=fontsize, boxed=False)

    if value_text is not None:
        draw_text(ax, x + 1.2, y_mid, value_text, ha="left", fontsize=fontsize, boxed=True)

    return {"top": (x, y_top), "bottom": (x, y_bottom)}


def draw_current_symbol(ax, x, y, direction, r=0.35, lw=2):
    """
    direction: +1 = out of page (dot), -1 = into page (cross)
    """
    # Hollow circle so the symbol is always visible
    circ = patches.Circle((x, y), r, facecolor="white", edgecolor="black", linewidth=lw)
    ax.add_patch(circ)

    if direction == 1:
        # dot (out of page)
        dot = patches.Circle((x, y), r*0.22, facecolor="black", edgecolor="black")
        ax.add_patch(dot)
    else:
        # cross (into page)
        ax.plot([x - r*0.55, x + r*0.55], [y - r*0.55, y + r*0.55], color="black", linewidth=lw)
        ax.plot([x - r*0.55, x + r*0.55], [y + r*0.55, y - r*0.55], color="black", linewidth=lw)


def arrow(ax, x, y, dx, dy, label=None, label_offset=(0, 0), fontsize=12):
    ax.arrow(
        x, y, dx, dy,
        length_includes_head=True,
        head_width=0.22, head_length=0.28,
        linewidth=2, color="black", zorder=Z_COMP
    )
    if label is not None:
        draw_text(ax, x + dx + label_offset[0], y + dy + label_offset[1], label,
                  fontsize=fontsize, boxed=True)
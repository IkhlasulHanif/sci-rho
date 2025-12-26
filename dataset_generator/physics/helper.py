# helper functions
import numpy as np

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
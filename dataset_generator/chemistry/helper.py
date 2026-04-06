import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Wedge, Arc, Polygon
from matplotlib.path import Path
import matplotlib.patches as mpatches

def draw_labeled_box(ax, x, y, width, height, label, sublabel=None, 
                     facecolor='lightblue', edgecolor='black', linewidth=2,
                     label_fontsize=13, sublabel_fontsize=10, label_weight='bold',
                     label_spacing=0.2):
    """
    Draw a rectangle with centered text label(s).
    
    Args:
        ax: matplotlib axis
        x, y: bottom-left corner coordinates
        width, height: box dimensions
        label: main text (centered)
        sublabel: optional text below main label (italic)
        facecolor, edgecolor, linewidth: box styling
        label_fontsize, sublabel_fontsize: text sizes
        label_weight: font weight for main label
        label_spacing: vertical spacing between labels (default 0.2, increased from 0.15)
    
    Returns:
        Rectangle patch object
    """
    rect = Rectangle((x, y), width, height, facecolor=facecolor, 
                     edgecolor=edgecolor, linewidth=linewidth)
    ax.add_patch(rect)
    
    center_x = x + width/2
    center_y = y + height/2
    
    if sublabel:
        ax.text(center_x, center_y + height*label_spacing, label, 
               fontsize=label_fontsize, ha='center', va='center', fontweight=label_weight)
        ax.text(center_x, center_y - height*label_spacing, sublabel, 
               fontsize=sublabel_fontsize, ha='center', va='center', style='italic')
    else:
        ax.text(center_x, center_y, label, 
               fontsize=label_fontsize, ha='center', va='center', fontweight=label_weight)
    
    return rect

def draw_circle_atom(ax, x, y, element, radius=0.3, color='lightblue', 
                     edgecolor='black', linewidth=2, fontsize=14, 
                     text_color='white', show_symbol=True):
    """
    Draw a circle representing an atom with element symbol.
    
    Args:
        ax: matplotlib axis
        x, y: center coordinates
        element: element symbol (e.g., 'C', 'H', 'O')
        radius: circle radius
        color: fill color (can use CPK coloring)
        edgecolor, linewidth: circle border
        fontsize: text size
        text_color: color of element symbol
        show_symbol: whether to show element text
    
    Returns:
        Circle patch object
    """
    circle = Circle((x, y), radius, color=color, ec=edgecolor, 
                   linewidth=linewidth, zorder=3)
    ax.add_patch(circle)
    
    if show_symbol:
        ax.text(x, y, element, fontsize=fontsize, ha='center', va='center', 
               color=text_color, fontweight='bold', zorder=4)
    
    return circle


def draw_bond(ax, x1, y1, x2, y2, bond_type='single', color='black', 
              linewidth=3, spacing=0.15):
    """
    Draw a chemical bond between two points.
    
    Args:
        ax: matplotlib axis
        x1, y1: start coordinates
        x2, y2: end coordinates
        bond_type: 'single', 'double', 'triple', 'dashed' (for coordination)
        color: line color
        linewidth: line thickness
        spacing: gap between parallel lines for multiple bonds
    
    Returns:
        List of Line2D objects
    """
    lines = []
    
    if bond_type == 'single':
        line, = ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)
        lines.append(line)
    
    elif bond_type == 'double':
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        
        perp_x = -dy * spacing / length
        perp_y = dx * spacing / length
        
        line1, = ax.plot([x1 + perp_x, x2 + perp_x], 
                         [y1 + perp_y, y2 + perp_y], 
                         color=color, linewidth=linewidth-1)
        line2, = ax.plot([x1 - perp_x, x2 - perp_x], 
                         [y1 - perp_y, y2 - perp_y], 
                         color=color, linewidth=linewidth-1)
        lines.extend([line1, line2])
    
    elif bond_type == 'triple':
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        
        perp_x = -dy * spacing / length
        perp_y = dx * spacing / length
        
        line1, = ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth-1)
        line2, = ax.plot([x1 + perp_x, x2 + perp_x], 
                         [y1 + perp_y, y2 + perp_y], 
                         color=color, linewidth=linewidth-2)
        line3, = ax.plot([x1 - perp_x, x2 - perp_x], 
                         [y1 - perp_y, y2 - perp_y], 
                         color=color, linewidth=linewidth-2)
        lines.extend([line1, line2, line3])
    
    elif bond_type == 'dashed':
        line, = ax.plot([x1, x2], [y1, y2], color=color, 
                       linewidth=linewidth, linestyle='--', alpha=0.6)
        lines.append(line)
    
    return lines


def draw_arrow(ax, x1, y1, x2, y2, label=None, label_position='side',
               arrowstyle='->', mutation_scale=25, linewidth=2, color='red',
               label_fontsize=11, label_color=None, label_offset=0.3):
    """
    Draw a reaction or process arrow with optional label.
    
    Args:
        ax: matplotlib axis
        x1, y1: start coordinates
        x2, y2: end coordinates
        label: text to display (can be multiline with \\n)
        label_position: 'side', 'above', 'below', 'end'
        arrowstyle: matplotlib arrow style
        mutation_scale: arrow head size
        linewidth: arrow thickness
        color: arrow color
        label_fontsize: label text size
        label_color: label color (defaults to arrow color)
        label_offset: distance from arrow to label
    
    Returns:
        FancyArrowPatch object
    """
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=arrowstyle,
                           mutation_scale=mutation_scale, linewidth=linewidth, 
                           color=color)
    ax.add_patch(arrow)
    
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        if label_color is None:
            label_color = color
        
        if label_position == 'side':
            dx = x2 - x1
            dy = y2 - y1
            length = np.sqrt(dx**2 + dy**2)
            offset_x = -dy * label_offset / length
            offset_y = dx * label_offset / length
            ax.text(mid_x + offset_x, mid_y + offset_y, label,
                   fontsize=label_fontsize, ha='center', va='center',
                   color=label_color, fontweight='bold')
        
        elif label_position == 'above':
            ax.text(mid_x, mid_y + label_offset, label,
                   fontsize=label_fontsize, ha='center', va='bottom',
                   color=label_color, fontweight='bold')
        
        elif label_position == 'below':
            ax.text(mid_x, mid_y - label_offset, label,
                   fontsize=label_fontsize, ha='center', va='top',
                   color=label_color, fontweight='bold')
        
        elif label_position == 'end':
            ax.text(x2 + 0.2, y2, label,
                   fontsize=label_fontsize, ha='left', va='center',
                   color=label_color, fontweight='bold')
    
    return arrow


def draw_bracket(ax, x, y, height, bracket_type='square', direction='left',
                 linewidth=3, subscript=None, subscript_fontsize=11):
    """
    Draw brackets for repeating units or structures.
    
    Args:
        ax: matplotlib axis
        x, y: bottom position of bracket
        height: bracket height
        bracket_type: 'square', 'curly', 'round'
        direction: 'left' or 'right'
        linewidth: bracket thickness
        subscript: text to place outside bracket (e.g., 'n')
        subscript_fontsize: subscript text size
    
    Returns:
        List of Line2D objects
    """
    lines = []
    
    if bracket_type == 'square':
        extension = 0.1
        
        if direction == 'left':
            line1, = ax.plot([x, x], [y, y + height], 'k-', linewidth=linewidth)
            line2, = ax.plot([x, x + extension], [y, y], 'k-', linewidth=linewidth)
            line3, = ax.plot([x, x + extension], [y + height, y + height], 'k-', linewidth=linewidth)
            
            if subscript:
                ax.text(x - 0.2, y + height/2, subscript, 
                       fontsize=subscript_fontsize, ha='right', va='center', fontweight='bold')
        else:
            line1, = ax.plot([x, x], [y, y + height], 'k-', linewidth=linewidth)
            line2, = ax.plot([x - extension, x], [y, y], 'k-', linewidth=linewidth)
            line3, = ax.plot([x - extension, x], [y + height, y + height], 'k-', linewidth=linewidth)
            
            if subscript:
                ax.text(x + 0.2, y + height/2, subscript, 
                       fontsize=subscript_fontsize, ha='left', va='center', fontweight='bold')
        
        lines.extend([line1, line2, line3])
    
    return lines


def draw_simple_molecule(ax, x, y, formula, bond_length=0.8, fontsize=12, 
                         show_bonds=True, bond_color='black'):
    """
    Draw a simple linear molecular formula with bonds.
    
    Args:
        ax: matplotlib axis
        x, y: starting position (left)
        formula: chemical formula string (e.g., 'CH₃-CH₂-OH')
        bond_length: distance between groups
        fontsize: text size
        show_bonds: whether to draw lines between groups
        bond_color: color of bond lines
    
    Returns:
        Total width of molecule drawn
    """
    parts = formula.split('-')
    current_x = x
    
    for i, part in enumerate(parts):
        ax.text(current_x, y, part, fontsize=fontsize, ha='center', 
               va='center', fontweight='bold')
        
        if show_bonds and i < len(parts) - 1:
            ax.plot([current_x + 0.3, current_x + bond_length - 0.3], 
                   [y, y], color=bond_color, linewidth=2)
        
        current_x += bond_length
    
    return current_x - x


def draw_functional_group(ax, x, y, width, height, group_name, group_formula,
                          highlight_color='yellow', alpha=0.3, 
                          edgecolor='red', linewidth=2):
    """
    Draw a highlighted box around a functional group.
    
    Args:
        ax: matplotlib axis
        x, y: bottom-left corner
        width, height: box dimensions
        group_name: name of functional group (e.g., 'Alcohol')
        group_formula: formula (e.g., '-OH')
        highlight_color: box fill color
        alpha: transparency
        edgecolor: border color
        linewidth: border thickness
    
    Returns:
        Rectangle patch object
    """
    rect = Rectangle((x, y), width, height, facecolor=highlight_color, 
                     alpha=alpha, edgecolor=edgecolor, linewidth=linewidth)
    ax.add_patch(rect)
    
    center_x = x + width/2
    ax.text(center_x, y + height/2, group_formula, 
           fontsize=16, ha='center', va='center', 
           fontweight='bold', color=edgecolor)
    
    ax.text(center_x, y - 0.3, group_name, 
           fontsize=11, ha='center', va='top',
           bbox=dict(boxstyle='round', facecolor=highlight_color))
    
    return rect


def draw_carbon_chain(ax, start_x, start_y, num_carbons, orientation='horizontal',
                      spacing=0.85, show_hydrogens=True, terminal_groups=None):
    """
    Draw a straight carbon chain skeleton.
    
    Args:
        ax: matplotlib axis
        start_x, start_y: starting position
        num_carbons: number of carbon atoms
        orientation: 'horizontal' or 'vertical'
        spacing: distance between carbons
        show_hydrogens: whether to show H atoms
        terminal_groups: dict with positions and group names
    
    Returns:
        List of carbon positions [(x, y), ...]
    """
    positions = []
    
    for i in range(num_carbons):
        if orientation == 'horizontal':
            x = start_x + i * spacing
            y = start_y
        else:
            x = start_x
            y = start_y + i * spacing
        
        positions.append((x, y))
        draw_circle_atom(ax, x, y, 'C', radius=0.25, color='black', text_color='white')
        
        if i < num_carbons - 1:
            if orientation == 'horizontal':
                draw_bond(ax, x, y, x + spacing, y, linewidth=3)
            else:
                draw_bond(ax, x, y, x, y + spacing, linewidth=3)
        
        if show_hydrogens:
            if i == 0 or i == num_carbons - 1:
                h_count = 3
            else:
                h_count = 2
            
            for h in range(h_count):
                pass
    
    return positions


def draw_double_bond(ax, x1, y1, x2, y2, spacing=0.15, linewidth=3):
    """
    Draw a double bond (C=C, C=O) with parallel lines.
    
    Args:
        ax: matplotlib axis
        x1, y1: start coordinates
        x2, y2: end coordinates
        spacing: gap between parallel lines
        linewidth: line thickness
    
    Returns:
        List of Line2D objects
    """
    return draw_bond(ax, x1, y1, x2, y2, bond_type='double', 
                    linewidth=linewidth, spacing=spacing)


def draw_reaction_scheme(ax, reactants, products, arrow_y, arrow_x_start, 
                         arrow_x_end, conditions=None, plus_positions=None):
    """
    Draw a complete reaction scheme: reactants → products.
    
    Args:
        ax: matplotlib axis
        reactants: list of (x, y, formula) tuples
        products: list of (x, y, formula) tuples
        arrow_y: y-coordinate of arrow
        arrow_x_start, arrow_x_end: arrow start and end x-coordinates
        conditions: text to show above/below arrow
        plus_positions: list of x-coordinates for '+' signs
    
    Returns:
        Arrow patch object
    """
    for x, y, formula in reactants:
        ax.text(x, y, formula, fontsize=12, ha='center', va='center', fontweight='bold')
    
    if plus_positions:
        for px in plus_positions:
            ax.text(px, arrow_y, '+', fontsize=18, ha='center', va='center', fontweight='bold')
    
    arrow = draw_arrow(ax, arrow_x_start, arrow_y, arrow_x_end, arrow_y,
                      label=conditions, label_position='above', color='black')
    
    for x, y, formula in products:
        ax.text(x, y, formula, fontsize=12, ha='center', va='center', fontweight='bold')
    
    return arrow


def draw_mechanism_step(ax, start_x, start_y, end_x, end_y, 
                       intermediate=None, step_label=None):
    """
    Draw a single mechanism step with curved arrow.
    
    Args:
        ax: matplotlib axis
        start_x, start_y: electron source
        end_x, end_y: electron destination
        intermediate: text description of intermediate
        step_label: step number/name
    
    Returns:
        FancyArrowPatch object
    """
    arrow = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                           arrowstyle='->', mutation_scale=20, 
                           linewidth=2, color='blue',
                           connectionstyle="arc3,rad=.3")
    ax.add_patch(arrow)
    
    if step_label:
        ax.text(start_x - 0.5, start_y + 0.5, step_label,
               fontsize=12, fontweight='bold')
    
    if intermediate:
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        ax.text(mid_x, mid_y - 0.5, intermediate,
               fontsize=10, ha='center', style='italic')
    
    return arrow


def draw_curly_arrow(ax, x1, y1, x2, y2, curvature=0.3, color='blue', 
                     linewidth=2, label=None):
    """
    Draw electron movement arrows (curly arrows) for mechanisms.
    
    Args:
        ax: matplotlib axis
        x1, y1: start (electron source)
        x2, y2: end (electron destination)
        curvature: how curved the arrow is (radius)
        color: arrow color
        linewidth: arrow thickness
        label: optional label text
    
    Returns:
        FancyArrowPatch object
    """
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20,
                           linewidth=linewidth, color=color,
                           connectionstyle=f"arc3,rad={curvature}")
    ax.add_patch(arrow)
    
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y, label, fontsize=9, ha='center',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
    return arrow


def draw_enthalpy_profile(ax, reactant_E, product_E, activation_E,
                          x_start=0, x_end=10, curve_smoothness=50):
    """
    Draw an enthalpy profile diagram skeleton.
    
    Args:
        ax: matplotlib axis
        reactant_E: reactant energy level
        product_E: product energy level
        activation_E: activation energy (peak)
        x_start, x_end: x-axis range
        curve_smoothness: number of points in transition curve
    
    Returns:
        dict with key positions and energies
    """
    plateau_width = (x_end - x_start) * 0.2
    
    ax.plot([x_start, x_start + plateau_width], [reactant_E, reactant_E], 
           'b-', linewidth=3)
    
    x_transition_start = x_start + plateau_width
    x_peak = (x_start + x_end) / 2
    x_transition_end = x_end - plateau_width
    
    x1 = np.linspace(x_transition_start, x_peak, curve_smoothness)
    y1 = reactant_E + (activation_E - reactant_E) * ((x1 - x_transition_start) / (x_peak - x_transition_start))**2
    
    x2 = np.linspace(x_peak, x_transition_end, curve_smoothness)
    y2 = activation_E - (activation_E - product_E) * ((x2 - x_peak) / (x_transition_end - x_peak))**2
    
    ax.plot(x1, y1, 'b-', linewidth=3)
    ax.plot(x2, y2, 'b-', linewidth=3)
    
    ax.plot([x_transition_end, x_end], [product_E, product_E], 'b-', linewidth=3)
    
    ax.set_xlabel('Reaction Progress', fontsize=14, fontweight='bold')
    ax.set_ylabel('Energy (kJ/mol)', fontsize=14, fontweight='bold')
    ax.set_xticks([])
    
    return {
        'reactant_level': reactant_E,
        'product_level': product_E,
        'activation_level': activation_E,
        'reactant_x': x_start + plateau_width/2,
        'product_x': x_end - plateau_width/2,
        'peak_x': x_peak
    }


def draw_vertical_annotation(ax, x, y1, y2, label, color='red', 
                             linewidth=2, label_offset=0.3, fontsize=12):
    """
    Draw a vertical double-headed arrow with label (for ΔH, Ea).
    
    Args:
        ax: matplotlib axis
        x: x-coordinate of arrow
        y1, y2: start and end y-coordinates
        label: text label
        color: arrow and text color
        linewidth: arrow thickness
        label_offset: distance from arrow to label
        fontsize: label text size
    
    Returns:
        FancyArrowPatch object
    """
    arrow = FancyArrowPatch((x, y1), (x, y2),
                           arrowstyle='<->', mutation_scale=20,
                           linewidth=linewidth, color=color)
    ax.add_patch(arrow)
    
    mid_y = (y1 + y2) / 2
    ax.text(x + label_offset, mid_y, label,
           fontsize=fontsize, color=color, fontweight='bold',
           ha='left', va='center')
    
    return arrow


def draw_bar_chart(ax, x_positions, values, labels, colors=None, 
                   width=0.8, xlabel='', ylabel='', title=''):
    """
    Draw a bar chart with labels.
    
    Args:
        ax: matplotlib axis
        x_positions: list of x-coordinates for bars
        values: list of bar heights
        labels: list of x-axis labels
        colors: list of bar colors (or single color)
        width: bar width
        xlabel, ylabel, title: axis labels
    
    Returns:
        BarContainer object
    """
    if colors is None:
        colors = 'blue'
    
    bars = ax.bar(x_positions, values, width=width, color=colors, 
                 edgecolor='black', linewidth=1.5, alpha=0.7)
    
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    return bars


def draw_line_graph(ax, x_data, y_data, color='blue', linewidth=3, 
                   marker='o', markersize=8, label=None,
                   xlabel='', ylabel='', title=''):
    """
    Draw a line graph with markers.
    
    Args:
        ax: matplotlib axis
        x_data, y_data: data arrays
        color: line color
        linewidth: line thickness
        marker: marker style
        markersize: marker size
        label: legend label
        xlabel, ylabel, title: axis labels
    
    Returns:
        Line2D object
    """
    line, = ax.plot(x_data, y_data, color=color, linewidth=linewidth,
                   marker=marker, markersize=markersize, label=label)
    
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    if label:
        ax.legend(fontsize=12)
    
    return line


def draw_data_table(ax, data, start_x=2, start_y=5, cell_width=3, 
                   cell_height=0.6, header_color='lightblue'):
    """
    Draw a formatted data table.
    
    Args:
        ax: matplotlib axis
        data: 2D list [[row1], [row2], ...]
        start_x, start_y: top-left corner
        cell_width: width of each cell
        cell_height: height of each cell
        header_color: background color for first row
    
    Returns:
        List of Rectangle patches
    """
    rectangles = []
    
    for i, row in enumerate(data):
        y = start_y - i * cell_height
        
        for j, cell in enumerate(row):
            x = start_x + j * cell_width
            
            if i == 0:
                rect = Rectangle((x, y - cell_height), cell_width, cell_height,
                               facecolor=header_color, edgecolor='black', linewidth=2)
                ax.text(x + cell_width/2, y - cell_height/2, str(cell),
                       fontsize=12, ha='center', va='center', fontweight='bold')
            else:
                rect = Rectangle((x, y - cell_height), cell_width, cell_height,
                               facecolor='white', edgecolor='black', linewidth=1)
                ax.text(x + cell_width/2, y - cell_height/2, str(cell),
                       fontsize=12, ha='center', va='center')
            
            ax.add_patch(rect)
            rectangles.append(rect)
    
    return rectangles


def add_formula_label(ax, x, y, formula, fontsize=12, ha='center', 
                      va='center', weight='bold', color='black',
                      bbox_style=None):
    """
    Add a chemical formula label with proper formatting.
    
    Args:
        ax: matplotlib axis
        x, y: text position
        formula: chemical formula string (subscripts as ₁₂₃, superscripts as ⁺⁻)
        fontsize: text size
        ha, va: horizontal and vertical alignment
        weight: font weight
        color: text color
        bbox_style: optional dict for background box
    
    Returns:
        Text object
    """
    if bbox_style:
        text = ax.text(x, y, formula, fontsize=fontsize, ha=ha, va=va,
                      fontweight=weight, color=color, bbox=bbox_style)
    else:
        text = ax.text(x, y, formula, fontsize=fontsize, ha=ha, va=va,
                      fontweight=weight, color=color)
    
    return text


def add_charge_label(ax, x, y, charge_type, fontsize=12, color='blue'):
    """
    Add δ+/δ- or full charge labels.
    
    Args:
        ax: matplotlib axis
        x, y: position
        charge_type: 'delta+', 'delta-', '+', '-', '2+', etc.
        fontsize: text size
        color: text color
    
    Returns:
        Text object
    """
    charge_map = {
        'delta+': 'δ+',
        'delta-': 'δ-',
        '+': '+',
        '-': '-',
        '2+': '²⁺',
        '2-': '²⁻',
        '3+': '³⁺'
    }
    
    display_text = charge_map.get(charge_type, charge_type)
    
    text = ax.text(x, y, display_text, fontsize=fontsize, 
                  color=color, fontweight='bold')
    
    return text

def add_charge_label_with_offset(ax, x, y, charge_type, fontsize=12, color='blue',
                                 x_offset=0, y_offset=0.6):
    """
    Add δ+/δ- or full charge labels with configurable offset.
    
    Args:
        ax: matplotlib axis
        x, y: base position
        charge_type: 'delta+', 'delta-', '+', '-', '2+', etc.
        fontsize: text size
        color: text color
        x_offset: horizontal offset from base position
        y_offset: vertical offset from base position (default 0.6, increased from 0)
    
    Returns:
        Text object
    """
    charge_map = {
        'delta+': 'δ+',
        'delta-': 'δ-',
        '+': '+',
        '-': '-',
        '2+': '²⁺',
        '2-': '²⁻',
        '3+': '³⁺'
    }
    
    display_text = charge_map.get(charge_type, charge_type)
    
    text = ax.text(x + x_offset, y + y_offset, display_text, fontsize=fontsize, 
                  color=color, fontweight='bold')
    
    return text

def add_title_box(ax, x, y, title, fontsize=16, facecolor='lightyellow',
                  edgecolor='black', linewidth=2, padding=0.3, 
                  min_spacing=0.5):
    """
    Add a centered title with background box.
    
    Args:
        ax: matplotlib axis
        x, y: center position
        title: title text
        fontsize: text size
        facecolor: box background color
        edgecolor: box border color
        linewidth: border thickness
        padding: space around text
        min_spacing: minimum spacing from plot elements (default 0.5)
    
    Returns:
        Text object
    """
    text = ax.text(x, y, title, fontsize=fontsize, ha='center', va='center',
                  fontweight='bold',
                  bbox=dict(boxstyle=f'round,pad={padding}', 
                           facecolor=facecolor, 
                           edgecolor=edgecolor, 
                           linewidth=linewidth))
    
    return text

def draw_test_tube(ax, x, y, width=1.4, height=3.5, solution_height=2.5,
                   solution_color='lightblue', tube_linewidth=2):
    """
    Draw a test tube outline with solution.
    
    Args:
        ax: matplotlib axis
        x, y: bottom-left corner
        width: tube width
        height: tube height
        solution_height: height of solution inside
        solution_color: color of solution
        tube_linewidth: outline thickness
    
    Returns:
        dict with tube and solution patches
    """
    tube = Rectangle((x, y), width, height, fill=False, 
                    edgecolor='black', linewidth=tube_linewidth)
    ax.add_patch(tube)
    
    solution = Rectangle((x + 0.05, y + 0.05), width - 0.1, solution_height,
                        facecolor=solution_color, edgecolor='black', linewidth=1)
    ax.add_patch(solution)
    
    return {'tube': tube, 'solution': solution}


def draw_beaker(ax, x, y, width=3, height=4, liquid_height=2.5,
               liquid_color='lightblue', beaker_linewidth=2):
    """
    Draw a beaker with liquid level.
    
    Args:
        ax: matplotlib axis
        x, y: bottom-left corner
        width: beaker width
        height: beaker height
        liquid_height: height of liquid inside
        liquid_color: color of liquid
        beaker_linewidth: outline thickness
    
    Returns:
        dict with beaker and liquid patches
    """
    beaker = Rectangle((x, y), width, height, fill=False,
                      edgecolor='black', linewidth=beaker_linewidth)
    ax.add_patch(beaker)
    
    liquid = Rectangle((x + 0.2, y + 0.2), width - 0.4, liquid_height,
                      facecolor=liquid_color, alpha=0.3, edgecolor='black', linewidth=1)
    ax.add_patch(liquid)
    
    return {'beaker': beaker, 'liquid': liquid}


def draw_mass_spectrum_peak(ax, mz, intensity, width=0.8, color='darkblue',
                            label_peak=True, label_offset=3):
    """
    Draw a single peak in a mass spectrum.
    
    Args:
        ax: matplotlib axis
        mz: m/z value (x-position)
        intensity: peak height (0-100)
        width: bar width
        color: bar color
        label_peak: whether to label with m/z value
        label_offset: distance above peak for label
    
    Returns:
        Rectangle patch
    """
    bar = ax.bar(mz, intensity, width=width, color=color,
                edgecolor='black', linewidth=1)
    
    # if label_peak:
    #     ax.text(mz, intensity + label_offset, f'{int(mz)}',
    #            fontsize=10, ha='center', fontweight='bold')
    
    return bar


def draw_nmr_peak(ax, chemical_shift, integration, splitting='singlet',
                 j_coupling=0.007, sigma=0.02, max_height=100):
    """
    Draw an NMR peak with splitting pattern.
    
    Args:
        ax: matplotlib axis
        chemical_shift: δ value (ppm)
        integration: relative integration value
        splitting: 'singlet', 'doublet', 'triplet', 'quartet', 'multiplet'
        j_coupling: coupling constant spacing (ppm)
        sigma: peak width
        max_height: maximum peak height
    
    Returns:
        Array of x, y values for the peak
    """
    x = np.linspace(chemical_shift - 0.5, chemical_shift + 0.5, 1000)
    y = np.zeros_like(x)
    
    if splitting == 'singlet':
        y = integration * max_height * np.exp(-((x - chemical_shift)**2) / (2 * sigma**2))
    
    elif splitting == 'doublet':
        for offset, ratio in zip([-0.5, 0.5], [1, 1]):
            pos = chemical_shift + offset * j_coupling
            y += integration * ratio * max_height/2 * np.exp(-((x - pos)**2) / (2 * sigma**2))
    
    elif splitting == 'triplet':
        for offset, ratio in zip([-1, 0, 1], [1, 2, 1]):
            pos = chemical_shift + offset * j_coupling
            y += integration * ratio * max_height/4 * np.exp(-((x - pos)**2) / (2 * sigma**2))
    
    elif splitting == 'quartet':
        for offset, ratio in zip([-1.5, -0.5, 0.5, 1.5], [1, 3, 3, 1]):
            pos = chemical_shift + offset * j_coupling
            y += integration * ratio * max_height/8 * np.exp(-((x - pos)**2) / (2 * sigma**2))
    
    line, = ax.plot(x, y, 'b-', linewidth=1.5)
    ax.fill_between(x, 0, y, alpha=0.3)
    
    return x, y

def draw_3d_molecule(ax, atom_positions, bonds, labels=None, 
                    atom_colors=None, radius=0.3, label_offset=0.4):
    """
    Draw a 3D molecule on a 3D axis.
    
    Args:
        ax: matplotlib 3D axis
        atom_positions: list of (x, y, z) tuples
        bonds: list of (i, j) tuples indicating bonded atoms
        labels: list of element symbols
        atom_colors: list of colors for each atom
        radius: atom sphere radius
        label_offset: distance from atom center to label (default 0.4, increased from 0.15)
    
    Returns:
        dict with atoms and bonds objects
    """
    if atom_colors is None:
        atom_colors = ['lightblue'] * len(atom_positions)
    
    if labels is None:
        labels = ['C'] * len(atom_positions)
    
    for i, ((x, y, z), color, label) in enumerate(zip(atom_positions, atom_colors, labels)):
        ax.scatter(x, y, z, s=500, c=color, marker='o', 
                  edgecolors='black', linewidths=2, zorder=3)
        # UPDATED: Use configurable label_offset instead of hardcoded 0.15
        ax.text(x, y, z + label_offset, label, fontsize=14, ha='center', 
               va='bottom', fontweight='bold', zorder=4)
    
    for i, j in bonds:
        p1 = atom_positions[i]
        p2 = atom_positions[j]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 
               'k-', linewidth=3)
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    return {'positions': atom_positions, 'bonds': bonds}

def draw_3d_info_box(ax, text, position='bottom', z_offset=-2.5, 
                    fontsize=14, facecolor='lightyellow'):
    """
    Add an information box to a 3D plot with better positioning.
    
    Args:
        ax: matplotlib 3D axis
        text: text to display (can be multi-line with \\n)
        position: 'bottom', 'top', 'left', 'right'
        z_offset: vertical offset from origin
        fontsize: text size
        facecolor: background color
    
    Returns:
        Text object
    """
    x_pos = 0
    y_pos = 0
    
    text_obj = ax.text(x_pos, y_pos, z_offset, text, fontsize=fontsize, 
                      ha='center', fontweight='bold',
                      bbox=dict(boxstyle='round', facecolor=facecolor, 
                               edgecolor='black'))
    return text_obj

def format_chemical_formula(text):
    """
    Convert text to properly formatted chemical formula.
    Handles common subscripts and superscripts.
    
    Args:
        text: raw text (e.g., "H2O", "Fe3+")
    
    Returns:
        Formatted string with Unicode subscripts/superscripts
    """
    subscript_map = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄',
                     '5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'}
    superscript_map = {'+':'⁺', '-':'⁻', '2':'²', '3':'³'}
    
    result = text
    
    for k, v in subscript_map.items():
        result = result.replace(k, v)
    
    return result

def draw_skeletal_formula(ax, atoms, bonds, cx=0.0, cy=0.0, scale=1.0,
                          fontsize=9, lw=2.0, color='black'):
    """
    Draw a skeletal (line-angle) formula centred at (cx, cy).
 
    atoms : list of (x, y, label)
        Normalised positions (nominal bond length = 1.0).
        label = None  -> carbon vertex (not drawn explicitly).
        label = str   -> heteroatom label drawn at that position
                         e.g. 'O', 'OH', 'Cl', 'Br'.
    bonds : list of (i, j, bond_type)
        bond_type : 'single' or 'double'
    cx, cy : centre of structure in axes coordinates
    scale  : multiplier applied to all normalised distances
    """
    if not atoms:
        return
 
    xs = [a[0] for a in atoms]
    ys = [a[1] for a in atoms]
    mid_x = (max(xs) + min(xs)) / 2.0
    mid_y = (max(ys) + min(ys)) / 2.0
 
    def coord(a):
        return (a[0] - mid_x) * scale + cx, (a[1] - mid_y) * scale + cy
 
    for i, j, btype in bonds:
        x1, y1 = coord(atoms[i])
        x2, y2 = coord(atoms[j])
        if btype == 'single':
            ax.plot([x1, x2], [y1, y2], color=color, lw=lw,
                    solid_capstyle='round', zorder=2)
        elif btype == 'double':
            dx, dy = x2 - x1, y2 - y1
            length = (dx**2 + dy**2) ** 0.5 + 1e-9
            gap = 0.055 * scale
            ox, oy = -dy * gap / length, dx * gap / length
            ax.plot([x1 + ox, x2 + ox], [y1 + oy, y2 + oy],
                    color=color, lw=lw * 0.85, solid_capstyle='round', zorder=2)
            ax.plot([x1 - ox, x2 - ox], [y1 - oy, y2 - oy],
                    color=color, lw=lw * 0.85, solid_capstyle='round', zorder=2)
 
    for atom in atoms:
        if atom[2] is not None:
            px, py = coord(atom)
            ax.text(px, py, atom[2],
                    fontsize=fontsize, ha='center', va='center',
                    color=color, fontweight='bold', zorder=3,
                    bbox=dict(facecolor='white', edgecolor='none', pad=1.5))
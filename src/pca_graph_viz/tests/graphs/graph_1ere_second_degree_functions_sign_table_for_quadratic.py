import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Second Degree Functions
# Subsection: Sign Table for Quadratic
# Description: A horizontal line representing the x-axis with roots marked. Above the line, show where the quadratic is positive (+) or negative (-). The discriminant determines if there are 0, 1, or 2 roots. Include the factored form if applicable.

# Consider f(x) = (x + 2)(x - 3) = x² - x - 6
# Roots at x = -2 and x = 3
root1 = -2
root2 = 3

# Generate the parabola for illustration
x = np.linspace(-4, 5, 100)
y = (x - root1) * (x - root2)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
positive_color = "#27ae60"  # Green
negative_color = "#e74c3c"  # Red
parabola_color = "#3498db"  # Blue

# Table structure
table_y = 1.5  # y position for the sign table
arrow_y = 2.5  # y position for variation arrow

# All visual elements in lines array
lines = [
    # Small parabola illustration
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": [y_val * 0.15 for y_val in y.tolist()]},
        "stroke": parabola_color,
        "stroke-width": 2,
        "fill": "none",
        "stroke-opacity": 0.5,
        "class": "curve parabola",
    },
    # Main horizontal line for sign table
    {
        "type": "line",
        "x1": -4,
        "y1": table_y,
        "x2": 5,
        "y2": table_y,
        "stroke": "#333333",
        "stroke-width": 2,
        "class": "sign-table-line",
    },
    # Root markers
    {
        "type": "circle",
        "cx": root1,
        "cy": table_y,
        "r": 0.08,
        "fill": "#333333",
        "class": "root-marker-1",
    },
    {
        "type": "circle",
        "cx": root2,
        "cy": table_y,
        "r": 0.08,
        "fill": "#333333",
        "class": "root-marker-2",
    },
    # Vertical lines at roots
    {
        "type": "line",
        "x1": root1,
        "y1": table_y - 0.3,
        "x2": root1,
        "y2": table_y + 0.3,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "class": "root-line-1",
    },
    {
        "type": "line",
        "x1": root2,
        "y1": table_y - 0.3,
        "x2": root2,
        "y2": table_y + 0.3,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "class": "root-line-2",
    },
    # Sign regions - curved arrows showing variation
    # Positive region (left)
    {
        "type": "path",
        "d": f"M -3.5 {arrow_y} Q -3 {arrow_y + 0.3} -2.5 {arrow_y}",
        "stroke": positive_color,
        "stroke-width": 2,
        "fill": "none",
        "marker-end": "url(#arrowhead)",
        "class": "positive-arrow-left",
    },
    # Negative region (middle)
    {
        "type": "path",
        "d": f"M -1.5 {arrow_y} Q 0.5 {arrow_y - 0.3} 2.5 {arrow_y}",
        "stroke": negative_color,
        "stroke-width": 2,
        "fill": "none",
        "marker-end": "url(#arrowhead)",
        "class": "negative-arrow-middle",
    },
    # Positive region (right)
    {
        "type": "path",
        "d": f"M 3.5 {arrow_y} Q 4 {arrow_y + 0.3} 4.5 {arrow_y}",
        "stroke": positive_color,
        "stroke-width": 2,
        "fill": "none",
        "marker-end": "url(#arrowhead)",
        "class": "positive-arrow-right",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -4,
        "y1": 0,
        "x2": 5,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1,
        "x2": 0,
        "y2": 3,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    # Function formula
    {
        "x": -1,
        "y": -0.8,
        "latex": r"f(x) = (x+2)(x-3)",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": parabola_color,
    },
    # Root labels
    {
        "x": root1 - 0.2,
        "y": table_y - 0.5,
        "latex": r"-2",
        "width": 25,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#333333",
    },
    {
        "x": root2 - 0.1,
        "y": table_y - 0.5,
        "latex": r"3",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#333333",
    },
    # Sign labels
    {
        "x": -3,
        "y": arrow_y + 0.2,
        "latex": r"+",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": positive_color,
    },
    {
        "x": 0.5,
        "y": arrow_y - 0.5,
        "latex": r"-",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": negative_color,
    },
    {
        "x": 4,
        "y": arrow_y + 0.2,
        "latex": r"+",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": positive_color,
    },
    # Interval labels
    {
        "x": -3.5,
        "y": table_y + 0.8,
        "latex": r"x \in ]-\infty, -2[",
        "width": 80,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#666666",
    },
    {
        "x": 0.2,
        "y": table_y + 0.8,
        "latex": r"x \in ]-2, 3[",
        "width": 60,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#666666",
    },
    {
        "x": 3.5,
        "y": table_y + 0.8,
        "latex": r"x \in ]3, +\infty[",
        "width": 70,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_second_degree_functions_sign_table_for_quadratic",
        "title": "Sign Table for Quadratic",
        "description": "Sign table showing where quadratic function is positive or negative",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 5,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

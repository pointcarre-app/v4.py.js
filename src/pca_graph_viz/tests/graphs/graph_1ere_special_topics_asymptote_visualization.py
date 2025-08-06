import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Asymptote Visualization
# Description: Function approaching but never reaching certain lines. Horizontal asymptotes as x → ±∞, vertical asymptotes where function undefined. Dashed lines for asymptotes, different color from function curve.

# Generate function with asymptotes: f(x) = 1/(x-1) + 2
x_left = np.linspace(-3, 0.9, 50)  # Left side of vertical asymptote
x_right = np.linspace(1.1, 4, 50)  # Right side of vertical asymptote

y_left = 1/(x_left - 1) + 2
y_right = 1/(x_right - 1) + 2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for function
asymptote_color = "#ec3059"  # Red for asymptotes

# All visual elements in lines array
lines = [
    # Function curve (left side)
    {
        "type": "curve",
        "id": "function_left",
        "data": {"x": x_left.tolist(), "y": y_left.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve function",
    },
    # Function curve (right side)
    {
        "type": "curve",
        "id": "function_right",
        "data": {"x": x_right.tolist(), "y": y_right.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve function",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -3,
        "y1": 0,
        "x2": 4,
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
        "y1": -2,
        "x2": 0,
        "y2": 6,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 2.5,
        "y": 4,
        "latex": r"f(x) = \frac{1}{x-1} + 2",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 1.2,
        "y": 3,
        "latex": r"x = 1",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": 2.5,
        "y": 2.2,
        "latex": r"y = 2",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_asymptote_visualization",
        "title": "Asymptote Visualization",
        "description": "Function f(x) = 1/(x-1) + 2 showing vertical asymptote at x=1 and horizontal asymptote at y=2",
        "svg": {
            "width": 400,
            "height": 350,
            "viewBox": "0 0 400 350",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 20,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

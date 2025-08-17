import numpy as np

# Simple parabola visualization: y = x² with y = 1 line

# Generate parabola: y = x²
x = np.linspace(-3, 3, 100)
y = x**2

# Simple colors matching DaisyUI theme
bg_color = "#ffffff"  # base-100
axis_color = "#1f2937"  # base-content
parabola_color = "#3b82f6"  # primary
line_color = "#10b981"  # secondary

# Simple visual elements
lines = [
    # X-axis
    {
        "type": "axis",
        "x1": -3,
        "y1": 0,
        "x2": 3,
        "y2": 0,
        "stroke": axis_color,
        "stroke-width": 1.5,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1,
        "x2": 0,
        "y2": 10,
        "stroke": axis_color,
        "stroke-width": 1.5,
        "class": "axis y-axis",
    },
    # Parabola curve
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": parabola_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve primary",
    },
    # Horizontal line y = 1
    {
        "type": "line",
        "x1": -3,
        "y1": 1,
        "x2": 3,
        "y2": 1,
        "stroke": line_color,
        "stroke-width": 1.5,
        "stroke-dasharray": "5,5",
        "class": "line secondary",
    },
]

foreign_objects = [
    # Parabola equation
    {
        "x": 1.5,
        "y": 8.5,
        "latex": r"y = x^2",
        "width": 60,
        "height": 25,
        "bg_color": "transparent",
        "text_color": parabola_color,
    },
    # Line equation
    {
        "x": -2.8,
        "y": 1.1,
        "latex": r"y = 1",
        "width": 50,
        "height": 20,
        "bg_color": "transparent",
        "text_color": line_color,
    },
    # X axis label
    {
        "x": 2.8,
        "y": -0.3,
        "latex": r"x",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": axis_color,
    },
    # Y axis label
    {
        "x": 0.1,
        "y": 9.5,
        "latex": r"y",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": axis_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "simple-parabola",
        "title": "Parabola y = x² with y = 1",
        "description": "Simple visualization of parabola with horizontal line",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 30,
            "show_axes": False,
            "show_grid": False,
            "x_range": [-3, 3],
            "y_range": [-1, 10],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

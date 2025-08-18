import numpy as np

# Simple parabola visualization: y = x² with y = 1 line

# Generate parabola: y = x²
x = np.linspace(-4, 4, 1000)
y = x**2

# Using CSS classes instead of hard-coded colors
# The classes are defined in sujets0.html and use DaisyUI CSS variables

# Simple visual elements
lines = [
    # X-axis
    {
        "type": "axis",
        "x1": -4,
        "y1": 0,
        "x2": 4,
        "y2": 0,
        "stroke-width": 1.5,
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1,
        "x2": 0,
        "y2": 16.2,
        "stroke-width": 1.5,
        "class": "axis y-axis stroke-base-content",
    },
    # Parabola curve
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve stroke-primary",
    },
    # Horizontal line y = 1
    {
        "type": "line",
        "x1": -4,
        "y1": 10,
        "x2": 4,
        "y2": 10,
        "stroke-width": 1.5,
        "stroke-dasharray": "5,5",
        "class": "line stroke-secondary",
    },
]

foreign_objects = [
    # Parabola equation
    {
        "x": 2.5,
        "y": 2.5,
        "latex": "y = x^2",
        "width": 80,
        "height": 25,
        "class": "svg-latex text-primary",
    },
    # Line equation
    {
        "x": -0.75,
        "y": 10.5,
        "latex": "y = 10",
        "width": 50,
        "height": 20,
        "class": "svg-latex text-secondary",
    },
    # X axis label
    {
        "x": 4,
        "y": -0.4,
        "latex": "x",
        "width": 20,
        "height": 20,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label
    {
        "x": 0.25,
        "y": 16,
        "latex": "y",
        "width": 20,
        "height": 20,
        "class": "svg-latex fill-base-content",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "simple-parabola",
        "title": "spe_sujet1_auto_07_question_canonical.py",
        "description": "Simple visualization of parabola with horizontal line",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": 30,
            "show_axes": False,
            "show_grid": False,
            "x_range": [-3, 3],
            "y_range": [-1, 17],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

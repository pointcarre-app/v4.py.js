import numpy as np

Y_LABEL_FOR_HORIZONTAL_LINE = 10

# Simple parabola visualization: y = x² with y = 1 line (small 150x150)

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
        "x1": -3.5,
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
        "y1": -4,
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
    # Horizontal line y = 10
    {
        "type": "line",
        "x1": -4,
        "y1": 10,
        "x2": 4,
        "y2": 10,
        "stroke-width": 1.5,
        # "stroke-dasharray": "5,5",
        "class": "line stroke-secondary",
    },
]

foreign_objects = [
    # Parabola equation
    # {
    #     "x": 3,
    #     "y": 1.5,
    #     "latex": "y = x^2",
    #     "width": 80,
    #     "height": 25,
    #     "class": "svg-latex text-primary",
    # },
    # Line equation
    {
        "x": 1.65,
        "y": 11,
        "latex": f"y={Y_LABEL_FOR_HORIZONTAL_LINE}",
        "width": 50,
        "height": 20,
        "class": "svg-latex text-secondary text-xs",
    },
    # X axis label
    {
        "x": 4,
        "y": -1,
        "latex": "x",
        "width": 20,
        "height": 10,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label
    {
        "x": 0.75,
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
        "id": "simple-parabola-small",
        "title": "Parabola y = x² with y = 1",
        "description": "Simple visualization of parabola with horizontal line (150x150)",
        "svg": {
            "width": 150,
            "height": 150,
            "viewBox": "0 0 150 150",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": {"top": 10, "right": 10, "bottom": 28, "left": 10},
            "show_axes": False,
            "show_grid": False,
            "x_range": [-4, 4],
            "y_range": [-4, 16],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

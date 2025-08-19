"""
Simple parabola visualization with configurable horizontal line.

When executed via Nagini from JavaScript (sujets0-app-simple.js),
the Y_LABEL_FOR_HORIZONTAL_LINE variable is injected into this module's namespace
before execution, allowing dynamic configuration from the UI.

The value can be changed using the control panel in sujets0-simple.html.
"""

import numpy as np

# Try to get the value from the namespace injected by Nagini/Pyodide
# If not found (e.g., when running locally without Nagini), use default value
try:
    # When executed via Nagini, this value is injected into globals()
    # See sujets0-app-simple.js lines 208-210 for the injection code
    Y_LABEL_FOR_HORIZONTAL_LINE = globals()["Y_LABEL_FOR_HORIZONTAL_LINE"]
    print(f"✅ Using injected Y_LABEL_FOR_HORIZONTAL_LINE = {Y_LABEL_FOR_HORIZONTAL_LINE}")
except KeyError:
    # Default value when not running via Nagini or value not injected
    Y_LABEL_FOR_HORIZONTAL_LINE = 10
    print(f"⚠️ Using default Y_LABEL_FOR_HORIZONTAL_LINE = {Y_LABEL_FOR_HORIZONTAL_LINE}")

# Simple parabola visualization: y = x² with horizontal line (small 150x150)

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
        "y1": Y_LABEL_FOR_HORIZONTAL_LINE,
        "x2": 4,
        "y2": Y_LABEL_FOR_HORIZONTAL_LINE,
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
        "y": Y_LABEL_FOR_HORIZONTAL_LINE + 1.45,
        "latex": f"y={Y_LABEL_FOR_HORIZONTAL_LINE}",
        "width": 50,
        "height": 20,
        "class": "svg-latex text-secondary text-xs",
        "style": "background-color: rgba(255, 255, 255, 0.7); border-radius: var(--rounded-box, 0.5rem); padding: 1px 3px;",
    },
    # X axis label
    {
        "x": 4.25,
        "y": -1,
        "latex": "x",
        "width": 20,
        "height": 10,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label
    {
        "x": 0.5,
        "y": 16.5,
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
        "title": "spe_sujet1_auto_07_question_small.py",
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

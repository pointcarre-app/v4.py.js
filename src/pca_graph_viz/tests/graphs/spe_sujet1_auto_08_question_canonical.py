"""
Affine function visualization with configurable coefficients.

When executed via Nagini from JavaScript (sujets0-app-simple.js),
the A_FLOAT_FOR_AFFINE_LINE and B_FLOAT_FOR_AFFINE_LINE variables are
injected into this module's namespace before execution, allowing dynamic
configuration from the UI.

The values can be changed using the control panel in sujets0-simple.html.
"""

import numpy as np

# Affine function visualization: y = a x + b (canonical 340x340)

# Try to get the values from the namespace injected by Nagini/Pyodide
# If not found (e.g., when running locally without Nagini), use default values
try:
    # When executed via Nagini, these values are injected into globals()
    # See sujets0-app-simple.js lines 209-210 for the injection code
    A_FLOAT_FOR_AFFINE_LINE = globals()["A_FLOAT_FOR_AFFINE_LINE"]
    B_FLOAT_FOR_AFFINE_LINE = globals()["B_FLOAT_FOR_AFFINE_LINE"]
    print(
        f"✅ Using injected A_FLOAT_FOR_AFFINE_LINE = {A_FLOAT_FOR_AFFINE_LINE}, B_FLOAT_FOR_AFFINE_LINE = {B_FLOAT_FOR_AFFINE_LINE}"
    )
except KeyError:
    # Default values when not running via Nagini or values not injected
    A_FLOAT_FOR_AFFINE_LINE = 0.75  # Slope coefficient (float)
    B_FLOAT_FOR_AFFINE_LINE = 2.0  # Y-intercept (integer as float)
    print(
        f"⚠️ Using default A_FLOAT_FOR_AFFINE_LINE = {A_FLOAT_FOR_AFFINE_LINE}, B_FLOAT_FOR_AFFINE_LINE = {B_FLOAT_FOR_AFFINE_LINE}"
    )

# Generate line data over a symmetric range
x = np.linspace(-8, 8, 1000)
y = A_FLOAT_FOR_AFFINE_LINE * x + B_FLOAT_FOR_AFFINE_LINE

# Visual elements using CSS utility classes (see sujets0.html)
lines = [
    # X-axis
    {
        "type": "axis",
        "x1": -8,
        "y1": 0,
        "x2": 8,
        "y2": 0,
        "stroke-width": 1.5,
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -8,
        "x2": 0,
        "y2": 8,
        "stroke-width": 1.5,
        "class": "axis y-axis stroke-base-content",
    },
    # Affine line y = a x + b
    {
        "type": "curve",
        "id": "affine-line",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve stroke-primary",
    },
]

foreign_objects = [
    # # Equation label
    # {
    #     "x": 2.5,
    #     "y": a_python_float * 2.5 + b_python_float + 0.6,
    #     "latex": f"y = {a_python_float}\\,x + {b_python_float}",
    #     "width": 120,
    #     "height": 24,
    #     "class": "svg-latex text-secondary",
    # },
    # X axis label
    {
        "x": 5,
        "y": -0.5,
        "latex": "x",
        "width": 16,
        "height": 16,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label
    {
        "x": 0.3,
        "y": 5,
        "latex": "y",
        "width": 16,
        "height": 16,
        "class": "svg-latex fill-base-content",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "affine-line",
        "title": "spe_sujet1_auto_08_question_canonical.py",
        "description": "Visualization of an affine function with axes",
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
            "x_range": [-8, 8],
            "y_range": [-8, 8],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

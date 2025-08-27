"""
Simple parabola visualization with configurable horizontal line.

REQUIRED: The Y_LABEL_FOR_HORIZONTAL_LINE variable MUST be injected into this module's
namespace by Nagini from JavaScript before calling get_graph_dict().

The value can be changed using the control panel in sujets0-simple.html.
"""

import numpy as np

# NO DEFAULT VALUE - Must be injected from JavaScript via Nagini
# If this variable is not set, get_graph_dict() will raise an error
# Y_LABEL_FOR_HORIZONTAL_LINE = <must be injected>

# Simple parabola visualization: y = x² with horizontal line (small 150x150)

# Generate parabola: y = x²
x = np.linspace(-4, 4, 1000)
y = x**2


def get_graph_dict(y_horizontal=None):
    """Return the graph as a standardized dictionary.

    Args:
        y_horizontal: Y coordinate for horizontal line (optional, uses injected value if not provided)

    Raises:
        NameError: If Y_LABEL_FOR_HORIZONTAL_LINE is not injected into namespace
    """
    # Check if variable was injected from JavaScript
    if "Y_LABEL_FOR_HORIZONTAL_LINE" not in globals():
        raise NameError(
            "Y_LABEL_FOR_HORIZONTAL_LINE must be injected into module namespace by Nagini. "
            "Ensure graphConfig is properly passed from JavaScript."
        )

    # Use parameter if provided, otherwise use injected value
    y_value = y_horizontal if y_horizontal is not None else globals()["Y_LABEL_FOR_HORIZONTAL_LINE"]

    # Build visual elements with the configured value
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
        # Horizontal line with dynamic y value
        {
            "type": "line",
            "x1": -4,
            "y1": y_value,
            "x2": 4,
            "y2": y_value,
            "stroke-width": 1.5,
            # "stroke-dasharray": "5,5",
            "class": "line stroke-secondary",
        },
    ]

    foreign_objects = [
        # Parabola equation (commented out)
        # {
        #     "x": 3,
        #     "y": 1.5,
        #     "latex": "y = x^2",
        #     "width": 80,
        #     "height": 25,
        #     "class": "svg-latex text-primary",
        # },
        # Line equation with dynamic value
        {
            "x": 1.65,
            "y": y_value + 1.65,
            "latex": f"y={y_value}",
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

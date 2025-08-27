"""
Affine function visualization with configurable coefficients (small version).

The A_FLOAT_FOR_AFFINE_LINE and B_FLOAT_FOR_AFFINE_LINE values can be passed
as parameters to get_graph_dict() for dynamic configuration from the UI.

The values can be changed using the control panel in sujets0-simple.html.
"""

import numpy as np

# Affine function visualization: y = a x + b (small 150x150)

# Default configuration values
# These can be overridden by passing parameters to get_graph_dict()
A_FLOAT_FOR_AFFINE_LINE = 0.75  # Slope coefficient (float)
B_FLOAT_FOR_AFFINE_LINE = 2.0  # Y-intercept (integer as float)

# Match canonical range while keeping small display size
x_base = np.linspace(-10, 10, 1000)


def get_graph_dict(a_affine=None, b_affine=None):
    """Return the graph as a standardized dictionary.

    Args:
        a_affine: Slope coefficient for affine line (optional, defaults to module value)
        b_affine: Y-intercept for affine line (optional, defaults to module value)
    """
    # Use parameters if provided, otherwise use module-level values
    a_value = a_affine if a_affine is not None else A_FLOAT_FOR_AFFINE_LINE
    b_value = b_affine if b_affine is not None else B_FLOAT_FOR_AFFINE_LINE

    # Calculate the affine line with the configured values
    x = x_base
    y = a_value * x + b_value

    # Build subtle grid lines first so they render beneath axes and curve
    GRID_MIN, GRID_MAX = -10, 10
    grid_lines = []
    for i in range(GRID_MIN, GRID_MAX + 1):
        if i == 0:
            continue  # axes will be drawn separately at 0
        # vertical line x = i
        grid_lines.append(
            {
                "type": "line",
                "x1": float(i),
                "y1": float(GRID_MIN),
                "x2": float(i),
                "y2": float(GRID_MAX),
                "stroke-width": 0.5,
                "stroke-opacity": 0.35,
                "class": "grid-line stroke-base-content opacity-40",
            }
        )
        # horizontal line y = i
        grid_lines.append(
            {
                "type": "line",
                "x1": float(GRID_MIN),
                "y1": float(i),
                "x2": float(GRID_MAX),
                "y2": float(i),
                "stroke-width": 0.5,
                "stroke-opacity": 0.35,
                "class": "grid-line stroke-base-content opacity-40",
            }
        )

    lines = grid_lines + [
        # X-axis
        {
            "type": "axis",
            "x1": -10,
            "y1": 0,
            "x2": 10,
            "y2": 0,
            "stroke-width": 1,
            "class": "axis x-axis stroke-base-content",
        },
        # Y-axis
        {
            "type": "axis",
            "x1": 0,
            "y1": -10,
            "x2": 0,
            "y2": 10,
            "stroke-width": 1,
            "class": "axis y-axis stroke-base-content",
        },
        # Affine line with dynamic coefficients
        {
            "type": "curve",
            "id": "affine-line",
            "data": {"x": x.tolist(), "y": y.tolist()},
            "stroke-width": 1,
            "fill": "none",
            "class": "curve stroke-primary",
        },
    ]

    # Build tick labels for axes (exclude 0)
    TICK_MIN, TICK_MAX = -9, 9
    y_tick_labels = []
    for yi in range(TICK_MIN, TICK_MAX + 1):
        if yi == 0:
            continue
        y_tick_labels.append(
            {
                "x": -0.5,
                "y": float(yi),
                "latex": f"{yi}",
                "width": 16,
                "height": 12,
                "class": "svg-latex fill-base-content text-2xs",
            }
        )

    x_tick_labels = []
    for xi in range(TICK_MIN, TICK_MAX + 1):
        if xi == 0:
            continue
        x_tick_labels.append(
            {
                "x": float(xi),
                "y": -0.5,
                "latex": f"{xi}",
                "width": 16,
                "height": 12,
                "class": "svg-latex fill-base-content text-2xs",
            }
        )

    foreign_objects = (
        [
            # Function equation (commented out for now)
            # {
            #     "x": 2.0,
            #     "y": a_value * 2.0 + b_value + 0.5,
            #     "latex": f"y = {a_value}\\,x + {b_value}",
            #     "width": 100,
            #     "height": 20,
            #     "class": "svg-latex text-secondary",
            # },
            {
                "x": 10,
                "y": -0.75,
                "latex": "x",
                "width": 16,
                "height": 16,
                "class": "svg-latex fill-base-content text-xs",
            },
            # Y axis label
            {
                "x": 0.75,
                "y": 10,
                "latex": "y",
                "width": 16,
                "height": 16,
                "class": "svg-latex fill-base-content text-xs",
            },
        ]
        + y_tick_labels
        + x_tick_labels
    )

    return {
        "id": "affine-line-small",
        "title": "spe_sujet1_auto_08_question_small.py",
        "description": "Small visualization of an affine function",
        "svg": {
            "width": 300,
            "height": 300,
            "viewBox": "0 0 150 150",
            "class": "fill-base-100",
        },
        # Explicit domain prevents auto-padding that pushed grid lines beyond the plot box
        "domain": {
            "x_min": -10,
            "x_max": 10,
            "y_min": -10,
            "y_max": 10,
        },
        "settings": {
            "margin": {"top": 10, "right": 10, "bottom": 10, "left": 10},
            "show_axes": False,
            "show_grid": False,
            "x_range": [-10, 10],
            "y_range": [-10, 10],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

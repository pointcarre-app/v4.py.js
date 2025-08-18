import numpy as np

# Affine function visualization: y = a x + b (small 150x150)

A_FLOAT_FOR_AFFINE_LINE = 0.75
B_INT_FOR_AFFINE_LINE = 2

# Match canonical range while keeping small display size
x = np.linspace(-8, 8, 1000)
y = A_FLOAT_FOR_AFFINE_LINE * x + B_INT_FOR_AFFINE_LINE

# Build subtle grid lines first so they render beneath axes and curve
GRID_MIN, GRID_MAX = -8, 8
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
        "x1": -8,
        "y1": 0,
        "x2": 8,
        "y2": 0,
        "stroke-width": 1,
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -8,
        "x2": 0,
        "y2": 8,
        "stroke-width": 1,
        "class": "axis y-axis stroke-base-content",
    },
    # Affine line
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
TICK_MIN, TICK_MAX = -7, 7
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
        # {
        #     "x": 2.0,
        #     "y": a_python_float * 2.0 + b_python_float + 0.5,
        #     "latex": f"y = {a_python_float}\\,x + {b_python_float}",
        #     "width": 100,
        #     "height": 20,
        #     "class": "svg-latex text-secondary",
        # },
        {
            "x": 8,
            "y": -0.75,
            "latex": "x",
            "width": 16,
            "height": 16,
            "class": "svg-latex fill-base-content text-xs",
        },
        # Y axis label
        {
            "x": 0.75,
            "y": 8.25,
            "latex": "y",
            "width": 16,
            "height": 16,
            "class": "svg-latex fill-base-content text-xs",
        },
    ]
    + y_tick_labels
    + x_tick_labels
)


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
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
            "x_min": -8,
            "x_max": 8,
            "y_min": -8,
            "y_max": 8,
        },
        "settings": {
            "margin": {"top": 10, "right": 10, "bottom": 10, "left": 10},
            "show_axes": False,
            "show_grid": False,
            "x_range": [-8, 8],
            "y_range": [-8, 8],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

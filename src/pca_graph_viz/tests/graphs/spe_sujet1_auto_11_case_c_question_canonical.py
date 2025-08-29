import numpy as np

# Cubic function visualization: y = (x - root1)(x - root2)(x - root3) (canonical 340x340)
# Case C: root1=-4, root2=2, root3=4

ROOT1 = -4
ROOT2 = 2
ROOT3 = 4


X_MIN = -5
X_MAX = 6
# Y_MIN = -100
# Y_MAX = 75

# Generate cubic function data
x = np.linspace(-5, 7, 1000)
y = (x - ROOT1) * (x - ROOT2) * (x - ROOT3)

# Visual elements using CSS utility classes
lines = [
    # X-axis
    {
        "type": "axis",
        "x1": X_MIN,
        "y1": 0,
        "x2": X_MAX,
        "y2": 0,
        "stroke-width": 2,  # Bigger tick
        "class": "axis x-axis stroke-base-content",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -100,
        "x2": 0,
        "y2": 160,
        "stroke-width": 1.5,
        "class": "axis y-axis stroke-base-content",
    },
    # Cubic curve
    {
        "type": "curve",
        "id": "cubic",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve stroke-primary",
    },
]

# Mark the roots with small circles
root_markers = [
    # Root 1
    {
        "type": "circle",
        "cx": ROOT1,
        "cy": 0,
        "r": 3,
        "class": "fill-base-content stroke-base-content",
    },
    # Root 2
    {
        "type": "circle",
        "cx": ROOT2,
        "cy": 0,
        "r": 3,
        "class": "fill-base-content stroke-base-content",
    },
    # Root 3
    {
        "type": "circle",
        "cx": ROOT3,
        "cy": 0,
        "r": 3,
        "class": "fill-base-content stroke-base-content",
    },
]

lines.extend(root_markers)

foreign_objects = [
    # Function label with background
    {
        "x": 6.75,
        "y": 35,
        "latex": "C_f",
        "width": 20,
        "height": 25,
        "class": "svg-latex text-primary",
        "style": "background-color: rgba(255, 255, 255, 0.7); border-radius: var(--rounded-box, 0.5rem); padding: 2px 2px;",
    },
    # X axis label
    {
        "x": X_MAX,
        "y": -5,
        "latex": "x",
        "width": 20,
        "height": 20,
        "class": "svg-latex fill-base-content",
    },
    # Y axis label
    {
        "x": 0.5,
        "y": 160,
        "latex": "y",
        "width": 20,
        "height": 20,
        "class": "svg-latex fill-base-content",
    },
    # Root labels (positioned below dots with better control)
    {
        "x": ROOT1,  # Slightly offset for "-4"
        "y": -8,  # Higher position
        "latex": str(ROOT1),
        "width": 20,  # Smaller width for better control
        "height": 18,
        "class": "svg-latex fill-base-content text-xs bg-base-100 bg-opacity-60",
        "style": "overflow: visible; text-align: center;background: rgba(255, 255, 255, 0.7);",
    },
    {
        "x": ROOT2,  # Slightly offset for "2"
        "y": -8,  # Higher position
        "latex": str(ROOT2),
        "width": 20,  # Smaller width for better control
        "height": 18,
        "class": "svg-latex fill-base-content text-xs bg-opacity-60",
        "style": "overflow: visible; text-align: center;background: rgba(255, 255, 255, 0.7);",
    },
    {
        "x": ROOT3,  # Slightly offset for "5"
        "y": -8,  # Higher position
        "latex": str(ROOT3),
        "width": 20,  # Smaller width for better control
        "height": 18,
        "class": "svg-latex fill-base-content text-xs bg-opacity-60",
        "style": "overflow: visible; text-align: center;background: rgba(255, 255, 255, 0.7);",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "cubic-function-case-c",
        "title": "spe_sujet1_auto_11_case_c_question_canonical.py",
        "description": "Visualization of cubic function with three roots - Case C",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": 0,
            "show_axes": False,
            "show_grid": False,
            "x_range": [-5, 7],
            "y_range": [-100, 100],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

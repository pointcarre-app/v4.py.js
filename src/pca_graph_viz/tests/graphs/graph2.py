import numpy as np

# Graph 2: Sine function on [-π, π]
x = np.linspace(-np.pi, np.pi, 200)
y_sin = np.sin(x)  # y = sin(x)

# Colors will be handled by CSS classes
# No need for explicit color definitions when using DaisyUI theme classes

# All visual elements in lines array
lines = []

# Add vertical grid lines at π/4 intervals
for i in range(-4, 5):
    x_pos = i * np.pi / 4
    lines.append(
        {
            "type": "line",
            "x1": x_pos,
            "y1": -2,
            "x2": x_pos,
            "y2": 2,
            "stroke-width": 0.5,
            "stroke-opacity": 0.5,
            "class": "grid-line vertical stroke-base-200",
        }
    )

# Add horizontal grid lines at every 1 unit
for y_pos in [-2, -1, 1, 2]:
    lines.append(
        {
            "type": "line",
            "x1": -np.pi,
            "y1": y_pos,
            "x2": np.pi,
            "y2": y_pos,
            "stroke-width": 0.5,
            "stroke-opacity": 0.5,
            "class": "grid-line horizontal stroke-base-200",
        }
    )

# Add the sine curve
lines.append(
    {
        "type": "curve",
        "id": "sine",
        "data": {"x": x.tolist(), "y": y_sin.tolist()},
        "stroke-width": 2,
        "fill": "none",
        "class": "curve sine-curve stroke-primary",
    }
)

# Add axes (on top of grid)
lines.extend(
    [
        # X-axis
        {
            "type": "axis",
            "x1": -np.pi,
            "y1": 0,
            "x2": np.pi,
            "y2": 0,
            "stroke-width": 1.5,
            "class": "axis x-axis stroke-base-content",
        },
        # Y-axis
        {
            "type": "axis",
            "x1": 0,
            "y1": -2,
            "x2": 0,
            "y2": 2,
            "stroke-width": 1.5,
            "class": "axis y-axis stroke-base-content",
        },
    ]
)

# Create x-axis labels at every π/4
pi_labels = [
    (-np.pi, r"-\pi"),
    (-3 * np.pi / 4, r"-\frac{3\pi}{4}"),
    (-np.pi / 2, r"-\frac{\pi}{2}"),
    (-np.pi / 4, r"-\frac{\pi}{4}"),
    (np.pi / 4, r"\frac{\pi}{4}"),
    (np.pi / 2, r"\frac{\pi}{2}"),
    (3 * np.pi / 4, r"\frac{3\pi}{4}"),
    (np.pi, r"\pi"),
]

foreign_objects = []
for x_val, label in pi_labels:
    foreign_objects.append(
        {
            "x": x_val,
            "y": -0.15,  # Just below the x-axis
            "latex": label,
            "width": 40,
            "height": 20,
            "class": "svg-latex text-base-content",
        }
    )

# Add a label for the sine function
foreign_objects.append(
    {
        "x": np.pi / 2,
        "y": 0.8,
        "latex": r"y = \sin(x)",
        "width": 60,
        "height": 20,
        "class": "svg-latex text-primary",
    }
)


def get_graph_dict():
    """Return the graph as a standardized dictionary (V2 format - curves in lines)."""
    return {
        "id": "graph2",
        "title": "Sine Function",
        "description": "Shows y = sin(x) on the interval [-π, π]",
        "domain": {
            "x_min": -np.pi - 0.2,  # Add padding for arrow
            "x_max": np.pi + 0.2,  # Add padding for arrow
            "y_min": -2.2,  # Add padding for arrow
            "y_max": 2.2,  # Add padding for arrow
        },
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": 5,
            "show_axes": False,  # We define axes in lines
            "show_grid": False,  # We define grid lines manually
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Parametric Curve Plot
# Description: A curve in x-y plane traced by parametric equations. Direction of increasing parameter t shown with arrows. Several points labeled with their parameter values. Both x(t) and y(t) equations displayed.

# Generate parametric curve: x(t) = cos(t), y(t) = sin(2t) for t ∈ [0, 2π]
t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(2*t)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for curve

# All visual elements in lines array
lines = [
    # Parametric curve
    {
        "type": "curve",
        "id": "parametric_curve",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": line_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve parametric",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1.5,
        "y1": 0,
        "x2": 1.5,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -1.5,
        "x2": 0,
        "y2": 1.5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": 0.2,
        "y": 1.3,
        "latex": r"Parametric Curve",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1.2,
        "y": 1.1,
        "latex": r"x(t) = \cos(t)",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color,
    },
    {
        "x": -1.2,
        "y": 0.9,
        "latex": r"y(t) = \sin(2t)",
        "width": 100,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": line_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_parametric_curve_plot",
        "title": "Parametric Curve Plot",
        "description": "Parametric curve with x(t) = cos(t) and y(t) = sin(2t) for t ∈ [0, 2π]",
        "svg": {
            "width": 400,
            "height": 350,
            "viewBox": "0 0 400 350",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 20,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

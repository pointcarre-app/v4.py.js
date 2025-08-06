import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Second Degree Functions
# Subsection: Canonical Form Visualization
# Description: A parabola showing the transformation from y = x² to y = a(x-α)² + β. Use different colors or styles to show: the basic parabola y = x², horizontal shift by α, vertical stretch/compression by a, and vertical shift by β.

# Generate x values
x = np.linspace(-3, 4, 100)

# Basic parabola y = x²
y_basic = x**2

# Canonical form: y = a(x-α)² + β
# Let's use a = 0.5, α = 1, β = -2
a = 0.5
alpha = 1  # horizontal shift
beta = -2  # vertical shift
y_canonical = a * (x - alpha) ** 2 + beta

# Intermediate step: just shifted horizontally
y_shifted = (x - alpha) ** 2

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
basic_color = "#95a5a6"  # Grey for basic
shifted_color = "#3498db"  # Blue for shifted
canonical_color = "#e74c3c"  # Red for final

# All visual elements in lines array
lines = [
    # Basic parabola y = x² (dashed)
    {
        "type": "curve",
        "id": "basic_parabola",
        "data": {"x": x.tolist(), "y": y_basic.tolist()},
        "stroke": basic_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,3",
        "fill": "none",
        "class": "curve basic-parabola",
    },
    # Shifted parabola y = (x-1)² (dashed)
    {
        "type": "curve",
        "id": "shifted_parabola",
        "data": {"x": x.tolist(), "y": y_shifted.tolist()},
        "stroke": shifted_color,
        "stroke-width": 2,
        "stroke-dasharray": "8,4",
        "fill": "none",
        "class": "curve shifted-parabola",
    },
    # Canonical form y = 0.5(x-1)² - 2 (solid)
    {
        "type": "curve",
        "id": "canonical_parabola",
        "data": {"x": x.tolist(), "y": y_canonical.tolist()},
        "stroke": canonical_color,
        "stroke-width": 3,
        "fill": "none",
        "class": "curve canonical-parabola",
    },
    # Vertex point of canonical form
    {
        "type": "circle",
        "cx": alpha,
        "cy": beta,
        "r": 0.08,
        "fill": canonical_color,
        "class": "vertex-point",
    },
    # Vertical line through vertex (dashed)
    {
        "type": "line",
        "x1": alpha,
        "y1": -3,
        "x2": alpha,
        "y2": 5,
        "stroke": "#999999",
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "vertex-line",
    },
    # Horizontal line through vertex (dashed)
    {
        "type": "line",
        "x1": -3,
        "y1": beta,
        "x2": 4,
        "y2": beta,
        "stroke": "#999999",
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "vertex-horizontal",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -3,
        "y1": 0,
        "x2": 4,
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
        "y1": -3,
        "x2": 0,
        "y2": 5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": -2.5,
        "y": 4,
        "latex": r"y = x^2",
        "width": 60,
        "height": 20,
        "bg_color": "transparent",
        "text_color": basic_color,
    },
    {
        "x": 2.5,
        "y": 3,
        "latex": r"y = (x-1)^2",
        "width": 80,
        "height": 20,
        "bg_color": "transparent",
        "text_color": shifted_color,
    },
    {
        "x": 1.5,
        "y": -0.5,
        "latex": r"y = \frac{1}{2}(x-1)^2 - 2",
        "width": 120,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": canonical_color,
    },
    {
        "x": alpha + 0.2,
        "y": beta - 0.3,
        "latex": r"(1, -2)",
        "width": 50,
        "height": 20,
        "bg_color": "transparent",
        "text_color": canonical_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_second_degree_functions_canonical_form_visualization",
        "title": "Canonical Form Visualization",
        "description": "Transformation from y = x² to canonical form y = a(x-α)² + β",
        "svg": {
            "width": 340,
            "height": 340,
            "viewBox": "0 0 340 340",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 5,
            "show_axes": False,
            "show_grid": True,
            "grid_color": grid_color,
            "axes_color": "#333333",
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

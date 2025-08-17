import numpy as np

# Graph: [sujets0][spé][sujet-1][automatismes][question-7]
# Question: On a représenté ci-contre la parabole d'équation y=x².
# On note (7) l'inéquation, sur ℝ, x² ≥ 10.
# L'inéquation (7) est équivalente à: x ≤ -√10 ou x ≥ √10

# Generate parabola: y = x²
x = np.linspace(-5, 5, 200)
y = x**2

# Key points for the inequality x² ≥ 10
# Cast to native float to avoid NumPy scalar types in the exported dict
sqrt_10 = float(np.sqrt(10))  # ≈ 3.162
x_left = -sqrt_10
x_right = sqrt_10
y_level = 10

# Generate regions for x² ≥ 10 (x ≤ -√10 or x ≥ √10)
x_left_region = np.linspace(-5, -sqrt_10, 50)
y_left_region = x_left_region**2

x_right_region = np.linspace(sqrt_10, 5, 50)
y_right_region = x_right_region**2

# Use nice hex colors
bg_color = "#f8f9fb"  # Very light background
grid_color = "#e0e4eb"  # Light grey for grid
parabola_color = "#4a90e2"  # Blue for parabola
solution_color = "#ff6b6b"  # Red for solution regions
line_color = "#2ecc71"  # Green for y = 10 line
point_color = "#e74c3c"  # Red for critical points

# All visual elements in lines array
lines = [
    # Grid lines (vertical)
    *[
        {
            "type": "line",
            "x1": i,
            "y1": -2,
            "x2": i,
            "y2": 26,
            "stroke": grid_color,
            "stroke-width": 0.5,
            "stroke-opacity": 0.5,
            "class": "grid-line",
        }
        for i in range(-5, 6)
    ],
    # Grid lines (horizontal)
    *[
        {
            "type": "line",
            "x1": -5,
            "y1": j,
            "x2": 5,
            "y2": j,
            "stroke": grid_color,
            "stroke-width": 0.5,
            "stroke-opacity": 0.5,
            "class": "grid-line",
        }
        for j in range(0, 26, 2)
    ],
    # X-axis
    {
        "type": "axis",
        "x1": -5,
        "y1": 0,
        "x2": 5,
        "y2": 0,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "stroke-opacity": 0.8,
        "class": "axis x-axis",
    },
    # Y-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": -2,
        "x2": 0,
        "y2": 26,
        "stroke": "#333333",
        "stroke-width": 1.5,
        "stroke-opacity": 0.8,
        "class": "axis y-axis",
    },
    # Parabola curve (main)
    {
        "type": "curve",
        "id": "parabola",
        "data": {"x": x.tolist(), "y": y.tolist()},
        "stroke": parabola_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve parabola",
    },
    # Highlight solution regions (left side: x ≤ -√10)
    {
        "type": "curve",
        "id": "solution-left",
        "data": {"x": x_left_region.tolist(), "y": y_left_region.tolist()},
        "stroke": solution_color,
        "stroke-width": 4,
        "fill": "none",
        "stroke-opacity": 0.8,
        "class": "curve solution",
    },
    # Highlight solution regions (right side: x ≥ √10)
    {
        "type": "curve",
        "id": "solution-right",
        "data": {"x": x_right_region.tolist(), "y": y_right_region.tolist()},
        "stroke": solution_color,
        "stroke-width": 4,
        "fill": "none",
        "stroke-opacity": 0.8,
        "class": "curve solution",
    },
    # Horizontal line y = 10
    {
        "type": "line",
        "x1": -5,
        "y1": y_level,
        "x2": 5,
        "y2": y_level,
        "stroke": line_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,5",
        "stroke-opacity": 0.7,
        "class": "threshold-line",
    },
    # Vertical lines at x = -√10 and x = √10 (dashed)
    {
        "type": "line",
        "x1": -sqrt_10,
        "y1": -2,
        "y2": 26,
        "x2": -sqrt_10,
        "stroke": point_color,
        "stroke-width": 1.5,
        "stroke-dasharray": "3,3",
        "stroke-opacity": 0.6,
        "class": "boundary-line",
    },
    {
        "type": "line",
        "x1": sqrt_10,
        "y1": -2,
        "y2": 26,
        "x2": sqrt_10,
        "stroke": point_color,
        "stroke-width": 1.5,
        "stroke-dasharray": "3,3",
        "stroke-opacity": 0.6,
        "class": "boundary-line",
    },
    # Points at (-√10, 10) and (√10, 10)
    {
        "type": "circle",
        "cx": -sqrt_10,
        "cy": 10,
        "r": 4,
        "fill": point_color,
        "stroke": "white",
        "stroke-width": 2,
        "class": "critical-point",
    },
    {
        "type": "circle",
        "cx": sqrt_10,
        "cy": 10,
        "r": 4,
        "fill": point_color,
        "stroke": "white",
        "stroke-width": 2,
        "class": "critical-point",
    },
]

foreign_objects = [
    # Main equation
    {
        "x": 0.5,
        "y": 24,
        "latex": r"y = x^2",
        "width": 70,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.95)",
        "text_color": parabola_color,
    },
    # Inequality
    {
        "x": 2.5,
        "y": 20,
        "latex": r"x^2 \geq 10",
        "width": 80,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.95)",
        "text_color": "#333333",
    },
    # y = 10 label
    {
        "x": 4.2,
        "y": 10.2,
        "latex": r"y = 10",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": line_color,
    },
    # Left critical point
    {
        "x": -sqrt_10 - 0.7,
        "y": 10.5,
        "latex": r"(-\sqrt{10}, 10)",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": point_color,
    },
    # Right critical point
    {
        "x": sqrt_10 + 0.1,
        "y": 10.5,
        "latex": r"(\sqrt{10}, 10)",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": point_color,
    },
    # Solution label (left)
    {
        "x": -4.5,
        "y": 18,
        "latex": r"x \leq -\sqrt{10}",
        "width": 100,
        "height": 25,
        "bg_color": "rgba(255, 235, 235, 0.95)",
        "text_color": solution_color,
    },
    # Solution label (right)
    {
        "x": 3.5,
        "y": 14,
        "latex": r"x \geq \sqrt{10}",
        "width": 90,
        "height": 25,
        "bg_color": "rgba(255, 235, 235, 0.95)",
        "text_color": solution_color,
    },
    # Title/Question reference
    {
        "x": -4.8,
        "y": 0.5,
        "latex": r"\text{Question 7}",
        "width": 90,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "[sujets0][spé][sujet-1][automatismes][question-7]",
        "title": "Inéquation x² ≥ 10 sur la parabole y = x²",
        "description": "Visualisation de l'inéquation x² ≥ 10, montrant que la solution est x ≤ -√10 ou x ≥ √10",
        "svg": {
            "width": 400,
            "height": 400,
            "viewBox": "0 0 400 400",
            "style": {"background-color": bg_color},
        },
        "settings": {
            "margin": 20,
            "show_axes": False,
            "show_grid": False,  # We're drawing our own grid
            "grid_color": grid_color,
            "axes_color": "#333333",
            "x_range": [-5, 5],
            "y_range": [-2, 26],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }

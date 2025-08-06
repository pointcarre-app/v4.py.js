import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Coordinate Geometry
# Subsection: Circle Equation Visualization
# Description: A circle on coordinate axes with center (a,b) marked, radius r shown, equation (x-a)² + (y-b)² = r² displayed. Several points on the circle to verify the equation. Can include tangent lines.

# Circle parameters
center = (1, 1)  # (a, b)
radius = 1.5

# Parametric circle points
theta = np.linspace(0, 2 * np.pi, 200)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)

# Cardinal points on the circle for verification
cardinal_points = [
    (center[0] + radius, center[1]),  # Right
    (center[0] - radius, center[1]),  # Left
    (center[0], center[1] + radius),  # Top
    (center[0], center[1] - radius),  # Bottom
]

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
circle_color = "#6b46c1"  # Purple
aux_color = "#ec4899"  # Pink for radius

# All visual elements in lines array
lines = [
    # Circle curve
    {
        "type": "curve",
        "id": "circle",
        "data": {"x": x_circle.tolist(), "y": y_circle.tolist()},
        "stroke": circle_color,
        "stroke-width": 2,
        "fill": "none",
        "class": "curve circle-curve",
    },
    # Radius line to the rightmost point (for visualising r)
    {
        "type": "line",
        "x1": center[0],
        "y1": center[1],
        "x2": center[0] + radius,
        "y2": center[1],
        "stroke": aux_color,
        "stroke-width": 2,
        "class": "radius-line",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -1,
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
        "y1": -1,
        "x2": 0,
        "y2": 4,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
    # Cardinal points on circle
    *[
        {
            "type": "circle",
            "cx": float(pt[0]),
            "cy": float(pt[1]),
            "r": 3,
            "fill": circle_color,
            "stroke": "#4c1d95",
            "stroke-width": 1.5,
            "class": "circle-point",
        }
        for pt in cardinal_points
    ],
]

foreign_objects = [
    # Equation label
    {
        "x": -0.5,
        "y": 2.8,
        "latex": rf"(x-{center[0]})^2 + (y-{center[1]})^2 = {radius}^2",
        "width": 160,
        "height": 25,
        "bg_color": "rgba(107, 70, 193, 0.1)",
        "text_color": circle_color,
        "border_radius": "0.25rem",
    },
    # Center label
    {
        "x": center[0],
        "y": center[1] - 0.15,
        "latex": "C(1,1)",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(236,72,153,0.1)",
        "text_color": aux_color,
        "border_radius": "0.25rem",
        "show_point": True,
    },
    # Radius label near middle of radius line
    {
        "x": center[0] + radius / 2,
        "y": center[1] + 0.12,
        "latex": "r",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": aux_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_coordinate_geometry_circle_equation_visualization",
        "title": "Circle Equation Visualization",
        "description": "Placeholder for circle equation visualization visualization",
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

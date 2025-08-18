import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Coordinate Geometry
# Subsection: Distance Formula Illustration
# Description: Two points in coordinate plane connected by a line segment. Right triangle formed using horizontal and vertical distances. Pythagorean theorem visualization: d² = (x₂-x₁)² + (y₂-y₁)².

# Two points to connect
P1 = (1, 2)  # Point 1
P2 = (4, 6)  # Point 2

# Calculate distance
dx = P2[0] - P1[0]
dy = P2[1] - P1[1]
distance = float(np.sqrt(dx**2 + dy**2))

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for main line
triangle_color = "#22c55e"  # Green for right triangle
point_color = "#ef4444"  # Red for points

# All visual elements in lines array
lines = [
    # Right triangle - horizontal leg
    {
        "type": "line",
        "x1": P1[0],
        "y1": P1[1],
        "x2": P2[0],
        "y2": P1[1],
        "stroke": triangle_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,3",
        "class": "triangle-horizontal",
    },
    # Right triangle - vertical leg
    {
        "type": "line",
        "x1": P2[0],
        "y1": P1[1],
        "x2": P2[0],
        "y2": P2[1],
        "stroke": triangle_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,3",
        "class": "triangle-vertical",
    },
    # Distance line (hypotenuse)
    {
        "type": "line",
        "x1": P1[0],
        "y1": P1[1],
        "x2": P2[0],
        "y2": P2[1],
        "stroke": line_color,
        "stroke-width": 3,
        "class": "distance-line",
    },
    # Right angle indicator
    {
        "type": "path",
        "d": f"M {P2[0] - 0.3} {P1[1]} L {P2[0] - 0.3} {P1[1] + 0.3} L {P2[0]} {P1[1] + 0.3}",
        "stroke": triangle_color,
        "stroke-width": 1.5,
        "fill": "none",
        "class": "right-angle",
    },
    # X-axis
    {
        "type": "axis",
        "x1": 0,
        "y1": 0,
        "x2": 5,
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
        "y1": 0,
        "x2": 0,
        "y2": 7,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
    # Point 1
    {
        "type": "circle",
        "cx": float(P1[0]),
        "cy": float(P1[1]),
        "r": 4,
        "fill": point_color,
        "stroke": "#dc2626",
        "stroke-width": 2,
        "class": "point-1",
    },
    # Point 2
    {
        "type": "circle",
        "cx": float(P2[0]),
        "cy": float(P2[1]),
        "r": 4,
        "fill": point_color,
        "stroke": "#dc2626",
        "stroke-width": 2,
        "class": "point-2",
    },
]

foreign_objects = [
    # Distance formula
    {
        "x": 0.5,
        "y": 6.5,
        "latex": r"d^2 = (x_2-x_1)^2 + (y_2-y_1)^2",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(107, 70, 193, 0.1)",
        "text_color": line_color,
        "border_radius": "0.25rem",
    },
    # Point 1 label
    {
        "x": P1[0] - 0.3,
        "y": P1[1] - 0.4,
        "latex": f"P_1({P1[0]},{P1[1]})",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(239, 68, 68, 0.1)",
        "text_color": point_color,
        "border_radius": "0.25rem",
    },
    # Point 2 label
    {
        "x": P2[0] + 0.1,
        "y": P2[1],
        "latex": f"P_2({P2[0]},{P2[1]})",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(239, 68, 68, 0.1)",
        "text_color": point_color,
        "border_radius": "0.25rem",
    },
    # Horizontal distance
    {
        "x": (P1[0] + P2[0]) / 2 - 0.3,
        "y": P1[1] - 0.3,
        "latex": f"{dx}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(34, 197, 94, 0.1)",
        "text_color": triangle_color,
    },
    # Vertical distance
    {
        "x": P2[0] + 0.2,
        "y": (P1[1] + P2[1]) / 2 - 0.1,
        "latex": f"{dy}",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(34, 197, 94, 0.1)",
        "text_color": triangle_color,
    },
    # Distance value
    {
        "x": (P1[0] + P2[0]) / 2 - 0.5,
        "y": (P1[1] + P2[1]) / 2 + 0.2,
        "latex": f"d = {distance:.1f}",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(107, 70, 193, 0.9)",
        "text_color": "white",
        "border_radius": "0.25rem",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_coordinate_geometry_distance_formula_illustration",
        "title": "Distance Formula Illustration",
        "description": "Distance formula visualization with Pythagorean theorem",
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

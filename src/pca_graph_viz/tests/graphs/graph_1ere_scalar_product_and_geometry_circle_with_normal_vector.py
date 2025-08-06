import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Scalar Product and Geometry
# Subsection: Circle with Normal Vector
# Description: A circle with center and radius marked. A line tangent to the circle at a point. A vector perpendicular to the tangent (normal vector) pointing outward from the circle. Shows relationship between tangent and normal.

# Circle parameters
center_x, center_y = 0, 0
radius = 1.5

# Generate circle
theta = np.linspace(0, 2 * np.pi, 100)
circle_x = center_x + radius * np.cos(theta)
circle_y = center_y + radius * np.sin(theta)

# Tangent point at 45 degrees
tangent_angle = np.pi / 4
tangent_x = center_x + radius * np.cos(tangent_angle)
tangent_y = center_y + radius * np.sin(tangent_angle)

# Tangent line (perpendicular to radius at tangent point)
tangent_slope = -np.cos(tangent_angle) / np.sin(tangent_angle)
t_range = np.linspace(-1, 1, 2)
tangent_line_x = tangent_x + t_range
tangent_line_y = tangent_y + tangent_slope * t_range

# Normal vector (from center through tangent point and beyond)
normal_end_x = tangent_x + 0.8 * np.cos(tangent_angle)
normal_end_y = tangent_y + 0.8 * np.sin(tangent_angle)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
circle_color = "#4169e1"  # Royal blue
tangent_color = "#ff6b6b"  # Coral red
normal_color = "#32cd32"  # Lime green

# All visual elements in lines array
lines = [
    # Circle
    {
        "type": "curve",
        "id": "circle",
        "data": {"x": circle_x.tolist(), "y": circle_y.tolist()},
        "stroke": circle_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve circle",
    },
    # Radius to tangent point (dashed)
    {
        "type": "line",
        "x1": center_x,
        "y1": center_y,
        "x2": tangent_x,
        "y2": tangent_y,
        "stroke": "#999999",
        "stroke-width": 1,
        "stroke-dasharray": "5,3",
        "class": "radius-line",
    },
    # Tangent line
    {
        "type": "curve",
        "id": "tangent",
        "data": {"x": tangent_line_x.tolist(), "y": tangent_line_y.tolist()},
        "stroke": tangent_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "tangent-line",
    },
    # Normal vector (arrow)
    {
        "type": "line",
        "x1": tangent_x,
        "y1": tangent_y,
        "x2": normal_end_x,
        "y2": normal_end_y,
        "stroke": normal_color,
        "stroke-width": 3,
        "marker-end": "url(#arrowhead)",
        "class": "normal-vector",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -3,
        "y1": 0,
        "x2": 3,
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
        "y2": 3,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
    # Right angle indicator at tangent point
    {
        "type": "path",
        "d": f"M {tangent_x - 0.15} {tangent_y} L {tangent_x - 0.15} {tangent_y - 0.15} L {tangent_x} {tangent_y - 0.15}",
        "stroke": "#666666",
        "stroke-width": 1.5,
        "fill": "none",
        "class": "right-angle",
    },
    # Center point
    {
        "type": "circle",
        "cx": center_x,
        "cy": center_y,
        "r": 0.05,
        "fill": "#333333",
        "class": "center-point",
    },
    # Tangent point
    {
        "type": "circle",
        "cx": tangent_x,
        "cy": tangent_y,
        "r": 0.05,
        "fill": "#333333",
        "class": "tangent-point",
    },
]

foreign_objects = [
    {
        "x": 0.8,
        "y": 0.4,
        "latex": r"\vec{n}",
        "width": 30,
        "height": 20,
        "bg_color": "transparent",
        "text_color": normal_color,
    },
    {
        "x": -0.5,
        "y": 1.8,
        "latex": r"\text{tangent}",
        "width": 60,
        "height": 20,
        "bg_color": "transparent",
        "text_color": tangent_color,
    },
    {
        "x": 0.2,
        "y": -0.8,
        "latex": r"r",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#999999",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_scalar_product_and_geometry_circle_with_normal_vector",
        "title": "Circle with Normal Vector",
        "description": "Circle with tangent line and normal vector showing perpendicular relationship",
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

import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Scalar Product and Geometry
# Subsection: Vector Scalar Product Visualization
# Description: Two vectors from common origin with angle θ between them. Arc showing the angle, labels for vector magnitudes |u| and |v|. Formula u·v = |u||v|cos(θ) displayed. Projection of one vector onto another shown with dashed line.

# Vector definitions with angle
angle_u = 0  # Vector u along positive x-axis
angle_v = np.pi / 3  # Vector v at 60 degrees
magnitude_u = 2.5
magnitude_v = 2.0

# Vector coordinates
u_x = magnitude_u * np.cos(angle_u)
u_y = magnitude_u * np.sin(angle_u)
v_x = magnitude_v * np.cos(angle_v)
v_y = magnitude_v * np.sin(angle_v)

# Projection of v onto u
projection_length = magnitude_v * np.cos(angle_v - angle_u)
proj_x = projection_length * np.cos(angle_u)
proj_y = projection_length * np.sin(angle_u)

# Arc for angle
arc_radius = 0.6
arc_angles = np.linspace(angle_u, angle_v, 30)
arc_x = arc_radius * np.cos(arc_angles)
arc_y = arc_radius * np.sin(arc_angles)

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
vector_u_color = "#e74c3c"  # Red
vector_v_color = "#3498db"  # Blue
projection_color = "#9b59b6"  # Purple

# All visual elements in lines array
lines = [
    # Vector u
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": u_x,
        "y2": u_y,
        "stroke": vector_u_color,
        "stroke-width": 3,
        "marker-end": "url(#arrowhead)",
        "class": "vector-u",
    },
    # Vector v
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": v_x,
        "y2": v_y,
        "stroke": vector_v_color,
        "stroke-width": 3,
        "marker-end": "url(#arrowhead)",
        "class": "vector-v",
    },
    # Projection line (dashed from v to projection point)
    {
        "type": "line",
        "x1": v_x,
        "y1": v_y,
        "x2": proj_x,
        "y2": proj_y,
        "stroke": projection_color,
        "stroke-width": 2,
        "stroke-dasharray": "5,3",
        "class": "projection-line",
    },
    # Projection vector
    {
        "type": "line",
        "x1": 0,
        "y1": 0,
        "x2": proj_x,
        "y2": proj_y,
        "stroke": projection_color,
        "stroke-width": 2.5,
        "stroke-opacity": 0.7,
        "class": "projection-vector",
    },
    # Right angle at projection
    {
        "type": "path",
        "d": f"M {proj_x - 0.15} {proj_y} L {proj_x - 0.15} {proj_y + 0.15} L {proj_x} {proj_y + 0.15}",
        "stroke": "#666666",
        "stroke-width": 1.5,
        "fill": "none",
        "class": "right-angle",
    },
    # Angle arc
    {
        "type": "curve",
        "id": "angle-arc",
        "data": {"x": arc_x.tolist(), "y": arc_y.tolist()},
        "stroke": "#27ae60",
        "stroke-width": 2,
        "fill": "none",
        "class": "angle-arc",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -0.5,
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
        "y1": -0.5,
        "x2": 0,
        "y2": 2.5,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
    # Origin point
    {
        "type": "circle",
        "cx": 0,
        "cy": 0,
        "r": 0.05,
        "fill": "#333333",
        "class": "origin-point",
    },
    # Projection point
    {
        "type": "circle",
        "cx": proj_x,
        "cy": proj_y,
        "r": 0.04,
        "fill": projection_color,
        "class": "projection-point",
    },
]

foreign_objects = [
    {
        "x": u_x - 0.2,
        "y": u_y - 0.3,
        "latex": r"\vec{u}",
        "width": 30,
        "height": 20,
        "bg_color": "transparent",
        "text_color": vector_u_color,
    },
    {
        "x": v_x + 0.1,
        "y": v_y - 0.1,
        "latex": r"\vec{v}",
        "width": 30,
        "height": 20,
        "bg_color": "transparent",
        "text_color": vector_v_color,
    },
    {
        "x": 0.3,
        "y": 0.2,
        "latex": r"\theta",
        "width": 25,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#27ae60",
    },
    {
        "x": 0.5,
        "y": -0.8,
        "latex": r"\vec{u} \cdot \vec{v} = |\vec{u}||\vec{v}|\cos(\theta)",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#333333",
    },
    {
        "x": proj_x - 0.4,
        "y": proj_y + 0.3,
        "latex": r"\text{proj}_{\vec{u}}\vec{v}",
        "width": 60,
        "height": 20,
        "bg_color": "transparent",
        "text_color": projection_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_scalar_product_and_geometry_vector_scalar_product_visualization",
        "title": "Vector Scalar Product Visualization",
        "description": "Visualization of scalar product with angle and projection",
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

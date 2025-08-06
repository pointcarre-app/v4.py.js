import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Scalar Product and Geometry
# Subsection: Orthogonal Vectors Diagram
# Description: Two perpendicular vectors forming a 90° angle. Right angle symbol at intersection. Emphasize that scalar product equals zero. Can include coordinate representation showing x₁x₂ + y₁y₂ = 0.

# Vector definitions
# Vector u = (3, 2)
u_x, u_y = 3, 2
# Vector v = (-2, 3) - perpendicular to u
v_x, v_y = -2, 3

# Scale vectors for better visualization
scale = 0.6
u_x, u_y = u_x * scale, u_y * scale
v_x, v_y = v_x * scale, v_y * scale

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
vector_u_color = "#ff4757"  # Red
vector_v_color = "#3742fa"  # Blue

# Right angle square size
square_size = 0.3

# Calculate right angle square vertices
# Normalize vectors for square calculation
u_norm = np.sqrt(u_x**2 + u_y**2)
v_norm = np.sqrt(v_x**2 + v_y**2)
u_unit = (u_x / u_norm, u_y / u_norm)
v_unit = (v_x / v_norm, v_y / v_norm)

# Square corners
square_path = (
    f"M {square_size * u_unit[0]} {square_size * u_unit[1]} "
    + f"L {square_size * (u_unit[0] + v_unit[0])} {square_size * (u_unit[1] + v_unit[1])} "
    + f"L {square_size * v_unit[0]} {square_size * v_unit[1]}"
)

# All visual elements in lines array
lines = [
    # Vector u (arrow)
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
    # Vector v (arrow)
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
    # Right angle indicator
    {
        "type": "path",
        "d": square_path,
        "stroke": "#666666",
        "stroke-width": 2,
        "fill": "none",
        "class": "right-angle",
    },
    # Dotted lines showing components
    {
        "type": "line",
        "x1": u_x,
        "y1": 0,
        "x2": u_x,
        "y2": u_y,
        "stroke": vector_u_color,
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "u-component-y",
    },
    {
        "type": "line",
        "x1": 0,
        "y1": u_y,
        "x2": u_x,
        "y2": u_y,
        "stroke": vector_u_color,
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "u-component-x",
    },
    {
        "type": "line",
        "x1": v_x,
        "y1": 0,
        "x2": v_x,
        "y2": v_y,
        "stroke": vector_v_color,
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "v-component-y",
    },
    {
        "type": "line",
        "x1": 0,
        "y1": v_y,
        "x2": v_x,
        "y2": v_y,
        "stroke": vector_v_color,
        "stroke-width": 1,
        "stroke-dasharray": "3,2",
        "stroke-opacity": 0.5,
        "class": "v-component-x",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2.5,
        "y1": 0,
        "x2": 2.5,
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
        "y1": -2.5,
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
]

foreign_objects = [
    {
        "x": u_x + 0.2,
        "y": u_y - 0.1,
        "latex": r"\vec{u} = (3, 2)",
        "width": 80,
        "height": 20,
        "bg_color": "transparent",
        "text_color": vector_u_color,
    },
    {
        "x": v_x - 0.8,
        "y": v_y + 0.1,
        "latex": r"\vec{v} = (-2, 3)",
        "width": 80,
        "height": 20,
        "bg_color": "transparent",
        "text_color": vector_v_color,
    },
    {
        "x": -1.5,
        "y": -2,
        "latex": r"\vec{u} \cdot \vec{v} = 3(-2) + 2(3) = 0",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#333333",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_scalar_product_and_geometry_orthogonal_vectors_diagram",
        "title": "Orthogonal Vectors Diagram",
        "description": "Two perpendicular vectors showing scalar product equals zero",
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

import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: 3D Coordinate System Preview
# Description: Three perpendicular axes (x, y, z) with a point (x₀, y₀, z₀) plotted. Projection lines to each coordinate plane. Right-hand rule for orientation. Basic for vector work in space.

# Generate 3D coordinate system visualization (2D projection)
# We'll show the three axes and a point with projection lines

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
x_color = "#ec3059"  # Red for x-axis
y_color = "#309110"  # Green for y-axis
z_color = "#0085c0"  # Blue for z-axis
point_color = "#6b46c1"  # Purple for point

# All visual elements in lines array
lines = [
    # X-axis (red)
    {
        "type": "axis",
        "x1": -2,
        "y1": 0,
        "x2": 2,
        "y2": 0,
        "stroke": x_color,
        "stroke-width": 2,
        "stroke-opacity": 0.8,
        "class": "axis x-axis-3d",
    },
    # Y-axis (green) - projected as diagonal
    {
        "type": "axis",
        "x1": 0,
        "y1": -1.5,
        "x2": 1.5,
        "y2": 0,
        "stroke": y_color,
        "stroke-width": 2,
        "stroke-opacity": 0.8,
        "class": "axis y-axis-3d",
    },
    # Z-axis (blue) - projected as vertical
    {
        "type": "axis",
        "x1": 0,
        "y1": -1.5,
        "x2": 0,
        "y2": 1.5,
        "stroke": z_color,
        "stroke-width": 2,
        "stroke-opacity": 0.8,
        "class": "axis z-axis-3d",
    },
]

foreign_objects = [
    {
        "x": 0.2,
        "y": 1.3,
        "latex": r"3D Coordinate System",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": 2.1,
        "y": 0.1,
        "latex": r"x",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": x_color,
    },
    {
        "x": 1.6,
        "y": -0.1,
        "latex": r"y",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": y_color,
    },
    {
        "x": 0.1,
        "y": 1.6,
        "latex": r"z",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": z_color,
    },
    {
        "x": 1.6,
        "y": 0.6,
        "latex": r"P(1,1,1)",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": point_color,
    },
    {
        "x": 0.1,
        "y": 0.1,
        "latex": r"O",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_3d_coordinate_system_preview",
        "title": "3D Coordinate System Preview",
        "description": "Three-dimensional coordinate system showing x, y, z axes and point P(1,1,1) with projection lines",
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

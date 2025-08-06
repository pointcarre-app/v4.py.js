import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Coordinate Geometry
# Subsection: Line in Coordinate System
# Description: A straight line on x-y axes with: two points clearly marked, slope triangle showing rise over run, y-intercept labeled, equation in form y = mx + b or ax + by + c = 0.

# Line equation: y = 2x + 1 (slope m = 2, y-intercept b = 1)
m = 2  # slope
b = 1  # y-intercept

# Generate line points
x = np.linspace(-3, 2, 100)
y_line = m * x + b

# Two specific points on the line
P1 = (-1, -1)  # When x = -1, y = 2(-1) + 1 = -1
P2 = (1, 3)    # When x = 1, y = 2(1) + 1 = 3

# Slope triangle vertices (showing rise over run)
triangle_x = 0  # Start of triangle
triangle_y = m * triangle_x + b  # y value at triangle_x
run = 1  # Horizontal distance
rise = m * run  # Vertical distance = slope * run

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
line_color = "#6b46c1"  # Purple for main line
point_color = "#ec4899"  # Pink for points
triangle_color = "#10b981"  # Green for slope triangle
intercept_color = "#f59e0b"  # Orange for y-intercept

# All visual elements in lines array
lines = [
    # Main line
    {
        "type": "curve",
        "id": "main_line",
        "data": {"x": x.tolist(), "y": y_line.tolist()},
        "stroke": line_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "main-line",
    },
    # Slope triangle - horizontal leg (run)
    {
        "type": "line",
        "x1": triangle_x,
        "y1": triangle_y,
        "x2": triangle_x + run,
        "y2": triangle_y,
        "stroke": triangle_color,
        "stroke-width": 2,
        "stroke-dasharray": "4,2",
        "class": "slope-run",
    },
    # Slope triangle - vertical leg (rise)
    {
        "type": "line",
        "x1": triangle_x + run,
        "y1": triangle_y,
        "x2": triangle_x + run,
        "y2": triangle_y + rise,
        "stroke": triangle_color,
        "stroke-width": 2,
        "stroke-dasharray": "4,2",
        "class": "slope-rise",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -3,
        "y1": 0,
        "x2": 2,
        "y2": 0,
        "stroke": "#666666",
        "stroke-width": 1.5,
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
        "stroke-width": 1.5,
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
        "stroke": "#be185d",
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
        "stroke": "#be185d",
        "stroke-width": 2,
        "class": "point-2",
    },
    # Y-intercept point
    {
        "type": "circle",
        "cx": 0,
        "cy": float(b),
        "r": 5,
        "fill": intercept_color,
        "stroke": "#d97706",
        "stroke-width": 2,
        "class": "y-intercept",
    },
]

foreign_objects = [
    # Slope-intercept form
    {
        "x": -2.5,
        "y": 4.5,
        "latex": r"y = 2x + 1",
        "width": 80,
        "height": 25,
        "bg_color": "rgba(107, 70, 193, 0.1)",
        "text_color": line_color,
        "border_radius": "0.25rem",
    },
    # Standard form
    {
        "x": -2.5,
        "y": 4,
        "latex": r"2x - y + 1 = 0",
        "width": 100,
        "height": 25,
        "bg_color": "rgba(107, 70, 193, 0.1)",
        "text_color": line_color,
        "border_radius": "0.25rem",
    },
    # Point 1 label
    {
        "x": P1[0] - 0.4,
        "y": P1[1] - 0.4,
        "latex": f"({P1[0]}, {P1[1]})",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(236, 72, 153, 0.1)",
        "text_color": point_color,
        "border_radius": "0.25rem",
    },
    # Point 2 label
    {
        "x": P2[0] + 0.1,
        "y": P2[1],
        "latex": f"({P2[0]}, {P2[1]})",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(236, 72, 153, 0.1)",
        "text_color": point_color,
        "border_radius": "0.25rem",
    },
    # Y-intercept label
    {
        "x": 0.2,
        "y": b,
        "latex": f"(0, {b})",
        "width": 45,
        "height": 20,
        "bg_color": "rgba(245, 158, 11, 0.9)",
        "text_color": "white",
        "border_radius": "0.25rem",
    },
    # Slope label
    {
        "x": 1.3,
        "y": 2.5,
        "latex": r"m = 2",
        "width": 50,
        "height": 20,
        "bg_color": "rgba(16, 185, 129, 0.1)",
        "text_color": triangle_color,
        "border_radius": "0.25rem",
    },
    # Rise label
    {
        "x": triangle_x + run + 0.1,
        "y": triangle_y + rise/2,
        "latex": "2",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": triangle_color,
    },
    # Run label
    {
        "x": triangle_x + run/2,
        "y": triangle_y - 0.3,
        "latex": "1",
        "width": 20,
        "height": 20,
        "bg_color": "transparent",
        "text_color": triangle_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_coordinate_geometry_line_in_coordinate_system",
        "title": "Line in Coordinate System",
        "description": "Line in coordinate system with slope triangle and equation forms",
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

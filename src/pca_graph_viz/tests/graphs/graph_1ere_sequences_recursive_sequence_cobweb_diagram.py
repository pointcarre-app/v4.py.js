import numpy as np

# Graph: Première Spécialité Mathématiques
# Section: Sequences
# Subsection: Recursive Sequence Cobweb Diagram
# Description: A square coordinate system with y = x line and function y = f(x). Starting from (u₀, 0), draw vertical to curve, horizontal to y = x line, repeat. Shows convergence, divergence, or oscillation of sequence.

# Generate x values
x = np.linspace(-0.5, 3, 100)


# Define recursive function: u_{n+1} = f(u_n) = 2*sqrt(u_n + 1) - 1
# This converges to the fixed point where f(x) = x
def f(x):
    return 2 * np.sqrt(x + 1) - 1


y_function = f(x)
y_identity = x  # y = x line

# Generate cobweb starting from u_0 = 0.5
u0 = 0.5
cobweb_points = [(u0, 0)]  # Start at (u_0, 0)

# Generate several iterations
current_x = u0
for i in range(6):
    # Vertical line to function
    current_y = f(current_x)
    cobweb_points.append((current_x, current_y))
    # Horizontal line to y=x
    cobweb_points.append((current_y, current_y))
    current_x = current_y

# Extract cobweb coordinates
cobweb_x = [p[0] for p in cobweb_points]
cobweb_y = [p[1] for p in cobweb_points]

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
function_color = "#e74c3c"  # Red
identity_color = "#3498db"  # Blue
cobweb_color = "#27ae60"  # Green

# All visual elements in lines array
lines = [
    # Function curve y = f(x)
    {
        "type": "curve",
        "id": "function",
        "data": {"x": x.tolist(), "y": y_function.tolist()},
        "stroke": function_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve recursive-function",
    },
    # Identity line y = x
    {
        "type": "curve",
        "id": "identity",
        "data": {"x": x.tolist(), "y": y_identity.tolist()},
        "stroke": identity_color,
        "stroke-width": 2.5,
        "fill": "none",
        "class": "curve identity-line",
    },
    # Cobweb diagram
    {
        "type": "curve",
        "id": "cobweb",
        "data": {"x": cobweb_x, "y": cobweb_y},
        "stroke": cobweb_color,
        "stroke-width": 2,
        "stroke-opacity": 0.8,
        "fill": "none",
        "class": "cobweb-path",
    },
    # Starting point
    {
        "type": "circle",
        "cx": u0,
        "cy": 0,
        "r": 0.06,
        "fill": cobweb_color,
        "class": "start-point",
    },
    # Fixed point (where curves intersect)
    {
        "type": "circle",
        "cx": 2,
        "cy": 2,
        "r": 0.06,
        "fill": "#9b59b6",
        "class": "fixed-point",
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
        "y2": 3,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

# Add iteration points as small circles
for i, (px, py) in enumerate(cobweb_points[1::2][:4]):  # Show first 4 iteration points
    lines.append(
        {
            "type": "circle",
            "cx": px,
            "cy": py,
            "r": 0.04,
            "fill": cobweb_color,
            "fill-opacity": 1 - i * 0.2,  # Fade out later points
            "class": f"iteration-point-{i}",
        }
    )

foreign_objects = [
    {
        "x": 1.5,
        "y": 2.3,
        "latex": r"y = f(x)",
        "width": 60,
        "height": 20,
        "bg_color": "transparent",
        "text_color": function_color,
    },
    {
        "x": 2.3,
        "y": 1.5,
        "latex": r"y = x",
        "width": 50,
        "height": 20,
        "bg_color": "transparent",
        "text_color": identity_color,
    },
    {
        "x": u0 - 0.2,
        "y": -0.3,
        "latex": r"u_0",
        "width": 30,
        "height": 20,
        "bg_color": "transparent",
        "text_color": cobweb_color,
    },
    {
        "x": 1.8,
        "y": 2.2,
        "latex": r"\text{Fixed}",
        "width": 45,
        "height": 20,
        "bg_color": "transparent",
        "text_color": "#9b59b6",
    },
    {
        "x": -0.3,
        "y": -1,
        "latex": r"u_{n+1} = 2\sqrt{u_n + 1} - 1",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#333333",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_sequences_recursive_sequence_cobweb_diagram",
        "title": "Recursive Sequence Cobweb Diagram",
        "description": "Cobweb diagram showing convergence of recursive sequence to fixed point",
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

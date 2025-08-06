# Graph: Première Spécialité Mathématiques
# Section: Derivatives and Functions
# Subsection: Function Variation Table
# Description: A horizontal table with rows for x values, derivative sign (f'(x)), and function arrows showing increase/decrease. Critical points where f'(x)=0 are marked, arrows indicate whether function is increasing (↗) or decreasing (↘), and local maxima/minima are clearly identified.

# Generate function variation table visualization
# Example: f(x) = x^2 - 2x, f'(x) = 2x - 2
# Critical point at x = 1 where f'(1) = 0

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
table_color = "#6b46c1"  # Purple for table lines

# All visual elements in lines array
lines = [
    # Table border
    {
        "type": "line",
        "x1": -2,
        "y1": 1,
        "x2": 2,
        "y2": 1,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-top",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": 1,
        "x2": -2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-left",
    },
    {
        "type": "line",
        "x1": 2,
        "y1": 1,
        "x2": 2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-right",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": -2,
        "x2": 2,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 2,
        "class": "table-border-bottom",
    },
    # Vertical dividers
    {
        "type": "line",
        "x1": -0.5,
        "y1": 1,
        "x2": -0.5,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    {
        "type": "line",
        "x1": 0.5,
        "y1": 1,
        "x2": 0.5,
        "y2": -2,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    # Horizontal dividers
    {
        "type": "line",
        "x1": -2,
        "y1": 0,
        "x2": 2,
        "y2": 0,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
    {
        "type": "line",
        "x1": -2,
        "y1": -1,
        "x2": 2,
        "y2": -1,
        "stroke": table_color,
        "stroke-width": 1,
        "class": "table-divider",
    },
]

foreign_objects = [
    {
        "x": 0,
        "y": 1.5,
        "latex": r"Function Variation Table",
        "width": 180,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1.25,
        "y": 0.5,
        "latex": r"x",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -0.25,
        "y": 0.5,
        "latex": r"f'(x)",
        "width": 40,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0.25,
        "y": 0.5,
        "latex": r"f(x)",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.25,
        "y": 0.5,
        "latex": r"Variation",
        "width": 60,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -1.25,
        "y": -0.5,
        "latex": r"< 1",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -0.25,
        "y": -0.5,
        "latex": r"-",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": 0.25,
        "y": -0.5,
        "latex": r"↘",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": 1.25,
        "y": -0.5,
        "latex": r"Decreasing",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#ec3059",
    },
    {
        "x": -1.25,
        "y": -1.5,
        "latex": r"> 1",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#2a88c0",
    },
    {
        "x": -0.25,
        "y": -1.5,
        "latex": r"+",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#10b981",
    },
    {
        "x": 0.25,
        "y": -1.5,
        "latex": r"↗",
        "width": 30,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#10b981",
    },
    {
        "x": 1.25,
        "y": -1.5,
        "latex": r"Increasing",
        "width": 80,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#10b981",
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_derivatives_and_functions_function_variation_table",
        "title": "Function Variation Table",
        "description": "Function variation table showing derivative signs and function behavior",
        "svg": {
            "width": 400,
            "height": 300,
            "viewBox": "0 0 400 300",
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

# Graph: Première Spécialité Mathématiques
# Section: Special Topics
# Subsection: Function Composition Diagram
# Description: Arrow diagram or mapping showing f: A → B and g: B → C. Composition g∘f: A → C illustrated. Can also show as nested function machines. Include specific example with values.

# Generate function composition diagram
# Example: f(x) = x², g(x) = x + 1, so g∘f(x) = x² + 1

# Use nice hex colors directly
bg_color = "#f5f7fb"  # Very light blue-grey
grid_color = "#dde3ed"  # Light grey
f_color = "#6b46c1"  # Purple for f
g_color = "#ab0084"  # Pink for g
composition_color = "#2a88c0"  # Blue for composition

# All visual elements in lines array
lines = [
    # Function f: A → B (x → x²)
    {
        "type": "line",
        "x1": -1.5,
        "y1": 0.5,
        "x2": -0.5,
        "y2": 0.5,
        "stroke": f_color,
        "stroke-width": 2,
        "class": "function-arrow",
    },
    # Function g: B → C (x → x + 1)
    {
        "type": "line",
        "x1": 0.5,
        "y1": 0.5,
        "x2": 1.5,
        "y2": 0.5,
        "stroke": g_color,
        "stroke-width": 2,
        "class": "function-arrow",
    },
    # X-axis
    {
        "type": "axis",
        "x1": -2,
        "y1": 0,
        "x2": 2,
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
        "y2": 1,
        "stroke": "#666666",
        "stroke-width": 1,
        "stroke-opacity": 0.7,
        "class": "axis y-axis",
    },
]

foreign_objects = [
    {
        "x": -1.5,
        "y": 1.2,
        "latex": r"Function Composition",
        "width": 150,
        "height": 25,
        "bg_color": "rgba(255, 255, 255, 0.9)",
        "text_color": "#503ab2",
    },
    {
        "x": -1.5,
        "y": 0.8,
        "latex": r"A",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 0,
        "y": 0.8,
        "latex": r"B",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": 1.5,
        "y": 0.8,
        "latex": r"C",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": "#666666",
    },
    {
        "x": -1,
        "y": 0.6,
        "latex": r"f",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": f_color,
    },
    {
        "x": 1,
        "y": 0.6,
        "latex": r"g",
        "width": 20,
        "height": 20,
        "bg_color": "rgba(255, 255, 255, 0.8)",
        "text_color": g_color,
    },
]


def get_graph_dict():
    """Return the graph as a standardized dictionary."""
    return {
        "id": "graph_1ere_special_topics_function_composition_diagram",
        "title": "Function Composition Diagram",
        "description": "Arrow diagram showing function composition g∘f where f(x) = x² and g(x) = x + 1",
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

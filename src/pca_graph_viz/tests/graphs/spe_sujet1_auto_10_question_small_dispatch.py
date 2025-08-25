import numpy as np

# Rendering/domain constants
SAMPLES = 1000


# Direct configuration mapping based on graph ID
# Each configuration is for a specific graph file
GRAPH_CONFIGS = {
    "s1_a_0": {  # y = x^2 (parabola_sign=1, a_shift=0)
        "X_MIN": -4.0,
        "X_MAX": 4.0,
        "Y_MIN": -5,
        "Y_MAX": 18,
        "x_axis_x1": -4.5,
        "x_axis_y1": 0,
        "x_axis_x2": 4.5,
        "x_axis_y2": 0,
        "y_axis_x1": 0,
        "y_axis_y1": -4.5,
        "y_axis_x2": 0,
        "y_axis_y2": 17,
        "x_label_x": 4.75,
        "x_label_y": -1,
        "y_label_x": 0.5,
        "y_label_y": 17,
    },
    "s1_a_m": {  # y = x^2 - 5 (parabola_sign=1, a_shift=-5)
        "X_MIN": -4.0,
        "X_MAX": 4.0,
        "Y_MIN": -5,
        "Y_MAX": 13,
        "x_axis_x1": -3,
        "x_axis_y1": 0,
        "x_axis_x2": 3,
        "x_axis_y2": 0,
        "y_axis_x1": 0,
        "y_axis_y1": -7,
        "y_axis_x2": 0,
        "y_axis_y2": 10.5,
        "x_label_x": 3.5,
        "x_label_y": -1,
        "y_label_x": 0.5,
        "y_label_y": 10.5,
    },
    "s1_a_p": {  # y = x^2 + 5 (parabola_sign=1, a_shift=5)
        "X_MIN": -4.0,
        "X_MAX": 4.0,
        "Y_MIN": -10,
        "Y_MAX": 19,
        "x_axis_x1": -4,
        "x_axis_y1": 4,
        "x_axis_x2": 4,
        "x_axis_y2": 4,
        "y_axis_x1": 0,
        "y_axis_y1": -6,
        "y_axis_x2": 0,
        "y_axis_y2": 22,
        "x_label_x": 4.5,
        "x_label_y": 3,
        "y_label_x": 0.5,
        "y_label_y": 22.5,
    },
    "sm1_a_0": {  # y = -x^2 (parabola_sign=-1, a_shift=0)
        "X_MIN": -4.0,
        "X_MAX": 4.0,
        "Y_MIN": -20,
        "Y_MAX": 4,
        "x_axis_x1": -4,
        "x_axis_y1": 0,
        "x_axis_x2": 4,
        "x_axis_y2": 0,
        "y_axis_x1": 0,
        "y_axis_y1": -21.5,
        "y_axis_x2": 0,
        "y_axis_y2": 1.25,
        "x_label_x": 4,
        "x_label_y": -1.0,
        "y_label_x": 0.5,
        "y_label_y": 1.5,
    },
    "sm1_a_m": {  # y = -x^2 - 5 (parabola_sign=-1, a_shift=-5)
        "X_MIN": -4.0,
        "X_MAX": 4.0,
        "Y_MIN": -20,
        "Y_MAX": 4,
        "x_axis_x1": -4.2,
        "x_axis_y1": -4.2,
        "x_axis_x2": 4,
        "x_axis_y2": -4,
        "y_axis_x1": 0,
        "y_axis_y1": -21.5,
        "y_axis_x2": 0,
        "y_axis_y2": -3.75,
        "x_label_x": 4.4,
        "x_label_y": -4.75,
        "y_label_x": 0.75,
        "y_label_y": -3.2,
    },
    "sm1_a_p": {  # y = -x^2 + 10 (parabola_sign=-1, a_shift=10)
        "X_MIN": -5.0,
        "X_MAX": 5.0,
        "Y_MIN": -10,
        "Y_MAX": 15,
        "x_axis_x1": -4.7,
        "x_axis_y1": 0,
        "x_axis_x2": 4.7,
        "x_axis_y2": 0,
        "y_axis_x1": 0,
        "y_axis_y1": -15,
        "y_axis_x2": 0,
        "y_axis_y2": 12,
        "x_label_x": 5,
        "x_label_y": -1.5,
        "y_label_x": 0.75,
        "y_label_y": 12,
    },
}


def compute_parameters(graph_id: str) -> dict:
    """Get parameters for a specific graph by its ID.

    Args:
        graph_id: Graph identifier (e.g., 's1_a_0', 's1_a_m', 'sm1_a_p')

    Returns:
        Dictionary with all display parameters for the graph

    Raises:
        ValueError: If graph_id is not found in GRAPH_CONFIGS
    """
    if graph_id not in GRAPH_CONFIGS:
        raise ValueError(f"Unknown graph ID: {graph_id}. Available: {list(GRAPH_CONFIGS.keys())}")

    return GRAPH_CONFIGS[graph_id]


def generate_parabola_graph(
    graph_id: str,
    parabola_sign: int,
    a_shift: float,
    filename: str,
    a_shift_for_label: float = None,
    a_adjust: float = 0,
):
    """Generate a parabola graph with the given parameters.

    Args:
        graph_id: Graph identifier for config lookup (e.g., 's1_a_0', 's1_a_m')
        parabola_sign: +1 for y = x^2 + a, -1 for y = -x^2 + a
        a_shift: The vertical shift value 'a' (used for the actual curve position)
        filename: The filename to use as the title
        a_shift_for_label: The value to display in the M point label (if different from a_shift)
        a_adjust: Fine-tuning adjustment for curve position (default 0, not shown in labels)

    Returns:
        A dictionary containing the graph data
    """
    # Get ALL parameters using the graph ID
    params = compute_parameters(graph_id)

    # Use a_shift_for_label if provided, otherwise use a_shift
    label_value = a_shift_for_label if a_shift_for_label is not None else a_shift

    X_MIN = params["X_MIN"]
    X_MAX = params["X_MAX"]

    # Generate data using the fixed a_shift value (NOT the dynamic label_value)
    # This keeps the curve position fixed regardless of slider changes
    # The a_adjust is for fine-tuning position without changing labels
    x = np.linspace(X_MIN, X_MAX, SAMPLES)
    y = parabola_sign * (x**2) + a_shift + a_adjust

    # Find the vertex point (closest to x=0)
    # For these parabolas, the vertex is at x=0
    vertex_x = 0
    vertex_y = parabola_sign * (vertex_x**2) + a_shift + a_adjust

    # Extract all values from params dict

    Y_MIN = params["Y_MIN"]
    Y_MAX = params["Y_MAX"]

    x_axis_x1 = params["x_axis_x1"]
    x_axis_y1 = params["x_axis_y1"]
    x_axis_x2 = params["x_axis_x2"]
    x_axis_y2 = params["x_axis_y2"]

    y_axis_x1 = params["y_axis_x1"]
    y_axis_y1 = params["y_axis_y1"]
    y_axis_x2 = params["y_axis_x2"]
    y_axis_y2 = params["y_axis_y2"]

    x_label_x = params["x_label_x"]
    x_label_y = params["x_label_y"]
    y_label_x = params["y_label_x"]
    y_label_y = params["y_label_y"]

    # Tick marks are commented out but keeping for future use
    # x_ticks = params["x_ticks"]
    # y_ticks = params["y_ticks"]
    # tick_length = params["tick_length"]

    # ========================================
    # BUILD AXES AND CURVES
    # ========================================

    lines = [
        # X-axis - horizontal line
        {
            "type": "axis",
            "x1": x_axis_x1,
            "y1": x_axis_y1,
            "x2": x_axis_x2,
            "y2": x_axis_y2,
            "stroke-width": 1.5,
            "class": "axis x-axis stroke-base-content",
        },
        # Y-axis - vertical line
        {
            "type": "axis",
            "x1": y_axis_x1,
            "y1": y_axis_y1,
            "x2": y_axis_x2,
            "y2": y_axis_y2,
            "stroke-width": 1.5,
            "class": "axis y-axis stroke-base-content",
        },
    ]

    # # Add tick marks on x-axis
    # for x_tick in x_ticks:
    #     lines.append(
    #         {
    #             "type": "tick",
    #             "x1": x_tick,
    #             "y1": -tick_length,
    #             "x2": x_tick,
    #             "y2": tick_length,
    #             "stroke-width": 1,
    #             "class": "stroke-base-content",
    #         }
    #     )

    # # Add tick marks on y-axis
    # for y_tick in y_ticks:
    #     lines.append(
    #         {
    #             "type": "tick",
    #             "x1": -tick_length,
    #             "y1": y_tick,
    #             "x2": tick_length,
    #             "y2": y_tick,
    #             "stroke-width": 1,
    #             "class": "stroke-base-content",
    #         }
    #     )

    # Add the parabola curve
    lines.append(
        {
            "type": "curve",
            "id": "parabola",
            "data": {"x": x.tolist(), "y": y.tolist()},
            "stroke-width": 2,
            "fill": "none",
            "class": "curve stroke-primary",
        }
    )

    # Add vertex dot (point closest to x=0)
    lines.append(
        {
            "type": "circle",
            "cx": vertex_x,
            "cy": vertex_y,
            "r": 4,
            "class": "fill-primary",
            "stroke": "none",
        }
    )

    # ========================================
    # BUILD LABELS
    # ========================================
    # Note: Label positions are defined in the CONFIGURABLE section above

    foreign_objects = [
        # X axis label
        {
            "x": x_label_x,
            "y": x_label_y,
            "latex": "x",
            "width": 20,
            "height": 10,
            "class": "svg-latex fill-base-content",
        },
        # Y axis label
        {
            "x": y_label_x,
            "y": y_label_y,
            "latex": "y",
            "width": 20,
            "height": 20,
            "class": "svg-latex fill-base-content",
        },
        # Vertex label M(0;a) - using the label value
        {
            "x": vertex_x + 2.25,  # Move right by ~20px in graph units
            "y": vertex_y - 0.3,  # Slightly above the dot
            "latex": f"M(0;{int(label_value)})",
            "width": 60,
            "height": 20,
            "class": "svg-latex text-primary text-xs",
            "style": "background: rgba(255, 255, 255, 0.7); padding: 2px 4px; border-radius: var(--radius-box, 4px);",
        },
    ]

    return {
        "id": f"parabola_sign_{parabola_sign}_a_{int(a_shift)}_small",
        "title": filename,
        "description": f"Parabola y = {'x^2' if parabola_sign == 1 else '-x^2'} + a with a={a_shift}",
        "svg": {
            "width": 180,
            "height": 180,
            "viewBox": "0 0 180 180",
            "class": "fill-base-100",
        },
        "settings": {
            "margin": {"top": 15, "right": 15, "bottom": 15, "left": 15},
            "show_axes": False,
            "show_grid": False,
            "x_range": [X_MIN, X_MAX],
            "y_range": [Y_MIN, Y_MAX],
        },
        "lines": lines,
        "foreign_objects": foreign_objects,
    }


# For direct testing/usage
def get_graph_dict():
    """Default graph for testing - can be overridden by importing modules."""
    return generate_parabola_graph("s1_a_0", 1, 0, "spe_sujet1_auto_10_question_small_dispatch.py")

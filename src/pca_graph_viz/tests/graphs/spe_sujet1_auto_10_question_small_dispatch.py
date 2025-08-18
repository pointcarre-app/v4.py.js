import numpy as np

# Rendering/domain constants
SAMPLES = 1000


def compute_parameters(parabola_sign: int, a_shift: float) -> dict:
    """Compute ALL parameters for the parabola graph.

    Returns a dict with all display parameters including ranges, axis positions,
    label positions, tick marks, etc. Everything is hardcoded for each case.
    """
    # Round a_shift to nearest reference value: -10, -5, 0, 5, or 10
    reference_values = [-10, -5, 0, 5, 10]
    closest_a = min(reference_values, key=lambda x: abs(x - a_shift))

    # Use match statement to handle all cases
    match (parabola_sign, closest_a):
        case (1, 0):  # y = x^2
            params = {
                "X_MIN": -4.0,
                "X_MAX": 4.0,
                "Y_MIN": -5,
                "Y_MAX": 18,
                "x_axis_x1": -4.5,  # X_MIN + 0.5
                "x_axis_y1": 0,
                "x_axis_x2": 4.5,  # X_MAX - 0.5
                "x_axis_y2": 0,
                "y_axis_x1": 0,
                "y_axis_y1": -4.5,
                "y_axis_x2": 0,
                "y_axis_y2": 17,  # Y_MAX - 1
                "x_label_x": 4.75,  # X_MAX - 0.25
                "x_label_y": -1,
                "y_label_x": 0.5,
                "y_label_y": 17,  # Y_MAX - 1
            }

        case (1, -5):  # y = x^2 - 5
            params = {
                "X_MIN": -4.0,
                "X_MAX": 4.0,
                "Y_MIN": -5,
                "Y_MAX": 13,
                "x_axis_x1": -3,
                "x_axis_y1": 0,
                "x_axis_x2": 3,
                "x_axis_y2": 0,
                "y_axis_x1": 0,
                "y_axis_y1": -5.5,  # MUST be >= Y_MIN (-6)
                "y_axis_x2": 0,
                "y_axis_y2": 10.5,  # MUST be <= Y_MAX (17)
                "x_label_x": 3.5,  # MUST be <= X_MAX (5)
                "x_label_y": -1,
                "y_label_x": 0.5,
                "y_label_y": 10.5,  # MUST be <= Y_MAX (17)
            }

        case (1, 5):  # y = x^2 + 5
            # TODO: clean // enormous cheat: use cause -10 and move the x-axis
            # case (1, -10):  # y = x^2 - 10
            params = {
                "X_MIN": -4.0,
                "X_MAX": 4.0,
                "Y_MIN": -10,
                "Y_MAX": 19,
                "x_axis_x1": -4,
                "x_axis_y1": 4,  #### HACK
                "x_axis_x2": 4,
                "x_axis_y2": 4,  #### HACK
                "y_axis_x1": 0,
                "y_axis_y1": -6,
                "y_axis_x2": 0,
                "y_axis_y2": 22,  # MUST be <= Y_MAX
                "x_label_x": 4,  # MUST be <= X_MAX
                "x_label_y": 5,  ## HACK
                "y_label_x": 0.5,
                "y_label_y": 22,  # MUST be <= Y_MAX (10)
            }

        case (-1, 0):  # y = -x^2
            params = {
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
                "x_label_x": 4.5,
                "x_label_y": -1.0,
                "y_label_x": 0.5,
                "y_label_y": 1.25,
            }

        case (-1, -5):  # y = -x^2
            params = {
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
                "x_label_x": 4.5,
                "x_label_y": -4.5,
                "y_label_x": 0.5,
                "y_label_y": -3.3,
            }

        # ========== DOWNWARD PARABOLAS (y = -x^2 + a) ==========
        case (-1, 10):  # y = -x^2 + 10
            params = {
                "X_MIN": -5.0,
                "X_MAX": 5.0,
                "Y_MIN": -10,
                "Y_MAX": 12,
                "x_axis_x1": -4.7,
                "x_axis_y1": 0,
                "x_axis_x2": 4.7,
                "x_axis_y2": 0,
                "y_axis_x1": 0,
                "y_axis_y1": -9.5,
                "y_axis_x2": 0,
                "y_axis_y2": 11.5,
                "x_label_x": 5,
                "x_label_y": -1.5,
                "y_label_x": 0.75,
                "y_label_y": 12,
            }

        # # Default case (shouldn't happen but just in case)
        # case _:
        #     params = {
        #         "X_MIN": -5.0,
        #         "X_MAX": 5.0,
        #         "Y_MIN": -10,
        #         "Y_MAX": 10,
        #         "x_axis_x1": -4.7,
        #         "x_axis_y1": 0,
        #         "x_axis_x2": 4.7,
        #         "x_axis_y2": 0,
        #         "y_axis_x1": 0,
        #         "y_axis_y1": -9.5,
        #         "y_axis_x2": 0,
        #         "y_axis_y2": 9.5,
        #         "x_label_x": 4.5,
        #         "x_label_y": -1.2,
        #         "y_label_x": 0.3,
        #         "y_label_y": 8.5,
        #         "x_ticks": [-4, -2, 2, 4],
        #         "y_ticks": [],
        #         "tick_length": 0.2,
        #     }

    return params


def generate_parabola_graph(parabola_sign: int, a_shift: float, filename: str):
    """Generate a parabola graph with the given parameters.

    Args:
        parabola_sign: +1 for y = x^2 + a, -1 for y = -x^2 + a
        a_shift: The vertical shift value 'a'
        filename: The filename to use as the title

    Returns:
        A dictionary containing the graph data
    """
    # Get ALL parameters from the centralized function
    params = compute_parameters(parabola_sign, a_shift)

    X_MIN = params["X_MIN"]
    X_MAX = params["X_MAX"]

    # Generate data
    x = np.linspace(X_MIN, X_MAX, SAMPLES)
    y = parabola_sign * (x**2) + a_shift

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
    return generate_parabola_graph(1, 0, "spe_sujet1_auto_10_question_small_dispatch.py")

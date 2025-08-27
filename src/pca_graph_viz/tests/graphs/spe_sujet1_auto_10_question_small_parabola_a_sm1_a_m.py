"""
Downward parabola with negative shift (y = -x^2 - a).

When executed via Nagini from JavaScript (sujets0-app-simple.js),
the A_SHIFT_MAGNITUDE variable is injected into this module's namespace
before execution, allowing dynamic configuration of the label display.

The value can be changed using the control panel in sujets0-simple.html.
"""

from .spe_sujet1_auto_10_question_small_dispatch import generate_parabola_graph

# Default configuration value
# This can be overridden by passing a parameter to get_graph_dict()
A_SHIFT_MAGNITUDE = 5

# Configuration for this specific parabola
PARABOLA_SIGN = -1  # -1 for y = -x^2 + a
A_SHIFT_FOR_CASE = -5  # Fixed value for matching graph case
A_ADJUST = 0  # Fine-tuning adjustment for curve position (not shown in labels)


def get_graph_dict(a_shift=None):
    """Return the graph dictionary for this configuration.

    Args:
        a_shift: Shift magnitude for the label (optional, defaults to module value)
    """
    # Use parameter if provided, otherwise use module-level value
    shift_magnitude = a_shift if a_shift is not None else A_SHIFT_MAGNITUDE
    a_shift_for_label = -shift_magnitude  # Negative for this case

    return generate_parabola_graph(
        "sm1_a_m",  # Graph ID
        PARABOLA_SIGN,
        A_SHIFT_FOR_CASE,
        "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m.py",
        a_shift_for_label,
        A_ADJUST,
    )

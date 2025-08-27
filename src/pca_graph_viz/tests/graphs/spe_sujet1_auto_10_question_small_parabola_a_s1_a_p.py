"""
Upward parabola with positive shift (y = x^2 + a).

REQUIRED: The A_SHIFT_MAGNITUDE variable MUST be injected into this module's namespace
by Nagini from JavaScript before calling get_graph_dict().

The value can be changed using the control panel in sujets0-simple.html.
"""

from .spe_sujet1_auto_10_question_small_dispatch import generate_parabola_graph

# NO DEFAULT VALUE - Must be injected from JavaScript via Nagini
# If this variable is not set, get_graph_dict() will raise an error
# A_SHIFT_MAGNITUDE = <must be injected>

# Configuration for this specific parabola
PARABOLA_SIGN = 1  # +1 for y = x^2 + a
A_SHIFT_FOR_CASE = 5  # Fixed value for matching graph case
A_ADJUST = 0  # Fine-tuning adjustment for curve position (not shown in labels)


def get_graph_dict(a_shift=None):
    """Return the graph dictionary for this configuration.

    Args:
        a_shift: Shift magnitude for the label (optional, uses injected value if not provided)

    Raises:
        NameError: If A_SHIFT_MAGNITUDE is not injected into namespace
    """
    # Check if variable was injected from JavaScript
    if "A_SHIFT_MAGNITUDE" not in globals():
        raise NameError(
            "A_SHIFT_MAGNITUDE must be injected into module namespace by Nagini. "
            "Ensure graphConfig is properly passed from JavaScript."
        )

    # Use parameter if provided, otherwise use injected value
    shift_magnitude = a_shift if a_shift is not None else A_SHIFT_MAGNITUDE
    a_shift_for_label = shift_magnitude  # Positive for this case

    return generate_parabola_graph(
        "s1_a_p",  # Graph ID
        PARABOLA_SIGN,
        A_SHIFT_FOR_CASE,
        "spe_sujet1_auto_10_question_small_parabola_a_s1_a_p.py",
        a_shift_for_label,
        A_ADJUST,
    )

from spe_sujet1_auto_10_question_small_dispatch import generate_parabola_graph

# Configuration for this specific parabola
PARABOLA_SIGN = 1  # +1 for y = x^2 + a
A_SHIFT = -10


def get_graph_dict():
    """Return the graph dictionary for this configuration."""
    return generate_parabola_graph(
        PARABOLA_SIGN, A_SHIFT, "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m10.py"
    )

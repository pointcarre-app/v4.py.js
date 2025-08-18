"""Nagini to v4.py.js adapter for loading graph modules independently.

This adapter provides functions to load and execute graph modules without
relying on complex package structures or __init__.py files.
"""

import json
import sys
import traceback
import types
from typing import Any, Dict


def ensure_package_structure():
    """Create minimal package structure for pca_graph_viz.tests.graphs if needed."""
    # Create pca_graph_viz.tests module if it doesn't exist
    if "pca_graph_viz.tests" not in sys.modules:
        tests_module = types.ModuleType("pca_graph_viz.tests")
        tests_module.__path__ = ["pca_graph_viz/tests"]
        sys.modules["pca_graph_viz.tests"] = tests_module
        print("Created pca_graph_viz.tests module")

    # Create pca_graph_viz.tests.graphs module if it doesn't exist
    if "pca_graph_viz.tests.graphs" not in sys.modules:
        graphs_module = types.ModuleType("pca_graph_viz.tests.graphs")
        graphs_module.__path__ = ["pca_graph_viz/tests/graphs"]
        sys.modules["pca_graph_viz.tests.graphs"] = graphs_module
        print("Created pca_graph_viz.tests.graphs module")

    # Add the graphs directory to sys.path for relative imports
    graphs_path = "/home/pyodide/pca_graph_viz/tests/graphs"
    if graphs_path not in sys.path:
        sys.path.insert(0, graphs_path)
        print(f"Added {graphs_path} to sys.path for relative imports")

    return True


def load_graph_module(module_name: str) -> Dict[str, Any]:
    """Load a graph module and extract its graph dictionary.

    Args:
        module_name: Name of the module (e.g., 'spe_sujet1_auto_07_question_small')

    Returns:
        Dict containing either:
        - {"graph": <graph_dict>, "title": <title>} on success
        - {"error": <error_msg>, "traceback": <traceback>} on failure
    """
    try:
        # Ensure package structure exists
        ensure_package_structure()

        # Import the module
        from importlib import import_module

        module = import_module(f"pca_graph_viz.tests.graphs.{module_name}")

        # Check if get_graph_dict exists
        if not hasattr(module, "get_graph_dict"):
            raise RuntimeError(f"get_graph_dict function not found in {module_name}")

        # Get the graph dictionary
        graph_dict = module.get_graph_dict()
        title = graph_dict.get("title", module_name)

        print(f"✅ Loaded graph: {title}")

        return {"graph": graph_dict, "title": title}

    except Exception as e:
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"❌ Error loading {module_name}: {error_msg}")
        print(tb)

        return {"error": error_msg, "traceback": tb}


def load_graph_from_source(source_code: str, module_name: str) -> Dict[str, Any]:
    """Execute graph module source code and extract its graph dictionary.

    This is useful when you need to load a module from source code directly
    without it being in the module system.

    Args:
        source_code: Python source code of the module
        module_name: Name to use for the module

    Returns:
        Dict containing either:
        - {"graph": <graph_dict>, "title": <title>} on success
        - {"error": <error_msg>, "traceback": <traceback>} on failure
    """
    try:
        # Create a namespace for execution
        namespace = {
            "__name__": f"dynamic_{module_name}",
            "__file__": f"<dynamic>/{module_name}.py",
        }

        # Execute the source code
        exec(source_code, namespace)

        # Check if get_graph_dict exists
        if "get_graph_dict" not in namespace:
            raise RuntimeError("get_graph_dict function not found in source")

        # Get the graph dictionary
        graph_dict = namespace["get_graph_dict"]()
        title = graph_dict.get("title", module_name)

        print(f"✅ Loaded graph from source: {title}")

        return {"graph": graph_dict, "title": title}

    except Exception as e:
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"❌ Error loading from source: {error_msg}")
        print(tb)

        return {"error": error_msg, "traceback": tb}


def render_graph(graph_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Render a graph dictionary to SVG.

    Args:
        graph_dict: Graph dictionary to render

    Returns:
        Dict containing either:
        - {"svg": <svg_string>} on success
        - {"error": <error_msg>, "traceback": <traceback>} on failure
    """
    try:
        from pca_graph_viz import graph_from_dict

        # Ensure reasonable defaults
        if "settings" not in graph_dict:
            graph_dict["settings"] = {}
        if "margin" not in graph_dict["settings"]:
            graph_dict["settings"]["margin"] = 16

        svg_output = graph_from_dict(graph_dict)

        return {"svg": svg_output}

    except Exception as e:
        error_msg = str(e)
        tb = traceback.format_exc()
        print(f"❌ Render error: {error_msg}")
        print(tb)

        return {"error": error_msg, "traceback": tb}


# For use with missive in Nagini
def load_and_send_graph(module_name: str):
    """Load a graph module and send it via missive (for Nagini)."""
    result = load_graph_module(module_name)
    missive(result)  # type: ignore[name-defined]  # missive is injected by Nagini


def render_and_send_graph(graph_dict_json: str):
    """Render a graph from JSON and send SVG via missive (for Nagini)."""
    try:
        graph_dict = json.loads(graph_dict_json)
        result = render_graph(graph_dict)
        missive(result)  # type: ignore[name-defined]  # missive is injected by Nagini
    except json.JSONDecodeError as e:
        missive({"error": f"JSON decode error: {e}", "traceback": traceback.format_exc()})  # type: ignore[name-defined]

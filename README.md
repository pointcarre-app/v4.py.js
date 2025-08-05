# 🎨 PCA Graph Visualization Engine

This repository contains a powerful and flexible visualization engine for rendering mathematical graphs and scenes directly in the browser. It uses a Python-based backend, running entirely in the browser via **Pyodide**, to generate clean, static SVG images from a declarative dictionary format.

The engine is designed for educational and technical applications where precise, LaTeX-annotated visualizations are critical. It powers the interactive graphical components of the [Nagini](https://github.com/pointcarre-app/nagini) project.

## ✨ Features

- **Declarative Scene Definition**: Define complex scenes—including curves, lines, axes, and grids—using a simple Python dictionary.
- **In-Browser Python**: All SVG generation is handled by Python code running in a web worker, powered by Pyodide. No server-side rendering required.
- **LaTeX Annotations**: Seamlessly embed mathematical formulas and labels using LaTeX, rendered beautifully with KaTeX.
- **Static SVG Output**: Generates clean, lightweight, and scalable SVG images that can be easily embedded and manipulated.
- **Flexible Styling**: Customize colors, strokes, and fills for every element in the scene.
- **Extensible Models**: The data models are built with Pydantic, making them easy to extend and validate.

## 🚀 Quick Start

### Live Demo

▶️ **View the live demo at: https://[your-username].github.io/pca-v4.py.js/scenery/**

The demo runs entirely in your browser using Pyodide (Python in WebAssembly) - no server required!

### Deployment to GitHub Pages

1. **Enable GitHub Pages**: Go to Settings → Pages → Source → Select "GitHub Actions"
2. **Push to main branch**: The workflow will automatically deploy your site
3. **Access your site**: Visit `https://[your-username].github.io/pca-v4.py.js/scenery/`

### Local Development

To run the visualization engine locally:

**1. Set up the environment:**

First, ensure you have Python 3.8+ installed. Then, install the project dependencies from `pyproject.toml`:

```bash
pip install .
```

This command installs all required packages, including `svgwrite` and `numpy`.

**2. Run the local server:**

A simple web server is included to serve the necessary files.

```bash
python serve.py
```

The server will start on `http://localhost:8022`.

**3. View the graphs:**

Open your browser and navigate to the following URL to see all the rendered graphs:

▶️ **http://localhost:8022/scenery/**

## 📁 Project Structure

The repository is organized following modern Python packaging standards.

```
.
├── src/
│   └── pca_graph_viz/      # The core Python package for SVG generation
│       ├── core/           # SVG rendering logic
│       ├── models/         # Pydantic data models for scene objects
│       └── tests/          # Graph definitions and tests
├── scenery/
│   └── index.html          # The web interface for displaying test graphs
├── pyproject.toml          # Project metadata and dependencies (PEP 621)
└── serve.py                # Local web server for testing
```

- **`src/pca_graph_viz`**: This is the main Python package, `pca_graph_viz`. It contains all the logic for parsing the graph dictionaries and generating SVG output.
- **`scenery/index.html`**: A simple HTML file that uses the Nagini JS library to execute the Python code and display the generated graphs. It serves as the primary testbed for the visualization engine.
- **`pyproject.toml`**: Defines all project dependencies and build configurations. `requirements.txt` is not needed, as all dependencies are managed here.

## 🔧 Dependencies

### JavaScript Dependencies (CDN)

The browser interface (`scenery/`) uses the following external libraries loaded from CDN:

- **[Nagini](https://github.com/pointcarre-app/nagini) v0.0.17**: Python-in-browser execution wrapper for Pyodide
  - Main library: `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/nagini.js`
  - Worker script: `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/pyodide/worker/worker-dist.js`
- **[KaTeX](https://katex.org/)**: Fast math typesetting library for LaTeX rendering
- **[Pyodide](https://pyodide.org/)**: Python runtime in WebAssembly (loaded via Nagini)

### Python Dependencies

Server-side development and testing dependencies (installed via `pip install .`):

- **numpy** ≥1.20.0: Numerical computing
- **svgwrite** ≥1.4.0: SVG generation
- **pydantic** ≥2.0.0: Data validation and models

## 🎨 Example Usage

The core of the engine is the `graph_from_dict` function, which takes a Python dictionary and returns an SVG string.

Here's a simple example of how to define a graph:

```python
from pca_graph_viz import graph_from_dict

# Define a scene with a single blue curve
graph_dict = {
    "title": "Simple Sine Curve",
    "curves": [
        {
            "type": "curve",
            "data": {"x": [0, 1, 2, 3], "y": [0, 1, 0, -1]},
            "stroke": "#1976d2",
            "stroke_width": 2
        }
    ],
    "axes": {"x_axis": True, "y_axis": True}
}

# Generate the SVG string
svg_output = graph_from_dict(graph_dict)

# You can now save svg_output to a file or embed it in a web page
with open("sine_curve.svg", "w") as f:
    f.write(svg_output)
```

This declarative approach makes it easy to generate a wide variety of mathematical visualizations with minimal code.

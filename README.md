# 🎨 PCA Graph Visualization Engine

> ⚠️ **UNSTABLE VERSION**: This is v0.0.2-unstable - an extremely experimental release with frequent breaking changes. Not recommended for production use. Expect bugs, API changes, and incomplete features.

A comprehensive mathematical visualization library for educational content, featuring 40+ interactive graphs covering the French Première Spécialité Mathématiques curriculum. The engine runs entirely in the browser using Python via **Pyodide**, generating clean SVG visualizations with LaTeX annotations.

This repository provides ready-to-use mathematical visualizations including trigonometry, calculus, probability, geometry, sequences, and more. Perfect for educational platforms, online courses, and interactive mathematics learning.

## ✨ Features

- **40+ Mathematical Visualizations**: Complete coverage of Première Spécialité topics including:
  - Trigonometry (unit circle, sine/cosine graphs)
  - Sequences (arithmetic, geometric, recursive with cobweb diagrams)
  - Calculus (derivatives, tangent lines, variation tables)
  - Functions (parabolas, transformations, canonical forms)
  - Vectors and geometry (scalar products, orthogonality)
  - Probability (Venn diagrams, tree diagrams, distributions)
- **In-Browser Python**: All SVG generation runs client-side via Pyodide - no server required
- **LaTeX Annotations**: Mathematical formulas rendered beautifully with KaTeX
- **Clean SVG Output**: Lightweight, scalable vector graphics
- **Declarative API**: Simple Python dictionary format for defining graphs
- **Educational Focus**: Designed specifically for mathematics education

## 🚀 Quick Start

### Live Demo

▶️ **View the live demo at: https://pointcarre-app.github.io/v4.py.js/**

The demo will automatically redirect to the scenery page, or you can directly visit:
- https://pointcarre-app.github.io/v4.py.js/scenery/

The demo runs entirely in your browser using Pyodide (Python in WebAssembly) - no server required!

### Deployment to GitHub Pages

1. **Enable GitHub Pages**: 
   - Go to Settings → Pages
   - Under "Source", select "GitHub Actions"
   
2. **Deploy the site**:
   - Push your changes to the main branch
   - The GitHub Actions workflow will automatically deploy
   - Wait ~2-5 minutes for the deployment to complete
   
3. **Access your site**: 
   - Main page: `https://[your-username].github.io/v4.py.js/`
   - Demo page: `https://[your-username].github.io/v4.py.js/scenery/`
   - Test page: `https://[your-username].github.io/v4.py.js/test-file-access.html`

**Note**: The entire repository is served as static files. The `.nojekyll` file ensures GitHub Pages serves all files without Jekyll processing.

### Available Visualizations

The demo includes 40+ interactive mathematical graphs organized by topic:
- **Trigonometry**: Unit circle, sine/cosine functions, angle wrapping
- **Sequences**: Arithmetic, geometric, recursive sequences with cobweb diagrams
- **Derivatives**: Tangent lines, function derivatives, variation tables
- **Second-degree functions**: Parabolas, canonical forms, sign tables
- **Vectors**: Scalar products, orthogonal vectors, projections
- **Probability**: Venn diagrams, tree diagrams, normal distributions
- **Coordinate geometry**: Circles, lines, distance formulas
- **Special topics**: 3D coordinates, parametric curves, optimization

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

Each visualization is defined using a Python dictionary structure. Here's an example from the included graphs:

```python
import numpy as np

# Example: Parabola with vertex and transformations
x = np.linspace(-3, 3, 100)
y_basic = x**2
y_transformed = 0.5 * (x - 1)**2 - 2  # Canonical form

graph_dict = {
    "title": "Parabola Transformations",
    "description": "Showing transformations from y=x² to canonical form",
    "svg": {
        "width": 340,
        "height": 340,
        "viewBox": "0 0 340 340"
    },
    "lines": [
        {
            "type": "curve",
            "data": {"x": x.tolist(), "y": y_basic.tolist()},
            "stroke": "#3498db",
            "stroke-width": 2
        },
        {
            "type": "curve",
            "data": {"x": x.tolist(), "y": y_transformed.tolist()},
            "stroke": "#e74c3c",
            "stroke-width": 3
        }
    ],
    "foreign_objects": [
        {
            "x": 1, "y": -2,
            "latex": r"y = \frac{1}{2}(x-1)^2 - 2",
            "width": 120,
            "height": 25
        }
    ]
}
```

All 40+ graphs follow this structure and are available in `src/pca_graph_viz/tests/graphs/`.

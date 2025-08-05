// ===== URL CONFIGURATION =====
const NAGINI_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/nagini.js';
const WORKER_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/pyodide/worker/worker-dist.js';
const PYTHON_FILES_BASE = `http://127.0.0.1:8022/`;

let manager;
let allGraphs = {};

async function main() {
    try {
        const { Nagini } = await import(NAGINI_PATH);

        const pythonFiles = [
            'src/pca_graph_viz/__init__.py',
            'src/pca_graph_viz/tests/__init__.py',
            'src/pca_graph_viz/core/__init__.py',
            'src/pca_graph_viz/core/svg_utils.py',
            'src/pca_graph_viz/core/color_utils.py',
            'src/pca_graph_viz/models/__init__.py',
            'src/pca_graph_viz/models/line_model.py',
            'src/pca_graph_viz/models/curve_model.py',
            'src/pca_graph_viz/models/line_object.py',
            'src/pca_graph_viz/models/foreign_object.py',
            'src/pca_graph_viz/tests/graphs/__init__.py',
            'src/pca_graph_viz/tests/graphs/graph1.py',
            'src/pca_graph_viz/tests/graphs/graph2.py',
            'src/pca_graph_viz/tests/graphs/graph3.py',
            'src/pca_graph_viz/tests/graphs/graph4.py',
            'src/pca_graph_viz/tests/graphs/graph5.py',
            'src/pca_graph_viz/tests/graphs/graph6.py',
            'src/pca_graph_viz/tests/graphs/graph7.py',
            'src/pca_graph_viz/tests/graphs/graph8.py',
            'src/pca_graph_viz/tests/graphs/graph9.py',
            'src/pca_graph_viz/tests/graphs/graph10.py',
            'src/pca_graph_viz/tests/graphs/graph11.py',
            'src/pca_graph_viz/tests/graphs/graph12.py',
            'src/pca_graph_viz/tests/graphs/graph13.py',
            'src/pca_graph_viz/tests/graphs/graph14.py',
            'src/pca_graph_viz/tests/graphs/graph15.py',
            'src/pca_graph_viz/tests/graphs/graph16.py',
            'src/pca_graph_viz/tests/graphs/graph17.py',
        ];

        const filesToLoad = pythonFiles.map(file => ({
            url: `${PYTHON_FILES_BASE}${file}`,
            path: file.replace('src/', '')
        }));

        console.log('🚀 Initializing Nagini with Pyodide backend...');
        manager = await Nagini.createManager(
            'pyodide',
            ["numpy", "svgwrite", "pydantic"],
            [],
            filesToLoad,
            WORKER_PATH
        );

        await Nagini.waitForReady(manager);
        console.log('✅ Nagini PyodideManager ready!');

        await loadAllGraphs();
        document.getElementById('loading').style.display = 'none';

        if (Object.keys(allGraphs).length > 0) {
            displayAllGraphs();
        } else {
            showError('No graphs were loaded successfully!');
        }

    } catch (error) {
        showError(`Initialization error: ${error.message}`);
        console.error(error);
    }
}

async function loadAllGraphs() {
    allGraphs = {};
    const graphNumbers = Array.from({ length: 17 }, (_, i) => i + 1);
    console.log('Loading graphs individually...');

    for (const num of graphNumbers) {
        const graphId = `graph${num}`;
        try {
            const namespace = { __name__: `graph${num}_namespace` };
            const result = await manager.executeAsync(`load_${graphId}.py`, `
import json
from pca_graph_viz.tests.graphs.graph${num} import get_graph_dict
graph_dict = get_graph_dict()
missive({"graph": graph_dict})
print("Loaded ${graphId} successfully!")
            `, namespace);

            if (result.missive) {
                const missiveData = typeof result.missive === 'string' ? JSON.parse(result.missive) : result.missive;
                if (missiveData.graph) {
                    allGraphs[graphId] = missiveData.graph;
                    console.log(`✅ Loaded ${graphId}: ${missiveData.graph.title || 'No title'}`);
                } else {
                    console.error(`No graph data in missive for ${graphId}:`, missiveData);
                }
            } else {
                console.error(`No missive in result for ${graphId}:`, result);
            }
        } catch (error) {
            console.error(`Error loading ${graphId}:`, error);
            showError(`Failed to load ${graphId}: ${error.message}`);
        }
    }
    console.log(`Total graphs loaded: ${Object.keys(allGraphs).length}`);
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error';
    errorDiv.textContent = message;
    document.getElementById('error-container').appendChild(errorDiv);
}

async function displayGraph(graphId, graphDict, container) {
    const row = document.createElement('div');
    row.className = 'graph-row';

    const svgContainer = document.createElement('div');
    svgContainer.className = 'graph-svg';
    svgContainer.innerHTML = `<div class="graph-title">${graphDict.title || graphId}</div>`;

    const jsonContainer = document.createElement('div');
    jsonContainer.className = 'graph-json';
    jsonContainer.innerHTML = `<div class="graph-title">JSON Entry Point</div><pre>${JSON.stringify(graphDict, null, 2)}</pre>`;

    row.appendChild(svgContainer);
    row.appendChild(jsonContainer);
    container.appendChild(row);

    try {
        const namespace = { __name__: `render_${graphId}_namespace` };
        const result = await manager.executeAsync(`render_${graphId}.py`, `
import json
from pca_graph_viz import graph_from_dict
graph_dict = json.loads(${JSON.stringify(JSON.stringify(graphDict))})
svg_output = graph_from_dict(graph_dict)
missive({"svg": svg_output})
print("Rendered ${graphId} successfully")
        `, namespace);

        if (result.error) {
            throw new Error(result.error.message);
        }

        console.log(result.stdout);
        const missiveData = typeof result.missive === 'string' ? JSON.parse(result.missive) : result.missive;
        const svg = missiveData.svg;
        const svgDiv = document.createElement('div');
        svgDiv.innerHTML = svg;
        svgContainer.appendChild(svgDiv);

        setTimeout(() => {
            const foreignObjects = svgContainer.querySelectorAll('foreignObject');
            foreignObjects.forEach(fo => {
                const divs = fo.querySelectorAll('div.svg-latex');
                divs.forEach(div => {
                    const latex = div.textContent.trim();
                    if (latex) {
                        try {
                            const originalBgColor = div.style.backgroundColor;
                            const originalColor = div.style.color;
                            div.innerHTML = '';
                            katex.render(latex, div, { throwOnError: false, displayMode: false });
                            if (originalBgColor) {
                                div.style.backgroundColor = originalBgColor;
                            }
                            if (originalColor) {
                                const katexElements = div.querySelectorAll('.katex, .katex *');
                                katexElements.forEach(el => {
                                    el.style.color = originalColor;
                                });
                            }
                        } catch (e) {
                            console.error('KaTeX error:', e);
                            div.textContent = latex;
                        }
                    }
                });
            });
        }, 100);

    } catch (error) {
        console.error(`Error displaying ${graphId}:`, error);
        svgContainer.innerHTML += `<div class="error">Error displaying ${graphId}: ${error.message}</div>`;
    }
}

async function displayAllGraphs() {
    const container = document.getElementById('graphs-container');
    container.innerHTML = '';

    if (!allGraphs || typeof allGraphs !== 'object') {
        showError('ERROR: Graphs data not loaded properly!');
        console.error('allGraphs is:', allGraphs);
        return;
    }

    const graphCount = Object.keys(allGraphs).length;
    if (graphCount !== 17) {
        showError(`WARNING: Expected 17 graphs but found ${graphCount}!`);
        console.error('Graphs loaded:', Object.keys(allGraphs));
    } else {
        console.log('✅ All 17 graphs loaded successfully!');
    }

    for (const [graphId, graphDict] of Object.entries(allGraphs)) {
        await displayGraph(graphId, graphDict, container);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, starting main()...');
    main().catch(error => {
        console.error('Fatal error in main:', error);
        showError(`Fatal error: ${error.message}`);
    });
});

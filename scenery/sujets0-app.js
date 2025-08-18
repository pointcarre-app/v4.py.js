// ===== URL CONFIGURATION =====
const NAGINI_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/nagini.js';
const WORKER_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/pyodide/worker/worker-dist.js';
const BUST = `v=${Date.now()}`;

// Automatically detect if running locally or on GitHub Pages
const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

// For GitHub Pages, we need absolute URLs for the worker
let PYTHON_FILES_BASE;
if (isLocal) {
    // Use current page origin to avoid localhost vs 127.0.0.1 CORS mismatches
    PYTHON_FILES_BASE = window.location.origin + '/';
} else {
    // Construct the absolute URL for GitHub Pages
    // We're at /v4.py.js/scenery/ and need to access /v4.py.js/src/
    PYTHON_FILES_BASE = 'https://pointcarre-app.github.io/v4.py.js/';
}

console.log('📍 Base URL for Python files:', PYTHON_FILES_BASE);
console.log('📍 Example file URL:', PYTHON_FILES_BASE + 'src/pca_graph_viz/__init__.py');

let manager;
let allGraphs = {};
// Per-graph headings/subtitles to render dynamically
const graphMeta = {
    graph_sujets0_spe_sujet1_automatismes_question7_canonical: {
        heading: '[1ere][sujets0][spé][sujet-1][automatismes][question-7]',
        subtitle: '_canonical.py',
    },
    graph_sujets0_spe_sujet1_automatismes_question7_small: {
        heading: '[1ere][sujets0][spé][sujet-1][automatismes][question-7]',
        subtitle: '_small.py',
    },
};

async function main() {
    try {
        const { Nagini } = await import(`${NAGINI_PATH}?${BUST}`);

        const pythonFiles = [
            'src/pca_graph_viz/__init__.py',
            'src/pca_graph_viz/core/__init__.py',
            'src/pca_graph_viz/core/svg_utils.py',
            'src/pca_graph_viz/core/color_utils.py',
            'src/pca_graph_viz/models/__init__.py',
            'src/pca_graph_viz/models/line_model.py',
            'src/pca_graph_viz/models/curve_model.py',
            'src/pca_graph_viz/models/line_object.py',
            'src/pca_graph_viz/models/foreign_object.py',
            // NOT loading test __init__ files to avoid circular imports
            // We'll fetch and exec the graph file directly instead
        ];

        const filesToLoad = pythonFiles.map(file => ({
            url: `${PYTHON_FILES_BASE}${file}?${BUST}`,
            path: file.replace('src/', '')
        }));

        console.log('📦 First file to load:', filesToLoad[0]);
        console.log('🚀 Initializing Nagini with Pyodide backend...');
        manager = await Nagini.createManager(
            'pyodide',
            ["numpy", "svgwrite", "pydantic"],
            [],
            filesToLoad,
            `${WORKER_PATH}?${BUST}`
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
    
    // Load multiple graphs by fetching and executing the files directly (avoid circular imports)
    console.log('Loading Question 7 graphs by fetching sources directly...');

    const graphsToLoad = [
        {
            file: 'graph_sujets0_spe_sujet1_automatismes_question7_canonical.py',
            key: 'graph_sujets0_spe_sujet1_automatismes_question7_canonical'
        },
        {
            file: 'graph_sujets0_spe_sujet1_automatismes_question7_small.py',
            key: 'graph_sujets0_spe_sujet1_automatismes_question7_small'
        }
    ];

    for (const entry of graphsToLoad) {
        const fileUrl = `${PYTHON_FILES_BASE}src/pca_graph_viz/tests/graphs/${entry.file}?${BUST}`;
        try {
            console.log('Fetching:', fileUrl);
            const response = await fetch(fileUrl, { cache: 'no-store' });
            if (!response.ok) {
                throw new Error(`HTTP ${response.status} for ${fileUrl}`);
            }
            const pythonSource = await response.text();
            console.log('Fetched Python source, length:', pythonSource.length);

            const sourceB64 = btoa(unescape(encodeURIComponent(pythonSource)));

            const namespace = { __name__: `load_${entry.key}_namespace` };
            const result = await manager.executeAsync(`load_${entry.key}.py`, `
import json
import traceback
import base64

try:
    # Decode and execute the fetched Python source in a namespace
    ns = {}
    source = base64.b64decode("${sourceB64}").decode("utf-8")
    
    # Execute the source
    exec(source, ns)
    
    # Check if get_graph_dict exists
    if 'get_graph_dict' not in ns:
        raise RuntimeError('get_graph_dict function not found in source')
    
    # Get the graph dictionary
    graph_dict = ns['get_graph_dict']()
    print(f"Got graph dict with title: {graph_dict.get('title', 'NO TITLE')}")
    
    # Send the graph dict
    missive({"graph": graph_dict})
    print("Loaded graph successfully!")
    
except Exception as e:
    error_msg = f"Python Error: {e}"
    print(error_msg)
    print(traceback.format_exc())
    try:
        missive({"error": str(e), "traceback": traceback.format_exc()})
    except:
        print("Could not send error through missive")
            `, namespace);

            // LOG EVERYTHING TO FIND THE ERROR
            console.log('🔍 FULL RESULT:', result);
            console.log('🔍 stdout:', result.stdout);
            console.log('🔍 stderr:', result.stderr);
            console.log('🔍 error:', result.error);
            console.log('🔍 missive:', result.missive);

            if (result.missive) {
                const missiveData = typeof result.missive === 'string' ? JSON.parse(result.missive) : result.missive;
                if (missiveData.error) {
                    console.error('📛 Python error from missive:', missiveData.error);
                    console.error('📛 Python traceback:', missiveData.traceback);
                    showError(`Python Error: ${missiveData.error}`);
                } else if (missiveData.graph) {
                    allGraphs[entry.key] = missiveData.graph;
                    console.log(`✅ Loaded graph: ${missiveData.graph.title || entry.key}`);
                } else {
                    console.error('No graph data in missive:', missiveData);
                }
            } else {
                console.error('No missive in result:', result);
                if (result.stderr) {
                    console.error('PYTHON STDERR:', result.stderr);
                    showError(`Python Error: ${result.stderr}`);
                }
                if (result.stdout) {
                    console.error('PYTHON STDOUT (might contain error info):', result.stdout);
                }
            }
        } catch (error) {
            console.error(`JavaScript error loading ${entry.file}:`, error);
            showError(`Failed to load ${entry.file}: ${error.message}`);
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
    // Dynamic per-graph heading/subtitle if provided
    const meta = graphMeta[graphId] || {};
    if (meta.heading || meta.subtitle) {
        const headerDiv = document.createElement('div');
        headerDiv.className = 'graph-header';
        headerDiv.innerHTML = `
            ${meta.heading ? `<h2>${meta.heading}</h2>` : ''}
            ${meta.subtitle ? `<p class="subtitle">${meta.subtitle}</p>` : ''}
        `;
        svgContainer.appendChild(headerDiv);
    }
    svgContainer.innerHTML += `<div class="graph-title">${graphDict.title || graphId}</div>`;

    const jsonContainer = document.createElement('div');
    jsonContainer.className = 'graph-json';
    jsonContainer.innerHTML = `<div class="graph-title" style="text-align: left;">JSON Entry Point</div><pre>${JSON.stringify(graphDict, null, 2)}</pre>`;

    row.appendChild(svgContainer);
    row.appendChild(jsonContainer);
    container.appendChild(row);

    try {
        // Ensure a reasonable default margin for padding if not provided
        try {
            graphDict.settings = graphDict.settings || {};
            if (typeof graphDict.settings.margin !== 'number') {
                graphDict.settings.margin = 16; // default padding around plot
            }
        } catch {}

        const namespace = { __name__: `render_${graphId}_namespace` };
        const result = await manager.executeAsync(`render_${graphId}.py`, `
import json, traceback
from pca_graph_viz import graph_from_dict
try:
    graph_dict = json.loads(${JSON.stringify(JSON.stringify(graphDict))})
    svg_output = graph_from_dict(graph_dict)
    missive({"svg": svg_output})
    print("Rendered ${graphId} successfully")
except Exception as e:
    err = str(e)
    tb = traceback.format_exc()
    print("PY RENDER ERROR:", err)
    print(tb)
    missive({"error": err, "traceback": tb})
        `, namespace);

        if (result.error) {
            console.error('🔴 Render error details:', result);
            console.error('🔴 Render stderr:', result.stderr);
            throw new Error(result.error.message || 'Pyodide execution error');
        }

        console.log(result.stdout);
        const missiveData = typeof result.missive === 'string' ? JSON.parse(result.missive) : result.missive;
        if (!missiveData || (!missiveData.svg && !missiveData.error)) {
            console.error('🔴 No SVG in missive:', missiveData);
            console.error('🔴 Full render result:', result);
            throw new Error('No SVG output from graph_from_dict');
        }
        if (missiveData && missiveData.error) {
            console.error('🔴 Python render error:', missiveData.error);
            if (missiveData.traceback) console.error(missiveData.traceback);
            throw new Error(missiveData.error);
        }
        const svg = missiveData.svg;
        const svgDiv = document.createElement('div');
        svgDiv.innerHTML = svg;
        const frameDiv = document.createElement('div');
        frameDiv.className = 'graph-svg-frame';
        frameDiv.appendChild(svgDiv);
        svgContainer.appendChild(frameDiv);

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
    const expectedCount = 2; // canonical + small
    if (graphCount !== expectedCount) {
        showError(`WARNING: Expected ${expectedCount} graph but found ${graphCount}!`);
        console.error('Graphs loaded:', Object.keys(allGraphs));
    } else {
        console.log(`✅ Graph loaded successfully!`);
    }

    let successCount = 0;
    let errorCount = 0;
    
    for (const [graphId, graphDict] of Object.entries(allGraphs)) {
        try {
            await displayGraph(graphId, graphDict, container);
            successCount++;
        } catch (error) {
            errorCount++;
            console.error(`Failed to display ${graphId}:`, error);
            // Create error placeholder for this graph
            const row = document.createElement('div');
            row.className = 'graph-row';
            row.innerHTML = `
                <div class="graph-svg">
                    <div class="graph-title">${graphDict.title || graphId}</div>
                    <div class="error">Failed to render: ${error.message}</div>
                </div>
                <div class="graph-json">
                    <div class="graph-title">JSON Entry Point</div>
                    <pre>${JSON.stringify(graphDict, null, 2)}</pre>
                </div>
            `;
            container.appendChild(row);
        }
    }
    
    console.log(`Rendering complete: ${successCount} successful, ${errorCount} failed`);
    if (errorCount > 0) {
        showError(`${errorCount} graph(s) failed to render. See individual errors above.`);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, starting main()...');
    main().catch(error => {
        console.error('Fatal error in main:', error);
        showError(`Fatal error: ${error.message}`);
    });
});
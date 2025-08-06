// ===== URL CONFIGURATION =====
const NAGINI_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/nagini.js';
const WORKER_PATH = 'https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.17/src/pyodide/worker/worker-dist.js';

// Automatically detect if running locally or on GitHub Pages
const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';

// For GitHub Pages, we need absolute URLs for the worker
let PYTHON_FILES_BASE;
if (isLocal) {
    PYTHON_FILES_BASE = 'http://127.0.0.1:8022/';
} else {
    // Construct the absolute URL for GitHub Pages
    // We're at /v4.py.js/scenery/ and need to access /v4.py.js/src/
    PYTHON_FILES_BASE = 'https://pointcarre-app.github.io/v4.py.js/';
}

console.log('📍 Base URL for Python files:', PYTHON_FILES_BASE);
console.log('📍 Example file URL:', PYTHON_FILES_BASE + 'src/pca_graph_viz/__init__.py');

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
            // New 1ere graphs
            'src/pca_graph_viz/tests/graphs/graph_1ere_coordinate_geometry_circle_equation_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_coordinate_geometry_distance_formula_illustration.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_coordinate_geometry_line_in_coordinate_system.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_derivatives_and_functions_derivative_graph_vs_original_function.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_derivatives_and_functions_function_variation_table.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_derivatives_tangent_line.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_exponential_function_exponential_comparison_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_exponential_function_exponential_growth_curve.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_exponential_function_logarithmic_scale_plot.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_function_transformations_reflection_and_stretching.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_function_transformations_translation_of_functions.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_probabilities_tree_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_probabilities_two_way_table.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_probabilities_venn_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_random_variables_and_statistics_box_plot.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_random_variables_and_statistics_cumulative_distribution_function.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_random_variables_and_statistics_histogram_with_normal_curve.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_random_variables_and_statistics_probability_distribution_bar_chart.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_scalar_product_and_geometry_circle_with_normal_vector.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_scalar_product_and_geometry_orthogonal_vectors_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_scalar_product_and_geometry_vector_scalar_product_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_second_degree_functions_canonical_form_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_second_degree_functions_parabola.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_second_degree_functions_sign_table_for_quadratic.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_sequences_arithmetic_sequence_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_sequences_geometric_sequence_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_sequences_recursive_sequence_cobweb_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_sequences_sequence_term_plot.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_3d_coordinate_system_preview.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_asymptote_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_function_composition_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_inequality_region_shading.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_integration_as_area.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_newton_s_method_iteration.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_optimization_problem_diagram.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_parametric_curve_plot.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_piecewise_function_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_special_topics_related_rates_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_trigonometry_angle_wrapping_visualization.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_trigonometry_cosine_function_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_trigonometry_sine_function_graph.py',
            'src/pca_graph_viz/tests/graphs/graph_1ere_trigonometry_unit_circle_with_angles.py',
        ];

        const filesToLoad = pythonFiles.map(file => ({
            url: `${PYTHON_FILES_BASE}${file}`,
            path: file.replace('src/', '')
        }));

        console.log('📦 First file to load:', filesToLoad[0]);
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
    
    // Load original graphs (graph1 to graph17)
    const graphNumbers = Array.from({ length: 17 }, (_, i) => i + 1);
    console.log('Loading original graphs...');

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
    
    // Load new 1ere graphs
    const graph1ereModules = [
        'graph_1ere_coordinate_geometry_circle_equation_visualization',
        'graph_1ere_coordinate_geometry_distance_formula_illustration',
        'graph_1ere_coordinate_geometry_line_in_coordinate_system',
        'graph_1ere_derivatives_and_functions_derivative_graph_vs_original_function',
        'graph_1ere_derivatives_and_functions_function_variation_table',
        'graph_1ere_derivatives_tangent_line',
        'graph_1ere_exponential_function_exponential_comparison_graph',
        'graph_1ere_exponential_function_exponential_growth_curve',
        'graph_1ere_exponential_function_logarithmic_scale_plot',
        'graph_1ere_function_transformations_reflection_and_stretching',
        'graph_1ere_function_transformations_translation_of_functions',
        'graph_1ere_probabilities_tree_diagram',
        'graph_1ere_probabilities_two_way_table',
        'graph_1ere_probabilities_venn_diagram',
        'graph_1ere_random_variables_and_statistics_box_plot',
        'graph_1ere_random_variables_and_statistics_cumulative_distribution_function',
        'graph_1ere_random_variables_and_statistics_histogram_with_normal_curve',
        'graph_1ere_random_variables_and_statistics_probability_distribution_bar_chart',
        'graph_1ere_scalar_product_and_geometry_circle_with_normal_vector',
        'graph_1ere_scalar_product_and_geometry_orthogonal_vectors_diagram',
        'graph_1ere_scalar_product_and_geometry_vector_scalar_product_visualization',
        'graph_1ere_second_degree_functions_canonical_form_visualization',
        'graph_1ere_second_degree_functions_parabola',
        'graph_1ere_second_degree_functions_sign_table_for_quadratic',
        'graph_1ere_sequences_arithmetic_sequence_graph',
        'graph_1ere_sequences_geometric_sequence_graph',
        'graph_1ere_sequences_recursive_sequence_cobweb_diagram',
        'graph_1ere_sequences_sequence_term_plot',
        'graph_1ere_special_topics_3d_coordinate_system_preview',
        'graph_1ere_special_topics_asymptote_visualization',
        'graph_1ere_special_topics_function_composition_diagram',
        'graph_1ere_special_topics_inequality_region_shading',
        'graph_1ere_special_topics_integration_as_area',
        'graph_1ere_special_topics_newton_s_method_iteration',
        'graph_1ere_special_topics_optimization_problem_diagram',
        'graph_1ere_special_topics_parametric_curve_plot',
        'graph_1ere_special_topics_piecewise_function_graph',
        'graph_1ere_special_topics_related_rates_visualization',
        'graph_1ere_trigonometry_angle_wrapping_visualization',
        'graph_1ere_trigonometry_cosine_function_graph',
        'graph_1ere_trigonometry_sine_function_graph',
        'graph_1ere_trigonometry_unit_circle_with_angles',
    ];
    
    console.log('Loading 1ere graphs...');
    
    // Add a small delay to ensure all files are properly loaded
    await new Promise(resolve => setTimeout(resolve, 100));
    
    for (const moduleName of graph1ereModules) {
        try {
            const namespace = { __name__: `${moduleName}_namespace` };
            const pythonCode = `
import json
import sys
print(f"Attempting to load module: ${moduleName}")
try:
    from pca_graph_viz.tests.graphs.${moduleName} import get_graph_dict
    graph_dict = get_graph_dict()
    print(f"Successfully got graph dict for ${moduleName}")
    missive({"graph": graph_dict})
except ImportError as e:
    import traceback
    error_msg = f"Import error in ${moduleName}: {str(e)}"
    print(error_msg)
    print(traceback.format_exc())
    missive({"error": error_msg})
except Exception as e:
    import traceback
    error_msg = f"Error in ${moduleName}: {str(e)}"
    print(error_msg)
    print(traceback.format_exc())
    missive({"error": error_msg})
            `;
            const result = await manager.executeAsync(`load_${moduleName}.py`, pythonCode, namespace);

            if (result.missive) {
                const missiveData = typeof result.missive === 'string' ? JSON.parse(result.missive) : result.missive;
                if (missiveData.error) {
                    console.error(`Python error in ${moduleName}:`, missiveData.error);
                    showError(`Python error in ${moduleName}: ${missiveData.error}`);
                } else if (missiveData.graph) {
                    allGraphs[moduleName] = missiveData.graph;
                    console.log(`✅ Loaded ${moduleName}: ${missiveData.graph.title || 'No title'}`);
                } else {
                    console.error(`No graph data in missive for ${moduleName}:`, missiveData);
                }
            } else {
                console.error(`No missive in result for ${moduleName}:`, result);
                if (result.stderr) {
                    console.error(`stderr:`, result.stderr);
                }
            }
        } catch (error) {
            console.error(`JavaScript error loading ${moduleName}:`, error);
            showError(`Failed to load ${moduleName}: ${error.message}`);
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
    const expectedCount = 59; // 17 original + 42 new 1ere graphs
    if (graphCount !== expectedCount) {
        showError(`WARNING: Expected ${expectedCount} graphs but found ${graphCount}!`);
        console.error('Graphs loaded:', Object.keys(allGraphs));
    } else {
        console.log(`✅ All ${expectedCount} graphs loaded successfully!`);
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

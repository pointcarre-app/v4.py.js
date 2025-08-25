// ===== URL CONFIGURATION =====
const NAGINI_PATH =
  "https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/nagini.js";
const WORKER_PATH =
  "https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/pyodide/worker/worker-dist.js";

// Automatically detect if running locally or on GitHub Pages
const isLocal =
  window.location.hostname === "localhost" ||
  window.location.hostname === "127.0.0.1";

// For GitHub Pages, we need absolute URLs for the worker
let PYTHON_FILES_BASE;
if (isLocal) {
  // Use current page origin to avoid localhost vs 127.0.0.1 CORS mismatches
  PYTHON_FILES_BASE = window.location.origin + "/";
} else {
  // Construct the absolute URL for GitHub Pages
  // We're at /v4.py.js/scenery/ and need to access /v4.py.js/src/
  PYTHON_FILES_BASE = "https://pointcarre-app.github.io/v4.py.js/";
}

console.log("📍 Base URL for Python files:", PYTHON_FILES_BASE);
console.log(
  "📍 Example file URL:",
  PYTHON_FILES_BASE + "src/pca_graph_viz/__init__.py"
);

let manager;
let allGraphs = {};
// Per-graph headings/subtitles to render dynamically
const graphMeta = {
  // Optional per-graph headings for display; keys must match graphId used below (entry.key)
  "spe_sujet1_auto_08_question_canonical.py": {
    heading: "[1ere][sujets0][spé][sujet-1][automatismes][question-8]",
    subtitle: "_canonical.py",
  },
  "spe_sujet1_auto_08_question_small.py": {
    heading: "[1ere][sujets0][spé][sujet-1][automatismes][question-8]",
    subtitle: "_small.py",
  },
};

async function main() {
  try {
    const { Nagini } = await import(`${NAGINI_PATH}`);

    // Define all graph modules to load
    const graphModules = [
      "spe_sujet1_auto_07_question_canonical",
      "spe_sujet1_auto_07_question_small",
      "spe_sujet1_auto_08_question_canonical",
      "spe_sujet1_auto_08_question_small",
      "spe_sujet1_auto_11_case_a_question_canonical",
      "spe_sujet1_auto_11_case_a_question_small",
      "spe_sujet1_auto_11_case_b_question_canonical",
      "spe_sujet1_auto_11_case_b_question_small",
      "spe_sujet1_auto_11_case_c_question_canonical",
      "spe_sujet1_auto_11_case_c_question_small",
      "spe_sujet1_auto_10_question_small_parabola_a_s1_a_0",
      "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m",
      "spe_sujet1_auto_10_question_small_parabola_a_s1_a_p",
      "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_0",
      "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m",
      "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p10",
    ];

    // First load core modules and dispatch
    const coreFiles = [
      // Core modules
      "src/pca_graph_viz/__init__.py",
      "src/pca_graph_viz/core/__init__.py",
      "src/pca_graph_viz/core/svg_utils.py",
      "src/pca_graph_viz/core/color_utils.py",
      "src/pca_graph_viz/core/nagini_adapter.py",  // Our new adapter
      // Model modules
      "src/pca_graph_viz/models/__init__.py",
      "src/pca_graph_viz/models/line_model.py",
      "src/pca_graph_viz/models/curve_model.py",
      "src/pca_graph_viz/models/line_object.py",
      "src/pca_graph_viz/models/foreign_object.py",
    ];
    
    // Graph modules that depend on dispatch - exclude the ones that import from dispatch
    const graphsWithDispatch = graphModules.filter(m => 
      m.includes("parabola_a_s") || m.includes("parabola_a_sm")
    );
    
    const graphsWithoutDispatch = graphModules.filter(m => 
      !m.includes("parabola_a_s") && !m.includes("parabola_a_sm")
    );
    
    // Load core files first, then non-dispatch graphs, then dispatch, then dispatch-dependent graphs
    const pythonFiles = [
      ...coreFiles,
      ...graphsWithoutDispatch.map(m => `src/pca_graph_viz/tests/graphs/${m}.py`),
      "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_dispatch.py",
      ...graphsWithDispatch.map(m => `src/pca_graph_viz/tests/graphs/${m}.py`)
    ];

    const filesToLoad = pythonFiles.map((file) => ({
      url: `${PYTHON_FILES_BASE}${file}`,
      path: file.replace("src/", ""),
    }));

    console.log("📦 Loading modules count:", filesToLoad.length);
    console.log("🚀 Initializing Nagini with Pyodide backend...");
    manager = await Nagini.createManager(
      "pyodide",
      ["numpy", "svgwrite", "pydantic"],
      [],
      filesToLoad,
      `${WORKER_PATH}`
    );

    await Nagini.waitForReady(manager);
    console.log("✅ Nagini PyodideManager ready!");
    
    // Initialize the adapter
    console.log("📝 Initializing package structure...");
    await manager.executeAsync("init_adapter.py", `
from pca_graph_viz.core.nagini_adapter import ensure_package_structure
ensure_package_structure()
print("✅ Package structure initialized")
    `);
    
    // Store graph modules for use in loadAllGraphs
    window.graphModules = graphModules;

    await loadAllGraphs();
    document.getElementById("loading").style.display = "none";

    if (Object.keys(allGraphs).length > 0) {
      displayAllGraphs();
    } else {
      showError("No graphs were loaded successfully!");
    }
  } catch (error) {
    showError(`Initialization error: ${error.message}`);
    console.error(error);
  }
}

async function loadAllGraphs() {
  allGraphs = {};

  console.log("Loading graphs from pre-loaded modules...");

  // Use the graphModules from main()
  const graphModules = window.graphModules;

  // Now import and get graphs from each module
  for (const moduleName of graphModules) {
    try {
      const key = `${moduleName}.py`;
      console.log(`Loading graph from module: ${moduleName}`);
      
      const result = await manager.executeAsync(
        `load_${moduleName}.py`,
        `
from pca_graph_viz.core.nagini_adapter import load_and_send_graph
load_and_send_graph("${moduleName}")
        `
      );

      if (result.missive) {
        const missiveData =
          typeof result.missive === "string"
            ? JSON.parse(result.missive)
            : result.missive;
        if (missiveData.error) {
          console.error(`📛 Error loading ${moduleName}:`, missiveData.error);
          showError(`Error loading ${moduleName}: ${missiveData.error}`);
        } else if (missiveData.graph) {
          allGraphs[key] = missiveData.graph;
          console.log(
            `✅ Loaded graph: ${missiveData.graph.title || key}`
          );
        }
      } else {
        console.error(`No missive result for ${moduleName}`);
      }
    } catch (error) {
      console.error(`JavaScript error loading ${moduleName}:`, error);
      showError(`Failed to load ${moduleName}: ${error.message}`);
    }
  }

  console.log(`Total graphs loaded: ${Object.keys(allGraphs).length}`);
}

function showError(message) {
  const errorDiv = document.createElement("div");
  errorDiv.className = "error";
  errorDiv.textContent = message;
  document.getElementById("error-container").appendChild(errorDiv);
}

async function displayGraph(graphId, graphDict, container) {
  const row = document.createElement("div");
  row.className = "graph-row";

  const svgContainer = document.createElement("div");
  svgContainer.className = "graph-svg";
  // Dynamic per-graph heading/subtitle if provided
  const meta = graphMeta[graphId] || {};
  if (meta.heading || meta.subtitle) {
    const headerDiv = document.createElement("div");
    headerDiv.className = "graph-header";
    headerDiv.innerHTML = `
            ${meta.heading ? `<h2>${meta.heading}</h2>` : ""}
            ${meta.subtitle ? `<p class="subtitle">${meta.subtitle}</p>` : ""}
        `;
    svgContainer.appendChild(headerDiv);
  }
  svgContainer.innerHTML += `<div class="graph-title">${
    graphDict.title || graphId
  }</div>`;

  const jsonContainer = document.createElement("div");
  jsonContainer.className = "graph-json";
  jsonContainer.innerHTML = `<div class="graph-title" style="text-align: left;">JSON Entry Point</div><pre>${JSON.stringify(
    graphDict,
    null,
    2
  )}</pre>`;

  row.appendChild(svgContainer);
  row.appendChild(jsonContainer);
  container.appendChild(row);

  try {
    const result = await manager.executeAsync(
      `render_${graphId}.py`,
      `
from pca_graph_viz.core.nagini_adapter import render_and_send_graph
render_and_send_graph(${JSON.stringify(JSON.stringify(graphDict))})
        `
    );

    if (result.error) {
      console.error("🔴 Render error details:", result);
      console.error("🔴 Render stderr:", result.stderr);
      throw new Error(result.error.message || "Pyodide execution error");
    }

    console.log(result.stdout);
    const missiveData =
      typeof result.missive === "string"
        ? JSON.parse(result.missive)
        : result.missive;
    if (!missiveData || (!missiveData.svg && !missiveData.error)) {
      console.error("🔴 No SVG in missive:", missiveData);
      console.error("🔴 Full render result:", result);
      throw new Error("No SVG output from graph_from_dict");
    }
    if (missiveData && missiveData.error) {
      console.error("🔴 Python render error:", missiveData.error);
      if (missiveData.traceback) console.error(missiveData.traceback);
      throw new Error(missiveData.error);
    }
    const svg = missiveData.svg;
    const svgDiv = document.createElement("div");
    svgDiv.innerHTML = svg;
    const frameDiv = document.createElement("div");
    frameDiv.className = "graph-svg-frame";
    frameDiv.appendChild(svgDiv);
    svgContainer.appendChild(frameDiv);

    setTimeout(() => {
      const foreignObjects = svgContainer.querySelectorAll("foreignObject");
      foreignObjects.forEach((fo) => {
        const divs = fo.querySelectorAll("div.svg-latex");
        divs.forEach((div) => {
          const latex = div.textContent.trim();
          if (latex) {
            try {
              const originalBgColor = div.style.backgroundColor;
              const originalColor = div.style.color;
              div.innerHTML = "";
              katex.render(latex, div, {
                throwOnError: false,
                displayMode: false,
              });
              if (originalBgColor) {
                div.style.backgroundColor = originalBgColor;
              }
              if (originalColor) {
                const katexElements = div.querySelectorAll(".katex, .katex *");
                katexElements.forEach((el) => {
                  el.style.color = originalColor;
                });
              }
            } catch (e) {
              console.error("KaTeX error:", e);
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
  const container = document.getElementById("graphs-container");
  container.innerHTML = "";

  if (!allGraphs || typeof allGraphs !== "object") {
    showError("ERROR: Graphs data not loaded properly!");
    console.error("allGraphs is:", allGraphs);
    return;
  }

  const graphCount = Object.keys(allGraphs).length;
  const expectedCount = 20;
  if (graphCount !== expectedCount) {
    showError(
      `WARNING: Expected ${expectedCount} graphs but found ${graphCount}!`
    );
    console.error("Graphs loaded:", Object.keys(allGraphs));
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
      const row = document.createElement("div");
      row.className = "graph-row";
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

  console.log(
    `Rendering complete: ${successCount} successful, ${errorCount} failed`
  );
  if (errorCount > 0) {
    showError(
      `${errorCount} graph(s) failed to render. See individual errors above.`
    );
  }
}

window.addEventListener("DOMContentLoaded", () => {
  console.log("DOM loaded, starting main()...");
  main().catch((error) => {
    console.error("Fatal error in main:", error);
    showError(`Fatal error: ${error.message}`);
  });
});

// ===== HARDCODED URL CONFIGURATION =====
// Using CDN URLs as recommended by Nagini documentation
const NAGINI_CDN_PATH = "https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/nagini.js";
const WORKER_CDN_PATH = "https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21/src/pyodide/worker/worker-dist.js";

// Detect if running locally or on GitHub Pages
const IS_LOCAL = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";
const BASE_URL = IS_LOCAL 
  ? `http://${window.location.hostname}:${window.location.port}`
  : "https://pointcarre-app.github.io/v4.py.js";

console.log("📍 Running in:", IS_LOCAL ? "LOCAL mode" : "GITHUB PAGES mode");
console.log("📍 Base URL:", BASE_URL);

let manager;
let allGraphs = {};

// Hardcoded list of essential files only
const ESSENTIAL_FILES = [
  "src/pca_graph_viz/__init__.py",
  "src/pca_graph_viz/core/__init__.py",
  "src/pca_graph_viz/core/svg_utils.py",
  "src/pca_graph_viz/core/color_utils.py",
  "src/pca_graph_viz/core/nagini_adapter.py",
  "src/pca_graph_viz/models/__init__.py",
  "src/pca_graph_viz/models/line_model.py",
  "src/pca_graph_viz/models/curve_model.py",
  "src/pca_graph_viz/models/line_object.py",
  "src/pca_graph_viz/models/foreign_object.py",
];

// Hardcoded graph files - load these separately
const GRAPH_FILES = {
  // Question 7
  "q7_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_07_question_canonical.py",
  "q7_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_07_question_small.py",
  
  // Question 8  
  "q8_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_08_question_canonical.py",
  "q8_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_08_question_small.py",
  
  // Dispatch module (needed by parabola graphs)
  "dispatch": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_dispatch.py",
  
  // Parabola graphs with s=1
  "parabola_s1_a0": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_0.py",
  "parabola_s1_am5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_m5.py",
  "parabola_s1_am10": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_m10.py",
  "parabola_s1_ap5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_p5.py",
  "parabola_s1_ap10": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_p10.py",
  
  // Parabola graphs with s=-1
  "parabola_sm1_a0": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_0.py",
  "parabola_sm1_am5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m5.py",
  "parabola_sm1_am10": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m10.py",
  "parabola_sm1_ap5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p5.py",
  "parabola_sm1_ap10": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p10.py",
};

async function initializeNagini() {
  try {
    console.log("🚀 Loading Nagini from CDN...");
    const { Nagini } = await import(NAGINI_CDN_PATH);
    
    // Load only essential files first
    const essentialFilesToLoad = ESSENTIAL_FILES.map(file => ({
      url: `${BASE_URL}/${file}`,
      path: file.replace("src/", ""),
    }));
    
    console.log("📦 Loading essential files:", essentialFilesToLoad.length);
    
    // Create manager with essential files only
    manager = await Nagini.createManager(
      "pyodide",
      ["numpy", "svgwrite", "pydantic"],
      [],
      essentialFilesToLoad,
      WORKER_CDN_PATH
    );
    
    await Nagini.waitForReady(manager);
    console.log("✅ Nagini ready with essential files!");
    
    // Initialize package structure
    await manager.executeAsync("init_packages.py", `
import sys
import types

# Create empty package modules
packages = [
    'pca_graph_viz.tests',
    'pca_graph_viz.tests.graphs'
]

for pkg in packages:
    if pkg not in sys.modules:
        mod = types.ModuleType(pkg)
        mod.__path__ = [pkg.replace('.', '/')]
        sys.modules[pkg] = mod
        print(f"Created package: {pkg}")

# Add graphs directory to path for relative imports
sys.path.insert(0, '/home/pyodide/pca_graph_viz/tests/graphs')

# Also add to Python's import path for relative imports
import os
if os.path.exists('/home/pyodide/pca_graph_viz/tests/graphs'):
    if '/home/pyodide/pca_graph_viz/tests/graphs' not in sys.path:
        sys.path.insert(0, '/home/pyodide/pca_graph_viz/tests/graphs')
        
print("✅ Package structure initialized")
    `);
    
    return true;
  } catch (error) {
    console.error("❌ Failed to initialize Nagini:", error);
    showError(`Failed to initialize: ${error.message}`);
    return false;
  }
}

async function loadGraphFile(key, filepath) {
  try {
    const url = `${BASE_URL}/${filepath}`;
    console.log(`📥 Loading ${key} from ${url}`);
    
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    
    const code = await response.text();
    const filename = filepath.split('/').pop();
    const moduleName = filename.replace('.py', '');
    
    // Convert to base64 to avoid escaping issues
    const codeBase64 = btoa(unescape(encodeURIComponent(code)));
    
    // Write the file using Python directly (more reliable than fs API)
    const result = await manager.executeAsync(`write_${key}.py`, `
import os
import base64
import sys
import types

# Decode the Python code from base64
code_b64 = "${codeBase64}"
code = base64.b64decode(code_b64).decode('utf-8')

# Ensure directory exists
os.makedirs('/home/pyodide/pca_graph_viz/tests/graphs', exist_ok=True)

# Write the file
filepath = '/home/pyodide/pca_graph_viz/tests/graphs/${filename}'
with open(filepath, 'w') as f:
    f.write(code)

print(f"✅ Written {len(code)} bytes to {filepath}")

# Make it importable by adding to sys.modules
module_name = '${moduleName}'
full_module_name = f'pca_graph_viz.tests.graphs.{module_name}'

# Create module object
module = types.ModuleType(full_module_name)
module.__file__ = filepath
module.__name__ = full_module_name
module.__package__ = 'pca_graph_viz.tests.graphs'

# Add the module's directory to its namespace for relative imports
module.__dict__['__file__'] = filepath
module.__dict__['__name__'] = full_module_name
module.__dict__['__package__'] = 'pca_graph_viz.tests.graphs'

# Try to execute the code in the module's namespace
try:
    exec(code, module.__dict__)
    # Register in sys.modules (both full name and short name for relative imports)
    sys.modules[full_module_name] = module
    sys.modules[module_name] = module  # Also register with short name for relative imports
    print(f"✅ Registered module: {full_module_name} and {module_name}")
except Exception as e:
    print(f"⚠️ Warning: Failed to execute module {module_name}: {e}")
    # Still register the module even if exec failed, it might be importable later
    sys.modules[full_module_name] = module
    sys.modules[module_name] = module
    `);
    
    if (result.error) {
      throw new Error(result.error.message || "Failed to write file");
    }
    
    console.log(`✅ Loaded ${key} -> ${filename}`);
    return true;
  } catch (error) {
    console.error(`❌ Failed to load ${key}:`, error);
    return false;
  }
}

async function loadAllGraphFiles() {
  console.log("📂 Loading graph files sequentially...");
  
  let successCount = 0;
  let failureCount = 0;
  
  // Load dispatch first (required by parabola graphs)
  try {
    if (await loadGraphFile("dispatch", GRAPH_FILES.dispatch)) {
      successCount++;
    } else {
      failureCount++;
    }
  } catch (e) {
    console.error("Failed to load dispatch:", e);
    failureCount++;
  }
  
  // Load question 7 & 8 graphs
  for (const [key, path] of Object.entries(GRAPH_FILES)) {
    if (key.startsWith("q7") || key.startsWith("q8")) {
      try {
        if (await loadGraphFile(key, path)) {
          successCount++;
        } else {
          failureCount++;
        }
      } catch (e) {
        console.error(`Failed to load ${key}:`, e);
        failureCount++;
      }
    }
  }
  
  // Load parabola graphs
  for (const [key, path] of Object.entries(GRAPH_FILES)) {
    if (key.startsWith("parabola")) {
      try {
        if (await loadGraphFile(key, path)) {
          successCount++;
        } else {
          failureCount++;
        }
      } catch (e) {
        console.error(`Failed to load ${key}:`, e);
        failureCount++;
      }
    }
  }
  
  console.log(`✅ Graph files loaded: ${successCount} success, ${failureCount} failed`);
}

async function getGraphDict(moduleName) {
  try {
    console.log(`🔍 Getting graph from ${moduleName}`);
    
    const result = await manager.executeAsync(`get_${moduleName}.py`, `
import json
import traceback
import sys

try:
    # The module should already be in sys.modules from loadGraphFile
    module_name = '${moduleName}'
    full_module_name = f'pca_graph_viz.tests.graphs.{module_name}'
    
    if full_module_name in sys.modules:
        module = sys.modules[full_module_name]
        print(f"Found module {full_module_name} in sys.modules")
    else:
        # Try to import it if not already loaded
        from importlib import import_module
        module = import_module(full_module_name)
        print(f"Imported module {full_module_name}")
    
    # Get graph dict
    if hasattr(module, 'get_graph_dict'):
        graph_dict = module.get_graph_dict()
        missive({"graph": graph_dict, "title": graph_dict.get('title', '${moduleName}')})
    else:
        raise RuntimeError(f'get_graph_dict not found in {full_module_name}')
except Exception as e:
    missive({"error": str(e), "traceback": traceback.format_exc()})
    `);
    
    if (result.missive) {
      const data = typeof result.missive === "string" 
        ? JSON.parse(result.missive) 
        : result.missive;
      
      if (data.error) {
        console.error(`❌ Error getting ${moduleName}:`, data.error);
        return null;
      }
      
      return data.graph;
    }
    
    return null;
  } catch (error) {
    console.error(`❌ Failed to get graph ${moduleName}:`, error);
    return null;
  }
}

async function loadGraphs() {
  allGraphs = {};
  
  // Define the module names to load
  const graphModules = [
    "spe_sujet1_auto_07_question_canonical",
    "spe_sujet1_auto_07_question_small",
    "spe_sujet1_auto_08_question_canonical",
    "spe_sujet1_auto_08_question_small",
    "spe_sujet1_auto_10_question_small_parabola_a_s1_a_0",
    "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m5",
    "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m10",
    "spe_sujet1_auto_10_question_small_parabola_a_s1_a_p5",
    "spe_sujet1_auto_10_question_small_parabola_a_s1_a_p10",
    "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_0",
    "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m5",
    "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m10",
    "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p5",
    "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p10",
  ];
  
  let successCount = 0;
  let failureCount = 0;
  
  for (const moduleName of graphModules) {
    try {
      const graph = await getGraphDict(moduleName);
      if (graph) {
        allGraphs[`${moduleName}.py`] = graph;
        console.log(`✅ Loaded graph: ${moduleName}`);
        successCount++;
      } else {
        console.log(`⚠️ Failed to get graph: ${moduleName}`);
        failureCount++;
      }
    } catch (error) {
      console.error(`❌ Error loading graph ${moduleName}:`, error);
      failureCount++;
    }
  }
  
  console.log(`📊 Graphs loaded: ${successCount} success, ${failureCount} failed`);
  console.log(`📊 Total graphs available: ${Object.keys(allGraphs).length}`);
}

function showError(message) {
  const errorDiv = document.createElement("div");
  errorDiv.className = "error";
  errorDiv.textContent = message;
  document.getElementById("error-container").appendChild(errorDiv);
}

async function renderGraph(graphId, graphDict) {
  try {
    const result = await manager.executeAsync(`render_${graphId}.py`, `
import json
from pca_graph_viz import graph_from_dict

try:
    graph_dict = json.loads('''${JSON.stringify(graphDict)}''')
    
    # Ensure defaults
    if 'settings' not in graph_dict:
        graph_dict['settings'] = {}
    if 'margin' not in graph_dict['settings']:
        graph_dict['settings']['margin'] = 16
    
    svg_output = graph_from_dict(graph_dict)
    missive({"svg": svg_output})
except Exception as e:
    import traceback
    missive({"error": str(e), "traceback": traceback.format_exc()})
    `);
    
    if (result.missive) {
      const data = typeof result.missive === "string" 
        ? JSON.parse(result.missive) 
        : result.missive;
      
      if (data.error) {
        throw new Error(data.error);
      }
      
      return data.svg;
    }
    
    throw new Error("No SVG output");
  } catch (error) {
    console.error(`❌ Render error for ${graphId}:`, error);
    throw error;
  }
}

async function displayGraph(graphId, graphDict, container) {
  const row = document.createElement("div");
  row.className = "graph-row";
  
  const svgContainer = document.createElement("div");
  svgContainer.className = "graph-svg";
  svgContainer.innerHTML = `<div class="graph-title">${graphDict.title || graphId}</div>`;
  
  const jsonContainer = document.createElement("div");
  jsonContainer.className = "graph-json";
  jsonContainer.innerHTML = `
    <div class="graph-title">JSON Entry Point</div>
    <pre>${JSON.stringify(graphDict, null, 2)}</pre>
  `;
  
  row.appendChild(svgContainer);
  row.appendChild(jsonContainer);
  container.appendChild(row);
  
  try {
    const svg = await renderGraph(graphId, graphDict);
    
    const svgDiv = document.createElement("div");
    svgDiv.innerHTML = svg;
    
    const frameDiv = document.createElement("div");
    frameDiv.className = "graph-svg-frame";
    frameDiv.appendChild(svgDiv);
    svgContainer.appendChild(frameDiv);
    
    // Render LaTeX
    setTimeout(() => {
      const foreignObjects = svgContainer.querySelectorAll("foreignObject");
      foreignObjects.forEach((fo) => {
        const divs = fo.querySelectorAll("div.svg-latex");
        divs.forEach((div) => {
          const latex = div.textContent.trim();
          if (latex && typeof katex !== 'undefined') {
            try {
              const bgColor = div.style.backgroundColor;
              const color = div.style.color;
              div.innerHTML = "";
              katex.render(latex, div, {
                throwOnError: false,
                displayMode: false,
              });
              if (bgColor) div.style.backgroundColor = bgColor;
              if (color) {
                div.querySelectorAll(".katex, .katex *").forEach(el => {
                  el.style.color = color;
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
    svgContainer.innerHTML += `<div class="error">Error: ${error.message}</div>`;
  }
}

async function displayAllGraphs() {
  const container = document.getElementById("graphs-container");
  container.innerHTML = "";
  
  for (const [graphId, graphDict] of Object.entries(allGraphs)) {
    await displayGraph(graphId, graphDict, container);
  }
  
  console.log(`✅ Displayed ${Object.keys(allGraphs).length} graphs`);
}

async function main() {
  try {
    document.getElementById("loading").textContent = "Initializing Nagini...";
    
    const initialized = await initializeNagini();
    if (!initialized) {
      throw new Error("Failed to initialize Nagini");
    }
    
    document.getElementById("loading").textContent = "Loading graph files...";
    await loadAllGraphFiles();
    
    document.getElementById("loading").textContent = "Processing graphs...";
    await loadGraphs();
    
    document.getElementById("loading").style.display = "none";
    
    const graphCount = Object.keys(allGraphs).length;
    if (graphCount > 0) {
      console.log(`📈 Displaying ${graphCount} graphs...`);
      await displayAllGraphs();
      
      // Show warning if some graphs failed
      if (graphCount < 14) {
        showError(`⚠️ Only ${graphCount} of 14 graphs loaded successfully. Some graphs may have import errors.`);
      }
    } else {
      showError("❌ No graphs were loaded! Check console for errors.");
    }
  } catch (error) {
    console.error("Fatal error:", error);
    showError(`Fatal error: ${error.message}`);
    document.getElementById("loading").style.display = "none";
  }
}

// Start when DOM is ready
window.addEventListener("DOMContentLoaded", () => {
  console.log("🎯 Starting SUJETS0 Graphs (Simple Version)");
  main().catch(error => {
    console.error("Unhandled error:", error);
    showError(`Unhandled error: ${error.message}`);
  });
});

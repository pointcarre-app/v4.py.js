/**
 * PCAGraphLoader - A modular, reusable graph loading system for PCA visualizations
 * 
 * Usage:
 * ```javascript
 * const loader = new PCAGraphLoader({
 *   baseUrl: 'auto', // or specific URL
 *   graphConfig: {
 *     Y_LABEL_FOR_HORIZONTAL_LINE: 10,
 *     A_FLOAT_FOR_AFFINE_LINE: 0.75,
 *     B_FLOAT_FOR_AFFINE_LINE: 2.0,
 *     A_SHIFT_MAGNITUDE: 5
 *   }
 * });
 * 
 * await loader.initialize();
 * const svg = await loader.renderGraph('q8_small');
 * ```
 */

export class PCAGraphLoader {
  constructor(options = {}) {
    // Configuration options
    this.options = {
      naginiVersion: options.naginiVersion || '0.0.21',
      pcaVersion: options.pcaVersion || 'v0.0.15-unstable',
      baseUrl: options.baseUrl || 'auto',
      graphConfig: options.graphConfig || {},
      debug: options.debug !== undefined ? options.debug : true,
      ...options
    };

    // Set up URLs based on environment
    this._setupUrls();

    // Initialize properties
    this.manager = null;
    this.initialized = false;
    this.loadedGraphs = new Map();
    
    // Graph configuration with defaults
    this.graphConfig = {
      Y_LABEL_FOR_HORIZONTAL_LINE: 10,
      A_FLOAT_FOR_AFFINE_LINE: 0.75,
      B_FLOAT_FOR_AFFINE_LINE: 2.0,
      A_SHIFT_MAGNITUDE: 5,
      ...this.options.graphConfig
    };

    // Available graphs (only small variants)
    this.availableGraphs = {
      // Question 7
      "q7_small": "spe_sujet1_auto_07_question_small",
      
      // Question 8  
      "q8_small": "spe_sujet1_auto_08_question_small",
      
      // Question 11 - Cases A, B, C
      "q11_case_a_small": "spe_sujet1_auto_11_case_a_question_small",
      "q11_case_b_small": "spe_sujet1_auto_11_case_b_question_small",
      "q11_case_c_small": "spe_sujet1_auto_11_case_c_question_small",
      
      // Question 10 - Parabola graphs
      "parabola_s1_a0": "spe_sujet1_auto_10_question_small_parabola_a_s1_a_0",
      "parabola_s1_am": "spe_sujet1_auto_10_question_small_parabola_a_s1_a_m",
      "parabola_s1_ap": "spe_sujet1_auto_10_question_small_parabola_a_s1_a_p",
      "parabola_sm1_a0": "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_0",
      "parabola_sm1_am": "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m",
      "parabola_sm1_ap": "spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p",
    };

    // Essential core files needed for all graphs
    this.essentialFiles = [
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
  }

  _setupUrls() {
    // Check if we're running on the v4.py.js local server (port 8022)
    const isV4PyJsLocal = window.location.port === "8022";
    
    if (this.options.baseUrl === 'auto') {
      if (isV4PyJsLocal) {
        // We're in the v4.py.js repo served on port 8022
        this.baseUrl = `http://localhost:8022`;
      } else {
        // Use jsDelivr for everything else (including other local servers)
        this.baseUrl = `https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@${this.options.pcaVersion}`;
      }
      
      // Always use CDN for Nagini dependencies
      this.naginiCdnPath = `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@${this.options.naginiVersion}/src/nagini.js`;
      this.workerCdnPath = `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@${this.options.naginiVersion}/src/pyodide/worker/worker-dist.js`;
    } else {
      // Manual override
      this.baseUrl = this.options.baseUrl;
      this.naginiCdnPath = this.options.naginiCdnPath || 
        `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@${this.options.naginiVersion}/src/nagini.js`;
      this.workerCdnPath = this.options.workerCdnPath || 
        `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@${this.options.naginiVersion}/src/pyodide/worker/worker-dist.js`;
    }

    if (this.options.debug) {
      console.log("📍 PCAGraphLoader Configuration:");
      console.log("   Base URL:", this.baseUrl);
      console.log("   Nagini CDN:", this.naginiCdnPath);
      console.log("   Worker CDN:", this.workerCdnPath);
      console.log("   PCA Version:", this.options.pcaVersion);
      console.log("   Environment:", isV4PyJsLocal ? "LOCAL (v4.py.js:8022)" : "CDN (jsDelivr)");
    }
  }

  /**
   * Initialize the Nagini manager and load essential files
   */
  async initialize() {
    if (this.initialized) {
      if (this.options.debug) console.log("✅ Already initialized");
      return this.manager;
    }

    try {
      if (this.options.debug) console.log("🚀 Loading Nagini from CDN...");
      const { Nagini } = await import(this.naginiCdnPath);
      
      // Load only essential files first
      const essentialFilesToLoad = this.essentialFiles.map(file => ({
        url: `${this.baseUrl}/${file}`,
        path: file.replace("src/", ""),
      }));
      
      if (this.options.debug) {
        console.log("📦 Loading essential files:", essentialFilesToLoad.length);
      }
      
      // Create manager with essential files only
      this.manager = await Nagini.createManager(
        "pyodide",
        ["numpy", "svgwrite", "pydantic"],
        [],
        essentialFilesToLoad,
        this.workerCdnPath
      );
      
      await Nagini.waitForReady(this.manager);
      if (this.options.debug) console.log("✅ Nagini ready with essential files!");
      
      // Initialize package structure
      await this.manager.executeAsync("init_packages.py", `
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
      
      this.initialized = true;
      return this.manager;
    } catch (error) {
      console.error("❌ Failed to initialize Nagini:", error);
      throw new Error(`Failed to initialize: ${error.message}`);
    }
  }

  /**
   * Update graph configuration parameters
   */
  updateConfig(config) {
    this.graphConfig = {
      ...this.graphConfig,
      ...config
    };
    
    // Clear loaded graphs to force reload with new config
    this.loadedGraphs.clear();
    
    if (this.options.debug) {
      console.log("📊 Updated configuration:", this.graphConfig);
    }
  }

  /**
   * Load a specific graph file
   */
  async _loadGraphFile(graphKey, filepath) {
    try {
      const url = `${this.baseUrl}/${filepath}`;
      if (this.options.debug) console.log(`📥 Loading ${graphKey} from ${url}`);
      
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      const code = await response.text();
      const filename = filepath.split('/').pop();
      const moduleName = filename.replace('.py', '');
      
      // Convert to base64 to avoid escaping issues
      const codeBase64 = btoa(unescape(encodeURIComponent(code)));
      
      // Get current configuration values
      const { Y_LABEL_FOR_HORIZONTAL_LINE, A_FLOAT_FOR_AFFINE_LINE, 
              B_FLOAT_FOR_AFFINE_LINE, A_SHIFT_MAGNITUDE } = this.graphConfig;
      
      // Write the file using Python directly
      const result = await this.manager.executeAsync(`write_${graphKey}.py`, `
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

# Inject configuration variables into the module's namespace
module.__dict__['Y_LABEL_FOR_HORIZONTAL_LINE'] = ${Y_LABEL_FOR_HORIZONTAL_LINE}
module.__dict__['A_FLOAT_FOR_AFFINE_LINE'] = ${A_FLOAT_FOR_AFFINE_LINE}
module.__dict__['B_FLOAT_FOR_AFFINE_LINE'] = ${B_FLOAT_FOR_AFFINE_LINE}
module.__dict__['A_SHIFT_MAGNITUDE'] = ${A_SHIFT_MAGNITUDE}

# Try to execute the code in the module's namespace
try:
    exec(code, module.__dict__)
    # After exec, re-inject config variables to ensure they override any defaults
    module.__dict__['Y_LABEL_FOR_HORIZONTAL_LINE'] = ${Y_LABEL_FOR_HORIZONTAL_LINE}
    module.__dict__['A_FLOAT_FOR_AFFINE_LINE'] = ${A_FLOAT_FOR_AFFINE_LINE}
    module.__dict__['B_FLOAT_FOR_AFFINE_LINE'] = ${B_FLOAT_FOR_AFFINE_LINE}
    module.__dict__['A_SHIFT_MAGNITUDE'] = ${A_SHIFT_MAGNITUDE}
    
    # Register in sys.modules
    sys.modules[full_module_name] = module
    sys.modules[module_name] = module
    print(f"✅ Registered module: {full_module_name}")
except Exception as e:
    print(f"⚠️ Warning: Failed to execute module {module_name}: {e}")
    # Still register the module even if exec failed
    sys.modules[full_module_name] = module
    sys.modules[module_name] = module
      `);
      
      if (result.error) {
        throw new Error(result.error.message || "Failed to write file");
      }
      
      if (this.options.debug) console.log(`✅ Loaded ${graphKey} -> ${filename}`);
      return moduleName;
    } catch (error) {
      console.error(`❌ Failed to load ${graphKey}:`, error);
      throw error;
    }
  }

  /**
   * Get graph dictionary from a loaded module
   */
  async _getGraphDict(moduleName) {
    try {
      if (this.options.debug) console.log(`🔍 Getting graph from ${moduleName}`);
      
      const result = await this.manager.executeAsync(`get_${moduleName}.py`, `
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
          throw new Error(data.error);
        }
        
        return data.graph;
      }
      
      throw new Error("No graph data returned");
    } catch (error) {
      console.error(`❌ Failed to get graph ${moduleName}:`, error);
      throw error;
    }
  }

  /**
   * Load a specific graph by key
   */
  async loadGraph(graphKey) {
    if (!this.initialized) {
      throw new Error("PCAGraphLoader not initialized. Call initialize() first.");
    }

    if (!this.availableGraphs[graphKey]) {
      throw new Error(`Unknown graph key: ${graphKey}. Available: ${Object.keys(this.availableGraphs).join(', ')}`);
    }

    // Check if already loaded with current config
    const cacheKey = `${graphKey}_${JSON.stringify(this.graphConfig)}`;
    if (this.loadedGraphs.has(cacheKey)) {
      if (this.options.debug) console.log(`✨ Using cached graph: ${graphKey}`);
      return this.loadedGraphs.get(cacheKey);
    }

    try {
      // Determine if we need dispatch module (for parabola graphs)
      const needsDispatch = graphKey.startsWith("parabola");
      
      if (needsDispatch) {
        // Load dispatch module first
        await this._loadGraphFile("dispatch", 
          "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_dispatch.py");
      }

      // Load the graph file
      const moduleName = this.availableGraphs[graphKey];
      const filepath = `src/pca_graph_viz/tests/graphs/${moduleName}.py`;
      await this._loadGraphFile(graphKey, filepath);
      
      // Get the graph dictionary
      const graphDict = await this._getGraphDict(moduleName);
      
      // Cache the result
      this.loadedGraphs.set(cacheKey, graphDict);
      
      if (this.options.debug) console.log(`✅ Loaded graph: ${graphKey}`);
      return graphDict;
    } catch (error) {
      console.error(`Failed to load graph ${graphKey}:`, error);
      throw error;
    }
  }

  /**
   * Render a graph to SVG
   * @param {string} graphKey - The graph key to render
   * @param {Object} config - Optional configuration overrides for this render only
   */
  async renderGraph(graphKey, config = null) {
    // If config is provided, temporarily update the configuration
    let originalConfig = null;
    if (config && Object.keys(config).length > 0) {
      // Save original config
      originalConfig = { ...this.graphConfig };
      
      // Apply temporary config
      this.updateConfig(config);
      
      if (this.options.debug) {
        console.log(`📊 Rendering ${graphKey} with custom config:`, config);
      }
    }
    
    try {
      const graphDict = await this.loadGraph(graphKey);
      
      const result = await this.manager.executeAsync(`render_${graphKey}.py`, `
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
      console.error(`❌ Render error for ${graphKey}:`, error);
      throw error;
    } finally {
      // Restore original config if it was temporarily changed
      if (originalConfig) {
        this.graphConfig = originalConfig;
        // Clear cache since config changed back
        this.loadedGraphs.clear();
        
        if (this.options.debug) {
          console.log(`📊 Restored original config after rendering ${graphKey}`);
        }
      }
    }
  }

  /**
   * Get list of available graphs
   */
  getAvailableGraphs() {
    return Object.keys(this.availableGraphs);
  }

  /**
   * Get current configuration
   */
  getConfig() {
    return { ...this.graphConfig };
  }
}

// Export for both ES modules and CommonJS
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PCAGraphLoader };
}

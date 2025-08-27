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
    this.loadedFiles = new Set(); // Track loaded files to avoid reloading
    this.executionCounter = 0; // For unique namespace generation
    
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
   * Generate a unique namespace object for isolated execution
   */
  _generateNamespace(configValues = null) {
    // Use provided config or fall back to instance config
    const config = configValues || this.graphConfig;
    return {
      Y_LABEL_FOR_HORIZONTAL_LINE: config.Y_LABEL_FOR_HORIZONTAL_LINE,
      A_FLOAT_FOR_AFFINE_LINE: config.A_FLOAT_FOR_AFFINE_LINE,
      B_FLOAT_FOR_AFFINE_LINE: config.B_FLOAT_FOR_AFFINE_LINE,
      A_SHIFT_MAGNITUDE: config.A_SHIFT_MAGNITUDE
    };
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
      
      // Initialize package structure once (no namespace needed)
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
    
    if (this.options.debug) {
      console.log("📊 Updated configuration:", this.graphConfig);
    }
  }

  /**
   * Load a specific graph file (without configuration injection)
   */
  async _loadGraphFile(graphKey, filepath) {
    const filename = filepath.split('/').pop();
    const moduleName = filename.replace('.py', '');
    
    // Check if already loaded
    if (this.loadedFiles.has(filepath)) {
      if (this.options.debug) console.log(`✨ File already loaded: ${filepath}`);
      return moduleName;
    }
    
    try {
      const url = `${this.baseUrl}/${filepath}`;
      if (this.options.debug) console.log(`📥 Loading ${graphKey} from ${url}`);
      
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      const code = await response.text();
      
      // Convert to base64 to avoid escaping issues
      const codeBase64 = btoa(unescape(encodeURIComponent(code)));
      
      // Write the file cleanly without any configuration injection (no namespace needed)
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

# Simply register the module name mapping for import
module_name = '${moduleName}'
full_module_name = f'pca_graph_viz.tests.graphs.{module_name}'

# Let Python handle the actual import when needed
print(f"✅ File ready for import: {full_module_name}")
      `);
      
      if (result.error) {
        throw new Error(result.error.message || "Failed to write file");
      }
      
      // Mark as loaded
      this.loadedFiles.add(filepath);
      
      if (this.options.debug) console.log(`✅ Loaded ${graphKey} -> ${filename}`);
      return moduleName;
    } catch (error) {
      console.error(`❌ Failed to load ${graphKey}:`, error);
      throw error;
    }
  }

  /**
   * Get graph dictionary from a loaded module with configuration passed via namespace
   */
  async _getGraphDict(moduleName, config = {}) {
    try {
      if (this.options.debug) {
        console.log(`🔍 Getting graph from ${moduleName}`);
        console.log('   Input config:', config);
        console.log('   Default graphConfig:', this.graphConfig);
      }
      
      // Merge default config with provided config
      const fullConfig = { ...this.graphConfig, ...config };
      
      if (this.options.debug) {
        console.log('   Merged fullConfig:', fullConfig);
      }
      
      // Create namespace object with configuration values - use fullConfig!
      const namespace = this._generateNamespace(fullConfig);
      
      if (this.options.debug) {
        console.log('   Namespace to inject:', namespace);
      }
      
      const result = await this.manager.executeAsync(`get_${moduleName}.py`, `
import json
import traceback
import sys
import importlib
import inspect

try:
    # Import the module cleanly
    module_name = '${moduleName}'
    full_module_name = f'pca_graph_viz.tests.graphs.{module_name}'
    
    # Force reload to ensure clean state
    if full_module_name in sys.modules:
        del sys.modules[full_module_name]
    
    # Import the module normally - no global tricks
    module = importlib.import_module(full_module_name)
    
    # Check if get_graph_dict accepts parameters
    if hasattr(module, 'get_graph_dict'):
        sig = inspect.signature(module.get_graph_dict)
        params = list(sig.parameters.keys())
        
        # Build kwargs based on what the function accepts
        kwargs = {}
        param_mapping = {
            'y_horizontal': 'Y_LABEL_FOR_HORIZONTAL_LINE',
            'a_affine': 'A_FLOAT_FOR_AFFINE_LINE', 
            'b_affine': 'B_FLOAT_FOR_AFFINE_LINE',
            'a_shift': 'A_SHIFT_MAGNITUDE'
        }
        
        for param, global_name in param_mapping.items():
            if param in params and global_name in globals():
                kwargs[param] = globals()[global_name]
        
        # Debug logging
        if kwargs:
            print(f"Calling get_graph_dict with parameters: {kwargs}")
        else:
            print(f"Calling get_graph_dict without parameters (using module defaults)")
        
        # Call with kwargs if any were matched, otherwise call without
        if kwargs:
            graph_dict = module.get_graph_dict(**kwargs)
        else:
            graph_dict = module.get_graph_dict()
            
        missive({"graph": graph_dict, "title": graph_dict.get('title', '${moduleName}')})
    else:
        raise RuntimeError(f'get_graph_dict not found in {full_module_name}')
        
except Exception as e:
    missive({"error": str(e), "traceback": traceback.format_exc()})
      `, namespace);
      
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
  async loadGraph(graphKey, config = null) {
    if (!this.initialized) {
      throw new Error("PCAGraphLoader not initialized. Call initialize() first.");
    }

    if (!this.availableGraphs[graphKey]) {
      throw new Error(`Unknown graph key: ${graphKey}. Available: ${Object.keys(this.availableGraphs).join(', ')}`);
    }

    try {
      // Determine if we need dispatch module (for parabola graphs)
      const needsDispatch = graphKey.startsWith("parabola");
      
      if (needsDispatch) {
        // Load dispatch module first if not already loaded
        await this._loadGraphFile("dispatch", 
          "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_dispatch.py");
      }

      // Load the graph file
      const moduleName = this.availableGraphs[graphKey];
      const filepath = `src/pca_graph_viz/tests/graphs/${moduleName}.py`;
      await this._loadGraphFile(graphKey, filepath);
      
      // Get the graph dictionary with configuration
      const graphDict = await this._getGraphDict(moduleName, config);
      
      if (this.options.debug) console.log(`✅ Loaded graph: ${graphKey}`);
      return graphDict;
    } catch (error) {
      console.error(`Failed to load graph ${graphKey}:`, error);
      throw error;
    }
  }

  /**
   * Render a graph to SVG and return both SVG and graph dictionary
   * @param {string} graphKey - The graph key to render
   * @param {Object} config - Optional configuration overrides for this render only
   * @returns {Promise<{svg: string, graphDict: Object}>} Object containing SVG string and graph dictionary
   */
  async renderGraph(graphKey, config = null) {
    try {
      // Load graph with config (if provided)
      const graphDict = await this.loadGraph(graphKey, config);
      
      // No namespace needed for rendering since config is already in graphDict
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
        
        // Return both SVG and graph dictionary
        return {
          svg: data.svg,
          graphDict: graphDict
        };
      }
      
      throw new Error("No SVG output");
    } catch (error) {
      console.error(`❌ Render error for ${graphKey}:`, error);
      throw error;
    }
  }
  
  /**
   * Render a graph to SVG only (backward compatibility helper)
   * @param {string} graphKey - The graph key to render
   * @param {Object} config - Optional configuration overrides for this render only
   * @returns {Promise<string>} SVG string only
   */
  async renderGraphSvg(graphKey, config = null) {
    const result = await this.renderGraph(graphKey, config);
    return result.svg;
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
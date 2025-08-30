


# Changelog



## v0.0.27

- max width 200px for sujets0

## v0.0.26

- Monochrome for sujets0-spe-sujet_1


## v0.0.25

- Cleaned all graphs for sujets0/spe1


```python
def was():
  return mess_then_safe_versioning
```


## v0.0.20-unstable

### Clean Parameter Passing Implementation - No More Global Tricks!

#### Overview
Complete refactor of parameter passing system to eliminate global state manipulation and implement clean, maintainable parameter passing to graphs.

#### Key Changes

**Python Graph Files** - Clean parameter acceptance:
- `spe_sujet1_auto_07_question_small.py` - `get_graph_dict(y_horizontal=None)`
- `spe_sujet1_auto_08_question_small.py` - `get_graph_dict(a_affine=None, b_affine=None)`
- All parabola files - `get_graph_dict(a_shift=None)`
- Removed all `globals()` and `builtins` tricks
- Parameters now passed directly as function arguments

**PCAGraphLoader.js** - Clean namespace usage:
- Uses Python's `inspect.signature()` to detect function parameters
- Passes values via Nagini's namespace object (not strings)
- No more builtins manipulation or global injection
- Automatic parameter mapping based on function signatures

**New Files Added**:
- `index-graphs.js` - Clean interface for building graphs with configuration
- `example-generators-integration.js` - Documentation and examples

**tests_main.html Improvements**:
- Fixed decimal separator (accepts both comma and dot)
- Proper form value extraction and passing
- Removed debug console statements
- Fixed inline style linter warnings

#### Usage Example
```javascript
import { buildPCAGraph } from './index-graphs.js';

// Build graph with dynamic configuration
const result = await buildPCAGraph('q7_small', {
    Y_LABEL_FOR_HORIZONTAL_LINE: 15
});

// result.svg contains the SVG markup
// result.graphDict contains the graph metadata
```

## v0.0.19-unstable

### Updating parameters injection in graphs (not so good)


## v0.0.18-unstable

### 📄 New Test Suite: tests_main.html

#### Overview
- **Comprehensive Test Suite for PCAGraphLoader**: This file serves as the main test suite for the PCAGraphLoader, covering all graph types with LaTeX rendering and dimension verification.

#### Features
- **LaTeX Rendering**: Utilizes KaTeX for rendering mathematical notation within graphs.
- **Graph Styling**: Integrates DaisyUI for consistent graph styling.
- **Configuration Parameters**: Provides a control panel for adjusting graph parameters such as Y Horizontal Line, Affine Slope, and Shift Magnitude.
- **Dynamic Graph Rendering**: Dynamically inserts graphs into the document based on configuration.
- **Dimension Verification**: Verifies the dimensions of rendered graphs against expected values.
- **Graph Dictionary Display**: Displays a detailed graph dictionary for each rendered graph, including metadata and configuration.
- **Responsive Design**: Adapts layout for different screen sizes, ensuring usability on mobile devices.
- **Loading State and Error Handling**: Displays loading spinners and error messages during graph rendering.

#### Technical Details
- **JavaScript Module**: Imports and utilizes the PCAGraphLoader module for graph rendering.
- **Event Listeners**: Includes event listeners for running tests and applying configurations.
- **Auto-run Tests**: Automatically runs all tests on page load.

#### Benefits
- **Comprehensive Testing**: Ensures all graph types are tested with full feature verification.
- **Debugging and Introspection**: Provides detailed information for debugging and introspection of graph rendering.

---

## v0.0.17-unstable

### 🔄 Breaking Change: renderGraph() Now Returns Graph Dictionary

#### Major API Enhancement
- **`renderGraph()` now returns both SVG and graph dictionary**
  - Changed return type from `string` to `{svg: string, graphDict: Object}`
  - Provides access to complete graph metadata alongside the rendered SVG
  - Graph dictionary includes all parameters, settings, lines, foreign objects, etc.

#### New Return Format
```javascript
// Before (v0.0.16 and earlier):
const svg = await loader.renderGraph('q8_small');

// Now (v0.0.17+):
const result = await loader.renderGraph('q8_small');
const svg = result.svg;           // SVG string
const dict = result.graphDict;    // Complete graph dictionary
```

#### Graph Dictionary Contents
The `graphDict` object contains:
- `id`: Graph identifier
- `title`: Graph title 
- `description`: Graph description
- `svg`: SVG configuration (width, height, viewBox, class)
- `settings`: Graph settings (margins, ranges, axes, grid)
- `lines`: Array of line definitions
- `foreign_objects`: Array of LaTeX labels and annotations
- All other graph-specific data from Python `get_graph_dict()`

#### Backward Compatibility
- Added `renderGraphSvg()` method for backward compatibility
  - Returns only the SVG string (like old `renderGraph()`)
  - Use when you don't need the graph dictionary

```javascript
// For backward compatibility
const svg = await loader.renderGraphSvg('q8_small');
```

#### Files Updated
- **PCAGraphLoader.js**: Core changes to return format
- **graph-loader-partial.html**: Updated helper function, stores dict as data attribute
- **test-config-params.html**: Updated to handle new format
- **test-loading-logic.html**: Logs graph dict information
- **test.html**: Logs graph dict to console
- **README.md**: Updated API documentation
- **SIMPLE_USAGE.md**: Updated usage examples
- **test-graph-dict.html**: New test page for verifying functionality

#### Benefits
- Access to complete graph metadata without separate API call
- Useful for debugging and introspection
- Can extract configuration for reuse or modification
- Enables advanced use cases like graph serialization
- Consistent with Python `get_graph_dict()` pattern

---

## v0.0.16-unstable

### 🎨 Dynamic Configuration for Graph Rendering

#### Major Enhancement
- **`renderGraph()` Method Now Accepts Configuration Parameters**
  - Added optional second parameter for temporary configuration overrides
  - Matches the dynamic configuration behavior from `sujets0-app-simple.js`
  - Configuration changes are applied only for that specific render
  - Original configuration is automatically restored after rendering

#### API Improvement
```javascript
// Before: Had to call updateConfig() separately
loader.updateConfig({ A_FLOAT_FOR_AFFINE_LINE: 1.5 });
const svg = await loader.renderGraph('q8_small');

// Now: Pass config directly to renderGraph()
const svg = await loader.renderGraph('q8_small', {
  A_FLOAT_FOR_AFFINE_LINE: 1.5,
  B_FLOAT_FOR_AFFINE_LINE: -2
});
```

#### Use Cases
- **Different Slopes for Same Graph**
  ```javascript
  const svg1 = await loader.renderGraph('q8_small');  // Default: a=0.75
  const svg2 = await loader.renderGraph('q8_small', { A_FLOAT_FOR_AFFINE_LINE: 1.5 });
  const svg3 = await loader.renderGraph('q8_small', { A_FLOAT_FOR_AFFINE_LINE: -0.5 });
  ```

- **Variable Parabola Shifts**
  ```javascript
  const svg1 = await loader.renderGraph('parabola_s1_ap');  // Default shift: 5
  const svg2 = await loader.renderGraph('parabola_s1_ap', { A_SHIFT_MAGNITUDE: 3 });
  const svg3 = await loader.renderGraph('parabola_s1_ap', { A_SHIFT_MAGNITUDE: 10 });
  ```

#### Technical Details
- Configuration is temporarily applied before loading/rendering
- Cache key includes configuration to prevent incorrect cached results
- Original configuration restored in `finally` block for safety
- No breaking changes - backward compatible (config parameter is optional)

#### Testing
- Created `test-config-params.html` to verify functionality
- Tests confirm configs are temporary and don't persist between renders
- Visual tests show different slopes and shifts render correctly

#### Documentation
- Updated `README.md` with new method signature
- Updated `SIMPLE_USAGE.md` with usage examples
- Added inline JSDoc comments for better IDE support

---

## v0.0.15-unstable

### 🔧 Improved Loading Logic & Testing

#### Major Changes
- **Enhanced PCAGraphLoader Detection System**
  - Changed from hostname-based to **port-based detection** (port 8022)
  - Only v4.py.js local server uses local files
  - All other environments (ports 3000, 5000, 5001, 8080, production) use jsDelivr CDN
  - Fixes 404 errors when using from other local development servers

- **Visual Test Page Enhancement** (`test-loading-logic.html`)
  - Added **live graph rendering display** section
  - Graph dropdown selector for all 11 available graph types
  - Visual feedback with actual SVG rendering
  - LaTeX mathematical formula rendering with KaTeX
  - Quick Test All button for automated testing sequence
  - Auto-run mode with `?auto` URL parameter
  - Color-coded console output (green/yellow/red)
  - Environment detection display

- **DaisyUI Color System Integration**
  - Fixed color system to use proper DaisyUI CSS variables
  - Changed from custom `--pca-color-*` to DaisyUI's `--p`, `--s`, `--a`, `--bc`, `--b1`, `--b2`, `--b3`
  - Uses `hsl(var(--p))` format for proper theme compatibility
  - All graphs now respect DaisyUI theme settings

#### Documentation Improvements
- **Created `SIMPLE_USAGE.md`** - Minimal, copy-paste ready examples
- **Created `LOADING_LOGIC.md`** - Detailed explanation of port detection system
- **Created `ALL_GRAPHS_REFERENCE.md`** - Complete list of all graphs with examples
- Removed `graph-loader-fragment.html` (keeping only `graph-loader-partial.html`)
- Simplified documentation structure for easier onboarding

#### Technical Details
- **Port Detection Logic**:
  ```javascript
  const isV4PyJsLocal = window.location.port === "8022";
  if (isV4PyJsLocal) {
      // Use local files from http://localhost:8022
  } else {
      // Use CDN from jsDelivr
  }
  ```
- Version updated from v0.0.14 to v0.0.15 across all CDN references
- No breaking changes - backward compatible

#### Benefits
- ✅ No more 404 errors on non-8022 ports
- ✅ Works seamlessly in any development environment
- ✅ Visual testing with immediate feedback
- ✅ Proper DaisyUI theme integration
- ✅ Simpler, clearer documentation

---

## v0.0.14-unstable

### 🎯 Major Feature: PCAGraphLoader Package

#### Overview
Created a **modular, reusable JavaScript class** for loading and rendering PCA mathematical visualization graphs. This package enables external repositories to easily integrate PCA graphs without complex setup.

### Added
- **`scenery/packaged/PCAGraphLoader.js`** - Main class module (475 lines)
  - Clean class-based API with zero global variables
  - Automatic environment detection (local vs CDN)
  - Dynamic configuration management
  - Graph caching and lazy loading
  - Promise-based error handling
  - Supports all small graph variants (q7, q8, q11, parabolas)

- **`scenery/packaged/test.html`** - Interactive test interface (585 lines)
  - Visual graph display with proper SVG rendering
  - Configuration controls for all parameters
  - Real-time graph updates
  - Matches exact styling from sujets0-simple.html
  - KaTeX LaTeX rendering support
  - Console debugging features

- **`scenery/packaged/README.md`** - Complete API documentation
  - Installation instructions (CDN and local)
  - API reference with all methods
  - Integration examples (React, Vue, Vanilla JS)
  - Configuration parameters
  - Troubleshooting guide
  - Browser compatibility notes

- **`scenery/packaged/example-external-usage.html`** - External usage demo
  - Shows CDN import pattern
  - No local installation required
  - Working example with buttons
  - Demonstrates real-world usage

- **`scenery/packaged/package.json`** - NPM package configuration
  - Ready for npm publication
  - Proper module exports
  - Package metadata

### Technical Improvements

#### Architecture
```
External App → PCAGraphLoader (JS) → Nagini Manager → Pyodide Worker → Python Modules → SVG Output
```

#### Key Features
1. **Dynamic URL Resolution**
   - Auto-detects local vs production environment
   - Uses jsDelivr CDN for GitHub-hosted content
   - Configurable base URLs for custom deployments

2. **Configuration Management**
   ```javascript
   const loader = new PCAGraphLoader({
     graphConfig: {
       Y_LABEL_FOR_HORIZONTAL_LINE: 10,
       A_FLOAT_FOR_AFFINE_LINE: 0.75,
       B_FLOAT_FOR_AFFINE_LINE: 2.0,
       A_SHIFT_MAGNITUDE: 5
     }
   });
   ```

3. **Available Graphs** (small variants only)
   - Question 7: `q7_small`
   - Question 8: `q8_small`
   - Question 11: `q11_case_a_small`, `q11_case_b_small`, `q11_case_c_small`
   - Parabolas: `parabola_s1_a0`, `parabola_s1_am`, `parabola_s1_ap`, `parabola_sm1_a0`, `parabola_sm1_am`, `parabola_sm1_ap`

4. **Simple API**
   ```javascript
   import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.15-unstable/scenery/packaged/PCAGraphLoader.js';
   
   const loader = new PCAGraphLoader();
   await loader.initialize();
   const svg = await loader.renderGraph('q8_small');
   ```

### Fixed
- **Graph Cropping Issues** in test.html
  - Aligned CSS with sujets0-simple.html structure
  - Added proper `.graph-svg-frame` wrapper
  - Fixed SVG max dimensions (340x340px)
  - Included all required color utility classes
  - Added DaisyUI theme support

### CSS Improvements
- Proper container hierarchy: `.graph-display` → `.graph-svg-frame` → SVG
- Consistent sizing with `max-width: 340px; max-height: 340px`
- Added essential color utilities for SVG rendering
- Imported `graphs.css` for consistent styling
- LaTeX rendering styles for mathematical notation

### Performance
- First initialization: ~5-10 seconds (Pyodide loading)
- Subsequent graph loads: ~100-500ms
- Graphs cached after first load
- Configuration changes clear cache intelligently

### Documentation
- Comprehensive API documentation in README.md
- Integration examples for major frameworks
- Package summary with architecture overview
- CSS fix documentation explaining display issues

### Benefits Over Original Implementation
1. **Encapsulation** - All functionality in a single class
2. **No Global Variables** - Clean namespace
3. **Reusability** - Import in any project via CDN
4. **Version Control** - Pin specific versions
5. **Better Error Handling** - Promise-based with clear messages
6. **Lazy Loading** - Only loads required graphs
7. **External Usage** - No installation needed

### Browser Support
- Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Requires: ES Modules, Dynamic imports, Web Workers, Async/await

### Usage Example
```html
<script type="module">
  import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.15-unstable/scenery/packaged/PCAGraphLoader.js';
  
  const loader = new PCAGraphLoader();
  await loader.initialize();
  const svg = await loader.renderGraph('q8_small');
  document.getElementById('graph-container').innerHTML = svg;
</script>
```

### Notes
- Skipped v0.0.13 (triskaidekaphobia)
- Package ready for npm publication as `@pointcarre/pca-graph-loader`
- Test interface available at `http://localhost:8022/scenery/packaged/test.html`
- All graphs render without cropping issues

---

## v0.0.12-unstable

### Changed
- **Updated project metadata** (`pyproject.toml`)
  - Changed license from MIT to AGPL-3.0
  - Updated author information to pointcarre.app with contact email
  - Version bumped to 0.2.0 (from previous 0.1.0)

### Cleaned up
- **CURRICULUM.md formatting**
  - Removed unnecessary blank lines at the beginning of the file
  - Improved document structure and readability

## v0.0.11-unstable

### Documentation
- **Added CURRICULUM.md**
  - Documents which graph files are actively used in sujets0 apps
  - Clarifies difference between production files and construction features
  - Maps graph files to French curriculum structure (Première Spé - Sujet 1)
  - Provides clear enumeration of all question-specific graphs

### Organized
- **Graph file categorization**
  - Production files: Used in generation engines and student apps
  - Construction features: Commented files for development reference only
  - Clear separation between canonical and small graph variants

## v0.0.10-unstable 

### Fixed
- **Critical syntax error in dispatch system**
  - Fixed typo `0.75s` → `0.75` in `sm1_a_m` configuration
  - This error was preventing all parabola modules from loading
  - Modules now load correctly with proper label display

### Confirmed Behavior
- **Label display working as intended**
  - `_a_0` files: Always show M(0;0) (static)
  - `_a_m` files: Show M(0;-value) based on slider (dynamic)
  - `_a_p` files: Show M(0;+value) based on slider (dynamic)
  - Curves remain fixed while labels update dynamically

### Technical Details
- Single character typo fix with major impact
- Restored functionality for 6 parabola graph modules
- No other code changes required

## v0.0.9-unstable 

### Adjusted
- **Fine-tuned graph display parameters**
  - Adjusted axis and label positions in parabola configurations
  - Improved visual balance for graph layouts
  - Updated Y-axis ranges for better curve visibility
  
### Changed  
- **Parameter refinements in dispatch system**
  - Modified `s1_a_p` label positions (x: 4.5, y: 3)
  - Updated `sm1_a_0` x-label position for consistency
  - Adjusted `sm1_a_p` Y-axis range (-15 to 12) for complete curve display
  - Fine-tuned label positions across multiple graph configurations

### Technical Details
- Minor coordinate adjustments for improved visual presentation
- No functional changes to graph logic or dispatch system
- All changes are cosmetic parameter updates

## v0.0.8-unstable 

### Major Refactoring
- **Simplified parabola graph dispatch system**
  - Replaced complex match statement with direct graph ID lookup
  - Removed confusing `closest_a` rounding logic
  - Introduced clean `GRAPH_CONFIGS` dictionary mapping
  - Graph IDs now directly map to configurations (e.g., `s1_a_m` → y = x² - 5)

### Fixed
- **Parabola curves now stay fixed while labels update dynamically**
  - Curves use fixed `a_shift` value for positioning
  - Labels use dynamic `A_SHIFT_FOR_LABEL` from UI controls
  - Resolves issue where curves would move with slider adjustments
  
### Changed
- **Graph parameter selection**
  - Each parabola file now passes a graph ID to dispatch
  - Direct configuration lookup instead of parameter matching
  - Cleaner separation between curve position and label display
- **Import statements**
  - Updated all parabola files to use relative imports (`.module_name`)
  - Fixes module resolution in Pyodide environment

### Documentation
- **Added comprehensive dispatch system documentation**
  - Created `scenery/sujets0-simple.md` with full architecture explanation
  - Documented variable flow from JavaScript UI to Python graphs
  - Included troubleshooting guide and debug commands
  - Added Mermaid diagram for configuration flow

### Technical Details
- Graph ID convention: `{sign}_{shift}` where:
  - `s1` = upward parabola (y = x²)
  - `sm1` = downward parabola (y = -x²)  
  - `a_0` = no shift, `a_m` = negative shift, `a_p` = positive shift
- Standardized default `A_SHIFT_MAGNITUDE` to 5 across all files
- Fixed axis and label positioning in several graph configurations

## v0.0.7-unstable

⚠️ **STILL HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

### Added
- **Graph styles**: New `src/pca_graph_viz/core/graphs.css` with utility class `.text-2xs` for dense labels and CSS-driven SVG styling.

### Changed
- **SVG engine** (`src/pca_graph_viz/core/svg_utils.py`):
  - Prefer CSS classes and `currentColor` to reduce inline styling
  - More robust margins (uniform or per-side) with correct transforms
  - Multi-curve rendering (`create_multi_curve_svg`) and class-based curve styling
  - Better axis arrows (marker defs; orientation-aware usage)
  - Safer `foreignObject` injection with margin offsets; optional point markers
  - Helper `dict_from_graph_params` for standardized graph dictionaries
- **Sujets 0 loader** (`scenery/sujets0-app.js`):
  - Fetch-and-exec Python sources (base64) to avoid circular imports
  - Cache-busting and improved local/GitHub Pages base-URL detection
  - Framed SVG container, default margins, and richer error/traceback logging
- **Main collection app** (`scenery/app.js`):
  - Unified env detection (local vs Pages) and absolute worker URLs
  - Full wiring for Première graph modules with diagnostics and counts
- **Pages** (`scenery/index.html`, `scenery/sujets0.html`):
  - Integrated Tailwind/DaisyUI + KaTeX
  - Consistent two-column layout and SVG utility classes

### Fixed
- Local dev CORS/caching issues using `window.location.origin` and cache-busting
- KaTeX color inheritance inside `foreignObject` content after render

### Removed
- Legacy Sujets 0 test files in favor of new naming scheme for Question 7

### Notes
- New Sujets 0 test graph files added under `src/pca_graph_viz/tests/graphs/` for Questions 7 and 8 (canonical and small variants)

---

## v0.0.5-unstable

⚠️ **STILL HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

### Added
- **New Question 7 graph**: Visualization of inequality x² ≥ 10 on parabola y = x²
  - File: `graph_sujets0_spe_sujet1_automatismes_question7_canonical.py`
  - Shows solution regions x ≤ -√10 or x ≥ √10
  - Named with pattern: [sujets0][spé][sujet-1][automatismes][question-7]
- **Dedicated Sujets 0 page**: Simplified visualization page for individual exam questions
  - File: `scenery/sujets0.html` - Clean two-column layout matching main visualization page
  - File: `scenery/sujets0-app.js` - Standalone loader for Sujets 0 graphs
  - Uses same rendering approach as main page but filtered to single graph
- **Template for Sujets 0 graphs**: Created `template_sujets0.py` to facilitate adding new exam questions

### Fixed
- **Resolved circular import issue**: Fixed Python module loading in Pyodide
  - Removed problematic `__init__.py` files from test modules
  - Implemented direct file fetching and execution via `exec()` to bypass import system
  - Uses base64 encoding to safely transfer Python source code
- **Improved error handling**: Added comprehensive logging for debugging Python execution errors
- **Simplified loading approach**: Aligned sujets0-app.js with proven app.js methodology

### Technical Improvements
- Fetch Python graph files directly via HTTP instead of relying on imports
- Execute graph code in isolated namespace to avoid module conflicts
- Better error reporting with Python traceback capture via missive

### Known Issues (Ongoing)
- All previous instability warnings still apply
- **NOT SUITABLE FOR PRODUCTION USE**
- Expect API changes without notice

---

## v0.0.4-unstable

⚠️ **STILL HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

### Changes from v0.0.3
- **Fixed browser caching issues**: Added cache-busting version parameter to app.js
- **Improved debugging**: Added console logging to track file loading
- **Worker URL fixes**: Ensured absolute URLs are used for GitHub Pages deployment

### Known Issues (Ongoing)
- All previous instability warnings still apply
- **NOT SUITABLE FOR PRODUCTION USE**

---

## v0.0.3-unstable

⚠️ **STILL HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

### Changes from v0.0.2
- **Fixed GitHub Pages URLs**: Corrected repository name from `pca-v4.py.js` to `v4.py.js` in all documentation
- **Simplified README**: 
  - Removed redundant deployment instructions (users don't need to re-host our repo)
  - Focused on live demo access
  - Added developer section for those who want to fork/customize
- **Added verification tools**: Created `VERIFY_GITHUB_PAGES.md` for troubleshooting deployment issues

### Documentation
- Streamlined README to be more user-focused
- Clear separation between user access and developer customization
- Better organization of content

### Known Issues (Ongoing)
- All previous instability warnings still apply
- **NOT SUITABLE FOR PRODUCTION USE**
- Expect API changes without notice

---

## v0.0.2-unstable

⚠️ **STILL HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

### Changes from v0.0.1
- **Fixed GitHub Pages deployment**: 
  - Added `.nojekyll` file to serve entire repository as static files
  - Updated `app.js` to automatically detect environment (local vs GitHub Pages)
  - Fixed Python module loading paths for browser deployment
- **Updated all placeholder graphs**: Replaced 6 remaining placeholder visualizations with meaningful mathematical content
- **Added test utilities**: Created diagnostic pages for verifying deployment
- **Documentation improvements**: Enhanced README with clearer deployment instructions

### Fixes
- Fixed cobweb diagram iteration points rendering
- Fixed file paths for static hosting on GitHub Pages
- Added 404 error page with navigation
- Improved environment detection for local vs production

### Known Issues (Ongoing)
- All v0.0.1 instability warnings still apply
- **NOT SUITABLE FOR PRODUCTION USE**
- API changes and breaking updates expected in every release

---

## v0.0.1-unstable

⚠️ **HIGHLY UNSTABLE - EXPERIMENTAL RELEASE** ⚠️

This is an extremely early, experimental release. Expect frequent breaking changes, incomplete features, and numerous bugs. **NOT SUITABLE FOR PRODUCTION USE.**

Initial proof-of-concept with 40+ mathematical visualizations for French Première Spécialité Mathématiques curriculum.

### Features
- **Core Engine**: Python-based SVG generation running in-browser via Pyodide
- **Mathematical Graphs**: Complete set of educational visualizations including:
  - Trigonometry (unit circle, sine/cosine functions)
  - Sequences (arithmetic, geometric, recursive/cobweb diagrams)
  - Derivatives and functions (tangent lines, variation tables)
  - Second-degree functions (parabolas, canonical forms, sign tables)
  - Scalar products and geometry (vectors, orthogonality, projections)
  - Probability (Venn diagrams, tree diagrams, distributions)
  - Coordinate geometry (circles, lines, distance formulas)
  - Special topics (3D previews, parametric curves, optimization)
- **LaTeX Support**: Mathematical notation rendered with KaTeX
- **Browser-Based**: No server required, runs entirely client-side

### Technical
- Declarative graph definition via Python dictionaries
- Pydantic models for data validation
- Clean SVG output with customizable styling
- Test suite covering all graph types

### ⚠️ Known Issues & Instabilities
- **API WILL CHANGE**: Graph dictionary structure is not finalized
- **Performance issues**: Some complex graphs may render slowly
- **Browser compatibility**: Only tested on latest Chrome/Firefox
- **Memory leaks**: Pyodide worker may accumulate memory over time
- **Incomplete error handling**: Many edge cases not covered
- **No documentation**: API documentation is minimal or missing
- **Breaking changes expected**: Every update may break existing code
- **Not production ready**: This is a prototype/proof-of-concept only

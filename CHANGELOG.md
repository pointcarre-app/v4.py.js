


# Changelog

## v0.0.9-unstable - 2024-12-19

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

## v0.0.8-unstable - 2024-12-19

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

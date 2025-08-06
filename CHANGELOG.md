


# Changelog

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

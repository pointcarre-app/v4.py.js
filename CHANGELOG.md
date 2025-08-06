


# Changelog

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

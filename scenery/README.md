# Scenery - Interactive Math Visualizations

This folder contains interactive visualization pages for mathematical graphs and problems.

## Available Pages

### 1. Main Collection (`index.html`)
- **URL**: `/scenery/index.html`
- **Description**: Complete collection of all PCA graphs
- **Content**: 
  - Original graphs (1-17)
  - Première Spécialité Mathématiques visualizations (42 graphs)
  - Question 7 graph (displayed first)
- **Total**: 60 graphs

### 2. Sujets 0 - Spécialité Mathématiques (`sujets0.html`)
- **URL**: `/scenery/sujets0.html`
- **Description**: Dedicated page for Sujets 0 examination questions
- **Language**: French interface
- **Features**:
  - Beautiful gradient design with card-based layout
  - Question statement display
  - Multiple choice options with correct answer highlighted in green
  - Interactive graph visualization
  - Detailed explanations
  - JSON graph dictionary display

## Current Graphs in Sujets 0

### Question 7 - Inéquation x² ≥ 10
- **File**: `graph_sujets0_spe_sujet1_automatismes_question7_canonical.py`
- **Topic**: Fonctions du second degré (Second Degree Functions)
- **Description**: Visualization of the inequality x² ≥ 10 on the parabola y = x²
- **Solution**: x ≤ -√10 or x ≥ √10 (option b)

## Local Development

To run locally:
```bash
# Start the server (from project root)
python serve.py

# Access the pages
# Main collection: http://127.0.0.1:8022/scenery/index.html
# Sujets 0: http://127.0.0.1:8022/scenery/sujets0.html
```

## GitHub Pages

When deployed to GitHub Pages:
- Main collection: `https://pointcarre-app.github.io/v4.py.js/scenery/index.html`
- Sujets 0: `https://pointcarre-app.github.io/v4.py.js/scenery/sujets0.html`

## Adding New Sujets 0 Questions

To add a new question to the Sujets 0 page:

1. **Create a new Python graph file** in `src/pca_graph_viz/tests/graphs/`
   - Use the template: `template_sujets0.py` as a starting point
   - Name it: `graph_sujets0_spe_sujet{N}_automatismes_question{M}.py`
   - Example: `graph_sujets0_spe_sujet1_automatismes_question8.py`

2. **Update `sujets0-app.js`**:
   - Add the file to the `pythonFiles` array:
     ```javascript
     'src/pca_graph_viz/tests/graphs/graph_sujets0_spe_sujet1_automatismes_question8.py',
     ```
   - Add question data to `questionData` object:
     ```javascript
     'graph_sujets0_spe_sujet1_automatismes_question8': {
         number: 8,
         topic: "Topic name",
         statement: "Question statement",
         choices: [
             { id: 'a', latex: 'Choice A', correct: false },
             { id: 'b', latex: 'Choice B', correct: true },
             // ...
         ],
         explanation: "Explanation text"
     }
     ```

3. **Load the graph** in `loadGraphs()` function (optional - can use the same pattern as Question 7)

4. The graph will automatically appear on the sujets0.html page

## Current Status

- **Working**: Question 7 graph displays correctly in the main collection (`index.html`)
- **In Progress**: Dedicated `sujets0.html` page with enhanced UI and question data
- **Available Template**: `src/pca_graph_viz/tests/graphs/template_sujets0.py` for creating new graphs

## File Structure

```
scenery/
├── index.html          # Main collection page
├── app.js             # JavaScript for main collection
├── sujets0.html       # Sujets 0 dedicated page
├── sujets0-app.js     # JavaScript for Sujets 0 page
├── README.md          # This file
└── math_visualizations_1ere.md  # Documentation
```

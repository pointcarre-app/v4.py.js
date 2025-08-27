# 🚀 PCAGraphLoader - Simple Usage Guide

## Quick Start (Copy-Paste Ready)

### Option 1: Using the HTML Partial (Recommended)

Copy this into your HTML file:

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Include the partial - this loads everything needed -->
    {% include 'graph-loader-partial.html' %}
</head>
<body>
    <!-- Your graph container -->
    <div id="my-graph"></div>
    
    <script>
        // That's it! Just call this function
        document.addEventListener('DOMContentLoaded', async () => {
            await window.renderPCAGraph('my-graph', 'q7_small');
        });
    </script>
</body>
</html>
```

### Option 2: Direct CDN Import (No Server Needed)

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Dependencies -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/dist/full.min.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
</head>
<body>
    <div id="my-graph"></div>
    
    <script type="module">
        // Import the loader
        import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.15-unstable/scenery/packaged/PCAGraphLoader.js';
        
        // Use it
        const loader = new PCAGraphLoader();
        await loader.initialize();
        const result = await loader.renderGraph('q7_small');
        document.getElementById('my-graph').innerHTML = result.svg;
        
        // Access graph metadata
        console.log('Graph dict:', result.graphDict);
    </script>
</body>
</html>
```

## What Gets Loaded?

### From `graph-loader-partial.html`:
- ✅ DaisyUI CSS (for colors)
- ✅ KaTeX (for math formulas)
- ✅ PCAGraphLoader module
- ✅ Helper function `renderPCAGraph()`
- ✅ All necessary styles

### From JavaScript (automatic):
- ✅ Pyodide (Python in browser)
- ✅ Python graph modules
- ✅ SVG generation code

## Available Graphs

```javascript
// Question graphs
await renderPCAGraph('container', 'q7_small');    // Question 7
await renderPCAGraph('container', 'q8_small');    // Question 8
await renderPCAGraph('container', 'q11_case_a_small'); // Question 11 A
await renderPCAGraph('container', 'q11_case_b_small'); // Question 11 B
await renderPCAGraph('container', 'q11_case_c_small'); // Question 11 C

// Parabola graphs
await renderPCAGraph('container', 'parabola_s1_a0');  // y = x²
await renderPCAGraph('container', 'parabola_s1_am');  // y = x² - a
await renderPCAGraph('container', 'parabola_s1_ap');  // y = x² + a
await renderPCAGraph('container', 'parabola_sm1_a0'); // y = -x²
await renderPCAGraph('container', 'parabola_sm1_am'); // y = -x² - a
await renderPCAGraph('container', 'parabola_sm1_ap'); // y = -x² + a
```

## With Configuration

### Using the Helper Function
```javascript
await renderPCAGraph('my-graph', 'q8_small', {
    A_FLOAT_FOR_AFFINE_LINE: 1.5,    // Slope
    B_FLOAT_FOR_AFFINE_LINE: -2      // Y-intercept
});
```

### Direct API Usage
```javascript
const loader = new PCAGraphLoader();
await loader.initialize();

// Pass config directly to renderGraph (temporary override)
const result = await loader.renderGraph('q8_small', {
    A_FLOAT_FOR_AFFINE_LINE: 1.5,
    B_FLOAT_FOR_AFFINE_LINE: -2
});
document.getElementById('graph').innerHTML = result.svg;
console.log('Graph metadata:', result.graphDict);

// Or update config permanently
loader.updateConfig({
    A_SHIFT_MAGNITUDE: 8
});
const result2 = await loader.renderGraph('parabola_s1_ap');

// For backward compatibility, use renderGraphSvg for SVG only
const svgOnly = await loader.renderGraphSvg('q7_small');
```

## Files You Need

If copying files locally:
```
your-project/
├── graph-loader-partial.html   # Include this in your HTML
└── (that's it!)
```

Everything else loads from CDN automatically!

## Browser Requirements

- Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Internet connection (for CDN resources)

## That's It! 🎉

No installation, no build step, no configuration. Just include and use!

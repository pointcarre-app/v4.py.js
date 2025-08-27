# PCA Graph Loader - Integration Guide

## Quick Start

### 1. Copy the Fragment
Copy the contents of `graph-loader-partial.html` into your template system.

### 2. Include in Your Page
```html
<!-- For Jinja2 -->
{% include 'graph-loader-partial.html' %}

<!-- For Django -->
{% include 'graph-loader-partial.html' %}

<!-- For direct HTML -->
<!-- Paste the fragment contents here -->
```

### 3. Add a Container
```html
<div id="my-graph"></div>
```

### 4. Render the Graph
```javascript
document.addEventListener('DOMContentLoaded', async () => {
    await window.renderPCAGraph('my-graph', 'q8_small');
});
```

## Minimal Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Math Page</title>
    <!-- Include the fragment here -->
    {% include 'graph-loader-partial.html' %}
</head>
<body>
    <h1>Quadratic Functions</h1>
    
    <div id="parabola-graph"></div>
    
    <script>
        document.addEventListener('DOMContentLoaded', async () => {
            await window.renderPCAGraph('parabola-graph', 'parabola_s1_a0');
        });
    </script>
</body>
</html>
```

## Key Features of the Fragment

### 1. **Minimal CSS Impact**
- All styles are scoped to `.pca-graph-container`
- Uses DaisyUI's standard CSS variables (--p, --s, --a, etc.)
- Won't interfere with your existing styles (unless you also use DaisyUI)

### 2. **Self-Contained Dependencies**
- DaisyUI for consistent styling and color system
- KaTeX for LaTeX rendering (with integrity checks)
- PCAGraphLoader from CDN
- No additional libraries needed

### 3. **Simple API**
```javascript
// Basic usage
await window.renderPCAGraph(containerId, graphType);

// With configuration
await window.renderPCAGraph(containerId, graphType, {
    A_SHIFT_MAGNITUDE: 7
});
```

### 4. **Automatic Features**
- LaTeX rendering for mathematical notation
- Loading states
- Error handling
- Cached loader instance for performance

## CSS Customization

The graphs use DaisyUI's color system. To customize colors, use DaisyUI's CSS variables:

```css
:root {
    --p: 221 83% 53%;    /* Primary color (HSL) */
    --s: 262 52% 46%;    /* Secondary color (HSL) */
    --a: 0 84% 60%;      /* Accent color (HSL) */
    --bc: 215 28% 17%;   /* Base content (HSL) */
    --b1: 0 0% 100%;     /* Base-100 (HSL) */
    --b2: 0 0% 95%;      /* Base-200 (HSL) */
    --b3: 0 0% 90%;      /* Base-300 (HSL) */
}
```

Or use any DaisyUI theme: https://daisyui.com/docs/themes/

## Files Included

- **graph-loader-partial.html** - The complete HTML fragment to include
- **JINJA_USAGE.md** - Detailed Jinja integration examples
- **fragment-example.html** - Working standalone example
- **INTEGRATION_GUIDE.md** - This file

## Requirements

- Modern browser with ES6 module support
- Internet connection (for CDN resources)
- A container element with unique ID

## Troubleshooting

### Graph Not Rendering
1. Check browser console for errors
2. Ensure container ID exists
3. Verify internet connection (CDN access)
4. Check graph type is valid

### Styling Issues
1. Ensure fragment CSS is included
2. Check for CSS conflicts with `.pca-graph-container`
3. Verify CSS variables are defined if customized

### Performance
- First load takes 5-10 seconds (Pyodide initialization)
- Subsequent graphs render in < 1 second
- Loader instance is cached automatically

## Support

For issues or questions, visit: https://github.com/pointcarre-app/v4.py.js

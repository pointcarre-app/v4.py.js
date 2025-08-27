# PCAGraphLoader API Documentation

A modular, reusable JavaScript class for loading and rendering PCA mathematical visualization graphs using Pyodide and Nagini.

## Overview

`PCAGraphLoader` provides a clean, class-based API for loading individual mathematical graphs from the PCA visualization system. It handles:

- Dynamic module loading from local or CDN sources
- Configuration injection for parameterized graphs
- Caching and lazy loading
- SVG rendering through Pyodide

## Installation

### From CDN (jsDelivr)

```javascript
// Latest version
import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.12-unstable/scenery/packaged/PCAGraphLoader.js';

// Specific version
import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.12-unstable/scenery/packaged/PCAGraphLoader.js';
```

### Local Development

```javascript
import { PCAGraphLoader } from './packaged/PCAGraphLoader.js';
```

## Quick Start

```javascript
// Create loader instance
const loader = new PCAGraphLoader({
  debug: true,
  graphConfig: {
    Y_LABEL_FOR_HORIZONTAL_LINE: 10,
    A_FLOAT_FOR_AFFINE_LINE: 0.75,
    B_FLOAT_FOR_AFFINE_LINE: 2.0,
    A_SHIFT_MAGNITUDE: 5
  }
});

// Initialize (loads Nagini and core modules)
await loader.initialize();

// Load and render a specific graph
const svg = await loader.renderGraph('q8_small');
console.log(svg); // SVG string output

// Get graph dictionary without rendering
const graphDict = await loader.loadGraph('q8_small');
console.log(graphDict); // Graph configuration object
```

## API Reference

### Constructor

```javascript
new PCAGraphLoader(options)
```

#### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `naginiVersion` | string | `'0.0.21'` | Nagini library version |
| `pcaVersion` | string | `'v0.0.12-unstable'` | PCA library version for CDN |
| `baseUrl` | string | `'auto'` | Base URL for loading files. Use `'auto'` for automatic detection |
| `graphConfig` | object | `{}` | Initial graph configuration parameters |
| `debug` | boolean | `true` | Enable debug logging to console |
| `naginiCdnPath` | string | auto | Override Nagini CDN URL |
| `workerCdnPath` | string | auto | Override Pyodide worker URL |

### Methods

#### `initialize()`

Initialize the loader, set up Nagini manager, and load core modules.

```javascript
await loader.initialize();
```

Returns: `Promise<NaginiManager>` - The initialized Nagini manager instance

#### `loadGraph(graphKey)`

Load a specific graph by its key.

```javascript
const graphDict = await loader.loadGraph('q8_small');
```

Parameters:
- `graphKey` (string): The graph identifier

Returns: `Promise<Object>` - The graph dictionary/configuration

#### `renderGraph(graphKey)`

Load and render a graph to SVG.

```javascript
const svg = await loader.renderGraph('q8_small');
```

Parameters:
- `graphKey` (string): The graph identifier

Returns: `Promise<string>` - The SVG output as a string

#### `updateConfig(config)`

Update graph configuration parameters. Clears cache to force reload with new values.

```javascript
loader.updateConfig({
  A_SHIFT_MAGNITUDE: 7,
  A_FLOAT_FOR_AFFINE_LINE: 1.5
});
```

Parameters:
- `config` (object): Partial configuration to merge with existing

#### `getAvailableGraphs()`

Get list of available graph keys.

```javascript
const graphs = loader.getAvailableGraphs();
// ['q7_small', 'q8_small', 'q11_case_a_small', ...]
```

Returns: `Array<string>` - Available graph keys

#### `getConfig()`

Get current configuration.

```javascript
const config = loader.getConfig();
```

Returns: `Object` - Current graph configuration

## Available Graphs

| Key | Description |
|-----|-------------|
| `q7_small` | Question 7 - Parabola with horizontal line |
| `q8_small` | Question 8 - Affine function y = ax + b |
| `q11_case_a_small` | Question 11 - Case A |
| `q11_case_b_small` | Question 11 - Case B |
| `q11_case_c_small` | Question 11 - Case C |
| `parabola_s1_a0` | Parabola y = x² |
| `parabola_s1_am` | Parabola y = x² - a |
| `parabola_s1_ap` | Parabola y = x² + a |
| `parabola_sm1_a0` | Parabola y = -x² |
| `parabola_sm1_am` | Parabola y = -x² - a |
| `parabola_sm1_ap` | Parabola y = -x² + a |

## Configuration Parameters

| Parameter | Type | Default | Used By |
|-----------|------|---------|---------|
| `Y_LABEL_FOR_HORIZONTAL_LINE` | number | 10 | Question 7 graphs |
| `A_FLOAT_FOR_AFFINE_LINE` | number | 0.75 | Question 8 graphs (slope) |
| `B_FLOAT_FOR_AFFINE_LINE` | number | 2.0 | Question 8 graphs (y-intercept) |
| `A_SHIFT_MAGNITUDE` | number | 5 | Parabola graphs (vertical shift) |

## Advanced Usage

### Custom Base URL

```javascript
const loader = new PCAGraphLoader({
  baseUrl: 'https://my-cdn.com/pca-graphs',
  naginiCdnPath: 'https://my-cdn.com/nagini.js',
  workerCdnPath: 'https://my-cdn.com/worker.js'
});
```

### Batch Loading

```javascript
// Load multiple graphs efficiently
const graphs = ['q7_small', 'q8_small', 'q11_case_a_small'];
const results = await Promise.all(
  graphs.map(key => loader.loadGraph(key))
);
```

### Error Handling

```javascript
try {
  const svg = await loader.renderGraph('q8_small');
  // Use SVG
} catch (error) {
  console.error('Failed to render graph:', error.message);
  // Handle error
}
```

### Direct Manager Access

```javascript
// After initialization, access Pyodide manager directly
await loader.initialize();
const manager = loader.manager;

// Execute custom Python code
const result = await manager.executeAsync('custom.py', `
print("Custom Python execution")
`);
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

Requires support for:
- ES Modules
- Dynamic imports
- Web Workers
- Async/await

## Integration Examples

### React Component

```jsx
import { useEffect, useState } from 'react';
import { PCAGraphLoader } from './PCAGraphLoader.js';

function GraphViewer({ graphKey, config }) {
  const [svg, setSvg] = useState(null);
  const [loader] = useState(() => new PCAGraphLoader({ graphConfig: config }));
  
  useEffect(() => {
    (async () => {
      await loader.initialize();
      const svgOutput = await loader.renderGraph(graphKey);
      setSvg(svgOutput);
    })();
  }, [graphKey]);
  
  return <div dangerouslySetInnerHTML={{ __html: svg }} />;
}
```

### Vue Component

```vue
<template>
  <div v-html="svg"></div>
</template>

<script>
import { PCAGraphLoader } from './PCAGraphLoader.js';

export default {
  props: ['graphKey', 'config'],
  data() {
    return {
      svg: null,
      loader: null
    };
  },
  async mounted() {
    this.loader = new PCAGraphLoader({ graphConfig: this.config });
    await this.loader.initialize();
    this.svg = await this.loader.renderGraph(this.graphKey);
  }
};
</script>
```

### Vanilla JavaScript

```html
<!DOCTYPE html>
<html>
<head>
  <title>Graph Display</title>
</head>
<body>
  <div id="graph-container"></div>
  
  <script type="module">
    import { PCAGraphLoader } from './PCAGraphLoader.js';
    
    async function displayGraph() {
      const loader = new PCAGraphLoader();
      await loader.initialize();
      
      const svg = await loader.renderGraph('q8_small');
      document.getElementById('graph-container').innerHTML = svg;
    }
    
    displayGraph();
  </script>
</body>
</html>
```

## Troubleshooting

### CORS Issues

If loading files locally, ensure your web server has proper CORS headers:

```javascript
// Development server example (Vite, Webpack Dev Server)
{
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
}
```

### Module Not Found

Ensure the graph key exists:

```javascript
console.log(loader.getAvailableGraphs());
```

### Slow Initial Load

The first initialization loads Pyodide and core modules. Cache the loader instance:

```javascript
// Singleton pattern
let loaderInstance;

export async function getLoader() {
  if (!loaderInstance) {
    loaderInstance = new PCAGraphLoader();
    await loaderInstance.initialize();
  }
  return loaderInstance;
}
```

## License

This package is part of the PCA v4.py.js project under the AGPL-3.0 license.

## Support

For issues or questions, please visit the [GitHub repository](https://github.com/pointcarre-app/v4.py.js).

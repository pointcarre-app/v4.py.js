# PCAGraphLoader Package Summary

## What Was Created

This package provides a clean, reusable class-based API for loading and rendering PCA mathematical graphs from external repositories.

### Files Created

```
scenery/packaged/
├── PCAGraphLoader.js       # Main class module
├── test.html              # Testing interface 
├── example-external-usage.html  # External usage example
├── README.md              # Full API documentation
└── PACKAGE_SUMMARY.md     # This file
```

## Key Features

### 1. **Clean Class-Based API**

```javascript
const loader = new PCAGraphLoader(options);
await loader.initialize();
const svg = await loader.renderGraph('q8_small');
```

### 2. **Dynamic CDN Loading**

- Automatically detects environment (local vs production)
- Uses jsDelivr CDN for GitHub-hosted content
- No installation required for external users

### 3. **Managed Dependencies**

- Handles Nagini/Pyodide initialization
- Loads only required Python modules
- Caches loaded graphs for performance

### 4. **Configurable Parameters**

```javascript
loader.updateConfig({
  Y_LABEL_FOR_HORIZONTAL_LINE: 15,
  A_SHIFT_MAGNITUDE: 7
});
```

## Available Graphs (Small Variants Only)

- **Question 7**: `q7_small`
- **Question 8**: `q8_small`
- **Question 11**: `q11_case_a_small`, `q11_case_b_small`, `q11_case_c_small`
- **Parabolas**: `parabola_s1_a0`, `parabola_s1_am`, `parabola_s1_ap`, `parabola_sm1_a0`, `parabola_sm1_am`, `parabola_sm1_ap`

## Usage From External Repository

### Option 1: Direct CDN Import

```javascript
import { PCAGraphLoader } from 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.12-unstable/scenery/packaged/PCAGraphLoader.js';

const loader = new PCAGraphLoader();
await loader.initialize();
const svg = await loader.renderGraph('q8_small');
```

### Option 2: Local Development

```javascript
import { PCAGraphLoader } from './path/to/PCAGraphLoader.js';
```

## Testing

1. **Local Testing**: Open `test.html` in browser
2. **Console Testing**: Use `window.loader` after initialization
3. **External Testing**: Use `example-external-usage.html`

## Configuration

The loader accepts these configuration parameters:

- `Y_LABEL_FOR_HORIZONTAL_LINE`: Controls Q7 horizontal line position
- `A_FLOAT_FOR_AFFINE_LINE`: Controls Q8 line slope
- `B_FLOAT_FOR_AFFINE_LINE`: Controls Q8 y-intercept
- `A_SHIFT_MAGNITUDE`: Controls Q10 parabola vertical shift

## Architecture

```
External App
     ↓
PCAGraphLoader (JS)
     ↓
Nagini Manager
     ↓
Pyodide Worker
     ↓
Python Modules
     ↓
SVG Output
```

## URLs Configuration

The package automatically handles URL resolution:

- **Local**: Uses `http://localhost:PORT`
- **Production**: Uses `https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@VERSION`
- **Nagini CDN**: `https://cdn.jsdelivr.net/gh/pointcarre-app/nagini@0.0.21`

## Benefits Over Original Implementation

1. **Encapsulation**: All functionality in a single class
2. **No Global Variables**: Clean namespace
3. **Reusable**: Can be imported in any project
4. **Versioned**: Can pin specific versions via CDN
5. **Lazy Loading**: Only loads needed graphs
6. **Error Handling**: Proper promise-based error handling
7. **Configuration Management**: Clean API for updates

## Integration Points

The loader can be integrated with:

- React/Vue/Angular components
- Vanilla JavaScript applications
- Server-side rendering (with appropriate polyfills)
- Jupyter notebooks (via JS cells)
- Educational platforms

## Performance Considerations

- First initialization: ~5-10 seconds (loads Pyodide)
- Subsequent graph loads: ~100-500ms
- Graphs are cached after first load
- Configuration changes clear cache

## Browser Requirements

- ES Modules support
- Dynamic imports
- Web Workers
- Modern JavaScript (ES2020+)

## License

Part of PCA v4.py.js project under AGPL-3.0 license.

## Support

For issues or improvements, see the main repository at https://github.com/pointcarre-app/v4.py.js

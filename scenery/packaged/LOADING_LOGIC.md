# PCAGraphLoader - Loading Logic Documentation

## Overview

The PCAGraphLoader uses smart detection to determine whether to load files locally or from CDN, based on the **port number** rather than just hostname.

## Detection Logic

```javascript
const isV4PyJsLocal = window.location.port === "8022";
```

### Why Port 8022?

- **Port 8022** is the dedicated port for the v4.py.js development server (`serve.py`)
- This ensures that only the actual v4.py.js repository server is detected as "local"
- Other local servers (e.g., on ports 3000, 5000, 5001, 8080) will use CDN

## Loading Behavior

### When on Port 8022 (v4.py.js Local)
```
✅ Detected: v4.py.js local server
📁 Base URL: http://localhost:8022
📂 Files loaded from: Local filesystem
```

### When on Any Other Port or Domain
```
📦 Detected: External usage
🌐 Base URL: https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.15-unstable
☁️ Files loaded from: jsDelivr CDN
```

## Usage Examples

### 1. Auto Detection (Recommended)

```javascript
const loader = new PCAGraphLoader({
    // baseUrl: 'auto' is the default
});

// Will automatically use:
// - Local files if on port 8022
// - CDN files everywhere else
```

### 2. Force CDN (Production)

```javascript
const loader = new PCAGraphLoader({
    baseUrl: 'https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.15-unstable'
});
```

### 3. Force Local (Development Only)

```javascript
const loader = new PCAGraphLoader({
    baseUrl: 'http://localhost:8022'
});
// ⚠️ Will only work when v4.py.js server is running on port 8022
```

## Version Management

Current version: **v0.0.15-unstable**

To update the version:
1. Change `pcaVersion` in the PCAGraphLoader constructor default
2. Update all CDN URLs in documentation and examples
3. Ensure the tag exists on GitHub

## Testing

Use `test-loading-logic.html` to verify the detection is working correctly:

```bash
# From v4.py.js repo (will detect as local)
python serve.py
# Visit: http://localhost:8022/scenery/packaged/test-loading-logic.html

# From another server (will use CDN)
python -m http.server 8080
# Visit: http://localhost:8080/scenery/packaged/test-loading-logic.html
```

## Benefits

1. **No False Positives**: Only the actual v4.py.js server is detected as local
2. **CDN by Default**: All external usage automatically uses CDN
3. **No Configuration**: Works out of the box for most use cases
4. **Reliable**: Port-based detection is more reliable than hostname-based

## Common Scenarios

| Scenario | Port | Detection | Files From |
|----------|------|-----------|------------|
| v4.py.js dev server | 8022 | Local | localhost:8022 |
| React dev server | 3000 | CDN | jsDelivr |
| Vue dev server | 8080 | CDN | jsDelivr |
| Flask dev server | 5000 | CDN | jsDelivr |
| Django dev server | 8000 | CDN | jsDelivr |
| Production website | 443/80 | CDN | jsDelivr |
| GitHub Pages | - | CDN | jsDelivr |

## Troubleshooting

### Files not loading (404 errors)

1. **On port 8022**: Ensure `serve.py` is running
2. **Other ports**: Check GitHub tag exists (`v0.0.15-unstable`)
3. **Network issues**: Check jsDelivr is accessible

### Wrong files being loaded

1. Check `window.location.port` in console
2. Verify it matches expected behavior above
3. Use manual `baseUrl` override if needed

### Performance issues

1. First load takes 5-10s (Pyodide initialization)
2. Subsequent loads should be instant (cached)
3. CDN may be slower on first access (caching)

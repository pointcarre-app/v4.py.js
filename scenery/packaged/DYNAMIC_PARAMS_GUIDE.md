# Guide: Dynamic Parameters with PCAGraphLoader

## 📋 Overview

PCAGraphLoader v1.1.0 (from v0.0.24) supports dynamic parameter injection into Python graph modules. This allows you to generate graphs with different values based on question data.

## ⚙️ How It Works

### 1. Python Modules Check for Injected Variables

```python
# In the Python graph module
def get_graph_dict(y_horizontal=None):
    if "Y_LABEL_FOR_HORIZONTAL_LINE" not in globals():
        raise NameError("Variable must be injected")
    
    # Access via globals()
    y_value = y_horizontal if y_horizontal is not None else globals()["Y_LABEL_FOR_HORIZONTAL_LINE"]
```

### 2. PCAGraphLoader Injects Variables

When you call `renderGraph()`, PCAGraphLoader:
1. Takes your config parameters
2. Injects them into the Python module's namespace
3. Calls the graph's `get_graph_dict()` function
4. The function can access the injected values via `globals()`

## 🎯 Usage Pattern

### ❌ DON'T: Set Default Config at Initialization

```javascript
// DON'T DO THIS - values are fixed at initialization
const loader = new PCAGraphLoader({
    graphConfig: {
        Y_LABEL_FOR_HORIZONTAL_LINE: 10,  // Fixed value!
        A_FLOAT_FOR_AFFINE_LINE: 0.75,    // Fixed value!
        B_FLOAT_FOR_AFFINE_LINE: 2.0      // Fixed value!
    }
});
```

### ✅ DO: Pass Values Dynamically at Render Time

```javascript
// Initialize without config
const loader = new PCAGraphLoader({ 
    debug: false 
});
await loader.initialize();

// Later, when generating questions...
for (const student of students) {
    // Get dynamic values from question generation
    const yValue = generateRandomY();  // e.g., returns 15
    
    // Pass the dynamic value when rendering
    const result = await loader.renderGraph("q7_small", {
        Y_LABEL_FOR_HORIZONTAL_LINE: yValue  // Dynamic value!
    });
}
```

## 📊 Complete Example

```javascript
import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.24/scenery/packaged/PCAGraphLoader.js";

// Initialize once
const loader = new PCAGraphLoader({ debug: false });
await loader.initialize();

// Generate questions with dynamic graphs
async function generateQuestionWithGraph(questionData) {
    let graphSvg = null;
    
    // Question 7: Parabola with horizontal line
    if (questionData.type === "q7") {
        const yValue = parseInt(questionData.components.n);
        const result = await loader.renderGraph("q7_small", {
            Y_LABEL_FOR_HORIZONTAL_LINE: yValue
        });
        graphSvg = result.svg;
    }
    
    // Question 8: Affine function
    else if (questionData.type === "q8") {
        const result = await loader.renderGraph("q8_small", {
            A_FLOAT_FOR_AFFINE_LINE: parseFloat(questionData.components.a),
            B_FLOAT_FOR_AFFINE_LINE: parseFloat(questionData.components.b)
        });
        graphSvg = result.svg;
    }
    
    // Question 10: Parabolas with shift
    else if (questionData.type === "q10") {
        const shiftValue = parseInt(questionData.components.shift);
        const graphKey = questionData.components.variant; // e.g., "parabola_s1_ap"
        const result = await loader.renderGraph(graphKey, {
            A_SHIFT_MAGNITUDE: shiftValue
        });
        graphSvg = result.svg;
    }
    
    return graphSvg;
}
```

## 🔑 Available Parameters

### Question 7 (Parabola with Horizontal Line)
- `Y_LABEL_FOR_HORIZONTAL_LINE`: Y-coordinate of the horizontal line

### Question 8 (Affine Function)
- `A_FLOAT_FOR_AFFINE_LINE`: Slope coefficient (a)
- `B_FLOAT_FOR_AFFINE_LINE`: Y-intercept (b)

### Question 10 (Parabolas)
- `A_SHIFT_MAGNITUDE`: Vertical shift magnitude

### Question 11 (Cubic Functions)
- No parameters needed (fixed root positions)

## 🐛 Troubleshooting

### Error: "Variable must be injected into module namespace"

**Cause**: The Python module expects a variable that wasn't provided.

**Solution**: Make sure you pass all required parameters:

```javascript
// For Q7
await loader.renderGraph("q7_small", {
    Y_LABEL_FOR_HORIZONTAL_LINE: 10  // Required!
});

// For Q8
await loader.renderGraph("q8_small", {
    A_FLOAT_FOR_AFFINE_LINE: 0.75,   // Required!
    B_FLOAT_FOR_AFFINE_LINE: 2.0     // Required!
});
```

### Parameters Not Reflected in Graph

**Cause**: Using an old version or initializing with fixed config.

**Solution**: 
1. Use v0.0.24 or later
2. Don't set `graphConfig` at initialization
3. Pass values at `renderGraph()` time

## 📋 Testing

Use `test-dynamic-params.html` to verify dynamic parameters work:

```bash
# Serve locally
python -m http.server 8022

# Open in browser
http://localhost:8022/scenery/packaged/test-dynamic-params.html
```

## 🎉 Benefits

1. **Dynamic Generation**: Each student gets different graph values
2. **Question-Driven**: Graph parameters come from question data
3. **Flexible**: Change values without reinitializing the loader
4. **Efficient**: One loader instance handles all variations

## 📦 Version Requirements

- PCAGraphLoader v1.1.0 or later
- pca-v4.py.js v0.0.24 or later
- Python modules with `globals()` access pattern

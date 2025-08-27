# PCA Graph Loader - Complete Graph Reference

## All Available Graphs with Configurations

Below are all the graphs from your list of interest, with the exact code to render each one.

### Question 7: Parabola with Horizontal Line

```javascript
// Default configuration
await window.renderPCAGraph('container-id', 'q7_small');

// With custom Y label for horizontal line
await window.renderPCAGraph('container-id', 'q7_small', {
    Y_LABEL_FOR_HORIZONTAL_LINE: 15  // Change the y-position of the horizontal line
});

// Different Y values
await window.renderPCAGraph('container-id', 'q7_small', {
    Y_LABEL_FOR_HORIZONTAL_LINE: -10
});

await window.renderPCAGraph('container-id', 'q7_small', {
    Y_LABEL_FOR_HORIZONTAL_LINE: 25
});
```

### Question 8: Affine Function (y = ax + b)

```javascript
// Default configuration (y = 0.75x + 2)
await window.renderPCAGraph('container-id', 'q8_small');

// Custom slope and intercept
await window.renderPCAGraph('container-id', 'q8_small', {
    A_FLOAT_FOR_AFFINE_LINE: 1.5,   // Slope
    B_FLOAT_FOR_AFFINE_LINE: -3     // Y-intercept
});

// Negative slope
await window.renderPCAGraph('container-id', 'q8_small', {
    A_FLOAT_FOR_AFFINE_LINE: -0.5,
    B_FLOAT_FOR_AFFINE_LINE: 4
});

// Steep positive slope
await window.renderPCAGraph('container-id', 'q8_small', {
    A_FLOAT_FOR_AFFINE_LINE: 2.5,
    B_FLOAT_FOR_AFFINE_LINE: 0
});
```

### Question 11: Three Cases (A, B, C)

```javascript
// Case A
await window.renderPCAGraph('container-id', 'q11_case_a_small');

// Case B  
await window.renderPCAGraph('container-id', 'q11_case_b_small');

// Case C
await window.renderPCAGraph('container-id', 'q11_case_c_small');
```

### Question 10: Parabolas with s=1 (Opening Upward)

```javascript
// y = x² (no shift)
await window.renderPCAGraph('container-id', 'parabola_s1_a0');

// y = x² - a (shifted down)
await window.renderPCAGraph('container-id', 'parabola_s1_am', {
    A_SHIFT_MAGNITUDE: 5  // Shift magnitude (1-10)
});

// y = x² + a (shifted up)
await window.renderPCAGraph('container-id', 'parabola_s1_ap', {
    A_SHIFT_MAGNITUDE: 5
});

// Different shift magnitudes
await window.renderPCAGraph('container-id', 'parabola_s1_ap', {
    A_SHIFT_MAGNITUDE: 10  // Maximum shift
});

await window.renderPCAGraph('container-id', 'parabola_s1_am', {
    A_SHIFT_MAGNITUDE: 3   // Smaller shift
});
```

### Question 10: Parabolas with s=-1 (Opening Downward)

```javascript
// y = -x² (no shift)
await window.renderPCAGraph('container-id', 'parabola_sm1_a0');

// y = -x² - a (shifted down)
await window.renderPCAGraph('container-id', 'parabola_sm1_am', {
    A_SHIFT_MAGNITUDE: 5
});

// y = -x² + a (shifted up)
await window.renderPCAGraph('container-id', 'parabola_sm1_ap', {
    A_SHIFT_MAGNITUDE: 5
});

// Different shift magnitudes
await window.renderPCAGraph('container-id', 'parabola_sm1_ap', {
    A_SHIFT_MAGNITUDE: 8
});

await window.renderPCAGraph('container-id', 'parabola_sm1_am', {
    A_SHIFT_MAGNITUDE: 2
});
```

## Complete HTML Example with All Graphs

```html
<!DOCTYPE html>
<html>
<head>
    <title>All PCA Graphs</title>
    {% include 'graph-loader-partial.html' %}
</head>
<body>
    <h1>Complete Graph Gallery</h1>

    <!-- Question 7 -->
    <h2>Question 7: Parabola with Horizontal Line</h2>
    <div id="q7"></div>

    <!-- Question 8 -->
    <h2>Question 8: Affine Function</h2>
    <div id="q8"></div>

    <!-- Question 11 -->
    <h2>Question 11 - Case A</h2>
    <div id="q11a"></div>
    
    <h2>Question 11 - Case B</h2>
    <div id="q11b"></div>
    
    <h2>Question 11 - Case C</h2>
    <div id="q11c"></div>

    <!-- Parabolas s=1 -->
    <h2>Parabola: y = x²</h2>
    <div id="p-s1-a0"></div>
    
    <h2>Parabola: y = x² - 5</h2>
    <div id="p-s1-am"></div>
    
    <h2>Parabola: y = x² + 5</h2>
    <div id="p-s1-ap"></div>

    <!-- Parabolas s=-1 -->
    <h2>Parabola: y = -x²</h2>
    <div id="p-sm1-a0"></div>
    
    <h2>Parabola: y = -x² - 5</h2>
    <div id="p-sm1-am"></div>
    
    <h2>Parabola: y = -x² + 5</h2>
    <div id="p-sm1-ap"></div>

    <script>
        document.addEventListener('DOMContentLoaded', async () => {
            // Question 7
            await window.renderPCAGraph('q7', 'q7_small', {
                Y_LABEL_FOR_HORIZONTAL_LINE: 10
            });

            // Question 8  
            await window.renderPCAGraph('q8', 'q8_small', {
                A_FLOAT_FOR_AFFINE_LINE: 0.75,
                B_FLOAT_FOR_AFFINE_LINE: 2
            });

            // Question 11 Cases
            await window.renderPCAGraph('q11a', 'q11_case_a_small');
            await window.renderPCAGraph('q11b', 'q11_case_b_small');
            await window.renderPCAGraph('q11c', 'q11_case_c_small');

            // Parabolas s=1
            await window.renderPCAGraph('p-s1-a0', 'parabola_s1_a0');
            await window.renderPCAGraph('p-s1-am', 'parabola_s1_am', {
                A_SHIFT_MAGNITUDE: 5
            });
            await window.renderPCAGraph('p-s1-ap', 'parabola_s1_ap', {
                A_SHIFT_MAGNITUDE: 5
            });

            // Parabolas s=-1
            await window.renderPCAGraph('p-sm1-a0', 'parabola_sm1_a0');
            await window.renderPCAGraph('p-sm1-am', 'parabola_sm1_am', {
                A_SHIFT_MAGNITUDE: 5
            });
            await window.renderPCAGraph('p-sm1-ap', 'parabola_sm1_ap', {
                A_SHIFT_MAGNITUDE: 5
            });
        });
    </script>
</body>
</html>
```

## Configuration Parameter Reference

| Parameter | Used By | Description | Range/Type |
|-----------|---------|-------------|------------|
| `Y_LABEL_FOR_HORIZONTAL_LINE` | `q7_small` | Y-position of horizontal line | Number (-50 to 50) |
| `A_FLOAT_FOR_AFFINE_LINE` | `q8_small` | Slope of the line (a in y=ax+b) | Number (-10 to 10) |
| `B_FLOAT_FOR_AFFINE_LINE` | `q8_small` | Y-intercept (b in y=ax+b) | Number (-20 to 20) |
| `A_SHIFT_MAGNITUDE` | All parabola graphs | Vertical shift magnitude | Integer (1 to 10) |

## Graph Key Summary

| Graph Key | Description | Configuration Support |
|-----------|-------------|----------------------|
| `q7_small` | Parabola with horizontal line | Y_LABEL_FOR_HORIZONTAL_LINE |
| `q8_small` | Affine function | A_FLOAT_FOR_AFFINE_LINE, B_FLOAT_FOR_AFFINE_LINE |
| `q11_case_a_small` | Question 11 Case A | None |
| `q11_case_b_small` | Question 11 Case B | None |
| `q11_case_c_small` | Question 11 Case C | None |
| `parabola_s1_a0` | y = x² | None |
| `parabola_s1_am` | y = x² - a | A_SHIFT_MAGNITUDE |
| `parabola_s1_ap` | y = x² + a | A_SHIFT_MAGNITUDE |
| `parabola_sm1_a0` | y = -x² | None |
| `parabola_sm1_am` | y = -x² - a | A_SHIFT_MAGNITUDE |
| `parabola_sm1_ap` | y = -x² + a | A_SHIFT_MAGNITUDE |

## Default Configuration Values

```javascript
{
    Y_LABEL_FOR_HORIZONTAL_LINE: 10,
    A_FLOAT_FOR_AFFINE_LINE: 0.75,
    B_FLOAT_FOR_AFFINE_LINE: 2.0,
    A_SHIFT_MAGNITUDE: 5
}
```

## Notes

- All graphs use the small variant (optimized for web display)
- The loader caches graphs with their configuration, so changing config requires reloading
- First load takes 5-10 seconds (Pyodide initialization), subsequent loads are instant
- Colors are controlled by DaisyUI theme variables (--p, --s, --a, --bc, --b1, --b2, --b3)

# Using PCAGraphLoader in Jinja Templates

## 1. Include the Fragment

### Option A: Direct Include in Base Template
```jinja
{# In your base.html or layout template #}
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <!-- Your other head content -->
    
    {# Include PCA Graph dependencies #}
    {% include 'graph-loader-partial.html' %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### Option B: Conditional Include
```jinja
{# Only include when needed #}
{% if show_graphs %}
    {% include 'graph-loader-partial.html' %}
{% endif %}
```

### Option C: In a Specific Page
```jinja
{% extends "base.html" %}

{% block head %}
    {{ super() }}
    {% include 'graph-loader-partial.html' %}
{% endblock %}

{% block content %}
    <div id="my-graph"></div>
{% endblock %}
```

## 2. Render Graphs in Your Templates

### Simple Graph Display
```html
<div id="graph-q7"></div>

<script>
    // Render after page loads
    document.addEventListener('DOMContentLoaded', async () => {
        await window.renderPCAGraph('graph-q7', 'q7_small');
    });
</script>
```

### With Configuration
```html
<div id="graph-q8"></div>

<script>
    document.addEventListener('DOMContentLoaded', async () => {
        await window.renderPCAGraph('graph-q8', 'q8_small', {
            A_FLOAT_FOR_AFFINE_LINE: 0.75,
            B_FLOAT_FOR_AFFINE_LINE: 2.0
        });
    });
</script>
```

### Dynamic Graph from Jinja Variables
```jinja
<div id="graph-{{ graph_id }}"></div>

<script>
    document.addEventListener('DOMContentLoaded', async () => {
        await window.renderPCAGraph(
            'graph-{{ graph_id }}',
            '{{ graph_type }}',
            {{ graph_config | tojson }}
        );
    });
</script>
```

## 3. Flask/Django Integration

### Flask Example
```python
from flask import render_template

@app.route('/math-lesson/<lesson_id>')
def math_lesson(lesson_id):
    graph_configs = {
        'lesson1': {
            'graph_type': 'q7_small',
            'config': {'Y_LABEL_FOR_HORIZONTAL_LINE': 10}
        },
        'lesson2': {
            'graph_type': 'q8_small',
            'config': {
                'A_FLOAT_FOR_AFFINE_LINE': 1.5,
                'B_FLOAT_FOR_AFFINE_LINE': -3
            }
        }
    }
    
    lesson_config = graph_configs.get(lesson_id, {})
    
    return render_template('lesson.html',
        graph_type=lesson_config.get('graph_type', 'q7_small'),
        graph_config=lesson_config.get('config', {})
    )
```

### Django Example
```python
# views.py
from django.shortcuts import render
import json

def math_visualization(request, graph_type):
    config = {
        'Y_LABEL_FOR_HORIZONTAL_LINE': request.GET.get('y_label', 10),
        'A_SHIFT_MAGNITUDE': request.GET.get('shift', 5)
    }
    
    return render(request, 'math_viz.html', {
        'graph_type': graph_type,
        'graph_config': json.dumps(config)
    })
```

## 4. Multiple Graphs on Same Page

```jinja
{% for graph in graphs %}
<div class="graph-wrapper">
    <h3>{{ graph.title }}</h3>
    <div id="graph-{{ loop.index }}"></div>
</div>
{% endfor %}

<script>
document.addEventListener('DOMContentLoaded', async () => {
    const graphs = {{ graphs | tojson }};
    
    for (let i = 0; i < graphs.length; i++) {
        await window.renderPCAGraph(
            `graph-${i + 1}`,
            graphs[i].type,
            graphs[i].config || {}
        );
    }
});
</script>
```

## 5. Custom Styling

The graphs use DaisyUI's color system. Override with DaisyUI CSS variables:

```css
<style>
    /* Custom DaisyUI colors (HSL format) */
    :root {
        --p: 221 83% 53%;    /* Primary */
        --s: 262 52% 46%;    /* Secondary */
        --a: 0 84% 60%;      /* Accent */
        --bc: 215 28% 17%;   /* Base content */
        --b1: 0 0% 100%;     /* Base-100 */
        --b2: 0 0% 95%;      /* Base-200 */
        --b3: 0 0% 90%;      /* Base-300 */
    }
    
    /* Or use a DaisyUI theme */
    [data-theme="dark"] {
        /* Dark theme colors automatically applied */
    }
    
    /* Custom container styling */
    .pca-graph-container {
        margin: 2rem auto;
        max-width: 600px;
    }
</style>
```

## 6. Available Graph Types

- `q7_small` - Question 7 (Parabola with horizontal line)
- `q8_small` - Question 8 (Affine function)
- `q11_case_a_small` - Question 11 Case A
- `q11_case_b_small` - Question 11 Case B
- `q11_case_c_small` - Question 11 Case C
- `parabola_s1_a0` - y = x²
- `parabola_s1_am` - y = x² - a
- `parabola_s1_ap` - y = x² + a
- `parabola_sm1_a0` - y = -x²
- `parabola_sm1_am` - y = -x² - a
- `parabola_sm1_ap` - y = -x² + a

## 7. Configuration Parameters

```javascript
{
    Y_LABEL_FOR_HORIZONTAL_LINE: 10,  // For Q7
    A_FLOAT_FOR_AFFINE_LINE: 0.75,    // For Q8 (slope)
    B_FLOAT_FOR_AFFINE_LINE: 2.0,     // For Q8 (y-intercept)
    A_SHIFT_MAGNITUDE: 5               // For parabolas (1-10)
}
```

## 8. Error Handling

```javascript
window.renderPCAGraph('my-graph', 'q8_small')
    .then(() => console.log('Graph rendered successfully'))
    .catch(error => {
        console.error('Failed to render graph:', error);
        document.getElementById('my-graph').innerHTML = 
            '<p>Unable to load graph. Please try again later.</p>';
    });
```

## 9. Lazy Loading

Load graphs only when visible:

```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const graphEl = entry.target;
            const graphType = graphEl.dataset.graphType;
            const config = JSON.parse(graphEl.dataset.config || '{}');
            
            window.renderPCAGraph(graphEl.id, graphType, config);
            observer.unobserve(graphEl);
        }
    });
});

// Observe all graph containers
document.querySelectorAll('.lazy-graph').forEach(el => {
    observer.observe(el);
});
```

```html
<div id="graph1" class="lazy-graph" 
     data-graph-type="q7_small" 
     data-config='{"Y_LABEL_FOR_HORIZONTAL_LINE": 15}'>
</div>
```

## Notes

- The fragment is self-contained with all dependencies
- CSS is scoped to `.pca-graph-container` to avoid conflicts
- KaTeX is loaded with integrity checks for security
- The loader instance is cached for performance
- LaTeX rendering happens automatically if KaTeX is available

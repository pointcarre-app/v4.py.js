# 🔍 CHECKLIST DE DÉBOGAGE POUR L'AUTRE REPO

## ✅ Vérifications à faire:

### 1. **Version CDN**
```javascript
// ❌ MAUVAIS - ancienne version cachée
import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.20-unstable/scenery/packaged/PCAGraphLoader.js";

// ✅ BON - nouvelle version
import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.21-unstable/scenery/packaged/PCAGraphLoader.js";
```

### 2. **KaTeX dans votre HTML**
Votre fichier HTML doit contenir:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
```

### 3. **Initialisation du loader**
```javascript
// ❌ MAUVAIS - au niveau module
const graphLoader = new PCAGraphLoader({ debug: false });
await graphLoader.initialize();

// ✅ BON - dans la fonction
let graphLoader = null;
export async function executeAllGenerators() {
    if (!graphLoader) {
        graphLoader = new PCAGraphLoader({ debug: true }); // debug: true pour voir les logs
        await graphLoader.initialize();
    }
    // ...
}
```

### 4. **Rendu LaTeX après insertion des SVG**
```javascript
// Après avoir inséré les SVG dans le DOM
setTimeout(() => {
    if (typeof katex !== 'undefined') {
        document.querySelectorAll('.svg-latex').forEach(el => {
            const latex = el.textContent;
            if (latex) {
                el.innerHTML = '';
                katex.render(latex, el, {
                    throwOnError: false,
                    displayMode: false
                });
            }
        });
    }
}, 100);
```

### 5. **Vérifier dans la console du navigateur**

Ouvrez la console (F12) et vérifiez:

1. **Y a-t-il des erreurs 404?**
   - Si oui, vérifiez les URLs des imports

2. **Voyez-vous les logs?**
   ```
   🚀 Initializing PCAGraphLoader v0.0.21...
   ✅ PCAGraphLoader initialized
   📊 Q7: Y=15 for student 1
   ```

3. **Test rapide dans la console:**
   ```javascript
   // Testez directement dans la console
   import("https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.21-unstable/scenery/packaged/PCAGraphLoader.js")
     .then(module => console.log("Module loaded:", module))
     .catch(err => console.error("Failed:", err));
   ```

### 6. **Vérifier le cache du navigateur**
- Ouvrez en mode incognito/privé
- Ou faites Ctrl+Shift+R (hard refresh)

### 7. **Imports relatifs dans votre repo**
Si votre repo a des imports comme:
```javascript
import { executeGeneratorWithSeed } from "./index-nagini.js";
```
Assurez-vous que ces fichiers existent dans votre repo.

## 🧪 TEST MINIMAL

Créez ce fichier HTML minimal dans votre autre repo pour tester:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Test Minimal</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
</head>
<body>
    <h1>Test Minimal</h1>
    <div id="result"></div>
    
    <script type="module">
        import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.21-unstable/scenery/packaged/PCAGraphLoader.js";
        
        async function test() {
            try {
                console.log("Starting test...");
                const loader = new PCAGraphLoader({ debug: true });
                await loader.initialize();
                console.log("Loader initialized");
                
                const result = await loader.renderGraph("q7_small", {
                    Y_LABEL_FOR_HORIZONTAL_LINE: 15
                });
                
                document.getElementById('result').innerHTML = result.svg;
                
                // Check if parameter was applied
                if (result.svg.includes('y=15')) {
                    console.log("✅ SUCCESS: Parameters are working!");
                } else {
                    console.error("❌ FAIL: Parameters not reflected");
                }
                
                // Render LaTeX
                setTimeout(() => {
                    if (typeof katex !== 'undefined') {
                        document.querySelectorAll('.svg-latex').forEach(el => {
                            const latex = el.textContent;
                            if (latex) {
                                el.innerHTML = '';
                                katex.render(latex, el, {
                                    throwOnError: false
                                });
                            }
                        });
                        console.log("LaTeX rendered");
                    }
                }, 100);
                
            } catch (error) {
                console.error("Error:", error);
            }
        }
        
        test();
    </script>
</body>
</html>
```

## 🚨 SI RIEN NE MARCHE

Essayez avec `@latest` pour forcer le refresh:
```javascript
import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@latest/scenery/packaged/PCAGraphLoader.js";
```

Ou utilisez unpkg:
```javascript
import { PCAGraphLoader } from "https://unpkg.com/@pointcarre/pca-graph-viz@0.0.21-unstable/scenery/packaged/PCAGraphLoader.js";
```

## 📝 ENVOYEZ-MOI:

1. **L'URL exacte de l'import** que vous utilisez
2. **Les erreurs dans la console** (screenshot ou texte)
3. **Le code exact** de votre executeAllGenerators
4. **Ce que vous voyez** quand vous inspectez le SVG généré

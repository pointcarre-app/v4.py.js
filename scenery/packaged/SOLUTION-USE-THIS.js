/**
 * ✅ SOLUTION FINALE - UTILISEZ CE CODE!
 * 
 * Version v0.0.22: Force l'injection des paramètres depuis JavaScript
 * - Les fichiers Python n'ont plus de valeurs par défaut
 * - Génère une erreur explicite si les paramètres ne sont pas injectés
 * - Garantit que les valeurs configurées sont bien utilisées
 * 
 * IMPORTANT: Pour le rendu LaTeX, ajoutez KaTeX dans votre HTML:
 * <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
 * <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
 */

import { executeGeneratorWithSeed } from "./index-nagini.js";
import { getGeneratorConfig, displayValidationTable } from "./index-form.js";
import { displayStudentResults } from "./index-results.js";
import generationResults, { StudentExerciseSet } from "./index-data-model.js";

export { generationResults };

// 🔥 UTILISEZ v0.0.22 - Force l'injection des paramètres (breaking change)
import { PCAGraphLoader } from "https://cdn.jsdelivr.net/gh/pointcarre-app/v4.py.js@v0.0.22/scenery/packaged/PCAGraphLoader.js";

// Variable pour le loader
let graphLoader = null;

/**
 * Randomly select N items from an array
 */
export function selectRandomItems(array, n) {
  const shuffled = [...array].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, n);
}

/**
 * Execute all generators with pagination
 */
export async function executeAllGenerators() {
  // Check if Nagini is ready
  if (!window.Nagini) {
    const errorData = {
      copies: { count: "-", isValid: false },
      questions: { perCopy: "-", isValid: false },
      program: { level: null, isValid: false },
      track: { type: null, isValid: false },
      isComplete: false,
      errors: [
        {
          field: "system",
          message: "Nagini n'est pas prêt. Veuillez patienter quelques secondes.",
        },
      ],
    };
    displayValidationTable(errorData);
    return;
  }

  // Initialize loader HERE, not at module level
  if (!graphLoader) {
    console.log("🚀 Initializing PCAGraphLoader v0.0.22...");
    graphLoader = new PCAGraphLoader({ 
      debug: false  // Set to true if you want to see debug info
    });
    await graphLoader.initialize();
    console.log("✅ PCAGraphLoader initialized");
  }

  // Extract and validate form data
  const config = getGeneratorConfig();
  if (!config) {
    return;
  }

  console.log("Generator configuration:", config);
  generationResults.config = config;

  const executeBtn = document.getElementById("execute-all-generators-btn");
  if (executeBtn) {
    executeBtn.disabled = true;
    executeBtn.textContent = "Génération en cours...";
  }

  const allGenerators = [
    "spe_sujet1_auto_01_question.py",
    "spe_sujet1_auto_02_question.py",
    "spe_sujet1_auto_03_question.py",
    "spe_sujet1_auto_04_question.py",
    "spe_sujet1_auto_05_question.py",
    "spe_sujet1_auto_06_question.py",
    "spe_sujet1_auto_07_question.py",
    "spe_sujet1_auto_08_question.py",
    "spe_sujet1_auto_09_question.py",
    "spe_sujet1_auto_10_question.py",
    "spe_sujet1_auto_11_question.py",
    "spe_sujet1_auto_12_question.py",
  ];

  // Select generators
  let selectedGenerators;
  if (config.nbQuestions === 12) {
    selectedGenerators = [...allGenerators];
  } else {
    selectedGenerators = selectRandomItems(allGenerators, config.nbQuestions);
  }
  generationResults.selectedGenerators = selectedGenerators;

  console.log(`Selected ${config.nbQuestions} generators:`, selectedGenerators);

  // Reset results
  generationResults.reset();
  generationResults.setConfig(config);
  generationResults.setSelectedGenerators(selectedGenerators);

  // Get or create results container
  let resultsContainer = document.getElementById("generator-results-container");
  const wrapper = document.getElementById("generator-results-wrapper");

  if (!resultsContainer) {
    resultsContainer = document.createElement("div");
    resultsContainer.id = "generator-results-container";
    if (wrapper) {
      wrapper.appendChild(resultsContainer);
    } else {
      const validationContainer = document.getElementById("validation-status-container");
      if (validationContainer && validationContainer.parentNode) {
        validationContainer.parentNode.appendChild(resultsContainer);
      }
    }
  }

  resultsContainer.className = "mt-6";
  resultsContainer.innerHTML = `
    <div class="alert alert-info">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-current shrink-0 w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
      </svg>
      <span>Génération de ${config.nbStudents} copies avec ${config.nbQuestions} questions chacune...</span>
    </div>
    <progress class="progress progress-primary w-full mt-4" value="0" max="${config.nbStudents}"></progress>
  `;

  // Process each student
  for (let studentNum = 1; studentNum <= config.nbStudents; studentNum++) {
    const seed = Math.floor(Math.random() * 1_000);
    const questionResults = [];

    // Update progress
    const progressBar = resultsContainer.querySelector("progress");
    if (progressBar) {
      progressBar.value = studentNum - 1;
    }

    // Execute each selected generator for this student
    for (const generator of selectedGenerators) {
      const result = await executeGeneratorWithSeed(generator, seed);

      // Handle Question 7 - Parabola with horizontal line
      if (generator === "spe_sujet1_auto_07_question.py") {
        const yValue = parseInt(result.data.components.n);
        console.log(`📊 Q7: Y=${yValue} for student ${studentNum}`);
        
        const svgAndDict = await graphLoader.renderGraph("q7_small", {
          Y_LABEL_FOR_HORIZONTAL_LINE: yValue
        });

        result.graphSvg = svgAndDict.svg;
        result.graphDict = svgAndDict.graphDict;
      }
      
      // Handle Question 8 - Affine function
      else if (generator === "spe_sujet1_auto_08_question.py") {
        const aValue = parseFloat(result.data.components.a);
        const bValue = parseFloat(result.data.components.b);
        console.log(`📊 Q8: a=${aValue}, b=${bValue} for student ${studentNum}`);
        
        const svgAndDict = await graphLoader.renderGraph("q8_small", {
          A_FLOAT_FOR_AFFINE_LINE: aValue,
          B_FLOAT_FOR_AFFINE_LINE: bValue
        });

        result.graphSvg = svgAndDict.svg;
        result.graphDict = svgAndDict.graphDict;
      }

      questionResults.push(result);
    }

    // Create and store student exercise set
    const studentExerciseSet = StudentExerciseSet.fromGeneratorResults(
      studentNum,
      seed,
      questionResults,
      selectedGenerators
    );

    generationResults.addStudent(studentExerciseSet);
  }

  // Display first student's results
  displayStudentResults(0);
  
  // Render LaTeX in all generated SVGs
  renderLatexInGraphs();

  // Re-enable button
  if (executeBtn) {
    executeBtn.disabled = false;
    executeBtn.textContent = "Générer";
  }
}

/**
 * Render LaTeX equations in SVG graphs using KaTeX
 * Call this after inserting SVGs into the DOM
 */
export function renderLatexInGraphs() {
  // Wait a bit for DOM to update
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
      console.log('✅ LaTeX rendered in graphs');
    } else {
      console.warn('⚠️ KaTeX not loaded - add KaTeX scripts to your HTML');
    }
  }, 100);
}

/**
 * 🎯 POINTS IMPORTANTS:
 * 
 * 1. Utilisez v0.0.22 (version stable avec injection forcée)
 * 2. Initialisez graphLoader DANS la fonction, pas au niveau module
 * 3. Les paramètres DOIVENT être passés (pas de valeurs par défaut)
 * 
 * Breaking change v0.0.22:
 * - Les fichiers Python n'ont plus de valeurs par défaut
 * - Une erreur NameError est générée si les variables ne sont pas injectées
 * - Garantit que les configurations sont toujours respectées
 */

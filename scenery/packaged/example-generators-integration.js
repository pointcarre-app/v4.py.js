/**
 * Example of how to integrate PCAGraphLoader with your generators
 * This shows how to properly pass dynamic configuration values to graphs
 */

import { buildPCAGraph } from './index-graphs.js';

/**
 * Example usage in your executeAllGenerators function
 * This shows the relevant parts you need to update
 */
async function exampleGeneratorIntegration() {
    
    // ... your existing code ...
    
    // When processing generator results for each student:
    for (const generator of selectedGenerators) {
        const result = await executeGeneratorWithSeed(generator, seed);
        
        // Handle Question 7 - Parabola with horizontal line
        if (generator === 'spe_sujet1_auto_07_question.py') {
            // Extract the Y value from the generator result
            const Y_LABEL_FOR_HORIZONTAL_LINE = parseInt(result.data.components.n);
            
            // Build the graph with the dynamic configuration
            const svgAndDict = await buildPCAGraph('q7_small', {
                Y_LABEL_FOR_HORIZONTAL_LINE: Y_LABEL_FOR_HORIZONTAL_LINE
            });
            
            // Store the results
            result.graphSvg = svgAndDict.svg;
            result.graphDict = svgAndDict.graphDict;
            
            console.log(`✅ Q7 Graph generated with Y=${Y_LABEL_FOR_HORIZONTAL_LINE}`);
        }
        
        // Handle Question 8 - Affine function
        else if (generator === 'spe_sujet1_auto_08_question.py') {
            // Extract coefficients from the generator result
            const A_FLOAT_FOR_AFFINE_LINE = parseFloat(result.data.components.a);
            const B_FLOAT_FOR_AFFINE_LINE = parseFloat(result.data.components.b);
            
            // Build the graph with the dynamic configuration
            const svgAndDict = await buildPCAGraph('q8_small', {
                A_FLOAT_FOR_AFFINE_LINE: A_FLOAT_FOR_AFFINE_LINE,
                B_FLOAT_FOR_AFFINE_LINE: B_FLOAT_FOR_AFFINE_LINE
            });
            
            // Store the results
            result.graphSvg = svgAndDict.svg;
            result.graphDict = svgAndDict.graphDict;
            
            console.log(`✅ Q8 Graph generated with a=${A_FLOAT_FOR_AFFINE_LINE}, b=${B_FLOAT_FOR_AFFINE_LINE}`);
        }
        
        // Handle Question 10 - Parabola variations
        else if (generator === 'spe_sujet1_auto_10_question.py') {
            // Example: if the generator provides a shift magnitude
            const A_SHIFT_MAGNITUDE = result.data.components.shift || 5;
            
            // Choose which parabola variant to use based on some logic
            const graphId = 'parabola_s1_am'; // or other variants
            
            const svgAndDict = await buildPCAGraph(graphId, {
                A_SHIFT_MAGNITUDE: A_SHIFT_MAGNITUDE
            });
            
            result.graphSvg = svgAndDict.svg;
            result.graphDict = svgAndDict.graphDict;
            
            console.log(`✅ Q10 Graph generated with shift=${A_SHIFT_MAGNITUDE}`);
        }
        
        // Handle Question 11 - Cubic function cases
        else if (generator === 'spe_sujet1_auto_11_question.py') {
            // Choose case based on generator result
            const caseType = result.data.components.case || 'a';
            const graphId = `q11_case_${caseType}_small`;
            
            // Q11 graphs don't take configuration parameters
            const svgAndDict = await buildPCAGraph(graphId);
            
            result.graphSvg = svgAndDict.svg;
            result.graphDict = svgAndDict.graphDict;
            
            console.log(`✅ Q11 Graph generated for case ${caseType}`);
        }
        
        questionResults.push(result);
    }
    
    // ... rest of your code ...
}

/**
 * Alternative: Render directly to a container in the DOM
 */
async function renderGraphExample() {
    import { renderGraphToContainer } from './index-graphs.js';
    
    // Render a graph with dynamic values directly to a container
    await renderGraphToContainer('graph-container-1', 'q7_small', {
        Y_LABEL_FOR_HORIZONTAL_LINE: 15
    });
    
    await renderGraphToContainer('graph-container-2', 'q8_small', {
        A_FLOAT_FOR_AFFINE_LINE: 1.5,
        B_FLOAT_FOR_AFFINE_LINE: -3
    });
}

/**
 * Important Notes:
 * 
 * 1. Import the buildPCAGraph function from index-graphs.js:
 *    import { buildPCAGraph } from './index-graphs.js';
 * 
 * 2. The configuration keys must match exactly:
 *    - Y_LABEL_FOR_HORIZONTAL_LINE (for q7)
 *    - A_FLOAT_FOR_AFFINE_LINE, B_FLOAT_FOR_AFFINE_LINE (for q8)
 *    - A_SHIFT_MAGNITUDE (for parabola variants)
 * 
 * 3. The graph IDs available are:
 *    - q7_small (parabola with horizontal line)
 *    - q8_small (affine function)
 *    - q11_case_a_small, q11_case_b_small, q11_case_c_small (cubic functions)
 *    - parabola_s1_a0, parabola_s1_am, parabola_s1_ap (upward parabolas)
 *    - parabola_sm1_a0, parabola_sm1_am, parabola_sm1_ap (downward parabolas)
 * 
 * 4. The buildPCAGraph function returns:
 *    {
 *      svg: string,      // The SVG markup
 *      graphDict: Object // The graph dictionary with all metadata
 *    }
 * 
 * 5. Make sure PCAGraphLoader.js and index-graphs.js are in the same directory
 *    as your generator files.
 */

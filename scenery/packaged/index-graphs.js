/**
 * Graph Module for Sujets0
 * Handles PCA graph generation with dynamic configuration
 */

import { PCAGraphLoader } from './PCAGraphLoader.js';

// Single instance of the loader
let graphLoader = null;

/**
 * Initialize the graph loader if not already initialized
 */
async function ensureLoaderInitialized() {
    if (!graphLoader) {
        graphLoader = new PCAGraphLoader({
            debug: false,
            baseUrl: 'auto'
        });
        await graphLoader.initialize();
    }
    return graphLoader;
}

/**
 * Build a PCA graph with dynamic configuration
 * @param {string} graphId - The graph identifier (e.g., 'q7_small', 'q8_small')
 * @param {Object} config - Configuration parameters for the graph
 * @returns {Promise<{svg: string, graphDict: Object}>} Object with SVG and graph dictionary
 */
export async function buildPCAGraph(graphId, config = {}) {
    try {
        // Ensure loader is initialized
        await ensureLoaderInitialized();
        
        // Map the config keys to what PCAGraphLoader expects
        const loaderConfig = {};
        
        // Map specific config keys if provided
        if ('Y_LABEL_FOR_HORIZONTAL_LINE' in config) {
            loaderConfig.Y_LABEL_FOR_HORIZONTAL_LINE = config.Y_LABEL_FOR_HORIZONTAL_LINE;
        }
        if ('A_FLOAT_FOR_AFFINE_LINE' in config) {
            loaderConfig.A_FLOAT_FOR_AFFINE_LINE = config.A_FLOAT_FOR_AFFINE_LINE;
        }
        if ('B_FLOAT_FOR_AFFINE_LINE' in config) {
            loaderConfig.B_FLOAT_FOR_AFFINE_LINE = config.B_FLOAT_FOR_AFFINE_LINE;
        }
        if ('A_SHIFT_MAGNITUDE' in config) {
            loaderConfig.A_SHIFT_MAGNITUDE = config.A_SHIFT_MAGNITUDE;
        }
        
        console.log(`📊 Building graph ${graphId} with config:`, loaderConfig);
        
        // Render the graph with the configuration
        const result = await graphLoader.renderGraph(graphId, loaderConfig);
        
        return result; // Returns {svg: string, graphDict: Object}
    } catch (error) {
        console.error(`Failed to build graph ${graphId}:`, error);
        throw error;
    }
}

/**
 * Render a graph into a DOM container
 * @param {string} containerId - The ID of the container element
 * @param {string} graphId - The graph identifier
 * @param {Object} config - Configuration parameters for the graph
 * @returns {Promise<void>}
 */
export async function renderGraphToContainer(containerId, graphId, config = {}) {
    try {
        const container = document.getElementById(containerId);
        if (!container) {
            throw new Error(`Container with ID '${containerId}' not found`);
        }
        
        // Show loading state
        container.innerHTML = '<div class="loading">Loading graph...</div>';
        
        // Build the graph
        const result = await buildPCAGraph(graphId, config);
        
        // Render the SVG
        container.innerHTML = result.svg;
        
        // Store the graph dictionary as data attribute if needed
        container.dataset.graphDict = JSON.stringify(result.graphDict);
        
        // Render any LaTeX in the graph
        if (typeof katex !== 'undefined') {
            renderLatexInGraph(container);
        }
        
    } catch (error) {
        console.error(`Failed to render graph to container ${containerId}:`, error);
        const container = document.getElementById(containerId);
        if (container) {
            container.innerHTML = `<div class="error">Failed to load graph: ${error.message}</div>`;
        }
    }
}

/**
 * Render LaTeX expressions in a graph container
 * @param {HTMLElement} container - The container element
 */
function renderLatexInGraph(container) {
    const foreignObjects = container.querySelectorAll('foreignObject');
    foreignObjects.forEach((fo) => {
        const divs = fo.querySelectorAll('div.svg-latex');
        divs.forEach((div) => {
            const latex = div.textContent.trim();
            if (latex) {
                try {
                    const bgColor = div.style.backgroundColor;
                    const color = div.style.color;
                    div.innerHTML = '';
                    katex.render(latex, div, {
                        throwOnError: false,
                        displayMode: false,
                    });
                    if (bgColor) div.style.backgroundColor = bgColor;
                    if (color) {
                        div.querySelectorAll('.katex, .katex *').forEach(el => {
                            el.style.color = color;
                        });
                    }
                } catch (e) {
                    console.error('KaTeX error:', e);
                    div.textContent = latex;
                }
            }
        });
    });
}

/**
 * Get the current graph loader instance
 * @returns {PCAGraphLoader|null}
 */
export function getGraphLoader() {
    return graphLoader;
}

/**
 * Reset the graph loader (forces reinitialization on next use)
 */
export function resetGraphLoader() {
    graphLoader = null;
}

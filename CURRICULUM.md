




# How to read this file


Non commented files in the below `GRAPH_FILES` enumerations are used in sujets0 apps, i.e. in : 
- generation engines for teachers 
- apps for students 
- referenced for cosonlindation with official curriculum


> We use js and not json for ensuring nice printing of comments. Also they are literally used in `js` files in the `/scenery` folder.

Commented files are never used in the above listed cased, they are just "visible construction features" ie *traits de constructions*.



# FRANCE


## Première 


### Sujets 0 

#### Spé - Sujet 1




```js
const GRAPH_FILES = {
  // Question 7
  //"q7_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_07_question_canonical.py",
  "q7_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_07_question_small.py",
  
  // Question 8  
  //"q8_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_08_question_canonical.py",
  "q8_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_08_question_small.py",
  


  // Question 11 - Case A 
  "q11_case_a_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_a_question_canonical.py",
  "q11_case_a_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_a_question_small.py",
  
  // Question 11 - Case B 
  "q11_case_b_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_b_question_canonical.py",
  "q11_case_b_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_b_question_small.py",

  // Question 11 - Case C 
  "q11_case_c_canonical": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_c_question_canonical.py",
  "q11_case_c_small": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_11_case_c_question_small.py",

  
  // Dispatch module (needed by parabola graphs)
  "dispatch": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_dispatch.py",
  
  // Parabola graphs with s=1
  "parabola_s1_a0": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_0.py",
  "parabola_s1_am5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_m.py",
  "parabola_s1_ap5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_s1_a_p.py",
  
  // Parabola graphs with s=-1
  "parabola_sm1_a0": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_0.py",
  "parabola_sm1_am5": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_m.py",
  "parabola_sm1_ap10": "src/pca_graph_viz/tests/graphs/spe_sujet1_auto_10_question_small_parabola_a_sm1_a_p.py",


}
```
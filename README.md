# Assignment 1 - Cracking PUFs
## Objective
* To train a linear model that predicts outcomes of a **COCO-PUF** (Cross Connection PUF).
* Given a dataset containing **40000** rows of **34** spaced integers with first **32** being the challenges & the last **2** being the responses (Response0 and Response 1) to train the model.

## Approach
* Developed a ML algorithm that gave us the mapping function to map Challenges into a feature vector
* Obtained a model to predict time taken by upper and lower signals to reach the end
* Then derived a final model using previously developed algorithms

## Impact
* While evaluating the model gave the following results


Criteria | Result
--- | ---
Dimensionality | 64
Train time | 1.653s
Map time | 0.278s
Error rate for Response0 | 0.07
Error rate for Response1 | 0.003

# Assignment 2 - Decision Tree




Criteria | Result
--- | ---
Training time | 0.082 s
Model size | 211.092 KB
Evaluation time | 1.008 s
Precision | 0.895

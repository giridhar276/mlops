# Hyperparameter Tuning with MLflow

## Use Case
Track multiple parameter combinations.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_03_hyperparameter_tuning_complete_usecase.ipynb
- 02_03_hyperparameter_tuning_practice_exercise.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

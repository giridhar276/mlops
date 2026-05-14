# Data and Model Drift

## Use Case
Compare baseline and current dataset drift.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_15_data_model_drift_complete_usecase.ipynb
- 02_15_data_model_drift_practice_exercise.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

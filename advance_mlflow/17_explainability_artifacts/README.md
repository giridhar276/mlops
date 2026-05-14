# Explainability Artifacts

## Use Case
Log confusion matrix and feature importance.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_17_explainability_artifacts_complete_usecase.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

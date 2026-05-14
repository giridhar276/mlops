# Sklearn Pipeline Best Practices

## Use Case
Log preprocessing and model together.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_19_sklearn_pipeline_best_practices_complete_usecase.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

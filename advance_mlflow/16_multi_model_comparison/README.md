# Multi-Model Comparison

## Use Case
Compare multiple algorithms.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_16_multi_model_comparison_complete_usecase.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

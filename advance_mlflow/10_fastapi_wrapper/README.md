# FastAPI Wrapper Around MLflow Model

## Use Case
Generate FastAPI wrapper using same-run model URI.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_10_fastapi_wrapper_complete_usecase.ipynb
- 02_10_fastapi_wrapper_practice_exercise.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

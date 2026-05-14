# Batch Inference Pipeline

## Use Case
Batch scoring using MLflow model.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_08_batch_inference_pipeline_complete_usecase.ipynb
- 02_08_batch_inference_pipeline_practice_exercise.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

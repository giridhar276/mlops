# Model Governance and Audit Trail

## Use Case
Owner, approval, risk metadata.

## Correction
Signature and registry are now part of the same run that logs the model. There is no separate final integration run.

## Contents
- datasets/
- mlruns/
- artifacts/
- outputs/
- architecture_diagram.png
- visual_steps.png
- 01_18_model_governance_audit_complete_usecase.ipynb

## Run
```bash
jupyter lab
```

## MLflow UI
```bash
mlflow ui --backend-store-uri ./mlruns
```

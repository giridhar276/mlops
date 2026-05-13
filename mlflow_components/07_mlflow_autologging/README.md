# MLflow Autologging

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_sklearn_autologging_basic.ipynb`: Sklearn autologging basic
- `02_autologging_with_manual_metrics.ipynb`: Autologging with manual metrics
- `03_autologging_multiple_models.ipynb`: Autologging multiple models
- `04_autologging_regression.ipynb`: Autologging regression
- `05_autologging_artifacts_and_plots.ipynb`: Autologging artifacts and plots
- `06_end_to_end_autologging_workflow.ipynb`: End-to-end autologging workflow

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
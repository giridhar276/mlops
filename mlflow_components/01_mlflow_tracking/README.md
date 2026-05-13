# MLflow Tracking

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_basic_experiment_tracking.ipynb`: Basic experiment tracking
- `02_multiple_runs_comparison.ipynb`: Multiple runs comparison
- `03_artifacts_and_plots.ipynb`: Artifacts and plots
- `04_classification_metrics_tracking.ipynb`: Classification metrics tracking
- `05_regression_metrics_tracking.ipynb`: Regression metrics tracking
- `06_end_to_end_churn_style_tracking.ipynb`: End-to-end churn tracking

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
# MLflow UI

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_generate_runs_for_ui.ipynb`: Generate runs for UI
- `02_compare_models_in_ui.ipynb`: Compare models in UI
- `03_log_visual_artifacts_for_ui.ipynb`: Log visual artifacts for UI
- `04_search_runs_programmatically.ipynb`: Search runs programmatically
- `05_experiment_dashboard_dataset.ipynb`: Experiment dashboard dataset
- `06_end_to_end_ui_demo.ipynb`: End-to-end UI demo

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
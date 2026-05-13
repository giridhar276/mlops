# MLflow Projects

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_project_structure_demo.ipynb`: Project structure demo
- `02_parameterized_training_script.ipynb`: Parameterized training script
- `03_reproducible_environment_demo.ipynb`: Reproducible environment demo
- `04_project_entry_points_demo.ipynb`: Project entry points demo
- `05_project_with_metrics_and_artifacts.ipynb`: Project with metrics and artifacts
- `06_end_to_end_project_template.ipynb`: End-to-end project template

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```

## Important MLflow Project Run Command

Use this command from inside `02_mlflow_projects`:

```bash
mlflow run sample_realtime_mlflow_project --experiment-name Project_Realtime_Workflow --experiment-name Project_Realtime_Workflow
```

Why this is used:
- It avoids local file-store issues where MLflow tries to use missing experiment ID `0`.
- It explicitly tells MLflow which experiment name to use.
- The generated `train.py` also clears inherited `MLFLOW_EXPERIMENT_ID` and `MLFLOW_RUN_ID` environment variables before creating the run.

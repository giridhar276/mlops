# Day2 Mlflow Basics

Run notebooks in order.

## Notebooks

- `01_mlflow_installation_and_ui_start.ipynb`
- `02_create_experiment_and_first_run.ipynb`
- `03_manual_logistic_regression_tracking.ipynb`
- `04_manual_random_forest_tracking.ipynb`
- `05_elasticnet_regression_tracking.ipynb`
- `06_log_confusion_matrix_artifact.ipynb`
- `07_log_dataset_profile_artifact.ipynb`
- `08_search_runs_and_compare_results.ipynb`
- `09_load_logged_model_for_prediction.ipynb`
- `10_day2_hands_on_summary_exercise.ipynb`


## How to run

1. Open terminal from project root: `mlflow_for_ml_dev_final`
2. Install dependencies: `pip install -r requirements.txt`
3. Start Jupyter: `jupyter notebook`
4. Open this folder under: `mlflow_for_ml_dev/notebooks/`
5. Run notebooks one by one.

## Start MLflow UI

For Day 2 and Day 3:

```bash
mlflow ui --backend-store-uri ./mlflow_for_ml_dev/mlruns --port 5000
```

For Day 4 model registry examples:

```bash
mlflow ui --backend-store-uri sqlite:///mlflow_for_ml_dev/mlflow.db --default-artifact-root ./mlflow_for_ml_dev/mlruns --port 5000
```

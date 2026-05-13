# MLflow Serving

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_prepare_model_for_serving.ipynb`: Prepare model for serving
- `02_serving_command_explained.ipynb`: Serving command explained
- `03_predict_payload_format.ipynb`: Predict payload format
- `04_local_batch_scoring_alternative.ipynb`: Local batch scoring alternative
- `05_api_client_template.ipynb`: API client template
- `06_end_to_end_serving_workflow.ipynb`: End-to-end serving workflow

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
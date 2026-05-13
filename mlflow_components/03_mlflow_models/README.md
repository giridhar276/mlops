# MLflow Models

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_log_and_load_sklearn_model.ipynb`: Log and load sklearn model
- `02_model_signature_and_input_example.ipynb`: Model signature and input example
- `03_pyfunc_prediction_demo.ipynb`: Pyfunc prediction demo
- `04_model_flavors_explained.ipynb`: Model flavors explained
- `05_custom_pyfunc_model.ipynb`: Custom pyfunc model
- `06_end_to_end_model_packaging.ipynb`: End-to-end model packaging

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
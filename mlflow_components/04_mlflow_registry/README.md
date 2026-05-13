# MLflow Registry

This folder contains 6 cell-wise notebooks, a datasets folder, and diagrams.

## Dataset
`datasets/customer_churn_500.csv` contains 500 records with categorical and numerical columns.

## Notebooks
- `01_register_model_basic.ipynb`: Register model basic
- `02_model_versions_demo.ipynb`: Model versions demo
- `03_aliases_and_stages_demo.ipynb`: Aliases and stages demo
- `04_model_descriptions_and_tags.ipynb`: Model descriptions and tags
- `05_load_registered_model.ipynb`: Load registered model
- `06_end_to_end_registry_lifecycle.ipynb`: End-to-end registry lifecycle

## Run
```bash
jupyter lab
```

After running notebooks:
```bash
mlflow ui --backend-store-uri ./mlruns
```
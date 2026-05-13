# MLflow Training Pack - Cell-wise Notebooks with Realtime Datasets

This regenerated version fixes the previous issue: code is no longer written in one single cell.

Each notebook now contains:
- Markdown explanation before each step
- Separate code cells
- Line-by-line comments
- Dataset loading from `datasets/customer_churn_500.csv`
- MLflow logging examples
- Trainer discussion note

## Setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Start Jupyter:
```bash
jupyter lab
```

## MLflow UI

Run this command from the same topic folder where notebooks were executed:

```bash
mlflow ui --backend-store-uri ./mlruns
```

Open:
```text
http://127.0.0.1:5000
```


## Special Note for `02_mlflow_projects`

When running the MLflow Project example, use:

```bash
cd 02_mlflow_projects
mlflow run sample_realtime_mlflow_project --experiment-name Project_Realtime_Workflow
```

The generated project script clears inherited MLflow environment variables to avoid:

```text
MlflowException: Could not find experiment with ID 0
```

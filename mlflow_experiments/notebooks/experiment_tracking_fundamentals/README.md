# Experiment Tracking Fundamentals - Independent Notebooks

This package contains independent MLflow notebooks. There is no `src` folder and no helper-module dependency.

## Install

```bash
pip install -r requirements.txt
```

## Important: use the same MLflow tracking folder

All notebooks now log runs to one common folder:

```text
~/mlflow_training_runs
```

So the MLflow UI must be started with the same backend-store-uri.

### macOS / Linux

```bash
mlflow ui --backend-store-uri file:$HOME/mlflow_training_runs --port 5000
```

### Windows PowerShell

```powershell
mlflow ui --backend-store-uri "file:$env:USERPROFILE/mlflow_training_runs" --port 5000
```

Then open:

```text
http://127.0.0.1:5000
```

## How to verify from notebook

Each notebook prints something like:

```text
Tracking URI used by this notebook: file:/Users/yourname/mlflow_training_runs
Run this command in terminal to see the same runs:
mlflow ui --backend-store-uri file:/Users/yourname/mlflow_training_runs --port 5000
```

Copy that exact command and run it in terminal.

## If runs are still not visible

1. Clear the filter/search box in the Runs page.
2. Click the correct experiment name on the left side, not only `Default`.
3. Refresh the browser.
4. Make sure at least one notebook cell with `mlflow.start_run()` was executed.
5. Confirm the terminal command uses the same folder printed in the notebook.

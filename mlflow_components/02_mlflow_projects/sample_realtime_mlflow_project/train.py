
import os
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Remove MLflow project-level experiment ID if it was automatically passed.
# This avoids "Could not find experiment with ID 0" error in local file tracking.
os.environ.pop("MLFLOW_EXPERIMENT_ID", None)

# Remove project-level run ID if any previous run context is passed.
os.environ.pop("MLFLOW_RUN_ID", None)

os.makedirs("mlruns", exist_ok=True)
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("02_mlflow_projects_01_project_structure_demo")

df = pd.read_csv("datasets/customer_churn_500.csv")
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]

categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()
numerical_columns = X.select_dtypes(exclude=["object"]).columns.tolist()

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_columns),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(n_estimators=150, max_depth=6, random_state=42)),
])

with mlflow.start_run(run_name="project_training_run"):
    mlflow.log_param("dataset", "datasets/customer_churn_500.csv")
    mlflow.log_param("model_family", "RandomForestClassifier")
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    mlflow.log_metric("accuracy", accuracy_score(y_test, predictions))
    mlflow.log_metric("precision", precision_score(y_test, predictions, zero_division=0))
    mlflow.log_metric("recall", recall_score(y_test, predictions, zero_division=0))
    mlflow.log_metric("f1_score", f1_score(y_test, predictions, zero_division=0))
    mlflow.sklearn.log_model(pipeline, "model")

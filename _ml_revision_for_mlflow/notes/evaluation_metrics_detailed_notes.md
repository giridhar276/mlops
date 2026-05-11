# Detailed Evaluation Metrics Notes for MLflow Training

## 1. Why evaluation metrics are required

### Layman style
Imagine four students wrote an exam. If you only say “all students passed”, that is not enough. You may still want to know:

- Who scored the highest?
- Who made fewer mistakes?
- Who performed well in practical questions?
- Who needs improvement?

Machine learning models are similar. A model may give predictions, but we need marks or scores to understand how good or bad the model is.

Evaluation metrics are the marks given to a machine learning model.

### Simple technical meaning
Evaluation metrics are numerical measurements used to compare model predictions with actual values.

They help us answer:

- Is the model performing well?
- Which model is better?
- Is the model making dangerous mistakes?
- Is the model suitable for business use?
- Should we improve data, features, or algorithm?

### Real-time example
Suppose we are building a customer churn model for a telecom company.

The model predicts whether a customer will leave the company.

If the model is good, the company can give offers to risky customers and retain them. If the model is poor, the company may waste offers on customers who were never going to leave, or miss customers who were actually going to leave.

So model evaluation is directly connected to business cost and business value.

---

# 2. Classification Metrics

Classification means predicting a category or class.

Examples:

- Customer will churn or not churn
- Email is spam or not spam
- Transaction is fraud or not fraud
- Patient has disease or no disease
- Ticket is high priority or low priority

For binary classification, we usually have two classes:

- Positive class: event of interest
- Negative class: normal/non-event class

Example: In churn prediction, `churn = 1` can be positive and `churn = 0` can be negative.

---

## 2.1 Confusion Matrix

### Layman style
A confusion matrix is like a report card of correct and wrong predictions.

It tells us four things:

1. How many positive cases were correctly identified?
2. How many negative cases were correctly identified?
3. How many negative cases were wrongly called positive?
4. How many positive cases were wrongly missed?

### Simple technical meaning
A confusion matrix compares actual class values with predicted class values.

For binary classification:

| Actual / Predicted | Predicted No | Predicted Yes |
|---|---:|---:|
| Actual No | True Negative | False Positive |
| Actual Yes | False Negative | True Positive |

### Terms

#### True Positive, TP
The actual value is positive and the model also predicted positive.

Example: Customer actually churned and model predicted churn.

#### True Negative, TN
The actual value is negative and the model also predicted negative.

Example: Customer did not churn and model predicted no churn.

#### False Positive, FP
The actual value is negative but model predicted positive.

Example: Customer did not churn but model predicted churn.

#### False Negative, FN
The actual value is positive but model predicted negative.

Example: Customer churned but model predicted no churn.

### Real-time example: fraud detection

- TP: Fraud transaction correctly detected as fraud
- TN: Normal transaction correctly detected as normal
- FP: Normal transaction wrongly blocked as fraud
- FN: Fraud transaction wrongly allowed as normal

In fraud detection, FN can be very costly because actual fraud is missed.

### Python example

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
```

### MLflow connection
The confusion matrix is usually saved as an artifact, often as an image or CSV file.

---

## 2.2 Accuracy

### Layman style
Accuracy means: Out of all predictions, how many were correct?

If the model made 100 predictions and 90 were correct, accuracy is 90%.

### Simple technical meaning
Accuracy is the ratio of correct predictions to total predictions.

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

### Real-time example
Suppose a model predicts whether 100 customers will churn.

- 85 predictions are correct
- 15 predictions are wrong

Accuracy = 85 / 100 = 85%

### When accuracy is useful
Accuracy is useful when classes are balanced.

Example:

- 50% churn
- 50% no churn

### When accuracy is misleading
Accuracy can be dangerous when data is imbalanced.

Example:

Suppose only 2 out of 100 transactions are fraud.

A model predicts “not fraud” for all 100 transactions.

It will get 98% accuracy, but it detected zero fraud cases.

So high accuracy does not always mean a useful model.

### Python example

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
```

### MLflow connection
Accuracy is logged as a metric.

```python
mlflow.log_metric("accuracy", accuracy)
```

---

## 2.3 Precision

### Layman style
Precision answers this question:

“When the model says Yes, how often is it actually correct?”

### Simple technical meaning
Precision measures correctness among positive predictions.

```text
Precision = TP / (TP + FP)
```

### Real-time example: email spam detection

If the model says 100 emails are spam, and 90 are truly spam:

Precision = 90 / 100 = 90%

### Why precision matters
Precision is important when false positives are costly.

Example: Spam detection

If a normal business email is wrongly marked as spam, the user may miss an important message.

Example: Loan approval risk

If a safe customer is wrongly predicted as risky, the bank may lose a good customer.

### Business interpretation
High precision means fewer false alarms.

### Python example

```python
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)
print(precision)
```

### MLflow connection
Precision is logged as a metric.

```python
mlflow.log_metric("precision", precision)
```

---

## 2.4 Recall / Sensitivity

### Layman style
Recall answers this question:

“Out of all actual Yes cases, how many did the model catch?”

### Simple technical meaning
Recall measures how many actual positive cases were correctly identified.

```text
Recall = TP / (TP + FN)
```

### Real-time example: disease detection

Suppose 100 patients actually have a disease.

The model detects 95 of them.

Recall = 95 / 100 = 95%

### Why recall matters
Recall is important when false negatives are costly.

Example: Medical diagnosis

Missing a real disease case can be dangerous.

Example: Fraud detection

Missing a fraud transaction can cause financial loss.

Example: Customer churn

Missing a customer who is likely to leave means the company loses the opportunity to retain that customer.

### Business interpretation
High recall means fewer missed positive cases.

### Python example

```python
from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)
print(recall)
```

### MLflow connection
Recall is logged as a metric.

```python
mlflow.log_metric("recall", recall)
```

---

## 2.5 F1-score

### Layman style
F1-score is a balanced score between precision and recall.

It is useful when we want both:

- Fewer false alarms
- Fewer missed cases

### Simple technical meaning
F1-score is the harmonic mean of precision and recall.

```text
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

### Real-time example: customer churn

In churn prediction:

- Precision matters because we do not want to give discounts to too many safe customers.
- Recall matters because we do not want to miss customers who may actually leave.

F1-score balances both.

### When F1-score is useful
F1-score is useful when:

- Dataset is imbalanced
- Both FP and FN matter
- You need one combined classification score

### Python example

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
print(f1)
```

### MLflow connection
F1-score is one of the most useful metrics to log for classification models.

```python
mlflow.log_metric("f1_score", f1)
```

---

## 2.6 Specificity

### Layman style
Specificity tells us how well the model identifies negative cases.

It answers:

“Out of all actual No cases, how many did the model correctly identify as No?”

### Simple technical meaning
Specificity is the true negative rate.

```text
Specificity = TN / (TN + FP)
```

### Real-time example: medical testing

If a person does not have a disease, a good test should say “no disease”.

Specificity measures how well the model avoids wrongly alarming healthy people.

### When specificity matters
Specificity matters when false positives are costly.

Example:

- Wrongly marking a healthy patient as sick
- Wrongly blocking a legitimate transaction
- Wrongly rejecting a good loan applicant

---

## 2.7 ROC-AUC

### Layman style
ROC-AUC tells us how well the model separates positive cases from negative cases.

A higher ROC-AUC means the model is better at ranking positive cases above negative cases.

### Simple technical meaning
ROC-AUC is the area under the ROC curve.

The ROC curve compares:

- True Positive Rate / Recall
- False Positive Rate

across different classification thresholds.

### Real-time example
Suppose a churn model gives probabilities:

- Customer A: 0.90 churn probability
- Customer B: 0.20 churn probability

A good model should generally assign higher probabilities to customers who actually churn.

ROC-AUC measures this ranking quality.

### Interpretation

| ROC-AUC | Meaning |
|---:|---|
| 0.50 | Random guessing |
| 0.60 - 0.70 | Weak model |
| 0.70 - 0.80 | Acceptable model |
| 0.80 - 0.90 | Good model |
| 0.90+ | Very strong model |

### Python example

```python
from sklearn.metrics import roc_auc_score

y_proba = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_proba)
print(roc_auc)
```

### MLflow connection
ROC-AUC is logged as a metric.

```python
mlflow.log_metric("roc_auc", roc_auc)
```

---

## 2.8 Precision-Recall AUC

### Layman style
Precision-Recall AUC tells us how well the model performs when positive cases are rare.

### Simple technical meaning
It calculates the area under the Precision-Recall curve.

This curve compares:

- Precision
- Recall

at different thresholds.

### Real-time example
Fraud detection usually has very few fraud cases.

In such imbalanced cases, Precision-Recall AUC can be more useful than ROC-AUC.

### When to use
Use Precision-Recall AUC when:

- Positive class is rare
- Fraud detection
- Disease detection
- Failure prediction
- Security alert detection

---

## 2.9 Log Loss

### Layman style
Log loss checks how confident and correct the model probabilities are.

If a model is confidently wrong, log loss punishes it heavily.

### Simple technical meaning
Log loss measures the error between actual labels and predicted probabilities.

Lower log loss is better.

### Real-time example
Suppose actual churn is 1.

Model A predicts churn probability = 0.90

Model B predicts churn probability = 0.51

Both may classify as churn if threshold is 0.5, but Model A is more confident and better.

Log loss captures this difference.

### MLflow connection
Log loss is useful when tracking probability-based classifiers.

---

# 3. Regression Metrics

Regression means predicting a continuous numerical value.

Examples:

- House price prediction
- Sales forecasting
- Salary prediction
- Delivery time prediction
- Electricity demand prediction

---

## 3.1 Error / Residual

### Layman style
Error means the difference between actual value and predicted value.

Example:

- Actual house price: ₹80,00,000
- Predicted house price: ₹75,00,000
- Error: ₹5,00,000

### Simple technical meaning

```text
Error = Actual Value - Predicted Value
```

Errors are the foundation of most regression metrics.

---

## 3.2 MAE - Mean Absolute Error

### Layman style
MAE tells us the average mistake made by the model.

If MAE is ₹4,00,000 in house price prediction, the model is wrong by around ₹4,00,000 on average.

### Simple technical meaning
MAE is the average of absolute errors.

```text
MAE = Average of |Actual - Predicted|
```

### Real-time example: house price prediction

If MAE = ₹5,00,000, then on average the prediction differs from the real price by ₹5,00,000.

### Advantages

- Easy to explain to business users
- Same unit as target variable
- Less sensitive to extreme outliers than RMSE

### Disadvantages

- Does not strongly punish very large errors

### Python example

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print(mae)
```

### MLflow connection

```python
mlflow.log_metric("mae", mae)
```

---

## 3.3 MSE - Mean Squared Error

### Layman style
MSE squares each error before averaging.

Large mistakes become much bigger after squaring.

### Simple technical meaning
MSE is the average of squared errors.

```text
MSE = Average of (Actual - Predicted)^2
```

### Real-time example
If one house price prediction is wrong by ₹20,00,000, MSE will punish that error heavily.

### Advantages

- Penalizes large errors strongly
- Useful for mathematical optimization

### Disadvantages

- Unit is squared, so it is harder to explain to business users

### Python example

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print(mse)
```

### MLflow connection

```python
mlflow.log_metric("mse", mse)
```

---

## 3.4 RMSE - Root Mean Squared Error

### Layman style
RMSE is similar to MAE, but it gives more punishment to large mistakes.

It is also in the same unit as the target.

### Simple technical meaning
RMSE is the square root of MSE.

```text
RMSE = sqrt(MSE)
```

### Real-time example: delivery time prediction

If RMSE is 12 minutes, the model has a typical prediction error of around 12 minutes, with larger errors punished more strongly.

### Advantages

- Same unit as target variable
- Penalizes large errors
- Commonly used in regression projects

### Disadvantages

- Sensitive to outliers

### Python example

```python
import numpy as np
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(rmse)
```

### MLflow connection

```python
mlflow.log_metric("rmse", rmse)
```

---

## 3.5 R² Score

### Layman style
R² tells us how much of the variation in the target variable is explained by the model.

If R² = 0.80, the model explains around 80% of the variation in the data.

### Simple technical meaning
R² compares model performance with a very simple baseline model that always predicts the average target value.

### Interpretation

| R² Value | Meaning |
|---:|---|
| 1.0 | Perfect prediction |
| 0.8 | Strong model |
| 0.5 | Moderate model |
| 0.0 | No better than predicting average |
| Negative | Worse than predicting average |

### Real-time example: sales prediction

If R² = 0.75, the model explains 75% of sales variation using the available features.

### Advantages

- Easy high-level model quality indicator
- Useful for comparing regression models on the same dataset

### Disadvantages

- Can be misleading if used alone
- Does not tell average error amount in business units

### Python example

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(r2)
```

### MLflow connection

```python
mlflow.log_metric("r2_score", r2)
```

---

## 3.6 Adjusted R²

### Layman style
Adjusted R² is a stricter version of R².

It checks whether adding more features is actually useful.

### Simple technical meaning
Adjusted R² adjusts R² based on the number of predictors in the model.

### Why it is needed
R² can increase when we add more features, even if those features are not useful.

Adjusted R² penalizes unnecessary features.

### Real-time example
Suppose we are predicting house prices.

Adding `area_sqft` may genuinely improve the model.

Adding random columns like `property_id_last_digit` may increase R² slightly by chance.

Adjusted R² helps detect such unnecessary features.

---

## 3.7 MAPE - Mean Absolute Percentage Error

### Layman style
MAPE tells average error in percentage form.

If MAPE is 10%, the model is wrong by around 10% on average.

### Simple technical meaning
MAPE is the average of absolute percentage errors.

```text
MAPE = Average of |Actual - Predicted| / Actual * 100
```

### Real-time example: sales forecasting

If actual sales are 10,000 units and predicted sales are 9,000 units:

Percentage error = 10%

### Advantages

- Easy to explain to business users
- Useful for forecasting

### Disadvantages

- Problematic when actual values are zero or close to zero

---

# 4. Choosing the Right Metric

## 4.1 Classification metric selection

| Use Case | Recommended Metric | Reason |
|---|---|---|
| Balanced classification | Accuracy | Classes are evenly distributed |
| Fraud detection | Recall, Precision-Recall AUC | Fraud cases are rare and missing fraud is costly |
| Spam detection | Precision | Avoid marking important emails as spam |
| Medical diagnosis | Recall | Avoid missing actual disease cases |
| Customer churn | F1-score, Recall | Balance retention cost and missed churners |
| Credit risk | Precision, Recall, F1 | Both false approvals and false rejections matter |

## 4.2 Regression metric selection

| Use Case | Recommended Metric | Reason |
|---|---|---|
| House price prediction | MAE, RMSE, R² | Error should be business readable and model comparable |
| Sales forecasting | MAE, RMSE, MAPE | Business wants error in units and percentage |
| Delivery time prediction | MAE, RMSE | Minutes of error are easy to understand |
| Demand forecasting | RMSE, MAPE | Large errors and percentage error matter |

---

# 5. Metrics and MLflow Mapping

| Concept | Example | MLflow Action |
|---|---|---|
| Accuracy | 0.86 | `mlflow.log_metric("accuracy", 0.86)` |
| Precision | 0.82 | `mlflow.log_metric("precision", 0.82)` |
| Recall | 0.78 | `mlflow.log_metric("recall", 0.78)` |
| F1-score | 0.80 | `mlflow.log_metric("f1_score", 0.80)` |
| RMSE | 12500 | `mlflow.log_metric("rmse", 12500)` |
| R² | 0.74 | `mlflow.log_metric("r2_score", 0.74)` |
| Confusion matrix | PNG/CSV | `mlflow.log_artifact("confusion_matrix.png")` |
| Classification report | TXT/JSON | `mlflow.log_artifact("classification_report.txt")` |

---

# 6. Trainer Script: How to Explain Metrics in Class

## Start with this question

“Suppose I trained 5 models. How do I know which one is best?”

Then explain:

“Model evaluation metrics are the scoring system for machine learning models. Without metrics, we cannot compare experiments.”

## Explain classification using confusion matrix first

Do not start with formulas. Start with TP, TN, FP, FN using a real example like churn or fraud.

## Then explain formulas

Once students understand the mistake types, formulas become easy.

## Then connect to business cost

Example:

- False positive in spam detection: important email goes to spam
- False negative in fraud detection: fraud transaction is missed
- False negative in churn: risky customer is not contacted

## Then connect to MLflow

Say:

“Every time we train a model, we should log these metrics. MLflow helps us compare runs without manually maintaining Excel files.”

---

# 7. Common Interview-Style Questions

## Question 1: Is accuracy always the best metric?

No. Accuracy is not always best, especially for imbalanced datasets. For fraud detection, a model can get high accuracy by predicting all transactions as non-fraud, but it will be useless because it misses fraud cases.

## Question 2: Difference between precision and recall?

Precision focuses on correctness of positive predictions. Recall focuses on catching actual positive cases.

## Question 3: When should we use F1-score?

Use F1-score when both precision and recall are important and the dataset is imbalanced.

## Question 4: Difference between MAE and RMSE?

MAE gives average absolute error. RMSE gives more penalty to large errors because it squares errors before averaging.

## Question 5: Can R² be negative?

Yes. Negative R² means the model is worse than simply predicting the average value.

---

# 8. Practical Activity for Students

Give students this task:

1. Train Logistic Regression, Decision Tree, Random Forest, and XGBoost.
2. Calculate accuracy, precision, recall, F1-score, and ROC-AUC.
3. Create a comparison table.
4. Identify the best model.
5. Explain which metric they selected and why.

Then ask:

“How will you track this if there are 100 experiments?”

This naturally introduces MLflow.
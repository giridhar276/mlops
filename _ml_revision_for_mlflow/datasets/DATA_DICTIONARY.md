# Data Dictionary

## customer_churn_training.csv
Synthetic classification dataset for Day 1 ML revision.

| Column | Type | Meaning |
|---|---|---|
| customer_id | Identifier | Unique customer id; do not use as ML feature |
| age | Numerical | Customer age |
| tenure_months | Numerical | Number of months with the company |
| monthly_charges | Numerical | Monthly bill amount |
| total_usage_gb | Numerical | Monthly usage in GB |
| support_tickets | Numerical | Count of support tickets raised |
| late_payments | Numerical | Count of late payments |
| contract_type | Categorical | Month-to-month, one year, or two year contract |
| payment_method | Categorical | Payment mode |
| city_tier | Categorical | Customer city tier |
| internet_service | Categorical | Service type |
| num_products | Numerical | Number of products used |
| churn | Target | 1 means churned, 0 means retained |

## house_price_training.csv
Synthetic regression dataset for Day 1 ML revision.

| Column | Type | Meaning |
|---|---|---|
| property_id | Identifier | Unique property id; do not use as ML feature |
| area_sqft | Numerical | Property area in square feet |
| bedrooms | Numerical | Number of bedrooms |
| bathrooms | Numerical | Number of bathrooms |
| age_years | Numerical | Property age |
| distance_from_city_center_km | Numerical | Distance from city center |
| floor | Numerical | Floor number |
| parking | Categorical | Parking availability |
| furnishing | Categorical | Furnishing status |
| locality_grade | Categorical | Premium, standard, or budget locality |
| property_type | Categorical | Apartment, villa, or independent house |
| city | Categorical | City |
| price_inr | Target | Property price in INR |
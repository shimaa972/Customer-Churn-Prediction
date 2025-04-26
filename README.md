# Customer-Churn-Prediction
 A Streamlit web app for predicting customer churn using a trained machine learning model. Uploads customer data and provides visualized predictions with downloadable results.
# 📊 Churn Dataset

This repository contains a sample dataset for customer churn analysis. It includes basic customer demographics and tenure details to be used for training and testing churn prediction models.

## 📁 Dataset Columns

- `Age`: Age of the customer (integer)
- `Tenure`: Number of months the customer has been with the company
- `Sex`: Gender of the customer (`Male` / `Female`)
- `Churn`: Whether the customer churned (`Yes` / `No`)

## 🧠 Use Cases

- Train machine learning models for churn prediction
- Practice data preprocessing, encoding, and model evaluation
- Educational or demonstration purposes with Streamlit apps

## 📄 File Included

- `churn_dataset.xlsx`: Excel file containing the dataset

## 🛠️ Example Usage in Python

```python
import pandas as pd

df = pd.read_excel('churn_dataset.xlsx')
df['Sex'] = df['Sex'].map({'Male': 1, 'Female': 0})
df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

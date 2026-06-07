# Customer Churn Prediction

Customer Churn Prediction is a Machine Learning web application that predicts whether a telecom customer is likely to leave the service based on customer demographics, subscription details, billing information, and service usage patterns.

The project uses Logistic Regression for classification and is deployed using Flask with a user-friendly web interface.

## Project Overview

Customer churn is one of the most important business problems in the telecom industry. Retaining existing customers is often more cost-effective than acquiring new ones.

This project analyzes customer information and predicts whether a customer is likely to churn or stay with the company.

## Features

* Customer Churn Prediction
* Logistic Regression Classification Model
* Data Cleaning and Preprocessing
* Feature Encoding
* Interactive Flask Web Application
* Professional User Interface
* Real-Time Prediction Results

## Dataset Information

Dataset: Telco Customer Churn Dataset

Total Records: 7043

Features Used:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

Target Variable:

* Churn (Yes/No)

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Feature Encoding
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Deployment Using Flask

## Model Performance

Algorithm Used:

Logistic Regression

Accuracy:

81.69%

Confusion Matrix:

```text
[[934, 102],
 [156, 217]]
```

Classification Report:

```text
Precision (Churn): 0.68
Recall (Churn): 0.58
F1-Score (Churn): 0.63
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Flask
* HTML
* CSS
* Jupyter Notebook

## Project Structure

```text
Project-04-Customer-Churn-Prediction/

│
├── app.py
├── customer_churn_model.pkl
├── customer_churn_prediction.ipynb
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How To Run

1. Clone the repository

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run Flask Application

```bash
python app.py
```

4. Open browser

```text
http://127.0.0.1:5000
```

## Future Improvements

* Random Forest Classifier
* XGBoost Model
* Probability Score Display
* Feature Importance Visualization
* Cloud Deployment

## Author

Shashank Srivastava

Aspiring AI/ML Engineer

100 Days of Machine Learning Challenge

---


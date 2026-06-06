# Project 03: Titanic Survival Prediction Web Application using Machine Learning and Flask

## Overview

This project is an end-to-end Machine Learning web application that predicts whether a passenger would survive the Titanic disaster based on passenger information such as class, gender, age, fare, family members aboard, and embarkation location.

The project demonstrates the complete Machine Learning workflow, including data cleaning, preprocessing, feature engineering, model training, evaluation, model serialization, and deployment using Flask.

## Features

* Predict passenger survival using Machine Learning
* Real-time prediction through a Flask web application
* Logistic Regression classification model
* Interactive and user-friendly interface
* Data preprocessing and feature engineering
* Model evaluation using classification metrics
* Professional project structure suitable for deployment and portfolio showcase

## Dataset Information

Dataset: Titanic Dataset

Features Used:

* Pclass
* Sex
* Age
* SibSp
* Parch
* Fare
* Embarked

Target Variable:

* Survived

Where:

* 0 = Did Not Survive
* 1 = Survived

Dataset Size:

* Rows: 891
* Columns: 12

## Technologies Used

Programming Language

* Python

Machine Learning Libraries

* Pandas
* NumPy
* Scikit-Learn

Data Visualization

* Matplotlib
* Seaborn

Web Development

* Flask
* HTML
* CSS

## Machine Learning Workflow

### 1. Data Cleaning

Removed unnecessary columns:

* PassengerId
* Name
* Ticket
* Cabin

### 2. Missing Value Handling

* Filled missing Age values using Median
* Filled missing Embarked values using Mode

### 3. Feature Encoding

Sex Encoding:

* Male = 0
* Female = 1

Embarked Encoding:

* Southampton (S) = 0
* Cherbourg (C) = 1
* Queenstown (Q) = 2

### 4. Model Development

Implemented:

* Logistic Regression

The model was trained to classify passengers as survived or not survived based on the selected features.

### 5. Model Evaluation

Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* Classification Report

Results:

* Accuracy: 79.89%

Confusion Matrix:

* True Negatives: 89
* False Positives: 16
* False Negatives: 20
* True Positives: 54

The model demonstrated strong classification performance and effectively captured survival patterns in the dataset.

### 6. Model Deployment

* Saved the trained model using Pickle
* Developed a Flask web application
* Integrated the trained model for real-time survival prediction

## Application Workflow

1. User enters passenger details.
2. Flask receives the input.
3. The trained Logistic Regression model processes the information.
4. The model predicts whether the passenger would survive.
5. The prediction is displayed on the result page.

## Project Structure

Project-03-Titanic-Survival-Prediction/

├── app.py

├── titanic_survival_model.pkl

├── train.csv

├── titanic_survival_prediction.ipynb

├── README.md

├── requirements.txt

├── .gitignore

│

├── templates/

│ ├── index.html

│ └── result.html

│

├── static/

│ └── style.css

│

└── screenshots/

├── home_page.png

├── result_page.png

├── confusion_matrix.png

└── classification_report.png

## Results

| Metric   | Value  |
| -------- | ------ |
| Accuracy | 79.89% |

### Final Model

Logistic Regression

The model achieved nearly 80% accuracy, making it a reliable baseline classification model for Titanic survival prediction.

## Screenshots

### Home Page

Add the application home page screenshot here.

### Prediction Result

Add the prediction result screenshot here.

### Confusion Matrix

Add the confusion matrix heatmap screenshot here.

### Classification Report

Add the classification report screenshot here.

## Installation and Setup

### Clone the Repository

git clone [https://github.com/your-username/Machine-Learning-Projects.git](https://github.com/your-username/Machine-Learning-Projects.git)

### Navigate to Project Directory

cd Project-03-Titanic-Survival-Prediction

### Install Dependencies

pip install -r requirements.txt

### Run Flask Application

python app.py

### Open Browser

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Classification Problems
* Logistic Regression
* Data Cleaning
* Missing Value Handling
* Feature Encoding
* Accuracy Evaluation
* Confusion Matrix Analysis
* Classification Report Interpretation
* Pickle Model Serialization
* Flask Integration
* Machine Learning Deployment
* Frontend and Backend Integration

## Future Improvements

* Compare multiple classification algorithms
* Hyperparameter tuning
* Probability-based predictions
* Enhanced UI/UX design
* Cloud deployment

## Author

Shashank Srivastava

Machine Learning | Artificial Intelligence | Data Science Enthusiast

Project Status: Completed

Challenge Progress: Project 03/100 Completed in the 100 Days of Machine Learning Challenge.

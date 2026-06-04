# Project 02: Salary Prediction Web Application using Machine Learning and Flask

## Overview

This project is an end-to-end Machine Learning web application that predicts employee salaries based on years of professional experience. The application is built using Python, Scikit-Learn, Flask, and Linear Regression, allowing users to enter their years of experience and receive real-time salary predictions.

The project demonstrates the complete Machine Learning workflow, including data analysis, visualization, model training, evaluation, and deployment through a Flask-based web application.

---

## Features

* Salary prediction based on years of experience
* Real-time prediction through a Flask web application
* Interactive and user-friendly interface
* Data visualization and analysis
* Linear Regression model implementation
* Model evaluation using MAE and R² Score
* Professional project structure for deployment and portfolio showcase

---

## Dataset Information

The dataset contains employee salary information with the following features:

* YearsExperience
* Salary

Dataset Size:

* Rows: 30
* Columns: 2

---

## Technologies Used

### Programming Language

* Python

### Machine Learning Libraries

* Pandas
* NumPy
* Scikit-Learn

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML
* CSS

---

## Machine Learning Workflow

### 1. Data Loading

* Imported and explored the salary dataset.

### 2. Data Inspection

* Verified data types.
* Checked for missing values.
* Confirmed dataset quality.

### 3. Exploratory Data Analysis

* Visualized the relationship between years of experience and salary.
* Identified a strong positive linear relationship.

### 4. Model Development

Implemented:

* Linear Regression

The model was trained to predict employee salary using years of experience as the input feature.

### 5. Model Evaluation

Evaluation Metrics:

* Mean Absolute Error (MAE)
* R² Score

Results:

* MAE: 6,286.45
* R² Score: 0.9024

The model achieved excellent predictive performance and demonstrated a strong fit to the dataset.

### 6. Model Deployment

* Saved the trained model using Pickle.
* Developed a Flask web application.
* Integrated the trained model for real-time salary prediction.

---

## Application Workflow

1. User enters years of professional experience.
2. Flask receives the input.
3. The trained Linear Regression model generates a salary prediction.
4. The predicted salary is displayed on the result page.

---

## Project Structure

Project-02-Salary-Prediction/

├── app.py

├── salary_prediction_model.pkl

├── Salary_Data.csv

├── salary_prediction.ipynb

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

├── input_page.png

├── result_page.png

├── experience_vs_salary.png

├── regression_line.png

└── actual_vs_predicted.png

---

## Results

| Metric   | Value    |
| -------- | -------- |
| MAE      | 6,286.45 |
| R² Score | 0.9024   |

### Final Model

Linear Regression

The model achieved an R² score greater than 90%, indicating a strong relationship between years of experience and employee salary.

---

## Screenshots

### Input Page

<img width="669" height="449" alt="Screenshot 2026-06-05 002303" src="https://github.com/user-attachments/assets/feb52f86-bcf6-46b5-956c-3eac6a255058" />

### Prediction Result

<img width="608" height="454" alt="Screenshot 2026-06-05 002309" src="https://github.com/user-attachments/assets/afafe808-55ef-40b2-a832-80796c8729cf" />


### Experience vs Salary Visualization

<img width="721" height="470" alt="image" src="https://github.com/user-attachments/assets/8edd9d02-c8e2-4cbb-a2b7-c8ea3736b080" />


### Regression Line

<img width="721" height="470" alt="image" src="https://github.com/user-attachments/assets/fca5cdbd-b7ad-4138-be1f-3397c906598d" />


---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Machine-Learning-Projects.git
```

### Navigate to Project Directory

```bash
cd Project-02-Salary-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Data Analysis
* Data Visualization
* Linear Regression
* Model Training
* Model Evaluation
* MAE Calculation
* R² Score Analysis
* Pickle Model Serialization
* Flask Integration
* Machine Learning Deployment
* Frontend and Backend Integration

---

## Future Improvements

* Add support for multiple salary-related features
* Implement advanced regression algorithms
* Improve UI/UX design
* Deploy the application to cloud platforms
* Add salary trend analytics

---

## Author

Shashank Srivastava

Machine Learning | Artificial Intelligence | Data Science Enthusiast

---

If you found this project helpful, consider giving it a star.

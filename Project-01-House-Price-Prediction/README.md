# House Price Prediction Web Application using Machine Learning and Flask

## Overview

This project is an end-to-end Machine Learning web application that predicts residential house prices based on various property features and amenities. The application is built using Python, Scikit-Learn, Flask, and Linear Regression, allowing users to enter house details through a user-friendly web interface and receive real-time price predictions.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, comparison of multiple algorithms, and deployment through a Flask-based web application.

---

## Features

* House price prediction based on property characteristics
* Interactive Flask web interface
* Real-time prediction generation
* Data preprocessing and feature encoding
* Exploratory Data Analysis (EDA)
* Correlation analysis using heatmaps
* Model performance evaluation
* Comparison of multiple Machine Learning algorithms
* Professional and responsive user interface

---

## Dataset Information

The dataset contains residential housing information with features such as:

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Guest Room Availability
* Basement Availability
* Hot Water Heating
* Air Conditioning
* Parking Capacity
* Preferred Area
* Furnishing Status
* House Price (Target Variable)

---

## Technologies Used

### Programming Language

* Python

### Machine Learning Libraries

* Scikit-Learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML
* CSS

---

## Machine Learning Workflow

### 1. Data Collection

* Loaded and explored the housing dataset.

### 2. Data Preprocessing

* Checked for missing values.
* Analyzed feature distributions.
* Encoded categorical variables.
* Performed feature transformation.

### 3. Exploratory Data Analysis

* Dataset inspection
* Statistical summary
* Correlation analysis
* Feature relationship visualization

### 4. Model Development

Two regression algorithms were implemented and compared:

#### Linear Regression

* Final selected model
* R² Score: 0.6529
* MAE: ₹970,043

#### Random Forest Regressor

* R² Score: 0.6114
* MAE: ₹1,022,560

After performance comparison, Linear Regression was selected as the final model due to better predictive performance on the test dataset.

### 5. Model Evaluation

Evaluation metrics used:

* Mean Absolute Error (MAE)
* R² Score

### 6. Model Deployment

* Trained model saved using Pickle.
* Flask application developed for real-time predictions.
* User inputs are processed and passed to the trained model.
* Predicted house price is displayed on a dedicated result page.

---

## Application Workflow

1. User enters property details through the web interface.
2. Flask receives and validates the inputs.
3. Data is transformed into the format required by the trained model.
4. The Linear Regression model generates a prediction.
5. The predicted house price is displayed along with the entered property details.

---

## Project Structure

```text
House-Price-Prediction-ML/
│
├── app.py
├── house_price_model.pkl
├── Housing.csv
├── house_price_prediction.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── input_page.png
│   ├── result_page.png
│   ├── correlation_heatmap.png
│   ├── actual_vs_predicted.png
│   └── model_comparison.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Results

| Model                   | MAE       | R² Score |
| ----------------------- | --------- | -------- |
| Linear Regression       | 970,043   | 0.6529   |
| Random Forest Regressor | 1,022,560 | 0.6114   |

### Final Model

**Linear Regression**

The Linear Regression model achieved the best overall performance and was selected for deployment in the Flask application.

---

## Screenshots

### Input Form

<img width="495" height="729" alt="Screenshot 2026-06-03 091020" src="https://github.com/user-attachments/assets/7547c669-6bc8-47e7-9afe-00d8399b9cd0" />


### Prediction Result

<img width="521" height="606" alt="Screenshot 2026-06-03 091029" src="https://github.com/user-attachments/assets/1ad0d77c-b4ba-429b-8aae-2a1944c1630a" />


### Correlation Heatmap

<img width="1116" height="889" alt="correlation" src="https://github.com/user-attachments/assets/8a260998-5752-4a40-989b-c07bdc36e37e" />


### Actual vs Predicted Prices

<img width="833" height="547" alt="vs" src="https://github.com/user-attachments/assets/e2fc6636-1922-4e50-84ea-1ee1e1e25d46" />

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction-ML.git
```

### Navigate to the Project Directory

```bash
cd House-Price-Prediction-ML
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Data Cleaning and Preprocessing
* Feature Engineering
* Exploratory Data Analysis
* Correlation Analysis
* Linear Regression
* Random Forest Regression
* Model Evaluation
* Model Comparison
* Flask Integration
* Machine Learning Deployment
* Frontend and Backend Integration

---

## Future Improvements

* Add advanced regression algorithms
* Improve model performance through hyperparameter tuning
* Deploy the application on cloud platforms
* Enhance UI/UX design
* Add prediction history and analytics dashboard
* Implement user authentication

---

## Author

Shashank Srivastava

Machine Learning | Artificial Intelligence | Data Science Enthusiast

---

If you found this project helpful, consider giving it a star.

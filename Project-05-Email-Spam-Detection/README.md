# Email Spam Detection Web Application

## Project Overview

The Email Spam Detection Web Application is an end-to-end Machine Learning project designed to classify email and SMS messages as Spam or Not Spam.

The project utilizes Natural Language Processing (NLP) techniques and a Multinomial Naive Bayes classifier to analyze text messages and predict whether a message is spam. A user-friendly Flask web application has been developed to provide real-time predictions through a clean and interactive interface.

This project was developed as part of my 100 Days of Machine Learning Challenge to strengthen my understanding of NLP, text classification, machine learning model deployment, and Flask development.

---

## Problem Statement

Spam messages are one of the most common challenges in digital communication. They often contain promotional content, fraudulent offers, phishing attempts, or unwanted advertisements.

The objective of this project is to build a machine learning model capable of automatically identifying spam messages and separating them from legitimate messages.

---

## Dataset Information

Dataset: SMS Spam Collection Dataset

Total Records: 5,572

Target Classes:

• Ham (Not Spam)
• Spam

Features:

• Message Text
• Label

---

## Project Workflow

1. Data Collection

   * Loaded the SMS Spam Collection dataset.

2. Data Cleaning

   * Removed unnecessary columns.
   * Renamed columns for better readability.
   * Checked and handled missing values.

3. Data Preprocessing

   * Encoded target labels.
   * Split the dataset into training and testing sets.

4. Text Vectorization

   * Converted text data into numerical features using TF-IDF Vectorization.

5. Model Training

   * Trained a Multinomial Naive Bayes classifier.

6. Model Evaluation

   * Evaluated model performance using:

     * Accuracy Score
     * Confusion Matrix
     * Classification Report

7. Model Saving

   * Saved the trained model using Pickle.
   * Saved the TF-IDF Vectorizer for deployment.

8. Flask Deployment

   * Built a web application for real-time spam detection.
   * Integrated the trained model and vectorizer with Flask.

---

## Technologies Used

Python

Pandas

NumPy

Scikit-Learn

Natural Language Processing (NLP)

TF-IDF Vectorizer

Multinomial Naive Bayes

Flask

HTML

CSS

Matplotlib

Seaborn

Pickle

Jupyter Notebook

---

## Model Performance

Accuracy Score: 96.68%

Confusion Matrix:

[[965, 0],
[37, 113]]

Classification Report:

Class 0 (Not Spam)
Precision: 0.96
Recall: 1.00
F1-Score: 0.98

Class 1 (Spam)
Precision: 1.00
Recall: 0.75
F1-Score: 0.86

---

## Project Structure

Project-05-Email-Spam-Detection/

│

├── spam.csv

├── email_spam_detection.ipynb

├── spam_model.pkl

├── tfidf_vectorizer.pkl

├── app.py

│

├── templates/

│   ├── index.html

│   └── result.html

│

├── static/

│   └── style.css

│

└── README.md

---

## Web Application Features

• Real-time Spam Detection

• User-Friendly Interface

• Machine Learning Powered Predictions

• NLP-Based Text Processing

• Responsive Design

• Instant Prediction Results

---

## Future Improvements

• Advanced Text Cleaning Pipeline

• Stemming and Lemmatization

• Support for Multiple Languages

• Deep Learning-Based Text Classification

• Email Integration

• Probability-Based Predictions

---

## Author

Shashank Srivastava

Aspiring AI/ML Engineer | Machine Learning Enthusiast

---

If you found this project useful, feel free to explore the repository and follow my Machine Learning journey through the 100 Days of Machine Learning Challenge.

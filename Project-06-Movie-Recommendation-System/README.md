# 🎬 Day 06 - Movie Recommendation System

Part of my **100 Days of Machine Learning Challenge**

**Project Number:** 06/100
**Category:** Recommendation Systems / NLP

---

## 📌 Project Overview

This project is a Content-Based Movie Recommendation System built using Machine Learning, Natural Language Processing (NLP), and Flask.

The system recommends movies similar to a selected movie by analyzing:

* Genres
* Keywords
* Cast
* Crew
* Movie Overview

using NLP techniques and Cosine Similarity.

---

## 🚀 Features

✅ Content-Based Recommendation Engine

✅ Natural Language Processing (NLP)

✅ Text Vectorization using CountVectorizer

✅ Cosine Similarity-Based Recommendations

✅ Top 5 Similar Movie Suggestions

✅ Interactive Flask Web Application

✅ Modern Responsive User Interface

✅ Searchable Movie Selection

✅ Recommendation Cards with Ranking

---

## 📊 Dataset

Dataset Used:

**TMDB 5000 Movie Dataset**

Files:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

Total Movies:

* 4800+ Movies

---

## 🧠 Machine Learning Workflow

### 1. Data Collection

Merged:

* Movies Dataset
* Credits Dataset

### 2. Feature Selection

Selected Features:

* genres
* keywords
* overview
* cast
* crew

### 3. Feature Engineering

Created a new feature called **tags** by combining:

* Overview
* Genres
* Keywords
* Cast
* Crew

### 4. NLP Preprocessing

Performed:

* Tokenization
* Lowercasing
* Stemming using Porter Stemmer

### 5. Vectorization

Used:

* CountVectorizer

Parameters:

* max_features = 5000
* stop_words = "english"

### 6. Similarity Calculation

Used:

* Cosine Similarity

### 7. Recommendation Generation

The system finds the five most similar movies based on content similarity.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Pickle

### Framework

* Flask

### Frontend

* HTML
* CSS

### Machine Learning Concepts

* Natural Language Processing (NLP)
* Feature Engineering
* Count Vectorization
* Cosine Similarity
* Content-Based Recommendation System

---

## 📁 Project Structure

```text
Project-06-Movie-Recommendation-System/

│
├── app.py
├── movie_recommendation.ipynb
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/
│
├── notebooks/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── screenshots/
    ├── home_page.png
    └── recommendation_page.png
```

---

## 📷 Application Screenshots

### Home Page

<img width="1007" height="856" alt="Screenshot 2026-06-20 084032" src="https://github.com/user-attachments/assets/24329c83-b645-4678-b1c4-56a5134fdeb7" />


* Modern Glassmorphism UI
* Searchable Movie Selection
* Statistics Dashboard
* Feature Highlights

### Recommendation Page

<img width="453" height="687" alt="Screenshot 2026-06-20 084048" src="https://github.com/user-attachments/assets/7e43c8ce-4c96-4447-b6b1-756716bf87d4" />

* Top 5 Recommendations
* Ranked Recommendation Cards
* Responsive Layout
* Interactive Design

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📈 Future Improvements

* Movie Posters using TMDB API
* Movie Ratings and Release Year
* Search Autocomplete Enhancements
* Hybrid Recommendation System
* Streamlit Version
* Deployment on Render
* Deployment on Hugging Face Spaces

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Data Cleaning and Feature Engineering
* Natural Language Processing
* Text Vectorization
* Stemming with NLTK
* CountVectorizer
* Cosine Similarity
* Recommendation Systems
* Model Serialization using Pickle
* Flask Application Development
* Frontend Design using HTML and CSS

---

## 💻 Author

**Shashank Srivastava**

Aspiring AI/ML Engineer

### 🚀 100 Days of Machine Learning Challenge

Progress:

**Day 06 / 100 Completed**

---

If you found this project interesting, feel free to explore the repository and follow my journey through the **100 Days of Machine Learning Challenge**.

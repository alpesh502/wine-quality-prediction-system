# 🍷 Wine Quality Prediction System – End-to-End Machine Learning Deployment Project

## 📖 Project Overview
This project is an end-to-end **Machine Learning regression and deployment solution** that predicts the **quality score of red wine** based on its physicochemical properties.

The project demonstrates a complete ML workflow — from data preprocessing and model training to deploying a trained model as a **Flask web application** for real-time predictions.

---

## 🌐 Live Demo
👉 https://wine-quality-ml-v9tk.onrender.com

---

## 🍷 Business Context
Wine quality evaluation is traditionally performed by human experts through sensory analysis. However, this process can be:
- Subjective  
- Time-consuming  
- Inconsistent across evaluators

This project addresses these challenges by using **machine learning regression** to predict wine quality objectively based on measurable chemical attributes.

---

## 🎯 Objective
The main objectives of this project are:

- Predict the **actual wine quality score** (continuous value)
- Use a **regression-based ML model** instead of binary classification
- Deploy the trained model using **Flask**
- Provide a **user-friendly web interface** for real-time predictions
- Follow industry-standard **separation of training and inference**

---

## 🛠️ Tech Stack

### Machine Learning & Data
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- RandomForestRegressor  

### Deployment & Web
- Flask  
- HTML & CSS  
- Pickle (model serialization)  

---

## 🧠 Machine Learning Approach

### Problem Type
- **Regression Problem**  
- Target Variable: `quality` (wine quality score)

### Model Used
- **Random Forest Regressor**
  - Handles non-linear relationships
  - Robust to noise
  - Performs well on structured/tabular datasets

### Model Workflow
1. Data preprocessing and feature selection  
2. Train-test split  
3. Model training using Random Forest Regressor  
4. Model evaluation using regression metrics (RMSE)  
5. Model serialization (`model.pkl`)  
6. Deployment for inference via Flask  

---

## 🏗️ Solution Architecture

The project follows a **production-style machine learning architecture**:

- Wine Dataset (CSV)
- Data Preprocessing & Training (Jupyter Notebook)
- Trained Regression Model (`model.pkl`)
- Flask Backend (Inference Layer)
- Web Interface (User Input → Prediction Output)


---

## 📈 Business Value
- Enables **objective and consistent wine quality prediction**
- Reduces reliance on manual sensory evaluation
- Provides **real-time quality scoring**
- Demonstrates a **production-grade ML deployment**
- Can be extended for:
    Winery quality control systems  
    Manufacturing optimization  
    Decision-support tools  

---

## 👤 Author
**Alpesh Singh**  
B.Tech (AIML) – 3rd Year  
Aspiring Data Engineer & Machine Learning Engineer  











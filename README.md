# 🍽️ Zomato Rating Prediction

An **end-to-end Machine Learning project** that predicts restaurant ratings on Zomato using key attributes such as location, restaurant type, cuisines, cost for two, online ordering, and table booking availability.  
The project includes **EDA, data cleaning, feature engineering, model selection, training, and deployment** using **Flask** and **Streamlit**.

---

## 📌 Project Overview

- **Problem Type**: Regression  
- **Target Variable**: Restaurant Rating  
- **Best Model**: Random Forest Regressor  
- **Deployment**:
  - Backend API: Flask
  - Frontend UI: Streamlit

---

## 📂 Dataset

📎 **Google Drive Link**  
https://drive.google.com/drive/folders/1Vq8eZV6KA3Y0p_V0Q8fcsQLqnTjSr1?usp=sharing

### Dataset Files
- `zomato.csv` → Raw dataset  
- `df_clean.csv` → Cleaned dataset  
- `X_final.csv` → Final feature set  
- `y.csv` → Target variable (ratings)

---

## 📁 Project Structure
Zomato-Rating-Prediction/
│
├── data/
│ ├── zomato.csv
│ ├── df_clean.csv
│ ├── X_final.csv
│ └── y.csv
│
├── notebooks/
│ ├── eda.ipynb
│ ├── data_cleaning_and_feature_engineering.ipynb
│ ├── model_selection.ipynb
│ └── model_training.ipynb
│
├── model/
│ ├── zomato_rating_model_rmse_0.321_20251229_0230.joblib
│ └── zomato_rating_model_metadata_20251229_0230.json
│
├── app.py
├── streamlit_app.py
├── requirements.txt
└── README.md


---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand:
- Distribution of restaurant ratings
- Relationship between votes, cost, and ratings
- Popular locations and cuisines
- Effect of online ordering and table booking

📘 Notebook: `eda.ipynb`

---

## 🧹 Data Cleaning & Feature Engineering

Steps performed:
- Removed unrated restaurants
- Handled missing and inconsistent values
- One-Hot Encoded categorical variables
- Created engineered features:
  - `cuisines_count`
  - `pop_cuisines_count`
- Selected top locations, cuisines, and restaurant types

📘 Notebook: `data_cleaning_and_feature_engineering.ipynb`

---

## 🤖 Model Selection & Training

### Models Evaluated
- Linear Regression  
- Ridge & Lasso Regression  
- Decision Tree  
- **Random Forest Regressor (Best Performing)**  

📘 Notebooks:
- `model_selection.ipynb`
- `model_training.ipynb`

### 🔥 Final Model Performance

| Metric | Value |
|------|------|
| RMSE | 0.3207 |
| MAE  | 0.1301 |
| R² Score | 0.6885 |
| Number of Features | 56 |

---

## 🚀 Deployment

### 🔹 Flask API

- Endpoint: `/predict`
- Method: `POST`
- Input: JSON feature vector
- Output: Predicted restaurant rating

Run Flask API:
python app.py

### 🔹 Streamlit Application
Interactive UI for entering restaurant details and predicting ratings.

Run Streamlit app:

streamlit run streamlit_app.py

### 🧠 Features Used

- Online order availability
- Table booking availability
- Number of votes
- Approx cost for two people
-  Location
- Restaurant type
- Listed city
- Listed category type
- Cuisine count
- Popular cuisine overlap count

### 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Flask
- Streamlit
- Joblib

### ✅ How to Run the Project

-Clone the repository
-Install dependencies
   pip install -r requirements.txt
- Start Flask backend
- Run Streamlit frontend
- Enter restaurant details and get predicted rating ⭐


### 👨‍💻 Author

Kartavya Gupta
Machine Learning Enthusiast 🚀



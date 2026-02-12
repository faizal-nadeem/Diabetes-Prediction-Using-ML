# 🩺 Diabetes Prediction (Machine Learning Project)

This is a **Machine Learning project** that predicts the likelihood of diabetes based on health-related features like **Pregnancies, Glucose, Blood Pressure, BMI, Age**, etc.  
It is built in **Python** and deployed as a **Streamlit web app**.

---

## 🚀 How to Run in VS Code

1. **Clone this repository**
   ```bash
   git clone https://github.com/faizal-nadeem/diabetes-prediction.git
   cd diabetes-prediction

2. **Create a virtual environment (recommended)**
    python -m venv venv
    venv\Scripts\activate     # For Windows
    source venv/bin/activate  # For Linux/Mac

3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the training notebook (optional)**
    Open diabetes.ipynb in VS Code Jupyter extension to explore data and train models.

5. **Run the web app**
    streamlit run app.py

# 📊 Dataset:-

We used the PIMA Indians Diabetes Dataset (from Kaggle/UCI repository).
It contains health information of women (≥21 years old).

# Features include:-

    Pregnancies
    Glucose
    Blood Pressure
    Skin Thickness
    Insulin
    BMI
    Diabetes Pedigree Function
    Age

# ⚙️ Tech Stack:-

    Python
    scikit-learn
    Pandas, NumPy
    Streamlit
    Joblib

# 📈 Model Performance:-

    Support Vector Machine (SVM) → ~75% Accuracy
    Logistic Regression → ~76% Accuracy
    Balanced Precision, Recall, and F1-Score

# ⚠️ Warning:-

    This project uses a small dataset (PIMA) and is meant only for practice/learning purposes.
    It should not be used for actual medical diagnosis. Always consult a qualified healthcare professional for real medical advice.
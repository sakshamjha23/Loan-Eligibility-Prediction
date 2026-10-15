# 🏦 Loan Eligibility Prediction System

> **A Machine Learning project that classifies loan eligibility using housing and property-related features.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Classification-orange?style=for-the-badge" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Scikit--Learn-Random%20Forest-green?style=for-the-badge&logo=scikit-learn" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
</p>

---

## ✨ Overview

**Loan Eligibility Prediction System** is a Python-based Machine Learning project that uses property-related information to classify a house into one of two categories: eligible or not eligible.

The project uses a **Random Forest Classifier** trained on housing data and provides an interactive web interface built with Streamlit. Users can enter property details and receive an instant classification.

The project demonstrates a practical Machine Learning workflow, including data preprocessing, feature encoding, model training, classification, and interactive prediction.

### Project Workflow

```text
🏠 Housing Dataset (CSV)
          ↓
🧹 Data Preprocessing
          ↓
🔢 Feature Encoding
          ↓
🏷️ Target Label Creation
          ↓
🤖 Random Forest Classifier
          ↓
🌐 Streamlit Web Interface
          ↓
✅ Eligibility Classification
```

---

## 🎯 Problem Statement

Classifying properties based on their characteristics can help demonstrate how Machine Learning models identify patterns in historical housing data.

This project builds a classification model using features such as property area, number of bedrooms and bathrooms, parking availability, amenities, and furnishing status.

The model uses historical property prices to generate binary labels and predicts the corresponding class for new property inputs.

**Note:** This is an educational classification project. It does not evaluate actual financial loan eligibility because it does not consider income, credit score, existing debt, employment, or lender-specific criteria.

---

## 🚀 Key Features

- 📂 Loads housing data from a CSV dataset using Pandas.
- 🧹 Preprocesses categorical property attributes using numerical encoding.
- 🏷️ Creates binary target labels based on the median housing price.
- 🤖 Trains a Random Forest Classifier using Scikit-learn.
- 🌐 Provides an interactive prediction interface using Streamlit.
- ⚡ Accepts property details through input fields and dropdown menus.
- 📊 Classifies property inputs into two categories based on learned patterns.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset loading and preprocessing |
| Scikit-learn | Model training and classification |
| Random Forest | Classification algorithm |
| Streamlit | Interactive web application |
| Housing.csv | Training and testing dataset |

---

## 📁 Project Structure

```text
Loan-Eligibility-Prediction/
│
├── app.py
├── Housing.csv
├── requirements.txt
└── README.md
```

### Files

- **`app.py`** — Loads and preprocesses data, trains the classifier, and runs the Streamlit application.
- **`Housing.csv`** — Contains the housing data used for model training and testing.
- **`requirements.txt`** — Lists the Python dependencies required to run the application.
- **`README.md`** — Documents the project, setup instructions, and workflow.

---

## 🔄 Machine Learning Workflow

### 1. Dataset Loading

The housing dataset is loaded from a CSV file using Pandas.

```python
import pandas as pd

df = pd.read_csv("Housing.csv")
```

### 2. Data Preprocessing

Categorical property attributes are converted into numerical values so that the model can process them.

Examples include:

- Yes/No property features mapped to `1` and `0`.
- Furnishing status encoded as `2`, `1`, and `0`.

### 3. Target Label Creation

The median property price is used to create the binary classification target.

```python
threshold = df["price"].median()

df["Loan_Status"] = df["price"].apply(
    lambda price: 1 if price > threshold else 0
)
```

Properties priced above the median receive label `1`, while properties priced at or below the median receive label `0`.

These labels are proxies for the demonstration's eligibility categories, not actual loan approval decisions.

### 4. Model Training

The dataset is divided into training and testing subsets, and a Random Forest Classifier is trained.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df.drop(["price", "Loan_Status"], axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(X_train, y_train)
```

### 5. Interactive Prediction

The Streamlit interface collects property information, converts the inputs into the expected numerical format, and passes them to the trained model.

The application displays one of two results:

- **Eligible:** The model predicts class `1`.
- **Not Eligible:** The model predicts class `0`.

---

## 🖥️ Application Interface

The application accepts the following inputs:

- Property area
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Parking spaces
- Main road access
- Guest room availability
- Basement availability
- Hot water heating
- Air conditioning
- Preferred area
- Furnishing status

After the user clicks **Check Eligibility**, the model generates a classification based on the supplied property details.

---

## ⚙️ Installation and Setup

### 1. Clone the repository

Replace the example URL with your updated GitHub repository URL after renaming it.

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Loan-Eligibility-Prediction
```

### 3. Install dependencies

Create a `requirements.txt` file containing:

```text
streamlit
pandas
scikit-learn
```

Install the packages:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The Streamlit application will provide a local URL in the terminal. Open it in your browser to use the prediction interface.

---

## 📈 Future Improvements

- [ ] Use a genuine loan eligibility dataset with approved and rejected loan applications.
- [ ] Include applicant income, credit score, employment status, and existing liabilities.
- [ ] Evaluate model performance using accuracy, precision, recall, F1-score, and a confusion matrix.
- [ ] Add cross-validation and hyperparameter tuning.
- [ ] Save and load the trained model instead of retraining on every application startup.
- [ ] Add input validation and improved error handling.
- [ ] Deploy the application to a cloud platform.

---

## 🎓 Learning Outcomes

This project provides practical experience with:

- Supervised Machine Learning and classification.
- Data preprocessing and categorical feature encoding.
- Training a Random Forest model.
- Splitting data into training and testing subsets.
- Building an interactive Streamlit application.
- Integrating a trained Machine Learning model into a web interface.

---

## 👨‍💻 Author

**Update this section with your own name, educational background, and GitHub profile.**

- GitHub: [Your GitHub Profile](https://github.com/)

---

<p align="center">
  <b>🏦 Turning Property Data into Machine Learning Predictions 🤖</b>
</p>

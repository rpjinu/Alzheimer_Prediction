# Alzheimer_Prediction
"A machine learning-based web application using Streamlit to predict Alzheimer's diagnosis based on patient demographics, lifestyle, and health factors, leveraging an encoded dataset and a trained Random Forest model. 🚀"

<img src="">

# 🧠 Alzheimer Prediction Project

## 📌 Overview
This project is a **machine learning-powered web application** that predicts **Alzheimer's diagnosis** based on various patient demographics, lifestyle habits, and health factors. Built with **Streamlit**, it allows users to input patient details and get a **real-time prediction**. 🚀

## ✨ Features
- 🏥 **Alzheimer Diagnosis Prediction** using a trained **Random Forest Classifier**
- 📊 **Feature Encoding** using a pre-trained **OneHotEncoder/LabelEncoder**
- 🖥️ **Web Interface** built with **Streamlit**
- 🏗 **End-to-End Pipeline**: Data Preprocessing ➡ Model Training ➡ Model Deployment
- 💾 **Model Persistence** using **joblib**

## 📂 Project Structure
```
📦 Alzheimer-Prediction
├── 📜 app.py                  # Streamlit Web App
├── 📜 model.pkl               # Trained Machine Learning Model
├── 📜 encoder.pkl             # Trained Encoder for Categorical Data
├── 📜 requirements.txt        # Required Python Libraries
├── 📜 README.md               # Project Documentation
└── 📁 dataset                 # Dataset (if available)
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Alzheimer-Prediction.git
cd Alzheimer-Prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📊 Dataset Overview
The dataset consists of **74283 records** with features such as:
- 🏡 **Demographics** (Age, Gender, Education Level)
- 🏃‍♂️ **Lifestyle Factors** (Physical Activity, Smoking, Alcohol, Diet)
- 💉 **Health Metrics** (Diabetes, Hypertension, Cholesterol)
- 🧠 **Cognitive & Psychological Indicators** (Cognitive Test Score, Depression, Stress, Sleep Quality)
- 🔬 **Genetic & Environmental Risk** (APOE-ε4 allele, Air Pollution Exposure)

### 🎯 **Target Column**
- `Alzheimer’s Diagnosis` (Binary: `0` = No, `1` = Yes)

## 🚀 Model Training & Prediction
### **🔹 Step 1: Preprocessing & Encoding**
- Used **Label Encoding** for categorical columns
- Scaled numerical features if necessary

### **🔹 Step 2: Model Training**
- **Random Forest Classifier** was used with **Hyperparameter Tuning**
- Other models tested: Logistic Regression, KNN, Decision Tree, SVM, Naive Bayes

### **🔹 Step 3: Saving Model & Encoder**
```python
import joblib
joblib.dump(model, 'model.pkl')
joblib.dump(encoder, 'encoder.pkl')
```

### **🔹 Step 4: Loading and Predicting in Streamlit**
```python
model = joblib.load('model.pkl')
encoder = joblib.load('encoder.pkl')

# Encode user input
data_encoded = encode_input(user_input, encoder)

# Make Prediction
prediction = model.predict(data_encoded)
```

## 🎨 Streamlit Web App UI
The **web interface** allows users to:
✅ Enter patient details
✅ Get **Alzheimer's Prediction** instantly
✅ View encoded inputs & backend model process

## 🎯 Future Improvements
- 🧪 **Deep Learning Models** (e.g., LSTMs, CNNs for medical imaging)
- 🌍 **API Deployment** (FastAPI, Flask, or Docker)
- 📊 **Feature Importance Analysis** to enhance explainability

## 🤝 Contributing
Want to improve this project? 🚀
- Fork this repository
- Create a new branch (`git checkout -b feature-xyz`)
- Commit changes (`git commit -m "Added XYZ feature"`)
- Push and open a **Pull Request**

## 📜 License
This project is open-source under the **MIT License**.

---
Made with ❤️ by **Rnajan kumar pradhan** 🚀


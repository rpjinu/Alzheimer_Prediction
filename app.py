import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model & encoder
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\model.pkl")
encoder = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\encoder.pkl")  # Ensure this encodes categorical variables

# Function to encode categorical inputs
def encode_input(data, encoder):
    df = pd.DataFrame([data], columns=["Gender", "Education Level", "Physical Activity Level", 
                                       "Smoking Status", "Alcohol Consumption", "Diabetes", 
                                       "Hypertension", "Cholesterol Level", "Family History of Alzheimer’s",
                                       "Depression Level", "Sleep Quality", "Dietary Habits", 
                                       "Air Pollution Exposure", "Genetic Risk Factor (APOE-ε4 allele)",
                                       "Social Engagement Level", "Stress Levels", "Age", "BMI", "Cognitive Test Score"])

    # Transform categorical features
    encoded_data = encoder.transform(df)  # If using OneHotEncoder, this returns a sparse matrix

    return encoded_data.toarray()  # Convert to NumPy array if needed

# Streamlit UI
st.title("Alzheimer's Diagnosis Prediction")

# Input fields
age = st.number_input("Age", min_value=30, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.number_input("Education Level (Years)", min_value=1, max_value=20, step=1)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
physical_activity = st.selectbox("Physical Activity Level", ["Low", "Medium", "High"])
smoking_status = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
alcohol = st.selectbox("Alcohol Consumption", ["Never", "Occasionally", "Regularly"])
diabetes = st.selectbox("Diabetes", ["No", "Yes"])
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
cholesterol = st.selectbox("Cholesterol Level", ["Normal", "High"])
family_history = st.selectbox("Family History of Alzheimer’s", ["No", "Yes"])
cognitive_score = st.number_input("Cognitive Test Score", min_value=0, max_value=100, step=1)
depression = st.selectbox("Depression Level", ["Low", "Medium", "High"])
sleep_quality = st.selectbox("Sleep Quality", ["Poor", "Average", "Good"])
dietary_habits = st.selectbox("Dietary Habits", ["Unhealthy", "Average", "Healthy"])
air_pollution = st.selectbox("Air Pollution Exposure", ["Low", "Medium", "High"])
genetic_risk = st.selectbox("Genetic Risk Factor (APOE-ε4 allele)", ["No", "Yes"])
social_engagement = st.selectbox("Social Engagement Level", ["Low", "Medium", "High"])
stress_levels = st.selectbox("Stress Levels", ["Low", "Medium", "High"])

# Prediction button
if st.button("Predict"):
    user_input = [gender, education, physical_activity, smoking_status, alcohol, diabetes, hypertension,
                  cholesterol, family_history, depression, sleep_quality, dietary_habits, air_pollution,
                  genetic_risk, social_engagement, stress_levels, age, bmi, cognitive_score]
    
    encoded_input = encode_input(user_input, encoder)
    prediction = model.predict(encoded_input)[0]
    
    result = "Positive for Alzheimer's" if prediction == 1 else "Negative for Alzheimer's"
    
    st.success(f"Prediction: {result}")


import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Score Predictor")

study_hours = st.number_input("Study Hours", 0.0, 12.0)
attendance = st.number_input("Attendance (%)", 0, 100)
previous_score = st.number_input("Previous Score", 0, 100)

if st.button("Predict"):
    input_data = np.array([[study_hours, attendance, previous_score]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Score: {prediction[0]:.2f}")
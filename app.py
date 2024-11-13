import streamlit as st
import joblib
import pandas as pd
import numpy as np
import keras

# Load the trained model from the .pkl file
model = joblib.load('model.pkl')  # Path to your model file

# Title of the app
st.title("Health and Lifestyle Questionnaire")

# User input fields
age = st.number_input("Age", min_value=0, max_value=120, value=25)
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=21.5)
weight = st.number_input("Weight (in kg)", min_value=0.0, max_value=200.0, value=60.0)
height = st.number_input("Height (in cm)", min_value=0.0, max_value=250.0, value=160.0)

pregnant = st.selectbox("Are you/Have you been Pregnant?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
abortions = st.number_input("No of abortions/miscarriages (- please enter 0 if none)", min_value=0, value=0)
period_months = st.number_input("After how many months do you get your period?", min_value=0, value=28)

hair_loss = st.selectbox("Do you have hair loss?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
exercise = st.selectbox("Do you regularly exercise?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
junk_food = st.selectbox("Junk food intake", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
weight_gain = st.selectbox("Do you gain weight easily?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
blood_pressure = st.selectbox("How is your Blood pressure?", [0, 1], format_func=lambda x: "High" if x == 1 else "Normal")
facial_hair = st.selectbox("Do you have excessive facial/body hair?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
married_years = st.number_input("How many years have you been married? (0 if unmarried)", min_value=0, value=0)
acne_skin = st.selectbox("Do you have acne/oily skin?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
stress = st.selectbox("Are you stressed often?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
skin_darkening = st.selectbox("Are you noticing skin darkening recently?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
mood_swings = st.selectbox("Do you experience mood swings?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
period_duration = st.number_input("How long does your period last? (How long do you bleed - in Days)", min_value=0, value=5)
lifestyle = st.selectbox("Do you have a more active or sedentary lifestyle?", [0, 1], format_func=lambda x: "Active" if x == 1 else "Sedentary")
thyroid = st.selectbox("Do you have thyroid?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Displaying user input summary
if st.button("Submit"):
    # Create a DataFrame with user inputs for prediction
    input_data = pd.DataFrame({
        'Age': [age],
        'BMI': [bmi],
        'Weight (in kg)': [weight],
        'Height (in cm)': [height],
        'Are you/Have you been Pregnant?': [pregnant],
        'No of abortions/miscarriages (- please enter 0 if none)': [abortions],
        'After how many months do u get your period?': [period_months],
        'Do you have hair loss?': [hair_loss],
        'Do you regularly exercise?': [exercise],
        'Junk food intake': [junk_food],
        'Do you gain weight easily?': [weight_gain],
        'How is your Blood pressure ?': [blood_pressure],
        'Do you have excessive facial/body hair?': [facial_hair],
        'How many years have you been married - (0 if unmarried)': [married_years],
        'Do you have acne/oily skin?': [acne_skin],
        'Are you stressed often?': [stress],
        'Are you noticing skin darkening recently?': [skin_darkening],
        'Do you experience mood swings ?': [mood_swings],
        'How long does your period last ? (How long do you bleed - in Days)': [period_duration],
        'Do you have excessive facial/body hair?': [facial_hair],
        'do you have a more active or sedentary life style?': [lifestyle],
        'Do you have thyroid?': [thyroid],
    })
    
    # Make a prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Show the prediction result
    st.write(f"## Prediction Result: {'Positive' if prediction[0] == 1 else 'Negative'}")

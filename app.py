pip install joblib 
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Load the trained pipeline model
model = joblib.load('satisfaction_model.joblib')

def predict_satisfaction(features):
    input_data = pd.DataFrame([features])
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Customer Satisfaction Input Form")
    st.write("Fill in the information below based on the dataset columns.")

    # Mappings for categorical fields to integers
    gender_mapping = {"Male": 0, "Female": 1}
    customer_type_mapping = {"Loyal Customer": 0, "Disloyal Customer": 1}
    type_of_travel_mapping = {"Business travel": 0, "Personal Travel": 1}
    class_mapping = {"Business": 0, "Eco": 1, "Eco Plus": 2}

    gender = st.selectbox("Gender", list(gender_mapping.keys()))
    customer_type = st.selectbox("Customer Type", list(customer_type_mapping.keys()))
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
    type_of_travel = st.selectbox("Type of Travel", list(type_of_travel_mapping.keys()))
    class_ = st.selectbox("Class", list(class_mapping.keys()))
    flight_distance = st.number_input("Flight Distance", min_value=0, max_value=10000, value=500, step=1)
    inflight_wifi_service = st.slider("Inflight wifi service", min_value=0, max_value=5, value=3, step=1)
    departure_arrival_time_convenient = st.slider("Departure/Arrival time convenient", min_value=0, max_value=5, value=3, step=1)
    ease_of_online_booking = st.slider("Ease of Online booking", min_value=0, max_value=5, value=3, step=1)
    gate_location = st.slider("Gate location", min_value=0, max_value=5, value=3, step=1)
    food_and_drink = st.slider("Food and drink", min_value=0, max_value=5, value=3, step=1)
    online_boarding = st.slider("Online boarding", min_value=0, max_value=5, value=3, step=1)
    seat_comfort = st.slider("Seat comfort", min_value=0, max_value=5, value=3, step=1)
    inflight_entertainment = st.slider("Inflight entertainment", min_value=0, max_value=5, value=3, step=1)
    on_board_service = st.slider("On-board service", min_value=0, max_value=5, value=3, step=1)
    leg_room_service = st.slider("Leg room service", min_value=0, max_value=5, value=3, step=1)
    baggage_handling = st.slider("Baggage handling", min_value=0, max_value=5, value=3, step=1)
    checkin_service = st.slider("Checkin service", min_value=0, max_value=5, value=3, step=1)
    inflight_service = st.slider("Inflight service", min_value=0, max_value=5, value=3, step=1)
    cleanliness = st.slider("Cleanliness", min_value=0, max_value=5, value=3, step=1)
    departure_delay_in_minutes = st.number_input("Departure Delay in Minutes", min_value=0, max_value=1440, value=0, step=1)

    # Map categorical inputs to integers
    features = {
        "Gender": gender_mapping[gender],
        "Customer Type": customer_type_mapping[customer_type],
        "Age": int(age),
        "Type of Travel": type_of_travel_mapping[type_of_travel],
        "Class": class_mapping[class_],
        "Flight Distance": int(flight_distance),
        "Inflight wifi service": int(inflight_wifi_service),
        "Departure/Arrival time convenient": int(departure_arrival_time_convenient),
        "Ease of Online booking": int(ease_of_online_booking),
        "Gate location": int(gate_location),
        "Food and drink": int(food_and_drink),
        "Online boarding": int(online_boarding),
        "Seat comfort": int(seat_comfort),
        "Inflight entertainment": int(inflight_entertainment),
        "On-board service": int(on_board_service),
        "Leg room service": int(leg_room_service),
        "Baggage handling": int(baggage_handling),
        "Checkin service": int(checkin_service),
        "Inflight service": int(inflight_service),
        "Cleanliness": int(cleanliness),
        "Departure Delay in Minutes": int(departure_delay_in_minutes),
    }

    if st.button("Predict"):
      prediction = predict_satisfaction(features)
      if (prediction == 0):
        st.write("Not Satisfied")
      else:
        st.write("Satisfied")

if __name__ == "__main__":
    main()

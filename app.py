import streamlit as st
import pandas as pd
from predictor import predict_health
import re
from datetime import date
from database import (
    create_table,
    add_patient,
    get_patients,
    delete_patient,
    update_patient
)

create_table()
st.title("🏥 HealthPredictAI")
st.markdown(
    "### Healthcare Prediction and Patient Management System"
)

st.header("Patient Health Prediction Form")

full_name = st.text_input("Full Name")
dob = st.date_input(
    "Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)
    
email = st.text_input("Email")

glucose = st.number_input("Glucose", min_value=0.0)
haemoglobin = st.number_input("Haemoglobin", min_value=0.0)
cholesterol = st.number_input("Cholesterol", min_value=0.0)

if st.button("Predict Health Risk"):

    if not full_name.strip():
        st.error("Full Name is required")

    elif not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        st.error("Enter a valid email address")

    else:
        result = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        add_patient(
            full_name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            result
        )

        st.success("Patient record saved successfully!")
        st.success(f"Prediction: {result}")
 
patients = get_patients()       
search_name = st.text_input("🔍 Search Patient by Name")

if search_name:
    patients = [
        patient for patient in patients
        if search_name.lower() in patient[1].lower()
    ]  
st.header("Saved Patient Records")

if patients:
    df = pd.DataFrame(
        patients,
        columns=[
            "ID",
            "Full Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False)

    st.download_button(
        "Download Patient Records",
        csv,
        "patients.csv",
        "text/csv"
    )
else:
    st.info("No patient records found.")
    
st.info("Use the ID shown in the patient records table for Update and Delete operations.")
st.header("Delete Patient Record")
selected_id = st.selectbox(
    "Select Patient ID",
    [patient[0] for patient in patients]
)
if st.button("Delete Record"):
    delete_patient(selected_id)
    st.success("Patient record deleted successfully!")
    st.rerun()
    
st.header("Update Patient Record")

update_id = st.selectbox(
    "Select Patient ID to Update",
    [patient[0] for patient in patients],
    key="update_id"
)

new_name = st.text_input(
    "New Full Name",
    key="new_name"
)

new_dob = st.date_input(
    "New DOB",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key="new_dob"
)

new_email = st.text_input(
    "New Email",
    key="new_email"
)

new_glucose = st.number_input(
    "New Glucose",
    min_value=0.0,
    key="new_glucose"
)

new_haemoglobin = st.number_input(
    "New Haemoglobin",
    min_value=0.0,
    key="new_haemoglobin"
)

new_cholesterol = st.number_input(
    "New Cholesterol",
    min_value=0.0,
    key="new_cholesterol"
)

if st.button("Update Record"):

    new_result = predict_health(
        new_glucose,
        new_haemoglobin,
        new_cholesterol
    )

    update_patient(
        update_id,
        new_name,
        str(new_dob),
        new_email,
        new_glucose,
        new_haemoglobin,
        new_cholesterol,
        new_result
    )

    st.success("Patient updated successfully!")
    st.rerun()
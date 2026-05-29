# HealthPredictAI

## Overview

HealthPredictAI is a Healthcare Prediction and Patient Management System developed using Python, Streamlit, SQLite, and Pandas.

The application allows users to manage patient records and predict possible health risks based on blood test parameters such as Glucose, Haemoglobin, and Cholesterol.

## Features

* Create Patient Records
* View Patient Records
* Update Patient Records
* Delete Patient Records
* Search Patients by Name
* Download Patient Records as CSV
* Email Validation
* Date of Birth Validation
* Health Risk Prediction
* SQLite Database Storage

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas

## Database Fields

* Patient ID
* Full Name
* Date of Birth
* Email
* Glucose
* Haemoglobin
* Cholesterol
* Remarks

## Health Prediction Logic

The system predicts possible health risks using the following rules:

* Glucose > 140 → Possible Diabetes Risk
* Haemoglobin < 12 → Possible Anemia Risk
* Cholesterol > 200 → Possible Heart Disease Risk

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the application

streamlit run app.py

## Project Structure

HealthPredictAI/
├── app.py
├── database.py
├── predictor.py
├── patients.db
├── requirements.txt
└── README.md


## 
#!/usr/bin/env python3
# Save as generate_healthcare_100k.py and run: python generate_healthcare_100k.py
# Requirements: pandas, numpy
# pip install pandas numpy

print("Generating synthetic healthcare datasets with 100,000 records each...")
print("Installing required packages if not already installed...")
print("Packages imported.")
import os
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import json
import zipfile
print("Packages imported successfully.")


random.seed(42)
np.random.seed(42)

OUT_DIR = "healthcare_data"
os.makedirs(OUT_DIR, exist_ok=True)

N = 100_000  # records per dataset

# Helper lists
first_names = ["Aarav","Vivaan","Aditya","Arjun","Isha","Saanvi","Ananya","Priya","Rahul","Kumar","Ravi","Sanjay","Neha","Pooja","Vikram","Meera","Arnav","Kabir","Deepa","Lakshmi"]
last_names = ["Sharma","Patel","Reddy","Khan","Gupta","Singh","Iyer","Das","Bose","Chowdhury","Nair","Menon","Joshi","Kumar","Desai","Rao","Malhotra","Verma","Kapoor","Jain"]
genders = ["Male","Female","Other"]
cities = ["Chennai","Bengaluru","Hyderabad","Mumbai","Delhi","Kolkata","Pune","Jaipur","Ahmedabad","Thiruvananthapuram"]
lab_tests = ["CBC","CMP","Lipid Panel","HbA1c","TSH","Urinalysis","CRP","D-Dimer","COVID-PCR","LFT"]
medicines = ["Paracetamol","Amoxicillin","Metformin","Atorvastatin","Amlodipine","Omeprazole","Cetirizine","Salbutamol","Losartan","Prednisone"]
diagnoses_list = ["Diabetes","Hypertension","Fever","Infection","COPD","Asthma","Cardiac Arrhythmia","UTI","Migraine","Anemia"]

# Patients
patient_ids = [f"P{str(i+1).zfill(8)}" for i in range(N)]
patients = {
    "PatientID": patient_ids,
    "FullName": [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(N)],
    "DOB": [(datetime(1940,1,1) + timedelta(days=random.randint(0,30000))).date().isoformat() for _ in range(N)],
    "Gender": [random.choices(genders, weights=[0.49,0.49,0.02])[0] for _ in range(N)],
    "Mobile": [f"+91{random.randint(6000000000,9999999999)}" for _ in range(N)],
    "Email": [f"user{str(i+1).zfill(8)}@example.com" for i in range(N)],
    "City": [random.choice(cities) for _ in range(N)],
    "RegistrationDate": [(datetime.now() - timedelta(days=random.randint(0,4000))).date().isoformat() for _ in range(N)]
}
df_patients = pd.DataFrame(patients)
df_patients.to_csv(os.path.join(OUT_DIR, "patients_100k.csv"), index=False)

# Lab results
lab = {
    "LabTestID": [f"L{str(i+1).zfill(9)}" for i in range(N)],
    "PatientID": np.random.choice(df_patients["PatientID"], N),
    "TestName": np.random.choice(lab_tests, N),
    "ResultValue": np.round(np.random.uniform(0.1,300.0, N), 2),
    "Unit": np.random.choice(["mg/dL","g/dL","%","IU/L","cells/uL","copies/mL","mMol/L"], N),
    "ResultDate": [(datetime.now() - timedelta(days=random.randint(0,3000))).date().isoformat() for _ in range(N)],
    "LabProvider": np.random.choice(["CityLab","MediLab","HospitalLab","QuickTest"], N)
}
df_lab = pd.DataFrame(lab)
df_lab.to_csv(os.path.join(OUT_DIR, "lab_results_100k.csv"), index=False)

# Prescriptions
presc = {
    "PrescriptionID": [f"RX{str(i+1).zfill(9)}" for i in range(N)],
    "PatientID": np.random.choice(df_patients["PatientID"], N),
    "Medicine": np.random.choice(medicines, N),
    "Dose": np.random.choice(["250 mg","500 mg","5 mg","10 mg","1 tablet","2 tablets"], N),
    "Quantity": np.random.randint(1,60, N),
    "PrescribedDate": [(datetime.now() - timedelta(days=random.randint(0,3000))).date().isoformat() for _ in range(N)],
    "PrescribedBy": np.random.choice(["Dr. Kumar","Dr. Sharma","Dr. Iyer","Dr. Gupta","Dr. Rao","Dr. Singh"], N)
}
df_presc = pd.DataFrame(presc)
df_presc.to_csv(os.path.join(OUT_DIR, "prescriptions_100k.csv"), index=False)

# Billing
billing = {
    "BillingID": [f"B{str(i+1).zfill(10)}" for i in range(N)],
    "PatientID": np.random.choice(df_patients["PatientID"], N),
    "Amount": np.round(np.random.uniform(50.0,100000.0, N),2),
    "BillingDate": [(datetime.now() - timedelta(days=random.randint(0,3000))).date().isoformat() for _ in range(N)],
    "IsPaid": np.random.choice([0,1], N, p=[0.2,0.8]),
    "PaymentMethod": np.random.choice(["Cash","Card","UPI","Insurance"], N),
    "ServiceDescription": np.random.choice(lab_tests + ["Consultation","Room Charges","OT Charges","Imaging"], N)
}
df_billing = pd.DataFrame(billing)
df_billing.to_csv(os.path.join(OUT_DIR, "billing_100k.csv"), index=False)

# Appointments
appointments = {
    "AppointmentID": [f"A{str(i+1).zfill(9)}" for i in range(N)],
    "PatientID": np.random.choice(df_patients["PatientID"], N),
    "DoctorID": np.random.randint(1000,2000, N),
    "AppointmentDate": [(datetime.now() - timedelta(days=random.randint(0,3000))).date().isoformat() for _ in range(N)],
    "Department": np.random.choice(["Cardiology","Neurology","Orthopedics","General Medicine","Dermatology","Pediatrics"], N),
    "Status": np.random.choice(["Scheduled","Completed","Cancelled","No-Show"], N)
}
df_appointments = pd.DataFrame(appointments)
df_appointments.to_csv(os.path.join(OUT_DIR, "appointments_100k.csv"), index=False)

# Diagnosis
diagnosis = {
    "DiagnosisID": [f"D{str(i+1).zfill(9)}" for i in range(N)],
    "PatientID": np.random.choice(df_patients["PatientID"], N),
    "Diagnosis": np.random.choice(diagnoses_list, N),
    "DiagnosisDate": [(datetime.now() - timedelta(days=random.randint(0,3000))).date().isoformat() for _ in range(N)],
    "ICD10Code": np.random.choice(["I10","E11","J45","A09","R50","K35"], N)
}
df_diagnosis = pd.DataFrame(diagnosis)
df_diagnosis.to_csv(os.path.join(OUT_DIR, "diagnosis_100k.csv"), index=False)

# SQL + ADF skeletons
sql_dir = os.path.join(OUT_DIR, "sql_scripts")
os.makedirs(sql_dir, exist_ok=True)
with open(os.path.join(sql_dir, "landing_tables.sql"), "w") as f:
    f.write("-- Landing schema: create tables matching CSV columns\n")
with open(os.path.join(sql_dir, "staging_tables.sql"), "w") as f:
    f.write("-- Staging schema: cleaned data types and constraints\n")
with open(os.path.join(sql_dir, "mart_tables.sql"), "w") as f:
    f.write("-- Mart schema: dims and facts (star schema)\n")

adf_dir = os.path.join(OUT_DIR, "adf")
os.makedirs(adf_dir, exist_ok=True)
pipeline = {
    "name": "CopyAllCSVToLanding",
    "properties": {
        "activities": [
            {"name":"CopyPatients","type":"Copy","inputs":[{"referenceName":"BlobPatients","type":"DatasetReference"}],"outputs":[{"referenceName":"SqlLandingPatients","type":"DatasetReference"}]},
            {"name":"CopyLab","type":"Copy","inputs":[{"referenceName":"BlobLab","type":"DatasetReference"}],"outputs":[{"referenceName":"SqlLandingLab","type":"DatasetReference"}]},
            {"name":"CopyPrescriptions","type":"Copy","inputs":[{"referenceName":"BlobPresc","type":"DatasetReference"}],"outputs":[{"referenceName":"SqlLandingPresc","type":"DatasetReference"}]},
            {"name":"CopyBilling","type":"Copy","inputs":[{"referenceName":"BlobBilling","type":"DatasetReference"}],"outputs":[{"referenceName":"SqlLandingBilling","type":"DatasetReference"}]}
        ]
    }
}
with open(os.path.join(adf_dir, "pipeline_copy_all.json"), "w") as f:
    json.dump(pipeline, f, indent=2)

# Zip
zip_path = os.path.join(OUT_DIR, "healthcare_100k_project.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(OUT_DIR):
        for file in files:
            z.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), OUT_DIR))

print("Done. Files created in:", OUT_DIR)
print("ZIP file:", zip_path)
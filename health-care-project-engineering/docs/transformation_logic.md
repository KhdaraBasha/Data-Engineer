
# Healthcare Data Engineering Project – Transformation Logic

This document explains the transformation rules applied through ADF Dataflows & SQL stored procedures.

---

# 1. Source → Landing (Raw Load)
### Rules:
- No transformation  
- Load as-is from CSV  
- Append mode  
- Metadata fields added:  
  - load_date  
  - filename  

---

# 2. Landing → Staging (Standardization)
### **patients_staging**
- Standardize phone formats → "+91-XXXXX-XXXXX"
- Convert names to Proper Case  
- Validate gender: default to "Unknown"  
- Remove special characters from names  

### **appointments_staging**
- Convert appointment_date to UTC  
- Normalize department names  
- Standardize appointment_status  
- Validate foreign key (invalid patient_ids sent to error table)  

### **diagnosis_staging**
- Convert ICD-10 codes to uppercase  
- Validate severity values  
- Ensure diagnosis_date is not future date  

### **lab_results_staging**
- Convert units to a consistent format  
- Derive result_flag (Normal/High/Low) if missing  
- Validate numeric ranges  

---

# 3. Staging → DataMart (Business Aggregations)

### **mart_patient_summary**
- total_visits = count(appointments.appointment_id)
- total_tests = count(lab_results.test_id)
- critical_conditions = count(severity = ‘Critical’)
- last_visit_date = max(appointments.appointment_date)

### **mart_diagnosis_trends**
- group by diagnosis_code  
- patient_count = distinct patient_id  
- avg_severity_score (Critical=3, Moderate=2, Low=1)  

### **mart_lab_summary**
- group by patient_id, test_type  
- avg_result_value  
- last_test_date  

---

# 4. Error Handling Logic
- Invalid patient_id → error_patient_fk  
- Future dates → error_future_dates  
- Invalid numeric values → error_range_check  
- Duplicates → error_duplicates  

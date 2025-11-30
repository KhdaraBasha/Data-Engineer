
# Healthcare Data Engineering Project – Data Quality & Performance Metrics

This document defines the KPIs and metrics tracked across the end-to-end data pipeline.

---

## 1. Data Quality Metrics

### **1.1 Completeness**
- % of non-null patient demographic fields  
- % of appointment records with valid patient_id  
- % of diagnosis records with assigned ICD-10 code  
- % of lab_result records with measurement values

### **1.2 Accuracy**
- Valid formats (email, phone number, dob)
- Valid numeric ranges (blood pressure, glucose, BMI)
- Valid date ranges (no future dates for visits)
- Consistent primary key / foreign key mappings

### **1.3 Uniqueness**
- Duplicate patient entries  
- Duplicate appointments  
- Duplicate lab results  
- Duplicate diagnosis codes

### **1.4 Timeliness**
- Latency from source → ADLS
- Latency from ADLS → SQL Landing
- Latency from SQL Landing → Mart
- End-to-end pipeline refresh time

### **1.5 Consistency**
- Patient profile consistent across CSV sources  
- Unified dimensional keys across marts  
- Correct transformation rules applied  

---

## 2. Pipeline Performance Metrics

### **2.1 ADF Pipeline Metrics**
- Pipeline runtime  
- Dataflow runtime  
- Throughput (rows/sec)  
- Copy activity throughput  
- Number of failures / month  
- Retries count  

### **2.2 SQL Database Metrics**
- Query performance (avg execution time)
- Staging → Mart load time
- Index usage efficiency
- Deadlocks or blocked queries count  

### **2.3 Power BI Metrics**
- Data refresh time  
- DAX query execution time  
- Dashboard load time  

---

## 3. Business KPIs

### **3.1 Patient Engagement**
- Active patients  
- Visits per patient  
- App usage insights  

### **3.2 Healthcare Utilization**
- Appointment no-show rate  
- Avg diagnosis per patient  
- Avg lab tests per patient  

### **3.3 Operational KPIs**
- Data processing success rate  
- Data availability SLA  
- System uptime  



# Healthcare Data Engineering Project – Full Project Plan

---

# Phase 1: Requirements & Architecture Design
### Deliverables:
- Architecture diagram  
- Data dictionary  
- Data quality framework  
- Azure resource plan  

Timeline: **2 days**

---

# Phase 2: Azure Environment Setup
### Tasks:
- Create Resource Group  
- Deploy ADF  
- Deploy Azure SQL DB  
- Deploy Data Lake Gen2 (raw, staging, mart containers)  
- Create Key Vault  

Timeline: **1 day**

---

# Phase 3: Data Generation (100,000 rows each)
### Tables:
- patients  
- appointments  
- diagnosis  
- lab_results  

### Deliverables:
- Synthetic data generator notebook  
- CSV files uploaded to ADLS  

Timeline: **1 day**

---

# Phase 4: Ingestion Pipelines (Source → ADLS → SQL Landing)
### Tasks:
- Create ADF linked services  
- Create datasets (CSV/ADLS/SQL)  
- Build Copy Activity pipelines  
- Add metadata logging  

Timeline: **2 days**

---

# Phase 5: Transformation Pipelines (ADF Dataflows + SQL)
### Tasks:
- ADLS Raw → SQL Landing  
- SQL Landing → SQL Staging transformations  
- Error handling tables  
- Slowly changing dimension rules  

Timeline: **3 days**

---

# Phase 6: DataMart Development
### Deliverables:
- mart_patient_summary  
- mart_diagnosis_trends  
- mart_lab_summary  
- mart_appointments  

Timeline: **2 days**

---

# Phase 7: Power BI Dashboard
### KPI Pages:
- Patient overview  
- Diagnoses trends  
- Lab summary  
- Hospital utilization metrics  

Timeline: **2 days**

---

# Phase 8: Documentation & GitHub Packaging
### Output:
- README.md  
- Architecture PNG  
- metrics.md  
- transformation_logic.md  
- data_dictionary.md  
- project_plan.md  
- Pipeline JSON templates  

Timeline: **1 day**

---

# Total Project Duration: **14 days**  

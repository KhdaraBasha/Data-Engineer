
# Healthcare Data Engineering Project – Data Dictionary

This document defines tables and fields used in the Healthcare Data Engineering Solution.

---

# 1. patients
|----------------|----------|----------------------|
| Column         | Type     | Description          |
|----------------|----------|----------------------|
| patient_id     | INT      | Unique identifier    |
| first_name     | VARCHAR  | Patient first name   |
| last_name      | VARCHAR  | Patient last name    |
| age            | INT      | Age of patient       |
| gender         | VARCHAR  | Male/Female/Other    |
| contact_number | VARCHAR  | Mobile number        |
| email          | VARCHAR  | Patient email        |
| city           | VARCHAR  | City of residence    |
| created_date   | DATETIME | Record creation date |
|----------------|----------|----------------------|

# 2. appointments
|---------------------|-------------|-----------------------------------|
| Column              | Type      	| Description 						|
|---------------------|-------------|-----------------------------------|
| appointment_id      | INT 		| Unique appointment record 		|
| patient_id          | INT 		| Linked to patients table 			|
| appointment_date    | DATETIME 	| Scheduled visit date 				|
| department          | VARCHAR 	| Department name 					|
| doctor              | VARCHAR 	| Assigned doctor 					|
| appointment_status  | VARCHAR 	| Completed / No-Show / Cancelled 	|
| created_date        | DATETIME 	| Record creation timestamp 		|
|---------------------|-------------|-----------------------------------|

# 3. diagnosis
|-----------------------|---------------|-----------------------------------|
| Column 				| Type 			| Description 						|
|-----------------------|---------------|-----------------------------------|
| diagnosis_id 			| INT 			| Unique ID 						|
| patient_id 			| INT 			| Linked to patients table 			|
| diagnosis_code 		| VARCHAR 		| ICD-10 code 						|
| diagnosis_description | VARCHAR 		| Medical condition 				|
| diagnosis_date 		| DATETIME 		| Date of diagnosis 				|
| severity 				| VARCHAR 		| Low / Moderate / Critical 		|
|-----------------------|---------------|-----------------------------------|

# 4. lab_results
|-----------------------|---------------|-----------------------------------|
| Column 				| Type 			| Description 						|
|-----------------------|---------------|-----------------------------------|
| test_id 				| INT 			| Unique ID 						|
| patient_id 			| INT 			| Linked to patients table 			|
| test_type 			| VARCHAR 		| Blood, Urine, X-Ray, etc. 		|
| test_name 			| VARCHAR 		| Glucose, CBC, Sodium, etc. 		|
| result_value 			| VARCHAR 		| Result numeric value 				|
| unit 					| VARCHAR 		| mg/dL, mmol/L 					|
| result_flag 			| VARCHAR 		| Normal / High / Low 				|
| test_date 			| DATETIME 		| Date of test 						|
|-----------------------|---------------|-----------------------------------|

# 5. mart_patient_summary
|-----------------------|---------------|-----------------------------------|
| Column 				| Type 			| Description 						|
|-----------------------|---------------|-----------------------------------|
| patient_id 			| INT 			| Key 								|
| total_visits 			| INT 			| Count of appointments 			|
| total_tests 			| INT 			| Count of lab tests 				|
| critical_conditions 	| INT 			| Count of severe diagnoses 		|
| last_visit_date 		| DATETIME 		| Most recent appointment 			|
|-----------------------|---------------|-----------------------------------|
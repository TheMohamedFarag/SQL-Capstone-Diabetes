# DEPI SQL Capstone Project: UCI Diabetes Feature Store

## Project Overview
This project delivers an enterprise-grade Feature Store pipeline built for the UCI Diabetes dataset using PostgreSQL as the core database engine and Python strictly for workflow orchestration (adhering strictly to the Anti-Pandas Mandate).

The mandatory target variable constructed in this pipeline is readmitted_within_30_days (Binary: 1 if readmitted in <30 days, 0 otherwise).

## Repository Architecture
depi-sql-capstone-diabetes/
├── README.md                  # Documentation & Data Dictionary
├── requirements.txt           # Minimal Python Dependencies
├── config.py                  # Database connection module
├── main.py                    # Interactive CLI Interface
├── etl.py                     # Master Orchestrator Pipeline
│
├── scripts/                   # Python execution scripts
│   ├── phase1.py              # Business Understanding
│   ├── phase2.py              # Data Understanding & Quality Audit
│   └── phase3.py              # Data Preparation & Feature Store Creation
│
├── sql/                       # Pure SQL queries
│   ├── audit_queries.sql      # Data Quality & Baseline queries
│   └── feature_store.sql      # DDL View Creation for Feature Store
│
└── outputs/                   # Generated Artifacts
    ├── phase2_eda_summary.csv
    ├── phase2_quality_audit.csv
    └── feature_store_export.csv

## How to Run

1. Configure Environment Variables:
Create a .env file in the root directory:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=UCI_create_scripts
DB_USER=postgres
DB_PASSWORD=your_password

2. Install Dependencies:
python -m pip install -r requirements.txt

3. Run the Complete Pipeline:
python main.py --phase all

Or run individual phases:
python main.py --phase 1
python main.py --phase 2
python main.py --phase 3

## Data Dictionary (Feature Store View)

| Column Name | Data Type | Description |
|---|---|---|
| patient_nbr | INTEGER | Unique identifier for each patient |
| encounter_id | INTEGER | Unique identifier for each clinical encounter |
| admission_type_id | INTEGER | Identifies admission type (e.g., Emergency, Urgent) |
| discharge_disposition_id | INTEGER | Discharge disposition identifier |
| admission_source_id | INTEGER | Admission source identifier |
| time_in_hospital | INTEGER | Length of stay in days |
| clean_medical_specialty | TEXT | Imputed medical specialty of the admitting physician |
| num_lab_procedures | INTEGER | Number of lab tests performed during the encounter |
| num_procedures | INTEGER | Number of non-lab procedures performed |
| num_medications | INTEGER | Number of distinct medications administered |
| number_outpatient | INTEGER | Number of outpatient visits in the year preceding the encounter |
| number_emergency | INTEGER | Number of emergency visits in the year preceding the encounter |
| number_inpatient | INTEGER | Number of inpatient visits in the year preceding the encounter |
| number_diagnoses | INTEGER | Number of diagnoses entered into the system |
| readmitted_within_30_days | INTEGER | TARGET VARIABLE: 1 if readmitted in <30 days, 0 otherwise |
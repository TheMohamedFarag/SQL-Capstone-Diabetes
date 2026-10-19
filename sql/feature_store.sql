CREATE OR REPLACE VIEW feature_store AS
SELECT 
    p.patient_nbr,
    a.encounter_id,
    a.admission_type_id,
    a.discharge_disposition_id,
    a.admission_source_id,
    a.time_in_hospital,
    
    COALESCE(
        CASE WHEN a.medical_specialty = '?' THEN 'Unknown' ELSE a.medical_specialty END, 
        'Unknown'
    ) AS clean_medical_specialty,
    
    a.num_lab_procedures,
    a.num_procedures,
    a.num_medications,
    a.number_outpatient,
    a.number_emergency,
    a.number_inpatient,
    a.number_diagnoses,
    
    CASE 
        WHEN a.readmitted = '<30' THEN 1 
        ELSE 0 
    END AS readmitted_within_30_days

FROM admissions a
JOIN patients p ON a.patient_nbr = p.patient_nbr
LEFT JOIN medical_details m ON a.encounter_id = m.encounter_id;
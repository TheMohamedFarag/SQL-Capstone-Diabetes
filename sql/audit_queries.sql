-- 1. Baseline record counts
SELECT 'patients' AS table_name, COUNT(*) AS total_records FROM patients
UNION ALL
SELECT 'admissions', COUNT(*) FROM admissions
UNION ALL
SELECT 'medical_details', COUNT(*) FROM medical_details;

-- 2. Check missing values in medical_details
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN payer_code IS NULL OR payer_code = '?' THEN 1 ELSE 0 END) AS missing_payer_code,
    SUM(CASE WHEN medical_specialty IS NULL OR medical_specialty = '?' THEN 1 ELSE 0 END) AS missing_medical_specialty,
    SUM(CASE WHEN diag_1 IS NULL OR diag_1 = '?' THEN 1 ELSE 0 END) AS missing_diag_1
FROM medical_details;
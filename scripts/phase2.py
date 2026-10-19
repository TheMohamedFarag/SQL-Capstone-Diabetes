import sys
import os
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_db_connection

def run_phase2():
    print("=" * 60)
    print("Starting Phase 2: Data Understanding & EDA Audit")
    print("=" * 60)
    
    os.makedirs("outputs", exist_ok=True)
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 1. Summary EDA (Record Counts)
        cursor.execute("""
            SELECT 'patients' AS table_name, COUNT(*) AS total_records FROM patients
            UNION ALL
            SELECT 'admissions', COUNT(*) FROM admissions
            UNION ALL
            SELECT 'medical_details', COUNT(*) FROM medical_details;
        """)
        summary_rows = cursor.fetchall()
        
        summary_file = os.path.join("outputs", "phase2_eda_summary.csv")
        with open(summary_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["table_name", "total_records"])
            writer.writerows(summary_rows)
        print(f" Saved: {summary_file}")
        
        # 2. Get actual columns of medical_details
        cursor.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = 'medical_details';
        """)
        columns = [row[0] for row in cursor.fetchall()]
        
        # Build dynamic SQL query for Quality Audit
        audit_selects = ["COUNT(*) AS total_rows"]
        for col in columns:
            audit_selects.append(
                f"SUM(CASE WHEN {col}::text IS NULL OR {col}::text = '?' OR {col}::text = '' THEN 1 ELSE 0 END) AS missing_{col}"
            )
            
        audit_query = f"SELECT {', '.join(audit_selects)} FROM medical_details;"
        cursor.execute(audit_query)
        audit_row = cursor.fetchone()
        
        # Column names for CSV output
        audit_headers = ["total_rows"] + [f"missing_{col}" for col in columns]
        
        audit_file = os.path.join("outputs", "phase2_quality_audit.csv")
        with open(audit_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(audit_headers)
            writer.writerow(audit_row)
        print(f" Saved: {audit_file}")
        
        cursor.close()
        conn.close()
        print("\nPhase 2 Completed Successfully!")
        return True
    except Exception as e:
        print(f"Phase 2 Execution Failed: {e}")
        return False

if __name__ == "__main__":
    run_phase2()
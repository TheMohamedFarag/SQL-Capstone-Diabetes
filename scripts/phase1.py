import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_db_connection

def run_phase1():
    print("=" * 60)
    print("Starting Phase 1: Business Understanding")
    print("=" * 60)
    
    objectives = {
        "Domain": "Healthcare Analytics & Clinical Readmissions",
        "Mandatory Target": "readmitted_within_30_days (Binary: 1 if <30 days, else 0)",
        "Pipeline Latency Goal": "< 2.0 Seconds",
        "Data Hygiene Metrics": "0% Duplicate Encounters, 100% Imputed Missing Identifiers"
    }
    
    print("\nProject Objectives & Targets:")
    for key, val in objectives.items():
        print(f"  * {key}: {val}")
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT current_database(), current_user;")
        db_info = cursor.fetchone()
        
        print("\nDatabase Connection Verified:")
        print(f"  * Database: {db_info[0]}")
        print(f"  * User: {db_info[1]}")
        
        cursor.close()
        conn.close()
        print("\nPhase 1 Completed Successfully!")
        return True
    except Exception as e:
        print(f"Phase 1 Execution Failed: {e}")
        return False

if __name__ == "__main__":
    run_phase1()
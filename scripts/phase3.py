import sys
import os
import csv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_db_connection

def run_phase3():
    print("=" * 60)
    print("Starting Phase 3: Data Preparation & Feature Store Creation")
    print("=" * 60)
    
    os.makedirs("outputs", exist_ok=True)
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql_file_path = os.path.join("sql", "feature_store.sql")
        with open(sql_file_path, "r", encoding="utf-8") as f:
            feature_store_sql = f.read()
            
        cursor.execute(feature_store_sql)
        conn.commit()
        print(" Created View: feature_store in PostgreSQL")
        
        cursor.execute("SELECT * FROM feature_store;")
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        
        export_file = os.path.join("outputs", "feature_store_export.csv")
        with open(export_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(colnames)
            writer.writerows(rows)
            
        print(f" Saved Final Dataset: {export_file} ({len(rows)} records)")
        
        cursor.close()
        conn.close()
        print("\nPhase 3 Completed Successfully!")
        return True
    except Exception as e:
        print(f"Phase 3 Execution Failed: {e}")
        return False

if __name__ == "__main__":
    run_phase3()
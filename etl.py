import sys
import os

from scripts.phase1 import run_phase1
from scripts.phase2 import run_phase2
from scripts.phase3 import run_phase3

def run_pipeline():
    print("=" * 60)
    print("🚀 Starting Complete DEPI SQL Capstone ETL Pipeline")
    print("=" * 60)
    
    # Run Phase 1
    p1_success = run_phase1()
    if not p1_success:
        print("❌ Pipeline aborted at Phase 1")
        return False
        
    print("\n")
    # Run Phase 2
    p2_success = run_phase2()
    if not p2_success:
        print("❌ Pipeline aborted at Phase 2")
        return False
        
    print("\n")
    # Run Phase 3
    p3_success = run_phase3()
    if not p3_success:
        print("❌ Pipeline aborted at Phase 3")
        return False
        
    print("\n" + "=" * 60)
    print("🎉 ETL Pipeline Completed Successfully!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    run_pipeline()
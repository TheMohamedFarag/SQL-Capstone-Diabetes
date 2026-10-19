import sys
import argparse
from etl import run_pipeline
from scripts.phase1 import run_phase1
from scripts.phase2 import run_phase2
from scripts.phase3 import run_phase3

def main():
    parser = argparse.ArgumentParser(description="DEPI SQL Capstone Pipeline CLI")
    parser.add_argument(
        "--phase", 
        type=str, 
        choices=["1", "2", "3", "all"], 
        default="all",
        help="Specify which phase to run: 1, 2, 3, or all"
    )
    
    args = parser.parse_args()
    
    if args.phase == "1":
        run_phase1()
    elif args.phase == "2":
        run_phase2()
    elif args.phase == "3":
        run_phase3()
    else:
        run_pipeline()

if __name__ == "__main__":
    main()
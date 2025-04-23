import sys
from subprocess import run, DEVNULL

ANALYSIS_DIR = "/adaqfs/home/a-molana/halla_molana/moller_analysis"

def analyze_run(r, quiet=False):
    cmd = f'cd {ANALYSIS_DIR} && ./run_molana_analysis.sh -r {r}'
    run(cmd, shell=True,
        stdout=DEVNULL if quiet else None,
        stderr=DEVNULL if quiet else None)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_run.py <run_number>")
        sys.exit(1)
    try:
        run_number = int(sys.argv[1])
    except ValueError:
        print("Run number must be an integer.")
        sys.exit(1)
    analyze_run(run_number)
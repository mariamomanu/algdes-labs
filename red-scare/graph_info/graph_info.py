import sys

from constants import DATA_DIR
import os

if __name__ == "__main__":
    assert os.getcwd().split("/")[-1] == "red-scare", "Working directory must be red-scare"

    TIMEOUT = 5  # seconds

    # List of input files. Get all files in directory
    input_files = sorted([os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                          if os.path.isfile(os.path.join(DATA_DIR, f)) and f.endswith('.txt')])
    assert input_files, "No input files found in data directory"

    for input_file_path in input_files:
        filename = os.path.basename(input_file_path)
        direction_set = set()
        with open(input_file_path, "r") as f:
            # Read the first line containing n, m, and _
            temp = f.readline().strip().split()
            n, m, r = map(int, temp)

            with open("graph_r.txt", "a") as graph_file:
                graph_file.write(f"{filename} {r}\n")
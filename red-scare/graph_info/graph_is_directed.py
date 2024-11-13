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
            n, m, _ = map(int, temp)

            # Read the line containing source and target names (assuming you need to read it)
            f.readline().strip().split()

            # Read n lines for nodes
            for i in range(n):
                f.readline().strip().split()

            # Read m lines for edges and collect directions
            for _ in range(m):
                _, direction, _ = f.readline().strip().split()
                direction_set.add(direction)

            assert len(direction_set) <= 1
            print(direction_set)
            print(f"{filename} {"yes" if direction_set == {"->"} else 'no'}")
            with open("is_directed.txt", "a") as graph_file:
                graph_file.write(f"{filename} {"yes" if direction_set == {"->"} else 'no'}\n")

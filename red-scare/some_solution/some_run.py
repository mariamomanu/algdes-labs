import subprocess
import os
import time

from constants import DATA_DIR, RESULTS_DIR, SOME_DIR

if __name__ == "__main__":
    assert os.getcwd().split("/")[-1] == "red-scare", "Working directory must be red-scare"

    # One hour
    TIMEOUT = 3600  # seconds

    # List of input files. Get all files in directory
    input_files = sorted([os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                          if os.path.isfile(os.path.join(DATA_DIR, f)) and f.endswith(
            '.txt')])
    assert input_files, "No input files found in data directory"

    # Get set of results file names from the results directory
    result_exists = set()
    with open(RESULTS_DIR / "some.txt", "r") as results:
        for line in results:
            result_exists.add(line.split()[0])

    # # Delete existing results file
    # if os.path.exists(RESULTS_DIR / "some.txt"):
    #     os.remove(RESULTS_DIR / "some.txt")

    output_file = RESULTS_DIR / "some.txt"
    batch_start = time.time()
    for input_file_path in input_files:
        result = None
        input_filename = input_file_path.split("/")[-1]
        if input_filename in result_exists:
            print(f"Skipping {input_filename}")
            continue
        print(f"Processing {input_filename}")

        # Run the script with the input file and capture the output
        run_start = time.time()
        try:
            process = subprocess.run(
                ["python", SOME_DIR / "some.py"],
                input=open(DATA_DIR / input_filename).read(),
                text=True,
                capture_output=True,
                timeout=TIMEOUT
            )
            # Check for process return code inside the try block to avoid issues if an exception is raised
            if process.returncode == 0:
                result = process.stdout.strip()
            else:
                # Strip out traceback from stderr and log only the last line of the error message
                result = process.stderr.splitlines()[
                    -1] if process.stderr else "Unknown error"
        except subprocess.TimeoutExpired:
            result = f"Timeout_{TIMEOUT}_s"

        print("\t"+result)
        print(f"\t{time.time() - run_start:.2f} seconds")
        # Write the filename and result to the output file
        with open(output_file, "a") as results:
            results.write(f"{input_filename} {result}\n")

    print(f"Batch completed in {time.time() - batch_start:.2f} seconds")
    print(f"Results saved to {RESULTS_DIR}")

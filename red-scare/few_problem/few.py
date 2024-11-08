import os

def read_files(directory, initial_string=None):
    """
    Reads files from a given directory.
    If an initial_string is provided, reads only files that start with that string.
    
    Args:
    - directory (str): Path to the directory containing the files.
    - initial_string (str): Optional. If provided, only files starting with this string will be read.
    
    Returns:
    - dict: A dictionary with filenames as keys and file contents as values.
    """
    file_contents = {}
    
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        # Check if it's a file and matches the initial_string (if provided)
        if os.path.isfile(os.path.join(directory, filename)):
            if initial_string is None or filename.startswith(initial_string):
                # Read and store the contents
                with open(os.path.join(directory, filename), 'r') as file:
                    file_contents[filename] = file.read()
    
    return file_contents

# Example usage
directory = "red-scare\data"  # Replace with your actual path
initial_string = "common-1-"  # Replace with initial string to filter, or set to None to read all

# Read files
files_data = read_files(directory, initial_string)

# Print results (for verification)
for filename, content in files_data.items():
    print(f"Filename: {filename}")
    print(f"Content: {content[:100]}")  # Print the first 100 characters to avoid too much output
    print("-" * 40)

n, m, r = map(int, input().strip().split())
start, terminal = input().split()
V = []
R = []
for i in range (n):
    temp = input()
    if ("*" in temp):
        R.append(temp.split[0])
    else:
        V.append(temp)

print(R)

adjacency_list = [[] for _ in V]

for i in range (m):
    u, direction, v = input.split()
    if (u in R or v in R):
        continue

    add_edge(adjacency_list, u, v)

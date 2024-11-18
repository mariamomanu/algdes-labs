import os
from few_graph import Graph
import sys

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
    
    # Debugging: Confirm the directory path and initial_string
    print(f"Reading from directory: {directory}")
    print(f"Initial string for filtering: {initial_string} (type: {type(initial_string)})")
    
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it's a file and matches the initial_string (if provided)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Debugging: Check if the file matches the condition
            matches_condition = initial_string is None or filename.startswith(initial_string)
            print(f"Checking file: {filename} | Matches condition: {matches_condition}")
            
            if matches_condition:
                # Read and store the contents
                print(f"Reading file: {filename}")  # Debugging filename
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content (first 100 chars): {content[:100]}")  # Debugging content preview
                    file_contents[filename] = content
    
    # Debugging: Print out the dictionary of file contents
    print("File contents dictionary keys:", list(file_contents.keys()))
    return file_contents


# # Print results (for verification)
# for filename, content in files_data.items():
#     print(f"Filename: {filename}")
#     print(f"Content: {content[:100]}")  # Print the first 100 characters to avoid too much output
#     print("-" * 40)


def input_handling_for_few(file_content):
    lines = file_content.splitlines()
    # n, m, r = map(int, input().strip().split())
    # start, terminal = input().split()
    n, m, r = map(int, lines[0].strip().split())
    n_lines_start_at = 2
    m_lines_start_at = n_lines_start_at+n
    start, terminal = lines[1].split()

    V = []
    R = []
# Vertices processing
    for i in range (n_lines_start_at, n_lines_start_at+n):
        temp = lines[i]
        if ("*" in temp):
            R.append(temp.split()[0])
        else:
            V.append(temp)
    print(R)

    # # Debugging output for verification
    # print(f"R: {R}")
    # print(f"V: {V}")

    adjacency_list_vertices = {}
    # Edges processing
    for i in range (m_lines_start_at, m_lines_start_at+m):
        u, direction, v = lines[i].split()
            
        if (u not in adjacency_list_vertices):
            adjacency_list_vertices[u] = []
        adjacency_list_vertices[u].append((u, direction, v))

    # Debugging output for verification
    print(f"Adjacency list V: {adjacency_list_vertices}")


    return V, R, adjacency_list_vertices


def dijsktra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.getnodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        unvisited_nodes.remove = current_min_node
    return previous_nodes, shortest_path

def print_results (previous_nodes, shortest_path, start_node, terminal_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print("found the path with fewest red nodes with a value of:".format(shortest_path[terminal_node]))
    print("->".join(reversed(path)))

def main():
    directory = "red-scare\instance-generators\handmade"  # Replace with your actual path
    initial_string = "G-ex"  # Set to None to read all files
    files_data = read_files(directory, initial_string)
    # Process files
    for filename, content in files_data.items():
        print(f"Processing file: {filename}")
        
        # 1. Input handling for the file (reading, parsing, etc.)
        V, R, adjacency_list_V, adjacency_list_R, adjacency_list_V_R = input_handling_for_few(content)
        
        # 2. Running the algorithm
        # few_dijkstra_logic(V, R, adjacency_list_V, adjacency_list_R, adjacency_list_V_R)
        Graph.construct_graph()
    
    


if __name__ == '__main__':
    main()
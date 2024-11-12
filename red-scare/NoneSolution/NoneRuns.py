import os
from collections import deque, defaultdict
# implementation from https://celerdata.com/glossary/breadth-first-search-bfs and https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
# BFS shortest path function
def BFS_SP(graph, start, goal, output_file):
    explored = []
    queue = [[start]]
    
    if start == goal:
        output_file.write("Same Node\n")
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    output_file.write(f"{len(new_path) - 1}\n")
                    return
            explored.append(node)
    
    output_file.write("-1\n")
    return

# Function to process a single file and write to output file object
def process_file(file_path, output_file):
    with open(file_path, 'r') as file:
        # Parsing input from file
        n, m, r = map(int, file.readline().strip().split())
        start, end = file.readline().strip().split()
        
        V = []
        R = []
        
        for _ in range(n):
            temp = file.readline().strip()
            if ("*" in temp and (temp.split(" ")[0]!= end and temp.split(" ")[0]!= start)):
                R.append(temp.split(" ")[0])
            else:
                V.append(temp)
        
        graph = defaultdict(list)
        
        for _ in range(m):
            u, direction, v = file.readline().strip().split()
            if u in R or v in R:
                continue
            
            match direction:
                case "--":
                    graph[u].append(v)
                    graph[v].append(u)
                case "->":
                    graph[u].append(v)
                #case "<-":
                 #   graph[v].append(u)
        
        # Run BFS on the parsed graph and write output
        BFS_SP(graph, start, end, output_file)

# Directory containing input files
data_dir = "./data"
combined_output_path = "./NoneSolution/answers.txt"
os.makedirs(os.path.dirname(combined_output_path), exist_ok=True)  # Ensure output directory exists

with open(combined_output_path, 'w') as combined_output:
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_dir, filename)
            combined_output.write(f"{filename}: ")
            process_file(file_path, combined_output)
            #combined_output.write("\n")  # Separate each file's output with a newline

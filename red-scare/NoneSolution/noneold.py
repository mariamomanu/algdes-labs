import os
from collections import deque, defaultdict

# BFS shortest path function
def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    
    if start == goal:
        print("Same Node")
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
                    print(len(new_path) - 1)
                    return
            explored.append(node)
    
    print(-1)
    return

# Function to process a single file
def process_file(file_path):
    with open(file_path, 'r') as file:
        # Parsing input from file
        n, m, r = map(int, file.readline().strip().split())
        start, end = file.readline().strip().split()
        
        V = []
        R = []
        
        for _ in range(n):
            temp = file.readline().strip()
            if "*" in temp:
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
                case "<-":
                    graph[v].append(u)
        
        # Run BFS on the parsed graph
        BFS_SP(graph, start, end)

# Directory containing input files
data_dir = "./data"

# Loop through each file in the directory
for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(data_dir, filename)
        print(f"Processing {filename}")
        process_file(file_path)




import os
import networkx as nx

from constants import DATA_DIR

def build_graph(edges, is_directed):
    # Choose Graph type based on direction
    G = nx.DiGraph() if is_directed else nx.Graph()

    # Add edges based on direction
    for u, direction, v in edges:
        if direction == "--":  # Undirected edge
            G.add_edge(u, v)
        elif direction == "->":  # Directed edge
            G.add_edge(u, v)

    return G


def has_cycle(G, is_directed):
    try:
        if is_directed:
            # Find a cycle in a directed graph
            cycle = nx.find_cycle(G, orientation='original')
            return True, cycle
        else:
            # For undirected graph, check if there's any cycle basis
            cycle_basis = nx.cycle_basis(G)
            return (len(cycle_basis) > 0), cycle_basis
    except nx.NetworkXNoCycle:
        return False, None


if __name__ == "__main__":
    assert os.getcwd().split("/")[
               -1] == "red-scare", "Working directory must be red-scare"

    # List of input files. Get all files in directory
    input_files = sorted([os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                          if os.path.isfile(os.path.join(DATA_DIR, f)) and f.endswith(
            '.txt')])
    assert input_files, "No input files found in data directory"

    for input_file_path in input_files:
        filename = os.path.basename(input_file_path)
        direction_set = set()
        with open(input_file_path, "r") as f:
            # Read graph structure
            temp = f.readline().strip().split()
            n, m, _ = map(int, temp)
            f.readline()  # Read source and target names line

            # Read node data
            for i in range(n):
                f.readline().strip().split()

            # Collect edges and determine if the graph is directed
            edges = []
            for _ in range(m):
                u, direction, v = f.readline().strip().split()
                edges.append((u, direction, v))
                direction_set.add(direction)

            # Determine if the graph is directed
            is_directed = "->" in direction_set

            # Build and check for cycles
            G = build_graph(edges, is_directed)
            cycle_exists, cycle_info = has_cycle(G, is_directed)

            # Output results
            print(f"{filename} has cycle: {cycle_exists}")

            with open("cycle_info.txt", "a") as cycle_file:
                cycle_file.write(f"{filename} {"yes" if cycle_exists else "no"}\n")
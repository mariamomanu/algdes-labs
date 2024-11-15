import dataclasses

from bellman_ford import bellman_ford

"""
Pseudo code:
    Read through the input vertices.
    Store all in a name to vertexID mapping.
    If vertex is red then store in red node set
    Create an adjacency matrix with the number of vertices.
    Iterate through the edges and add to the adjacency matrix.
    If direction is "-->" then:
        Add vertices to a vertex weight list. If edge ends in a red node then weight is 1 else 0.
        return bellman_ford to find the heaviest path from source to all nodes.
    else:
        not supported
"""
import sys


def preprocess_graph(adj_matrix, red_nodes, is_directed):
    num_nodes = len(adj_matrix)
    modified_adj_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u][v] == 1:
                if red_nodes[v] == 1:
                    modified_adj_matrix[u][v] = -1  # -1 for edges to red nodes
                else:
                    modified_adj_matrix[u][v] = 0  # Normal weight for other edges
                # If undirected, set the reverse edge
                if not is_directed:
                    if red_nodes[u] == 1:
                        modified_adj_matrix[v][u] = -1 # -1 for edges to red nodes
                    else:
                        modified_adj_matrix[v][u] = 0 # Normal weight for other edges
    return modified_adj_matrix

def build_adj_matrix(source_name, target_name):
    adj_matrix = [[0] * (n) for _ in range(n)]
    red_nodes, name_vertex_map = [0] * n, {}
    for i in range(n):
        temp = sys.stdin.readline().split()
        if temp[-1] == "*":
            red_nodes[i] = 1
        name_vertex_map[temp[0]] = i

    source, target = name_vertex_map[source_name], name_vertex_map[target_name]

    is_directed = False
    for i in range(m):
        u, direction, v = input().split()
        if direction == "--":
            adj_matrix[name_vertex_map[u]][name_vertex_map[v]] = 1
            adj_matrix[name_vertex_map[v]][name_vertex_map[u]] = 1
        elif direction == "->":
            is_directed = True
            adj_matrix[name_vertex_map[u]][name_vertex_map[v]] = 1
        elif direction == "<-":
            raise NotImplementedError("This direction is not supported")
    return adj_matrix, red_nodes, is_directed, source, target

if __name__ == "__main__":
    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    source_name, target_name = sys.stdin.readline().split()

    adj_matrix, red_nodes, is_directed, source, target = build_adj_matrix(source_name, target_name)

    mod_adj_matrix = preprocess_graph(adj_matrix, red_nodes, is_directed)

    result = bellman_ford(mod_adj_matrix, source, target)
    print(result)

    exit(0)




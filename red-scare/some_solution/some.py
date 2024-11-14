import copy

from edmonds_karp import EdmondsKarp
from ford_fulkerson import ford_fulkerson

"""
Pseudo code:
    Read through the input vertices.
    Store all in a name to vertexID mapping.
    If vertex is red then store in red list.
    Create an adjacency matrix with the number of vertices.
    Iterate through the edges and add to the adjacency matrix.
    If "--" then both directions are added.
    Connect s and t to super sink with edge weights of 1
    while red vertex list is not empty:
        Pop red vertex from the list and connect to super source with edge weight of 2
        Run Ford Fulkerson to find the max flow between super source and super sink.
        If max_flow = 2 then return true
    return false
"""
import sys

# Example usage
if __name__ == "__main__":

    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    adj_matrix = [[0] * (n + 2) for _ in range(n + 2)]  # n + 2 for super source and super sink
    source_name, target_name = sys.stdin.readline().split()

    red_nodes, name_vertex_map = [], {}
    for i in range(n):
        temp = sys.stdin.readline().split()
        if temp[-1] == "*":
            red_nodes.append(i)
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

    if is_directed:
        # If Many algorithm returns greater than zero then return True
        print("many_algorithm")
        exit(0)

    super_source, super_sink = n, n + 1
    adj_matrix[source][super_sink] = 1
    adj_matrix[target][super_sink] = 1
    while red_nodes:
        red_node = red_nodes.pop()
        adj_matrix_copy = copy.deepcopy(adj_matrix)  # Make a deep copy
        adj_matrix_copy[super_source][red_node] = 2
        try:
            edmonds_karp = EdmondsKarp(adj_matrix_copy)
            max_flow, _ = edmonds_karp.run(super_source, super_sink)
            # max_flow = ford_fulkerson(adj_matrix_copy, super_source, super_sink)
        except RecursionError:
            print("RecursionError")
            exit(0)
        if max_flow == 2:
            print("True")
            exit(0)
    print("False")




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

# Example usage
if __name__ == "__main__":
    n, m, n_of_r = map(int, sys.stdin.readline().strip().split())
    adj_matrix = [[0] * (n) for _ in range(n)]
    source_name, target_name = sys.stdin.readline().split()

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

    if is_directed:
        print(bellman_ford(adj_matrix, red_nodes, source, target, is_directed))
    else:
        print(bellman_ford(adj_matrix, red_nodes, source, target, is_directed))

    exit(0)




def bellman_ford(adj_matrix, weights, source, target, is_directed):
    """
    Created with inspiration from https://www.geeksforgeeks.org/bellman-ford-algorithm-in-python/

    Perform Bellman-Ford algorithm to find longest path from source to all nodes.
    Works for both directed and undirected graphs based on the `is_directed` flag.

    Parameters:
    - adj_matrix: 2D list (matrix) where adj_matrix[i][j] is 1 if there is an edge from node i to j.
    - weights: List of weights corresponding to each node (e.g., 1 for red nodes, 0 for others).
    - source: Starting node (integer index).
    - is_directed: Boolean indicating whether the graph is directed (True) or undirected (False).

    Returns:
    - distances: List of maximum path weights from source to each node.
    - predecessors: List of predecessors to reconstruct paths if needed.
    """
    # Number of nodes
    num_nodes = len(adj_matrix)

    # Initialize distances and predecessors
    distances = [-float(
        'inf')] * num_nodes  # Use negative infinity for longest path tracking
    distances[source] = weights[source]  # Start with the weight of the source node

    # Relax all edges |V|-1 times
    for _ in range(num_nodes - 1):
        for u in range(num_nodes):
            for v in range(num_nodes):
                # Check if there is an edge from u to v
                if adj_matrix[u][v] == 1:
                    # Relaxation for u -> v
                    if distances[u] + weights[v] > distances[v]:
                        distances[v] = distances[u] + weights[v]

                    # If the graph is undirected, also consider v -> u
                    if not is_directed:
                        if distances[v] + weights[u] > distances[u]:
                            distances[u] = distances[v] + weights[u]

    # Check for positive-weight cycles (optional in this problem)
    for u in range(num_nodes):
        for v in range(num_nodes):
            if adj_matrix[u][v] == 1:
                if distances[u] + weights[v] > distances[v]:
                    return "PositiveWeightCycle"
                if not is_directed and distances[v] + weights[u] > distances[u]:
                    return "PositiveWeightCycle"

    return distances[target]

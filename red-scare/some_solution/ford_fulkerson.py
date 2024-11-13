def _dfs(residual_graph, source, sink, visited):
    # Base case: if we reached the sink, return the path
    if source == sink:
        return [source]

    # Mark the current node as visited
    visited.add(source)

    # Explore all neighbors of the current node using adjacency matrix
    for neighbor in range(len(residual_graph)):
        capacity = residual_graph[source][neighbor]
        # If neighbor is not visited and the edge has available capacity
        if neighbor not in visited and capacity > 0:
            path = _dfs(residual_graph, neighbor, sink, visited)
            if path:  # If path is found, append the current node and return
                return [source] + path

    # Return None if no path is found
    return None

def _update_residual_graph(residual_graph, path, flow):
    """ Updates the residual graph by adjusting forward and backward edges. """
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]

        # Forward edge: reduce capacity by the flow sent
        residual_graph[u][v] -= flow

        # Backward edge: increase capacity to allow for flow cancellation
        residual_graph[v][u] += flow

def ford_fulkerson(residual_graph, source, sink):
    """ Ford-Fulkerson algorithm to compute the maximum flow using adjacency matrix. """
    max_flow = 0

    while True:
        visited = set()
        # Find an augmenting path using DFS
        path = _dfs(residual_graph, source, sink, visited)

        if not path:
            # If no augmenting path is found, we're done
            break

        # Find the bottleneck capacity (minimum residual capacity along the path)
        bottleneck_flow = min(
            residual_graph[u][v] for u, v in zip(path, path[1:])
        )

        # Augment the flow along the path
        _update_residual_graph(residual_graph, path, bottleneck_flow)

        # Add the bottleneck flow to the total max flow
        max_flow += bottleneck_flow

    return max_flow
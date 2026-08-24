# Depth-Limited Search (DLS) implementation


def depth_limited_search(graph, node, goal, limit, visited=None):
     """
    graph: dict mapping each node -> list of neighboring nodes
    node: current node being visited
    goal: target node to search for
    limit: maximum depth still allowed to explore
    visited: set of already-visited nodes (used internally to avoid cycles)
    """
    if visited is None:
        visited = set()

    print(f"Visiting: {node}, Depth remaining: {limit}")

    # Goal test
    if node == goal:
        return True

    # Depth limit reached
    if limit <= 0:
        return False

    visited.add(node)

    # Explore neighbors
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if depth_limited_search(graph, neighbor, goal, limit - 1, visited):
                return True

    return False


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

start = 'A'
goal = 'H'
depth_limit = 3

found = depth_limited_search(graph, start, goal, depth_limit)

print("\nGoal Found!" if found else "\nGoal Not Found")

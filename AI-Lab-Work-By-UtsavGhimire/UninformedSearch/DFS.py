# depth first search algorithm implementation


def dfs(graph, start):
    """
    graph: dict mapping each node -> list of neighboring nodes
    node: current node being visited
    goal: target node to search for
    visited: set of already-visited nodes (used internally to avoid cycles)
    """
    visited = set()
    stack = [start]

    visited.add(start)``

    while stack:
        node = stack.pop()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J', 'K'],
    'F': [],
    'G': ['L'],
    'H': [],
    'I': ['M'],
    'J': [],
    'L': [],
    'K': ['N'],
    'M': [],
    'N': [],
}

print("DFS Traversal:")
dfs(graph, 'A')

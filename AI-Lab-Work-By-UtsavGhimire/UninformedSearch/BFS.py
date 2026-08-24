# breadth first search algorithm implementation

from collections import deque


def bfs(graph, start):
    """
    graph: dict mapping each node -> list of neighboring nodes
    start: starting node
    goal: target node to search for
    """
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example graph (adjacency list)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J', 'K'],
    'F': [],
    'G': ['L'],
    'H': [],
    'I': 'M',
    'J': [],
    'L': [],
    'K': 'N',
    'M': [],
    'N': [],
}

print("BFS Traversal:")
bfs(graph, 'A')

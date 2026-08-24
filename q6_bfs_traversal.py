from collections import deque

# Question 6: Breadth First Search Traversal
#
# NOTE:
# The assignment says "the following graph", but no graph appears in the
# supplied PDF. This is an illustrative graph. Replace GRAPH if your
# instructor provided a specific graph separately.

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["E", "F"],
}


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


result = bfs(GRAPH, "A")
print("BFS Traversal:", " -> ".join(result))

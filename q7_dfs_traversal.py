# Question 7: Depth First Search Traversal using a Stack
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


def dfs(graph, start):
    stack = [start]
    visited = set()
    traversal = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)

        # Reverse the neighbors so the traversal follows the listed order
        # when using a LIFO stack.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return traversal


result = dfs(GRAPH, "A")
print("DFS Traversal:", " -> ".join(result))

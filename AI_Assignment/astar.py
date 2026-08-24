import heapq

# Weighted graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 3},
    'G': {}
}

# Heuristic values
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 3,
    'G': 0
}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_f = new_cost + h[neighbor]

            heapq.heappush(
                queue,
                (new_f, new_cost, neighbor, path + [neighbor])
            )

    return None, float('inf')


path, cost = astar('A', 'G')

print("Optimal Path:", path)
print("Total Cost:", cost)
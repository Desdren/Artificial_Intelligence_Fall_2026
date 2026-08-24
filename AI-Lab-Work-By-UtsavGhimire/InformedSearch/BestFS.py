import heapq


def best_first_search(start, goal, get_neighbors, heuristic):
    """
    start: starting node
    goal: goal node
    get_neighbors(node) -> list of neighboring nodes
    heuristic(node, goal) -> estimated distance/cost to goal (lower = better)
    """
    visited = {start}
    pq = [(heuristic(start, goal), start, [start])]

    while pq:
        _, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(
                    pq, (heuristic(neighbor, goal), neighbor, new_path))

    return None


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F'],
}

# Heuristics
heuristic_values = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0,
}


def get_neighbors(node):
    return graph[node]


def heuristic(node, goal):
    return heuristic_values[node]


path = best_first_search('A', 'G', get_neighbors, heuristic)
print(path)

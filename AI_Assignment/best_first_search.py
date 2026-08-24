import heapq

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
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

def greedy_best_first(start, goal):
    queue = [(h[start], start)]
    visited = set()

    while queue:
        _, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        print("Visited:", node)

        if node == goal:
            print("Goal Reached")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (h[neighbor], neighbor))

    print("Goal Not Found")


greedy_best_first('A', 'G')
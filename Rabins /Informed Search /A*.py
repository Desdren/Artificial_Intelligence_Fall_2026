from queue import PriorityQueue

# Graph with cost
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 5,
    'G': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))

    cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        current = pq.get()[1]

        if current == goal:
            break

        for neighbor, edge_cost in graph[current]:
            new_cost = cost[current] + edge_cost

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                pq.put((priority, neighbor))

                parent[neighbor] = current

    # Path finding
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Path:", path)
    print("Total Cost:", cost[goal])

# Function call
astar('A', 'G')
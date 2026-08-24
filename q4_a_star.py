import heapq

# Question 4: A* Search Algorithm
#
# NOTE:
# The assignment PDF says a weighted graph and heuristic values are given,
# but the supplied PDF does not actually include those values.
# The graph below is therefore an illustrative example.
# Replace GRAPH and HEURISTIC with your instructor's graph if it was supplied separately.

GRAPH = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 3, "E": 5},
    "C": {"A": 4, "F": 3},
    "D": {"B": 3, "G": 4},
    "E": {"B": 5, "G": 2},
    "F": {"C": 3, "G": 5},
    "G": {"D": 4, "E": 2, "F": 5},
}

HEURISTIC = {
    "A": 7,
    "B": 6,
    "C": 5,
    "D": 4,
    "E": 2,
    "F": 5,
    "G": 0,
}


def a_star(graph, heuristic, start, goal):
    # Priority queue entries: (f_cost, g_cost, node)
    queue = [(heuristic[start], 0, start)]
    came_from = {start: None}
    g_cost = {start: 0}
    closed = set()

    while queue:
        f, current_g, current = heapq.heappop(queue)

        if current in closed:
            continue

        closed.add(current)

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = came_from[node]

            path.reverse()
            return path, g_cost[goal]

        for neighbor, edge_cost in graph[current].items():
            new_g = current_g + edge_cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                came_from[neighbor] = current
                f_cost = new_g + heuristic[neighbor]
                heapq.heappush(queue, (f_cost, new_g, neighbor))

    return None, None


path, cost = a_star(GRAPH, HEURISTIC, "A", "G")

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")

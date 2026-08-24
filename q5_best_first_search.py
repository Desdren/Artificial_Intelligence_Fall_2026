import heapq

# Question 5: Greedy Best First Search
#
# NOTE:
# The assignment PDF requires a graph and heuristic values, but the supplied
# PDF does not include the actual graph/values. The following is an
# illustrative graph. Replace it with the instructor's graph if provided.

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"],
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


def greedy_best_first_search(graph, heuristic, start, goal):
    queue = [(heuristic[start], start)]
    visited = set()

    while queue:
        _, current = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)
        print("Visited:", current)

        if current == goal:
            print("Goal Reached")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor))

    print("Goal not reachable.")


if __name__ == "__main__":
    greedy_best_first_search(GRAPH, HEURISTIC, "A", "G")

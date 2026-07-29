from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    while not pq.empty():
     h,node = pq.get()

     if node in visited:
            continue

     
     print(node, end=" ")
     visited.add(node)

     if node == goal:
        print("\nGoal reached!")
        return

     for neighbor in graph[node]:
        if neighbor not in visited:
            pq.put((heuristic[neighbor], neighbor))
# Graph (Adjacency List)

graph = {
'A': ['B', 'C', 'D'],
'B': ['E', 'F'],
'C': ['G'],
'D': ['H'],
'E': [],
'F': [],
'G': [],
'H': []
}

# Heuristic values (lower = better)

heuristic = {
'A': 5,
'B': 3,
'C': 4,
'D': 6,
'E': 2,
'F': 1,
'G': 0,
'H': 7
}

print("--- Compiled by Rohit Yadav ---\n")
best_first_search(graph,'A','G',heuristic)
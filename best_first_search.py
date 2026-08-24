import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    # Priority queue stores: (heuristic_value, current_node)
    pq = [(heuristics[start], start)]
    
    print("Greedy Best First Search Traversal")
    while pq:
        h, current = heapq.heappop(pq)
        
        if current in visited:
            continue
            
        visited.add(current)
        print(f"Visited Node: {current} (Heuristic: {h})")
        
        if current == goal:
            print("Goal Reached")
            return
            
        for neighbor, _ in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor))
                
    print("Goal not found.")

# Example Graph with Adjacency List
graph = {
    'A': [('B', 3), ('C', 6)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 6)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 7,
    'G': 0
}

best_first_search(graph, heuristics, 'A', 'G')
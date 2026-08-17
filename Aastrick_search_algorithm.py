import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue stores: (f_score, g_score, current_node, path)
    pq = [(heuristics[start], 0, start, [start])]
    g_scores = {start: 0}
    
    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path, g
            
        for neighbor, weight in graph.get(current, []):
            tentative_g = g + weight
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [neighbor]))
                
    return None, float('inf')

# Example Graph and Heuristics
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('G', 10)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'G': 0
}

optimal_path, total_cost = a_star_search(graph, heuristics, 'A', 'G')

print("A* Search Results")
print(f"Optimal Path: {' -> '.join(optimal_path)}")
print(f"Total Cost: {total_cost}")
def dfs_stack(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            
            # Push neighbors in reverse order so left-to-right processing matches standard DFS order via stack
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order

# Graph Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

order = dfs_stack(graph, 'A')
print("DFS Traversal Order (using Stack)")
print(" -> ".join(order))
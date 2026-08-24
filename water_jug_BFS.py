from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque([((0, 0), [])]) 
    
    print("--- Visited States ---")
    while queue:
        (jug1, jug2), path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
            
        visited.add((jug1, jug2))
        current_state = (jug1, jug2)
        print(f"Visited: {current_state}")
        
        if jug1 == target or jug2 == target or (jug1 + jug2) == target:
            print("\nTarget found!")
            return path + [current_state]
            
        # Generate possible valid transitions
        transitions = [
            (cap1, jug2),             # Fill Jug 1
            (jug1, cap2),             # Fill Jug 2
            (0, jug2),                # Empty Jug 1
            (jug1, 0),                # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (max(0, jug1 - (cap2 - jug2)), min(cap2, jug2 + jug1)),
            # Pour Jug 2 -> Jug 1
            (min(cap1, jug1 + jug2), max(0, jug2 - (cap1 - jug1)))
        ]
        
        for next_state in transitions:
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
                
    print("No Solution.")
    return None

# Execution
solution_path = water_jug_bfs(5, 3, 4)
if solution_path:
    print("Path taken:")
    for step in solution_path:
        print(step)
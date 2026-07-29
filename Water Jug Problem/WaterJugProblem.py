from collections import deque

# Jug capacities
JUG1 = 5
JUG2 = 3

# Initial state
start = (0, 0)

# Target
target = 4


def get_next_states(state):
    x, y = state

    states = []

    # Fill Jug 1
    states.append((JUG1, y))

    # Fill Jug 2
    states.append((x, JUG2))

    # Empty Jug 1
    states.append((0, y))

    # Empty Jug 2
    states.append((x, 0))

    # Pour Jug 1 -> Jug 2
    amount = min(x, JUG2 - y)
    states.append((x - amount, y + amount))

    # Pour Jug 2 -> Jug 1
    amount = min(y, JUG1 - x)
    states.append((x + amount, y - amount))

    return states


def bfs_water_jug():
    queue = deque([start])
    visited = {start}

    while queue:

        current = queue.popleft()

        print("Visited:", current)

        # Check target
        if current[0] == target or current[1] == target:
            print("\nTarget reached:", current)
            return

        # Generate next states
        for next_state in get_next_states(current):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    print("No Solution.")


bfs_water_jug()
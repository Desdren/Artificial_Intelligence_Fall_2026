from collections import deque

# Question 3: Water Jug Problem using BFS

JUG1 = 5
JUG2 = 3
TARGET = 4


def get_next_states(state):
    a, b = state
    states = []

    # Fill Jug 1
    states.append((JUG1, b))

    # Fill Jug 2
    states.append((a, JUG2))

    # Empty Jug 1
    states.append((0, b))

    # Empty Jug 2
    states.append((a, 0))

    # Pour Jug 1 -> Jug 2
    amount = min(a, JUG2 - b)
    states.append((a - amount, b + amount))

    # Pour Jug 2 -> Jug 1
    amount = min(b, JUG1 - a)
    states.append((a + amount, b - amount))

    return states


def bfs():
    start = (0, 0)
    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()
        print("Visited:", state)

        if state[0] == TARGET or state[1] == TARGET:
            print("Target found:", state)
            return

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    print("No Solution.")


if __name__ == "__main__":
    bfs()

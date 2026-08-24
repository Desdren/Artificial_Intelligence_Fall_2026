from collections import deque


def water_jug(cap1, cap2, target):
    # Queue stores: (jug1, jug2, path)
    queue = deque()
    queue.append((0, 0, []))

    visited = set()

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        path = path + [(jug1, jug2)]

        # Goal test
        if jug1 == target or jug2 == target:
            return path

        # Possible operations
        next_states = [
            (cap1, jug2),                 # Fill Jug 1
            (jug1, cap2),                 # Fill Jug 2
            (0, jug2),                    # Empty Jug 1
            (jug1, 0),                    # Empty Jug 2
        ]

        # Pour Jug1 -> Jug2
        transfer = min(jug1, cap2 - jug2)
        next_states.append((jug1 - transfer, jug2 + transfer))

        # Pour Jug2 -> Jug1
        transfer = min(jug2, cap1 - jug1)
        next_states.append((jug1 + transfer, jug2 - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None

#inputsfor sizes and target
capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("Solution Found:\n")
    for step in solution:
        print(step)
else:
    print("No Solution")

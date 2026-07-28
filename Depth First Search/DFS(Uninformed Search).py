from collections import deque

def dfs(graph, start):
 visited = set()
 stack = [start]

 visited.add(start)

 while stack:
    node = stack.pop()   # difference: pop() instead of popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
graph = {
'A': ['B', 'C','D'],
'B': ['E', 'F'],
'C': ['G','H'],
'D': ['I'],
'E': ['J','K'],
'F': [],
'G':['L'],
'H':[],
'I':['M'],
'J':[],
'L':[],
'K':['N'],
'M':[],
'N':[],
}

print("--- Compiled by Rohit Yadav ---\n")

print("DFS Traversal:")
dfs(graph, 'A')
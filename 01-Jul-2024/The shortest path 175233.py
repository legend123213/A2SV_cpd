# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

num_vertices, num_edges = map(int, input().split())
start, goal = map(int, input().split())

graph = defaultdict(list)

for _ in range(num_edges):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()

queue = deque([start])
parent_dict = {start: None}
found = False
visited.add(start)

while not found and queue:
    current = queue.popleft()

    for child in graph[current]:
        if child in visited: continue
        visited.add(child)

        parent_dict[child] = current
        if child == goal:
            found = True
            break

        queue.append(child)



if found:
    path = []
    current = goal
    path_len = 0
    while current:
        path.append(current)
        current = parent_dict[current]
        path_len+=1

    print(path_len-1)
    print(" ".join(str(i) for i in path[::-1]))
else:
    print(-1)
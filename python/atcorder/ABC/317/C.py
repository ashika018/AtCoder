N, M = [int(i) for i in input().split(' ')]
road_info = [[int(i) for i in input().split(' ')] for _ in range(M)]

graph = {}
road_length_d = {}
for info in road_info:
    if(info[0] not in graph): graph[info[0]] = [info[1]]
    else: graph[info[0]].append(info[1])
    if(info[1] not in graph): graph[info[1]] = [info[0]]
    else: graph[info[1]].append(info[0])

    key = [for i in sorted(info[0:1])]
    road_length_d[''.join(sorted(info[0:-1]))] = info[-1]

print(graph)
print(road_length_d)
'''
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
'''
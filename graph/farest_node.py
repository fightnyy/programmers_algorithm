from collections import deque, defaultdict
from pdb import set_trace
import copy


def bfs(f, graph, visited):
    q = deque()
    count = 0
    q.append([f, count])
    while q:
        # set_trace()
        node, cnt = q.popleft()
        if visited[node-1] != -1:
            continue
        else:
            visited[node-1] = cnt
            for v in graph[node]:
                q.append([v, cnt+1])
    return visited


def solution(n, edge):
    visited = [-1]*n
    answer = 0
    cnt = 0
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    answer = bfs(1, graph, visited)
    for val in visited:
        if val == max(answer):
            cnt += 1
    return cnt

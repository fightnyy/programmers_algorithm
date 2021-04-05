from collections import deque, defaultdict
from pdb import set_trace
import copy


def bfs(graph, visited):
    q = deque()
    q.append(graph[1])
    visited[0] = 1
    count = 0
    cnt_dict = defaultdict(int)
    while any(v == 0 for v in visited):
        # set_trace()
        for node_list in copy.deepcopy(q):
            for node in node_list:
                if visited[node-1]:
                    continue
                else:
                    visited[node-1] = 1
                    cnt_dict[node] = count + 1
                    q.append(graph[node])
        count += 1
    max_value = max(cnt_dict.values())
    return list(cnt_dict.values()).count(max_value)


def solution(n, edge):
    visited = [0]*n
    answer = 0
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    answer = bfs(graph, visited)
    return answer


n = 6
vertex = [[1, 2], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))

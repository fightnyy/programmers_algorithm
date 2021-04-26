import sys
import copy
from pdb import set_trace
input = sys.stdin.readline
INF = sys.maxsize

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
di = [0,
      [[0], [1], [2], [3]],  # 각 4방향
      [[0, 1], [2, 3]],  # 서로 반대 방향
      [[1, 2], [1, 3], [0, 2], [0, 3]],  # 서로 직각인 방향
      [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],  # 3방향
      [[0, 1, 2, 3]],  # 4방향
      ]

MIN = float('inf')


def dfs(start, MAP, cctv):
    global MIN
    if start == len(cctv):
        cnt = 0
        for y in range(0, row):
            for x in range(0, col):
                if MAP[y][x] == 0:
                    cnt += 1
        MIN = min(MIN, cnt)
        return

    num, y, x = cctv[start]
    for dir in di[num]:
        tmp = copy.deepcopy(MAP)
        for i in dir:
            ny, nx = y+dy[i], x+dx[i]
            while row > ny >= 0 and col > nx >= 0:
                if tmp[ny][nx] == 6:
                    break
                elif tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
                ny += dy[i]
                nx += dx[i]
        dfs(start+1, tmp, cctv)


if __name__ == "__main__":
    row, col = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(row)]
    cctv = []
    for y in range(0, row):
        for x in range(0, col):
            if MAP[y][x] not in [0, 6]:
                cctv.append([MAP[y][x], y, x])
    dfs(0, MAP, cctv)
    print(MIN)

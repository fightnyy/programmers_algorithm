from collections import defaultdict
from pdb import set_trace


def solution(n, results):
    d = {}
    count = 0
    for i in range(1, n+1):
        d[i] = set(), set()  # win_list, lost_list
    for win, lost in results:
        d[win][0].add(lost)
        d[lost][1].add(win)
    for i in d:
        wins, losts = d[i]
        for w in wins:
            d[w][1].update(losts)
        for l in losts:
            d[l][0].update(wins)
    for i in range(1, len(d)+1):
        if len(d[i][0]) + len(d[i][1]) == n-1:
            count += 1
    return count

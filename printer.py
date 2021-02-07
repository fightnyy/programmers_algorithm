"""
가장먼저 인쇄되면 1
"""


def solution(priorities, location):
    answer = []
    tmp = []
    
    idx_priorities = [(idx, value) for idx, value in enumerate(priorities)]
    while idx_priorities:
        max_value = max(idx_priorities, key = lambda x:x[1])[1]
        if idx_priorities[0][1] == max_value:
            tmp.append(idx_priorities.pop(0)[0])
            
            
        else :
            idx_priorities.append(idx_priorities.pop(0))
        
    return tmp.index(location) + 1
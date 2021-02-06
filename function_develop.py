import collections
def solution(progresses, speeds):
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)
    tmp = []
    answer = []
    
    while speeds:
        for i in range(len(progresses)): 
            progresses[i] += speeds[i] 
        for i in range(len(progresses)): 
            if progresses[0] >= 100 :
                tmp.append(progresses.popleft())
                speeds.popleft()
        if tmp:
            answer.append(len(tmp))
            tmp.clear()
    return answer



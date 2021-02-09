"""
파이썬 sort를 사용했는데 시간 초과가 나는 경우라면
파이썬 heap을 사용해보자
"""
import heapq
def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    answer  = 0
    while heap[0] < K :
        if len(heap) >= 2:
            answer += 1
            heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
        else :
            return -1
    return answer
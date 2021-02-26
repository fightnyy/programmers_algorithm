from collections import deque
import heapq
def solution(A, B):
    count = 0
    A = [-i for i in A]
    B = [-i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)

    
    while A:
        if abs(heapq.heappop(A))<abs(B[0]):
            count += 1
            heapq.heappop(B)
    return count
import heapq
def solution(operations):
    heap = []
    inverse_heap=[]
    
    for an in operations:
        tmp_oprd, tmp_num = an.split() 
        if tmp_oprd == 'D':
            if tmp_num=='1': # 최댓값 삭제
                if heap:
                    heap.remove(max(heap))
                
            else :   # 최소값 삭제
                if heap:
                    heap.remove(min(heap))
        else : # 값 삽입
            heapq.heappush(heap,int(tmp_num))
              
    if len(heap)==0 :
        return [0,0]
    else:
        return  [max(heap),heapq.heappop(heap)]
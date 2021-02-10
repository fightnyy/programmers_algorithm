def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        sort_array =[]
        sort_array=array[i-1:j]
        sort_array.sort()
        answer.append(sort_array[k-1])
        
    return answer
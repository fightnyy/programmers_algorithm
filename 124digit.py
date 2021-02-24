def solution(n):
    answer = ''
    num_list = ["1","2","4"]
    while n > 0:
        n -= 1
        answer=num_list[n%3] + answer
        n//=3
        
    return answer
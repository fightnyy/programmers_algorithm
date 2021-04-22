# sig_completion : completion 한 사람중 한명
"""
1 차 풀이
Time over
""" 
def solution(participant, completion):
    for sig_completion in completion:
        if sig_completion in participant:
            index=participant.index(sig_completion)
            participant.pop(index)
    return participant[0]

"""
2 차 풀이
Time over
""" 
def solution(participant, completion):
    for com in completion:
        participant.remove(com)
    return participant.pop(0)



"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (1.20ms, 10.2MB)
테스트 4 〉	통과 (3.47ms, 10.3MB)
테스트 5 〉	통과 (3.14ms, 10.4MB)
효율성  테스트
테스트 1 〉	
테스트 2 〉	
테스트 3 〉	
테스트 4 〉	
테스트 5 〉	
"""
        

"""
3 차 풀이
Counter 는 빼기가 된다!
""" 
import collections

def solution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return answer.most_common()[0][0]
"""
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.37ms, 10.3MB)
테스트 4 〉	통과 (0.72ms, 10.5MB)
테스트 5 〉	통과 (0.83ms, 10.6MB)
효율성  테스트
테스트 1 〉	통과 (30.64ms, 24.4MB)
테스트 2 〉	통과 (58.19ms, 27.8MB)
테스트 3 〉	통과 (69.22ms, 30.1MB)
테스트 4 〉	통과 (93.00ms, 39MB)
테스트 5 〉	통과 (81.38ms, 39MB)
"""
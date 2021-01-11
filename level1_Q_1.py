def solution(n):
    answer = 0

    while n != 0:
        des = n%10
        answer += des
        n //=10
    return answer
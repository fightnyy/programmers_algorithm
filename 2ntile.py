def solution(n):
    a=1
    b=2
    for i in range(2,n):
        a,b = b,a + b
    return b % 1000000007
def solution(prices):
    answer = [0] * len(prices)
    tmp = 0 
    for index in range(len(prices)):
        for jndex in range(index+1, len(prices)):
            tmp += 1
            if prices[index] > prices[jndex]:
                break
        answer[index] = tmp
        tmp = 0
                
    return answer
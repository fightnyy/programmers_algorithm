def solution(money):
    dp1 = [0] * (len(money) - 1)  # 0을 뺄거다
    dp2 = [0] * (len(money) - 1)  # 마지막을 뺄거다

    dp1[0] = money[1]
    dp1[1] = max(money[1], money[2])
    dp1[2] = max(dp1[0] + money[3], dp1[1])

    dp2[0] = money[0]
    dp2[1] = max(money[0], money[1])
    dp2[2] = max(dp2[0] + money[2], dp2[1])

    for i in range(3, len(money)):
        dp1[i - 1] = max(dp1[i - 3] + money[i], dp1[i - 2])

    for jdx in range(2, len(money) - 1):
        dp2[jdx] = max(dp2[jdx - 2] + money[jdx], dp2[jdx - 1])
    return max(dp1[-1], dp2[-1])

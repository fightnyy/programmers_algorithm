from collections import Counter
from itertools import combinations


def solution(orders, course):
    candidate = []
    answer = []
    for order in orders:
        for i in range(2, len(order)+1):
            for c_tuple in list(combinations(order, i)):
                c_str = "".join(sorted(c_tuple))
                candidate.append(c_str)
    counter = Counter(candidate)
    # 길이가 오름차순으로 배열됨
    counter = sorted(counter.items(), key=lambda x: len(x[0]))
    for n_menu in course:
        meet = []
        for sg_counter in counter:  # (word, 나온 횟수)
            if n_menu == len(sg_counter[0]):
                meet.append(sg_counter)
        meet.sort(key=lambda x: x[1], reverse=True)  # 가장 많이 나온 순으로 정렬
        if meet:  # 스카피가 원하는 메뉴수에
            big = meet[0][1]  # 가장 큰거를 줌
        for cnd in meet:
            if big == cnd[1] and cnd[1] >= 2:
                answer.append(cnd[0])
    return sorted(answer)


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))

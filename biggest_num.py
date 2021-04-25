import itertools
import functools


def solution(numbers):
    def compare(a, b):
        t1 = a+b
        t2 = b+a
        return (int(t1) > int(t2)) - (int(t2) > int(t1))
    str_num = list(map(str, numbers))
    # possble_per=list(itertools.permutations(str_num))
    # str_num=["".join(s_num) for s_num in possble_per]
    # print(str_num)
    # num = list(map(int,str_num))
    # return str(max(num))
    numbers = sorted(str_num, key=functools.cmp_to_key(compare), reverse=True)
    return str(int("".join(numbers)))

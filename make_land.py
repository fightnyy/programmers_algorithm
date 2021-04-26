def solution(land):
    for i in range(len(land)-1):
        new_list = land[i+1][:]
        # print(f"new_list : {new_list}")
        for j in range(len(land[0])):
            for k in range(len(land[0])):
                if j == k:
                    continue
                else:
                    land[i+1][j] = max(land[i+1][j], new_list[j]+land[i][k])
        # set_trace()
    return (max(land[-1]))

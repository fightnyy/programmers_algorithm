def solution(routes):
    count = 0
    routes.sort(key=lambda x: x[0])
    right = routes[0][1]
    count += 1
    for i in range(1, len(routes)):
        if right >= routes[i][0]:
            if right > routes[i][1]:
                right = routes[i][1]
        else:
            count += 1
            right = routes[i][1]

    return count

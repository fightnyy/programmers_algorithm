from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if cache:
                    cache.popleft()
                    cache.append(city)
            answer += 5
    return answer

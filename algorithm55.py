def solution(citations):
    cache= []
    for i in range(len(citations)):
        key = citations[i]
        cnt = 0
        for j in range(len(citations)):
            if key <= citations[j]:
                cnt += 1
        if cnt >= key:
            cache.append((key, cnt))
    cache.sort(reverse=True)
    print(cache)
    return cache[0][0]


print(solution([3,0,6,1,5]))
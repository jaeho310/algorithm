def solution(numbers):
    answer = ''
    cache = []
    for i in numbers:
        temp = list(map(str,str(i)))
        cache.append(temp)

    sortedNum = sorted(cache,key=lambda x: x*3,reverse=True)
    for i in sortedNum:
        for j in i:
            answer += str(j)
    
    return str(int(answer))

print(solution([6,10,2]))
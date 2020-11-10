def solution(n):
    a = set()
    for i in range(len(n)-1):
        for j in range(i,len(n)):
            a.add(n[i]+n[j+1])
    result = list(a)
    result.sort()
    return result


print(solution([2,1,3,4,1]))
    

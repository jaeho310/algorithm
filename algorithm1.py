def solution(n):
    return sorted(list({n[i]+n[j] for i in range(len(n)) for j in range(i+1,len(n))}))

print(solution([2,1,3,4,1]))
def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)):
        answer.append(int(n[i])) 
    answer.reverse()
    return answer

print(solution(12345))
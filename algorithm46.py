def solution(s):
    queue = list(s)
    answer = []
    n = 1
    cnt = 1
    while n <= len(s):
        temp = ''
        while len(queue) >= n:
            word = ''
            for i in range(n):
                word += queue.pop(0)
            if word == ''.join(queue[:n]):
                cnt += 1
            else:
                temp += (str(cnt)) + word if cnt > 1 else word
                cnt = 1
        temp += ''.join(queue)
        answer.append(len(temp))
        queue = list(s)
        n += 1

    return min(answer)
    

    

print(solution("ababcdcdababcdcd"))
        

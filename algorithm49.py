def solution(num):
    answer = ""
    cache = ['4','1','2']
    while num:
        num, remain = divmod(num, 3)
        answer = cache[remain] + answer
        
        if remain == 0:
            num -= 1

    return answer

print(solution(10))
# def solution(n):
#     answer = ""
#     answer_list = sorted([i for i in str(n)],reverse=True)
#     for i in answer_list:
#         answer += i
#     return int(answer)

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))

print(solution(123))



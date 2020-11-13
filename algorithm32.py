def solution(phone_number):
    answer = ""
    cnt = len(phone_number)
    answer += '*'*(cnt-4)
    answer += phone_number[cnt-4:]

    return answer

print(solution("334444"))
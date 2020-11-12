def solution(s, n):
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
            else:
                result += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        else:
            result += i
    return result

print(solution("z a",1))

print(ord(" "))
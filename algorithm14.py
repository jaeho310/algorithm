def solution(s):
    pcnt = 0
    ycnt = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcnt += 1
        if s[i] == "y" or s[i] == "Y":
            ycnt += 1
    if pcnt == ycnt:
        return True
    return False

print(solution("Pyy"))

#def solution(s):
    # return s.lower().count('p') == s.lower().count('y')
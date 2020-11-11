def solution(s):
    return ''.join(sorted(list(s), key = lambda x:x[0], reverse = True))

print(solution('Zbcdefg'))
def solution(s):
    if 4 == len(s) or len(s) == 6:
        if s.isdigit():
            return True
    return False
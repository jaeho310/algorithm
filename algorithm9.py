def solution(n):
    trinum = []
    while n >= 3:
        trinum.insert(0,n%3)
        n = n // 3
    trinum.insert(0,n)
    result = 0
    for i in range(len(trinum)):
        result += (3**i) * trinum[i]
    return result



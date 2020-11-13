def solution(num):
    return collatz(num,0)

def collatz(n,cnt):
    if cnt == 500:
        return -1
    if n == 1:
        return cnt
    if n % 2 == 0:
        return collatz(n/2,cnt+1)
    elif n % 2 != 0:
        return collatz(n*3 + 1, cnt + 1)

print(solution(6))

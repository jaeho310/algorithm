def solution(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):            # n의 최대 약수가 sqrt(n) 이하
        if sieve[i] == True:             # i가 소수인 경우 
            for j in range(2*i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return len([i for i in range(2, n+1) if sieve[i] == True])  # len()으로 개수 반환


def fibo(num):
    cache = [0 for i in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]
    


# Memoization 기법을 사용하여 이전의 데이터를 기억하여 같은 계산을 하지 않게하는 프로그래밍 기법이다.
# 대표적으로 피보나치 수열을 구할때 재귀적용법을 사용하면 양쪽에서 같은데이터를 연산하게되는데
# 동적프로그래밍은 그런 단점을 해결해준다.
# 비슷한 용법으로 분할정복이 있는데 병합정렬 퀵정렬이 이에 속한다. 문제를 잘개 쪼갤때 부분문제가 서로 중복되지 않는다는 장점.
# 점화식을 만들어 푸는 경우도 존재한다.
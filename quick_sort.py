def sort(a):
    if len(a) <= 1:
        return a
    
    pivot = a[0]
    left = [i for i in a[1:] if i < mid]
    right = [i for i in a[1:] if i >= mid]
    return left + [pivot] + right





# 퀵소트
# 정렬알고리즘의 꽃이다.
# 피벗값을 임의로 지정 (보통 첫번째 인덱스의 데이터) 그 데이터를 기준으로 큰값과 작은값을 기준으로
# 데이터를 잘라 재귀적 용법을 통해 정렬한다.
# 시간복잡도는 nLogN 최악의경우는 n^2이다
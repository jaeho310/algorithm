def solution(arr, divisor):
    result = sorted([i for i in arr if i % divisor == 0])
    if result == []:
        return [-1]
    return result
print(solution([5,10,11,15],4))
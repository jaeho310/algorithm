def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        result = bin(i|j)[2:]
        zero_cnt = n - len(result)
        if zero_cnt > 0:
            result = '0'*zero_cnt + result
        result = result.replace('1','#')
        result = result.replace('0',' ')
        answer.append(result)
    return answer




print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))


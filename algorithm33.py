def solution(arr1, arr2):
    tmp = []
    answer = []
    for a, b in zip(arr1, arr2):   # 1번째 for문
        for c,d in zip(a,b):        # 2번째 for문
            tmp.append(c+d)
        answer.append(tmp)
        tmp = []
    return answer



print(solution([[1,2],[2,3]], [[3,4],[5,6]]))


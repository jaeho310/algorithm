def solution(array, commands):
    answer = []
    temp = []
    for i in commands:
        start = i[0]
        finish = i[1]
        idx = i[2]

        for j in range(start-1,finish):
            temp.append(array[j])
            
        temp.sort()
        answer.append(temp[idx-1])
        temp.clear()
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer
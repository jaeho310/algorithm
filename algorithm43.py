def solution(priorities, location):
    answer = 0
    max_value = max(priorities)
    while True:
        n = priorities.pop(0)
        if max_value == n:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_value = max(priorities)
        else:
            priorities.append(n)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

        
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer

print(solution([1, 1, 9, 1, 1, 1],0))



# import copy
# def solution(temp):
#     answer = []
#     temp = copy.copy(prices)
#     for i in range(len(prices)):
#         k = temp.pop(0)
#         key = True
#         for j in temp:
#             if k-1 >= j:
#                 n = temp.index(j) + 1
#                 answer.append(n)
#                 key = False
#                 break
#         if key:
#             answer.append(len(prices)-i-1)
#     return answer



from collections import deque

def solution(prices):
    answer = []
    
    que_prices = deque(prices)
    
    while que_prices :
        price = que_prices.popleft()
        up_time = 0
        for n in que_prices :
            up_time += 1
            if price > n :
                break
        answer.append(up_time)
        
    return answer

print(solution([1,2,3,2,3]))

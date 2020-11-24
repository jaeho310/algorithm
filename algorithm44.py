from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    total_weight = []
    total_weight.append((1,truck_weights.pop(0)))
    while truck_weights:
        answer += 1
        current_weight = truck_weights.pop(0)
        if answer - total_weight[0][0] + 1> bridge_length:
            del total_weight[0] 
        temp = sum(i[1] for i in total_weight)
        if temp + current_weight > weight:
            truck_weights.insert(0,current_weight)
        else:
            total_weight.append((answer,current_weight))

    answer += bridge_length
    return answer



print(solution(2, 10, [7,4,5,6]))
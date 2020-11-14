def solution(prices):
    answer = []
    for i in range(len(prices)):
        if prices[i]-1 in prices:
            n = prices.index(prices[i]-1) - i
            answer.append(n)
            continue
        else:
            answer.append(len(prices)-i-1)
    return answer

print(solution([1,2,3,2,3]))


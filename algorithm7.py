def solution(coinList, value):
    result = []
    for i in coinList:
        temp_cnt = value // i
        result.append([i,temp_cnt])
        value -= i * temp_cnt
    return result

coinList = [1000,500,100,50,10]
print(solution(coinList,7780))
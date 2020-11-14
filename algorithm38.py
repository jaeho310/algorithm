def solution(N, stages):
    answer = []
    fail_rate_dic = {}
    fail_rate = 0 
    current_challenger = len(stages)

    for i in range(N):
        if current_challenger == 0:
            fail_rate_dic[i+1] = 0
            continue
        fail_rate = stages.count(i+1) / current_challenger
        current_challenger -= stages.count(i+1)
        fail_rate_dic[i+1] = fail_rate

    print(fail_rate_dic)

    result = sorted(fail_rate_dic.items(), key = lambda x: x[1], reverse=True)

    for i in result:
        answer.append(i[0])
    
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))

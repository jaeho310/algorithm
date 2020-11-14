def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        n = []
        isFail = False
        for j in skill:
            if j in i: # 스킬트리 첫번째꺼가 있다면
                if len(n) != 0 and isFail == False:
                    if (n[-1]) > i.index(j):
                        isFail = True
                n.append(i.index(j))
            else:
                n.append(27)
        if isFail == False:
            answer += 1

    return answer


print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
# print(solution("CBD",["BDA"]))
#     skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
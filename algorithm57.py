def solution(clothes):
    cloth_dic = {}
    for cloth, cloth_type in clothes:
        if cloth_type not in cloth_dic:
            cloth_dic[cloth_type] = 0
        cloth_dic[cloth_type] += 1
    cnt = 1

    print(cloth_dic)
    for i in cloth_dic.values():
        cnt *= (i+1)
    return cnt -1
    

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
            


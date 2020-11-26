def solution(p):
    check_num = 0
    split_point = 0
    is_correct = True


    if len(p) == 0:
        return ""


    for i in range(len(p)):
        if p[i] == '(':
            check_num += 1
        else:
            check_num -= 1
            if check_num < 0:
                is_correct = False

        if check_num == 0:
            split_point = i
            break
    
    u, v = p[:split_point+1], p[split_point+1:]

    if is_correct:
        return u + solution(v)
    else:
        temp1 = '(' + solution(v) + ')'
        temp2 = ''
        for i in u[1:-1]:
            if i == '(':
                temp2 += ')'
            else:
                temp2 += '('
        return temp1 + temp2
# def uv_check(u,v):




print(solution(")("))     
    
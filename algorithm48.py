def solution(name):
    answer = 0
    a = []
    for i in name:
        a.append(min(ord(i)-ord('A'),1+ord('Z')-ord(i)))
    if 'A' not in name:
        answer = len(name)-1 +sum(a)

    i = 0

    if 'A' in name:
        while True:
            answer += a[i]
            a[i] = 0
            if sum(a) == 0:
                break
            left, right = (1,1)
            while a[i-left] <= 0:
                left += 1
            while a[i+right] <= 0:
                right +=1
            
            if left < right:
                answer += left
                i -= left
            else:
                answer += right
                i += right
    return answer
    
    #이제 이동하는것에 대한 경로 수를 더한다.

    

solution("JEAAAOEN")

# 알파벳은 총 26개
# 65로 나눈 나머지를 가지고 탐욕법 적용할꺼고
# 즉 0부터 25까지 총 26개
# 전체 /2 + 1 까지는 앞에서 그외에는 뒤에서 움직이는게 빠르다

# 카운트 한것은 0으로 바꾸고 0이 아닐떄까지 이동하는 경로가 적은곳으로 이동할 것이다.


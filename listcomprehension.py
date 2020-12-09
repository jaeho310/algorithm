# # 1. 1~10까지 짝수 출력하기
# # for문 앞에 list.append시킬 요소를 넣어주면 된다.

# evens = [x * 2 for x in range(6)]
# print(evens)

# # 2. 중첩시키면 두 리스트의 모든 페어를 구할 수 있다.

# a = ['철수', '영희']
# b = ['민수', '민석']

# result = [[i,j] for i in a for j in b]
# print(result)

# # 3. 뒤에 if문을 달아서 조건을 걸어줄 수 있다.
# # 지훈이는 무조건 혼자앉는다고 가정
# a = ['철수', '영희', '지훈']
# b = ['민수', '민석']

# result = [[i,j] for i in a for j in b if '지훈' not in i]
# print(result)

e = [1,0,1,1]

temp = []
temp.append([i for i in e])
print(temp)
# 1. 일반적인 오름차순 정렬

a = [[3,6],[2,6],[1,3],[1,5],[2,1]]
a.sort()
print(a)
print()

# 2. 내부인자의 0번으로 오름차순 1번으로 내림차순으로 정렬

result = sorted(a, key = lambda x: (x[0],-x[1]))
print(result)
print()

# 3. [0]/[1] 의 조건으로도 sort 가능하며 3번째 매개변수에 reverse를 달아주면 역순으로 정렬이 가능하다.
# 탐욕 알고리즘 등에서 자주 활용되며, 가중치를 구하기 용이하다.

result = sorted(a, key = lambda x: (x[0]/x[1]), reverse = True)
print(result)
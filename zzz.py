# import math
# a = [1,3,5,6,2,1]
# b = 4
# c = "abcd"

# d = list(c)
# # print(d)

# # print(a.index(88))

# # print(max(a))

# # q = [(i,p) for i,p in enumerate(a)]
# # print(q)

# # a = [5]
# # print(a

# a.sort(reverse=True)

# print(a)
class Solution:
    def solution(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.solution(n-1) + self.solution(n-2)

a = Solution()
a.solution(3)
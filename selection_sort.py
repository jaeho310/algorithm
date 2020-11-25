def sort(a):
    min_idx = -1
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
            else:
                break
        a[i],a[min_idx] = a[min_idx],a[i]

a = [2,4,1,6,3]
sort(a)
print(a)

# 시간복잡도는 n^2이지만 최선의 경우 n도 나온다.

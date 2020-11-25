def sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1 -i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

a = [3,6,2,77,1,854,34,23,5]
sort(a)
print(a)
            
# 시간복잡도는 n^2으로 느린 편
# 최댓값이나 최솟값을 가장 뒤나 앞으로 옮기면서 정렬하는 기법이다.
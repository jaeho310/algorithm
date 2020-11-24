def sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1 -i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

a = [3,6,2,77,1,854,34,23,5]
sort(a)
print(a)
            
c
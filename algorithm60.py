def solution(arr):
    return list(Recursive(arr))


def Recursive(arr):
    half = int(len(arr)/2)
    temp_zero = 0
    temp_one = 0

    if half == 1:
        for i in arr:
            for j in i:
                if j == 0:
                    temp_zero += 1
                else:
                    temp_one +=1
        
        if temp_one == 4:
            temp_one -= 3
        elif temp_zero == 4:
            temp_zero -= 3

        return temp_zero, temp_one

    upper_arr = arr[:half]
    lower_arr = arr[half:]

    new_arr1 = []
    new_arr2 = []
    new_arr3 = []
    new_arr4 = []
    
    for i in upper_arr:
        new_arr1.append([ i[j] for j in range(0,len(i)//2)])
        new_arr2.append([ i[j] for j in range(len(i)//2,len(i))])

    for i in lower_arr:
        new_arr3.append([ i[j] for j in range(0,len(i)//2)])
        new_arr4.append([ i[j] for j in range(len(i)//2,len(i))])

    return Recursive(new_arr1)+Recursive(new_arr1)+Recursive(new_arr1)+Recursive(new_arr1)
    

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
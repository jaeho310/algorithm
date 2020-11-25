def sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

a = [5,2,1,6,3]
sort(a)
print(a)

# 삽입정렬
# 시간복잡도는 최선의경우 n 평균적으로 n^2이다.
# 앞에서부터 순회하며 데이터를 앞부분에 정렬시키며 진행하는 방법이다.

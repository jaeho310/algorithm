def binary_search(data, search):
    print (data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    
    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)



# 이진탐색
# 정렬된 데이터를 탐색할때 사용하며
# 가운데 값을 기준으로 좌우로 쪼개고 찾는값이 있는부분에서 다시 이진탐색을 진행한다.
# 시간복잡도는 LogN
hash_table = list([0 for i in range(10)])
# [0,0,0,0,0,0,0,0,0,0,0]
# 얘를들어 인덱스값과 테이블을 이용한 해시테이블을 만듬

def hash_func(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

if __name__ == "__main__":
    data1 = 'Andy'
    data2 = 'Dave'
    data3 = 'Trump'
    print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
    print(ord(data1[0]), ord(data1[0]) % 5) # 해쉬주소를 출력
    hash_add = hash_func(ord(data1[0]))
    print(hash_add) # 해쉬주소를 출력

    storage_data('Andy', '010-1111-1111')
    storage_data('Trump', '010-2222-2222')
    storage_data('Dave', '010-3333-3333')

    print(get_data('Andy'))

# def get_key(data):
#     return hash(data)

# def hash_function(key):
#     return key % 8

# def save_data(data, value):
#     hash_address = hash_function(get_key(data))
#     hash_table[hash_address] = value

# def read_data(data):
#     hash_address = hash_function(get_key(data))
#     return hash_table[hash_address]



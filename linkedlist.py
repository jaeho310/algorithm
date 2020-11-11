class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 1. 넣기 메서드. 헤드를 첫번째 위치로 지정하고 마지막 객체까지 접근해준후 next에 객체를 생성과 동시에 넣어준다.
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


# 모든 링크드 리스트 출력
def print_linked_list(head):
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print (node.data)


# 데이터찾기 찾기
def isexsited(target_data):
    node = head
    while node.next:
        if node.data == target_data:
            return True
        node = node.next
    return False

node1 = Node(1)
head = node1
for index in range(2,10):
    add(index)

print_linked_list(node1)
print(isexsited(3))

# 더블 링크드리스트는 next와 pre를 모두 갖고있는 링크드리스트이다.
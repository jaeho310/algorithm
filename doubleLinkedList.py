class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMng:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert_before(self,key,data):
        node = self.tail
        while node.data != key:
            node = node.prev
            if node == self.head:
                print("데이터없음")
                return False
        new = Node(data)
        temp = node.prev
        temp.next = new
        new.prev = temp        
        new.next = node
        node.prev = new

            


double_linked_list = NodeMng(0)
for i in range(1,5):
    double_linked_list.insert(i)

double_linked_list.desc()

print()

double_linked_list.insert_before(2,2.5)

double_linked_list.desc()

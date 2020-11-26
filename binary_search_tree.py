class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class NodeMng:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        
        if searched:
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None
                del self.current_node
            elif self.current_node.left == None and self.current_node.right != None:
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right
            elif self.current_node.left != None and self.current_node.right != None:
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right != None:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None
                    self.parent.left = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.change_node.left
                # case 3-2
                else:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right != None:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None
                    self.parent.right = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left

                    
            


head = Node(1)
BST = NodeMng(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(2))

# 이진탐색트리
# 노드 좌우로 큰수와 작은수를 구분하여 넣는경우 이진탐색트리라고 하며 아닌경우 그냥 이진트리.
# 최악의 경우는 n의 시간복잡도로 링크드리스트와 동일하다. 평균은 LogN이다


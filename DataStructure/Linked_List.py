class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
class NodeMerge:
    def __init__(self,data):
        # Class 호출과 동시에 시작 노드 생성
        self.head = Node(data)
    
    def add(self,data):
        # 혹시 방어 코드
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            # node.next가 None이면 이어지는 노드가 없으니 새로 추가하는 노드 추가
            while node:
                node = node.next
            node.next = Node(data)
            
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head = '':
            print("해당 값을 가진 노드가 없음")
            return
        if self.head == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

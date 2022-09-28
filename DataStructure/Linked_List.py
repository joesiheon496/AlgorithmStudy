class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add(data):
    # 링크드 리스트의 시작점 지정
    node = head
    # 마지막 노드를 찾기위한 작업
    while node.next:
        node = node.next
    # 새로운 노드 추가, 연결
    node.next = Node(data)

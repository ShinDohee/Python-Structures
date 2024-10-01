class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        answer = []  # 결과를 저장할 빈 리스트 생성
        current_node = self.head  # head 노드에서 시작

        while current_node is not None:  # 리스트 끝에 도달할 때까지 반복
            answer.append(current_node.data)  # 현재 노드의 데이터를 answer 리스트에 추가
            current_node = current_node.next  # 다음 노드로 이동

        return answer  # 완성된 리스트 반환

# traverse 함수는 링크드 리스트의 모든 노드를 순회하면서 각 노드의 데이터를 answer 리스트에 추가합니다.
# 마지막에 answer 리스트를 반환하여 리스트의 모든 데이터를 포함하도록 합니다.
# 위의 예시 코드에서는 링크드 리스트를 직접 생성하여 traverse 함수의 결과를 확인할 수 있습니다.

# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0



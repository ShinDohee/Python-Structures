# 1강 리스트

```python
L = ['Bob', 'Cat', 'Spam', 'Programers']
print(L.index('Programers'))
```

------

# 3강 Sort and Search

## Python 리스트의 정렬

### 1. `sorted()`

- 파이썬 내장 함수
- 정렬된 새로운 리스트를 반환함

### 2. `sort()`

- 리스트의 메서드로, 해당 리스트 자체를 정렬함

### 예시

```python
z = [10, 1, 2, 3, 4, 5]
# sorted()를 이용하여 정렬된 새로운 리스트 얻기
L2 = sorted(L)
print(L2)  # [1, 2, 3, 4, 5, 10]
```

### 역순 정렬

- `reverse=True` 옵션을 사용하여 리스트를 역순으로 정렬할 수 있음

```python
L2 = sorted(L, reverse=True)
print(L2)  # [10, 5, 4, 3, 2, 1]
```

### 리스트의 정렬 메서드 사용

```python
A = [3, 2, 7, 1, -13, 4]
A.sort(reverse=True)
print(A)  # [7, 4, 3, 2, 1, -13]
```

### 문자열 리스트의 정렬

- 문자열은 기본적으로 사전 순서대로 정렬됨 (대문자가 우선)
- 문자열 길이 순으로 정렬하고 싶다면 `key`를 설정

```python
Lstr = ['abcd', 'xyz', 'spam']
a2 = sorted(Lstr, key=lambda x: len(x))
print(a2)  # ['xyz', 'spam', 'abcd']
```

### 레코드 정렬 예시

```python
L.sort(key=lambda x: x['name'], reverse=True)
```

------

## 탐색

### 1. 선형 탐색 (Linear Search)

- 앞에서부터 순차적으로 비교하는 방식 (순차탐색)

```python
S = [3, 5, 6, 7, 8, 9]
print(S.index(6))  # 2
```

### 2. 이진 탐색 (Binary Search)

- 이미 정렬된 리스트에서만 사용 가능
- 중간 값을 기준으로 리스트를 반씩 줄여가며 탐색
- 성능 비교 시, 선형 탐색보다 이진 탐색이 효율적임

------

# 4강 재귀 알고리즘

- 하나의 함수에서 자신을 다시 호출하는 방식
- 예시: 이진 트리

### 중요한 점

- 재귀함수에서는 **종결 조건**이 매우 중요함

------

## 과제

### 피보나치 수열

- 재귀와 반복문을 이용해 구현해볼 것

### 참고

- 재귀는 효율성 측면에서 약간 불리할 수 있음
- 하노이의 탑, 이진 탐색을 재귀로 시도해 볼 것



------

- # 7강 연결 리스트 1

  ## 추상적 자료구조

    - **Data** : 정수, 문자열, 레코드,...
    - **A set of operations**
        - 삽입, 삭제, 순회,...
        - 정렬, 탐색,...

  파이썬의 클래스를 사용할 수 있음!

  ### 기본적 연결 리스트 필요 데이터

  예) head, tail, of nodes:3

    - **Node**

        - Data
        - Link(next)

    - **링크드 리스트**

      노드 내의 데이터는 다른 구조로 이루어질 수 있음 (ex: 문자열, 레코드, 또 다른 연결 리스트)

      ```python
      class Node:  # 생성자 노드 
          def __init__(self, item):
              self.data = item
              self.next = None
              
      class LinkedList:  # 생성자 연결 리스트 
          def __init__(self):
              self.nodeCount = 0
              self.head = None
              self.tail = None
      ```

## 연산 정의

![image-20241002012742694](C:\Users\eceri\AppData\Roaming\Typora\typora-user-images\image-20241002012742694.png)

1. **특정 원소 참조**

   ```python
   def getAt(self, pos):
       if pos < 1 or pos > self.nodeCount:
           return None
       i = 1
       curr = self.head
       while i < pos:
           curr = curr.next
           i += 1
       return curr![image-20241002000138281]()
   ```

2. **리스트 순회**

   ```python
   def traverse(self):
       answer = []  # 결과를 저장할 빈 리스트 생성
       current_node = self.head  # head 노드에서 시작
   
       while current_node is not None:  # 리스트 끝에 도달할 때까지 반복
           answer.append(current_node.data)  # 현재 노드의 데이터를 answer 리스트에 추가
           current_node = current_node.next  # 다음 노드로 이동
   
       return answer  # 완성된 리스트 반환
   ```

    - **잘못된 부분**: 초기 코드에서는 `self.getAt(i)`로 접근했지만, `current_node`를 이용해야 함.

3. **길이 얻어내기**

    - `nodeCount`를 이용하면 됨.

4. **원소 삽입**

    - pos가 가리키는 위치에 (1 <= pos <= nodeCount + 1), NewNode 삽입하고 성공/실패에 따라 true/false를 리턴.

    - pos-1과 pos 사이에 `prev`라는 노드를 추가할 예정.

        - pos-1 노드를 `prev`로 정의: `self.getAt(pos - 1)`

        1. new 노드에 뒤쪽 링크

        2. 앞선 노드가 newNode를 가리키고

        3. Node Count에 1 증가

           ** 코드 구현 주의사항

            1. 삽입하려는 위치가 리스트의 맨 앞일 때:
                - `prev` 없음
                - Head 조정 필요 (빈 리스트에 삽입할 때 처리)
            2. 삽입하려는 위치가 리스트 맨 끝, 즉 pos == nodeCount + 1인 경우:
                - `tail` 조정 필요
                - 하지만 맨 앞에서부터 찾아갈 필요는 없다!

   ```python
   def insertAt(self, pos, newNode):
       # 삽입 위치가 유효한지 확인
       if pos < 1 or pos > self.nodeCount + 1: 
           return False  # 유효하지 않으면 False 반환
   
       # 삽입 위치가 첫 번째인 경우
       if pos == 1:
           newNode.next = self.head  # 새 노드의 다음을 현재 head로 설정
           self.head = newNode  # head를 새 노드로 업데이트
   
       else:
           # 삽입 위치가 마지막인 경우
           if pos == self.nodeCount + 1:
               prev = self.tail  # prev를 현재 tail 노드로 설정
           else:
               # 삽입 위치가 중간인 경우
               prev = self.getAt(pos - 1)  # pos-1 노드를 prev로 정의
           newNode.next = prev.next  # 새 노드의 다음을 prev의 다음으로 설정
           prev.next = newNode  # prev의 다음을 새 노드로 업데이트
   
       # 삽입 위치가 마지막인 경우 tail 업데이트
       if pos == self.nodeCount + 1:
           self.tail = newNode  # tail을 새 노드로 업데이트
   
       self.nodeCount += 1  # 노드 수 증가
       return True  # 삽입 성공 시 True 반환
   ```

5. **원소 삭제**

    - pos가 가리키는 위치의 (1 <= pos <= nodeCount) 노드를 삭제하고, 그 노드의 데이터를 리턴!

        1. pos-1 번째 노드(prev)로 정의

        2. curr을 뽑고, prev.next <- curr.next로 바꿔줌

        3. node.Count - 1 해줌

           ** 삭제하려는 노드가 맨 앞일 때. ** 리스트 맨 끝의 노드를 삭제할 때. (즉, pos == nodeCount인 경우는? 한번에 처리할 수 없다. prev를 찾을 방법이 없으므로. 그래서 앞에서부터 찾아와야 함! 선형적 탐색이 필요.)

           if) 유일한 노드를 삭제할 때? 이 조건에 의해 처리가 되는가?

   ```python
   def popAt(self, pos):
       if pos < 1 or pos > self.nodeCount:
           raise IndexError
   
       if pos == 1:  # 첫 번째 노드를 삭제하는 경우
           curr = self.head
           self.head = curr.next
           if self.nodeCount == 1:  # 리스트에 하나만 있던 노드를 삭제하는 경우
               self.tail = None
   
       else:  # 중간이나 마지막 노드를 삭제하는 경우
           prev = self.getAt(pos - 1)
           curr = prev.next
           prev.next = curr.next
           if pos == self.nodeCount:  # 마지막 노드를 삭제하는 경우
               self.tail = prev
   
       self.nodeCount -= 1
       return curr.data
   ```

6. **두 리스트 합치기**

   ```python
   def concat(self, L):
       # 현재 리스트의 tail의 다음 노드를 L 리스트의 head로 연결
       self.tail.next = L.head  
       
       # L 리스트의 tail이 None이 아닌 경우
       if L.tail:  # 뒤에 붙는 리스트에 tail이 None일 경우 체크
           self.tail = L.tail  # 현재 리스트의 tail을 L 리스트의 tail로 업데이트
       
       # 현재 리스트의 노드 수에 L 리스트의 노드 수를 추가
       self.nodeCount += L.nodeCount  
   ```

------

## 배열과 비교한 연결 리스트

- **저장 공간**: 배열 (연속한 위치) / 연결 리스트 (임의의 위치)
- **특정 원소 지칭**: 배열 (매우 간편) O(1) / 연결 리스트 (선형 탐색과 유사) O(n)

------

# 10강 양방향 연결 리스트 (이중 연결 리스트, Doubly Linked List)

- 한쪽으로만 링크를 연결하지 말고, 양쪽으로 연결!

    - 앞으로도 다음 노드/ 뒤로도 이전 노드 진행 가능.

      ```python
      class Node:
          def __init__(self, item):
              self.data = item
              self.prev = None
              self.next = None
      ```

- 리스트 처음과 끝에 dummy node를 두자!

  ```python
  class DoublyLinkedList:
      def __init__(self):
          self.nodeCount = 0
          self.head = Node(None)
          self.tail = Node(None)
          self.head.prev = None
          self.head.next = self.tail
          self.tail.prev = self.head
          self.tail.next = None
  ```

- 양방향 리스트 순회

  ```python
  def traverse(self):
      result = []
      curr = self.head
      while curr.next.next:
          curr = curr.next
          result.append(curr.data)
      return result
  ```

- 리스트 역순회

  ```python
   def reverse(self):
      result = []
      curr = self.tail
      while curr.prev.prev:
          curr = curr.prev
          result.append(curr.data)
      return result
  ```

- 원소 삽입

    - 삽입할 노드의 `prev` -> 그 앞 노드
    - 삽입할 노드의 `next` -> 그 뒤 노드
    - 그리고 그 전 노드의 `next` -> 새로운 노드
    - 그 뒤 노드의 `prev` -> 새로운 노드 지정하고
    - 마지막으로 `nodeCount` +1

  if) 리스트 마지막에 원소 삽입하면? ==> 리스트가 길어지면 부담스러움

  --> 이럴 땐 `getAt` 메소드를 수정하여 구현해봄

  ```python
  def insertAfter(self, prev, newNode):
      next = prev.next
      newNode.prev = prev
      newNode.next = next 
      prev.next = newNode
      next.prev = newNode
      self.nodeCount += 1
      return True
  
  def insertAt(self, pos, newNode):
      if pos < 1 or pos > self.nodeCount + 1:
          return False
  
      prev = self.getAt(pos - 1)
      return self.insertAfter(prev, newNode)
      
  def getAt(self, pos):  # 특정 원소 얻어내기 (전 강의와 완전 동일)
      if pos < 0 or pos > self.nodeCount:
          return None
  
      if pos > self.nodeCount // 2:
          i = 0
          curr = self.tail
          while i < self.nodeCount - pos + 1:
              curr = curr.prev
              i += 1
      else:
          i = 0
          curr = self.head
          while i < pos:
              curr = curr.next
              i += 1
  ```


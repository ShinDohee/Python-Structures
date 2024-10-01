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
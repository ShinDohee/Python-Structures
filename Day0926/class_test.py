#1강 리스트 탐색
L = ['Bob', 'Cat', 'Spam', 'Programers']
print(L.index('Programers'))


#3강 sort , search
# python 리스트의 정렬
# 1. sorted() - 파이썬의 내장함수, 정렬된 새로운 리스트를 얻어낼 수 있음
# 2. sort() -> 리스트의 메서드 / 해당 리스트를 정렬
# 쓰는 방법 잘 숙지 할 것!

L = [10, 1, 2, 3, 4, 5]
# L2 = sorted(L)
# 내장함수기 때문에 sorte() 를 구현하지 않고 바로 사용 가능하다
# print(L2)

A = [3, 2, 7, 1, -13, 4]
# A.sort()
# print(A)


# 정렬의 순서를 반대로
# reverse=True

L2 = sorted(L, reverse=True)
A.sort(reverse=True)
print(L2)
print(A)

# 문자열로 이루어진 리스트는 -. 정렬수서는 사전순서를 따름 ( 대문자가 무조건 우선)
# if 문자열 길이 순서로 정렬 하려면 ??
# 정렬에 이용하는 키를 지정

Lstr = ['abcd', 'xyz', 'spam']
a2 = sorted(Lstr, key=lambda x:len(x))
print(a2)

# L.sort(key=lamda x:x['name'], reverse=True)
#-> 레코드들 이름 순서대로 정렬 하는 방법

#탐색
# 1. 선형 탐색 -> 앞에서부터 순차적으로 비교 하는 방법 (= 순차탐색)

S = [3, 5, 6, 7, 8, 9]
print(S.index(6))


# 2.이진탐색
# 이미 정렬되어 있는 경우에만 적용가능
# 크기순으로 정렬되어 있다는 성질 이용
# 한번에 비교가 일어날때마다 리스트 반씩줄어짐
# 성능 비교 ==> 선형탐색보다 이진 탐색이 더 효율 좋음



# 4강 재귀 알고리즘
# 하나의 함수에서 자신을 다시 호출하는 것
# ex) 이진트리
# 재귀함수에서는 종결 조건이 매우 중요함
### ! 과제 피보나치 수열 재귀랑/반복문으로 구현

# 재귀는 효율성 측면에서는 약간 불리할 수 있음
#하노이의 탑!
# 재귀함수 -> 이진 탐색 시도 해 볼것!


# Node   ( data , link(next) )
# 1. 특정 원소 참조
#2. 리스트 순회
#3. 길이 얻어내기
#4. 원소 삽입
#5. 우너소 삽게
# 두 리스트 합치기
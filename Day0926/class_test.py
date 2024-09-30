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
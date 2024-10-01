# 피보나치 수열 재귀로 표현
# def solution(x):
#     if x==0:
#         return 0
#     elif x==1:
#         return 1
#     else:
#         return solution(x-1) + solution(x-2)

# 재귀적 이진 탐색

def solution1(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution1( L,x,l,mid-1 )
    else:
        return solution1( L,x,mid+1,u )

L = [2, 5, 7, 9, 11]
x = 4
l = 0
u = 4

print(solution1(L, x, l, u))
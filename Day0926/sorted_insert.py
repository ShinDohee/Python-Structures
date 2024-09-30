
# 2강 선형배열( linear Array)
def solution(L, x):
    for i in range(len(L)):
        if L[i] > x:
            L.insert(i, x)
            return L

    L.append(x)
    return L


result = solution([20, 37, 58, 72, 91], 65)
print(result)


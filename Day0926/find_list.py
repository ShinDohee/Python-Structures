
# 2강 새로운 요소 삽입학/ 찾아내기.
def solution(L, x):
    answer = []

    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)

    if not answer:
        return [-1]

    return answer


result = solution([64, 72, 83, 72, 54],  72)
print(result)
# 1리스트 원소 두개의 합 구하기
def solution(x):
    return x[0] + x[-1]

# 리스트를 입력 값으로 전달
result = solution([5, 3, 7, 1])
print(result)  # 첫 번째 값(5) + 마지막 값(1) = 6

# 문자열을 입력 값으로 전달
result = solution("Python")
print(result)  # 첫 번째 문자('P') + 마지막 문자('n') = 'Pn'

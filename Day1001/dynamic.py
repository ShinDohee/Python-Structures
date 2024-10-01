def solution(N, number):
    # 1. 숫자 N을 이용해 만들 수 있는 숫자들을 저장할 리스트 s 생성 (8개의 집합 생성)
    s = [set() for x in range(8)]  # N을 최대 8번까지 사용해서 만들 수 있는 숫자를 저장할 집합 리스트

    # 2. N을 1번부터 8번까지 이어붙인 숫자들을 각 집합에 추가
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))  # N을 i번 반복한 숫자를 해당 집합에 추가 (예: N, NN, NNN 등)

    # 3. i번째 집합을 채우면서 목표 숫자 number를 찾는 과정 (i는 0부터 시작)
    for i in range(len(s)):  # N을 i+1번 사용했을 때의 경우를 다룸
        # 4. 집합을 두 부분으로 나누어 계산 (분할정복 방식)
        for j in range(i):  # j는 첫 번째 부분의 연산을 담당하는 인덱스
            for op1 in s[j]:  # 첫 번째 집합에서 가능한 숫자 op1을 순차적으로 가져옴
                for op2 in s[i - j - 1]:  # 두 번째 집합에서 가능한 숫자 op2를 순차적으로 가져옴
                    # 5. 각각의 연산 수행 (덧셈, 뺄셈, 곱셈, 나눗셈)
                    s[i].add(op1 + op2)  # op1 + op2의 결과를 i번째 집합에 추가
                    s[i].add(op1 - op2)  # op1 - op2의 결과를 i번째 집합에 추가
                    s[i].add(op1 * op2)  # op1 * op2의 결과를 i번째 집합에 추가
                    if op2 != 0:  # 나눗셈의 경우, op2가 0이 아닐 때만 수행
                        s[i].add(op1 // op2)  # op1 // op2의 결과를 i번째 집합에 추가

        # 6. 만약 목표 숫자 number가 현재 i번째 집합에 있다면, 답을 구한 것으로 처리
        if number in s[i]:
            answer = i + 1  # i는 0부터 시작하므로 실제로는 i+1번 사용했음을 의미
            break  # 목표 숫자를 찾았으므로 더 이상 연산할 필요 없이 루프 종료

    # 7. 만약 8번 사용해도 목표 숫자를 찾지 못했을 경우, -1 반환
    else:
        answer = -1  # 목표 숫자를 만들 수 없을 때 -1 반환

    return answer  # 최종적으로 answer를 반환

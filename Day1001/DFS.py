def solution(tickets):
    # routes라는 사전을 만들어 항공권의 출발 공항을 키, 도착 공항을 값으로 저장
    routes = {}

    # 주어진 항공권 목록을 순회하며, 출발 공항을 키로 하고 도착 공항 리스트를 값으로 저장
    for t in tickets:
        # routes.get(t[0], [])는 t[0]이라는 키가 존재하지 않으면 빈 리스트를 반환하고, 도착 공항을 리스트에 추가
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        # 출발 공항이 키가 되고, 갈 수 있는 도착 공항들이 리스트로 추가됨

    # 각 출발 공항에 대해, 도착 공항 리스트를 역순으로 정렬
    # 스택 방식으로 뒤에서부터 도착지를 처리하므로, 역순 정렬이 효율적
    for r in routes:
        routes[r].sort(reverse=True)

    # "ICN"을 시작점으로 하는 스택을 생성
    stack = ["ICN"]

    # 경로를 저장할 리스트
    path = []

    # 스택이 비어있지 않은 동안 반복
    while len(stack) > 0:
        # 스택의 맨 위 공항을 가져옴 (현재 위치)
        top = stack[-1]

        # 만약 top 공항이 routes에 없거나, 더 이상 갈 수 있는 도착 공항이 없는 경우
        if top not in routes or len(routes[top]) == 0:
            # 현재 공항을 경로에 추가하고 스택에서 제거 (여행이 끝난 공항)
            path.append(stack.pop())
        else:
            # 갈 수 있는 공항이 남아 있는 경우, 그 공항을 스택에 추가
            stack.append(routes[top][-1])
            # 도착 공항을 스택에 추가한 후, 해당 공항을 리스트에서 제거
            routes[top] = routes[top][:-1]

    # 경로가 스택에서 역순으로 추가되었으므로, 최종적으로 경로를 뒤집어서 반환
    return path[::-1]




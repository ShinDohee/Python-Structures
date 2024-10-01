import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break;

        min2 = heapq.heappop(scoville)
        X = min1 + 2 * min2
        heapq.heappush(scoville, X)
        answer += 1

    return answer
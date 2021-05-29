import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        cnt += 1

        if scoville[0] > K: return cnt
        if len(scoville) == 1 and scoville[0] < K: return -1

scoville = list(map(int,input().split()))
K = int(input())
print(solution(scoville,K))
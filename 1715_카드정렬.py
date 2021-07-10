# 반례를 생각하지 못했다 - 합친 카드 팩과 다른 것을 비교할때 다른 두개가 더 작을경우
# 그 두개 먼저 비교해야하는데 그 경우를 생각하지 못했다.
# 시간복잡도가 너무 크게나와 우선순위 큐를 힙으로 구현하여 사용하기로 했다.
import sys
import heapq
N = int(input())
data = []
for i in range(N):
    heapq.heappush(data, int(sys.stdin.readline()))

result = 0
if len(data) == 1:  # data 가 1개일 경우 비교할 필요 없음
    print(0)
else:
    while len(data) > 1:
        temp_1 = heapq.heappop(data)
        temp_2 = heapq.heappop(data)
        result += temp_1+temp_2
        heapq.heappush(data, temp_1+temp_2)
    print(result)
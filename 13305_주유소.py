# 포인트는 방문한 곳 중 가장 기름이 싼 곳에서 산 기름으로 나머지 거리를 운행하는 것
import sys
N = int(input())  # 도시의 개수
d = list(map(int, sys.stdin.readline().split()))  # index 도시 사이의 거리
c = list(map(int, sys.stdin.readline().split()))  # index 도시의 기름 값
cost = 0  # 총 필요한 기름 값
minimum = c[0]  # 방문한 도시 중 가장 낮은 기름 값
for i in range(N-1):
    if minimum > c[i]:  # 가장 기름 값이 싼 도시의 기름 값 갱신
        minimum = c[i]
    cost += d[i]*minimum  # distance와 cost를 곱해서 더해주기
print(cost)

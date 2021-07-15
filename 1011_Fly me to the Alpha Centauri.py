import sys
# 테스트 케이스 입력
T = int(input())
# 각 테스트 케이스의 현재 위치와 목표 위치 저장
distance = []
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance.append(y-x)  # 각 케이스에 이동해야하는 거리를 저장

for i in range(T):
    count = 0
    k = 1  # 처음 이동 거리
    total = 0  # 총 이동 거리
    while total < distance[i]:
        count += 1
        total += k
        if count % 2 == 0:
            k += 1
    print(count)
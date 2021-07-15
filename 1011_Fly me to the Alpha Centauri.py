import sys
# 테스트 케이스 입력
T = int(input())
# 각 테스트 케이스의 현재 위치와 목표 위치 저장
L = [None]*T
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    L[i] = [x,y]

for i in range(T):
    count = 0
    # 작동 시 이동 거리
    k = 1
    while True:  # (현재 위치)와 (목표 위치-1) 이 같아지면
        L[i][0] += k    # count 에 1만 더하고 break
        count += 1
        k += 1
        if L[i][0] >= L[i][1]:  # 넘어서면
            count += 1
            print(count)
            break
        elif L[i][0] == L[i][1]-1: # 딱 되면
            count += 1
            print(count)
            break



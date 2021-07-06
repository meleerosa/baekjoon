# 지불 할 돈
N = int(input())
# 거스름 돈
P = 1000-N
# 잔돈 개수
k=0
C = [500, 100, 50, 10, 5, 1]
for c in C:
    k += P//c
    P = P%c
print(k)
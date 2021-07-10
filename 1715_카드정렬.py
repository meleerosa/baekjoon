# a b c d 장의 카드를 서로 비교하는 과정에서는
# (a+b) + (a+b+c) + (a+b+c+d) 번의 비교가 필요하다
# 4팩의 카드에서 3a+3b+2c+1d가 필요한 것이다.

import sys
N = int(input())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

result = -data[0]
for i in range(len(data)):
    result += (len(data)-i)*data[i]

print(result)
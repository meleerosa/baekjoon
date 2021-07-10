# 반례를 생각하지 못했다 - 합친 카드 팩과 다른 것을 비교할때 다른 두개가 더 작을경우
# 그 두개 먼저 비교해야하는데 그 경우를 생각하지 못했다.

import sys
N = int(input())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
result = 0
for i in range(N):
    if len(data) >= 2:
        data.sort(reverse=True)  # 시간복잡도, pop쓰기위해 거꾸로 정렬
        a = data.pop()
        b = data.pop()
        result += a+b
        data.append(a+b)
    else: pass
print(result)
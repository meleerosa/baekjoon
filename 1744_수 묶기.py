import sys
N = int(input())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
ans = 0

while True:
    if len(data) == 0:
        break
    elif len(data) == 1:
        ans += data.pop()
    else:
        a = data.pop()
        b = data.pop()
        if a*b > 0:
            ans += a*b
        elif a*b == 0:
            if a+b > 0:
                ans += a+b
        else:
            ans += a+b
print(ans)

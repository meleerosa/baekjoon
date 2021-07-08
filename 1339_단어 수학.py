import sys
N = int(input())
data = [sys.stdin.readline().strip() for i in range(N)]
data.sort(key=lambda x: len(x), reverse=True)  # 입력 data를 길이가 긴 순으로 정렬
sumation = []
a = {}
v = 9
for i in range(N):
    for j in data[i]:
        if j not in a:
            a[j] = str(v)
            j = v
            v -= 1

for i in range(N):
    sumation.append([])
    for j in data[i]:
        sumation[i].append(a.get(j))
    sumation[i] = "".join(sumation[i])

sum = 0
for i in range(N):
    sum += int(sumation[i])
print(sum)
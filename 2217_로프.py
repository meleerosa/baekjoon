# 임의의 로프 몇개를 골라서 w의 하중 버티기
# 반례 잘 생각하기 - 모든 로프를 선택할 필요는 없음
N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
W = 0
for i in range(len(rope)):
    temp = rope[i]*(i+1)
    if temp > W:
        W = temp
print(W)
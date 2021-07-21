N = int(input())  # 저울 추의 개수
M = list(map(int,input().split(' ')))  # N개 저울 추 각각의 무게
M.sort()

# 주어진 추들로 측정할 수 없는 양의 정수 무게 중 최솟값 출력
ans = 1
for i in range(N):
    if ans < M[i]:
        break
    ans += M[i]
print(ans)
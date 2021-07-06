# N개의 동전으로 K의 가치 만들기
N, K = input().split()
N, K = int(N), int(K)
C = []
for i in range(N):
    C.append(int(input()))

# K를 동전의 가치로 나눠 몫을 다 더함
# 나눌 수 있는 가장 큰 동전 가치부터 나누기 시작
coin = 0
for i in range(N-1, -1, -1):
    q = K//C[i]  # 몫 저장
    K = K-q*C[i]  # K값 갱신
    coin += q
print(coin)

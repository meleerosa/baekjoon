#N은 사람 수
#P1,P2,P3,P4,P5는 각 사람이 돈을 인출하는데 걸리는 시간
N=int(input())
P= list(map(int,input().split())) #사람 수에 따라 인출하는데 걸리는 시간 리스트에 저장
P=sorted(P) #인출하는데 걸리는 시간 정렬
T=[None]*N #각 사람이 돈을 인출하는데 걸리는 시간 리스트에 저장
for i in range(N):
    T[i]=sum(P[0:i+1]) #앞사람들 시간 + 자기 시간
print(sum(T))
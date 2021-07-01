# N킬로의 설탕을 3킬로그램 봉지와 5킬로그램 봉지로 나눠서 저장
# 최소 봉지 수 구하기
N=input()
N=int(N)
a=-1  #answer 저장
for i in range(round(N/5)+1): #i는 5킬로 봉지의 개수
    for j in range(round((N/3)+1)): #j는 3킬로 봉지의 개수
        if N==5*i+3*j:
            a=i+j

print(a)

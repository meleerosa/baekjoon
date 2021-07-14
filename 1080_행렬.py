count = 0
N,M = map(int,input().split())

change_maps = [list(map(int,input())) for _ in range(N)]
result_maps = [list(map(int,input())) for _ in range(N)]

# 3X3 행렬을 변환 0->1, 1->0 으로
def convert3x3(x,y,arr):
    for i in range(x,x+3):
        for j in range(y,y+3):
            change_maps[i][j] = 1 - change_maps[i][j]

for i in range(0,N-2):
    for j in range(0,M-2):
        if change_maps[i][j] != result_maps[i][j]: # 배열의 값이 같지 않다
            convert3x3(i,j,change_maps)
            count += 1

# 전체 배열 검사
nonResult = False
for i in range(0,N):
    for j in range(0,M):
        if change_maps[i][j] != result_maps[i][j]:
            nonReulst = True

if nonResult:
    print(-1)
else:
    print(count)

import sys
import numpy as np
# n행 m열의 행렬을 저장하기
N, M = map(int, sys.stdin.readline().split())
A = []
B = []
for i in range(N):
    a = sys.stdin.readline().rstrip()
    A.append(list(a))
for i in range(N):
    b = sys.stdin.readline().rstrip()
    B.append(list(b))
A = np.array(A).reshape(N, M)
B = np.array(B).reshape(N, M)

# x행,y열의 원소부터 3x3 부분 행렬의 원소를 변환하기
def convert(x, y):
    for i in range(3):
        for j in range(3):
            if A[i+x][j+y] == '1':
                A[i+x][j+y] = '0'
            else:
                A[i+x][j+y] = '1'

count = 0

while not np.array_equal(A, B):
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                convert(i,j)
                count += 1
print(count)
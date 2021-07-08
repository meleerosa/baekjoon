# 어떤 지원자의 두 성적이 다른 어떤 지원자보다 낮으면 선발되지 않는다.
# 시간 초과가 나와서 다른 방법으로 생각해보기로 했다. - 차원 수 낮추기, sys.stdin.readline()쓰기
import sys
T = int(input())  # test case 의 개수
grade = []
for i in range(T):
    grade.append([])  # 서류심사 케이스 석차 리스트
    N = int(input())  # 지원자의 숫자
    for j in range(N):  # 지원자의 석차1, 석차2
        a, b = list(map(int, sys.stdin.readline().split()))
        grade[i].append([a,b])
for i in grade:
    count = 1  # 1등은 미리 포함
    i.sort(key=lambda x: x[0])  # i가 none type이 되어서 새로 반복문 만듦
    max = i[0][1]  # 합격할 수 있는 최소 석차
    for j in i:
        if max > j[1]:
            count += 1
            max = j[1]  # 합격할 수 있는 최소 석차 갱신
    print(count)
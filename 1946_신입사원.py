# 어떤 지원자의 두 성적이 다른 어떤 지원자보다 낮으면 선발되지 않는다.
T = int(input())  # test case 의 개수
grade1 = []  # 서류심사
grade2 = []  # 면접심사

for i in range(T):
    grade1.append([])  # 서류심사 케이스 석차 리스트
    grade2.append([])  # 면접심사 케이스 석차 리스트
    N = int(input())  # 지원자의 숫자
    for j in range(N):  # 지원자의 석차1, 석차2
        a, b = list(map(int, input().split()))
        grade1[i].append(a)
        grade2[i].append(b)

# 각 심사의 가장 높은 석차를 받은 지원자의 다른 심사에서 받은 석차보다
# 낮은 석차를 기록한 지원자는 무조건 떨어진다.
# 반례는 겹치는 지원자
for i in range(T):
    count = set()
    index_1 = grade1[i].index(1)
    index_2 = grade2[i].index(1)
    for j in range(len(grade2[i])):
        if grade2[i][index_1] < grade2[i][j]:
            count.add(j)
    for j in range(len(grade1[i])):
        if grade1[i][index_2] < grade1[i][j]:
            count.add(j)
    print(len(grade1[i]) - len(count))


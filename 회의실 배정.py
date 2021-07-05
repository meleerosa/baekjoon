N = int(input())  # 회의의 수
conf = []  # 회의의 정보
m_conf = []  # 최대로 회의
for i in range(N):
    start, end = map(int, input().split())
    conf.append([start, end])

# 회의의 시작시간과 끝나는 시간이 같을 수 있어 시작시간으로 먼저 정렬
conf.sort(key=lambda x: x[0])
# 끝나는 시간으로 정렬
conf.sort(key=lambda x: x[1])


# 끝나는 시간 순으로 m_conf 에 겹치지 않게 삽입
m_conf.append(conf[0])
for i in range(1, N):
    if conf[i][0] >= m_conf[-1][1]:  # 다음 회의시작 시간이 끝나는 시간보다 느려야함
        m_conf.append(conf[i])
print(len(m_conf))
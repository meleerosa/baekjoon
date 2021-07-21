N = int(input())  # 저울 추의 개수
M = list(map(int,input().split(' ')))  # N개 저울 추 각각의 무게
M.sort()

# 주어진 추들로 측정할 수 없는 양의 정수 무게 중 최솟값 출력

# 출력 가능 여부 조사
def measurable(x):
    weight = [m for m in M if m<=x]  # x보다 작거나 같은 무게추
    weight.sort()
    tmp = 0
    while True:
        p = weight.pop()
        tmp += p
        if tmp > x:
            tmp -= p
        elif tmp == x:
            return True
        elif len(weight) == 0:
            return False

ans = 1
while True:
    if not measurable(ans):
        print(ans)
        break
    ans += 1



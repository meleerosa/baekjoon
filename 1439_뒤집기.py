S = input()

# 뒤집어야 하는 횟수 세기
reverse_count_0 = 0  # 0을 뒤집어야하는 횟수
reverse_count_1 = 0
tmp = '2'  # 이전 문자와 비교하기위해 잠시 저장
for i in S:
    if i == '0' and tmp != i:  # 이전 문자와 비교하여 바뀌면 count
        reverse_count_0 += 1
    elif i == '1' and tmp != i:
        reverse_count_1 += 1
    tmp = i

print(min(reverse_count_0,reverse_count_1))
T = int(input())
count_a = 0
count_b = 0
count_c = 0
count_a += T//300
T = T % 300
count_b += T//60
T = T % 60
count_c += T//10
T = T % 10
if T != 0:
    print(-1)
else:
    print(count_a, count_b, count_c)

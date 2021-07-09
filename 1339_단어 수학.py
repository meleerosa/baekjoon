import sys
N = int(input())
data = []
for i in range(N):  # data 에 입력받은 문자열을 리스트로 정렬
    data.append(list(sys.stdin.readline()))
    data[i].pop()

# 높은 자리수의 알파벳에 높은 숫자 배정하여 딕셔너리에 저장
a = {}
for i in data:
    k = len(i)-1
    for j in i:
        if j in a:  # 만약 딕셔너리에 이미 있으면
            a[j] += pow(10, k)  # 자릿수만큼 곱한것 더함
        else:
            a[j] = pow(10, k)  # 딕셔너리에 추가
        k -= 1
nums = []
for value in a.values():
    nums.append(value)

# 숫자 큰 순으로 정렬하기
nums.sort(reverse=True)
# 결과와 곱해야하는 수 초기화 하기
result, t = 0,9
# 값 구하기
for i in range(len(nums)):
    result += nums[i]*t
    t -= 1
print(result)
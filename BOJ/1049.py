# 기타줄 개수 n
# 기타줄 브랜드 m
# 각 브랜드에서 파는 6개 기타 줄 패키지의 가격, 낱개의 가격
# (6줄 패키지 사거나 1개 or 그 이상의 줄 낱개로 사거나)
# 적어도 n개를 사기 위해 필요한 돈의 수

n, m = map(int, input().split())
six_list = []
one_list = []
ans = 0

for _ in range(m):
    six, one = map(int, input().split())
    six_list.append(six)
    one_list.append(one)

six_list.sort()
one_list.sort()

if six_list[0] <= one_list[0] * 6:
    ans = six_list[0] * (n // 6) + one_list[0] * (n % 6)
    if six_list[0] < one_list[0] * (n % 6):
        ans = six_list[0] * (n // 6 + 1)
else:
    ans = one_list[0] * n

print(ans)

# // 몫
# %  나머지
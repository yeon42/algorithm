# 11-5. 볼링공 고르기

n, m = map(int, input().split()) # 개수, 최대 무게
k = map(int, input().split()) # 무게

data = [0] * 11 # 0 ~ 10

for i in k:
    data[i] += 1

cnt = n*(n-1) // 2

for i in data:
    if i>=2:
        cnt -= i*(i-1) // 2

print(cnt)

'''
1, 2, 2, 3, 3
'''
# 잔돈: 500, 100, 50, 10, 5, 1
# 거스름돈 개수가 가장 적게 잔돈을 줌
# 1000엔 한 장을 냈을 때 받을 잔돈에 포함된 잔돈의 개수?

give = int(input()) # 지불할 돈
money = 1000 - give

subs = [500, 100, 50, 10, 5, 1]
ans = 0

for s in subs:
    ans += money // s
    money %= s

print(ans)
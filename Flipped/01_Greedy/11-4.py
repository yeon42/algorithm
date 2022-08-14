# 11-4. 만들 수 없는 금액

n = int(input())
coin = map(int, input().split())
coin.sort()

target = 1
for x in coin:
    if x > target:
        break # for문 종료
    target += x

print(target)

'''
1, 1, 2, 3, 9

target = 1, 2, 3, 5, 8
'''
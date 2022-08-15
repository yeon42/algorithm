# 동전 n종류
# 그 합을 k로 만드는데 필요한 동전 개수 최솟값

n, k = map(int, input().split())
worth = []
for _ in range(n):
    a = int(input())
    worth.append(a)

worth.sort()
worth.reverse()

ans = 0

for w in worth:
    if w <= k: # 1000 <= 4200
        ans += k//w
        k %= w

print(ans)
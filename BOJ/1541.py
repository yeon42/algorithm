s = input().split('-') # 마이너스로 분리

# print(s)

ans = 0
for i in s[0].split('+'):
    ans += int(i)

for i in s[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)
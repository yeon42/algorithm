s = input()

prev = '?'
cnt = 0

for i in s:
    if i != prev:
        prev = i
        cnt += 1

print((cnt)//2)
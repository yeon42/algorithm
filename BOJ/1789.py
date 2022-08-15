import math

s = int(input())

new_s = int(math.sqrt(s*2))

for n in range(new_s, 0, -1):
    if s >= n*(n+1)/2:
        if s <= (n+1)*(n+2)/2:
            print(n)
            break
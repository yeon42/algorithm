# 2 위, 1 오른쪽
# 1 위, 2 오른쪽
# 1 아래, 2 오른쪽
# 2 아래, 1 오른쪽

# 방문한 칸의 수 최대
# 이동 횟수 >= 5: 이동 방법 모두 한 번씩 사용해야 함
# 이동 횟수 <= 4: 이동 방법 제약 x

# 방문할 수 있는 칸의 최대 개수
# n: 세로, m: 가로

n, m = map(int, input().split())
ans = 0

if n == 1:
    ans = 1
elif n == 2: # 2, 3번
    ans = min(4, 1 + (m-1)//2)
elif m <= 6:
    ans = min(4, m)
else: # 오른쪽 2번
    ans = m-2

print(ans)


'''
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X


X X X X X X
X X X X X X
X X X X X X

X X X X X
X X X X X

X X X X X X X
X X X X X X x


X X X X X X X
X X X X X X X
'''

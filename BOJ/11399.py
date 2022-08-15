# i번 사람 돈 인출하는데 걸리는 시간 P_i분
# 각 사람이 돈을 인출하는데 걸리는 시간의 합 최소 구하기

# 1 2 3 4 5 인덱스
# 3 1 4 3 2 시간

# 2 5 1 4 3
# 1 2 3 3 4

n = int(input())
time = list(map(int, input().split()))
ans = 0

time.sort()
for i, t in enumerate(time):
    ans += (len(time) - i) * t

print(ans)
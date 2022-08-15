# 1개의 회의실 & N개의 회의
# 각 회의 겹치지 않게 회의실 사용할 수 있는 회의의 최대 개수

n = int(input())
meeting = []

for _ in range(n):
    meet = list(map(int, input().split())) # 시작시간, 끝나는 시간
    meeting.append(meet)

meeting.sort(key=lambda x: (x[1], x[0])) # 빨리 끝나는 시간대로 정렬
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

ans = 0
end = 0
for s, e in meeting:
    if s >= end:
        ans += 1
        end = e

print(ans)
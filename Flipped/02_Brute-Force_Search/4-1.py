# 4-1. 상하좌우

'''
NxN 크기의 정사각형 공간
- 가장 왼쪽 위: (1, 1) / 가장 오른쪽 아래: (N, N)

여행가 A는 상하좌우로 이동동할 수 있으며 시작 좌표는 (1, 1).
- 정사각형 공간 벗어나는 움직임은 무시됨

- L: 왼쪽으로 한 칸 이동
- R: 오른쪽으로 한 칸 이동
- U: 위로 한 칸 이동
- D: 아래로 한 칸 이동

계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램 작성하기
'''

'''
Q(4-1)
- 첫째 줄: 공간의 크기 N
- 둘째 줄: A가 이동할 계획서 내용
- 출력: A가 도착할 지점 좌표 (X, Y)
'''


n = int(input()) # 공간 크기 N
plans = input().split() # 계획서

x, y = 1, 1 # 시작 위치

# L, R, U, D에 따른 이동 방향
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1] 
dy = [-1, 1, 0, 0]

# 이동 계획 하나씩 확인
for p in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if p == move_types[i]: # 같으면
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)


'''
주의할 점
- 우리가 흔히 아는 좌표계와 다름
- L은 y좌표가 1 감소, R은 y좌표가 1 증가
- U은 x좌표가 1 감소, D은 x좌표가 1 증가
'''
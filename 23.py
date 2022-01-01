# %% 2차워 리스트
a = [[10, 20], [30, 40], [50, 60]]
a



# %%
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0])
print(a[1][0])



# %% 톱니형 리스트
a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a



# %%
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)



# %%
a = [[10, 20], [30, 40], [50, 60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print() # 엔터키



# %%
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i<len(a):
    x, y = a[i] # 요소 2개 한꺼번에 가져오기
    print(x, y)
    i += 1



# %% 반복문으로 리스트 생성
a = []
for i in range(10):
    a.append(0)
print(a)



# %%
a = []
for i in range(3):
    line = [] # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)



# %%
a = [[0 for j in range(2)] for i in range(3)]
a




# %% 톱니형 리스트 생성
a = [3, 1, 3, 2, 5]
b = []

for i in a: # 바깥쪽 리스트
    line = []
    for j in range(i): # 안쪽 리스트
        line.append(0)
    b.append(line)

print(b)



# %%
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500 # a, b에 모두 반영
print(a)
print(b)



# %%
a = [[10, 20], [30, 40]]
b = a.copy() # 마찬가지로 모두 반영
b[0][0] = 500
print(a)
print(b)



# %%
import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a) # copy.deepcopy로 깊은 복사
b[0][0] = 500
print(a)
print(b)



# %% 23.6 연습문제: 3차원 리스트 만들기
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)



# %% 23.7 심사문제: 지뢰찾기
# col: 가로, row: 세로
col, row = map(int, input().split())

matrix = []
for i in range(row): # 세로줄 개수만큼 입력
    matrix.append(list(input()))

cnt = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if 0<=a<row and 0<=b<col and matrix[a][b] == '*':
                        cnt += 1
            print(cnt, end='')
            cnt = 0
        else:
            print(matrix[i][j], end='')
    print() # 엔터





# %% 다른 분 풀이 !!!!!!!

x,y = map(int, input().split())

matrix = []
for i in range(y):
    matrix.append(list(input()))

for i in range(y):
    for j in range(x):
        count = 0
        if matrix[i][j] == ".":
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    if not (a<0 or b<0 or a>= y or b>= x):
                        if matrix[a][b] == "*":
                            count += 1 
            matrix[i][j] = count
            print(matrix[i][j], end= "")
        else:
            print(matrix[i][j], end = "")
    print()
# %%

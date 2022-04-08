# 4-2. 시각

'''
- 입력: 정수 N
- 출력: 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수 출력
'''

N = int(input())

cnt = 0
for n in range(N+1):
    for i in range(0, 60):
        for j in range(0, 60):
            # if '3' in str(n) or '3' in str(i) or '3' in str(j):
            if '3' in str(n) + str(i) + str(j): # str로 더하는 방법도 있구나
                cnt += 1

print(cnt)
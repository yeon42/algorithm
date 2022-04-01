# 3-2. 큰 수의 법칙

'''
앞선 과정은 M>=100억 이상이라면 시간 초과 판정을 받을 것
- 반복된 수열에 대해 파악하자.
- 수열의 반복된 횟수는? M을 (K+1)로 나눈 몫이 수열의 반복되는 횟수일 것이다.
-> 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수일 것

- 만약 M이 (K+1)로 나누어 떨어지지 않는다면?
- 그 나머지만큼 큰 수가 더해질 것 !!

int(M / (K+1)) * K + M % (K+1)
- M / (K+1)만큼 수열이 K번 반복될 것이고
- 그 나머지만큼 큰 수가 더해질 것이다.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)

## int(A/B) == A//B

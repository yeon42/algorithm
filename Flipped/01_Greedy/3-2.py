# 3-2. 큰 수의 법칙 (단순하게 푸는 방법)

'''
다양한 수로 이루어진 배열이 있을 때
주어진 수들을 M번 더하여 '가장 큰 수'를 만드는 법칙
- 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과해 더해질 수 없다.
'''

'''
Q(3-2)
첫째 줄) N, M, K 공백으로 구분해 입력하기 (K<=M)
둘째 줄) N개의 자연수 공백으로 입력

출력) 큰 수의 법칙에 따라 더해진 답을 출력하기
- 주어진 N개의 자연수들을 M번 더하여 가장 큰 수 만들기 (연속해서 K번을 초과할 수는 없음)
'''

'''
아이디어
- 가장 큰 수, 두 번째로 큰 수 저장
- 가장 큰 수는 K번 더하기 + 두 번째로 큰 수는 1번 더하는 연산 반복 (good good)
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬
            # 리스트로 바꿔줘야 .sort() 함수 사용 가능

first = data[-1]
second = data[-2]

# print(first, second)

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m=0 이라면 반복문 탈출
            break
        result += first # 가장 큰 수 k번 더하기
        m -= 1 # 더할 때마다 1씩 빼기

    if m == 0: # m=0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

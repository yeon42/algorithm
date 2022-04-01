# 3-3. 숫자 카드 게임 - min() 함수 이용

'''
여러 숫자 카드 중 가장 `높은` 숫자가 쓰인 카드 한 장 뽑는 게임
- 숫자 카드들이 NxM 형태로 놓여있는데, 뽑고자 하는 카드가 포함되어 있으면 행을 선택하고,
  선택된 행에 포함된 카드들 중 가장 숫자가 `낮은` 카드를 뽑아야 한다.
- 처음 카드를 골라낼 행을 선택할 때 해당 행에서 가장 숫자가 낮은 카드 뽑을 것을 고려하여
  최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세우자.
'''

'''
Q(3-3)
첫째 줄) N(행), M(열) 입력
둘째 줄) NxM의 숫자 입력
'''

'''
아이디어
- 각 행마다 가장 작은 수를 찾은 뒤 그 수 중 가장 큰 수를 찾자
'''

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 각 행마다 최솟값 찾기
    min_value = min(data)
    result = max(result, min_value)

print(result)
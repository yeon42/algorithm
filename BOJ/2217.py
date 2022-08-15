# n개의 로프
# k개의 로프를 사용해 중량이 w인 물체를 들어올릴 때,
# 각 로프에는 고르게 w/k 만큼의 중량이 걸림

# 이 로프들을 통해 들어올릴 수 있는 물체의 최대 중량 구하기

n = int(input())
weight = []

for _ in range(n):
    w = int(input()) # 각 로프가 버틸 수 있는 최대 중량
    weight.append(w)

weight.sort(reverse=True)

result = []
for i in range(n):
    result.append(weight[i] * (i+1))

print(max(result))
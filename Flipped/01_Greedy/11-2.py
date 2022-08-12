# 11-2. 곱하기 혹은 더하기

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)): # 두 번째 숫자부터
    num = int(data[i])
    if num <= 1 or result <=1 :
        result += num
    else:
        result *= num

print(result)
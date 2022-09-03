from collections import Counter
import sys

name = list(str(input()))
name.sort()

name_cnt = Counter(name)

odd = 0
odd_alpha = ''
for alpha in name_cnt:
    if name_cnt[alpha] % 2 == 1:
        odd += 1
        odd_alpha += alpha
    if odd >= 2: # 홀수 2개 이상이면 펠린드롬 x
        print("I'm Sorry Hansoo")
        sys.exit()

answer = ''
for i in range(0, len(name), 2):
    if name_cnt[name[i]] % 2 == 1:
        name_cnt[name[i]] -= 1 # 다음엔 펠린드롬에 추가
    else:
        answer += name[i]

temp = answer[::-1] # 거꾸로
answer += odd_alpha # 홀수인 문자 1개 중앙에
answer += temp
print(answer)



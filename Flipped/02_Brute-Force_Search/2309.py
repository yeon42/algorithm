# 백준 2309. 일곱 난쟁이

'''
아이디어
- 9명 중 2개를 제외한 키가 100이라면 ok!
- 전체 9명의 키의 합에서 차례때로 2명의 키를 뺀게 100이라면 반복문 탈출하기
'''


''' first - pop 쓰면 안 됨 '''
# height = []
# for i in range(9):
#     height.append(int(input())) # 전체 키 저장

# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(height) - (height[i] + height[j]) == 100:
#             height.pop(i)
#             height.pop(j)
#             height.sort()

#             for h in range(len(height)):
#                 print(height[h])
#             break

#     if len(height) == 7:
#         break




''' second - for문 안에서 출력하는 형식 좋지 x '''
# height = []
# for i in range(9):
#     height.append(int(input())) # 전체 키 저장

# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(height) - (height[i] + height[j]) == 100:
#             height.remove(height[i])
#             height.remove(height[j])
#             height.sort()

#             for h in range(len(height)):
#                 print(height[h])
#             break

#     if len(height) == 7:
#         break




''' third '''
height = []
for i in range(9):
    height.append(int(input())) # 전체 키 저장

for i in range(9):
    for j in range(i+1, 9):
        if sum(height) - height[i] - height[j] == 100:
            one = height[i]
            two = height[j]

height.remove(one)
height.remove(two)
height.sort()

for h in range(len(height)):
    print(height[h])

# print('\n'.join(map(str, sorted(height))))

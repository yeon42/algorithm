#%% 16.1.1
for i in range(10):
    print("Hello, world!", i)

#%%
for i in range(5, 12):
    print("Hello, world!", i)

# %%
for i in range(0, 10, 2):
    print("Hello, world!", i)

# %% 동작 x
for i in range(10, 0):
    print("Hello, world!", i)


# %%
for i in range(10, 0, -1):
    print("Hello, world!", i)


# %%
for i in reversed(range(10)):
    print("Hello, world!", i)

# %%
for i in range(10):
    print(i, end=' ')
    i = 10

#%%
count = int(input('반복할 횟수를 입력하세요: '))
for i in range(count):
    print("Hello, world!", i)

# %%
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)


#%%
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)


#%%
for letter in 'Python':
    print(letter, end=' ')


# %%
for letter in reversed('Python'):
    print(letter, end=' ')


# %% 16.5 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')


# %% 16.6 심사문제: 구구단 출력하기
num = int(input())

for i in range(1, 10):
    print(num, '*', i, '=', num*i)

# %% 연습문제
# num = list(map(int, input().split()))
# print(min(num))

# %% 연습문제
a, b, c = map(int, input().split())

min = a if (a<b) else b
min = min if (min<c) else c

print(min)

# %% 다른 분 풀이
nums = list(map(int, input().split()))
min = nums[0]
for num in nums:
    min = num if num < min else min
print(min)
# %%

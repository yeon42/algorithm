#%%
i=0
while i<10:
    print("Hello, world!", i)
    i += 1


# %%
i=1
while i<=10:
    print("Hello, world!", i)
    i +=1

                        
# %%
i=10
while i>0:  
    print('Hello, world!', i)
    i -= 1


# %%
count = int(input())
i=0
while i<count:
    print("Hello, world!", i)
    i +=1


# %%
count = int(input())
while count > 0:
    print("Hello, world!", count)
    count -= 1


# %%
import random
random.random()


# %%
random.randint(1, 6) # 범위에 지정한 숫자도 포함됨


# %%
import random
i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)
        
# %%    
dice = [1, 2, 3, 4, 5, 6]
random.choice(dice)


# %% 17.5 연습문제
i = 2
j = 5
while i<=32 and j>=1:
    print(i, j)
    i *= 2
    j -= 1


# %% 17.6 심사문제: 교통카드 잔액  출력하기
money = int(input())
once = 1350

while(money-once>=0):
    money -= once
    print(money)

# %%

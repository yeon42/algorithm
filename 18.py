#%%
# break: 제어흐름 중단하고 반복문 끝내기
i = 0
while True:
    print(i)
    i += 1
    if i == 15:
        break # 반복문 끝냄, while문 벗어남


# %%
for i in range(10000):
    print(i)
    if i == 10:
        break


# %%
# continue: 제어흐름 유지한 상태에서 코드 건너 뛰기
for i in range(40):
    if i % 2 == 0:
        continue # 아래 코드 실행하지 않고 건너뜀
    print(i)


# %%
i = 0
while i<40:
    i+=1
    if i%2 == 0:
        continue
    print(i)


# %%
# pass: 아무 일도 안 하지만, 반복문의 형태를 유지하고 싶다면?
for i in range(10):
    pass

while True:
    pass


# %%
count = int(input())

i=0
while True:
    print(i)
    i += 1
    if i == count:
        break


# %%
count = int(input())

for i in range(count+1):
    if i%2 == 0:
        continue
    print(i)



# %% 18.5 연습문제; 3으로 끝나는 숫자만 출력하기
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break

    print(i, end=' ')
    i += 1


#%%
for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
    if i > 4:
        break
    print(i)
print("Done")


# %% 18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
start, stop = map(int, input().split())
i = start

for i in range(start, stop+1):
    if i > stop: # 종료 조건
        break # 반복문(for문) 벗어남
    if i%10 == 3:
        i+=1
        continue # 아래 코드 실행하지 않고 건너뜀

    print(i, end=' ')
    i+=1
        

# %% 추가 연습문제
while True:
    A, B = map(int, input().split())
    if (A==0 and B==0):
        # print(0, 0)
        break
    else:
        print(A+B)
# %%

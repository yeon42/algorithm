# %% 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(50) # 끝에 추가
print(a)
print(len(a))



# %%
a = []
a.append(10)
a



# %% 리스트 안에 리스트 추가
a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))



# %% 리스트 확장하기 (요소 여러 개 추가)
a = [10, 20, 30]
a.extend([500, 600]) # 위의 append와 다른 것 확인 가능
print(a)
print(len(a))



# %% 리스트의 특정 인덱스에 요소 추가
a = [10, 20, 30]
a.insert(2, 500) # 인덱스 2에 500 추가하기
print(a)
print(len(a))



# %%
a = [10, 20, 30]
a.insert(0, 500)
a



# %%
a = [10, 20, 30]
a.insert(len(a), 500) # 리스트 끝에 값 추가
a



# %%
a = [10, 20, 30]
a.insert(1, [500, 600])
a



# %%
a = [10, 20, 30]
a[1:1] = [500, 600]
a



# %% 리스트에서 특정 인덱스의 요소 삭제하기
a = [10, 20, 30]
a.pop() # 마지막 요소 삭제
a



# %%
a = [10, 20, 30]
a.pop(1)
a



# %%
a = [10, 20, 30]
del a[1]
a



# %% 리스트에서 특정 값 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20)
a



# %%
a = [10, 20, 30, 20]
a.remove(20) # 가장 처음의 20만 제거!
a



# %% 리스트로 스택과 큐 만들기
'''
리스트로 스택과 큐 만들기
덱: 양쪽 끝에서 추가/삭제 가능한 자료 구조
'''

from collections import deque
a = deque([10, 20, 30])
print(a)

a.append(500) # 덱의 오른쪽에 500 추가
print(a)

a.popleft() # 덱의 왼쪽 요소 하나 삭제
print(a)



# %% 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
a.index(20)



# %% 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
a.count(20) # 20의 개수 구하기



# %% 리스트 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
a

# %%
a = [10, 20, 30, 15, 20, 40]
a = list(reversed(a))
a


# %% 리스트 요소 정렬
a = [10, 20, 30, 15, 20, 40]
a.sort() # 오름차순 정렬
a



# %%
a = [10, 20, 30, 15, 20, 40]
a.sort(reverse=True) # 내림차순 정렬
a



# %%
a = [10, 20, 30, 15, 20, 40]
sorted(a)



# %% 리스트 모든 요소 제거
a = [10, 20, 30]
a.clear()
a



# %%
a = [10, 20, 30]
del a[:]
a



# %% 리스트 슬라이스로 조작
a = [10, 20, 30]
a[len(a):] = [500] # 리스트 끝에 추가
a



# %%
a = [10, 20, 30]
a[len(a):] = [500, 600]
a



# %% 리스트 비었는지 확인하기
'''
if not seq: # 비어있으면 true
if seq: # 요소 있으면 true
'''



# %% 리스트 할당과 복사
a = [0, 0, 0, 0, 0]
b = a

print(a is b) # True

''' 변수 이름만 다를 뿐 a와 b는 같은 객체 '''

b[2] = 99
print(a)
print(b)



# %% copy()
''' 리스트 a와 b를 완전히 두 개로 만드려면 '''
a = [0, 0, 0, 0, 0]
b = a.copy()

print(a is b) # False (다른 객체)
print(a == b) # True (요소는 같으므로)

b[2] = 99
print(a)
print(b)



# %%
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)



# %%
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)



# %% enumerate에 start 지정해주기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a, start=1):
    print(index, value)



# %% 인덱스를 요소로 출력
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])



# %%
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1



# %% 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
smallest



# %%
a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
largest



# %%
a = [38, 21, 53, 62, 19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])



# %%
a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))



# %% 요소 합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i
x



# %%
a = [10, 10, 10, 10, 10]
sum(a)




# %% 리스트 컴프리헨션
''' 리스트 안에 for과 if문 지정하여 리스트 생성 '''
a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)



# %%
c = [i+5 for i in range(10)]
print(c)

d = [i*2 for i in range(10)]
print(d)



# %% 리스트 표현식에서 if 조건문 사용
a = [i for i in range(10) if i%2==0]
a



# %%
b = [i+5 for i in range(10) if i%2==1]
print(b)



# %%
a = [i*j for j in range(2, 10) for i in range(1, 10)]
a



# %%
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
a



# %%
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
a



# %%
a = list(map(str, range(10)))
a



# %%
a = input().split()
a



# %%
a = map(int, input().split())
print(a) # 맵 객체
print(list(a))



# %%
x = input().split()
m = map(int, x)
a, b = m



# %% 튜플 특정 값 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
a.index(53)




# %%
a = (10, 20, 30, 15, 20, 40)
a.count(20)



# %%
a = (38, 21, 53, 62, 19, 53)
for i in a:
    print(i, end=' ')



# %% 튜플 표현식 사용하기
a = tuple(i for i in range(10) if i%2==0)
a



# %% 튜플에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
a



# %% 22.9 연습문제: 리스트에서 특정 요소만 뽑아내기

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [str for str in a if len(str)==5]

print(b)



# %% 22.10 심사문제: 2의 거듭제곱 리스트 생성하기
num1, num2 = map(int, input().split())

l = []
for i in range(num1, num2+1):
    l.append(2**i)

del l[1]
del l[-2]

print(l)

# %%
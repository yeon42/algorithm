# %% 람다 표현식
plust_ten = lambda x: x+10
plus_ten(1)



# %% 람다 표현식 자체를 호출하기
(lambda x: x+10)(1)

# %%
y = 10
(lambda x: x+y)(1)



# %%
def plus_ten(x):
    return x+10

list(map(plus_ten, [1, 2, 3]))
# %% 람다 함수 만들어 map에 넣기
list(map(lambda x: x+10, [1, 2, 3]))


# %% 람다 표현식으로 매개변수 없는 함수 만들기
(lambda : 1)()
# %%
x = 10
(lambda: x)()

''' 콜론 뒤에 반드시 반환할 값이 있어야 함 '''



# %% 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x%3 == 0 else x, a))

'''
람다에서 if문을 사용했다면 else를 반드시 사용해야 함
'''



# %%
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+10, a))

# %%
def f(x):
    if x==1:
        return str(x)
    elif x==2:
        return float(x)
    else:
        return x+10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(f, a))



# %% map에 객체 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x*y, a, b))




# %% filter 사용하기
''' filter(함수, 반복가능한 객체) '''

def f(x):
    return x>5 and x<10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))



# %%
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x: x>5 and x<10, a))



# %%
def f(x, y):
    return x+y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a)



# %% 32.4 연습문제: 이미지 파일만 가져오기
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('jpg')!=-1 or x.find('.png')!=-1, files)))

''' * find 메서드 *
찾을 문자열이 있으면 인덱스 반환,
찾을 문자열이 없으면 -1 반환
'''



# %% 32.5 심사문제: 파일 이름을 한꺼번에 바꾸기

'''
map: 리스트 요소 각각 처리
filter: 조건문 만족한 요소들을 반환
'''

files = input().split()
print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1], files)))





# %%
b = "Hi, everyone"
b.split(",")





# %%
def f(x):
    return x>5 and x<10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(map(f, a)))
print(list(filter(f, a)))

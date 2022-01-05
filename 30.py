# %% 위치 인수: 인수의 위치가 정해짐
print(10, 20, 30)

''' 어떠한 기호(list, tuple 등)가 붙어있지 않음 '''



# %% 위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30)



# %% 언패킹 사용하기
x = [10, 20, 30]
print_numbers(*x)

'''
인수를 순서대로 넣을 때 리스트, 튜플 사용하기
앞에 *를 붙여 함수에 넣어주면 된다. -> 언패킹
'''



# %%
print_numbers(*[10, 20, 30])




# %% 가변 인수 함수 만들기
'''
위치 인수와 리스트 언패킹은 인수의 개수가 정해지지 않은 가변 인수에 사용함
ex. 같은 함수에 인수를 한 개 or 열 개 or nothing을 넣을 수 있다. 
'''

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10, 20, 30, 40)
print_numbers()



# %%
x = [10]
print_numbers(*x)

y = [10, 20, 30, 40]
print_numbers(*y)



# %% 고정 인수와 가변 인수 함께 사용하기
def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)
print('---------------')
print_numbers(1, 10, 20)
print('---------------')
print_numbers(*[10, 20, 30])
print('---------------')
print_numbers(10, *[20, 30])

print(print_numbers(*[10, 20, 30]) is print_numbers(10, *[20, 30]))

'''
*args가 고정 매개변수보다 앞쪽에 오면 안 됨
'''



# %%
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')

# %% 키워드 인수 방식으로 호출
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

''' 인수의 순서 맞추지 않아도 ok ! '''

# %% print 함수에서 사용했던 sep과 end도 키워드 인수이다.
print(10, 20, 30, sep=':', end='')



# %% 키워드 인수와 딕셔너리 언패킹 사용하기
''' 딕셔너리를 사용해 키워드 인수로 값을 넣는 딕셔너리 언패킹 '''
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x)

'''
** 두 개는 value 값이 나오고, (두 번 unpacking -> 값)
* 한 개는 key 값이 나오더라 (한 번 unpacking -> 키)
'''



# %% 키워드 인수 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동')

# %%
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')



# %% 딕셔너리 만들고 앞에 ** 붙여도 됨
x = {'name': '홍길동'}
personal_info(**x)

y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**y)



# %%
def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs[name])
    if 'age' in kwargs:
        print('나이: ', kwargs[age])
    if 'address' in kwargs:
        print('주소: ', kwargs[address])



# %% 고정 인수, 가변 인수(키워드 인수) 함께 사용하기
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

personal_info('홍길동')
# %%
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
# %%
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})



# %% 위치 인수와 키워드 인수 함께 사용하기 (어렵다)
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')

''' **kwargs가 *args보다 앞 쪽에 오면 안 됨 '''




# %%
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)
# %%
personal_info('홍길동', 30, '서울시 용산구 이촌동')

'''
- 매개변수에 초기값 지정되어 있더라도 값 넣으면 해당 값 전달 됨
- 초기값이 지정된 매개변수는 뒤쪽으로 몰아주자
'''




# %% 30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
kor, eng, math, sci = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(kor, eng, math, sci)
print('높은 점수: ', max_score)

max_score = get_max_score(eng, sci)
print('높은 점수: ', max_score)



# %% 30.7 심사문제: 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기

'''
함수를 호출할 때마다 인수의 개수가 달라지고 있음 -> 가변 인수 함수로 만들기
'''

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def get_average(**args):
    return sum(args.values()) / len(args) # values()로 딕셔너리의 값만 가져옴


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))


# %%

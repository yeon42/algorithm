# %% 함수
def hello():
    print('Hello, world!')
hello()



# %%
def add(a, b):
    return a+b

x = add(10, 20)
x



# %% 매개변수는 없고 반환값만 있는 함수
def one():
    return 1

x = one()
x



# %% return으로 함수 중간에서 빠져 나오기
def not_ten(a):
    if a == 10:
        return # 함수 중간에서 빠져 나온다.
    print(a, '입니다.', sep='')

not_ten(5)



# %%
def add_sub(a, b):
    return a+b, a-b

x, y = add_sub(10, 20)
print(x)
print(y)



# %% 값 여러 개를 직접 반환하기
def one_two():
    return (1, 2) # 튜플에 지정해주자
    # return [1, 2] # 리스트로 지정
    # 1, 2 # 괄호 없이도 가능

x, y = one_two()
print(x, y)



# %%
def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)

x = 10
y = 20
add(x, y)



# %%
def three():
    return 1, 2, 3

three()


# %% 29.3 연습문제: 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3

def get_quotient_remainder(x, y):
    return x//y, x%y

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))




# %% 29.4 심사문제: 사칙 연산 함수 만들기
x, y = map(int, input().split())

def calc(x, y):
    return x+y, x-y, x*y, x/y

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))

# %%

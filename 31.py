# %% 재귀 호출 사용하기 (다음은 무한호출 예시)
# def hello():
#     print('Hello, world!')
#     hello()
# hello()



# %%
def hello(count):
    if count == 0: # 종료 조건
        return

    print('Hello, world!', count)

    count -= 1
    hello(count) # 다시 hello()에 넣음

hello(5)



# %%
def factorial(n):
    if n == 1:
        return 1 # 1 반환 후 재귀호출 끝냄
    return n * factorial(n-1)

print(factorial(5))



# %% 31.4 연습문제: 재귀호출로 회문 판별하기

'''
회문: 거꾸로 읽어도 제대로 읽는 것과 같은 문장, 낱말, 숫자, 문자열 등
'''

def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))




# %% 31.5 심사문제: 재귀호출로 피보나치 수 구하기

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))


# %%

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))

# %%

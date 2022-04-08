# %% 딕셔너리에 키와 기본값 저장하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e') # 키-값 쌍 추가
print(x)

x.setdefault('f', 100)
print(x)
# %%
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90, f=60)
x
# %%
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
y
# %%
y.update([[2, 'TWO'], [4, 'FOUR']])
y
# %%
y.update(zip([1, 2], ['one', 'two']))
y
# %%
'''
setdefault 는 키-값 쌍 추가만 가능하고,
    이미 들어있는 키의 값은 수정할 수 없음
update는 키-값 쌍 추가와 값 수정 모두 가능
'''
# %% 딕셔너리에서 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
x
# %%
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
x
# %% 딕셔너리에서 임의의 키-값 쌍 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem() # 마지막 아이템 삭제
x

# %% 모든 키-값 쌍 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
x

# %% 딕셔너리에서 키의 값 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a')

# %% 딕셔너리에서 키-값 쌍 모두 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())

# %% 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys) # 리스트로 딕셔너리 생성
x

# %%
y = dict.fromkeys(keys, 100)
y
# %% defaultdict 사용하기
''' 없는 키에 접근하더라도 에러 발생하지 않으며 기본값 반환 '''
from collections import defaultdict
y = defaultdict(int) # 기본값으로 0 설정
y['z']

# %%
z = defaultdict(lambda: 'python')
print(z['a'])
print(z[0])
# %%
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)
# %%
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()} # value에 어떤 값도 넣지 x
x
# %%
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():
#     if value == 20:
#         del x[key]

# print(x)

x = {key: value for key, value in x.items() if value!=20}
x
# %%
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x

print(x is y)

y['a'] = 99
print(x)
print(y)
# %%
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()

print(x is y)
print(x == y)
# %%
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()

y['a']['python'] = '2.7.15'
print(x)
print(y)
# %% 중첩 딕셔너리 완전히 복사 -> deepcopy
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy
y = copy.deepcopy(x)

y['a']['python'] = '2.7.15'
print(x)
print(y)

''' y의 값 변경해도 x에 영향 미치지 x '''
# %% 25.7 연습문제: 평균 점수 구하기
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

avg = sum(maria.values()) / len(maria)
print(avg)


# %% 25.8 심사문제: 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {key: value for key, value in x.items() if key!='delta' and value!=30}

print(x)

# %%

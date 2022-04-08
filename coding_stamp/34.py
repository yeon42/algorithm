'''

클래스(Class)?
하나의 클래스를 통해 여러 개의 객체를 생성함으로써 코드의 반복을 줄일 수 있다.

객체: 실체화 된 것 (클래스를 통해 생성된 것)
인스턴스 = 실체화 한 객체
self: 클래스를 통해 생성된 객체 그 자신

'''



# %% 클래스와 메서드 만들기
class Person:
    def greeting(self): # 메서드
        print('Hello')


# %%
# 클래스 사용하기
''' 인스턴스 = 클래스() '''
james = Person()

# 메서드 호출하기
''' 인스턴스.메서드() '''
james.greeting()

''' 인스턴스 메서드: 인스턴스를 통해 호출하는 메서드 '''



# %% 파이썬에서 흔히 볼 수 있는 클래스
a = int(10) # int 클래스
print(a)

b = list(range(10)) # list 클래스
print(b)

c = dict(x=10, y=20) # dict 클래스
print(c)

# %%
print(type(a))
print(type(b))
print(type(c))
maria = Person()
print(type(maria))



# %% 메서드 안에서 메서드 호출하기
class Person:
    def greeting(self):
        print('Hello')
    
    def hello(self):
        self.greeting() # self.메서드() 형식으로 클래스 안의 메서드 호출

james = Person()
james.hello() # Hello

'''
self 없이 메서드 이름만 사용하면
클래스 바깥쪽에 있는 함수를 호출한다는 뜻!
'''



# %% isinstance: 특정 클래스의 인스턴스인지 확인하기
class Person:
    pass

james = Person()
isinstance(james, Person) # True



# %% isinstance: 객체의 자료형 판단
def factorial(n):
    if not isinstance(n, int) or n<0: # n이 정수가 아니거나 음수이면 함수 끝냄
        return None
    if n==1:
        return 1
    return n*factorial(n-1)





# %%
'''
클래스에서 속성 만들고 사용하기
__init__ 메서드 안에서 self.속성 에 값 할당하기
'''

# %% self.속성
class Person:
    def __init__(self):
        self.hello = '안녕하세요.' # 자기 자신에 속성 추가
    
    def greeting(self):
        print(self.hello)

james = Person()
james.greeting() # 안녕하세요

#%%

'''
* __init__ 메서드
- 인스턴스를 만들 때 호출되는 특별한 메서드
- 인스턴스(객체) 초기화
- 파이썬이 자동으로 호출해줌


* self
- 인스턴스 자기 자신
- 위 예제에서 self에 들어가는 값은 Person()
'''



# %% 인스턴스를 만들 때 값 받기
class Person:
    def __init__(self, name, age, address): # 매개변수 지정
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
    
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name)) # 내부적 접근

# 메서드 바깥에서 접근
maria = Person('마리아', 20, '서울시 서초구 반포동') # 인스턴스로 접근 (구체적인 Person을 인스턴스로 만들어준다.)
maria.greeting()

# 인스턴스 속성: 인스턴스를 통해 접근하는 속성
print('이름: ', maria.name)
print('나이: ', maria.age)
print('주소: ', maria.address)



# %% 클래스의 위치 인수 & 리스트 언패킹
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])



# %% 클래스의 키워드 인수 & 딕셔너리 언패킹
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})



# %% 인스턴스 생성 뒤 속성 추가하기
class Person:
    pass

maria = Person() # 인스턴스 생성
maria.name = '마리아' # 인스턴스 만든 뒤 속성 추가
maria.name



# %% 인스턴스의 특정 속성만 허용하기
james = Person()
james.name # maria 인스턴스에만 name 속성 추가했으므로 여기엔 x



# %%
class Person:
    def greeting(self):
        self.hello = '안녕하세요' # greeting 메소드에서 hello 속성 추가

maria = Person()
maria.hello # 아직 hello 속성이 없음
# %%
maria.greeting() # greeting 메서드를 호출해야
maria.hello # hello 속성이 생성됨



# %% __slots__ : 특정 속성만 허용, 다른 속성은 제한
class Person:
    __slots__ = ['name', 'age'] # name, age만 허용 (다른 속성은 생성 제한)

maria = Person()
maria.name = '마리아'
maria.age = 20
maria.address = '서울시 서초구 반포동' # 허용되지 않은 속성 추가 -> 에러




# %% 비공개 속성
class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 변수 앞에 __를 붙여 비공개 속성으로 만듦

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000 # 클래스 바깥에서 비공개 속성에 접근하면 에러 발생



# %% 
class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 변수 앞에 __를 붙여 비공개 속성으로 만듦

    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네...')
            return
        self.__wallet -= amount # 클래스 안의 메서드에서만 접근 o

        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)



# %% 비공개 메서드 사용하기
class Person:
    def __greeting(self):
        print('Hello')
    
    def hello(self):
        self.__greeting() # 클래스 안에서는 비공개 메서드 호출 가능

james = Person()
james.__greeting() # 에러: 클래스 바깥에선 비공개 메서드 호출 불가능




# %% 34.5 연습문제: 게임 캐릭터 클래스 만들기

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print('베기')

x = Knight(health=542.2, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()




# %% 34.6 심사문제; 게임 캐릭터 클래스 만들기

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print("티버: 피해량", self.ability_power * 0.65 + 400)

health, mana, ability_power = map(float, input().split())


x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()





# %% self가 없어도 되는 이유

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print("티버: 피해량", ability_power * 0.65 + 400, hi)

health, mana, ability_power = map(float, input().split())
hi = 20

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()



# %%
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(ability_powers):
        print('tibber:', 'damage', ability_power*0.65+400)
        
health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
# %%

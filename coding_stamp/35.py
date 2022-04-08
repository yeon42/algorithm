# %% 클래스 속성 사용하기
class Person:
    bag = [] # 클래스 속성

    def put_bag(self, stuff): # 메서드
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(james.__class__.bag)
print(maria.bag)

'''
bag=[] ; 클래스 속성은 모든 인스턴스에서 공유한다. 
'''



# %%
james.__dict__
# %%
Person.__dict__



''' 가방을 여러 사람이 공유하지 않으려면? '''
# %% 인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = [] # 인스턴스 속성 (반복할 때마다 bag 초기화)
    
    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)



# %%

'''
클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용
'''





# %% 비공개 클래스 속성 사용
class Knight:
    __item_limit = 10 # 비공개 클래스 속성

    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 안에서만 접근 가능

x = Knight()
x.print_item_limit() # 10

# print(Knight.__item__limit) # 클래스 바깥에서는 접근 x



# %% 독스트링 사용
class Person:
    ''' 사람 클래스입니다.'''

    def greeting(self):
        '''인사 메서드입니다.'''
        return 'Hello'
    
print(Person.__doc__)
print(Person.greeting.__doc__)

maria = Person()
print(maria.greeting.__doc__)
# print(maria.greeting())




'''
지금까지는 클래스의 메서드를 사용할 때 인스턴스를 통해 호출함
'''

# %% 정적 메서드: @staticmethod
class Calc:
    @staticmethod
    def add(a, b): # 정적 메서드는 매개변수에 self를 지정하지 x
        print(a+b)
    
    @staticmethod
    def mul(a, b):
        print(a*b)

# 클래스에서 바로 메서드 호출 (직접 접근 가능)
Calc.add(10, 20) # 첫 번째 인자 self 생략
Calc.mul(10, 20)




# %%

'''
정적 메서드
: 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수의 경우
- 순수함수: 입력값이 같으면 언제나 같은 출력 값 반환
즉, 인스턴스의 상태를 변화시키지 않는 메서드를 만들 때 사용
'''


# %% 인스턴스의 내용을 변경해야 할 때 (update)
a = {1, 2, 3, 4}
a.update({5}) # 인스턴스 메서드
a

# %% 인스턴스 내용과 상관없이 결과만 구할 때 (set.union)
set.union({1, 2, 3, 4}, {5}) # 정적(클래스) 메서드




# %% 클래스 메서드: @classmethod
class Person:
    count = 0 # 클래스 속성

    def __init__(self):
        Person.count += 1 # 인스턴스가 만들어질 때
                          # 클래스 속성인 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count)) # cls로 클래스 속성에 접근

    @classmethod
    def create(cls):
        p = cls() # cls()로 인스턴스 생성
        return p

james = Person()
maria = Person() # 누적

Person.print_count() # 2명 생성되었습니다.


# %%
'''
클래스 메서드
: 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용
- cls 사용하면 메서드 안에서 현재 클래스의 인스턴스 생성 가능
'''




# %% 추가 예시 1
class Language:
    default_language = " English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @staticmethod
    def static_my_language():
        return Language()

    @classmethod
    def class_my_language(cls):
        return cls()

    def print_language(self):
        print(self.show)

class KoreanLanguage(Language):
    default_language = " 한국어"


a = KoreanLanguage.static_my_language() # 부모 클래스 속성
b = KoreanLanguage.class_my_language() # cls 클래스 속성
a.print_language()
b.print_language()





# %% 추가 예시 2
class Test:
    name = "Test"

    @staticmethod
    def static_function():
        return Test.name # 부모 클래스 속성에 접근

    @classmethod
    def class_function(cls): # cls로 클래스 속성에 접근
        return 

class Test2(Test):
    name = "Test2"


if __name__ == "__main__":
    print(Test.static_function()) # Test 출력
    print(Test2.static_function()) # Test 출력
    print(Test.class_function()) # Test 출력
    print(Test2.class_function()) # Test2 출력




# %% 35.5 연습문제: 날짜 클래스 만들기
class Date:
    @staticmethod
    def is_date_valid(date):
        year, month, day = map(int, date.split('-'))
        return month<=12 and day<=31

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')



# %% 35.6 심사문제: 시간 클래스 만들기
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return 0<=hour<=24 and 0<=minute<=59 and 0<=second<=60


time_string = input()
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

    
    # @classmethod
    # def from_string(cls, time):
    #     hour, minute, second = map(int, time.split(':'))
    #     time = cls(hour, minute, second)
    #     return time

    # @staticmethod
    # def is_time_valid(time):
    #     hour, minute, second = map(int, time.split(':'))
    #     return 0<=hour<=24 and 0<=minute<=59 and 0<=second<=60


# time_string = input()

# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')

# %%

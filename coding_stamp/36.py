'''
상속: 물려받은 기능을 유지한 채 다른 기능 추가할 때 사용
- 기반 클래스(base class): 기능을 물려주는 클래스
    - 부모(슈퍼) 클래스
- 파생 클래스(derived class): 상속을 받아 새롭게 만드는 클래스
    - 자식(서브) 클래스

기반 클래스의 능력을 그대로 활용하면서 새로운 클래스를 만들 때 사용!
- 중복되는 기능을 만들지 않아도 된다는 이점 (기존 기능 재사용)
'''

# %% 사람 클래스로 학생 클래스 만들기
class Person:
    def greeting(self):
        print('안녕하세요.')
    
class Student(Person): # Person 클래스를 상속받음
    def study(self):
        print('공부하기')

james = Student()
james.greeting() # 기반 클래스 Person의 메서드 호출
james.study() # 파생 클래스 Student에 추가한 study 메서드

''' Student 클래스는 Person 클래스를 상속받았으므로
greeting 메서드 호출 가능 '''



# %% 상속 관계 확인하기: issubclass
class Person:
    pass

class Student(Person):
    pass

issubclass(Student, Person) # True




# %% 상속 관계
class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')



# %% 포함 관계 *******
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = [] # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person): # 리스트 속성에 Person 인스턴스를 추가
        self.person_list.append(person)
    
    def print_person(self):
        return self.person_list

a = PersonList()
a.append_person('Maria')
a.append_person('James')
a.print_person()


# %%
'''
속성에 인스턴스를 넣어 관리 -> PersonList가 Person을 포함함
- 같은 종류 + 동등한 관계: 상속 사용
- 그 이외: 인스턴스를 넣는 포함 방식 사용
'''



# %% 기반 클래스의 속성 사용하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello) # 기반 클래스의 (인스턴스)속성 출력하려 하면 에러 발생

''' Why?
기반 클래스 Person의 __init__ 메서드가 호출되지 않았으므로
즉, Person의 __init__ 메서드가 호출되지 않으면
self.hello = '안녕하세요' 도 실행되지 않아 속성이 만들어지지 x
'''



# %% super()로 기반 클래스 초기화하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello) # __init__() 메서드가 호출되었으므로 hello도 호출 가능


# %%
'''
super().__init__(): 기반 클래스 Person의 __init__ 메서드를 호출해주면
기반 클래스가 초기화되어 속성이 만들어진다.
'''



# %% 기반 클래스를 초기화하지 않아도 되는 경우
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    pass

james = Student()
print(james.hello)

# %%
'''
즉, 파생 클래스에 __init__ 메서드가 없다면
기반 클래스의 __init__이 자동으로 호출되므로 기반 클래스의 속성 사용 가능
'''



# %% 좀 더 명확하게 super 사용하기
'''
파생 클래스에 self를 넣어 현재 클래스가 어떤 클래스인지 명확하게 표시
'''
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()
        self.school = '파이썬 코딩 도장'




# %%
'''
메서드 오버라이딩
: 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드 오버라이딩
'''
# %% 메서드 오버라이딩
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self): # 마찬가지로 greeting 메서드 만들기
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()

# %%
'''
오버라이딩(overriding): 무시하다, 우선하다
- 기반 클래스의 메서드 무시하고 새로운 메서드 만든다.

Why Use?
- 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 활용
'''



# %% 중복되는 문구 줄이기
class Person:
    def greeting(self):
        print('안녕하세요.')
    
class Student(Person):
    def greeting(self):
        super().greeting() # 기반 클래스의 메서드 호출하여 중복 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()



# %% 다중 상속
class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()




# %% 다이아몬드 상속: 애매하다.
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass

x = D()
x.greeting() # 안녕하세요, B입니다.


# %% 메서드 탐색 순서 확인
D.mro()

# D -> B -> C -> A 순이므로 B의 greeting이 호출
# (D는 greeting 메서드가 없으므로)




# %% object 클래스
int.mro() # [int, object]




# %%
'''
추상 클래스
: 메서드의 목록만 가진 클래스이며, 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용
- 파생 클래스가 반드시 구현해야 하는 메서드 정해줌
'''
# %% abc(abstract base class)
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass # 인스턴스 만들 수 없으니 호출 할 일 x -> 빈 메서드(pass)

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self): # @abstractmethod가 붙은 추상 메서드 모두 구현해야 함
        print('학교가기')

james = Student()
james.study()
james.go_to_school()




# %% 36.8 연습문제: 리스트에 기능 추가하기
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)




# %% 36.9 심사문제: 다중 상속 사용하기
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))
# %%

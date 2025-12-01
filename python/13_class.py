# 객체 지향 프로그래밍(OOP): 객체를 기반으로 프로그램을 설계하는 프로그래밍 ex) c++
# 객체: 데이터와 데이터를 조작하는 기능(메서드)을 하나로 묶은 독립적인 실행 단위
# 객체는 실제 세계의 사물이나 개념을  프로그래밍적으로 모델링한 것
# 객체의 특징
# + 상태 --> 객체의 속성(데이터, 변수)
# + 행동 --> 객체의 기능(메서드, 함수)
# + 식별성 --> 객체 고유의 존재
# 객체: "속성과 행동"을 함께 묶어서 현실 세계의 개념을 표현할 수 있도록 함
# 모델링: 현실 세계의 복잡한 개념을 프로그래밍에서 다룰 수 있도록 단순화하는 과정

# oop가 등장하기 전에는 절차적 프로그래밍이 널리 사용되었음
# 절차적 프로그래밍
# + 프로그램을 순차적인 절차와 함수로 구성하는 방식
# + 함수 (또는 프로시저) 단위로 코드가 실행되며, 데이터를 함수가 직접 처리
# --> 코드가 복잡헤지고 유지보수가 어려워지는 문제점이 발생

# 절차적 프로그래밍의 문제점
# + 데이터와 함수가 분리되어 있음
# + 함수가 많아지면 코드가 복잡해짐
# + 코드 재사용성이 낮음
# + 유지보수가 어려움

# oop의 핵심 개념
# + 1.캡슐화: 객체 내부 데이터를 외부에서 직접 접근하지 못하도록 보호
# 의의:
# + 데이터 보호를 통해 잘못된 값이 저장되지 않도록 방지
# + 내부 동작을 숨겨 코드 변경이 있어도 외부에서 영향 없이 사용가능(모듈화)

# 2. 상속: 기존 클래스를 확장하여 새로운 기능을 추가할 수 있음
# 의의:
# + 코드의 재사용성을 높이고 유지보수를 쉽게 만듦
# + 기존 클래스를 기반으로 새로운 기능을 추가하는 것이 용이함

# 3. 다형성: 같은 함수를 서로 다른 방식으로 실행할 수 있음
# 의의:
#+ 새로운 클래스 추가 시 기존 코드를 변경할 필요 없음
# + 같은 인터페이스를 사용해 다양한 기능을 쉽게 추가할 수 있음

# 4. 추상화: 필요한 정보만 보여주고, 불필요한 내부 구현은 숨기는 개념
# 의의:
# + 불필요한 세부 사항 없이 핵심 기능만 제공하여 코드가 관리가 쉬워짐
# + 공통적인 동작을 정의하고, 세부 구현을 각 클래스에서 따로 처리 가능

# oop가 중요한 이유
# 1. 코드 재사용성 증가
# + 같은 클래스를 여러 개의 객체로 생성하여 사용 가능
# 2. 유지보수 및 확장 용이
# + 클래스 단위로 개발하면 새로운 기능을 추가하기 쉬움
# + 기존 클래스를 수정하는 관련된 모든 객체에 반영됨
# 3. 현실 세계 모델링 가능
# + 현실 세계의 개념을 코드로 직접 표현할 수 있음

# 클래스(class)
# + 데이터와 기능을 하나로 묶는 구조
# + 개념적(기능정)으로 유사한 과계에 있는 것들을 묶어줌

# 클래스 기본 문법
# 클래스의 정의
class ClassName: # <--pascal case
    # 생성자(constructor): 인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의 가능
    def __init__(self, name): # __init__(생성자): 객체가 생성될 때 자동 호출되는 초기화 매서드
        # 인스턴스 변수
        # self: 인스턴스 자기 자신을 가리킴
        self.name = name
        self.age = 0

    # (인스턴스) 메서드
    def method_name(self):
        print(f"이 인스턴스의 이름은{self.name}입니다.")
        pass

# 인스턴스 생성
my_instance = ClassName("I1")
print(my_instance.name)
my_instance.method_name()

another_instance = ClassName("I2")
another_instance.method_name()

# 클래스와 객체
# 클래스: 객체를 만들기 위한 설계도
# 객체: 클래스로부터 만들어진 실제 데이터
# 클래스는 공통적인 속성과 동작을 정의하고, 객체는 이를 기반으로 실제 데이터를 가지는 객체

# 생성자__init __() 함수
# 생성자(Constructor)
# 클래스로부터객체(인스턴스)를 생성할 때 자동으로호출되는초기화함수
# 객체생성시 필요한속성초기화및 기본상태설정에 사용
# __init__()메서드로생성자정의
# 하나의 클래스에 하나의__init__()만 정의가능함

# 실습 1-1. 책 클래스 만들기
class Book:
    def __init__(self, title, author,total_pages, current_page):
        self.x1 = title
        self.x2 = author
        self.x3 = total_pages
        self.x4 = current_page

    def read_page(self):
        if self.x4 > self.x3:
            print("책의 범위를 벗어났습니다.")
        else:
            print(f"현재 {self.x4}페이지를 읽으시고 있는 중입니다.")
        pass

    # def read_page(self, page):
    #     self.x4 += page

    #     if page > self.x3:
    #         self.x4 = self.x3      
    #         print("책의 범위를 벗어났습니다.")
    #     else:
    #         print(f"현재 {page}페이지를 읽으시고 있는 중입니다.")
    #     pass

    def progress(self):
        ratio = self.x4 / self.x3 * 100
        result = round(ratio, 1) # 소수점 첫 째 자리까지 반올림
        print(f"전체 중 {result}(%) 읽으셨습니다.")

Dongyuns_Story = Book("Dongyuns_story", "Dongyun2", 500, 245)
Dongyuns_Story.read_page() 
Dongyuns_Story.progress()

# 실습 1-2. Rectangle 클래스 구현
class Rectangle:
    def __init__(self, width, height):
        self.x1 = width
        self.x2 = height
    
    def area(self):
        rect = self.x1 * self.x2
        print(f"사각형의 넓이는 {rect}(단위없음)입니다.")

bdy = Rectangle(int(input("width: ")), int(input("height: ")))
# input().split()으로 한 번에 두 개의 입력을 넣으려면,
'''
Rectangle클래스는 두 개의 인자를 필요로 하므로 Rectangle(input, input)처럼 각각 전달해야함.
input().split은 리스트 하나를 반환하기 때문에 그대로 쓰면 인자 개수가 맞지 않아서 에러가 발생함.
w, h = map(int, input("width, height: ").split()) # map(int,  ....): 문자열을 정수로 변환
bdt = Rectangle(w, h) # w, h: 각각 width, height로 할당됨
'''
bdy.area()

# 인스턴스 변수
# 각 인스턴스(객체)가 개별적으로 소유하는 변수
# + self.변수이름 형태로 정의하며, 생성자(__init__)안에서 초기화
# + 객체마다 서로 다른 값을 가짐
# + 인스턴스이름.변수이름으로 접근

# 클래스 변수: 클래스 자체에 소속된 변수
# + 모든 인스턴스가 공통적으로 공유
# + 클래스 블록 내부, 메서드 바깥에서 선언함
# + 클래스이름.변수이름으로 접근
# --> 공유해야 하는 값을 클래스 변수로 사용

# 인스턴스 메서드: 클래스 인스턴스를 통해 호출되는 메서드
# + 첫 번째 인자는 self, 호출한 객체 자신을 의미
# + 인스턴스이름.메서드이름()으로 접근

# 클래스 메서드(@classmethod): 클래스 자체를 대상으로 동작하는 메서드
# + 첫 번째 인자 cls, 클래스 자신을 참조
# + 클래스 변수를 조작할 때 주로 사용

# 정적 메서드(@staticmethod): 일반적인 유틸리티 함수를 클래스 내부에 정의할 때 사용
# + self나 cls를 사용하지 않는 유틸리티 함수
# + 클래스와 관련은 있지만 클래스나 인스턴스 상태에 의존하지 않는 기능을 제공

# 클래스 변수
# - 클래스가 가지고 있는 변수
# - 모든 인스턴스가 공유할 수 있음
class Dog:
    # 클래스 변수
    kind = "강아지"

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    
dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print("인스턴스1", dog1.kind)
print("인스턴스2", dog2.kind)
print("클래스", Dog.kind)

# 클래스 메서드
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스 데이터를 조작하는데 사용

class Book2:
    book_count = 0

    def __init__(self, title, author):
        Book2.book_count += 1
        self.title = title
        self.author = author

    # 클래스 메서드
    @ classmethod # 데코레이터
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있다.")

book1 = Book2("B1", "author1")
book2 = Book2("B2", "author2")
print(Book2.book_count)
Book2.get_count()

# 정적 메서드
# - 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# - 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# - 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음

class OperationTool:
    
    @staticmethod # 데코레이터
    def add(a, b):
        return a + b
    
print(OperationTool.add(10, 20))

class User:

    username = 0
    points = 0
    total_users = 0

    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points >= 0 and self.points <= 99:
            print(f"{self.username} / Tier: Bronze")
        elif self.points >= 100 and self.points <= 499:
            print(f"{self.username} / Tier: Silver")
        elif self.points >= 500:
            print(f"{self.username} / Tier: Gold")
        elif self.points < 0:
            print(f"{self.username} / Iron(심해)")

    @classmethod
    def get_total_users(cls):
        print(f"생성된 전체 유저 수: {cls.total_users}")

gamer1 = User("Dongyun2", 1000)
gamer2 = User("배칠수의 꽃배달", 200)
gamer3 = User("신바람 이박사", 99999)
gamer1.get_level()
gamer2.get_level()
gamer3.get_level()
User.get_total_users()

# 정보 은닉과 캡슐화
# 정보 은닉
# + 객체의 내부 상태(데이터)를 외부에서 직접 접근하지 못하도록 막고, 공개된 메서드를 통해서만 접근하도록 제한하는 것
# + 데이터 무결성 보호, 코드 안정성 향상에 기여
# 캡슐화
# + 객체가 자신의 속성과 메서드를 하나로 묶고, 외부에는 필요한 부분만 공개하는 것
# + 정보 은닉은 캡슐화의 하위 개념으로 실현 방법 중 하나임

# public 멤버: 클래스 외부에서 자유롭게 접근 가능
# + 파이썬에서 일반적으로 정의한 인스턴스 변수는 기본적으로 모두 public

# protected 멤버: 외부에서는 직접 접근하지 않는 것을 권장
# + _변수명으로 표현
# + 보호 수준을 명시적으로 표현하기 위한 개발자 간 약속
# + 외부에서의 직접 접근은 가능 -> 캡슐화를 깨뜨리는 행위로 간주되며 권장되지 않음

# private 멤버: 클래스 외부에서 직접 접근 불가
# + __변수명으로 표현(underbar 2)
# + 네임 맹글링(name mangling)
# ++ 내부적으로 _{클래스명}__변수명으로 이름이 변경되어 접근을  어렵게 함
# ++ _{클래스명}__변수명으로 접근할 수 있지만 권장되지 않음


# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상 시키기 위함

class Person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private: 언더바(__) 두 개를 변수 앞에 붙여서 정의
        self.__age = age
        
        # getter
        def get_age(self):
            return self.__age

        # setter
        def set_age(self, value):
            if value > 120 or value < 0:
                print("유효하지 않은 나이입니다.")
            else:
                self.__age = value

p1 = Person2("lee", 15)
print(p1.name)
#print(p1.__age)
print(p1.get_age())
p1.set_age(-10)

# 게터(getter): 객체의 내부 속성값을 읽을 수 있도록 외부에 제공하는 메서드
# 세터: 객체의 내부 속성 값을 변경할 수 있도록 외부에 제공하는 메서드
# --> 외부에서 직접 변수에 접근하지 못하도록 하고,  메서드를 통해 접근할 때 사용

# @property 데코레이터
# 메서드를 속성처럼 사용할 수 있도록 만들어주는 파이썬의 내장 데코레이터
# + 주로 캡슐화된(private) 인스턴스 변수에 접근하거나 수정할 대, 메서드 호출처럼 보이지 않게 하면서 내부 로직을 수정할 수 있도록 도와줌
# + 외부에는 속성처럼 보이게 하면서, 내부에서는 함수 호출을 통한 유효성 검사 또는 부가처리를 하고 싶을 때 사용

# @property 데코레이터
# - 메서드를 속성처럼 보이게 만들어주는 데코레이터

class Ex:
    def __init__(self):
        self.value = 0

    # getter
    @property
    def value(self):
        return self.__value
    
    # setter
    @value.setter
    def value(self, val):
        if val < 0:
            print("우효하지 않는 값입니다.")
        else:
            self.__value = val

ex1 = Ex()
print(ex1.value)
ex1.value = 100
print(ex1.value)
ex1.value = -100
print(ex1.value)

# 실습 3-1. UswerAccount 클래스: 비밀번호 보호

class UserAccount:
    def __init__(self, username, password):
        # 생성자에서 사용자 이름과 비밀번호 초기화(0으로 초기화하는 것이 아님;;)
        self.username = username
        self.__password = password # private으로 선언

    def change_password(self, old_pw, new_pw):
        if old_pw != self.__password:
            print("비밀번호 불일치")
        else:
            self.__password = new_pw
            print("비밀번호 변경됨")

    def check_password(self, pw):
        if self.__password == pw:
            print(True)
        else:
            print(False)

    # def check_password(self, password):
        # return self.__password == password

bank = UserAccount("Dongyun2", 12345678) # 계좌 이용자, 비밀번호 입력
bank.change_password(12345678, 7777) # 비밀번호 7777로 변경
bank.check_password(775847) # 비밀번호 불일치 확인
bank.change_password(7777, 6666) # 변경된 비밀번호를 다른 비밀번호(6666)로 다시 변경
bank.change_password(1235, 77) # 비밀번호 불일치 유도
bank.check_password(6666) # 변경된 비밀번호 확인

# print(bank.username) # "Dongyun2"
# print(user.__password) # 출력안됨

# 실습 3-2 Student 클래스: 성적검증(@property사용)

class Student:
    def __init__(self, name, __score):
        self.name = name
        self.__score = __score

    @property # getter
    def score(self):
        return self.__score
    
    @score.setter # setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("성적은 0에서 100 사이여야 합니다.")
        
s1 = Student("Alice", 85)
print(s1.name)
print(s1.score) # 85

# s1.score = 105 # ValueError
s1.score = 95
print(s1.score) # 95

# 상속의 개념과 필요성
# 기존에 정의된 클래스의 속성과 메서드를 물려받아 새로운클래스를 만드는 것
# + 코드의 재사용을 높임
# + 공통된 기능은 부모 클래스에 정의하고, 자식 클래스에서 확장하거나 수정

# 상속
# 부모 클래스의 속성과 메서드를 물려받아 새로운 자녀 클래스를 만드는 것을 의미함


# 상속 기본 문법
# 부모 클래스
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print("동물이 울음소리를 냅니다.")

# # 자식 클래스
# class Dog(Animal):
#     pass

# dog = Dog("구름이")
# dog.bark()
# print(dog.name)

# super()를 사용한 부모 생성자 호출
# super(): 부모클래스의 메서드나 생성자를 호출할 수 있도록 해주는 내장함수
# + 자식 클래스에서 부모 클래스의 메서드, 생성자, 속성을 명시적 클래스명 없이 호출할 때 사용
# + 코드의 유연성과 유지보수성 향상

# super() 사용시 주의사항
# super()는 반드시 클래스 내부 메서드에서 사용해야함
# 생성자에서 super().__init__()를 호출하지 않으면 부모 생성자가 생략됨
# super().__init__()는 Parent.__init__(self)를 직접 호출하는것과 유사하지만, 상속구조가 변경되어도 자동 추적되므로 안전함

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("동물이 울음소리를 냅니다.")

# 자식 클래스
class Dog(Animal):
    def __init__(self, name, age, species):
        # super는 부모를 가리킴
        super().__init__(name, age)
        self.species = species

        # 오버라이딩
    def bark(self):
        super().bark()
        print("월월이청청")

dog = Dog("구름이", 17, "포메라니안")
dog.bark()
print(dog.name)
print(dog.age)
print(dog.species)

# 메서드 오버라이딩
# 부모 클래스의 메서드를 자식 클래스에서 동일한 이름으로 다시 정의하는 것
# 기존 기능을 새로운 방식으로 변경하거나 특화된 동작을 구현할 수 있음

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printinfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        self.sides = sides
        self.base = base
        self.height = height

    # 오버라이딩
    def area(self):

        print(f"사각형의 넓이: {self.base * self.height}")
    
class Triangle(Shape):
    def __init__(self, sides, base, height):
        self.sides = sides
        self.base = base
        self.height = height
    
    # 오버라이딩
    def area(self):
        print(f"삼각형의 넓이: {(self.base * self.height) /2}")

# 실행

shape = Shape(20, 7)
shape.printinfo()
shape.area()

rect = Rectangle(4, 10, 17)
rect.printinfo()
rect.area()

tri = Triangle(3, 15, 13)
tri.printinfo()
tri.area()

#  추상 클래스
# 직접 인스턴스를 만들 수 없으며, 반드시 자식 클래스에서 구현을 완성해야 하는 클래스
# + 공통적인 구조는 정의하되, 구체적인 동작은 상속받은 클래스에서 구형하도록 강제하는 용도로 사용

# 추상 클래스의 목적
# + 공통 인터페이스 정의: 모든 하위 클래스가 따라야 할 메서드 구조 정의
# + 일관성 유지: API나 프레임워크의 통일된 동작 보장
# + 구현강제: 필수 메서드를 구현하지 않으면 오류 발생
# + 코드 재사용 + 설계 명확화: 일부 구현을 제공하면서도 확장 기능하도록 설계

# 추상 클래스(Abstract Class)
# 클래스의 구조를 정의하는 클래스

from abc import ABC, abstractmethod # abc에서, ABC, abstractmethod를 가져와라.

class Animal(ABC):
    
    # 추상 메서드
    @abstractmethod
    def bark(self): # 자식 클래서에서 모조건 구현을 하라고 강제하는거임
        pass

class Dog(Animal):
    def bark(self):
        print("멍멍")

# a = Animal()
a = Dog()
a.bark()

# 실습 5. 추상 클래스 Payment 구현

class Payment(ABC):

    # 추상 메서드
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")

money = CardPayment()
money.pay(10000000000000000000000)

moneyyyy = CashPayment()
moneyyyy.pay(2398623946912837612984986748498487)
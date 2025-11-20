# 함수
# + 특정 작업을 수행하는 코드 블록

# 함수의 필요성
# 1. 코드 재사용(재활용성)
# + 동일한 작업을 반복할 때 매번 코드를 다시 작성할 필요 없음 -> 한 번 정의한 함수는 여러 번 호출 가능
# 2. 코드의 가독성 향상
# + 기능 단위로 묶어서 코드가 논리적으로 명확해짐
# + 다른 사람이 읽고 이해하기 쉬워짐
# 3. 유지보수 용이성
# + 수정이 필요한 부분이 생기면 함수 내부만 고치면 됨 -> 중복 코드 수정의 부담 감소
# 4. 프로그램의 구조화(모듈화)
# + 큰 프로그램을 여러 개의 작은 작업으로 나누어 체계적으로 관리
# + 각 함수는 하난의 "기능"만 담당하게 설계하는 것이 원칙(단일 책임 원칙)
# 5. 협업과 확장성
# + 개발자끼리 작업 분담이 쉬움
# + 작은 단위의 함수가 쌓여 큰 기능을 구성(계층적 설계)

# 내장함수와 사용자 정의 함수
# + 내장함수: 파이썬이 기본적으로 제공하는 함수들로, 별도 정의 없이 바로 사용할 수 있는 함수 ex) print(), len()
# + 사용자 정의 함수: 사용자가 def 키워드를 사용하여 직접 만든 함수

'''
함수(function)
- 특정 작업을 수행하는 코드들의 모음
- 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
- 특정한 코드들을 재사용할 수 있게 함
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의: define의 약자로 def사용

def 함수이름 (매개변수):
    # 실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 시행(호출, call)
result = 함수이름("인자")
print(result)

# 매개변수(parameter): 매개 + 변수
# + 매개: 둘 사이를 연결해줌
# + 함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할

# 함수 뒤 괄호: 함수에 전달할 값이 없더라도 실행시 괄호 반드시 필요
# 인자: 함수 호출 시 전달하는 값

# 함수의 필요성 예제
# a = 10
# b = 20

# if a > b:
#     print(a - b)
# else:
#     print(b + a)

# c = 30
# d = 40

# if c > d:
#     print(c - d)
# else:
#     print(c + d)

#================

# def my_func(a, b):
#     if a > b:
#         return(a - b)
#     else:
#         return(b + a)

# print(my_func(10, 20))
# print(my_func(30, 40))

# 실습 1. 사칙연산 계산기 함수 만들기

# def calculator(a, b, operator):
#     #operator = "+" or "-" or "*" or "/"
#     if (operator == "+"):
#         return (a + b)
#     elif (operator == "-"):
#         return (a - b)
#     elif (operator == "*"):
#         return (a * b)
#     elif (operator == "/"):
#         return float(a / b)
#     else:
#         return("지원하지 않는 연산입니다.")
    
# print(calculator(4, 5, "*"))
# print(calculator(7, 9, "-"))
# print(calculator(43454223, 56462, "/"))
# print(calculator(65423, 3121, "+"))
# print(calculator(4, 5, "#%^"))


# # 키워드 인자 
# # 예시 1.
# print("안녕하세요", "반값습니다!", sep='-', end='/')

# # 예시 2.
# def my_func(a, b, c=None, operator=None):
#     if operator =="+":
#         return a + b
#     else:
#         return c

# print(my_func(10, 20, operator="+"))

# # 기본값 인자
# # 단, 기본값 매개변수는 뒤쪽에 위치해야함
# def greet(name, message="안녕하세요~!"):
#     print(f"{name}님, {message}")

# # 호출 시 인자 생량 -> 기본값 사용
# greet("Dongyun2")
# greet("ff", "반갑습니다!")

# # 위치 가변 인자(*args <- arguments)
# # 여러 개의 값을 유동적으로 받을 수 있음
# # 값이 튜플 형태로 받아짐

# def add_all(*args):
#     return sum(args)

# print(add_all(1, 2, 3, 4, 5))

# # 키워드 가변인자(**kwargs)
# # 여러 키워드 인자를 유동적으로 받을 수 있음
# # 딕셔너리 형태로 값이 입력됨

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name = "동윤2", age = 26, city = "포항")

# 가변 인자 사용시 주의사항
# --> 위치 인자 --> 기본값 인자 --> *args --> **kwargs 순서로 정의해야 함

# 매개변수 전달 방식
# 파이썬은 값 전달(call by value)이 아닌, 객체 참조에 의한 전달(call by object reference)방식
# + 변경 가능한 객체(mutable): 함수 내 변경 --> 외부에도 영향
# + 변경 불가능한 객체(immutable): 함수 내 변경 --> 외부 영향 없음

# # *args 사용 연습

# # 실습 2-1. 숫자 여러 개의 평균 구하기

# def average(*args):
    
#     return sum(args) / len(args)

# print(average(1, 3, 5, 4, 5, 6))

# # 실습 2-2. 가장 긴 문자열 찾기(max함수)
# def longgest_str(*args):
    
#         return max(args, key=len)
    
# print(longgest_str("안녕", "안녕하시렵니까", "쎕쎄요는 나의 유행어", "에어컨~"))

# # *kwargs 사용 연습

# # 실습 2-3. 사용자 정보 출력 함수
# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# info(user_name = "동윤2", age = 26, city = "포항", phone_number = "010-1234-5678")

# # 실습 2-4. 할인 계산기
# def bargain(**kwargs):
#     sale_items = {}

#     for key, value in kwargs.items():

#         sale_items[key] = int(value * 0.9)

#         print(f"{key}: {value}")

#     return sale_items

# print(bargain(cable = 18000, bottle = 5000, chair = 64000, wallet = 50000))


# 파이썬의 메모리 구조

# 스택 영역
# + 지역변수(local variable), 매개변수(parameter) 등이 저장되는 공간
# 힙 영역
# + 파이썬에서 생성되는 모든 객체(숫자, 문자열, 리스트, 딕셔너리, 클래스 등)가 저장되는 공간

# 변수의 유효 범위(scope)
# scope: 어떤 이름(변수, 함수 등)을 참조할 수 있는 코드의 범위
# 파이썬의 이름 규칙 : LEGB Rule
# local, enclosing, global, built-in

# 지역변수(local variable)
# + 함수 내부에서 선언된 변수
# + 함수가 호출될 때 생성되고, 함수가 끝나면 소멸됨

# 전력변수(global variable)
# + 함수 외부에서 선언된 변수
# + 프로그램 전체에서 접근 가능(단, 함수 내부에서 값 변경은 제한됨)


# 전역변수: 함수 밖에 선언된 변수
# 지역변수: 함수 안에 선언된 변수

# 전역변수
# x = 200

# # 예제
# def my_func():
#      #지역변수
#      x = 10
#      print(x)

# my_func()

# print("함수 밖", x)


# 예제2(UnboundLocalError발생)
# x = 10
# def my_func2():
#     # x = 20
#     x = x + 5
#     print(x)

# my_func2()

# print("전역변수", x)

# 예제3(global 사용 예제)
# x = 10
# def my_func3():
#     global x # 전역변수 사용 선언
#     x = x + 5
#     print("지역", x)

# my_func3()

# print("전역", x)

# 권장되는 패턴
# 부수효과(side effect)를 발생시키지 않는 함수를 위주로 프로그래밍

# x = 10

# def my_func4(x):
#     x += 5
#     return x

# x = my_func4(x)

# print("전역", x)

# 실습 3. 로그인/로그아웃 전역 상채 관리

current_user = ''
name = ''

def login(name):
    global current_user

    if current_user:
        print(f"이미 {current_user}(이/가) 로그인되어 있습니다.")
    else:
        current_user += name
        print(f"{name}님 로그인 성공")
        
    return current_user
    

def logout():
    global current_user

    current_user = '' # 걍 초기화 해버림

    print("로그아웃 되었습니다.")
    
    return current_user
    
login("동윤2")
login("빠니보틀")
logout()
login("빠니보틀")
print(current_user)
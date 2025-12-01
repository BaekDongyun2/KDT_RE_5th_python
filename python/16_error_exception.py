# 에러(error)와 예외(exception)

# 에러
# + 프로그램이 실행 자체를 할 수 없게 만드는 치명적이 문제
#+ 예) 구문(syntax) 오류: 문법에 맞지 않거나 오타가 났을 경우 발생하는 오류/ IDE에서 실행 전에 알 수 있음

# 예외
# + 실행 중(runtime)에 발생하며, 코드가 실행을 시작했으나 특정 상황에서 중단되는 문제
# + 예) 파일을 읽어 사용하려는 데 파일이 없는 경우, 리스트 값을 출력하려는 데 리스트 요소가 없는 경우 등 -> 에러가 발생되면 프로그램의 동작이 중지 또는 종료됨

# 예외 처리
# + 에러가 발생할만한 부분을 예측하여, 미리 예외 상황에 대한 처리를 하는 것. Try 블록에서 발생한 예외를 except 블록에서 처리한다.
# 프로그램이 예기치 않게 종료되는 것을 방지

# 예외 처리 기본 문법
# try:
#   # 예외가 발생할 수 있는 코드
# except:
#   # 예외가 발생했을 때 실행할 코드

# 예외 처리 기본 문법
try:
    # 예외가 발생할 수 있는 코드
    pass
except:
    # 예외가 발생했을 때 실행할 코드
    # 특정 에러를 지정 가능
    pass

# 예외 종류
# 1. 인덱스 에러
# shop = ['반팔', '청바지', '이어폰', '키보드']
# print(shop[2])
# print(shop[10]) # IndexError: list index out of range
# print("예외 처리")

# 2. ValueError
# + 부적절한 값을 가진 인자를 받았을 댸 발생
# number = int("hello") # ValueError: invalid literal for int() with base 10: 'hello'

# print(shop.index("X")) # ValueError: 'X' is not in list

# 3. ZeroDivisionError
# + 0으로 나눌 때 발생
# print(5 / 0) # ZeroDivisionError: division by zero

# 4. NameError
# + 존재하지 않는 변수를 호출할 때
# print(x) # NameError: name 'x' is not defined

# 5. FileNotFoundError
# + 존재하지 않는 파일을 호출할 때
# file = open('test.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# 예외 처리
# 1) 단일 except
# try:
#     num = int(input("숫자를 입력하세요"))
#     print(10 / num)
# except:
#     print("예외 발생")

# 2) 특정 예외 처리
# try:
#     num = int(input("숫자를 입력하세요"))
#     print(10 / num)
# except ValueError as e:
#     print("숫자가 아닙니다.", e)
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.", e)
# else 절은 try 블록에서 예외가 발생하지 않았을 때 실행
# finally 절은 예외 발생 여부와 관계없이 항상 실행됨
# raise 절은 일반적으로 함수나 로직에서 잘못된 조건을 감지했을 때 의도적으로 예외를 발생시킴
'''
# 예외 처리 기본 문법
try:
    # 예외가 발생할 수 있는 코드
    pass
except 오류내용1:
    # 예외가 발생했을 때 실행할 코드
    # 특정 에러를 지정 가능
    pass
except 오류내용2:
    pass

else:
    # 에외 없는 경웽 실행
finally:
    # 예외 발생 여부와 상관없이 실행
    '''

# 실습 1
# try:
#     num = int(input("숫자를 입력하세요"))
# except ValueError as e:
#     print(e)
#     num = -1
# if num > 0 :
#     print("0보다 큽니다.")
# else:
#     print("숫자가 아닙니다.")

# 실습 2

# def calculator():

#     while True:
#         try:
#             num1 = int(input("연산할 숫자를 입력하세요"))
#             break
#         except ValueError as e1:
#             print("숫자가 아닙니다. 다시 입력해주세요.")
        
#     while True:
#         try:
#             operator = input("연산자를 입력하세요.")
#             if operator in ["+", "-", "*", "/"]:
#                 break
#         except:
#             print("연산자가 아닙니다. 다시 입력해주세요.")
        
#     while True:
#         try:
#             num2 = int(input("연산할 숫자를 입력하세요"))
#             break
#         except ValueError as e1:
#             print("숫자가 아닙니다. 다시 입력해주세요.")

#     if (operator == "+"):
#         result = num1 + num2
#     elif (operator == "-"):
#         result = num1 - num2
#     elif (operator == "*"):
#         result = num1 * num2
#     elif (operator == "/"):
#         result =  float(num1 / num2)
        
#     print(f"결과값은 <{num1} {operator} {num2} = {result} 입니다.>")

# calculator()

def print_result(n1, op, n2, result):
    print(f"{n1} {op} {n2} = {result}")

while True:
    try:
        num1 = float(input("첫 번째 숫자: "))
        op = input("연산자: ")
        num2 = float(input("두 번째 숫자: "))

        if op not in ["+", "-", "*", "/"]:
            raise ValueError("잘못된 연산자입니다.")
        
        if op == '/' and num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        
        # 계산
        if (op == "+"):
            result = num1 + num2
        elif (op == "-"):
            result = num1 - num2
        elif (op == "*"):
            result = num1 * num2
        else:
            result = num1 / num2

        print(f"{num1} {op} {num2} = {result}")
        break
    
    except ValueError:
        print("입력이 잘못되었습니다. 다시 입력하세요.\n")
    except ZeroDivisionError as e:
        print(e)
        print("0으로 나눌 수 없습니다. 다시 입력하세요.\n")
    except Exception:
        print("알 수 없는 오류가 발생했습니다.\n")
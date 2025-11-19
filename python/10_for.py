# 반복(iteration)의 정의
# --> 동일한 작업(코드 블록)을 여러번 실행하는 구조적 프로그래밍 기법
# --> python은 for 또는 while문을 사용하여 반복문을 구현함

# 반복문의 사용목적
# + 동일한 작업의 반복 실행
# + 가독성과 유지보수성 향상
# + 자동화와 대량 처리

# for 문
# 시퀀스/이리터블(순회가능한) 객체의 항목을 하나씩 꺼내서 실행 블록에 전달하는 반복문

# for 변수 in 이터러블: 기본구조
# + 변수: 각 반복마다 이터러블 객체의 항목을 하나씩 대입받는 변수
# + 이터러블: 순회 가능한 객체(list, tuple, str, dict, set, range 등)
# + : <-- 코드 블록의 시작을 알림
# + 들여쓰기를 통해 코드 블록 범위를 명확히 구분
'''
# 리스트 반복

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")

# 문자열 반복

text = "Hello"
for ch in text:
    print (ch)
# + 문자열은 문자 하나하나가 반복 대상
# + 문자열은 순서 있는 시퀀스이므로 인덱스로 접근하거나 반복문으로 순회가능

my_str = "Apple"

for char in my_str:
    print(char)

# 튜플 반복
coords = [(1, 2), (10, 15), (-6, 8)]
# 언패킹 (구조분해 가능)
for x,y in coords:
    print(f"x좌표: {x}, y좌표: {y}")

# 딕셔너리 반복
person = {"name" : "Dongyun", "age" : 26, "address" : "seoul"}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}")

# value 만 가져오기
for value in person.values():
    print(f"value: {value}")

# item 가져오기
for key, value in person.items():
    print(f"key: {key}, value: {value}")

# set 반복
my_set = {1, 2, 3, 4}

for s in my_set:
    print(s)


# 실습 1-1
numbers = [3, 6, 1, 8, 4]
for num in numbers:
    num *= 2
    print(num)

# 실습 1-2

words = ["apple", "banana", "kiwi", "grape"]
for word in words:
    length = len(word) # words 리스트 안의 요소인 word의 길이를 length에 할당해야 함
    print(length)


#for length in words:
#    length = len(words)
#    print(length)
#이렇게 반복문을 구성해버리면
#length 변수는 word리스트의 길이를 계산할거니까
#항상 4가 리스트 요소의 개수인 4번 반복하여 출력이 됨
#너무 당연한 말이긴 해. 


# 실습 1-3
x_values = []
y_values = []

coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print(x_values, y_values)


# for 문과 range() <-- 지정된 범위의 시퀀스를 생성하는 내장 함수
# + 주로 for문과 함께 사용되어 반복 횟수를 제어함
# range(start, stop[, step])
# start: 시작 정수, stop: stop -1까지 생성, step: 정수 증가 간격(기본값 1)
# range 함수: 지정된 범위의 정수 시퀀스 생성

# 기본문법
# range(start, end, step)
# - start: 생략가능, 기본값 0
# - end: end - 1 까지 생성
# - step: 생략가능, 기본값 1

range(1, 5)

for i in range(1,5):
    print(i)
for i in [1, 2, 3, 4]:
    print(i)

print("======================")

# start 생략
for i in range(10):
    print(i)

# step 지정
for i in range(0, 11, 2):
    print(i)

print("======================")

for j in range(10, -1, -1):
    print(j)

# 실습 2 -1

n = int(input())
for num in range(1, n):
    total = sum(range(1, n+1))
print(total)


# 실습 2-2

n = int(input())
for num in range(1, 10):
    multiplier = n * num
    print(multiplier)

# 실습 2-3

sigma = 0
for num in range(1, 101):
    if (num % 3) == 0:
        sigma += num
print(sigma)

# 실습 2-4

n = int(input())
for even in range(1, n+1):
    if ((even % 2) == 0 and (even % 5) == 0): # or just (even % 10)
        print(even)

#  루프 제어문
# break: 반복 즉시 중단
# 반복문 실행 중 break를 만나면 반복문을 즉시 종료함
# continue: 현재 반복만 건너뛰고 다음 반복 수행
# 반복문 실행 중 continue를 만나면 다음 반복문으로 넘어감
# pass: 아무동작하지 않고 자리만 차지
# 반복문 실행 블록 구현 전 에러 방지용으로 사용
# for - else: 반복이 정상적으로 모두 수행된 경우 else 블록을 실행

# 루프 제어문
# + 특정 조건 하에서만 작동하도록 구현


# break: 반복을 즉시 중단
for i in range(10):
#   print(i)가 여기 있었다면 0에서 5까지 출력이 됐을 것이다.
    if i == 5:
        break
    print (i)
print("반복종료")

# continue: 현재 반복을 넘어감
for i in range(5):
    if i == 2:
        print("continue = 건너뜀")
        continue
    print(i)
print("반복종료")

# pass: 아무 동작도 하지 않고 차리만 차지
for i in range(10):
    pass

# for - else: 반복이 정상적으로 모두 수행된 경우 else 블록을 진행
# + break로 종료시 else 구문 실행이 되지 않는다.
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("반복종료")

# 중첩 for 문
# + 하나의 for 블록 안에 또 다른 for문이 들어있는 구조
# + 2차원 이상의데이터 구조나 반복 패턴을 처리할 때 사용 됨

# 이중 for 문
for i in range(5):
    for j in range(5):
        print("i, j", i, j)
    print()

# 실습 3-1

for num1 in range(1, 10):
    print(f"[  {num1}단  ]")
    for num2 in range(1, 10):
        multiplier = num1 * num2
        print(f"{num1} X {num2} = {multiplier}")
'''


'''
# 실습 3-2(왼쪽 정렬)

n = int(input("몇 줄 만들거냐? : "))

for i in range(1, n+1): # 높이
    line ='' # 매 줄마다 새로 초기화한다
    for j in range(i):
        line += '*'
    print(line)
      
# 실습 3-2(가운데 정렬)

n = int(input("몇 줄 만들거냐? : "))

line ='' # 매 줄마다 새로 초기화

for i in range(1, n+1): # 높이
    line ='' # 매 줄마다 새로 초기화
    # 왼쪽 공백
    for j in range(n-i):
        line += ' '
    # 별
    for k in range(2*i-1):
        line += '*'
    print(line)

# 실습 3-2(오른쪽 정렬)

n = int(input("몇 줄 만들거냐? : "))

for i in range(1, n+1):
    line = ''
    for j in range(n-i):
        line += ' '
    for k in range(i):
        line += '*'
    print(line)
'''

# for i in range(2, 10):
#     print(f"[ {i}단 ]")
#     for j in range(1, 10):
#         num = i * j
#         print(f"{i} X {j} = {num}")

#n = int(input("몇 줄로 만들거냐: "))

# for i in range(1, n+1): # 별 피라미드의 높이 설정 반복문
#     line = "" # 매 줄마다 초기화
#     for j in range(n-i): # 왼쪽 공백
#         line += " "
#     for k in range(2 * i - 1): # 별
#         line += "*"
#     print(line)

# for i in range(1, n+1):
#     line = ''
#     for j in range(n-i):
#         line += ' '
#     for k in range(i):
#         line += '*'
#     print(line)


# 리스트 컴프리헨션(list comprehension)
# - for문을 리스트에 한줄로 축약하여 새 리스트를 생성하는 문법
# - [표현식(리스트의 원소) for 변수 in 반복대상 if 조건]
# - 표현식: 값을 유도하는 식(표현)


# # for문 이용
# squares = []
# for x in range(1, 6):
#     squares.append(x**2)
# print(squares)

# # 리스트 컴프리헨션
# squares2 = [x**2 for x in range(1, 6)]
# print(squares2)

# # 조건문 추가하기
# square3 = [x**2 for x in range(1, 11) if x % 2 ==0]
# print(square3)

# 실습 4-1
power2 = [x**2 for x in range(1, 11)]
print(power2)

# 실습 4-2
multi3 = [y for y in range(1, 51) if y % 3 == 0]
print(multi3)

# 실습 4-3
fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

longg = [fruit for fruit in fruits if len(fruit) >= 5]
print(longg)

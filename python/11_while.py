# while문
# + 조건이 True인 동안 루프 안의 코드를 반복 실행하는 반복문
# + 조건식이 False가 되면 반복을 멈추고 루프를 빠져나옴

# while 조건식:
#   실행할 코드

# while문의 필요성
# + 반복 횟수가 정해지지 않았을 때 ex) 사용자가 'exit'을 입력할 때 까지 계속 입력 받기
# + 조건 기반 루프가 필요할 때 ex) 파일이 존재하는 동안 반복 처리
# + 무한 루프 + 조건 분기 구조에 유용 ex) 게임 루프, 서버 대기 루프 등

# 실행 흐름
# 1. 조건실 평가
# + 조건식이 True이면 블록 내부 코드 실행
# + 조건식이 False이면 반복 종료
# 2. 블록 실행 후 다시 조건 평가
# + 조건이 여전히 True이면 다시 반복
# 3. 조건이 False가 될 때까지 반복

'''
while문
- 조건이 True인 동안 코드를 반복하는 반복문
- 조건이 False가 되면 반복을 멈춤
- 반복횟수가 정해지지 않았을 때 사용

'''

# while문 기본 문법
# 조건: 참/거짓을 구분할 수 있는 문장
# while 조건:
    # 반복할 코드

# 무한루프
# 사용시 주의, 반드시 종료 조건이 있어야 함
# while True:
#     print("반복문") # ctrl + C로 무한루프를 빠져나오셈


# 예시
# 변수 i를 1로 초기화
i = 1

# i가 5이하일 동안 반복
while i <= 5:
    print(i) # i출력
    i = i + 1 # i에 1을 더해서 갱신
    print(i) # 실행 후 i 값을 증가시키지 않으면 무한 루프에 빠질 수 있음

# 예제 1
light = "green"
while light == "green" :
    print("계속 가세요")
    light = input("신호등의 신호를 입력하세요(green/red/yellow): ")
print("중지")

# # 예제 2
i = 0

while i < 5:
    print(i, "반복")
    i += 1
print("반복 종료")

# 실습 1-1

secret_code = Dongyun2

while secret_code != "Dongyun2":

    print("다시 입력해.")
    secret_code = input("비밀 코드를 입력하세여(ex/ 열려라 참깨) :")

print("성공!")

# # 실습 1-2
import random

print("1~100 사이의 무작위 수를 생성 중입니다.")

num = int
answer = random.randint(1, 100)
iteration = 0

while num != answer:
    num = int(input("숫자를 입력하시오. : "))
    iteration += 1

    if num > answer:
        print(f"{num} 보다는 작아")
    elif num < answer:
        print(f"{num} 보다는 커")
    else:
        print(f"정답! {answer} 입니다!!` ")

print(f"총 {iteration}번 만에 정답을 맞췄어.")

# # 루프 제어문
# running = True
# while running:
#     if 조건1:
#         running = False
    
#     if 조건2:
#         running = False

# # 예제 1
i = 0

while True:
    print(i, "실행")
    my_select = input("메뉴를 골라주세요: ")

    if my_select == "종료":
        break

    i += 1
print("반복문 종료")

# continue

i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("반복종료")

# 실습 2-1

secret_code = input("비밀 코드를 입력하세여(ex/ 열려라 참깨) :")

while secret_code != "Dongyun2":

    print("다시 입력해.")
    secret_code = input("비밀 코드를 입력하세여(ex/ 열려라 참깨) :")

    if secret_code == "Dongyun2":
        print("입장완료요~")
        break


# 실습 2-2

times = 0 
sum_age = 0

age = 0

while times < 5:
   
    age = int(input("나이를 입력하세요: "))

    
    if (age <= 0 or age > 120):
        print("잘못된 입력입니다. 다시 입력하세여.")
        continue

    sum_age += age
    times += 1
    
    print(f"입력횟수: {times}")
    average_age = sum_age / times

    if times >= 5:
        break
print(sum_age, average_age)

    
# 중첩 while문
# 예제
dan =2 
while dan <= 9:
    num = 1
    print(f"{dan}단")
    
    while num <=9:
        num += 1
        if num % 2 == 0:
            continue
        else:
            print(f"{dan} X {num} = {dan * num}")
        
    print()
    dan += 1

# 실습 3

ID = input("고갱님의 ID를 입력하세요. : ")

while ID != "Dongyun2":

    print("ㅠㅠ틀렸어요. 다시 입력하세요.")
    ID = input("고갱님의 ID를 입력하세요. : ")

    while ID == "Dongyun2":
        
        PW = input("고갱님의 PW를 입력하세요. : ")
        
        while PW != "yeahyeah":
             print("ㅠㅠ틀렸어요. 다시 입력하세요.")
             PW = input("고갱님의 PW를 입력하세요. : ")
    
        print("로그인 성공~")
        break

# 분리된 while로.
while True:
    user_id = input("고갱님의 ID를 입력하세요. : ")
    if user_id == ID:
        break
    print("ㅠㅠ틀렸어요. 다시 입력하세요.")

while True:
    user_pw = input("고갱님의 PW를 입력하세요. : ")
    if user_pw == PW:
        print("로그인 성공~")
        break
    print("ㅠㅠ틀렸어요. 다시 입력하세요.")

# 실습 3 추가 문제
while True:
    ID = "Dongyun2"
    PW = "yeahyeah"

    print('''=====로그인 화면=====
    1. 로그인
    2. 종료''')
    num = int(input("선택 :"))

    if num == 2:
        print("종료합니다.")

    if num == 1:
        
            ID = input("ID :")
            PW = input("PW :")

            while ((ID != "Dongyun2") or (PW != "yeahyeah")):

                print("로그인 실패다! 다시 시도하거라.")
                ID = input("ID :")
                PW = input("PW :")

            while ((ID == "Dongyun2") and (PW == "yeahyeah")):
                    
                print('''로그인 성공했도다!
                        
=====메뉴=====
1. 정보 보기
2. 설정
3. 로그아웃
==============''')
                n = input("메뉴 선택하거라. : ")
                
                if n == "1":
                    print("회원님의 정보입니다.")
                    
                elif n == "2":
                    print("설정 메뉴입니다.")
                    
                elif n == "3":
                    print("로그아웃합니다.")
                    break
                else:
                    print("다시 입력하세요.")
                continue
    else:
        print("다시 입력하세요.")


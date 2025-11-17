'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건: 참/거짓을 구분할 수 있은 문장
'''
'''
# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행

a = int(input())
if a > 10:
    print("a는 10보다 크다.")
else:
    print("a는 10보다 작다.")
print("조건문 종료")

# 들여쓰기 에러 예시 <- 들여쓰기를 안하면
if a > 10 :
    print("조건문 종료")
# print("a는 10보다 크다") # IndetantationError

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
if a > 100:
    pass

# 실습1
todays_weather = input("오늘의 날씨를 입력하세요.(비/맑음): ")

if (todays_weather == "비"):
    print("우산을 챙기세요!")
if (todays_weather == "맑음"):
    print("썬크림을 바르세요!")

# if-else문
# 조건이 참일 때는 if문을 조건이 거짓일 때는 else문을 실행
# else -> ~아니라면의 의미 -> 조건이 필요x, if 문과 반드시 같이 나와야 함.

a = int(input())
if a > 10:
    print("a는 10보다 커")
else:
    print("a는 10보다 작아")

# 실습2

a = int(input("정수를 입력해주세요.: "))
b = a % 2
if (b == 0):
    print("짝수 입니다.")
else:
    print("홀수 입니다.")



# if-elif-else구문
# elif: else if의 약자
# elif에서 조건을 반드시 기록
# if가 있어야만 사용 가능
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

age = int(input("나이를 입력하세요: "))
if (0 <= age & age <= 12):
    print("나이구간: 0~12세 / 관람 가능 등급: 전체 관람가")
if (13 <= age & age <= 15):
    print("나이구간: 13~15세 / 관람 가능 등급: 12세 이상 관람가")
if (16 <= age & age <= 18):
    print("나이구간: 16~18세 / 관람 가능 등급: 15세 이상 관람가")
else:
    print("나이구간: 19세 이상 / 관람 가능 등급: 청소년 관람불가")

seconds = int(input("시간(초)을 입력해라"))

if (seconds < 60):
    print(seconds, "초")
elif (60 <= seconds & seconds <3600):
    print((seconds // 60), "분", (seconds % 60), "초")
elif (3600 <= seconds):
    print((seconds // 3600), "시간", ((seconds // 3600) // 60), "분", ((seconds % 3600) % 60), "초")


# 중첩 조건문
# 하나의 if문 안에 또 다른 if문을 사용하는 것

username = input("관리자 아이디를 입력해 :")
password = input("비밀번호를 입력해 :")

if username =="admin":
    if password == "abcd":
        print("로그인 성공")
    else:
        print("비밀번호가 잘못됐습니다.")
        
else:
    print("잘못된 사용자입니다.")
'''

# 실습

money = int(input("금액 내라"))
item = dict{"김밥":2500, "삼각김밥" : 1500, "도시락" : 4000}

items = input(
           '''뭐 살건데?
              김밥        2500원
              삼각김밥     1500원
              도시락       4000원
              입력해: '''). split(", ")

total_price = 0

if "김밥" in items:
    total_price = total_price + item("김밥")
if "삼각김밥" in items:
    total_price = total_price + item("삼각김밥")
if "도시락" in items:
    total_price = total_price + item("도시락")

print(f"총 금액은 {total_price}원 입니다.")

if (money >= total_price):
    print("구매 성공했습니다~")
else:
    print("금액이 부족합니다.")'''
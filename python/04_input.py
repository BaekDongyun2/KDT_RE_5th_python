# 사용자 입력 (input)
# - input 함수: 콘솔을 통해 사용자로부터 문자열 형태로 입력을 받음

# input 함수 사용법
# my_input = input("콘솔에 띄울설명")
# name = input("이름을 입력하세요: ")
# print("안녕하세요, ", name)
'''
# 숫자로 활용 시 형 변환 필요
a = input() # 정수로 받고자 할 경우엔 int(input())
b = input() # 정수로 받고자 할 경우엔 int(input())
print(a + b) # 문자열로 인식됨.

c = float(input())
d = float(input())
print(c + d)
'
# split으로 문자열 나누기 --> 문자열이 list로 나뉘어짐
fruit = "사과 참외 수박". split()
print(fruit)

# split: 문자열만 사용 가능한 함수(숫자 사용 불가)
# split의 괄호 안에 구분자 지정 가능(기본: 공백)

# split + input으로 여러 변수에 입력하기
과일1, 과일2, 과일3 = input(). split()
print(과일1, 과일2, 과일3)

# 문자열을 쪼개주는 함수: split()
# 기본 구분자: 공백

# 다른 구분자 사용
apple, banana, grape = input().split("-")
print(apple, banana, grape)

'''
이름, 나이 = input().split(",")
print(f"안녕하세요. 저는 {이름}이고, {나이}살입니다.")

가로 = int(input("가로를 입력하세요."))
세로 = int(input("세로를 입력하세요."))

넓이 = 가로 * 세로
둘레 = 2 * (가로 + 세로)
print(f"넓이: {넓이}\
        둘레: {둘레}")

num1, num2, num3, num4 =input(). split(" ")
print(f"천의 자리: num1\n 백의 자리: num2\n 십의 자리: num3\n 일의 자리: num4\n")
# 사실 자릿수를 확인할 때는 입력받는 정수에 list를 사용하는 게 더 맞다고 생각됨


사람1, 사람2, 사람3 = input("발표자 이름 3명을 입력하세요: "). split(", ")
주제1, 주제2, 주제3 = input("발표 주제 3개를 입력하세요:"). split(", ")

print(f"발표 순서 안내입니다.\
       1조 발표자: {사람1} - 주제: {주제1}\
       2조 발표자: {사람2} - 주제: {주제2}\
       3조 발표자: {사람3} - 주제: {주제3} ")

year, month, day = input("년, 월, 일을 입력해주세요: "). split(".")
hour, minute, second = input("시, 분,초를 입력해주세요: "). split(":")

print(f"RE5의 개강일은 {year}년 {month}월 {day}일\
        시작 시간은 {hour}시 {minute}분 {second}초입니다.")

# input() 문자열만 가능하지만 숫자를 입력할 경우에는 int(input())을 사용한다.
# 하지만 정수에는 .split() 적용되지 않기 때문에 오류가 난다.
# 따라서 list()를 사용하여 list(input)...를 사용하거나 각각의 정수를 받아서 사용하도록 하나씩 코드를 작성해야 한다.


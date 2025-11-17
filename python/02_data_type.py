'''
# 자료형(Data type)
## 변수에 저장되는 데이터의 종류와 구조를 정의하는 것

# 정수형 (int, integer)
# 크기 제한이 없다
my_int1 = 100;
my_int2 = 10909090909090909090909090909090;
print(type(my_int1)) # <class 'int'>

# 실수형(float)
# 부동 소수점 방식
my_float = 100.0
print(type(my_float)) # <class 'float'>

# 문자열(str, string)
my_str1 = '' # 빈 문자열
my_str2 = " " # 공백 문자열
my_str3 = "안녕하세요"

# 문자열 여러줄로 만들기
multi_str = """ 
코딩을 하는 처음 배우는 파이썬 언어
"""

print(multi_str)
print(type(multi_str)) # <class 'str'>

# 따옴표 속에 따옴표 쓰기
print("'python'코딩언어") # 'python'코딩언어
print('"python"코딩언어') # "python"코딩언어
# print(''python'코딩언어') --> Error

# 불리언형, 논리형(참, 거짓 또는 1, 0) (bool, boolean)
# 참과 거짓을 표현하는 자료형

print(True)
print(False)
print(type(True)) # <class 'bool'>

# 형 변환(Type casting): 하나의 자료형을 다른 자료형으로 변환하는 것
# 명시적 형변환 vs 암시적 형변환

# 1. 정수로 변환: int()
# 1) 실수 -> 정수
# 2) 문자열로 표현된 정수 -> 정수
# 3) 논리형 -> 정수

# 가능한 경우
print(int(3.14)) # 3
print(int("100")) # 100
print(int(True)) # 1
print(int(False)) # 0
# 불가능한 경우
# print(int("3.14")) # 실수 문자형
# print(int("Hello")) # 문자열
# print(int("abc"))

# 2. 실수로 변환: float()

1) 정수 -> 실수
2) 문자열로 표현된 실수 -> 실수
3) 문자열로 표현된 정수 -> 실수
4) 논리형 -> 실수

# 가능한 경우
print(float(7))
print(float('3.14'))
print(float('10000'))
print(float(True), float(False))

# 불가능한 경우
# print(float("abc")) # 숫자가 아닌 문자열은 불가능하다.

# 3. 문자열로 변환: str()
# 4.논리형으로 변환: bool()
print(bool(1)) # True
print(bool(0)) # False

# 암시적 형변환
# 정수와 실수의 연산에서 자동으로 실행되는 연산
print(10 + 5.0) # 15.0

#-----------------------------------------
# 문자열 포맷팅 (f-string)
# 문자열 안에 변수를 쓸 수 있도록 해주는 기능

name = "Dongyun"
age = 26

print("내 이름은", name, "이고, 나이는", age, "입니다.")
print(f"내 이름은 {name}이고, 나이는 {age}입니다.")


movie, director, year, genre = "Now You See Me: Now You Don't", "Ruben Fleischer", 2025, "Crime/Thriller"
print(f"Title: {movie} Director: {director} Year: {year} Genre: {genre}")
'''

name, age, MBTI = "Dongyun", 26, "INTP"
print(f"안녕하세요.\n제 이름은 {name}이고,\n{age}살 입니다.\n제 MBTI는 {MBTI}에요.")

'''
print(f"""안녕하세요.
      제 이름은 {name}이고,
      {age}살 입니다.
      제 MBTI는 {MBTI}에요.""")
'''
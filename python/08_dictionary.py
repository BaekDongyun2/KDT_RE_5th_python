# 딕셔너리(dict): 하나의 키(key)와 값(value)을 쌍으로 묶어 데이터를 저장하는 자료형 <--걍 닉값대로 사전임
'''
주요특징
+ 키-값쌍(key-value pair) 구조
+ 키는 유일해야 함, 값은 중복 가능
순서보장
변경가능(mutable)

장점
+ 빠른 검색: 키를 통해 값을 매우 빠르게 찾을 수 있음(해시 기반)
+ 명확한 구조: 각 항목이 어떤의미를 가지는지 명확함(key로 의미부여 가능)
+ 확장성과 유연성: JSON과의 호환성이 뛰어나고, 다양한 자료구조 표현 가능
'''
'''
# dict 만들기
d1 = {} # 빈 dict 만들기
print(d1, type(d1))

person = {"name": "백동윤", "age": 26}
print(person)

# dict 함수로 생성
d2 = dict()
print(d2, type(d2))

# 키가 문자열인 경우
movie = dict(tittle = "interstella", director = "christopher nolan")
print(movie, movie["director"])

# 리스트나 튜플로 만들기
pairs = [("name", "dongyun"), ("age", 40), ("job", "dev")]
person = dict(pairs)
print(person)

# zip() 함수와 함께 사용
keys = ["title", "director", "year"]
values = ["paracite", "봉준호", "2019"]

movie = dict(zip(keys, values))
print(movie)

# 딕셔너리 데이터 접근
# + 딕셔너리에 값을 가져올 때는 키(key)를 사용하여 접근함
# + 대괄호를 사용한 방식 - 일반적인 접근
# + get() 매서드를 사용하는 방식 - 안전한 접근

# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야한다 
d1 = {(1, 2, 3): (1, 2, 3)} # 튜플 사용가능
d2 = {1 : 10}
print(d1, d2)
# d3= {[1, 2, 3] : "리스트 값을 키로"}
# print(d3) # TypeError: unhashable type: 'list'


# dict 데이터 조회
print(person["name"])
print(person["age"])
# print(person["city"]) # KeyError: 'city'

print(person.get("name"))
print(person.get("email")) # None (오류아님) -> default
print(person.get("email", "이메일이 존재하지 않습니다."))

# get 사용예제
user_data = {
    "username" : "Dongyun2",
    "email" : "bdy0010317@gmail.com",
    "password" : "1235234"
}

#key = input("조회할 정보를 입력하세요.(username, email, password): ")
#result = user_data.get(key, "존재하지 않는 데이터입니다.")
#print(result)


# 파이썬 딕셔너리에서 데이터의 추가와 수정은 동일한 문법을 사용함
# + 만약 해당 키가 존재하지 않으면 -> 새로운 항목이 추가
# + 이미 존재하는 키라면 -> 해당 키의 값이 수정

# 데이터 추가 및 수정

# 1) 기본적인 추가, 수정방법
user_data["phone"] = "010-1234-5678"
user_data["username"] = "Dongyun222222222"
print(user_data)

# 2) update 매서드 활용
user_data.update({"nickname" : "Dongyun2"})

# 키가 문자열인 경우
user_data.update(phone = "013-4564-2739")

# 다른 딕셔너리 추가
extra_data = {"city" : "seoul"}
user_data.update(extra_data)

print(user_data)

# 딕셔너리 데이터 삭제
del user_data["city"]
# del user_data["age"] # KeyError: 'age'

print(user_data)

# 키로 제거
nickname = user_data.pop("nickname")
print("pop >>", user_data, nickname, sep="///")

# 가장 마지막 요소 제거
phone = user_data.popitem()
print(user_data, phone, sep = "///")

# dict 비우기
user_data.clear()
print(user_data)

# dict 삭제하기
del user_data
# print(user_data) # NameError: name 'user_data' is not defined
'''

# 딕셔너리 메서드
user_data = {
    "username" : "Dongyun2",
    "email" : "bdy0010317@gmail.com",
    "password" : "1235234"
}

# keys: 모든 키를 반환
print("키", user_data.keys()) # dict_keys(['username', 'email', 'password'])
print("키", list(user_data.keys()))
# + dict_keys객체를 반환함(리스트처럼 보이지만 실제 리스트는 아니다.)
# + 리스트로 변환하고 싶다면 list()함수로 변환

# values: 모든 값을 반환
print("키", list(user_data.values()))
# + dict_values객체를 반환함 (리스트X)
# + 리스트로 변환하고 싶다면 list()함수로 변환

# items: 모든 키-값쌍을 반환
print("쌍", list(user_data.items()))
# + dict_items객체를 반환함 (리스트X)
# + 리스트로 변환하고 싶다면 list()함수로 변환


'''
# 실습1-1
user = dict()
user = {"username" : "skywalker", "email" : "sky@gmail.com", "level" : 5}

email_value = user["email"]
print(email_value)

user.update({"level" : 6})
print(user)


print(user.get("phone", "미입력"))

user.update({"nickname" : "sky"})

del user["email"]

signup_date = user.setdefault("signup_date", "2025-07-10")

print(signup_date)

# 실습1-2

students = dict()
students = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
students["David"] = 80
students.update({"Alice" : 88})
del students["Bob"]
print(students)
'''
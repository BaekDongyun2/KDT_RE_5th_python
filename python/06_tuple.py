# Tuple: 여러 개의 값을 하나의 변수에 저장할 수 있는 자료형
# 순서가 유지되며, 변경이 불가능(immutable)한 시퀀스 타입
# 불변성(immutable), 순서유지, 중복허용

# 단일 요소인 튜플을 만들 때는, 쉼표(,)를 꼭 붙여야 튜플로 인식한다.

# unpacking: 시퀀스에 저장된 여러 값을 여러 변수에 한 번에 나누어 저장하는 문법

'''
튜플
- 순서가 존재하는 여러 데이터의 모음
- 불변 (immutable) 자료형
- 중복이 허용됨
'''
'''
#--------튜플생성----------
my_tuple = (1, 2, 3, 4)
print(my_tuple) # 1, 2, 3, 4
print(type(my_tuple)) # <class 'tuple'>

my_tuple2 = (5, 6, 7, 8)
print(type(my_tuple2)) # <class 'tuple'>

# 단일 요소 튜플 생성
single_ele_tuple = (100,)

# 튜플 생성 함수로 생성
my_tuple2 = tuple()
print(my_tuple2)

my_tuple3 = tuple("codingon")
print(my_tuple3)

#--------언패킹--------
# 시퀀스에 저장된 여러 값을 여러 변수에 나눠 저장하는 것
# 튜플, 리스트, 문자열...
apple, banana, kiwi = ("apple", "banana", "kiwi")
print(apple, banana, kiwi)

#-----------------------------------

# 불변성(immutable)
# -객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
# my_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment
# 삭제
# del my_tuple[1] # TypeError: 'tuple' object doesn't support item deletion
# 튜플 자체는 삭제가 가능하지만 원소 삭제는 불가하다.
# del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined

# indexing, slicing --> 다른 시퀀스 자료형(문자열, 리스트)과 동일하게 사용가능함

# 튜플이 불변성을 가지는 이유
# 데이터 보호, 성능 최적화, 키(key)사용가능

# ---------튜플 수정-----------
my_tuple4 = (10, 20, 30)
new_tuple = (100,) + my_tuple4[1:]
print("원본 튜플", my_tuple4)
print("새로운 튜플", new_tuple)
'''
# step1
unknown = ("minji", 25, "Seoul")
user = ("eunji",) + unknown[1:]
restored_user = user
print("Restored User", restored_user)

# step2
name, age, city = restored_user
print(name, age, city)

# step 3
city = input("거주 지역을 입력하세요: ")
if city.lower() == "seoul": # 대소문자 구분없이 비교 가능
    print("서울 지역 보안 정책 적용 대상입니다.")
else :
    print("일반 지역 보안 정책 적용 대상입니다.")

# step 4
users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))
print(users.index("soojin"))

# step 5
sorted_users = sorted(users)
print("Customers Name", sorted_users)

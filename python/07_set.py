# set(집합): 중복을 허용하지 않고, 순서가 없는 컬렉션 자료형
'''
set(집합): 원소의 중복을 허용하지 않는 여러 데이터의 모음
-순서가 없는 컬렉션 자료형
'''
'''
# set 만들기
s1 = {1, 2, 3}
print(s1, type(s1))

s2 = {1, 1, 1, 11, 2, 2, 2, 2,2 ,22, 3, 3, 4, 5, 6, 754 ,23432, 4}
print(s2) # {1, 2, 3, 4, 5, 6, 23432, 11, 754, 22}

# s = {} --> 빈 중괄호{}는 dict로 해석됨
# 빈집합을 만드려면 반드시 set을 사용해야 함.

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict로 인식이 된다.
s3 = {}
print(type(s3)) # <class 'dict'>

# set 함수 생성
s4 = set()
print(s4, type(s4)) # set() <class 'set'>

# set함수의 활용: 원소의 중복 제거
my_list = [1, 1, 12, 3, 4, 3, 4, 5, 6, 4, 3, 354532 ]
s5 = set(my_list)
print(s5) # {1, 3, 4, 5, 6, 354532, 12}

# 인덱싱, 슬라이싱 사용불가
# s1[1] # TypeError: 'set' object is not subscriptable

# set의 기본 문법
s = {'apple', 'banana', 'cherry'}
for fruit in s:
    print(fruit)
# 순서가 없지만 for 등과 같은 반복문 가능
# 출력 순서는 예측 불가(내부적으로 해시값 기반 저장)

ss = {1, 2, (3, 4)}
# ss = {[1, 2]} # TypeError: unhashable type: 'list'
# set의 원소는 변경 불가능한(immutable) 객체여야 함
# 리스트나 딕셔너리처럼 mutable한 객체는 원소로 쓸 수 없다.

# 자료형의 제한
# - 가변(mutable) 자료형은 원소로 사용할 수 없다.
s1 = {1, 2, 4, [3, 5, 6]}

# set 연산
# 집합의 연산: 합집합, 교집합, 차집합, 대칭차집합
a = {1, 2, 3}
b = {3, 4, 5}

# 합집합(| 또는 .union)
s_union1 = a | b
s_union2 = a.union(b)
print("합집합1", s_union1)
print("합집합2", s_union2)

# 교집합(& 또는 .intersection)
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합1", s_inter1)
print("교집합2", s_inter2)

# 차집합(- 또는 difference) <-- 순서가 바뀌면 결과가 바뀜
s_diff1 = a - b
s_diff2 = a.difference(b)
print("차집합1", s_diff1)
print("차집합2", s_diff2)

# 대칭 차집합(^ 또는 symmetric_difference)
s_sym1 = a ^ b
s_sym2 = a.symmetric_difference(b)
print("대칭차집합1", s_sym1)
print("대칭차집합2", s_sym2)

submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
students = set(submissions)
print(len(students))
print(students)

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
set1 = user1 & user2
set2 = user1 ^ user2
set3 = user1 | user2
print("공통 관심 장르: ", set1)
print("서로 다른 장르: ", set2)
print("전체 장르: ", set3)
    
# set 메서드
s1 = {1, 2, 3}

# 원소 추가
s1.add(4)
print("원소 추가", s1)

# 여러 원소 추가
s1.update({5, 6, 7})
print("여러 원소 추가", s1)

# 원소 제거
s1.remove(4)
print("원소 제거1", s1)
# s1.remove(100) # KeyError: 100 <-- 존재하지 않는 원소 삭제 시도시 에러발생

s1.discard(100) # 해당 요소 제거(없으면 무시함)
s1.discard(6)
print("원소 제거2", s1)

deleted = s1.pop() # 임의의 요소 제거 후 반환
print("원소 제거3", s1, deleted)

# 부분 집합(subset) 관련 메서드
a = {10, 20, 30, 40, 50} # 상위집합
b = {20, 30, 40} # 부분집합
c = {10, 200, 300, 400, 500}

# 부분집합 여부 판단
print(b.issubset(a)) # True
print(a.issubset(b)) # False

# 상위집합 여부 판다
print(a.issuperset(b)) # True
print(b.issuperset(a)) # False

# 공통 원소 유무 확인
print(a.isdisjoint(b)) # False <-- 공통원소가 있으면 False 출력!
print(a.isdisjoint(c)) # False
print(b.isdisjoint(c)) # True <-- 공통원소가 없어서!
'''

my_certificates= {'SQL', 'Python', 'Linux'}
job_required= {'SQL', 'Python'}
set4 = my_certificates & job_required
print("지원 자격 충족 여부: ", my_certificates.issuperset(job_required))


''' 
list: 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스로 각 항목에 접근할 수 있으며, 요소의 추가/삭제/수정이 자유로움
- index: 각 값에 부여된 순서(0부터 시작)
- 가변 자료형(mutable): 원소의 추가/수정/삭제 가능
- 순서 유지, 중복 허용, 다양한 자료형 저장 가능, 가변객체(Mutable)
'''
'''
# list 만들기
list1 = [] # 빈 리스트
list2 = ["안녕하세요", "반갑습니다"] # 문자열이 들어간 리스트
list3 = [10, "gold", 3.14, [1, 2, 3, 5]]

print(list1, list2, list3)

list4 = list() # 리스트 함수를 이용해서 빈 리스트를 만듦
list5 = list("CODINGON") # 문자열의 각 문자를 하나씩 리스트화 됨
print(list4, list5)

# indexing: 시퀀스 자료형에서 특정 위치(index)의 값을 조회하는 것
# - 인덱스는 0부터 시작함
# - 음수 인덱스를 사용하면 뒤에서부터 접근 가능

# =====================
# 인덱싱과 슬라이싱
# =====================

my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # 1
print(my_list[-1]) # 5

my_list[3] = -1
print(my_list) # [1, 2, 3, -1, 5]

number = input("네 자릿수 정수를 입력하세요: ")
천 = number[0]
백 = number[1]
십 = number[2]
일 = number[3]
print(천, 백, 십, 일)

# ----------------------------
# 슬라이싱
# ----------------------------

# slicing: 시퀀스에서 특정 구간을 잘라내어 부분적으로 추출하는 방법
# - 원본은 변경되지 않으며, 새로운 시퀀스를 생성함

my_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_numbers[1:4]) # 1 --> 시작 인덱스(포함), 4 --> 끝 인덱스(불포함)
print(my_numbers[3:]) # 40 ~ 100
print(my_numbers[:4])
print(my_numbers[:]) # 전체 복사
print(my_numbers[::-1]) # 문자열 뒤집기
# [start:end:step] --> step에 -1을 사용해서 전체 복사 = 리스트를 반전해서 복사
my_numbers[2:4] = [300, 400]
print(my_numbers)
my_numbers[1:5] = [9, 4, 3]
print(my_numbers)

nums1 = [10, 20, 30, 40, 50]
print(nums1[0], nums1[4])

nums2 = [100, 200, 300, 400, 500, 600, 700]
print(nums2[2:5])

nums3 = [1, 2, 3 ,4 ,5]
num1 = nums3[0] * 2
num2 = nums3[1] * 2
num3 = nums3[2] * 2
num4 = nums3[3] * 2
num5 = nums3[4] * 2
nums4 = [num1, num2, num3, num4, num5]
print(nums4[:])

items = ["a", "b", "c", "d", "e"]
print(items[::-1])

data = ["zero", "one", "two", "three", "four", "five"]
print(data[::2])

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print(movies[:])

subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
print(subjects[3::2])


datax = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data1 = datax[0:3] # datax[0:3:-1]도 가능
data2 = datax[3:6] # datax[3:6:-1]도 가능
data3 = datax[6:8] # datax[6:8:-1]도 가능
print(data1[::-1], data2[::-1], data3[::-1]) # print(data1[:], data2[:], data3[:]) <-- datax[x:y:-1]로 바꿨을 때


# del: 파이썬의 내장 키워드로, 개게?를 삭제(delete)하는데 사용됨
# 인덱싱, 슬라이싱 주의사항
my_list = [1, 2, 3, 4]
my_list[5] # IndexError: list index out of range

my_list = [1, 2, 3, 4, 5]
#print(my_list[4:1:2]) # [] # IndexError: list index out of range
print(my_list[1:3:-1]) #[]

# ========================
# 리스트 연산 - del
# ========================
my_list = [10, 20, 30, 40, 50]
del my_list[2] # 특정 요소 삭제
print(my_list)
del my_list[1:3] # 슬라이스 범위 공개
print(my_list)
del my_list # 리스트 삭제
print(my_list) # Exception has occurred: NameError

#===========================
# 리스트 연결: +
#===========================
list1 = ["가", "나", "다"]
list2 = ["라", "마", "바"]
new_list = list1 + list2
print(list1, list2, new_list, sep=" / ")

# 리스트 반복: *
medal = ["금", "은", "동"]
new_list = medal * 3
print(medal, new_list, sep = " / ")

# 포함 여부(in, not in)
fruits = ["토마토", "사과", "포도", "수박", "바나나"]
print("포도" in fruits)
print("참외" not in fruits)

fruitss = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruitss[1:4]
print(fruitss)

letters = ["A", "B"]
new_letter_list = letters * 3
del new_letter_list [2]
print(new_letter_list)

# len(): 길이(요소 개수)반환 --> 시퀀스나 컬렉션 자료형의 요소 개수를 반환
# append(x): 리스트 끝에 요소 추가 --> 리스트 마지막에 하나의 요소를 추가함
# extend(iterable): 리스트 끝에 여러 요소 추가 --> 다른 리스트나 이터러블의 모든 요소를 추가함
# insert(index, x): 원하는 위치에 요소 삽입 --> 지정한 인덱스에 요소를 삽입함
# remove(x): 특정 값을 찾아 삭제 --> 가장 처음 발견된 해당 값(x)을 삭제함
# pop(index): 인덱스 요소를 꺼내고 삭제 --> 인덱스를 지정하면 해당하는 인덱스의 요소를 삭제하고 반환함, 인덱스를 지정하지 않으면 마지막 요소를 삭제하고 반환함
# sort(), sorted() --> list.sort(): 원본 리스트를 정렬, sorted(list): 정렬된 새로운 리스트 반환, 오름차순이 기본이며, reverse = True 옵션을 주면 내림차순으로 정렬 됨

# ==================
# 리스트 주요 메서드
# ==================

# 길이
numbers = [1, 2, 3, 4, 5]
print("1. len()", len(numbers), len("Codingon"))

# 삽입
numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers)

numbers.insert(2, 2.5)
numbers.insert(4, 3.5)
print("3. insert()", numbers)

numbers.extend([9, 10])
print("4. extend()", numbers)

# 삭제
numbers.append(2.5)
numbers.remove(2.5)
print("5. remove()", numbers)

a = numbers.pop(4)
print("6. pop() 삭제한 요소", a)
print(numbers)
b = numbers.pop()
print("6. pop() 삭제한 요소", b)
print(numbers)

# 정렬
numbers1 = [3, 2, 1, 4]
numbers1.sort()
print("7-1. sort()", numbers1)
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1)

numbers2 =[50, 52, 53, 51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse = True)
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc)

# 뒤집기
my_numbers = [100, 101, 104, 103, 102]
my_numbers.reverse()
print("8-1. reverse()", my_numbers) # [102, 103, 104, 101, 100]

my_numbers2 = list(reversed(my_numbers))
# my_numbers = reversed(my_numbers) --> <list_reverseiterator object at 0x000001BF00CF7370>
print("8-2. reversed()", my_numbers2, my_numbers)

# count(x): 값의 개수 세기
# max(), min(): 최대/ 최소값 찾기
# sum(): 요소들의 합 구하기

# count, min, max, sum
numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
print("9. count()", numbers.count(2))
print("10. min/max()", min(numbers), max(numbers))
print("11. sum", sum(numbers))
'''

passengers = ["철수", "영희"]
passengers.extend(["민수", "지훈"]) 
del passengers[1]
passengers.insert(0, "수진")
del passengers[2]
now_passengers = list(reversed(passengers))
print("현재 승객들의 좌석 순서", now_passengers)

card_game_list = [5, 3, 7]
card_game_list.extend([4, 9])
print("mininum", min(card_game_list), "maximum", max(card_game_list))
print(sum(card_game_list))
card_game_list.sort()
del card_game_list[4]
print("최종 리스트", card_game_list)


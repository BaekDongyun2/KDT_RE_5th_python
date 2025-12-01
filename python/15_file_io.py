# 파일 입출력
# 프로그램이 저장장치(ex: 하드디스크)에 저장된 파일을 읽어오거나, 반대로 데이터를 파일에 저장하는 작업
# + 입력(input): 파일로부터 데이터를 읽어오는 것
# + 출력(output): 데이터를 파일로 저장(기록)하는 것

# 입, 출력 스트림
# 스트림: 자료흐름이 물의 흐름과 같다는 뜻
# + 입력 스트림 - 동영상을 재생하기 위해 동영상 파일에서 자료를 읽을 때 사용함
# + 출력 스트림 - 사용자가 쓴 글을 파일에 저장할 때는 출력 스트림 사용함.

# 파일 입출력의 필요성
# + 프로그램 실행 중에 메모리에 저장된 데이터는 프로그램이 종료되면 사라짐
# + 데이터를 프로그램이 종료된 후에도 계속해서 사용하려면 파일에 저장하고 필요할 때 파일을 읽어서 데이터를 사용할 수 있음

# 파일 열기 open()
# open() 함수: 파일을 열어 파일 객체(file, object)를 반환하는 내장하는 함수
# 파일 객체: open()으로 반환되는 객체로, 이 객체를 통해 파일의 내용을 읽거나 쓰는 메서드(read, write 등)를 사용할 수 있음


# 파일 열기와 닫기
# 파일 열기: open()
# open("파일 경로", mode = "r", encoding = "원하는 인코딩 - utf8")
# open으로 파일을 읽으면 '파일 객체'를 반환

# f = open("example.txt", "w", encoding = "utf-8")

# f.write("파이썬 파일 입출력 예제\n")
# f.write("파이썬 공부!\n그까짓거 해보죠\n")

# # 파일 닫기: close()
# # 열린 파일을 닫아 시스템 자원을 해제함
# f.close

# # 파일 읽기
# # read(): 전체 내용을 한 번에 읽기
# f = open("example.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# # readline(): 한 줄씩 순차적으로 읽기
# f = open("example.txt", "r", encoding="utf-8")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

# print("첫 번째 줄: ", line1.strip())
# print("두 번째 줄: ", line2)
# f.close()

# # for문으로 읽기
# f = open("example.txt", "r", encoding="utf-8") # f.close가 없으면 이 문장을 그대로 사용해도 된다.
# for line in f:
#     print(line.strip())
# f.close()

# # readlines(): 모든 줄을 한 번에 리스트로 읽기
# f = open("example.txt", "r", encoding="utf-8")
# contents = f.readlines()
# print(contents) # print(contents[]) 특정 줄만 출력할 때는 리스트로 변환된 line의 인덱스를 넣으면 출력된다.
# f.close()

# # 파일 읽기 메서드
# # tell(): 현재 읽고 있는 위치(바이트)를 반환
# f = open("example.txt", "r", encoding="utf-8")
# print("처음 위치: ", f.tell())
# f.read(5)
# print("5바이트 읽은 후 위치: ", f.tell())
# f.close

# # seek(): 파일 포인터 위치를 이동
# f = open("example.txt", "r", encoding="utf-8")
# print(f.read(10)) # 처음부터 10글자 읽기
# f.seek(0) # 포인터를 다시 처음으로 이동
# print(f.read())
# f.close()


# # a 모드: 추가 쓰기
# # + 기존 파일 끝에 새로운 내용을 추가
# # + 파일이 없으면 새로 생성
# f = open("example.txt", "a", encoding="utf-8")
# f.write("\n추가한 내용입니다.")
# f.close()

# # w 모드: 덮어 쓰기
# # + 파일이 존재하면 기존 내용을 모두 삭제하고 새로 작성
# # + 파일이 없으면 새로 생성

# # with 문: 파일 작업 시 컨텍스트 관리자를 사용해 블록이 끝나면 자동으로 close()를 호출해주는 안전한 파일 처리 구문
# with open("with_example.txt", "w", encoding = "utf-8") as f1:
#     f1.write("with문으로 작성한 파일이에요\n")
#     f1.write("파일 입출력 완료")

# # 예제 1. 파일에서 랜덤 추출
# with open("words.txt", "w", encoding="utf-8") as f1: # 쓰기모드
#     words = [
#       "apple", "banana", "orange", "grape", "lemon",
#       "peach", "melon", "cherry", "plum", "pear",
#       "school", "friend", "family", "flower", "garden",
#       "window", "bottle", "pencil", "summer", "winter",
#       "happy", "future", "travel", "animal", "market",
#       "doctor", "planet", "energy", "nature", "memory"
#   ]
#     for i in words:
#         f1.write(i + "\n")

# import random

# with open("word.txt", "r", encoding="utf-8") as f1: # 읽기모드
#     data = f1.readlines()
#     for i in range(5):
#         word = random.choice(data).strip() # strip(): 공백제거
#         print(word)


# # 예제 2. 입력 받아 파일 쓰기
# with open("with_example.txt", "a", encoding="utf-8") as f1:
#     while True:
#         text = input("저장할 내용을 입력해주세요(종료: z)")
#         if text == "Z" or text == "z":
#             break
#         f1.write(text + "\n")

# # 실습 1. 회원 명부 작성하기
# # with open("member.txt", "w", encoding="utf-8") as f2:
# #     mem_count = 0
# #     while mem_count < 3:
# #         mem_info = input("회원님의 이름과 비밀번호를 입력하세요: ")
# #         mem_count += 1
# #         f2.write(mem_info + "\n")

# # with open("member.txt", "r", encoding="utf-8") as f2:
# #     members = f2.readlines()
# #     for i in members:
# #         print(i)

# # 실습 2, 3. 회원 명부를 이용한 로그인 기능/ 로그인 성공 시 전화번호 저장하기
# # 코드 다 뜯어고쳐야겠슨...
# with open("member.txt", "r", encoding="utf-8") as f3:
#     mem_data = f3.readlines()
#     member_count = 0
#     while member_count < 3:
#         id = input("이름을 입력하세요: ")
#         pw = input("비밀번호를 입력하세요: ")
        
#         for k in mem_data:
#             k = k.strip()
#             id_str, pw_str = k.split(", ")
    
#             if id == id_str and pw == pw_str:
#                 print("로그인 성공!")
#                 member_count += 1
                
#                 ph = input("전화번호를 입력하세요. ex) 010-0000-0000: ")

#                 # 기존 파일 읽기
                
#                 with open("member_tel.txt", "a", encoding="utf-8") as f5:
#                 #     tel = f5.readlines() 
#                 # new_tel = []
#                 # found = False
#                 # for j in tel:    
#                 # ph = input("전화번호를 입력하세요. ex) 010-0000-0000: ")
#                 #     f4.write(f"{id_str} / {ph}\n")
                    
#                     with open("member_tel.txt", "r", encoding="utf-8") as f5:
#                         tel = f5.readlines()
                        
#                         for j in tel:
#                             name, phone = j.strip().split(" / ")
#                             saved_name = name # 다른 변수로 name 문자열을 저장
#                             if name == id:
#                                 with open("member_tel.txt", "w", encoding="utf-8") as f5:
#                                     f5.write(f"{saved_name} / {ph}\n") # 전화번호만 바꾸고 구조를 유지
#                     break
            
#         else:
#             print("로그인 실패")

#         if member_count == 3:
#             print("모든 회원 로그인 성공")
#             break

# # 실습 1

# import os
# # ------------------------------------------
# # 1. 회원 3명 입력하여 파일에 저장
# # ------------------------------------------
# if os.path.exists("member.txt"): <-- 경로에 member.txt가 존재하는지 여부 확인
#     print("member.txt가 이미 존재합니다. 회원 등록을 건너뜁니다.\n")
# else: <-- member.txt의 존재가 확인 되었을 때, 회원 등록
#     with open("member.txt", "w", encoding="utf-8") as f:
#         for i in range(3):
#             name = input(f"{i+1}번째 회원의 이름: ")
#             password = input(f"{i+1}번째 회원의 비밀번호: ")
#             f.write(f"{name},{password}\n")
        
# print("\n[회원 명부 저장 완료]\n")


# # ------------------------------------------
# # 2. 로그인 과정
# # ------------------------------------------
# input_name = input("로그인 - 이름을 입력하세요: ")
# input_password = input("로그인 - 비밀번호를 입력하세요: ")

# login = False <-- login을 우선 False로 설정
# with open("member.txt", "r", encoding="utf-8") as f: <-- member.txt를 읽어오기
#     for line in f:
#         name, password = line.strip().split(",") <-- member.txt의 모든 줄의 정보를 ", "으로 나눠서 다시 name과 password변수에 저장
#         if input_name == name and input_password == password:
#             login = True
#             break
        

# # ------------------------------------------
# # 3. 로그인 성공 시 전화번호 등록/수정
# # ------------------------------------------
# if login: <-- 로그인 성공
#     print("\n로그인 성공!")
    
#     # 기존 전화번호 데이터 로드
#     phone_data = {} <-- 전화번호 데이터를 빈 딕셔너리에 넣겠다.
    
#     if os.path.exists("member_tel.txt"): <-- 파일 경로에 member_tel.txt가 있는지 여부 확인
#         with open("member_tel.txt", "r", encoding="utf-8") as f:
#             for line in f:
#                 name, phone = line.strip().split(",") <-- member_tel.txt에 존재하는 전화번호 데이터를 split으로 나눠서 name과 phone 변수에 저장한다.
#                 phone_data[name] = phone <-- 이런 형식으로 딕셔너리의 key, value값으로 지정한다고.
                
#     # 전화번호 입력
#     new_phone = input(f"{input_name}님의 전화번호를 입력하세요: ") <-- member_tel.txt에 전화번호가 이미 존재하니까 다시 다른 변수로 전화번호를 받아와서 덮어쓰겠다는 거지.
    
#     # 추가 또는 수정
#     if input_name in phone_data: <-- phone_data 딕셔너리에 input_name key값이 존재할 때 수정~
#         print("기존 전화번호 수정")
#     else:
#         print("전화번호 새로 추가")
    
#     phone_data[input_name] = new_phone
    
#     # 전화번호 파일 갱신
#     with open("member_tel.txt", "w", encoding="utf-8") as f:
#         for name, phone in phone_data.items():
#             f.write(f"{name},{phone}\n")
            
#     print("전화번호 저장 완료!")
# else:
#     print("\n로그인 실패!")


# 바이너리 파일 읽고 쓰기
# wb모드: 바이너리 쓰기 모드 -> 문자열은 encode()로 변환 후 작성
# rb모드: 바이너리 읽기 모드 -> 바이트 데이터를 decode()로 다시 문자열 변환

import os

print(os.getcwd()) # 상대경로

# 바이너리 파일 읽기
with open('./python/images/애옹이.webp', 'rb') as f: # .의 의미: 현재 경로, os.getcwd()를 . 대신에 넣으면 절대경로가 된다.
    img = f.read
    

# 바이너리 파일 쓰기
with open("./python/images/애옹이_copy.webp", "wb") as f:
    f.write(img)
    print(img)


# pickle 모듈
# + 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있는 모듈
# + 이때 객체는 리스트나 딕셔너리 등의 자료구조도 포함한다.

# pickle.dump: 쓰기
# pickle.load: 읽기

import pickle

# 리스트, 딕셔너리 파일 저장
with open('pickle.txt', 'wb') as f:
    li = ['dog', 'cat']
    dic = {1: 'dog', 2: 'cat'}

    pickle.dump(li, f)
    pickle.dump(dic, f)

# 읽기
with open('pickle.txt', 'rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)

    print(li, dic)
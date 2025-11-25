# 모듈
# 여러 기능들이 뭉쳐진 하나의 .py 파일
# 함수, 변수, 클래스 등을 담아 코드의 재사용성과 관리 효율을 높임

# 모듈을 사용하는 이유
# + 코드의 분할 및 재사용
# + 유지보수 용이성
# + 네임스페이스 분리로 충돌 방지

# 모듈(module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것

# 모듈 불러오기(1) <-- 모듈 전체 불러오기
import hello

hello.greeting("Baek")

# 모듈 불러오기(2) <-- 특정 함수만 불러오기
from hello import greeting

greeting("Dongyun")

# 모듈 불러오기(3) <-- 모든 함수/변수 불러오기
from hello import *
introduce("Dongyun2", "26")

# 모듈 불러오기(4) <-- 모듈에 별칭을 사용
import hello as h
h.greeting("dingdong")

# 실습1. 계산기 모듈 만들어보기

import my_package.calc as calc
calc.add(100, 28)

from my_package.calc import subtract
subtract(555, 55)

import my_package.calc as m
m.multiply(77, 847821)

import my_package.calc as calc
calc.divide(123876493296178326498, 0)

import my_package.calc as n
n.divide(78346, 24)

# 패키지
# 어러 모듈(.py파일)을 폴더 (디렉터리) 단위로 묶은 것
# + 대규모 프로젝트, 라이브러리 제작 시 사용

# 패키지
# 모듈의 묶음
# 모듈을 폴더 단위로 묶어 놓은 것

# 패키지에서 모듈 불러오기(1)

from my_package import calc as c
c.add(10, 20)

# 패키지에서 모듈 불러오기(2)
from my_package.calc import add
add(10, 20)

# 파이썬 표준 라이브러리
# math 모듈: 수학적 연산에 사용되는 모듈

import math as m

# 1. 올림/내림
# ceil: 올림, 소수점 지정x
m.ceil(3.14)

# floor: 내림, 소수점 지정x
m.floor(3.14)

# round: 반올림 - 내장함수
round(3.141592, 24)

# 2. 제곱, 제곱근
# pow(x, y): 제곱 - x ^ y
m.pow(2, 3)

# sqrt(x): 제곱근 반환
m.sqrt(16)

# 3. 상수
# pi: 원주율
print(m.pi)

# 4. 수학계산 편의 기능
print(m.factorial(3))
# 최대 공약수
print(m.gcd(12, 20))
# 최소 공배수
print(m.lcm(12, 20))

# 실습 2-1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기
import math as a

x1, y1, x2, y2 = map(int, input("변수값 입력(x1, y1, x2, y2) : ").split(", "))

distance = a.sqrt(a.pow(int(x2-x1), 2) + a.pow(int(y2-y1), 2))
print(distance)

# 실습 2-2. 상품 나누기: 최소 공배수와 최대 공약수
import math as a

students = 18
teachers = 24

# 최대 공약수
print(a.gcd(students, teachers))
# 최소 공배수
print(a.lcm(students, teachers))
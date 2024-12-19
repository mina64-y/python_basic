# 코드 주석 처리 [Ctrl + /]
# 콘솔 창에 괄호 안 텍스트(문자열)을 출력 하는 명령어
print("Hello world!!")
print("파이썬 배우기😍😊😂")

# 변수(Variable) 선언
# 변수란 값이 바뀔 수 있는 저장소를 의미
# 프로그램밍 언어에서 등호(=)는
# 등호 오른쪽의 값을 외쪽에 저장해라는 의미
mirae = 10000

# 변수에 저장된 값을 확인
print("mirae") # mirae 출력
print(mirae)   # 10000 출력
fusion = 5000
print(fusion)
# 텍스트(문자열)을 변수에 저장
mina = "미나"
print(mina)

# mirae를 15000 담기
mirae = 15000
print(mirae)

# navi 변수가 선언되기 전에 사용할 수 없음
# print(navi)
# navi = "네비"

# 실행 단축키 = Shift + F10

# 변수의 타입(Type)
a = 10
print(a)

# 변수의 타입 확인
# type() 괄호 안에 변수를 넣으면 해당 변수의 타입을 리턴
type(a)

# 숫자는 소수점이 없는 타입과 소수점이 있는 타입, 두개로 나뉜다.
# 정수(Interger)는 소수점이 없는 숫자를 의미
print(type(a))     # <class 'int'>

b = 3.14
print(b)

# 변수 b의 타입을 콘솔창에 출력하기
# 소수는 영어로 float
print(type(b))     #<class 'float'>

# 변수 c에 문자열 "몽키"를 담고,
# 변수 c의 타입을 콘솔창에 출력하기

c = "몽키"

# 문자열(String)은 '문자들'을 의미
print(type(c))     # <class 'str'>

# 불리언(boolean) 타입
# 참 / 거짓, Ture/False 을 나타내는 값
d = True
print(type(d))    #<class 'bool'>

# 개발을 할 때 혼동하기 쉬운 변수 타입
# 주민번호 앞자리 961028
e = 961028
print(type(e))
print(e)

# 네임테그(명칭)와 같이 사용하는 숫자값은 문자열 타입으로 사용
# 주민번호 앞자리 000320
# f = 030320     > print(f)  >  320로 출력됨
f = "030320"

#해당 숫자를 이용해서 사칙연산을 할 것이 아니라면 문자열 타입으로 사용

#생년만 문자열로 확보한 경우
year = "1993"

# 자동으로 나이 계산을 해야하는 경우
# 문자열 타입과 숫자 타입은 연산을 할 수 없음
# 타입을 변환한 후 연산을 수행한다
# str 타입의 year를 int 타입으로 변환
age = 2024 - int(year)

# 실행순서
# age = 2024 - int(year)
# age = 2024 - int("1993")  >  year이 "1993"로 변환
# age = 2024 - 1993         >  int("1993")이 1993로 변환
# age = 31                  >  결과값 출력

print(age)

# str -> int 타입 변환이 되네?
# 그럼 이것도 될까?
g = "문자열"
# 오로지 숫자로만 이루어진 문자열만 int 타입으로 변환 가능
# h = int(g)
# print(h)       > 오류

# 사칙연산 (+, -, *, /)
a = 10
b = 3

#  변수 a의 값과 변수 b의 값을 더한 뒤 변수 c에 저장(담다, 할당한다)
c = a+b

# 실행순서
# c = a + b
# c = 10 + b
# c = 10 + 3
# c = 13

print(c)

d= a - b
# 실행순서
# d = a - b
# d = 10 - b
# d = 10 - 3
# d = 7

print(d)
# print(d) 와 print(a - b)의 값이 같다.
# 변수에 꼭 담을 필요는 없다.
print(a-b)

print(a*b)     # 30
print(a/b)     # 3.3333333333333335

# 나머지 연산자 (%)
# 10을 3으로 나누면 나머지는? 1
print(a % b)

# 3을 10으로 나누면 나머지는? 3
print(3 % 10)

# 숫자형 문자열 -> int 변환
# int -> str 변환?

# 문자열 타입 + 문자열 타입
# 두 문자열이 합쳐 진다.

apple = "사과"
banana = "바나나"
# 기존 코드와 이름 충돌을 피하는 방법 (변수 앞에 v_ 붙이기, 다른 이름으로 바꾸기 등)
v_sum = apple + banana
print(v_sum)     # 사과바나나

price = 3000
# 사과3000 작성해보기

# v_sum = apple + price
# print(v_sum)    # 에러

# str + int 시 에러 발생
# int -> str 변환 이용
# str + str

v_sum = apple + str(price)

# 실행 순서
# v_sum = apple + str(price) # 라인 복사 [Ctrl + SLt + 방향키 아래]
# v_sum = "사과" + str(price)
# v_sum = "사과" + str(3000)
# v_sum = "사과" + 3000
# v_sum = "사과3000"

print(v_sum)    #사과3000

# 단축키 -> 편집기 마다 단축 키가 다르다. -> 단축키 불러 오기 가능.
# 단축키 불러 오기 세팅 방법 -> 메뉴 -> settings -> plugin -> Eclipce 검색 -> 설치 -> keymap에서 Eclipce으로 설정

# 자주 사용 하는 단축키(Eclipce 단축키)

# 라인 복사 [Ctrl + SLt + 방향키 아래]
# 라인 삭제 [Ctrl + D]
# 실행 취소 [Ctrl + Z]
# 실행 취소 되돌리기 [Ctrl + Y]

# "사과 : 3000"가 되도록 연산하기
v_sum = apple + ": "+str(price)
print(v_sum)

# 변수 값을 출력할 때, 변수 명도 같이 출력 되면 콘솔창에서 확인 용이
money = 13000
print("money: "+ str(money))
print("money:",money) # 출력될 때 붙어서 출력됨

# 변수 값에 사칙연산 하기
# 용돈을 받아서 money에 값 추가하기(+30000)
money = money+30000
print(money)

money = money * 2
print(money)

# 대입 연산자 방법
# money에 14000을 더해라
money += 14000
print(money)

# money 를 5로 나누기
# money /= 5  와 money = money / 5 가 같다
money /= 5
print(money)
money = money / 5
print(money)

# 반복문

# 콘솔창에 Hello를 10번 출력
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# 반복문을 이용해서 Hello를 10번 출력
for i in range(0, 10):
    print("Hello")

# range(0,10) 는 배열 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 와 같다고 생각
print(range(0, 10))  # range(0, 10)으로 출력
print(list(range(0, 10)))  # list를 넣어야 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]로 출력

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("Hello")

# 콘솔창에 1부터 10까지 출력
# 반복문을 이용하는 가장 큰 이유 -> 중복코드 합치기

for i in range(1, 11):
    print(i)

numArray = [2, 5, 3, 4]
for i in numArray:  # 일반 배열도 in 옆에 사용 가능
    print(i)

stuArray = ["김호빵", "이찐빵", "박꿀빵"]
for i in stuArray:
    print(i)

numArray = [2, 5, 3, 4]
# numArray의 모든 값에 3을 곱하기
print(numArray * 3)

# 배열 내 값 수정
print(numArray)  # [2, 5, 3, 4]
print(numArray[0])  # 2
print(numArray[0] * 3)  # 6

numArray[0] = numArray[0] * 3
print(numArray[0])  # 6

numArray[1] = numArray[1] * 3
print(numArray)

numArray[2] *= 3
print(numArray)

numArray = [2, 5, 3, 4]
print(numArray)
# for문으로 바꿔보기
numArray[0] *= 3
numArray[1] *= 3
numArray[2] *= 3
numArray[3] *= 3
print(numArray)

numArray = [2, 5, 3, 4, 8, 9]

# i가 0,1,2,3 이 되도록 하는 for문
for i in range(0, len(numArray)):
    numArray[i] *= 3

print(numArray)

# 다른 사람이 만든 배열 라이브러리 numpy 라이브러리 사용
# munpy 라이브러리 불러오기
import numpy as np  # as는 alias(별칭)의 약자

# 메뉴 -> settings -> project:python project-> python inter

numArray = [2, 5, 3, 4]
npArray = np.array([2, 5, 3, 4])

print(numArray)  # <class 'list'>
print(npArray)  # <class 'numpy.ndarray'>

print(type(numArray))
print(type(npArray))

print(npArray * 3)
print(npArray)

npArray = npArray * 3
print(npArray)

npArray *= 3
print(npArray)

# 1부터 10까지 다 더하면?
# n(n+1)/2
# i가 1부터 100이 되도록 for문 만들기
sum = 0
for i in range(1, 101):
    sum += i

print(sum)  # 5050

# 20부터 40까지 다 더하면?
sum = 0
for i in range(20, 41):
    sum += i

print(sum)  # 630

# 5 팩토리얼 값은? 5! -> 5 * 4 * 3 * 2 * 1
# 10! -> 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

mul = 1
for i in range(1, 6):
    mul *= i
print(mul)

mul = 1
for i in range(1, 11):
    mul *= i
print(mul)

# range로 거꾸로 배열 생성
for i in range(10, 0, -1):  # 10부터 0까지 가는 데 -1씩 한다.
    print(i)

# 1부터 30까지 숫자 중 홀수만 출력
# 1. i가 1부터 30이 되도록 for문 생성
# 2. i가 1~30이 되는 데, i가 홀수인지 체크(조건 체크 -> 조건문 사용)
for i in range(1, 31):
    if i % 2 == 1:
        print(i)

# 30부터 60까지 숫자 중 짝수만 다 더하면?
sum = 0
for i in range(30, 61):  # i가 30부터 60이 되도록 for문 생성
    if i % 2 == 0:  # i가 짝수인지 확인
        sum += i  # 값 더하기

print(sum)  # 720

# range의 범위 조정
sum = 0
for i in range(30, 61, 2):  # 30부터 61까지 가는 데 2씩 증가
    sum += i  # [30, 32, 34, 36, ....., 60]

print(sum)

nameArray = ["김호빵", "이찐빵", "박꿀빵", "김식빵", "김붕어빵"]

# 김씨 성을 가진 사람이 몇 명인지 세어 보기
sum = 0
for i in nameArray:  # i는 "김호빵", "이찐빵", "박꿀빵", ...
    if i[0] == "김":  # i의 첫번째 글자만 꺼내기 # 꺼낸 첫번째 글자가 "김"인지 조건 체크
        sum += 1  # 조건이 Ture면 sum에 1을 더하기

print(sum)

# 콘솔창에
# *
# **
# ***
# ****
# *****
# 와 같이 출력되도록 반복문을 작성하기

# 빈 문자열(empty) 선언
star = ""
# 5번 반복하는 for문 선언

print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(0, 5)))  # [0, 1, 2, 3, 4]
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 5):
    star = star + "*"
    print(star)  # for문에 반복될 때 마다 star에 "*"를 추가한 후 출력

# 콘솔창에
# *****
# ****
# ***
# **
# *
# 와 같이 출력되도록 반복문을 작성하기

# 5번 반복하는 for문 생성
# for문이 반복될 때마다 star의 길이를 한칸씩 줄이기
# star = star[0:5]
# star = star[0:4]
# star = star[0:3]
# star = star[0:2]
# star = star[0:1]

star = "******"
for i in range(5, 0, -1):  # [5, 4, 3, 2, 1]
    print(star[0:i])

for i in range(5):  # [0, 1, 2, 3, 4]
    # i 는 0, 1, 2, 3, 4
    # ? 는 5, 4, 3, 2, 1
    # 5 - i = ?
    print(star[0:5 - i])

# 트리 만들기
#     *
#    ***
#   *****
#  *******
# **********


# print가 5번 실행되므로 5번 반복하는 for문 생성
for i in range(5):       # [0, 1, 2, 3, 4]
    # i가 0, 1, 2, 3, 4
    # *은 1, 3, 5, 7, 9   ...i와의 관계는? 2 * i + 1
    #  는 4, 3, 2, 1, 0   ...i와의 관계는? 4 - i

    star = ""
    for k in range(2 * i + 1):   # 바깥 for문의 내부 변수 i와 다른 변수명 사용
        star += "*"

    blank = ""
    for k in range(4-i):
        blank += " "

    print(blank+star)


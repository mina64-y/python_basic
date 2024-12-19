# 조건문 (if문 사용)
# if : 만약에 ~라면

# 조건에 따라 다른 명령을 내릴 때 사용

# 조건이 참(Ture)이면 실행, 거짓(False)이면 실행X

# 비교연산자
a = 10
b = 10

# a와 b가 서로 같습니까?
print(a == b)

# 실행순서
# print(a == b)
# print(10 == b)
# print(10 == 10)
# print(Ture)

a = 10
b = 3

# a와 b가 서로 같습니까?
print(a == b)

# 실행순서
# print(a == b)
# print(10 == b)
# print(10 == 3)
# print(False)

# a와 b가 서로 다릅니까?
print(a != b)

# a가 b보다 큽니까?
print(a > b)

# a가 b보다 이상입니까? (같거나 큽니까?)
a = 10
b = 10
print(a >= b)

# b가 a보다 큽니까?
print(b > a)
# a가 b보다 작습니까?
print(a < b)

# a가 b보다 이하입니까?
print(a <= b)  # (<=, >=, !=) 등호는 항상 오른쪽

# 주민번호 뒷자리의 첫번째 숫자가
# 짝수면 여자, 홀수면 남자
# 1, 2, 3, 4, 5, 6, 7, 9, 0
# 1900년도에 태어난 남자 1, 여자 2
# 2000년도에 태어난 남자 3, 여자 4
# 1900년도에 태어난 외국인 남자 5, 여자 6
# 2000년도에 태어난 남자 7, 여자 8
# 1800년도에 태어난 남자 9, 여자 0

idNum = "1234567"

# idNum 의 첫번재 숫자가 홀수면 남성 출력, 짝수면 여성 출력
print(idNum[0])

fst = idNum[0]
# fst의 타입? 문자열
print(type(fst))  # '1'

# 파이썬은 배열에 곱하기를 하면 내용이 그 수만큼 늘어남
print(fst * 3)  # 111

# 홀수, 짝수 계산을 위해 fst를 int로 변환해야함
fst = int(fst)

# 홀수, 짝수 계산
# 어떤 수든 2로 나눴을 때 나머지 0이면 짝수, 1이면 홀수
print(fst % 2 == 0)

# 실행순서
# print(fst % 2 == 0)
# print(1 % 2 == 0)
# print(1 == 0)
# print(False)

print(fst % 2 == 1)

#  짝수일 때는 여성, 홀수일 때는 남성 출력
fst = 4
# if문의 조건이 Ture일 때만 if문 내부 코드가 실행 됨
if fst % 2 == 0:
    print("여성")  # Tap이 있기에 if문 내부 코드가 됨
print("성별체크")  # Tap이 없기에 if문과 무관한 코드

# fst가 홀수 일때는 남성이 출력되도록 if문 작성
if fst % 2 == 1:
    print("남성")

# 두 개의 if문을 하나로 묶기
if fst % 2 == 0:
    print("여성")
elif fst % 2 == 1:  # 위 if문이 false면, 추가적인 조건 체크
    print("남성")

# 짝수 체크를 해서 Ture면 짝수이고, false면 fst가 홀수라는 뜻
fst = 3
if fst % 2 == 0:
    print("여성")
else:  # 위 if문이 false면, 체크없이 실행
    print("남성")

# fsr가 1~4면 한국인
# fsr가 5~8면 외국인
# 1 <= fst <= 4
fst = 6
print(1 <= fst <= 4)
print(5 <= fst <= 8)  # boolean 값 (조건)

# if문 에 대해 1~4면 한국인, 5~8이면 외국인 출력하기
if 1 <= fst <= 4:
    print("한국인")
elif 5 <= fst <= 8:
    print("외국인")

if 1 <= fst <= 4:
    print("한국인")
else:
    print("외국인")

# 성적이 90점 이상이면 A등급 출력
# 성적이 80점대면 B등급 출력
# 성적이 70점대면 C등급 출력
# 그 외 나머지는 D등급 출력

score = 95
# score가 90점 이상 인지 확인
print(score >= 90)
# score가 80점대 인지 확인
print(80 <= score < 90)

if score >= 90:
    print("A등급")
elif 80 <= score < 90:
    print("B등급")
elif 70 <= score < 80:
    print("C등급")
else:
    print("D등급")

# if문의 실행 순서를 잘 고려한다면,
score = 85
if score >= 90:
    print("A등급")
elif 80 <= score:    # 이 타이밍에 score < 90 인 상황
    print("B등급")
elif 70 <= score:    # 이 타이밍에 score < 80 인 상황
    print("C등급")
else:
    print("D등급")

score = 95
if score >=70:       # 실행되면 아래의 코드는 실행되지 않음
    print("C등급")    # score >=70이 Fure로 실행되었으므로 즉시 종료.
elif 80 <= score:    # 그러므로  이 if문의 결과는 'C등급'
    print("B등급")
elif score >= 90:
    print("A등급")
else:
    print("D등급")

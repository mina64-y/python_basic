# 01_start.py를 실행 해서 메모리에 저장 되었던 변수 등은
# 01_start.py의 실행이 끝나면 모두 사라짐

# 01_string.py를 실행 하면 01_start.py는 전혀 실행 되지 않음.

# 문자열 가지고 놀기
station = "정부청사역, 시청역, 탄방역"

# 자동 완성 단축키 [Ctrl + Space]
print(station)

# 문자열 글자수 확인
# length의 약자를 써서 len()사용
print(len(station))

# 문자열의 인덱스(넘버링)를 이용해 특정 문자 꺼내기
print(station[1])
print(station[3])

# 어떤 문자열이든 첫번째 문자만 꺼내기
stuA = "김병준"
stuB = "김상"
stuC = "낭궁민궁"

print(stuA[0])
print(stuB[0])
print(stuC[0])

# 어떤 문자열이든 마지막 문자만 꺼내기
# stuA (3글자) 의 마지막 문자의 인덱스 : 2
# stuA (2글자) 의 마지막 문자의 인덱스 : 1
# stuA (4글자) 의 마지막 문자의 인덱스 : 3

print(stuA[2])
print(stuB[1])
print(stuC[3])

stuX = "김하얀푸른하늘꽃"
last = len(stuX) - 1
print(last)
print(stuX[last])

# 코드 자동 정렬(포맷팅) 단축키 [Ctrl + Shift + F]
print(stuA[len(stuA) - 1])
print(stuB[len(stuB) - 1])
print(stuC[len(stuC) - 1])

# 파이썬은 거꾸로도 인덱스 번호를 부여해 놓음
print(stuA[-1])
print(stuB[-1])
print(stuC[-1])

print(station[7])
print(station[-8])

# 문자열 내 특정 문자의 인덱스 번호 찾기
print(station.find("시"))
print(station.index("시"))

# 문자열 내 존재하지 않은 문자를 찾는 경우 차이점이 존재
print(station.find("용"))       # -1
# print(station.index("용"))
# 에러 발생(에러가 발생하는 시점에서 프로그램의 동작이 멈춤) -> 에러 처리
# 에러 처리를 해주면 프로그램이 멈추지 않음
try:
    print(station.index("용"))
except:
    print("에러 처리 구문") #에러가 발행 하면 실행O, 에러가 발생 하지 않으면 실행X

#문자열에서 인덱스 번호를 이용해서 특정 문자를 꺼내는 것을 인덱싱이라 함
print(station[3])

# 인덱스 번호를 이용해 여러 개의 문자를 꺼내는 것을 슬라이스라 함
# 정부청사역은 인덱스 0,1,2,3,4 에 해당
print(station[0:4])     # 0~3에 해당
print(station[0:5])     # 0~4에 해당

# 슬라이스해서 시청역을 출력하기
print(station[7:10])

print(station[7:])    # 7~마지막에 해당
print(station[:10])   # 처음~10에 해당

# 변수 이름 짓는 방식
name = "정창웅"

# 마나 포인트(mana point)
# 1. 스네이크 방식
mana_point = 50

# 2. 카멜 방식
manaPoint = 50

# 3. 요약 방식(Datebase 컬럼명에 자주 보임)
mp = 50
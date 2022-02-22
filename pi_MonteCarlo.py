import random  # 난수 생성 함수 라이브러리

sq_size = int(input("반복 수 입력 : "))  # 찍을 점의 개수 입력
cr_size = 0  # 원의 넓이 저장하는 변수 선언

for i in range(sq_size):  # 입력한 만큼 반복
    x = random.random()  # 랜덤 x좌표 생성
    y = random.random()  # 랜덤 y좌표 생성
    len = (x*x) + (y*y)  # 원점으로부터의 거리 계산

    if(len <= 1):  # 만약 거리가 1보다 작거나 같으면
        cr_size += 1  # 원의 넓이에 1만큼 더하라

pi = 4*(cr_size/sq_size)  # 원주율 계산
print("pi : %.15lf" % pi)  # 결괏값 출력
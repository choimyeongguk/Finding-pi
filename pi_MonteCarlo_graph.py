from matplotlib import pyplot as plt  # 그래프 관련 라이브러리
import random  # 난수 관련 라이브러리
import math  # 수학 관련 라이브러리
import os  # 시스템 관련 라이브러리


def circle(a, b, r):  # 원 그리기 함수 선언
    x = []
    y = []
    for theta in range(0, 360):
        x.append(a+r*math.cos(math.radians(theta)))  # x좌표 이동
        y.append(b+r*math.sin(math.radians(theta)))  # y좌표 이동
    plt.plot(x, y, color="gray")  # 원 그리기


plt.figure(figsize=(7, 7))  # 그래프 관련 설정
plt.axis([0, 1, 0, 1])  # 그래프 범위 0~1
plt.xlabel('x')  # x축
plt.ylabel('y')  # y축
circle(0, 0, 1)  # 함수 실행

sq_size = int(input("반복 수 입력 : "))  # 찍을 점 개수 입력
cr_size = 0  # 변수 선언

for i in range(sq_size):  # 입력한 만큼 반복
    x = random.random()  # 0~1 사이 랜덤 x좌표 생성
    y = random.random()  # 0~1 사이 랜덤 y좌표 생성
    len = (x*x) + (y*y)  # 원점으로부터의 거리 계산

    if(len <= 1):  # 만약 원점에서의 거리가 1이하라면,(부채꼴 안에 들어간다면)
        cr_size += 1  # 원안의 점 +1
        plt.scatter(x, y, s=50, c='r')  # 좌표에 점 찍기
    else:  # 아니면 (부채꼴 밖이면)
        plt.scatter(x, y, s=50, c='b')  # 좌표에 점 찍기

pi = 4*(cr_size/sq_size)  # 원주율 계산 pi=s/(r*r)
print("pi : %.15lf" % pi)  # 계산한 값 출력
plt.title("n = %d, π = %lf" % (sq_size, pi), fontsize=25)  # 그래프 제목
plt.show()  # 그래프 출력

os.system("pause")  # 콘솔창 유지

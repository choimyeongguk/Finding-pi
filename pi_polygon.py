# import os  # 시스템 관련 라이브러리

# for i in range(0, 14, 1):  # 14번 반복
#     side = 1  # 다각형 변 길이 초기화
#     angle = 6*2**i  # 다각형 변 개수 계산

#     for j in range(i):  # i번 반복
#         side = (2-(4-side*side)**.5)**.5  # 공식 적용
#     pi = angle*side/2  # 원주율 계산 pi=(변 길이)*(변 개수)/(대각선 길이)

#     print("%d회, 정%d각형, pi : %.15lf" % (i+1, angle, pi))  # 계산한 값 출력

# os.system("pause")  # 콘솔창 유지


num = int(input("반복 횟수 입력 : "))  # 반복할 횟수 입력
angle_num = 6*2**num  # 다각형 변 개수 계산
side_length = 1  # 변 개수 초기화

for i in range(num):  # 입력한 값 만큼 반복
    side_length = (2-(4-side_length*side_length)**.5)**.5  # 식 대입
pi = angle_num*side_length/2  # pi=(변의 길이)*(변의 개수)/2

print("%d회, 정%d각형, pi : %.15lf" % (num, side_length, pi))  # 결과 출력

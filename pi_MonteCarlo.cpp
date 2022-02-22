#include <stdio.h>  //라이브러리 : 이미 만들어진 함수 모음 
#include <stdlib.h>  //랜덤 함수 라이브러리 
#include <time.h>  //시간 함수 라이브러리

int main(){
	double pi,x,y,len=0,cr_size,sq_size;
	double max=32767;
		
	printf("반복 수 입력 : ");
	scanf("%lf",&sq_size);  //반복할 횟수 입력 
		
	srand(time(NULL));  //난수 초기화 
	
	for(int i=0;i<sq_size;i++){  //입력한 수 만큼 반복 
		x=rand()/max;  //랜덤 x 좌표 
		y=rand()/max;  //랜덤 y 좌표 
		len=(x*x) + (y*y);  //원점으로 부터의 거리 
		
		if(len<=1){  //만약 거리가 1보다 작거나 같다면 
			cr_size++;  //원넓이 1 추가 
		}
		pi=4*(cr_size/sq_size);  //원주율 구하기 반*반*pi*1/4=cr_size 
	}
	printf("pi : %.15lf\n",pi);  //결과값 출력
	
	printf("\nPress enter to exit");
	system("pause>nul");
	return 0;
}	

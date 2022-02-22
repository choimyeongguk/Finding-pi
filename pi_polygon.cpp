#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
	
	int num;
	double b=1;
	double pi;
	
	printf("반복 수 입력 : ");
	scanf("%d",&num);
	int angle=6*pow(2,num);
	
	for(int i=0;i<num;i++)
	{
		b=sqrt(2-sqrt(4-b*b));
	}
	
	pi=angle*b/2;
	printf("정%d각형, pi : %.15lf",angle,pi);
	
	printf("\n\nPress enter to exit");
	system("pause>nul");
	return 0;
}

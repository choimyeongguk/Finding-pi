#include <stdio.h>  //���̺귯�� : �̹� ������� �Լ� ���� 
#include <stdlib.h>  //���� �Լ� ���̺귯�� 
#include <time.h>  //�ð� �Լ� ���̺귯��

int main(){
	double pi,x,y,len=0,cr_size,sq_size;
	double max=32767;
		
	printf("�ݺ� �� �Է� : ");
	scanf("%lf",&sq_size);  //�ݺ��� Ƚ�� �Է� 
		
	srand(time(NULL));  //���� �ʱ�ȭ 
	
	for(int i=0;i<sq_size;i++){  //�Է��� �� ��ŭ �ݺ� 
		x=rand()/max;  //���� x ��ǥ 
		y=rand()/max;  //���� y ��ǥ 
		len=(x*x) + (y*y);  //�������� ������ �Ÿ� 
		
		if(len<=1){  //���� �Ÿ��� 1���� �۰ų� ���ٸ� 
			cr_size++;  //������ 1 �߰� 
		}
		pi=4*(cr_size/sq_size);  //������ ���ϱ� ��*��*pi*1/4=cr_size 
	}
	printf("pi : %.15lf\n",pi);  //����� ���
	
	printf("\nPress enter to exit");
	system("pause>nul");
	return 0;
}	

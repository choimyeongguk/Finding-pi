#include <stdio.h>

int f(int x);

int main()
{
	for(int i=0;i<5;i++)
	{
		printf("f(%d) = %d\n",i,f(i));
	}
}

int f(int x)
{
	return 2*x+1;
}

#include <stdio.h>

int main() {
	printf("Counting\n");
	long int sum=0;
	for (int x=0; x<1000000000; ++x)
		sum+=x;
	printf("Sum is %ld\n",sum);
	return 0;
}

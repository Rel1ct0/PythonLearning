#include <iostream>
using namespace std;

int main() {
	cout << "Counting" << endl;
	long int x=0;
	for (int i=0; i<1000000000; ++i) 
		x+=i;
	cout << "Sum is " << x << endl;
	return 0;
}

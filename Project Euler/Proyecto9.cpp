#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
int numero; 
int c;
int d;

for(int a=1;a<1000;a++){
	for(int b=1;b<1000;b++){
		if((a+b+sqrt(pow(a,2)+pow(b,2)))==1000){
			numero=a*b*sqrt(pow(a,2)+pow(b,2));
			c=a;
			d=b;
			
		}
	}
}
printf("%i\n", c);
printf("%i\n", d);
printf("%i\n", sqrt(pow(c,2)+pow(d,2)));
printf("%i", numero);
}

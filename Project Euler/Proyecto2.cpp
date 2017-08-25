#include <iostream>
#include <stdio.h>
#include<math.h>
#include<limits.h>
#include<stdint.h>

using namespace std;

int main(){	
int contador=0;
long long int suma;
long long int fibonacci1=1;
long long int fibonacci2=2;
long long int sumafibonacci=2;

for(int x=0;x<4000000;x++){
	if(contador==0 &fibonacci2<4000000){
		fibonacci1+=fibonacci2;
		contador=1;
		if(fibonacci1%2==0){
			sumafibonacci+=fibonacci1;
		}
	}else if(contador==1&fibonacci1<4000000){
		fibonacci2+=fibonacci1;
		contador=0;
		if(fibonacci2%2==0){
			sumafibonacci+=fibonacci2;
		}
	}
}
printf("%lli", sumafibonacci);
}

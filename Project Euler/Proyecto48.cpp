#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
long long int suma;
long long int numerotemporal;
int numero;

for(int x=1;x<1001;x++){
	numerotemporal=x;
	numero=x;
	for(int y=1;y<x;y++){
		numerotemporal=(numerotemporal*numero)%10000000000;
		}
suma=(suma+numerotemporal)%10000000000;
}
printf("%lli\n", suma-1);
}

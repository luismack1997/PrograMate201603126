#include <iostream>
#include <stdio.h>
#include<math.h>
#include<limits.h>
#include<stdint.h>

using namespace std;

int main(){	
long long int primo[200001];
long long int numero=3;
primo[0]=2;
int contador=1;
long long int sumaprimos=2;

while(contador<200000){
	for(int x=0;x<contador;x++){
		if(numero%primo[x]==0){
			numero++;
			x=contador;
		}else if(primo[x]>sqrt(numero)){
			primo[contador]=numero;	
			if(numero<2000000){
				sumaprimos+=numero;	
		}
	numero++;
	contador++;
	x=contador;
	
	}
}
}
printf("%lli\n",sumaprimos);
	
}

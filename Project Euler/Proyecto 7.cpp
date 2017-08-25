#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[12001];
int numero=3;
primo[0]=2;
int contador=1;

while(contador<12002){
	for(int x=0;x<contador;x++){
	if(numero%primo[x]==0){
		numero++;
		x=contador;
	}else if(primo[x]>sqrt(numero)){
		primo[contador]=numero;
		numero++;
		contador++;
		x=contador;
	
	}
}
}
printf("%i\n",primo[12000]);	
}


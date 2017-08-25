#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[200001];
int numero=3;
primo[0]=2;
int contador=1;
int elnumero;
int compuesto=3;

while(contador<200002){
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

while(elnumero==0){
	for(int x=0;x<sqrt(compuesto);x++){
		if(compuesto%primo[x]==0){
			for(int y=0;primo[y]<=compuesto;y++){
				for(int z=1;z<=sqrt(compuesto);z++){
					if(compuesto==primo[y]+2*pow(z,2)){
						z=sqrt(compuesto);
						y=compuesto;
						x=sqrt(compuesto);
					}else if(z==sqrt(compuesto)&primo[y]>compuesto){
						elnumero=compuesto;
					
				}
				}
			}
		}
	}
	compuesto+=2;

}

printf("%i", elnumero);	
}

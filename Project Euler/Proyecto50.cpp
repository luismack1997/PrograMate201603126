#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[100001];
int numero=3;
primo[0]=2;
int contador=1;
int sumaparcial;

while(contador<100002){
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

for(int z=100;z>0;z--){
	for(int x=0;x<z;x++){
	for(int y=x;y<100002;y++){
		if(sumaparcial+primo[y]<1000000){
			sumaparcial+=primo[y];
		}else {
			for(int w=0;w<sumaparcial;w++){
				if(sumaparcial%primo[w]==0){
		sumaparcial=0;
		w=sumaparcial;
		y=100002;
	}else if(primo[w]>sqrt(sumaparcial)){
		w=sumaparcial;
		y=100002;
		x=z;
		z=0;
	
	}
			}
			
		}
		}
}
}
printf("%i", sumaparcial);
	
}

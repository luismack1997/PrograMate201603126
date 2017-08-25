#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[12001];
int numero=3;
long long int contador=1; 
int noPrimosRelativos=0;
int contador1=0;
primo[0]=2;
float a=0;



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

for(int x=2;x<=12000;x++){
	for(int y=1;y<x;y++){
		noPrimosRelativos=0;
		for(int z=0;primo[z]<=y;z++){
			if(y%primo[z]==0 and x % primo[z]==0){
				noPrimosRelativos=1;
				break;
			}
		}

		if(noPrimosRelativos==0 and 3*y>x and 2*y<x){
			contador1++;
		}
	}
	
}

printf("%lli", contador1);

}


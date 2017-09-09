#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[80001];
int numero=3;
primo[0]=2;
int contador=1;
long long int sum=0;
int primo1=1;
int contador2=0;
int temporal=0;
int a=0;
int suma=0;

while(contador<80002){
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

while(primo[contador2]<1000000){
	temporal=primo[contador2];
	a=pow(10,int(log10(primo[contador2])));
	for(int x=1;x<=int(log10(primo[contador2]));x++){
		temporal=(temporal % a )*10+(temporal-temporal %a )/a;
		for(int y=0;primo[y]<=int(sqrt(temporal));y++){
			 if(temporal % primo[y] ==0){
			 	primo1=0;
			 }   	
		}       
	}
	if(primo1==1){
		suma++;
	}
	
	contador2++;
	primo1=1;
}
printf("%lli", suma);
	
}

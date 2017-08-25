#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int Phi(int);
int primo[100000];


int main(){	
primo[0]=2;
int numero=3;
int contador1=1; 
long long int suma=0;
int temporal2=0;
while(contador1<100001){
	for(int x=0;x<contador1;x++){
	if(numero%primo[x]==0){
		numero++;
		x=contador1;
	}else if(primo[x]>sqrt(numero)){
		primo[contador1]=numero;
		numero++;
		contador1++;
		x=contador1;
	
	}
}
}

for(int x=2;x<=1000000;x++){
	temporal2=Phi(x);
	suma+=temporal2;
}
printf("%lli", suma);

}

int Phi(int numero){
	int contador[200001];
	int PrimosRelativos=1;
	int contador2=0;
	int temporal=1;
	for (int x = 0; primo[x]<=numero;x++){
		if (numero % primo[x] == 0){
			numero=numero/primo[x];
			contador[2*contador2]=1;
			contador[2*contador2+1]=primo[x];
			while(temporal>0){
				if(numero%primo[x]==0){
					contador[2*contador2]++;
					numero=numero/primo[x];
				}else{
					temporal=0;
				}	
			}
  			contador2++;
  			temporal=1;}	
	}
	for(int y=0;y<=contador2-1;y++){
	PrimosRelativos*=(contador[2*y+1]-1)*pow(contador[2*y+1],contador[2*y]-1);
}

return PrimosRelativos; 	
}

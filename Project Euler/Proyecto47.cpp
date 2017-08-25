#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int Divisores(int);
int primo[100000];


int main(){	
primo[0]=2;
int numero=3;
int contador1=1; 
long long int elNumero=0;
int temporal2=0;
long long int numero2=2;
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

while(elNumero==0){
	temporal2=Divisores(numero2);
	if(temporal2==4){
		temporal2=Divisores(numero2+1);
		if(temporal2==4){
			temporal2=Divisores(numero2+2);	
			if(temporal2==4){
				temporal2=Divisores(numero2+3);
				if(temporal2==4){
					elNumero=numero2;
				}
			}
		}
	}
	numero2++;
}
printf("%lli", elNumero);

}

int Divisores(int numero){
	int contador[200001];
	int contador2=0;
	int temporal=1;
	for (int x = 0; primo[x]<=numero;x++){
		if (numero % primo[x] == 0){
			numero=numero/primo[x];
			contador[contador2]=1;
			while(temporal>0){
				if(numero%primo[x]==0){
					contador[contador2]++;
					numero=numero/primo[x];
				}else{
					temporal=0;
				}	
			}
  			contador2++;
  			temporal=1;}	
	}

return contador2; 	
}




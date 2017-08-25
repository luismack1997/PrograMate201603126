#include <iostream>
#include <stdio.h>
#include<math.h>
#include <fstream>
using namespace std;

int main(){	
int cantidadmasgrande;
long long int numero; 
int elnumero;
int cantidad;


for(int x=3;x<=999999;x+=2){
	numero=x;
	while(numero!=1){
		if(numero%2==0){
			numero=numero/2;
			cantidad++;
		}else{
			numero=3*numero+1;
			cantidad++;
		}
	}

	if(cantidad>cantidadmasgrande){
		elnumero=x;
		cantidadmasgrande=cantidad; 
	}
	cantidad=0;	
}

printf("%lli", elnumero);
}

#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
int digito[200001];
int sumadigitos;
digito[0]=1;
int contador=0;

for(int x=1;x<=200000;x++){
	for(int y=contador;y>=0;y--){
		if(y==contador & digito[contador]>4){
			digito[y]=digito[y]*2-10;
			contador++;	
			digito[contador]=1;
		}else if(digito[y]>4){
			digito[y]=digito[y]*2-10;	
			digito[y+1]+=1;
		}else{
			digito[y]*=2;
		}
	}
}

for(int y=contador;y>=0;y--){
	sumadigitos+=digito[y];
printf("%i", digito[y]);
}
printf("\n");

printf("%i\n", sumadigitos);
printf("%i\n", contador+1);
}

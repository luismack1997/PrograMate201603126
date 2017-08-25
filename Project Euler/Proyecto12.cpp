#include <iostream>
#include <stdio.h>
#include<math.h>
using namespace std;

int main(){	
int primo[2000];
int numero=3;
primo[0]=2;
long long int triangular;
int contador1=1; 
int CantidadDivisores=1;
long long int elTriangular;
int contador[100001];
int contador2=0;
int contador3=2;
int temporal=1;
int a;


while(contador1<2000){
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

 
while(CantidadDivisores<500){
	triangular=contador3*(contador3+1)/2;
	a=triangular;
	contador3++;
	
	for (int x = 0; primo[x]<=triangular;x++){
		if (triangular % primo[x] == 0){
			triangular=triangular/primo[x];
			contador[contador2]=1;
			while(temporal>0){
				if(triangular%primo[x]==0){
					contador[contador2]++;
					triangular=triangular/primo[x];
				}else{
					temporal=0;
				}	
			}
  contador2++;
  temporal=1;
  }	
 }
 
for(int y=0;y<=contador2;y++){
	CantidadDivisores=CantidadDivisores*(contador[y]+1);
}


if(CantidadDivisores<500){
	CantidadDivisores=1;
for(int y=0;y<=5000;y++){
	contador[y]=0;
	contador2=0;
}

}else{
	elTriangular=a;
}	
}
printf("%lli\n", elTriangular);


}
	



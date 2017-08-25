#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
int PrimoMayor;

for(int x=sqrt(600851475143);x>0;x--){
	if(600851475143%x==0){
		for(int y=sqrt(x);y>0;y--){
			if(y==1){
				PrimoMayor=x;
				x=0;
			}else if(x%y==0){
				y=0;
			}
			}		
	
}

}
printf("%i\n",PrimoMayor);
}

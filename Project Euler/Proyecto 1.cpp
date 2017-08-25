#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
int suma=0;

for(int x=1;x<1000;x++){
	if(x%3==0 or x%5==0){
		suma+=x;
	}
}
printf("%i\n", suma);
}

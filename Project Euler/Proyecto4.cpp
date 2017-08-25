#include <iostream>
#include <stdio.h>
#include<math.h>

using namespace std;

int main(){	
int palindrome;
int xy;


for(int x=999;x>100;x--){
	for(int y=999;y>100;y--){
		xy=x*y;
		if(x*y>100000){
			if((xy-(xy%1000))/1000== (xy%10)*100+xy%100-(xy%10)+  (xy%1000-xy%100)/100){
				if(xy>palindrome){
				palindrome=x*y;	
				}
 
			}
	}
}
}
printf("%lli\n", palindrome);
}

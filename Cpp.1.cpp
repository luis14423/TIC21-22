#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	int x[5];
	int cont;
	float suma=0.0;
	for(cont=0;cont<5;cont++){
		printf("Dame un numero: ");
		scanf("%d",&x[cont]);
	}
	
	for(cont=0;cont<5;cont++){
		printf("\n%d",x[cont]);
		suma=suma+x[cont];
	}
	
	float media=(suma/5.0);
	
	printf("\nLa suma es igual a %f",suma);
	printf("\nLa media es igual a %f",media);
	
	return(0);
}

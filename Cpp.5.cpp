#include<stdio.h>

int main(){
	char palabra[5];
	int cont;
	printf("Escribe una palabra: ");
	scanf("%s",palabra);
	printf("\nHAS ESCRITO LA PALABRA %s",palabra);
	printf("\nVOY A DELETREARLA: ");
	for(cont=0;cont<5;cont++){
		printf("\n%c",palabra[cont]);
	}
	
	
	palabra[1]='u';
	printf("\nPalabra cambiada: %s",palabra); //cambiar la letra en posicion 1
	
	
	printf("\nQuien es quien: ");
	printf("\npalabra[0]=%x",&palabra[0]); //Esto es para ver la direccion
		
	
	
	return(0);
}
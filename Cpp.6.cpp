#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//PUNTERO 3

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[100]; //reservo una variable auxiliar para guardar provisionalmente la palabra
	int longitud; //defino el tamano de la palabra
	printf("\nDime una palabra: ");
	scanf("%s",aux); //leo la palabra
	longitud=strlen(aux);
	char *palabra;//palabra es un puntero (una variable que contiene una direccion de la memoria de algo que es una letra)
	palabra=(char*)malloc(longitud*sizeof(char));//memory allocation
	strcpy(palabra,aux);
	printf("\nRESULTADO: ");
	printf("%s",palabra);
	return(0);
}
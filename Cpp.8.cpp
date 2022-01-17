#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	//PUNTERO 5
	char aux[10];//reservo una variable aux
	int longitud; //Defino el tamano
	char *mispalabras[5];
	int cont;
	for(cont=0;cont<5;cont++){
		//Pido el nombre de un rey
		printf("\nDime la palabra %d: ",cont);
	
		//Lo guardo en una var aux
		scanf("%s",aux);
		//Cuento el numero de letras
		longitud=strlen(aux);
		//Busco un hueco en la memoria de ese tamano y apunto su direccion
		mispalabras[cont]=(char*)malloc(longitud*sizeof(char));
		//Copio el nombre desde aux hasta el hueco encontrado
		strcpy(mispalabras[cont],aux);
	}
	printf("\n LAS CINCO PALABRAS SON: ");
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont)); //sustituyo mispalabras[cont] por *(mispalabras+cont)
	}
	
	
	
return(0);
}
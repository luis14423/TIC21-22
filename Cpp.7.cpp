#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	//REYES MAGOS
	char aux[10];//reservo una variable aux
	int longitud; //Defino el tamano
	char *lista[3];//
	int cont;
	for(cont=0;cont<3;cont++){
		//Pido el nombre de un rey
		printf("\nDime un nombre de un rey %d: ",cont);
	
		//Lo guardo en una var aux
		scanf("%s",aux);
		//Cuento el numero de letras
		longitud=strlen(aux);
		//Busco un hueco en la memoria de ese tamano y apunto su direccion
		lista[cont]=(char*)malloc(longitud*sizeof(char));
		//Copio el nombre desde aux hasta el hueco encontrado
		strcpy(lista[cont],aux);
	}
	printf("\n LOS TRES REYES MAGOS SON: ");
	for(cont=0;cont<3;cont++){
		printf("\n %s",lista[cont]);
	}
	
	
	
	
	
	
	
	
	
	
	
return(0);
}
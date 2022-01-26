#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int cuenta_vocales(char *letrita){
	int n_vocales=0;
	int cont;
	int longitud;
	longitud=strlen(letrita);
	for(cont=0;cont<longitud;cont++){
		if(*(letrita+cont)=='A'||*(letrita+cont)=='a'){
			n_vocales++;
		}
		
		if(*(letrita+cont)=='E'||*(letrita+cont)=='e'){
			n_vocales++;
		}
		
		if(*(letrita+cont)=='I'||*(letrita+cont)=='i'){
			n_vocales++;
		}
		
		if(*(letrita+cont)=='O'||*(letrita+cont)=='o'){
			n_vocales++;
		}
		
		if(*(letrita+cont)=='U'||*(letrita+cont)=='u'){
			n_vocales++;
		}
	}
	
	
	return(n_vocales);
}
int main(){
	//PUNTERO NUMERO DE VOCALES
	char provisional[10];
	char *aux;//reservo una variable aux para guardar la direccion de la palabra
	int longitud; //Defino el tamano
	char *mispalabras[5];
	int cont;
	int repetir;
	int voc1;
	for(cont=0;cont<5;cont++){
		//Pido el nombre de un rey
		printf("\n");
		printf("\nDime la palabra %d: ",cont);
	
		//Lo guardo en una var aux
		scanf("%s",provisional);
		printf("La palabra %s tiene %d vocales",provisional,cuenta_vocales(provisional));
		//Cuento el numero de letras
		longitud=strlen(provisional);
		//printf("\nMide %d",longitud); //pido que me muestre la longitud
		//Busco un hueco en la memoria de ese tamano y apunto su direccion
		mispalabras[cont]=(char*)malloc(longitud*sizeof(char));
		//Copio el nombre desde aux hasta el hueco encontrado
		strcpy(mispalabras[cont],provisional);
	}
	printf("\n");
	printf("\nLAS CINCO PALABRAS SON: ");
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont)); //sustituyo mispalabras[cont] por *(mispalabras+cont)
	}
	
	for(repetir=1;repetir<5;repetir++){
		for(cont=0;cont<=3;cont++){
			if((cuenta_vocales(mispalabras[cont]))>(cuenta_vocales(mispalabras[cont+1]))){
				aux=mispalabras[cont];
				mispalabras[cont]=mispalabras[cont+1];
				mispalabras[cont+1]=aux;
			
			}
		}
	}
	printf("\n");//Dejo un poco de hueco
	printf("\n");//Dejo un poco de hueco
	printf("\n");//Dejo un poco de hueco
	
	//vuelvo a mostrar las palabras ordenadas
	printf("\n LAS CINCO PALABRAS SON: ");
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont)); //sustituyo mispalabras[cont] por *(mispalabras+cont)
	}
	
	return(0);
}
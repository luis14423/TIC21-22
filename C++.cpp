#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//REPASO CON DOS PROGRAMAS PARA EXAMEN
//CONTADOR DE DIAS
int main(){
	int mes;
	int cont;
	int dia;
	
	printf("Introduzca el mes: ");
	scanf(" %d",&mes);
	
	printf("Introduzca el dia: ");
	scanf(" %d",&dia);
	
	printf("\ndia: %d",dia);
	printf("\nmes: %d",mes);
	
	int fecha=30*(mes-1)+dia;
	
	printf("\nHan pasado %d dias desde ano nuevo",fecha);
	
	
	return(0);
}

//HALLADOR DE DENOMINADORES COMUNES
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	int x;
	int y;
	int cont;
	
	printf("Introduzca un numero: ");
	scanf("%d",&x);
	
	printf("Introduzca otro numero: ");
	scanf("%d",&y);
	
	for(cont=1;cont<100;cont=cont+1){
		if(x%cont==0 and y%cont==0){
			printf("\nEl numero %d es un denominador comun",cont);
		}
	}
	
	
	return(0);
}

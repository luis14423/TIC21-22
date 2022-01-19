#include<stdio.h>
#include<string.h>
#include<stdlib.h>
 //METODO DE ORDENAR 1
 int main(){
 	int numeros[5];
 	int cont;
 	int aux;
 	int repetir;
 	
 	
 	for(cont=0;cont<5;cont++){
 		printf("\nIntroduzca un numero: ");
 		scanf("%d",&numeros[cont]);//leo la lista
 	}
 	
 	
 	printf("\nLos numeros introducidos son: ");
 	for(cont=0;cont<5;cont++){
 		printf("%d ",numeros[cont]);//muestro la lista
 	}
 	
 	
	//ordeno la lista
	for(repetir=1;repetir<5;repetir++){
		for(cont=0;cont<=3;cont++){
			if(numeros[cont]>numeros[cont+1]){
				aux=numeros[cont];
				numeros[cont]=numeros[cont+1];
				numeros[cont+1]=aux;
			
			}
		
		}
	}
	
	//la vuelvo a mostrar
	printf("\nLISTA ORDENADA: ");
 	for(cont=0;cont<5;cont++){
 		printf("%d ",numeros[cont]);
	
	}
 	return(0);
 }
 
 //54321
 //43215
 //32145
 //21345
 //12345
 
 
 
 
 
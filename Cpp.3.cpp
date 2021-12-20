#include <stdio.h>//FICHERO DE CABECERA
int main() {
    char letras[5];
    int cont;
   
   
    for(cont=0;cont<5;cont++){
        printf("introduzca la letra %d: ",cont);
        scanf(" %c",&letras[cont]);
    }
    // Escribo datos en la pantalla
    printf("\nHAS ESCRITO LA PALABRA: ");
    for(cont=0;cont<5;cont++){
        printf("%c",letras[cont]);
       
    }
    //escribo la palabra al reves
    printf("\nTU PALABRA AL REVES ES: ");
    for (cont=4;cont>=0;cont--){
        printf("%c",letras[cont]);
    }
   
   
    return (0);
}
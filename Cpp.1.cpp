#include <stdio.h>//FICHERO DE CABECERA
int main() {
    int x[10];
    int cont;
    float suma=0;
    float media;
    for(cont=0;cont<10;cont++){//numero empezamos;hasta que numero;de cuanto en cuanto sumamos
    // cont++=cont+1
        printf("dame un numero: ");
        scanf("%d",&x[cont]);
    }
    // Escribo datos en la pantalla
    for(cont=0;cont<10;cont++){
        printf("\n%d",x[cont]);
        suma=suma+x[cont];
        //Suma=+x[cont];
    }
    media=suma/cont;
    printf("\nLa MEDIA VALE= %.2f",media);
    //Donde pone %d ahi saldra lo que queramos que salga
    return (0);
}
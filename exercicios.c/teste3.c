/*
    NOME: JEAN LUCAS
    DATA: 25/03/2026
    OBJETIVO: 
*/

#include <stdio.h>

int main() 
{
    float   nota1;
    float   nota2;
    float   nota3;
    float   nota4;
    float   media;

    printf("Digite sua nota: ");
    scanf("%f", &nota1);

    printf("Digite sua nota: ");
    scanf("%f", &nota2);

    printf("Digite sua nota: ");
    scanf("%f", &nota3);

    printf("Digite sua nota: ");
    scanf("%f", &nota4);

    media = (nota1 + nota2 + nota3 + nota4) / 4;

    if (media >= 7) 
    {
        printf("Voce passou de ano com uma media de %.1f", media);
    } else 
    {
        printf("Voce reprovou com uma media de %.1f", media);
    }

    return 0;
}

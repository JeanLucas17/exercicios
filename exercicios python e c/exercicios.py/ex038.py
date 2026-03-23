for i in range(2):
    numero = int(input('Digite um numero inteiro: '))
    if i == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
if maior != menor:
    print(f'O maior numero é o {maior}!\nO menor numero é o {menor}!')
else:
    print('Os dois numeros são iguais!')

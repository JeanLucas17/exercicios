from random import randint

computador = randint(1, 100)
tentativas = 0
jogador = 0

print('=-=' * 23)
print('JOGUE UM JOGO!! VOCÊ TEM QUE ACERTAR O NUMERO QUE ESTOU PENSANDO!')
print('=-=' * 23)

while computador != jogador:
    jogador = int(input('DIGITE UM NUMERO DE 1 A 100, Sua tentativa: '))
    tentativas += 1
    if jogador < computador:
        print('MAIOR!')
    elif jogador > computador:
        print('MENOR!')
print(f'Parabéns! Você ganhou com {tentativas} tentativas!')

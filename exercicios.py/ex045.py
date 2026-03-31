from random import choice

lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)


print('Jogue pedra, papel e tesoura com o computador!')

jogador = input('Sua escolha: ').lower().replace(' ', '')

if jogador not in lista:
    print('Apenas pedra, papel e tesoura')
else:
    if jogador == 'pedra' and computador == 'tesoura':
        print(f'Parabéns! Você ganhou!')
    elif jogador == 'tesoura' and computador == 'papel':
        print(f'Parabéns! Você ganhou!')
    elif jogador == 'papel' and computador == 'pedra':
        print(f'Parabéns! Você ganhou!')
    elif jogador == computador:
        print(f'Empate! O computador também escolheu {computador}!')
    else:
        print(f'Você perdeu! O computador escolheu {computador}!')

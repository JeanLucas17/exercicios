nota1 = float(input('Digite sua nota em matematica: '))
nota2 = float(input('Digite sua nota em português: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Você reprovou com uma media de {media:.1f}!')
elif media < 6.9:
    print(f'Você ficou de recuperação com uma media de {media:.1f}!')
else:
    print(f'Você foi aprovado com uma media de {media:.1f}!')

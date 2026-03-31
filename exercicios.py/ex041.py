ano = int(input('Digite o ano que você nasceu: '))
idade = 2026 - ano

if idade <= 9:
    print('Você esta na categoria MIRIM!')
elif idade <= 14:
    print('Você esta na categoria INFANTIL!')
elif idade <= 19:
    print('Você esta na categoria JUNIOR!')
elif idade <= 20:
    print('Você esta na categoria SÊNIOR!')
else:
    print('Você esta na categoria MASTER!')

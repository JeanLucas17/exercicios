ano = int(input('Digite o ano que você nasceu: '))
idade = 2026 - ano
alistamento = ano + 18

if idade < 18:
    print(f'Você ainda vai se alistar! Faltando {18 - idade} ano!')
elif idade == 18:
    print(f'Você irá se alistar esse ano! Se prepare!')
else:
    print(f'Você deveria ter se alistado em {alistamento}!')

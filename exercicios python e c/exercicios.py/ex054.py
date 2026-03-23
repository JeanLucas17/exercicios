total_maior = 0
total_menor = 0

for i in range(7):
    ano = int(input('Digite o seu ano de nascimento: '))
    idade = 2026 - ano
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'{total_maior} pessoas são maiores de idade!\n{total_menor} pessoas são menores de idade!')

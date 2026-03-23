maior_peso = 0
menor_peso = 0

for i in range(5):
    peso = float(input('Digite o seu peso: '))
    if i == 0:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif menor_peso > peso:
        menor_peso = peso
else:
    print(f'O maior peso é Kg {maior_peso}!\nO menor peso é {menor_peso}!')

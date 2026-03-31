maior = menor = 0

for i in range(5):
    peso = float(input("Digite seu peso em Kg: "))
    if i == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior} Kg, e o menor peso é {menor} Kg!")

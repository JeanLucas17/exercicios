s = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        s += i
print(f'A soma de todos os numeros impares multiplos de 3 entre 1 e 500 é {s}!')

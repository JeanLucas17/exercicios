s = 0

for i in range(6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos numeros pares é {s}!')

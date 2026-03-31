s = 0
numeros_digitados = 0

num = int(input("Digite um numero: "))

while num != 999:
    s += num
    numeros_digitados += 1
    num = int(input("Digite um numero: "))

print(f"Foram digitados {numeros_digitados} numeros. A soma dos numeros é {s}")

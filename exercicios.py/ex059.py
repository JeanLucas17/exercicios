from time import sleep

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

print("Menu: \n [1] Soma \n [2] Multiplicação \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa")
escolha = int(input("Sua escolha: "))

while escolha != 5:
    if 1 <= escolha <= 4:
        if escolha == 1:
            print(f"A soma de {num1} + {num2} = {num1 + num2}!")
        elif escolha == 2:
            print(f"A multiplicação de {num1} x {num2} = {num1 * num2}!")
        elif escolha == 3:
            print(f"O maior numero é {max(num1, num2)}")
        else:
            num1 = int(input("Digite o novo numero: "))
            num2 = int(input("Digite o outro numero: "))
    else:
        print("Apenas escolhas de 1 a 5!")

    sleep(2)

    print("Menu: \n [1] Soma \n [2] Multiplicação \n [3] Maior \n [4] Novos numeros \n [5] Sair do programa")
    escolha = int(input("Sua escolha: "))

print("Saindo...")
sleep(2)

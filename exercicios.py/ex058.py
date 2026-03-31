from time import sleep
from random import randint

computador = randint(0, 10)
tentativas = 0
jogador = 11

print("JOGUE UM JOGO! ADIVINHE O NUMERO DE 0 A 10!")
print("Pensando...")
sleep(2)

while jogador != computador:
    jogador = int(input("Em que numero eu pensei? "))
    if 0 <= jogador <= 10:
        tentativas += 1
        if jogador == computador:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        else:
            print("Errado!")
    else:
        print("Apenas numeros de 0 a 10!")

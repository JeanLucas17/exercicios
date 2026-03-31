print("Verificar se é palindromo!")
frase = str(input("Digite uma frase: ")).lower().replace(' ', '')

inverso = frase[::-1]

if frase == inverso:
    print(f"A frase '{frase}' é palindromo!")
else:
    print(f"A frase '{frase}' não é palindromo!")

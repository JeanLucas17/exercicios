frase = input('Digite uma frase: ').lower().replace(' ', '')
inverso = frase[::-1]

if frase == inverso:
    print('A frase é palindromo!')
else:
    print('A frase não é palindromo!')

numero = int(input('Digite um numero inteiro: '))
base = int(input('Bases de conversão:\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal\nSua escolha: '))

if base < 1 or base > 3:
    print('Apenas escolhas 1, 2 e 3!')
else:
    if base == 1:
        print(f'O numero {numero} em Binário é {bin(numero)[2:]}')
    elif base == 2:
        print(f'O numero {numero} em Octal é {oct(numero)[2:]}')
    else:
        print(f'O numero {numero} em Hexadecimal é {hex(numero)[2:]}')

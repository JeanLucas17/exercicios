r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triangulo!')
    if r1 == r2 == r3:
        print('Esse triangulo é Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Esse triangulo é Isóceles!')
    else:
        print('Esse triangulo é Escaleno!')
else:
    print('Não pode formar um triangulo!')

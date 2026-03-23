from math import sqrt, pow

num = int(input('Digite um numero: '))
print(f'''
O dobro de {num} é {pow(num, 2):.0f}
O triplo de {num} é {pow(num, 3):.0f}
A raiz quadrada de {num} é {sqrt(num):.2f}
''')

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você esta abaixo do Peso!')
elif imc < 25:
    print('Você esta com Peso ideal!')
elif imc < 30:
    print('Você esta acima do Peso!') 
elif imc < 40:
    print('Você esta Obeso(a)!')
else:
    print('Você esta em estado de Obesidade mórbida!') 
print(f'Com um imc de {imc:.2f}')

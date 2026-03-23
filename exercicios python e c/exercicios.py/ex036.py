valor_casa = float(input('Qual o valor da casa:\nR$ '))
salario = float(input('Digite seu salario:\nR$ '))
ano = int(input('Em quantos anos você irá pagar?\n'))
salario_maximo = salario * 0.30
prestacao = valor_casa / (ano * 12)

print(f'Prestação: R$ {prestacao:.2f}')
print(f'Limite permitido: R$ {salario_maximo:.2f}')

if prestacao <= salario_maximo:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo reprovado!')

saque = float(input('Digite quantos R$ voê quer sacar: R$ '))

nota50 = saque // 50
resto = saque % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota1 = resto

print(f'''
Para sacar {saque} você irá receber:
{nota50:.0f} notas de 50
{nota20:.0f}  notas de 20
{nota10:.0f}  notas de 10
{nota1:.0f}  notas de 1
''')

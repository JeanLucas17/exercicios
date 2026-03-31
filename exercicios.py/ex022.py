nome = input('Digite seu nome: ')
split_nome = nome.split()
print(f'''
{nome.upper()}
{nome.lower()}
{len(nome.replace(' ', ''))}
{len(split_nome[0])}
''')

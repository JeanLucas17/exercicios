preco = float(input('Digite o valor do produto: R$ '))
escolha = int(input('''
Escolha a opção de pagamento:
    1 - A vista dinheiro / cheque 
    2 - A vista no cartão
    3 - 2 vezes no cartão
    4 - 3 vezes ou mais no cartão
Sua escolha: '''))

if escolha == 1:
    print(f'A vista no dinheiro / cheque o preço do produto de R$ {preco} fica R$ {preco - (preco * 0.10):.2f}')

elif escolha == 2:
    print(f'A vista no cartão o preço do produto de R$ {preco:.2f} fica R$ {preco - (preco * 0.05):.2f}')

elif escolha == 3:
    parcelas = preco / 2
    print(f'Em 2 vezes no cartão o preço fica R$ {parcelas:.2f} por mês sem desconto! O total é de R$ {preco:.2f}')

elif escolha == 4:
    meses = int(input('Digite em quantas vezes você ira pagar: '))
    if meses < 3:
        print('A opção 4 só permite a partir de 3 vezes no cartão!')
    else:  
        preco_juros = preco + (preco * 0.2)
        prestacao = preco_juros / meses
        print(f'Em {meses} vezes no cartão ira ficar R$ {prestacao:.2f} por mês! O total é de R$ {preco_juros:.2f}')
else:
    print('Apenas as opções 1, 2, 3 e 4!')

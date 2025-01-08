#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
#condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto: R$ '))
forma_pagamento = input('Informe a forma de pagamento (dinheiro/cheque, cartão à vista, 2x no cartão, 3x ou mais no cartão): ').strip().lower()

if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
    preco_final = preco * 0.90
    print(f'O valor a ser pago será R$ {preco_final:.2f} com 10% de desconto.')
elif forma_pagamento == 'cartão à vista':
    preco_final = preco * 0.95
    print(f'O valor a ser pago será R$ {preco_final:.2f} com 5% de desconto.')
elif forma_pagamento == '2x no cartão':
    preco_final = preco
    print(f'O valor a ser pago será R$ {preco_final:.2f} em 2x no cartão (sem desconto).')
elif forma_pagamento == '3x ou mais no cartão':
    preco_final = preco * 1.20
    print(f'O valor a ser pago será R$ {preco_final:.2f} com 20% de juros.')
else:
    print('Forma de pagamento inválida.')

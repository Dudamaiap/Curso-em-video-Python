# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por km para viagens
# de até 200Km e 0,45 para viagens mais longas
distancia = (int(input('Qual a distância da viagem em Km?')))
if distancia <= 200:
    preco=distancia*0,50
    print(f'O valor da viagem é R${preco:.2f}')
else:
    preco=distancia*0,45
    print(f'O preço da viagem é R${preco:.2f}')



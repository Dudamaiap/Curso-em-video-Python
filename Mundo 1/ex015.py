#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km foram rodados? '))
dias = int(input('Quantos dias ele foi alugado? '))
preco= (0.15*km)+(dias*60)
print(f'O carro foi alugado por {dias} dias e rodou {km} Km. Seu preço final foi R$ {preco}')
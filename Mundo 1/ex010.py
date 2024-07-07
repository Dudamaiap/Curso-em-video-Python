#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar US$1.00=R$3.27

real=float(input('Quantos reais você tem na carteira?'))
dolar=real/3.27
print(f'Você pode comprar {dolar:.3} dolares')
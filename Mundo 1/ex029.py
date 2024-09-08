#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

velocidade = (int(input('Insira a velocidade do carro: ')))
if (velocidade > 80):
    print ('Você foi multado!')
    multa = ((velocidade/10)*7)
    print(f'O valor da multa é {multa}')
else:
    print('Você não ultrapassou o limite de velocidade. Parabéns')

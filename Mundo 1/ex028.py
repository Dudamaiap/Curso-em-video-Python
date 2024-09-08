#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

numero=47

entrada=int(input('Escolha um número: '))
if entrada == numero:
    print('Você escolheu o numero certo!!')
else:
    print('Você errou tente de novo!')
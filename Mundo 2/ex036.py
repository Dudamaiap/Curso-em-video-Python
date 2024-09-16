#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o impréstimo será negado

valorcasa= float(input('Qual o valor da casa?'))
salario= float(input('Qual o seu salário?'))
prazo= int(input('Em quantos anos você vai pagar?'))

prestacao= valorcasa/(prazo*12)
limite= salario * 0.30

print(f"Para pagar uma casa de R$ {valorcasa:.2f} em {prazo} anos, a prestação será de R$ {prestacao:.2f}.")
if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")
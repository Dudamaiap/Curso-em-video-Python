#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario= float(input('Informe o seu salário: '))
salariofinal=salario+(salario*15/100)
print(f'O seu salário com o aumento de 15% fica R${salariofinal:.2f}')
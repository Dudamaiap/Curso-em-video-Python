#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
#mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

peso = float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a sua altura (m): '))

imc = peso / (altura ** 2)

print(f'O seu IMC é {imc:.2f}.')

if imc < 18.5:
    print('Status: Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Status: Peso Ideal')
elif 25 <= imc < 30:
    print('Status: Sobrepeso')
elif 30 <= imc < 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade Mórbida')

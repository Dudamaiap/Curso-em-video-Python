# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minúsculas
# Quantas letras ao total
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome..')

print(f'Seu nome em maiusculas é {nome.upper()}')

print(f'Seu nome em minúsculas é {nome.lower()}')

total_letras = len(nome.replace(' ', ''))
print(f'Seu nome tem ao todo {total_letras} letras')


primeiro_nome = nome.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {letras_primeiro_nome} letras')




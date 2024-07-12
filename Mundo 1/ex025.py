# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Qual é o seu nome completo? ')).strip()

nome = nome.upper()

silva = 'SILVA' in nome

print(f'Seu nome tem Silva? {silva}')
# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Informe o número: '))

print(f'Analisando o número {num}')

u = num // 1 % 10
print(f'Unidade: {u}')

d = num // 10 % 10
print(f'Dezena: {d}')

c = num // 100 % 10
print(f'Centena: {c}')

m = num // 1000 % 10
print(f'Milhar: {m}')
# Faça um programa que leia algo e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

entrada=input('Digite algo:')
print('O tipo primitivo desse valor é', type(entrada))
print('Só tem espaços?', entrada.isspace())
print('É um número?', entrada.isnumeric())
print('É alfabetico?', entrada.isalpha())
print('É alfanumérico?', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em miúsculas?', entrada.islower())
print('Está capitalizada?', entrada.istitle())


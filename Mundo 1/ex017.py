# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# o comprimento da hipotenusa

from math import hypot
catoposto = float(input('Insira o comprimento do cateto oposto: '))
catadjacente = float(input('Insira o tamanho do cateto adjacente: '))
hipotenusa = hypot(catoposto,catadjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2}')
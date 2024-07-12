# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Insira o valor de um ângulo qualquer: '))

radiano = math.radians(angulo)

seno = math.sin(radiano)
coss = math.cos(radiano)
tang = math.tan(radiano)

print(f'O seno é {seno:.2f}, cosseno{coss:.2f} e a tangente {tang:.2f}')
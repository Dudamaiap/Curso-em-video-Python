# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necesária para pinta-la,
#sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura*altura
tinta = area/2
print(f'Para pintar parede você precisa de {tinta:.2f} litros de tinta')

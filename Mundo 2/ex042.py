lado1 = float(input('Informe o comprimento do primeiro lado: '))
lado2 = float(input('Informe o comprimento do segundo lado: '))
lado3 = float(input('Informe o comprimento do terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('As retas podem formar um triângulo.')

if lado1 == lado2 == lado3:
        print('O triângulo é EQUILÁTERO.')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é ISÓSCELES.')
else:
        print('O triângulo é ESCALENO.')
else:
    print('As retas NÃO podem formar um triângulo.')

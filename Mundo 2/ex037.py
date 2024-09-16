#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1- para binario 2- para octal 3- para hexadecimal

numero = int(input('Digite um número inteiro: '))

print('''Escolha uma base para conversão: 
 [1] Binário 
 [2] Octal 
 [3] Hexadecimal ''')

opcao=int(input('Sua opção: '))

if opcao==1:
    print(f'{numero} convertido para binário é {bin(numero)[2:]}')
elif opcao==2:
    print(f'{numero} convertido para octal é {oct(numero)[2:]}')
elif opcao==3:
    print(f'{numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida')
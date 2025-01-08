nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Você está reprovado!')
elif media >= 5 and media < 7:
    print('Você está de recuperação')
elif media >= 7:
    print('Você está aprovado')

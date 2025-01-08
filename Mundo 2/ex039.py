#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo

nascimento= int(input('Em que ano você nasceu? '))
ano_atual = 2025
idade = ano_atual - nascimento

if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda vai se alistar. Faltam {tempo} anos.")
elif idade == 18:
    print("É hora de se alistar!")
else:
    tempo = idade - 18
    print(f"Você já passou do tempo de alistamento. Passaram-se {tempo} anos.")

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de dedsconto
produto=float(input('Qual o preço do produto? R$'))
desconto =produto*0.05
produto_final=produto-desconto
print(f'O novo preço do produto com o desconto é R${produto_final:.2f} ')

#Faça um algoritmo que leia o preço, de um produto e mostre seu novo preço, com 5% de desconto.

preco= float(input("Qual o preço do produto? R$"))
descont= preco * 5 / 100
novop= descont - preco
print(f"O produto do valor R$ {preco} vai ganhar 5% desconto no total de R${descont}, o novo valor do produto será R${novop}")


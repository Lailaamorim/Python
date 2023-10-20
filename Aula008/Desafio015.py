#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos 
#quais ele foi alugado e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km=float(input("Escreva a quantidade de quilometro percorridos pelo carro: "))
dias= int(input("Informe por quantos dias ele foi alugado: "))
pago = (dias * 60 ) + (km *0.15)
print(f"o valor do aluguel do carro será R${pago}")
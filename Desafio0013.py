#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario= float(input("Digite o salario do funcionario:"))
aumento= salario * 15 / 100
valorno = aumento + salario

print(f"O Salario do funcionario no valor de R$ {salario} vai ganhar o aumento de 15% no valor de R$  {aumento}, ficando com o novo salario no valor de {valorno}")
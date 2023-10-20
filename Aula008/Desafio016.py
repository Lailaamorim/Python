#Crie um programa que leia ume número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#EX: 
#Digite um número:6.127
#O número 6.127 tem a parte Inteira 6.

#import math
#num= float(input("Digite um valor: "))
#print("O valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num)))

from math import trunc
num= float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num,trunc(num)))

num= float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num,int(num)))
#Um professor que sortear um dos  seus quatro alunos para apagar o quatro. faça um programa que ajude a ele, 
#lendo o nome dos alunols e escrevendo o nome do escolhido
import random
n1 = input("Primeiro Aluno: ")
n2 = input("Segundo Aluno: ")
n3 = input("Terceiro Aluno: ")
n4 = input("Quarto Aluno: ")

lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)
print(f"O aluno escolhido foi:{escolhido}")

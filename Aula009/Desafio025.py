#Crie um programa que leia o nome de umaa pessoa e diga se ela tem "Silva" no nome
nome =str(input("Qual é o seu nome completo: ")).strip()

print("Seu nome tem silva? {}".format("SILVA" in nome.upper()))
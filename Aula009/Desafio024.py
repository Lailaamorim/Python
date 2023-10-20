#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cid = str(input("Em que cidade você nasceu? ")).strip()# O strip elimina os espaços da frente e de tras
print(cid[:5].upper() == "SANTO")
 # O [:5] para pegar as primeiras 5 letras / .upper passa tudo para Maiúsculo


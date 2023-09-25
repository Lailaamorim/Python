# Faça um programa que leia a largura e a altura e a altura de uma parede em metros, calcule a sua área e a quatidade
#de tinta necessaria para pintá-la, sabendo que cada litro e tinta, pinta uma area de 2m.
largura= int(input("Largura da parede: "))
altura= int(input("Altura da parede: "))

area= largura*altura

print(f"A sua parede tem a dimensão de {largura} X {altura} e sua area {area} m²")

tinta = area/2

print(f"Para pintar essa parede, você precisará de {tinta} L de tinta ")
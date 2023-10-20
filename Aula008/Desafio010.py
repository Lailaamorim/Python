# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere 
# U$$1,00= R$3,27

Real = float(input("Quanto de dinheiro vc tem na carteira? R$"))
dolar = Real / 4.93
euro = Real / 5,27
ienes = Real / 4,18

print(f"Com R${Real} você pode comprar US$ {dolar}")
print(f"Com R${Real} você pode comprar EUR {euro}")
print(f"Com R${Real} você pode comprar ienes {ienes}")
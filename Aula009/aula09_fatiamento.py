#Fatiamento

frase = "Curso em Video Python"
 # C U R S O   E M   V  I  D  E  O     P   Y   T   H   O   N
 # 0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15  16  17  18  19 20
print(frase[3])#pega a tetra que está na posição 3
print(frase[3:13]) #vai da letra que está no três, até a que esta no número 13
print(frase.count("o"))#conta quantas vezes aparece a letra que está entre parenteses
print(frase.count("o",0,13))# quantas letras "o" tem de zero a treze
print(frase.find("deo"))# Ele vai dizer em que momento na frase começou a palavra deo, nesse caso no posição 11
print("Curso" in frase)# verá se tem a palavra curso na frase e se sim dirá que é verdade]
print(frase.replace("Python", "Andromeda"))#Substiruie a palavra antiga pçela palavra nova
print(frase.upper())# transforma as letras minusculas em maiusculas
print(frase.lower())# transforma as letras mauisculas em minusculas
print(frase.capitalize())# ele tranforma todas as letras maiscusculas em menusculas menos as iniciais 
print(frase.title())# Vai analizar quantas palavras tem na frase e mudar para maicusla a inicial de cada uma delas.
print(frase.strip())#Ele irá remover todos os espaços inúteis no início e no final da string
print(frase.rstrip())#Remove o espaço só no lado direito
print(frase.lstrip())#Remove espaço só no lado esquerdo
print("_".join(frase))#Coloca um espaço ou um traço em cada palavra                                                                        
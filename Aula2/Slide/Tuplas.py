#tuplas:
#          0         1         2        3
nomes = ("Goku", "Vegeta", "Trunks", "Gohan")
print(nomes)        #todos os nomes
print(nomes[0])     #nome no indice 0
print(nomes[3])     #nome no indice 3
print(nomes[-1])    #primeiro nome de traz pra frente
print(nomes[-2])    #segundo nome de traz pra frente
print(len(nomes))   #numero de nomes
print(nomes[1:3])   #nomes iniciando no indice 1(inclusive) e indo até o indice 3(exclusive)
print(nomes[:2])    #nomes do inicio até o indice final (exclusive)
print(nomes[2:])    #nomes do incidice incial até o final da tupla

#não é possível alterar, nem deletar e nem adicionar valores de uma tupla --> IMUTAVEL

for nome in nomes:   #mostrar os nomes
    print(nome)

for cont in range(0, len(nomes)):
    print(f"Nome {cont}: {nomes[cont]}")

print(sorted(nomes)) #ordem alfabética

#tuplas aceitam elementos de diferentes tipos
personagem = ("Goku", 37, "Sayajin", 85.5)

print(personagem)
print(len(personagem))

x = (2,6,8)
y = (5,6,9,1)
z = x + y
print(z)
print(z.count(6))
print(z.index(6))
print(max(z), min(z))

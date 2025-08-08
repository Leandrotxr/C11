#listas:
#          0         1         2        3
nomes = ["Goku", "Vegeta", "Trunks", "Gohan"]        #todos os nomes

#adicionando elementos
nomes.append("Bulma")   #insere o nome no elemento final da lista
nomes.insert(1, "Kuririn")      #coloca o nome no indice indicado e o que estava no indice vai para o proximo
print(nomes)

#alterando elementos
nomes[0] = "Picolo"
print(nomes)

#exculindo
del nomes[0] #exclui o que esta no indice 0
nomes.remove("Gohan")
print(nomes)

if "Goku" in nomes:
    nomes.remove("Goku")
    print("Elemento removido")
else:
    print("Elemento não existe")


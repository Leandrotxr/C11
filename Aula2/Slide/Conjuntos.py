#conjuntos (set):
#é uma coleção NÃO ORDENADA e que NÃO ADMITE ELEMENTOS DUPLICADOS

nomes = {"Goku", "Vegeta", "Trunks", "Gohan","Goku"}        #todos os nomes
print(nomes) #Goku aparece apenas uma vez

#adicionando elementos
nomes.add("Bulma")   #insere o nome no elemento final da lista
nomes.add("Goku")
print(nomes)         #não vai mostrar o segundo add pois goku ja existe

#exculindo
nomes.remove("Gohan")
print(nomes)

#como conjuntos são aleatórios, não conseguimos manipular com indices:
sorted(nomes) #ordena e retorna no tipo lista
print(type(nomes))

#Dicionarios:
#key : value

dados = {
    "nome" : "Goku",
    "idade" : 43
}
print(dados)

#adicionando key:value
dados["sexo"] = "Masculino"
dados["filhos"] = ["Gohan", "Goten"]       #adicionando uma lista em um dicionario
print(dados)

#alterando key:value
dados["idade"] = 45
print(dados)

#removendo key:values
del dados["idade"]
print(dados)

#acessando um elemento na lista dentro do dicionario
print(dados["filhos"][1]) #mostra o elemento 1 da lista de filhos
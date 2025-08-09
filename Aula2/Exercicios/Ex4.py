pessoas = []

for i in range(3):
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso: "))
    pessoa = {"Nome": nome, "Peso": peso}
    pessoas.append(pessoa)

print("Pessoa mais pesada:", max(pessoas, key=lambda x: x["Peso"]))
print("Pessoa mais leve:", min(pessoas, key=lambda x: x["Peso"]))

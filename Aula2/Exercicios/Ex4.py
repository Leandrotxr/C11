pessoas = []

for i in range(3):
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso: "))
    pessoa = {"Nome": nome, "Peso": peso}
    pessoas.append(pessoa)

maisPesada = pessoas[0]
maisLeve = pessoas[0]

for pessoa in pessoas:
    if pessoa["Peso"] > maisPesada["Peso"]:
        maisPesada = pessoa
    if pessoa["Peso"] < maisLeve["Peso"]:
        maisLeve = pessoa

print("Pessoa mais pesada:", maisPesada["Nome"])
print("Pessoa mais leve:", maisLeve["Nome"])
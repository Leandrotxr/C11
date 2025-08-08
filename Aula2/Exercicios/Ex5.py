pessoas = []

mulheresMenores = 0
somaIdade = 0

variavelTeste = True

while variavelTeste:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    somaIdade += idade
    while True:
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        if sexo == "M":
            break
        elif sexo == "F":
            if idade < 20:
                mulheresMenores += 1
            break
        else:
            print("Entrada inválida. Tente novamente.")

    pessoa = {"Nome": nome, "Idade": idade, "Sexo": sexo}
    pessoas.append(pessoa)

    while True:
        opcao = input("Deseja cadastrar novas pessoas? [S/N]").strip().upper()
        if opcao == "N":
            variavelTeste = False
            break
        elif opcao == "S":
            break
        else:
            print("Entrada invalida. Tente novamente.")

media = somaIdade / len(pessoas)
print("Média das idades:",media)
print("Número de mulheres com menos de 20 anos:",mulheresMenores)

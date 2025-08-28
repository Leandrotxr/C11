while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo == "M":
        print("Sexo masculino.")
        break
    elif sexo == "F":
        print("Sexo feminino.")
        break
    else:
        print("Entrada inválida. Tente novamente.")
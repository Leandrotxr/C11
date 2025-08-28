aluno = {}
aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Media"] = float(input("Digite o valor da média: "))

if aluno["Media"] >= 50:
    aluno["Situação final"] = "AP"
else:
    aluno["Situação final"] = "RP"

print(aluno)
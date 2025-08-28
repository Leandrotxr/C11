numero = int(input("Digite o número que deseja saber a tabuada: "))
inicio = int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))

if fim < inicio:
    varteste = inicio
    inicio = fim
    fim = varteste

for i in range(inicio, fim + 1, 1):
    print(numero, "x", i, "=", numero * i)
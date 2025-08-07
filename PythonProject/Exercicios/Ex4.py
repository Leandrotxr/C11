distancia = float(input("Qual a distância da viagem: "))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print("Valor da viagem: R$", f"{valor:.2f}")
while True:
    numero = int(input("Digite um número: "))

    if  1000 <= numero <= 9999:
        break

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)
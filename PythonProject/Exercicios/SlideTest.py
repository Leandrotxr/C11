import math

print("Hello World")                  #texto
print(7+7)                            #operação matemática
print("O resultado de 7 + 7 é:",7+7)  #texto + operação matemática

nome  = "Leandro"        #string
idade = 21               #int
peso = 66.5              #float
print(nome,idade,peso)

nome = input("Qual o seu nome?")
idade = int(input("Qual a sua idade?"))
peso = float(input("Qual o seu peso?"))
print("Seu nome é {}, sua idade é {} e seu peso é {}".format(nome,idade,peso))

print(type(nome))
print(type(idade))
print(type(peso))

num = 2.5
print(math.trunc(num)) #inteiro


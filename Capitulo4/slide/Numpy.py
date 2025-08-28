import numpy as np


#array unidimensional (apenas elementos do mesmo tipo)
arr = np.array([1, 2, 3])
print(arr)
arr = np.array([1, 2, 3, "teste"]) #transforma tudo em string
print(arr)

#array bidimensional (matriz --> lista de listas)
mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtz)

#necessário declarar as variasveis
n = 2  #tamanho dos arrays que criarei
f = 1; l = 5; s = 1

#array uni ou bidimensional formado por 0's
arr0 = np.zeros(n)
print(arr0)
mtz0 = np.zeros([n,n])
print(mtz0)

#array uni ou bidimensional formado por 1's
arr1 = np.ones(n)
print(arr1)
mtz1 = np.ones([n,n])
print(mtz1)

#array 2D de 0's (transformando array unidimensional para bidimensional)
mtz2 = np.zeros(10).reshape(5,2) #array --> matriz 1:10 --> matriz 5:2
print(mtz2)
print(mtz2.size)         #num de elementos
print(mtz2.ndim)         #num de dimensões
print(mtz2.shape)        #tupla com o tamanho de cada dimensao

#array UNIDIMENSIONAL formado por elementos espaçados
arr2 = np.arange(n)
print(arr2)

#(f-first element, l-last element, s-step)
arr3 = np.arange(f,l,s)
print(arr3)

arr4 = np.arange(10,101,10)
print(arr4)
#maior
print(arr4.max())
print(arr4.argmax()) #indice do maior
#menor
print(arr4.min())
print(arr4.argmin()) #indice do menor
#soma
print(arr4.sum())

#operações com pyarrays

arr5 = np.arange(1,10,1)
arr6 = np.arange(9,0,-1)

print(arr5)
print(arr6)
print(arr5 + arr6)   #soma cada indice
print(arr5 - arr6)   #subtrai cada indice
print(arr5 * arr6)   #multiplica cada indice

print(np.concatenate((arr5, arr6))) #concatenado os arrays (mostra um array e dps o outro)

arr7 = np.arange(1,11,1).reshape(5,2)
print(arr7)
print(arr7.sum(axis=0))  #tupla com a soma de cada coluna
print(arr7.sum(axis=1))  #tupla com a soma de cada linha

#numeros aleatórios
arr8 = np.random.randint(1,11,10)
print(arr8)
mtz3 = np.random.randint(1,101,[5,2])
print(mtz3)

#numeros unicos
print(np.unique(arr8))
print(np.unique(arr8, return_counts=True))
print(np.unique(mtz3))
print(np.unique(mtz3, return_counts=True))

#Fatiamento de numpy arrays e condicionais
mtz = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(mtz[2])   #mostrando apenas a linha 2
print(mtz[0:2]) #mostra linha 0 até a 2 (exclusive)

print(mtz[:,1]) #mostra a coluna 1
print(mtz[0:2,1:]) #mostra a coluna 0 até a 2 (exclusive) e a linha 1 até o final

print(mtz > 5) #mostra uma matriz comparando elemento por elemento, se a condição for satisfeita retorna true
print(mtz[mtz > 5]) #mostra os elementos que são true no ex acima

cond = mtz % 2 == 0 #testa se é par
print(mtz[cond])

arr = np.array(["python", "numpy","panda","data","pypy"])
sub = "py"
print(np.char.find(arr, sub)) #verifica se no array possui a sub, retorna a posição caso tenha e -1 caso não tenha

print(np.char.startswith(arr, sub)) #retorna true para elementos do array que começa com a sub

print(np.char.upper(arr)) #retorna o array inteiro em letras maiusculas

print(np.char.count(arr, sub)) #retorna o numero d vezes que a sub aparece em cada elemento

print(np.char.isalpha(arr)) #retorna true se no texto tiver apenas letras


#salvando e carregando dados  com numpy
#carregando arquivo de texto normal ou .csv
dataset = np.loadtxt('arquivo.txt')
print(dataset)
np.savetxt('arquivo.txt', dataset) #salvando o arquivo

#carregando um arquivo binario numpy(.npy)
dataset2 = np.load('arquivo.npy')
print(dataset2)
np.save('arquivo.npy') #salvando o arquivo

#Dataset space.csv
dataset3 = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')
print(dataset3)
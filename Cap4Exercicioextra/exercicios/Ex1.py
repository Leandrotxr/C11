import numpy as np

dataset = np.loadtxt('../data/paises.csv', delimiter=';', dtype=str, encoding = 'utf-8')
dataset = np.char.strip(dataset)

header = np.char.strip(dataset[0])
dados = dataset[1:]

datasetResumido = dataset[1:,0:4]
print(datasetResumido)
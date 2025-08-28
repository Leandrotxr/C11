import numpy as np

dataset = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')

header = dataset[0]
dados = dataset[1:]

col_Local = np.where(header == "Location")[0][0]

locais = dados[:,col_Local]
qtdUSA = np.sum(np.char.find(locais,"USA") >= 0)
print("Quantidade de missões realizadas pelos USA:",qtdUSA)
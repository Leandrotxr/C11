import numpy as np

dataset = np.loadtxt('../data/paises.csv', delimiter=';', dtype=str, encoding = 'utf-8')
dataset = np.char.strip(dataset)

header = np.char.strip(dataset[0])
dados = dataset[1:]

col_regiao = np.where(header == "Region")[0][0]

regioes = dados[:, col_regiao]
regioes_unicas = np.unique(regioes)
print("Regiões únicas encontradas:",regioes_unicas)
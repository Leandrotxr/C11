import numpy as np

dataset = np.loadtxt('../data/paises.csv', delimiter=';', dtype=str, encoding = 'utf-8')
dataset = np.char.strip(dataset)

header = np.char.strip(dataset[0])
dados = dataset[1:]
header[0] = header[0].replace("\ufeff", "")

col_pais = np.where(header == "Country")[0][0]
col_regiao = np.where(header == "Region")[0][0]

norte = dados[dados[:, col_regiao] == "NORTHERN AMERICA"]
print("Quantidade de países na América do Norte:",len(norte))
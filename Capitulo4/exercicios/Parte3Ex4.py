import numpy as np

dataset = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')

header = dataset[0]
dados = dataset[1:]

col_empresa = np.where(header == "Company Name")[0][0]
col_custo = np.where(header == " Cost")[0][0]

spacex = dados[dados[:,col_empresa] == "SpaceX"]
custosSpacex = np.where(spacex[:,col_custo] == "", "0", spacex[:,col_custo]).astype(float)

custoMax = np.argmax(custosSpacex)
missaoMaisCara = spacex[custoMax]
print(missaoMaisCara)
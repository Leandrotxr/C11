import numpy as np

dataset = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')

header = dataset[0]
dados = dataset[1:]

col_custo   = np.where(header == " Cost")[0][0]

custos = dados[:,col_custo]
custos = np.where(custos == "", "0", custos)
custos = custos.astype(float)
custosValidos = custos[custos != 0]

media = np.mean(custosValidos)
print("Custo médio de missões com dados:",media)
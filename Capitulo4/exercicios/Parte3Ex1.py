import numpy as np

dataset = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')

header = dataset[0]
dados = dataset[1:]

col_status = np.where(header == "Status Mission")[0][0]

total = len(dados)
sucesso = np.sum(dados[:,col_status] == "Success")
pct = (sucesso/total)*100
print("Porcentagem de missões bem sucedidas:",pct)
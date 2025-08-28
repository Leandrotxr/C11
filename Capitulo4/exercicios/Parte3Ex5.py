import numpy as np

dataset = np.loadtxt('../data/space.csv', delimiter=';', dtype=str, encoding = 'utf-8')

header = dataset[0]
dados = dataset[1:]

col_empresa = np.where(header == "Company Name")[0][0]
col_status  = np.where(header == "Status Mission")[0][0]

empresas = {}

for linha in dados:
    empresa = linha[col_empresa]
    status = linha[col_status]
    if status == "Success":
        empresas[empresa] = empresas.get(empresa, 0) + 1

for empresa, qtd in empresas.items():
    print(f"{empresa}: {qtd} missões bem-sucedidas")
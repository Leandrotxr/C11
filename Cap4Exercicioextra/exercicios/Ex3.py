import numpy as np

dataset = np.loadtxt('../data/paises.csv', delimiter=';', dtype=str, encoding = 'utf-8')
dataset = np.char.strip(dataset)

header = np.char.strip(dataset[0])
dados = dataset[1:]

col_literacy = np.where(header == "Literacy (%)")[0][0]

literacy = dados[:, col_literacy]
literacy_col = np.char.replace(literacy, "N/A", "nan")
literacy_col = literacy_col.astype(float)

media_literacy = np.nanmean(literacy_col)
print("Media de alfabetização mundial:", media_literacy)

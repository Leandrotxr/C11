import numpy as np

dataset = np.loadtxt('../data/paises.csv', delimiter=';', dtype=str, encoding = 'utf-8')
dataset = np.char.strip(dataset)

header = np.char.strip(dataset[0])
dados = dataset[1:]
header[0] = header[0].replace("\ufeff", "")

col_pais = np.where(header == "Country")[0][0]
col_regiao = np.where(header == "Region")[0][0]
col_gdp = np.where(header == "GDP ($ per capita)")[0][0]

lat_carib = dados[dados[:, col_regiao] == "LATIN AMER. & CARIB"]

gdp_col = np.char.replace(lat_carib[:, col_gdp], "N/A", "nan").astype(float)

idx_max = np.nanargmax(gdp_col)
pais_max_gdp = lat_carib[idx_max, col_pais]
gdp_max = gdp_col[idx_max]

print("País com maior GDP na América do Sul/Caribe:",pais_max_gdp,"(",gdp_max,")")
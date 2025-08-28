import numpy as np

np.random.seed(10)

mtz = np.random.randint(1,51,[4,4])
print(mtz)

media_linhas = np.mean(mtz, axis=1)
print("Média de cada linha:",media_linhas)
media_colunas = np.mean(mtz, axis=0)
print("Média de cada coluna:",media_colunas)

print("Maior média das linhas:", np.max(media_linhas))
print("Maior média das colunas:", np.max(media_colunas))

print(np.unique(mtz, return_counts=True))

valores, repeticoes = np.unique(mtz, return_counts=True)

print("Valores que repetem 2+ vezes:",valores[repeticoes >= 2])
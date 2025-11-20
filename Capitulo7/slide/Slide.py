import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Carregando o dataset do Índice de Volume de Vendas no Setor Varejista Brasileiro
dataset = pd.read_csv('../data/retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# Transformando os dados de y em float
dataset['retail_index'].astype(float)

# Plotando a Time Series
dataset['retail_index'].plot(figsize=(8, 6),
title='Índice de volume de vendas no setor varejista brasileiro',
xlabel='Data', ylabel='Índice', x_compat=True)
plt.show()

df = pd.read_csv('../data/retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)
# criando um modelo de previsão
model = ExponentialSmoothing(endog=df.retail_index, trend = 'add',
                             seasonal = 'add', seasonal_periods=12).fit()

# realizando a previsão
# limitando o gráfico para facilitar a visualização
# prevendo 3 anos
predictions = model.forecast(steps = 36)
df['retail_index']['2015-01-01':].plot(figsize= (8, 6))
predictions.plot()
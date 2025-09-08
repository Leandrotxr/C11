import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index = ['A','B','C','D','E'], #linhas
    columns = ['W','X','Y','Z'], #colunas
    data = np.random.randint(1,50,[5,4])
)
#questão 6
print("\nMédia dos elementos de X menores de 30:",df[df['X'] < 30]['X'].mean())

#questão 7
mediaD = df.loc['D'].mean()
print("\nMédia da linha D:",mediaD)
somaE = df.iloc[4,:].sum()
print("Soma da linha E:",somaE)

#questão 8
slicing = df.loc[['A','C','E'],['X','Y']]
print("\nSlicing:")
print(slicing)
print("\nSoma das linhas:")
print(slicing.sum(axis=1))
print("\nSoma das colunas:")
print(slicing.sum(axis=0))
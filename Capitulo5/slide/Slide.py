import pandas as pd
import numpy as np

indices = ['a','b','c']
valores = [1,2,3]
dic = {'a':10,'b':20,'c':30} #funciona como um dicionario
dic2 = {'a':10,'b':20,'d':40}

#criando e mostrando uma series
#series = pd.Series(valores)
series = pd.Series(dic)
print(series)
print(type(series))
print(series['a'])

series2 = pd.Series(dic2)
print(series2)

#operações entre series

print(series + series2)  #não faz nada quando não possuem a mesma label (c e d no exemplo)
print(series - series2)

print(series.add(series2, fill_value=0)) #este metodo faz com a operação COM O VALOR PADRÃO
print(series.sub(series2, fill_value=100)) #o modo seta um valor onde não possui

#condicionais no pandas
print(series < 20)  #retorna true ou false
print(series[series < 20])  #retorna os elementos

np.random.seed(10)

df = pd.DataFrame(
    index = ['A','B','C','D','E'], #linhas
    columns = ['W','X','Y','Z'], #colunas
    data = np.random.randint(1,50,[5,4])
)
print(df)

df2 = pd.DataFrame({'a':[1,2,3],'b':[4,5,6]}) #'a' é a coluna e os valores dela
print(df2)

#fazendo slicing com iloc (padrão numpy)
print(df.iloc[0:2,:])

#fazendo slicing com loc (padrão numpy)
print(df.loc[['A','B'],['W','X','Y','Z']]) #bom quando precio de colunas que não estão lado a lado
print(df.loc[['A','B'],['W','Z']])
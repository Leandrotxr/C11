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

dfpaises = pd.read_csv('../data/paises.csv', delimiter=';')
print(dfpaises.columns) #mostrando apenas  as colunas
print(dfpaises.head(2)) #mostrando apenas os dois primeiros
print(dfpaises.tail(2)) #mostrando apenas os dois ultimos

#criando uma nova coluna no dataset
totalPopulation = np.sum(dfpaises['Population'])
seriesPercPopulation = (dfpaises['Population'] / totalPopulation) * 100
dfpaises['PopulationPercent'] = np.round(seriesPercPopulation, 3)
dfpaises.to_csv('../data/paises_v2.csv', sep = ';')
#dfpaises.drop('Region', axis=1) #usada para deletar uma coluna

dfpaises2 = pd.read_csv('../data/paises_v2.csv', sep = ';') #lendo o novo dataset
print(dfpaises2)

#agrupando
groupRegion = dfpaises2.groupby('Region')
print(groupRegion.count()['Country']) #contando quantos paises tenho por região
print(groupRegion.sum()['Country']) #contando quantos paises tenho por região
print(groupRegion.sum()['Population']) #soma da população de cada região
print(groupRegion.describe())

def tenpercent(x):
    return x * 0.9

deathrate1 = dfpaises['Deathrate']
print(deathrate1)

deathrate2 = dfpaises2['Deathrate'].apply(tenpercent)
print(deathrate2)

dfpaises3 = pd.concat([deathrate1, deathrate2],axis=1)
dfpaises3.columns = ["Taxa de mortalidade", "Taxa de mortalidade com desconto"] #mudando o nome das colunas
print(dfpaises3)

#dados ausente
novodf = dfpaises3.dropna() #remove linhas que possuam dados ausentes
novodf2 = dfpaises2.fillna(0) #preenche dados ausentes com o valor desejado
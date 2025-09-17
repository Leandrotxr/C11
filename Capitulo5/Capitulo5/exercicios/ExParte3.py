import pandas as pd

dfpaises = pd.read_csv('../data/paises.csv', delimiter=';')
dfpaises = dfpaises.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

#questão 1
oceania = dfpaises[dfpaises['Region'].str.contains("OCEANIA", case=False)]
print("Paises da Oceania:\n",oceania['Country'])
print("\nNúmero de paises na Oceania:",len(oceania))

#questão 2
maiorPopulation = dfpaises['Population'].idxmax()
print(f"País mais populoso: {dfpaises['Country'][maiorPopulation]} "f"(Região: {dfpaises['Region'][maiorPopulation]})")

#questão 3
groupregion = dfpaises.groupby('Region')['Literacy (%)'].mean()
print("\nMédia de alfabetização de cada região:\n",groupregion)

#questão 4
noCoast = dfpaises[dfpaises['Coastline (coast/area ratio)'] == 0]['Country']
noCoast.to_csv("../data/noCoast.csv", index=False)

#questão 5
def taxamortalidade(x):
    if x < 9:
        return "Balanced"
    else:
        return "Urgent"


dfpaises['Humanitarian Help'] = dfpaises['Deathrate'].apply(taxamortalidade)
print(dfpaises)
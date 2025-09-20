import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/space.csv', delimiter=';')
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

df["Country"] = df["Location"].apply(lambda x: str(x).split()[-1])
dfFiltrado = df[df["Country"].isin(["USA", "China"])]

uniqueCompanies = dfFiltrado.groupby("Country")["Company Name"].nunique()

countries = uniqueCompanies.index
values = uniqueCompanies.values

plt.bar(countries, values, color=["blue", "red"])
plt.ylabel("Número de Empresas Espaciais Únicas")
plt.title("Empresas Espaciais: EUA vs China")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('../data/paises.csv', delimiter=';')
dfpaises = dfPaises.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

americaNorte = dfpaises[dfpaises["Region"] == "NORTHERN AMERICA"]

plt.plot(americaNorte["Country"], americaNorte["Deathrate"],'o-g',americaNorte["Country"], americaNorte["Birthrate"],'o-b')
plt.show()
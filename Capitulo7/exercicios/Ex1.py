import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

air = pd.read_csv('../data/airtravel.csv', delimiter=',')
air = air.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

air['Date'] = pd.to_datetime(air['Date'])
air.set_index('Date', inplace=True)

air_series = air["Passengers"]

plt.figure(figsize=(10, 4))
plt.plot(air_series)
plt.title("AirTravel - Passageiros por Mês")
plt.xlabel("Ano")
plt.ylabel("Passageiros")
plt.show()

air_decomp = seasonal_decompose(air['Passengers'], model='additive', period=12)

air_decomp.plot()
plt.suptitle("Decomposição da Série AirTravel", fontsize=14)
plt.tight_layout()
plt.show()

# A) Sim. A tendência é crescente, pois a linha de tendência sobe continuamente ao longo dos anos.
# B) Sim. A série apresenta um padrão sazonal anual, repetindo-se a cada 12 meses.
# C) Sim. O ciclo aparece porque, além da sazonalidade anual, há flutuações de longo prazo
#         relacionadas ao aumento contínuo da demanda por viagens aéreas.

# ============================================================================

co2 = pd.read_csv('../data/co2_emissions.csv', delimiter=',')
co2 = co2.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

co2['Year'] = pd.to_datetime(co2['Year'], format='%Y')
co2.set_index('Year', inplace=True)

co2_series = co2["CO2_Emissions"]

plt.figure(figsize=(10, 4))
plt.plot(co2_series)
plt.title("CO2 Emissions - Série Anual")
plt.xlabel("Ano")
plt.ylabel("Emissões de CO2")
plt.show()

co2_decomp = seasonal_decompose(co2['CO2_Emissions'], model='additive', period=5)

co2_decomp.plot()
plt.suptitle("Decomposição da Série de CO2", fontsize=14)
plt.tight_layout()
plt.show()

# A) Sim. A tendência é decrescente, embora com pequenas oscilações ao longo dos anos,
#    a linha de tendência mostra queda do início da série até o final.
# B) Sim. A série apresenta um padrão sazonal a cada 7 anos aproximadamente.
# C) Sim. O ciclo ocorre porque, além da sazonalidade, há movimentos de médio e longo prazo associados
#    a fatores econômicos, políticas ambientais, crescimento ou redução da atividade industrial etc.
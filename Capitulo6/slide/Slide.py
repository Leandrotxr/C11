import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#x = np.array([1,2,3,4])
#y = x * 2
#y2 = x*x
#plt.xlabel("x")
#plt.ylabel("y")
#plt.plot(x,y,'*:r',x, y2,'s--g', linewidth=2, markersize=10)
#plt.show()

#plotando dois graficos separados
#plt.subplot(1,2,1) #1 linha; 2 coluna; posição 1
#plt.title("Linear")
#plt.plot(x,y,'r-')

#plt.subplot(1,2,2) #1 linha; 2 coluna; posição 2
#plt.title("Exponencial")
#plt.plot(x,y2,'b-')
#plt.show()


dfPaises = pd.read_csv('../data/paises.csv', delimiter=';')
dfpaises = dfPaises.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
dfPaises2 = dfPaises.nlargest(6,'Area (sq. mi.)')

#grafico de dispersão
plt.scatter(dfPaises2['Country'],dfPaises2['GDP ($ per capita)'],s=dfPaises2['Area (sq. mi.)']/10000)
plt.show()

dfBiggestGDP = dfPaises.nlargest(5,'GDP ($ per capita)')
dfBiggestGDP_Country = dfBiggestGDP['Country']
dfBiggestGDP_gdp = dfBiggestGDP['GDP ($ per capita)']

#grafico de barras
plt.bar(dfBiggestGDP_Country,dfBiggestGDP_gdp, color='blue')
plt.show()

dfpaisesNocoast = dfpaises[dfpaises['Coastline (coast/area ratio)'] == 0]
qtdPaisesNocoast = len(dfpaisesNocoast)
qtdPaisesCoast = len(dfPaises) - qtdPaisesNocoast

#grafico de pizza
plt.pie(x=[qtdPaisesCoast,qtdPaisesNocoast],labels = ['% Paises com Costa','% Paises sem Costa'], autopct = '%1.1f%%')
plt.show()
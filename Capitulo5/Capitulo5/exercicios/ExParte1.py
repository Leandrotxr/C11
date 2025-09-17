import pandas as pd

seriesAno1 = {'Java':16.25, 'C':16.04, 'Python':9.85}
seriesAno2 = {'C':16.21, 'Python':12.12, 'Java':11.68}

seriesAno1 = pd.Series(seriesAno1)
seriesAno2 = pd.Series(seriesAno2)

print("\nPorcentagem total das linguagens no ano 1:",seriesAno1.sum())
print("Porcentagem total das linguagens no ano 2:",seriesAno2.sum())

seriessub = seriesAno2.sub(seriesAno1, fill_value=0)
print("\nCrescimento / declínio de cada linguagen:")
print(seriessub)

print("\nApenas linguagens que tiveram crescimento:")
print(seriessub[seriessub > 0])

projecao2anos = seriesAno2 + 2*seriessub

print("\nLinguagem mais popular em 2 anos mantendo o crescimento:",projecao2anos.nlargest(1))
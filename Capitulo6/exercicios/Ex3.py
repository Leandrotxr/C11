import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/space.csv', delimiter=';')
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

dfRoscosmos = df[df["Company Name"] == "Roscosmos"]
print(dfRoscosmos)

success = len(dfRoscosmos[dfRoscosmos["Status Mission"] == "Success"])
failure = len(dfRoscosmos) - success

plt.pie(x=[success, failure], labels=['Success', 'Failure'], autopct = '%1.1f%%')
plt.show()
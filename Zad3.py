import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

grouped3 = df.groupby(['Plec'])
g = grouped3.count()
print(g)

wykres = g.plot.pie(subplots=True, autopct='%.2f %%', fontsize=5, figsize=(6,6), legend=(0, 0))
plt.legend(loc="lower right")
plt.show()
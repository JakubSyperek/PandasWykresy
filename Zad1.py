import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

grouped3 = df.groupby(['Rok'])
g = grouped3.count()
print(g)

wykres = g.plot.bar()
plt.show()
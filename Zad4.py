import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')
print(df)

grouped3 = df.groupby(['Sprzedawca'])
g = grouped3.count()
print(g)

wykres = g.plot.bar()
plt.show()
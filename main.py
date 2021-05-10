import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))

#s = s.cumsum()
#print(s)
#s.plot()
#plt.show()

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171045, 207847528, 38675467]}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
wykres = grupa.plot.bar()

wykres = grupa.plot
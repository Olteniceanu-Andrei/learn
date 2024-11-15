from cProfile import label

import matplotlib.pyplot as plot
import pandas as pd

data = {
    "An": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    "Incasari": [200, 400, 350, 560, 970, 600, 300, 1000]
}

df = pd.DataFrame(data)
print(df)

df.plot(x="An", y="Incasari", marker=('o'), linestyle=(":"), label=('Vanzari'))

plot.xlabel('An')
plot.ylabel('Suma Incasata')
plot.title("Acesta este titlul la grafic")
plot.grid()
plot.show()
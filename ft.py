import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ti=pd.read_csv('train.csv')
ti.plot(y='Survived', x='Sex')
plt.show()


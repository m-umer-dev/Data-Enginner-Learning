import pandas as pd
import numpy as np

df = pd.read_csv('Superstore.csv', parse_dates=['Ship Date', 'Order Date'])

df.head()
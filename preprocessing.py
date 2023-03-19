# Nama : Adam Ghosam
# Nim : A11.2019.12040
# Title : Data Mining Covid 19 di indonesia

# import library untuk Proses data Sient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime


# memanggil dataset
dataset = pd.read_csv('Data.csv')
# dataset['Month'] = dataset['Date'].apply(lambda x:datetime.datetime.strptime(x, '%m/%d/%Y').strftime('%Y-%m'))

# cov = dataset[dataset['Location'] != 'Indonesia']

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)



# Nama : Adam Ghosam
# Nim : A11.2019.12040
# Title : Data Mining Covid 19 di indonesia

# import library untuk Proses data Sient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd





# memanggil dataset
dataset = pd.read_csv('Data.csv')

# print(dataset)

x = dataset.iloc[:, :-2].values
y = dataset.iloc[:, 2].values

print (y)



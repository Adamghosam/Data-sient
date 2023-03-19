# Nama : Adam Ghosam
# Nim : A11.2019.12040
# Title : Data Mining Covid 19 di indonesia

# import library untuk Proses data Sient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# memanggil dataset
dataset = pd.read_csv('Data.csv')



x = dataset.iloc[:, :28].values
y = dataset.iloc[:, 28].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(x[:, 1:28])
x[:, 1:28] = imputer.transform(x[:, 1:28])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct =ColumnTransformer(transformer=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))


from sklearn.preprocessing import LabelEncoder
le =LabelEncoder()
y = le.fit_transform(y)

print(x)
print(y)
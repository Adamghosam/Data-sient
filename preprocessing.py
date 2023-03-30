# Nama : Adam Ghosam
# Nim : A11.2019.12040
# Title : Data Mining Covid 19 di indonesia

# import library untuk Proses data Sient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# memanggil dataset
dataset = pd.read_csv('Data.csv')

# print(dataset)

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values



# sklearn.impute.SimpleImputer adalah untuk mengubah data yang hilang dengan mengunakan cara mengambil nilai rata rata

def mean_data(x):
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(x[:, 1:3])
    x[:, 1:3] = imputer.transform(x[:, 1:3])
    return x

hasil = mean_data(x)
# print (hasil)

def pastg(x):
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
    x = np.array(ct.fit_transform(x))
    return x

hasil_pastg =pastg(hasil)
# print (hasil_pastg)




def rubah(y):

    le = LabelEncoder()
    y = le.fit_transform(y)
    return y

hasil_y =rubah(y)
# print (hasil_y)

def xtrain(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=1)
    # Data = "Data Extrain :\n{}\n Data Extest:\n {} \n Data Yetrain:\n{} \n Data Yetest:\n{}".format(x_train,x_test, y_train, y_test)
    # return Data

    return x_train,x_test

hasil_x =xtrain(hasil_pastg,hasil_y)
data1= (hasil_x[0]) 
data2= (hasil_x[1]) 





def finisedd (x_train,x_test):
    sc = StandardScaler()
    x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
    x_test[:, 3:] = sc.transform(x_test[:, 3:])

    return x_train,x_test


datanya = finisedd(data1,data2)

print (datanya[0])
print (datanya[1])

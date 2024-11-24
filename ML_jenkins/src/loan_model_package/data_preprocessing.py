import numpy as np
import pandas as pd
#import data_loader
from . import data_loader
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def data_split(dataset, target, size=0.2, stratify=None):
    Xtrain, Xtest, Ytrain, Ytest= train_test_split(dataset,target, test_size=0.2)
    return Xtrain, Xtest, Ytrain, Ytest

def capping(dataset,col):
    dataset.loc[dataset[col]> np.quantile(dataset[col], 0.99), col]=np.quantile(dataset[col], 0.99)
    return dataset

def scaling(Xtrain, Xtest, col_list):
    scaler=StandardScaler()
    for col in col_list:
        Xtrain[col]=scaler.fit_transform(Xtrain[[col]])
        Xtest[col]=scaler.transform(Xtest[[col]])

    return Xtrain, Xtest 

def encoder(Xtrain, Xtest, col_list):
    for col in col_list:
        le=LabelEncoder()
        Xtrain[col]=le.fit_transform(Xtrain[col])
        Xtest[col]=le.transform(X_test[col])

    return Xtrain, Xtest
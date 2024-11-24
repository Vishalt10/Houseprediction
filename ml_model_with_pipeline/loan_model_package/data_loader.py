import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def data_loader():
    df=pd.read_csv(r"E:\End to End ML projects\1st ML project\experiment\loan_data.csv")
    X=df.drop(columns=['Loan_Status'])
    Y=df['Loan_Status']
    xtrain, xtest, ytrain, ytest=train_test_split(X,Y, test_size=0.2)
    return xtrain, xtest, ytrain, ytest


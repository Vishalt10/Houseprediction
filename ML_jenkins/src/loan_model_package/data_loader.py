import pandas as pd
import numpy as np


def data_loader():
    df=pd.read_csv(r"E:\End to End ML projects\1st ML project\experiment\loan_data.csv")
    return df


def data_imputation(dataset):
    ## check if there are missing values in any col and which category does it belong to
    temp=dataset.isnull().sum()

    temp[temp>0]

    null_cols=temp[temp>0].index

    categorical_cols=list(dataset.select_dtypes(exclude=np.number))

    numerical_cols=list(dataset.select_dtypes(include=np.number))

    for name in null_cols:
        if name in categorical_cols:
            print(f"the col {name} requires mode impuation")
            dataset[name].fillna(dataset[name].mode()[0], inplace=True)
        else:
            print(f"the col {name} requires mean impuation")
            dataset[name].fillna(dataset[name].mean(), inplace=True)

    temp=dataset.isnull().sum()

    if temp.sum()==0:
        print("All missing values handled")
    
    return dataset
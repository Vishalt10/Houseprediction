import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

class mean_imputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables=variables
        ## a list of numerical variables would be passed and their means
        ## would be calculated to impute missing values

    def fit(self, x, y=None):
        self.mean_dict={}
        for col in self.variables:
            self.mean_dict[col]=x[col].mean()
        return self
    
    def transform(self, x):
        x=x.copy()
        for col in self.variables:
            x[col].fillna(self.mean_dict[col], inplace=True)
        return x
    

class mode_imputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables=variables

    def fit(self,x, y=None):
        self.mode_dict={}
        for col in self.variables:
            self.mode_dict[col]=x[col].mode()
        return self
    
    def transform (self, x):
        x=x.copy()
        for col in self.variables:
            x[col]=x[col].fillna(self.mode_dict[col], inplace=True)
        return x
    

class capper(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables=variables

    def fit(self, x, y=None):
        self.cap_values={}
        for col in self.variables:
            self.cap_values[col]=np.quantile(x[col], 0.99)
        return self
    
    def transform(self, x):
        x=x.copy()
        for col in self.variables:
            x.loc[x[col]>self.cap_values[col], col]=self.cap_values[col]
        return x
    
class drop_cols(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables=variables

    def fit(self, x,y=None):
        return self
    
    def transform(self, x):
        x=x.copy()
        x.drop(columns=self.variables, inplace=True)
        return x
    
class custom_encoder(BaseEstimator, TransformerMixin):
    def __init__(self, variables):
        self.variables=variables

    def fit(self, x, y=None):
        self.encoder_dict={}
        for col in self.variables:
            col_values=x[col].value_counts(sort=True).index
            self.encoder_dict[col]={k:i for i,k in enumerate(col_values)}
        return self
    
    def transform(self, x):
        x=x.copy()
        for col in self.variables:
            x[col]=x[col].map(self.encoder_dict[col])
        return x
    
    


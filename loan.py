import numpy as np
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
#from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
import warnings

warnings.filterwarnings("ignore")


def load_df():
    df=pd.read_csv(r'E:\End to End ML projects\1st ML project\experiment\loan_data.csv')

    return df

def metrics (actual, pred):

    acc=accuracy_score(actual, pred)
    f1=f1_score(actual, pred)
    cm=confusion_matrix(actual, pred)

    return acc, f1, cm

## load the dataset and split
df = load_df()
Y=df['Loan_Status']
X=df.drop(columns=['Loan_Status'])
X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.1)

## for categorical column imputation
for col in X_train.select_dtypes(exclude=np.number).columns:
    X_train[col].fillna(X_train[col].mode()[0], inplace=True)
    X_test[col].fillna(X_test[col].mode()[0], inplace=True)

### for numerical col imputation

for col in X_train.select_dtypes(include=np.number).columns:
    X_train[col].fillna(X_train[col].mean(), inplace=True)
    X_test[col].fillna(X_test[col].mean(), inplace=True)

## drop unwanted col
    
X_train.drop(columns=['Loan_ID'], inplace=True)
X_test.drop(columns=['Loan_ID'], inplace=True)

### label encoding of categorical columns

def encoder(columns):
    le=LabelEncoder()
    for col in columns:
        X_train.loc[:, col]=le.fit_transform(X_train.loc[:, col])
        X_test.loc[:, col]=le.transform(X_test.loc[:, col])


encoder(list(X_train.select_dtypes(exclude=np.number).columns))


### normalization of numerical cols

for col in X_train.select_dtypes(include=np.number).columns:
    scaler=StandardScaler()
    X_train[col]=scaler.fit_transform(X_train[[col]])
    X_test[col]=scaler.transform(X_test[[col]])

## label encoding 
    
le=LabelEncoder()
Y_train=le.fit_transform(Y_train)
Y_test=le.transform(Y_test)


## Logistic Regression

param_grid={'penalty':['l1', 'l2'], 'solver': ['lbfgs', 'liblinear', 'sag'], 'max_iter':[100, 200, 300]}

regressor_grid=GridSearchCV(param_grid=param_grid, estimator=LogisticRegression(), cv=5, return_train_score=True)
regressor_model=regressor_grid.fit(X_train, Y_train)


#id=mlflow.create_experiment("first_prediction")

def mlflow_logger(model, x, y, name):
    mlflow.set_experiment("first_prediction")
    with mlflow.start_run():
        y_pred=model.predict(x)
        acc, f1, cm= metrics(y, y_pred)
        mlflow.log_param("penalty", model.best_params_['penalty'])
        mlflow.log_param("solver", model.best_params_['solver'])
        mlflow.log_param("max_iter", model.best_params_['max_iter'])
        mlflow.log_metric("f1", f1)
        mlflow.log_metric("acc",acc)
        #mlflow.log_metric("confusion_matrix", cm)

    mlflow.end_run()

mlflow_logger(regressor_model, X_test, Y_test, 'regressor')

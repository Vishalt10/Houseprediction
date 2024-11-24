#import data_loader
from . import data_loader
from . import data_preprocessing
#import data_preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import RandomOverSampler, SMOTE

def model_training():
    dataset=data_loader.data_loader()
    dataset=data_loader.data_imputation(dataset=dataset)
    dataset.drop(columns=['Loan_ID'], inplace=True)
    numerical_cols=['ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History']

    categorical_cols=['Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area']
    dataset=data_preprocessing.capping(dataset, 'CoapplicantIncome')

    X=dataset.iloc[:,:-1]
    Y=dataset.iloc[:,-1]
    ## Splitting dataset
    Xtrain, Xtest, Ytrain, Ytest=data_preprocessing.data_split(X, Y)

    print("Splitting finished")

    
    Xtrain, Xtest=data_preprocessing.scaling(Xtrain=Xtrain, Xtest=Xtest, col_list=numerical_cols)
    print("Scaling for the dataset has been done")
    # Xtrain, Xtest=encoder(Xtrain=Xtrain, Xtest=Xtest, col_list=categorical_cols)
    for col in categorical_cols:
        le=LabelEncoder()
        Xtrain[col]=le.fit_transform(Xtrain[col])
        Xtest[col]=le.transform(Xtest[col])
    print("Encoding has been concluded")

    ## resampling

    ros=RandomOverSampler()
    x,y=ros.fit_resample(Xtrain, Ytrain)

    le2=LabelEncoder()
    y=le2.fit_transform(y)

    Ytest=le2.transform(Ytest)

    ### grid search cv on logistic regression

    #param_grid={'penalty':['l1', 'l2'], 'solver': ['liblinear', 'sag'], 'max_iter':[100, 200, 300]}

    #param_grid2={'n_estimators':[200, 150, 225], 'criterion':['gini'], 'max_depth':[7,6,5]}

    #regressor_grid=GridSearchCV(param_grid=param_grid2, estimator=RandomForestClassifier(), cv=5, return_train_score=True)
    #regressor_model=regressor_grid.fit(x, y)


    clf_xgb=XGBClassifier()

    clf_xgb.fit(x,y)

    with open("model_test_xgb.pkl", 'wb') as f:
        pickle.dump(clf_xgb,f)

    print("The model has been successfully trained and saved")

    ## model accuracy

    # ypred=clf_xgb.predict(Xtest)
    # print(confusion_matrix(Ytest, ypred))


if __name__=='__main__':
    model_training()
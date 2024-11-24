#import data_loader
# from . import data_loader
import loan_model_package.data_loader as data_loader
import loan_model_package.data_preprocessing as data_preprocessing
#import data_preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import RandomOverSampler, SMOTE
# from . import data_loader
#import loan_model_package.data_handler as data_handler


def model_training():
    xtrain, xtest, ytrain, ytest=data_loader.data_loader()
    ytrain=ytrain.map({'N':0, 'Y':1})
    pp.pipe.fit(xtrain, ytrain)
    ypred=pp.pipe.predict(xtest)
    print(confusion_matrix(ytest, ypred))



if __name__=='__main__':
    model_training()
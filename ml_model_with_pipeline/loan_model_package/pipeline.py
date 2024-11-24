from sklearn.pipeline import Pipeline
import os
from . import config
from . import data_handler
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBClassifier

cwd=os.path.abspath(__file__)

PACKAGE_ROOT= os.path.dirname(cwd)

pipe=Pipeline([('column_drop', data_handler.drop_cols(config.DROP_COLS)),
               ('mean_imputation', data_handler.mean_imputer(config.NUM_FEATURES)),
               ('mode_imputation', data_handler.mode_imputer(config.CAT_FEATURES)),
               ('capping_of_coapplicantincome', data_handler.capper(['CoapplicantIncome'])),
               ('custom_encoding', data_handler.custom_encoder(config.CAT_FEATURES)),
               ('standard_scaling', StandardScaler()),
               ('XGBoostClassifer', XGBClassifier())])
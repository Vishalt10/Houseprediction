import os
import pathlib


FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']



NUM_FEATURES = ['ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History']

CAT_FEATURES=['Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area']

DROP_COLS=['Loan_ID']

cwd=os.path.abspath(__file__)
PACKAGE_ROOT=os.path.dirname(cwd)

# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
#print(pathlib.Path(loan_model_package.__file__).resolve().parent)